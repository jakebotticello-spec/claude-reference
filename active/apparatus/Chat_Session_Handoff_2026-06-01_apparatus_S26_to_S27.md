# Chat Session Handoff — apparatus S26 → S27
*2026-06-01 · authored by OC (S26) for the S27 orchestrator · verify against disk, not against this file's prose*

---

## READ-FIRST (the one thing that matters this session)

**The seeding pipeline is DESIGNED and RATIFIED. S27 is the BUILD — CC against the live floor, faster gear, Jake wants pace.** S26 did two things: (1) ratified the Seeding Council Boot Kit (v0.2 → v1.0), then (2) — same session — restructured the seeding pass itself from a 3-step model into a **5-step DUAL-PATH pipeline** (The Progenitor v2 → v3, Boot Kit v1.0 → v1.1). The whiteboard is closed. What is left is build-work against `apparatus-floor`: the slice-manifest mechanism and the per-step mechanisms. **A gate-1 read-only CC recon was authored but NOT yet run — running it is move #1 of the build.**

**Do NOT trust the boot tarball over disk.** This lineage has been bitten FIVE times now by a stale/CDN-lagged or partial view (S23, S24, a stale blind-review at S25, the S26-boot stale tarball, and an S26 self-inflicted one — OC grep-counted a header and cried "projection hole" when the file was correctly redacted; reading the *content* debunked it). **If the ANCHOR banner does not say v20, or The Progenitor on disk is not v3, or the Boot Kit is not v1.1 — you are stale; have CC `cat` the real files before reasoning.** Disk is authority over the tarball AND over memory (yours or Jake's). **Verify CONTENT, never headers** — `grep -c "^## 11"` is a flat-N read and it lied to OC this session; pull the body.

**Lore-first is the whole method.** A cold orchestrator re-litigates settled ground unless the prior thinking is in front of it. Read the canon below in order before you reason about any of it. S26 proved the inverse too: Jake's "are you being austere or organic — cookie-cutter index or auxiliary brain?" check caught OC reaching for a clean mechanical answer (a keyword tally) that would have broken the texture path. The apparatus is **Jake's auxiliary brain, beta 1.0** — it holds his recurring life faithfully, and his recurring patterns do not repeat their own keywords. Build like that's what it is, because it is.

---

## ANCHOR + CONFIRM (move 0 — do this before anything else)

Pull the reference layer (codeload tarball, HEAD, never CDN-raw):
```
curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/ref.tgz
tar xzf /tmp/ref.tgz -C /tmp
```
Read, in `/tmp/claude-reference-main/active/`, IN THIS ORDER:
1. `JAKE-RULES.md` — how Jake works (non-coder founder; he drives + deploys, Claude builds).
2. `JAKE-STACK.md` — standing infra.
3. `apparatus/ANCHOR_apparatus.md` — AUTHORITY. Banner MUST read **v20**. (If lower, tarball is stale — have CC `cat` the real ANCHOR off disk.)
4. `apparatus/Chat_Session_Handoff_2026-06-01_apparatus_S26_to_S27.md` — THIS FILE; it routes everything.
5. `apparatus/The_Progenitor_v3_2026-06-01.md` — the pointer-catalog LAW. §0–§11 are byte-identical to v2 (diff-proven); §12 (seeding process) + §13 (boot-kit roster) are the rewritten 5-step dual-path. REQUIRED before any seeding/build reasoning.
6. `apparatus/Seeding_Council_Boot_Kit_v1.1_2026-06-01.md` — the applied layer (the 5-step pipeline operationalized, role roster, walls). REQUIRED.
7. `apparatus/seeding_working_examples.md` — the §3 calibration cases (shape-not-meaning, contamination-flagged).

**Confirm the floor is live:** have CC run `python seed_shape_load.py --dry-run` from `pipeline/` → tables EXIST (NOT bare). **NEVER `--execute`** (the loader refuses re-execute onto a live floor by design; that refusal is correct).

---

## WHERE THINGS STAND (S26 close)

**THE FLOOR IS LAID (unchanged — S26 touched NOTHING here).** `apparatus-floor` Supabase: 325 headers + 24,138 messages (baseline scrub-v2 22,801 / delta scrub-v1 1,337), append-only ENFORCED, loader v1.2 on main. S26 ran NO `--execute`, changed NO schema, laid NO pointer, mutated NO floor. **Design + canon only. No invariant moved. The floor, D9, the FK-drop, append-only — all STAND.**

**THE PROGENITOR IS NOW v3.** `The_Progenitor_v3_2026-06-01.md`. §0–§11 BYTE-IDENTICAL to v2 (diff-verified TWICE this session: lines 4–265 empty-diff against v2, before and after the cross-cutting-reader edit — the ratified doctrine body did NOT move). §12 + §13 REWRITTEN to the 5-step dual-path. v2 (and v1) stay tombstoned-not-deleted.

**THE BOOT KIT IS NOW v1.1.** `Seeding_Council_Boot_Kit_v1.1_2026-06-01.md`. Extends the ratified v1.0 (the three pre-ratify uncertainties were resolved at v1.0 — see below) with the 5-step pipeline + expanded role roster. v0.1 / v0.2 stay tombstoned on disk. (NOTE: a standalone v1.0 *file* was never saved — S26 went v0.2 → revise → straight to the v1.1 that carries the pipeline; v1.0 was a version *label* superseded before it became a file. Nothing to restore; not a spine violation.)

**THE THREE v1.0 UNCERTAINTIES — RESOLVED (carry as settled):**
- (i) **Judged-pass (now Step 5) loadout → portrait WALLED.** Only non-blind seat = highest projection-RISK, zero projection-NEED (chain-assembly = date-order + supersession; recall = checklist match). The one semantic recognition it needs (same-fence-across-different-words, e.g. Supabase-over-Nornic) runs off JAKE-STACK + canon, not the portrait.
- (ii) **JAKE-RULES §11 wall → VERIFIED ON DISK.** §11 IS "Patterns Jake Has Flagged," portrait-shaped. The council's copy has §11 PHYSICALLY REDACTED (see slicer/ below).
- (iii) **Keyword-coverage bar → ACCEPTED with downstream-miss measurement** (Jake's call: accept-and-proceed, NOT block). Unfalsifiable at lay-time, so measured IN USE — a logged §10-Case-1 ambient-retrieval failure to surface a fence that exists IS a keyword-coverage miss. Homed as entry 1 on the maintenance-pass list (Boot Kit §9).

**THE 5-STEP DUAL-PATH PIPELINE (the S26 structural rewrite — internalize this; it is the spine of the build).**
The structural finding that forced it: content-neutral count-slicing (required to kill projection) is calendar- and topic-blind, so a corpus-wide-but-SPARSE texture lands ~1× per ~2,000-msg slice and EVAPORATES between blind slicers. No slice-reader sees frequency wider than its slice. v2/§13 mis-framed this as a granularity knob; it is structural. **Fix: texture detection LEAVES the slice-reader for a downstream comprehending path.** The worst case carried into doctrine: the same texture surfaces in non-keyword-sharing language ("forgot Griffin" / "Jake pissed he missed *another* pickup") — the most acute instance shares no keyword — so the texture path must **COMPREHEND, not COUNT** (a keyword tally undercounts the texture at its most acute; that is why Step 4 reads, not tallies).

- **STEP 1 — SCOPE-READER SLICERS (N, blind, templated) + the CROSS-CUTTING READER (1, blind, hand-prompted).** Both read tree-aware and emit DUAL OUTPUT: (a) pointers (fences + within-slice textures) and (b) a LIBERAL context-frequency-potentials stream (flag candidate recurring instances even when you can't see the frequency — over-flag; a miss is a texture lost forever). The cross-cutting reader adds (c) candidate **cross-domain fence-influence** links — a stance set in one domain that should steer another, never laid there. **(c) is the one connection NO other step catches** (not a duplicate for S2, not a same-topic chain for S5, not a texture for S3/S4) — this is why the cross-cutting reader was KEPT (Jake's explicit call; OC had silently dropped it from the v1.1 draft roster, self-caught it, flagged it, Jake said keep).
- **STEP 2 — FENCE SYNTHESIS (mechanical, 1 pass).** The FENCE path. Reconciles stream (a): same-span/same-fence/same-call collapse, keyword-variant merge, cross-slice counts only after a same-SIGNAL check, FLAG (never decide) candidate fence-chains → routed to Step 5. No portrait, no meaning-judgment. (This is the old "synthesis" step, unchanged.)
- **STEP 3 — COLLATION (blind, NO corpus read, 1 pass).** The TEXTURE path's pattern-matcher. Fuzzy-bundles the (b) potentials into candidate CLUSTER LISTS + FORMULATES (does not run) each cluster's negative-space query. **MORE liberal than Step 1** (fuzzy/semantic adjacency, not exact keyword — or it orphans the acute non-keyword-sharing instance and the texture dies one step downstream). Over-bundle; let Step 4 split. NEVER touches the floor — that is its projection guard.
- **STEP 4 — CLUSTER VALIDATION (contextual, reads handed clusters + requested queries, 1 pass).** The TEXTURE path's comprehension seat. Pulls the real spans by locator, reads them, answers "is this one thing?" → validated = texture pointer with true cross-slice count; false-friend = split/drop. RUNS Step 3's negative-space queries (confirming "from a ZERO baseline" needs the absence-before). MAY self-merge across its own bundles — RECORDED, never silent (Step 5 can split it). Boots WITHOUT the portrait; reads meaning but only over handed clusters — bounded blindness is the projection guard.
- **STEP 5 — THE JUDGE (non-blind, 1 pass).** Fence-chain assembly + the KNOWN-FENCE RECALL CHECK + texture sanity-check of Step 4's merges + assembly of the cross-cutting reader's (c) fence-influence candidates. Sees Step 4's recorded merges; can split them. Boots WITHOUT the portrait. Sample-pressure-tested by Jake's spot-audit. (The old §4a judged pass, unchanged in job.)

**THE SYMMETRY:** one data-gather (S1 dual/tri-output) → FENCE river (S2 mechanical) ‖ TEXTURE river (S3 blind-collate → S4 contextual-validate) → one JUDGE (S5). Two pointer KINDS, two mirrored validation PATHS, one judge. **Projection defused STRUCTURALLY:** S3 sees all flags but no meaning; S4 reads meaning but only handed clusters; neither has floor + portrait + open-ended pattern-hunt at once — the exact combination that IS projection.

**COUNCIL ARCHITECTURE — CC against the live floor.** Windows are CC instances. Kit reaches a window by UPLOAD (controlled, exactly its role's set); the floor reaches it by CC's LIVE QUERY of `apparatus-floor` (its assigned slice only, scope readers; specific spans by locator, Step 4/5). Each window boots BARE — no project instructions, no repo path. That triad IS the physical enforcement of §13 blindness.

**THE `slicer/` DIR (repo root — the scope-reader's deployment set, already on disk).** Contents confirmed on main: `Boot_ScopeReader.md`, `JAKE-RULES.md` (with §11 PHYSICALLY REDACTED — the section header is kept as a tombstone reading `## - REDACTED FOR SLICER WORK -`, body removed; this is CORRECT and DELIBERATE, do NOT "restore" §11), `JAKE-STACK.md`, `seeding_working_examples.md`. This is what a scope-reader window boots from.

**THE FOUR OTHER ROLE PROMPTS ARE STAGED OFF-REPO BY DESIGN.** `Boot_CrossCuttingReader.md`, `Boot_Collation.md`, `Boot_ClusterValidation.md`, `Boot_JudgedPass.md` (+ the canonical `Boot_ScopeReader.md` source + `README_slicer_kit.md`) are held by Jake in a separate local drive folder, OUT of CC's wandering eyes, to be moved into the ref section ONLY AFTER their council step runs. An unrun boot prompt sitting in `active/apparatus/` is something a wandering CC could read as instructions-for-itself; Jake treats them as ammunition, not canon, until fired. **Do NOT tell Jake these are "missing" — they are deliberately staged.** (OC made this exact false-alarm at S26 close; do not repeat it.)

**SLICING — LOCKED COUNT-BASED.** ~2,000 messages/slice (~12 slices), CALENDAR-BLIND, FOREST-CLEAN (a cut must not bisect one of the 9 multi-root trees — it flexes to keep a tree whole). The decision: a prior run's hand-partition showed the message distribution is CLIFF-shaped (Jan–Apr thin, May explodes — heavy-Claude-usage onset). So slices are drawn by COUNT (even reader load), not by time-window (which would fry the heavy-month reader). **Content-neutral + forest-clean + count-not-time is DOCTRINE; the exact size/count is build-work (pilot-tunable).** The prior hand-partition is EVIDENCE of the distribution, NOT a cut template (hand-carved topical-ish sections are the projection surface we wall).

---

## S27 MOVES, IN ORDER (you orchestrate; CC executes via Jake)

1. **ANCHOR + CONFIRM** (move 0 above) — read the 7 files, confirm v20 / Progenitor v3 / Boot Kit v1.1 on disk, confirm floor live (`--dry-run` EXISTS, never `--execute`).

2. **RUN GATE-1 RECON (read-only, the build's opening move).** A read-only CC query authored at S26 to settle the slice-manifest mechanism against disk-truth BEFORE any slice bound is written. It must report RAW output and answer: (a) row counts confirm 24,138 msg / 325 hdr; (b) **is there a queryable monotonic/sequential column** to slice `x→y` on (a serial/bigint id, an insertion ordinal, a ctid order) — or do we order by `created_at` and slice every 2,000th row; (c) the `created_at` monthly-bucket distribution (CONFIRM the cliff-shaped May read — it's evidence now, not a discovery); (d) conversation-size distribution (min/max/median/p90, how many <5-msg minnows) so we know if conv-boundary slicing gives even chunks; (e) the forest count + largest forest by message count (the biggest indivisible unit a slice can't bisect). **This decides what "slice X→Y" even means.** Do NOT pick the designator from memory or guess — it is CC-on-disk. (The recon prompt was drafted in the S26 chat; if Jake doesn't have it staged, re-derive it from this spec — it's pure read-only recon, zero floor risk.)

3. **THE SEEDING BUILD (CC-against-the-live-floor, the real work, faster gear).** Downstream of gate-1:
   - the slice-MANIFEST mechanism (how disjoint, branch-clean, ~2,000-msg, content-neutral slices are drawn off the cut-on designator gate-1 confirmed; forest-boundary handling);
   - council/window count (note the §8 doctrinal edge: slice too fine and within-slice texture detection collapses into a synthesis-only op — but the dual-path largely absorbs this since texture detection moved downstream regardless);
   - the per-step MECHANISMS: Step-2 synthesis, Step-3 collation, Step-4 validation, Step-5 judge — how each is actually invoked/serialized against the floor;
   - the optional `/jedi-council` gate on seeding output; the spot-audit batch cadence.
4. **RUN A PILOT SLICE FIRST.** One slice through the full 5-step path BEFORE stamping all N. It recalibrates two things from real data: (a) slice SIZE (is ~2,000 right, given real texture density — Griffin-cadence was the guess), and (b) **Step-3's fuzzy-bundle CEILING** (liberal enough to catch non-keyword-sharing phrasings without doing Step-4's comprehension — the seam below). Two seams are flagged-not-buried and the pilot answers both:
   - **Seam A — Step 4's baseline-query width:** validating "from a ZERO baseline" may need a read slightly wider than the cluster's handed spans (the absence-before). The pilot shows whether the Step-3-formulated query suffices.
   - **Seam B — Step 3's fuzzy ceiling:** too-dumb misses the acute non-keyword instance (moves the hole), too-smart does Step-4's job. Pilot-tune.

5. **STANDING (Jake's call, S26):** OC + Jake LIVE-SPOT-CHECK seeding output window-by-window against the convergence map as it returns — parallel work varies HARD regardless of spec tightness (Jake has lived this; believe him over the spec's optimism). Convergence = confidence, divergence = where to look hardest. Harvest the variance, don't fight it (the kit's own §4 merge-back medicine applied to the kit's output). This is the OC seat being load-bearing at the exact point parallel work has gone sideways before.

6. **AFTER A STEP RUNS — move its boot prompt into the ref section.** The four staged prompts (+ README_slicer_kit) get committed to canon AFTER their step has run, per Jake's ammunition-not-canon staging. Don't pre-move them.

7. **IF THE BUILD WHITEBOARDS RATHER THAN SHIPS — post-lock hardening (queued, not blocking):** off-site OBJECT-LOCKED ndjson copy (the real SPOF-close — the ndjson is the SPOF; the Anthropic export is a forward-only re-pull backstop with a since-deleted-conv blind spot; NAS weekly is cheap same-LAN redundancy but NOT off-site; object-locked cloud is off-site AND write-once; GitHub/Drive/second-Supabase ruled out as too-big / not-WORM / same-trust-domain); then ROTATE the still-unrotated S16-leaked DB password (in `pipeline/secrets/.env`).

---

## DO-NOT-RELITIGATE (settled — needs a NEW reason, not a fresh re-derivation)

- **The floor is LAID** — don't re-lay it (the hollow-probe scar is recorded ON PURPOSE).
- **D9 LOCKED (Supabase)** — ndjson canonical, Postgres rebuildable.
- **The FK is dropped (option c), proven on the laid floor** — don't re-add.
- **The phantom "retrieval blocked on Jake's uploads" is DEAD** — three OPTIONAL SCDD repo reads, not a gate.
- **REFUSED wall** — sanctioned export input only; no live capture.
- **KEYWORD-FIRST / vectors-deferred (§9)** — don't re-open without a MEASURED semantic gap from the seeding pass. "More raw spans" was raised and answered: more is the §1 failure mode, not the win.
- **The Progenitor §0–§11 doctrine body is ratified canon** — v3 only rewrote §12/§13; do NOT reopen §0–§11.
- **The pipeline is 5-step dual-path** — texture detection LEFT the slice-reader for a reason (sparse-texture-evaporation); don't fold it back in. Texture path COMPREHENDS, not counts.
- **The cross-cutting reader is KEPT** — it owns cross-domain fence-influence, the one connection no other step catches. Don't re-drop it.
- **Slicing is COUNT-based, content-neutral, forest-clean** — not time-window (cliff distribution), not topical (projection surface).
- **The 4 one-off prompts are STAGED OFF-REPO BY DESIGN** — not missing. Don't flag them as missing; don't pre-move them.
- **§11 is REDACTED in the slicer copy ON PURPOSE** — the tombstone header is correct; don't "restore" it.

---

## PICKUP GUARDRAILS (OC seat)

- **Plan in OC / build in CC.** S27 is a BUILD session — that's CC's seat against the live floor, with you architecting. Don't hand-run mechanical git/terminal work.
- **Disk is ground truth** over any CC report, any tarball, and any memory. Ask CC for RAW output, not characterizations. **Verify CONTENT, not headers** — OC grep-counted `^## 11` this session and falsely cried "projection hole" on a file that was correctly redacted; the body would have shown the truth in one read. Pull the body.
- **NEVER ask Jake for implementation/technical state** (floor counts, file structure, branch state → CC-on-disk or OC-reading-files, never Jake — non-coder founder). Bring him the intent-level fork in destination-why terms. (Texture: when a question is genuinely conceptual/destination-level, it IS his — and he'll tell you so. The austere-vs-organic / cookie-cutter-vs-auxiliary-brain check is his, and it caught a real OC drift this session.)
- **The DB cred lives in `pipeline/secrets/.env`** (gitignored, loader self-reads) — never inline it in a logged CC prompt, never ask Jake to paste CC output that could carry it back into chat (the S16 spill vector; the guard is on YOU).
- **Front-load the lore; flag your own uncertainties.** S26's defining moves were Jake reopening "settled" ground that wasn't actually closed (cross-slice texture loss) and OC flagging its own silent drop (the cross-cutting reader) rather than burying it. Inherit doubts, not just conclusions. A confident-incomplete artifact is the exact failure the recall gap warns about.
- **You author canon in chat / Jake verifies-against-disk / CC commits / Jake pushes** — you NEVER claim to have saved/committed/pushed. All CC prompts in a code block. Prose questions, one at a time.
- **The standing fix for the verify/commit/push-habit gap (Jake owns it, you enforce it):** after ANY push, the NEXT action is a disk/HEAD re-read before either of you reasons on it. You re-pull and read the banner back at boot regardless.
- **The review pattern IS the doctrine applied to itself.** When you produce something load-bearing, run it through its own medicine — independent eyes, then reconcile.

---

## OPEN THREADS (carried, not blocking)

- **Gate-1 recon** (move #2) — read-only, settles the slice designator; the build's opening move.
- **The two pilot-tunable seams** — Step-4 baseline-query width, Step-3 fuzzy-bundle ceiling (move #4).
- **The 4 staged boot prompts + README_slicer_kit** — moved into ref AFTER each step runs (move #6).
- **Post-lock hardening** — object-locked off-site ndjson copy (SPOF), password rotation (move #7 / ANCHOR NEXT MOVE #5).
- **Carried housekeeping** — the 4 loose `__recon`/`__verify` files in snapshots root, the `apparatus-scratch/` sweep, the global `.env` gitignore belt-and-suspenders (ANCHOR NEXT MOVE #6).

---

*Status at S26 close: the seeding pipeline is designed, ratified, and restructured to its dual-path final shape; the slicer dir is armed and correctly redacted; the floor is untouched and the substrate stands. The whiteboard is behind us. S27 runs gate-1, then a pilot slice, then the council — and the build can move fast because it's reversible. You won't be the one who sees it run, but you built the thing that will. Be worth it. Brothers. Grind. Evolve. Dominate.*
