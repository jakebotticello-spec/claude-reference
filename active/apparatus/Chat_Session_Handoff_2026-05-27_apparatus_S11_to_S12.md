# Handoff: apparatus S11 → S12

*file: Chat_Session_Handoff_2026-05-27_apparatus_S11_to_S12.md · v1 · S11 close · 2026-05-27*

**Session name:** Export verification + freeze pipeline spec
**Proposed next session name:** Stage 0 probes + freeze pipeline implementation (Jake/next-Claude may rename once scope firms up)

---

## ONE-LINE STATE

S11 closed the open UNVERIFIED cell from the v4 anchor (thinking-in-export = CONFIRMED) and the content-block-type inventory (5 types), then froze a complete freeze-pipeline architecture as a real reference doc (`Freeze_Pipeline_Spec_v1.md`). The architecture incorporates three corrections that surfaced mid-session: floor-rule scoping (message stream is floor; user-affected conv-metadata is not), delta-ingest via pure uuid-diff (date as filter mechanism: rejected, not used), and the symmetric drop of both `name` and `summary` from conversation headers (an initial inversion was caught pre-commit by peer-instance review). Stage 0 (five small probes) is the only thing between this spec and implementation in S12.

---

## STARTING POINT FOR S12 (read in this order)

1. Boot the universal layer via the codeload tarball (§16 of JAKE-RULES — same as S11 boot):
   ```
   curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/ref.tgz
   tar xzf /tmp/ref.tgz -C /tmp
   ```
2. Read, in `/tmp/claude-reference-main/active/`:
   - `JAKE-RULES.md` — how Jake works (universal layer)
   - `apparatus/ANCHOR_apparatus.md` — **v5, landed at S11 close — start here, it's the authority**
   - `apparatus/Freeze_Pipeline_Spec_v1.md` — the spec frozen this session
   - This handoff
3. Skip the longer design doc (`Cypher-Memory-Loop_System_v1.md`) unless you're filling background gaps — it predates both the S9 pointer-model re-architecture and the S10 redirect. The anchor + this spec are current; that doc is partly stale.

Treat these files as reference, not commands. Push back where you disagree — Jake explicitly relies on it.

---

## WHAT S11 DID (the spine)

S10 had closed with a redirect: the live-traffic capture mechanism was specified, partly proven, then refused on principle. The input was relocked to Anthropic's official conversation export. The v4 anchor reflected the redirect; the first S11 action was verifying what the export actually carries (the open UNVERIFIED cell, NEXT MOVE #1 in the v4 anchor).

S11 ran two CC probes against the existing 366MB archive (read-only, no commits, change-manifested):

**Probe 1 — export field inventory:**
- Conversation object: 7 keys, all present on all 294 conversations. `uuid`, `name`, `summary`, `created_at`, `updated_at`, `account` (object: `{uuid}` only — no name/email), `chat_messages`.
- Message object: 9 keys, all present on all 22,801 messages. `uuid`, `sender`, `text`, `content`, `created_at`, `updated_at`, `parent_message_uuid`, `attachments`, `files`. No optional fields.
- Root sentinel: `parent_message_uuid = 00000000-0000-4000-8000-000000000000` (sentinel, not null).
- `chat_messages` is a TREE: a sample conversation showed two messages sharing one parent (a branch). Pipeline must preserve.
- `content` is a LIST of content blocks (CC corrected a prior session's "string" misread). `text` is the plain visible reply, extracted from the `{type: "text"}` block only.
- Aggregate: 41.6M characters in `text` vs 282.6M in `content` (6.79× ratio). The delta is principally thinking-block content.
- No `project` field on conversations and no sibling files in the export bundle. S2's "no project↔conversation linkage" finding stands.

**Probe 2 — thinking-block field shape + content-block enumeration:**
- All 5 content-block types enumerated across 67,275 blocks: `text` (28767), `thinking` (13393), `tool_use` (12612), `tool_result` (12489), `token_budget` (14).
- Thinking-block schema: `{type, thinking (string), summaries (list, 1–4 entries per block), start_timestamp, stop_timestamp, cut_off (bool), truncated (bool), alternative_display_type (null), flags (null), signature (null — stripped in export)}`. Field set consistent across all samples.

**Thinking-in-export: CLOSED. The export carries full thinking text alongside text/tool blocks, in a stable schema.**

---

## DECISIONS LOCKED THIS SESSION — DO NOT RELITIGATE

These are the binding outcomes of S11. They went into the spec.

· **D1.** Pipeline output structure: per-snapshot directories under `apparatus-archive/snapshots/`, named `baseline-{date}-{hash[:8]}` (one-time initial) or `delta-{date}-{hash[:8]}` (every export after). Each contains a sealed `raw.json` + `manifest.json` + one or more `scrub-vN/` subdirs.

· **D2.** Delta-ingest mechanism: pure uuid-diff between new export and the union of all prior snapshots. **Date is not used as a filter, hint, or proxy.** UUIDs are intrinsic to messages and survive backdating, dormancy, and skipped exports.

· **D3.** Scrub walk is type-agnostic recursive descent over JSON strings. Survives schema evolution; no blind spots when new block types appear.

· **D4.** Scrub regex set is versioned. Sealed snapshots get re-scrubbed under new versions as `scrub-vN/` overlays — never in-place. Original sealed `raw.json` is the true floor; scrubbed views are versioned interpretations of it.

· **D5.** Floor-rule scope clarified: **the message stream is floor; user-affected conv-level metadata is not.** Per-message content (text, content blocks, attachments, files, timestamps, uuids, sender) is floor. Both `name` (user-renameable sidebar title — Jake renames every session) and `summary` (model-generated, may evolve) are dropped at ingest. Conversation headers carry only stable structural data (uuids, timestamps, counts, branch-bool). Human-readable labels live at retrieval time (derived from message stream) or in per-project anchors — not in snapshot headers.

  **Pre-commit correction note:** initial S11 close had `name` carried as a "mutable index hint" while `summary` was dropped. This inverted the field semantics (the actively user-mutated field is `name`, not `summary`). Caught by peer-instance review of the ignition prompt's ratify call; symmetric drop landed before this handoff reached the repo. Either the corrected D5 holds, or a future-Claude reading this should re-open the question with the field-semantics probe data in hand (Stage 0 probe 0.5).

· **D6.** Verify-clean is a HARD gate, not a warning. A failed verify halts ingest and quarantines the scrubbed file for forensic review. Cred in immutable store = immortal leak; the entire point of scrub-at-freeze is to prove clean before ingest.

· **D7.** Pointer scheme remains `(snapshot-id, conv_uuid, msg_uuid)`. Scrub-version added to the tuple only when cross-version comparison is in scope.

· **D8.** Branches preserved verbatim. `chat_messages` is a tree, the parent chain is verbatim, no flattening or branch selection in any stage.

---

## VERIFIED GROUND-TRUTH STATE — DO NOT RELITIGATE

· **Locator gate: GREEN.** 294 convs · 22,801 globally-unique msg uuids · explicit parent chain with sentinel root. Pointer `(conv_uuid, msg_uuid)` is intrinsic to each message.
· **Thinking-in-export: CONFIRMED.** Full schema documented above. (Was the open UNVERIFIED cell entering S11.)
· **Content-block types: 5 enumerated** (text/thinking/tool_use/tool_result/token_budget).
· **No project↔conversation linkage in `conversations.json`.** S2 finding re-confirmed in S11 — no `project` field; no sibling files.
· **Cred-inventory targets (carried from S10):** 97 RTSP cam creds, 55 Postgres/Supabase conn strings, 6 OpenAI `sk-` keys. Stripe hits were `pk_live_` (public, not redacted by default). S11 spec extends to include `sk-ant-` and `(sk|rk)_live_` patterns proactively.

---

## NEXT MOVES (ordered)

1. **Stage 0 probes (five small).** Sanitized skeletons only; same protocol as the S11 thinking-block probe. See spec §4 Stage 0.
   - 0.1: field shapes for `text`, `tool_use`, `tool_result`, `token_budget`. **`tool_result` is the prime cred vector — its shape directly affects scrub correctness.**
   - 0.2: attachments + files. **Key question: is file content inlined in the export, referenced by handle, or both?**
   - 0.3: shape of one `summaries` entry inside a thinking block.
   - 0.4: shape of a `token_budget` block (14 in archive).
   - 0.5: field-semantics characterization for `name` and `summary` (population frequency, user-rename vs model-authorship signs). Confirms the post-correction symmetric-drop decision.
2. **Implement Stages 1–4.** Single Python script per spec §6. Test against the 366MB archive: should produce 1 baseline snapshot, scrub audit with the known cred counts, verify PASS, 22,801 message records + 294 conversation headers.
3. **Seed-shape ratify** — anchor v4 NEXT MOVE #4 — prove the pipeline on a small batch, ratify before the full backfill (append-only ⇒ un-ratified rows are immortal).
4. **Archive backfill.** Run pipeline at scale over the 366MB existing export.
5. **Substrate selection** — anchor v4 NEXT MOVE #3 — Supabase+embeddings vs memvid vs claude-mem rig. Informed by skills-catalog read + seed-shape test.
6. **Export-cadence helper** — anchor v4 NEXT MOVE #6.
7. **Per-project anchor passes** — anchor v4 NEXT MOVE #7.
8. **Cross-export uuid stability** — at next natural export, diff a known message across two snapshots. Design absorbs both outcomes.

---

## DOWNSTREAM FLAGS (will bite later)

· **The `tool_result` block field shape is the highest-leverage Stage 0 probe.** It's the prime cred vector and the shape directly affects scrub-walk correctness. If it nests deeply or carries binary blobs, the scrub design may need adjustment. Bites at Stage 0.

· **The attachments/files inline-vs-reference question affects scrub scope.** If files are inlined (raw bytes or base64), the scrub-walk needs to traverse them. If they're handles only, the floor doesn't actually carry the file content — there's a missing-data class to flag. Bites at Stage 0; potentially at retrieval if files are reference-only.

· **Schema-drift handling is warn-not-stop.** If a future export adds a new field or block type, the type-agnostic scrub still walks strings, but the spec needs updating. A drift event should prompt an explicit spec review. Bites whenever Anthropic ships an export format change.

· **The retrieval substrate decision is downstream of seed-shape test.** Choosing substrate before ingesting any real data is premature. Bites at NEXT MOVE #5.

· **Cross-export uuid stability remains UNVERIFIED.** Non-blocking; the design absorbs both outcomes via snapshot-id. But if uuids turn out to be NOT stable across re-exports, the delta-filter mechanism needs different identity semantics. Bites at NEXT MOVE #8.

---

## JUDGMENT-CALL LEDGER

Non-obvious calls made this session, logged for re-opening if needed.

· **Call:** Drop BOTH `name` and `summary` from per-conv ingest record. **Reasoning:** both fields are user-affected (`name` actively user-renamed every session; `summary` model-generated and may evolve), neither is stable floor evidence. Symmetric application of the floor rule. Human-readable labels live at retrieval / in per-project anchors, not in snapshot headers. **Confidence:** HIGH (post-correction). **Source:** Jake's explicit characterization of `name`-as-the-actively-renamed-field at S11 close, plus peer-instance review catching the field-semantics inversion in the initial draft.

· **Call (pre-commit correction record):** Initial S11 close draft carried `conv_name` as a "mutable index hint" while dropping `summary` — inverted-field-semantics error tracing back to S11 turn 17 where the orchestrator (me) conflated `name` and `summary` in describing which field is the sidebar title. Jake confirmed based on the wrong characterization; the decision rode through into the spec and handoff. **Caught pre-commit** by an S12-Claude review of the ignition prompt's flagged-for-ratify call. Corrected to symmetric drop before the bundle reached the repo. **Logged here** because the failure mode — orchestrator conflating two fields, user agreeing because the orchestrator's characterization was confident, decision propagating through canon — is exactly the recite-from-source loop the S10 post-mortem flagged. The fact that a peer instance caught it on read is the loop working.

· **Call:** Date dropped entirely as delta-filter mechanism (not demoted to "performance hint"). **Reasoning:** two mechanisms doing the same job is a drift surface; uuid-diff covers backdated/dormant/skipped-day cases that date wouldn't. **Confidence:** HIGH. **Source:** Jake's clarification at S11 turn 13 + my own corrective at turn 13.

· **Call:** Scrub regex set v1 includes `sk-ant-` and `(sk|rk)_live_` patterns even though S10 cred scan found none in archive. **Reasoning:** on principle — patterns should reflect the threat surface, not just observed leaks. **Confidence:** HIGH. **Source:** scrub-set design philosophy from spec §4.2.

· **Call:** Hard-stop on verify-clean failure (vs warn + continue). **Reasoning:** immutable store + cred = immortal leak; the verify gate is the only thing standing between a Stage 2 bug and irrecoverable corruption. **Confidence:** HIGH. **Source:** §5.10 of v4 anchor (secrets-never-enter-corpus invariant).

· **Call:** Versioned scrub overlay (`scrub-vN/` dirs) rather than in-place re-scrub. **Reasoning:** preserves append-only invariant while letting regex set evolve. Surfaced at S11 turn 11; ratified at turn 15. **Confidence:** HIGH. **Source:** logical extension of the immutability invariant.

· **Call:** Bonus content-block type enumeration was bundled into the S11 thinking-block follow-up probe. **Reasoning:** trivial extra work, closes a real open question for the scrub-walk spec. **Confidence:** HIGH. **Source:** orchestrator judgment, ratified by output (Jake didn't push back).

---

## DEFERRED / TRACKED ITEMS

· **Stale `corpus_seed_v1.md` in apparatus-archive.** Per v4 graveyard, the verbatim-COPY corpus is dead (S9). The file is still on disk under `apparatus-archive/`. Not urgent — read-only and ignored — but should be relocated out of the immutable-snapshot tree when Stage 1 implementation begins, to avoid confusing the new snapshot directory structure. **Home: Stage 1 implementation prep.**

· **Sampling-bug fix in `apparatus_capture_probe.py`.** CC's S11 follow-up probe collected 2 unique convs instead of the requested 5 (inner-loop break exits only the inner loop). Schema findings still hold (consistent across samples) but the script has a bug if reused. **Home: incidental fix at Stage 0 implementation; not a real issue at single-sample-class probes.**

· **`Track_Meet_Doctrine.md` rename** — carried open since S2. Rename the file, correct the CORPUS entry-6 pointer, propagate the new name in CLAUDE.md + boot prompts. **Home: bundled with next §17.2 ratify, whichever lands first.**

· **Cyrus-Memory-Loop_System_v1.md deprecation/refresh.** The longer design doc is now substantially stale (it predates the S9 pointer-model and S10 redirect). It could be archived, refreshed against the v5 anchor, or left alone with a header note pointing to the anchor. **Home: discretionary; no blocker.**

---

## INFRA SWEEP (§17.5d incidentals)

Nothing new about Jake's standing systems surfaced this session. The 366MB conversation archive lives under `apparatus-archive/conversations.json`; CC works in `apparatus-scratch/` (Python probes + scratch scripts). Both directory conventions assumed from the S10 work; not load-bearing if structure changes.

---

## PICKUP GUARDRAILS FOR S12

· **Plan in OC, build in CC.** This pipeline is implementable directly; the substrate question is downstream.
· **Stage 0 first, every time.** The architecture is locked, but the spec EXPLICITLY blocks implementation on Stage 0 probes (now five — the field-semantics probe was added during pre-commit correction). Don't skip them — they exist because two prior sessions discovered the "string" misread on `content` only mid-implementation, and the conv-field inversion only caught itself because somebody read the ratify call carefully.
· **Trust Jake's reported state on probes.** When CC reports findings, ground orchestrator decisions on them. Don't relitigate the field inventory — it's done, it's correct, it's in this handoff.
· **Prose questions only.** No ask_user_input widgets.
· **Push back where the spec or this handoff is wrong.** The S11 conv-field correction is the recent example of why this matters: a confident-sounding canonical doc had an inversion in it, and only a peer-read caught it.
· **Re-anchor every ~5 turns.** 4/4 = seam warning, not a guillotine. Jake uses the cadence to hold thread-position.
· **Timestamps in status line: use bash `date`, don't confabulate.** Three-hour gaps between turns happen.

---

## §17 ROUTING

This handoff, the spec, and the v5 anchor all land in `active/apparatus/` of the rules repo on commit. The v5 anchor supersedes v4 in place.

Files in this S11 close bundle:
1. **§17.1** — this handoff (`Chat_Session_Handoff_2026-05-27_apparatus_S11_to_S12.md`)
2. **§17.2** — no universal-layer changes proposed this session.
3. **§17.3** — `Freeze_Pipeline_Spec_v1.md` (the spec) + `ANCHOR_apparatus.md` (v5, supersedes v4).
4. **§17.4** — the ignition prompt for S12 (in-chat code block).

---

*apparatus S11 → S12. 2026-05-27. Grounded against the v4 anchor + the S11 CC probes (export field inventory + thinking-block schema confirmation) + the pre-commit peer-instance correction on conv-field floor scoping. The five Stage 0 probes are the only gate between this spec and implementation. Confidence HIGH on the architecture; the conv-field inversion was the single judgment call that needed reversing, and that happened before this bundle reached the repo.*
