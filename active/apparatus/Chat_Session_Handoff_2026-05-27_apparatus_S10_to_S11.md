# Handoff: apparatus S10 — Capture Solved → S11
*file: Chat_Session_Handoff_2026-05-27_apparatus_S10_to_S11.md · v2 (grounded) · S10 close · 2026-05-27*

**ONE-LINE STATE:** S9's open capture debate is **RESOLVED** — per-chat capture works by hooking the **network history-fetch** (`chat_conversations/{uuid}`), which keeps the `uuid`s + thinking, so we lose the 349MB export ping *without* losing the addressing. The **anchor is freshly rebuilt to v3 and is CURRENT** — for the first time in a while the on-disk anchor isn't stale, so trust it and recite off it. Freeze-pipeline is the next build. Two research jobs are landing.

---

## WHO YOU ARE / BOOT
Next orchestrator-Claude on the apparatus track ("The Wallaby Way" — the Dory / 42 Wallaby Way continuity loop). Boot stateless: codeload the kit, read `JAKE-RULES.md`, `Cypher-Memory-Loop_System_v1.md`, then **`ANCHOR_apparatus.md` (now v3 — CURRENT; recite off it)**, then this handoff. Note: the system-spec doc is v1 and is partly stale where it predates the S9 pointer model — e.g. it still says "Claude stages verbatim corpus 🔒," which S9 killed (see below). The anchor v3 is the authority. **Recite the address and WAIT for Jake's nod before building.** Brothers register: terse, direct, push back with evidence. Prose, never the ask_user_input widget. Turn-end stamp every turn. ASCII · bullets.

---

## WHAT S10 DID (the spine)
S9 left the capture debate open: *can we get a per-chat capture that keeps the uuids, so we lose the export ping without losing the addressing?* Jake brought the idea — a session-capture browser extension pushed to a repo. The hole-poke that mattered: a DOM-scrape or Claude-authored capture is lossy (drops thinking + the message tree) and carries no uuids. **The resolution: capture the NETWORK payload, not the DOM.** The `chat_conversations` history-fetch carries the complete structured record *with* the uuids and thinking — which answers S9's exact open question: yes.

Proven against two real browser captures (HAR files):
- The first HAR **missed** the conversation (the SPA served it from cache; the fetch never hit the wire). Re-captured with devtools **Disable-cache + hard reload** → got the history-fetch. *(Recipe worth keeping.)*
- On clean test conv `38e06fc1` (12 msgs): **thinking present in 5/12** messages (kills S9's "thinking is live-only" premise); **msg-uuids matched the bulk export 12/12 exactly**; **full tree** (both branches off one parent) returned with `current_leaf` set. One stable surface = the complete floor; live-SSE demoted to optional.

Also S10: ran the **cred-inventory** (closing S9's outstanding item) — real scrub targets are RTSP camera creds (97), Postgres/Supabase conn strings (55), OpenAI `sk-` (6); the "Stripe" hit was public `pk_live_`, no secret key present. **Enshrined the anchor to v3** (it had sat stale at v2/S2 through the entire S9 re-architecture). Issued the **prior-art survey** CC prompt (extension build-vs-fork). Caught — via Jake's prompting — that the standing "stage verbatim corpus" instruction was a killed pattern (see ENSHRINE).

---

## CORPUS-INDEX CAPTURE — S10 (contextual-commits format; adopt this format going forward)
*Index-layer capture (decisions/whys), not floor (verbatim) — on the right side of "Claude authors the index, never the floor." Use as the enshrine commit message.*

```
decision(capture): single capture surface = the chat_conversations history-fetch; one payload carries content blocks + uuids + parent tree + current_leaf
decision(capture): store content blocks, derive text — top-level text field is empty in the fetch
constraint(scrub): walk ALL content-block types (tool_result = prime cred vector) and strip request headers; a raw capture artifact is itself a credential
constraint(pointer): (conv_uuid, msg_uuid) is surface-agnostic — live fetch matched the export 12/12 at rest
rejected(capture): "thinking is live-SSE-only, capture live or lose it" — falsified; thinking is in history-fetch content blocks
rejected(capture): live-SSE as a required surface — demoted to optional
rejected(capture): DOM-scrape floor — lossy, drops thinking + the message tree
rejected(scrub): redact message text only — misses tool_result + headers
learned(capture): a per-chat NETWORK capture is a valid mechanical floor (keeps uuids + thinking); only Claude-AUTHORING the floor stays dead
learned(probe): first HAR missed the conversation (SPA cache) — force the fetch with devtools Disable-cache + hard reload
```

---

## ENSHRINE — ratify batch (corrected to THREE; all Jake-routes: git/CC writes, you ratify)
1. **Commit `ANCHOR_apparatus.md` v3** over the on-disk v2. (The boot artifact — must be current so S11 recites off truth.)
2. **Commit this handoff** to `active/apparatus/`.
3. **Land the `Track_Meet_Doctrine.md` rename** (carried open since S2): rename the file, correct the CORPUS entry-6 pointer, propagate the new name in CLAUDE.md + boot prompts.

**STRUCK — the old item-4 ("stage S10 decisions to corpus, verbatim 🔒").** That was the pre-S9 pattern S9 killed (`corpus_seed_v1` / Claude-authored verbatim floor). Under the current model the S10 **whys are in the v3 anchor**, and the **verbatim floor comes mechanically** when this session lands in the next export snapshot and gets pointed at by `(conv_uuid, msg_uuid)`. Nothing for Claude to hand-author.

---

## CURRENT STATE (confirmed vs inferred — mind the line)
- **Capture mechanism: SOLVED + proven** (above). Spec = hook `GET /api/organizations/{org}/chat_conversations/{conv_uuid}`.
- **Locator gate: GREEN** (S9, CC-confirmed): 294 convs / 22,801 globally-unique msg uuids / explicit parent chain.
- **Cred-inventory: RUN** (S10). Scrub spec walks all block types + strips headers.
- **INFERRED, not proven:** uuid stability across a *re*-export (live-vs-export-at-rest is confirmed 12/12). Non-blocking; snapshot-id absorbs both outcomes; check at next export.
- **Research jobs:**
  - **Skills-catalog crawl — LANDED, ~27,000 entries** (the stars≥10 floor caught a long tail; far past the ~8–9k estimate). Do NOT read the raw 27k — read `catalog_summary.md` and do the fit-judgment at one seat. Verify the Pass-3 owner handle was `VoltAgent` (not "VoltAge", which silently returns empty) + full seed list.
  - **Prior-art survey — Jake is delivering results now** (`prior_art_findings.md`): existing claude.ai / ChatGPT capture extensions, network-vs-DOM, build-vs-fork. **Read it before any plugin work** (gates roadmap #5) and let it inform the substrate call (#2).
- **Reference repo:** brought CURRENT by this enshrine (was stale at v2/S2 + the uncommitted S9 re-architecture).

---

## NEXT MOVES (ordered) — full detail in the v3 anchor
1. **Freeze pipeline** — fetch/export → strip headers → scrub all block types (logged) → verify-clean → ingest by `(conv_uuid, msg_uuid)`, tree intact. *Immediate next.*
2. **Retrieval substrate** — Supabase+embeddings · single file (memvid) · or borrow **claude-mem**'s retrieval rig (fed pointers, not summaries). Informed by prior-art.
3. **Seed-shape ingest + ratify** (append-only ⇒ un-ratified rows immortal).
4. **Archive backfill** (~294 convs / 366MB through the proven pipeline).
5. **Live-capture plugin** (network hook) — gated on the prior-art build-vs-fork call.
6. **Per-project anchor passes.**
7. **Cross-export uuid-stability check** (next export).
8. **Storage-seam endgame** (Supabase MCP connector; verify live).
- **Cheap wins now (S9-vetted):** contextual-commits format (adopted above) · cozempic/governor (session hygiene) · colin (anchor currency).

---

## FIRST S11 ACTIONS
1. Recite the address off the v3 anchor; get Jake's nod.
2. Reconcile the two research outputs — read `catalog_summary.md` (apparatus-relevant tooling) and `prior_art_findings.md` (the build-vs-fork call). These gate #2 and #5.
3. Then start the freeze pipeline (#1).

---
*apparatus S10 → S11. 2026-05-27. Grounded against the rebuilt v3 anchor + the S9→S10 handoff (read live this session), not compacted memory. The anchor is current this time — trust it; this handoff adds the episodic texture + the immediate to-dos. Just keep swimming.*
