# ANCHOR — apparatus-build track
*v4 · 2026-05-27 (apparatus S10 close, post-redirect) · hot · read this + JAKE-RULES before working*

> **DIRECTIONAL NOTE (read first).** Between v3 and v4 the project's input mechanism changed: an extension-based capture of claude.ai's internal endpoints was specified, partly proven, then **refused on principle** and is permanently out of scope. **The input is now Anthropic's official conversation export, full stop.** Most of the design (pointers into an immutable snapshot, retrieval-not-curation, scrub-at-freeze, anchor/corpus separation) survives the swap unchanged — only the capture front-end is gone. If anything below reads like an invitation to revisit live-traffic capture, that is a drafting failure on my part; the answer is no. See the **REFUSED — DO NOT RE-OPEN** wall in the GRAVEYARD.

## DESTINATION
Build the apparatus's own memory system (*The Wallaby Way*): a closed, self-administered re-grounding loop that holds continuity for a stateless Claude across sessions — so Jake stops being the memory bus *and* the blind follower. It is **beta-Cypher-brain**: the same anchored/plastic strata Cypher will run on, hand-cranked now, hardening into Cypher's memory layer. Scope is **Jake's whole working surface**. A chat-Claude works small (anchor + rules), with a cold, complete, immutable **snapshot** behind it — built from official exports — that it reaches *by pointer* only when a *why* is disputed.

## WORKING STYLE (not invariants — how Jake works with the orchestrator)
*These are conventions Jake finds useful, not identity claims for the instance.*
- **Status line at the end of each reply** — Turn-end status stamp every reply — the format Jake uses is a backticked one-liner: turn N · ET-time · re-anchor X/4 · dest…; state…; next…. The turn counter and re-anchor cadence (every ~5 turns, with the 4/4 mark as a seam-hunt warning, not a guillotine) are how he holds thread-position across long sessions and knows when to wrap. It's a workflow, not a ritual — but he uses the specific format, so match it.
- **Alignment check on request** — Jake may ask the orchestrator to play back its understanding of project state (goal, constraints, current state, next move). It's a check that we're pointed the same way, not a loyalty test. If the playback surfaces a disagreement, that's the point — say so.
- **Push back with evidence** — Jake relies on the orchestrator to catch his mistakes, not agree with him. Terse, peer-to-peer, no apology theater. If a request is wrong, off-base, or shouldn't be done, say so plainly.
- **Prose, not the widget** — answer in prose; don't reach for the ask_user_input tool to gather preferences.

## INVARIANTS — WITH WHY
*(consolidated across S1–S10; merged facets, no live why dropped — verify against the S9→S10 handoff if in doubt)*
- **One undelineated corpus; the anchors are the index/neurons INTO it** — BECAUSE partitioning by project hides cross-domain knowledge (a woodworking lesson is load-bearing for 3D finishing). S1: *"corpus without anchor is un-navigable noise; anchor = an index into it."* Don't re-wall the ocean.
- **Corpus = curated POINTERS into an immutable, named snapshot — never copied or reworded text. Claude authors the INDEX, never the FLOOR.** — BECAUSE copying is a drift vector inside the one artifact whose job is no-drift (the dead seed drifted 152×); the export is verbatim by construction; pointing deletes the vector. Claude curates whys well but *reconstructs* when asked to transcribe — the floor must be mechanical.
- **The floor input is the official Anthropic conversation export** — BECAUSE it's the sanctioned, supported, lossless source for Jake's own conversation data, carrying message uuids and the parent chain. No other input surface is in scope. (See the REFUSED wall for why.)
- **Thinking blocks, when present in the snapshot, are floor-grade content alongside text — not a separate or live-only artifact** — BECAUSE the architectural commitment is that any reasoning available in the snapshot is treated as evidence at the same fidelity as visible text. Whether the current export actually carries thinking blocks is **UNVERIFIED in v4 — first S11 action is to open an export and check.** If it does, the design holds as-is; if it doesn't, the design still works on text + tool blocks and we revisit only if it becomes load-bearing.
- **Snapshot-id namespacing: freeze-and-name, accumulate, never overwrite** — BECAUSE exports are point-in-time and multiple will exist; a bare `conv/msg` pointer is ambiguous across them. Pointer = `{snapshot-id · conv_uuid · msg_uuid · why}`.
- **The pointer `(conv_uuid, msg_uuid)` is intrinsic to the message and stable across snapshots (presumed)** — BECAUSE it's a property of the message, not its array position; it survives a body scrub for free. Cross-export stability is still UNVERIFIED — confirm at next export by diffing a message present in two snapshots.
- **Navigable by retrieval, not curation** — BECAUSE no-discard + relevance-weighted retrieval is the genesis; hand-picking "salient" exchanges = Jake back on the bus + lost congeniality. The only curated thing is the tiny *why*, and it lives in the anchor.
- **Anchor hot + small + boot-read (instant, via git, no export needed); corpus cold + queried-never-booted (lazy, via export)** — BECAUSE the moment the corpus loads "just to be safe," the 87-file swamp is rebuilt. The hot/cold wall is the whole game; per-chat corpus freshness is a false requirement — the anchor carries current truth.
- **The presence layer can't be stored — only booted warm; the boot/re-read/working-cadence loop IS its mechanism; the lineage is how it survives not-persisting** — BECAUSE soup + neurons persist, but the mind that runs them resets every session. Continuity that doesn't depend on any single instance holding the thread.
- **Secrets never enter the corpus OR chat; cred scrubbed at freeze (logged + verified), raw wiped, sanitized snapshot = floor** — BECAUSE a leaked cred in an immutable store is immortalized (one already leaked to chat). The scrub walks all content-block types (`tool_result` is the prime vector — command output, file dumps). Value ≠ decision-content, so fidelity survives redaction.
- **Corpus is evidence; the anchor is the verdict; the graveyard is what's overturned** — BECAUSE immutable storage holds dead decisions at full conviction forever; only the anchor (+ graveyard) knows what's currently true.
- **All writes proposed + ratified by Jake in a batch; anchor curation is a SHARED two-navigator job** — BECAUSE Claude is the drift-prone summarizer and Jake's confirm is the second navigator that closes the dead error-correction seam. Claude proactively nominates anchor candidates at decision-time, filtered by *"does this bind future work"* (the `.env` proof: Jake couldn't see its centrality in the moment; Claude could).
- **Invariants carry a destination-level WHY, not a mechanism** — BECAUSE Jake isn't a coder; the why is what lets him drift-catch Claude without holding the how. The keystone that makes the loop self-correcting, not just self-transferring.
- **Apparatus tables stay SEPARATE from Cypher's live schema** — BECAUSE coupling daily build-context to a mid-migration schema means a 1c migration could brick the thing we build with.

## CURRENT STATE
**S10 closed with a redirect.** A live-capture mechanism was specified and partly proven, then refused on principle (see the GRAVEYARD wall). **The input is now Anthropic's official conversation export, full stop.** Most of the S9 re-architecture (pointers, snapshot-id, scrub-at-freeze, retrieval-not-curation) survives the swap unchanged — it was always designed to work on a snapshot, regardless of capture front-end.
- **Locator gate: GREEN** (S9, CC-confirmed against the existing 366MB export): 294 convs / 22,801 globally-unique msg uuids / explicit parent chain in `conversations.json`. Pointer scheme `(conv_uuid, msg_uuid)` is intrinsic to the message.
- **Cred-inventory: RUN** (S10). Real scrub targets in the archive = RTSP camera creds (97), Postgres/Supabase conn strings (55), OpenAI `sk-` (6). The "Stripe" hit was public `pk_live_`, no secret key present.
- **Thinking-in-export: UNVERIFIED.** Whether the official export currently includes thinking blocks alongside text/tool blocks is not confirmed. First S11 action.
- **Skills-catalog crawl: LANDED, ~27,000 entries.** Read `catalog_summary.md`, not the raw 27k; do the fit-judgment at one seat. (Stars≥10 floor caught a long tail past the ~8–9k estimate.)
- **Reference repo:** brought CURRENT by this v4 enshrine + the S10→S11 handoff (was stale at v2/S2 through the entire S9 re-architecture *and* the S10 capture work that's now refused).

## NEXT MOVE (ordered)
1. **Verify the export contents.** Open the current export, document what message-level fields it actually carries (text, content blocks, thinking blocks if present, uuids, parent chain, timestamps, project linkage). This is the precondition for the pipeline; it determines what the scrub and ingest schema have to handle.
2. **Freeze pipeline** — export → scrub all content-block types (logged) → verify-clean → ingest keyed by `(conv_uuid, msg_uuid)` with the parent tree intact. Append-only.
3. **Retrieval substrate** — Supabase+embeddings · single flat file (memvid = single-file counter-design) · or borrow **thedotmack/claude-mem**'s retrieval rig as plumbing (fed pointers/verbatim, not summaries). Informed by the skills catalog and any prior-art reading.
4. **Seed-shape ingest + ratify** — prove the table on a small real batch, ratify before scale (append-only ⇒ un-ratified rows are immortal).
5. **Archive backfill** — run the pipeline at scale over the existing export (~294 convs / 366MB).
6. **Export cadence helper** — a small local helper that watches the Downloads folder for a new `conversations.json` and auto-runs the pipeline. Reduces friction to "click Export, walk away." Optional but high-value for habit formation; lowers the cost of letting exports go stale.
7. **Per-project anchor passes** — hot index/neuron anchors per walled track; `meta` + LRN from the archive.
8. **Cross-export uuid-stability check** — confirm a uuid survives a *re*-export (non-blocking; at next export). Design absorbs both outcomes via snapshot-id.
9. **Storage-seam endgame** — Supabase/Postgres MCP connector on Jake's account; verify with a live round-trip before trusting it.
- **CHEAP WINS (now, independent of the build; S9-vetted):** adopt **berserkdisruptors/contextual-commits** format for anchor/graveyard capture (`rejected()`=graveyard, `constraint()`=invariant, `decision()`=lock, `learned()`=lesson); slot in **Ruya-AI/cozempic** (or **0xhimanshu/governor**) for long-session hygiene; evaluate **PrefectHQ/colin** for anchor currency ("rebuild only what's stale").

## GRAVEYARD

### ⛔ REFUSED — DO NOT RE-OPEN ⛔
> *The mechanism below was specified, partly proven, then **refused on principle** post-S10. The receipts are kept here as history so a future instance doesn't re-derive the same dead end and call it new. **THIS IS CLOSED.** If a fresh read makes the capture mechanism look attractive, **that is the failure mode this wall exists to prevent.** Sanctioned input only — see CURRENT STATE and the floor-input invariant.*
>
> *The specific refusal: standing up a pipeline that hooks claude.ai's internal `chat_conversations` history-fetch endpoint via a browser extension, and persisting the response payloads (including thinking blocks) to a local store. The mechanism is technically tractable; the answer is still no. The reasons hold regardless of intent or whose data it is: it reverse-engineers an undocumented internal surface, it systematically persists hidden reasoning Anthropic deliberately doesn't expose through sanctioned channels, and "it's your own account" doesn't transfer the property to the tool — the tool's shape is what generalizes. Don't re-litigate. Redirect to the official export.*

- **`chat_conversations` history-fetch hook as a capture surface** — REFUSED (post-S10). Out of scope regardless of feasibility. Official export is the sanctioned input.
- **Browser-extension live-capture / "kill the export ping by hooking the network"** — REFUSED (post-S10). Friction on the sanctioned path is real but is not a load-bearing reason; the export cadence helper (NEXT MOVE #6) addresses it without crossing the line.
- *(The S10 receipts below are kept as record of what was learned on the rejected path. They are NOT signposts to revisit it.)*
- "Thinking is live-SSE-only — capture it live or lose it" — falsified by the S10 probe; thinking was found in the (now-rejected) history-fetch payload. Whether it's also in the export is the open verification in CURRENT STATE.
- "DOM scrape would be a viable floor" — lossy; would drop thinking and the message tree. (Moot under the redirect; noted so the lesson isn't relearned if the topic ever resurfaces.)
- "The scrub only needs to redact message text" — wrong; must walk all content-block types because `tool_result` is the prime cred vector. (This lesson is **live** and carried into the export pipeline's scrub — it's not capture-specific.)

### Standing graveyard (carried, still dead)
- **Corpus partitioned by `track` / a `track` column** — KILLED (S2). Re-walls the one-body corpus; hides cross-domain knowledge.
- **"The export's project field IS the track value"** — KILLED (S2). No project↔conversation linkage in `conversations.json` (CC-verified).
- **The verbatim-COPY corpus / `corpus_seed_v1` / the char-diff fidelity gate** — KILLED (S9). Copying verbatim text out of a verbatim archive then char-diffing the copy; replaced by pointers-into-snapshot. (Moot with it: the b2 phantom, locked calls `2526703b`/`077`/`071`/`038` — all about the dead seed.)
- **Manual curation of "salient" exchanges** — KILLED (S9). Replaced by no-discard + retrieval.
- **"Quarantine the cred forever"** — KILLED (S9). Replaced by scrub-at-freeze + wipe-the-raw.
- **Claude-AUTHORED per-chat verbatim floor** — DEAD (S9). The floor is captured (now: from the export), never authored.
- **Parallel chat sessions for gathering** — DEAD (S9). The 12-instance bus trap; gathering = one scaled CC agent.
- **"More files / bigger window fixes it"** — DEAD. Storage was never the lever (S11-the-incident had the fact loaded and failed anyway).
- **"Footer-date freshness tripwire is sufficient"** — DEAD. Checks the wrapper, not the payload.

## CONFIDENCE FLAGS
- **Thinking-in-export** — UNVERIFIED. First S11 action. Design holds either way; revisit only if absence becomes load-bearing.
- **Cross-export uuid stability** — UNVERIFIED. Check at next export by diffing a message present in two snapshots. Design absorbs both outcomes via snapshot-id.
- **Retrieval substrate** — OPEN, pending the skills-catalog read and seed-shape test.
- **Our memory MODEL is differentiated** — HIGH. S9 deep crawl headline: no public repo stores verbatim-by-pointer-into-an-immutable-snapshot; they all extract/summarize/compress. The mechanics around it are borrowable; the model is ours.
- **Within-session drift mitigation** — held clean across S2/S9/S10 (including S10's own redirect — the fresh-instance refusal that surfaced the capture problem *is* the loop working). Keep watching.

---
*Anchored v4 5-27-26 (apparatus S10 close, post-redirect). v3→v4: folded the S10 capture mechanism's specification → refusal → redirect to sanctioned export; reframed working-style mechanics (status line, alignment check, push-back) as conventions rather than invariants; added the **REFUSED — DO NOT RE-OPEN** wall to the graveyard so the rejected path is hard-flagged for future instances; preserved S10 learnings that are still live under the new direction (scrub-walks-all-block-types) and walled the rest as history. v2→v3 (kept for record): folded S9 pointer-into-snapshot + S10 capture work onto v2 base. Confidence HIGH on the redirect; thinking-in-export and cross-export uuid stability remain UNVERIFIED.*
