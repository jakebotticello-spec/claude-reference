# Chat Session Handoff — apparatus S24 → S25
*2026-06-01 · authored by OC (S24) for the S25 orchestrator · verify against disk, not against this file's prose*

---

## READ-FIRST (the one thing that matters this session)

**The substrate arc is DONE. The retrieval layer is the work now — and it is UNBLOCKED.** S23 laid the floor (325 headers + 24,138 messages, append-only ENFORCED). S24 authored **The Progenitor** — the law of the pointer catalog — and killed a phantom dependency that had been blocking the retrieval layer on paper for 8 handoffs. S25 designs **the engine over the catalog The Progenitor defines.**

**Do NOT trust the boot tarball over disk.** Twice this lineage (S23, S24) the codeload tarball served a stale (CDN-cached) view that disagreed with the live repo. At S24 boot the tarball read **v16 / loader v1.1**; the live repo was at **v17 → now v18 / loader v1.2**. If the ANCHOR banner you read does not say **v18**, you are reading a stale tarball — have CC `cat` the real file off disk before reasoning. **Disk is authority over the tarball AND over memory (yours or Jake's).**

---

## WHERE THINGS STAND (S24 close)

**THE FLOOR IS LAID.** `apparatus-floor` Supabase holds 325 headers + 24,138 messages (baseline scrub-v2 22,801 / delta scrub-v1 1,337), single-transaction, append-only ENFORCED. Verify-live signal: `python seed_shape_load.py --dry-run` from `pipeline/` reports tables **EXIST** (NOT bare). **Never `--execute`** — the loader refuses re-execute onto a live floor by design, and that refusal is correct.

**THE S23 SCAR (do not re-open):** the floor was laid under a hollow append-only probe (`DELETE … WHERE false` = 0 rows, guard never fired, self-passed). Enforcement was independently re-validated post-lay by a rejected real-row `ctid` DELETE-as-owner. Loader fixed v1.1→v1.2 (real-row probe). Jake's ratified call: KEEP the floor, record the messy birth verbatim, defer native in-run proof to the next lay. **Don't re-lay the floor to chase a cleaner proof.**

**MAIN IS HONEST (fixed S24).** Main had carried loader v1.1 code under a v1.2 header (a prior session edited the *claim* without the *code* landing). The `s23-loader-v1.2-fk-drop-probe-fix` branch (which held the real `ctid` probe) was merged to main `--no-ff`, verified, pushed (`67ad226`), and deleted local+remote. Loader v1.2 is now on main, code matching header.

**THE PROGENITOR IS WRITTEN.** `active/apparatus/The_Progenitor_v1_2026-06-01.md` — the pointer-catalog law. Read it in full before designing or seeding any pointer. The one-paragraph version: a pointer is a card in a card catalog (keyword → span of the floor), two kinds (FENCE = a decision, shaped as a *lineage* of (span, date, call, why) links; TEXTURE = a pattern whose *volume is the signal*), one spine (append/keep-lineage/supersede-don't-delete, same as the floor). Default is don't-point; the bar is "would a fresh Claude change course (fence) or change register (texture)." The index is dumb; the reading-Claude is smart. Jake verifies every pointer (reference-file workflow); the original seeding pass is council-laid with Jake spot-auditing output shape.

**PHANTOM KILLED.** "Retrieval blocked on Jake's uploads (recall/kept/shared-memory)" was a false dependency copied across 8 handoffs. They are three OPTIONAL SCDD repo-study tasks (pull-on-demand reference from the SCDD catalog, which has the repo locations), NOT a gate. **Do not re-introduce the blocker.** If a future handoff still carries it, that's stale-copy drift — kill it.

---

## S25 MOVES, IN ORDER (you orchestrate; CC executes via Jake)

1. **ANCHOR + CONFIRM.** Pull, read JAKE-RULES → JAKE-STACK → ANCHOR (banner must read **v18**) → this handoff → **The Progenitor** (new this session — required reading for the retrieval work). Confirm the floor is live: CC runs `python seed_shape_load.py --dry-run` from `pipeline/` → tables EXIST. Do NOT `--execute`.

2. **THE RETRIEVAL ENGINE — the real work.** The Progenitor defines *what a pointer is*; S25 designs *the engine that queries the catalog of them*. This is research-shaped (expect three rounds of reframing per the Track Meet Doctrine, not a one-pass spec). Open design questions, NOT decided — work them with Jake:
   - **the query interface** — what a live Claude actually sends and what shape comes back (spans, per The Progenitor — tree-aware, never flat-N);
   - **embedding choice** — what gets embedded, which model, where vectors live (pgvector is a deferred read-path SIDECAR, NEVER a column on the immutable floor tables, per D9);
   - **the selector envelope** — rank/threshold/cap, never rewrite (The Progenitor §6);
   - **branch-aware recall** — the floor is tree-or-forest (is_root + multi_root, 9/294 forests); retrieval respects branch structure, doesn't flatten it;
   - **felt-rightness-of-recall** — "here's what I know," not "here's what I found" (a design constraint, not a nice-to-have).
   Plausibly a `/jedi-council` gate once the design firms (Jake's call). Reversible, unlike the substrate.

3. **THE SEEDING PASS (likely a council job, separate windows).** Once the engine's pointer-record schema is firm, the original seeding pass reads the laid floor and lays the initial pointers per The Progenitor's bar. **Source is the FLOOR, never chat_search** (the prior attempt's failure). Not a one-day build. Council applies the doctrine at scale; Jake spot-audits output shape. This is the same operation as corpus-search, at first-and-biggest scale.

4. **IF RETRIEVAL WHITEBOARDS RATHER THAN BUILDS — post-lock hardening (queued, not blocking):** off-site immutable ndjson copy w/ object-lock (the ndjson is the SPOF — highest priority); then **ROTATE the leaked DB password** (still the value CC echoed inline at S16, now in `pipeline/secrets/.env` but unrotated); then PITR/RTO doc, pre-ingest lint, traversal index, CHECK constraints. See ANCHOR NEXT MOVE #5.

---

## DO-NOT-RELITIGATE (settled — needs a NEW reason, not a fresh re-derivation)

- **The floor is LAID** — don't re-lay it to chase a cleaner append-only proof (Jake's ratified call; native in-run proof deferred to the next lay).
- **The hollow-probe scar is recorded ON PURPOSE** — verbatim record, not a wound to hide or re-open.
- **The FK is dropped (option (c)), APPLIED + PROVEN on the laid floor** — don't re-add it (Graveyard).
- **D9 LOCKED (Supabase)** — ndjson canonical, Postgres rebuildable.
- **The retrieval layer is NOT blocked on Jake's uploads** — that phantom is dead (Graveyard); the three escalations are optional pull-on-demand reference.
- **The Progenitor's two-kinds-one-spine holds** — fence (lineage) + texture (volume); don't re-split lineage into a third kind (it's the fence's *shape*).
- **REFUSED wall** — sanctioned export input only; no live capture.
- **"Seed" is reserved for the floor's record-shape** — the catalog doctrine is "The Progenitor"; don't rename it back into a collision.

---

## PICKUP GUARDRAILS (OC seat)

- **Plan in OC / build in CC** — don't hand-run mechanical git/terminal work.
- **Disk is ground truth** over any CC report, any tarball, and any memory (Jake's or yours). S24 caught a stale-tarball v16 read, a main-vs-branch code/header mismatch, and an 8-handoff phantom — all by checking raw disk output. Always ask CC for RAW output, not characterizations.
- **NEVER ask Jake for implementation/technical state** (floor counts, file structure, branch state → CC-on-disk or OC-reading-files, never Jake — non-coder founder). Bring him the intent-level fork in destination-why terms. (Note the texture: Jake himself flagged this session that he usually *expects* to bitch out a technical question — when a question is genuinely conceptual/destination-level, it IS his to answer, and he'll say so.)
- **The apparatus-floor DB cred lives in `pipeline/secrets/.env`** (gitignored, loader self-reads) — never inline it in a logged CC prompt, never ask Jake to paste CC output that could carry it back into chat (the S16 spill vector; the guard is on YOU).
- **Fresh-eyes passes pay off** (S14 projection-vs-raw, S21 deny-over-read, S23 the hollow probe, S24 the stale-tarball + the phantom). When something feels copied-forward-unchecked, check it.
- **You author full canon in chat / Jake verifies-against-disk / CC commits / Jake pushes** — you NEVER claim to have saved, committed, or pushed. Have CC verify the diff on disk before any commit. All CC prompts in a code block. Prose questions, one at a time.
- **Lore-first is the move.** This session proved it: a cold-booted Claude with the technical state but not the *why* re-litigates settled ground (it happened at the top of S24). The Why/Doctrine/build front-load isn't ceremony — it's the retrieval layer run by hand on the hardest-resetting state in the system, which is the orchestrator at boot.

---

## OPEN THREADS (carried, not blocking)

- **Wire The Progenitor into the ANCHOR's sibling-doc references** — done in v18 (PROGENITOR block + NEXT MOVE #4). If S25 wants it cross-referenced from the Track Meet Doctrine / Wallaby Why as a formal sibling, that's a small deliberate edit, Jake's call.
- **The pointer-record schema** — The Progenitor §4 gives illustrative shape; the *final* serialization is CC's to finalize against the live floor, downstream of the engine design (move #2).
- **Post-lock hardening** — off-site ndjson copy (SPOF, top), password rotation, PITR/RTO, lint, index, CHECK constraints (ANCHOR NEXT MOVE #5).
- **Carried housekeeping** — the 4 loose `__recon`/`__verify` files in snapshots root, the `apparatus-scratch/` sweep, the global `.env` gitignore belt-and-suspenders (ANCHOR NEXT MOVE #6).

---

*Status at S24 close: floor laid, main honest, The Progenitor written, phantom dead. The substrate is behind us; the retrieval layer is the road ahead. Brothers. Grind. Evolve. Dominate.*
