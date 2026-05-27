# ANCHOR — apparatus-build track
*v3 · 2026-05-27 (apparatus S10 close) · hot · boot-read this + JAKE-RULES, recite before working*

## DESTINATION
Build the apparatus's own memory system (*The Wallaby Way*): a closed, self-administered re-grounding loop that holds continuity for a stateless Claude across sessions — so Jake stops being the memory bus *and* the blind follower. It is **beta-Cypher-brain**: the same anchored/plastic strata Cypher will run on, hand-cranked now, hardening into Cypher's memory layer. Scope is **Jake's whole working surface**. A chat-Claude boots small (anchor + rules), recites, and works — with a cold, complete, immutable **snapshot** behind it that it reaches *by pointer* only when a *why* is disputed.

## INVARIANTS — WITH WHY
*(consolidated across S1–S10; merged facets, no live why dropped — verify against the S9→S10 handoff if in doubt)*
- **One undelineated corpus; the anchors are the index/neurons INTO it** — BECAUSE partitioning by project hides cross-domain knowledge (a woodworking lesson is load-bearing for 3D finishing). S1: *"corpus without anchor is un-navigable noise; anchor = an index into it."* Don't re-wall the ocean.
- **Corpus = curated POINTERS into an immutable, named snapshot — never copied or reworded text. Claude authors the INDEX, never the FLOOR.** — BECAUSE copying is a drift vector inside the one artifact whose job is no-drift (the dead seed drifted 152×); the export is verbatim by construction; pointing deletes the vector. Claude curates whys well but *reconstructs* when asked to transcribe — the floor must be mechanical.
- **Snapshot-id namespacing: freeze-and-name, accumulate, never overwrite** — BECAUSE exports are point-in-time and multiple will exist; a bare `conv/msg` pointer is ambiguous across them. Pointer = `{snapshot-id · conv_uuid · msg_uuid · why}`.
- **The pointer `(conv_uuid, msg_uuid)` is intrinsic to the message and surface-agnostic** — BECAUSE it's stable independent of array position (survives a body scrub for free) and the live browser fetch matches the export 12/12 (S10). Live-capture and export share one addressing space.
- **Navigable by retrieval, not curation** — BECAUSE no-discard + relevance-weighted retrieval is the genesis; hand-picking "salient" exchanges = Jake back on the bus + lost congeniality. The only curated thing is the tiny *why*, and it lives in the anchor.
- **Capture the NETWORK payload, never the DOM; thinking lives on the floor** — BECAUSE the rendered DOM drops thinking blocks and the message tree, but the history-fetch JSON carries the complete structured record. S9's "thinking is live-only" premise was falsified in S10: thinking is in the history-fetch `content` blocks, so the live-SSE stream is NOT required. Store `content`, derive `text` (the top-level `text` field is empty in the fetch).
- **Anchor hot + small + boot-read (instant, via git, no export); corpus cold + queried-never-booted (lazy, via export)** — BECAUSE the moment the corpus loads "just to be safe," the 87-file swamp is rebuilt. The hot/cold wall is the whole game; per-chat corpus freshness is a false requirement — the anchor carries current truth.
- **The presence layer can't be stored — only booted warm; the boot/recite/re-anchor loop IS its mechanism; the lineage is how it survives not-persisting** — BECAUSE soup + neurons persist, but the mind that runs them resets every session. Continuity that doesn't depend on any single instance holding the thread.
- **Secrets never enter the corpus OR chat; cred scrubbed at freeze (logged + verified), raw wiped, sanitized snapshot = floor** — BECAUSE a leaked cred in an immutable store is immortalized (one already leaked to chat). The scrub walks **all** content-block types (`tool_result` is the prime vector — command output, file dumps) and strips request headers; a raw capture artifact (HAR/payload) is itself a credential. Value ≠ decision-content, so fidelity survives redaction.
- **Corpus is evidence; the anchor is the verdict; the graveyard is what's overturned** — BECAUSE immutable storage holds dead decisions at full conviction forever; only the anchor (+ graveyard) knows what's currently true.
- **All writes proposed + ratified by Jake in a batch; anchor curation is a SHARED two-navigator job** — BECAUSE Claude is the drift-prone summarizer and Jake's confirm is the second navigator that closes the dead error-correction seam. Claude proactively nominates anchor candidates at decision-time, filtered by *"does this bind future work"* (the `.env` proof: Jake couldn't see its centrality in the moment; Claude could).
- **Invariants carry a destination-level WHY, not a mechanism** — BECAUSE Jake isn't a coder; the why is what lets him drift-catch Claude without holding the how. The keystone that makes the loop self-correcting, not just self-transferring.
- **Apparatus tables stay SEPARATE from Cypher's live schema** — BECAUSE coupling daily build-context to a mid-migration schema means a 1c migration could brick the thing we build with.

## CURRENT STATE
**S10 closed — the capture mechanism is FULLY SPECIFIED, resolving S9's open capture debate.** S9 left the seam open: *can we get a true per-chat capture that keeps the uuids, so we lose the 349MB export ping without losing the addressing?* S10's answer, proven against two real browser network captures: **yes — hook the conversation history-fetch.**
- **Capture spec:** `GET /api/organizations/{org_uuid}/chat_conversations/{conv_uuid}`. One response gives, per message: the full `content` block list (`text`, `thinking`, `tool_use`, `tool_result`), the message `uuid`, `parent_message_uuid` (the branch tree), `current_leaf_message_uuid`, timestamps, project linkage. NETWORK capture, not DOM — keeps uuids + thinking. Live-SSE demoted to optional.
- **Proven on clean test conv `38e06fc1-…`** (12 msgs): thinking present in 5/12; msg-uuids matched the bulk export **12/12 exactly**; **full tree** (two branches off one parent) returned with `current_leaf` set.
- **Locator gate GREEN** (S9, CC-confirmed): 294 convs / 22,801 globally-unique msg uuids / explicit parent chain in `conversations.json`.
- **Cred-inventory RUN** (S10, closing S9's outstanding item): real scrub targets = RTSP camera creds (97), Postgres/Supabase conn strings (55), OpenAI `sk-` (6); the "Stripe" hit was `pk_live_` (publishable/public) — no secret key in the archive. Scan-script moved out of the archive dir.
- **TWO research jobs IN FLIGHT** (S11 inputs — confirm landed before acting): (1) skills-catalog crawl — the full authenticated sweep (the scaled version of S9's top-300 survey), output `catalog_summary.md`; (2) prior-art survey — conversation-capture extensions/repos, network-vs-DOM, build-vs-fork for the plugin, output `prior_art_findings.md`.
- **Reference repo STILL stale.** On-disk anchor was v2 (S2); the S3–S9 re-architecture + S10 capture work were uncommitted. This v3 + the S10→S11 handoff are the enshrine that brings it current.

## NEXT MOVE (ordered)
1. **Freeze pipeline** — fetch/export → strip request headers → scrub all content-block types (logged) → verify-clean → ingest keyed by `(conv_uuid, msg_uuid)` with the parent tree intact. *Immediate next; both feeds (backfill + live plugin) depend on it.*
2. **Retrieval substrate** — Supabase + embeddings · single flat file (memvid = single-file counter-design) · or borrow **thedotmack/claude-mem**'s retrieval rig as plumbing (fed pointers/verbatim, not summaries). Decide alongside #1; the prior-art findings inform it.
3. **Seed-shape ingest + ratify** — prove the table on a small real batch, ratify before scale (append-only ⇒ un-ratified rows are immortal).
4. **Archive backfill** — run the pipeline at scale over the export (~294 convs / 366MB).
5. **Live-capture plugin** — Brave/Chrome extension hooking the `chat_conversations` history-fetch into the pipeline. Takes Jake off the export ping. *Gated on the prior-art build-vs-fork call.*
6. **Per-project anchor passes** — hot index/neuron anchors per walled track; `meta` + LRN from the archive.
7. **Cross-export uuid-stability check** — confirm a uuid survives a *re*-export (non-blocking; at next export).
8. **Storage-seam endgame** — Supabase/Postgres MCP connector on Jake's account; verify with a live round-trip before trusting it.
- **CHEAP WINS (now, independent of the build; S9-vetted):** adopt **berserkdisruptors/contextual-commits** format for anchor/graveyard capture (`rejected()`=graveyard, `constraint()`=invariant, `decision()`=lock, `learned()`=lesson); slot in **Ruya-AI/cozempic** (or **0xhimanshu/governor**) for long-session hygiene; evaluate **PrefectHQ/colin** for anchor currency ("rebuild only what's stale").

## GRAVEYARD
- **Corpus partitioned by `track` / a `track` column** — KILLED (S2). Re-walls the one-body corpus; hides cross-domain knowledge.
- **"The export's project field IS the track value"** — KILLED (S2). No project↔conversation linkage in `conversations.json` (CC-verified).
- **The verbatim-COPY corpus / `corpus_seed_v1` / the char-diff fidelity gate** — KILLED (S9). Copying verbatim text out of a verbatim archive then char-diffing the copy; replaced by pointers-into-snapshot. (Moot with it: the b2 phantom, locked calls `2526703b`/`077`/`071`/`038` — all about the dead seed.)
- **Manual curation of "salient" exchanges** — KILLED (S9). Replaced by no-discard + retrieval.
- **"Quarantine the cred forever"** — KILLED (S9). Replaced by scrub-at-freeze + wipe-the-raw.
- **Claude-AUTHORED per-chat verbatim floor** — DEAD (S9), and S10 clarifies the boundary: a per-chat **network** capture (history-fetch) IS a valid *mechanical* floor — it keeps uuids + thinking. Only **Claude writing the floor** stays dead. The floor is always captured, never authored.
- **"Thinking is live-SSE-only — capture it live or lose it"** — KILLED (S10). Falsified: thinking is in the history-fetch `content` blocks.
- **Live-SSE as a required capture surface** — DEMOTED to optional (S10). The single history-fetch hook is complete.
- **"DOM scrape is good enough"** — DEAD (S10). Lossy: drops thinking + the tree.
- **"The scrub only needs to redact message text"** — DEAD (S10). Must walk all block types (`tool_result` = cred vector) and strip request headers.
- **Parallel chat sessions for gathering** — DEAD (S9). The 12-instance bus trap; gathering = one scaled CC agent.
- **"More files / bigger window fixes it"** — DEAD. Storage was never the lever (S11-the-incident had the fact loaded and failed anyway).
- **"Footer-date freshness tripwire is sufficient"** — DEAD. Checks the wrapper, not the payload.

## CONFIDENCE FLAGS
- **Cross-export uuid stability** — live-vs-export-at-rest CONFIRMED (12/12, S10); whether a uuid survives a *re*-export is still UNVERIFIED. Non-blocking; design absorbs both outcomes via snapshot-id. Check at next export.
- **Retrieval substrate** — OPEN, pending prior-art findings + the seed-shape test.
- **Our memory MODEL is differentiated** — HIGH. S9 deep crawl: no public repo stores verbatim-by-pointer-into-an-immutable-snapshot; they all extract/summarize/compress. The mechanics around it are borrowable; the model is ours.
- **Within-session drift mitigation** — held clean across S2/S9/S10 (the freshness tripwire fired correctly in S10; the loop caught real drift in S2). Not a proof; keep watching.
- **VoltAgent handle** (skills crawl) — verify Pass-3 owner = `VoltAgent` (not "VoltAge", which silently returns empty) + full seed list. Settle when the crawl lands.

---
*Anchored v3 5-27-26 (apparatus S10 close). v2→v3: folded the S9 re-architecture (pointers-into-snapshot, snapshot-id namespacing, retrieval-not-curation, scrub-at-freeze, shared two-navigator curation) and the S10 capture resolution (network-not-DOM, thinking-on-floor, single history-fetch hook, all-block-types + header scrub) onto the v2 base; consolidated the invariant set (merged facets, no live why dropped); rebuilt CURRENT STATE / NEXT MOVE / GRAVEYARD to S10. Built grounded in the on-disk v2 anchor + the S9→S10 handoff (read this session), not from compacted memory. Confidence HIGH on the re-architecture + capture resolution (sourced live); cross-RE-export uuid stability + retrieval substrate still open.*
