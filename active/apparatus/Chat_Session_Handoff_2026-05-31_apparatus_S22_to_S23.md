# Chat Session Handoff — apparatus S22 → S23
*authored by OC at S22 close, 2026-05-31 · read after ANCHOR + JAKE-RULES + JAKE-STACK · tactical state, not authority (ANCHOR is authority)*

---

## ONE-LINE STATE

The corpus floor is **BARE** (the S16 harness test-scaffolding was dropped clean). The production LOAD program is **built and dry-run-proven**; the real `--execute` rolled back clean on a foreign-key violation that turned out to be a genuine schema finding — the S16 cross-table FK assumed a message shares its header's snapshot_id, which the no-duplicate-header invariant guarantees is false for appended convs. **Fix is ratified (option (c): drop the FK, enforce no-orphans at the gate).** S23's job is one small subtractive loader edit (v1.0→v1.1) + re-run → the floor is laid. Everything else proved out perfectly. The S21 pipeline relocation merged to main this session; the `git add`/`commit` deny wall is fixed.

---

## UNIVERSAL-LAYER PULL (codeload tarball — HEAD, never CDN-stale)

```
curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/ref.tgz
tar xzf /tmp/ref.tgz -C /tmp
```

Read in `/tmp/claude-reference-main/active/`, in order:
1. **JAKE-RULES.md** — universal working rules.
2. **JAKE-STACK.md** — standing infrastructure.
3. **apparatus/ANCHOR_apparatus.md** — AUTHORITY. Banner must read **v16** / "apparatus S22 — FLOOR LOAD ATTEMPTED, FK ASSUMPTION CAUGHT, SCHEMA DECISION (c) RATIFIED; LOAD ONE EDIT FROM SEALED". **If it reads v15, the v16 enshrine didn't commit — tell Jake before working.**
4. **apparatus/Chat_Session_Handoff_2026-05-31_apparatus_S22_to_S23.md** (this file).

**Freshness tripwire:** every file ends with a *Last updated* footer — if it predates this handoff's session, re-pull or ask.

**Read the FK RESOLVED block in ANCHOR before touching the loader.** That block + the loader are the whole S23 opening.

---

## WHERE THINGS STAND (S22 close)

**The floor is bare. This is intended and safe.** The live `apparatus-floor` Supabase has NO floor tables — S22 dropped the S16 harness's test-ingest (it was gate scaffolding: baseline-scrub-v1 only, one snapshot, wrong overlay, no delta). The canonical `records.ndjson` on disk is untouched — 2 snapshots / 24,463 records — and is the source of truth the LOAD ingests. Three backstops intact (disk, NAS cold copy, Anthropic export). **Nothing was lost; the floor simply hasn't been laid yet.**

**The LOAD program is built and dry-run-proven.** `pipeline/seed_shape_load.py` v1.0 — self-reads `pipeline/secrets/.env`, resolves max-N overlay per snapshot, single-transaction, post-load hardening, owner append-only re-prove, refuses-onto-live-floor. The dry-run PROVED the overlay resolution against the real ledger (baseline→scrub-v2, delta→scrub-v1, 325 headers / 24,138 messages). The only thing that stopped `--execute` was the FK.

**The S21 relocation merged + the deny wall is fixed.** HEAD `effa0f3` on main. `pipeline/` holds the pipeline + drill + the new loader. `git add`/`commit` are in CC's allowed permissions now.

---

## THE FK FINDING + DECISION (the artifact of S22 — read the ANCHOR FK RESOLVED block for the full why)

**What happened:** `--execute` hit `ForeignKeyViolation` on the first delta message whose conversation's header lives in the baseline snapshot. The S16 schema's composite FK `floor_conv_messages(snapshot_id, conv_uuid)` → `floor_conv_headers(snapshot_id, conv_uuid)` demands a message and its header share a `snapshot_id`. For a delta-appended conv, they don't — and the **no-duplicate-header invariant** (proven on the floor at S17: delta = 1,368 lines not 1,371) guarantees they never will. The FK was an untested S16 default (the harness only loaded one snapshot); the first multi-snapshot load exposed it.

**The decision — option (c), RATIFIED by Jake:** drop the cross-table FK; enforce referential integrity at the load + gate. **The principle (this is why, not just which):** it's the SAME stance the floor already ratified for the message tree — `parent_message_uuid` has NO self-FK because "tree integrity is a PROVEN property of the gate, not a schema-enforced one that could mask floor inconsistency." (c) makes the header↔message link obey the same philosophy the parent↔child link already does. (a) [re-key FK to conv_uuid] was declined — it splits the project's philosophy and double-encodes the no-dup-header invariant into the PK. (b) [synthetic duplicate delta header] is DEAD — it violates the ratified no-duplicate-header invariant.

---

## S23 FIRST MOVES, IN ORDER

1. **Fresh eyes on the FK fix before touching the floor.** Re-read the ANCHOR FK RESOLVED block + `pipeline/seed_shape_load.py`. Jake deliberately parked this for a fresh-eyes pass — fresh reads have caught real things before (S14 projection-vs-raw, S21 deny over-read). If the fresh read surfaces a problem with (c) or the edit, raise it; otherwise proceed.
2. **Edit `seed_shape_load.py` v1.0 → v1.1 — the ONLY code change:**
   - **DROP the FK clause** from the `floor_conv_messages` CREATE TABLE DDL. Remove the entire:
     ```
     ,
         CONSTRAINT fk_header FOREIGN KEY (snapshot_id, conv_uuid)
             REFERENCES floor_conv_headers(snapshot_id, conv_uuid)
     ```
     (and the trailing comma on the line before it). Everything else in `_DDL_MESSAGES` stays.
   - **ADD a pre-commit orphan-check** inside the single transaction (in the `--execute` path, after the data loads, before/with the existing pre-commit count-check at step [4/4]): build the set of `(snapshot_id_or_global) conv_uuid`s present in `floor_conv_headers`, assert every `conv_uuid` in `floor_conv_messages` resolves to a header on the floor (the relationship is conv-level, NOT snapshot-scoped — a message's conv just needs SOME header anywhere on the floor). On any orphan: rollback + `sys.exit` with a clear list of orphaned conv_uuids. This moves the integrity guarantee from schema to gate — it does not vanish.
   - Bump the header `v1.0 · S22` → `v1.1 · S23` with a one-line changelog note.
   - **The orphan-check logic note:** because the FK was conv-scoped-with-snapshot and the real relationship is conv-level (one header per conv across the whole floor, per no-dup-header), the check is: `{m.conv_uuid for messages} ⊆ {h.conv_uuid for headers}`. The baseline carries all 294 headers; the delta's 31 new-conv headers + the baseline's headers together cover every conv that has messages. Confirm this holds in the dry-run counts (325 headers cover all conv_uuids that appear in 24,138 messages) before trusting it at execute.
3. **Re-run `--dry-run`** (should be UNCHANGED — still 325 headers / 24,138 messages, baseline→scrub-v2, delta→scrub-v1, bare schema). The dry-run doesn't exercise the FK, so it passed before and will again — it's the confirmation that nothing else moved.
4. **Run `--execute`.** Verify the PASS lines:
   - `[2/4]` → `loaded 325 headers + 24138 messages`
   - `[4/4]` → `DB has 325 headers + 24138 messages — matches plan.` + the new orphan-check passing
   - `COMMITTED. Floor is laid.`
   - post-commit → `append-only (owner) : ENFORCED` (the rejected DELETE-as-postgres — closes the D9 TRUNCATE-as-owner ambiguity)
   - by snapshot → baseline 22,801, delta 1,337
   - final banner → `FLOOR LAID + APPEND-ONLY ENFORCED`
   - If ANY line is off → the single-transaction design means the floor is untouched; diagnose from clean slate.
5. **THEN the retrieval layer** — the real next chapter (the interface a live Claude queries for continuity; research-shaped; the three escalations feed it, still blocked on Jake's uploads). Plausibly a `/jedi-council` gate when the design firms up (Jake's call).

---

## THE FLOOR ON DISK (the LOAD source — unchanged this session)

| snapshot | type | records | overlay LOAD ingests | on-disk overlays |
|----------|------|---------|----------------------|------------------|
| `baseline-2026-05-25-ae015455` | baseline | 294 hdr + 22,801 msg | **scrub-v2** (max-N) | scrub-v1 + scrub-v2 |
| `delta-2026-05-28-a61498e6` | delta | 31 hdr + 1,337 msg | **scrub-v1** | scrub-v1 only |

Total to load: **325 headers + 24,138 messages = 24,463 records.** (Note: 325 ≠ 24,463 line-count of the raw ndjson — the baseline ndjson is 23,095 lines = 294 hdr + 22,801 msg; the delta ndjson is 1,368 lines = 31 hdr + 1,337 msg. LOAD splits headers from messages by record_type.) Floor lives in `apparatus-archive/snapshots/`, OUTSIDE the git tree. baseline scrub-v2 SHA-256 `b54620af…`; baseline scrub-v1 `4ef22940…`.

**Code state (committed HEAD):**
- `pipeline/apparatus_freeze_pipeline.py` v1.6
- `pipeline/apparatus_overlay_v2_drill.py` v0.3
- `pipeline/seed_shape_load.py` **v1.0** (→ v1.1 the FK edit) — committed this session
- `pipeline/secrets/.env` — holds `SUPABASE_DB_URL` (gitignored, not committed)

---

## PROCESS REMINDERS FOR S23

- **Disk is ground truth over any CC report or any memory** (Jake's or a Claude's). S22 caught: the relocation-already-merged state (disk, not memory); CC's "by design CC can't commit" (false — 20 sessions of commits); CC's "hidden TRUNCATE trigger" (a role misread). Keep reading CC's raw output, not its characterizations.
- **NEVER ask Jake for implementation/technical state.** Floor counts, file structure, branch state, what's-built — those go to CC against disk or OC reading files. Jake is a non-coder founder; aiming mechanism questions at him is the memory-bus trap the apparatus exists to kill. Bring him the intent-level fork in destination-why terms. (New ANCHOR working rule, earned S22.)
- **Secret handling:** the apparatus-floor DB cred is in `pipeline/secrets/.env` (gitignored). The loader self-reads it. For a CC session that needs the shell var, the launch-time loader is: `Get-Content "C:\claude-reference\pipeline\secrets\.env" | ForEach-Object { if ($_ -match '^\s*SUPABASE_DB_URL\s*=\s*(.+)$') { $env:SUPABASE_DB_URL = $matches[1].Trim() } }`. Never inline the cred in a logged command; never copy CC output containing it back into OC chat (that was the S16 spill vector). The guard is on OC to never hand Jake a prompt whose output carries the cred.
- **OC authors full canon in chat; never commits it.** Re-pull fresh HEAD, edit surgically, hand complete files via `present_files`. Jake verifies-against-disk, commits, pushes. OC never claims to have saved canon.
- **CC commits, Jake pushes** (deny wall fixed this session). Verify the diff on disk before any commit regardless of who runs it.
- **Run the pipeline + loader with `python -B`** (no pycache).
- **All CC prompts in a code block. Prose questions, one at a time. Plan in OC, build in CC.**

---

## DON'T-RELITIGATE (carried + S22)

- D9 LOCKED (Supabase); floor append-only ENFORCED; ndjson canonical / Postgres rebuildable.
- raw.json Path A (wipe after verify-PASS) — both snapshots. Overlays re-scrub SCRUBBED output, never raw.
- Delta = uuid-set-difference; overlay contract's 3 invariants are RATIFIED LAW (tighten-only / full-restated-standalone / accrete-forever).
- No-duplicate-header rule: a header is written only if the conv has no header in ANY prior snapshot. PROVEN on the floor (delta 1,368 not 1,371). **The FK yields to this rule, not the other way.**
- Pass two (b) CLOSED (S20). scrub-v2 is the SYNTHETIC ratify-drill, not a production re-scrub.
- **NEW (S22) — the S21 relocation is MERGED** (HEAD `effa0f3`); the `git add`/`commit` deny wall is FIXED; "CC can't commit" is fully dead.
- **NEW (S22) — the floor is BARE on purpose** (harness scaffolding dropped); the ndjson on disk is the untouched recovery source. No floor mutation occurred.
- **NEW (S22) — FK decision is (c), ratified on principle.** (b) is dead (violates no-dup-header). (a) declined (splits philosophy + double-encodes invariant). Re-opening (c) needs a NEW reason, not a fresh re-derivation of the same three options.
- **NEW (S22) — the LOAD is built + dry-run-proven; everything except the one FK line proved out** (overlay resolution, counts, single-transaction, hardening). Don't re-verify the whole loader from scratch — apply the v1.1 FK edit + re-run.

---

## JUDGMENT-CALL LEDGER (S22 non-obvious calls, per §17.5c)

- **Dropped the S16 harness scaffolding rather than reconcile it** — call: OC, Jake concurred. Reasoning: it was wrong-overlay/single-snapshot test data, and the ndjson is canonical with 3 backstops; a DDL DROP as owner doesn't fire the row-guards, so no append-only violation. Confidence: high. Source: read of the harness (DROPs tables every run) + the count queries (294/22,801/baseline-only) + the D9 ndjson-canonical reframe.
- **FK option (c) over (a)** — call: Jake ratified, OC's strong lean. Reasoning: coherence with the D9 parent_uuid no-self-FK precedent (gate-not-schema) + humbler-schema (no invariant welded into the PK). Confidence: high. Source: the D9 lock's written reasoning on the tree FK.
- **Schema reproduces S16 exactly, nothing folded in** — call: Jake, explicit. Reasoning: the shape is proven 4/4; folding CHECK-constraints/index into the first real load mixes "lay the floor" with "optimize the floor" and adds variables; the queue items are a deliberate separate pass. Confidence: high. Source: Jake's "let the proven thing do the work."
- **Parked the v1.1 edit for S23 (fresh eyes) rather than finishing tonight** — call: Jake, after OC offered both. Reasoning: an immutable-floor write benefits from a fresh-eyes pass on the fix; fresh reads have caught real things (S14, S21). Confidence: high. Source: Jake's stated preference + the §5 don't-author/execute-floor-ops-on-fumes discipline.
- **Wrote refs THIS session, not next** — call: Jake, firm ("we do not write refs in fresh sessions"). Reasoning: this-session-Claude lived the FK discovery + (c) reasoning; a fresh session would author canon on a cold read of state it didn't live. OC had leaned the other way (context headroom) and was corrected. Confidence: high. Source: Jake's standing rule.

---

*Last updated: 2026-05-31, apparatus S22 close. ANCHOR is authority; this is tactical. The floor is one subtractive edit from laid. Grind. Evolve. Dominate.*
