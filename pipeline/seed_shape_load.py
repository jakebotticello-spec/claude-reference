# seed_shape_load.py · v1.2 · apparatus S23 · 2026-05-31 · production floor LOAD
# v1.1 S23: drop cross-table FK; orphan-check at gate (pre-flight on plan + in-txn re-prove). see ANCHOR FK RESOLVED.
# v1.2 S23: fix post-commit append-only probe — WHERE false matched 0 rows so the per-row trigger never fired (false negative); use a real-row DELETE via ctid, rolled back, so the trigger actually fires and the rejection is proven.
#
# The real production ingest of the corpus floor into the locked apparatus-floor
# Supabase project. Distinct from the S16 seed-shape HARNESS (a DROP-and-load test
# rig that proved the shape ingests 4/4): this is the floor-of-record loader.
#
# Reuses proven parts verbatim:
#   - schema DDL + insert shapes  ← s16_seed_shape_harness.py (the shape that passed 4/4)
#   - max-N overlay resolution    ← apparatus_freeze_pipeline.py _build_seen_set (S19/S20 proven)
#
# What is new (and the whole point of LOAD vs the harness):
#   - reads BOTH snapshots from the ledger, each at its max-N overlay
#     (baseline → scrub-v2, delta → scrub-v1), NOT a single hardcoded path
#   - SINGLE TRANSACTION over the entire ingest (D9 post-lock rec #6): all-or-nothing,
#     so a mid-load failure rolls back to bare schema — zero stranded rows, no
#     append-only-violating DELETE ever needed to recover
#   - installs the append-only hardening (guard fn + BEFORE DELETE/UPDATE triggers +
#     REVOKEs) AFTER the data lands, inside the same transaction
#   - self-reads pipeline/secrets/.env (no pre-set shell var required at runtime)
#   - re-proves append-only as the OWNER role specifically (closes the S22 TRUNCATE-
#     on-postgres ambiguity: don't assume, prove a rejected DELETE as postgres)
#
# Schema reproduces S16 EXACTLY — nothing folded in. The D9 post-lock queue items
# (CHECK constraints, traversal index) are a deliberate SEPARATE pass, not this load.
# Floor keeps ALL bytes: no display_content strip (strip is a retrieval-layer concern;
# the floor's job is fidelity — 15.6% of display_content CARRIES_UNIQUE file text).

import argparse
import json
import os
import re
import sys
from pathlib import Path

import psycopg
import psycopg.errors
from psycopg.types.json import Jsonb

# --- Paths ------------------------------------------------------------------
# This file lives in pipeline/. The floor lives in apparatus-archive/snapshots/,
# OUTSIDE the git tree (sibling of the repo-tracked dirs). .env lives in
# pipeline/secrets/ (gitignored).
_HERE = Path(__file__).resolve().parent                 # .../claude-reference/pipeline
_REPO = _HERE.parent                                    # .../claude-reference
_ENV_PATH = _HERE / 'secrets' / '.env'
_SNAPSHOTS = _REPO / 'apparatus-archive' / 'snapshots'

ROOT_SENTINEL = '00000000-0000-4000-8000-000000000000'
BATCH_SIZE = 500   # batching is for executemany chunking only — NOT per-batch commit

# --- DDL (verbatim from S16 harness — the proven 4/4 schema) ----------------
_DDL_DROP = [
    "DROP TABLE IF EXISTS floor_conv_messages CASCADE",
    "DROP TABLE IF EXISTS floor_conv_headers CASCADE",
    "DROP FUNCTION IF EXISTS floor_immutable_guard() CASCADE",
]
_DDL_HEADERS = """
CREATE TABLE floor_conv_headers (
    snapshot_id   text    NOT NULL,
    conv_uuid     uuid    NOT NULL,
    account_uuid  uuid    NOT NULL,
    record_type   text    NOT NULL,
    multi_root    boolean NOT NULL,
    has_branches  boolean NOT NULL,
    message_count integer NOT NULL,
    scrub_version integer NOT NULL,
    created_at    text    NOT NULL,
    updated_at    text    NOT NULL,
    PRIMARY KEY (snapshot_id, conv_uuid)
)"""
_DDL_MESSAGES = """
CREATE TABLE floor_conv_messages (
    snapshot_id         text    NOT NULL,
    conv_uuid           uuid    NOT NULL,
    msg_uuid            uuid    NOT NULL,
    parent_message_uuid uuid    NOT NULL,
    is_root             boolean NOT NULL,
    sender              text    NOT NULL,
    text                text    NOT NULL,
    content_blocks      jsonb   NOT NULL,
    attachments         jsonb   NOT NULL,
    files               jsonb   NOT NULL,
    scrub_version       integer NOT NULL,
    created_at          text    NOT NULL,
    updated_at          text    NOT NULL,
    PRIMARY KEY (snapshot_id, conv_uuid, msg_uuid)
)"""

# --- Append-only hardening DDL (verbatim shape from the D9 lock) ------------
# Installed AFTER the data lands, inside the same transaction. The guard raises on
# DELETE/UPDATE with no escape hatch; TRUNCATE is walled by REVOKE from app roles
# (owner retains TRUNCATE by PG design — re-proven against owner via DELETE below).
_DDL_GUARD_FN = """
CREATE OR REPLACE FUNCTION floor_immutable_guard() RETURNS trigger AS $$
            BEGIN
                RAISE EXCEPTION 'immutable floor: % not permitted on %', TG_OP, TG_TABLE_NAME
                    USING ERRCODE = '42501';
                RETURN NULL;
            END;
            $$ LANGUAGE plpgsql"""
_DDL_TRIGGERS = [
    """CREATE TRIGGER floor_conv_headers_no_delete_update
       BEFORE DELETE OR UPDATE ON floor_conv_headers
       FOR EACH ROW EXECUTE FUNCTION floor_immutable_guard()""",
    """CREATE TRIGGER floor_conv_messages_no_delete_update
       BEFORE DELETE OR UPDATE ON floor_conv_messages
       FOR EACH ROW EXECUTE FUNCTION floor_immutable_guard()""",
]
_DDL_REVOKES = [
    "REVOKE TRUNCATE, REFERENCES, TRIGGER ON floor_conv_headers FROM anon, authenticated, service_role",
    "REVOKE TRUNCATE, REFERENCES, TRIGGER ON floor_conv_messages FROM anon, authenticated, service_role",
]

# --- Insert SQL (verbatim column order from S16 harness) --------------------
_SQL_INS_HDR = """
INSERT INTO floor_conv_headers
    (snapshot_id, conv_uuid, account_uuid, record_type, multi_root, has_branches,
     message_count, scrub_version, created_at, updated_at)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
_SQL_INS_MSG = """
INSERT INTO floor_conv_messages
    (snapshot_id, conv_uuid, msg_uuid, parent_message_uuid, is_root, sender,
     text, content_blocks, attachments, files, scrub_version, created_at, updated_at)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""


def hdr_params(r):
    return (r['snapshot_id'], r['conv_uuid'], r['account_uuid'], r['record_type'],
            r['multi_root'], r['has_branches'], r['message_count'], r['scrub_version'],
            r['created_at'], r['updated_at'])


def msg_params(r):
    return (r['snapshot_id'], r['conv_uuid'], r['msg_uuid'], r['parent_message_uuid'],
            r['is_root'], r['sender'], r['text'],
            Jsonb(r['content_blocks']), Jsonb(r['attachments']), Jsonb(r['files']),
            r['scrub_version'], r['created_at'], r['updated_at'])


# --- .env reader (self-contained; never prints the value) -------------------
def read_db_url():
    """Read SUPABASE_DB_URL from pipeline/secrets/.env. Falls back to the shell env
    if the file is absent (back-compat with the launch-time loader). Never echoes
    the value."""
    if _ENV_PATH.exists():
        for line in _ENV_PATH.read_text(encoding='utf-8').splitlines():
            m = re.match(r'^\s*SUPABASE_DB_URL\s*=\s*(.+)$', line)
            if m:
                return m.group(1).strip().strip('"').strip("'")
    return os.environ.get('SUPABASE_DB_URL')


# --- Ledger + max-N overlay resolution (mirrors pipeline _build_seen_set) ---
def read_ledger():
    """Return ledger entries in order. Each entry is a snapshot manifest dict."""
    ledger_path = _SNAPSHOTS / 'ledger.jsonl'
    if not ledger_path.exists():
        sys.exit(f"ERROR: ledger not found at {ledger_path}")
    entries = []
    with open(ledger_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    if not entries:
        sys.exit("ERROR: ledger is empty — nothing to load")
    return entries


def resolve_max_n_overlay(snapshot_id):
    """Resolve the highest-numbered scrub-vN overlay dir for a snapshot, return its
    records.ndjson path + the scrub version int. Same logic as the pipeline's proven
    _build_seen_set: iterdir + fullmatch(scrub-v\\d+) + integer-max."""
    snap_dir = _SNAPSHOTS / snapshot_id
    if not snap_dir.exists():
        sys.exit(f"ERROR: snapshot dir not found: {snap_dir}")
    scrub_dirs = sorted(
        [p for p in snap_dir.iterdir()
         if p.is_dir() and re.fullmatch(r'scrub-v\d+', p.name)],
        key=lambda p: int(p.name[len('scrub-v'):]),
    )
    if not scrub_dirs:
        sys.exit(f"ERROR: no scrub-v* overlay under {snap_dir} — floor integrity failure")
    chosen = scrub_dirs[-1]
    scrub_version = int(chosen.name[len('scrub-v'):])
    records_path = chosen / 'records.ndjson'
    if not records_path.exists():
        sys.exit(f"ERROR: records.ndjson not found at {records_path}")
    return records_path, scrub_version


def load_records(records_path):
    """Parse a snapshot's records.ndjson into (headers, messages) lists.
    Headers = records without a msg_uuid; messages = records with one."""
    headers, messages = [], []
    with open(records_path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec.get('record_type') == 'conversation_header' or 'msg_uuid' not in rec:
                headers.append(rec)
            else:
                messages.append(rec)
    return headers, messages


def _batched(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


# --- main -------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description='apparatus production floor LOAD (S22)')
    ap.add_argument('--dry-run', action='store_true',
                    help='Resolve overlays + count records; connect read-only; write NOTHING')
    ap.add_argument('--execute', action='store_true',
                    help='Perform the real single-transaction load + hardening install')
    args = ap.parse_args()

    if not args.dry_run and not args.execute:
        sys.exit("ERROR: supply --dry-run (report only) or --execute (real load)")
    if args.dry_run and args.execute:
        sys.exit("ERROR: pick one of --dry-run / --execute")

    # --- Resolve what we will load, from the ledger, before any DB work -----
    print("=== apparatus production floor LOAD (S22) ===\n")
    ledger = read_ledger()
    print(f"Ledger: {len(ledger)} snapshot(s)\n")

    plan = []   # list of (snapshot_id, type, records_path, scrub_version, headers, messages)
    total_h = total_m = 0
    for entry in ledger:
        sid = entry['snapshot_id']
        stype = entry.get('type', '?')
        rpath, sver = resolve_max_n_overlay(sid)
        headers, messages = load_records(rpath)
        total_h += len(headers)
        total_m += len(messages)
        plan.append((sid, stype, rpath, sver, headers, messages))
        print(f"  {sid}")
        print(f"    type           : {stype}")
        print(f"    overlay        : scrub-v{sver}  (max-N)")
        print(f"    records source : {rpath}")
        print(f"    headers        : {len(headers)}")
        print(f"    messages       : {len(messages)}")
        print()

    print(f"TOTAL TO LOAD: {total_h} headers + {total_m} messages = {total_h + total_m} records\n")

    # --- PRE-FLIGHT GATE: no-orphans, proven on the plan before any DB work -----
    # The cross-table FK was dropped in v1.1 (see ANCHOR FK RESOLVED). Referential
    # integrity is proven at the gate, not in the schema — same stance as the message
    # tree's parent_uuid (D9). This is the PRIMARY gate: the plan in memory is the whole
    # intended floor (both snapshots resolved), so this is the most faithful place to
    # prove "every message's conv has a header somewhere on the floor." Conv-LEVEL,
    # not snapshot-scoped: a message's conv needs SOME header anywhere on the floor.
    header_convs = {r['conv_uuid'] for _, _, _, _, headers, _ in plan for r in headers}
    message_convs = {r['conv_uuid'] for _, _, _, _, _, messages in plan for r in messages}
    orphan_convs = sorted(message_convs - header_convs)
    if orphan_convs:
        sys.exit(
            f"ERROR (pre-flight): source ndjson has messages whose conv_uuid has no "
            f"header on the planned floor — {len(orphan_convs)} orphaned conv(s): "
            f"{orphan_convs}. Nothing was written; no DB connection opened."
        )
    print(f"PRE-FLIGHT: no-orphans OK — all {len(message_convs)} message convs have a header on the planned floor.\n")

    db_url = read_db_url()
    if not db_url:
        sys.exit("ERROR: SUPABASE_DB_URL not found (pipeline/secrets/.env or shell env)")

    # =======================================================================
    # DRY RUN — connect, confirm bare schema, write nothing
    # =======================================================================
    if args.dry_run:
        print("--- DRY RUN: connecting read-only to confirm target state ---")
        with psycopg.connect(db_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT current_user")
                whoami = cur.fetchone()[0]
                cur.execute(
                    "SELECT tablename FROM pg_tables "
                    "WHERE tablename IN ('floor_conv_headers','floor_conv_messages')"
                )
                existing = [r[0] for r in cur.fetchall()]
            conn.rollback()   # touch nothing
        print(f"  connected as       : {whoami}")
        print(f"  floor tables now   : {existing if existing else 'NONE (bare schema)'}")
        if existing:
            print("  NOTE: tables already exist — --execute will refuse unless they are bare.")
        print("\n[DRY RUN] No writes performed. Re-run with --execute to load for real.")
        return

    # =======================================================================
    # EXECUTE — single transaction: CREATE → load both → harden → commit
    # =======================================================================
    print("--- EXECUTE: single-transaction load ---")
    # psycopg3: the connection context manager commits on clean exit, rolls back on
    # exception. We do NOT commit mid-stream — the whole thing is one transaction.
    with psycopg.connect(db_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT current_user")
            owner_role = cur.fetchone()[0]
            print(f"  connected as: {owner_role}")

            # Refuse if floor tables already hold data — never load onto a live floor.
            cur.execute(
                "SELECT tablename FROM pg_tables "
                "WHERE tablename IN ('floor_conv_headers','floor_conv_messages')"
            )
            if cur.fetchall():
                conn.rollback()
                sys.exit(
                    "ERROR: floor tables already exist. LOAD refuses to run onto an existing "
                    "floor. Drop to bare schema first (deliberate, logged) — then re-run."
                )

            # 1) CREATE tables (no guards yet — guards installed after data lands)
            print("  [1/4] CREATE tables (drop-if-exists guard fn first, then tables)...")
            for stmt in _DDL_DROP:
                cur.execute(stmt)
            cur.execute(_DDL_HEADERS)
            cur.execute(_DDL_MESSAGES)

            # 2) LOAD — headers first, then messages. Header-first is no longer
            # DB-enforced (cross-table FK dropped v1.1); kept because it matches the
            # gate's mental model — headers define the convs, messages attach to them —
            # and keeps the load order legible.
            print("  [2/4] Load headers (all snapshots), then messages (headers-first)...")
            ins_h = ins_m = 0
            for sid, stype, rpath, sver, headers, messages in plan:
                for chunk in _batched([hdr_params(r) for r in headers], BATCH_SIZE):
                    cur.executemany(_SQL_INS_HDR, chunk)
                    ins_h += len(chunk)
            for sid, stype, rpath, sver, headers, messages in plan:
                for chunk in _batched([msg_params(r) for r in messages], BATCH_SIZE):
                    cur.executemany(_SQL_INS_MSG, chunk)
                    ins_m += len(chunk)
                    print(f"      messages: {ins_m:,}", end='\r')
            print(f"\n      loaded {ins_h} headers + {ins_m} messages")

            # 3) HARDEN — guard fn + triggers + REVOKEs (same transaction)
            print("  [3/4] Install append-only hardening (guard fn + triggers + REVOKEs)...")
            cur.execute(_DDL_GUARD_FN)
            for stmt in _DDL_TRIGGERS:
                cur.execute(stmt)
            for stmt in _DDL_REVOKES:
                cur.execute(stmt)

            # 4) In-transaction sanity: counts match the plan before we commit
            print("  [4/4] Pre-commit count check...")
            cur.execute("SELECT COUNT(*) FROM floor_conv_headers")
            db_h = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM floor_conv_messages")
            db_m = cur.fetchone()[0]
            if db_h != total_h or db_m != total_m:
                conn.rollback()
                sys.exit(
                    f"ERROR: pre-commit count mismatch — DB {db_h}h/{db_m}m vs "
                    f"plan {total_h}h/{total_m}m. Rolled back. Floor untouched."
                )
            # Belt-and-suspenders re-prove: the pre-flight gate already proved the SOURCE
            # is orphan-free; this proves the WRITE matched that validated plan. If the
            # pre-flight passed and THIS fails, the bug is in the insert path, not the source.
            cur.execute(
                "SELECT COUNT(DISTINCT m.conv_uuid) FROM floor_conv_messages m "
                "WHERE NOT EXISTS (SELECT 1 FROM floor_conv_headers h "
                "WHERE h.conv_uuid = m.conv_uuid)"
            )
            db_orphans = cur.fetchone()[0]
            if db_orphans:
                conn.rollback()
                sys.exit(
                    f"ERROR: post-insert DB orphan-check failed — {db_orphans} message "
                    f"conv(s) have no header in the DB. The write did not match the "
                    f"validated plan. Rolled back. Floor untouched."
                )
            print(f"      DB has {db_h} headers + {db_m} messages — matches plan.")
            print(f"      orphan re-prove: 0 message convs without a header — write matches plan.")
        # clean exit of the `with conn` block commits the whole transaction here
    print("  COMMITTED. Floor is laid.\n")

    # =======================================================================
    # POST-COMMIT PROOF — append-only enforced as OWNER (closes TRUNCATE ambiguity)
    # =======================================================================
    print("--- POST-COMMIT: re-prove append-only as owner ---")
    with psycopg.connect(db_url) as conn:
        # Attempt a DELETE as the connected (owner) role — must be REJECTED by trigger.
        delete_rejected = False
        try:
            with conn.cursor() as cur:
                # Real-row DELETE: WHERE false matches 0 rows, so a BEFORE-ROW trigger
                # never fires and the probe self-passes (the S23 false negative). Target
                # one real row via ctid so the immutable guard actually fires. The whole
                # probe is rolled back — the floor is never mutated.
                cur.execute(
                    "DELETE FROM floor_conv_messages "
                    "WHERE ctid IN (SELECT ctid FROM floor_conv_messages LIMIT 1)"
                )
            conn.rollback()
            print("  *** WARNING: real-row DELETE as owner was NOT rejected — append-only NOT enforced ***")
        except psycopg.errors.Error as e:
            delete_rejected = True
            conn.rollback()
            print(f"  DELETE as owner rejected (expected): {type(e).__name__} — {str(e).splitlines()[0]}")

        with conn.cursor() as cur:
            cur.execute("SELECT current_user")
            who = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM floor_conv_headers")
            fh = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM floor_conv_messages")
            fm = cur.fetchone()[0]
            cur.execute(
                "SELECT snapshot_id, COUNT(*) FROM floor_conv_messages "
                "GROUP BY snapshot_id ORDER BY snapshot_id"
            )
            by_snap = cur.fetchall()
        conn.rollback()

    print(f"  role                : {who}")
    print(f"  append-only (owner) : {'ENFORCED' if delete_rejected else '*** NOT ENFORCED ***'}")
    print(f"  floor headers       : {fh}")
    print(f"  floor messages      : {fm}")
    print(f"  by snapshot         :")
    for sid, cnt in by_snap:
        print(f"      {sid}: {cnt}")

    ok = delete_rejected and fh == total_h and fm == total_m
    print()
    print("=" * 60)
    print(f"LOAD RESULT: {'FLOOR LAID + APPEND-ONLY ENFORCED' if ok else '*** REVIEW — see above ***'}")
    print("=" * 60)
    if not ok:
        sys.exit(1)


if __name__ == '__main__':
    main()
