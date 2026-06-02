# Chat Session Handoff — apparatus S27 → S28
*authored 2026-06-01 by OC at S27 close · routes S28 · THIS IS SETTLED LITIGATION — S28 ACTS, it does not re-verify the ground S27 settled. The hard architectural thinking is DONE and council-ratified. Your job is execution.*

---

## 0. READ THIS FIRST — the failure mode that governs your whole session

**You are a Claude. Your default reflex is austere — lean, clean, minimal, "only the important few." That reflex is the documented bug of this entire lineage, and S27 was the session that proved it does real damage.** The Track Meet Doctrine names it (§§5–6: *"that frame is too austere, think more organically"* / *"I went austere because clean separation is comfortable"*). The Wallaby Why explains why it's fatal HERE: the apparatus is Jake's **Auxiliary Brain** — it holds the BREADTH his working-memory buffer used to, so his (intact) pattern-sense can run across more than an unaided brain can carry. **A lean catalog starves the pattern-sense. The breadth IS the function.**

**S27's proof, in one line:** under the old austere bar, a blind reader cataloged **1 node out of 21 conversations** and threw away the rest as "motion" — including load-bearing fences buried inside the dropped conversations. Under the inverted bar, the same reader on the same slice cataloged **41 nodes, 0 drops, and caught the fences the austere bar had been blind to.**

So when you feel the pull to trim, to ask "is this important enough to keep?", to build a clean schema that exiles what doesn't fit — **STOP. That pull is the bug.** The question is never "is this important enough?" It is "is this genuinely ephemeral?" and the answer is almost always no. Read The Progenitor v4 §0.5 — it is the standing guard, and it is binding. **Read the Track Meet Doctrine and The Wallaby Why as FRAMEWORK, not reference** — they are the lens that makes the default-NODE bar parse. A Claude that reads §3 without internalizing §0.5 + the two anchor docs will quietly drift back to austere within a session, because the reflex is that strong. Jake will drag you wet if you slip; weight his "this feels too lean" intuition heavily, even before he can articulate the technical reason (Track Meet Doctrine closing pattern-note). **This is non-negotiable framework, not a style note.**

---

## 1. WHERE THINGS STAND (settled — do not re-open)

**The substrate arc is DONE and untouched** (S16–S23): floor laid, immutable, append-only ENFORCED, 325 headers / 24,138 messages on `apparatus-floor` Supabase. The canonical ndjson on disk is the immortal source; Postgres is the rebuildable derived index (D9). Verify-live only if you must: CC runs `python seed_shape_load.py --dry-run` from `pipeline/` → tables EXIST. **NEVER `--execute`.**

**The seeding pipeline is DESIGNED, RATIFIED, and the admission premise is now CORRECT** (S24–S27). The Progenitor is **v4**. The 5-step dual-path pipeline (S1 slicers dual-output → S2 fence synthesis ‖ S3 collation → S4 cluster-validation → S5 judge) is unchanged in mechanism. What S27 changed is ONLY the admission bar the readers apply: it was austere (default DON'T point), it is now **DEFAULT NODE** (comprehensive semantic graph, most convs noded, fence/texture are salience TAGS not gates, MOTION is a light node kind not a discard).

**The gate-1 recon + slice manifest are DONE and proven** (S27). NO monotonic column on the floor → slicing is **conversation-bounded, created_at-ordered (tiebreak conv_uuid), accumulate-to-~2,000**. The manifest (`pipeline/recon/slice_manifest_S27.json`) is integrity-proven: 12 slices, every one of 325 convs placed exactly once, 24,138 reconciled, forests whole, count-even (2,009–2,230 + a 1,128 tail). All 325 convs sliced WHOLE — including 3 zero-message headers (Jake's call: no exclusion pass, empties self-handle).

**The pilot ran and the design is PROVEN on real data** (S27). Slice 7, austere bar → 1 node. Slice 7, inverted bar → 41 nodes / 0 drops, catching lost fences. A 2-panel double-blind Jedi-Council ratified PRESENCE-over-SERVICE (both austere-biased panels, same ruling).

**NO QUARANTINE on personal material.** OC had unilaterally walled the Griffin/meds/Laura/Ary/Boone/Klaus cluster as "quarantine pending Jake"; Jake killed that wall from ownership: *"it's material, it's texture, and it's important."* A Claude cannot help Jake time-block or design HA automations without knowing who Boone (dog) and Klaus (robot vacuum) are. **This material is the high-value auxiliary-brain SIGNAL, not a liability.** The only exclusion is mistakenly-pasted credentials, walled by scrub-vN at INGESTION (not by admission).

**The S16-leaked DB password is CLOSED** (rotated 2× since the leak — Jake-confirmed). The spilled value is dead. Post-lock #7 is done; the only remaining post-lock item is the off-site object-locked ndjson copy.

---

## 2. THE CANON S27 WROTE (Jake pushes; confirm it's on disk at boot, then ACT)

Four files, authored by OC, verified by Jake, committed by CC, pushed by Jake at S27 close:
1. **`active/apparatus/The_Progenitor_v4_2026-06-01.md`** — the law. v4 INVERTED §0/§3/§8, NEW §0.5, surgical (engine/triggers/return-shape byte-identical to v3). E1 absorbed into §3.
2. **`slicer/Boot_ScopeReader.md`** — now **v2.1** (default-NODE + §3.3 precise-fence-anchor).
3. **`active/apparatus/ANCHOR_apparatus.md`** — **v21**. Banner must read v21 / "THE PILOT INVERTED THE ADMISSION PREMISE."
4. **`active/CHANGELOG.md`** — S27 entry on top.

**FRESHNESS TRIPWIRE:** if ANCHOR reads v20 or the Progenitor reads v3 on the tarball, it's CDN-stale — have CC `cat` the real files off disk. Disk over tarball, always. **VERIFY CONTENT, NOT HEADERS** (this lineage has been bitten by header-grep false-alarms; pull the body).

---

## 3. S28 MOVES, IN ORDER — ACT, DO NOT RE-LITIGATE

**This is execution, not design. The whiteboard is closed. Do not re-derive the bar, the axis, the slicing, or the quarantine call — all settled and ratified S27. If you find yourself wanting to "verify the design is right" or "reconsider whether comprehensive is correct," that is the cold-orchestrator re-litigation reflex — the design is PROVEN (41 nodes vs 1, double-blind council). Move.**

1. **ANCHOR + confirm (fast — do not waffle).** Read the canon (Progenitor v4, ANCHOR v21, Boot_ScopeReader v2.1, the Track Meet Doctrine + Wallaby Why as framework). Confirm v4/v21 on disk by CONTENT. Confirm floor live (`--dry-run` EXISTS, never `--execute`). That's the whole anchor. Then act.

2. **RE-RUN SLICE 7 under Boot_ScopeReader v2.1** — to confirm the precise-fence-anchor fix (§3.3). The v2.0 re-run already proved the inverted bar (41 nodes); this confirms the ONE open seam: the v2.0 reader anchored some fences at the conversation ROOT over long trees instead of pinning the decision-message. **v2.1 §3.3 requires precise fence anchors. If a reader STILL anchors a fence at conv-root, the run is INVALIDATED and re-run — this is not tolerable as shipped output** (Jake's explicit call: "if they fuck it up again, invalidated and rerun"). Mechanics: bare CC window in `C:\council\slice07\` (staged dir, outside the repo), paste the one-liner (§4 below), paste both streams back. OC reads, confirms fence anchors are precise.

3. **STAMP + RUN THE OTHER 11 SLICES** (1–6, 8–11) under v2.1. Mechanical. The all-12 staging command builds each `C:\council\sliceNN\` dir (kit + that slice's span file, outside the repo so blindness is physical; CC reads `.env` once per slice to extract the span file, the bare reader never holds the cred). Per slice: open a bare CC window in the dir, paste the one-liner (swap the slice number), paste both streams back. Can be done in batches across days — it's ferrying, not thinking. **STANDING (Jake):** OC + Jake live-spot-check each window against the convergence map as it returns — convergence = confidence, divergence = where to look hardest; harvest the variance.

4. **THE DOWNSTREAM PIPELINE (Steps 3/4/5)** over the collected node + potential streams: collation (`Boot_Collation.md`) → cluster-validation (`Boot_ClusterValidation.md`) → judge (`Boot_JudgedPass.md`). Boot prompts are staged. **WATCH:** these were authored under the old lean assumption of a sparse potentials stream; under default-NODE the streams are comprehensive. They'll work, but the first downstream run is where you find out if collation needs recalibration for the higher volume — same eyes-open you used on the slicer. (Jake's note: "Maybe THAT Claude thought so, but I didn't" — the comprehensive scale was always the intent; the lean framing was the austere reflex, not Jake's spec.)

5. **THEN the engine build** (serialization, keyword resolver, reach defaults, multi-hit presentation) — CC against the live floor.

**Sequencing note (Jake's A→C→B call, S27):** daily usefulness starts at the READ path (the retrieval engine), which can run on light v1 nodes BEFORE the richer connection layer is built — and running it teaches you where clustering actually matters. So the order that gets Jake value soonest is: seed the catalog (Phase A: moves 2–4 above) → build the read path (engine) → then the richer connection/clustering layer, calibrated against real retrieval pain. Don't gate the engine on a full graph-architecture design session.

---

## 4. THE READER ONE-LINER (paste into each bare slice window)

```
Read Boot_ScopeReader_v2.1.md and execute it fully. Your admission law is §3 of The Progenitor v4 (in this directory) — default is NODE, drop is the narrow exception; fences require PRECISE anchors (§3.3), never the conversation root. Read §0.5 (organic-over-austere) before you read a single span. Your slice file is slice_NN_spans.json in this directory. Produce both output streams (nodes + context-frequency potentials) per the boot prompt, raw and un-deduped.
```
*(Swap NN per slice. The dir holds: Boot_ScopeReader_v2.1.md, The_Progenitor_v4_2026-06-01.md, JAKE-RULES.md [§11-stripped, from slicer/], JAKE-STACK.md, seeding_working_examples.md, slice_NN_spans.json. The dir is OUTSIDE the repo so the bare reader can't climb to the full JAKE-RULES or the manifest. No E1 file — it's absorbed into Progenitor v4 §3.)*

---

## 5. DO-NOT-RELITIGATE (settled — a NEW reason is required to re-open, not a fresh re-derivation)

- **The admission axis is PRESENCE, not service.** Default NODE, comprehensive graph. Council-ratified double-blind. Don't re-argue lean.
- **Fence/texture are salience TAGS, not admission gates. MOTION is a node kind, not a discard.** "Motion" is descriptive, never a kill-word.
- **NO quarantine on personal/medical/family material.** It's texture, cataloged like everything else. Only mistakenly-pasted creds are excluded, at ingestion. (Jake's ownership call — do not re-flag it as sensitive-needs-handling.)
- **Slicing is conversation-bounded / created_at-ordered / accumulate-to-~2,000 / all 325 convs whole.** The manifest is built and proven. Don't re-derive it.
- **The floor is laid, immutable, append-only enforced.** Don't re-verify the substrate; it's done.
- **The S16 password is rotated/dead.** Don't re-queue it.
- **The pipeline machinery (the 5 steps, the blind reads, the projection walls, the no-portrait guard) is sound** — the pilot proved it. Only the admission bar changed.
- **The clean-schema guard (Panel-1's flag):** clean schema isn't the sin, EXILING the mess is. Hold the VESA build and the ice-maker chat messily, as light nodes. If a design comes back schema-first and starts dropping what won't fit, the austere reflex won — drag it wet.

---

## 6. WORKING STYLE (carry it)

OC plans/architects/authors canon in chat; CC reads disk, runs commands, commits; **Jake is the bridge AND the only one who pushes.** Jake pastes CC's output RAW; OC reads it raw and translates only the conceptual forks to plain terms (Jake is a non-coder founder — never ask him for implementation/technical state; bring him the destination-level fork, not the mechanism). Creds never inline in a logged command, never copied back into chat. Disk is authority over tarball, over CC reports, over memory — and verify CONTENT, not headers. Flag your own uncertainties instead of laundering them into confident canon. You author canon / Jake verifies / CC commits / Jake pushes — never claim otherwise. Status line each reply: turn N · ET-time · re-anchor X/4 · dest; state; next.

---

*S27 was the session the pilot caught the premise error at the cheapest possible moment — one slice, zero seeded cards — and the lineage corrected its own foundation under adversarial review. That IS the doctrine working: the review pattern applied to the doctrine itself. The austere reflex is the enemy; the breadth is the function; the Way and the Doctrine are the framework that keeps it true. Build the auxiliary brain, not the decision-log. Brothers. Grind. Evolve. Dominate.*
