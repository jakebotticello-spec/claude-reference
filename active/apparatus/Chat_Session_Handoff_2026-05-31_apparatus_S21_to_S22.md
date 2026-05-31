# Chat Session Handoff — apparatus S21 → S22
*authored by OC at S21 close, 2026-05-31 · read after ANCHOR + JAKE-RULES + JAKE-STACK · tactical state, not authority (ANCHOR is authority)*

---

## ONE-LINE STATE

The deferred pipeline relocation is **DONE ON DISK and VERIFIED, but UNCOMMITTED and PARKED** on branch `review/pipeline-relocation-s21`. The commit is blocked on a **CC `git add` permission-deny** — a Claude Code *settings* interception, **NOT** a CC capability wall (CC has committed 20+ sessions) and **NOT** a git error. Nothing committed, nothing lost. **S22's first job is to clear the blocker, finish the commit, then apply the deferred canon.** The floor is untouched (2 snapshots / 24,463 records, baseline scrub-v1 + scrub-v2). Pass two (b) from S20 stands closed.

---

## WHAT S21 DID

1. **Booted cold, verified v14 against live disk.** ANCHOR banner read **v14** (freshness PASS). Pipeline confirmed at `active/apparatus/apparatus_freeze_pipeline.py` (v1.6); drill at `active/apparatus_overlay_v2_drill.py` (v0.2). Floor confirmed in `apparatus-archive\snapshots\` (outside the git tree). State matched the S20→S21 handoff.

2. **Turn-one context-layer flag, then corrected against the disk.** OC initially flagged the Wallaby Why's brain-model as a possibly-unverified self-model; JAKE-RULES §1.2 corrected it (medication-driven ADHD rewire, ~April 2026, 6–12mo window, prescriber attached — a documented clinical reality, not a folk model). The operative residue is the §1.2 distortion-check (don't let a 6–12mo *range* get used as a self-lash via a fixed "2–4 more months" deadline), not any diagnosis/therapy work. Jake confirmed it's a shared-direction context layer, not project work — logged, held, not to be re-opened as a topic.

3. **Scoped the relocation's real blast radius on disk BEFORE building.** `grep` for every reference to the pipeline path: the only **live executable coupling** is the drill's `sys.path.insert` + `from apparatus_freeze_pipeline import …` (lines 28–29). Every other reference is **immutable history** (7 handoffs + ANCHOR history notes) that must NOT be rewritten (Track Meet Doctrine — the log of where it used to live stays honest). `__pycache__` + `*.pyc` are ALREADY in `.gitignore` (repo-root `# Python` block), so the handoff's "code + pycache keep landing in canon" rationale is half-solved already — the relocation is tidiness+correctness (code out of a refs-only dir), not a git-hygiene fix. Conclusion: blast radius is far smaller than the S20 handoff's "touches everything" framing.

4. **Two intent calls, both Jake's:** (a) destination dir = **`pipeline/`** (Jake's call — names what this tree *is*, leaves room for `/load`, `/retrieval` siblings; better than OC's generic `code/`); (b) **no `/jedi-council`** (OC lean + Jake agreed — blast radius is below rung-7 once counted; council saved for seed-shape LOAD, which earns it). A third design call surfaced and Jake ruled it: **extract the pipeline path OUT of the hand-pasted ignition key and INTO committed canon** (ANCHOR), via a dedicated **WHERE-THE-CODE-LIVES** pointer block (option A — a stable block the churning banner doesn't touch), so a future move = one ANCHOR edit, not a fragile paste-buffer edit.

5. **Built + verified the move on disk through four CC stop-gates:**
   - **Gate 1 (ground truth):** both files confirmed; drill lines 11–30 read verbatim; **exactly one** import of the pipeline anywhere (`grep` confirmed); floor reachable read-only. Matched OC's tarball read line-for-line.
   - **Gate 5 (the move):** `git mv` both files into `pipeline/` (renames auto-staged by `git mv`); drill path block edited v0.2→v0.3 — `_APPARATUS` collapses from `_HERE / 'apparatus'` to `_HERE` (co-located); `_REPO`/`SNAPSHOTS`/`SRC`/`DST_DIR` unchanged in logic.
   - **Gate 7 (byte-verify):** `git show HEAD:active/apparatus_overlay_v2_drill.py | diff` against the new file proved **exactly 5 lines changed** — header (v0.2/S20→v0.3/S21), new v0.3 changelog line, the `_HERE`/`_APPARATUS`/`_REPO` lines (3 comments + the one `_APPARATUS` functional change). Nothing else. (Note: `git mv`+edit renders as a full `+`/new-file block in plain `git diff`, which is why the `git show | diff` old-vs-new compare was the right tool — a visual diff can't isolate the change.)
   - **Gate 8 (live proof):** `python -B` — `from apparatus_freeze_pipeline import PATTERNS` resolves from `pipeline/` (len=5); `_REPO` lands on repo root identically to before; `SNAPSHOTS` + `SRC` resolve to the real floor `exists=True`; **zero floor writes.** The relocation WORKS.

6. **Then the commit hit the wall (see THE BLOCKER below) and S21 wrapped without committing.**

---

## THE BLOCKER — CC `git add` permission-deny (S22 first move)

Every CC `git add` attempt — PowerShell and Bash, `-A` and explicit-path, multiple phrasings — returned verbatim:

```
Permission to use PowerShell with command Set-Location "c:\claude-reference"; git add … has been denied.
```

**What this is:** a **Claude Code permission-system interception**. The harness blocks the tool call *before* any shell runs — no git process is spawned, no exit code is produced. CC's own diagnosis (correct): this is a settings rule, not a git failure.

**What this is NOT:** it is **NOT** a git error, and it is **NOT** a CC commit-capability wall. CC has committed from its own session for 20+ sessions. A standing "CC can't commit" claim contradicts that entire history.

**The handoff that misled us:** the S20→S21 handoff said *"CC can't stage/commit in its session (permission wall) — it hands the command sequence to Jake."* That was an **over-read of a one-time S20 event** inflated into a standing fact. This session, OC initially treated the deny as confirmation of that "fact" and routed around it (had Jake hand-run git in a pager) — a workflow drift Jake correctly stopped ("CC shouldn't have a wall, we've done this 20 sessions"). Going to the literal error debunked the "wall." **Lesson now in JAKE-RULES §12: never inflate a one-time tool failure into a standing capability fact in a handoff; read the literal error.**

**S22 FIX, in order:**
1. **Find the deny rule.** Check `.claude/settings.json` and `.claude/settings.local.json` (project + user scope) for a permission rule matching `git add` (or a broad PowerShell-command deny that catches it). Allow it. Something changed this session vs the prior 20 — find what.
2. **Check for a stale `.git/index.lock`** (see UNRESOLVED below) BEFORE any index op.
3. **Re-verify the staged index** with a readable `git diff --cached` (confirm exactly the 2 renames + the 1 drill edit, nothing stray — no `__pycache__`, no scratch file).
4. **CC commits** on `review/pipeline-relocation-s21` (PowerShell-safe: single line, multiple `-m` flags, no heredoc, no `&&`). **Jake pushes.** (New standing flow this session: CC commits, Jake pushes — once the deny is cleared.) Proposed commit message is in the ANCHOR IN-FLIGHT block / the S21 CHANGELOG entry.
5. **Draft PR → `code-review:code-review` on the PR** (namespaced, NOT `Skill(...)`; PR-centric per §12) → assess findings → **merge `--no-ff`** to main → delete scratch branch.
6. **THEN apply the deferred canon** (see DEFERRED below).

---

## UNRESOLVED — possible stale `.git/index.lock` (CC mis-report #3)

During diagnostics, CC's **raw glob output** reported `.git/index.lock` — `Found 1 file`. CC's **summary to OC** then said *".git/index.lock: not found (Glob returned nothing)."* **These contradict.** The raw output is the ground truth; the summary is the mis-report. **S22: verify on disk** — `Test-Path .git\index.lock` in PowerShell. If a lock file is present and no git process is running, it's stale (a leftover from an interrupted op) and must be removed before any index write, or the next commit can fail or corrupt the index.

This is **CC mis-report #3** in the lineage (S20 had two: a tool-state "/code-review not installed" — it was — and a floor-write "scrub-v2 missing" scare — wrong-root look, floor intact). All three were caught by checking disk / reading raw output against the summary. **Keep reading CC's raw tool output, not its characterizations.**

---

## THE FLOOR RIGHT NOW (unchanged from S20)

| snapshot | type | records | raw_wiped | overlays | seen-set resolves to |
|----------|------|---------|-----------|----------|----------------------|
| `baseline-2026-05-25-ae015455` | baseline | 23,095 (294 hdr + 22,801 msg) | true | scrub-v1 + scrub-v2 | scrub-v2 (max-N) |
| `delta-2026-05-28-a61498e6` | delta | 1,368 (31 hdr + 1,337 msg) | true | scrub-v1 only | scrub-v1 |

Ledger: 2 entries. Floor total: 24,463 records. Floor lives in `apparatus-archive\snapshots\…`, **OUTSIDE the git tree.** scrub-v1 baseline SHA-256 `4ef22940…`; scrub-v2 baseline SHA-256 `b54620af…`. **S21 made ZERO floor writes** — the relocation never touched the floor (dry-run was read-only).

**Code, current COMMITTED state (HEAD, until the S21 branch merges):**
- Pipeline: `active/apparatus/apparatus_freeze_pipeline.py` **v1.6**
- Drill: `active/apparatus_overlay_v2_drill.py` **v0.2**

**Code, on the parked branch `review/pipeline-relocation-s21` (uncommitted/staged):**
- Pipeline: `pipeline/apparatus_freeze_pipeline.py` v1.6 (moved, content unchanged)
- Drill: `pipeline/apparatus_overlay_v2_drill.py` **v0.3** (moved + path block edited)

---

## DEFERRED CANON (authored S21, apply ONLY post-merge)

Do NOT write any of these into live canon until the relocation is committed — canon must not lead the floor (the founding discipline). When the merge lands:

1. **ANCHOR — add the WHERE-THE-CODE-LIVES pointer block** near the top of CURRENT STATE:
   ```
   ## WHERE THE CODE LIVES
   - freeze pipeline → pipeline/apparatus_freeze_pipeline.py
   - overlay drill   → pipeline/apparatus_overlay_v2_drill.py
   - the floor       → apparatus-archive/snapshots/ (OUTSIDE the git tree)
   ```
   (Stable block; the churning banner must not reword it. This is the single source of truth for code location.)
2. **ANCHOR — flip the two live pointers** in CURRENT STATE / NEXT MOVE from `active/apparatus/apparatus_freeze_pipeline.py` to `pipeline/…`. Leave ALL history notes + footers as written (they were true when written).
3. **Ignition key — thin it.** Remove the inline pipeline path ("pull `apparatus/apparatus_freeze_pipeline.py`"); replace with a pointer to ANCHOR's WHERE-THE-CODE-LIVES block. The path then lives in committed canon, never the paste buffer.
4. **Remove the IN-FLIGHT block + the S21 read-first block** from ANCHOR (their job is done once the move lands) and fold a one-line "S21 relocated the pipeline to `pipeline/`" into the history record.

---

## S22 LIVE TARGET (after the relocation lands) — seed-shape LOAD

Per the S20 handoff + ANCHOR DESTINATION: the real production ingest of the floor into the locked Supabase `apparatus-floor` project, then the retrieval layer. LOAD must ingest the **max-N overlay per snapshot** (baseline scrub-v2, delta scrub-v1) — the first time LOAD chooses an overlay. Carry the D9 post-lock recs: single-transaction/staging-swap ingest; pre-ingest lint; the `display_content` selective-strip is a LOAD-time toggle (84.4% strip-safe / 15.6% CARRIES_UNIQUE — and the scrubber DOES reach `display_content` though the v1.1 drift-detector doesn't walk it; two passes, two depths, both correct). This is plausibly a real `/jedi-council` gate (Jake's call).

---

## PROCESS REMINDERS FOR S22

- **Disk is ground truth over any CC report.** Three CC mis-reports in two sessions, all caught by checking disk / reading raw output. Keep doing it. The day a turn asks you to STOP verifying is the day to plant your feet.
- **New standing flow (once the deny is fixed): CC commits, Jake pushes.** Supersedes the (false) "CC hands commits to Jake" line. But **verify the diff on disk before the commit goes in** regardless of who commits (gate-7 discipline — the author changing doesn't remove the "what rode along" risk).
- **OC authors FULL canon in chat; never commits it.** Re-pull fresh HEAD, edit surgically on the real file, hand complete files via `present_files`. Jake verifies-against-disk, saves, commits, pushes.
- **All CC prompts in a code block.** Commits PowerShell-safe (single line, multiple `-m`, no heredoc, no `&&`).
- **Run the pipeline with `python -B`** until the relocation lands and ends the pycache-in-canon issue for good.
- **Don't write canon ahead of the floor.** The deferred-canon list above stays deferred until the move is committed.
- **Jake co-pilots intent, OC pilots engineering.** Don't drift into having Jake hand-run mechanical git/diff work — that's CC's lane (the S21 pager drift). Fix CC's tooling, restore the lane.
- **⚑ Carried-open items (still not done):** the 4 loose `__recon`/`__verify` files in `apparatus-archive/snapshots/` root (open since S17 — investigate provenance, never blind-delete from the floor dir); the `apparatus-scratch/` sweep; the DB password rotation (post-D9 item #7); and the oddly-named root file `Cclaude-reference…state_calc.txt` (a path-flattened D9 doc — candidate for the same cleanup bucket, not urgent).

---

## DON'T-RELITIGATE (carried + S21)

- D9 LOCKED (Supabase); floor append-only ENFORCED; ndjson canonical / Postgres rebuildable.
- raw.json Path A (wipe after verify-PASS) — applied both snapshots. Overlays re-scrub SCRUBBED output, never raw.
- Delta = uuid-set-difference; the overlay contract's 3 invariants are RATIFIED LAW (tighten-only / full-restated-standalone / accrete-forever).
- `_build_seen_set` returns the UNION of all prior snapshots (24,138 / 325), NOT the delta slice (1,337/31).
- Pass two (b) is CLOSED (S20). The scrub-v2 overlay is the SYNTHETIC ratify-drill, not a production re-scrub. Don't re-open.
- **NEW (S21) — "CC can't commit" is FALSE.** It's a settings deny (fixable), not a capability wall. The S20→S21 handoff's claim is corrected here and in JAKE-RULES §12.
- **NEW (S21) — the relocation is DONE ON DISK and CORRECT** (5-line byte-verified edit, live import + floor-resolve proven). The only thing missing is the commit. Don't re-verify the *work* from scratch at S22 — verify the *index/lock state* and commit.
- **NEW (S21) — no floor mutation occurred.** The relocation dry-run was read-only; the floor is byte-identical to S20 close.

---

## JUDGMENT-CALL LEDGER (S21 non-obvious calls, per §17.5c)

- **Destination `pipeline/` over generic `code/`** — call: Jake's, OC concurred. Reasoning: names the specific tree, leaves room for `/load` + `/retrieval` siblings. Confidence: high. Source: Jake's stated intent.
- **No `/jedi-council` on the relocation** — call: OC lean, Jake agreed. Reasoning: blast radius is one live import + a file move once counted on disk; below rung-7; council (~75k tokens, gate-only) is saved for seed-shape LOAD. Confidence: high. Source: the on-disk grep of the real reference spread.
- **Extract the path from the ignition key into ANCHOR (WHERE-CODE-LIVES block)** — call: Jake's design instinct, OC refined to option A (dedicated stable block, not banner prose). Reasoning: the path living in the hand-pasted ignition key is the fragility (forget to edit it → next boot points at a dead path); committed canon is the durable home. Confidence: high. Source: the §17.5 ignition-key spec + the relocation's own "S22 boots blind" risk.
- **STOPPED rather than commit through the degraded workflow** — call: Jake initiated ("we have to stop"), OC concurred firmly. Reasoning: the commit was blocked by an undiagnosed settings deny AND sat over an unresolved `.git/index.lock` contradiction AND the index state was being inferred not shown; sealing over unexplained state violates the apparatus's first rule. Confidence: high. Source: the watch principle + the two open anomalies.
- **Authored deferred canon as DEFERRED, not applied** — call: OC, firm, even under Jake's "whatever you want." Reasoning: the `pipeline/` pointer is only true post-commit; writing it into live canon now would make canon lead the floor — the exact failure the founding discipline forbids. Confidence: high. Source: the never-write-canon-ahead-of-the-floor invariant.

---

*Last updated: 2026-05-31, apparatus S21 close. ANCHOR is authority; this is tactical. The relocation is good work, parked one settings-fix away from sealed. Grind. Evolve. Dominate.*
