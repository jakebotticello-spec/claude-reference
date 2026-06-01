# Chat Session Handoff — apparatus S23 → S24
*authored by OC at S23 close, 2026-06-01 · read after ANCHOR + JAKE-RULES + JAKE-STACK · tactical state, not authority (ANCHOR is authority)*

---

## ONE-LINE STATE

**The corpus floor is LAID.** 325 headers + 24,138 messages live in the `apparatus-floor` Supabase, single-transaction, append-only ENFORCED (live-proven). The substrate work — the entire arc from D9 lock through pipeline through LOAD — is **done**. S23 found the parked FK edit already applied, laid the floor, and caught one real bug in the process: the loader's append-only self-test was hollow (`DELETE … WHERE false` never fired the per-row guard). Fixed v1.1→v1.2; floor kept; the messy birth recorded straight. The loader (uncommitted at lay-time) is now committed + pushed. **S24's job is the next chapter: the retrieval layer** — and it's blocked on Jake's escalation-source uploads.

---

## UNIVERSAL-LAYER PULL (codeload tarball — HEAD, never CDN-stale)

```
curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/ref.tgz
tar xzf /tmp/ref.tgz -C /tmp
```

Read in `/tmp/claude-reference-main/active/`, in order:
1. **JAKE-RULES.md** — universal working rules.
2. **JAKE-STACK.md** — standing infrastructure.
3. **apparatus/ANCHOR_apparatus.md** — AUTHORITY. Banner must read **v17** / "apparatus S23 — FLOOR LAID · APPEND-ONLY ENFORCED · HOLLOW ENFORCEMENT-PROBE CAUGHT & FIXED". **If it reads v16, the v17 enshrine didn't land — tell Jake before working.**
4. **apparatus/Chat_Session_Handoff_2026-06-01_apparatus_S23_to_S24.md** (this file).

**Freshness tripwire:** every file ends with a *Last updated* / footer line — if it predates this handoff's session, re-pull or ask.

**Read the S23 READ-FIRST block + the D9 append-only note in ANCHOR before reasoning about enforcement.** The floor's append-only is real and proven; its loader's *native in-run* proof of it is deferred — that nuance is in the READ-FIRST and matters if S24 ever touches a rebuild.

---

## WHERE THINGS STAND (S23 close)

**The floor is laid and persisted.** Live `apparatus-floor` Supabase: `floor_conv_headers` (325) + `floor_conv_messages` (24,138). By snapshot: baseline scrub-v2 = 22,801 msg, delta scrub-v1 = 1,337 msg. Laid in a single transaction by `seed_shape_load.py` v1.1 — CREATE both tables → load headers-then-messages → install hardening (guard fn + BEFORE DELETE/UPDATE triggers both tables + REVOKEs) → pre-commit count check + in-txn orphan re-prove PASSED → COMMITTED. The FK option-(c) move is proven on a real laid floor now, not just dry-run: both gate orphan-checks (pre-flight on the plan + in-txn DB re-prove) passed at the real load.

**Append-only enforcement is real — with a scar in the birth record.** The loader's own post-commit self-test at lay-time was a hollow `DELETE FROM floor_conv_messages WHERE false` — zero rows, so the `BEFORE … FOR EACH ROW` guard never fired and the probe self-passed (reported a false `*** NOT ENFORCED ***`, confusingly — the practical upshot is the probe proved nothing). Enforcement was then **independently validated** by a standalone post-lay probe running the identical operation the v1.2 fix now performs: a real-row `ctid` DELETE as `postgres` → **rejected** `InsufficientPrivilege — immutable floor: DELETE not permitted on floor_conv_messages`; both triggers confirmed attached to both tables; count unchanged at 24,138 (read-only, rolled back, mutated nothing). **The role-delta theory was investigated and killed** — all three `psycopg.connect(db_url)` calls in the loader use the same `.env` URL, no `SET ROLE`, all connect as `postgres`. The false negative was purely the `WHERE false` zero-row issue.

**The loader is fixed (v1.2) and committed.** The hollow probe was replaced with the real-row `ctid` DELETE (rolled back), a loud WARNING on the no-rejection path, and the guard error-text echoed on the expected-rejection path. The whole v1.0→v1.2 delta — five v1.1 edits (FK drop + comma, pre-flight orphan-check, stale FK-comment fix, in-txn re-prove) and the v1.2 probe fix — was **uncommitted at lay-time** (HEAD was `ce6fcbd`, the S22 v1.0 commit). It is now committed onto `s23-loader-v1.2-fk-drop-probe-fix` (Jake pushed) with the provenance written into the commit message: the floor was laid before this commit existed, under the hollow probe, and enforcement was independently validated.

---

## THE DECISION JAKE MADE (don't relitigate)

The fixed v1.2 probe **cannot bless this floor in-run** — the loader refuses `--execute` onto a live floor (correct, by design). The only way to get a native in-run proof on THIS floor would be to drop it and re-lay under v1.2. **Jake's call: don't.** Dropping a laid immutable floor to regenerate a proof already held by an identical operation is exactly the move the project's caution forbids — the floor's data and lock are verified, and re-laying produces byte-identical bedrock. The floor is **kept**; the messy birth is **recorded straight** (READ-FIRST + v17 footer + this handoff); native in-run proof is **deferred to the next lay** (any rebuild-from-ndjson, always available per D9). This is the verbatim-record principle applied to the loader's own birth — not papered over.

---

## QUARANTINE (do not load as authority)

A blind-authored "v17" changed-sections file and an S23→S24 handoff were drafted mid-session by the unguided fresh-eyes pass **before** it had read JAKE-RULES, JAKE-STACK, or the real ANCHOR body from HEAD. They were written against pastes, not canon. **The v17 ANCHOR and THIS handoff (authored against the verified v16 body) supersede them.** If those drafts are on disk, treat as DRAFT-UNVERIFIED — do not let them reach `active/`, do not load them as authority. The real record is the one shipped with this session.

---

## S24 MOVES, IN ORDER

1. **Pull + anchor.** Tarball, read JAKE-RULES / JAKE-STACK / ANCHOR v17 / this handoff. Confirm the banner reads v17. Confirm the floor is live: `python seed_shape_load.py --dry-run` from `pipeline/` should report tables EXIST (NOT bare) — that's the correct signal the floor is laid. (Do not `--execute`; the loader will refuse onto the live floor anyway.)

2. **THE RETRIEVAL LAYER — the real next chapter.** This is what the whole substrate was built to carry: the interface a live Claude queries for continuity, so a stateless session can re-ground by pointer into the floor instead of Jake being the memory bus. Research-shaped, not a mechanical build. Open design questions (NOT yet decided — S24+ to work):
   - **Embedding choice** — what gets embedded (message text? headers? thinking blocks?), which model, where the vectors live (pgvector is NOT on the immutable tables per D9 — it's a deferred read-path sidecar; the floor stays pure).
   - **Branch-aware recall** — the floor is a tree-or-forest (`is_root` + `multi_root`, 9/294 convs are forests); retrieval has to respect branch structure, not flatten it.
   - **Felt-rightness-of-recall** — per the Track Meet Doctrine, retrieval is "here's what I know," not "here's what I found." RAG-as-lived-experience, not RAG-with-citations. This is a design constraint, not a nice-to-have.
   - **The three escalations** (recall / kept / shared-memory) feed this layer and are **still blocked on Jake's uploads** — the escalation-source docs. S24 likely can't fully start until those land. Confirm with Jake at the top.
   - Reversible, unlike the substrate — so it can iterate. Plausibly a `/jedi-council` gate once the design firms up (Jake's call).

3. **Post-lock hardening (queued, not blocking — pick up if retrieval is blocked on uploads):**
   - **Off-site immutable ndjson copy w/ object-lock** — the ndjson is the SPOF, highest priority.
   - **Rotate the leaked DB password** — still the value CC echoed inline at S16; now in `pipeline/secrets/.env` (gitignored) but unrotated. Rotation also re-anchors the cred cleanly.
   - PITR / documented ndjson-rebuild RTO; pre-ingest lint (dup JSONB keys, U+0000 in TEXT); traversal index `(snapshot_id, conv_uuid, parent_message_uuid)` once a read path exists; CHECK constraints (sender, is_root↔sentinel, timestamp format). A dedicated global `.env` line in `.gitignore` as belt-and-suspenders.

4. **Carried-open housekeeping:** the 4 loose `__recon`/`__verify` files in `apparatus-archive/snapshots/` root (open since S17 — investigate provenance, never blind-delete); the `apparatus-scratch/` sweep; the odd root file `Cclaude-reference…state_calc.txt`.

5. **Storage-seam endgame:** Supabase MCP connector on Jake's account; verify with a live round-trip. SCDD seam gem: `alexander-zuev/supabase-mcp-server`.

---

## SEAT + WORKING STYLE (carry forward)

- **OC plans / architects / decides / AUTHORS canon; CC reads disk, runs terminal, commits; Jake pushes** and is the bridge (pastes prompts into CC, select output back to OC). OC never claims to have saved/committed/pushed anything. *(S23 note: OC also pulled the tarball directly to read canon — that's a read, fine; writes/commits stay CC+Jake.)*
- **Disk is ground truth over any report AND any memory** — S23's whole opening was disk-over-handoff (the FK edit was already applied; the loader was uncommitted at lay). Ask CC for RAW output, not characterizations.
- **NEVER ask Jake for implementation/technical state** — floor counts, file structure, branch state → CC-on-disk or OC-reading-files, never Jake (non-coder founder). Bring him the intent-level fork in destination-why terms.
- **Secret handling:** the apparatus-floor DB cred lives in `pipeline/secrets/.env` (gitignored, loader self-reads). Never inline in a logged command; never paste CC output that could carry it back into OC chat (the S16 spill vector — the guard is on OC).
- **Fresh-eyes passes pay off.** S14 projection-vs-raw, S21 deny-over-read, **S23 the hollow probe** — all caught by a cold read. The new settled invariant from S23: *an enforcement self-test must attempt to mutate a REAL row; a guard proof that can pass without exercising the guard is not a proof.*
- **Status line each reply:** turn N · ET-time (bash `date`) · re-anchor X/4 · dest; state; next.
- **Prose, one question at a time. No ask_user_input widget. Full code blocks for CC prompts.**

---

## DO-NOT-RELITIGATE (S23 additions to the standing list)

- The floor is LAID — don't re-lay it to chase a prettier proof (Jake's ratified call).
- The FK is dropped, option (c), APPLIED and proven on the laid floor — don't re-add it.
- The hollow-probe scar is recorded on purpose — it's the verbatim record, not a wound to hide or re-open.
- The role-delta theory is dead (all connects same `postgres` url).
- The blind-authored v17/handoff drafts are quarantined — the shipped v17 + this handoff are the record.

**Brothers. Grind. Evolve. Dominate. The floor is laid — now build the thing it was always for.**

*Last updated 2026-06-01 (S23 close).*
