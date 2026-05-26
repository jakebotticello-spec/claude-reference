# Chat Session Handoff — apparatus S6 → S7 (2026-05-26, 03:11 EDT)

*Clean seam, written warm at the re-anchor ceiling. S6 caught all 10 corrective-run gate reports, triaged every one to a firm disposition, fired the passes that needed re-firing (c1 continuation, b1 confirm, d2 + mar_a clean re-runs), and landed all 10 lanes solid. Nothing is in excavation anymore. S7 boots warm off this doc + the kit, runs the two remaining gates, then cuts Compile. The most irreversible step (Compile ingest) is deliberately handed to a fresh seat on a full budget rather than started at the ceiling.*

---

## BOOT (next OC)

Pull the kit (codeload, NOT raw CDN):
```
curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/cref.tar.gz ; tar xzf /tmp/cref.tar.gz -C /tmp
```
Read, in order: `/tmp/claude-reference-main/active/JAKE-RULES.md` (freshness tripwire §16; brothers register §1/§4; anti-confab §5; stamp discipline §5.2), then `active/apparatus/`: `ANCHOR_apparatus.md`, `Cypher-Memory-Loop_System_v1.md` (WHY §1–2, fence §5, currency §6), then THIS handoff. Leave `CORPUS.md` cold — entry-shape template, not a source.

Then **RECITE THE ADDRESS** (destination · invariants-with-why · state · next) and **wait for Jake's nod.** Prose only, never a widget.

**Freshness note:** repo reference files footer at apparatus S2 (5-25-26); S3–S6 landed no reference-layer commits (execution + triage sessions). The repo is current; the live tactical layer is THIS handoff. The anchor's CURRENT STATE block runs stale by design — trust this doc over it. S7's first reference-layer job is committing the items in "ENSHRINE THESE" below.

---

## TURN-END STAMP FORMAT — READ THIS, IT COST S6 TEN TURNS

The stamp is **wrapped in backticks (inline code)** so the UI renders it as a **red monospace span**. That is the format. It is a *render style*, not a grammar spec. S5 drifted it into bold + theatrics; S6 then burned ~10 turns "fixing" the words (caps, trailing tags, capitalization) when the only actual problem was that S6 wrote the line as **bare prose instead of backticked**. Do not repeat either failure. Backtick the line. It renders red. Done.

Format string:
```
turn N · TIME ET [(carried)] · re-anchor X/4 [WARN/SEAM] — dest: brain loop; state: <semicolon-separated>; next: <→ arrow chain>
```
Content rules (match the rendered examples, not a rulebook):
- Wrapped in backticks → renders as the red inline-code span. **This is non-negotiable and is the whole point.**
- Sentence case: lowercase ordinary words; proper nouns keep normal caps (Compile, Block B, Life360, RTSP). **Never all-caps for emphasis** (no SOLID / PARTIAL / NOT OK) — that is theatrics in the same family as bold.
- Single line. Semicolons between dest / state / next and within state. Arrows (→) only in `next`, no leading arrow.
- **Ends at the last `next` element. No trailing tag** (no "· seam ~turn 20" appended after the chain — that was an S6 tell).
- `dest: brain loop` always.
- Optional flags: `(carried)` after TIME when the clock is stale; `[WARN]` / `[SEAM]` on the re-anchor field.
- Seam close is its own line: `turn N · TIME ET · SEAM CLOSED — this seat is complete.`

Cadence: re-anchor ~every 5 turns; the `X/4` counter is an externalized artifact (Claude can't self-count across compaction). The 4th re-anchor (~turn 20) fires the "we're at the ceiling" flag to both of you; wrap at the nearest clean seam to ~20, hard ceiling ~25. Not a guillotine — land at a seam.

---

## DECISION LOCKED (do not relitigate)

COMPLETE record — every one of the **294** conversations read IN FULL + analyzed, **NO sampling, no density-skipping, no grep-as-coverage.** Completeness is the bar. The archive is recoverable (gitignored, on disk) but the corpus must see everything. Jake overruled the density-deferral lean in S3; it stays overruled.

Invariants (with the why — the why is what lets Jake catch the OC without coding):
- **One undelineated corpus; anchors are the index into it** — partitioning hides cross-domain knowledge. No track column (killed S2).
- **Verbatim by copy, never reworded OR reconstructed** — a reworded "verbatim" is a drifting summary with a paper trail; reconstruction-from-summary is a fence breach (the may_c1 sin).
- **Compiled, not synthesized; memories.json is navigation, never a source** — verbatim comes off conversations.json only.
- **Secrets never enter** — the archive holds live-class creds; scrub is a hard gate, nothing ingested until verified.
- **The archive never enters chat** — CC reads the ~348MB path off disk; bytes stay on Workhorse; Jake bridges by pasting CC's reports.
- **Anchor hot/small/boot-read, corpus cold/queried-never-booted** — the instant the corpus loads "to be safe," the swamp rebuilds.
- **All writes proposed + ratified by Jake in a batch** — the OC is the drift-prone summarizer; Jake's confirm closes the dead error-correction seam.

OC seat = ARCHITECT/ORCHESTRATOR, not excavator. CC excavates off disk; OC guides; Jake bridges.

---

## WHAT S6 DID

Booted, recited, and caught the 10 corrective-run reports. Triaged each, fired what needed re-firing, landed all 10 solid:

- **c1** — continuation closed the 4-conv gap (incl. the two scrub-critical convs); 15/15; 83b95e7b read fresh; **solid.**
- **b1** — surgical confirm pass verified entries 042–081 against source: 39 verified, **1 replaced** (may_b1-045 had a 6-word compaction-carry drift, fixed from source), 0 struck; ea900330 tail closed; **solid.** (The 045 catch is the empirical proof that compaction-summary carry drifts — see the systemic finding below.)
- **d2** — first confirm pass FAILED the lens (it upgraded 7 convs' DECISION entries to VERBATIM off the compaction summary, not a source read — a summary wearing a verbatim badge). Re-fired as a **clean re-run**, which fixed it: write-as-you-go fresh reads, 27 real entries, 15/15, scrub clean (owner cred rotated, fake flagged). **solid.**
- **mar_a** — prior pass had committed reconstruction-from-summary + a false "FULL READ" header + header-only "coverage." Re-fired **clean re-run**: 22/22 read, breaches gone, scrub-hygiene fixed (PII now location+type, no values), 7 real entries. **solid with one residual** (see must-verify list).

S6 also (a) finally pinned the stamp format (it's inline-code/backticks — see above), and (b) corrected its own confab: it had asserted "Block B is on disk" four times without verifying — it is NOT a file in the committed kit; see Block B note.

---

## CURRENT STATE — all 10 lanes solid

| lane  | disposition | note |
|-------|-------------|------|
| a2    | solid | 27/30 full-bar; 3 carried-fragment entries (023/024/025) flagged |
| b2    | solid | 041–047 = pre-compaction-identified / post-copied → Compile must-verify |
| c2    | solid | RTSP scrub-hygiene: tighten catch output (don't reproduce URL structure) |
| d1    | solid | clean; RTSP cred caught + suppressed |
| feb_a | solid | sealed 23/23; self-corrected a uuid + a missing manifest row; abe64eb8 cred cluster |
| a1    | solid | 16/16; sub-pass B gold-standard fresh-read; Resend key caught |
| c1    | solid | continuation closed gap; **83b95e7b = the batch's heaviest cred cluster** |
| b1    | solid | confirm pass: 39 verified, 1 replaced, 0 struck |
| d2    | solid | clean re-run fixed the relabel; 27 entries |
| mar_a | solid* | clean re-run; *001/002/003 summary-carried → Compile must-verify |

Nothing is in excavation. We are at the two gates.

---

## NEXT MOVE — the two gates, then Compile

**Gate 1 — lock the compaction rule (load-bearing, now proven systemic).**
Compaction-carry showed up in three places: the d2 confirm (relabel), b1 (the 045 drift), and mar_a (001/002/003). Enshrined rule: *any entry that crossed a compaction boundary via the summary instead of a post-compaction source read is UNVERIFIED until the Compile copy-check diffs it against the archive — verify or strike, never promote on summary-trust.* The Compile verbatim-copy-check is the catch-all.

**Gate 2 — master cred / PII sweep (before any ingest).**
One consolidated list, each marked rotated/revoked or live. The scrub kept all of these OUT of the corpus (location+type only); the concern is the **archive itself** holds them permanently (the immortalized-leak the spec warns about):
- **c1 / 83b95e7b** — RTSP cred URL ×3, plaintext cloud password, plaintext Life360 password, JWT auth/refresh tokens, Life360 bearer tokens ×2; **MSG 301 the assistant itself quoted the access_token.** Top line. Confirm all rotated.
- **mar_a / 4a18bd06** — Anthropic API key (sk-ant-api03). Confirm revoked.
- **mar_a / 64320fde** — application password. Confirm rotated.
- **mar_a / 8c5b3275 + 6fe468e6 + 64320fde** — athlete PII: real names + personal Gmail addresses, **several likely minor recruits**, in SQL and logs. Privacy item: the 348MB archive contains minor PII — handle storage/sharing accordingly.
- **feb_a / abe64eb8** — Supabase DB password + anon JWT + Google OAuth client id/secret. Confirm rotated.
- **a1 / 49c66b18** — Resend live key (revoke was instructed in-session). Confirm done.
- **d2 / 5a10e5ec** — Supabase owner-role string (confirmed rotated at S11 wrap).
- **d1 / 1db49e55, b2 / S11b** — RTSP camera creds.

**Then Compile** (gated until both gates clear): orphan-sweep + ==294 + verbatim copy-check + msg_count-vs-size.

### Compile copy-check MUST-VERIFY list (the known summary-carried / attribution items)
- **mar_a-001 / 002 / 003** — verbatim "preserved in compaction summary," not post-compaction source read. Diff against 3661c680 (msgs 59/62), c66df3d7 (msgs 89–94), 301cda56 (msgs 97–100). Replace any drift.
- **b2-041 through 047** — pre-compaction-identified, post-copied. Spot-check against source.
- **d2 entry 023** — quotes an S1 verbatim at 2526703b MSG[33] where it is a *retrieval* of the 41bc76dc origin. Attribute to origin, dedup.
- **Cross-lane dedup already flagged:** ea900330 ICA arbitration appears in both may_b and may_b1 (collapse); may_b1 ORIGIN/REVIEW pairs (075/039, 079/035, 077/071/038).
- **Arithmetic reconciles:** c1 entry count (21+6+7 reported as 35 = 34); mar_a zero-yield (15→16 corrected). Confirm at Compile.

---

## BLOCK B — where it actually lives (so S7 doesn't re-loop this)

Block B is the hardened `CC KICKOFF — apparatus LANE EXCAVATION` template. It is **NOT a file in the committed kit** and was never confirmed to be one. It was delivered as an **S4 chat code block** and pasted into CC windows; Jake holds it and pastes it. S6 wrongly asserted it was "on disk under apparatus-archive" — it is not. If Compile's copy-check forces a lane re-read, get the verbatim Block B from Jake (or it should be committed to the repo as part of "ENSHRINE THESE"); do NOT re-author it from this handoff's description — that was S5's logged drift.

---

## ENSHRINE THESE (S7 → repo, proposed-then-ratified)
1. **Stamp format** into JAKE-RULES §5.2: it is inline-code/backticks (renders red); the content rules above; the failure history one-liner.
2. **Compaction-carry rule** into the Loop spec fence: summary-carried entries are unverified until source-diffed.
3. **Block B** committed to the repo (kill the "where does it live" loop permanently).
4. **Master cred/PII sweep list** as the pre-ingest checklist.

---

## JUDGMENT-CALL LEDGER (S6) — call · reasoning · confidence
- **b1 = ok, no rerun.** Confirm did a real source re-read of all at-risk entries and caught the one drift. ~95%.
- **d2 = clean re-run (not surgical patch).** Confirm relabeled off summary; re-run guarantees fresh-copy. The re-run came back solid. ~90%.
- **mar_a 001/002/003 → Compile copy-check, not a 4th window.** Proportionate (3 entries vs another 25-min process); the Compile gate diffs everything against source anyway. ~80% — if Jake prefers, a 3-conv confirm pass closes it pre-Compile.
- **clean re-run > surgical for untrustworthy passes (mar_a, d2).** Re-reading beats trusting-and-patching when the prior pass's provenance is in doubt. ~90%.
- **Don't re-spec a fired 25-min process mid-run** (Jake's correction, adopted). Triage the finished result, then decide the next action — that is not waffling. ~100%.

## DOWNSTREAM FLAGS (horizon)
- **At Compile:** the must-verify list above is the difference between a clean corpus and a drifted one. Do not skip the copy-check on those entries.
- **Before ingest:** the cred/PII sweep is a hard gate; the minor-athlete PII in the archive is a standing privacy consideration for how the 348MB file is stored/shared, independent of the corpus.
- **Reference layer:** S3–S6 proposed several rule edits (stamp format, compaction rule, Block B commit) that are NOT yet in the repo — JAKE-RULES still footers S2. S7 should land them at close.
