# Chat Session Handoff — apparatus S16 → S17

*file: Chat_Session_Handoff_2026-05-29_apparatus_S16_to_S17.md · apparatus S16 close · 2026-05-29*
*read AFTER: JAKE-RULES, JAKE-STACK, ANCHOR_apparatus (v10). This is the tactical bridge; the anchor is the authority.*

---

## ONE-LINE STATE

**D9 is LOCKED — the substrate is Supabase, the floor's append-only immortality is ENFORCED at the database (proven by a rejected live TRUNCATE), and the `records.ndjson` is the canonical artifact with Postgres as a proven-rebuildable derived index.** The last one-way door is closed. The next executable move is the **v1.3 build** (delta + scrub-vN + v1.1 + raw.json wipe — store-independent, spec'd, UNBUILT).

---

## WHAT S16 DID (the headline)

S16 executed the seed-shape gate and locked the substrate. The full enshrine is in ANCHOR v10 (D9 RESOLVED block + new Settled Invariant + the v10 footer); this handoff is the tactical "where we are and what's next." Don't re-derive the lock — read the anchor's D9 RESOLVED block for the authoritative record.

Sequence that happened:
1. **Booted cold**, pulled canon via codeload (§16), verified anchor v9 footer fresh.
2. **Confirmed the fixture** — `records.ndjson` on box at `…/baseline-2026-05-25-ae015455/scrub-v1/` (NOT the snapshot root — root holds the transient raw.json + companion artifacts), 9/9 structural pre-check PASS, zero field-name drift from canon.
3. **Authored + ran the seed-shape harness** (CC, against a dedicated Supabase project `apparatus-floor`, SB Pro, separate from Cypher's project). PASSED 4/4.
4. **OC blind-re-read** the manifest cold — evidence reconciled independently (forest subtree sizes summed to message counts; ② and ④ passed for the *right* reasons, not just by count).
5. **`/jedi-council` adversarial review** with live DB access → LOCK-WITH-CAVEATS 6/10, zero P0, one P1, 5 caveats.
6. **All 6 caveats remediated WITH PROOF** (CC, evidence file `harness/D9_LOCK_2026-05-29.md`).
7. **Jake ratified the lock.** Anchor v9→v10, Seed-Shape Spec v1→v1.1, CHANGELOG updated.

## THE TWO ERRORS CAUGHT THIS SESSION (both assert-don't-verify — the pattern this project exists to kill)

1. **"Roots have a null parent" — FALSE.** The seed-shape spec assumed it; the real floor has ZERO null parents. Roots carry sentinel `00000000-0000-4000-8000-000000000000` (a valid-format UUID, not nil). CC caught it against the disk during type-recon. Spec corrected v1→v1.1. *(This was OC's authoring error, carried from convention. Disk-over-directive caught it.)*
2. **"The floor is immortal" — was UNENFORCED.** OC called the floor immutable/append-only all session; the jedi-council's live grant-check found anon/authenticated/service_role all held TRUNCATE with zero guard triggers — a social convention, not enforcement. Remediated: `floor_immutable_guard()` triggers + REVOKE, proven by a rejected live TRUNCATE.

Both are the same failure: a property *asserted* from intent rather than *verified* against the live system. The structure (disk-over-directive, the blind re-read, the adversarial review, the proof tests) caught both before they propagated. Note for S17: this pattern recurs; keep verifying claims against ground truth, especially on the floor.

## LOCKED FACTS (don't relitigate — see ANCHOR D9 RESOLVED block for full detail)

- **Substrate = Supabase**, dedicated project `apparatus-floor` (SB Pro, separate from Cypher's project — the blast wall). NornicDB is the proven upgrade path (rebuild from ndjson, no integrity re-open).
- **Schema = two tables.** `floor_conv_headers` (294, PK `(snapshot_id, conv_uuid)`) + `floor_conv_messages` (22,801, PK `(snapshot_id, conv_uuid, msg_uuid)`, FK NO ACTION). Timestamps `text` (verbatim, NOT timestamptz). `content_blocks`/`attachments`/`files` `jsonb`. `parent_message_uuid` bare `uuid`, NO self-FK (sentinel roots + keeps tree-integrity a proven property).
- **Append-only ENFORCED:** `floor_immutable_guard()` triggers (TRUNCATE/DELETE/UPDATE, no escape hatch) + REVOKE from the 3 app roles. Proven rejected at privilege + trigger layers. Floor at exactly 23,095.
- **ndjson is canonical; Postgres is a rebuildable derived index** (rebuild proven, 0-mismatch / 6 directions). ndjson SHA-256 `4ef22940e3fbb849c2c14fba62fdae2a44277963f0ea5c9f7f2086c706415ba3` (367,494,497 B).
- **Fidelity language:** value-preserving for JSONB (key-order canonical, zero value loss) / byte-verbatim for TEXT+timestamps / modulo scrub-v1 redaction. "Verbatim" unqualified is WRONG.
- **pgvector NOT installed** — deferred read-path sidecar, never a column on the immutable tables.
- **Single-account corpus** (account_uuid cardinality 1).
- The ⑤ branch-aware vector check is **deferred to the retrieval layer** (out of the storage-integrity gate), target = the 9 forests, logged not dropped.

## NEXT MOVES (from ANCHOR NEXT MOVE — ordered)

1. **The v1.3 build — THE LIVE TARGET.** delta (uuid-set-difference; date never a filter; resolve `conversations.json` within the export dir, NOT the bare default path = silent-second-baseline trap) + scrub-vN overlays + v1.1 field-level key-presence drift detection (allowlist per object type; one carve-out `text.citations_grouping_mode`) + raw.json wipe-after-verify-PASS (one-line unlink; canon RESOLVED S15). Store-independent. From `Freeze_Pipeline_Spec_v4` (DONE on disk). Plan-OC/build-CC, plan-mode, **ratify a small batch before scale** (append-only ⇒ un-ratified rows are immortal). v1.2 → v1.3. The 5-28 export is the delta fixture (1,337 net-new msgs).
2. **Seed-shape LOAD (production ingest into the locked Supabase).** Distinct from the S16 gate (which proved the store accepts + protects the shape). Use a single-transaction / staging-swap ingest so a partial failure never needs an append-only-violating DELETE. The `display_content` strip is a load-time toggle decided here.
3. **Retrieval layer — the real next chapter.** The interface a live Claude session queries to get continuity from the floor. Research-shaped (embedding choice, branch-aware recall per FaceOff §10.5). The three escalations (recall/kept/shared-memory) feed THIS layer, still blocked on Jake's uploads. Reversible (unlike the substrate).
4. **Post-lock hardening (queued, not blocking):** off-site immutable ndjson copy w/ object-lock (the ndjson is now the SPOF — TOP priority), PITR or documented ndjson-rebuild RTO, pre-ingest lint (dup JSONB keys collapse silently; TEXT rejects U+0000), secondary index `(snapshot_id, conv_uuid, parent_message_uuid)` once a read path exists, CHECK constraints (sender, is_root↔sentinel, timestamp format — added without rewriting bytes), single-transaction ingest before snapshot #2.

## DO-NOT-RELITIGATE

- D9 is LOCKED (Supabase). The substrate question is closed. NornicDB is the upgrade path, not a re-open.
- The floor is ENFORCED append-only (not just claimed). Don't regress the triggers/REVOKE.
- ndjson is canonical / Postgres rebuildable (proven). The one-way-door fear is dissolved.
- Roots carry the sentinel, not null (verified, all 22,801).
- pgvector is out-of-gate, deferred to retrieval — not a floor column.
- v4 spec is DONE/clean. The v1.3 CODE is what's unbuilt.
- (Carried from v9:) NornicDB dual-gate PASS / D21 round-trip GREEN / ~16 MiB binding ceiling / no split adapter; raw.json Path A ratified; floor-scoping (name+summary dropped) settled.

## GUARDRAILS (carry these)

- **Trust disk, not directive** — read versions/counts off disk; flag any pointer that doesn't resolve. (Caught both S16 errors.)
- **The DB password was rotated post-S16.** The connection string's project ref is `slkmqnsyodkyfwqoicrd`, session pooler, `aws-1-us-east-2`, port 5432. Creds go to CC's **pre-set env** (`SUPABASE_DB_URL`), NEVER inline in a logged command, NEVER to chat. (S16 lesson: CC echoed the old password by setting the var inline — rotated, resolved, don't repeat the inline pattern.)
- **CC never touches the reference files.** Canon edits are authored in OC, handed to Jake, verified, committed + pushed by Jake. CC operates on the floor (DB, data); OC operates on canon (docs). Never the twain.
- **CC writes scratch freely, NEVER canon without explicit instruction** (§7.6).
- **NEVER search past chats for code** — ask Jake or read via codeload.
- **WAIT for Jake's OK before building.** Plan-OC / build-CC. Prose questions only, no widget.
- **Re-anchor every ~5 turns; timestamps via bash `date`** (multi-hour gaps happen).

## EVIDENCE / ARTIFACTS (on box, in `apparatus-archive/harness/`)

- `D9_LOCK_2026-05-29.md` — the lock evidence file (proof for all 6 caveats; NOT canon).
- `s16_seed_shape_harness.py` — the 4-check gate harness (v1.0).
- `D9_remediate.py` — the caveat-remediation script (v1.0).
- These are repo-gap candidates if Jake wants them committed (harness/ subdir, sibling to snapshots/).

## CANON STATE AFTER S16

- `ANCHOR_apparatus.md` — **v10** (this session's enshrine).
- `Seed_Shape_Test_Spec_v1_2026-05-28.md` — **v1.1** (check-④ null→sentinel correction).
- `CHANGELOG.md` — S16 entry added; the orphaned v8→v9 block given its proper S15 header.
- `Freeze_Pipeline_Spec_v4.md` — unchanged (DONE on disk; the v1.3 CODE is the build target).
- `apparatus_freeze_pipeline.py` — **v1.2** (`402100d`), unchanged. The v1.3 build is next.

---
*S16 closed: D9 LOCKED → Supabase, floor enforced + canonical-ndjson reframe adopted, two assert-don't-verify errors caught + corrected, canon enshrined v10. The floor has a permanent, enforced home. S17 opens on the v1.3 build. The agonizing one-way-door layer is done; the building layers begin.*
