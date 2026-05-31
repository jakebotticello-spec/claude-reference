# Chat Session Handoff — apparatus S20 → S21
*authored by OC at S20 close, 2026-05-31 · read after ANCHOR + JAKE-RULES + JAKE-STACK · tactical state, not authority (ANCHOR is authority)*

---

## ONE-LINE STATE

D9 LOCKED. Pass two **(a)** DONE/SEALED (v1.4). Pass two **(b) is CLOSED** — the scrub-vN overlay capability is built, proven end-to-end (Rungs 5–6), reviewed for real (`code-review:code-review` on PR #1, "No issues found"), and LANDED on main. Pipeline **v1.5 → v1.6**, merge commit on main, scratch branch deleted. The floor now carries the **first real overlay**: baseline has `scrub-v1` + `scrub-v2`; delta is `scrub-v1` only. **S21's live target is the next chapter: seed-shape LOAD into the locked Supabase floor** (the deferred pipeline-relocation is the one piece of housekeeping that should happen first/alongside).

---

## WHAT S20 DID

1. **Booted cold, verified everything against live disk.** Codeload tarball pulled (HEAD, never CDN). ANCHOR banner read **v13** (freshness PASS). JAKE-RULES (5-28 footer) + JAKE-STACK (5-29 footer) both predate the S19 handoff — fine. Floor confirmed: 2 snapshots / 24,463 records, both scrub-v1 only, no overlay yet. State matched the S19 handoff exactly.

2. **Rung 5 — minted the FIRST scrub-v2 overlay, TINY (synthetic ratify-drill).** Jake's turn-one intent call: **synthetic drill**, not a production re-scrub (no known v1-miss; the goal was to walk the overlay PATH end-to-end before a real re-scrub is ever needed). Synthetic rule: literal standalone token `EXAMPLE` (case-sensitive, `\bEXAMPLE\b`) → `[SCRUB-V2-DRILL]` — trivial, benign, strict superset of v1. N=10 slice off baseline `scrub-v1/records.ndjson` (1 header + 9 messages). Three ambiguities CC surfaced, all ruled: (#1) **omit `conversations.scrubbed.json`** from scrub-v2/ — it's a stage3 raw-ingest leftover, raw is wiped, contract names only 3 companion artifacts (Jake blessed the omit explicitly, since it's the one place the as-built v1 folder (4 files) disagreed with the ratified contract (3 files)); (#2) **six keys** in verify.log (5 v1 cred classes + EXAMPLE); (#3) **skip scrub_walk for conversation_header** (pure metadata, no text). Built `apparatus_overlay_v2_drill.py` v0.1. **All 4 gates PASS**, EXAMPLE hit 0 (zero-hit on a 10-rec slice = expected PASS), Gate-4 sha read back `4ef22940…` UNCHANGED. Jake **ratified the tiny overlay**.

3. **Rung 6 — scaled to the FULL baseline snapshot (N=23,095) + proved rung 6's hash gate at scale.** Same proven path, only N changed. The one legitimate write-inside-an-existing-overlay-dir: the scrub-v2/ drill artifacts (10 records) had to be replaced by the full 23,095-record version. Mechanism = **rm-then-rewrite** (chosen over chmod-in-place: unlink makes the drill→ratified turnover unambiguous; a sealed-then-mutated file is conceptually muddy), **guarded** by a pre-delete assert (folder must contain exactly the 3 expected files AND records.ndjson must be exactly 10 lines — positively identify the drill artifact before unlinking; never blind-delete). Script v0.1 → v0.2. **All 4 gates PASS**, Gate-4 sha `4ef22940…` UNCHANGED both ends (rung 6 proven at full scale), output records.ndjson = 367,494,524 B (full restatement). **EXAMPLE fired 3× at scale** (all in conv `3ef82921…`, 2 of the 3 hits in `display_content.json_block` — see downstream flag), first real before/after of the scrubber's match path. verify.log EXAMPLE:0 is CORRECT (verify scans the *output* — the 3 tokens are already `[SCRUB-V2-DRILL]` and don't match `\bEXAMPLE\b`; audit counts input hits, verify counts survivors — they're supposed to disagree when a rule fires). **WANT check PASS:** `_build_seen_set` on the live floor resolves **baseline → scrub-v2 (max-N=2), delta → scrub-v1 (max-N=1)** — the v1.5 seam fix confirmed on the real overlay, not just the S19 synthetic fixture.

4. **Rung 7 — the code-review gate, with a real detour (see THE /code-review LESSON below).** Manual review surfaced 3 fixable items; the REAL `code-review:code-review` tool was then run on PR #1 and returned **"No issues found"** (9 findings, all below the 80 threshold or false-positive). Three fixes applied to the drill script before commit (§6 header changelog, an unclosed file handle in the pre-delete guard → `with`-block, a discarded `_build_seen_set` return → `_, _ =`), all 3 disk-verified by Jake before commit. Pipeline header bumped v1.5 → v1.6 (changelog lines only, ZERO code change). Committed `84374cd` on scratch branch `review/scrub-v2-overlay-s20`, draft PR #1 opened, real review run, **landed to main via `merge --no-ff`**, scratch branch deleted local + remote. **Pass two (b) CLOSED.**

---

## THE /code-review LESSON (carry this — it cost real turns, and it's a §12 ref update)

**`code-review:code-review` reviews a GitHub *PR*, not a bare working tree.** Its pipeline fetches the PR via `gh pr view`, reads the PR diff, and posts findings back as a PR comment. A pre-commit review gate therefore needs a **scratch branch + draft PR** to point the tool at — you cannot run it on uncommitted working-tree changes. S20 sequenced rung 7 as "review before commit" and hit a wall: no PR existed, so the tool had nothing to fetch. The fix (path 1): commit to a scratch branch → open a draft PR → run the tool on the PR → land to main after ratification. **Also:** the correct invocation is the plugin-namespaced `code-review:code-review`, NOT `Skill(skill="code-review")`. (Proposed as a JAKE-RULES §12 addition — see 17.2 below.)

---

## CC RELIABILITY NOTE (the watch worked — twice)

CC mis-reported reality **twice** this session; both times OC stopped and checked disk instead of building on the report, and both times disk settled it:
1. **Tool-state:** CC reported `/code-review` "not a registered skill" and substituted a hand-rolled manual review. It WAS installed — wrong invocation string. OC refused to build the commit on the substitute; forced the real tool.
2. **Floor-write (the scare):** Jake (correctly, eyes-on-disk) reported "no scrub-v2 in my claude-reference dir." Triggered a ~6-turn verification pass. **Resolution: NO data loss** — Jake was looking in the *code repo* dir; the floor lives in `apparatus-archive\snapshots\…`, *outside* the git tree. scrub-v2 was exactly where it belonged, dated 5/30 6:47 PM (matching the rung-6 run), 3 files, records.ndjson 367,494,524 B, sealed read-only. **scrub-v1 live-hashed `4EF22940…` = sealed original provably untouched.** The double-paste-deletes-it fear was also ruled out (the only delete in the whole op was CC's guarded rm-then-rewrite of the *drill* files inside its own run; not Jake-triggerable from a chat paste).

**Takeaway for S21:** disk is ground truth over any CC report. The append-only floor + the per-rung sha gate are what made the scare a non-event — the architecture held exactly as designed. Keep verifying; the day a turn asks you to stop is the day to plant your feet.

---

## THE FLOOR RIGHT NOW

| snapshot | type | records | raw_wiped | overlays | seen-set resolves to |
|----------|------|---------|-----------|----------|----------------------|
| `baseline-2026-05-25-ae015455` | baseline | 23,095 (294 hdr + 22,801 msg) | true | **scrub-v1 + scrub-v2** | **scrub-v2** (max-N) |
| `delta-2026-05-28-a61498e6` | delta | 1,368 (31 hdr + 1,337 msg) | true | scrub-v1 only | scrub-v1 |

Ledger: 2 entries. Floor total: 24,463 records. `_build_seen_set` (v1.6) returns the union of all prior snapshots: **24,138 pairs / 325 headers** (this is the function's real return — NOT the 1,337/31 delta-content figure; the S19 mistake, don't re-make it).

**Immutability anchors (live-verified at S20 close):**
- baseline **scrub-v1** records.ndjson SHA-256: `4ef22940e3fbb849c2c14fba62fdae2a44277963f0ea5c9f7f2086c706415ba3` (367,494,497 B) — the sealed original, untouched through the entire overlay operation.
- baseline **scrub-v2** records.ndjson: 367,494,524 B, sealed read-only, SHA-256 `b54620afd59f0f6c9ad1b746e9254b27797e4dca1a085bdfe471ab3ef289a96c` (the full restatement; differs from v1 by the 3 `[SCRUB-V2-DRILL]` replacements + the scrub_version bump on every record).

**Pipeline:** `active/apparatus/apparatus_freeze_pipeline.py` **v1.6** on main. **Drill script:** `active/apparatus_overlay_v2_drill.py` v0.2 on main (in `active/`, NOT `active/apparatus/` — placement deferred with the pipeline relocation).

---

## S21 LIVE TARGET — seed-shape LOAD (+ pipeline relocation as the housekeeping first move)

Pass two is fully done. The next chapter (per the S19 directional note and the ANCHOR DESTINATION) is **seed-shape LOAD: the real production ingest of the floor into the locked Supabase `apparatus-floor` project**, then the **retrieval layer**. This is the research-shaped part — the three escalations feed it, still blocked on Jake's uploads.

**Before LOAD, do the deferred housekeeping (it's been queued since S19 and S20 is the natural time, or do it as the opening move of S21):**

1. **Pipeline relocation — move `apparatus_freeze_pipeline.py` OUT of `active/apparatus/`.** Canon dir = refs + context only; the pipeline is *code* and its `__pycache__` keeps landing in canon. This is a **tracked-file relocation** — touches the spec, the ignition boot list, ANCHOR read-order, every pipeline pointer, AND the drill script's `sys.path` line. NOT a casual `mv`. Deliberate pass, its own plan-mode cycle, its own commit. **The drill script placement is coupled** — wherever the pipeline lands, the drill script (currently `active/`) co-locates with it or follows the same logic. Decide both together. This is plausibly a `/jedi-council` gate (higher blast radius than rung 7) — Jake's call on whether it warrants the heavy tool.

**LOAD specifics carried from canon (D9 lock post-lock recs):**
- Single-transaction / staging-swap ingest (post-lock rec #6) — so a partial-ingest failure doesn't require an append-only-violating DELETE.
- The `display_content` selective-strip is a **load-time** transform decided at LOAD (84.4% strip-safe / 15.6% `CARRIES_UNIQUE` — see S14). **Downstream flag (from S20):** the EXAMPLE drill fired in `display_content.json_block`, confirming the scrubber DOES reach into display_content even though the v1.1 drift-detector deliberately does NOT walk it — two different passes, two different depths, both correct. Hold this distinction clear when the selective-strip toggle is designed at LOAD.
- pre-ingest lint (post-lock rec #3): duplicate JSONB keys collapse silently; TEXT rejects U+0000.
- **WHICH overlay loads:** the floor now has a real scrub-v2 on baseline. LOAD must ingest the **max-N** overlay per snapshot (baseline scrub-v2, delta scrub-v1) — the same `_build_seen_set` max-N resolution, now load-side. This is the first time LOAD has to choose an overlay; before S20 it was scrub-v1 trivially everywhere.

---

## PROCESS REMINDERS FOR S21

- **Commits to Jake are PowerShell-safe.** Single-line, multiple `-m` flags. NO bash heredocs (`$(cat <<EOF)` choked S19). No `&&` chaining. One command per line. Jake on Workhorse / PowerShell.
- **OC authors FULL canon files in chat; never-commit ≠ never-author.** Re-pull fresh HEAD, edit surgically on the real file (str_replace / char-offset, not retype-from-context), hand the complete file via `present_files`. Jake verifies-against-disk, saves, commits, pushes. OC never commits canon; OC DOES author it.
- **All CC prompts go in a code block.** Clean seam OC-prose vs CC-instruction.
- **Run the pipeline with `python -B`** (no `__pycache__` in canon dir — and the relocation above exists precisely to end this).
- **`code-review:code-review` needs a PR** — scratch branch + draft PR, not a bare working tree. (The S20 lesson; §12 update proposed.)
- **CC can't stage/commit in its session** (permission wall hit at `git add`, S20) — CC hands the command sequence to Jake, Jake runs it. This is fine and rule-consistent (push stays Jake's anyway). Verify CC's claimed edits on disk BEFORE Jake commits (`git diff` for tracked files; `Get-Content`/`Select-String` for untracked — `git diff` is BLIND to untracked files, that's how the S20 script-fix verification almost got skipped).
- **Disk is ground truth over any CC report.** Two CC mis-reports this session, both caught by checking disk. Keep doing it.
- **The floor lives in `apparatus-archive\snapshots\…`, OUTSIDE the git tree.** Not in `active/`, not in the repo root. (The S20 scare was looking in the wrong root.)
- **⚑ 4 loose files STILL in `apparatus-archive/snapshots/` root** — `__recon_step0.py`, `__recon_step0b.py`, `__recon_step0c.py`, `__verify_shape.py`. Open since S17, NOT resolved S18/S19/S20. Investigate provenance with fresh eyes, THEN remove if confirmed junk. **Never blind-delete from inside the floor dir.**
- **⚑ S20 scratch accumulation** — `apparatus-scratch/` carries the S19 files + whatever the drill runs left. All gitignored, harmless — worth a sweep so they don't become the next "what are these."
- **⚑ DB password rotation still queued** (post-D9-lock item #7, CC echoed it to chat in S16). Not blocking; owner Jake/homelab.
- **Jake co-pilots intent, OC pilots engineering.** Jake is not a coder — don't hold technical/syntax calls for his approval; DO hold intent calls (real-vs-synthetic, warn-vs-stop, accept-a-tradeoff, land-vs-fix-first). Translate to plain English.

---

## DON'T-RELITIGATE (carried + S20 additions)

- D9 LOCKED (Supabase); floor append-only ENFORCED; ndjson canonical / Postgres rebuildable.
- raw.json Path A (wipe after verify-PASS) — applied both snapshots. **Raw is wiped, gone, never in the picture again.** Overlays re-scrub the SCRUBBED output, never raw.
- Delta = uuid-set-difference, date never a filter.
- No-duplicate-header rule — PROVEN on the floor (1,368 not 1,371). 31 (header-based) is correct, don't "fix" to 34.
- Roots carry sentinel `00000000-0000-4000-8000-000000000000`, no self-FK.
- 5-28 is a FULL point-in-time export (superset of baseline), NOT the delta slice.
- token_budget n=14 is the true population — included in v1.1 allowlist, annotated low-confidence. Don't exclude it.
- v1.1 depth is top-level keys only, warn-not-stop — both deliberate.
- The seam fix (v1.5) is DONE + PROVEN — max-N glob, integer sort, hard-stop-on-missing-dir. Don't reopen.
- The overlay contract's 3 invariants are RATIFIED LAW (tighten-only / full-restated-standalone / accrete-forever). Build to them, don't redesign.
- `_build_seen_set` returns the UNION of all prior snapshots (24,138 / 325), NOT the delta slice (1,337/31).
- **NEW — pass two (b) is CLOSED.** Overlay capability built, proven (Rungs 5–6), reviewed (real `code-review:code-review`, PR #1, "No issues found"), landed on main at v1.6. Don't re-open it. The scrub-v2 overlay on baseline is the first real overlay and it's correct + sealed.
- **NEW — the scrub-v2 overlay is SYNTHETIC (a ratify-drill), not a production re-scrub.** It exists to prove the path, redacting only the benign `EXAMPLE` token (3 hits). It is NOT a change to production redaction policy. A REAL re-scrub (a genuine improved-scrubber pass catching a real v1-miss) is a future event that will mint scrub-v3 when/if a real miss is found. Don't mistake the drill overlay for a production redaction improvement.
- **NEW — the S20 "missing scrub-v2" was a NON-EVENT** (wrong-root look; floor intact; scrub-v1 hash unchanged). Don't carry it forward as a data-integrity question — it's settled. The floor is in `apparatus-archive\`, not the code tree.

---

## JUDGMENT-CALL LEDGER (S20 non-obvious calls, per §17.5c)

- **Recommended synthetic drill over real re-scrub for the first overlay** — call: OC rec, Jake's intent decision. Reasoning: no known v1-miss in hand; exercising the overlay path end-to-end on zero-stakes data means the FIRST real re-scrub runs a proven path. Confidence: high. Source: the rung-5 first-move intent gate in the S19 handoff.
- **Blessed omitting `conversations.scrubbed.json` from scrub-v2/** — call: Jake's, OC strong rec (~90%). Reasoning: it's a stage3 raw-ingest leftover, raw is wiped, the ratified contract names exactly 3 companion artifacts; emitting a v2 of it would invent an unspecified transform on the first immortal write. Confidence: high — contract text backs it. Source: the overlay contract (ANCHOR v13) + the as-built v1 folder inspection.
- **rm-then-rewrite over chmod-in-place for the drill→full swap** — call: CC proposed, OC OK'd. Reasoning: unlink makes the drill→ratified turnover unambiguous; a sealed-then-overwritten file is conceptually muddy on an append-only floor. Guarded by a pre-delete 3-files-and-10-lines assert. Confidence: high. Source: the contract's may/must-not boundary + append-only doctrine.
- **Refused to accept the manual review as the rung-7 gate; forced the real tool** — call: OC, firm. Reasoning: Jake specifically asked for `/code-review` as the safety net; the real tool turned out runnable (PR-shaped); accepting the substitute would write a false "review passed" into the record. Confidence: high — it's the §5 / the-watch principle applied to the gate itself. Source: the false-tool-state report + Jake's confirmation the tool is installed.
- **Recommended LAND AS-IS on the 9-finding review (none ≥80)** — call: OC rec, Jake ratified. Reasoning: 2 false-positives are the tool misreading intentional design; the 7 below-threshold are real-in-principle/zero-in-practice on a throwaway harness; nothing touches floor-write correctness or the gates. Confidence: high. Source: read all 9 findings against the code.
- **Declined `/jedi-council` as a substitute for the blocked `/code-review`** — call: OC. Reasoning: council is heavy (gate-only, ~75k tokens) and likely shares the PR dependency; swapping tools dodges the real sequencing issue rather than fixing it; the drill script isn't a council-worthy gate. Flagged council as the RIGHT tool for the COMING gates (pipeline relocation / seed-shape LOAD). Confidence: high. Source: JAKE-RULES §12.
