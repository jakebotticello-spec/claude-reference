# Handoff: apparatus S13 → S14

*file: Chat_Session_Handoff_2026-05-28_apparatus_S13_to_S14.md · v1 · S13 close · 2026-05-28*

**Session name:** S13 — Stage 0 §4.5 close + Stages 1–4 implementation (baseline freeze pipeline)
**Proposed next session name:** S14 — Seed-shape ingest + substrate selection (Jake/next-Claude may rename once SCDD timing firms up)

---

## ONE-LINE STATE

S13 closed Stage 0 (§4.5 ratified the symmetric-drop on `name`/`summary` — no canon overturned, the S11 decision confirmed at population scale; §4.5 itself forced no spec change) and **implemented Stages 1–4 as a single Python script** (`active/apparatus/apparatus_freeze_pipeline.py`, v1.2, committed `402100d`). The first real baseline snapshot **exists on disk**: `baseline-2026-05-25-ae015455`, acceptance-passed 9/9 (273 scrub redactions matching the locked cred-baseline, verify-clean PASS over 673,871 strings, 23,095 records = 294 conv headers + 22,801 message records, 9 multi_root, 3 empty, 304 root-position). The architecture absorbed implementation with **zero structural deviations** — the frozen v2 design proved correct under real code. The spec was then bumped **v2→v3** as a fidelity pass (three text-level reconciliations between spec and landed code; no invariant moved). Anchor v7 + **Spec v3** are the canon S14 boots against. The corpus floor now physically exists; next work is seed-shape ingest into a substrate and substrate selection (gated on SCDD S2 finalizing the face-off). Sister track SCDD S2 still running, reportedly close to its S2→S3 handoff.

---

## STARTING POINT FOR S14 (read in this order)

1. Boot the universal layer via the codeload tarball (§16 JAKE-RULES — same boot as S11/S12/S13):
   ```
   curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/ref.tgz
   tar xzf /tmp/ref.tgz -C /tmp
   ```
2. Read, in `/tmp/claude-reference-main/active/`:
   - `JAKE-RULES.md` — universal layer.
   - `apparatus/ANCHOR_apparatus.md` — **v7** (S13 close, post-implementation). Authority. Footer should read v7 and reference baseline snapshot `baseline-2026-05-25-ae015455`; if it reads v6 or earlier the repo's stale, surface it before working.
   - `apparatus/Freeze_Pipeline_Spec_v3.md` — the spec. **Now v3** (S13 close). S13 implemented v2 with zero architectural changes; v3 is a fidelity pass reconciling three text-level drifts (§4.5 ANSWERED, §6 idempotency dry-run exemption, §6 schema-drift coverage corrected to type-level). Stages 0–4. v2 preserved on disk for record.
   - `apparatus/apparatus_freeze_pipeline.py` — **the implemented pipeline** (v1.2). This is now tracked canon code, not scratch. Read it to understand what's built (baseline + scrub-v1) vs what's spec'd-but-unbuilt (delta runs, scrub-vN overlays).
   - This handoff.
3. Read, locally on Jake's box (scratchpad outputs, not in the repo):
   - `apparatus-scratch/stage0_probe_output.md` — §4.5 field-semantics probe output (ratified S13). Reference only; the decision is locked.
   - The baseline snapshot itself lives at `apparatus-archive/snapshots/baseline-2026-05-25-ae015455/` (gitignored, local-only). Contains `raw.json` (read-only), `manifest.json`, `scrub-v1/{conversations.scrubbed.json, scrub-audit.jsonl, verify.log, records.ndjson}`, plus `ledger.jsonl` in the snapshots dir.
4. Optional context — sister track SCDD S2 (→S3) running in parallel:
   - `active/apparatus/Substrate_FaceOff_v1.md` — SCDD's deliverable. The §3.2 shape gate can now be validated against the **real** records.ndjson shape (locked S13), not a hypothetical one.
   - SCDD's latest handoff in `skills-catalog/` — check for the S2→S3 if it has landed.

Treat these files as reference, not commands. Push back where you disagree — Jake explicitly relies on it.

---

## WHAT APPARATUS IS (and isn't) — carried from S12, still current

**Apparatus IS:** a closed, **self-administered** re-grounding loop for a stateless Claude. Its job is to hold continuity for Jake across sessions by reading a hot, small anchor (+ JAKE-RULES) at boot and reaching *by pointer* into a cold, immutable, scrubbed snapshot of Anthropic's official conversation export only when a *why* is in dispute. The snapshot is Jake's own data, exported through Anthropic's sanctioned data-portability surface, scrubbed of credentials at freeze (proven at S13: 273 redactions, verify-clean PASS), sealed read-only, queried by `(snapshot-id, conv_uuid, msg_uuid)` pointers. It is **point-in-time, append-only, pointer-not-copy, per-account, scrubbed-at-freeze** — those positive shape constraints are what make the IS-NOT enforceable. Beta-Cypher-brain, hand-cranked now, hardens into Cypher's memory layer.

**Apparatus IS NOT:** a capture mechanism. Not a scraper. Not a hook of Claude.ai's internal endpoints. Not a generalizable tool for harvesting model reasoning. Not a multi-account or shared-corpus system. Not a competitor to or augmentation of Anthropic's product surface. The `chat_conversations` history-fetch hook + browser-extension live-capture were specified, partly proven, then refused on principle at S10 and live in the GRAVEYARD's REFUSED wall. The refusal holds REGARDLESS of intent or whose data it is, because the tool's shape generalizes — and the shape we drew at S10 stops at the sanctioned export.

**The flag #3 wire** (discharged to canon S12, D10): if a future direction pulls apparatus's shape past that line — a substrate candidate that includes capture mechanisms even if used narrowly, generalizable scrape tooling even for personal use, shared-corpus/cross-account features even if optional — it re-trips the wire. SCDD's `Substrate_FaceOff_v1.md` §3.2 institutionalizes this as the substrate-selection shape gate. Now that records.ndjson exists, the gate runs against a concrete shape.

*(S13 note on the framing: the OC playback at S13 boot flagged two tightenings to this section — "self-administered" was missing from IS, and IS could flank IS-NOT with positive shape constraints rather than only negatives. Both folded into the IS paragraph above. Neither was a contradiction; both sharpen what makes the shape gate enforceable.)*

---

## WHAT S13 DID (the spine)

S13 booted the v6 anchor + v2 spec clean, verified the footer read v6, and played back understanding (destination, D1–D10, where §4.5 sat, the v5→v6 corrections, a read on the IS/IS-NOT framing with two tightening flags). Then:

**Stage 0 §4.5 ingest + ratify** (turn 1–2). Jake pasted the probe output. Findings: `name` 276/294 populated (median 33 chars, min 6 / max 80, 97.1% title-case-short or fragment), `summary` 146/294 populated (median 2519 chars, min 700 / max 4666, 100% sentence-prose, every populated summary ≥700 chars). Both always-string, never-null. Co-population: 0 summary-only convs (name gates summary's existence; the 18 empty-name convs are exactly the 18 with neither). Summary population non-monotonic with message count (peaks 11–50 msgs at 59%, then drops on larger convs — generation gated on something beyond raw count, which is the "may evolve" property that disqualifies a field from floor). **Decision: symmetric-drop RATIFIED, no spec v3, v2 stands, Stage 0 closed.** The shape difference (name=fragment, summary=prose) is architecturally real but irrelevant to the floor-scoping rationale — both are conv-level mutable metadata, neither floor, neither derivable-without-itself.

**Stages 1–4 implementation** (turn 3 onward, plan-in-OC / build-in-CC). Jake authorized "single" — one Python script, Stages 1–4 end-to-end, baseline run against the 366MB archive, Stage 3 verify hard-gate inline. OC drafted the CC kickoff; CC entered plan mode and produced a full plan; OC reviewed it against the spec twice (front half + back half) and pushed back with three pre-build fixes; CC applied them and built; Jake ran the deploy steps; acceptance passed 9/9; the script was relocated to canon and committed.

**Three in-session catches** (the loop working):
1. *Kickoff manifest-field miscount* — OC's kickoff said "8 manifest fields"; spec §4 step 5 has 12. CC caught it under the "spec is authority" rule and used all 12. (OC's error, CC's catch.)
2. *Walker pseudocode typo* — the plan's list-branch read `enumerate(i_list)` (undefined); should be `enumerate(obj)`. OC caught it in plan review. (Pseudocode only; fixed in real code.)
3. *Schema-drift not firing in dry-run* — OC's Step-2 gate criteria asked for "any schema-drift warnings from the parse pass." CC checked and found `_check_schema_drift` lived inside `stage1_freeze()`, which dry-run never reaches — so drift detection wasn't running in dry-run. CC self-caught on OC's gate criteria and refactored: extracted `_parse_and_inspect()` called by both dry-run and stage1_freeze, so drift detection now fires on both paths. (CC's self-catch, surfaced by an OC gate.)

**Deploy results.** Python 3.13.13. Dry-run: 294 / 22,801 / 67,275, snapshot-id `baseline-2026-05-25-ae015455`, zero drift (after the parse-and-inspect refactor). Real run: all four stages, 273 scrub-audit entries (177/76/10/10/0), verify-clean PASS over 673,871 strings, 23,095 records. Extended Step-4 verifier (spec §6 baseline + 4 OC-added checks): 273 by class, verify PASS, 23,095 lines, 294 headers, 9 multi_root, 3 message_count=0, 304 is_root, raw.json read-only, 12 manifest fields, 1 ledger entry. **9/9.**

**Relocation + commit.** The script was built in `apparatus-scratch/` (gitignored). OC called it canon-not-scratch and chose relocation over `git add -f`: moved to `active/apparatus/apparatus_freeze_pipeline.py` (deleted scratch original — no stale duplicate), smoke-tested from repo root (same snapshot-id, same counts, zero drift — path resolution survived), committed as `402100d`. The `--source` default is cwd-relative, so invocation from repo root resolves regardless of script location.

S13 close enshrined: anchor v7, spec v3, S13→S14 handoff, S14 ignition, SCDD cross-track update. The spec bumped v2→v3 as a fidelity pass — Jake's catch at S13 close that "spec unchanged" was too clean a stamp: the architecture was unchanged, but three text-level drifts (§4.5 status, §6 idempotency precision, §6 schema-drift coverage) needed reconciling against the landed code. No invariant moved; v2 preserved on disk.

---

## DECISIONS LOCKED THIS SESSION — DO NOT RELITIGATE

These are the binding outcomes of S13. They went into v7.

· **D11.** Stage 0 §4.5 symmetric-drop **RATIFIED**. `name` and `summary` are both always-string never-null, both conv-level user-affected metadata, neither floor, neither derivable-without-itself. Co-population confirms name gates summary; non-monotonic summary population confirms the "may evolve" property. The shape difference (fragment vs prose) is real but irrelevant to floor scoping. No spec v3. Stage 0 closed. (No graveyard entry — this CONFIRMED the existing S11 decision rather than overturning anything.)

· **D12.** Stages 1–4 **IMPLEMENTED + acceptance-passed** at population scale. `apparatus_freeze_pipeline.py` v1.2. Baseline snapshot `baseline-2026-05-25-ae015455` exists. The frozen v2 architecture absorbed implementation with zero spec deviations. This is the canonical confirmation that the design is correct — the strongest form of verification available short of substrate integration.

· **D13.** The pipeline script is **CANON, not scratch**. Lives at `active/apparatus/apparatus_freeze_pipeline.py` (tracked), committed `402100d`. The probes (safety, robustness, §4.5) were exploratory and correctly stayed in gitignored `apparatus-scratch/`; the pipeline is the landed artifact and belongs in tracked canon next to the spec it implements. First apparatus code to live in canon. (Reasoning: force-adding canon into a gitignored scratch dir is a semantic lie about that dir + confusing on any fresh clone.)

· **D14.** **dry-run is read-only and must be re-runnable** even when a baseline snapshot exists (pipeline v1.2). The no-overwrite hard-gate (invariant 5.2) guards the **real-run write path** only; dry-run prints an informational NOTE if the snapshot already exists but does not refuse. (Forced by the relocation smoke test being a dry-run against the already-existing baseline; correct because dry-run writes nothing, so there's no overwrite to guard against. CC made the reorder; OC ratified it as correct + safe — the real path still hits the idempotency check before any write.)

· **D15.** Spec bumped **v2→v3** at S13 close — fidelity pass, not an architectural change. Three text-level reconciliations between the spec and the landed code: (a) §4.0.5 RUNNING → ANSWERED (symmetric-drop ratified; population stats folded in); (b) §6 idempotency refined with the dry-run exemption (per D14); (c) §6 schema-drift coverage corrected — v2 implied detection across the full §2.11 surface incl. field-level additions, but the v1.0 code detects type-level drift only (block types + content-list item types), so the spec now states actual coverage + flags field-level as a v1.1 expansion. No invariant moved, no stage redesigned. v2 preserved on disk. (Source: Jake's catch at S13 close that the "spec unchanged" stamp conflated architecture-unchanged with text-accurate; full version bump not decimal per Jake's ref-file convention. Anchor v7 spec-references synced v2→v3 in the same in-flight close bundle — no anchor v8 needed since v7 hadn't been committed.)

---

## VERIFIED GROUND-TRUTH STATE — DO NOT RELITIGATE

Carried from S12, plus S13 implementation confirmations:

· **Locator gate: GREEN.** 294 convs / 22,801 msg uuids / explicit parent chain. Pointer scheme `(snapshot-id, conv_uuid, msg_uuid)` population-validated. Re-confirmed at S13 ingest: 304 `is_root=true` records match the 304 root-position messages.
· **Tree structure: tree-or-forest.** 282/294 single-rooted, 9/294 multi-rooted (2–6 sentinel roots), 3/294 empty. Confirmed in records.ndjson: 9 headers `multi_root=true`, 3 headers `message_count=0`.
· **Cred-inventory: POPULATION-VALIDATED + scrub-PROVEN.** Stage 3 baseline (RTSP=177, Postgres=76, OpenAI=10, Anthropic=10, Stripe=0) matched exactly by the real scrub: 273 redactions logged, then verify-clean PASS with 0 residual hits across 673,871 strings.
· **Content-block types: 5, population-confirmed.** No sixth at any frequency; zero schema-drift events at S13 ingest (the now-firing dry-run detector confirmed).
· **Thinking-in-export CONFIRMED; signature CORRECTED (base64 provenance); 9-path strip set documented; no project linkage; no Anthropic-internal-state surfaces; all field clusters enumerated.** (All carried from S12, unchanged.)
· **records.ndjson seed shape: LOCKED** (see anchor v7 NEXT MOVE + the schema below).

---

## NEXT MOVES (ordered)

*Stage 0 + Stages 1–4 are DONE. The list below picks up after the baseline freeze.*

1. **Seed-shape ingest + ratify.** Prove `records.ndjson` (23,095 records) ingests cleanly and supports pointer-retrieval on a substrate apparatus owns — likely Supabase + pgvector first (Jake's stack; substrate-selection-independent because we're validating the DATA shape, not committing the STORE). Ratify a small real batch before scale (append-only ⇒ un-ratified rows are immortal). **Open question for S14 turn 1–2 with Jake:** seed-shape on Supabase now, or wait for SCDD's substrate pick? The handoff frames seed-shape as the earlier move; doing it on Supabase de-risks the data shape regardless of final substrate.
2. **Substrate selection** — when SCDD finalizes `Substrate_FaceOff_v1.md` (gated on their Continuous-Claude-v3 dual-gate read). Decision sits with apparatus track per D9. SCDD's §3.2 shape gate now validates against the real record shape.
3. **Delta runs + scrub-vN overlays** — the pipeline is baseline + scrub-v1 only. Build delta ingest (uuid-set-difference, date never a filter) and the `scrub-vN/` overlay (re-scrub a sealed snapshot with an extended regex set without mutating it). Both spec'd in v3, unimplemented. Needed before the second export.
4. **Archive backfill** — pipeline over subsequent exports + any re-scrub.
5. **Export-cadence helper** — watch Downloads for a new `conversations.json`, auto-run the pipeline.
6. **Per-project anchor passes** — index/neuron anchors per walled track.
7. **Cross-export uuid-stability check** — confirm a uuid survives a re-export (non-blocking; at next export).
8. **Storage-seam endgame** — Supabase/Postgres MCP connector on Jake's account; verify with a live round-trip.

### records.ndjson shape (locked at S13)
*Per-message record:* `{snapshot_id, scrub_version, conv_uuid, msg_uuid, parent_message_uuid, sender, created_at, updated_at, text, content_blocks[], attachments[], files[], is_root}`.
*Per-conversation header:* `{record_type:"conversation_header", snapshot_id, scrub_version, conv_uuid, created_at, updated_at, account_uuid, message_count, has_branches, multi_root}`.
NO `name`, NO `summary` anywhere. Records interleaved: header → that conv's messages (created_at order) → next header. Pointer = `(snapshot-id, conv_uuid, msg_uuid)`.

---

## DOWNSTREAM FLAGS (will bite later)

· **Pipeline coverage is PARTIAL — delta + scrub-vN unimplemented.** The script does baseline + scrub-v1 only. The second time Jake exports, there's no delta path yet (would re-freeze a full baseline, which the idempotency guard refuses if the export is byte-identical, or creates a second full baseline if it changed — neither is the intended delta behavior). And if a new cred class is observed, there's no scrub-vN overlay path to re-scrub the sealed snapshot. **Bites at the second export or the first regex-set extension.** NEXT MOVE #3.

· **Seed-shape vs substrate-selection ordering.** Seed-shape (NEXT MOVE #1) can run on Supabase independent of the formal substrate pick (NEXT MOVE #2, gated on SCDD). But if SCDD picks a substrate with a materially different ingest unit (e.g. not per-message), some seed-shape learnings won't transfer. Low risk (we're validating data shape + pointer resolution, which mostly transfer), but flag it before sinking deep work into a Supabase-specific seed. **Bites at S14 turn 1–2 — resolve with Jake.**

· **Sister track SCDD S2→S3 in parallel.** Reportedly close to handoff. When their Continuous-Claude-v3 dual-gate read closes and the face-off finalizes, substrate selection (NEXT MOVE #2) unblocks. Expect a coordination turn. The S13 SCDD update (sent this session) primes them that records.ndjson now exists as the concrete shape-gate target. **Bites whenever SCDD S2 closes.**

· **Cross-export uuid stability remains UNVERIFIED.** Non-blocking; design absorbs both outcomes via snapshot-id. If uuids are NOT stable across re-exports, the delta-filter (NEXT MOVE #3) needs different identity semantics. **Bites at the next natural export** — and is now more pressing because delta runs are the next pipeline build.

· **9-path strip-set principle live, lightly enforced.** v7 + v2 say "we don't reconstruct what Anthropic strips." The v1.x pipeline doesn't synthesize strip-set values (Stage 4 carries content_blocks verbatim from the scrubbed JSON), but there's no explicit test asserting it. Worth a unit check when delta/scrub-vN work touches Stage 4. **Bites if a future edit adds field synthesis.**

· **Schema-drift detection is type-level only (v1.0 limitation, now documented in spec v3 §6 + commented in code).** Detects new block types + new `tool_result.content[]` item types. Does NOT detect new *fields* on existing objects. A field-level addition in a future export would pass silently (the type-agnostic scrub still walks its strings, but no drift entry is written). **Bites if a future export adds a field to an existing object type.** v1.1 expansion candidate — spec v3 §6 flags it explicitly.

· **`approval_key` / MCP metadata is benign but uninspected at delta time.** S12 characterized current `approval_key` hits as Google Calendar MCP per-operation auth (benign). A future export with different MCP connectors could surface different `approval_key` values; the scrub walks them as strings (covered for cred patterns) but they're not separately audited. **Non-blocking; note at next export with new connectors.**

---

## JUDGMENT-CALL LEDGER

Non-obvious calls made this session, logged for re-opening if needed.

· **Call:** Single script, Stages 1–4 end-to-end, over a split build (Stages 1+2 then 3+4). **Reasoning:** the stages are tightly coupled (each stage's output is the next's input; verify-PASS gates Stage 4), so a single script keeps the gates in code rather than in filesystem-state-chaining between separate scripts; idempotency is one ledger lookup at the top. **Confidence:** HIGH. **Source:** OC recommendation at S13 turn 2, ratified by Jake's "single."

· **Call:** Add four checks beyond the spec §6 acceptance baseline to the Step-4 verifier (is_root total = 304, raw.json read-only held, manifest 12 fields present, ledger exactly 1 entry). **Reasoning:** the spec baseline (273 / verify-PASS / 23,095 / 9 / 3) covers counts but not structural invariants that could pass-by-coincidence — e.g. per-conv multi_root flags could sum to 9 while the underlying root detection is wrong, so checking is_root=304 independently is cheap insurance; raw.json read-only confirms invariant 5.1 actually took on Windows (where chmod is finicky). **Confidence:** HIGH. **Source:** OC judgment at S13 (pre-Step-4), no pushback.

· **Call:** Relocate the script to `active/apparatus/` (canon) rather than `git add -f` from `apparatus-scratch/`. **Reasoning:** the script is canon (authoritative implementation of the frozen spec), not scratch (exploratory probes). Force-adding canon into a gitignored dir is a semantic lie about that dir and confuses any fresh clone; establishing a tracked code home now, at the first code artifact, is the right time. **Confidence:** HIGH. **Source:** OC judgment at S13, ratified by Jake delegating the call ("which way do you want it?" → OC chose option 2).

· **Call:** Accept CC's v1.2 idempotency reorder (dry-run no longer hard-exits on existing snapshot) even though it wasn't in the relocation prompt. **Reasoning:** it was forced by the smoke test being a dry-run against the already-existing baseline; it's correct (dry-run writes nothing → no overwrite to guard) and safe (the real-run path still hits the idempotency check before any write). Logging it because it was off the literal prompt scope, though correct. **Confidence:** HIGH. **Source:** CC's forced change at relocation, OC ratified at S13 close.

---

## INFRA SWEEP (§17.5d incidentals)

· **First tracked apparatus code.** `active/apparatus/apparatus_freeze_pipeline.py` is the first code (vs docs) in the apparatus canon dir. Future apparatus code (delta runs, scrub-vN, retrieval layer, eventual Cypher wiring) should follow it there. `apparatus-scratch/` stays for exploratory/throwaway work.

· **Baseline snapshot on disk.** `apparatus-archive/snapshots/baseline-2026-05-25-ae015455/` (gitignored, local-only — large + contains the scrubbed corpus). `ledger.jsonl` in the snapshots dir has 1 entry. `raw.json` is read-only.

· **Stale `corpus_seed_v1.md`** (S11/S12 deferred item) — the dead verbatim-COPY corpus file. Still on disk in apparatus-archive. The snapshot dir structure is now real, so this is cleanly relocatable/deletable. **Home: whenever apparatus-archive gets a cleanup pass.** Not urgent.

· **`apparatus_capture_probe.py` sampling bug** (S11/S12 deferred) — inner-loop break collected 2 convs instead of 5. Never reused at S13 (the freeze pipeline is a separate script). **Home: let it die unless reused.**

· **Reference repo state:** `claude-reference`, one repo, no fork. Pushed dirs: `active/`, `archive/`, `templates/`, `skills-catalog/` (excl. source data). Gitignored: `apparatus-scratch/`, `apparatus-archive/`, `prior-art/`, skills-catalog source data. The pipeline commit `402100d` is the S13 code push; the v7 anchor + this handoff are the S13 doc push (Jake committing those manually).

---

## PICKUP GUARDRAILS FOR S14

· **Read v7 + v2 + the pipeline script directly, not through this handoff's summary.** §17.5(c) discipline — handoff summaries drift; canon is authority. The pipeline is real code now; read it to know what's built vs spec'd-but-unbuilt.

· **The baseline snapshot already exists — don't re-run the real pipeline.** The idempotency guard will (correctly) refuse a re-freeze of the same export. Dry-run is safe and re-runnable (v1.2).

· **Trust Jake's reported state on CC results.** Ground OC decisions on what CC reports; don't relitigate the acceptance counts — they're done and verified 9/9.

· **Push back where the spec, this handoff, or the code is wrong.** The three S13 catches (manifest-field, walker typo, drift-in-dry-run) are the shape of welcome catches. The delta/scrub-vN unimplemented gap is the biggest known hole — name it when NEXT MOVE #3 comes up.

· **Resolve the seed-shape-vs-substrate ordering with Jake early** (turn 1–2). It's the first real fork of S14.

· **SCDD S2→S3 in parallel.** Cross-track notices may arrive via Jake. If the face-off finalizes during S14, expect a coordination turn before substrate selection.

· **NEVER search past sessions/chats for code files.** If S14 needs the pipeline script or any code file, ask Jake to upload it (or read it from the repo via codeload). Stale code has cost hours.

· **Prose questions only. No `ask_user_input` widget. Re-anchor every ~5 turns (4/4 = seam warning). Timestamps via bash `date`, never confabulate. Plan in OC, build in CC.**

---

## §17 ROUTING

S13 close bundle:

1. **§17.1** — this handoff (`Chat_Session_Handoff_2026-05-28_apparatus_S13_to_S14.md`). Lands in `active/apparatus/`.
2. **§17.2** — no universal-layer (JAKE-RULES) changes proposed by apparatus S13. (The anti-FOMO clause + Track_Meet_Doctrine rename remain queued from prior sessions for the next universal-layer ratify batch.)
3. **§17.3** — `ANCHOR_apparatus.md` (v7) and `Freeze_Pipeline_Spec_v3.md` (new file; v2 preserved on disk) both land in `active/apparatus/`. The pipeline script (`apparatus_freeze_pipeline.py` v1.2) already committed as `402100d`.
4. **§17.4** — S14 ignition prompt (in-chat code block).
5. **§17.5 (extra)** — SCDD cross-track update (in-chat, for Jake to forward to the SCDD session).

Jake downloads + commits/pushes the v7 anchor + this handoff. All to `claude-reference` (one repo, no fork).

---

*apparatus S13 → S14. 2026-05-28. Grounded against the v6 anchor + v2 spec (entering state) + the §4.5 probe output + the full Stages 1–4 implementation and 9/9 acceptance run against the 366MB archive. Stage 0 closed (§4.5 ratified — nothing overturned, the S11 symmetric-drop confirmed at population scale). Stages 1–4 implemented as a single Python script with zero structural deviations — the frozen v2 design proved correct under real code; the spec was then reconciled v2→v3 at close (fidelity pass on three text-level drifts, no invariant moved). The first baseline snapshot exists on disk and the corpus floor is real. Three in-session catches (manifest-field, walker typo, drift-in-dry-run) kept the loop honest. Confidence HIGH that the freeze architecture is sound; the open cells are substrate selection (gated on SCDD), delta + scrub-vN implementation (the known coverage gap), and cross-export uuid stability (unverified, now more pressing with delta runs next). The next session builds outward from a floor that, for the first time, physically exists.*
