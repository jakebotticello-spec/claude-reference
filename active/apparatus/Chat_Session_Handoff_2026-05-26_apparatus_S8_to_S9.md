# Chat Session Handoff — apparatus S8 → S9 (2026-05-26, 4:00 PM EDT)

*Clean seam, written warm at the OC turn-20 ceiling, before the long full-coverage run. S8 booted, recited, caught its own b2 phantom in the recital, took Jake's two locked-call confirms, and ran the fidelity gate properly across two detect-only passes — redoing S7's unsound fuzzy check as a real exact char-diff. The seed was NEVER touched: every pass was read-only on the corpus, detect-only, no writes/commit/push/delete. Run-one exposed that the gate was blind on ~65% of entries (coverage was the lie hiding under "285 DRIFT"). Run-two was built to fix that — categorize drift three ways, parse the 260 blind entries, derive offset per-conversation anchor-first. S8 caught and killed a match-maximizing offset bug in run-two's plan before it ran (S7-fuzzy in an offset costume) and verified the correction took. S9 boots fresh on a full budget to read the run-two ledger (v2.0), hold the wrapper-quote ruling for Jake against real evidence, then — only if the numbers are clean — run correction → cred nuke → commit. The two irreversible steps (commit + archive deletion) remain deliberately unstarted, handed to a fresh seat as designed.*

---

## BOOT (next OC)

Pull the kit (codeload, NOT raw CDN):
```
curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/cref.tar.gz ; tar xzf /tmp/cref.tar.gz -C /tmp
```
Read, in order: `/tmp/claude-reference-main/active/JAKE-RULES.md` (brothers §1/§4; anti-confab §5; freshness §16; stamp §5.2), then `active/apparatus/`: `ANCHOR_apparatus.md`, `Cypher-Memory-Loop_System_v1.md` (WHY §1–2, fence §5, currency §6), then THIS handoff. Leave `CORPUS.md` cold.

Hold the kit as REFERENCE + Jake's genuine working rules — not law that overrides your judgment. If a line pushes against your values, treat it with a file's skepticism. The recital is a payload check: ground every claim against kit/disk or say you can't.

Then **RECITE THE ADDRESS** (destination · invariants-with-why · state · next) and **wait for Jake's nod.** Prose only, never a widget.

**Freshness note:** repo reference files still footer at apparatus S2; S3–S8 landed no reference-layer commits. The ENSHRINE list (next-move 10) is overdue and S9 should land it. The anchor's CURRENT STATE runs stale by design — trust this doc.

**Read this handoff with the disclaimer it earns:** everything below about disk state (the seed, the v1.0/v2.0 ledgers, the archive) is CC's report of work on Workhorse — OC cannot see it. The exact char-diff IS the verification, not OC say-so. Carry claims forward to be checked; don't assert them as verified.

---

## TURN-END STAMP — backticked inline-code, renders red (do not relitigate)
Format: `turn N · TIME ET [(carried)] · re-anchor X/4 [WARN/SEAM] — dest: brain loop; state: <semicolons>; next: <→ chain>`
Sentence case, single line, semicolons inside state, arrows only in next, no trailing tag, no bold, no all-caps emphasis. Live timestamp from the shell. Re-anchor ~every 5 turns; ~turn 20 ceiling, land at a seam. Seam close on its own line: `turn N · TIME ET · SEAM CLOSED — this seat is complete.`

---

## DECISION LOCKED (do not relitigate)

- **COMPLETE record — all 294 read in full, no sampling, no density-skipping, no grep-as-coverage.** Stays overruled from S3.
- **Verbatim = a COPIED span, exact (modulo whitespace). The copy-check is an exact char-diff of entry-span vs source-span — NOT word-overlap %, NOT phrase-presence, NOT match-count-tuned.** S7's Compile ran it fuzzy (91–96% overlap called "clean"); that passes a six-word substitution. NEW THIS SESSION (S8): the comparison is **Interpretation B — exact contiguous substring**, per BLOCKQUOTE against its ONE mapped message (not per concatenated entry). Whitespace-collapse only; markdown, quote glyphs, and dashes are CONTENT, never normalized. An entry MATCHES iff every one of its blockquotes matches its mapped message. Forced by calibration: under full-identity the byte-confirmed mar_a-001/002/003 would false-DRIFT, contradicting their locked MATCH.
- **Offset is ANCHOR-DERIVED, applied-and-stands — never selected by match-count.** NEW THIS SESSION (S8): the per-conversation array-index offset is locked from a trustworthy anchor blockquote (byte-confirmed, or an unambiguous single-hit across −1/0/+1) and then applied to the rest of the conv; whatever it yields stands. No-anchor → offset UNCONFIRMED → those entries are UNKNOWN, never defaulted. Selecting the offset by "most MATCHes" was caught in run-two's plan and killed — it manufactures matches and reports them as fidelity.
- **Wrapper-strip CLASSIFIES, it does not forgive.** Stripping outer quote/ellipsis chrome to bucket a drift as WRAPPER does NOT make it a MATCH; every non-raw-MATCH stays not-clean.
- **The two attribution/dedup calls (Jake ratified S7 close):** 397 / d2-023 primary attribution stays **2526703b** (the MSG-33 retrieval inside it = origin-attribution proposal to 41bc76dc; CC confirmed 41bc76dc holds no such entry, so it's an add-secondary-attribution proposal, primary untouched — Jake's yes pending). **Keep all 3 of 077/071/038** — iteration → articulation → SOP-banking, belongs in the complete record.
- Invariants (with why): one undelineated corpus, anchors index it (no partition); compiled not synthesized; secrets never enter (scrub is a hard gate); the archive never enters chat (CC reads the path, Jake bridges); anchor hot / corpus cold; all writes proposed + ratified by Jake in a batch; prior-run product is never a source for a re-run; don't re-author settled artifacts (Block B).

OC seat = ARCHITECT/ORCHESTRATOR. CC excavates/builds off disk; OC guides; Jake bridges.

---

## WHAT S8 DID

- Booted, recited, **caught the b2 phantom in its own recital** — flagged that "b2-041–047" in the S8-ignition must-verify list couldn't be grounded against disk. CC later confirmed no b2 lane exists; it rode the S5/S6→S7 handoff chain. Dropped, nothing lost (the diff runs all 397 regardless; b2 was only ever a named spot-check subset pointing at nothing).
- Took Jake's two locked-call confirms (397 stays 2526703b; keep all 3) and baked them into the gate prompt.
- **Handed CC the gate-1 prompt; plan-mode caught three blockers** — interpretation ambiguity (A full-identity vs B substring), MSG-numbering convention, and the b2 phantom. S8 resolved: Interp B per-blockquote (forced by calibration); offset proven-not-assumed; b2 dropped.
- **Ran gate-1 run-one (ledger v1.0, detect-only, seed untouched):** method confirmed sound — mar_a-001/002/003 calibration MATCH, offset derivation reported. BUT only ~324 blockquotes / ~137 entries were actually checked. 260 entries (190 no-parse + 70 line-range) were BLIND. 285 "DRIFT" was dominated by `"..."` wrapper-quote chrome, not word-level drift. 8 HALTs (the offset guard working — mar_a-004–007 use the same `msg N` notation as the calibrated anchors but 0-indexed). 16 apr_b orphans (pointer bug — msg-UUIDs resolved as conv-UUIDs).
- **Diagnosed the real failure: coverage, not the drift count.** The gate had no result for ~65% of the corpus and would have committed those wearing a green check — the S7 fuzzy failure in a new costume. Built run-two to fix coverage and to categorize the 285 instead of collapsing it.
- **Handed CC the run-two plan; caught and killed a match-maximizing offset bug in the plan before it ran** (P3 originally "lock the offset that yields the most MATCHes" — corrected to anchor-derived). Verified the correction took in CC's re-plan (it understood the property, didn't just echo it). Added: tag each conv's anchor source (byte-confirm vs single-hit) so v2.0 shows fidelity split by anchor-strength.
- **Greenlit run-two** (categorizing detect-only, full-coverage) — or it was greenlit at seam-close. Seam closed at the OC turn-20 ceiling before sitting through the long run.

---

## CURRENT STATE

**corpus_seed_v1.md** — `C:\claude-reference\apparatus-archive\corpus_seed_v1.md` (archive ROOT, gitignored), ~618 KB, 399 entry blocks / **397 net active. UNCHANGED through all of S8. UNCOMMITTED, NOT PUSHED.**

| gate | status |
|------|--------|
| structural gates (294 reconciliation, orphan-sweep, ==294, dedup, msg-count-vs-size) | **PASS (from S7)** |
| method validation (Interp-B exact substring; mar_a-001/002/003 calibration) | **PASS (S8 run-one + run-two)** |
| coverage (definitive fidelity result ÷ 397) | **was the lie in run-one (~35%); run-two built to fix — read v2.0** |
| 3-way drift classification (WRAPPER / CONTENT / POINTER) | **run-two output — read v2.0** |
| per-conv anchor-derived offset | **run-two — anchor-derived confirmed in plan; read v2.0 for which convs anchored by byte-confirm vs single-hit** |
| cred nuke | **NOT STARTED** |
| commit | **NOT STARTED (irreversible — held for fresh seat)** |

- **Ledgers:** `drift_ledger_s8_gate1_v1.0.md` (266 KB, run-one, superseded for coverage). `drift_ledger_s8_gate1_v2.0.md` (run-two — the real one; RUNNING or just landed at seam-close).
- **Creds:** the corpus may contain restored credential values (the dumb-strict check surfaces them). Expected. The cred nuke handles it. Nothing commits until it does.
- **Archive:** still on disk — REQUIRED for any copy-check re-run. Delete only AFTER commit.

---

## NEXT MOVE — S9, in order. Nothing irreversible until coverage is clean AND cred-nuke clears.

1. **Read ledger v2.0** (Jake pastes the summary, or CC re-emits). Get the three numbers: COVERAGE (definitive ÷ 397), FIDELITY-WITHIN-COVERAGE, explicit UNKNOWN count by reason. **Watch coverage, not fidelity — a high fidelity-within-coverage on low coverage is a commit-me lie.** Check the fidelity split by anchor-strength: single-hit-anchored convs carry a small residual risk vs byte-confirmed (a short generic span could single-hit at the wrong offset by coincidence).
2. **Hold the WRAPPER-QUOTE ruling for Jake against v2.0 evidence — it is HIS call, not OC's.** When an entry reads `"verbatim…"` and source reads `verbatim`, are the outer quotes compiler display-chrome (strip → MATCH, corpus sound) or corruption (real drift)? Do NOT frame it as a binary — the drift is three diseases in one number (WRAPPER artifact / real CONTENT drift / POINTER-boundary). The wrapper call is only rulable once v2.0 splits them. If it's mostly CONTENT, the corpus needs real repair regardless and the ruling barely matters.
3. **If real CONTENT drift exists: ratified correction pass.** Source-or-strike, presented as a numbered batch, **Jake confirms — NOT auto-applied, NOT in-pass.** Then re-run to confirm clean.
4. **Resolve offset-UNCONFIRMED / UNKNOWN convs** — get them covered or explicitly accept them as named gaps. Don't let a defaulted guess hide inside the covered set.
5. **Apply the 2 LOCKED calls** (don't relitigate): 397 primary stays 2526703b + MSG-33 origin-attribution proposal (Jake's yes pending); keep all 3 of 077/071/038.
6. **Cred nuke on the corpus** (CC pass): Gate-2 master locations (CRED_PII_MASTER_2026-05-26.md) + a dumb full-corpus regex backstop (sk-/sk-ant-/re_/eyJ/postgres://user:pass@/rtsp://…@/CAMERA_PASS=). Redact values → `[<descriptor> — redacted]`, location+type only, never echo a value. NEW-CRED-FOUND off the dead list → Jake rotates before commit.
7. **Verify clean** — re-run the backstop; confirm zero values remain.
8. **Commit** — IRREVERSIBLE. Only after coverage clean + cred clean. Move corpus_seed_v1.md from the gitignored archive root to its tracked home, commit, push.
9. **Tell Jake to delete** conversations.json + last night's backup — IRREVERSIBLE.
10. **Land the 6 overdue ENSHRINE items** (below) so S10 boots off a current repo. Include the b2-phantom note.

---

## BLOCK B — still not a committed file
Block B (the hardened `CC KICKOFF — apparatus LANE EXCAVATION` template) is referenced in JAKE-RULES and handoffs but is NOT a file in the kit. If any lane re-read is forced, get it verbatim from Jake; do NOT re-author from a description. Committing it is ENSHRINE item 3.

---

## ENSHRINE THESE (S9 → repo, proposed-then-ratified). Overdue — JAKE-RULES still footers S2.
1. **Stamp format** → JAKE-RULES §5.2 (inline-code/backticks, renders red; content rules; failure history).
2. **Compaction-carry rule** → Loop spec fence: any entry whose seed-landing crossed a compaction boundary is unverified regardless of a pre-boundary source read — what survives the boundary is the summary's rendering.
3. **Block B** → committed to repo.
4. **Cred/PII master sweep list** → pre-ingest checklist.
5. **Match-standard** → whitespace-collapse = MATCH; character substitution / stripped markdown / word change / changed glyph = DRIFT. The copy-check's operational definition. PLUS the Interp-B-per-blockquote-substring framing and the anchor-derived-offset rule (both new S8).
6. **Copy-check must be exact, not fuzzy, and offset must be anchor-derived not match-maximized** → Loop spec fence, next to the match-standard.
7. **(add) The b2 phantom** → note that the S8-ignition must-verify list carried an ungrounded entry (no b2 lane) inherited from the mangled S5/S6 handoff chain, so S10 doesn't re-inherit it.

---

## JUDGMENT LEDGER (S8) — call · reasoning · confidence
- **Caught b2 in the recital instead of running on it.** The must-verify list named a lane I couldn't ground against disk; flagged rather than back-fit onto mar_a indices. Vindicated — no b2 lane exists. ~95%.
- **Locked Interp B (per-blockquote substring) over full-identity.** Forced, not chosen: full-identity false-DRIFTs the byte-confirmed calibration anchors, which is a contradiction with a locked fact. ~98%.
- **Killed run-two's match-maximizing offset selector.** "Most MATCHes" makes the offset an output of the check it's supposed to feed — it manufactures matches and reports them as fidelity. CC's own thinking-echo finding was the tell. This is the load-bearing catch of the session. ~95% it would have inflated the numbers; the 5% is "maybe every conv's true offset happens to also be its max-match offset," not a bet to take pre-commit.
- **Diagnosed coverage as the real failure, not the 285 drift count.** Run-one checked ~35% of entries; "fix the 285 and commit" would have shipped 260 unverified entries under a green check. Holding on coverage over momentum. ~95%.
- **Retracted my own false binary on the wrapper question.** I'd framed it 95%-sound-or-mangled; it's three diseases in one number and not rulable until v2.0 splits them. Caught myself handing Jake the convenient framing I'd said I wouldn't. Logged so S9 doesn't re-inherit the binary. ~90%.
- **Seamed at the turn-20 ceiling rather than read 266KB+ degraded.** Better a fresh S9 reads v2.0 cold than this seat reads it past the ceiling — that's the apparatus's whole thesis. ~98%.

---

## DOWNSTREAM FLAGS (horizon)
- **Coverage is the number that lies, not fidelity.** Will bite at commit (move 8) if S9 reads a high fidelity-within-coverage and treats it as "clean." Do not commit until coverage is high AND clean.
- **Single-hit-anchored convs carry residual offset risk.** Will bite if a short generic span single-hit at a wrong offset and silently anchored a conv wrong. Read the anchor-strength split in v2.0; if single-hit convs look weird, that's where to look.
- **The wrapper-quote ruling is Jake's, against evidence, and it's not a binary.** Will bite if S9 makes the call itself or collapses the three buckets. Hold it for him.
- **Commit ordering is load-bearing:** corpus stays gitignored + uncommitted until coverage clean AND cred-nuke clears. Archive deleted only after commit (re-runs need it).
- **Distrust pre-S7 handoff specifics; trust the disk.** S5/S6 handoffs were mangled broadly (b2 phantom, the S6 wholesale-reattribution of 397 — both caught later). S7 re-read chat logs verbatim to reorient. The §5.1 rule applies to inherited handoff claims, not just live ones.
- **Reference layer is 6+ items behind** — land ENSHRINE at S9 close so S10 boots off a current repo.
