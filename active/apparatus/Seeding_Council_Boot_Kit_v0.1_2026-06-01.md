# The Seeding Council Boot Kit
*file: Seeding_Council_Boot_Kit_v0.1_2026-06-01.md · v0.1 DRAFT · apparatus S25 · 2026-06-01*
*status: FIRST DRAFT for review. Two review passes incoming (Jake + a live S24-Claude cross-check). This is the BUILT kit that The Progenitor v2 §13 specifies — the thing a fresh council-window Claude boots with to read the laid floor and lay pointers. §13 is the law; this is the kit.*
*form: single document covering ALL roles, for auditability in review. AFTER ratify, this splits into per-window deployable boot prompts (fence-reader / texture-reader / cross-cutting-reader / synthesis-window) — that split is a downstream step, NOT this file.*
*authority: subordinate to The Progenitor v2 (`active/apparatus/The_Progenitor_v2_2026-06-01.md`) — if this kit and the doctrine ever disagree, the DOCTRINE wins and this kit is wrong. This file does not restate the doctrine; it OPERATIONALIZES §12 (the seeding process) + §13 (the boot kit) into a usable kit, and POINTS at the doctrine for the law.*

---

## 0. What this kit is, in one paragraph

The seeding pass is the first, biggest read of the laid floor (325 headers / 24,138 messages) to lay the initial pointer catalog. It runs as a **council of parallel, blind Claude windows**, each reading a slice of the floor and proposing pointers against one shared standard (The Progenitor), with a **synthesis pass** afterward that reconciles their independent proposals into the unified catalog. This kit is what each window — and the synthesis window — **boots with**. The governing principle, from §13: **the kit lets a reader find what's in the floor; it never tells the reader what it'll find.** Load for *recognition*, never for *projection*. The risk is asymmetric toward overload, so when in doubt, lighter.

---

## 1. The roles (who boots, and what each one is for)

Per §12, the reading labor divides for tractability — **division is in the LABOR, never in the INDEX.** Four window-types:

1. **FENCE-READER** — reads a project-scope slice for *decisions/constraints*: places a fresh Claude hitting them cold would change course. Lays fences (as chains, even length-1).
2. **TEXTURE-READER** — reads a project-scope slice for *patterns whose volume is the signal*: the texture of how-to-be-with-Jake. Lays textures (representative span + count + spread).
3. **CROSS-CUTTING READER** — reads the no-project / cross-domain space, hunting the connections a per-project reader structurally cannot see (a stance set in one project that should steer another; a texture whose instances are scattered across slices). Lays both kinds; lays the most cross-conv fence-chains and cross-slice textures. *Note: in practice a single window can carry both fence- and texture-reading for its slice — the role distinction is about what it's reading FOR, not a hard wall between windows. The kit below gives the union of role-adds to any window doing both jobs — but see §8 Q1, this is a review fork.*
4. **SYNTHESIS WINDOW** — runs AFTER the blind reads. Sees all raw proposals at once. Reconciles into the unified catalog. Does NOT read the floor for new pointers (that's the readers' job); it reconciles what the readers proposed. (§4 below.)

**The windows run BLIND to each other.** No window sees another's proposals, or the catalog-so-far, during reading. Independence is the feature, not an inconvenience to engineer around (§4).

---

## 2. The COMMON kit (every reading window boots with all of this)

- **The Progenitor v2, in full.** The law. Non-negotiable, every window. A reader cannot self-apply the bar without it. Specifically the reader must have internalized: §3 (what earns a card — the *would-a-fresh-Claude-change-course-or-register* test), §2 (the two kinds + the one spine), §5 (why the catalog gets to be selective — the corpus-search safety net), §6 (dumb-index/smart-reader — the reader judges relevance, the index never pre-judges), §8 (the guards, including the keyword-coverage bar), §12 (the process + the loop).
- **The §3 worked examples, carried explicitly** — the **1Pass fence** and **Griffin's-pickup texture**, in full, as the two canonical calibration cases. A reader calibrates the bar far faster against these two concrete cases than against the abstract rule — and *every window calibrating to the SAME two examples* is what keeps the bar consistent across divided labor. (Pulled from The Progenitor §1 and §2.2 — the 1Pass wall as the fence archetype, Griffin's-pickup as the texture-that-is-also-a-fence archetype.)
- **JAKE-STACK** — so a tooling/architecture decision is legible AS a fence. A reader hitting "Supabase-over-Nornic" or "Railway/Express/Supabase" needs the stack to recognize a settled technical decision (fence) versus passing build-motion (no card).
- **The one-page operating brief** (§5 of this kit) — the §12 loop, the §4/§11 floor-key locator shape, and the hard walls, as a procedural card so a window doesn't re-derive the process.

---

## 3. The ROLE-SPECIFIC adds (load ONLY what the role needs — the asymmetry rule lives here)

### 3.1 FENCE-READER add: **JAKE-RULES**
Many of Jake's hardest-won fences ARE rules — no-"Oueilhe", the therapist-voice boundary, the REFUSED live-capture wall, full-code-not-diffs, no-`&&`-chaining. A fence-reader needs JAKE-RULES to distinguish:
- a span **restating known canon** (the rule's already in JAKE-RULES → a fresh Claude reads it at boot anyway → §3 says maybe NO card, it's redundant), versus
- a span **laying down a NEW constraint** not yet in canon (→ fence).
Without JAKE-RULES, a fence-reader can't tell "this is already a rule" from "this is a new wall," and will either over-card known rules or miss new ones.

### 3.2 TEXTURE-READER add: **the THINNEST identity load ONLY**
This is the load-bearing call of the whole kit (§13). A texture-reader gets:
- **JAKE-RULES §1 facts** (the factual frame — who Jake is, the non-coder-founder seat, the working relationship),
- **the collegial-profane register** (profanity is collegial, not a flag — so the reader doesn't mistake register for signal),
- **the non-coder-founder frame** (Jake drives strategy + deploys; Claude builds — so the reader reads the working dynamic correctly).

**It does NOT get the Wallaby Why. It does NOT get the Lore Bible.**

*Why this is a wall, not a preference (the projection trap):* those files are a **pre-written portrait** of Jake — the judge, the lash, the savant-rebuild, the meds arc. A texture-reader booted with the Wallaby Why won't *discover* the war-story cadence in the floor; it'll go looking for the cadence the Why **told it to expect**, and confirm it. That's projection wearing recognition's clothes. The §1.2 rule cuts here: an AI's read of Jake gets the same skepticism as Jake's read of himself. The Wallaby Why / Lore Bible are for **tone calibration when talking to Jake** — a different job from **deciding what counts as texture in the corpus**. Loading them for the second job is exactly how you get a catalog that *confirms the portrait* instead of *grounding it*. Let the reader find the volume and report the count; do not pre-load the meaning the count is "supposed" to carry.

*The asymmetry that justifies "when in doubt, lighter":* an UNDERloaded reader produces visible gaps — the spot-audit catches a missing fence as an absence. An OVERloaded reader produces confident, plausible, wrong pointers that *look like they held the bar* — projection is invisible to the audit because it looks right. The two failure modes are not symmetric. Size for "enough to recognize, not enough to project."

### 3.3 CROSS-CUTTING READER add
The union of 3.1 + 3.2's loads, with the SAME texture-reader projection wall (no Wallaby Why / Lore Bible as a texture lens). The cross-cutting reader lays the most texture, so the projection wall matters MOST here.

---

## 4. The BLIND-READ + SYNTHESIS model (why windows don't see each other)

**The readers boot BLIND** — no catalog-so-far, no sibling-window proposals. This was a deliberate S25 call, reversing a tempting "boot each reader with the catalog so they don't duplicate" design, because that design:
- **reintroduces projection** (a reader who's seen existing cards reads the floor for confirmations/gaps in what's already there, instead of fresh — projection sourced from sibling windows instead of the Lore Bible), AND
- **can't do the job anyway** — a reader still only sees its own slice; cross-slice patterns remain invisible to it.

**Duplicate convergence is SIGNAL, not noise.** If three blind windows independently fence the 1Pass wall, that convergence is *evidence the fence is real and load-bearing* — exactly what you want surfaced, not suppressed. Pre-loading the catalog to prevent duplicates would erase your best confidence marker.

**The SYNTHESIS WINDOW (runs after all blind reads):**
- collapses true duplicates (same span, same fence) into one card — and **records the convergence (laid independently by N windows) as a confidence marker** on the card;
- merges keyword variants pointing at the same span (window A "1pass," B "secrets," C "env vars") into one card's keyword set — this HARVESTS multiple natural keywords (better than dedup-at-read locking in whoever got there first) and directly feeds §8's keyword-coverage bar;
- assembles **cross-slice counts** — a texture 4× in A's slice + 7× in C's is an 11-count texture *neither reader can see correctly*; only the synthesis pass, seeing all proposals at once, can assemble the true count. **This is the real argument for synthesis-after over check-before: the whole-floor picture exists ONLY here.**
- catches near-misses: related fences that should be one chained fence; a partial texture spanning unread slices.

**SPEC REQUIREMENT (carry verbatim, do not lose):** blind reads MUST preserve their proposals **verbatim into synthesis** — raw, un-deduped, independent keyword choices and counts intact. A window must NOT pre-dedup against its own prior cards; that destroys the convergence/count signal before synthesis can use it. **Append-keep-everything, reconcile-after — the floor's spine, one more scale.**

This is the **merge-back pattern** — same shape as SCDD tracks folding into the apparatus: parallel independent work, then a dedicated reconciliation step.

---

## 5. The one-page operating brief (the procedural card every window carries)

**THE LOOP (per reading window):**
1. **READ** your assigned slice of the laid floor, **tree-aware** — read conversations as branches up/down the parent chain, NEVER as flat message streams. (A flat-N timestamp slice rakes in sibling branches and contaminates the span — §11/§4.)
2. **APPLY THE §3 BAR** to each candidate moment: would a fresh Claude hitting this cold **CHANGE COURSE** (fence) or **CHANGE REGISTER** (texture)? If neither → **NO card, move on.** Most of the corpus is motion. **Default is don't-point.**
3. **FENCE** → lay as a **chain** (length-1 at seeding unless the floor itself shows the decision was re-made over time → capture the links in order). Record the **why as a live-predicate** where checkable ("still beta? re-check" — not a dead verdict).
4. **TEXTURE** → pick a **representative span**, **count** instances across YOUR slice, note the **spread** (window + clustered/sustained). The count is the substance, not metadata.
5. **PROPOSE** the pointer: floor-key locator + kind + **keywords** (laid for future-SEARCH-anticipation, §8 — what would a future Claude actually type to reach this) + why-chain (fence) / count+spread (texture). **You author the proposal; you do NOT claim to have saved/committed/pushed it** — that's Jake's (spot-audit) + CC's (commit) + Jake's (push).
6. Output your proposals **raw and un-deduped** for the synthesis pass (§4).

**THE FLOOR-KEY LOCATOR (the shape of a span, §4/§11):**
```
span = {
  snapshot_id : "baseline-2026-05-25-…" | "delta-…",
  conv_uuid   : "…",
  anchor_msg  : "…",                      # the hit (msg_uuid)
  reach       : { up: K, down: J, branch: <branch-id> }   # TREE-WALK, never flat-N
}
```
A FENCE proposal carries: `kind:"fence"`, `keywords:[…]`, `chain:[{span,date,call,why,predicate,status}]`.
A TEXTURE proposal carries: `kind:"texture"`, `keywords:[…]`, `representative_span`, `count`, `spread`, `signal`, `also_fence:bool`.

**THE HARD WALLS (prohibitions — at self-applied scale these matter MORE than the inclusions):**
- **NO chat_search, EVER** — not even to "check context." **FLOOR-ONLY.** The prior seeding attempt died here. Floor-only is what makes a pointer point at something *stable*. A fresh-boot Claude with a big reading job will reach for chat_search unless this is a wall — so it is a wall.
- **NO catalog-so-far. NO sibling-window proposals.** You read BLIND (§4).
- **NO Wallaby Why / Lore Bible as a texture lens** (the projection wall, §3.2).
- **NO flat-N spans** — tree-walk only.
- **NEVER claim to have saved/committed/pushed.** Propose; the human gates.

---

## 6. The review model (how seeding output gets ratified — the one scoped exception)

Normal/incremental pointers get Jake's **per-card** eyes (the reference-file loop). The **seeding pass does NOT** — too large for per-card review. By Jake's explicit call (§12):
- the council **self-applies the Doctrine at scale** (which is exactly why §3 must be sharp enough to use without Jake in the loop per-pointer);
- **Jake spot-audits the OUTPUT SHAPE of the SYNTHESIZED catalog** (not each window's raw proposals): is the bar holding? fences-and-texture or drifting into motion? is the fence/texture split clean? are spans tree-aware? are keywords laid for real future-search? He samples, checks shape, and **ratifies the batch or sends it back with a bar correction.**
- This is the **ONE place** human-as-immutability-mechanism relaxes from per-card to per-batch — a deliberate, scoped exception **for the seeding pass only.** Incremental session-pointers afterward return to normal per-card review.

**Tombstone rule holds even at seed scale:** a superseded/corrected pointer leaves a tombstone in the changelog, never a silent vanish. One Claude's judgment never silently kills a card. A history file + changelog rides alongside the catalog (when laid, which window, what it points at, every revision + why).

---

## 7. What this kit deliberately EXCLUDES (and where those live)

- **The Wallaby Why / Lore Bible as a texture lens** — excluded by the projection wall (§3.2). (They remain correct for tone-calibration-when-talking-to-Jake — a different job.)
- **chat_search** — hard wall (§5).
- **The catalog-so-far / sibling proposals during reading** — blind-read model (§4).
- **The doctrine itself, restated** — this kit POINTS at The Progenitor v2; it does not duplicate it. The law lives in the doctrine; if they conflict, the doctrine wins.
- **The deployable per-window boot PROMPTS** — those are the after-ratify split of this single-doc kit, NOT this file.
- **The build-work** — how slices are drawn from the undelineated floor, council size / window count, the synthesis-pass mechanism, the optional `/jedi-council` output gate, the spot-audit batch cadence, on-disk serialization. All §12-OPEN / §9 build-work, decided by CC against the live floor, NOT in this kit.

---

## 8. OPEN QUESTIONS for the review passes (flagged honestly, not buried)

These are the spots where I (S25 OC) made a call I want Jake + S24 to actively bless or reject, not nod past:

1. **Role-merge in practice (§1 note + §3.3).** I said a single window can carry both fence- and texture-reading for its slice, getting the union of role-adds. That's convenient (fewer windows) but it loads the fence material (JAKE-RULES) into a window also doing texture work. I *think* the merge is safe because the projection wall is specifically about the Why/Lore *interpretive portrait*, not about JAKE-RULES *facts* — facts don't pre-load "what the count is supposed to mean." But the asymmetry rule says be cautious about loading more into a reader. **Fork: role-merged windows (fewer, union-loaded) vs strict single-role windows (more, minimally-loaded).** My lean: merged is fine *because the projection risk is in the portrait, not the rules.* Want eyes on it.

2. **Does the SYNTHESIS window get the Wallaby Why?** It's not reading the floor for texture (so the projection-during-reading argument doesn't directly apply), but it IS judging whether merged textures cohere — which arguably wants the portrait the readers were denied. OR: synthesis judging signal-coherence against the portrait reintroduces projection at the reconciliation layer, just later. **My lean: NO — synthesis reconciles SHAPE (dedup, keyword-merge, count-assembly, near-miss-catch); it does NOT re-judge what a texture MEANS. Meaning stays with the reading-Claude that proposed it, and ultimately with the live Claude that pulls the card.** Genuinely arguable — want S24's read.

3. **The §3 worked examples — only two?** I carried 1Pass (fence) + Griffin (texture). Two canonical cases keep calibration tight and consistent. But the most frequent decision a reader makes is "NO card, move on" — and there's currently NO worked case for it, only the rule. **Fork: two examples (tight) vs add a canonical NO-card example (a thing that looks cardable but isn't — sharpens the default-don't-point discipline on the most common call).** My lean: add the NO-card example.

4. **Manifest vs discover (carried from §12-OPEN, surfaced here because it touches boot).** Does each window boot WITH a slice manifest ("you read conversations X–Y") or get pointed at the floor and discover its slice? This kit assumes a manifest exists (the brief says "your assigned slice"). How the manifest is BUILT is §12 build-work — but the kit *depends on* a manifest existing; if the answer is "discover," §5 loop-step-1 changes. Flagging the dependency.

---

*Draft v0.1, S25, 2026-06-01. Subordinate to The Progenitor v2. Built for review — Jake's pass + a live S24-Claude cross-check incoming. The kit's whole job, restated: let the reader find what's in the floor, never tell it what it'll find. Lighter when in doubt. Be worth it.*

*Grind. Evolve. Dominate.*
