# Chat Session Handoff — apparatus S17 → S18
*authored by OC at S17 close, 2026-05-29 · read after ANCHOR + JAKE-RULES + JAKE-STACK · tactical state, not authority (ANCHOR is authority)*

---

## ONE-LINE STATE

D9 is LOCKED (Supabase, append-only ENFORCED, ndjson canonical). **The v1.3 delta + raw.json wipe is BUILT, PROVEN, and SEALED** (`delta-2026-05-28-a61498e6`, commit `43306fa`, pushed). The floor holds two snapshots. **S18's live target is pass two: v1.1 field-drift (bounded) + scrub-vN overlays (heavier — opens on the scrub-version seam PREREQUISITE).**

---

## WHAT S17 DID

1. **Booted cold, verified everything against live disk.** ANCHOR v10 freshness PASS. Re-verified the baseline records.ndjson as the seen-set authority (23,095 lines, 22,801 distinct msg_uuid, 0 unparseable, byte size matches the D9 fingerprint). Hand-computed the delta against the sealed baseline BEFORE scripting: 1,337 net-new, 141 appended, 1,196 brand-new, 0 vanished.

2. **Built v1.3 pass one in CC** (delta runs + raw.json wipe), plan-reviewed in OC first. Three review fixes landed before build: drift-detection runs on the FULL export not the slice (a real bug — a schema change on an untouched conv would've been invisible); `vanished > 0` hard-stops on a real run (warns on dry-run); the scrub-version seam flagged-not-built.

3. **Dry-run proved it, then `/code-review`, then the real seal.** All dry-run numbers PASS. Code review came back clean except H1 (below). Real run sealed `delta-2026-05-28-a61498e6`: all 7 post-seal checks PASS — 1,368 records (31 headers + 1,337 msgs; the no-dup-header rule proven on the floor), deterministic snapshot_id held, Stage 3 verify PASS, 38 live creds scrubbed (19 postgres / 19 RTSP), raw.json wiped + manifest `raw_wiped: true`, ledger gained exactly one delta entry (prior_snapshot_id → baseline), the two sha256s differ.

4. **Committed + pushed** `43306fa` (v1.3 + M1/M3 review cleanups folded in by CC — cosmetic, no logic change, fine). Working tree clean.

5. **Closed two H1-class items** (see below).

6. **OC authored the canon updates** (ANCHOR v11 change-set, this handoff, CHANGELOG) — Jake applies + commits + pushes.

---

## THE FLOOR RIGHT NOW

Two snapshots, append-only, both raw originals wiped:

| snapshot | type | records | raw_wiped | notes |
|----------|------|---------|-----------|-------|
| `baseline-2026-05-25-ae015455` | baseline | 23,095 (294 hdr + 22,801 msg) | true (S17 H1 backfill) | the seen-set authority |
| `delta-2026-05-28-a61498e6` | delta | 1,368 (31 hdr + 1,337 msg) | true (auto, v1.3) | prior → baseline; 38 creds scrubbed |

Ledger: 2 entries. Floor total: 24,463 records across two snapshots.

---

## TWO H1-CLASS ITEMS CLOSED THIS SESSION

**H1 — baseline raw.json was never wiped.** The baseline was built under v1.2, before the wipe code existed, so its 366 MB unscrubbed cred-bearing original sat on disk since 5-25. Surfaced by `/code-review`. Remediated: verified baseline integrity first, wiped raw via `_wipe_raw`, confirmed records.ndjson still 23,095 after. Working tree now has zero unscrubbed-cred originals.

**NAS cold-copy disposition (carry this — future sessions need both halves):** Jake intentionally retains a verbatim copy of the baseline original on NASBackup (.248) — a known, deliberate copy (not a folder-backup side effect), held as project-lifetime recovery insurance because the export is point-in-time (a re-pull won't reconstruct since-deleted convs). **(1) It EXISTS for re-derivation recovery. (2) It is a PENDING-REMOVAL cred liability — Jake removes it at project end.** Deliberate carve-out from the S15 "never staged to NAS" line (which targeted automatic staging). Don't flag as a violation; do flag for removal at project end.

---

## S18 LIVE TARGET — PASS TWO (two pieces, unequal weight)

**Do NOT start without Jake's OK. Plan-OC / build-CC / plan-mode, as always.**

**(a) v1.1 field-level key-presence drift detection — BOUNDED, do this first.**
The v1.0 detector is type-level only — a new field in a future export passes silently. v1.1 adds key-presence checking against a per-object-type allowlist (S14 characterized every object type's key set at population scale — that data exists). The ONE carve-out: `text.citations_grouping_mode` (~0.1%, genuinely optional). Low-risk, floor-independent, testable against the 5-28 export which is known drift-zero (clean fixture). This is a tight, safe build.

**(b) scrub-vN overlays — HEAVIER, opens on a hard prerequisite.**
The model: sealed snapshots never re-scrub in place; a new scrub is a versioned overlay (`scrub-vN/`). Two reasons this is the careful one:
- **PREREQUISITE — the scrub-version seam.** `_build_seen_set` reads a hardcoded `scrub-v{SCRUB_VERSION}` (correct today, only v1 exists). It MUST become per-snapshot max-N resolution BEFORE any scrub-v2 is generated, or the seen-set silently reads the wrong overlay / misses snapshots. Flagged in the code (`# SEAM (pass-two PREREQUISITE)` in `_build_seen_set`) and in the ANCHOR seen-set invariant. **Fix this seam as the opening move of the scrub-vN work.**
- **Immortal-floor blast radius.** Get the overlay-vs-sealed-snapshot relationship subtly wrong on an append-only floor and you've got immortal bad rows. Fresh-head work.

**After pass two:** seed-shape LOAD (real production ingest into locked Supabase, single-transaction/staging-swap per post-lock rec #6, `display_content` strip is a load-time toggle decided there) → retrieval layer (the real next chapter; research-shaped; the three escalations feed it, blocked on Jake's uploads).

---

## PROCESS REMINDERS FOR S18

- **⚑ SWITCH CC TO VS CODE at the next fresh CC instance.** Jake flagged this S17 — raise it at S18 boot so it doesn't slip.
- **⚑ INVESTIGATE 4 loose files in `apparatus-archive/snapshots/` root** — `__recon_step0.py`, `__recon_step0b.py`, `__recon_step0c.py`, `__verify_shape.py`. Surfaced during S17 scratch-cleanup; they look like misplaced S16 harness probes sitting loose IN the floor directory. NOT deleted in S17 on purpose — nothing inside `snapshots/` gets removed on a casual cleanup. S18: confirm provenance (are they inert S16 scratch, or referenced by any tooling?) with fresh eyes, THEN remove if confirmed junk. Do not blind-delete from inside the floor dir.
- **Run the pipeline with `python -B`** (e.g. `python -B active/apparatus/apparatus_freeze_pipeline.py --export-dir ...`). The `-B` suppresses `__pycache__`/`.pyc` writes — without it, running the pipeline drops a `__pycache__/` into `active/apparatus/` (the canon dir), which S17 had to clean up. `-B` keeps the canon shelf clean; the pyc cache buys nothing for an occasional hand-run against a 400MB load.
- **⚑ S18 DECISION (flagged, not urgent): move `apparatus_freeze_pipeline.py` OUT of `active/apparatus/`.** The canon dir is meant for refs + context only; the pipeline is *code* and its exhaust (the `__pycache__` above) keeps landing in canon because the source lives there. The clean fix is relocating the `.py` to a code home on CC's side (alongside `apparatus-archive` / `apparatus-scratch`). This is a TRACKED-FILE relocation — touches the spec, the ignition boot list, ANCHOR's read-order, and every `read apparatus/apparatus_freeze_pipeline.py` pointer — so it's a deliberate task with reference-updates, NOT a casual move. If done, it also makes the `-B` habit moot (pyc would land on CC's side, harmlessly). Decide in S18 whether to do it now or defer.
- **Pipeline commits go through CC** (it's the code owner for the `.py`); **push stays in Jake's hands.** Canon (.md) is OC-authored / Jake-committed; CC never touches canon.
- **31 vs 34 — DO NOT "fix."** Canon's "31 wholly-new convs" is CORRECT (header-based). A transient "34" appeared mid-S17 from a message-based count (against 291 message-bearing baseline convs instead of 294 header-bearing). The 3-conv gap = the 3 empty-baseline convs getting first messages = appended, not new = part of the 141. Same reality, two lenses. If a future session "corrects" 31→34, it's re-introducing the error.
- **Records-as-seen-set-authority is proven** — the sealed records.ndjson is the durable authority; any uuids.txt cache is convenience only. Rebuild from records if the cache is missing.
- **Standard working rules hold:** trust disk over directive; flag stale pointers turn-one; WAIT for OK before building; prose questions not the widget; never search past chats for code (ask Jake / read via codeload); re-anchor ~every 5 turns; timestamps via bash `date`; status line each reply.

---

## DON'T-RELITIGATE (carried + S17 additions)

- D9 LOCKED (Supabase); floor append-only ENFORCED; ndjson canonical / Postgres rebuildable.
- raw.json Path A (wipe after verify-PASS) — RESOLVED S15, now BUILT + applied to both snapshots S17.
- Delta = uuid-set-difference, date never a filter — BUILT + PROVEN S17.
- No-duplicate-header rule — PROVEN on the floor S17 (1,368 not 1,371).
- 31 (header-based) is correct — reconciled S17, not an error.
- Roots carry sentinel `00000000-0000-4000-8000-000000000000`, no self-FK.
- pgvector out-of-gate (retrieval-layer sidecar, never a floor column).

---

*S17 took the delta from UNBUILT to SEALED in one session, every step gated. The discipline held: verify against disk, plan before build, dry-run before real, review before seal. The floor grew by one honest snapshot and lost two cred liabilities. Pass two is the last of the v1.3 spec — then LOAD, then retrieval. Grind. Evolve. Dominate.*

— OC, S17 close, 2026-05-29. Be worth it.
