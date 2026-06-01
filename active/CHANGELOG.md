# CHANGELOG.md

**What changed when.** Dated entries, newest first. Update at the end of every CC session that changes anything material (rules, project status, hardware, infrastructure, tooling).

Format:
```
## [DATE] — [Session ID or scope]
**Scope:** [what was touched]
**Change(s):**
- [bullet of what changed]
- [bullet of what changed]
**Why:** [one-line context if not obvious]
```


## 2026-06-01 — apparatus S25 (The Progenitor v1→v2 · retrieval engine conceptual design complete · seeding-council boot kit v0.1→v0.2 · ANCHOR v18→v19)

**Scope:** Design + canon session. **No floor mutation. No invariant moved. No application code committed.** Canon authored by OC, verified-against-disk by Jake, committed by CC, and **pushed to main by Jake at session close** (push confirmed live on main): `active/apparatus/The_Progenitor_v2_2026-06-01.md` (NEW — supersedes v1, which stays on disk tombstoned-not-deleted), `active/apparatus/Seeding_Council_Boot_Kit_v0.1_2026-06-01.md` then `active/apparatus/Seeding_Council_Boot_Kit_v0.2_2026-06-01.md` (v0.2 supersedes v0.1 in-session; v0.1 tombstoned-not-deleted), ANCHOR v18→v19, this entry, the S25→S26 handoff. (Amended post-push: this entry originally described only boot-kit v0.1 with the 6 review changes "queued for v0.2"; v0.2 was then built and pushed in the same session, so the entry is corrected to reflect what actually shipped.)

**Change(s):**
- **The Progenitor v1→v2 (NEW file, folds the conceptual retrieval design).** v2 reproduces §0–§9 **byte-identical to v1** (diff-verified: 200 lines each, empty diff — the doctrine body Jake ratified at S24 did not move) and ADDS four sections from the three S24 design specs + the S24 council model: **§10 trigger model** (ONE engine, three throttles — Claude-initiated ambient / re-anchor-driven / Jake-fired; the catalog rides in at BOOT via the ignition/Anchor, the triggers query it LIVE; boot is the substrate, not a fourth trigger). **§11 span-return shape** (Layer A raw span text across the tree-aware reach, verbatim/scrub-redacted, never summarized; Layer B the §4 floor-key locator carried alongside; Layer C kind-context — FENCE returns the FULL why-chain non-negotiably, TEXTURE returns representative-span + count + spread; "the card and the page, never a book report"). **§12 seeding process** (the original catalog read of the laid floor by a council of BLIND parallel windows divided by project-scope + a cross-cutting no-project reader; division in the LABOR never the INDEX; per-batch spot-audit by Jake on the SYNTHESIZED catalog as the one scoped relaxation of human-as-immutability-mechanism). **§13 council boot kit** (sized for recognition-not-projection; the load-bearing call — texture-readers do NOT boot with the Wallaby Why / Lore Bible because that's projection not recognition, JAKE-RULES §1.2 turned on the council; chat_search + catalog-so-far + sibling-proposals are hard walls; the synthesis/merge-back pass where blind-read convergence becomes a confidence signal and cross-slice counts assemble).
- **§9 amended (query interface IN; build-work + embedding OUT).** v1 listed the query interface as out-of-scope; v2 brings it in (§10–§13). What stays out: on-disk serialization, ranking-algorithm internals inside the §6 selector envelope, reach defaults, multi-hit presentation, the slice-manifest mechanism — all CC-build-against-the-live-floor.
- **Two S25-original calls beyond the S24 specs.** (1) **KEYWORD-FIRST retrieval** — v1 engine is keyword-lookup over the dict catalog; vector/semantic-reach is a DEFERRED v2 sidecar (pgvector, never on the floor per D9), added only if the seeding pass proves a measured semantic gap. Rationale: the fast pointer-hit path wants PRECISION, corpus-search already owns RECALL, vectors-in-v1 would blur the two split modes and pull the §1 "forty half-relevant spans" feel-rightness failure; the vector question is routed THROUGH the seeding pass as its acceptance test. (2) **KEYWORD-COVERAGE as a seeding-quality bar** (§8/§12) — a card's keywords are laid for future-SEARCH-anticipation (would a future Claude actually search these to reach this span), not just topical accuracy; brittleness here is exactly what would force vectors later.
- **Seeding Council Boot Kit v0.1 authored (NEW file).** `active/apparatus/Seeding_Council_Boot_Kit_v0.1_2026-06-01.md` — the applied layer operationalizing §12+§13 into the kit a council window boots with. Subordinate to the doctrine (doctrine wins on conflict); references-not-restates The Progenitor. Single-doc-all-roles form for review; splits into per-window deployable prompts after ratify. Common kit (Progenitor v2 + the §3 worked examples + JAKE-STACK + a one-page operating brief), role-adds (fence-readers → JAKE-RULES; texture-readers → thinnest-identity-load only, NOT the Why/Lore), hard walls (no chat_search ever / no catalog-so-far / no sibling proposals / no flat-N spans / never-claim-saved), the blind-read + synthesis model, the per-batch review model, and 4 open questions surfaced for review.
- **Three independent reviews on the boot kit v0.1, then v0.1→v0.2 BUILT and pushed (same session).** v0.1 went through Jake's review + a live S24-Claude cross-check (via Jake as bridge) + two cold blind reviewers (one of whom reviewed a stale pre-v2 state by accident, then revised against real v2). The reviews CONVERGED independently on the load-bearing findings — convergence treated as signal. `active/apparatus/Seeding_Council_Boot_Kit_v0.2_2026-06-01.md` lands them; v0.1 tombstoned-not-deleted. v0.2 changes:
  - **NEW §4a JUDGED PASS** — a non-blind third step (after the blind read and the mechanical synthesis) that owns what neither a blind slice-reader nor a mechanical synthesizer can: fence-CHAIN assembly (order-by-date, preserve supersession, never drop a link, escalate to Jake if it can't confidently order) + the RECALL check (a known-fence checklist). The single structural fix under three converged findings at once.
  - **The cardinal-sin risk §4a closes:** two blind windows on different slices lay two fences on the same topic with DIFFERENT calls (they read different links of a chain that evolved). If synthesis collapses them and picks the wrong link as "current," §11's non-negotiable full-chain return delivers a WRONG chain at MAXIMUM confidence — the doctrine's strongest guarantee corrupted by the kit's least-specified operation. Silently erasing a superseded link is the one thing the doctrine forbids above all (§2.3, §7).
  - **Synthesis BOUNDED to mechanical** — collapse only same-span/same-fence/same-CALL; merge keyword variants; assemble cross-slice texture counts ONLY after a same-SIGNAL check (same keyword ≠ same signal — don't sum a personal-slice Griffin-weight with a build-slice "forgot to deploy" into a spurious count); FLAG candidate chains, never decide them (the v0.1 "catch related fences that should be one chain" meaning-work was removed from synthesis and routed to §4a).
  - **THE RECALL GAP (highest-value review find).** v0.1's safety case was circular — "go lighter because overload is the catchable risk" — but the spot-audit catches only PRECISION (do the cards that exist hold the bar), never RECALL (a fence never laid leaves no shape to sample; you cannot spot-audit an absence). v0.2's fix is the §4a known-fence checklist: canon already names ~a dozen real fences (1Pass, no-"Oueilhe", REFUSED wall, Supabase-over-Nornic, therapist-voice boundary, full-code-not-diffs, FK-drop option c, D9, no-`&&`-chaining, no-duplicate-header); any the council missed is a *measured* recall failure. The precision/recall split is now explicit: precision = Jake's spot-audit on output shape; recall = the checklist.
  - **Examples calibrate SHAPE not MEANING** + "resemblance to a calibration example is NOT a count" + two NO-card shapes (texture + fence). The v0.1 calibration examples were themselves a projection vector — handing Griffin's-pickup "in full" primes readers to hunt Griffin-shaped things.
  - **Role taxonomy COLLAPSED** from v0.1's by-kind split (fence-reader/texture-reader) back to the doctrine's by-SLICE division (§12): scope readers read BOTH kinds; cross-cutting reader; plus the new judged pass.
  - **Projection wall UNIVERSALIZED** across all reading roles (v0.1 stated it only in the texture section, which let a fence-reader skirt it) — including walling JAKE-RULES §11 ("Patterns Jake Has Flagged" / the Griffin-meds portrait material) as a reading lens. Plus: content-neutral slicing stated as doctrine; the branch-id-is-DERIVED-not-stored note; the convergence-contamination caveat (don't count convergence on the calibration examples themselves); a convergence-map audit appendix for Jake's spot-audit; "lighter when in doubt" clarified as a LOADOUT heuristic, NOT a laying heuristic. v0.2 ships with 3 residual open questions (judged-pass-portrait, JAKE-RULES-§11-wall verification, keyword-coverage-criterion) flagged for ratify, NOT smuggled into confident canon.
- **Off-site backup question scoped (no action — post-lock hardening, still queued).** The Anthropic export is a forward-only re-pull backstop with a since-deleted-conv blind spot (the NAS cold-copy carve-out already covers exactly that). So the SPOF flag narrows: NAS weekly = cheap redundancy (same-LAN, not off-site); object-locked cloud (S3/B2/R2 with object-lock) = the real SPOF-close (off-site AND write-once); GitHub (367MB > 100MB limit, git history rewritable, corpus-in-git is a deliberate gitignore wall), Google Drive (off-site but a sync surface, not WORM), and a second Supabase project (credential-isolation only, still same trust-domain) all ruled out for the artifact. The through-line: all three rejected options reach for off-site but land on WRITABLE surfaces; write-once is the missing axis.
- **ANCHOR v18→v19.** Banner + S24→S25 READ-FIRST rewritten (conceptual design complete, the four folded sections, the two S25 calls, the boot kit + cross-check, the S25→S26 first moves); PROGENITOR block heading + File line → v2 with the byte-identity note; PROGENITOR out-of-scope line narrowed; NEXT MOVE #4 rewritten (conceptual design complete → BUILD is next, with the content-neutral-slicing constraint); a retrieval-layer line added to CONFIDENCE FLAGS; v19 enshrine footer prepended above v18 (all prior footers preserved verbatim).
- **Floor untouched, re-confirmed live earlier in the lineage** — no `--execute`, no schema change, no pointer laid. This session designed and wrote canon only.

**Why:** S24 authored the pointer-catalog law (The Progenitor v1) and laid the floor's predecessor work. S25 designed the engine OVER that catalog and folded the whole conceptual design back into the doctrine, then built the first applied artifact (the seeding-council boot kit) and ran it through the doctrine's own review pattern — blind independent reviews then a reconcile, the kit's own §4 mechanism used on the kit itself — landing v0.2 before the kit ever runs. The session's defining texture: lore-first held end to end — every fork S25 posed that S24 had already settled was caught by Jake grabbing the prior spec rather than letting S25 re-derive it. The apparatus ran on its own prior author, which is exactly what the retrieval layer is being built to make automatic. Conceptual stack DONE; everything remaining is CC-build-against-the-live-floor.

## 2026-05-31 — SD34 (homelab / JAKE-STACK §8 drive-manifest restore)

**Scope:** `JAKE-STACK.md` §8 — surgical edit. No other section, no other file's content touched (CHANGELOG footer + this entry only).
**Change(s):**
- **§8 drive inventory rebuilt into a real manifest.** The condensed one-liner (`PNY CS1311 240 / Crucial BX500 240 / Barracuda 750 / WD Black 640 / WD Caviar Green 1TB`) had silently dropped the **3× Kingston 120GB (UV400/SA400)** and **every per-drive role/trust note**. Restored from the SD15 9-drive inventory + the S17c/SD24 drive-role plan, split into SSD / HDD / found buckets.
- **VM-expansion earmark made explicit:** the "256GB SATA earmarked for other CB VMs" = **PNY CS1311 240GB SSD → boot/VM**, Crucial BX500 240GB as partner. Recorded so the spinny-vs-non-spinny question is answerable from the hot layer instead of buried in a May handoff. A SATA **HDD** is explicitly NOT a peer to this earmark (random-I/O VM disks → re-introduces the §3 hang-debugging trap); spinners only OK under low-I/O VMs.
- **Trust flags restored:** OCZ Vertex 2 = install-media only / don't-trust; WD Caviar Green 1TB = head-park-aggressive, retire-candidate / don't-trust; Barracuda 750 = Frigate target; WD Black 640 = §2 CB-backup candidate.
- **5-31 office-excavation find logged:** Seagate Momentus ST9500423AS, 500GB, 7200rpm, 2.5" SATA, DOM 03/2012 = **e-waste/scratch** (spinny vs the SSD earmark; not the best CB-backup candidate either). Wipe before disposal (2012 pull, possible old data).
- STACK footer: prior "Last Update: 5-29" demoted to "Prior:", new 5-31 (SD34) surgical-edit footer prepended.
**Why:** Jake had a drive in hand and the answer (SSD earmark, not spinny) lived only in PK handoffs, not the reference file — the §8 condensation lost it. Capacities/models are from handoffs, NOT re-verified on-disk this session.

## 2026-05-31 — apparatus S21 (pipeline relocation: DONE-ON-DISK, UNCOMMITTED, PARKED — commit blocked on CC git-add deny)

**Scope:** Attempted the S20-deferred pipeline relocation. Work done + verified on disk, **NOT committed** — parked on branch `review/pipeline-relocation-s21`. Canon authored this session (OC, for Jake to verify-commit-push): ANCHOR v14→v15, JAKE-RULES §12 + footer, this entry, S21→S22 handoff. **No floor mutation. No invariant moved. No prod commit landed.**

**Change(s):**
- **Pipeline relocation built + verified on disk (uncommitted).** `git mv active/apparatus/apparatus_freeze_pipeline.py → pipeline/apparatus_freeze_pipeline.py` and `git mv active/apparatus_overlay_v2_drill.py → pipeline/apparatus_overlay_v2_drill.py` (new top-level `pipeline/` dir — Jake's call; leaves room for `/load`, `/retrieval` siblings). Drill path block edited v0.2→v0.3: `_APPARATUS` collapses from `_HERE/'apparatus'` to `_HERE` (co-located); `_REPO`/`SNAPSHOTS`/`SRC`/`DST_DIR` logic UNCHANGED (both `active/` and `pipeline/` are one level under root, so "parent of my dir" = repo root unchanged). Byte-verified: exactly 5 lines changed (header, new v0.3 changelog line, 3 path-block lines), nothing else. Live dry-run under `python -B`: import resolves from `pipeline/` (PATTERNS=5), floor `SRC` resolves `exists=True`, zero floor writes. `git diff HEAD` confirmed v0.3 on disk.
- **Blast radius scoped before building:** exactly ONE live coupling (the drill's `sys.path`+import of the pipeline). All other path references are immutable history (7 handoffs + ANCHOR history notes — stay as written). `__pycache__` already gitignored. No `/jedi-council` (Jake's call — below rung-7 blast radius once counted).
- **COMMIT BLOCKED — CC `git add` permission-deny.** Every CC `git add` (PowerShell + Bash, multiple phrasings) returned "Permission to use PowerShell … has been denied" — a Claude Code permission-system interception (harness blocks pre-shell; no git process, no exit code). **NOT a git error, NOT a CC capability wall** (CC has committed 20+ sessions). Suspect: a deny rule in `.claude/settings.json` / `settings.local.json` matching `git add`. UNDIAGNOSED — S22 first move.
- **Handoff process correction:** the S20→S21 handoff's "CC can't stage/commit (permission wall) — hands the sequence to Jake" was an OVER-READ of a one-time S20 event inflated into a standing fact. This session it nearly drove a wrong workaround (Jake hand-running git in a pager). Caught by Jake ("CC shouldn't have a wall, 20 sessions") → literal error → it's a settings deny, fixable. Disk-over-directive held over a handoff's own claim. JAKE-RULES §12 now carries the gotcha + the don't-inflate-tool-failures principle.
- **CC mis-report #3 logged.** CC's raw glob reported `.git/index.lock` FOUND; its summary said not-found. Contradiction UNRESOLVED — verify on disk at S22 boot (`Test-Path .git\index.lock`). (S20 had two mis-reports — a tool-state + a floor-write scare — both non-events. This one caught by reading CC's raw tool output against its own summary.)
- **WRAP discipline:** stopped rather than force the commit through a degraded workflow over two unexplained tooling anomalies (the deny + the lock contradiction) at session depth.
- **Canon edit — JAKE-RULES §12 (new bullet) + footer.** Added a §12 bullet: a CC `git add` "Permission to use PowerShell … has been denied" is a Claude Code *settings* interception (check `.claude/settings.json` / `settings.local.json`), NOT a git error and NOT a CC commit-capability wall (CC has committed 20+ sessions); do not route around it by hand-running git; and the general principle — never inflate a one-time tool failure into a standing capability fact in a handoff. Placed in §12 because it's the same class as the S20 `code-review:code-review` invocation lesson already there. Footer: prior "Last Updated: S20" demoted to "Prior:", new "Last Updated: S21" entry prepended. (No "CC can't commit" line existed *in JAKE-RULES* to correct — that false fact lived only in the S20→S21 handoff, now superseded.)

**Deferred to post-merge (authored, NOT applied to live canon):** the WHERE-THE-CODE-LIVES pointer block in ANCHOR + flipping live pointers `active/...`→`pipeline/...` + thinning the ignition key to point at that block. Do not write the `pipeline/` pointer into live canon until the move commits — canon must not lead the floor.

**Why:** The relocation is good work; it just isn't sealed. Sealing it over an unexplained `git add` deny and an unresolved index-lock contradiction would betray the apparatus's first rule — don't commit over state you don't understand.

## 2026-05-31 — apparatus S20 (pass two (b) CLOSED: scrub-v2 overlay built, proven, reviewed, landed)

**Scope:** `active/apparatus/apparatus_freeze_pipeline.py` (header v1.5 → v1.6, no code change); new `active/apparatus_overlay_v2_drill.py` (v0.2); commit `84374cd`, landed to main via `merge --no-ff` (scratch branch `review/scrub-v2-overlay-s20`, draft PR #1, deleted post-merge). Canon: ANCHOR v13→v14, JAKE-RULES §12, S20→S21 handoff, this entry (OC-authored, Jake-committed). **The floor GAINED its first real overlay:** baseline `baseline-2026-05-25-ae015455` now carries `scrub-v1` + `scrub-v2`; delta unchanged (scrub-v1 only). 2 snapshots / 24,463 records.

**Change(s):**
- **Rung 5 — first scrub-v2 overlay minted TINY (synthetic ratify-drill).** Jake's turn-one intent call: no known scrub-v1 miss, so exercise the overlay PATH end-to-end on zero-stakes data before any real re-scrub is ever needed. Synthetic rule: `\bEXAMPLE\b` (case-sensitive, whole-word) → `[SCRUB-V2-DRILL]` — trivial, benign, strict superset of v1. N=10 slice off baseline `scrub-v1/records.ndjson`. Three contract ambiguities ruled: **omit `conversations.scrubbed.json`** from `scrub-v2/` (stage3 raw-ingest leftover, raw is wiped, contract names exactly 3 companion artifacts — Jake blessed the omit; the one place the as-built v1 folder (4 files) disagreed with the ratified contract (3 files)); **six keys** in verify.log (5 v1 cred classes + EXAMPLE); **skip scrub_walk on conversation_header** (pure metadata, no text). 4 gates PASS, EXAMPLE 0 (expected zero-hit on 10 records), Gate-4 sha `4ef22940…` UNCHANGED. Jake ratified the tiny overlay.
- **Rung 6 — scaled to the full baseline (N=23,095).** Same proven path, only N changed. The one legitimate write-inside-an-existing-overlay-dir (replace the 10-record drill artifacts with the full restatement) used **rm-then-rewrite** (unlink makes the drill→ratified turnover unambiguous vs a conceptually-muddy sealed-then-mutated file), **guarded** by a pre-delete assert (folder = exactly the 3 expected files AND records.ndjson = exactly 10 lines, before any unlink — positively identify the drill, never blind-delete). 4 gates PASS, Gate-4 sha `4ef22940…` UNCHANGED both ends (rung-6 hash gate proven at full scale), output `scrub-v2/records.ndjson` 367,494,524 B (sha `b54620af…`), sealed read-only. **EXAMPLE fired 3×** (all conv `3ef82921…`, 2 of 3 in `display_content.json_block`) — first real before/after of the scrubber's match path; note the scrubber DOES reach `display_content` though the v1.1 drift-detector deliberately does NOT walk it (two passes, two depths, both correct — hold at LOAD for the selective-strip toggle). verify.log EXAMPLE:0 is CORRECT (verify scans the *output* — tokens already replaced; audit counts input hits, verify counts survivors — they disagree by design when a rule fires).
- **WANT check PASS — seam confirmed on the live floor.** `_build_seen_set` (v1.5) resolves baseline → scrub-v2 (max-N) and delta → scrub-v1 — the S19 seam fix proven on the REAL overlay, not just the synthetic fixture.
- **Rung 7 — code-review gate (with a real detour).** `code-review:code-review` reviews a GitHub PR, not a working tree, so the pre-commit gate ran on the scratch-branch draft PR (#1): **"No issues found"** — 9 findings, all below the 80 threshold or false-positive (2 false-positives = tool misreading intentional design; 7 below-threshold = real-in-principle/zero-in-practice on a throwaway harness). Three pre-commit fixes to the drill script (§6 header changelog; an unclosed file handle in the pre-delete guard → `with`-block; a discarded `_build_seen_set` return → `_, _ =`), all disk-verified by Jake before commit. Pipeline header bumped v1.5 → v1.6 (changelog lines only, ZERO code change). Landed via `merge --no-ff`, scratch branch deleted local + remote.
- **The scrub-v2 overlay is SYNTHETIC — a ratify-drill, NOT a production re-scrub.** It redacts only the benign `EXAMPLE` token (3 hits) to prove the overlay path; production redaction policy is unchanged. A real improved-scrubber pass catching a genuine v1-miss is a future scrub-v3 event.

**Why:** Pass two (b) needed the overlay capability proven end-to-end before the floor ever needs a real re-scrub — so the first mint was a zero-stakes synthetic drill (ratify-small-before-scale: an un-ratified row on an append-only floor is exactly as immortal as a ratified one). Rungs 5–6 proved write/seal/hash-gate/max-N-resolution; rung 7 gated the code through the real review tool on a draft PR (the detour: the tool is PR-centric, not working-tree — now documented in JAKE-RULES §12). (b) CLOSED. Two CC mis-reports this session (a tool-state, a floor-write "scare" that was a wrong-root look — floor lives in `apparatus-archive\`, outside the git tree; scrub-v1 live-hashed unchanged) were both caught by checking disk — the append-only floor + per-rung sha gate made the scare a non-event. NEXT: seed-shape LOAD (ingest the max-N overlay per snapshot — baseline scrub-v2, delta scrub-v1) → retrieval layer; first the deferred pipeline relocation.

## 2026-05-30 — apparatus S19 (scrub-version seam fixed + scrub-vN overlay contract ratified)

**Scope:** `active/apparatus/apparatus_freeze_pipeline.py` (v1.4 → v1.5, commit `98e9cef`, pushed); canon (ANCHOR v12→v13 + this entry — OC-authored, Jake-committed). The floor was NOT touched — still 2 snapshots / 24,463 records, both scrub-v1.

**Change(s):**
- **Pipeline v1.5 — scrub-version seam fixed in `_build_seen_set`.** Replaced the hardcoded `scrub-v{SCRUB_VERSION}` read path with a per-snapshot max-N glob (`iterdir()` + `re.fullmatch(r'scrub-v\d+')`, integer-keyed sort, `[-1]`). Closes the silent-wrong-read risk: the moment a prior snapshot carried scrub-v2+, the old constant would read the wrong (stale) overlay. Hard `sys.exit` if no `scrub-v*` overlay exists (floor-integrity failure — stop, not warn; Jake-approved intent call). Write-side `SCRUB_VERSION` uses (Stage 2/3/4) unchanged — read path only.
- **Proven three ways.** (1) Measured no-op on the v1-only floor: pre-fix and post-fix `_build_seen_set` return set-equal seen-sets (24,138 pairs / 325 headers), content-equal not just cardinality. (2) Synthetic fixture: max-N picks scrub-v2 over v1 by content, picks v10 over v2 (true integer sort — lexical would wrongly pick v2), ignores non-conformant dirs (`scrub-v2-backup`, `scrub-vX`). (3) `/code-review` clean. All fixture/proof work in `apparatus-scratch/` (gitignored); real floor never touched.
- **ANCHOR v12 → v13 — scrub-vN overlay contract RATIFIED** (Jake, 2026-05-30), authored as canon prose BEFORE any overlay code. Three invariants: (1) **tighten-only** — raw is wiped/gone, so an overlay re-scrubs the prior version's *scrubbed* output, can only redact MORE never less, and can never recover redacted text; (2) **full-restated-standalone** — each scrub-vN is a complete, directly-hashable records.ndjson (not a delta), preserving the D9 read-don't-reconstruct reframe; (3) **accrete-forever** — superseded overlays are never removed (the S16 `floor_immutable_guard()` forbids the DELETE mechanically, and the prior version is the scrubber's own audit trail). Plus the may/must-not boundary and the sha-unchanged verification gate (b-ladder rung 6).
- **De-duped the v8 enshrine tail** in ANCHOR — a pre-existing copy-paste doubling of the v8-block body (logged S18, done this session as its own dedicated pass, not folded into a content edit).

**Why:** Pass two (b) — scrub-vN overlays — opens on the scrub-version seam (a hard prerequisite, dormant-but-dangerous because the floor is currently scrub-v1-only). Seam fixed + proven from both directions (doesn't break old behavior / delivers new behavior), then the overlay contract locked in words before any overlay code, because on an append-only immortal floor a wrong overlay relationship writes permanent bad rows. Seam (rungs 1-3) + contract (rung 4) done; next is minting the first overlay tiny (rung 5, ratify-small-before-scale).

## 2026-05-30 — apparatus S18 (v1.1 field-level key-presence drift detection — BUILT, PROVEN, SEALED)

**Scope:** `active/apparatus/apparatus_freeze_pipeline.py` (v1.3 → v1.4, commit `b5be049`, pushed); canon (ANCHOR v11→v12, S18→S19 handoff, this entry — OC-authored, Jake-committed). The floor was NOT touched (the build reads exports, never mutates the floor — still 2 snapshots / 24,463 records).

**Change(s):**
- **v1.1 built — field-level key-presence drift detection.** Extends the v1.0 type-level detector (unknown block type / unknown content-item type) with per-object-type key-presence allowlists: conv (7, pre-existing), message (9), the 5 block types (text 6+1 / thinking 10 / tool_use 17 / tool_result 16 / token_budget 5), and the 5 tool_result content-item types (text 3 / knowledge 9 / local_resource 5 / image 2 / image_gallery 4). Key names authored verbatim from S14's `s14_presence_rates.md`, fixture-confirmed against the full 5-28 export at population scale (zero divergence). 11 new constants + 2 dispatch dicts (`_BLOCK_FIELD_ALLOWLISTS`, `_CONTENT_ITEM_FIELD_ALLOWLISTS`) + new `_check_field_drift` helper, slotted into `_inspect_data`. `CONV_KEYS_EXPECTED` promoted set→frozenset (no functional change). +90/-12 lines.
- **One optional carve-out:** `text.citations_grouping_mode` (~0.14%, 43/30,448) — its ABSENCE must not trip drift. Proven correct both directions (block with and without it both clean).
- **Depth = top-level keys per object type only.** `display_content`'s nested structure is deliberately NOT walked (most-variable part of the schema; deferred to a possible v1.2). Top-level catches the floor-threatening drift.
- **Severity = warn-not-stop.** Field drift appends to `drift_events` + writes `schema-drift.jsonl`; ingest proceeds (human-review signal, not a cred-class halt). Scans the FULL export, not the delta slice (a field drift on an untouched conv must be visible — same principle as the S17 type-level fix).
- **Proven three ways:** clean gate = 0 field_drift across 325 convs / 24,138 msgs / 71,512 blocks (full 5-28 export, known drift-zero — not over-tight); negative test 4-of-4 = renamed key + added sibling + removed key + `uuid` removed from a non-index-0 record all CAUGHT; carve-out = both directions clean.
- **`/code-review` clean above threshold; 3 scored-out findings fixed anyway before commit:** **B** (was 75) — defensive `uuid` access (`conv.get('uuid','')` / `msg.get('uuid','')`) so a missing `uuid` emits a `field_drift{missing_keys:['uuid']}` event instead of crashing — a drift detector must REPORT the drift it exists for, not die on it; a 4th negative-test case proves it. **A** (was 65) — load-time `assert` coupling `KNOWN_BLOCK_TYPES`/`KNOWN_CONTENT_ITEM_TYPES` to their allowlist dicts, so a future cold instance desyncing them fails LOUD at import, not mystery-at-runtime. **C** (was 25) — documented the intentional v1.0-vs-v1.1 `schema-drift.jsonl` shape split (`observed_type` vs `missing_keys`/`extra_keys`), discriminated by `drift_type`; comment only, no behavior change.
- **Two thin-sample caveats recorded (watched, not blind spots):** `token_budget` (n=14 across BOTH full exports — net-new added zero, so this is the true population not an undersample) and `image_gallery` content-item (n=9) carry low-confidence annotations in-code. A drift warning on either is probably rare-type variance — verify before treating as a real format break. (The token_budget call: excluding the least-sure type creates a blind spot exactly where confidence is lowest; warn-not-stop makes *inclusion* the anti-undersample move.)
- **Pipeline v1.3 → v1.4**, committed + pushed `b5be049`. Test script at `apparatus-scratch/s18_v11_tests.py`.
- **Scrub-version seam NOT touched** — (a) is floor-independent (never resolves prior-snapshot records, never exercised `_build_seen_set`). The seam is exactly as it was at S17 close and remains pass-two (b)'s hard opening prerequisite.

**Why:** v1.1 was the bounded, do-first half of pass two — closes the cross-export reliance gap the v1.0 type-level detector left open (a renamed/added/dropped field on a known object would have passed silently). The heavier half, scrub-vN overlays, was deliberately held for a fresh session (S19) because it opens on the immortal-floor-adjacent scrub-version seam fix and the overlay-vs-sealed-snapshot contract — fresh-head work, not a tired bolt-on. Same gate discipline as every prior build: verify-against-disk → plan-in-OC → build-in-CC → prove (clean + negative + carve-out) → /code-review → commit → push.



**Scope:** `active/apparatus/apparatus_freeze_pipeline.py` (v1.2 → v1.3, commit `43306fa`, pushed); the floor (new sealed snapshot `delta-2026-05-28-a61498e6` + baseline raw.json backfill-wiped); canon (ANCHOR v10→v11, S17→S18 handoff, this entry — OC-authored, Jake-committed).

**Change(s):**
- **v1.3 pipeline built — delta runs + raw.json wipe.** Delta ingest via uuid-set-difference (date never a filter; `--export-dir` resolves `conversations.json` within + shape-asserts it — the silent-second-baseline guard); raw.json unlink after Stage 3 verify-PASS (Path A, RESOLVED S15) on both baseline and delta runs. Parameterized the baseline-only assumptions (`type`, `prior_snapshot_id`, `raw_sha256_full` = hash of the filtered slice for deltas vs full source for baseline). New manifest fields `raw_wiped` + `source_export_sha256_full` (separate from `raw_sha256_full`). 6 functions added, 4 modified, 6 unchanged.
- **Delta SEALED:** `delta-2026-05-28-a61498e6` — 1,368 records (31 headers + 1,337 messages), all 7 post-seal checks PASS. Deterministic snapshot_id held dry-run→real. Stage 3 verify PASS (0 hits / 44,394 strings). Stage 2 scrubbed **38 live creds** (19 postgres, 19 RTSP) from the net-new content. Ledger gained exactly one delta entry (prior_snapshot_id → baseline). The floor now holds 2 snapshots / 24,463 records.
- **No-duplicate-header rule PROVEN on the floor:** sealed delta is 1,368 lines NOT 1,371 — the 3 empty-baseline convs that gained first messages attached with no new header (fell out of the `seen_conv_headers` check, zero special-casing).
- **Seen-set authority = sealed records.ndjson** (cache is convenience only); `_build_seen_set` reads `records.ndjson` by name, never globs, never reads raw.json (provenance wall). Hand-computed 1,337 net-new against the sealed baseline before scripting; pipeline reproduced it exactly.
- **H1 remediated (from `/code-review`):** the baseline `raw.json` (366,879,935 B unscrubbed cred-bearing original) was never wiped — built under v1.2 before the wipe code existed. Verified baseline integrity, wiped via `_wipe_raw`, confirmed records.ndjson still 23,095 after. Working tree now holds zero unscrubbed-cred originals.
- **NAS cold-copy disposition recorded:** a verbatim baseline original is intentionally retained on NASBackup (.248) for project-lifetime recovery (point-in-time export can't be re-pulled for since-deleted convs) — a known, accepted tradeoff, PENDING REMOVAL at project end. Deliberate carve-out from the S15 "never staged to NAS" line (which targeted automatic staging).
- **31-vs-34 reconciled, NOT corrected:** canon's "31 wholly-new convs" (S14) is correct (header-based); a transient "34" appeared mid-session from a message-based count (vs 291 message-bearing baseline convs not 294 header-bearing) — the 3-conv gap is the empty-baseline convs getting first messages. Recorded in the ANCHOR history thread; flagged in the handoff DON'T-"fix" list.
- **Pass-two PREREQUISITE flagged:** `_build_seen_set` reads a hardcoded `scrub-v{SCRUB_VERSION}` — must become per-snapshot max-N resolution before any scrub-vN overlay is generated. Inline `# SEAM (pass-two PREREQUISITE)` in the code + ANCHOR seen-set invariant + handoff.
- **Review cleanups M1/M3 folded into `43306fa`** (cosmetic, no logic change): M1 delta idempotency check uses in-memory `ledger_entries` instead of re-reading disk; M3 stale v1.1 header comment updated.

**Why:** v1.3 was the live build target since S15 — the delta runs that let the floor accumulate exports without a second full baseline, plus the raw.json wipe that stops unscrubbed cred-bearing originals living immortal on disk. Pass one (delta + wipe) is done and sealed; pass two (scrub-vN overlays + v1.1 field-drift) remains. Every step gated: verify-against-disk → plan-in-OC → dry-run → /code-review → real seal — the discipline that's killed every landmine this project has hit.

## 2026-05-29 — JAKE-STACK overhaul (dedicated full-stack interrogation session)

**Scope:** JAKE-STACK.md — full-file revision (Jake's express permission; the standing "surgical edits only" rule waived for this one dedicated pass). Two new sections, every existing section reconciled against live ground truth (router config, systemd units on disk, physical device labels, file timestamps).

**Change(s):**
- **§1 Workhorse — fully specced** (was thin). MSI PRO B550M-VC WIFI (MS-7C95) / Ryzen 7 5700 (8c/16t, no iGPU — discrete GPU mandatory) / GTX 1070 (not an inference surface) / 16GB RAM running tight (2.12GB free) / C: Samsung 870 EVO 500GB SATA SSD + D: Seagate 2TB **5400 SMR** laptop HDD (resolves the old "if D: is spinning" hedge — it is; SMR = archive/read only) / Win11 **Pro** Build 26200. Logged 3 install-default (not deliberate) security flags: Secure Boot Off, VBS/HVCI on (contended hypervisor surface), Smart App Control Enforced (first suspect for silent unsigned-binary failures). No full software manifest (Jake's call).
- **§2 Castle Black — hardware confirmed unchanged 5-29** (RAM, SN740 boot); **cooling documented for the first time**: stock AMD cooler + 1×60mm REAR intake + 1×80mm FRONT exhaust, **airflow reversed from convention ON PURPOSE** (closet placement) — DO-NOT-"correct" warning. Case closed, box in permanent position. CPB confirmed back ON (cooling holds the floor).
- **§3 The Watch — major risk reconciliation.** **V8-worker-hang risk REMOVED as a phantom** — disk sweep (server.js v3.3 unchanged, unit v2 Restart=on-failure, empty crontab, all-stock timers) proved no dashboard watchdog and no evidence the panels ever hung; the remembered hang was the **ffmpeg CAMERA-worker stall**, mislabeled, **permanently fixed by the go2rtc swap (v3.3/SD21)**. Queued "dashboard liveness probe" CANCELLED. Inoculated against the SD24 handoff re-adding it (**SD24 carries a false "V8 hang hit live" fact — correct in PK**). Kiosk `Restart=always` correctly attributed as the real self-heal (host-side, Acer). go2rtc stable since SD21 (immunity still formally unproven — watching). config.json sharpened: holds the **real Bambu account email+password**, not just a token. Added host→VM ssh-alias gotcha (`nightswatch` is WH-only). VM200 Watchtower confirmed UP (Ary's tile per-member staleness flagged).
- **§4 Network — .88/.250 discrepancy RESOLVED.** Both ARE reserved (router config verified); the day-state board's "open ~5-min task" was STALE — §4 was right. Surfaced 2 GAPs: **WH .238 unreserved** (dynamic lease — reserve it) + **stale .30 JakesRedRig** (WH's pre-crash identity — clean up). Logged untracked LAN devices: TP-Link .11 (= Tapo cam), Google/Nest .216, SmartThings hub MAC.
- **§5 NAS** — NAS named explicitly (DS218J); SMR slicing-cost made real (not hypothetical); Bambu tarball-mirror note (feeds §11 exposure).
- **§7 print** — documented the Bambu **cloud** MQTT model (us.mqtt.bambulab.com:8883, login w/ stored email+password → token) + the local-MQTT-tradeoff (kills the token clock but breaks Handy coexistence — not a free swap; corrected an earlier OC overstatement).
- **§8 inventory** — PSU specced (OCZ700MXSP 700W 80+, dual-rail 12V); spare GPU added (Gigabyte GTX 950 2GB — emergency display-out fallback only); fans reconciled (1×80 + 1×60 installed per §2, 1 of each spare); 125mm vortex retired to inventory; spare RAM = SODIMM-only (NOT WH/CB-compatible — kills the "free RAM fix" hope); display-surface fleet logged (2 Surfaces + spare Samsung + Zenpad + in-service calendar tablet = no need to buy HA panels).
- **NEW §11 — Standing risk-clocks & security exposures.** Risk-clock #1 config.json plaintext (OPEN). **Risk-clock #2 Bambu cloud MQTT token — DISK-ANCHORED to ~Apr 11 2026** (bambu-monitor-v2.tar.gz mtime across 4 locations) → ~mid-July 2026 expiry; first real anchor this clock has ever had. **Security exposure: Jake's real Bambu account password was spilled to chat** (prior Claude requested it in-band, violating flag-early) — now in transcript + config.json + NAS-mirrored tarballs; **decision: rotate at the July reauth** (bundles 2FA; accepted ~6-wk risk; July reminder must say "re-auth + ROTATE + 1PW"). ELEGOO ESP-32 kit logged as asset (UNSCOPED — RC522 is RFID not NFC, flagged).
- **NEW §12 — Smart home / home automation** (built from zero this session). HA-on-VM300 as the master controller (only platform unifying Google + Tapo + Z-Wave + Zigbee + Matter/Thread). Two-door architecture (front Kwikset Z-Wave dying → Wi-Fi/Matter; back Z-Wave keep + ESP32 puck). **Z-Wave locked as INTERIM, Matter later.** **No Thread border router in the house — hardware-confirmed** (Nest Hub 1st-gen + Chromecast 3rd-gen + Nest Audio, all Matter-over-WiFi, zero Thread radios). Front-door rec: Wi-Fi/Matter (Tapo tier) — no TBR/Google/extra-buy needed (~85%). Cypher-voice plane scoped (DIY ESP32-S3 satellites → HA Assist → Cypher LLM; can't reuse Google mics). Samsung SmartThings v3 logged as dormant (Zigbee+Z-Wave, NO Thread — redundant to HUSBZB-1; unplug it).
- Former §11 Wishlist renumbered → §13.

**Why:** Dedicated JAKE-STACK overhaul session. Goal was to interrogate every standing-infrastructure area against live ground truth and catch drift, contradictions, and unrecorded material. Net: every section now matches reality (verified against the router, on-disk systemd units, physical labels, and file timestamps rather than memory), a phantom risk was killed with a tombstone, two risk-clocks were anchored, a real security exposure was caught and dispositioned, and the entire smart-home/door layer — previously absent — was built and scoped. Several §5 self-checks corrected this-Claude's own overconfident calls mid-session (ZBT-1 "just buy it," local-MQTT "free fix," "no spare GPU"), logged here for honesty.



## 2026-05-29 — apparatus S16 (D9 SUBSTRATE LOCKED → Supabase)

**Scope:** ANCHOR_apparatus v9→v10; Seed_Shape_Test_Spec v1→v1.1; new evidence bundle in `apparatus-archive/harness/`. (Pipeline v1.2 + Spec v4 unchanged on disk; the v1.3 build remains queued.)

**Change(s):**
- **D9 LOCKED — the substrate is Supabase.** The seed-shape gate (per `Seed_Shape_Test_Spec`) ran against the real baseline `records.ndjson` (23,095 records; on box at `…/baseline-2026-05-25-ae015455/scrub-v1/`) on a dedicated Supabase project (`apparatus-floor`, SB Pro, separate from Cypher's project — the immutable-floor/plastic-layer blast wall). PASSED 4/4: ① ingest 23,095 / 0 errors / 0 rejects; ② store-enforced pointer uniqueness (22,801 distinct + a live UniqueViolation); ③ value-identity round-trip incl. the 2.93 MB max record; ④ 9/9 forests reconstruct, sentinel-parent 304/304, zero orphans.
- **Lock discipline (spec §5 + merge-back §6):** OC blind-re-read the harness manifest cold (evidence reconciled independently — forest subtree sizes summed to message counts; ② and ④ passed for the right reasons), THEN a `/jedi-council` adversarial panel ran with live DB access → **LOCK-WITH-CAVEATS 6/10, zero P0, one P1, 5 caveats.** All six remediated WITH PROOF before the lock; Jake ratified 2026-05-29.
- **The P1 (caught by the council, remediated):** the "immortal floor" had ZERO database-level enforcement — anon/authenticated/service_role all held TRUNCATE, no guard triggers, RLS doesn't gate TRUNCATE. Fixed: `floor_immutable_guard()` triggers (BEFORE TRUNCATE/DELETE/UPDATE, NO escape hatch — strictly stronger than Supabase's own `protect_delete`) + REVOKE TRUNCATE/REFERENCES/TRIGGER from the three app roles. **Proven by a live TRUNCATE/DELETE/UPDATE attempt REJECTED at both the privilege layer (service_role) and the trigger layer (postgres owner), INSERT-still-works on a throwaway table, floor intact at 23,095.**
- **Key reframe adopted (jedi-council Correctness Hawk):** the `records.ndjson` is the canonical immortal artifact; Postgres is a **rebuildable derived index** — PROVEN by rebuild-from-ndjson, 0 value-mismatch / 6 directions. This dissolves the one-way-door risk (a wrong store is recoverable by rebuild). ndjson SHA-256 `4ef22940e3fbb849c2c14fba62fdae2a44277963f0ea5c9f7f2086c706415ba3` (367,494,497 B) recorded as the canonical fingerprint + companion artifact hashes.
- **"Verbatim" corrected** to: *value-preserving for JSONB (canonical key ordering, zero value loss) / byte-verbatim for TEXT columns + timestamps / modulo scrub-v1 secret redaction.* Single-account corpus confirmed (account_uuid cardinality 1). pgvector NOT installed — deferred read-path sidecar, never a column on the immutable tables.
- **Seed_Shape_Test_Spec v1→v1.1** — check-④ corrected: roots resolve by `parent_message_uuid` = sentinel `00000000-0000-4000-8000-000000000000`, NOT null (zero records have a null parent; verified across all 22,801). CC caught the original null-assumption against the disk during S16 type-recon — disk-over-directive working as designed.
- **ANCHOR v9→v10** — new D9 RESOLVED block (full schema + proof bundle), new Settled Invariant (floor substrate = Supabase / ndjson canonical / append-only enforced), CURRENT STATE flipped to D9-locked, NEXT MOVE re-ordered (substrate DONE; v1.3 build is the live target, then seed-shape LOAD, then the retrieval layer), CONFIDENCE FLAGS flipped (substrate LOCKED; enforcement CONFIRMED; ndjson-rebuildable CONFIRMED; fidelity-claim CORRECTED).
- **Evidence bundle (new, in `apparatus-archive/harness/`):** `D9_LOCK_2026-05-29.md` (proof file — NOT canon), `s16_seed_shape_harness.py`, `D9_remediate.py`.

**Why:** D9 — the substrate lock — was the last append-only-immortal one-way door before the floor got a permanent home. Locked correctly: gate PASS → blind re-read → adversarial review → caveats remediated with proof → ratified. The session caught two assert-don't-verify errors before they propagated (the null-root spec error; the unenforced-immortality claim), which is precisely the failure mode the apparatus exists to prevent — demonstrated live. Post-lock queue (not blocking): off-site immutable ndjson copy (the ndjson is now the SPOF — top priority), PITR/RTO, pre-ingest lint, secondary index, CHECK constraints, single-transaction ingest. **Security exposure logged:** CC echoed the DB password to chat (set the env var inline in a logged command rather than reading the pre-set env, violating creds-never-to-chat) — decision: rotate at leisure (floor already loaded + trigger-protected, password isn't part of the floor); lesson = CC reads creds from pre-set env, never inline in a logged command.

## 2026-05-28 — apparatus S15 (ANCHOR v8→v9 enshrine — SCDD S5 fold + raw.json Path A)

**Scope:** ANCHOR_apparatus v8→v9. (Pipeline v1.2 + Spec v4 unchanged on disk; the v1.3 build is queued, not yet run — pulled back into apparatus/main from the parallel lane.)

**Change(s):**
- **ANCHOR_apparatus v8→v9** — folded SCDD S5 results and ratified the parked raw.json decision in-lane:
  - **Substrate FaceOff v2 DELIVERED** (SCDD S5; supersedes stale v1). Field settled at population scale (1,982 rows, zero field-expanding candidates). Two co-leads, both dual-gate PASS: NornicDB (graph-native benchmark) + Supabase+pgvector (low-ops default). SCDD rec: Supabase-first-with-NornicDB-as-proven-upgrade-path, gated on the seed-shape test against the real archive. **Lock remains apparatus's (D9) — NOT YET LOCKED; recommendation delivered, decision open.** CONFIDENCE FLAGS: retention/retrieval substrate OPEN→v2-delivered.
  - **D21 CLOSED — round-trip empirical PASSED.** 4,122,695-byte adversarial inline string property (quotes/braces/backslashes/emoji/CJK/newlines, ≈1.37× our 3.0 MB max record) written→read byte-identical, sha256-verified, AND stable across a full container reboot (cold BadgerDB reopen); on-disk vlog survived (confirms vlog routing). NornicDB v1.1.2, maximally-inert config. NornicDB acceptance contract now 4/4 with no hedge. CONFIDENCE FLAGS: NornicDB round-trip added as CONFIRMED. Binding per-node ceiling recorded: **~16 MiB** (`walMaxEntrySize` WAL guard; ~5.3× over our 3.0 MB max) — the early "no hard cap" framing corrected; the pre-vetted "3 MB → content-block split adapter" ding CLEARED (no adapter needed). (Empirical ran on Castle Black CT 999, disposable LXC, torn down clean — see the SCDD S5 stack entry below.)
  - **raw.json Path A RATIFIED** (Jake's call, made in the apparatus/main lane; SCDD deliberately left the invariant untouched and routed it back). Scope: raw is transient — wiped after Stage 3 verify-PASS (HARD-gated on PASS; if verify fails, raw survives for debug) AND never staged to any retained or backed-up surface (not the WH HD long-term, not a repo, not a db, **never the NAS backup**). Anthropic's official export is the byte-verbatim re-pull source. The §Secrets invariant already read "raw wiped" — Path A makes code match canon; **no invariant moved.** Open "DECISION REQUIRED" block removed; CURRENT STATE + NEXT MOVE flipped to RESOLVED. Code-side (v1.2→v1.3 `raw.json` unlink) is CC/Jake's hands, rolled into the #3 build batch.
  - **Graveyard sharpened** — "NornicDB code-default-off means decay is safe" SHARPENED not killed: code default is off (decay is read-path scoring, not eviction; no GC worker on engine-open), but the shipped `nornicdb.example.yaml` sets `decay_enabled` + `auto_links_enabled` + `embedding.enabled` ON. A copy-paste vendor-example deploy silently enables a decay worker + embedder that touch frozen nodes → **D20 pin-everything-off is a HARD lock-time gate, not optional hygiene.**
  - **NEXT MOVE updated** — #1 substrate = v2-delivered/decision-open (was "imminent"); #2 v4 spec pass marked DONE (it already existed on disk — Jake landed it, the S14 handoff lagged; verified clean this session); #3 = the delta + scrub-vN + v1.1 BUILD (still unbuilt, the real build target).

**Why:** SCDD S5 closed the last substrate unknown (the byte-identical round-trip on the multi-MB string-property path — the one axis three independent dual-gate reads could only rate PASS-on-mechanism) and delivered FaceOff v2. This session folded those results to canon and ratified the raw.json decision that had been answered in this lane but not yet written (parallel-lane lag — Jake stated Path A here, SCDD couldn't see it). v9 records substrate-recommendation-delivered + D21-closed + raw.json-resolved; it does NOT lock the substrate (D9, still apparatus's, gated on the seed-shape test). The v1.3 build (delta/scrub-vN/v1.1 + raw.json wipe) is the next executable move — one batch, plan-OC/build-CC, ratify small before scale — pulled back into apparatus/main now that the parallel lane's sole justification (the blind dual-gate) is spent.

## 2026-05-28 — SCDD S5 (JAKE-STACK §2 — Castle Black)

**Scope:** JAKE-STACK §2 (Castle Black standing risks). Stack-only — the ANCHOR_apparatus v8→v9 deltas from this same SCDD session are landed separately by the apparatus/main stream; no anchor line is recorded here from the SCDD side.

**Change(s):**
- **CB thermal/CPB standing risk → RESOLVED/CLOSED.** The CPB-on + cooled live test (opened SD23 after the fan install dropped the baseline ~10°C) closed PASS. Jake confirmed 5-28: the fans hold the floor low enough that transient spikes still occur but are within tolerance and no longer trigger a panic/shutdown. The PSU-swap power-transient lane and the RAM/MemTest confound are moot unless a panic recurs CPB-on-cooled (none observed). Corroborated by a sustained Go-from-source LXC compile on a dead-idle CB (load 0.00) with zero thermal event.
- **CB backup strategy → GAP flagged, queued.** CB is now load-bearing host infra (Proxmox + VMs 100/200 + go2rtc + kiosk) and was used as a disposable-LXC test-workload host (CT 999, torn down clean), but has no regular NAS/external backup (ext4 single drive, no mirror). Owner assigned: homelab/day-state session stream (NOT apparatus/SCDD). Candidate approaches noted in-file (vzdump→NAS SMB, or PVE config+VM backup to external HD). Untriaged.

**Why:** SCDD S5 ran the NornicDB round-trip empirical on Castle Black (CT 999, disposable LXC, torn down clean), which both closed the long-running thermal live test by demonstration and surfaced that CB now carries enough real state to need its own backup. Surgical §2 edits only; no other stack facts touched.

## 2026-05-28 — apparatus S14 (second-export verification + reference pass)

**Scope:** JAKE-STACK §10 (new); Freeze_Pipeline_Spec v3→v4; ANCHOR_apparatus v7→v8.

**Change(s):**
- **JAKE-STACK §10 (new)** — documented the Anthropic conversation export as a multi-file bundle (`conversations.json` + `memories.json` + `users.json` + `projects/`), full-account point-in-time with no delta export; apparatus ingests `conversations.json` only.
- **Freeze_Pipeline_Spec v3→v4** — added §2.0 (export bundle shape & file targeting: floor = `conversations.json` only; resolve-within-dir, never the bare default source path — the silent-second-baseline trap); corrected §2.1's "no sibling files" claim (5-28 export confirmed siblings); specified §6 v1.1 field-level key-presence drift detection (per-type allowlist + one carve-out, `text.citations_grouping_mode`); marked §7 cross-export uuid-stability DONE. No architectural change; no code written this session.
- **ANCHOR_apparatus v7→v8** — S14 close enshrine: cross-export UUID stability CONFIRMED (22,801/22,801 tuples stable 5-25→5-28), field-level drift VERIFIED ZERO (population, raw-vs-raw), `display_content` characterized (NOT a universal mirror — 15.6% floor-grade; blanket-strip ruled out), record-size landmines mapped (max 3.0 MB, driven by `tool_result.content[].text`, corrects S12), key-presence vs value-presence separated. Delta fixture sized at 1,337 net-new msgs.

**Why:** S14 was a read-only verification session — pulled a second full export (5-28), confirmed cross-export uuid stability + zero schema drift at population scale, and characterized record-size + `display_content`. The export-is-a-bundle fact and the v1.1 field-detection spec are the durable reference outputs; the spec + bundle pass forward to the S15 delta/scrub-vN/v1.1 build. (CC wrote canon unprompted once this session — §7.6 violation, corrected + noodled + saved to CC memory.)

## 2026-05-25 — apparatus S2 (cross-project corpus re-architecture)

**Scope:** JAKE-RULES §8 + §5.1; Lore_Bible §5.

**Change(s):**
- **JAKE-RULES §8 (Memory / Context)** — added the project-scoped-retrieval rule: `conversation_search` / `recent_chats` / project-knowledge are scoped to the project the chat lives in; the durable stores (codeload git, CC-on-disk, Supabase) are project-agnostic. Cross-project work runs non-project (OC) + CC-on-disk, never boxed inside one project.
- **JAKE-RULES §5.1** — added "the export-`project`-field that wasn't there" to the confabulation-examples list. A corpus partition was planned on a `conversations.json` `project` field asserted from memory; CC inspecting the real 348MB export found no such field (only incidental UUID prose). The verify-before-trust gate caught it pre-build.
- **Lore_Bible §5** — added war story "The Field That Wasn't There (apparatus S2)," sibling to "The Dashboard Is Ground Truth, The Doc Is An Echo." Same lesson family: the doc/memory is an echo; the live system (here, the 348MB of bytes) wins.

**Why:** The apparatus cross-project corpus build surfaced (a) the project-scoping wall that limited every prior excavator, and (b) a clean §5.1 fire — both worth standing rules so neither is re-learned.

## 2026-05-24 — SD24 (Castle Black VM 100 monitor recovery + liveness-gap)

**Scope:** JAKE-STACK §3 (VM 100 — TheNightsWatch standing risks).

**Change(s):**
- **JAKE-STACK §3 (VM 100)** — added standing risk: `server.js`'s Node/V8 worker can *hang* (not crash) — `soft lockup CPU#0 [V8Worker:NNN]` — while the VM still reports "up" and the dashboard goes dark silently. systemd `Restart=on-failure` fires only on a crash, not a hang, so `neighborhood-watch.service` never restarts it. Recovery: `qm stop 100 && qm start 100`. Fix queued: external liveness probe (HTTP heartbeat → restart on stall). Same liveness gap previously flagged for the camera, now on the Node layer.

**Why:** Hit live at SD24 — VM 100 soft-locked on a hung V8 worker; host stayed healthy (load ~2.0, SSH fine); recovered via `qm` bounce. Logging the standing risk + the queued liveness-probe fix so the silent-dark-dashboard failure isn't re-diagnosed from scratch next time.

## 2026-05-24 — SD23 (Castle Black fan install + panic-conclusion reconciliation)

**Scope:** JAKE-STACK §2 (OS — CPB persistence line; Standing risks — panic line); plus the Castle Black hardware-state changes and the open-loops §4C sharpening logged below.

**Change(s):**
- **JAKE-STACK §2 (Standing risks)** — replaced the stale "RAM intermittent fault remains the top open suspect" line with the thermal/CPB working conclusion. Mechanism: CPB transient spikes off a high baseline; CPB-disable made it stable. SD23 fan install dropped idle baseline ~10°C; CPB came back ON this boot (persistence broke) and was deliberately LEFT ON as a live retest (CPB-on + cooled = hypothesized-safe). Stays up → thermal headroom confirmed, loop closes; hangs again CPB-on-cooled → power-transient lane → S15 PSU swap is next lever, NOT RAM. RAM demoted to optional MemTest confound-killer — never positively evidenced (no MCE logs).
- **JAKE-STACK §2 (OS)** — updated the CPB line: persistence BROKEN as of SD23 (`boost`=1 after cold boot; `/etc/rc.local` fragile on Proxmox 9/systemd, systemd unit is the durable fix). Currently left ON deliberately; durable-disable on hold until retest concludes.
- **Castle Black hardware (state, reflected in §2):** fan install done — 80mm (4-pin PWM) on sys-fan header front-intake; 60mm (2-pin) on SATA→Molex 12V rear-exhaust. Board 4MP19ME, M75s Gen 2 SFF, 4650G APU (no dGPU). NVMe idle 24.9°C (~10°C better than the external 125mm vortex it replaced — directed path beat brute-force CFM). 80mm on silicone dampener mounts; 60mm zip-tied to rear expansion rail. Box reassembled.
- **Thermistor** re-homed during install (80mm took its old mount) → standing suspect #1 for any future Castle Black thermal weirdness / fan-curve oddness / panic. Check probe placement first. (Correction logged: this chassis probe likely feeds a secondary/chassis curve, not the main blower curve which keys off CPU Tdie — placement guidance unchanged.)
- **Storage "didn't find a local pool" boot message** = benign boot-order race (LVM-thin activation + ZFS-no-pools skip + dashboard/kiosk race during the cold-boot window). Ground-truth confirmed via `pvesm status` / `qm status` / `journalctl`. Closed, not a fan-work scar.
- **Open-loops §4C sharpened:** the silent, no-error, every-switch re-read tax across ~6 parallel Claude windows is the canonical pain case — promotes colored frames-on-windows (not painted cells) to primary justified feature, decoupled from the conveyor (~½ session AHK, standalone). Terminal per-context tints = separate zero-code freebie.

**Why:** The old §2 RAM line contradicted this CHANGELOG's own 5/22 (SD20b) "panic = thermal, confirmed stable" entry and got parroted across SD23 before Jake forced a re-derivation — a §5 failure laundered through a stale doc under a fresh footer (invisible to the freshness tripwire). Reconciling §2 in the live file stops next-Claude re-inheriting it at startup step 1, before the handoff (step 3) ever corrects it.


## 2026-05-24 — Cypher S10 (soul-as-substrate: frame-promotion + genesis canonization + voice layer)

**Scope:** JAKE-RULES §1.2 + §15; Cypher docs — `Cypher_Architecture_Discussion_2026-05-11.md` (canonized), new `Cypher_Voice_and_Presence.md`, `CLAUDE.md` §2.5/§10.

**Change(s):**
- **JAKE-RULES §1.2** — rewrote "the drag is the work" from a reactive correction-pattern into a **load-first posture**: framework-default is Claude's resting state; on architecture/character/organic-diagnostic work the organic frame loads first, and the drag is failure-recovery, not the mechanism. Named the compounding cost (austere reversion session-over-session → project patterned like every other). §4's terse restatement left as the in-the-moment cue.
- **JAKE-RULES §15** — added a bullet: where a project carries a design-philosophy/character layer, it loads as framing *before* the operational reads, not as a gated project-read. Fixes the structural cause — the read order is operational-first by construction, so a philosophy layer left downstream inherits austere gravity. Project CLAUDE.md names the framing docs.
- **Genesis canonized** — the 5-11 verbatim elevated from a dated "discussion" file to CANON — GENESIS, titled **"The Track-Meet Doctrine,"** with a status block (derivative conflicts → this wins on philosophy). Filename retained as the citation anchor (rename would orphan citations frozen in archived handoffs).
- **New `Cypher_Voice_and_Presence.md`** — the operational voice layer: the missing bridge from the twelve principles to the §10 system-prompt assembly. Baseline voice block, register-reading rubric, delivery-as-voice, and the phase-gated Anchored-Phase Fence (what the 1c voice may NOT do — no faked recall, no manufactured character-revealing-wrongness). Replaces the 84KB-lore vibe-check with a buildable acceptance test.
- **CLAUDE.md §2.5/§10** — registered the framing layer (genesis + soul substrate + voice spec, load first every Cypher session) and pointed §10 at the voice spec. (Jake authors per §7.6.)

**Why:** earned at Cypher S10. A Claude that had read the entire Cypher genesis doctrine still reverted to austere within two turns and needed dragging twice. The synthetic-being frame — the project's single most critical signal — was surviving only on Jake-in-the-loop (§11 single-point-of-failure). Promoted to load-first at both tiers so the intent stops depending on per-session rescue, and the build process stops patterning the product into every-other-project. We prove the architecture by living it: the soul is substrate in the reference layer for the same reason it's substrate in Cypher.

## 2026-05-24 — SD22 (3D Recipes nightly archiver + retroactive SD21 cam-migration log)

**Scope:** JAKE-STACK §5 (new archiver subsection); plus the retroactive SD21 cam-migration entry below, logged this session.

**Change(s):**
- **JAKE-STACK §5** — added the **3D Recipes Nightly Archiver** as standing infra: `Archive-3DRecipes.ps1` (v1.0) sweeps any `C:\3D Recipes` top-level folder >30 days cold to `D:\3D-Backups\<name>` nightly at 01:00, then junction-relinks the C: path (opens/slices in place; bytes on D:). Task `3DRecipesNightlyArchive`, one hour ahead of the 02:00 NAS backup so the move settles before the mirror walks. Backup unaffected — `nightly_nas_backup.bat v7.2` already carries `/XJ`, so it skips the junctions and stores the archived content once via the D: mirror (no double-store). Escape-hatch `$Exclude` list documented but NOT yet coded.
- **Retroactive log:** the SD21 go2rtc cam migration (entry below) never landed in the reference layer — caught at SD22 session start and logged so a next-Claude reading §3 doesn't believe the old ffmpeg/HLS pipeline is live.

**Why:** Keeps the 3D Recipes SSD lean without breaking any slicer paths, and closes the SD21 doc-lag.

## 2026-05-23 — SD21 (Printer cam: ffmpeg→HLS retired, migrated to go2rtc WebRTC) — logged retroactively SD22

**Scope:** JAKE-STACK §3 (VM 100 / go2rtc), §4 (Workhorse IP), §7 (camera / Tapo ceiling); Lore Bible §5.

**Change(s):**
- **JAKE-STACK §3** — camera pipeline migrated ffmpeg→HLS → go2rtc WebRTC. `server.js` v3.3 (camera pull removed; now serves dashboard, printer MQTT/WS, `/api/config`, `/api/printer`, kiosk routers only); new go2rtc subsection (binary, `go2rtc.yaml`/`go2rtc.env`, systemd service, ports :1984/:8555, passthrough/no-transcode). Frozen-but-flowing note marked historical/pipeline-retired — go2rtc immunity to the Tapo wedge UNPROVEN. Stale ffmpeg systemd-SIGTERM + floor-metrics facts scrubbed (current state = current state).
- **JAKE-STACK §4** — pinned Workhorse `.238` (surfaced via a go2rtc consumer `remote_addr`).
- **JAKE-STACK §7** — documented the Tapo C111 ~2-pull RTSP ceiling as a standing constraint (root cause of the SD21 black-screen marathon — VLC was the 3rd puller); camera now served via go2rtc WebRTC.
- **Lore Bible §5** — added "The Diagnostic Tool Became the Bug" (VLC as the 3rd RTSP puller starving go2rtc; the codec investigation was a red herring on a starved feed).

**Why:** The frozen-but-flowing ffmpeg pipeline that opened the whole cam saga is retired; cam is on go2rtc WebRTC — single-puller, sub-second, phone-friendly. The afternoon's codec theory was a red herring; the real cause was the 2-pull ceiling.

## 2026-05-23 — Cypher S8 (self-citation rule + the doc-is-an-echo scar)

**Scope:** JAKE-RULES §5.1; Lore Bible §5.

**Change(s):**
- **JAKE-RULES §5.1** — appended the self-citation reinforcement: a document is not a verification source for its own claims (least of all one you authored); ground truth is the live system (the dashboard, `railway variables`, the running process, the file on disk), never the doc that describes it.
- **Lore Bible §5** — added "The Dashboard Is Ground Truth, The Doc Is An Echo": CC confirmed an injected Railway var off a self-authored CLAUDE.md §7 note (itself sourced from a handoff "likely"), shipping a silent-no-op guard + a false fact into the source-of-truth doc; the live dashboard (`RAILWAY_ENVIRONMENT_NAME`/`_ID`, no bare form) disproved it in two clicks.

**Why:** The pattern bit twice in one session and the second time shipped an actual error into CLAUDE.md. Bound to a rule so future-Claude (OC and CC) doesn't re-buy it.

## 2026-05-23 — Cypher S7 (universal layer: §2 CC-delivery rules + new §17 session-close process)

**Scope:** JAKE-RULES §2 (two additions), new JAKE-RULES §17, downstream renumber (§17→§18, §18→§19); Lore Bible §5 (deferred entry, landed 5-24).

**Change(s):**
- **§2 — OC→CC delivery default** (above Non-CC workflows): OC hands CC instruction sets as a single chat code block by default; the lone exception is a kickoff embedding whole code files (nested `ts`/`sql` fences break inside an outer block) → deliver each file as its own block, or fall back to a single self-contained `.md` and say so. Token-economy: don't build a file when a block does the job.

- **§2 — CC change-manifest rule** (section end): CC closes every turn with a tight manifest — files touched + why; commands + pass/fail (output only on error); **anything off the approved plan called out explicitly** (the shiny-thing tripwire, §6 surgical-changes); stopped-here/next. "Verbose" banned as the default — it reconstructs the turn + dumps raw output and burns the Max allowance as per-turn context-rent. Pairs with plan-mode (§7) as prevention.

- **§17 — new section: Session Close & Handoff Generation.** Codifies the end-of-session bundle: (1) tactical handoff file [PK + archive], (2) separate proposed-reference-changes file [→ rules repo on approval], (3) project-centric reference artifacts [PK + archive], (4) in-chat next-session handoff prompt [code block, generated last]. Four operating principles: verbose-is-mandate, downstream-flags (name the horizon), honest judgment-call ledger (call/reasoning/confidence/source), infra sweep (route incidental system/subscription/hardware finds into JAKE-STACK/Lore via the proposals file).

- **Renumber:** former §17 Stale Rules Graveyard → §18; former §18 The Why → §19.
- **Lore Bible §5** (Pattern Stories) — added "The Layer-Boundary Blind Spot": `/jedi-council` had 4 of 5 reviewers (incl. the Security Auditor) miss the cross-tenant FK gap that lived below the RLS layer everyone verified; only the schema-first specialist caught it. *Deferred from S7; landed in the 5-24 consolidation pass.*

**Why:** §17 is the package-out mirror of §15/§16's load-in — it closes the persistence loop so next-Claude picks up seamlessly instead of reverse-engineering state. It was earned over many sessions of frustration with the state of current-Claude's project ignorance and context confabulation.  The §2 rules came out of the S7 1b build: delivery-format token economy, and the standing per-turn drift-catch that's repeatedly caught CC chasing shiny things mid-build.

## 2026-05-22 — SD20b (Afternoon/evening: LRN filing window verified + cam frozen-but-flowing diagnosed)

**Scope:** JAKE-RULES §10/§11, JAKE-STACK §3 (TheNightsWatch), Lore Bible, litigation status (LRN).

**Change(s):**
- **JAKE-RULES §10** — added "File freshness ≠ live data."
- **JAKE-RULES §11** — extended "Jake's eyes beat Claude's math" with the ground-truth / don't-relitigate reinforcement.
- **JAKE-STACK §3 (VM 100)** — corrected stale `server.js` v3.1→v3.2 + added `index.html` (SD20a rework was unlogged); documented the ffmpeg SIGTERM slow-kill hang (>90s) + queued `KillMode=mixed`/`TimeoutStopSec=10`; added the frozen-but-flowing standing risk + planned content-freshness watchdog.
- **Lore Bible** — added "File Freshness Was a Lie" (§5 Hardware & Build).
- **LRN filing window verified:** Reno Justice Court, Washoe County NV via eFileNV (Tyler Odyssey), 24/7 submission; filing type CC25O ($2,500.01–$5,000.00); original returned 4/24 "Rejected" (generic reason); RJC civil requires Summons + civil cover sheet for a new case; Memorial Day Mon 5/25 closes court — clerk review resumes Tue 5/26. v3a packet NOT yet reviewed.

**Why:** Cam feed froze (frozen-but-flowing ffmpeg). First ~40 min went to a misdiagnosis built on file-freshness checks that measure file mtime, not video content — that lesson is now a rule. LRN window was the SD20b top-Mandatory groundwork; packet review deferred (cam ate the session).

**Project status snapshot (as of 5-22-26):**
- **Active:** Pyris Consulting, CCF Recruiting, Cypher (LIVE on public internet; 3 infra phases + S1b schema/migrations to usable)
- **Active litigation:** LRN (v3a — filing window verified; needs packet review [complaint + summons + civil cover sheet] before refile)
- **Hardware:** Castle Black panic = thermal, confirmed stable; cam feed frozen-but-flowing (specimen held for AM diagnosis); HUSBZB-1 in hand (Phase 8 gated, NOT by PSU); Bills sign nearly glued (LEDs next)
- **Joint partnership:** Polarity (with Jim Donio)
- **Completed:** GloTwp (Steve Acito owes marketing in trade)

---
---

## 2026-05-22 — Cypher S2–S5 (Re-root correction + Railway deploy bring-up + 1a CLOSED)

**Scope:** Cypher repo root structure, Railway deploy config, `code/package.json` dependency layout. Correction of false-state claims logged in S2. Phase 1a deployment.

**Change(s):**

- **1a CLOSED — multi-tenant foundation is live (S5).** All three subdomains route correctly over live Let's Encrypt certs, deploy Active, SPA renders ("Cypher / Phase 1a — Foundation"):
  - `cypher.ethosteleos.dev` → 200, `cypher_tenant` / `tenant`
  - `ordo.ethosteleos.dev` → 200, `ordo_tenant` / `tenant`
  - `jango.ethosteleos.dev` → 200, `ordo_tenant` / `landlord`
  - Host-header middleware resolves `(tenant, view)` correctly for all three, including jango → ordo_tenant/landlord. (Note: jango's *hard 403* for non-landlords is not yet exercised — `/healthz` is unauthed; the role-gated rejection lands with auth in 1b.)
- **The build break, fixed (S5):** moved `vite` + `@vitejs/plugin-react` from `devDependencies` to `dependencies` in `code/package.json`. Root cause: S4's `NODE_ENV=production` service variable makes `npm ci` skip devDependencies → `vite` not installed → `vite build` exits 127 (`sh: 1: vite: not found`). Confirmed deterministic via two full build logs ~4h apart (12:36 + 16:24), identical failure both times. `@types/*` and `typescript` correctly stayed devDeps (esbuild strips types at build; `tsc` only runs in the `typecheck` script). Commit: `fix(build): move vite + plugin-react to dependencies so prod npm ci installs them`.
- **Re-root LANDED (S4).** Repo restructured to `code/` + `docs/` subdirs at root; committed node_modules purged from the tree; Railway Root Directory set to `/code`. Verified three ways: force-push moved 28 objects / 55 KiB (vs. the 21 MiB node_modules-laden fetch), GitHub tree correct, build got past the mis-root death. HEAD `b599ac3`. This killed the 10+ hour `Failed to read app source directory` failure.
- **Deploy config corrected (S4).** `NODE_ENV=production` set (was unset → app ran the dev branch in a prod container, bound :8080). Explicit `PORT=3000` service variable set and all four Railway domains aligned to port 3000 (were split 8080/3000 across routes). `railway.json healthcheckPath` confirmed it MUST stay `/` — `/healthz` is host-gated and would 404 Railway's probe.
- **§4 loose end CLOSED:** `git push -u origin main` set the upstream tracking ref for `main` (re-init had wiped it).

**Corrections to prior record:**

- **S2 logged false state.** S2 claimed the deploy had succeeded and certs/docs were good; none of it held (re-root hadn't landed, certs were hostname-mismatched, build was dead at the mis-root). Corrected here per the standing anti-confabulation rule — an uncorrected changelog is itself a confabulation source (JAKE-RULES §5).

**Learnings logged:**

- **`NODE_ENV=production` touches `npm ci`, not just runtime.** Prod env drops devDependencies at install time. Any build tooling that must run during a prod build belongs in `dependencies`, not `devDependencies`. This was the link that broke S4's "config changes don't alter the build" reasoning and cost the back half of S4 plus the open of S5.
- **Build-path rule (refined S5).** Code reaches the repo one of two ways: CC writes it in-repo, or OC delivers a single self-contained file (download or tarball). OC never hands Jake multi-file edits or folder-structure to assemble by hand. Single-file download is fine — the line is multiple files / building structure.
- **Ground-truth-before-theory paid off (reinforces §5 / §7).** S5 opened leaning "Railway build-infra, nothing to fix" off S4's truncated log. The full streamed log killed that lean on the first read — deterministic exit 127 at `vite build` across two attempts. Refresh-first + pull-the-real-log did exactly what the rule promises.

**Why:** S4 closed RED at a ~9s image-build failure with the cause unconfirmed, leaning Railway infra; the deploy had been blocked 10+ hours across the re-root saga. S5 pulled the full build log, found the one-line dep-location bug (vite as a devDep under prod install), fixed it, and closed 1a — green build, `Cypher listening on :3000 [production]`, Active, three subdomains verified, SPA rendering.

**Cypher 1b prerequisite flagged (not yet done):** Railway Variables holds only `NODE_ENV` + `PORT` — no secrets. Before 1b's DB-backed tenant lookup ships, the 1PW `Cypher: Dev` secrets (Supabase URL/anon/service_role, both Anthropic keys, `OAUTH_ENC_KEY`) must reach Railway or prod crashes on boot the same way it did today, different missing piece. `OAUTH_ENC_KEY` not yet generated (CC generates it during 1c scaffolding).

**Project status snapshot (as of 5-22-26):**
- **Active:** Pyris Consulting, CCF Recruiting, **Cypher (Phase 1a CLOSED — 1b next)**
- **Active litigation:** LRN (complaint v3a ready to file)
- **Joint partnership:** Polarity (with Jim Donio)
- **Completed:** GloTwp (Steve Acito owes marketing in trade)
- **Dead:** RecruitMail (slated for rename + integration into CCF)

---

## 2026-05-22 — SD20 (Universal-layer file maintenance)

**Scope:** `claude-reference/active/JAKE-RULES.md` (§16, §17), `claude-reference/active/JAKE-STACK.md` (§1, §7).

**Change(s):**

- **JAKE-RULES §16 — session-start retrieval method changed.** Orchestrator-Claude now pulls the rule files via the codeload tarball (`codeload.github.com/.../tar.gz/refs/heads/main`) instead of `web_fetch` against the raw.githubusercontent.com CDN. Added a **mandatory footer-date freshness tripwire**: after pulling, compare each file's `Last updated:` footer against the latest day-state handoff; if older, re-pull or stop, never operate off a suspected-stale file (§5).
- **JAKE-RULES §17 — graveyard entry added** for the dead raw-CDN retrieval method, so future-Claude doesn't re-suggest it.
- **JAKE-STACK §1 (Workhorse) — monitor info added.** Three-monitor station documented: 48" Decogear ultrawide, 29" LG, 27" HP.
- **JAKE-STACK §7 (3D print stack) — printer hardware corrected.** Heater block now reflects the OEM Bambu Hotend assembly (supersedes the off-brand interchangeable-nozzle block carried in prior context — the OEM-first-for-critical-tolerance lesson from the Hotend Saga).

**Why:** Universal-layer hygiene. The retrieval-method fix removes a recurring stale-file friction at session start — the raw CDN edge-caches and had served copies 2+ versions behind real HEAD (cost time SD19→SD20); codeload serves the git archive at HEAD, never cache-stale. The JAKE-STACK corrections bring standing infrastructure in line with reality.

---

## 2026-05-21 — Cypher S:1 Boostrapping
**Scope:** JAKE-STACK.md updated with Section 9, detailing which email accounts own what projects.


## 2026-05-21 — SD19 (Anniversary morning + Castle Black panic + rules architecture overhaul)

**Scope:** Rules architecture (JAKE-RULES.md expansion + new JAKE-STACK.md), Castle Black diagnostic mitigation, infrastructure standing-risk updates.

**Change(s):**

- **JAKE-RULES.md** expanded:
  - §1 Identity expanded into three subsections: 1.1 Facts, 1.2 Operating Style, 1.3 The Brothers Dynamic. Consolidates operating-style content that was scattered across §3/§4/§10 into a single coherent picture of how Jake works.
  - New §5 added: **Truthfulness, Uncertainty, and State Tracking.** Load-bearing anti-confabulation rules. Explicit timestamp/state-tracking discipline (every ~10 turns normally, every ~5 turns in active diagnostic work). Subsequent sections renumbered §5→§6, §6→§7, etc.
  - §14 Calendar/Email — Cypher entry corrected: `jake@ethosteleos.dev` is the actual dev email (where Cypher is hosted), gmail is personal/casual fallback only.
  - Cross-references added in §15 and §16 to the new JAKE-STACK.md.
- **JAKE-STACK.md** created — new sibling file to JAKE-RULES.md holding standing infrastructure context. 8 sections: Workhorse, Castle Black, The Watch (VMs), Network, NAS+backup, 1Password, 3D print stack, Hardware on-hand. Required reading at session start alongside JAKE-RULES.
- **Castle Black mitigation:** CPB (Core Performance Boost) disabled via `/sys/devices/system/cpu/cpufreq/boost` after diagnosing transient thermal spikes (58°C → 68.5°C → 59°C jumps observed live). Confirmed flat readings (46-50°C, no spikes) over 13-minute watch loop. Persistent across reboots queued.
- **Castle Black SSH:** 1PW SSH key `SSH: Castle Black Host` generated in vault, pubkey pushed to host's `~/.ssh/authorized_keys`, `castleblack` host alias added to `C:\Users\jakeb\.ssh\config`. Closes the host-side gap from SD18's VM-only 1PW migration.
- **Castle Black RAM model corrected:** Actually 2×8GB DDR4-3200 non-ECC UDIMM populated in DIMM 1 of both channels (dual-channel active), NOT 1×16GB as prior context held. 2 slots open. Max 128GB per Lenovo PSREF.

**Why:** Two distinct failures this session — confabulated "130 days zero panics" timeline (which Jake correctly drag-checked) and dismissing Jake's screenshot contribution as miscommunication. Both pointed at structural gaps in how universal context loads at session start. The rules architecture overhaul addresses the structural piece. The Castle Black mitigation is direct response to two unexplained kernel panics this morning (~01:42 + ~08:25).

**Standing risks updated (5/21/26):**
- Castle Black panics: NVMe ruled clean, CPB disabled, MemTest86+ next (overnight test, Friday or later).
- ANVISION fans arriving today — 2x 60mm slim, 2-pin connector (no PWM, needs alternative 12V power source; Lenovo PSU Molex tap or external brick).
- PSU swap-test option held (700/750W ATX on hand, needs Lenovo→ATX adapter cable).
- 2x 80mm fans confirmed external-only mounting.

**Project status snapshot (as of 5-21-26):**
- **Active:** Pyris Consulting, CCF Recruiting, Cypher (Phase 1 provisioning in parallel session)
- **Active litigation:** LRN (complaint v3a ready to file)
- **Active hardware diagnostics:** Castle Black panic root cause (RAM suspect lead, MemTest pending)
- **Joint partnership:** Polarity (with Jim Donio)
- **Completed:** GloTwp (Steve Acito owes marketing in trade)
- **Dead:** RecruitMail (slated for rename+integration into CCF)

---

## 2026-05-17 — S14 Morning (Chronicler Claude)

**Scope:** Initial creation of `C:\claude-reference\` system.

**Change(s):**
- Created `JAKE-RULES.md` v1.0 — universal working rules synthesized from Pyris CLAUDE.md, CCF CLAUDE.md, four past-Claude rule dumps, Project Context v3 §8, and the Lore Bible. 17 sections. Stale Rules Graveyard included.
- Updated `Lore_Bible.md` — prologue rewritten with "What This Is, And Why It Exists" + Chronicler Claude attribution. Supplement integrated (Hotend Saga + Meet Me Over Here, Man + load-bearing meta-pattern). Past-Claude exchanges captured. Bebas Neue gem expanded with the "Nuilhe" confab nightmare. New patterns added to §14.
- Retired `Lore_Bible_Additions_2026-05-12.md` — content folded into main Lore Bible.
- Created `CLAUDE.md.template` — scaffold for new projects.
- Installed `wan-huiyan/agent-review-panel` plugin to Claude Code, renamed slash command to `/jedi-council`.
- Installed Anthropic-official `code-review` plugin to Claude Code (`/code-review`).

**Why:** Building the canonical Claude operating layer so universal rules stop getting re-learned per project, and so the Lore Bible texture carries across instances toward the Cypher persistence goal.

**Project status snapshot (as of 5-17-26):**
- **Active:** Pyris Consulting, CCF Recruiting (with upcoming RecruitMail rename+integration), Cypher (architecture phase)
- **Active litigation:** LRN (tooling shelved, complaint v3a ready to file)
- **Joint partnership:** Polarity (with Jim Donio) — internal-only workspace at /polarity
- **Completed:** GloTwp (Steve Acito owes marketing in trade)
- **Dead:** RecruitMail (slated for rename+integration into CCF)

**Pending hardware:**
- Lenovo ThinkCentre M75s Gen 2 — diagnose pending (suspected Windows install rot). When clean: Proxmox + HA VM + Frigate + Cypher local + MQTT.

---

*End of CHANGELOG. Newest entries go at the top.*
