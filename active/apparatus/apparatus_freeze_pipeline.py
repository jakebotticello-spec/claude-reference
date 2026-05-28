# apparatus_freeze_pipeline.py · v1.2 · apparatus S13 · 2026-05-27 · initial implementation of Stages 1–4 per Freeze_Pipeline_Spec_v2.md
# v1.1: extracted _parse_and_inspect + _file_sha256; dry-run now exercises drift detection;
#        stage1_freeze uses shutil.copyfile (no raw bytes held alongside parsed dict)
# v1.2: moved to active/apparatus/ (canon, not scratch); idempotency check moved after
#        dry-run early-return so dry-run works correctly when snapshot already exists

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRUB_VERSION = 1
ROOT_SENTINEL = '00000000-0000-4000-8000-000000000000'

# Regex set v1 — locked at S12. Anthropic pattern listed before OpenAI; OpenAI uses
# negative lookahead (?!ant-) so sk-ant-... never matches the OpenAI class.
PATTERNS = [
    ('RTSP',      r'rtsp://[^/\s:]+:[^/\s@]+@',            '<RTSP_CRED_REDACTED>'),
    ('postgres',  r'postgres(?:ql)?://[^/\s:]+:[^/\s@]+@',  '<POSTGRES_CRED_REDACTED>'),
    ('anthropic', r'sk-ant-[A-Za-z0-9_-]{20,}',             '<ANTHROPIC_KEY_REDACTED>'),
    ('openai',    r'sk-(?!ant-)[A-Za-z0-9_-]{20,}',          '<OPENAI_KEY_REDACTED>'),
    ('stripe',    r'(?:sk|rk)_live_[A-Za-z0-9]{20,}',        '<STRIPE_KEY_REDACTED>'),
]

# Population-confirmed at S12 (5 block types, 67,275 blocks; 5 content-item types)
KNOWN_BLOCK_TYPES = {'text', 'thinking', 'tool_use', 'tool_result', 'token_budget'}
KNOWN_CONTENT_ITEM_TYPES = {'text', 'knowledge', 'local_resource', 'image', 'image_gallery'}
# v1.0 detects type-level drift only (block types + tool_result.content[] item types);
# field-level drift on existing objects is a v1.1 expansion if a drift event surfaces.


# ---------------------------------------------------------------------------
# Core recursive helpers
# ---------------------------------------------------------------------------

def _file_sha256(path):
    """Streaming sha256 — never holds the full file in memory."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def _parse_and_inspect(src_path):
    """Parse source JSON, count records, detect schema drift.
    Returns (raw_data, counts, drift_events). Does not hold raw bytes.
    Drift warnings surface to stderr here so both dry-run and real-run paths see them.
    schema-drift.jsonl is written only by stage1_freeze (needs snapshot dir)."""
    with open(src_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    conv_count = len(data)
    message_count = sum(len(conv.get('chat_messages', [])) for conv in data)
    content_block_count = sum(
        len(msg.get('content', []))
        for conv in data
        for msg in conv.get('chat_messages', [])
    )

    # Schema-drift detection — type-level only in v1.0 (see constants comment above)
    drift_events = []
    for conv in data:
        for msg in conv.get('chat_messages', []):
            for block in msg.get('content', []):
                btype = block.get('type')
                if btype not in KNOWN_BLOCK_TYPES:
                    drift_events.append({
                        'drift_type': 'unknown_block_type',
                        'observed_type': btype,
                        'conv_uuid': conv['uuid'],
                        'msg_uuid': msg['uuid'],
                    })
                    sys.stderr.write(
                        f"WARNING schema-drift: unknown block type '{btype}' "
                        f"conv={conv['uuid'][:8]} msg={msg['uuid'][:8]}\n"
                    )
                if btype == 'tool_result':
                    for item in block.get('content', []):
                        itype = item.get('type')
                        if itype not in KNOWN_CONTENT_ITEM_TYPES:
                            drift_events.append({
                                'drift_type': 'unknown_tool_result_content_item_type',
                                'observed_type': itype,
                                'conv_uuid': conv['uuid'],
                                'msg_uuid': msg['uuid'],
                            })
                            sys.stderr.write(
                                f"WARNING schema-drift: unknown tool_result.content[] "
                                f"type '{itype}' conv={conv['uuid'][:8]} msg={msg['uuid'][:8]}\n"
                            )

    return data, (conv_count, message_count, content_block_count), drift_events


def _scrub_walk(obj, path, audit_fn):
    """Type-agnostic recursive descent — walks every string at every depth.
    Returns rebuilt structure; cred substrings replaced by class tokens."""
    if isinstance(obj, str):
        return audit_fn(obj, path)
    elif isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            child_path = f"{path}.{k}" if path else k
            result[k] = _scrub_walk(v, child_path, audit_fn)
        return result
    elif isinstance(obj, list):
        return [_scrub_walk(item, f"{path}[{i}]", audit_fn) for i, item in enumerate(obj)]
    else:
        return obj


def _make_audit_fn(conv_uuid, msg_uuid, snapshot_id, audit_list):
    """Returns a string-replacement function that appends an audit entry per match.
    Captured value never enters the audit record — original_length only."""
    def audit_fn(s, path):
        result = s
        for pname, pattern, token in PATTERNS:
            def replacer(m, pn=pname, tk=token):
                audit_list.append({
                    'snapshot_id': snapshot_id,
                    'scrub_version': SCRUB_VERSION,
                    'conv_uuid': conv_uuid,
                    'msg_uuid': msg_uuid,
                    'json_path': path,
                    'pattern_class': pn,
                    'redaction_token': tk,
                    'original_length': len(m.group(0)),
                })
                return tk
            result = re.sub(pattern, replacer, result)
        return result
    return audit_fn


def _verify_walk(obj, hits, counters):
    """Count regex hits across all strings — no replacement, no audit entries."""
    if isinstance(obj, str):
        counters['strings'] += 1
        counters['bytes'] += len(obj.encode('utf-8'))
        for pname, pattern, _ in PATTERNS:
            hits[pname] += len(re.findall(pattern, obj))
    elif isinstance(obj, dict):
        for v in obj.values():
            _verify_walk(v, hits, counters)
    elif isinstance(obj, list):
        for item in obj:
            _verify_walk(item, hits, counters)


# ---------------------------------------------------------------------------
# Stage functions
# ---------------------------------------------------------------------------

def stage1_freeze(source_path, source_sha256, snapshot_id, snapshot_dir,
                  conv_count, message_count, content_block_count,
                  snapshots_base, drift_events):
    """Freeze: create snapshot dir, write sealed raw.json, manifest.json, append ledger.
    Uses shutil.copyfile for byte-verbatim source→raw.json (no re-serialization)."""
    print(f"[Stage 1] Creating snapshot: {snapshot_id}")
    snapshot_dir.mkdir(parents=True, exist_ok=False)

    raw_path = snapshot_dir / 'raw.json'
    shutil.copyfile(source_path, raw_path)  # byte-verbatim; re-reads source from disk
    os.chmod(raw_path, 0o444)               # sealed read-only — invariant 5.1
    print(f"[Stage 1] raw.json written ({raw_path.stat().st_size:,} bytes) — sealed read-only")

    # Write schema-drift.jsonl only when drift was detected (snapshot dir now exists)
    if drift_events:
        entries = [dict(snapshot_id=snapshot_id, **e) for e in drift_events]
        with open(snapshot_dir / 'schema-drift.jsonl', 'w', encoding='utf-8') as f:
            for entry in entries:
                f.write(json.dumps(entry) + '\n')
        print(f"[Stage 1] schema-drift.jsonl: {len(entries)} entries (warn-not-stop)")

    source_mtime = os.path.getmtime(source_path)
    manifest = {
        'snapshot_id': snapshot_id,
        'type': 'baseline',
        'source_export_path': str(source_path.resolve()),
        'source_export_mtime': datetime.fromtimestamp(source_mtime, tz=timezone.utc).isoformat(),
        'source_export_sha256_full': source_sha256,
        'raw_sha256_full': source_sha256,  # baseline: verbatim copy, same hash
        'raw_byte_size': raw_path.stat().st_size,
        'conv_count': conv_count,
        'message_count': message_count,
        'content_block_count': content_block_count,
        'prior_snapshot_id': None,
        'frozen_at': datetime.now(tz=timezone.utc).isoformat(),
    }
    (snapshot_dir / 'manifest.json').write_text(
        json.dumps(manifest, indent=2), encoding='utf-8'
    )
    print(f"[Stage 1] manifest.json: {conv_count} convs / {message_count} msgs / "
          f"{content_block_count} blocks")

    with open(snapshots_base / 'ledger.jsonl', 'a', encoding='utf-8') as f:
        f.write(json.dumps(manifest) + '\n')
    print(f"[Stage 1] ledger.jsonl appended")


def stage2_scrub(snapshot_dir, data, snapshot_id):
    """Scrub: type-agnostic recursive descent over every string. Returns scrubbed data."""
    print(f"[Stage 2] Scrubbing (scrub-v{SCRUB_VERSION} regex set)...")
    scrub_dir = snapshot_dir / f'scrub-v{SCRUB_VERSION}'
    scrub_dir.mkdir(exist_ok=False)

    audit_list = []
    scrubbed_convs = []

    for conv in data:
        conv_uuid = conv['uuid']

        # Conv-level fields (all keys except chat_messages) walked with msg_uuid=''.
        # name and summary: walked as strings per invariant 5.5 (no skip list); preserved
        # in scrubbed JSON in original shape; Stage 4 drops them — neither field carried
        # to headers or message records.
        conv_fn = _make_audit_fn(conv_uuid, '', snapshot_id, audit_list)
        sc = {}
        for key, val in conv.items():
            if key != 'chat_messages':
                sc[key] = _scrub_walk(val, key, conv_fn)

        # Each message scrubbed with its own uuid for audit traceability
        scrubbed_msgs = []
        for msg in conv.get('chat_messages', []):
            msg_fn = _make_audit_fn(conv_uuid, msg['uuid'], snapshot_id, audit_list)
            scrubbed_msgs.append(_scrub_walk(msg, '', msg_fn))
        sc['chat_messages'] = scrubbed_msgs
        scrubbed_convs.append(sc)

    (scrub_dir / 'conversations.scrubbed.json').write_text(
        json.dumps(scrubbed_convs, ensure_ascii=False), encoding='utf-8'
    )

    with open(scrub_dir / 'scrub-audit.jsonl', 'w', encoding='utf-8') as f:
        for entry in audit_list:
            f.write(json.dumps(entry) + '\n')

    counts = {}
    for e in audit_list:
        counts[e['pattern_class']] = counts.get(e['pattern_class'], 0) + 1
    print(f"[Stage 2] scrub-audit.jsonl: {len(audit_list)} entries — {counts}")
    return scrubbed_convs


def stage3_verify(snapshot_dir, scrubbed_data, snapshot_id):
    """Verify-clean hard gate. Returns True on pass; quarantines + returns False on fail.
    Stage 4 must not run if this returns False — caller enforces."""
    print(f"[Stage 3] Verify-clean scan...")
    scrub_dir = snapshot_dir / f'scrub-v{SCRUB_VERSION}'

    hits = {pname: 0 for pname, _, _ in PATTERNS}
    counters = {'strings': 0, 'bytes': 0}
    _verify_walk(scrubbed_data, hits, counters)
    total_hits = sum(hits.values())
    passed = total_hits == 0

    verify_log = {
        'passed': passed,
        'scrub_version': SCRUB_VERSION,
        'scanned_bytes': counters['bytes'],
        'scanned_strings': counters['strings'],
        'regex_hits_per_class': {
            'RTSP':      hits['RTSP'],
            'postgres':  hits['postgres'],
            'openai':    hits['openai'],
            'anthropic': hits['anthropic'],
            'stripe':    hits['stripe'],
        },
    }
    (scrub_dir / 'verify.log').write_text(
        json.dumps(verify_log, indent=2), encoding='utf-8'
    )

    if passed:
        print(f"[Stage 3] PASSED — 0 hits across {counters['strings']:,} strings / "
              f"{counters['bytes']:,} bytes")
        return True

    sys.stderr.write(f"[Stage 3] FAILED — {total_hits} hits: {hits}\n")
    quarantine = (snapshot_dir.parent / 'quarantine' / snapshot_id /
                  f'scrub-v{SCRUB_VERSION}')
    quarantine.mkdir(parents=True, exist_ok=True)
    shutil.move(
        str(scrub_dir / 'conversations.scrubbed.json'),
        str(quarantine / 'conversations.scrubbed.json'),
    )
    sys.stderr.write(f"[Stage 3] Scrubbed file quarantined to: {quarantine}\n")
    return False


def stage4_ingest(snapshot_dir, scrubbed_data, snapshot_id):
    """Ingest: write records.ndjson (conv headers + message records). Seal scrub-vN/."""
    print(f"[Stage 4] Ingesting {len(scrubbed_data)} conversations...")
    scrub_dir = snapshot_dir / f'scrub-v{SCRUB_VERSION}'

    sorted_convs = sorted(scrubbed_data, key=lambda c: c['created_at'])
    header_count = 0
    msg_count = 0

    with open(scrub_dir / 'records.ndjson', 'w', encoding='utf-8') as f:
        for conv in sorted_convs:
            msgs = conv.get('chat_messages', [])

            root_count = sum(1 for m in msgs if m['parent_message_uuid'] == ROOT_SENTINEL)
            multi_root = root_count > 1

            parent_child_counts: dict = {}
            for m in msgs:
                p = m['parent_message_uuid']
                if p != ROOT_SENTINEL:
                    parent_child_counts[p] = parent_child_counts.get(p, 0) + 1
            has_branches = any(c >= 2 for c in parent_child_counts.values())

            # Conversation header — name and summary intentionally excluded (invariant 5.4 / D5)
            header = {
                'record_type':   'conversation_header',
                'snapshot_id':   snapshot_id,
                'scrub_version': SCRUB_VERSION,
                'conv_uuid':     conv['uuid'],
                'created_at':    conv['created_at'],
                'updated_at':    conv['updated_at'],
                'account_uuid':  conv['account']['uuid'],
                'message_count': len(msgs),
                'has_branches':  has_branches,
                'multi_root':    multi_root,
            }
            f.write(json.dumps(header, ensure_ascii=False) + '\n')
            header_count += 1

            for msg in sorted(msgs, key=lambda m: m['created_at']):
                # conv_name and conv_summary intentionally absent — invariant 5.4 / D5
                record = {
                    'snapshot_id':         snapshot_id,
                    'scrub_version':       SCRUB_VERSION,
                    'conv_uuid':           conv['uuid'],
                    'msg_uuid':            msg['uuid'],
                    'parent_message_uuid': msg['parent_message_uuid'],
                    'sender':              msg['sender'],
                    'created_at':          msg['created_at'],
                    'updated_at':          msg['updated_at'],
                    'text':                msg['text'],
                    'content_blocks':      msg['content'],
                    'attachments':         msg['attachments'],
                    'files':               msg['files'],
                    'is_root':             msg['parent_message_uuid'] == ROOT_SENTINEL,
                }
                f.write(json.dumps(record, ensure_ascii=False) + '\n')
                msg_count += 1

    print(f"[Stage 4] records.ndjson: {header_count} headers + {msg_count} messages = "
          f"{header_count + msg_count} lines")

    for fpath in scrub_dir.iterdir():
        if fpath.is_file():
            os.chmod(fpath, 0o444)
    print(f"[Stage 4] scrub-v{SCRUB_VERSION}/ sealed read-only")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description='apparatus freeze pipeline — Stages 1–4')
    p.add_argument(
        '--source',
        default='apparatus-archive/conversations.json',
        help='Path to conversations.json export (default: apparatus-archive/conversations.json)',
    )
    p.add_argument(
        '--dry-run', action='store_true',
        help='Parse + inspect for drift + report counts; write nothing',
    )
    args = p.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        sys.exit(f"ERROR: source not found: {source_path}")

    snapshots_base = source_path.parent / 'snapshots'

    # Streaming sha256 — no raw bytes held in memory alongside parsed dict
    print(f"Hashing {source_path} ({source_path.stat().st_size / 1024 / 1024:.1f} MB)...")
    source_sha256 = _file_sha256(source_path)
    source_mtime = os.path.getmtime(source_path)
    # UTC for mtime date — deterministic across timezone changes
    mtime_date = datetime.fromtimestamp(source_mtime, tz=timezone.utc).strftime('%Y-%m-%d')
    snapshot_id = f"baseline-{mtime_date}-{source_sha256[:8]}"
    snapshot_dir = snapshots_base / snapshot_id

    # Parse, count, detect drift — drift warnings surface to stderr here
    print(f"Parsing JSON...")
    data, (conv_count, message_count, content_block_count), drift_events = \
        _parse_and_inspect(source_path)

    print(f"Snapshot ID  : {snapshot_id}")
    print(f"Counts       : {conv_count} convs / {message_count} msgs / "
          f"{content_block_count} content blocks")
    print(f"Schema drift : {len(drift_events)} events"
          + (" (see stderr warnings above)" if drift_events else ""))

    if args.dry_run:
        if snapshot_dir.exists():
            print(f"NOTE: snapshot already exists — real run would refuse (invariant 5.2)")
        print(f"\n[DRY-RUN] Snapshot dir would be: {snapshot_dir}")
        print("[DRY-RUN] No files written.")
        return

    # Idempotency check — invariant 5.2: sealed snapshots never overwritten
    # (after dry-run exit: dry-run writes nothing so no overwrite risk)
    if snapshot_dir.exists():
        sys.exit(
            f"ERROR: snapshot {snapshot_id} already exists at {snapshot_dir} — "
            f"refusing overwrite (invariant 5.2)"
        )
    if (snapshots_base / 'ledger.jsonl').exists():
        with open(snapshots_base / 'ledger.jsonl', encoding='utf-8') as lf:
            for line in lf:
                if line.strip() and json.loads(line).get('snapshot_id') == snapshot_id:
                    sys.exit(
                        f"ERROR: snapshot {snapshot_id} already in ledger — "
                        f"refusing re-run (invariant 5.2)"
                    )

    stage1_freeze(
        source_path, source_sha256, snapshot_id, snapshot_dir,
        conv_count, message_count, content_block_count,
        snapshots_base, drift_events,
    )

    scrubbed_data = stage2_scrub(snapshot_dir, data, snapshot_id)

    if not stage3_verify(snapshot_dir, scrubbed_data, snapshot_id):
        sys.exit(
            f"ERROR: Stage 3 verify-clean FAILED — Stage 4 halted. "
            f"See {snapshot_dir / f'scrub-v{SCRUB_VERSION}' / 'verify.log'}"
        )

    stage4_ingest(snapshot_dir, scrubbed_data, snapshot_id)

    print(f"\nDone. Snapshot : {snapshot_id}")
    print(f"Location       : {snapshot_dir}")


if __name__ == '__main__':
    main()
