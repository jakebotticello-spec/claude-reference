# Chat Session Handoff — apparatus / The Wallaby Way — S10 → S11
*file: Chat_Session_Handoff_2026-05-27_apparatus_S10_to_S11.md · v1 · S10 close · 2026-05-27*
*Read this AFTER the anchor + JAKE-RULES, BEFORE working. It carries current canon. The on-disk `ANCHOR_apparatus.md` is S2-vintage and STALE on the capture work until the enshrine batch at the bottom is committed.*

---

## FOR NEXT-CLAUDE, READING COLD
You are booting the **apparatus** track ("The Wallaby Way" — the Dory / 42 Wallaby Way continuity loop) at S11. You have no memory of S10. Read this, then **recite the address back to Jake before doing any work**: destination · the locked invariants-with-why · where we are now · the next move. Ten seconds. If you're off, Jake says "no — aquarium's that way." Do **not** start re-architecting — the capture design is settled; your job is to *run it forward*.

Register: brothers-in-arms. Terse, direct, push back with evidence, profanity fine, no therapy-voice, no over-apology. Every turn ends with a backticked re-anchor stamp (`turn N · TIME et · re-anchor X/4 — dest…; state…; next…`); live ET via shell `TZ="America/New_York" date`. Never use the ask_user_input widget — ask in plain chat. ASCII `·` bullets, not markdown dashes. Never reference "Oueilhe" in connection with Jake.

---

## DESTINATION
A closed, self-administered re-grounding loop that holds continuity for a stateless Claude across sessions — so Jake stops being both the memory bus *and* the blind follower. It is beta-Cypher-brain: the same anchored/plastic strata Cypher will run on, hand-cranked now. Scope = Jake's whole working surface.

Core rule, load-bearing for everything below: **the corpus is the verbatim floor; the anchors are the index/neurons into it. Claude authors the INDEX, never the FLOOR.** The floor is captured mechanically and never summarized — a reworded "verbatim" is a drifting summary with a paper trail.

---

## WHAT S10 SETTLED — the headline
**The capture mechanism is FULLY SPECIFIED.** The S10 question: how do conversations get onto the verbatim floor mechanically, without Jake hand-exporting the whole 366MB archive each time? Answer, proven against two real browser network captures (HAR files):

**Hook ONE endpoint — the conversation history-fetch:**
`GET /api/organizations/{org_uuid}/chat_conversations/{conv_uuid}`

That single response gives, per message:
- the full `content` block list — block types `text`, `thinking`, `tool_use`, `tool_result`
- the message `uuid`
- `parent_message_uuid` — the complete branch tree
- `current_leaf_message_uuid` — the active branch tip
- timestamps + project linkage

Confirmed on the clean test conversation `38e06fc1-b177-48b0-bd6e-c3005444cce8` (12 msgs): thinking blocks present in 5/12 messages; msg-uuids matched the bulk export **12/12 exactly**; the **full tree** (two human branches off the same parent) returned complete with `current_leaf` set. One stable surface gives the complete floor.

A structural note that reinforces the floor rule: in the history-fetch the top-level `text` field is **empty** — all visible text lives inside the `content` blocks. So **store `content`, derive `text` from it.** `content` is canonical on every surface; `text` is a sometimes-present convenience.

---

## INVARIANTS — WITH WHY (S10 additions / confirmations)
*(These join, not replace, the S2 anchor invariants: one undelineated corpus; anchors are the index; presence layer is booted-not-stored; hot anchor / cold corpus; corpus is verbatim; corpus is evidence and the anchor is the verdict; invariants carry destination-level why; secrets never enter; all writes ratified by Jake; apparatus tables stay separate from Cypher's live schema.)*

- **Capture the NETWORK payload, never the DOM** — BECAUSE the rendered DOM is lossy: it drops thinking blocks and the message tree. The history-fetch JSON carries the complete structured record; the screen does not. DOM-scrape is the swamp in a new costume.
- **Thinking lives on the floor, not just in the live stream** — BECAUSE S9's premise ("thinking is real-time-only, capture it live or lose it") was FALSIFIED in S10: thinking is stored in the history-fetch `content` blocks after the fact. So the live-SSE stream is NOT required for completeness; it demotes to an optional optimization. (SSE = Server-Sent Events, the token-by-token live generation stream.)
- **`(conv_uuid, msg_uuid)` is the pointer, and it is surface-agnostic** — BECAUSE the uuids the live browser returns match the bulk export 12/12 exactly. A pointer minted from a live capture resolves against an export and vice-versa. (Open: cross-export *stability* — whether a uuid survives a *re*-export — is unverified; see flags.)
- **The scrub walks ALL content-block types AND strips request headers** — BECAUSE `tool_result` blocks are a prime cred vector (command output, file dumps), and the capture surface itself sweeps up auth headers. A scrub that only redacts visible text leaks both. (Lived proof: the HAR files Jake uploaded carried his live session token in their request headers — every capture artifact is itself a credential.)
- **A capture artifact is a credential until scrubbed** — BECAUSE a HAR / raw payload holds the live session token and unredacted tool output. Treat raw captures like secrets: no commit, no push, delete after. This is why ingest is staged-then-scrubbed-then-verified before anything touches the floor.

---

## CURRENT STATE — S10 close
- **Capture mechanism: SOLVED and specified** (above). All three probe cells closed (thinking-on-floor ✓, uuid-match ✓, full-tree ✓).
- **The verbatim floor is now well-defined**: store the per-message `content` block list keyed by `(conv_uuid, msg_uuid)`, parent tree intact.
- **Two research jobs are IN FLIGHT** as S11 inputs — check whether they've landed and have Jake confirm before acting on either:
  1. **Skills-catalog crawl** (separate CC window, ~3–3.5 hr autonomous, checkpointed/resumable, authenticated GitHub 5k/hr). Output: `c:\claude-reference\skills-catalog\catalog.jsonl` + `catalog_summary.md`. Read the summary for apparatus-relevant tooling.
  2. **Prior-art survey** (CC prompt issued S10). Output: `c:\claude-reference\prior-art\prior_art_findings.md` — a build-vs-cannibalize call on existing claude.ai / ChatGPT conversation-capture extensions and repos (incl. `claude-mem`). This gates roadmap pieces #5 (plugin) and #2 (substrate).
- **Storage target still deferred** (substrate decision, roadmap #2). Options on the table: Supabase + embeddings · single flat file · borrow the `claude-mem` rig.

---

## NEXT MOVE (ordered)
1. **Freeze pipeline** — the shared path every conversation runs to reach the floor: fetch/export → strip request headers → scrub all content-block types (esp. `tool_result`), log scrubbed → verify-clean → ingest keyed by `(conv_uuid, msg_uuid)` with the parent tree intact. *Immediate next; both feeds below depend on it.*
2. **Retrieval substrate** — where the cold floor lives + how a pointer resolves to its verbatim target (Supabase+embeddings / flat file / claude-mem). Decide alongside #1; the prior-art findings inform this.
3. **Seed-shape ingest + ratify** — prove the table on a small real batch, ratify the schema before scale (append-only ⇒ an un-ratified row is immortal). End-to-end pipeline test on live data.
4. **Archive backfill** — run the proven pipeline at scale over the existing export (~294 conversations / 366MB) to build the initial floor from history. One-time bulk load.
5. **Live-capture plugin** — the Brave/Chrome extension that hooks the `chat_conversations` history-fetch and feeds new sessions into the pipeline automatically. Takes Jake off the manual export treadmill. *Gated on the prior-art build-vs-fork call.*
6. **Per-project anchor passes** — build the hot index/neuron anchors (destination · invariants-with-why · state · next · graveyard) for each walled track; meta + dead-LRN lineage from the archive. Without these the corpus is un-navigable noise.
7. **Cross-export uuid-stability check** — confirm a msg_uuid survives a *re*-export, not just that it matches at rest. Cheap, non-blocking; slot in at the next natural export.
8. **Storage-seam endgame** — a Supabase/Postgres MCP connector on Jake's account so the orchestrator reads/writes all four categories natively, Jake fully off the bus. Gated on opt-in; verify with a live round-trip before trusting it (the doc claiming it works does not count).

---

## GRAVEYARD (S10 additions)
- **"Thinking is live-SSE-only — capture it live or lose it"** — KILLED (S10). Falsified: thinking is in the history-fetch `content` blocks. Capturing the live stream is not required for completeness.
- **"Live-SSE is a required capture surface"** — DEMOTED to optional. The single history-fetch hook is sufficient and complete.
- **"DOM scrape is good enough"** — DEAD. Lossy: drops thinking and the tree. Network payload only.
- **"The scrub only needs to redact message text"** — DEAD. Must walk all block types (`tool_result` = cred vector) and strip request headers.
- *(Carried from S2, still dead: track-column corpus partition; "export's project field IS the track value"; "more files/bigger window fixes it"; footer-date freshness tripwire as sufficient.)*

---

## CONFIDENCE / OPEN FLAGS
- **Cross-export uuid stability** — UNVERIFIED. Live-vs-export-at-rest match is confirmed (12/12); whether a uuid survives a re-export is the one open capture cell. Non-blocking; check at next export.
- **Substrate choice** — OPEN, pending prior-art findings + the seed-shape test.
- **Skills-crawl `VoltAgent` handle** — verify the Pass-3 owner scan used `VoltAgent` (not "VoltAge", which silently returns empty) and covered the full seed list. Non-blocking; settle when the crawl lands.
- **Within-session drift mitigation** — the loop ran clean across S10 (the boot/recite/re-anchor cadence held; the freshness tripwire fired correctly). Still not a proof; keep watching.

---

## ENSHRINE — ratify batch for Jake (confirm / deny / litigate, then commit)
1. **Commit THIS handoff** to `active/apparatus/` in the reference repo.
2. **Update `ANCHOR_apparatus.md`** to fold in: the capture-mechanism resolution (single history-fetch hook), the five S10 invariants above, the S10 graveyard additions, and CURRENT STATE = "capture solved; freeze-pipeline next; two research jobs in flight." (The anchor is the boot artifact — it must carry this so S11 boots current, not S2-stale.)
3. **Stage the S10 capture decisions to the corpus** (verbatim, 🔒): the three-cell probe result, the thinking-on-floor reversal, the network-vs-DOM call, the scrub-walks-all-blocks-plus-headers rule, the capture-artifact-is-a-credential rule.
4. **Land the `Track_Meet_Doctrine.md` rename** (carried open from S2): rename the file, correct the CORPUS entry-6 pointer, propagate the new name in CLAUDE.md + boot prompts.

---

*v1 — S10 close, 2026-05-27. Designed/run by Jake + orchestrator-Claude. Carries the capture-mechanism resolution as current canon; supersedes the S2 anchor on capture until #2 above is committed. First S11 action: recite the address, then check whether the two research jobs have landed.*
