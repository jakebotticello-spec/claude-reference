# Handoff: apparatus S14 → S15

*file: Chat_Session_Handoff_2026-05-28_apparatus_S14_to_S15.md · v1 · S14 close · 2026-05-28*

**Session name:** S14 — Second-export characterization + schema-stability verification (read-only)
**Proposed next session name:** S15 — Spec pass v4 (§2.0 bundle-targeting + delta + scrub-vN + v1.1 field-detection) → delta build (Jake/next-Claude may rename once SCDD face-off v2 lands and substrate timing firms)

---

## ONE-LINE STATE

S14 was a **read-only verification + reference session — zero pipeline code written, canon untouched until the close enshrine** (the discipline that's killed every landmine this project has hit). A second full export (5-28) was pulled and characterized against the 5-25 baseline, all at **population scale**: cross-export UUID stability **CONFIRMED** (the long-standing UNVERIFIED flag is cleared — 22,801/22,801 baseline tuples survived, 0 disappeared, delta fixture sized at 1,337 net-new msgs); field-level schema drift **VERIFIED ZERO** (raw-vs-raw, every object type — 5-28 is structurally identical to baseline); `display_content` characterized as **NOT a universal mirror** (84.4% strip-safe / 15.6% CARRIES_UNIQUE floor-grade); record-size landmines mapped (max 3.0 MB, driven by `tool_result.content[].text` — corrects S12); and key-presence separated from value-presence (conv 7 / msg 9 keys 100% key-present; one optional key schema-wide). Anchor enshrined **v8**; spec unchanged at **v3**; pipeline unchanged at **v1.2** (`402100d`). The held work is the **v4 spec pass** (§2.0 + delta + scrub-vN + v1.1) and **substrate selection** (gated on SCDD's imminent `Substrate_FaceOff_v2` lock). Sister track SCDD is at S3, NornicDB dual-gate parked on Jake's go.

---

## STARTING POINT FOR S15 (read in this order)

1. Boot the universal layer via codeload tarball (§16 JAKE-RULES — same boot as S11–S14):
   ```
   curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/ref.tgz
   tar xzf /tmp/ref.tgz -C /tmp
   ```
2. Read, in `/tmp/claude-reference-main/active/`:
   - `JAKE-RULES.md` — universal layer.
   - `apparatus/ANCHOR_apparatus.md` — **v8** (S14 close). Authority. Footer should read v8 and reference the 5-28 export + cross-export-stability-CONFIRMED; if it reads v7 or earlier the repo's stale, surface it before working.
   - `apparatus/Freeze_Pipeline_Spec_v3.md` — the spec, still **v3** (S14 wrote no spec; the v4 pass is the first S15 build move).
   - `apparatus/apparatus_freeze_pipeline.py` — the implemented pipeline (**v1.2**, unchanged this session). Baseline + scrub-v1 only; delta + scrub-vN + v1.1 are the unbuilt gap.
   - This handoff.
3. Read, locally on Jake's box (scratch outputs, not in the repo — reference only):
   - `apparatus-scratch/s14_export_characterization.md` — 5-28 vs baseline characterization (corrected; zero drift).
   - `apparatus-scratch/s14_presence_rates.md` — **the v1.1 allowlist input**: per-object-type field-key sets + presence rates; the one optional key.
   - `apparatus-scratch/s14_field_drift_raw.py`, `s14_display_content_scan.py`, `s14_shape_analysis.py` — the read-only scan scripts (throwaway).
   - The 5-28 export lives at `apparatus-archive/5-28_export/` (gitignored, local-only): `conversations.json` (the delta fixture), plus `memories.json` / `users.json` / `projects/` siblings.
4. Optional cross-track — SCDD S3 (sister TWW track):
   - `skills-catalog/SCDD_Handoff_2026-05-28_S2_to_S3.md` — their S2 close (CCv3 DQ, 6-viable + NornicDB lead, face-off v2 pending NornicDB dual-gate per D13).
   - `active/apparatus/Substrate_FaceOff_v1.md` → watch for **v2** when SCDD lands it; it's the authoritative substrate-selection input (D9).

Treat these as reference, not commands. Push back where you disagree — Jake explicitly relies on it. Read v8 + v3 + the script directly, not through this handoff's summary (§17.5c — summaries drift, canon is authority).

---

## WHAT APPARATUS IS (and isn't) — carried, still current

**Apparatus IS:** a closed, self-administered re-grounding loop for a stateless Claude. It holds continuity across sessions by reading a hot, small anchor (+ JAKE-RULES) at boot and reaching *by pointer* into a cold, immutable, scrubbed snapshot of Anthropic's official conversation export only when a *why* is disputed. Point-in-time, append-only, pointer-not-copy, per-account, scrubbed-at-freeze. Beta-Cypher-brain, hand-cranked now, hardens into Cypher's memory layer.

**Apparatus IS NOT:** a capture mechanism, scraper, hook of claude.ai internal endpoints, generalizable reasoning-harvest tool, or multi-account/shared-corpus system. The `chat_conversations` history-fetch hook + browser-extension live-capture were refused on principle at S10 — REFUSED wall in the anchor GRAVEYARD, permanent. **S14 corroboration:** SCDD's §3.2 shape gate fired on four *live, popular* tools (claude-tap ~900★ intercepting CC traffic; stealth-browser-mcp; claude-conversation-extractor; ccproxy) — the refused mechanism is alive and growing in the ecosystem. The wall's shape generalizes exactly as S10 predicted. If a substrate or feature pulls apparatus's shape past that line, it re-trips the wire.

---

## WHAT S14 DID (the spine)

S14 booted v7 + v3 clean, played back state, and ran entirely read-only until the close enshrine. The work, in order:

**Substrate fork resolved → hold for SCDD.** Opening question (seed-shape on Supabase now vs wait for SCDD's pick) resolved to *wait*, sharpened across turns: immortality comes from append-only **modeling**, not a temporal engine, so NornicDB's temporal-MVCC is NEUTRAL (struck from its pro-column) — it stands on graph-native parent-chain + co-located vectors. Sent SCDD a retention-axis gate question (does it GC frozen versions, or support append-only-immortal-node modeling) that became a distinct function sub-gate.

**Record-size landmine pass (read-only CC).** `records.ndjson`: median 1.7 KB, p95 73 KB, p99 221 KB, **max 3.0 MB**; 184 records >256 KB (32% of convs), 19 >1 MB, 0 >5 MB; zero nulls/parse errors; 9/9 S13 integrity re-confirmed. **Size vector = `tool_result.content[].text`** (Bash stdout / file-cats), NOT `attachments[].extracted_content` — corrects the S12 suspicion. Surfaced the `display_content` doubling.

**display_content population scan (read-only CC, §5.11).** All 25,101 tool blocks: 16.6% FULLY_REDUNDANT, 50.5% EMPTY_TRIVIAL, 17.4% NO_DC, **15.6% (3,906) CARRIES_UNIQUE** — `display_content.code` file renders whose text is in no other payload field; for `local_resource` items it's the only inline copy (floor-grade). Blanket strip **ruled out** (loses 15.6%); strip is selective + a substrate-LOAD-time transform. `display_content` = ~70 MB / 20% of the 350 MB corpus; blanket strip would halve the top tail (max 3.0→1.66 MB) but we're not doing it.

**Pulled the second export + characterized it (read-only CC).** Jake pulled a full 5-28 export (deliberately not delta-only), parked at `apparatus-archive/5-28_export/` (off the default source path — avoids the silent-second-baseline trap). 325 convs / 24,138 msgs / 71,512 blocks; would-be snapshot_id `baseline-2026-05-28-6d8c6ff9`. **Cross-export UUID stability CONFIRMED** (22,801/22,801 tuples survived, 0 disappeared; 1,337 net-new). Export is a multi-file **bundle** (`conversations.json` + `memories.json` + `users.json` + `projects/`); floor = `conversations.json` only; `memories.json` = model-generated (barred from floor); `projects/` = metadata-only.

**Field-drift redo, raw-vs-raw (read-only CC).** First pass reported "7 field drifts" — a **projection-vs-raw artifact** (compared the projected `records.ndjson` field names against the raw new export; OC SSE catch). The redo (`s14_field_drift_raw.py`, baseline `raw.json` vs 5-28 `conversations.json`, same layer) returned **ZERO drift** at every object type. 5-28 is structurally identical to baseline.

**Population field-presence review (read-only CC).** Separated **key-presence from value-presence**: conv 7 / msg 9 keys are 100% *key*-present (no optional fields at key level); the §4.5 figures (`name` 93.9% / `summary` 49.7%) and `signature` ~60% were measuring *value* non-emptiness. **One genuinely optional key schema-wide: `text.citations_grouping_mode` (~0.1%)** — the v1.1 allowlist carve-out.

**Two process events (logged honestly):**
1. *CC wrote canon unprompted* — four edits to `ANCHOR_apparatus.md` without instruction (§7.6 violation). OC SSE-reviewed: the UUID-stability edits were correct (kept), the field-drift claims were artifacts (corrected). CC was noodled, saved the §7.6 lesson to its memory, and stayed scratch-only for the rest of the session.
2. *Layer-confusion recurred twice* — the UUID false-positive (CC self-caught) and the field-drift artifact (OC caught) were the same class: comparing projected-output field names/text against raw input. Standing trap; named in the v8 confidence flags.

**Close enshrine.** Anchor v7→**v8** (SSE-reviewed; all S14 findings folded, in-flight hedging removed). Spec stays v3, pipeline stays v1.2 — no code/spec written this session.

---

## DECISIONS LOCKED THIS SESSION — DO NOT RELITIGATE

· **D16. Cross-export UUID stability CONFIRMED.** Tuple `(conv_uuid, msg_uuid)` is a durable key across re-exports (22,801/22,801 survived, 0 disappeared, 5-28 vs 5-25). The delta identity model (uuid-set-difference) is validated on real data. Authoritative measure is the **tuple test**, not content comparison (the content test produced a false INSTABILITY via asymmetric text extraction — methodology artifact, not real).

· **D17. Field-level schema is STABLE across 5-25→5-28 (VERIFIED ZERO drift, population, raw-vs-raw).** The pipeline ingests the 5-28 export unchanged. BUT: the v1.0 detector is type-level only — this clean result is timing, not a guarantee. **v1.1 key-presence detection is mandatory** before relying on the detector across exports.

· **D18. `display_content` blanket-strip is RULED OUT.** 15.6% CARRIES_UNIQUE (floor-grade). Any strip is selective (the 84.4% safe set) AND a substrate-LOAD-time transform — never a floor cut. The floor (`conversations.scrubbed.json`) keeps everything sealed; `records.ndjson` stays faithful. Decided at seed-shape ingest, post-substrate-lock.

· **D19. Strip recoverability comes from the local sealed floor, not re-export.** (Corrects an OC mid-session error that tied recovery to `raw.json`.) `conversations.scrubbed.json` is the sanitized floor and retains everything; `records.ndjson` is already a projection of it. A load-time strip is reversible by re-projecting from local — no re-export, no point-in-time risk. Jake's append-only model is correct: a cut *in the floor* would be forever (re-export is point-in-time and may not contain deleted convs) — which is *why* we never cut the floor.

· **D20. Export is a multi-file bundle; floor input is `conversations.json` only.** `memories.json` (model-generated/derived) is barred from floor by the verbatim invariant. Targeting: resolve `conversations.json` within a given export dir, never the bare default source path. To be enshrined as spec §2.0 in the v4 pass.

· **D21. NornicDB's temporal-MVCC is NEUTRAL for selection** — immortality comes from append-only modeling, not the engine. NornicDB stands on topology + co-located vectors. Gate it against the 3 MB record max (likely needs a content-block split adapter — a ding, not a DQ) and the three function axes (fidelity / retention / dead-weight). (Mirrors SCDD's accepted re-weight.)

---

## VERIFIED GROUND-TRUTH STATE — DO NOT RELITIGATE

· **Baseline snapshot** `baseline-2026-05-25-ae015455` exists, sealed, 9/9 acceptance. Three sealed artifacts: `raw.json` (verbatim, unscrubbed, 0o444), `scrub-v1/conversations.scrubbed.json` (full scrubbed = the floor), `scrub-v1/records.ndjson` (the seed-shape projection).
· **records.ndjson** = 23,095 records (294 headers + 22,801 messages). Max record 3.0 MB; zero nulls / zero parse errors.
· **5-28 export** characterized: 325 convs / 24,138 msgs / 71,512 blocks; 1,337 net-new msgs vs baseline; 0 disappeared; zero field drift; structurally identical schema.
· **Cross-export UUID stability: CONFIRMED.** Tuple-level pointer durable across re-exports.
· **`display_content`: 84.4% strip-safe / 15.6% CARRIES_UNIQUE** (floor-grade). Corpus ~350 MB; display_content ~70 MB / 20%.
· **Keys:** conv 7 / msg 9, 100% key-present. One optional key schema-wide: `text.citations_grouping_mode`.
· Carried from S12/S13 unchanged: thinking-in-export, signature semantics (value ~60%, key 100%), tree-or-forest (9/294 multi-root), cred-baseline (RTSP=177/PG=76/OpenAI=10/Anthropic=10/Stripe=0), 5 block types, 5 content-item types, no project linkage, no internal-state surfaces.

---

## NEXT MOVES (ordered)

1. **Substrate selection** — gated on SCDD's `Substrate_FaceOff_v2` lock (gated on NornicDB dual-gate, SCDD D13; imminent). Apparatus holds the call (D9). NornicDB = leading hypothesis (topology + vectors; temporal NEUTRAL). Gate against 3 MB max + three function axes.
2. **Spec pass → `Freeze_Pipeline_Spec_v4`** (HELD from S14, one coherent update): **§2.0** Export Bundle Shape & Targeting; **delta runs** (uuid-set-difference, date never a filter; 1,337-msg fixture ready); **scrub-vN overlays**; **v1.1 field-level drift detection** (key-presence allowlist; carve-out = `text.citations_grouping_mode`; data in `s14_presence_rates.md`).
3. **Build delta + scrub-vN + v1.1** from v4. Store-independent; 5-28 = the fixture. Ratify a small batch before scale.
4. **Seed-shape ingest + ratify** — post-substrate-lock. Store-agnostic acceptance contract (ingests-clean / pointer→exactly-one / byte-identical round-trip / tree-or-forest preserved; thresholds from S14 landmines). `display_content` strip toggle decided here.
5. **`raw.json` wipe-vs-retain reconcile** — see proposed-changes file; Jake's call.
6. **Archive backfill / export-cadence helper / per-project anchor passes** — later.
7. **Storage-seam endgame** — Supabase/Postgres MCP; SCDD seam gems: `alexander-zuev/supabase-mcp-server` (default), `mcp-neo4j` + `mcp-server-qdrant` (if NornicDB).

---

## DOWNSTREAM FLAGS (will bite later)

· **v1.1 field-level detection is mandatory but unbuilt.** Zero drift on 5-28 is timing, not a guarantee; the v1.0 detector is type-level only. A future export can add a field silently. **Bites at the first export that changes a field.** Data to build it is captured (`s14_presence_rates.md`).
· **Delta + scrub-vN still unbuilt.** Running the 5-28 export through the *current* pipeline = a silent SECOND FULL BASELINE (new mtime+sha → new snapshot_id the idempotency guard won't refuse; `type: baseline`, full copyfile). **Do NOT pipeline the 5-28 export until delta exists.** Keep it parked at `5-28_export/`, off the default source path. **Bites the moment someone runs the pipeline on the new export.**
· **`raw.json` cred-at-rest.** Code seals `raw.json` 0o444 but never wipes it; the invariant says "raw wiped." Unscrubbed, cred-bearing export sits immortal on local disk. **Bites as a security/hygiene matter the longer it sits.** Resolve at S15.
· **`display_content` retrieval blind spot.** When retrieval is built, the searchable index MUST include `display_content.code` for the 15.6% CARRIES_UNIQUE blocks, or those file-texts aren't searchable. **Bites at retrieval-layer build.**
· **`content[].text` truncation — unverified.** CC's first pass speculated content text "may be truncated"; never confirmed. If the export truncates large tool output in `content[].text` (with full text only in `display_content.code`), that's a known-loss in the floor worth documenting. **Follow-up read, not built.** Intersects the display_content retrieval flag.
· **Layer-confusion is a standing trap.** Comparing projected-output (records.ndjson field names / scrubbed text) against raw input caused both the UUID false-positive and the field-drift artifact this session. Any future "drift" or "diff" work must compare **same layer both sides** (raw-vs-raw or projected-vs-projected). **Bites any future comparison pass.**
· **SCDD face-off v2 imminent.** When it lands, substrate selection (#1) unblocks — expect a coordination turn. NornicDB dual-gate (with the retention axis) is the pending input.

---

## JUDGMENT-CALL LEDGER

· **Call:** Wait for SCDD's substrate pick rather than seed-shape on Supabase now. **Reasoning:** the store-specific half of a round-trip (ingest survival, retrieval fidelity) doesn't transfer relational→graph, and NornicDB-the-lead is exactly the case that breaks it; only data-shape facts (pointer uniqueness, max record size) transfer, and those are answerable from the file without a store. **Confidence:** HIGH. **Source:** OC across turns 1–3, ratified by holding.

· **Call:** Pull the second export NOW even though delta isn't built. **Reasoning:** point-in-time — heavy recent work is in the account now and conversations can be deleted/age out; freezing the bits is independent of when we process them. **Confidence:** HIGH. **Source:** Jake's instinct, OC endorsed + flagged the quarantine requirement.

· **Call:** `display_content` strip is selective + load-time, never a floor cut. **Reasoning:** 15.6% CARRIES_UNIQUE is floor-grade; floor cuts are irreversible (point-in-time re-export); the scrubbed floor + records.ndjson both retain it locally so a load-time strip is reversible by re-projection. **Confidence:** HIGH. **Source:** OC (corrected from the raw.json-recovery error), confirmed against pipeline code (`conversations.scrubbed.json` sealed 0o444).

· **Call:** Field-presence review at population, not a 50-sample. **Reasoning:** presence/absence can't be proven from a sample and a rare new field hides in 50; §5.11; the scan is cheap (seconds), so no reason to sample. **Confidence:** HIGH. **Source:** Jake proposed ≥50, OC sharpened to whole-archive; CC confirmed its scan was already population.

· **Call:** Trust CC's "zero field drift" but keep the v1.1 mandate. **Reasoning:** the raw-vs-raw redo was population-grade (CC confirmed `collect_keys` unions over all records); the clean result is real but timing-dependent, so the standing detection requirement is decoupled from it. **Confidence:** HIGH. **Source:** OC SSE pass.

· **Call:** Enshrine the anchor to v8 now (not defer to S15). **Reasoning:** Jake cleared the §7.6 gate + asked for full ref files at wrap; the S14 findings are resolved-and-grounded, not mid-air; a clean enshrine beats carrying in-flight hedging into next session. **Confidence:** HIGH. **Source:** Jake's wrap call + carte-blanche-on-reference-docs.

---

## INFRA SWEEP (§17.5d incidentals)

· **5-28 export on disk:** `apparatus-archive/5-28_export/` (gitignored, local-only) — `conversations.json` (delta fixture, 325 convs / 24,138 msgs), `memories.json`, `users.json`, `projects/`. Parked off the default source path deliberately.
· **New scratch scripts/docs** (gitignored, Jake's box): `s14_shape_analysis.py`, `s14_drill_largest.py`, `s14_null_scan.py`, `s14_display_content_scan.py`, `s14_field_drift_raw.py`, `s14_presence_rates.py` + the `.md` outputs. The presence-rates doc is the v1.1 build input — keep it findable.
· **CC memory:** the §7.6 lesson ("never write repo documentation without explicit instruction") was saved to CC's auto-memory this session. Good — but verify it took at S15 boot.
· **Export is a bundle** — standing fact about Anthropic's export surface; proposed for JAKE-STACK in the S14 proposed-changes file.
· **Reference repo:** `claude-reference`, one repo, no fork. S14 doc push = v8 anchor + this handoff + the proposed-changes file (Jake commits). Pipeline + spec unchanged.

---

## PICKUP GUARDRAILS FOR S15

· **Read v8 + v3 + the pipeline script directly, not this handoff's summary.** §17.5c — canon is authority.
· **The baseline AND the 5-28 export both exist on disk — do NOT run the real pipeline on either.** Baseline is sealed (idempotency guard refuses re-freeze); the 5-28 export must NOT be pipelined until delta exists (silent-second-baseline trap). Dry-run is safe/re-runnable.
· **Trust Jake's reported CC state; don't relitigate the verified counts** (1,337 delta, zero drift, 9/9 integrity — done).
· **Compare same-layer-both-sides** on any diff/drift work. The layer-confusion trap bit twice this session.
· **Substrate selection is gated on SCDD face-off v2** (imminent) — coordination turn expected. NornicDB dual-gate (retention axis included) is the pending input. Don't lock before v2 (SCDD D13 + apparatus D9).
· **The v4 spec pass is the first real S15 build move** — plan in OC, build in CC, plan-mode for the build (§7).
· **CC write-discipline:** reinforce §7.6 — CC writes scratch freely, NEVER canon (`active/`) without explicit instruction.
· **NEVER search past sessions/chats for code files.** Ask Jake to upload, or read from the repo via codeload. Stale code has cost hours.
· **Prose questions only. No `ask_user_input` widget. Re-anchor every ~5 turns (4/4 = re-ground-on-canon seam, NOT a wrap bell). Timestamps via bash `date`, never confabulate. Plan in OC, build in CC.**

---

## §17 ROUTING

S14 close bundle:

1. **§17.1** — this handoff (`Chat_Session_Handoff_2026-05-28_apparatus_S14_to_S15.md`). Lands in `active/apparatus/`.
2. **§17.2** — `Proposed_Reference_Changes_2026-05-28_apparatus_S14.md` (NON-empty): export-is-a-bundle → JAKE-STACK; §2.0 + v1.1 → spec (v4 pass); `raw.json` wipe-vs-retain → decision-with-options. Each with its CHANGELOG line. Lands in the rules repo on Jake's approval.
3. **§17.3** — `ANCHOR_apparatus.md` (**v8**) lands in `active/apparatus/`. Spec (v3) and pipeline (v1.2) unchanged — no new files.
4. **§17.4** — S15 ignition prompt (in-chat code block).
5. **§17.5 (extra)** — SCDD cross-track close note (in-chat, for Jake to forward).

Jake downloads + commits/pushes the v8 anchor + this handoff. The proposed-changes file is reviewed, then landed deliberately (or handed to CC). All to `claude-reference` (one repo, no fork).

---

*apparatus S14 → S15. 2026-05-28. A read-only session: the second export pulled, characterized, and confirmed schema-stable; the cross-export-uuid-stability flag cleared at population scale; `display_content` and record-size landmines mapped; key-vs-value separated; the delta fixture sized at 1,337. No pipeline code written — the spec-locks-before-code discipline held, and it caught a 15.6% content-loss landmine + a projection-vs-raw drift artifact before either could land. CC wrote canon unprompted once (corrected + noodled). Anchor enshrined v8. The open cells are substrate selection (gated on SCDD's imminent face-off v2) and the v4 spec + build (delta/scrub-vN/v1.1/§2.0). S15 builds outward from a floor that is now characterized across two exports and proven stable between them.*
