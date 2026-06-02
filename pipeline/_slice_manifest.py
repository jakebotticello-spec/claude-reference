"""pipeline/_slice_manifest.py
Deterministic conversation-bounded slice manifest for apparatus floor.
Read-only — SELECT only, conn.rollback() at end. No floor mutations.
"""
import re, sys, json
from pathlib import Path

# -- creds (same pattern as _recon_gate1.py) --
env_path = Path(__file__).parent / 'secrets' / '.env'
db_url = None
for line in env_path.read_text(encoding='utf-8').splitlines():
    m = re.match(r'^\s*SUPABASE_DB_URL\s*=\s*(.+)$', line)
    if m:
        db_url = m.group(1).strip().strip('"').strip("'")
if not db_url:
    sys.exit("ERROR: SUPABASE_DB_URL not found")

import psycopg

TARGET = 2000

with psycopg.connect(db_url) as conn:
    with conn.cursor() as cur:

        # Query A: per-conv message counts + MIN created_at from live messages table
        cur.execute("""
            SELECT conv_uuid::text,
                   COUNT(*)                      AS msg_count,
                   MIN(created_at::timestamptz)  AS min_ts
            FROM floor_conv_messages
            GROUP BY conv_uuid
        """)
        msg_stats = {r[0]: {'msg_count': r[1], 'min_ts': r[2]} for r in cur.fetchall()}

        # Query B: all distinct conv_uuids from headers + header min created_at + multi_root
        cur.execute("""
            SELECT conv_uuid::text,
                   MIN(created_at::timestamptz)  AS hdr_min_ts,
                   bool_or(multi_root)            AS multi_root
            FROM floor_conv_headers
            GROUP BY conv_uuid
        """)
        hdr_stats = {r[0]: {'hdr_min_ts': r[1], 'multi_root': r[2]} for r in cur.fetchall()}

    conn.rollback()

# -- assemble per-conv records --
convs = []
for conv_uuid, hdr in hdr_stats.items():
    if conv_uuid in msg_stats:
        msg_count    = msg_stats[conv_uuid]['msg_count']
        sort_ts      = msg_stats[conv_uuid]['min_ts']
        zero_msg_rule = None
    else:
        msg_count = 0
        if hdr['hdr_min_ts'] is not None:
            sort_ts       = hdr['hdr_min_ts']
            zero_msg_rule = 'header_created_at'
        else:
            sort_ts       = None
            zero_msg_rule = 'conv_uuid_last'

    convs.append({
        'conv_uuid':      conv_uuid,
        'msg_count':      msg_count,
        'sort_ts':        sort_ts,
        'multi_root':     hdr['multi_root'],
        'zero_msg_rule':  zero_msg_rule,
    })

# -- deterministic sort: sort_ts ASC (None last), then conv_uuid ASC --
convs.sort(key=lambda c: (c['sort_ts'] is None, c['sort_ts'], c['conv_uuid']))

# -- slice accumulation --
slices      = []
cur_convs   = []
cur_msgs    = 0
running     = 0

for conv in convs:
    cur_convs.append(conv)
    cur_msgs  += conv['msg_count']
    running   += conv['msg_count']
    if cur_msgs >= TARGET:
        slices.append({'convs': cur_convs, 'slice_msgs': cur_msgs, 'running': running})
        cur_convs, cur_msgs = [], 0

if cur_convs:
    slices.append({'convs': cur_convs, 'slice_msgs': cur_msgs, 'running': running})

# -- build JSON manifest --
manifest = []
for i, sl in enumerate(slices):
    ts_vals = [c['sort_ts'] for c in sl['convs'] if c['sort_ts'] is not None]
    manifest.append({
        'slice_index':           i,
        'conv_uuids':            [c['conv_uuid'] for c in sl['convs']],
        'conv_count':            len(sl['convs']),
        'message_count':         sl['slice_msgs'],
        'running_total':         sl['running'],
        'span_first_created_at': ts_vals[0].isoformat()  if ts_vals else None,
        'span_last_created_at':  ts_vals[-1].isoformat() if ts_vals else None,
    })

out_dir  = Path(__file__).parent / 'recon'
out_dir.mkdir(exist_ok=True)
out_path = out_dir / 'slice_manifest_S27.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, default=str)

# ── REPORT ─────────────────────────────────────────────────────────────────────
print("=" * 72)
print("(a) SLICE TABLE")
print("=" * 72)
print(f"{'idx':>3}  {'convs':>5}  {'msgs':>6}  {'running':>8}  span")
print("-" * 72)
for sl in manifest:
    print(f"{sl['slice_index']:>3}  {sl['conv_count']:>5}  {sl['message_count']:>6,}  "
          f"{sl['running_total']:>8,}  "
          f"{sl['span_first_created_at'] or 'n/a'}  ->  {sl['span_last_created_at'] or 'n/a'}")
print(f"\nTotal slices: {len(manifest)}")

print()
print("=" * 72)
print("(b) SUM CHECKS")
print("=" * 72)
total_msgs  = sum(sl['message_count'] for sl in manifest)
total_convs = sum(sl['conv_count']    for sl in manifest)
print(f"  SUM message_counts = {total_msgs:,}  {'MATCH' if total_msgs == 24138 else f'FLAG -- expected 24138'}")
print(f"  SUM conv_counts    = {total_convs}  {'MATCH' if total_convs == 325   else f'FLAG -- expected 325'}")

# build conv→slice lookup
conv_to_slice = {}
for sl in manifest:
    for cu in sl['conv_uuids']:
        conv_to_slice[cu] = sl['slice_index']

print()
print("=" * 72)
print("(c) FORESTS (multi_root=true)")
print("=" * 72)
forests = [c for c in convs if c['multi_root']]
print(f"  Forest count: {len(forests)}  {'MATCH (9)' if len(forests) == 9 else 'FLAG'}")
for c in sorted(forests, key=lambda x: conv_to_slice[x['conv_uuid']]):
    print(f"  slice {conv_to_slice[c['conv_uuid']]:>2}  {c['conv_uuid']}  msgs={c['msg_count']}")

print()
print("=" * 72)
print("(d) ZERO-MESSAGE CONVS")
print("=" * 72)
zeros = [c for c in convs if c['zero_msg_rule'] is not None]
print(f"  Zero-msg count: {len(zeros)}")
for c in zeros:
    print(f"  slice {conv_to_slice[c['conv_uuid']]:>2}  {c['conv_uuid']}  "
          f"rule={c['zero_msg_rule']}  sort_ts={c['sort_ts']}")

print()
print("=" * 72)
print("(e) SLICE SIZE STATS")
print("=" * 72)
sizes = [sl['message_count'] for sl in manifest]
mean  = sum(sizes) / len(sizes)
print(f"  min  : {min(sizes):,}")
print(f"  max  : {max(sizes):,}")
print(f"  mean : {mean:,.1f}")

print()
print(f"Manifest written -> {out_path}")
print("=" * 72)
print("DONE -- no writes to floor tables.")
print("=" * 72)
