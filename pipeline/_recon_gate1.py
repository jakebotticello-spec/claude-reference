"""Gate 1 recon — read-only, no mutations. Answers all 5 questions."""
import re, os, sys
from pathlib import Path

env_path = Path(__file__).parent / 'secrets' / '.env'
db_url = None
for line in env_path.read_text(encoding='utf-8').splitlines():
    m = re.match(r'^\s*SUPABASE_DB_URL\s*=\s*(.+)$', line)
    if m:
        db_url = m.group(1).strip().strip('"').strip("'")
if not db_url:
    sys.exit("ERROR: SUPABASE_DB_URL not found")

import psycopg

with psycopg.connect(db_url) as conn:
    with conn.cursor() as cur:

        # ── 1. ROW COUNTS ──────────────────────────────────────────────────
        print("=" * 60)
        print("1. ROW COUNTS")
        print("=" * 60)
        cur.execute("SELECT count(*) FROM floor_conv_messages")
        msg_count = cur.fetchone()[0]
        cur.execute("SELECT count(*) FROM floor_conv_headers")
        hdr_count = cur.fetchone()[0]
        print(f"  floor_conv_messages : {msg_count:,}")
        print(f"  floor_conv_headers  : {hdr_count:,}")
        print(f"  expected 24,138 msg : {'MATCH' if msg_count == 24138 else f'FLAG -- got {msg_count}'}")
        print(f"  expected 325 hdr    : {'MATCH' if hdr_count == 325 else f'FLAG -- got {hdr_count}'}")

        # ── 2. COLUMN LISTING + ORDINAL CHECK ──────────────────────────────
        print()
        print("=" * 60)
        print("2. MESSAGES TABLE COLUMNS + TYPES")
        print("=" * 60)
        cur.execute("""
            SELECT column_name, data_type, is_nullable, column_default
            FROM information_schema.columns
            WHERE table_name = 'floor_conv_messages'
            ORDER BY ordinal_position
        """)
        rows = cur.fetchall()
        for col, dtype, nullable, default in rows:
            print(f"  {col:<28} {dtype:<20} nullable={nullable}  default={default}")

        print()
        print("  ORDINAL/SEQUENCE CHECK:")
        cur.execute("""
            SELECT column_name, data_type, column_default
            FROM information_schema.columns
            WHERE table_name = 'floor_conv_messages'
              AND (column_default LIKE 'nextval%'
                   OR data_type IN ('bigint','integer','smallint'))
            ORDER BY ordinal_position
        """)
        ordinal_hits = cur.fetchall()
        if ordinal_hits:
            for c in ordinal_hits:
                print(f"    candidate: {c[0]}  type={c[1]}  default={c[2]}")
        else:
            print("    NONE -- no serial/sequence/int column found")

        cur.execute(
            "SELECT min(ctid::text), max(ctid::text) FROM floor_conv_messages"
        )
        ctid_row = cur.fetchone()
        print(f"  ctid range (physical, NOT stable): min={ctid_row[0]}  max={ctid_row[1]}")

        # ── 3. created_at DISTRIBUTION ─────────────────────────────────────
        print()
        print("=" * 60)
        print("3. created_at DISTRIBUTION")
        print("=" * 60)
        # stored as TEXT -- cast to timestamptz
        cur.execute("""
            SELECT min(created_at::timestamptz), max(created_at::timestamptz)
            FROM floor_conv_messages
        """)
        mn, mx = cur.fetchone()
        print(f"  MIN created_at : {mn}")
        print(f"  MAX created_at : {mx}")

        print()
        print("  Monthly buckets (full table):")
        cur.execute("""
            SELECT date_trunc('month', created_at::timestamptz) AS m,
                   count(*) AS cnt
            FROM floor_conv_messages
            GROUP BY m
            ORDER BY m
        """)
        lumpiest_month, lumpiest_count = None, 0
        for row in cur.fetchall():
            m_label = row[0].strftime('%Y-%m') if row[0] else 'NULL'
            cnt = row[1]
            if cnt > lumpiest_count:
                lumpiest_count, lumpiest_month = cnt, m_label
            print(f"    {m_label}  {cnt:>6,}")
        print(f"  lumpiest: {lumpiest_month} @ {lumpiest_count:,}")

        # ── 4. CONVERSATION SIZE DISTRIBUTION ──────────────────────────────
        print()
        print("=" * 60)
        print("4. CONVERSATION SIZE DISTRIBUTION (from floor_conv_headers)")
        print("=" * 60)
        cur.execute("""
            SELECT
                count(*) AS conv_count,
                min(message_count)  AS min_msgs,
                max(message_count)  AS max_msgs,
                round(avg(message_count), 1) AS avg_msgs,
                percentile_cont(0.5) WITHIN GROUP (ORDER BY message_count) AS median,
                percentile_cont(0.9) WITHIN GROUP (ORDER BY message_count) AS p90
            FROM floor_conv_headers
        """)
        r = cur.fetchone()
        conv_count, mn_m, mx_m, avg_m, median_m, p90_m = r
        print(f"  conv count : {conv_count}")
        print(f"  min msgs   : {mn_m}")
        print(f"  max msgs   : {mx_m}")
        print(f"  avg msgs   : {avg_m}")
        print(f"  median     : {median_m}")
        print(f"  p90        : {p90_m}")

        print()
        print("  TOP 20 whales (message_count DESC):")
        cur.execute("""
            SELECT conv_uuid, snapshot_id, message_count
            FROM floor_conv_headers
            ORDER BY message_count DESC
            LIMIT 20
        """)
        for row in cur.fetchall():
            print(f"    {row[0]}  snap={row[1]}  msgs={row[2]:,}")

        cur.execute("SELECT count(*) FROM floor_conv_headers WHERE message_count < 5")
        minnows = cur.fetchone()[0]
        print(f"\n  Convs with < 5 messages (minnows): {minnows}")

        # ── 5. FORESTS ─────────────────────────────────────────────────────
        print()
        print("=" * 60)
        print("5. FORESTS")
        print("=" * 60)
        cur.execute("SELECT count(*) FROM floor_conv_headers WHERE multi_root = true")
        forest_count = cur.fetchone()[0]
        cur.execute("SELECT count(*) FROM floor_conv_headers WHERE multi_root = false")
        tree_count = cur.fetchone()[0]
        print(f"  multi_root=true  (forests) : {forest_count}")
        print(f"  multi_root=false (trees)   : {tree_count}")
        print(f"  total                       : {forest_count + tree_count}")

        print()
        print("  Top 5 forests by message_count:")
        cur.execute("""
            SELECT conv_uuid, snapshot_id, message_count
            FROM floor_conv_headers
            WHERE multi_root = true
            ORDER BY message_count DESC
            LIMIT 5
        """)
        for row in cur.fetchall():
            print(f"    {row[0]}  snap={row[1]}  msgs={row[2]:,}")

        print()
        cur.execute("""
            SELECT count(*)
            FROM (
                SELECT conv_uuid
                FROM floor_conv_messages
                WHERE is_root = true
                GROUP BY conv_uuid
                HAVING count(*) > 1
            ) sq
        """)
        actual_forests = cur.fetchone()[0]
        print(f"  Cross-check via is_root column: convs with >1 root msg = {actual_forests}")

    conn.rollback()

print()
print("=" * 60)
print("RECON COMPLETE -- no writes performed")
print("=" * 60)
