# The Seeding Council Boot Kit
*file: Seeding_Council_Boot_Kit_v1.0_2026-06-01.md · v1.0 RATIFIED · apparatus S26 · 2026-06-01*
*status: RATIFIED. v0.1 (first draft) → v0.2 (second draft, three independent reviews) → v1.0 (this file): the three pre-ratify uncertainties are resolved (judged-pass loadout WALLED, JAKE-RULES §11 wall verified-on-disk, keyword-coverage criterion accepted with downstream-miss measurement). v0.1 and v0.2 stay on disk, tombstoned-not-deleted. This is canon.*
*form: single document covering ALL roles, for auditability. The deployable per-window boot prompts are now AUTHORED as separate files (`Boot_ScopeReader.md`, `Boot_CrossCuttingReader.md`, `Boot_JudgedPass.md`) — this file is the spec they derive from; they are the thing each window actually receives. (Standing drafting caution, carried from v0.2: "load LIGHTER when in doubt" is a LOADOUT heuristic — how much to put in a window's head — NOT a laying heuristic; a per-window prompt must not let "lighter" leak into "lay fewer cards." The candidate-level bar stays the neutral §3 bar.)*
*authority: subordinate to The Progenitor v2 (`active/apparatus/The_Progenitor_v2_2026-06-01.md`) — if this kit and the doctrine ever disagree, the DOCTRINE wins and this kit is wrong. **DEPLOY PREREQUISITE: v2 must be on `main` (the codeload boot path), not just authored — every window's common kit says "boot with The Progenitor v2, in full," and that file has to exist where windows boot from.** This kit operationalizes §12 (seeding process) + §13 (boot kit) and POINTS at the doctrine for the law; it does not restate it.*

---

## 0. What this kit is, in one paragraph

The seeding pass is the first, biggest read of the laid floor (325 headers / 24,138 messages) to lay the initial pointer catalog. It runs as a **council of parallel, blind CC windows**, each reading a content-neutral slice of the floor and proposing pointers against one shared standard (The Progenitor), with **two later passes**: a **synthesis pass** that mechanically reconciles the blind proposals, and a **judged pass** that does the meaning-work neither a blind reader nor a mechanical synthesizer can own (chain-assembly + recall-check). The governing principle, from §13: **the kit lets a reader find what's in the floor; it never tells the reader what it'll find.** Load for *recognition*, never for *projection*. The risk is asymmetric toward overload **on loadout** (so: load lighter when in doubt) — but see §6, that asymmetry is only safe if under-reading is *catchable*, which is why the recall check exists.

---

## 0a. HOW THE COUNCIL RUNS — CC against the live floor (S26 decision)

**The council windows are CC instances with live read access to `apparatus-floor` (Supabase).** A window does NOT receive its slice as uploaded data — it QUERIES the floor for its assigned slice directly. This makes "source is the floor, never chat_search" (§5) literal: the floor reaches the window through CC's database read, not through any chat surface.

**Three enforcement consequences, all load-bearing (S26):**
1. **Each window boots BARE — no project instructions.** The project-instruction layer carries the codeload-pull directive, the OC/CC operating model, and the re-anchor SOP — i.e. a live path to the repo AND the orchestrator frame. A blind slice-reader must have neither: no repo path (it would defeat upload-only blindness) and no orchestrator frame (it would read the floor as OC, not as a fresh recognizer). Council windows run in a no-project context.
2. **The kit reaches the window by UPLOAD STREAM only.** Jake hands each window exactly-and-only its role's file set (see §1a / the per-role cheat sheet). Controlled upload IS the enforcement of §13's blindness at the boot boundary — a window that pulled its own kit off the repo could wander into sibling files or the catalog-so-far and contaminate the independence that makes convergence (§4) a real signal.
3. **The floor reaches the window by CC's live query** — its assigned slice only. Not chat_search, not an ndjson upload, not a repo path.

So: kit IN by upload (controlled, exactly its set), floor IN by CC query (its slice only), everything else OUT (no project instructions, no repo path, no chat_search, no sibling work). That is the physical shape of blindness.

---

## 1. The roles — DIVIDED BY SLICE, NOT BY KIND (settled v0.2)

**v0.1 split windows into fence-reader / texture-reader — a by-KIND split the doctrine never asked for. The Progenitor §12 divides labor by SLICE (project-scope), with each window reading for BOTH kinds.** The fence/texture distinction is about *what earns a card* (§3 of the doctrine), not *who reads* — baking it into window roles was a category error that created load asymmetry with no upside. The roles:

1. **SCOPE READER** — reads one content-neutral slice of the floor (§5/§6 on how slices are drawn) for BOTH kinds: fences (decisions/constraints a fresh Claude would hit and change course on) AND textures (patterns whose volume is the signal). Most windows are these. *(Deployable file: `Boot_ScopeReader.md`.)*
2. **CROSS-CUTTING READER** — reads the no-project / cross-domain space, hunting the connections a single-slice reader structurally cannot see: a stance set in one scope that should steer another; a texture or fence-link whose instances scatter across slices. Also reads for both kinds. This reader matters most for fence-CHAINS, whose links are scattered across sessions by definition (see §4 + §4a). *(Deployable file: `Boot_CrossCuttingReader.md`.)*
3. **SYNTHESIS WINDOW** — runs after the blind reads. MECHANICAL reconciliation only (§4). Does NOT read the floor for new pointers; does NOT judge meaning. *(Mechanism is build-work — see §7; no portrait, no judgment, so it carries no separate reading-role boot prompt of the §1a shape.)*
4. **JUDGED PASS** — runs after synthesis. A non-blind Claude (or Jake) that does the two jobs neither a blind reader nor a mechanical synthesizer can own: assembling fence-CHAINS from independently-laid links (ordering by date, preserving supersession), and the RECALL check (§4a). *(Deployable file: `Boot_JudgedPass.md`.)*

**The windows (1 + 2) run BLIND to each other.** No window sees another's proposals, or the catalog-so-far, during reading. Independence is the feature (§4).

*Load is sized per the asymmetry rule (§3) — every reading window carries the same base load and reads for both kinds, so "what to load" is a single decision, not a per-role fork.*

---

## 1a. THE PER-ROLE LOADOUT (what each window receives — S26, resolves the file-list question)

This table IS the resolution of "who gets which files." JAKE-RULES is **role-relevant but §11-stripped for everyone reading** (see §3 + the §11 verification note below). The portrait files (Wallaby Why / Lore Bible) are loaded by NOBODY as a reading lens.

**COMMON to every reading + judging window:**
- `The_Progenitor_v2_*.md` — the law, in full.
- `JAKE-STACK.md` — so a tooling/architecture fence is legible as a fence (a reader hitting "Supabase-over-Nornic" needs the stack to know it's a fence, not motion).
- `JAKE-RULES.md` **with §11 physically removed from the council's copy** — the §1 facts + working-relationship frame + the rule-shaped fences (no-"Oueilhe", REFUSED wall, full-code-not-diffs) are needed to recognize restating-known-canon vs. laying-a-new-constraint. §11 ("Patterns Jake Has Flagged") is portrait-shaped and is cut (below).
- The §3 worked examples **as SHAPES, not meanings** (§3).
- Its own role boot prompt (`Boot_*.md`).

**PER ROLE, added to common:**
- **Scope reader** → its slice assignment (which content-neutral slice it queries). Nothing else.
- **Cross-cutting reader** → the cross-domain / no-project floor space as its read target. Nothing else.
- **Judged pass** → the **synthesized catalog** (what it judges) + the **known-fence checklist** (§4a). **NO portrait** — this is the one non-blind seat, so projection risk is highest and projection need is zero (§4a / §8 resolved-3).

**THE §11 STRIP IS A DELIBERATE PREP ACTION.** The council's uploaded copy of JAKE-RULES has §11 removed before upload — not "present but instructed to ignore." Can't read what isn't there; it's the clean enforcement and it's cheap because the kit is hand-fed by upload anyway. Stated here so the strip is deliberate, not silent.

**§11-WALL VERIFICATION (S26, on disk):** the live JAKE-RULES §11 was read off disk at S26 anchor. It is "Patterns Jake Has Flagged" — day-shape-is-heartbeat, self-perception-pessimistic-on-closed-deals, eyes-beat-math, two-word-compression, scarcity-underpricing, the Griffin/meds-adjacent material. That IS portrait-shaped — a pre-written read of how Jake behaves, the exact thing that makes a reader confirm a pattern instead of discovering it. The S25 call to wall §11 as a reading lens was made from memory; S26 confirmed it against the real bytes. The cut holds and is not too deep — fence-recognition runs off the *rule-shaped* canon (§1, the REFUSED wall, etc.), which stays.

---

## 2. The COMMON kit (every reading window boots with all of this)

- **The Progenitor v2, in full.** The law. Non-negotiable. Internalize §3 (the bar), §2 (two kinds, one spine), §5 (why the catalog is selective — the corpus-search net), §6 (dumb-index/smart-reader), §8 (guards incl. keyword-coverage), §10–§13 (triggers, return-shape, seeding process, this kit's parent).
- **JAKE-RULES §1 facts + the working-relationship frame + the rule-shaped fences** — who Jake is (non-coder founder; he drives, Claude builds), the collegial-profane register (so profanity reads as register, not signal), and the rules that ARE fences (so a fence-reader can tell new-constraint from restating-canon). **§11 removed** (§1a, §3).
- **JAKE-STACK** — tooling/architecture context, so an infra fence is legible as a fence.
- **The §3 worked examples — AS SHAPES, NOT INTERPRETED MEANINGS (§3).**
- **The one-page operating brief** (§5) — the loop, the locator shape, the hard walls.

---

## 3. Loadout discipline + the projection wall (UNIVERSAL across all reading roles)

**The asymmetry (loadout):** an UNDER-loaded reader produces *visible gaps* (catchable — but see §6, the catch is weaker than it looks, which is why §4a's recall check exists); an OVER-loaded reader produces *confident, plausible, wrong pointers that look like they held the bar* — projection is invisible to a shape-audit because it looks right. So on LOADOUT — how much interpretive material to put in a window's head — **lighter is safer.** (Corrected to "loadout," not a laying instinct — the candidate-level bar stays the neutral §3 bar for both kinds. A fence-reader told "lay lighter" would optimize against the cheap failure toward the expensive one; that is NOT what this rule says.)

**THE PROJECTION WALL — applies to EVERY reading window, all roles, AND the judged pass.**

- **NO Wallaby Why. NO Lore Bible. NO JAKE-RULES §11 ("Patterns Jake Has Flagged" / the Griffin-meds material) as a reading lens.** These are a pre-written *portrait* of Jake. A reader booted with the portrait won't *discover* a pattern in the floor — it'll go looking for the cadence the portrait told it to expect and CONFIRM it. That's projection wearing recognition's clothes — JAKE-RULES §1.2 (an AI's read of Jake gets the same skepticism as Jake's read of himself) turned on the council. The portrait is for *tone-calibration-when-talking-to-Jake*, a different job from *deciding what's in the corpus*.
- **The wall holds at the §4a judged-pass seat too (S26, uncertainty (i) resolved).** The judged pass is the ONE non-blind window — it sees across slices to assemble chains and run the recall check. That makes it the highest projection-RISK seat in the council (cross-slice view makes a projected pattern look authoritative) with ZERO projection-NEED (chain-assembly is date-ordering + supersession; the recall check is a checklist match; neither needs the portrait). Highest risk, no need → wall it. The asymmetry the kit runs on, pointed at its own most-dangerous seat. (The one semantic recognition the judged pass DOES need — that "Supabase-over-Nornic" and "not using NornicDB" name the same fence — runs off JAKE-STACK + canon, which name the real fences, NOT off the emotional portrait.)

**THE CALIBRATION-EXAMPLES ARE THEMSELVES A PROJECTION VECTOR (the finding all three reviews converged on).** v0.1 built the wall against portrait *files*, then handed every window the 1Pass fence and Griffin's-pickup texture "in full" as calibration — and Griffin-in-full ("med-related time-blindness, load-bearing, the count IS the meaning") is a portrait fragment through the side door. A reader primed on Griffin hunts for the next Griffin-shaped thing and finds it. Same gun, pointed the other way. The fix:

- **Examples calibrate SHAPE, not MEANING.** Show the reader the *shape* of a fence (a decision with a why that would change a fresh Claude's course) and the *shape* of a texture (a recurring count + spread where the volume itself is the signal). Do NOT carry the interpreted signal-line ("take this seriously, it's med-related"). The reader learns "this is what a fence/texture looks like structurally," not "this specific meaning is load-bearing."
- **Explicit instruction every window carries: resemblance to a calibration example is NOT itself evidence.** "This looks like Griffin" is not a count. The reader must find the volume/decision in ITS slice on its own merits; the example taught the shape to recognize, not the conclusion to reach.
- **Carry the NO-CARD examples too**, presented as shapes — the most frequent call any reader makes is "no card, move on" (most of the corpus is motion, §3), and calibrating that most-common call against ZERO examples while giving two vivid "yes" templates is a structural bias toward over-carding. Canonical NO-card cases as shapes:
  - **Texture NO-card:** a word/phrase with a high count but zero signal — the count is incidental, nothing about the volume tells Claude how to show up. *Shape lesson: high frequency alone is NOT texture; the volume has to carry meaning.*
  - **Fence NO-card:** a routine build step that recurs constantly (a git push, a dev-server restart) but re-encountering it cold costs nothing — no course changes. *Shape lesson: recurrence + decision-flavor is NOT a fence; only "a fresh Claude would change course" is.*

Two "no" shapes against two "yes" shapes balances the calibration toward the bar's actual center of gravity: don't point.

---

## 4. The BLIND-READ + SYNTHESIS model (mechanical reconciliation only)

**The readers boot BLIND** — no catalog-so-far, no sibling proposals. Pre-loading the catalog reintroduces projection (sourced from sibling windows) AND can't assemble cross-slice patterns anyway. **Duplicate convergence is SIGNAL** — if independent blind windows fence the same thing, that's evidence it's real.

**Caveat on convergence-as-confidence:** do NOT count convergence on the *calibration examples themselves*. If three windows all fenced 1Pass and 1Pass was their shared worked example, that convergence is partly an artifact of shared priming, not independent discovery. The confidence marker is only clean for cards NOT in the example set.

**THE SYNTHESIS WINDOW — MECHANICAL ONLY.** Bounded to operations that need no portrait and no meaning-judgment:
- collapse TRUE duplicates (**same span, same fence, same call**) into one card, recording convergence (laid by N blind windows) as a confidence marker (minus the example-contamination caveat above);
- merge keyword variants pointing at the SAME span into one card's keyword set (harvests natural keywords — feeds §8's keyword-coverage bar);
- assemble cross-slice TEXTURE counts — **but only after a same-SIGNAL check, not just same-keyword.** A texture surfacing in two project-scope slices may be two *contexts*, not one count (Griffin-weight in personal slices vs a "forgot to deploy" pattern in build slices must not be falsely summed into a spurious 11). Same keyword ≠ same signal; synthesis sums counts ONLY when the signal matches.
- **FLAG — do NOT decide — candidate fence-chains.** Where synthesis sees same-fence-topic with DIFFERENT calls across slices (the signature of a chain whose links were laid independently), it marks them as a candidate chain and routes them to the JUDGED PASS (§4a). **Synthesis NEVER collapses or orders divergent-call fences itself** — that's the cardinal-sin risk (§4a).

**SPEC REQUIREMENT (load-bearing):** blind reads preserve proposals VERBATIM into synthesis — raw, un-deduped, independent keywords and counts intact. No window pre-dedups against its own prior cards. Append-keep-everything, reconcile-after — the floor's spine, one more scale.

---

## 4a. THE JUDGED PASS (the step that owns what neither blind-reader nor synthesis can)

The three reviews converged on a structural hole: **fence-CHAIN assembly and RECALL both fall in the crack between "readers are blind and slice-limited" and "synthesis does shape, not meaning."** A blind slice reader sees only one link of a chain that evolved over time and lays it length-1; a mechanical synthesizer can't safely order divergent-call links without judging meaning. So a third pass owns it.

**THE CARDINAL-SIN RISK this closes.** A fence is a LINEAGE, not a verdict (Progenitor §2.1). Two blind windows reading different slices lay two fences on the same topic with DIFFERENT calls — because they read different links in a chain that evolved (e.g. 1Pass-blocked-in-June vs 1Pass-viable-once-beta-lifts). If synthesis collapses these into one card and picks the wrong link as "current," then §11's NON-NEGOTIABLE full-why-chain return will faithfully deliver a WRONG chain with maximum confidence — the doctrine's strongest guarantee (§11) corrupted by the kit's least-specified operation. Silently erasing a superseded link is the one thing the doctrine forbids above all (§2.3, §7: supersede-don't-delete; no pointer dies on one Claude's judgment).

**WHO runs it.** A NON-blind Claude (it may see the whole synthesized catalog + the candidate-chain flags) or Jake. NOT a blind reader (can't see across slices), NOT the synthesis window (mechanical only). **It boots WITHOUT the portrait** (§3, S26 uncertainty (i)) — highest projection-risk seat, zero projection-need.

**WHAT it does:**
1. **Chain assembly.** For each candidate-chain flag from synthesis (same fence-topic, divergent calls), order the links BY DATE from the floor, preserve every link (latest = current, earlier = superseded-not-erased), and emit ONE fence laid as a proper multi-link chain per §2.1 / §12-step-3. Never drop a link. If it can't confidently order them, it escalates to Jake rather than guessing.
2. **The RECALL check (the hole-in-the-floor finding).** The kit's safety case is "overload is the real risk, go lighter on loadout." That is only safe if under-reading is *catchable* — but §6's spot-audit samples the synthesized catalog and can only validate PRECISION (do the cards that exist hold the bar), never RECALL (what fences were never laid because every window read light). You cannot spot-audit an absence. So the judged pass runs the seeded catalog against a **KNOWN-FENCE CHECKLIST** — canon already names real fences: 1Pass, no-"Oueilhe", the REFUSED wall, Supabase-over-Nornic, the therapist-voice boundary, full-code-not-diffs, the FK-drop (option c), D9, no-`&&`-chaining, no-duplicate-header. Any known fence the council MISSED is a *measured recall failure* — a signal to re-read (the slice that should have carried it) or recalibrate the bar. This is the feedback loop v0.1 asserted ("lighter is safe") without providing.
   - *Optional stronger posture (Jake's call):* run a PILOT slice deliberately over-seeded, measure the prune rate at spot-audit, and calibrate the bar from real data instead of asserting "lighter." The known-fence checklist is the cheap floor; the pilot is the richer version.

**Jake's per-batch spot-audit (§6) sits AFTER the judged pass** — he audits the shape of the chain-assembled, recall-checked catalog.

---

## 5. The one-page operating brief (the procedural card every reading window carries)

**THE LOOP (per reading window):**
1. **READ** your assigned content-neutral slice, **tree-aware** — conversations as branches up/down the parent chain, NEVER flat message streams (a flat-N slice rakes in sibling branches and contaminates the span — §11/§4). (The slice reaches you via CC's live query of `apparatus-floor`, §0a — never chat_search.)
2. **APPLY THE §3 BAR** to each candidate (both kinds): would a fresh Claude hitting this cold CHANGE COURSE (fence) or find the volume tells it how to show up (texture)? Neither → **NO card, move on.** Default is don't-point. (Calibrate against the SHAPE examples — both yes AND no — never against "does this resemble Griffin.")
3. **FENCE** → lay as a chain, **length-1 at seeding** (you are slice-limited and blind — you likely see only one link; the JUDGED PASS assembles multi-link chains across slices, §4a). Record the why as a live-predicate where checkable. Do NOT try to chain across what you can't see.
4. **TEXTURE** → representative span + count **across YOUR slice** + spread + the SIGNAL (what the volume tells Claude). The count is substance. (Cross-slice counts are assembled later, signal-checked — §4.)
5. **PROPOSE**: floor-key locator + kind + **keywords** (laid for future-SEARCH-anticipation, §8) + why-chain (fence) / count+spread+signal (texture). **You author the proposal; you do NOT claim to have saved/committed/pushed.**
6. Output proposals **raw and un-deduped** for synthesis (§4).

**THE FLOOR-KEY LOCATOR (§4/§11):**
```
span = {
  snapshot_id : "baseline-…" | "delta-…",
  conv_uuid   : "…",
  anchor_msg  : "…",                  # the hit (msg_uuid)
  reach       : { up: K, down: J, branch: <derived> }
}
```
**`branch` is DERIVED from the parent-chain walk, NOT a stored field.** The floor stores `is_root`, `multi_root`, and a bare `parent_message_uuid` (no self-FK, no branch-id column). A window must not author a locator citing a stored branch-id that doesn't exist; branch identity comes from walking the parent chain. Only 9/294 convs are forests, so this bites rarely — but every window authors this shape, so state it.

**THE HARD WALLS (prohibitions outweigh inclusions at self-applied scale):**
- **NO chat_search, EVER** — floor-only, via CC's live query (§0a). The prior attempt died here. Floor-only is what makes a pointer point at something stable.
- **NO catalog-so-far. NO sibling proposals.** Read BLIND (§4).
- **NO portrait as a reading lens** — no Wallaby Why / Lore Bible / JAKE-RULES §11 (§3, universal).
- **NO project instructions, NO repo path** — bare boot, kit-by-upload only (§0a).
- **NO flat-N spans** — tree-walk only.
- **NO chaining across what you can't see** — lay length-1; the judged pass chains (§4a).
- **NEVER claim to have saved/committed/pushed.** Propose; the human gates.

---

## 6. The review model (the one scoped human-immutability exception) — PRECISION + RECALL

Normal/incremental pointers get Jake's **per-card** eyes. The seeding pass is too large for that, so (Jake's explicit call, §12): the council self-applies the Doctrine at scale; **Jake spot-audits the OUTPUT SHAPE of the catalog** — but the catalog he audits is now the **chain-assembled, recall-checked** one (post-§4a), not raw synthesis output. This is the ONE place human-as-immutability-mechanism relaxes from per-card to per-batch — scoped to seeding only.

**The precision/recall split (the load-bearing correction):** spot-auditing shape validates **precision** (do the cards that exist hold the bar — fences-vs-motion, clean kind-split, tree-aware spans, future-searchable keywords). It is **structurally blind to recall** (a fence never laid leaves no shape to sample). So recall is NOT Jake's spot-audit's job — it's the **known-fence checklist in the judged pass (§4a)**. Precision = Jake samples the shape; recall = the checklist measures the misses. Both, or the catalog is confidently incomplete and passes review anyway.

**The convergence-map audit appendix (from the S24 cross-check):** the synthesis/judged passes surface to Jake not the raw proposals but a **convergence map** — what merged, what was a lone-window call, where counts were assembled cross-slice (and signal-checked), which chains the judged pass assembled, and the known-fence checklist result. This lets the shape-audit see whether the *readers* held the bar, not just whether the output looks clean — otherwise a systematically over-carding reader is invisible when synthesis dedups its noise against real convergence.

**OC-Jake live spot-check during the run (S26 — Jake's standing call).** Beyond the per-batch audit, OC and Jake walk results together as windows come back — window by window against the convergence map — because parallel work varies hard no matter how tight the spec, and divergence is the map of where the bar is soft. This is the kit's §4 medicine applied to the kit's own output: don't fight the variance, harvest it (convergence = confidence, divergence = where we look hardest). OC is load-bearing here at exactly the point parallel work has gone sideways before. Standing commitment for the seeding run.

**Tombstone rule holds at seed scale:** superseded/corrected pointers leave a tombstone, never a silent vanish. One Claude's judgment never silently kills a card. History file + changelog ride alongside.

---

## 7. What this kit deliberately EXCLUDES (and where those live)

- **Portrait files as a reading lens** (Wallaby Why / Lore Bible / JAKE-RULES §11) — projection wall, §3. (Correct for tone-calibration-when-talking-to-Jake — different job.)
- **chat_search** — hard wall, §5.
- **Catalog-so-far / sibling proposals during reading** — blind model, §4.
- **Meaning-judgment in the synthesis window** — bounded to mechanical, §4; meaning-work routed to the judged pass, §4a.
- **The doctrine restated** — this kit POINTS at Progenitor v2; doctrine wins on conflict.
- **Build-work** — council size / window count (but see the §8 note: slice granularity has a doctrinal edge), the synthesis + judged-pass *mechanism*, the manifest-build mechanism, on-disk serialization, the optional `/jedi-council` gate, the keyword-coverage acceptance criterion's *measurement* (now homed on the maintenance-pass list — §8 resolved-1 + §9). CC-against-the-live-floor.

---

## 8. OPEN QUESTIONS / RESIDUAL — resolved at v1.0, and what's still build-work

**RESOLVED at v1.0 (the three pre-ratify uncertainties — S26):**
1. **Keyword-coverage bar had no acceptance criterion** → **ACCEPTED with downstream-miss measurement (Jake's call: accept-and-proceed, not block).** The bar is unfalsifiable at lay-time (the future Claude that would test the keywords doesn't exist yet), so it is NOT measured at seed-time — it is measured **in use**: when ambient retrieval (Progenitor §10 Case 1) fails to surface a fence that demonstrably exists in the catalog, that is a logged keyword-coverage failure. Same measured-recall mechanism as §4a's known-fence checklist, one layer later in time. **This measurement is homed on the MAINTENANCE-PASS LIST (§9) as its first entry** — an active periodic check of logged retrieval-misses against the catalog, not a passive "if someone notices." Rationale for accept-over-block: you cannot honestly measure future-search-anticipation before the future searches exist; blocking to whiteboard a seed-time number is the molasses failure. The gate is named, the mechanism specified, wired to the §10 retrieval the engine build delivers. Matches house style (claim less, prove integrity where it's visible — the FK call again).
2. **Judged-pass loadout (does it get the portrait?)** → **NO, WALLED (§3, §4a).** Highest projection-risk seat (only non-blind window), zero projection-need (chain-assembly = date-order + supersession; recall = checklist match). The one semantic recognition it needs runs off JAKE-STACK + canon, not the portrait.
3. **JAKE-RULES §11 wall** → **VERIFIED ON DISK, holds (§1a).** §11 is "Patterns Jake Has Flagged," portrait-shaped; walling it as a reading lens was the right call and the S25 memory of its content was accurate. §11 physically stripped from the council's JAKE-RULES copy.

**RESOLVED earlier (v0.2, carried):**
- **Q1 role-merge** → DISSOLVED — by-SLICE division, both kinds per window (§1).
- **Q2 synthesis-gets-the-portrait** → NO, WALL (§4); chaining moved to the judged pass (§4a).
- **Q3 NO-card example** → ADDED as shapes (§3).
- **Q4 manifest-vs-discover** → MANIFEST; content-neutral slicing stated as DOCTRINE (slices drawn by content-neutral heuristics — conversation boundary, time window, account — used only as reading aids, never a topical pre-sort; tree-aware so slices are disjoint and branch-clean). The mechanism is build-work; the constraint is doctrine.

**STILL BUILD-WORK (CC-against-the-live-floor, not whiteboard — flagged, not blocking ratification):**
- **Slice granularity is partly doctrinal, not purely build-work.** More windows = smaller slices = lower per-window count for any given texture = more textures pushed below the "is the volume the signal" threshold within a slice, dumping load onto synthesis's cross-slice assembly (the weakest link). Past some fineness, slice granularity degrades texture-detection into a synthesis-only operation. The number is CC's; the constraint (don't slice so fine that within-slice texture detection collapses) is doctrine. For the seeding-build session.
- **The synthesis + judged-pass mechanism**, the **manifest-build mechanism**, **on-disk serialization**, **reach defaults**, the optional **`/jedi-council` gate** on seeding output, the **spot-audit batch cadence**. CC-against-the-live-floor.

---

## 9. THE MAINTENANCE-PASS LIST (S26 — a named home, not yet a spec)

Seeding is first-and-biggest, NOT one-and-done (Progenitor §12: the catalog grows by use forever). Some checks can only run *after* the catalog is live and in use — they need real retrieval behavior to measure against. This list is their home so they don't evaporate; each will want its own small spec later (build-work, CC-against-the-live-floor).

**Entry 1 — keyword-coverage miss-logging (from §8 resolved-1).** A periodic pass checks logged §10-Case-1 retrieval failures (ambient retrieval failed to surface a fence that exists in the catalog) against the catalog, identifying keyword-coverage gaps empirically. Same family as the §4a known-fence recall checklist, run on a cadence instead of once at seed-close. This is the measured acceptance criterion the keyword-coverage bar was missing — it lives here because it is, by nature, a downstream/in-use measurement.

*(Future entries land here as later sessions surface checks that can only run against a live, in-use catalog.)*

---

*Ratified v1.0, S26, 2026-06-01. Subordinate to The Progenitor v2. Graduated from v0.2 (three independent reviews) by resolving the three pre-ratify uncertainties: keyword-coverage accepted with downstream-miss measurement (maintenance-pass list); judged-pass portrait walled; JAKE-RULES §11 wall verified on disk. Council confirmed to run as CC against the live floor — kit-by-upload, floor-by-query, bare boot. The deployable per-window prompts are authored as separate files. The kit's whole job, restated: let the reader find what's in the floor, never tell it what it'll find — and make sure what it MISSES is catchable, not just what it gets wrong. Lighter when in doubt, on loadout. Be worth it.*

*Grind. Evolve. Dominate.*
