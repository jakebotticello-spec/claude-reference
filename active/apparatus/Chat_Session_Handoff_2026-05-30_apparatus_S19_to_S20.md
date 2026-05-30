# Chat Session Handoff — apparatus S19 → S20
*authored by OC at S19 close, 2026-05-30 · read after ANCHOR + JAKE-RULES + JAKE-STACK · tactical state, not authority (ANCHOR is authority)*

---

## ONE-LINE STATE

D9 is LOCKED (Supabase, append-only ENFORCED, ndjson canonical). Pass two **(a) — v1.1 field-drift — is DONE/SEALED** (v1.4). Pass two **(b) is IN PROGRESS:** the scrub-version seam is FIXED, PROVEN, and SEALED (pipeline v1.4 → v1.5, commit `98e9cef`, pushed), and the **scrub-vN overlay contract is RATIFIED in canon** (ANCHOR v12 → v13). **S20's live target is the rest of the (b) ladder, starting at RUNG 5: mint the FIRST scrub-vN overlay tiny → verify → Jake ratifies → scale.** Floor unchanged — 2 snapshots / 24,463 records, both scrub-v1 only; NO overlay minted yet.

---

## WHAT S19 DID

1. **Booted cold, verified everything against live disk.** ANCHOR v12 freshness PASS (banner v12 / "S18 — v1.1 FIELD-DRIFT BUILT, PROVEN & SEALED" / v1.4 live). Re-pulled fresh HEAD mid-session before authoring canon (confirmed the v1.5 floor commit had landed and the ANCHOR was unchanged by it — code and canon are separate trees). Confirmed the seam at `_build_seen_set` line ~366 in the live code, exactly where canon said — the ONE read-side `scrub-v{SCRUB_VERSION}` use, vs the ~8 write-side uses that are correct as-is.

2. **Rung 1 — fixed the scrub-version seam.** Replaced the hardcoded `scrub-v{SCRUB_VERSION}` read path in `_build_seen_set` with per-snapshot max-N resolution: `iterdir()` + `re.fullmatch(r'scrub-v\d+')` filter, integer-keyed sort (`key=lambda p: int(...)`), `[-1]` picks the highest overlay. Hard `sys.exit` if NO `scrub-v*` dir exists — **a missing overlay at seen-set-build time = floor integrity already broken; stop, don't warn** (Jake's ratified intent call — continuing would build the seen-set off incomplete data, which on an append-only floor = immortal wrong rows). Write-side `SCRUB_VERSION` uses unchanged. Pipeline v1.4 → v1.5.

3. **Rung 2 — PROVED the seam fix is a measured no-op on the v1-only floor.** Not argued — measured. Ran pre-fix (v1.4, pulled from git) and post-fix (v1.5) `_build_seen_set` against the real floor; both return a **set-equal** seen-set (not just same cardinality — content-equal): **24,138 pairs / 325 headers.** This corrected a spec error of OC's own: the build prompt targeted "1,337/31," but that's the *delta records.ndjson content*, NOT what `_build_seen_set` returns. The function returns the **UNION of all prior snapshots** (baseline 22,801 + delta 1,337 = 24,138; headers 294 + 31 = 325). CC flagged the mismatch, OC did NOT accept the reconciliation on faith — forced a true before/after on the same quantity (rung-2 close-out turn), and it came back identical. The union-contract is now banked as the correct ground-truth.

4. **Rung 3 — PROVED the fix delivers the NEW behavior (synthetic fixture).** A no-op proof alone can't tell "correct max-N" from "always returns v1." Built a two-snapshot fixture in `apparatus-scratch/`: snap-A with scrub-v1 (2 pairs) + scrub-v2 (3 pairs, different UUIDs), snap-B scrub-v1 only. Proved THREE ways, all PASS: (1) snap-A resolves **v2 by content** (v2 UUIDs present, v1 UUIDs absent), snap-B resolves v1; (2) junk dirs (`scrub-v2-backup`, `scrub-vX`) ignored by the regex; (3) **scrub-v10 added → picks v10 not v2** — proves TRUE INTEGER max-N, not lexical sort (lexical would wrongly pick "v2" > "v10"). The v10>v2 check is the teeth — it's the bug the int-keyed sort exists to prevent. (Note: fixture records had no headers, so `headers=0` throughout — examined and benign; the glob resolves one records.ndjson path per snapshot, headers and pairs both read from that same resolved file, so proving pairs picks v2 proves headers would too. Path resolution is upstream of the pairs/headers split.)

5. **v1.5 committed + pushed `98e9cef`.** (Process scar: the first commit attempt used a bash heredoc `$(cat <<EOF)` that choked in PowerShell — "missing file specification." Burned two turns sorting out repo state (the `git add` HAD run, only the commit heredoc failed). Lesson now in the ignition + below: **commits to Jake are PowerShell-safe single-line multi-`-m`, never heredocs.**)

6. **Rung 4 — AUTHORED + Jake RATIFIED the scrub-vN overlay contract in canon prose, BEFORE any overlay code.** Three intent questions put to Jake one at a time, all ruled:
   - **Tighten-only** — raw is wiped, so an overlay re-scrubs the prior version's *scrubbed* output; can redact MORE, never less, never recovers redacted text. Jake accepted the stated cost: "if v1 over-redacted, v2 cannot give it back."
   - **Full-restated-standalone** — each scrub-vN is a complete, directly-hashable records.ndjson (NOT a delta), preserving the D9 read-don't-reconstruct reframe. Disk cost accepted (scrub-vN events rare).
   - **Accrete-forever** — superseded overlays never removed (S16 `floor_immutable_guard()` forbids the DELETE mechanically + the prior version is the scrubber's own audit trail).
   The contract (3 invariants + may/must-not boundary + the sha-unchanged gate tied to rung 6) is now a RATIFIED INVARIANT block in ANCHOR. **ANCHOR v12 → v13.**

7. **De-duped the v8 enshrine tail** (the S18-logged copy-paste doubling) as its own pass — a 2,864-char dangling bare duplicate of the v8-block body, cut by character span on disk (str_replace had failed on smart-quote/em-dash mismatch; Python char-offset cut worked). "S13 closed Stage 0" went 4 → 3 occurrences (all 3 remaining legit: line-16 note, the v8-block's own statement, the nested v6→v7 recap inside v8).

8. **OC authored the FULL canon files in chat** (ANCHOR v13 + CHANGELOG S19 entry), handed via `present_files` for Jake to verify-against-disk → save → commit → push. (Process correction worth carrying: OC initially refused to regenerate the full ANCHOR, conflating never-COMMIT-canon with never-AUTHOR-canon. Jake corrected: authoring the full file in chat IS the OC role; Jake's verify-against-disk is the drift check. OC then re-pulled fresh HEAD and made the edits surgically on the real file rather than retyping 200 lines from context — the right way to honor the §5 don't-reproduce-from-memory concern WITHOUT refusing the job.)

---

## THE FLOOR RIGHT NOW (unchanged from S17/S18 — S19 didn't touch it)

| snapshot | type | records | raw_wiped | overlays | notes |
|----------|------|---------|-----------|----------|-------|
| `baseline-2026-05-25-ae015455` | baseline | 23,095 (294 hdr + 22,801 msg) | true | scrub-v1 only | seen-set authority |
| `delta-2026-05-28-a61498e6` | delta | 1,368 (31 hdr + 1,337 msg) | true | scrub-v1 only | prior → baseline |

Ledger: 2 entries. Floor total: 24,463 records. **Both snapshots scrub-v1 only** — no overlay exists yet. `_build_seen_set` (v1.5) returns the union: **24,138 pairs / 325 headers** (bank this number — it's the function's real return, not the 1,337/31 delta-content figure).

baseline scrub-v1 records.ndjson SHA-256 (the immutability anchor for rung 6): `4ef22940e3fbb849c2c14fba62fdae2a44277963f0ea5c9f7f2086c706415ba3` (from the D9 lock). **Re-confirm this read-back UNCHANGED after any overlay is minted — that's rung 6.**

---

## S20 LIVE TARGET — PASS TWO (b), RUNGS 5–7: mint the first scrub-vN overlay

**Do NOT start without Jake's OK. Plan-OC / build-CC / plan-mode. This is the immortal-floor-WRITING half — the first three rungs only fixed+proved the read path and authored the contract; rung 5 is the first turn that actually WRITES a new floor artifact. Fresh head, max paranoia.**

**⚑ FIRST MOVE is an INTENT question, not code: is the first overlay a REAL production re-scrub or a SYNTHETIC ratify-drill?** An overlay exists only when the scrubber materially improved (caught a cred class v1 missed). Two cases, Jake's call turn one:
- **Real:** there's a known v1-miss (a cred pattern that survived into the scrub-v1 output). Then scrub-v2 is a production re-scrub with a genuinely improved scrubber regex set, and the small-batch is a real subset.
- **Synthetic ratify-drill:** no known v1-miss yet, but we want to exercise + prove the overlay PATH end-to-end before a real re-scrub is ever needed. Then mint a trivial-but-real scrub-v2 (e.g. one additional benign redaction rule) on a tiny slice purely to walk the contract's machinery and prove rungs 6–7, NOT to change production redaction.
Which one it is changes everything downstream. Get Jake's ruling before planning the build.

The ladder for rungs 5–7, in order (NEED = won't proceed without; WANT = cheap insurance):

5. **NEED — ratify a small batch before scale.** Append-only ⇒ un-ratified rows are immortal. Generate the FIRST scrub-v2 overlay TINY (a small record subset), verify it against the contract (full-restated-standalone: it's a complete records.ndjson for that subset, hashable; tighten-only: it redacts ≥ what v1 did, never less), Jake ratifies, THEN scale to the full snapshot. The contract's may/must-not boundary is LAW the code must obey — overlay writes a NEW `scrub-v2/` dir, touches NO existing `scrub-v1/` file.
6. **NEED — prove the overlay did NOT mutate the sealed scrub-v1.** Read back the baseline scrub-v1 `records.ndjson` sha256 after the v2 overlay is generated — must equal `4ef22940…` unchanged. This is the contract's explicit verification gate. Overlay = new versioned layer, never edit-in-place.
7. **NEED — `/code-review` + Jake ratification before the overlay-code commit.** Pipeline v1.5 → v1.6 at (b) close. (This is also the natural pairing-point for the pipeline-relocation decision — see process flags.)

**WANT (cheap insurance, fit where natural):** confirm the max-N glob (v1.5, already proven on the synthetic fixture) resolves the NEW real v2 overlay correctly once it exists on the real floor — i.e. that `_build_seen_set` now reads v2 for the re-scrubbed snapshot. This is the live-floor version of the rung-3 fixture proof.

**After pass two (b) fully closes:** seed-shape LOAD (real production ingest into locked Supabase, single-transaction/staging-swap per post-lock rec #6; the `display_content` selective-strip is a load-time toggle decided there) → retrieval layer (the real next chapter; research-shaped; the three escalations feed it, still blocked on Jake's uploads).

---

## PROCESS REMINDERS FOR S20

- **Commits to Jake are PowerShell-safe.** Single-line, multiple `-m` flags. NO bash heredocs (`$(cat <<EOF)` choked in PowerShell, S19, cost two turns). No `&&` chaining. One command per line. Jake is on Workhorse / PowerShell.
- **OC authors FULL canon files in chat; never-commit ≠ never-author.** When canon needs editing, OC re-pulls fresh HEAD, makes the edits surgically on the real file (str_replace / char-offset, not retype-from-context — honors §5), hands the complete file via `present_files`. Jake verifies-against-disk, saves, commits, pushes. OC never commits canon; OC absolutely DOES author it.
- **All CC prompts go in a code block** (clean visual seam between OC-prose-for-Jake and instruction-for-CC).
- **Run the pipeline with `python -B`** (suppresses `__pycache__` landing in the canon dir).
- **Pipeline commits go through CC; push stays Jake's. Canon (.md) is OC-authored / Jake-committed; CC never touches canon.**
- **⚑ 4 loose files STILL in `apparatus-archive/snapshots/` root** — `__recon_step0.py`, `__recon_step0b.py`, `__recon_step0c.py`, `__verify_shape.py`. Open since S17, NOT resolved S18 or S19. Investigate provenance with fresh eyes (inert old probes, or referenced by tooling?), THEN remove if confirmed junk. **Never blind-delete from inside the floor dir.**
- **⚑ S19 scratch accumulation** — `apparatus-scratch/` now holds `pipeline_v14_readonly.py`, `s19_noop_proof.py`, `s19_rung3_fixture.py` + the `s19_rung3_fixture/` dir. All gitignored, all under apparatus-scratch/, harmless — but worth a sweep so they don't become the next "what are these" mystery. NOT in snapshots/.
- **⚑ DECISION still open: move `apparatus_freeze_pipeline.py` OUT of `active/apparatus/`.** Canon dir = refs + context only; the pipeline is code and its `__pycache__` keeps landing in canon. TRACKED-FILE relocation (touches spec, ignition boot list, ANCHOR read-order, every pipeline pointer) — deliberate task with reference-updates, NOT a casual move. Good pairing: do it alongside the v1.6 commit since the file's being edited anyway. Decide in S20.
- **⚑ DB password rotation still queued** (post-D9-lock item #7 — CC echoed it to chat in S16). Not blocking; owner is Jake/homelab.
- **The v8 enshrine de-dupe is DONE (S19) — don't re-raise it.**
- **VS Code switch — DONE (S18). Don't re-raise.**
- **Jake co-pilots intent, OC pilots engineering.** Jake is not a coder — don't hold technical/syntax calls out for his approval. DO hold intent calls (real-vs-synthetic overlay, warn-vs-stop, accept-a-tradeoff) — his alone, the second-navigator seam. Translate results to plain English.

---

## DON'T-RELITIGATE (carried + S19 additions)

- D9 LOCKED (Supabase); floor append-only ENFORCED; ndjson canonical / Postgres rebuildable.
- raw.json Path A (wipe after verify-PASS) — RESOLVED S15, applied both snapshots S17. **Raw is wiped, gone, never in the picture again** — overlays re-scrub the SCRUBBED output, never raw.
- Delta = uuid-set-difference, date never a filter — BUILT + PROVEN S17.
- No-duplicate-header rule — PROVEN on the floor S17 (1,368 not 1,371).
- 31 (header-based) is correct — reconciled S17, NOT an error. Don't "fix" 31→34.
- Roots carry sentinel `00000000-0000-4000-8000-000000000000`, no self-FK.
- 5-28 is a FULL point-in-time export (superset of baseline), NOT the delta slice.
- token_budget n=14 is the true population — included in v1.1 allowlist, annotated low-confidence. Don't exclude it.
- v1.1 depth is top-level keys only, and warn-not-stop — both deliberate. Don't "harden" either.
- **NEW — the seam fix (v1.5) is DONE + PROVEN. Don't reopen it.** Max-N glob, integer sort, hard-stop-on-missing-`scrub-v*`-dir, all ratified + proven (no-op on v1 floor / picks-v2-by-content / v10>v2 / ignores-junk).
- **NEW — the overlay contract's 3 invariants are RATIFIED LAW.** Tighten-only / full-restated-standalone / accrete-forever. Do NOT redesign them — BUILD to them. They were authored as prose and Jake-ratified specifically so the overlay code has a fixed contract to obey.
- **NEW — `_build_seen_set` returns the UNION of all prior snapshots (24,138 pairs / 325 headers), NOT the delta slice.** 1,337/31 is the delta records.ndjson *content* — a different quantity. S19 briefly mistook one for the other and corrected it; don't re-mistake it. The union IS the function's contract (it's building "everything seen so far" so the next delta can diff against it).

---

## JUDGMENT-CALL LEDGER (S19 non-obvious calls, per §17.5c)

- **Forced a true before/after on `_build_seen_set` rather than accepting CC's union-reconciliation** — call: re-measure old-code vs new-code on the same quantity. Reasoning: CC's explanation of why my "1,337/31" target was wrong was plausible AND it was the verifier explaining away a mismatch against the expected value — indistinguishable from rationalization without the measurement. Confidence: high it was the right call (it's the §5 watch applied to the proof itself). Source: the no-op proof is rung 2, a NEED; "argued" ≠ "measured."
- **Kept the new hard-stop on a missing overlay dir (stop, not warn)** — call: Jake's, OC recommended stop. Reasoning: a missing overlay at seen-set-build = floor integrity already broken; "warn and continue" builds the seen-set off incomplete data → immortal wrong rows. Confidence: high. Source: append-only doctrine + the contract.
- **Reformatted the CHANGELOG entry to the house Scope/Change(s)/Why template** — call: match existing entries rather than ship the looser prose draft. Reasoning: consistency in canon; the draft would've been the stylistic odd-one-out. Confidence: high, cosmetic. Source: the format block at the top of CHANGELOG.md.
- **Char-offset cut for the v8 de-dupe after str_replace failed** — call: switch from str_replace to a Python char-span cut. Reasoning: str_replace missed on smart-quote/em-dash mismatch in the dense line; the char-offset approach is robust to those characters and I verified the cut boundaries (tail occurrences, following context) before writing. Confidence: high (verified S13-closed count 4→3, all remaining legit). Source: the live-file grep + view.

---

*S19 took pass-two (b) from "seam still live" to "seam fixed + proven both directions + overlay contract ratified law" — the entire read-side-and-contract half of (b), every step gated. The first three rungs were deliberately the safe half (fix a read path, prove it, write words); rung 5 is where the first immortal floor-WRITE happens, which is exactly why it was held for a fresh head. The one thing S20 must settle before any code: is the first overlay real or a ratify-drill? Grind. Evolve. Dominate.*

— OC, S19 close, 2026-05-30. Be worth it.
