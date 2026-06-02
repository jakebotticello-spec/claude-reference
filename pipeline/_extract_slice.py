"""pipeline/_extract_slice.py
Extract one slice's conversations from the apparatus floor into a JSON span file.
Read-only -- SELECT only, conn.rollback() at end. No floor mutations.
Usage: python _extract_slice.py [slice_index]   (default: 7)
"""
import re, sys, json, os
from pathlib import Path

SLICE_INDEX = int(sys.argv[1]) if len(sys.argv) > 1 else 7

# -- creds (same pattern as _recon_gate1.py) --
env_path = Path(__file__).parent / 'secrets' / '.env'
db_url = None
for line in env_path.read_text(encoding='utf-8').splitlines():
    m = re.match(r'^\s*SUPABASE_DB_URL\s*=\s*(.+)$', line)
    if m:
        db_url = m.group(1).strip().strip('"').strip("'")
if not db_url:
    sys.exit("ERROR: SUPABASE_DB_URL not found")

# -- read conv_uuids from manifest (never hardcoded) --
manifest_path = Path(__file__).parent / 'recon' / 'slice_manifest_S27.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
slice_entry = next((s for s in manifest if s['slice_index'] == SLICE_INDEX), None)
if slice_entry is None:
    sys.exit(f"ERROR: slice_index {SLICE_INDEX} not found in manifest")

conv_uuids     = slice_entry['conv_uuids']
expected_msgs  = slice_entry['message_count']
expected_convs = slice_entry['conv_count']

print(f"Slice {SLICE_INDEX}: {expected_convs} convs, {expected_msgs} messages expected")
print(f"  conv_uuids read from manifest -- not hardcoded")

import psycopg

with psycopg.connect(db_url) as conn:
    with conn.cursor() as cur:

        # Query A: headers
        cur.execute("""
            SELECT snapshot_id, conv_uuid::text, account_uuid::text, record_type,
                   multi_root, has_branches, message_count, scrub_version,
                   created_at, updated_at
            FROM floor_conv_headers
            WHERE conv_uuid::text = ANY(%s)
            ORDER BY conv_uuid, snapshot_id
        """, (conv_uuids,))
        hdr_rows = cur.fetchall()
        HDR_COLS = ['snapshot_id', 'conv_uuid', 'account_uuid', 'record_type',
                    'multi_root', 'has_branches', 'message_count', 'scrub_version',
                    'created_at', 'updated_at']

        # Query B: messages (all columns the reader needs)
        cur.execute("""
            SELECT snapshot_id, conv_uuid::text, msg_uuid::text,
                   parent_message_uuid::text,
                   is_root, sender, text, content_blocks, created_at
            FROM floor_conv_messages
            WHERE conv_uuid::text = ANY(%s)
        """, (conv_uuids,))
        msg_rows = cur.fetchall()
        MSG_COLS = ['snapshot_id', 'conv_uuid', 'msg_uuid', 'parent_message_uuid',
                    'is_root', 'sender', 'text', 'content_blocks', 'created_at']

    conn.rollback()

# -- reconciliation gate: STOP before writing if counts diverge --
actual_total = len(msg_rows)
if actual_total != expected_msgs:
    print()
    print("FLAG: message count mismatch -- file NOT written")
    print(f"  manifest  : {expected_msgs}")
    print(f"  floor     : {actual_total}")
    print(f"  delta     : {actual_total - expected_msgs:+d}")
    sys.exit(1)

print(f"  Reconciliation PASS: {actual_total} messages match manifest")

# -- organise into dicts --
def to_dict(row, cols):
    return dict(zip(cols, row))

headers_by_conv = {cu: [] for cu in conv_uuids}
for row in hdr_rows:
    d = to_dict(row, HDR_COLS)
    if d['conv_uuid'] in headers_by_conv:
        headers_by_conv[d['conv_uuid']].append(d)

msgs_by_conv = {cu: [] for cu in conv_uuids}
for row in msg_rows:
    d = to_dict(row, MSG_COLS)
    if d['conv_uuid'] in msgs_by_conv:
        msgs_by_conv[d['conv_uuid']].append(d)

# -- tree-order: iterative DFS pre-order --
# Sentinel parent UUID for root messages
SENTINEL = '00000000-0000-4000-8000-000000000000'

def tree_order(messages):
    # Deduplicate by msg_uuid (snapshot_id sort so baseline wins over delta)
    seen = {}
    for m in sorted(messages, key=lambda x: x['snapshot_id']):
        if m['msg_uuid'] not in seen:
            seen[m['msg_uuid']] = m
    unique = list(seen.values())

    msg_set  = {m['msg_uuid'] for m in unique}
    children = {m['msg_uuid']: [] for m in unique}
    roots, orphans = [], []

    for m in unique:
        if m['is_root']:
            roots.append(m)
        else:
            parent = m['parent_message_uuid']
            if parent in children:
                children[parent].append(m)
            else:
                orphans.append(m)

    if orphans:
        print(f"  WARNING: {len(orphans)} orphan(s) in {unique[0]['conv_uuid']} treated as roots")
        roots.extend(orphans)

    # Deterministic: sort by (created_at str, msg_uuid str)
    roots.sort(key=lambda x: (x['created_at'], x['msg_uuid']))
    for k in children:
        children[k].sort(key=lambda x: (x['created_at'], x['msg_uuid']))

    # Iterative DFS pre-order (safe for deep trees)
    result = []
    stack  = list(reversed(roots))
    while stack:
        node = stack.pop()
        result.append(node)
        for kid in reversed(children.get(node['msg_uuid'], [])):
            stack.append(kid)
    return result

# -- assemble output (conversations in manifest order) --
output = []
for cu in conv_uuids:
    output.append({
        'conv_uuid': cu,
        'headers':   headers_by_conv[cu],
        'messages':  tree_order(msgs_by_conv[cu]),
    })

# -- write file --
out_path = Path(__file__).parent / 'recon' / f'slice_{SLICE_INDEX:02d}_spans.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, default=str)

file_bytes = os.path.getsize(out_path)

# ── REPORT ─────────────────────────────────────────────────────────────────────

print()
print("=" * 72)
print("(a) COUNTS")
print("=" * 72)
n_convs = len(output)
n_msgs  = sum(len(c['messages']) for c in output)
print(f"  conv count    : {n_convs}  {'MATCH' if n_convs == expected_convs else f'FLAG -- expected {expected_convs}'}")
print(f"  message total : {n_msgs}   {'MATCH' if n_msgs == expected_msgs   else f'FLAG -- expected {expected_msgs}'}")

print()
print("=" * 72)
print("(b) PER-CONVERSATION MESSAGE COUNTS")
print("=" * 72)
print(f"  {'conv_uuid':<36}  {'msgs':>5}")
print(f"  {'-'*36}  {'-----':>5}")
for c in output:
    print(f"  {c['conv_uuid']}  {len(c['messages']):>5}")

print()
print("=" * 72)
print("(c) OUTPUT FILE")
print("=" * 72)
print(f"  path : {out_path}")
print(f"  size : {file_bytes:,} bytes  ({file_bytes / 1048576:.2f} MB)")

print()
print("=" * 72)
print("(d) ROOT COUNTS PER CONV (forest / branch check)")
print("=" * 72)
root_counts = {c['conv_uuid']: sum(1 for m in c['messages'] if m['is_root'])
               for c in output}
max_roots = max(root_counts.values()) if root_counts else 0
flag_found = any(v != 1 for v in root_counts.values())
print(f"  max roots in any conv : {max_roots}  "
      f"{'all single-root trees as expected' if not flag_found else 'FLAG: see below'}")
for cu, rc in root_counts.items():
    if rc != 1:
        print(f"  FLAG: {cu} has {rc} roots")

print()
print("=" * 72)
print("(e) SAMPLE -- first conv header + first 3 messages (truncated)")
print("=" * 72)
first = output[0]
print(f"  conv_uuid     : {first['conv_uuid']}")
print(f"  header rows   : {len(first['headers'])}")
if first['headers']:
    h = first['headers'][0]
    for k in ('snapshot_id','record_type','multi_root','has_branches',
              'message_count','scrub_version','created_at'):
        print(f"    {k:<16}: {h[k]}")
print(f"  messages in conv: {len(first['messages'])}")
print()
for i, msg in enumerate(first['messages'][:3], 1):
    cb = msg['content_blocks']
    if isinstance(cb, list) and cb:
        cb_summary = f"[{len(cb)} block(s): " + ', '.join(
            b.get('type', '?') if isinstance(b, dict) else '?' for b in cb
        ) + "]"
    elif isinstance(cb, list):
        cb_summary = "[]"
    else:
        cb_summary = repr(cb)[:60]
    preview = (msg['text'] or '')[:120].replace('\n', ' ')
    print(f"  msg {i}:")
    print(f"    msg_uuid   : {msg['msg_uuid']}")
    print(f"    parent     : {msg['parent_message_uuid']}")
    print(f"    is_root    : {msg['is_root']}")
    print(f"    sender     : {msg['sender']}")
    print(f"    created_at : {msg['created_at']}")
    print(f"    text[:120] : {preview!r}")
    print(f"    c_blocks   : {cb_summary}")
    print()

print("=" * 72)
print("DONE -- no writes to floor tables.")
print("=" * 72)
