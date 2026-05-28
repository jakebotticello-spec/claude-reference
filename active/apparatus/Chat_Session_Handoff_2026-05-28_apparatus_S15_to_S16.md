# Handoff: apparatus S15 → S16

*file: Chat_Session_Handoff_2026-05-28_apparatus_S15_to_S16.md · v1 · S15 close · 2026-05-28*

**Session name:** S15 — Substrate result fold-in (FaceOff v2 + D21 round-trip), anchor v9 enshrine, raw.json Path A ratify, seed-shape test lock, SCDD merge-back
**Proposed next session name:** S16 — Seed-shape test → D9 substrate lock + the v1.3 build (delta / scrub-vN / v1.1 / raw.json-wipe) *(rename once the lock lands)*

---

## ONE-LINE STATE

The substrate question is **unparked and one test from locked**: SCDD delivered FaceOff v2 (two co-leads, both dual-gate PASS — NornicDB + Supabase, Supabase the recommended lower-regret first lock), the D21 round-trip is empirically CLOSED (byte-identical at 1.37× max record across a cold reboot), the anchor is enshrined **v9** on HEAD (substrate v2-delivered/lock-open, raw.json Path A ratified, decay→D20 hard gate, v4-spec-DONE recorded), and the **seed-shape test is LOCKED as the D9 gate** (`Seed_Shape_Test_Spec_v1_2026-05-28.md`). SCDD folded back in — apparatus/main is now the single thread and holds the lock (D9). The two executable moves left are the **seed-shape test → blind re-read → D9 lock** and the **v1.3 build** (store-independent; parallelizable with the lock).

---

## WHAT S15 DID (honest record)

- **Booted v8 (Jake-uploaded) + pulled the repo; caught a repo-vs-canon fork on turn 1:** a `Freeze_Pipeline_Spec_v4.md` was already on disk when canon (v8 footer + S14 handoff §17) said the v4 pass was unbuilt/held-for-S15. Stopped instead of rebuilding it. Resolution (Jake): he'd landed v4 himself and not updated the handoff — artifacts lagged the work. Diffed v4 vs v3, verified it clean/surgical (v3 + §2.0 + the §2.1/§6/§7 edits). **v4 spec pass = DONE.**
- **raw.json decided — Path A.** Walked Jake through the wipe-vs-retain call; he chose Path A at a firmer scope than the original invariant: wipe after Stage 3 verify-PASS **and never staged to any retained/backed-up surface (incl. the NAS)**. Anthropic's export is the byte-verbatim re-pull source.
- **Ran the NornicDB dual-gate cold from source** (independent re-run requested by SCDD S4, findings stripped). Verdict: fidelity PASS / retention PASS (both (a) default-off AND (b) mapping-immunity) / dead-weight DING / shape PASS / acceptance 4/4, binding ceiling **~16 MiB** (`walMaxEntrySize`), no split adapter, default-local embedding (no corpus egress). One soft axis flagged: byte-identical round-trip on the multi-MB *string* path (the existing large-node test exercises *embeddings*) — rated MEDIUM-HIGH, named as a pre-lock gate (D21).
- **Converged with SCDD blind, then reconciled.** Zero verdict divergence. SCDD S5 then **ran the round-trip empirical GREEN** (D21 CLOSED) on Castle Black CT 999 (disposable LXC, torn down clean): 4,122,695-byte adversarial inline string, byte-identical + sha256-stable across a full container reboot, vlog survived. (An in-lane attribution cross-wire over which read found the 16 MiB ceiling / held the round-trip open was caught + corrected mid-session — facts held; Jake's resolution: doc was SCDD's *response* to my verdict, not a blind parallel read. Settled; do not relitigate.)
- **Enshrined anchor v8→v9** (surgical edits on the real file, no retype): substrate confidence flags OPEN→v2-delivered + round-trip CONFIRMED (with 16 MiB ceiling), D21 closed, graveyard decay-landmine sharpened → D20 hard gate, raw.json Path A ratified + DECISION block removed + CURRENT-STATE/NEXT-MOVE flipped to RESOLVED, NEXT MOVE #1 split-adapter prediction CLEARED, #2 v4-spec marked DONE. Delivered downloadable; **Jake committed v9.**
- **Revised the CHANGELOG on live HEAD** — caught a push-behind (HEAD had gained the SCDD S5 Castle Black entry after my first pull); rebased the S15 entry onto current HEAD so the Castle Black entry was preserved, not clobbered. **Jake committed.**
- **Verified SCDD made zero anchor changes** (byte-diff: start-v8 == HEAD-v8 identical) — my v9 clobbered nothing. Checked the bytes, not the doc's self-claim.
- **Read the SCDD S1–S6 merge-back** — SCDD folded in. Reconciled it vs current (it was authored pre-v9-push, so its §8.3/8.4/8.5 "to-do" items were already DONE).
- **Locked the seed-shape test** as the D9 gate (`Seed_Shape_Test_Spec_v1_2026-05-28.md`), grounded on FaceOff_v2 §8/§10/§13.
- **Pulled the build home** to apparatus/main (the parallel lane's sole justification — the blind dual-gate — is spent). Routed `cool_gems_menu.xlsx` (the missing menu).

---

## VERIFIED GROUND-TRUTH — do-not-relitigate

- **v4 spec is DONE + clean** (Jake landed it; verified v3 + §2.0, surgical, no architectural change).
- **Anchor is v9 on HEAD** (footer confirms). FaceOff_v2 + both `apparatus_delta_menu_S3.xlsx` / `workflow_menu_S6.xlsx` are in the repo.
- **NornicDB: dual-gate PASS, acceptance 4/4, D21 round-trip GREEN (empirical).** Binding ceiling ~16 MiB (not "no cap"); no content-block split adapter; default embedding is local.
- **Substrate field settled at population scale** (1,982 apparatus + 459 cool + 554 workflow judged; zero field-expanding candidates). Stop re-broadening.
- **Continuous-Claude-v3 does NOT gate** (function FAIL — compresses corpus). The lock is a clean Supabase-vs-NornicDB selection, not a fork-vs-build.
- **raw.json Path A ratified canon-side** (wipe-after-verify-PASS + never-to-any-backup-surface). The §Secrets invariant was unchanged (already said "raw wiped"); Path A makes code match it.
- **The lock is apparatus's (D9), NOT YET MADE** — gated on the seed-shape test.

---

## DECISIONS LOCKED THIS SESSION

1. **raw.json = Path A** (wipe after verify-PASS; never to any retained/backed-up surface).
2. **Anchor enshrined v9.**
3. **D20 = HARD lock-time config gate** (pin decay/TTL/auto-links/embeddings OFF if NornicDB; the vendor `example.yaml` ships them ON).
4. **Seed-shape test LOCKED as the D9 gate** (5-point acceptance contract; baseline `records.ndjson` fixture; blind-re-read discipline).
5. **Build pulled back into apparatus/main** (SCDD track wraps its own lineage).

---

## WHAT'S OPEN — ordered next steps for S16

1. **Seed-shape test → blind re-read → D9 substrate lock.** Per the locked spec. Run on the **baseline `records.ndjson`** (23,095 records, exists on the box — confirm at boot). PASS on the lead being locked + a blind re-read (append-only ⇒ immortal) → lock the substrate → close D9. **This is the headline move; everything downstream needs a home for the floor.** Supabase is the §8 lower-regret default; NornicDB if Jake wants graph-native fidelity now.
2. **The v1.3 build** — delta (uuid-set-difference, 1,337-msg 5-28 fixture, date never a filter, resolve-within-dir) + scrub-vN overlays + v1.1 field-drift (key-presence allowlist from `s14_presence_rates.md`, carve-out `text.citations_grouping_mode`) + raw.json wipe-after-verify. Authored from spec v4. **Store-independent → parallelizable with #1.** Plan-OC/build-CC, plan-mode, ratify a small batch before scale. Pipeline v1.2 → v1.3.
3. **Commit repo-gap files** — `cool_gems_menu.xlsx` (staged to outputs this session → `skills-catalog/`); `chunks-v0.3/` (the multi-label output, workflow=554 + 806 overlap; re-runnable in minutes from the in-repo script if not uploading). Closes the stale-vs-canon gap.
4. **Three escalations** (recall / kept / shared-memory) — blocked on Jake uploading repos; feed the **retrieval** layer, not the substrate pick, so they don't block the lock. `kept`: do NOT borrow its ingest until export-vs-scrape is verified.

---

## DOWNSTREAM FLAGS (protect the timeline)

- **records.ndjson is a local snapshot artifact (not in the repo).** S16 must confirm the baseline output is on the box before running the seed-shape; if gone, the v1.3 delta build regenerates one (but baseline is the bigger/honester fixture). **Bites at seed-shape run.**
- **Trust disk, not directive.** This session lost turns to the v4-already-existed fork + a push-behind CHANGELOG; the merge-back independently flagged the same enshrine-lag (cost S4 two turns, S6 three). **S16 reads versions/counts off the disk and flags any pointer that doesn't resolve — never works off a directive's claim.**
- **Blind re-read before the D9 lock.** The three-AI-council / cross-read discipline is load-bearing for an append-only substrate-altering call. **Bites at lock-commit.**
- **D20 config gate if NornicDB** — pin decay/auto-links/embeddings OFF; verify the *running* config, not the example. **Bites at NornicDB deploy.**
- **test-host ≠ deploy-host** — "ran the round-trip on Castle Black" ≠ "deploys on Castle Black." Decide the deploy target deliberately.

---

## JUDGMENT-CALL LEDGER

- **Stopped on the v4-already-exists fork instead of rebuilding.** Repo > directive (§2). HIGH. Correct — rebuilding would have clobbered good work.
- **raw.json Path A.** Recommended A; Jake ratified at firmer scope (never-to-NAS). HIGH. Anthropic is the re-pull source; sealed-but-present raw is the "immortalized cred" the posture walls against.
- **Ran the dual-gate cold, didn't reconcile toward SCDD's read.** HIGH. The one divergence (round-trip open vs closed) was real signal → kept D21 as a gate → ran green.
- **Held 16 MiB WAL as the binding ceiling vs "no hard cap."** HIGH. Folded to canon; FaceOff_v2 §D19 agrees.
- **Seed-shape on the baseline records.ndjson rather than waiting on the delta build.** MEDIUM-HIGH — decouples the lock from the v1.3 build, but depends on the baseline output still being on the box (canon says it exists; not eyeballed from the repo). Confirm at boot.

---

## §17 ROUTING (S15 close bundle)

1. **§17.1** — this handoff (`Chat_Session_Handoff_2026-05-28_apparatus_S15_to_S16.md`) → `active/apparatus/`.
2. **§17.2** — no formal proposed-reference-changes file: the canon edits this session (anchor v9, CHANGELOG) were *landed*, not proposed. One soft queued item: the **boot-doc principle** (point-at-canon + invite-the-turn-1-flag, instead of fortifying against the verification reflex) — bank for the boot-doc/ignition-template rewrite; not a ratified rule edit.
3. **§17.3** — `Seed_Shape_Test_Spec_v1_2026-05-28.md` → `active/apparatus/` (the D9 gate spec, S16 executes it). Plus `cool_gems_menu.xlsx` → `skills-catalog/`.
4. **§17.4** — S16 ignition prompt (in-chat code block, generated with this handoff).

Jake commits: this handoff + the seed-shape spec → `active/apparatus/`; `cool_gems_menu.xlsx` (+ `chunks-v0.3/`) → `skills-catalog/`. Anchor v9 + CHANGELOG already pushed.

---

## PICKUP GUARDRAILS FOR S16

- **Trust disk, not directive** — read v9 / v4 / FaceOff_v2 / the seed-shape spec off disk; flag any pointer that doesn't resolve.
- **Blind re-read before the D9 lock** — append-only is immortal; don't rubber-stamp the seed-shape's own PASS.
- **Plan-OC / build-CC, plan-mode for the v1.3 build, ratify small before scale.**
- **CC writes scratch freely, NEVER canon (`active/`) without explicit instruction** (§7.6).
- **Do NOT run the real pipeline on the 5-28 export at the default source path** (silent-second-baseline trap); it's the delta fixture, parked off-path. Baseline is sealed.
- **NEVER search past chats for code** — ask Jake to upload, or read via codeload.
- **Prose questions only, no widget. Re-anchor ~5 turns (4/4 = re-ground-on-canon seam). Timestamps via bash `date`.**

---

*apparatus S15 → S16. 2026-05-28. The substrate got characterized, dual-gated, round-trip-proven, and face-off'd; the anchor enshrined v9; raw.json resolved Path A; the seed-shape test locked as the last gate before the floor gets a permanent home; SCDD folded back in. S16 runs the seed-shape, locks the substrate, and builds the v1.3 pipeline. Apparatus is unparked.*
