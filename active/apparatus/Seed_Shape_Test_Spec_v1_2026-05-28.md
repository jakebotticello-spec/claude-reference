# Seed-Shape Test — the D9 substrate-lock gate

*file: Seed_Shape_Test_Spec_v1_2026-05-28.md · v1.1 · apparatus S15 (authored) · S16 (check-④ corrected) · 2026-05-28 / corrected 2026-05-29*
*authority: locks the test that gates the D9 substrate lock. Grounded on Substrate_FaceOff_v2 §8 (recommendation), §10.1 (seed-shape), §13 (don't-lock-on-the-doc-alone), and the store-agnostic acceptance contract (ANCHOR NEXT MOVE #4). NOT the lock itself — the gate the lock rides on.*
*S16 status: this gate was EXECUTED and PASSED on Supabase; D9 is LOCKED. See the close note. Retained as the gate's record.*

---

## 1. Purpose

The substrate lock (D9) is **append-only ⇒ immortal**: a wrong store choice cannot be edited out, only superseded at cost. FaceOff_v2 proved the *storage primitive* is sound on both leads (NornicDB empirically at 1.37× max record across a cold reboot; Supabase by Postgres's nature). It explicitly does **NOT** substitute for ingesting the real archive at scale (§13). **This test is the only fully honest verdict.** Lock on this, not on the doc alone.

## 2. Fixture (the real archive, not a synthetic string)

- **Primary fixture: the baseline `records.ndjson`** — 23,095 records (294 conv headers + 22,801 message records) from the sealed `baseline-2026-05-25-ae015455`. It already exists on the pipeline box, it is the real projected floor, and it **includes the 3.0 MB max record** (`tool_result.content[].text`) + the 9 multi-root convs + the 304 root-position records. This is the honest at-scale fixture and it needs no new build.
  - ⚑ **Confirm it's on the box at S16 boot** (local snapshot artifact, gitignored, not in repo). If it isn't, the v1.3 delta build produces a fresh `records.ndjson` — but the baseline is the bigger/honester fixture, so prefer it.
  - *(S16 note: confirmed on box at `…/baseline-2026-05-25-ae015455/scrub-v1/records.ndjson`, 367,494,497 B; 9/9 fixture-shape pre-check PASS. Canonical path is the `scrub-v1/` subdir, not the snapshot root — root holds the transient `raw.json` + companion artifacts.)*
- **Secondary (optional): the 1,337-msg 5-28 delta**, once the v1.3 build emits it. Adds cross-export records but the baseline alone satisfies the gate.

## 3. What to run it against

Per FaceOff_v2 §8, both leads pass both gates; the lock is fidelity-vs-ops:
- **Supabase + pgvector** — the recommended first lock (lowest ops, already in stack, native seam). Run the seed-shape on it first.
- **NornicDB** — run it too **only if** Jake wants graph-native fidelity *now* (otherwise it's the proven upgrade path, adoptable later without re-opening storage integrity — the round-trip proof + dual seam connectors are why). Decision is Jake's (D9).
- Minimum to lock: the seed-shape PASSES on the lead being locked. If running both to compare, same contract on each.
- *(S16 result: Supabase was the pick; seed-shape PASSED 4/4 on it; D9 LOCKED on Supabase. NornicDB remains the proven upgrade path.)*

## 4. Acceptance contract (all five must PASS on the lead being locked)

1. **Ingests clean** — all 23,095 records load; zero parse errors, zero oversize rejects (the 3.0 MB record lands; binding ceiling is ~16 MiB on NornicDB, none on Postgres-scale text).
2. **Pointer resolves to exactly one** — `(snapshot_id, conv_uuid, msg_uuid)` → exactly one record; no collisions across the 22,801 message records (uuid global-uniqueness already CONFIRMED at population; this verifies the *store* enforces it).
3. **Byte-identical round-trip at scale** — read back the 3.0 MB max record + a random sample (≥50 records spanning sizes); sha256/byte-diff each against the source `records.ndjson` line. The lab proved a synthetic adversarial string; this re-proves it on the **real** archive.
   - **Fidelity-comparison method (S16, load-bearing):** the correct comparison is **value-identity, not byte-identity, for JSONB-backed fields.** Postgres JSONB canonically reorders object keys (alphabetical) and strips insignificant whitespace — so a stored `content_blocks` will not be byte-equal to its source line, but carries **zero value loss.** Compare: arrays **order-sensitive** (sequence is meaningful), JSON objects **order-insensitive** (key order is not). TEXT columns and timestamps stored as `text` ARE byte-verbatim. See the corrected fidelity language in §6 / the lock artifact.
4. **Tree-or-forest preserved** — reconstruct the parent chain from `parent_message_uuid`; the 9 multi-root convs reconstruct as forests (`is_root` honored, no orphaned/misparented nodes); spot-check 3 of the 9 multi-root convs explicitly.
   - **ROOT MARKER — CORRECTED S16 (was wrong as authored).** This spec originally said roots resolve as roots via `parent_message_uuid` **null**. That is **FALSE** against the real floor: **zero** records have a null parent. Roots carry the sentinel UUID `00000000-0000-4000-8000-000000000000` (a valid-format UUID — NOT the all-zeros nil UUID). Verified across all 22,801 message records (S16 type-recon + full-file scan). The reconstruction test identifies roots by **parent == sentinel**, not parent == null; the sentinel-parent count must equal the `is_root=true` count (304) — proves the marker is exclusive (all roots carry it, no non-root does). *(Original null-root assumption was an authoring error, caught against the disk by CC at S16 — disk-over-directive working as designed.)*
5. **Query at scale** — pointer-retrieval latency acceptable across 23,095 records; **if vectors are in play, the Supabase-specific branch-aware recall check** (FaceOff_v2 §10.5: do embeddings get confused by interleaved branches?) — only required if Supabase advances with vector recall.
   - *(S16: DEFERRED by decision. The D9 lock is storage-integrity only; embeddings/pgvector are a retrieval-layer concern, out-of-gate per §7 + FaceOff §11. Logged as the first retrieval-layer verification, target = the 9 forests, NOT dropped. pgvector is NOT installed on the locked floor.)*

## 5. Discipline at lock (load-bearing, per merge-back §6)

- **Blind re-read before committing the lock.** Append-only makes a wrong lock immortal; the three-AI-council / cross-read discipline is load-bearing for any substrate-altering call. Run the lock decision the same way the dual-gate ran — a fresh read before the commit, not a rubber-stamp of this test's own PASS.
  - *(S16: done. OC blind-re-read the harness manifest cold (evidence reconciled independently — forest subtree sizes summed to message counts, ② and ④ passed for the right reasons not just by count), THEN a `/jedi-council` adversarial panel ran with live DB access. Verdict LOCK-WITH-CAVEATS 6/10, zero P0, one P1 (append-only unenforced) + 5 caveats — ALL remediated with proof before the lock. See `harness/D9_LOCK_2026-05-29.md`.)*
- **If NornicDB is the pick: D20 is a HARD config gate at lock** — pin `decay` / `TTL` / `auto_links` / `embeddings` OFF. The code default is safe, but the shipped `nornicdb.example.yaml` enables all three; a copy-paste deploy runs a decay worker against frozen nodes. Verify the running config, not the example. *(N/A at S16 — Supabase was the pick. Stands if NornicDB is ever adopted as the proven upgrade path.)*
- **test-host ≠ deploy-host** (FaceOff_v2 §13). "Ran the seed-shape on box X" is not "deploys on box X." Decide the deploy target deliberately. *(S16: the gate ran against the live deploy target — a dedicated Supabase project `apparatus-floor`, SB Pro tier, separate from Cypher's project. Deliberate.)*

## 6. Decision rule (what a PASS means)

- Seed-shape PASSES on Supabase → lock Supabase (the §8 lower-regret default), NornicDB stays the proven upgrade path. **Unless** Jake names a reason to prefer graph-native fidelity now → run + lock NornicDB instead.
- Seed-shape FAILS on a lead → that lead is out for now; the other lead is the lock candidate (re-run the contract on it). A double-fail re-opens the field (not expected — both passed the dual-gate).
- The lock, once committed, lands in the anchor as a Settled Invariant + closes D9.
- *(S16 OUTCOME: PASSED on Supabase → Supabase LOCKED → D9 CLOSED, enshrined in ANCHOR v10. NornicDB is the proven upgrade path.)*

## 7. Out of scope (don't let the seed-shape creep)

Retrieval-interface design, embedding choice (if Supabase), per-project anchor passes, index design — all substrate-specific and **after** the lock. The three escalations (recall / kept / shared-memory) feed the *retrieval* layer, not this gate, and stay blocked on Jake's uploads. This test answers exactly one question: **does the real floor ingest, resolve, round-trip, and reconstruct at scale on the lead being locked.**

---
*Locked S15 as the D9 gate. Run it in S16 (or later) against the baseline `records.ndjson`; PASS + blind-re-read → lock the substrate → close D9. Apparatus is unparked; this is the last gate before the floor gets a permanent home.*
*S16 (2026-05-29): gate EXECUTED on Supabase, PASSED 4/4 (① ingest 23,095 / ② store-enforced pointer uniqueness + UniqueViolation / ③ value-identity round-trip incl. the 2.93 MB max record / ④ 9/9 forests, sentinel-parent 304/304, zero orphans). Blind-re-read + /jedi-council adversarial review + 6 caveats remediated with proof → **D9 LOCKED on Supabase.** check-④ null→sentinel correction folded in (v1→v1.1). This spec is now the historical record of the gate that the lock rode on.*
