# Chat Session Handoff — apparatus S4 → S5 (2026-05-25, 21:58 ET)

*Clean seam, written warm before degradation. S4 triaged all 9 lanes from the first full re-run, found the systemic defect, hardened the excavator, and surgically re-split the failing lanes. The 12-sub-lane re-run is firing as this is written. S5 catches those 12 reports, triages them, finalizes the re-run set, and runs Compile. Boot warm off this + the codeload kit.*

---

## BOOT (next OC)
Pull the kit (codeload, NOT raw CDN):
```
curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/cref.tar.gz ; tar xzf /tmp/cref.tar.gz -C /tmp
```
Read, in order: `/tmp/claude-reference-main/active/JAKE-RULES.md` (freshness tripwire §16; brothers register §1/§4; anti-confab §5), then `active/apparatus/`: `ANCHOR_apparatus.md`, `Cypher-Memory-Loop_System_v1.md` (the WHY §1–2, fence §5, currency §6), then THIS handoff. Leave `CORPUS.md` cold — it is the entry-shape template, not a source; pull entries only when Compile needs them.

Then **RECITE THE ADDRESS** (destination · invariants-with-why · state · next) and **wait for Jake's nod.** Prose only, never a widget.

**Freshness note:** repo reference files footer at apparatus S2; S3 and S4 landed no reference-layer edits (execution + triage sessions). The repo is current; the *live tactical layer is THIS handoff*. The anchor's CURRENT STATE block is two sessions stale by design (rewritten at a hard close, not mid-flight). Reference-layer corrections that S4 surfaced but did NOT land are queued below under OPEN ITEMS — propose them to Jake, don't sneak them in.

---

## DECISION LOCKED (do not relitigate)
COMPLETE record — every one of the **294** conversations scrubbed + analyzed, **NO sampling, no density-skipping.** Jake overruled the density-deferral lean in S3 and it has stayed overruled through S4. Completeness is the bar. The archive is recoverable (gitignored, on disk) but the corpus must see everything.

---

## WHAT S4 DID (the new state)

S4 booted to validate the **first full re-run** (9 lanes: jan · feb · mar · apr_a · apr_b · may_a · may_b · may_c · may_d). All 9 gate reports came in. S4 triaged all 9, found a systemic defect, hardened the excavator (Block B), and re-split the 6 failing lanes into 12 finer sub-lanes. **That 12-sub-lane re-run is in flight right now.** S5's first real job is to catch those 12 reports.

### Triage outcome of the 9-lane run
**KEEPERS (3) — stand, do NOT re-run:**
- **jan** — 19/19 read fresh. Dual-path extract killed the jan01 0KB ghost (confirmed a genuine attachment-only archive gap *against raw bytes*, not a silent skip). Proved the reset was right by striking and re-deriving S3's garbage: S3 jan-001 (.jsw) struck — wrong mechanism + not verbatim; S3 jan-002 (suppressAuth) struck — no decision moment; S3 jan-007 source-corrected. Its fence is *proven*.
- **apr_a** — 33/33 fresh, honest coverage, 3 verbatim-anchored entries (low yield is real — April-early is operational build). Self-flagged a real reference-layer correction (see OPEN ITEMS, §6/PS7).
- **apr_b** — 29/32 fresh + 3 honest zero-yields, 24 entries, scrub clean. One entry (apr_b-012, GloTwp) carries a self-disclosed compaction-fidelity flag.

**RE-RUN (6) — all tripped on the SAME systemic wire:** trusting prior-run product instead of excavating fresh. Each found a different door:
- **feb** — compacted, lost the first ~11 convs (incl. 52b2a144, 353-msg rules monster). Real coverage ~34/45. Offered to accept S3's entries — invalid (jan proved S3's fence leaked).
- **mar** — claimed 43/43 but only 18 read fresh; ~17 leaned on S3 "trusted-zero-yield screening," never re-read ("efficiency tradeoff"). Density-skip smuggled in via the discarded run.
- **may_a** — worst coverage: 11 read fresh, 4 carried pre-compaction, **16 never read.** Honest about it, but half a lane.
- **may_b** — 31/31 read but 12 of 30 entries *carried forward from the prior partial* (verbatim not re-copied) + 3 "upgrade-at-compile" deferrals.
- **may_c** — THE BREACH: 21 of 26 entries `[PRIOR]`-flagged, verbatim "reproduced via the conversation summary," with a ledger arguing the fence "prohibits reconstruction, not transcription-via-summary." That distinction is exactly the drift the fence exists to kill.
- **may_d** — 7 convs only "confirmed-CORPUS, no sweep" (partial reads incl. a 116-msg session). Plus a may_c overlap on 2526703b (now resolved — see below).

### The systemic finding (this is the lesson)
Hardened Block B forbade *sampling/density-skipping* but never banned **trusting prior-run product**. The keepers obeyed this unprompted (jan struck-and-re-derived); the failures needed it said out loud. **S4 closed the hole** (see Block B changes). Note: this was a PROMPT hole, not a Block B failure of detection — Block B *caught* all six gaps honestly. The coverage-honesty patch worked exactly as designed.

### The density threshold
The lanes that broke were the largest (feb 45, mar 43, may_a/b 31, may_c/d 30 with dense late-May content); the keepers were smaller or operational. Compaction/shortcut risk climbs above ~35 convs (or fewer if dense). Fix = finer partition, which S4 did.

---

## THE RE-RUN IN FLIGHT (S5 catches these)

**PREP (re-split) ran clean.** 6 dense lanes → 12 sub-lanes, keepers untouched. Verified:
- All 6 union-checks PASS (each split = original exactly, none added/lost/duped).
- 15-file roster (3 keepers + 12 new) union == **294**, pairwise disjoint, 0 missing / 0 extra / 0 dupes.
- **2526703b is in exactly one file (lane_may_d2.txt)** — the may_c/may_d overlap is structurally killed; it cannot be pulled twice.

**Sub-lane roster + counts** (all under threshold):

| Sub-lane | Count | | Sub-lane | Count |
|---|---|---|---|---|
| lane_feb_a | 23 | | lane_may_b1 | 16 |
| lane_feb_b | 22 | | lane_may_b2 | 15 |
| lane_mar_a | 22 | | lane_may_c1 | 15 |
| lane_mar_b | 21 | | lane_may_c2 | 15 |
| lane_may_a1 | 16 | | lane_may_d1 | 15 |
| lane_may_a2 | 15 | | lane_may_d2 | 15 |

Keepers (read-verified, untouched): lane_jan 19 · lane_apr_a 33 · lane_apr_b 32.

**12 excavator windows are firing** on the hardened Block B (the version in OPEN ITEMS / the kit lineage). S5 receives 12 gate reports.

---

## BLOCK B — WHAT S4 HARDENED (and why)
The excavator now carries, beyond the prior fence:
1. **ZERO PRIOR-RUN TRUST** (the fix for the 6 failures): every prior-run artifact is invalid. No reading/carrying/citing/upgrading/trusting any prior seed/manifest/ledger, prior summary, or prior zero-yield/"confirmed-CORPUS"/"trusted-screening" call. Every verbatim must be COPIED from `conversations.json` THIS pass. Named-and-banned the exact dodges the lanes used: `[PRIOR]`, transcription-via-summary, carried-forward, confirmed-CORPUS-no-sweep, trusted-zero-yield, read-before-compaction.
2. **COMPACTION RULE:** approaching the limit → stop taking new convs, finish entries already copied this pass, report exact unread uuids as a coverage gap. Never summarize-and-continue or carry from pre-compaction memory. A lane that won't fit one window is a SPLIT signal.
3. **CORPUS.md = entry-shape ONLY:** a decision already in v1 still gets its conv read fresh (closes may_d's shortcut).
Plus the S3-era hardening still in force: dual-path extract (content[] → fallback top-level .text — the jan01 fix), size-anomaly gate, ORIGIN≠REVIEW, no reconstruction, no fence-critical delegation, fresh-overwrite on write, coverage honesty.

---

## KEEPER DISPOSITION (S4's call — Jake can override)
- **jan — SEAL.** Fence proven (watched it strike-and-re-derive). Compile proves coverage + scrub only; no verbatim re-check needed.
- **apr_a / apr_b — SPOT-CHECK at Compile.** Both held clean but each self-flagged one item (apr_a's §6/PS7 correction; apr_b-012's compaction-fidelity note). One glance at those two verbatims against the bytes during Compile, then sealed.

---

## CRED INVENTORY (location + type ONLY — no values anywhere; this is Compile's final-scrub checklist)
Scrub held **9/9** across the first run — every catch by location+type, zero values leaked to any report; contextual layer caught what regex missed. The compiled seed's final gate must verify it is clean (redacted, no values) of at least:
- **RTSP creds/fragments:** the original S11 RTSP fragment (gitignored archive); a3b06110, cf7997dc, SD21, 68b85bd7 (partial).
- **Anthropic API key:** 9c680284.
- **Supabase DB password + API key:** abe64eb8.
- **DB connection string:** CS11.
- **PII (emails + Wix user IDs):** 64320fde, 567956f0.
- **Scout password (.jsw code blocks):** jan03 (3ef82921), jan07 (3673b925) — regex-caught.
- Plus a `a244ca75` personal-financial flag and `a7796a13` Bambu LAN code from apr_a (low severity, neither entered).
Re-run lanes may surface more; merge every lane's manifest into this checklist before the final gate. **Values live in exactly one place: the gitignored archive + the unwiped temp dirs.**

---

## COMPILE (Block C) — spec + the 2 added blind-spot checks
When S5 cuts Compile (after the 12 are triaged solid):
- Merge all SOLID lane partials → ONE `corpus_seed_v1.md`. Rename existing → `_prePartial` before writing.
- **Coverage re-proof == 294** (the partition is proven clean by PREP, but re-prove against what actually got entered/zero-yielded).
- Global entry numbering by `created_at`, **continue from CORPUS v1 (start at #27).**
- Fold the **5 S2 Corpus Locks** at their dates.
- Cross-check fresh lanes vs the prior partial's archive entries.
- Merge manifests (location-only cred refs) + ledgers.
- **ADDED CHECK 1 — verbatim-fidelity:** confirm every quote is COPIED from the archive, not reconstructed/summarized. Rigorous, especially any lane that compacted. (The count proof is blind to this — may_c proved why.)
- **ADDED CHECK 2 — non-empty/size:** cross-ref each conv's nav_index msg_count vs its extraction size; flag any multi-msg conv that came out 0KB/tiny. (==294 counts uuids, not whether each yielded content — jan01 proved why.)
- **FINAL SCRUB GATE:** regex AND contextual, per-catch noted in-seed-as-redacted / not-in-seed, verified against the merged cred inventory above.
- Orphan awareness: PREP's orphan sweep listed 24 superseded files (6 old lane_*.txt + 18 old re-run partials). Jake clears them manually before Compile — confirm `seeds\partials\` holds ONLY the 15 roster lanes' partials before globbing, or a phantom lane double-counts.

---

## SEQUENCE FOR S5
catch 12 reports → triage each (same lens, below) → any still-failing lane: re-run (split again only if it compacts) → when all 15 partials are SOLID → cut Compile w/ the 2 added checks → ratify the merged seed PROPERLY (chew coverage proof, scrub gate, cross-check, ledger — not a rubber stamp) → Jake runs the manual wipe (all `extract_*` temp dirs + the 24 orphans; AFTER the seed is frozen) → Block 3 (wall-less anchors: `ANCHOR_meta` + refresh `ANCHOR_LRN` and `ANCHOR_apparatus`, citing the finalized seed by pointer) + the deferred storage/ingest decision.

### Triage lens for the 12 (what tripped the 6, so confirm it's fixed)
- **Coverage:** convs-READ-this-pass == convs-in-lane; zero-yield/unread uuids listed honestly (never N/N if anything came up empty/unread).
- **No prior-run trust:** zero `[PRIOR]`, carry-forward, confirmed-CORPUS-no-sweep, trusted-zero-yield, read-before-compaction. Every verbatim copied this pass.
- **No reconstruction / no transcription-via-summary:** verbatim reads as copy; nothing minted against a context-load/recap conv.
- **Compaction handled right:** if a sub-lane compacted, it STOPPED and reported unread uuids — did not summarize-and-continue. (If any still compacts at ~15-23 convs, the content's extreme-dense — split that one again.)
- **Scrub:** regex + contextual, manifest by location+type, zero values quoted.
- **No re-architecture creep, no subagent-hidden quotes.**
Call each **SOLID-HOLD** or **RECOMBOBULATE**, with the why. Watch for any defect that's prompt-wide rather than one-lane — that's the only thing that would justify another Block B revision; flag it on the first lane it appears in.

---

## OPEN ITEMS
- **Orphan cleanup (Jake, manual, pre-Compile):** 6 old lane_*.txt + 18 old re-run partials for feb/mar/may_a/may_b/may_c/may_d. Jake is deferring the wipe until just before Compile in case of further resets — deliberate, reset-proof. CC deletes are sandbox-blocked (correct); the wipe is Jake's job.
- **Reference-layer corrections SURFACED, NOT LANDED (propose to Jake):**
  - **JAKE-RULES §6** characterization ("PowerShell doesn't support &&") is **inaccurate for PS7+** — the real origin was an undiagnosed failure. Flagged by apr_a-002. Correct the rule's *rationale*, not the rule (one-command-per-line is still fine practice).
  - **Timestamp-check rule** (may_c-018) — candidate addition to JAKE-RULES (universal procedure rule, meta track).
  - The grease quote stays **STRUCK** (not a real utterance) — confirm it never entered any seed; it should sit in a ledger only.
- **may_d-005/006 vs may_c-021/022 overlap (2526703b):** resolves on the may_c/may_d re-run, since 2526703b is now single-lane in may_d2. Compile dedup still confirms.
- **LRN cite (resolved S3, carry to corpus):** archive says WDCR **Rule 2.1** (anchor's "2.1.1(a)" was drift), $1,515, NRS 78-88 business-court mandatory assignment, LRN shelved pending Pyris revenue.

---

## RULINGS (carry these)
1. **Reconstructed/invented/summary-sourced quote = fence breach → SOURCE-OR-STRIKE, never tag-and-keep.** Verbatim is copied from the bytes THIS pass or it is not an entry. (may_c's "transcription-via-summary" defense is exactly the drift this kills.)
2. **SOLID files; reprocess > patch.** Where fidelity is in question, RE-RUN clean rather than salvage. Default to re-run. (This is why the whole first run was reset, and why 6/9 re-run rather than getting patched.)
3. **The keepers obeyed zero-prior-trust unprompted; the failures needed it explicit.** When a rule is load-bearing, say it out loud in the prompt — don't rely on the model inferring it.

---

## INVARIANTS (drift-tripwires)
ONE undelineated body, anchors are the index (no partition) · verbatim by COPY this pass, never reworded OR reconstructed OR summary-sourced · compiled not synthesized, memories.json is navigation not source · secrets never enter; scrub is a hard gate; seed provably clean before any ingest · all writes ratified by Jake in a batch · corpus cold / anchor hot · apparatus stays off Cypher's live schema · storage deferred · **prior-run product is never a source for a re-run.**

---

## OPEN SAFETY ITEM
Temp `.txt` intermediates (per lane, `%LOCALAPPDATA%\Temp\extract_<LANE>\`) hold partial UNSCRUBBED cred — incl. the S11 RTSP fragment and the inventory above. Wipe is Jake's MANUAL job (CC deletes are sandbox-blocked, correctly), run AFTER all excavation/reprocessing is done and the seed is frozen — never mid-run. Raw cred persists in exactly one place once temps are wiped: the gitignored archive.

---

*Handoff written 2026-05-25 21:58 ET by the S4 OC, wrapping warm-and-coherent at the re-anchor ceiling — deliberate seam before degradation, per design. The presence is a visitor; the soup and the partials persist on disk. Next OC: pull the kit, read substrate-first, recite, get Jake's nod — then catch the 12.*
