# apparatus_freeze_pipeline.py · v1.6 · apparatus S20 · 2026-05-31 · overlay capability milestone
# v1.1: extracted _parse_and_inspect + _file_sha256; dry-run now exercises drift detection;
#        stage1_freeze uses shutil.copyfile (baseline) / write_bytes (delta, filtered slice)
# v1.2: moved to active/apparatus/ (canon, not scratch); idempotency check moved after
#        dry-run early-return so dry-run works correctly when snapshot already exists
# v1.3: delta runs (uuid-set-difference, seen-set from prior records.ndjson, no-duplicate-
#        header rule); raw.json wipe after Stage 3 verify-PASS (Path A, canon RESOLVED S15);
#        --export-dir as primary CLI arg (provenance/second-baseline guard); --baseline guard;
#        drift detection separated from ingest counts (full export vs delta slice)
# v1.4: field-level key-presence drift detection (v1.1 detector layer); per-object-type
#        allowlists for conv, message, all 5 block types, all 5 content-item types; optional-
#        key carve-out for text.citations_grouping_mode; warn-not-stop, same drift_events sink
# v1.5: scrub-version seam fix in _build_seen_set — per-snapshot max-N glob replaces
#        hardcoded SCRUB_VERSION; no behavioral change on current floor (scrub-v1 only)
# v1.6: overlay capability proved end-to-end (Rungs 5-6, S20) — scrub-v2/ minted + scaled
#        for baseline; _build_seen_set max-N seam confirmed on real floor; pass-two (b) closed

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
# v1.0: type-level drift (unknown block/item types); v1.1: field-level drift (key-set allowlists)

# Shape-assert allowlist — S14 confirmed: conv 7 keys, 100% key-present
CONV_KEYS_EXPECTED = frozenset({'uuid', 'name', 'summary', 'created_at', 'updated_at',
                                'account', 'chat_messages'})

# ---------------------------------------------------------------------------
# v1.1 field-level allowlists — key names verbatim from S14 s14_presence_rates.md
# Source: population scan over both exports (baseline 22,801 msgs + 5-28 export 24,138 msgs /
# 71,512 blocks); zero raw-vs-raw field drift confirmed by s14_field_drift_raw.py (2026-05-28)
# ---------------------------------------------------------------------------

# 9 keys, all 100% key-present (n=24,138 messages, full 5-28 export)
MESSAGE_KEYS_EXPECTED = frozenset({
    'attachments', 'content', 'created_at', 'files',
    'parent_message_uuid', 'sender', 'text', 'updated_at', 'uuid',
})

# text block — 6 mandatory keys, all 100% key-present (n=30,448 blocks)
TEXT_BLOCK_KEYS = frozenset({
    'citations', 'flags', 'start_timestamp', 'stop_timestamp', 'text', 'type',
})
# citations_grouping_mode: optional (~0.14%, 43/30,448 blocks); absence must NOT trip drift
TEXT_BLOCK_OPTIONAL_KEYS = frozenset({'citations_grouping_mode'})

# 10 keys, all 100% key-present (n=14,271 blocks)
THINKING_BLOCK_KEYS = frozenset({
    'alternative_display_type', 'cut_off', 'flags', 'signature',
    'start_timestamp', 'stop_timestamp', 'summaries', 'thinking', 'truncated', 'type',
})

# 17 keys, all 100% key-present (n=13,451 blocks)
TOOL_USE_BLOCK_KEYS = frozenset({
    'approval_key', 'approval_options', 'context', 'display_content', 'flags',
    'icon_name', 'id', 'input', 'integration_icon_url', 'integration_name',
    'is_mcp_app', 'mcp_server_url', 'message', 'name',
    'start_timestamp', 'stop_timestamp', 'type',
})

# 16 keys, all 100% key-present (n=13,328 blocks)
TOOL_RESULT_BLOCK_KEYS = frozenset({
    'content', 'display_content', 'flags', 'icon_name', 'integration_icon_url',
    'integration_name', 'is_error', 'mcp_server_url', 'message', 'meta', 'name',
    'start_timestamp', 'stop_timestamp', 'structured_content', 'tool_use_id', 'type',
})

# 5 keys, all 100% key-present (n=14 across BOTH full exports — LOW-CONFIDENCE population;
# a drift warning here is probably rare-type variance, verify manually before treating as
# a real format break)
TOKEN_BUDGET_BLOCK_KEYS = frozenset({
    'flags', 'remaining', 'start_timestamp', 'stop_timestamp', 'type',
})

# tool_result.content[] item-type keys — distinct names avoid text-block/text-item collision
# 3 keys, all 100% key-present (n=12,954 items)
CONTENT_ITEM_TEXT_KEYS = frozenset({'text', 'type', 'uuid'})
# 9 keys, all 100% key-present (n=4,210 items)
CONTENT_ITEM_KNOWLEDGE_KEYS = frozenset({
    'is_citable', 'is_missing', 'links', 'metadata', 'prompt_context_metadata',
    'text', 'title', 'type', 'url',
})
# 5 keys, all 100% key-present (n=1,929 items)
CONTENT_ITEM_LOCAL_RESOURCE_KEYS = frozenset({'file_path', 'mime_type', 'name', 'type', 'uuid'})
# 2 keys, all 100% key-present (n=664 items)
CONTENT_ITEM_IMAGE_KEYS = frozenset({'file_uuid', 'type'})
# 4 keys, all 100% key-present (n=9 items — low-n, same manual-verify caveat as token_budget)
CONTENT_ITEM_IMAGE_GALLERY_KEYS = frozenset({'images', 'is_expired', 'type', 'uuid'})

# Dispatch: block-type → (mandatory_keys, optional_keys)
_BLOCK_FIELD_ALLOWLISTS = {
    'text':         (TEXT_BLOCK_KEYS,         TEXT_BLOCK_OPTIONAL_KEYS),
    'thinking':     (THINKING_BLOCK_KEYS,     frozenset()),
    'tool_use':     (TOOL_USE_BLOCK_KEYS,     frozenset()),
    'tool_result':  (TOOL_RESULT_BLOCK_KEYS,  frozenset()),
    'token_budget': (TOKEN_BUDGET_BLOCK_KEYS, frozenset()),
}
# Dispatch: content item-type → mandatory keys (no optional keys on any item type)
_CONTENT_ITEM_FIELD_ALLOWLISTS = {
    'text':           CONTENT_ITEM_TEXT_KEYS,
    'knowledge':      CONTENT_ITEM_KNOWLEDGE_KEYS,
    'local_resource': CONTENT_ITEM_LOCAL_RESOURCE_KEYS,
    'image':          CONTENT_ITEM_IMAGE_KEYS,
    'image_gallery':  CONTENT_ITEM_IMAGE_GALLERY_KEYS,
}

# Fix A: load-time coupling guard — KNOWN_*_TYPES and their field-allowlist dicts must cover
# identical type sets. A mismatch causes a silent KeyError at runtime in _inspect_data's else
# branch; assert fires loudly at import time instead with a clear diagnostic.
assert set(KNOWN_BLOCK_TYPES) == set(_BLOCK_FIELD_ALLOWLISTS), (
    f"KNOWN_BLOCK_TYPES vs _BLOCK_FIELD_ALLOWLISTS mismatch — "
    f"missing from allowlists: {sorted(KNOWN_BLOCK_TYPES - set(_BLOCK_FIELD_ALLOWLISTS))} "
    f"extra in allowlists: {sorted(set(_BLOCK_FIELD_ALLOWLISTS) - KNOWN_BLOCK_TYPES)}"
)
assert set(KNOWN_CONTENT_ITEM_TYPES) == set(_CONTENT_ITEM_FIELD_ALLOWLISTS), (
    f"KNOWN_CONTENT_ITEM_TYPES vs _CONTENT_ITEM_FIELD_ALLOWLISTS mismatch — "
    f"missing from allowlists: {sorted(KNOWN_CONTENT_ITEM_TYPES - set(_CONTENT_ITEM_FIELD_ALLOWLISTS))} "
    f"extra in allowlists: {sorted(set(_CONTENT_ITEM_FIELD_ALLOWLISTS) - KNOWN_CONTENT_ITEM_TYPES)}"
)


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


def _shape_assert(data, source_path):
    """Assert conversations.json is a JSON list with expected conv-level keys.
    A mismatch is a human-review signal — renamed field, added sibling, shape change.
    STOP with a clear error; do NOT auto-handle."""
    if not isinstance(data, list):
        sys.exit(
            f"ERROR: shape-assert FAILED — {source_path} parsed as {type(data).__name__}, "
            f"expected a JSON list. Human review required."
        )
    if data:
        observed = set(data[0].keys())
        missing = CONV_KEYS_EXPECTED - observed
        extra   = observed - CONV_KEYS_EXPECTED
        if missing or extra:
            sys.exit(
                f"ERROR: shape-assert FAILED — conv[0] key mismatch. "
                f"missing={sorted(missing)} extra={sorted(extra)}. Human review required."
            )
    print(f"[Shape] conversations.json: {len(data)} convs, key shape OK")


def _check_field_drift(object_type, mandatory_keys, optional_keys, observed_keys,
                       conv_uuid, msg_uuid, drift_events):
    """v1.1 field-level drift check for one object. Appends to drift_events and writes
    stderr on mismatch. optional_keys may be absent without triggering missing-key drift
    and may be present without triggering extra-key drift."""
    missing = mandatory_keys - observed_keys
    extra   = observed_keys - (mandatory_keys | optional_keys)
    if not missing and not extra:
        return
    drift_events.append({
        'drift_type':   'field_drift',
        'object_type':  object_type,
        'missing_keys': sorted(missing),
        'extra_keys':   sorted(extra),
        'conv_uuid':    conv_uuid,
        'msg_uuid':     msg_uuid,
    })
    sys.stderr.write(
        f"WARNING schema-drift: field_drift on {object_type} "
        f"missing={sorted(missing)} extra={sorted(extra)} "
        f"conv={conv_uuid[:8]} msg={msg_uuid[:8]}\n"
    )


def _inspect_data(data):
    """Count records and detect schema drift on loaded conv data.
    v1.0: type-level drift (unknown block/item types).
    v1.1: field-level drift (per-object-type key-set allowlists, warn-not-stop).
    Drift warnings surface to stderr. Returns (conv_count, message_count,
    content_block_count, drift_events). Does no file I/O."""
    conv_count = len(data)
    message_count = sum(len(conv.get('chat_messages', [])) for conv in data)
    content_block_count = sum(
        len(msg.get('content', []))
        for conv in data
        for msg in conv.get('chat_messages', [])
    )

    drift_events = []
    for conv in data:
        cu = conv.get('uuid', '')  # '' if missing — drift fires below, not KeyError
        # v1.1: conv-level field drift
        _check_field_drift('conversation', CONV_KEYS_EXPECTED, frozenset(),
                           frozenset(conv.keys()), cu, '', drift_events)
        for msg in conv.get('chat_messages', []):
            mu = msg.get('uuid', '')  # '' if missing — drift fires below, not KeyError
            # v1.1: message-level field drift
            _check_field_drift('message', MESSAGE_KEYS_EXPECTED, frozenset(),
                               frozenset(msg.keys()), cu, mu, drift_events)
            for block in msg.get('content', []):
                btype = block.get('type')
                # v1.0: type-level check
                if btype not in KNOWN_BLOCK_TYPES:
                    drift_events.append({
                        'drift_type': 'unknown_block_type',
                        'observed_type': btype,
                        'conv_uuid': cu,
                        'msg_uuid': mu,
                    })
                    sys.stderr.write(
                        f"WARNING schema-drift: unknown block type '{btype}' "
                        f"conv={cu[:8]} msg={mu[:8]}\n"
                    )
                else:
                    # v1.1: block field drift (known types only)
                    mandatory, optional = _BLOCK_FIELD_ALLOWLISTS[btype]
                    _check_field_drift(f'block:{btype}', mandatory, optional,
                                       frozenset(block.keys()), cu, mu, drift_events)
                if btype == 'tool_result':
                    for item in block.get('content', []):
                        itype = item.get('type')
                        # v1.0: type-level check
                        if itype not in KNOWN_CONTENT_ITEM_TYPES:
                            drift_events.append({
                                'drift_type': 'unknown_tool_result_content_item_type',
                                'observed_type': itype,
                                'conv_uuid': cu,
                                'msg_uuid': mu,
                            })
                            sys.stderr.write(
                                f"WARNING schema-drift: unknown tool_result.content[] "
                                f"type '{itype}' conv={cu[:8]} msg={mu[:8]}\n"
                            )
                        else:
                            # v1.1: content item field drift
                            _check_field_drift(
                                f'content_item:{itype}',
                                _CONTENT_ITEM_FIELD_ALLOWLISTS[itype], frozenset(),
                                frozenset(item.keys()), cu, mu, drift_events,
                            )

    return conv_count, message_count, content_block_count, drift_events


def _parse_and_inspect(src_path):
    """Parse source JSON, assert shape, count records, detect schema drift.
    Returns (raw_data, counts, drift_events). Does not hold raw bytes.
    Drift warnings surface to stderr here so both dry-run and real-run paths see them.
    schema-drift.jsonl is written only by stage1_freeze (needs snapshot dir)."""
    with open(src_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    _shape_assert(data, src_path)
    conv_count, message_count, content_block_count, drift_events = _inspect_data(data)
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
# Delta helpers
# ---------------------------------------------------------------------------

def _read_ledger(snapshots_base):
    """Read ledger.jsonl; return list of entry dicts. Empty list if absent/empty."""
    ledger_path = snapshots_base / 'ledger.jsonl'
    if not ledger_path.exists():
        return []
    entries = []
    with open(ledger_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def _build_seen_set(snapshots_base, ledger_entries):
    """Build the seen-set from all prior snapshots' records.ndjson.
    Returns (seen_pairs: set of (conv_uuid, msg_uuid),
             seen_conv_headers: set of conv_uuid with a header in any prior snapshot).
    The records.ndjson is the authority — never reads raw.json or globs siblings."""
    seen_pairs = set()
    seen_conv_headers = set()
    for entry in ledger_entries:
        sid = entry['snapshot_id']
        # Resolve the highest-numbered scrub-vN overlay for this prior snapshot.
        _scrub_dirs = sorted(
            [p for p in (snapshots_base / sid).iterdir()
             if p.is_dir() and re.fullmatch(r'scrub-v\d+', p.name)],
            key=lambda p: int(p.name[len('scrub-v'):]),
        )
        if not _scrub_dirs:
            sys.exit(
                f"ERROR: seen-set build failed — no scrub-v* overlay found under "
                f"{snapshots_base / sid}. "
                f"Data integrity failure; cannot proceed with incomplete seen-set."
            )
        records_path = _scrub_dirs[-1] / 'records.ndjson'
        if not records_path.exists():
            sys.exit(
                f"ERROR: seen-set build failed — records.ndjson not found at {records_path}. "
                f"Data integrity failure; cannot proceed with incomplete seen-set."
            )
        print(f"[Seen-set] Reading: {records_path}")
        with open(records_path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                if rec.get('record_type') == 'conversation_header':
                    seen_conv_headers.add(rec['conv_uuid'])
                else:
                    seen_pairs.add((rec['conv_uuid'], rec['msg_uuid']))
    return seen_pairs, seen_conv_headers


def _filter_delta(full_data, new_pairs):
    """Return a filtered conv list for the delta raw.json: only convs with net-new messages,
    with chat_messages trimmed to only the new ones. Conv-level metadata carried verbatim
    (Stage 2 scrubs it; Stage 4 drops name/summary per invariant 5.4)."""
    result = []
    for conv in full_data:
        cu = conv['uuid']
        new_msgs = [m for m in conv.get('chat_messages', [])
                    if (cu, m['uuid']) in new_pairs]
        if not new_msgs:
            continue
        filtered = {k: v for k, v in conv.items() if k != 'chat_messages'}
        filtered['chat_messages'] = new_msgs
        result.append(filtered)
    return result


def _wipe_raw(snapshot_dir):
    """Unlink raw.json (Path A, canon RESOLVED S15). Hard-gated: caller must only invoke
    after Stage 3 PASS + Stage 4 complete. Updates manifest.json raw_wiped=True.
    Ledger.jsonl is NOT updated (append-only; manifest.json is the living per-snapshot record)."""
    raw_path = snapshot_dir / 'raw.json'
    raw_size = raw_path.stat().st_size
    os.chmod(raw_path, 0o666)   # Windows requires writable before unlink on a 0o444 file
    os.unlink(raw_path)
    manifest_path = snapshot_dir / 'manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    manifest['raw_wiped'] = True
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f"[Wipe] raw.json unlinked ({raw_size:,} bytes); manifest updated raw_wiped=True")


# ---------------------------------------------------------------------------
# Stage functions
# ---------------------------------------------------------------------------

def stage1_freeze(source_path, source_export_sha256, snapshot_id, snapshot_dir,
                  conv_count, message_count, content_block_count,
                  snapshots_base, drift_events,
                  run_type='baseline', prior_snapshot_id=None,
                  raw_bytes=None, raw_sha256_full=None):
    """Freeze: create snapshot dir, write raw.json, manifest.json, append ledger.
    Baseline: shutil.copyfile from source (byte-verbatim). raw_sha256_full = source hash.
    Delta: write raw_bytes (the filtered slice) directly. raw_sha256_full passed in."""
    print(f"[Stage 1] Creating snapshot: {snapshot_id}")
    snapshot_dir.mkdir(parents=True, exist_ok=False)

    raw_path = snapshot_dir / 'raw.json'
    if raw_bytes is None:
        # Baseline: byte-verbatim copy; re-reads source from disk (no large bytes in memory)
        shutil.copyfile(source_path, raw_path)
        _raw_sha256_full = source_export_sha256
    else:
        # Delta: write the pre-serialized filtered slice
        raw_path.write_bytes(raw_bytes)
        _raw_sha256_full = raw_sha256_full  # pre-computed by caller from the same bytes
    os.chmod(raw_path, 0o444)               # sealed read-only — invariant 5.1
    print(f"[Stage 1] raw.json written ({raw_path.stat().st_size:,} bytes) — sealed read-only")

    # Write schema-drift.jsonl only when drift was detected (snapshot dir now exists).
    # Fix C: two intentionally distinct event shapes coexist in this file, discriminated by
    # drift_type. v1.0 type-level events: {drift_type, observed_type, conv_uuid, msg_uuid}.
    # v1.1 field-level events: {drift_type, object_type, missing_keys, extra_keys, conv_uuid,
    # msg_uuid}. Always check drift_type first before accessing type-specific fields.
    if drift_events:
        entries = [dict(snapshot_id=snapshot_id, **e) for e in drift_events]
        with open(snapshot_dir / 'schema-drift.jsonl', 'w', encoding='utf-8') as f:
            for entry in entries:
                f.write(json.dumps(entry) + '\n')
        print(f"[Stage 1] schema-drift.jsonl: {len(entries)} entries (warn-not-stop)")

    source_mtime = os.path.getmtime(source_path)
    manifest = {
        'snapshot_id':              snapshot_id,
        'type':                     run_type,
        'source_export_path':       str(source_path.resolve()),
        'source_export_mtime':      datetime.fromtimestamp(source_mtime, tz=timezone.utc).isoformat(),
        'source_export_sha256_full': source_export_sha256,
        'raw_sha256_full':          _raw_sha256_full,
        'raw_byte_size':            raw_path.stat().st_size,
        'raw_wiped':                False,   # updated to True by _wipe_raw after Stage 4
        'conv_count':               conv_count,
        'message_count':            message_count,
        'content_block_count':      content_block_count,
        'prior_snapshot_id':        prior_snapshot_id,
        'frozen_at':                datetime.now(tz=timezone.utc).isoformat(),
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


def stage4_ingest(snapshot_dir, scrubbed_data, snapshot_id, seen_conv_headers=None):
    """Ingest: write records.ndjson (conv headers + message records). Seal scrub-vN/.
    seen_conv_headers: set of conv_uuids that already have a header in a prior snapshot.
    None/empty = baseline (all convs get a header). Delta: existing convs skip the header
    but always get their new message records."""
    seen_conv_headers = seen_conv_headers or set()
    run_label = 'delta' if seen_conv_headers else 'baseline'
    print(f"[Stage 4] Ingesting {len(scrubbed_data)} conversations ({run_label})...")
    scrub_dir = snapshot_dir / f'scrub-v{SCRUB_VERSION}'

    sorted_convs = sorted(scrubbed_data, key=lambda c: c['created_at'])
    header_count = 0
    msg_count = 0

    with open(scrub_dir / 'records.ndjson', 'w', encoding='utf-8') as f:
        for conv in sorted_convs:
            msgs = conv.get('chat_messages', [])
            conv_uuid = conv['uuid']

            if conv_uuid not in seen_conv_headers:
                # New conv — write a conversation_header record
                root_count = sum(1 for m in msgs if m['parent_message_uuid'] == ROOT_SENTINEL)
                multi_root = root_count > 1

                parent_child_counts: dict = {}
                for m in msgs:
                    p = m['parent_message_uuid']
                    if p != ROOT_SENTINEL:
                        parent_child_counts[p] = parent_child_counts.get(p, 0) + 1
                has_branches = any(c >= 2 for c in parent_child_counts.values())

                # name and summary intentionally excluded (invariant 5.4 / D5)
                header = {
                    'record_type':   'conversation_header',
                    'snapshot_id':   snapshot_id,
                    'scrub_version': SCRUB_VERSION,
                    'conv_uuid':     conv_uuid,
                    'created_at':    conv['created_at'],
                    'updated_at':    conv['updated_at'],
                    'account_uuid':  conv['account']['uuid'],
                    'message_count': len(msgs),
                    'has_branches':  has_branches,
                    'multi_root':    multi_root,
                }
                f.write(json.dumps(header, ensure_ascii=False) + '\n')
                header_count += 1

            # Always write message records — all are net-new by construction in delta
            for msg in sorted(msgs, key=lambda m: m['created_at']):
                # conv_name and conv_summary intentionally absent — invariant 5.4 / D5
                record = {
                    'snapshot_id':         snapshot_id,
                    'scrub_version':       SCRUB_VERSION,
                    'conv_uuid':           conv_uuid,
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
        '--export-dir',
        help='Export directory containing conversations.json (primary; use for all delta runs '
             'and new baselines). Pipeline resolves conversations.json within this dir.',
    )
    p.add_argument(
        '--source',
        help='Path to conversations.json directly (legacy back-compat for the original '
             'baseline invocation). --export-dir wins if both are given.',
    )
    p.add_argument(
        '--dry-run', action='store_true',
        help='Parse + inspect for drift + report counts; write nothing',
    )
    p.add_argument(
        '--baseline', action='store_true',
        help='Force baseline mode. Refuses if ledger already contains a baseline '
             '(guard against silently minting a second baseline).',
    )
    args = p.parse_args()

    # --- Resolve source path + snapshots_base ---
    if args.export_dir:
        export_dir = Path(args.export_dir)
        source_path = export_dir / 'conversations.json'
        snapshots_base = export_dir.parent / 'snapshots'
    elif args.source:
        source_path = Path(args.source)
        snapshots_base = source_path.parent / 'snapshots'
    else:
        sys.exit("ERROR: must supply --export-dir DIR or --source FILE")

    if not source_path.exists():
        sys.exit(f"ERROR: conversations.json not found: {source_path}")

    # --- Hash source (always the full export — used as source_export_sha256_full) ---
    print(f"Hashing {source_path} ({source_path.stat().st_size / 1024 / 1024:.1f} MB)...")
    source_sha256 = _file_sha256(source_path)
    source_mtime = os.path.getmtime(source_path)
    mtime_date = datetime.fromtimestamp(source_mtime, tz=timezone.utc).strftime('%Y-%m-%d')

    # --- Run-type detection ---
    ledger_entries = _read_ledger(snapshots_base)
    if args.baseline:
        if any(e.get('type') == 'baseline' for e in ledger_entries):
            sys.exit(
                "ERROR: --baseline refused — ledger already contains a baseline snapshot. "
                "To ingest new exports use delta mode (--export-dir without --baseline)."
            )
        run_type = 'baseline'
    elif not ledger_entries:
        run_type = 'baseline'
    else:
        run_type = 'delta'

    print(f"Run type: {run_type}")

    # =========================================================================
    # BASELINE PATH
    # =========================================================================
    if run_type == 'baseline':
        snapshot_id = f"baseline-{mtime_date}-{source_sha256[:8]}"
        snapshot_dir = snapshots_base / snapshot_id

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
        if snapshot_dir.exists():
            sys.exit(
                f"ERROR: snapshot {snapshot_id} already exists at {snapshot_dir} — "
                f"refusing overwrite (invariant 5.2)"
            )
        ledger_path = snapshots_base / 'ledger.jsonl'
        if ledger_path.exists():
            with open(ledger_path, encoding='utf-8') as lf:
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
            run_type='baseline',
        )

        scrubbed_data = stage2_scrub(snapshot_dir, data, snapshot_id)

        if not stage3_verify(snapshot_dir, scrubbed_data, snapshot_id):
            sys.exit(
                f"ERROR: Stage 3 verify-clean FAILED — Stage 4 halted. raw.json survives. "
                f"See {snapshot_dir / f'scrub-v{SCRUB_VERSION}' / 'verify.log'}"
            )

        stage4_ingest(snapshot_dir, scrubbed_data, snapshot_id)
        _wipe_raw(snapshot_dir)

    # =========================================================================
    # DELTA PATH
    # =========================================================================
    else:
        if not ledger_entries:
            sys.exit("ERROR: delta mode requires at least one prior snapshot in ledger — none found")

        seen_pairs, seen_conv_headers = _build_seen_set(snapshots_base, ledger_entries)
        print(f"[Seen-set] {len(seen_pairs):,} (conv,msg) pairs / "
              f"{len(seen_conv_headers)} conv headers from {len(ledger_entries)} prior snapshot(s)")

        print(f"Loading export JSON...")
        with open(source_path, 'r', encoding='utf-8') as f:
            full_data = json.load(f)
        _shape_assert(full_data, source_path)

        # Drift detection on the FULL export — catches schema changes on any conv,
        # not just convs with net-new messages. A change on an untouched conv would be
        # invisible if we only inspected the slice. Counts here are for reporting only.
        full_conv_count, full_msg_count, full_block_count, drift_events = _inspect_data(full_data)
        print(f"Drift detection (full export): {full_conv_count} convs / {full_msg_count} msgs / "
              f"{full_block_count} blocks / {len(drift_events)} drift event(s)"
              + (" (see stderr warnings above)" if drift_events else ""))

        # UUID-set-difference — date NEVER a filter, hint, or proxy (invariant 5.9)
        export_pairs = {
            (c['uuid'], m['uuid'])
            for c in full_data
            for m in c.get('chat_messages', [])
        }
        new_pairs = export_pairs - seen_pairs
        vanished  = seen_pairs - export_pairs

        if vanished:
            warn_msg = (
                f"{'WARN' if args.dry_run else 'ERROR'}: {len(vanished)} baseline (conv,msg) "
                f"pair(s) are missing from this export — cross-export UUID instability "
                f"suspected or wrong/corrupt export."
            )
            if not args.dry_run:
                sys.exit(
                    f"{warn_msg} Real run refused — sealing a delta against this is immortal. "
                    f"Investigate before proceeding."
                )
            print(warn_msg)

        delta_data = _filter_delta(full_data, new_pairs)

        # Ingest counts — what we're actually sealing (distinct from the full-export drift scan)
        delta_conv_count  = len(delta_data)
        delta_msg_count   = sum(len(c.get('chat_messages', [])) for c in delta_data)
        delta_block_count = sum(
            len(m.get('content', []))
            for c in delta_data
            for m in c.get('chat_messages', [])
        )

        # Delta breakdown: convs getting a new header vs convs getting only message records
        brand_new_conv_uuids = {c for c, m in new_pairs} - seen_conv_headers
        append_conv_uuids    = {c for c, m in new_pairs} & seen_conv_headers
        brand_new_msgs = sum(1 for c, m in new_pairs if c in brand_new_conv_uuids)
        append_msgs    = sum(1 for c, m in new_pairs if c in append_conv_uuids)

        # Serialize + hash the filtered slice — raw_sha256_full ≠ source_sha256 for delta
        raw_bytes  = json.dumps(delta_data, ensure_ascii=False).encode('utf-8')
        raw_sha256 = hashlib.sha256(raw_bytes).hexdigest()
        snapshot_id      = f"delta-{mtime_date}-{raw_sha256[:8]}"
        snapshot_dir     = snapshots_base / snapshot_id
        prior_snapshot_id = ledger_entries[-1]['snapshot_id']

        print(f"Snapshot ID  : {snapshot_id}")
        print(f"Source sha256 (full export) : {source_sha256}")
        print(f"Raw sha256   (delta slice)  : {raw_sha256}")
        print(f"Delta (to seal): {delta_conv_count} convs / {delta_msg_count} msgs / "
              f"{delta_block_count} blocks")
        print(f"Net-new messages  : {len(new_pairs):,}")
        print(f"  brand-new convs : {len(brand_new_conv_uuids)} convs / {brand_new_msgs} msgs "
              f"(will write header)")
        print(f"  existing convs  : {len(append_conv_uuids)} convs / {append_msgs} msgs "
              f"(no new header)")
        print(f"  vanished pairs  : {len(vanished)}")
        print(f"Schema drift : {len(drift_events)} event(s)"
              + (" (see stderr warnings above)" if drift_events else ""))

        if args.dry_run:
            if snapshot_dir.exists():
                print(f"NOTE: snapshot already exists — real run would refuse (invariant 5.2)")
            print(f"\n[DRY-RUN] Snapshot dir would be: {snapshot_dir}")
            print("[DRY-RUN] No files written.")
            return

        # Idempotency check
        if snapshot_dir.exists():
            sys.exit(
                f"ERROR: snapshot {snapshot_id} already exists at {snapshot_dir} — "
                f"refusing overwrite (invariant 5.2)"
            )
        if any(e.get('snapshot_id') == snapshot_id for e in ledger_entries):
            sys.exit(
                f"ERROR: snapshot {snapshot_id} already in ledger — "
                f"refusing re-run (invariant 5.2)"
            )

        stage1_freeze(
            source_path, source_sha256, snapshot_id, snapshot_dir,
            delta_conv_count, delta_msg_count, delta_block_count,
            snapshots_base, drift_events,
            run_type='delta', prior_snapshot_id=prior_snapshot_id,
            raw_bytes=raw_bytes, raw_sha256_full=raw_sha256,
        )

        scrubbed_data = stage2_scrub(snapshot_dir, delta_data, snapshot_id)

        if not stage3_verify(snapshot_dir, scrubbed_data, snapshot_id):
            sys.exit(
                f"ERROR: Stage 3 verify-clean FAILED — Stage 4 halted. raw.json survives. "
                f"See {snapshot_dir / f'scrub-v{SCRUB_VERSION}' / 'verify.log'}"
            )

        stage4_ingest(snapshot_dir, scrubbed_data, snapshot_id,
                      seen_conv_headers=seen_conv_headers)
        _wipe_raw(snapshot_dir)

    print(f"\nDone. Snapshot : {snapshot_id}")
    print(f"Location       : {snapshot_dir}")


if __name__ == '__main__':
    main()
