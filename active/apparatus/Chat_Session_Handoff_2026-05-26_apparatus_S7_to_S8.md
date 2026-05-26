# Chat Session Handoff — apparatus S7 → S8 (2026-05-26, 10:41 EDT)

*Clean seam, written warm before the irreversible step. S7 booted, byte-confirmed the three compaction-carried mar_a entries (the asterisk is gone), ran the Gate 2 cred/PII master sweep, took Jake's reorder (compile-first, scrub-the-output), and ran Compile. The structural side of Compile is solid — corpus built, 294 reconciled, parents excluded, dedups correct. But the verbatim copy-check was run with a FUZZY method (word-overlap %, phrase-presence) instead of an exact char-diff, so the fidelity gate did not actually verify fidelity. The corpus is built but NOT commit-ready. S8 boots warm on a full budget, redoes the copy-check for real, resolves two attribution calls, runs the cred nuke, then — and only then — commits. The most irreversible step (commit + archive deletion) is deliberately handed to this fresh seat rather than run at the S7 ceiling.*

---

## BOOT (next OC)

Pull the kit (codeload, NOT raw CDN):
```
curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/cref.tar.gz ; tar xzf /tmp/cref.tar.gz -C /tmp
```
Read, in order: `/tmp/claude-reference-main/active/JAKE-RULES.md` (freshness §16; brothers register §1/§4; anti-confab §5; stamp discipline §5.2), then `active/apparatus/`: `ANCHOR_apparatus.md`, `Cypher-Memory-Loop_System_v1.md` (WHY §1–2, fence §5, currency §6), then THIS handoff. Leave `CORPUS.md` cold (entry-shape template only).

Then **RECITE THE ADDRESS** (destination · invariants-with-why · state · next) and **wait for Jake's nod.** Prose only, never a widget. Recital is a payload check — if a claim in here can't be grounded against the kit/disk, say so rather than reciting it (S7's recital caught the S6→S7 handoff being unpushed-at-boot this way).

**Freshness note:** repo reference files still footer at apparatus S2; S3–S7 landed no reference-layer commits. The ENSHRINE list below is overdue and S8 should land it. The anchor's CURRENT STATE runs stale by design — trust this doc.

---

## TURN-END STAMP — backticked inline-code, renders red (do not relitigate)
Format: `turn N · TIME ET [(carried)] · re-anchor X/4 [WARN/SEAM] — dest: brain loop; state: <semicolons>; next: <→ chain>`
Sentence case, single line, semicolons inside state, arrows only in next, no trailing tag, no bold, no all-caps emphasis. Live timestamp from the shell. Re-anchor ~every 5 turns; ~turn 20 ceiling, land at a seam. Seam close on its own line: `turn N · TIME ET · SEAM CLOSED — this seat is complete.`

---

## DECISION LOCKED (do not relitigate)

- **COMPLETE record — all 294 read in full, no sampling, no density-skipping, no grep-as-coverage.** Jake overruled the density-deferral lean in S3; stays overruled.
- **Verbatim = a COPIED span, exact (modulo whitespace). NEW THIS SESSION (S7): the copy-check must be an exact char-diff of the entry's span vs the source span — NOT word-overlap %, NOT phrase-presence.** S7's Compile used a fuzzy similarity metric and called 91–96% overlap "no drift"; that would pass a b1-045-style six-word substitution. Fuzzy-match-as-copy-check is grep-as-coverage in a new costume. The proof it was fuzzy: mar_a-001/002 were replaced to exact source bytes in S7's confirm pass, so an exact diff reads ~100%, yet Compile reported 91–96%.
- Invariants (with the why): one undelineated corpus, anchors index it (no partition); compiled not synthesized, memories.json is navigation never a source; secrets never enter (scrub is a hard gate); the archive never enters chat (CC reads the path, Jake bridges); anchor hot / corpus cold; all writes proposed + ratified by Jake in a batch; prior-run product is never a source for a re-run; don't re-author settled artifacts (Block B).

OC seat = ARCHITECT/ORCHESTRATOR. CC excavates/builds off disk; OC guides; Jake bridges.

---

## WHAT S7 DID

- Booted, recited, caught the S6→S7-handoff-unpushed-at-boot via the recital, re-pulled and confirmed once Jake pushed it.
- **mar_a confirm pass** (targeted, 3 convs, not a full re-fire): 001 REPLACED (single→double quotes + restored `**Section 1G:**` bold), 002 REPLACED (quote + restored bold on the three list labels), 003 VERIFIED. Flags flipped to `[byte-confirmed 2026-05-26 this pass]`. **mar_a asterisk cleared — all 10 lanes solid.**
- **Gate 2 cred/PII master sweep** (manifests-only, archive untouched): 20 manifests, ~68 catches → 25 distinct. Reconciled against the S6 handoff list and caught extras the handoff missed (C-08 jan SCOUT_PASSWORD; the Bambu RTSP cred spans 8 convs / 6 lanes, not 1–2; full P-01…P-12 PII incl. Jake's home address). **Jake confirmed all creds dead/rotated.**
- **MANIFEST-HYGIENE-BREACH found:** 8 actual values leaked into 6 manifests (the "clean" layer) — MHB-03 (likely-minor athlete real names) and MHB-07/08 (partial camera passwords) the sharpest. This falsified "the seeds are value-clean by assumption" and spawned the seed/corpus value-scan requirement.
- **Reorder (Jake's call, adopted — cleaner than S7's proposed copy-check carve-out):** instead of redacting seeds pre-Compile (which collides with the copy-check restoring values from the still-present archive), Compile runs dumb-strict on fidelity, then a cred pass scrubs the *output*. Fidelity and cleanliness become separate steps. S7's carve-out is dropped.
- **Archive deletion decided:** Jake deletes conversations.json + last night's backup once done → moots archive-side hygiene (immortalized source + minor-PII access control). Both dropped. (Seeds/manifests/corpus are NOT the archive; see below.)
- **Ran Compile** (build + verify + report, STOP-gated). Structural gates passed; fidelity gate ran fuzzy (see CURRENT STATE).

---

## CURRENT STATE

**corpus_seed_v1.md built** — `C:\claude-reference\apparatus-archive\corpus_seed_v1.md` (archive ROOT, gitignored), ~618 KB (617,976 bytes), 399 entry headers, 2 DROPPED, 4 FLAGGED, **397 net active. UNCOMMITTED, NOT PUSHED.**

| gate | status |
|------|--------|
| 294 reconciliation (5 parents excluded as proven stale unions; 15 canonical = exactly 294 disjoint) | **PASS** |
| orphan-sweep (all 294 have entries or zero-yield log) | **PASS** |
| ==294 | **PASS** |
| dedup (035→079, 039→075 dropped; 077/071/038 + d2-023 flagged not auto-decided) | **PASS** |
| msg_count-vs-size | **PASS** |
| arithmetic (c1 21+6+7=34; mar_a 15→16) | reported reconciled — re-confirm at proper copy-check |
| **VERBATIM COPY-CHECK** | **UNSOUND METHOD — fuzzy word-overlap/phrase-presence, NOT exact char-diff. MUST REDO.** |

- **Creds:** the corpus MAY contain restored credential values (the dumb-strict copy-check restores `[…—redacted]` markers from the archive). Expected. The cred nuke handles it. Nothing commits until it does.
- **Archive:** still on disk — REQUIRED for the proper copy-check redo. Delete only AFTER commit.

---

## NEXT MOVE — S8 pre-commit gates, in order. Nothing commits until 1 and 4 both clear.

1. **Redo the verbatim copy-check as a REAL exact char-diff** (CC pass, fresh window). Per entry: extract the source span at the entry's conv-uuid + msg pointer; collapse whitespace ONLY; diff exact against the entry's verbatim span. MATCH = whitespace-collapse-identical. DRIFT = any character/word/markdown difference → replace from source (source-or-strike). Do NOT score similarity; do NOT presence-check a phrase. Re-confirm the must-verify set exactly: mar_a-001/002/003 (should now read 100% — they were byte-confirmed), b2-041–047, and the arithmetic. Report drift count + which.
2. **Two attribution/dedup calls — RESOLVED by Jake at S7 close:**
   - **d2-023 (entry 397) — LOCKED: primary attribution stays 2526703b.** The MSG 32 brain-soup ruling is the heart of the entry and was made there; S6's wholesale reattribute-to-41bc76dc was wrong (Jake's call). One residual sub-step for S8 to settle with the texts — does NOT change 397's primary attribution: the MSG 33 *retrieval* inside 397 is a quote of an S1 verbatim that originated at 41bc76dc → attribute that portion to origin per ORIGIN≠REVIEW, or dedup it if 41bc76dc already carries that verbatim.
   - **077/071/038 — LOCKED: keep all 3.** Jake's call: it's iteration and evolution (origin → articulation → SOP-banking) and belongs in the complete-record corpus. No drop.
3. **Cred nuke on the corpus** (CC pass): targeted at the Gate-2 master locations (CRED_PII_MASTER_2026-05-26.md) + a dumb full-corpus regex backstop (sk-/sk-ant-/re_/eyJ/postgres://user:pass@/rtsp://…@/CAMERA_PASS=) to catch anything the original scrub missed entirely (MHB proved it's fallible). Redact values → `[<descriptor> — redacted]`, location+type only, never echo a value. Any NEW-CRED-FOUND not on the dead list → back to Jake to rotate before commit.
4. **Verify clean** — re-run the regex backstop; confirm zero values remain.
5. **Commit** — only after 1 + 4 clear and the two calls are resolved. Move corpus_seed_v1.md from the gitignored archive root to its tracked home, commit, push.
6. **Tell Jake to delete** conversations.json + last night's backup.

---

## BLOCK B — still not a committed file
Block B (the hardened `CC KICKOFF — apparatus LANE EXCAVATION` template) is referenced in JAKE-RULES and handoffs but is NOT a file in the kit. If any lane re-read is forced, get it verbatim from Jake; do NOT re-author from a description (S5's logged drag, Ruling 4). Committing it is ENSHRINE item 3.

---

## ENSHRINE THESE (S8 → repo, proposed-then-ratified). Overdue — JAKE-RULES still footers S2.
1. **Stamp format** → JAKE-RULES §5.2 (inline-code/backticks, renders red; content rules; failure history).
2. **Compaction-carry rule** → Loop spec fence. SHARPENED in S7: *any entry whose seed-landing crossed a compaction boundary is unverified regardless of a pre-boundary source read — what survives the boundary is the summary's rendering.* (The flag `[verbatim confirmed pre-compaction this pass]` was the tell.)
3. **Block B** → committed to repo.
4. **Cred/PII master sweep list** → pre-ingest checklist.
5. **Match-standard** (S7): whitespace-collapse = MATCH; character substitution / stripped markdown / word change = DRIFT. The copy-check's operational definition.
6. **Copy-check must be exact, not fuzzy** (S7): no word-overlap %, no phrase-presence; exact char-diff of entry-span vs source-span. Goes in the Loop spec fence next to the match-standard.

---

## JUDGMENT LEDGER (S7) — call · reasoning · confidence
- **mar_a 001/002/003 → targeted confirm pass (not full re-fire, not Compile-deferral).** They were never-byte-copied (summary-carried); b1-045 proved that drifts; the pass is 3 convs at known offsets, verifies+fixes in one move, asymmetric cost. Came back 2 REPLACED / 1 VERIFIED — vindicated. ~90%.
- **Adopted Jake's compile-first reorder over my copy-check carve-out.** His separation of fidelity vs cleanliness is structurally cleaner and removes a coupling I'd have had to get exactly right. ~95%.
- **Let Compile run despite the reflex-approve.** Build-only, STOP-gated, gitignored output, non-destructive (reads seeds, writes one local file) — nothing irreversible to stop. Correct to let it finish. ~98%.
- **Flagged the fuzzy copy-check instead of blessing "gates passed."** The fidelity gate is the corpus's entire reason to exist; a similarity metric is not a verbatim check. Holding the line here over momentum. ~90% it genuinely needs the exact redo; the 10% is "maybe the fuzzy pass happened to miss nothing," not a bet to take pre-commit.

## DOWNSTREAM FLAGS (horizon)
- **The exact copy-check (gate 1) is the difference between a verbatim corpus and a plausible-looking one.** Do not let S8 re-run it fuzzy to save time.
- **Commit ordering is load-bearing:** corpus stays gitignored + uncommitted until exact-copy-check AND cred-nuke both clear. Archive deleted only after commit (the copy-check needs it).
- **Reference layer is 6 items behind** — land ENSHRINE at S8 close so S9 boots off a current repo.
