# ANCHOR — apparatus-build track
*v2 · 2026-05-25 (apparatus S2 close) · hot · boot-read this + JAKE-RULES, recite before working*

## DESTINATION
Build the apparatus's own memory system (*The Wallaby Way*): a closed, self-administered re-grounding loop that holds continuity for a stateless Claude across sessions — so Jake stops being the memory bus *and* the blind follower. It is **beta-Cypher-brain**: the same anchored/plastic strata Cypher will run on, hand-cranked now, hardening into Cypher's memory layer. Scope is **Jake's whole working surface** (all projects + no-project), not just Cypher.

## INVARIANTS — WITH WHY
- **The corpus is ONE undelineated body; the anchors are the index/neurons INTO it** — BECAUSE partitioning the corpus by project hides cross-domain knowledge (a woodworking lesson is load-bearing for 3D-model finishing). Congeniality-across-knowledge is the whole point of a brain. S1 settled this: *"corpus without anchor is un-navigable noise; anchor = an index into it."* Do not re-wall the ocean into buckets. *(This killed the S2 `track`-column drift — see graveyard.)*
- **Anchors are discovered per-project, where the project walls give clean relevance; `meta` + pre-Projects/LRN are built from the archive, because they have no wall** — BECAUSE `conversation_search`/PK are project-scoped, so a project boundary is a *cleaner* relevance signal than a content-classifier guessing across a blob. Wall-less tracks (lineage-wide lessons; the pre-Projects era) need the archive's whole-corpus view.
- **The presence layer (the booted mind) can't be stored — only booted warm; the boot/recite/re-anchor loop IS its mechanism, and the lineage is how it survives not-persisting** — BECAUSE soup (corpus) and neurons (anchors) persist, but the mind that runs them resets every session. Continuity that doesn't depend on any single instance holding the thread. The recital isn't ceremony; it's the mind coming online against the soup+neurons.
- **Anchor is hot + small + boot-read; corpus is cold + queried-never-booted** — BECAUSE the moment the corpus loads "just to be safe," the 87-file swamp is rebuilt. The hot/cold wall is the whole game.
- **Corpus is verbatim, never reworded** — BECAUSE a reworded "verbatim" is a drifting summary with a paper trail; the immutable original is the only thing that stops context-warp.
- **Corpus is evidence; the anchor is the verdict; the graveyard is what's overturned** — BECAUSE immutable storage holds dead decisions at full conviction forever; only the anchor (+ graveyard) knows what's currently true.
- **Invariants carry a destination-level WHY, not a mechanism** — BECAUSE Jake isn't a coder; the why is what lets him drift-catch Claude without holding the how. The keystone that makes the loop self-correcting, not just self-transferring.
- **Secrets never enter the corpus** — BECAUSE a leaked cred in an over-retaining immutable store is immortalized; one already leaked to chat (S11). The raw archive HAS that cred — scrub is a hard gate before any ingest.
- **All writes are proposed and ratified by Jake in a batch** — BECAUSE Claude is the drift-prone summarizer; Jake's confirm is the second navigator that closes the dead error-correction seam.
- **Apparatus tables stay SEPARATE from Cypher's live schema** — BECAUSE coupling daily build-context to a mid-migration schema means a 1c migration could brick the thing we build with.

## CURRENT STATE
**S2 closed.** CORPUS v1 (`CORPUS.md`) **ratified** — fence held (excavator not architect; secrets clean; honest tagging); it's the **template + a calibration target** for the archive build. The 7 track anchors **ratified** for shape / invariants-with-why / corpus-traceability / flag-honesty (2 open items routed to archive resolution: Printer "it's just grease" quote = source-or-strike; LRN business-court reasoning missing from corpus). **Archive route (B) chosen** over 15 per-scope excavators; excavation moved from OC-spawned siblings → **CC-on-Workhorse reading the archive off disk** (`C:\claude-reference\apparatus-archive\`). **Mid-session re-architecture:** the project-field partitioner was **falsified by CC on 348MB** (no project↔conversation linkage in `conversations.json` — §5.1 fired live); replaced first with content-driven tagging, then **superseded entirely** by the brain-soup model above (undelineated corpus + per-project anchor neurons). Storage target (new Supabase project vs `apparatus` schema in Cypher's project) **deferred** — needed only at ingest, off the critical path; **B doesn't need the MCP seam** (CC writes Supabase directly). `Track_Meet_Doctrine.md` rename **finalized** (was `Cypher_Architecture_Discussion_2026-05-11.md`); pointer + file edits pending (see next move).

## NEXT MOVE (ordered)
1. **Run S3 — archive-fed corpus excavation** (CC-on-Workhorse, corrected Phase-1 = build ONE undelineated indexed body, NO track partition). Ignition prompt is the S2 close deliverable.
2. **In parallel, decide storage target** (new Supabase project [lean] vs `apparatus` schema in Cypher's). Not on S3's critical path.
3. **Per-project anchor-discovery passes** — the 7 walled tracks, each in its own project's claude.ai; `meta` + LRN from the archive. (Separate from S3's corpus build.)
4. **Schema-from-seed-shape, then CC ingest** — build the table AFTER the seed shape is proven; ratify before ingest (append-only = un-ratified rows are immortal).
5. **Land the `Track_Meet_Doctrine.md` rename:** Jake renames the file; the CORPUS entry-6 pointer gets corrected (Corpus-Claude pointer-edit prompt, or fold into the S3 calibration pass); propagate the new name in CLAUDE.md + boot prompts (Universal sweep).

## GRAVEYARD
- **"Corpus partitioned by `track` / a `track` column / a locked track vocabulary"** — KILLED (S2). Re-walls the one-body corpus S1 settled; partition hides cross-domain knowledge. Corpus is undelineated; anchors are the index. (Claude's drift, caught by Jake against S1 canon — the "un-navigable noise / index into it" receipt.)
- **"The export's project field IS the track value"** — KILLED (S2). No project↔conversation linkage exists in `conversations.json` (CC verified on 348MB). §5.1 fired live — an export-format claim asserted from memory, in the same doc that said "don't assert export format from memory."
- **"15 per-scope excavators"** — NOT dead; demoted to the **fallback** for archive gaps only (B chosen).
- "More files / bigger notebook / longer window fixes it" — DEAD. Storage was never the lever; S11 had the fact loaded and failed anyway.
- "Footer-date freshness tripwire is sufficient" — DEAD. Checks the wrapper, not the payload.
- "All four categories in Supabase, OC maintains, today" — NOT available now: OC has no Supabase reach from a bare chat. Endgame, gated on the seam — and B routes around it (CC writes the DB).

## CONFIDENCE FLAGS
- **Archive completeness** — does `conversations.json` carry full message text + timestamps + role attribution? **UNVERIFIED until CC Phase-0** (the gate). If reduced, Option A is the per-scope fallback.
- **Within-session-drift mitigation** — now **partially proven**: the loop ran live across S2; the boot-recite + re-anchor cadence caught a real drift (Claude's `track`-column proposal) against the S1 receipt. One session is not a proof — keep watching.
- **Supabase seam install-vs-build** — UNVERIFIED (registry gated on opt-in); deferred, B doesn't need it.

---
*Anchored v2 5-25-26 (apparatus S2 close). v1→v2: scope expanded to whole working surface; added undelineated-corpus / per-project-anchor / presence-layer invariants; logged the project-field falsification + the killed track-column; moved excavation to CC-on-disk; CORPUS v1 + 7 anchors ratified. Confidence: HIGH on the re-architecture (sourced live this session + the S1 genesis receipt); archive completeness UNVERIFIED pending CC Phase-0.*
