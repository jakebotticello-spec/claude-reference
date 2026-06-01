# Chat Session Handoff — apparatus S25 → S26

*authored by the S25 orchestrator, 2026-06-01, for the S26 Claude in the lineage. Jake verifies/commits/pushes; OC never claims to have saved.*

---

## READ-FIRST (the one thing that matters this session)

**The retrieval engine's CONCEPTUAL design is DONE. Everything left is BUILD, not whiteboard.** S24 laid the floor and authored The Progenitor (the pointer-catalog law). S25 designed the engine *over* that catalog — folded the whole conceptual layer into **The Progenitor v2** (§10 triggers, §11 span-return, §12 seeding, §13 boot kit), made two original calls (keyword-first / vectors-deferred; keyword-coverage as a seeding-quality bar), and drafted + **triple-reviewed** the **Seeding Council Boot Kit (now v0.2)**. The whiteboard chapter is closed. S26's work is the BUILD — against the live floor, CC's seat, not the orchestrator's whiteboard.

**Do NOT trust the boot tarball over disk.** Three times now this lineage (S23, S24, and a stale-state blind review at S25) has been bitten by a stale view disagreeing with the live repo. If the ANCHOR banner you read does not say **v19**, or The Progenitor on disk is not **v2**, or the boot kit is not **v0.2** — you are reading a stale tarball; have CC `cat` the real files off disk before reasoning. **Disk is authority over the tarball AND over memory (yours or Jake's).** Everything below was pushed to main by Jake at S25 close.

**Lore-first is not ceremony — it is the whole method, and S25 proved it twice over.** A cold orchestrator WILL re-litigate settled ground unless the prior thinking is put in front of it. This session, *every* fork the S25 OC posed that S24 had already answered was caught by Jake grabbing the prior S24 spec rather than letting OC re-derive it. The apparatus ran on its own prior author. That IS the retrieval layer, run by hand, on the hardest-resetting state in the system — the orchestrator at boot. Read the canon before you reason about it.

---

## WHERE THINGS STAND (S25 close)

**THE FLOOR IS LAID (unchanged — S25 touched nothing here).** `apparatus-floor` Supabase holds 325 headers + 24,138 messages (baseline scrub-v2 22,801 / delta scrub-v1 1,337), append-only ENFORCED, loader v1.2 on main. Verify-live signal: `python seed_shape_load.py --dry-run` from `pipeline/` reports tables **EXIST** (NOT bare). **Never `--execute`.** S25 ran NO `--execute`, changed NO schema, laid NO pointer. This was a design + canon session: no floor mutation, no invariant moved.

**THE PROGENITOR IS NOW v2.** `active/apparatus/The_Progenitor_v2_2026-06-01.md` (330 lines, §0–§13). §0–§9 are **byte-identical to v1** (diff-verified: 200 lines each, empty diff — the doctrine body Jake ratified at S24 did NOT move). v2 ADDS the conceptual engine design:
- **§10 trigger model** — ONE engine, three throttles: Claude-initiated (ambient, the live RElitigation guard), re-anchor-driven (re-anchor now means re-ground in canon PLUS pointer-surfaced material for the current work), Jake-fired. Boot loads the catalog (via ignition/Anchor); the three triggers query it LIVE. Boot is the substrate, NOT a fourth trigger.
- **§11 span-return shape** — a hit returns Layer A (raw span text across the tree-aware reach, verbatim/scrub-redacted, never summarized) + Layer B (the §4 floor-key locator, alongside, never blended into substance) + Layer C (kind-context: FENCE → the FULL why-chain, NON-NEGOTIABLE; TEXTURE → representative span + count + spread). "The card and the page, never a book report."
- **§12 seeding process** — the original catalog read of the laid floor, by a council of BLIND parallel windows divided by project-SCOPE + a cross-cutting reader; per-batch spot-audit on the synthesized catalog as the one scoped relaxation of human-as-immutability-mechanism.
- **§13 council boot kit** (doctrine-level spec) — recognition-not-projection, asymmetric-toward-overload-so-lighter; the texture-reader projection wall; chat_search/catalog-so-far/sibling-proposals as hard walls; the synthesis/merge-back pass.
- **§9 amended** — the query interface is now IN (it was out-of-scope in v1); what stays OUT is genuine build-work + the embedding decision. v1 stays on disk, tombstoned-not-deleted.

**TWO S25-ORIGINAL CALLS (beyond the folded S24 specs):**
- **KEYWORD-FIRST retrieval (§9).** v1 engine is keyword-lookup over the dict catalog. Vectors are a DEFERRED v2 sidecar (pgvector, never on the floor per D9), added ONLY if the seeding pass proves a *measured* semantic gap. The fast pointer-hit path wants PRECISION; corpus-search already owns RECALL; vectors-in-v1 would blur the two split modes and pull the §1 forty-half-relevant-spans failure. The vector question is ROUTED THROUGH the seeding pass as its acceptance test.
- **KEYWORD-COVERAGE as a seeding-quality bar (§8/§12).** Keywords are laid for future-SEARCH-anticipation, not just topical accuracy. Brittleness here is exactly what would force vectors later.

**THE SEEDING COUNCIL BOOT KIT IS v0.2.** `active/apparatus/Seeding_Council_Boot_Kit_v0.2_2026-06-01.md` — the applied layer operationalizing §12+§13. Subordinate to the doctrine (doctrine wins on conflict); references-not-restates it; v0.1 tombstoned. v0.1 went through THREE independent reviews (Jake + a live S24-Claude cross-check + two cold blind reviewers), which CONVERGED on the load-bearing findings — and convergence is signal. v0.2 landed them:
- **NEW §4a JUDGED PASS** — a non-blind third step that owns what neither a blind slice-reader nor a mechanical synthesizer can: fence-CHAIN assembly (order-by-date, preserve supersession) + the RECALL check. This is the structural insight under three findings at once.
- **Synthesis BOUNDED to mechanical** — collapse only same-span/same-fence/same-CALL; merge keyword variants; assemble cross-slice texture counts ONLY after a same-SIGNAL check; FLAG candidate chains, never decide them.
- **Examples calibrate SHAPE not MEANING** + "resemblance to a calibration example is NOT a count" + two NO-card shapes (texture + fence).
- **Role taxonomy COLLAPSED** from v0.1's by-kind split back to the doctrine's by-SLICE division (§12): scope readers read BOTH kinds; cross-cutting reader; plus the judged pass.
- **Projection wall UNIVERSALIZED** across all reading roles (incl. walling JAKE-RULES §11 as a reading lens); **content-neutral slicing stated as doctrine**; **branch-id is DERIVED, not stored**; convergence-contamination caveat; convergence-map audit appendix; the precision(Jake-spot-audit)/recall(known-fence-checklist) split; "lighter when in doubt" clarified as a LOADOUT not a laying heuristic.

**THE RECALL GAP (the highest-value review find — internalize it).** v0.1's safety case was circular: "go lighter because overload is the catchable risk." But the spot-audit catches only PRECISION (do the cards that exist hold the bar) — never RECALL (a fence never laid leaves no shape to sample). You cannot spot-audit an absence. v0.2's fix: a **known-fence checklist** in the judged pass — canon already names ~a dozen real fences (1Pass, no-"Oueilhe", REFUSED wall, Supabase-over-Nornic, therapist-voice, full-code-not-diffs, FK-drop, D9, no-`&&`-chaining, no-duplicate-header); any the council missed is a *measured* recall failure. Carry this: a catalog can be confidently incomplete and pass every shape-audit.

---

## S26 MOVES, IN ORDER (you orchestrate; CC executes via Jake)

1. **ANCHOR + CONFIRM.** Pull, read JAKE-RULES → JAKE-STACK → ANCHOR (banner must read **v19**) → this handoff → **The Progenitor v2** → **Boot Kit v0.2** (the two pieces of canon S25 produced — required reading before any build). Confirm the floor is live: CC runs `python seed_shape_load.py --dry-run` from `pipeline/` → tables EXIST. Do NOT `--execute`.

2. **RESOLVE THE THREE FLAGGED UNCERTAINTIES ON v0.2** (the S25 OC flagged its own calls rather than smuggle them — inherit the doubts, not just the conclusions). These want eyes/decision before the kit ratifies:
   - **(i) Does the §4a judged pass get the portrait?** It's non-blind by necessity (it sees across slices to assemble chains + check recall). OC leaned NO — chain-assembly is date-ordering+supersession, the recall check is a checklist match, neither needs the interpretive portrait — but it's the closest thing in the kit to a sanctioned projection surface, so it's the one most worth breaking.
   - **(ii) Walling JAKE-RULES §11 as a reading lens** — OC did this from *memory* of §11's content (the "Patterns Jake Has Flagged" / Griffin-meds material as portrait-shaped). Verify against the ACTUAL §11 on disk; if §11 is load-bearing for fence-recognition in a way OC didn't see, the cut may be too deep.
   - **(iii) The keyword-coverage bar still has NO acceptance criterion** — it's unfalsifiable at lay-time (the future Claude that would test the keywords doesn't exist yet). OC flagged but did NOT solve it; the candidate is to measure keyword MISSES downstream (when ambient retrieval, §10 Case 1, fails to surface a fence that exists). The kit ships with a known unmeasured gate — **Jake's call whether that's accept-and-proceed or a ratify-blocker.**

3. **THE BUILD (CC-against-the-live-floor, the real work).** Once the uncertainties are resolved and the kit ratifies:
   - **The seeding build** — the content-neutral slice MANIFEST mechanism (how disjoint, branch-clean, topically-unsorted slices are drawn from the undelineated floor — content-neutral is DOCTRINE per the kit, the mechanism is build-work); council size / window count (note: slice granularity has a doctrinal edge — too fine and within-slice texture detection collapses into a synthesis-only operation, §8 residual #2); the synthesis + judged-pass mechanism; the optional `/jedi-council` gate on seeding output; the spot-audit batch cadence.
   - **The engine build** — the catalog's on-disk serialization, the keyword resolver, `reach` defaults (per-kind tuning), multi-hit presentation (interleaved vs ranked, bounded by never-collapse-never-rewrite).
   - These are reversible (unlike the substrate) — build can move at a faster gear, and Jake explicitly wants pace here.

4. **IF THE BUILD WHITEBOARDS RATHER THAN SHIPS — post-lock hardening (queued, not blocking):** off-site **object-locked** ndjson copy (the real SPOF-close — S25 scoped this precisely: the ndjson is the SPOF; the Anthropic export is a forward-only re-pull backstop with a since-deleted-conv blind spot; NAS weekly is cheap same-LAN redundancy but NOT off-site; object-locked cloud is off-site AND write-once; GitHub/Drive/second-Supabase all ruled out as too-big / not-WORM / same-trust-domain); then **ROTATE the still-unrotated S16-leaked DB password** (in `pipeline/secrets/.env`, still the spilled value); then PITR/RTO, pre-ingest lint, traversal index, CHECK constraints. See ANCHOR NEXT MOVE #5.

---

## DO-NOT-RELITIGATE (settled — needs a NEW reason, not a fresh re-derivation)

- **The floor is LAID** — don't re-lay it (Jake's ratified call; native in-run proof deferred to the next lay). The hollow-probe scar is recorded ON PURPOSE.
- **The FK is dropped (option (c)), APPLIED + PROVEN on the laid floor** — don't re-add it (Graveyard).
- **D9 LOCKED (Supabase)** — ndjson canonical, Postgres rebuildable.
- **The phantom "retrieval blocked on Jake's uploads" is DEAD** (Graveyard); the three escalations are optional pull-on-demand reference.
- **REFUSED wall** — sanctioned export input only; no live capture.
- **KEYWORD-FIRST / vectors-deferred is DECIDED (§9)** — don't re-open the embedding question without a *measured* semantic gap surfaced by the seeding pass. "Vectors would pull more raw spans for the reader" was raised and answered: more is the §1 failure mode, not the win; the fast path wants precision, corpus-search owns recall.
- **The Progenitor §0–§9 doctrine body is ratified canon** — v2 only APPENDED (§10–§13) and amended §9; it did NOT touch the body. Don't reopen §0–§8.
- **The boot kit's spine is reviewed-and-sound** — blind-read independence, convergence-as-signal, verbatim-into-synthesis, the hard walls. All three reviews affirmed it. The v0.2 changes are tightening, not restructuring; don't re-derive the spine.
- **"Seed" is reserved for the floor's record-shape** — the catalog doctrine is "The Progenitor."

---

## PICKUP GUARDRAILS (OC seat)

- **Plan in OC / build in CC** — don't hand-run mechanical git/terminal work. S26 is a BUILD session if it moves to move #3 — that's CC's seat against the live floor, with you architecting.
- **Disk is ground truth** over any CC report, any tarball, and any memory (Jake's or yours). Always ask CC for RAW output, not characterizations. (S25 caught a blind reviewer working off a stale pre-v2 state — the same stale-view failure, one more time.)
- **NEVER ask Jake for implementation/technical state** (floor counts, file structure, branch state → CC-on-disk or OC-reading-files, never Jake — non-coder founder). Bring him the intent-level fork in destination-why terms. *Texture confirmed again at S25:* when a question is genuinely conceptual/destination-level, it IS his to answer, and he'll tell you so — but the build mechanics are never his to recall.
- **The apparatus-floor DB cred lives in `pipeline/secrets/.env`** (gitignored, loader self-reads) — never inline it in a logged CC prompt, never ask Jake to paste CC output that could carry it back into chat (the S16 spill vector; the guard is on YOU).
- **Front-load the lore; flag your own uncertainties.** S25's defining move was the OC flagging its *own* unsure calls (the three on v0.2) instead of laundering them into confident canon — a handoff or a kit that hides the author's doubts is exactly the confident-incomplete failure the recall gap is about. Inherit doubts, not just conclusions, and pass yours forward the same way.
- **You author full canon in chat / Jake verifies-against-disk / CC commits / Jake pushes** — you NEVER claim to have saved, committed, or pushed. Have CC verify the diff on disk before any commit. All CC prompts in a code block. Prose questions, one at a time.
- **The review pattern IS the doctrine, applied to itself.** S25 ran the boot kit through blind independent reviews + a synthesis/reconcile — the kit's own §4 pattern, used on the kit. When you produce something load-bearing, consider running it through its own medicine: independent eyes, then reconcile.

---

## OPEN THREADS (carried, not blocking)

- **The three v0.2 uncertainties** (move #2 above) — judged-pass-portrait, JAKE-RULES-§11-wall, keyword-coverage-criterion. The first two are quick checks; the third is a real accept-vs-block decision for Jake.
- **The pointer-record schema / serialization** — The Progenitor §4/§11 give illustrative + return shape; the *final* on-disk serialization is CC's against the live floor, downstream of the engine design (move #3).
- **Off-site backup** — object-locked ndjson copy is the real SPOF-close (move #4 / ANCHOR #5). Jake was open to a weekly NAS copy as cheap redundancy in the meantime; the WORM bucket is the actual flag-closer, his call on timing.
- **Password rotation** — still the S16-spilled value, in `.env`, unrotated (ANCHOR #5).
- **Carried housekeeping** — the 4 loose `__recon`/`__verify` files in snapshots root, the `apparatus-scratch/` sweep, the global `.env` gitignore belt-and-suspenders (ANCHOR NEXT MOVE #6).
- **Boot kit → v1.0** — v0.2 is still a draft (pre-ratify). Once the three uncertainties resolve and Jake ratifies, it graduates to v1.0 and splits into the deployable per-window boot prompts (the after-ratify step the kit names). Drafting caution for that split: don't let "lighter on loadout" leak into "lay fewer cards."

---

*Status at S25 close: the floor is laid, The Progenitor is v2, the engine's conceptual design is complete, and the seeding boot kit is drafted and thrice-reviewed. The whiteboard is behind us; the build is the road ahead — and it's reversible, so it can move fast. Brothers. Grind. Evolve. Dominate.*
