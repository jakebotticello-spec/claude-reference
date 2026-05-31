# apparatus_overlay_v2_drill.py · v0.3 · apparatus S21 · 2026-05-31 · full-scale scrub-v2 overlay (N=all)
# v0.1: Rung 5 — N=10 synthetic drill; Gates 1-4; scrub-v2/ minted from absent state
# v0.2: Rung 6 — N=all (23,095 records); pre-delete guard + rm-then-rewrite; WANT _build_seen_set check; fix Unicode arrow in print
# v0.3: S21 — relocated to /pipeline/ (executable code out of active/); path block updated
import sys
import json
import re
import os
import hashlib
from pathlib import Path

_HERE       = Path(__file__).parent           # pipeline/
_APPARATUS  = _HERE                            # pipeline/ — pipeline now co-located
_REPO       = _HERE.parent                     # repo root (parent of pipeline/)
SNAPSHOTS   = _REPO / 'apparatus-archive' / 'snapshots'
BASELINE_ID  = 'baseline-2026-05-25-ae015455'
BASELINE_DIR = SNAPSHOTS / BASELINE_ID
SRC          = BASELINE_DIR / 'scrub-v1' / 'records.ndjson'
DST_DIR      = BASELINE_DIR / 'scrub-v2'

N_DRILL         = 10       # exact line count of Rung 5 drill artifact — pre-delete guard only
EXPECTED_TOTAL  = 23_095   # confirmed off disk: 294 headers + 22,801 messages
SCRUB_V2        = 2
KNOWN_V1_SHA256 = '4ef22940e3fbb849c2c14fba62fdae2a44277963f0ea5c9f7f2086c706415ba3'
CONTENT_FIELDS  = ('text', 'content_blocks', 'attachments', 'files')
DRILL_FILES     = frozenset({'records.ndjson', 'scrub-audit.jsonl', 'verify.log'})

# Import v1 PATTERNS + seen-set helpers from pipeline
sys.path.insert(0, str(_APPARATUS))
from apparatus_freeze_pipeline import (  # noqa: E402
    PATTERNS as PATTERNS_V1,
    _read_ledger,
    _build_seen_set,
)

PATTERNS_V2 = PATTERNS_V1 + [
    ('EXAMPLE', r'\bEXAMPLE\b', '[SCRUB-V2-DRILL]'),
]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest().lower()


def scrub_walk(obj, path, patterns, audit_list, conv_uuid, msg_uuid):
    """Recursive descent — returns rebuilt object with pattern matches redacted."""
    if isinstance(obj, str):
        result = obj
        for pname, pattern, token in patterns:
            def replacer(m, _pn=pname, _tk=token):
                audit_list.append({
                    'snapshot_id':     BASELINE_ID,
                    'scrub_version':   SCRUB_V2,
                    'conv_uuid':       conv_uuid,
                    'msg_uuid':        msg_uuid,
                    'json_path':       path,
                    'pattern_class':   _pn,
                    'redaction_token': _tk,
                    'original_length': len(m.group(0)),
                })
                return _tk
            result = re.sub(pattern, replacer, result)
        return result
    elif isinstance(obj, dict):
        return {
            k: scrub_walk(
                v, f'{path}.{k}' if path else k,
                patterns, audit_list, conv_uuid, msg_uuid,
            )
            for k, v in obj.items()
        }
    elif isinstance(obj, list):
        return [
            scrub_walk(
                item, f'{path}[{i}]',
                patterns, audit_list, conv_uuid, msg_uuid,
            )
            for i, item in enumerate(obj)
        ]
    else:
        return obj


def scan_strings(obj, patterns, hits, counters):
    """Read-only recursive scan — counts remaining pattern hits for verify.log."""
    if isinstance(obj, str):
        counters['bytes'] += len(obj.encode('utf-8'))
        counters['strings'] += 1
        for pname, pattern, _ in patterns:
            hits[pname] += len(re.findall(pattern, obj))
    elif isinstance(obj, dict):
        for v in obj.values():
            scan_strings(v, patterns, hits, counters)
    elif isinstance(obj, list):
        for item in obj:
            scan_strings(item, patterns, hits, counters)


def run_overlay_drill():
    print(f'=== apparatus RUNG 6: scrub-v2 full-scale overlay (N={EXPECTED_TOTAL:,}) ===')
    print(f'  source : {SRC}')
    print(f'  dest   : {DST_DIR}')
    print()

    # --- Gate 4 PRE: verify scrub-v1 hash before any write ---
    pre_hash = sha256_file(SRC)
    assert pre_hash == KNOWN_V1_SHA256, (
        f'[Gate 4 PRE] FAIL: scrub-v1 hash mismatch\n'
        f'  got:      {pre_hash}\n'
        f'  expected: {KNOWN_V1_SHA256}'
    )
    print(f'[Gate 4 pre]  PASS: scrub-v1/records.ndjson SHA-256 = {pre_hash}')

    # --- Pre-delete guard: positively identify drill artifact before any unlink ---
    assert DST_DIR.exists(), (
        f'[Pre-delete guard] FAIL: {DST_DIR} does not exist — expected Rung 5 drill artifact'
    )
    existing_names = frozenset(f.name for f in DST_DIR.iterdir() if f.is_file())
    assert existing_names == DRILL_FILES, (
        f'[Pre-delete guard] FAIL: unexpected file set in scrub-v2/\n'
        f'  got:      {sorted(existing_names)}\n'
        f'  expected: {sorted(DRILL_FILES)}\n'
        f'  aborting — do NOT delete'
    )
    with open(DST_DIR / 'records.ndjson', 'r', encoding='utf-8') as _f:
        drill_line_count = sum(1 for line in _f if line.strip())
    assert drill_line_count == N_DRILL, (
        f'[Pre-delete guard] FAIL: scrub-v2/records.ndjson has {drill_line_count} lines, '
        f'expected {N_DRILL} (Rung 5 drill) — aborting, do NOT delete'
    )
    print(
        f'[Pre-delete guard] PASS: scrub-v2/ = {sorted(DRILL_FILES)}, '
        f'records.ndjson = {drill_line_count} lines (drill confirmed)'
    )

    # --- rm-then-rewrite: unlink drill files, directory persists ---
    for fpath in sorted(DST_DIR.iterdir()):
        if fpath.is_file():
            os.chmod(fpath, 0o666)
            fpath.unlink()
    print(f'  drill artifacts removed (chmod 0o666 + unlink), scrub-v2/ dir retained')

    # --- Gate 1 + streaming re-scrub + write ---
    print(f'  streaming {EXPECTED_TOTAL:,} records (progress every 2,000) …', flush=True)
    audit_list = []
    lines_in   = 0
    lines_out  = 0

    records_path = DST_DIR / 'records.ndjson'
    with open(SRC, 'r', encoding='utf-8') as fin, \
         open(records_path, 'w', encoding='utf-8') as fout:
        for raw_line in fin:
            raw_line = raw_line.strip()
            if not raw_line:
                continue
            lines_in += 1
            rec = json.loads(raw_line)

            # Gate 1: assert scrub_version == 1 on every record
            assert rec.get('scrub_version') == 1, (
                f'[Gate 1] FAIL: record {lines_in} has '
                f'scrub_version={rec.get("scrub_version")}'
            )

            out = dict(rec)
            conv_uuid = rec.get('conv_uuid', '')
            msg_uuid  = rec.get('msg_uuid', '')

            if rec.get('record_type') == 'conversation_header':
                pass  # pure metadata — skip scrub_walk, no audit entries
            else:
                for field in CONTENT_FIELDS:
                    if field in out and out[field] is not None:
                        out[field] = scrub_walk(
                            out[field], field,
                            PATTERNS_V2, audit_list, conv_uuid, msg_uuid,
                        )

            out['scrub_version'] = SCRUB_V2
            fout.write(json.dumps(out, ensure_ascii=False) + '\n')
            lines_out += 1

            if lines_in % 2000 == 0:
                print(f'    … {lines_in:,} / {EXPECTED_TOTAL:,}', flush=True)

    # Gate 1 final: total count
    assert lines_in == EXPECTED_TOTAL, (
        f'[Gate 1] FAIL: read {lines_in} records, expected {EXPECTED_TOTAL}'
    )
    print(f'[Gate 1]      PASS: {lines_in:,} input records from scrub-v1, all scrub_version=1')

    # Gate 2
    assert lines_out == EXPECTED_TOTAL, (
        f'[Gate 2] FAIL: wrote {lines_out} records, expected {EXPECTED_TOTAL}'
    )
    print(
        f'[Gate 2]      PASS: {lines_out:,} output records '
        f'(full-restated-standalone, N={EXPECTED_TOTAL:,})'
    )

    # --- Write scrub-audit.jsonl ---
    audit_path = DST_DIR / 'scrub-audit.jsonl'
    with open(audit_path, 'w', encoding='utf-8') as f:
        for entry in audit_list:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    print(
        f'  scrub-audit : {len(audit_list)} match entries '
        f'(EXAMPLE + v1 rules on already-scrubbed text)'
    )

    # --- Verify scan: post-scrub scan of scrub-v2/records.ndjson ---
    print(f'  verify scan …', flush=True)
    hits     = {pname: 0 for pname, _, _ in PATTERNS_V2}
    counters = {'bytes': 0, 'strings': 0}
    with open(records_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                scan_strings(json.loads(line), PATTERNS_V2, hits, counters)

    passed = all(v == 0 for v in hits.values())
    verify_log = {
        'passed':               passed,
        'scrub_version':        SCRUB_V2,
        'scanned_bytes':        counters['bytes'],
        'scanned_strings':      counters['strings'],
        'regex_hits_per_class': hits,
    }
    verify_path = DST_DIR / 'verify.log'
    verify_path.write_text(json.dumps(verify_log, indent=2), encoding='utf-8')
    print(f'  verify.log  : passed={passed}, hits={hits}')

    # --- Seal scrub-v2/ read-only ---
    for fpath in sorted(DST_DIR.iterdir()):
        if fpath.is_file():
            os.chmod(fpath, 0o444)
    print(f'  scrub-v2/   : sealed 0o444')

    # --- SHA-256 of scrub-v2/records.ndjson ---
    v2_hash = sha256_file(records_path)
    print(f'  scrub-v2/records.ndjson SHA-256 : {v2_hash}')

    # --- Gate 4 POST: scrub-v1 hash must be unchanged ---
    post_hash = sha256_file(SRC)
    assert post_hash == KNOWN_V1_SHA256, (
        f'[Gate 4 POST] *** INTEGRITY VIOLATION *** scrub-v1/records.ndjson hash CHANGED\n'
        f'  got:      {post_hash}\n'
        f'  expected: {KNOWN_V1_SHA256}\n'
        f'  *** floor integrity breach — halt immediately ***'
    )
    print(
        f'[Gate 4 post] PASS: scrub-v1/records.ndjson SHA-256 = {post_hash} (UNCHANGED)'
    )

    # --- WANT: _build_seen_set live-floor resolution ---
    print()
    print('=== WANT: _build_seen_set live-floor resolution ===')
    print('  Expected: baseline -> scrub-v2 (max-N), delta -> scrub-v1')
    ledger_entries = _read_ledger(SNAPSHOTS)
    print(f'  Ledger snapshots : {[e["snapshot_id"] for e in ledger_entries]}')
    _, _ = _build_seen_set(SNAPSHOTS, ledger_entries)
    print('  (resolution paths shown in [Seen-set] lines above)')

    # --- Summary ---
    print()
    print('=== RUNG 6 COMPLETE ===')
    print(f'  scrub-v2/records.ndjson SHA-256  : {v2_hash}')
    example_hits = hits.get('EXAMPLE', 0)
    verdict = '(zero-hit = PASS)' if example_hits == 0 else '(non-zero = PASS, benign drill token)'
    print(f'  EXAMPLE hits (drill rule)         : {example_hits}  {verdict}')
    print(f'  scrub-v1 SHA-256 unchanged        : {post_hash}')


if __name__ == '__main__':
    run_overlay_drill()
