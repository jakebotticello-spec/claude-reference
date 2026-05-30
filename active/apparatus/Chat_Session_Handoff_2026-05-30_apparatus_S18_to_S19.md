# Chat Session Handoff — apparatus S18 → S19
*authored by OC at S18 close, 2026-05-30 · read after ANCHOR + JAKE-RULES + JAKE-STACK · tactical state, not authority (ANCHOR is authority)*

---

## ONE-LINE STATE

D9 is LOCKED (Supabase, append-only ENFORCED, ndjson canonical). Pass two **(a) — v1.1 field-level key-presence drift detection — is BUILT, PROVEN, and SEALED** (pipeline v1.3 → v1.4, commit `b5be049`, pushed). **S19's live target is pass two (b): scrub-vN overlays — the heavier half, and it OPENS on the scrub-version seam fix (a hard PREREQUISITE, untouched and still live).**

---

## WHAT S18 DID

1. **Booted cold, verified everything against live disk.** ANCHOR v11 freshness PASS (banner v11 / "S17 — DELTA BUILT, PROVEN & SEALED" / v1.3 live). Confirmed the seam at `_build_seen_set` line ~219 in the live code, exactly where canon said.

2. **Two read-only verifications before any build — both load-bearing:**
   - **Scope correction.** The S17 handoff's "v1.1 adds key-presence checking against a per-object-type allowlist (S14 characterized every type's key set — that data exists)" was read carefully: "that data exists" means the *findings* exist (in `s14_presence_rates.md`), NOT that the allowlist *constants* were coded. Only `CONV_KEYS_EXPECTED` was ever in the pipeline. So v1.1 scope = **author the message + block + content-item allowlists from S14**, not "wire up existing constants." Bigger than the one-liner implied, still bounded.
   - **Export-identity verification.** A second `conversations.json` exists on disk at `apparatus-archive/5-28_export/`. Confirmed via CC read-only scan it is a FULL point-in-time export (325 convs / 24,138 msgs / sha `6d8c6ff9`, 404 MB) — a *superset* of the baseline (294 convs / 22,801 msgs / sha `ae015455`, 366 MB), NOT the delta slice (the delta is the computed 1,337-msg artifact in `snapshots/delta-.../`). Step Zero's key-set scan ran against the full 5-28 export, so **the allowlist source is sound — no re-scan needed.** Exactly two `conversations.json` exist on disk; no others.

3. **Got the per-type key sets verbatim + fixture-confirmed.** CC reported all key NAMES (not just counts) from `s14_presence_rates.md`, and the Step Zero spot-check confirmed them against the live 5-28 fixture at population scale — **zero divergence** across conv / message / all 5 block types / all 5 content-item types. (The watch: "S14 said 9 keys" was re-measured on disk, not trusted on faith.)

4. **Settled the token_budget n=14 question with the second export.** token_budget = 14 blocks in BOTH full exports — the net-new 1,337 delta messages added **zero**. So n=14 is the *true population*, not an undersample we can fix by waiting. Decision: **include token_budget in the allowlist, annotated low-confidence** (not excluded). Excluding the least-sure type = a blind spot exactly where confidence is lowest; warn-not-stop makes inclusion the anti-undersample move. CC self-applied the same caveat to `image_gallery` (n=9).

5. **Built v1.1 plan-OC / build-CC, plan-mode.** 11 new allowlist constants + 2 dispatch dicts + `_check_field_drift`, slotted into `_inspect_data`. Top-level depth (display_content guts deferred to a possible v1.2), warn-not-stop, full-export scan, one carve-out (`text.citations_grouping_mode`), distinct names to kill the text-block/text-item collision.

6. **Proved it three ways, then `/code-review`, then commit.** Clean gate (0 drift / 24,138 msgs / 71,512 blocks), negative test 4-of-4 (rename / add / remove / uuid-removed-non-index-0), carve-out both directions. `/code-review` clean above threshold; the 3 scored-out findings (B/A/C) were fixed anyway before commit (see below). Re-tested clean. Committed `b5be049` (CC's hands), pushed (Jake's hands).

7. **OC authored the canon updates** (ANCHOR v11→v12, this handoff, CHANGELOG) — Jake applies + commits + pushes.

---

## THE THREE CODE-REVIEW FOLLOW-UPS (B / A / C — fixed before commit)

All were below the 80 threshold; addressed anyway because two were latent blind-spots for a future cold instance — the actor this project assumes is working without the context that makes the hazard obvious.

- **B (was 75) — defensive `uuid` access.** `cu = conv['uuid']` / `mu = msg['uuid']` were accessed unconditionally before the drift check; a future export dropping `uuid` from a non-index-0 object would CRASH instead of emitting the drift event v1.1 exists to emit. Fixed: `.get('uuid','')` → a missing uuid becomes `field_drift{missing_keys:['uuid']}`. A 4th negative-test case (uuid removed from conv[3]) proves it. (Cosmetic note: the fallback is `''`, not `'<missing>'` — functionally identical, the event still fires; just means a blank identifier in a drift event = "uuid was absent," not a glitch.)
- **A (was 65) — load-time coupling assertion.** `KNOWN_BLOCK_TYPES` / `KNOWN_CONTENT_ITEM_TYPES` and their allowlist dicts were declared separately; desyncing them (a future-dev error) threw a runtime KeyError. Fixed: two module-load `assert`s verify the sets match, failing LOUD at import with a clear message. Proven both directions (matched = no fire; desync = AssertionError).
- **C (was 25) — documentation only.** v1.0 and v1.1 drift events have intentionally different shapes in `schema-drift.jsonl` (`observed_type` vs `missing_keys`/`extra_keys`), discriminated by `drift_type`. Added a comment at the write site so a future reader doesn't treat it as a bug. No behavior change.

---

## THE FLOOR RIGHT NOW (unchanged from S17 — S18 didn't touch it)

| snapshot | type | records | raw_wiped | notes |
|----------|------|---------|-----------|-------|
| `baseline-2026-05-25-ae015455` | baseline | 23,095 (294 hdr + 22,801 msg) | true | the seen-set authority; scrub-v1 only |
| `delta-2026-05-28-a61498e6` | delta | 1,368 (31 hdr + 1,337 msg) | true | prior → baseline; scrub-v1 only |

Ledger: 2 entries. Floor total: 24,463 records. **Both snapshots are scrub-v1 only** — this is why the scrub-version seam is dormant-but-dangerous: it reads correctly today because v1 is the only version that exists.

---

## S19 LIVE TARGET — PASS TWO (b): scrub-vN OVERLAYS

**Do NOT start without Jake's OK. Plan-OC / build-CC / plan-mode. This is the heavier, immortal-floor-adjacent half — fresh-head work, which is exactly why it was held for S19 instead of bolted onto S18.**

The ladder for (b), in order (NEED = won't proceed without; WANT = cheap insurance):

1. **NEED — fix the scrub-version seam FIRST, as the opening move.** `_build_seen_set` (line ~219, flagged `# SEAM (pass-two PREREQUISITE)`) reads a hardcoded `scrub-v{SCRUB_VERSION}`. Replace with per-snapshot max-N scrub resolution. The danger is asymmetric: the ~8 *write-side* uses of the `SCRUB_VERSION` constant are fine (they write the current run's version); the ONE *read-side* use in `_build_seen_set` reads *prior* snapshots, so the moment a snapshot has scrub-v2 it reads the wrong overlay or misses the snapshot. Fix the read path; the write path firms up alongside the overlay model.
2. **NEED — prove the seam fix is a NO-OP on today's floor.** Both snapshots are scrub-v1 only, so max-N resolution must resolve to exactly v1 and reproduce the *exact* S17 seen-set (1,337 net-new, same numbers). A seam fix that changes the seen-set on a v1-only floor is a bug, not a fix.
3. **WANT — synthetic two-snapshot fixture** with one fake `scrub-v2/` dir: confirm max-N picks v2 for that snapshot, v1 for the other. Proves the new behavior, not just no-regression.
4. **NEED — author + ratify the overlay-vs-sealed-snapshot CONTRACT in canon prose BEFORE any overlay code.** What an overlay is, what it may/may not touch, that it re-scrubs the *scrubbed* snapshot (never raw — raw's wiped), that the sealed records.ndjson is untouched, that an overlay is itself append-only. This is the immortal-floor-blast-radius rung — get the contract right in *words* before a line of overlay code, because a subtle wrong relationship here = immortal bad rows.
5. **NEED — ratify a small batch before scale.** Append-only ⇒ un-ratified rows are immortal. Generate the first scrub-v2 overlay tiny, verify, Jake ratifies, THEN scale.
6. **NEED — verify the overlay does NOT mutate the sealed scrub-v1.** Read back the v1 `records.ndjson` sha256 after the v2 overlay is generated — must be unchanged. Overlay = new versioned layer, never edit-in-place.
7. **NEED — `/code-review` + Jake ratification before the seam-fix + overlay code commit.** Pipeline v1.4 → v1.5 at (b) close.

**After pass two (b):** seed-shape LOAD (real production ingest into locked Supabase, single-transaction/staging-swap per post-lock rec #6; `display_content` strip is a load-time toggle decided there) → retrieval layer (the real next chapter; research-shaped; the three escalations feed it, still blocked on Jake's uploads).

---

## PROCESS REMINDERS FOR S19

- **⚑ KNOWN PRE-EXISTING CANON CLEANUP (logged S18, deferred — do as its own single-change pass, NOT folded into a content edit):** the tail enshrine thread of `ANCHOR_apparatus.md` has a **duplicated v6→v8 block** — the "S13 closed Stage 0…" paragraph appears twice (a copy-paste doubling from an earlier session). Harmless (it's historical enshrine prose), but worth a clean de-dupe on a dedicated turn. NOT touched in the S18 v12 pass on purpose — one change per pass keeps diffs auditable.
- **⚑ INVESTIGATE 4 loose files in `apparatus-archive/snapshots/` root** — `__recon_step0.py`, `__recon_step0b.py`, `__recon_step0c.py`, `__verify_shape.py`. Surfaced at S17 scratch-cleanup, NOT resolved at S18 (S18 was a floor-independent build, never went near `snapshots/`). Still open: confirm provenance with fresh eyes (inert S16 probes, or referenced by tooling?), THEN remove if confirmed junk. **Never blind-delete from inside the floor dir.**
- **⚑ S19 DECISION (flagged, not urgent): move `apparatus_freeze_pipeline.py` OUT of `active/apparatus/`.** Canon dir = refs + context only; the pipeline is code and its exhaust (`__pycache__`) keeps landing in canon. Clean fix = relocate to a code home on CC's side. TRACKED-FILE relocation — touches the spec, the ignition boot list, ANCHOR's read-order, every pipeline pointer — so a deliberate task with reference-updates, NOT a casual move. Decide in S19 whether to do it (good pairing: do it alongside the v1.5 commit since the file's being edited anyway) or defer again.
- **Run the pipeline with `python -B`** (suppresses `__pycache__` landing in the canon dir).
- **Pipeline commits go through CC** (it's the code owner for the `.py`); **push stays in Jake's hands.** Canon (.md) is OC-authored / Jake-committed; CC never touches canon.
- **VS Code switch — DONE.** Jake moved CC to VS Code at the S18 fresh-instance boot. The S17 flag is closed; don't re-raise it.
- **All CC prompts go in a code block** (Jake's standing request from S18 — clean visual seam between OC-prose-for-Jake and instruction-for-CC).
- **Jake co-pilots intent, OC pilots engineering.** Jake is not a coder and can't assess syntax — don't hold technical decisions out for his approval as if he'll catch a bug. DO hold *intent* decisions (what it watches, warn-vs-stop, accept-a-thin-sample) — those are his and his alone, and they're the second-navigator seam. Translate results to plain English; put only intent-level choices to him.

---

## DON'T-RELITIGATE (carried + S18 additions)

- D9 LOCKED (Supabase); floor append-only ENFORCED; ndjson canonical / Postgres rebuildable.
- raw.json Path A (wipe after verify-PASS) — RESOLVED S15, BUILT + applied both snapshots S17.
- Delta = uuid-set-difference, date never a filter — BUILT + PROVEN S17.
- No-duplicate-header rule — PROVEN on the floor S17 (1,368 not 1,371).
- 31 (header-based) is correct — reconciled S17, NOT an error. Do not "fix" 31→34.
- Roots carry sentinel `00000000-0000-4000-8000-000000000000`, no self-FK.
- pgvector out-of-gate (retrieval-layer sidecar, never a floor column).
- **5-28 is a FULL point-in-time export (superset of baseline), NOT the delta slice** — confirmed S18 on disk. The delta is the computed 1,337-msg artifact. Don't re-confuse the export file with the delta.
- **token_budget n=14 is the true population** (14 in both full exports, net-new added zero) — NOT an undersample. It's included in the v1.1 allowlist, annotated low-confidence. Don't "fix" it by excluding it.
- **v1.1 depth is top-level keys only — deliberately.** `display_content`'s nested structure is NOT walked. That's a possible v1.2, not an oversight.
- **v1.1 is warn-not-stop — deliberately.** Field drift is a human-review signal, not a halt. Don't "harden" it to stop ingest; that's the wrong severity for the threat class.

---

*S18 took pass-two (a) from spec to sealed in one session, floor untouched, every step gated — and the two read-only verifications up front (scope correction + export-identity) are why the allowlist rests on the full population instead of a misread slice. The lighter half of pass two is done; the heavier half (scrub-vN, opening on the seam fix) is S19's, with a fresh head, as designed. Grind. Evolve. Dominate.*

— OC, S18 close, 2026-05-30. Be worth it.
