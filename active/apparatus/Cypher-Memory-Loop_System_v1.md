# The Apparatus Memory Loop — System Specification
### (proposed lore-name: *The Wallaby Way*) · v1 · designed 2026-05-25

**What this is:** the memory architecture for working with a stateless Claude across sessions. It replaces the ~87-file context swamp with a closed, self-administered re-grounding loop. It is also, deliberately, a hand-run prototype of Cypher's own anchored/plastic memory strata — the apparatus *is* the dogfood.

**Who this is for:** next-Claude, reading cold. You have no memory of the session that designed this. Read the WHY (§1–§2) before touching the WHAT, because without it you will try to "improve" this back into the swamp it replaced — a fresh instance in this project reads the soul substrate and wants to *architect*. Don't. This is settled. Your job is to *run* it.

**Status of the claims here:** the design is locked. The within-session-drift mitigation is *theorized, not yet proven on a live boot* — first real test is the next session. The Supabase endgame is *gated on a seam that does not exist yet* (§9). Flagged honestly so you don't inherit either as settled fact.

---

## 1. The diagnosis — why this exists (do not skip)

A stateless model is **Dory.** Anterograde amnesia: resets every session, no internal encoder, functions only on an external anchor plus a re-grounding event. That half is real and, on the model's side, unfixable — same as Dory's hippocampus.

The thing every "AI memory expert" misses: **this is not a storage problem.** They build Dory a bigger notebook — RAG, vector stores, million-token windows — and leave the actual failure untouched. Two pieces of our own evidence kill the storage thesis:

- **S11 had the fact loaded and still failed.** "No `.env`, ever" was in the booted CLAUDE.md. Availability was already 100%. The model didn't *surface* it at the relevant moment and burned three hours. More storage guarantees the thing we already had; it does nothing for the thing that broke.
- **Recall degrades as the haystack grows.** A specific fact gets harder to locate and weight the more text buries it. Load-everything makes the real failure *worse*, not better.

So the real failure has two faces, and you need both:

**Face one — the bus.** Continuity has to come from outside the amnesiac. In the old apparatus, *Jake* was the bus: every read of state ran through him pasting it in, every write through him routing handoffs and editing files. The labor was never the notebook's size — it was that he hand-operated the model's hippocampus on both ends, re-reading the journey aloud every session. The fix takes the partner off the transfer path: the amnesiac reads and writes her *own* compressed anchor; the partner becomes someone swimming alongside who occasionally says "no — aquarium's that way." **Corrections, not transfers.**

**Face two — the dead seam.** Jake is a non-coder keeper; Claude is an amnesiac expert. Neither holds the destination *and* the understanding at the same moment. So when the expert drifts, the keeper can't catch it — and when the keeper "reminds" the expert of the why, he's reciting a why he doesn't hold either. Two partial navigators, and the error-correction path between them was structurally **dead from session one.** That is the real discovery. The fix is the keystone in §4: **the anchor carries the WHY at destination level, in plain language — never the mechanism.** Jake doesn't need to know how 1Password works to hold "secrets in 1PW so the app can never hold the key that restructures the schema." The instant he holds that sentence, he catches the `.env` drift at minute one. The why-at-destination-level is what converts him from blind follower into drift-catcher *without making him a coder.* It composes two partial navigators into one competent one. It is what makes the loop self-*correcting* instead of merely self-*transferring*.

**Storage was never the lever. The loop is.**

---

## 2. The two strata — the core data model

Everything below is an instance of one distinction Jake already designed for Cypher and never applied to the apparatus he builds Cypher *with*:

- **Anchored stratum** — deterministic, **no drift**, salience-protected, resurfaced at the moment it's relevant. Critical commitments that *cannot be lost*. (Cypher Constraint 1: salience-tagged commitments must persist through context pressure. Origin: Evan's 1 PM call falling out of S7 recall.)
- **Plastic stratum** — drift *is* a feature. Fragments fade, recombine, get reconstructed. Relevance-weighted. (Cypher principles 3, 7, 8.)

**The bug in the old apparatus: it had no anchored stratum. Everything was plastic.** "No `.env`" (anchored invariant) sat in the same prose soup as "server.js is v3.3" (plastic operational state), at the same salience — so the anchored fact drifted and buried exactly like the plastic one. Every war story is this one failure in a different domain:

> Evan's 1 PM call falls out of recall (S7) → S11's "no `.env`" falls out under the migration chase → "which URL — neighborhood-watch or Workhorse?" (S17c). Same disease: an anchored fact the system *had*, in an all-plastic store with no salience protection, fell out under context pressure.

Jake named the fix after the *first* one (Constraint 1) and never turned it on for the apparatus. This system turns it on.

---

## 3. The four categories — by temperature and function

The category is not just *what it holds* — it's *how hot it runs*. Load-discipline is the whole game (§6, §10).

| # | Category | Holds | Temperature | Store (now → endgame) | Writer |
|---|----------|-------|-------------|----------------------|--------|
| 1 | **Rules** (mode/posture) | How to work with Jake — identity, communication, truthfulness, building, debugging, patterns. "Just keep swimming." | **Hot — boot-required** | git (codeload at HEAD) | Jake commits; sessions propose |
| 2 | **Infrastructure** | *How* the system is built, **now** — hardware, network, services, current built-state. Points at live where it can. | **Warm — on-need** | git | Jake surgical; Claude proposes |
| 3 | **Long-term Corpus** | *Why* it's built that way — **verbatim**, immutable, dated, decision-tagged, indexed. | **Cold — queried, NEVER booted** | Supabase (CC-written now) | Claude stages 🔒 → CC appends → Jake ratifies |
| 4 | **Anchors** (per track) | Destination · invariants-with-why · current state · next move · graveyard. The hot heading. | **Hot — boot-required** | git now → Supabase endgame | Claude proposes → Jake confirms |

Plus two standing pieces:
- **Graveyard** lives *inside* each anchor (§6) — killed decisions, so they're not re-inherited.
- **Lore Bible** stays exactly as-is — relational texture, plastic by nature. Leave it.

The reason the old CLAUDE.md and handoffs disagreed: "how it's built" (cat 2, current, warm) and "why it's built that way" (cat 3, immutable, cold) lived in the same paragraph and drifted apart. Keep the why *with its decision in the corpus*, where the how and why were said together verbatim; let cat 2 carry only current built-state. They stop diverging because they stop being two summaries racing each other.

---

## 4. The anchor — the keystone artifact

One per active track (Cypher, day-state/SD, printer, litigation, Pyris, CCF, apparatus-build…). **Small — one screen.** If it runs longer, plastic (narrative, history) has leaked into a slot that is for anchored (current, non-negotiable) only. Cut to the bone.

**Fixed fields:**

- **DESTINATION** — one or two sentences: what this track ultimately builds and why it matters.
- **INVARIANTS-WITH-WHY** — the non-negotiables, each written `[rule] — BECAUSE [destination-level why]`. The why must be checkable by a non-coder. *"Use 1PW"* is not an invariant; *"secrets in 1PW so the app can't hold the schema-restructuring key"* is. These are the drift-tripwires: if a proposed move contradicts one, either party catches it — because both hold the why.
- **CURRENT STATE** — where the track stands right now. One paragraph. Built / live / mid-flight.
- **NEXT MOVE** — the immediate next action(s), ordered.
- **GRAVEYARD** — killed decisions, one line each, so they don't get re-inherited.
- **CONFIDENCE FLAGS** — anything inferred rather than known, flagged so it gets checked, not laundered. A wrong anchor poisons the boot recital instead of preventing the failure.

**The boot recital does three jobs at once** (§7) and is the highest-leverage step in the system: it proves the anchor loaded (a stale/wrong anchor surfaces *in the recital* — the payload check the footer-tripwire never was), it re-grounds Jake (he hears the heading and nods or redirects), and it sets the shared why both parties drift-check against for the rest of the session.

---

## 5. The corpus — immutable evidence

- **Verbatim means actual quoted text.** The moment you reword, it's a summary wearing a verbatim badge — confabulation with a paper trail. Quote, attribute (Jake/Claude), date. Your only judgment is where a quoted block starts and stops.
- **Salient (keep):** decisions + the reasoning that produced them; pushback that changed direction; corrections of fact bought with real time/money; architectural reasoning, even mid-thought.
- **Chaff (cut):** banter that doesn't move the football; pure acknowledgments; false starts superseded later in the same conversation — *unless the false start is itself the lesson.*
- **When in doubt, KEEP.** Cold storage makes over-retention cheap (bytes) and under-retention fatal (gone forever). The selection-pressure that made old summaries lossy only existed because the files were *hot*. Cold kills the pressure.
- **Secrets NEVER enter.** Reference that one was discussed (`[owner connection string — redacted]`), never the value. A live cred leaked into chat once; an over-retaining immutable store would immortalize it. Hard rule.
- **Append-only.** Never edited, only superseded by an anchor pointer. Dated · decision-tagged · indexed at top so a reader finds an entry without loading the whole file.
- **Capture when sharp, write when governed.** Lock the exchange the *moment the decision lands* (🔒 staged inline, while both parties are sharp — selecting at session-end means cutting at the model's most degraded point). The staged set surfaces in the close batch for Jake's ratification (§8).

---

## 6. The currency law — the ruling

**The corpus is evidence. The anchor is the verdict. The graveyard is what's overturned.**

The corpus can *never* be trusted for what's-live, because immutable means dead decisions sit in it forever at full conviction in their original convincing words — "Pyris is on Wix," the raw-CDN fetch method, the RAM theory — carrying zero "later killed" signal. Query the corpus for the *why*; adjudicate *currency* against the anchor plus the graveyard.

This is Jake's own §5.1 generalized: **a document is not ground truth for its own currency — least of all an immutable one.** It is the "File Freshness Was a Lie" lesson pointed at docs: the footer-date tripwire checks the *wrapper* (the `Last updated:` line) while a stale fact rots in the *payload* underneath a current date (SD23 laundered a dead theory forward; the `--env-file` line *caused* the failure it should have prevented). Measure the payload, not the wrapper. The citation forged at decision-time (§9) is what avoids the fuzzy-query warp — retrieval follows a pointer written when both parties were sharp, not a degraded-Dory blind search of 2MB.

---

## 7. The modus operandi — every session, both directions

**BOOT — self-read.** The track anchor + the Rules layer (cat 1). Two small things. Plastic (corpus, lore, old handoffs) is *available for reconstruction if needed* — it is **NOT** a required boot read. That is the entire weight off Jake's back.

**CONFIRM — recite the address back, before any work.** Destination · locked invariants-with-why · where we are now · next move. Jake nods or "no — aquarium's that way." Ten seconds. It is P. Sherman, 42 Wallaby Way said out loud at the start so neither party swims the wrong way for three hours.

**WORK — every move tied to the destination, out loud.** Not "do X" — "X, because it serves [destination-level why]." That sentence is the live drift-tripwire both parties hold. **Re-anchor every ~5 turns** — re-read the small anchor, not the whole context (the re-anchor is cheap *because the anchor is small*). The §5.2 re-anchor rule, made structural instead of a rule-in-a-file-read-once.

**CLOSE — self-write.** Finalize the anchor (state, next, invariant changes). The corpus already holds the day's 🔒-staged verbatims. Present everything as the governance batch (§8). Jake confirms; he can, because it's plain-language and destination-level. The verbose handoff becomes *optional plastic* — generated only if there's real episodic narrative worth cold-storing, and it carries **no** anchored facts.

**The terminus.** There is **no in-session token/usage meter** — Claude has zero visibility into context fill. The only proxy is an **externalized turn counter**: each re-anchor states "re-anchor N/4," incrementing in the block Claude rewrites (externalize the thing the model is bad at counting). The 4th re-anchor (~turn 20) fires a "we're at 20" flag to *both* parties. It is a **warning that triggers a seam-hunt, not a guillotine**: wrap at the next clean seam, hard ceiling ~turn 25. A five-turn window to land at a seam — never a hard cut that strands a half-locked decision. Turn-count being fuzzy (20 dense turns ≠ 20 light ones) doesn't hurt a window; it would only hurt a guillotine.

> Why the terminus actually holds instead of relying on willpower: it kills both incentives. Claude pushes phase-completeness; Jake hoards live context. The warm active-phase corpus (§9) removes both — Claude doesn't need to finish the phase in one session because the anchor + warm slice carry clean state across the seam (no half-state penalty for stopping), and Jake doesn't need to hoard the session because the warm slice *is* his context-hoard and it survives the close. Neither white-knuckles against their nature; the architecture deletes the thing each was gripping.

---

## 8. Governance — the write interface

All writes are **proposed, never auto-applied** (JAKE-RULES §7 / §17.2). The end-of-session interface is a **numbered batch**: every change presented as a code block, each ratified **confirm / deny / litigate**. Two cadences, by drift-risk:

- **Corpus verbatims** — staged inline (🔒) when the decision is sharp; the staged set surfaces in the close batch for ratification. Low drift risk (it's verbatim), but still gets Jake's yes.
- **Anchor / infrastructure / graveyard changes** — pure close-batch. This is where Claude's summarizing drift is most dangerous and Jake's verification most valuable.

**Claude generates; Jake routes.** Claude cannot write the repo, PK, or Supabase itself from a bare orchestrator chat — that is a tool boundary, not a preference (§9). Never claim a write that didn't happen.

---

## 9. Storage + the honest mechanism reality — the seam

**Current state, stated plainly so it isn't hand-waved:** from a bare orchestrator chat, Claude has **no reach into Supabase** — and cannot even *discover* a connector without Jake opting in (verified this session: the registry check hit an opt-in gate). git, by contrast, is boot-readable by the orchestrator via codeload (proven). CC has full DB access (it runs the migrations).

**Interim — works now, zero new infra:**
- Rules / Infrastructure / Anchors → **git** (orchestrator codeloads at boot).
- Corpus → **Supabase, via CC** at decision-time. The layer most wanted in Supabase is exactly the one Claude's no-reach doesn't bite, *because the corpus is never a boot read.*

**Endgame — the seam:** a Supabase/Postgres **MCP connector** on Jake's Claude account. Stand it up and the orchestrator boot-reads the anchor and read/writes all four categories natively — Jake fully off the bus. **Caveat, no soft-pedal:** verify any connector with a live round-trip before trusting it (doc says it works; the live system decides — §5.1). Unknown yet whether the seam is an install or a custom build — that's the registry check, gated on opt-in.

**Middle ground that gives "deep working context" without loading everything:** the *active phase's* corpus rides **warm** (small, high-relevance, loadable on-need while the phase is live); everything older goes **cold** (citation-only, pulled on a pointer). Recency, not totality — Jake's own staleness-sort. The needle stays findable because the haystack stays phase-sized.

**Schema decision (locked this session):** the apparatus's corpus + anchor go in **separate tables**, NOT Cypher's live memory schema. Reason — coupling the daily build-context to a schema that is mid-migration *right now* (1c-i) means a migration could brick the thing we build with. *"It needs to be its own system driving the build of the new system, not the new system building itself."* Cannibalize into Cypher later if wanted; decoupled lifecycle now. (JAKE-RULES §6/§11: is the coupling load-bearing, or just elegant?)

---

## 10. The honest ceiling — no soft-pedal

This system trades a **labor** problem for a **discipline** problem. It holds *only* as long as: the **hot/cold wall holds** (the corpus is NEVER a boot read — the first time someone loads it "just to be safe," the swamp is rebuilt, concatenated); **verbatim stays actually verbatim**; the **corpus never gets a currency vote**; and **secrets never enter**. Those disciplines can lapse — but they lapse **cheap** (noise, a thin anchor) instead of **expensive** (three hours and a leaked cred).

It does **not** abolish the irreducible Dory-slip mid-session. Between re-anchors, the model can still drift; a wrong anchor poisons the recital instead of preventing the failure. What it buys is this: it stations **two independent drift-catchers on every move where there were zero.** That is the real purchase — not that the model stops forgetting, but that the forgetting stops costing Jake the day. It converts a dead error-correction seam into a live, redundant one. That is the most any system in this shape can honestly buy, and it is the difference between S11 and not-S11.

---

## 11. The dogfood note

This system was designed in the session that it now closes, and it was closed *using itself* — the apparatus-build track got an anchor, the session's decisions got 🔒-staged to corpus, and the next session is ignited by reciting an address instead of re-reading 87 files. We prove the architecture by living it (Cypher Voice §7). The apparatus *is* Cypher's memory model, hand-run, and it hardens into Cypher: corpus + anchor in Supabase today via CC, Cypher-driven tomorrow. Carousel-hardens-into-Cypher, pointed at context itself. Nothing thrown away.

---

## Appendix A — Bootstrap (one-time, 2026-05-25)

The initial cat-3 corpus, cat-4 anchors, and cat-1/2 reorganization were built by three **fenced excavator** sibling chats run in parallel (Corpus → Anchors → Universal; that dependency order because anchors cite the corpus and the rewrite partly depends on seeing the corpus shape). Each was fenced *"extract/structure, do not redesign"* because a fresh instance in this project will try to re-architect. Their outputs are **ratified in the main thread, not in the siblings** — the siblings produce; the main thread is the only place changes get confirm/deny/litigated and the only place the Supabase-migration decision is made. The three prompts are preserved in the session corpus.

## Appendix B — The live apparatus-build anchor

The first real anchor (`ANCHOR_apparatus.md`) is delivered alongside this spec as the worked example and the live v1 for this track. Read it as the canonical shape.

---

*v1 — 2026-05-25. Designed by Jake + orchestrator-Claude across an 8-turn meta-session. Proposed lore-name: The Wallaby Way. Revise as the loop proves out against live use; first live boot-and-recite test is the next session. This document is itself cat-1/cat-3 in nature — it carries its own why with its decisions, on purpose.*
