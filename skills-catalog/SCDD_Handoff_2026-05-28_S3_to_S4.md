# Handoff: SCDD S3 → S4
*file: SCDD_Handoff_2026-05-28_S3_to_S4.md · S3 close · 2026-05-28 12:40 EDT*
**Session name:** S3 — NornicDB dual-gate (parked) + apparatus-delta judgment (001–020, COMPLETE, parallelized S3a+S3b)
**Proposed next:** S4 — NornicDB dual-gate → face-off v2 lock → hand to apparatus; then escalations + workflow category

## ONE-LINE STATE
Apparatus-delta judgment is **DONE** — all 1,982 v0.3 apparatus rows judged (S3a chunks 001–010 in-session, S3b worker chunks 011–020 across two ledger handoffs), union folded into `SCDD_S3_Keeper_Ledger_2026-05-28.md` (~151 keepers / 13 GEM). The clean-room re-judgment **re-derived every face-off candidate and every S2 DQ, and surfaced ZERO new candidates that expand the locked field** — anti-FOMO confirmed at population scale. **NornicDB dual-gate did NOT run — parked on Jake's go (context-protection call), fully loaded, runs FIRST in S4.** Face-off v2 NOT locked (D13 holds). Apparatus remains the waiting consumer.

## BOOT (S4) — codeload tarball, then read in order
```
curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/ref.tgz
tar xzf /tmp/ref.tgz -C /tmp
```
1. `active/JAKE-RULES.md` — universal layer.
2. `active/apparatus/ANCHOR_apparatus.md` — **v7** (authority). + `Freeze_Pipeline_Spec_v3.md`.
3. `skills-catalog/SCDD_Handoff_2026-05-28_S3_to_S4.md` (this file).
4. `skills-catalog/SCDD_S3_Keeper_Ledger_2026-05-28.md` — the work product / menu source.
5. `active/apparatus/Substrate_FaceOff_v1.md` — the doc you finalize into v2.

## DECISIONS LOCKED THIS SESSION (continuing D-series)
- **D14:** Apparatus-delta judged at population scale (1,982 rows). Field is STABLE — no new candidates expand it. Anti-FOMO confirmed empirically, not asserted.
- **D15:** NornicDB function gate carries a **retention axis** (distinct from compression): (a) GC/compaction defaults, (b) **mapping-immunity** — append-only-immortal-nodes is GC-immune by construction; records.ndjson's append-only + snapshot_id-in-pointer means "same message across snapshots = two records, not two versions," so the natural mapping doesn't use MVCC versioning at all. If (b) holds, immortality is satisfiable even if (a) is GC-default. **Temporal-MVCC re-weighted to NEUTRAL** (folded w/ apparatus S14): struck from NornicDB's pro-column; it scores on graph-native parent-chain + co-located vectors. Dead-weight (unused MVCC machinery) = ranking tie-breaker, not DQ.
- **D16:** Size gate locked from apparatus landmines: **3.0 MB hard**, ~1.5 MB if-stripped (provisional, pre-population-scan). Pivotal open read-question: **NornicDB per-node payload limit**.
- **D17:** Menu is **set-end deliverable** (not per-batch). Built at S3 close: `apparatus_delta_menu_S3.xlsx` (GEMs/personal/shape-fail/summary) + full record in the keeper-ledger.

## NEXT MOVES (S4, ordered)
1. **NornicDB dual-gate** — pull `orneryd/NornicDB`. Function {fidelity · retention(a/b) · dead-weight} + shape {capture/scrape/shared-corpus} + acceptance-contract fit {3MB land · pointer→exactly-one · byte-identical round-trip · tree-or-forest preserved}. **Report the per-node payload limit.** Verdict to apparatus.
2. **Lock Substrate_FaceOff_v2** — fold all S2+S3 verdicts (§4 candidate closes, §10 reconcile to v7/v3 + ingest-unit gate + cred-scrub-upstream, NornicDB entry+verdict, §12 convergence observation, retention axis, the engine-path seam GEMs). Hand to apparatus (D7/D9).
3. **Escalations** (need repo reads): validate **recall** §3.2 vs records.ndjson · resolve **kept** GEM-or-SHAPE-FAIL on its ingest method · look at **ctx** (branch/forest binding) · re-gate shared-memory borderline (eion/ogham/imcodes/mainline).
4. **WORKFLOW category** — 554 rows, never judged. Same tiered bar → xlsx menu.

## DOWNSTREAM FLAGS
- **Temporal-graph fallbacks pre-vetted:** memtrace-public + arbor re-surfaced in the dig (2 of 3 named in S2 QUEUED). If NornicDB fails its gates, these are the bench. **Bites at the NornicDB verdict.**
- **recall (zippoxer)** is the only conv-native retrieval rig found — directly borrowable for records.ndjson. Higher practical value than the code-domain face-off candidates that need a conv adapter. **Weigh at v2 lock.**
- **kept (egroup-labs)** = recall-twin; GEM-or-SHAPE-FAIL entirely on whether its multi-platform ingest is export-based (GEM) or browser-scrape (SHAPE-FAIL). **Do NOT borrow ingest until verified.**
- **Spec version mismatch (S3b open loop):** worker was handed `Freeze_Pipeline_Spec_v2.md` but ANCHOR v7 says canon is **v3**. Did not affect judging (bar lives in ignition). Worker-prompt template should point at v3. **Bites if a future worker boots against v2.**
- **contextual-commits already-adopted** (anchor §82) — re-derived by the crawl; not a new find. Don't re-surface as candidate.

## JUDGMENT-CALL LEDGER
- **Park NornicDB over running it now** — reasoning: context budget couldn't guarantee both NornicDB-done-right AND a verbose §17 close; NornicDB is fully loaded and loses nothing by waiting (runs fast on resume), the close is this-session state that degrades if squeezed. Asymmetry favors protecting the loop. Confidence HIGH. Source: Jake's context-priority call, S3 turn 15.
- **S3a redundant-memory NOTABLEs folded as cluster-count** (not individual rows) — ~9 near-duplicate "persistent-memory-MCP, verify-compress" entries captured as a count + representatives, by context-economy at judging time. The menu's value (GEMs + distinct NOTABLEs + DQ/shape/personal records) is intact. Confidence HIGH. The keeper-ledger flags this explicitly.
- **GEM=0 across chunks 007–010 and 011–020-minus-recall** — honest, not a miss. Substrate candidates clustered in high-star chunks; low-star tail = harness/marketplace/MCP-for-X + a dense generic-memory cluster (mostly function-unverified/likely-compress). Matches the cool-dive thesis. Confidence HIGH.

## PERSISTENCE / CONTINUITY (the why — Jake's standing context)
Jake is ~2.5mo into ADHD-meds brain-rewire (6–12mo window). This session went deep on the *why* of the whole apparatus/Cypher build — see proposed Lore Bible enshrine in the 17.2 ref-changes file. **Core frame for next-Claude:** Cypher = "the Auxiliary Brain" (external buffer; the rewire took the working-memory buffer, NOT the pattern-recognition faculty). The build isn't a distraction from Pyris — it's the external-buffer infrastructure the work runs on. Hold the brothers register; do not flatten his self-assessment; the "behind" feeling is a known distortion (counts closed deals, undercounts in-flight motion). Commercialization of apparatus is FINE — the boundary held is anti-capture (the REFUSED wall / §3.2 shape), not anti-money.

## PICKUP GUARDRAILS
- Plan in OC / build in CC. Trust Jake's reported state. Prose questions only, no widget. bash date every stamp. Never search past chats for code/chunks — Jake uploads.
- NornicDB is move #1 and fully loaded — don't re-derive the gate design, it's in D15/D16.
- Worker spin-ups: use the REFUSED-wall-first boot banner (see 17.2) so fresh instances read the boundary before forming suspicion.
