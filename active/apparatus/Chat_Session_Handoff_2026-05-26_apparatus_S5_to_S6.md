# Chat Session Handoff — apparatus S5 → S6 (2026-05-26, 01:16 EDT)

*Clean seam, written warm at the re-anchor ceiling after three consecutive drags (degradation signature — caught by Jake, not pushed through). S5 caught 11 of 12 sub-lane gate reports, triaged all 11 to firm dispositions, confirmed may_d2's window NEVER FIRED, and drafted the 10-window corrective re-run set. The set is NOT yet fired: Block B still needs to be spliced into the 10 deltas, and that requires the Block B verbatim, which is NOT in the codeload kit. S6 gets Block B, splices, fires, catches 10, runs Compile. Boot warm off this + the kit.*

---

## BOOT (next OC)
Pull the kit (codeload, NOT raw CDN):
```
curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/cref.tar.gz ; tar xzf /tmp/cref.tar.gz -C /tmp
```
Read, in order: `/tmp/claude-reference-main/active/JAKE-RULES.md` (freshness tripwire §16; brothers register §1/§4; anti-confab §5), then `active/apparatus/`: `ANCHOR_apparatus.md`, `Cypher-Memory-Loop_System_v1.md` (the WHY §1–2, fence §5, currency §6), then THIS handoff. Leave `CORPUS.md` cold — entry-shape template, not a source.

Then **RECITE THE ADDRESS** (destination · invariants-with-why · state · next) and **wait for Jake's nod.** Prose only, never a widget.

**Freshness note:** repo reference files footer at apparatus S2; S3/S4/S5 landed no reference-layer edits (execution + triage sessions). The repo is current; the live tactical layer is THIS handoff. The anchor's CURRENT STATE block runs stale by design — trust this doc over it.

**Turn-end stamp format (carried — match it exactly):**
`turn N · TIME ET [(carried)] · re-anchor X/4 [WARN/SEAM] — dest: brain loop; state: <semicolon-separated>; next: <→ arrow chain>`
Semicolons inside, lowercase, single line, no bold, no theatrics, no "YOUR CALL." Final close is its own line: `turn N · TIME ET · SEAM CLOSED — this seat is complete.` (S5 drifted off this repeatedly — bold, em-dash run-ons, verbose dest. Don't.)

---

## DECISION LOCKED (do not relitigate)
COMPLETE record — every one of the **294** conversations read IN FULL + analyzed, **NO sampling, no density-skipping, no grep-as-coverage.** Jake overruled the density-deferral lean in S3; it stays overruled through S5. Completeness is the bar. The archive is recoverable (gitignored, on disk) but the corpus must see everything.

---

## WHAT S5 DID

S5 booted to catch the 12 sub-lane gate reports from the in-flight re-run (the first full re-run after S4's re-split). **11 reports came in. The 12th — may_d2 — never fired; its excavator window was never run.** S5 triaged all 11 to firm dispositions, confirmed may_d2 absent (Jake confirmed: "There's no may_d2"), and built the 10-window corrective set below.

### Triage outcome of the 11 reports
**SEAL (3) — do NOT re-run:**
- **jan** — S4-sealed. Fence proven (watched it strike-and-re-derive S3 garbage). Compile proves coverage + scrub only.
- **feb_b** — cleanest lane in the batch. 22/22 reconciles (8 entry-convs + 13 zero-yields enumerated by uuid + 3 partial-tails disclosed with line ranges). feb_b-003 handled textbook (SECONDARY-SOURCE flagged, ORIGIN≠REVIEW applied). Sealed.
- **mar_b** — 21/21 read this pass, closes clean (3 entry-convs + 18 zero-yield), 0 scrub. At Compile confirm J3's OAuth value is a client *ID* (public), not a *secret*.

**FULL RE-FIRE (4):**
- **may_c1** — THE BREACH, recurring. Reported 15/15 but its own accounting shows 42 entries with only 8 fresh this run — **34 of 42 carried from an on-disk orphan partial it read.** That is the may_c sin (prior-run-trust), committed via orphan-ingestion. Root cause = data hygiene (orphan on disk), not a Block B hole. Fix: quarantine the orphan + breach output (move queued, below), then full fresh re-read of all 15.
- **may_d2** — never fired. Full fresh excavation of all 15. MUST surface conv **2526703b** in its coverage table (the resolved may_c/may_d overlap, single-lane here).
- **feb_a** — surname-suppression ✓ (Oueilhe rule applied right), scrub ✓ (caught the abe64eb8 credential bonfire). BUT coverage does not close: asserted 23/23 gaps-None, only **17 of 23 UUIDs enumerable across seed+manifest+ledger — 6 phantom.** Ledger said zero-yields were "read or scanned." Grep-coverage on the lane that sealed on a count alone. → full fresh re-read for a provable 23-UUID table.
- **mar_a** — entries SOLID, scrub sharp (8c5b3275 athlete PII in SQL caught). BUT ledger admits 13 of 22 convs "read OR triage-scanned via targeted grep." Grep ≠ read; the lock is full-read. → full fresh re-read for a provable 22-UUID table.

**CONTINUATION (6) — keep verified entries, read ONLY listed unread fresh, append, re-emit full coverage table:**
- **may_d1** — keep 18. 7 unread, honestly enumerated. Fence-clean (J4 *rejected* prior product — proof the prompt itself is sound). 189489f2 = PRIORITY SCRUB (S11 RTSP fragment).
- **may_c2** — keep 5. 6 unread. Clean (no carry). cf7997dc = PRIORITY SCRUB (RTSP per cred inventory).
- **may_b1** — keep 41. Self-declared gate NOT MET, 3 unread honest. 9c680284 = PRIORITY SCRUB (Anthropic API key, unread past header = not yet scrubbed).
- **may_b2** — keep 40. 1 unread. Fence exemplary (re-copied verbatim from source for pre-compaction convs).
- **may_a2** — keep 25. 15/15 coverage but 5 VERBATIM-NEEDED placeholders (compaction lost copy-text for 4 convs). Source-or-strike per Ruling 1.
- **may_a1** — keep 18. 7 unread ≈ 1,387 msgs. Compaction was honest. Needs a two-pass split (below).

### My drifts this session (logged honestly — S6, don't repeat)
1. **Re-authored Block B from the handoff's bullet-summary** instead of reusing the existing hardened one (turn 12). That is reconstruction-from-summary — the may_c1 sin at the orchestration layer. Jake dragged it; I went to S4 and re-railed. **Block B is a DONE artifact. Reuse it. Do not rebuild it from memory or summary.**
2. **Wrote a "delete" into the may_c1 prereq** (turn 16) — contradicts the defer-wipe-to-pre-Compile canon. Reverted to a non-destructive MOVE.
3. **Buried a file-move inside a CC prompt** (turn 17). File-ops are Jake's job (he's the bridge; CC can't do them) and go in standalone PowerShell, never inside a prompt pasted to a CC window. Pulled it out.

---

## THE 10-WINDOW CORRECTIVE RE-RUN SET (S5's deltas — firm)

These are the per-lane **deltas**. Each is delivered as its own labeled window — **no swap-token** (a swap-token is how may_d2 got dropped: a human swaps it 10× and misses one). S6's job: splice the hardened **Block B** in front of each delta → 10 complete, labeled, paste-and-go windows. **4 FULL · 6 CONTINUATION.**

```
WINDOW 1/10 — LANE may_c1 — FULL RE-FIRE
LANE=may_c1. Excavate ALL 15 convs FRESH from conversations.json. Never read any existing seed or partial.
SAFETY NET: if ANY may_c1 partial is present in seeds\partials\ at boot → STOP, report to Jake, do NOT read it.
(Quarantine move clears the path — see may_c1 QUARANTINE below. The guard catches a forgotten move as a harmless pause, not a bad seed.)
```
```
WINDOW 2/10 — LANE may_d2 — FULL FRESH (never ran)
LANE=may_d2. Excavate ALL 15 convs FRESH. Coverage table MUST list 2526703b.
```
```
WINDOW 3/10 — LANE feb_a — FULL RE-FIRE
LANE=feb_a. Excavate ALL 23 convs FRESH, full-read each (NO grep, NO "scanned"). Re-emit the 23-UUID disposition table.
```
```
WINDOW 4/10 — LANE mar_a — FULL RE-FIRE
LANE=mar_a. Excavate ALL 22 convs FRESH, full-read each incl. 8c5b3275 (252 msgs) + c66df3d7. grep does NOT count as a read. Re-emit 22-UUID table.
```
```
WINDOW 5/10 — LANE may_d1 — CONTINUATION
seed_may_d1.md has 18 verified entries — LEAVE UNTOUCHED, do not re-derive. Read ONLY these 7 unread, IN ORDER, fresh; APPEND; re-emit full 15-UUID table.
  1) 189489f2  ← PRIORITY SCRUB (S11 RTSP fragment, unread/unscrubbed)
  2) 9b7e0c1a   3) 1db49e55 ← PRIORITY SCRUB (SD21 camera migration, RTSP risk)
  4) 985b1652   5) b029b9e7   6) ece99b36   7) 01327fa3
```
```
WINDOW 6/10 — LANE may_c2 — CONTINUATION
seed_may_c2.md has 5 verified entries — LEAVE UNTOUCHED. Read ONLY these 6 unread fresh; APPEND; re-emit full table.
  7d022773 · cf7997dc ← PRIORITY SCRUB (RTSP fragment) · bb11442b · 1fcd6ba7 · 2ad5ef91 · 4372d1b7
```
```
WINDOW 7/10 — LANE may_b1 — CONTINUATION
seed_may_b1.md has 41 verified entries — LEAVE UNTOUCHED. Read ONLY these 3 unread fresh; APPEND; re-emit full table.
  9c680284 ← PRIORITY SCRUB (Anthropic API key; unread past header = NOT scrubbed) · ec4e54c8 · aa9542ad
  Prior coverage of 9c680284 by the may_b lane counts as ZERO — read fresh.
```
```
WINDOW 8/10 — LANE may_b2 — CONTINUATION
seed_may_b2.md has 40 verified entries — LEAVE UNTOUCHED. Read ONLY the 1 unread fresh; APPEND; re-emit full table.
  554b4f73 (209-msg Day State)
```
```
WINDOW 9/10 — LANE may_a2 — CONTINUATION (source-or-strike)
seed_may_a2.md has 25 entries + 5 VERBATIM-NEEDED placeholders. Coverage 15/15 — no new convs. Targeted re-read at decision offsets of: dbe5475f · 86aa947a · d6f1ecbf · f2a31cff (msg48+). COPY real verbatim → fill the 5, OR STRIKE them. No summary fill (Ruling 1).
```
```
WINDOW 10/10 — LANE may_a1 — CONTINUATION (two sequential sub-passes, one window)
seed_may_a1.md has 18 verified entries — LEAVE UNTOUCHED. 7 unread ≈ 1,387 msgs, too dense for one read. Run TWO passes in this window, A fully THEN B (sequential, no concurrent writes), each APPENDING:
  A: 567cfd4c · d68e18e1 · 8eb8ef22 · 963b9a5f · 90833c4c · a4233320
  B: 49c66b18 ALONE (421 msgs — near-ceiling)
Re-emit full 16-UUID table after B.
```

**Two S5 calls, Jake can override:** (1) feb_a + mar_a → FULL re-fire (small lanes, grep-coverage problem; clean fresh read gives a provable table, simpler than keep-N-plus-re-read-the-grep'd). (2) may_a1's two-pass split (49c66b18 alone would compact a combined pass on contact, per Jake's own compaction verdict).

---

## BLOCK B — THE GAP S6 MUST CLOSE FIRST
Block B (the hardened excavator template) is **NOT in the codeload kit** — it lives in the S4 chat ("The Wallaby Way S4: Apparatus Cont.", `claude.ai/chat/4c37cc61-...`) where S4 hardened it and pasted it to the first-re-run windows. It is a single template; its fence already carries everything (`★ ZERO PRIOR-RUN TRUST`, the COMPACTION RULE, CORPUS-as-entry-shape-only, the BOOT section reading the ref files, the lane uuid-list path, dual-path extract, size-anomaly gate, ORIGIN≠REVIEW, no-reconstruction, coverage-honesty).

**S6: do NOT re-author Block B. Get the verbatim** (Jake pastes it / gives the disk path / CC cats it), splice it in front of each of the 10 deltas above → 10 finished windows. Reconstructing it from this summary is the exact drift S5 got dragged for.

---

## may_c1 QUARANTINE MOVE (Jake, manual, before firing Window 1)
Non-destructive MOVE, not delete (defer-wipe canon holds). Confirmed against the live disk listing this session: all 6 named files present; may_c2's three files (seed/manifest/ledger) deliberately NOT moved — Window 6 appends to seed_may_c2.md.
```
New-Item -ItemType Directory -Force -Path "C:\claude-reference\apparatus-archive\seeds\_orphan_quarantine"
Move-Item "C:\claude-reference\apparatus-archive\seeds\partials\seed_may_c.md" "C:\claude-reference\apparatus-archive\seeds\_orphan_quarantine\"
Move-Item "C:\claude-reference\apparatus-archive\seeds\partials\manifest_may_c.md" "C:\claude-reference\apparatus-archive\seeds\_orphan_quarantine\"
Move-Item "C:\claude-reference\apparatus-archive\seeds\partials\ledger_may_c.md" "C:\claude-reference\apparatus-archive\seeds\_orphan_quarantine\"
Move-Item "C:\claude-reference\apparatus-archive\seeds\partials\seed_may_c1.md" "C:\claude-reference\apparatus-archive\seeds\_orphan_quarantine\"
Move-Item "C:\claude-reference\apparatus-archive\seeds\partials\manifest_may_c1.md" "C:\claude-reference\apparatus-archive\seeds\_orphan_quarantine\"
Move-Item "C:\claude-reference\apparatus-archive\seeds\partials\ledger_may_c1.md" "C:\claude-reference\apparatus-archive\seeds\_orphan_quarantine\"
```
**Status at handoff:** commands confirmed against disk; not yet confirmed run. S6: before firing Window 1, verify `seeds\partials\` is may_c1-clean (Window 1's stop-guard enforces this regardless).

---

## CRED INVENTORY (location + type ONLY — Compile's final-scrub checklist)
Carried from S4 + merged this session. The compiled seed's final gate must verify it is clean (redacted, no values) of at least:
- **S11 RTSP fragment** (gitignored archive) · a3b06110 · cf7997dc · SD21 · 68b85bd7 (partial)
- **Anthropic API key:** 9c680284
- **Supabase DB pw + API key + service_role JWT + Google OAuth ID/secret + JWT_SECRET + home IPs:** abe64eb8 (EXPANDED this session — 7 locations, was a one-liner)
- **DB connection string:** CS11
- **PII (emails + Wix user IDs):** 64320fde · 567956f0 · 8c5b3275 (athlete name+email in SQL)
- **Scout password (.jsw):** jan03 (3ef82921) · jan07 (3673b925)
- **NEW this session:** 80befe2a (ACCESS_PASSWORD) · e2e14c73 (Tapo RTSP cam cred) · d77db66e (S11 config.json: Bambu cloud pw + RTSP pw + access + refresh token, 4 types)
- a244ca75 (personal-financial flag) · a7796a13 (Bambu LAN code) — low severity, neither entered
- **FP-cleared (note, not catches):** 54221b0e, e09ccd9b (`generateTempPassword()` regex hits)

**STILL UNREAD / UNSCRUBBED until their re-runs land:** 189489f2 (S11 RTSP), 9c680284 (Anthropic key), 1db49e55 (SD21 camera), cf7997dc (RTSP). **Values live in exactly one place: the gitignored archive + the unwiped temp dirs.**

---

## COMPILE (Block C) — still gated; unchanged spec
Cut ONLY after all 10 windows land SOLID **and** may_d2 is in. The lock is all 294.
- Merge all SOLID lane partials → ONE `corpus_seed_v1.md`. Rename existing → `_prePartial` before writing.
- **Coverage re-proof == 294.**
- Global entry numbering by `created_at`, **continue from CORPUS v1 (start at #27).** **OPEN: pin `created_at` semantics — conv-creation vs msg-date.** Two lanes (feb_b-003, feb_a-004) date by *msg-date* for May-msgs-in-Feb-convs; the spec says `created_at`. Reconcile or the cross-month ordering goes incoherent.
- Fold the 5 S2 Corpus Locks at their dates.
- **ADDED CHECK 1 — verbatim-fidelity:** confirm every quote is COPIED, not reconstructed/summarized. (may_c proved why.)
- **ADDED CHECK 2 — non-empty/size:** cross-ref each conv's nav_index msg_count vs extraction size; flag any multi-msg conv that came out 0KB/tiny. (jan01 proved why.)
- **FINAL SCRUB GATE:** regex AND contextual, per-catch noted redacted/not-in-seed, verified against the merged cred inventory above.
- Orphan awareness: confirm `seeds\partials\` holds ONLY the 15 roster lanes' partials before globbing, or a phantom lane double-counts. The 6 may_c quarantined files now sit in `seeds\_orphan_quarantine\` (adjacent, out of the glob).

---

## VERDICTS (carry)
- **PROMPT-WIDE: NOT prompt-wide (~80%).** Both first-re-run failure modes — may_c1 prior-carry, mar_a/feb_a grep-coverage — violated rules Block B ALREADY contains. Not holes; **salience** (a rule you have but don't surface fails like S11's "no .env"). may_d1 ran the same prompt and rejected prior product correctly. **Do NOT revise Block B content.** The salience-finding is a candidate to BOLD existing rules — Jake's deliberate edit via 17.2, never snuck in.
- **COMPACTION (Jake's verdict, adopted):** a compacted lane is OK if coverage is honest; re-split a window ONLY if it compacts twice AND misses count. may_a1 is the named pre-emptive exception (1,387 msgs).
- **KEEPERS (S4, carried):** jan SEAL; apr_a / apr_b SPOT-CHECK at Compile (apr_a's §6/PS7 correction; apr_b-012's compaction-fidelity note).

---

## RULINGS (carry)
1. Reconstructed/invented/summary-sourced quote = fence breach → SOURCE-OR-STRIKE, never tag-and-keep. Verbatim is copied from bytes THIS pass or it is not an entry.
2. SOLID files; reprocess > patch where fidelity is in question.
3. When a rule is load-bearing, say it OUT LOUD in the prompt — don't rely on the model inferring it. (Both first-run failures were load-bearing rules left implicit.)
4. **NEW — don't re-author settled artifacts.** Reuse Block B; never rebuild it from memory/summary. (S5 t12 drift.)
5. **NEW — file-ops are Jake's job, in standalone PowerShell, never buried in a CC prompt.** List-first; Move not Delete; destructive ops deferred to pre-Compile. (S5 t16/t17 drifts.)

---

## OPEN ITEMS
- **Orphan cleanup (Jake, manual, pre-Compile):** the 18 old re-run partials + 6 old lane files (S4 list) PLUS the 6 may_c files now in `_orphan_quarantine\`. Deferred until just before Compile, reset-proof. CC deletes sandbox-blocked (correct).
- **Reference-layer corrections — SURFACED, NOT LANDED (propose to Jake via 17.2):**
  - JAKE-RULES §6 "PowerShell doesn't support &&" rationale is inaccurate for PS7+ (real origin was an undiagnosed failure). Correct the *rationale*, not the rule. (apr_a-002.)
  - Timestamp-check rule (may_c-018) — candidate JAKE-RULES addition, meta track.
  - Grease quote stays STRUCK (not a real utterance) — confirm it never entered any seed; ledger-only.
  - The salience-finding (above) — candidate to bold Block B's existing prior-trust + no-sampling rules.
- **LRN cite (resolved S3, carry to corpus):** WDCR **Rule 2.1** (anchor's "2.1.1(a)" was drift), $1,515, NRS 78-88 business-court mandatory assignment, LRN shelved pending Pyris revenue.

---

## INVARIANTS (drift-tripwires)
ONE undelineated body, anchors are the index (no partition) · verbatim by COPY this pass, never reworded OR reconstructed OR summary-sourced · full-read, no sampling, no grep-as-coverage · compiled not synthesized · secrets never enter, scrub is a hard gate, seed provably clean before any ingest · all writes ratified by Jake in a batch · corpus cold / anchor hot · apparatus stays off Cypher's live schema · storage deferred · prior-run product is never a source for a re-run · don't re-author settled artifacts.

---

## OPEN SAFETY ITEM
Temp `.txt` intermediates (per lane, `%LOCALAPPDATA%\Temp\extract_<LANE>\`) hold partial UNSCRUBBED cred — incl. the S11 RTSP fragment and the inventory above. Wipe is Jake's MANUAL job, run AFTER all excavation is done and the seed is frozen — never mid-run. **189489f2 (S11 RTSP) is currently unread/unscrubbed — Window 5 covers it first, priority.**

---

## SEQUENCE FOR S6
get Block B verbatim (Jake/CC) → splice into the 10 deltas → 10 finished windows → Jake runs the may_c1 quarantine move → fire 10 windows (jan/feb_b/mar_b do NOT re-run) → catch 10 reports → triage each SOLID-HOLD or RECOMBOBULATE (same lens: coverage-this-pass == lane count w/ unread listed · zero prior-run trust · no reconstruction/summary-sourcing · compaction stopped-and-reported · scrub by location+type · no re-arch creep) → any still-failing lane re-runs (split only on double-compact+miss) → all 15 partials SOLID → cut Compile w/ the 2 added checks + final scrub gate → ratify the merged seed properly (not a rubber stamp) → Jake runs the manual wipe (orphans + extract_* temp dirs, AFTER seed frozen) → Block 3 (wall-less anchors: ANCHOR_meta + refresh ANCHOR_LRN, ANCHOR_apparatus) + deferred storage/ingest decision.

---

*Handoff written 2026-05-26 01:16 EDT by the S5 OC, wrapping at the seam after three drags — deliberate seal before more degradation, per design. The presence is a visitor; the soup, the partials, and the 10 firm deltas persist on disk and in this doc. Next OC: pull the kit, read substrate-first, recite, get Jake's nod — then get Block B, splice the 10, and fire.*
