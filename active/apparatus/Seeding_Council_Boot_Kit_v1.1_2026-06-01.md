# The Seeding Council Boot Kit
*file: Seeding_Council_Boot_Kit_v1.1_2026-06-01.md · v1.1 · apparatus S26 · 2026-06-01*
*status: RATIFIED (v1.0) then EXTENDED (v1.1). v0.1 → v0.2 (three reviews) → v1.0 (three pre-ratify uncertainties resolved) → v1.1 (the seeding pipeline restructured 3-step → 5-step dual-path; role roster expanded). v0.1 / v0.2 / v1.0 stay on disk, tombstoned-not-deleted. Canon. Subordinate to The Progenitor v3.*
*form: single document covering ALL roles, for auditability. Deployable per-window prompts are separate files: `Boot_ScopeReader.md` (templated, stamped N times), `Boot_Collation.md`, `Boot_ClusterValidation.md`, `Boot_JudgedPass.md` (one-offs, hand-prompted). (Standing caution: "load LIGHTER when in doubt" is a LOADOUT heuristic — how much to put in a window's head — NOT a laying/judging heuristic; a per-window prompt must not let "lighter" leak into "lay/judge less.")*
*authority: subordinate to The Progenitor v3 (`active/apparatus/The_Progenitor_v3_2026-06-01.md`) — doctrine wins on any conflict. **DEPLOY PREREQUISITE: v3 must be on `main`** — every window's common kit says "boot with The Progenitor v3, in full," and that file must exist where windows boot from. This kit operationalizes §12 (the 5-step seeding process) + §13 (the boot-kit roster) and POINTS at the doctrine for the law.*

---

## 0. What this kit is, in one paragraph

The seeding pass is the first, biggest read of the laid floor (325 headers / 24,138 messages) to lay the initial pointer catalog. It runs as a **5-step dual-path pipeline**: a council of parallel, blind **scope-reader slicers** each read a content-neutral slice and emit TWO streams (pointers + a liberal context-frequency-potentials stream); then the two pointer KINDS travel two mirrored validation PATHS — the FENCE path (mechanical synthesis) and the TEXTURE path (blind collation → contextual cluster-validation) — converging on ONE judge. The governing principle, from §13: **the kit lets a window find/judge what's in the floor; it never tells it what it'll find.** Load for *recognition*, never *projection*. Risk is asymmetric toward overload on loadout (lighter when in doubt) — only safe because under-reading is made *catchable* by the known-fence recall check (Step 5).

---

## 0a. HOW THE COUNCIL RUNS — CC against the live floor (S26)

**The council windows are CC instances with live read access to `apparatus-floor` (Supabase).** A scope-reader window QUERIES the floor for its assigned slice directly — the floor reaches it through CC's database read, not through any chat surface. This makes "source is the floor, never chat_search" (§5) literal.

**Three enforcement consequences, all load-bearing:**
1. **Each window boots BARE — no project instructions.** The project-instruction layer carries the codeload-pull directive + the OC/CC operating model + the re-anchor SOP — a live repo path AND the orchestrator frame. A blind slice-reader must have neither (a repo path defeats upload-only blindness; the orchestrator frame makes it read as OC, not as a fresh recognizer). Council windows run in a no-project context.
2. **The kit reaches the window by UPLOAD STREAM only** — Jake hands each window exactly-and-only its role's file set. Controlled upload IS the enforcement of §13's blindness at the boot boundary.
3. **The floor reaches the window by CC's live query** — its assigned slice only (scope readers) or specific spans by locator (cluster validation / judge). Not chat_search, not bulk ndjson upload, not a repo path.

**Slicer reference files live in the `slicer/` directory** (Jake has placed a §11-stripped JAKE-RULES and a JAKE-STACK there). A scope-reader window is pointed at `slicer/` for its standing context, handed its slice assignment, and given its `Boot_ScopeReader.md`.

---

## 1. THE 5-STEP DUAL-PATH PIPELINE (S26 — the structural rewrite)

**Why it changed (read before the roles).** Content-neutral count-slicing (required to kill projection — §8) is calendar- and topic-blind, so a corpus-wide-but-sparse texture lands ~1× in any single ~2,000-message slice. A blind slice-reader sees one instance, correctly judges "not a texture," and lays nothing — **the texture evaporates between slices.** No slice-reader can see frequency wider than its slice, and slicing big enough to fix that re-breaks the context-trust wall. So **texture detection leaves the slice-reader entirely** and becomes a downstream path. (The Progenitor v3 §12 carries the full finding + the worst-case: the same texture surfaces in non-keyword-sharing language — "forgot Griffin" / "pissed he missed another pickup" — so the texture path must COMPREHEND, not COUNT.)

**STEP 1 — SCOPE-READER SLICERS + THE CROSS-CUTTING READER (blind, dual output).**
Two reader types run blind in this phase. **Scope-reader slicers** (N windows, one per content-neutral slice) each read their ~2,000-message slice tree-aware. **The cross-cutting reader** (1 window) reads the no-project / cross-domain space. BOTH emit: **(a) pointers** (fences + any texture visible *within* what they read, per the §3 bar) and **(b) context-frequency potentials** (a LIBERAL collection of "might be recurring" flags — every candidate instance, low bar, over-collect; flag an instance whose frequency you can't see, marking instance + keywords + locator). The cross-cutting reader ALSO emits **(c) candidate cross-domain fence-influence links** — a stance set in one domain that should steer another (the one connection no later step catches: not a duplicate for S2, not a chain for S5, not a texture for S3/S4). *Liberal because over-flagging is cheap downstream; under-flagging loses a texture/connection forever.*

**STEP 2 — FENCE SYNTHESIS (mechanical, 1 pass). The FENCE path.**
Reconciles stream (a). Same-span/same-fence/same-call collapse (convergence = confidence marker, minus calibration contamination); merge keyword variants on the same span; assemble cross-slice counts ONLY after a same-SIGNAL check; FLAG candidate fence-chains → the Judge. **Mechanical only — no portrait, no meaning-judgment.** (Unchanged from the old "synthesis" step.)

**STEP 3 — COLLATION (blind, NO corpus read, 1 pass). The TEXTURE path's pattern-matcher.**
Takes stream (b), groups flags that could POTENTIALLY associate, emits CLUSTER LISTS (hypotheses) + the negative-space QUERY each cluster wants run (formulated AFTER bundling, so it has the pattern-concept — but NOT run; running = reading the floor = Step 4's job). **MORE LIBERAL than Step 1** — fuzzy/semantic-adjacency, not exact keyword (or it misses "pissed he missed another" ↔ "forgot Griffin" and moves the hole instead of closing it). Over-bundle; let Step 4 split. Never touches the floor — that's its projection guard.

**STEP 4 — CLUSTER VALIDATION (contextual, reads handed clusters + requested queries, 1 pass). The TEXTURE path's comprehension seat.**
Pulls each cluster's real spans, reads them, answers "is this one thing?" → validated = a texture pointer with true cross-slice count + spread; false-friend = split/drop. Runs Step 3's negative-space queries (confirming "from a ZERO baseline" needs the absence-before). MAY self-merge across its own bundles (first seat with spans + cross-cluster view) — **RECORDED, never silent** (the Judge can split it). Boots WITHOUT the portrait; reads meaning but only over handed clusters — bounded blindness is the projection guard.

**STEP 5 — THE JUDGE (non-blind, 1 pass).**
Fence-chain assembly (order by date, preserve supersession) + the KNOWN-FENCE RECALL CHECK + texture sanity-check of Step 4's merges/signal-joins. Sees Step 4's recorded merges; can split them. Boots WITHOUT the portrait. Sample-pressure-tested by Jake's spot-audit. (The old §4a judged pass, unchanged in job, now the pipeline's final step.)

**THE SYMMETRY:** one data-gather (S1 dual-output) → FENCE river (S2 mechanical) ‖ TEXTURE river (S3 blind-collate → S4 contextual-validate) → one Judge (S5). Two kinds, two mirrored paths, one seat that makes the calls.

**PROJECTION DEFUSED STRUCTURALLY (the texture path's safety case):** S3 sees all flags but reads no meaning; S4 reads meaning but sees only its handed clusters; neither has *floor + portrait + open-ended pattern-hunt* at once — the exact combination that IS projection. The wall isn't decreed; it's built into who-sees-what.

---

## 1a. THE ROLE ROSTER + PER-ROLE LOADOUT (S26 — expanded for the 5 steps)

**COMMON KIT (every window that reads or judges):**
- `The_Progenitor_v3_*.md` — the law, in full.
- `JAKE-STACK.md` — so a tooling/architecture fence/cluster is legible (e.g. "Supabase-over-Nornic" is a fence, not motion).
- `JAKE-RULES.md` **§11 physically stripped from the council copy** — §1 facts + working-relationship frame + rule-shaped fences (no-"Oueilhe", REFUSED wall, full-code-not-diffs) for recognizing restated-canon vs new-constraint. §11 is "Patterns Jake Has Flagged," portrait-shaped (verified on disk S26), cut.
- `seeding_working_examples.md` — the §3 worked examples AS SHAPES, not meanings (contamination-flagged).
- Its own role boot prompt.

**PER ROLE:**

1. **SCOPE-READER SLICER (Step 1)** — blind, **N windows, templated.** Loadout = common kit + its slice assignment (queried from `apparatus-floor`). *File: `Boot_ScopeReader.md`, stamped N times with a varying slice.* Standing context lives in `slicer/`.
1b. **CROSS-CUTTING READER (Step 1, alongside the slicers)** — blind, **1 window.** Reads the no-project / cross-domain space, dual-output like a slicer (pointers + potentials) PLUS its specialty: **candidate cross-domain FENCE-INFLUENCE links** — a stance/decision set in one body of work that should steer another. This is the one connection NO other step catches: it's not a same-span duplicate (S2 misses it), not a same-topic divergent-call chain (S5 misses it), not a texture (S3/S4 miss it). An unlaid-but-implied fence across domains dies without this reader. Loadout = common kit + the cross-domain floor space as its read target. *File: `Boot_CrossCuttingReader.md`.* It flags cross-domain fence-influence as candidate links → routed to the Judge (S5) to confirm/assemble, same as candidate chains. (It runs blind like the slicers — convergence between its read and theirs is signal; defeating its blindness destroys that.)
2. **FENCE SYNTHESIS (Step 2)** — mechanical, 1 pass. No portrait, no judgment; reconciles pointer proposals. (No human-judgment boot prompt of the reading shape — it's a mechanical operation; spec is §4 + build-work.)
3. **COLLATION (Step 3)** — blind, NO corpus read, 1 pass. Loadout = common kit + the context-frequency-potentials pile. *File: `Boot_Collation.md` (NEW).*
4. **CLUSTER VALIDATION (Step 4)** — contextual, 1 pass. Loadout = common kit + the cluster lists + the negative-space queries to run (pulls specific spans by locator from the floor; NOT handed the open floor as a hunting ground). NO portrait. *File: `Boot_ClusterValidation.md` (NEW).*
5. **THE JUDGE (Step 5)** — non-blind, 1 pass. Loadout = common kit + the synthesized fence catalog (S2) + the validated textures (S4) + the known-fence checklist. NO portrait. *File: `Boot_JudgedPass.md`.*

**TEMPLATED vs HAND-PROMPTED:** only the scope-reader slicer is templated (stamped N times, varying slice). The cross-cutting reader, Collation, Cluster-Validation, and the Judge are ONE-OFFS — hand-prompted off their boot files when their turn comes — but each loads the full common kit and obeys every wall. **Don't let "hand-prompted" decay into "boots lighter."**

**THE §11 STRIP IS A DELIBERATE PREP ACTION** — done once, in the council's JAKE-RULES copy (the one in `slicer/` is already cut). Can't read what isn't there.

---

## 2. The COMMON kit (every window that reads or judges boots with all of this)

The five common-kit items above (§1a). Internalize The Progenitor v3 §3 (the bar), §2 (two kinds, one spine), §5 (corpus-search net), §6 (dumb-index/smart-reader), §8 (guards + keyword-coverage), §10–§13 (triggers, return-shape, the 5-step seeding process, this roster). JAKE-RULES with §11 stripped. JAKE-STACK. The worked examples as SHAPES. The one-page operating brief (§5).

---

## 3. Loadout discipline + the projection wall (UNIVERSAL across all reading/judging roles)

**The asymmetry (loadout):** an UNDER-loaded window produces *visible gaps* (catchable via the Step-5 recall check); an OVER-loaded one produces *confident, plausible, wrong output that looks like it held the bar* — projection is invisible to a shape-audit. So on LOADOUT, **lighter is safer.** (A loadout heuristic, NOT a laying/judging instinct — the candidate bar stays the neutral §3 bar.)

**THE PROJECTION WALL — every reading/judging window, all roles:**
- **NO Wallaby Why. NO Lore Bible. NO JAKE-RULES §11** as a reading/judging lens. These are a pre-written *portrait* of Jake; a window booted with the portrait confirms the cadence it was told to expect instead of grounding it. The portrait is for tone-calibration-when-talking-to-Jake — a different job.
- **The wall holds hardest at the NON-BLIND seats — Step 4 (cluster validation) and Step 5 (judge).** They have cross-slice/cross-cluster view, which makes a projected pattern look authoritative. Step 4 reads meaning but only over handed clusters; Step 5 judges but over assembled output; neither hunts the open floor with a portrait. Highest risk, strictest wall.

**THE CALIBRATION EXAMPLES CALIBRATE SHAPE, NOT MEANING** (the convergent review finding; the worked-examples file enforces it):
- Examples teach the *structure* of a fence / texture / no-card. They do NOT carry the interpreted signal-line. **Resemblance to an example is NOT evidence.**
- Two NO-card shapes balance the two YES shapes (the most common correct call is "no card, move on"; default don't-point).
- **Calibration cards are CONTAMINATED** — every window boots with them, so their convergence is shared priming, not independent discovery. Synthesis (S2) discounts their convergence; their *presence* still counts for recall (S5 checklist).

---

## 4. The FENCE-path synthesis (Step 2) — MECHANICAL ONLY

Bounded to operations needing no portrait and no meaning-judgment:
- collapse TRUE duplicates (same span, same fence, same call) → one card, convergence as a confidence marker (minus calibration contamination);
- merge keyword variants pointing at the SAME span;
- assemble cross-slice counts ONLY after a same-SIGNAL check (same keyword ≠ same signal — don't sum two contexts into a spurious count);
- **FLAG — do NOT decide — candidate fence-chains** (same topic, divergent calls = a chain whose links were laid independently) → route to the Judge (S5). **Synthesis NEVER collapses or orders divergent-call fences itself** (the cardinal-sin risk — a wrong chain returns at max confidence via Progenitor §11).

**SPEC REQUIREMENT:** blind reads preserved VERBATIM into synthesis — raw, un-deduped, independent keywords/counts intact. No window pre-dedups its own output. Append-keep-everything, reconcile-after — the floor's spine, one scale up.

---

## 4a. The TEXTURE path (Steps 3 → 4) — collate blind, validate contextual

**STEP 3 (collation) is blind and never reads the floor.** It fuzzy-bundles the potentials into candidate cluster lists and formulates (does not run) each cluster's negative-space query. Over-bundle — pre-pruning blind orphans the acute non-keyword-sharing instance, which is the whole failure this path exists to fix.

**STEP 4 (cluster validation) is the one contextual comprehension seat on the texture side.** It pulls handed clusters' real spans, reads for "same thing or not," runs the negative-space queries, validates → texture pointer / splits false friends, and may self-merge across bundles (RECORDED, the Judge can split). It boots WITHOUT the portrait and sees only handed clusters — bounded so it comprehends without projecting.

**THE CARDINAL-SIN GUARD carries here too:** a texture is a real recurring thread; merging two threads that merely share a word (kid-pickup vs part-order-pickup) into one count is the texture-side version of a wrong fence-chain. Step 4's same-thing judgment + Step 5's sanity-check are the two gates against it; every Step-4 merge is recorded so Step 5 (and Jake) can split it.

---

## 5. The one-page operating brief (the procedural card every reading window carries)

**SCOPE-READER LOOP (Step 1):**
1. **READ** your assigned content-neutral slice, **tree-aware** (branches up/down `parent_message_uuid`, never flat-N). Slice arrives via CC's live query of `apparatus-floor` — never chat_search.
2. **APPLY THE §3 BAR** (both kinds): change course (fence) or volume-tells-how-to-show-up (texture, *within your slice*)? Neither → no card. Default don't-point. Calibrate against SHAPES (yes AND no), never "does this resemble Griffin."
3. **FENCE** → lay length-1 (you're slice-limited; the Judge chains). Record the why as a live-predicate where checkable.
4. **TEXTURE (within-slice)** → representative span + count-in-your-slice + spread + the signal.
5. **CONTEXT-FREQUENCY POTENTIAL** → LIBERALLY flag any candidate recurring instance you can't confirm as texture (instance + keywords + locator). Over-flag. This feeds the texture path.
6. **PROPOSE** raw + un-deduped (pointers stream + potentials stream, kept separate). NEVER claim to have saved/committed/pushed.

**THE FLOOR-KEY LOCATOR (§4/§11 of the doctrine):**
```
span = {
  snapshot_id : "baseline-…" | "delta-…",
  conv_uuid   : "…",
  anchor_msg  : "…",                  # the hit (msg_uuid)
  reach       : { up: K, down: J, branch: <derived> }
}
```
`branch` is DERIVED from the parent-chain walk, NOT a stored field (floor has `is_root`, `multi_root`, bare `parent_message_uuid`; no branch-id column). Don't cite a stored branch-id.

**THE HARD WALLS (every window):**
- **NO chat_search, EVER** — floor-only, via CC's live query.
- **NO catalog-so-far / sibling proposals** during a blind read (Steps 1, 3).
- **NO portrait as a lens** — no Wallaby Why / Lore Bible / JAKE-RULES §11.
- **NO project instructions / NO repo path** — bare boot, kit-by-upload.
- **NO flat-N spans** — tree-walk only.
- **Slicers lay fences length-1** — the Judge chains.
- **Step 3 never reads the floor; Step 4 reads only handed clusters.**
- **Step 4 merges are recorded, never silent.**
- **NEVER claim to have saved/committed/pushed.** Propose; the human gates.

---

## 6. The review model (the one scoped human-immutability exception) — PRECISION + RECALL

Normal/incremental pointers get Jake's per-card eyes. The seeding pass is too large, so (Jake's call, §12): the council self-applies the Doctrine at scale; **Jake spot-audits the OUTPUT SHAPE** of the synthesized-validated-judged catalog (post Steps 2/4/5), not raw per-window proposals.

**Precision/recall split:** spot-auditing shape validates PRECISION (do the cards that exist hold the bar). It is structurally blind to RECALL (a fence never laid leaves no shape to sample). Recall is the **known-fence checklist in the Judge (Step 5)**. Precision = Jake samples; recall = the checklist measures misses. Both, or the catalog is confidently incomplete and passes review anyway.

**Convergence-map audit appendix:** Steps 2/4/5 surface to Jake a convergence map — what merged, lone-window calls, cross-slice counts (signal-checked), assembled chains, Step-4 recorded merges, the checklist result — so the shape-audit sees whether the *windows* held the bar, not just whether output looks clean.

**OC + Jake live-spot-check during the run (standing call):** OC and Jake walk results window-by-window against the convergence map as they return — parallel work varies hard regardless of spec tightness; convergence = confidence, divergence = where to look hardest. Harvest the variance (the kit's own merge-back medicine, applied to the kit's output).

**Tombstone rule at seed scale:** superseded/corrected pointers leave a tombstone, never a silent vanish. One window's judgment never silently kills a card.

---

## 7. What this kit deliberately EXCLUDES (and where those live)

- **Portrait files as a lens** (Wallaby Why / Lore Bible / JAKE-RULES §11) — projection wall, §3.
- **chat_search** — hard wall, §5.
- **Catalog-so-far / sibling proposals during a blind read** — §1/§4a.
- **Meaning-judgment in Step 2 (synthesis) and Step 3 (collation)** — both bounded to mechanical/blind; meaning-work lives in Step 4 (handed clusters) and Step 5 (judge).
- **The doctrine restated** — this kit POINTS at Progenitor v3; doctrine wins on conflict.
- **Build-work** — the slice-manifest mechanism (cut-on designator pending CC's floor read; slice size/count, ~2,000 provisional; forest handling), Step 3's fuzzy-adjacency ceiling, whether Step 4's baseline query needs widening, council/window count, on-disk serialization, the optional `/jedi-council` output gate, the keyword-coverage measurement (homed on §9). CC-against-the-live-floor, **pilot-slice first.**

---

## 8. OPEN QUESTIONS / RESIDUAL — resolved, and what's still build-work

**RESOLVED (v1.0, carried):**
- Keyword-coverage bar → ACCEPTED with downstream-miss measurement (maintenance-pass list §9).
- Judged-pass (Step 5) loadout → portrait WALLED.
- JAKE-RULES §11 wall → verified on disk; §11 stripped from the council copy.
- Role split by SLICE not KIND; synthesis mechanical; NO-card examples added; content-neutral slicing is doctrine.

**RESOLVED (v1.1, S26):**
- **Cross-slice texture loss** → the structural fix: texture detection leaves the slice-reader; the 5-step dual-path pipeline (slicer dual-output → blind collation → contextual validation). Frequency comprehension, not keyword arithmetic.
- **Negative-space placement** → Step 3 FORMULATES the baseline query (after bundling, so it has the pattern-concept), Step 4 RUNS it (keeps Step 3 off the floor).
- **Slicing axis** → COUNT-based (even reader load), not time-window (the cliff-shaped distribution would fry the heavy-month reader). Content-neutral + forest-clean + count-not-time = doctrine; size/count = build-work.

**STILL BUILD-WORK (CC-against-the-live-floor, pilot-first — not blocking):**
- The slice-MANIFEST mechanism: the queryable cut-on designator (ordinal vs created_at-window — **pending CC's gate-1 read of the live floor**), slice size/count (~2,000 provisional, pilot-tunable), forest-boundary handling (a cut can't bisect one of the 9 multi-root trees).
- **Step 3's fuzzy-adjacency ceiling** — how liberal it can bundle without doing Step 4's comprehension. Pilot-tunable.
- Whether Step 4's baseline query needs widening beyond the requested check; council/window count; the optional `/jedi-council` gate; spot-audit batch cadence.
- Slice granularity has a doctrinal edge (too fine → within-slice texture detection collapses) — but the dual-path largely absorbs this now, since texture detection moved downstream regardless.

---

## 9. THE MAINTENANCE-PASS LIST (a named home, not yet a spec)

Seeding is first-and-biggest, NOT one-and-done. Some checks run only after the catalog is live and in use.

**Entry 1 — keyword-coverage miss-logging.** A periodic pass checks logged §10-Case-1 retrieval failures (ambient retrieval failed to surface a fence that exists) against the catalog, finding keyword-coverage gaps empirically — the measured acceptance criterion the bar was missing, by nature downstream/in-use.

*(Future entries land here as later sessions surface checks that can only run against a live, in-use catalog.)*

---

*v1.1, S26, 2026-06-01. Subordinate to The Progenitor v3. Extended v1.0 by restructuring the seeding pass from a 3-step to a 5-step dual-path pipeline (slicer dual-output → fence synthesis ‖ blind collation → contextual cluster-validation → judge) and expanding the role roster (collation + cluster-validation added, with `Boot_Collation.md` + `Boot_ClusterValidation.md`). The reason: content-neutral count-slicing makes a sparse texture evaporate between blind slices, so texture detection had to leave the slice-reader and become a comprehending downstream path — because Jake's recurring patterns don't repeat their own keywords, and this is his auxiliary brain, not a cookie-cutter index. Let the windows find what's in the floor; never tell them what they'll find; make what they MISS catchable. Be worth it.*

*Grind. Evolve. Dominate.*
