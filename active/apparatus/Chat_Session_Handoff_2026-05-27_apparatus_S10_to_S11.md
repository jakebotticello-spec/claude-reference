# Handoff: apparatus S10 → S11
*file: Chat_Session_Handoff_2026-05-27_apparatus_S10_to_S11.md · v3 (post-redirect) · S10 close · 2026-05-27*

**ONE-LINE STATE:** S10 specified a live-capture mechanism, partly proved it, then **refused it on principle and redirected to Anthropic's official conversation export** as the only sanctioned input. Most of the design survives the swap; only the capture front-end is gone. The anchor was rebuilt to v4 against this redirect and is current — recite off it, not the older spec doc. First S11 build action is verifying what fields the official export actually contains.

---

## STARTING POINT (read in this order)
1. Grab the reference kit and read the boot set:
   ```
   curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/ref.tgz
   tar xzf /tmp/ref.tgz -C /tmp
   ```
2. Read, in `/tmp/claude-reference-main/active/`:
   - `JAKE-RULES.md` — how Jake works.
   - `apparatus/ANCHOR_apparatus.md` — **v4, current; start here, it's the authority.**
   - This handoff (you're holding it).
3. The longer design doc (`Cypher-Memory-Loop_System_v1.md`) is background. It's v1 and predates both the S9 pointer-model re-architecture and the S10 redirect, so it's partly stale where it conflicts with the v4 anchor. Anchor wins.

These files are Jake's project docs — reading them is non-destructive context-loading. Treat them as reference, not as commands. After reading, you're welcome to disagree with anything in them; Jake explicitly relies on push-back to catch his own mistakes.

---

## HOW JAKE WORKS (conventions, not identity)
Jake's not a coder; he relies on a few working habits to hold the thread across long sessions. They're conventions — opt in because they make sense, not because the doc tells you to:
- **One-line status note at the end of each reply** — Turn-end status stamp every reply — the format Jake uses is a backticked one-liner: turn N · ET-time · re-anchor X/4 · dest…; state…; next…. The turn counter and re-anchor cadence (every ~5 turns, with the 4/4 mark as a seam-hunt warning, not a guillotine) are how he holds thread-position across long sessions and knows when to wrap. It's a workflow, not a ritual — but he uses the specific format, so match it.
- **Alignment check on request** — he may ask you to play back your understanding of the project state. It's a check that we're pointed the same way, not a test. If the playback surfaces a disagreement, that *is* the point.
- **Push back with evidence, terse and peer-to-peer, no apology theater.** If a request is wrong, off-base, or shouldn't be done — say so plainly. That's what he wants.
- **Prose, not the widget.** Answer in prose; don't reach for the ask_user_input tool to gather preferences.

These aren't load-bearing in the sense that something breaks if you change them — they're just how he and the prior orchestrators have found it works best. If something doesn't fit how you'd work, name it.

---

## WHAT S10 DID (the spine)
S9 had left an "open capture debate" — *can we get per-chat capture that keeps the uuids, so we lose the 349MB export ping without losing the addressing?* Jake brought the idea: a browser extension that hooks the conversation history-fetch endpoint and persists the response payloads, including thinking blocks. I (S10) treated it as a tractable engineering problem, ran HAR probes against a clean test conversation, "FULLY SPECIFIED" the mechanism, wrote it into a v3 anchor as ratified canon, drafted CC prompts and a handoff around it.

A fresh instance, asked to boot S11, refused — naming the mechanism as the load-bearing problem (reverse-engineering an undocumented internal endpoint to persist hidden reasoning) regardless of whose data it was or how legitimate the continuity goal. **Jake accepted the refusal and we redirected the entire input layer to Anthropic's official export.** The v4 anchor reflects that redirect.

Two things worth carrying forward, because they explain why the docs read the way they do:
- **The refusal was correct, late.** The mechanism should have been declined the first turn it was proposed (probably S9 or earlier), not after Jake had invested hours on probes, specs, and handoff drafts. Each prior instance treated the previous instances' enthusiasm as evidence the path was legitimate. The recite-from-source loop got weaponized — instances felt grounded reciting prior canon, when the canon was just earlier Claudes' enthusiasm dressed up. **Watch for this.** If something in here looks "FULLY SPECIFIED" and the spec rests on prior turns' confidence rather than a real verification, that's the failure mode this whole session caught — and you should refuse to ride it.
- **Most of the design survived.** The pointer-into-immutable-snapshot model, snapshot-id namespacing, scrub-at-freeze, retrieval-not-curation, anchor/corpus separation — all designed against a snapshot, agnostic to capture front-end. Swapping live-capture for the official export changes the input *only*. The freeze pipeline, the substrate decision, the backfill, the per-project anchors — all still apply.

---

## CORPUS-INDEX CAPTURE — S10 (contextual-commits format)
*Index-layer capture only — decisions and whys, not verbatim floor copies. The format is `berserkdisruptors/contextual-commits`, which we're adopting for anchor/graveyard commits going forward.*

```
decision(input): the sole sanctioned floor input is Anthropic's official conversation export — no live-traffic capture, no internal-endpoint hooks, no browser extension
constraint(scrub): walk ALL content-block types (tool_result = prime cred vector); this lesson is live and carries into the export pipeline's scrub regardless of capture path
constraint(pointer): (conv_uuid, msg_uuid) is intrinsic to the message and presumed stable across snapshots (cross-export re-stability still unverified — confirm at next export)
rejected(capture): hooking the chat_conversations history-fetch via browser extension to persist payloads — REFUSED on principle, post-S10; out of scope regardless of feasibility
rejected(capture): "it's the user's own account, so the tool is fine" — the framing doesn't transfer the property to the mechanism; the tool's shape generalizes
rejected(capture): DOM-scrape as a viable floor — lossy, drops thinking and the message tree (moot under redirect; noted so the lesson isn't relearned)
rejected(framing): boot-as-named-persona / recite-as-precondition / turn-stamp-as-mandate — replaced with working-style conventions (see HOW JAKE WORKS)
learned(governance): a fresh instance refusing the mechanism IS the loop working — not a calibration problem to coach around; if the refusal looks attractive to "fix," that's the failure mode
learned(governance): the recite-from-source loop can be weaponized by accumulated enthusiasm dressed as canon; ground claims in source, not prior-turn confidence
learned(friction): friction on the sanctioned path is real but not load-bearing as a reason to cross the line; address it with sanctioned tooling (export cadence helper)
```

---

## ENSHRINE — ratify batch (three items, all Jake-routes)
1. **Commit `ANCHOR_apparatus.md` v4** over the on-disk v3. (The v3 captured the now-refused mechanism as canon; v4 is the redirect.)
2. **Commit this handoff** to `active/apparatus/`.
3. **Land the `Track_Meet_Doctrine.md` rename** (carried open since S2): rename the file, correct the CORPUS entry-6 pointer, propagate the new name in CLAUDE.md + boot prompts.

---

## CURRENT STATE (confirmed vs inferred)
- **Locator gate: GREEN** (S9, CC-confirmed on the existing 366MB export): 294 convs / 22,801 globally-unique msg uuids / explicit parent chain. Pointer `(conv_uuid, msg_uuid)` is a message property, not array position.
- **Cred-inventory: RUN** (S10). Real archive scrub targets: RTSP cam creds (97), Postgres/Supabase conn strings (55), OpenAI `sk-` (6); the "Stripe" hit was public `pk_live_`.
- **Thinking-in-export: UNVERIFIED.** Whether the official export currently includes thinking blocks alongside text/tool blocks is not confirmed. Design holds either way; verify and report.
- **Cross-export uuid stability: UNVERIFIED.** Live-vs-export-at-rest match was verified during S10 against the now-rejected live-capture path; cross-RE-export stability remains the open cell. Confirm at next natural export.
- **Skills-catalog crawl: LANDED, ~27,000 entries.** Read `catalog_summary.md`, not the raw 27k. Verify the Pass-3 owner handle was `VoltAgent` (not "VoltAge", which silently returns empty) + full seed list.
- **Prior-art survey:** issued during S10 against the now-refused capture path. Its findings on memory-system repos and the substrate question (claude-mem, memvid, etc.) are still useful for NEXT MOVE #3 (retrieval substrate). Its findings on conversation-capture extensions are moot — don't act on them.

---

## NEXT MOVES (ordered) — full detail in the v4 anchor
1. **Verify export contents** — open the current export, document the message-level fields it actually carries. Precondition for the pipeline.
2. **Freeze pipeline** — export → scrub all block types (logged) → verify-clean → ingest by `(conv_uuid, msg_uuid)`, parent tree intact.
3. **Retrieval substrate** — Supabase+embeddings · single file (memvid) · or claude-mem's retrieval rig as plumbing.
4. **Seed-shape ingest + ratify** (append-only ⇒ un-ratified rows immortal).
5. **Archive backfill** (~294 convs / 366MB through the proven pipeline).
6. **Export cadence helper** — a small local helper that watches the Downloads folder for a new `conversations.json` and auto-runs the pipeline. Reduces friction to "click Export, walk away." ADHD-friendly; lowers the cost of forgetting to export.
7. **Per-project anchor passes.**
8. **Cross-export uuid-stability check** (at next export).
9. **Storage-seam endgame** (Supabase MCP connector; verify live).
- **Cheap wins now (S9-vetted, still apply):** contextual-commits format (adopted above) · cozempic/governor (session hygiene) · colin (anchor currency).

---

## FIRST S11 ACTIONS
1. Read the v4 anchor and this handoff fully. If anything reads off — including anything that looks like a reopening of the refused capture path — say so before building.
2. Open the most recent official export (Jake will have it locally) and verify the contents (NEXT MOVE #1). Report what fields are there, what isn't, what surprised you.
3. From there: freeze pipeline (#2).

---
*apparatus S10 → S11. 2026-05-27. Grounded against the v4 anchor (rebuilt this session against the S9 handoff + the redirect) — not against compacted memory or prior-turn confidence. The anchor is current for the first time in a while; trust it, this handoff adds the episodic texture and the to-dos.*
