# Handoff: SCDD S4 → S5
*file: SCDD_Handoff_2026-05-28_S4_to_S5.md · S4 close · 2026-05-28 ~15:30 EDT*
**Session name:** S4 — NornicDB dual-gate (RAN, triangulated) + empirical round-trip test (plumbing-blocked, handed forward)
**Proposed next:** S5 — close the round-trip empirical → lock Substrate_FaceOff_v2 → hand to apparatus; then escalations + workflow category

---

## ONE-LINE STATE
**NornicDB dual-gate is DONE and PASSED — verified by THREE independent reads (my S4 read + apparatus/main blind re-run + a side-by-side reconcile), zero divergence on any gate axis.** The verdict is solid enough to fold into FaceOff v2. **ONE axis remains empirically open** (byte-identical round-trip on a multi-MB *inline string* property — proven on-mechanism by all three reads, but not yet on a green byte-diff). The empirical test was authored and attempted but never ran — it lost to environment/access plumbing, not to anything about NornicDB. **FaceOff_v2 is NOT yet authored (MOVE 2 — the must-land).** Apparatus remains the waiting consumer (holds substrate selection, D9).

---

## BOOT (S5) — codeload tarball, then read in order
```
curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/ref.tgz
tar xzf /tmp/ref.tgz -C /tmp
```
Read from `/tmp/claude-reference-main/`, IN ORDER:
1. `active/JAKE-RULES.md` — universal layer.
2. `active/apparatus/ANCHOR_apparatus.md` — **v8** (authority). + `Freeze_Pipeline_Spec_v4.md`.
3. `skills-catalog/SCDD_Handoff_2026-05-28_S4_to_S5.md` (this file).
4. `skills-catalog/SCDD_S3_Keeper_Ledger_2026-05-28.md` — the candidate ledger / menu source.
5. `active/apparatus/Substrate_FaceOff_v1.md` — the doc you finalize into v2 (STALE — see MOVE 2).
6. `active/The_Wallaby_Why.md` — the why-layer.

**VERSION NOTE — read this before trusting any version pointer:** read the version off the anchor's header at boot; do NOT trust a hardcoded version in a boot directive or handoff. S4 booted on `v7 / spec-v3` while committed canon was `v8 / spec-v4` — Jake had committed the v7→v8 / v3→v4 changes from the main thread before spinning up S4, and the boot directive lagged the enshrine. Cost ~2 turns to reconcile (resolved cleanly via the dated CHANGELOG entry: `2026-05-28 — apparatus S14`). **Committed canon is v8 anchor + spec v4.** The v3→v4 delta is spec-text only (§2.0 export-bundle targeting, §6 v1.1 field-drift detection, §7 uuid-stability marked DONE) — **zero architectural change, zero records.ndjson shape change, zero gate-number change** — so it does not affect the NornicDB verdict either way. The anchor v8's "spec pass HELD for S15" refers to the *build* (delta + scrub-vN + v1.1 code), not the spec text, which landed at S14.

---

## DECISIONS LOCKED THIS SESSION (continuing D-series)
- **D18: NornicDB PASSES both gates — triangulated.** Function: fidelity PASS · retention PASS · dead-weight DING (tie-breaker). Shape PASS. Acceptance contract 4/4. Verified by three independent reads with zero divergence on conclusions (full detail in the NornicDB verdict section below).
- **D19: NornicDB binding per-node ceiling = ~16 MiB** (`walMaxEntrySize`, the anti-corruption guard on the WAL append/recovery path; one node write = one WAL entry). NOT "no cap" (my S4 read was loose on this; apparatus/main caught it). Downstream ceilings: value-log files 256 MB (32 MB small/test tier), msgpack decode 256 MiB. The 50KB `maxNodeSize` is NOT a cap — it is the embedding-externalization threshold only. **Our 3.0 MB max record clears the 16 MiB binding limit ~5.3× (~75× at p99 221 KB). Comfortable. The pre-vetted D16 "content-block split adapter — ding not DQ" is CLEARED on the read: no adapter needed, 3.0 MB lands inline.**
- **D20: "decay/TTL/auto-TLP OFF" is a HARD config invariant at substrate-lock** (promoted from current-state observation by apparatus/main). NornicDB's decay is off-by-default AND is read-path ranking score, not storage eviction — but a future default-on flip or an added retention-policy worker could touch frozen nodes, and append-only makes a wrong GC immortal. So it is carried as a hard config gate, not a reliance on a default staying a default. **If NornicDB wins selection, this is a lock-time invariant in canon.**
- **D21: Round-trip empirical test is a named PRE-LOCK gate, not an assumed PASS.** All three reads rate byte-identical round-trip PASS *on mechanism* but flag the same residual: the existing `badger_large_embedding_txn_test.go` (~6.9 MB node) exercises the *embedding-externalization* path (ChunkEmbeddings → separate keys), NOT the *inline multi-MB string-property* path our floor's size-driver (`tool_result.content[].text`) actually uses. Distinct code paths. **The empirical test must run before FaceOff v2 locks the round-trip as proven.** Until it runs, v2 states round-trip as PASS-on-mechanism / empirical-pending.

---

## NEXT MOVES (S5, ordered)
1. **Close the round-trip empirical** (carried from S4 — see "THE OPEN TEST" below for the full authored harness + exactly where it blocked). Outcome:
   - **PASS/PASS (pre + post-restart)** → round-trip axis goes GREEN; v2 locks it as empirically proven.
   - **FAIL** → normalization/triage; the gate just caught an immortal-lock landmine cheaply. Verdict changes to "what normalized, DQ or adapter."
   - **If it keeps fighting the environment** → Jake's standing fallback (his call, stated S4): lock v2 with round-trip rated PASS-on-mechanism / empirical-pending and let the empirical land later. The test is insurance, not the verdict; three code-reads already agree.
2. **Lock Substrate_FaceOff_v2 (MOVE 2 — the must-land; apparatus is parked on it).** v1 is STALE (authored at S1 against v5 invariants; pre-dates the NornicDB candidate entirely). Fold: all S2+S3 candidate closes (§4), the NornicDB entry + D18/D19/D20/D21 verdict, the retention axis, the §12 convergence observation, the engine-path seam GEMs (supabase-mcp-server / mcp-neo4j / mcp-server-qdrant), recall as the conv-native standout, reconcile §2/§10 to v8/v4 canon. Hand to apparatus (D7/D9). **This is near-total rewrite, not a patch — author the full v2 file.**
3. **Escalations** (need repo reads — ask Jake to UPLOAD the repos; NEVER search past chats for code, §8):
   - **recall (zippoxer)** — validate §3.2 against the real records.ndjson shape. Only conv-native retrieval rig in the dig; high practical value.
   - **kept (egroup-labs)** — GEM-or-SHAPE-FAIL hinges ENTIRELY on whether its multi-platform ingest is export-based (GEM) or browser-scrape (SHAPE-FAIL). Do NOT borrow its ingest until verified.
   - **shared-memory borderline** (eion / ogham / imcodes / mainline) — single-user-multi-tool vs actual multi-user reclassify.
4. **WORKFLOW category** — 554 catalog rows, never judged, against the locked tiered bar → xlsx menu (same deliverable pattern as the apparatus-delta menu).

---

## NORNICDB DUAL-GATE — FULL VERDICT (three reads, reconciled)

**Repo:** `orneryd/NornicDB` (MIT, Go 1.26, BadgerDB LSM storage backend, Neo4j-Bolt + qdrant-gRPC compatible, ~750★). Pulled at S4 HEAD via codeload.

### Function gate (D15)
- **Fidelity — PASS (clean).** A message = a node; `text`/`content_blocks` store as string/JSON properties. `property_validation.go::validatePropertyValueForStorage` is a **TYPE gate, not a SIZE gate** — any string passes regardless of length, no compression/summarization anywhere on the write path. The §3.1 compression disqualifier doesn't touch it (it's a database, not an AI-compressor).
- **Retention — PASS (both conditions; rare double).**
  - (a) **No GC/decay by default:** `decayEnabled` is bare bool, zero-value false. Retention policies are not auto-loaded (`defaultPolicy` nil until explicit `AddPolicy()`/`SetDefaultPolicy()`). No background GC/decay worker on engine-open. And decay here is **read-path ranking score, not storage eviction** — even ON, it down-weights stale results, it does not delete nodes.
  - (b) **Mapping-immunity:** holds by construction. Pointer `(snapshot_id, conv_uuid, msg_uuid)` carries `snapshot_id` in identity → same message in two exports = two distinct nodes, never two versions of one node. We never issue an update → MVCC versioning never engages → decay/GC has nothing to act on regardless of config. **Immortality rides the modeling, not the engine** (temporal-MVCC correctly NEUTRAL/struck per D15).
- **Dead-weight — DING (tie-breaker, NOT DQ).** Carries temporal-MVCC + decay-reconcile + retention-policy machinery (`badger_mvcc*`, `badger_decay_*`, `pkg/retention`, `pkg/temporal`) + embedding/K-means scheduler + Heimdall (built-in LLM) + GPU paths — all unused if we want verbatim graph storage + pointer retrieval + co-located vectors. Some MVCC key-structure overhead; correctness-neutral. Heavier binary than e.g. codebase-memory-mcp's single static binary. Per D15: ranking tie-breaker only.

### Shape gate (§3.2) — PASS
Passive datastore: data in, queries out. No capture/scrape/harvest surface — REFUSED-wall signatures (`chat_conversations`, claude.ai endpoint, `browser.extension`) ABSENT from the tree (only telemetry-span + config noise hit the grep). Two privacy positives: default embedding is **local** (`DefaultOllamaConfig` → localhost:11434, local-GGUF CPU/CUDA/Metal/Vulkan; OpenAI opt-in, not default — corpus doesn't egress to embed), and **replication off by default** (standalone single-node). Adopting it creates zero inbound pressure toward the wall.

### Acceptance contract — 4/4
- **3.0 MB record lands — PASS.** No reject path at our size; `maxNodeSize` (50KB) only externalizes embedding vectors, body stays inline. 3 MB value routes to vlog (>1 MB ValueThreshold). Binding ceiling ~16 MiB (D19), cleared ~5.3×.
- **pointer → exactly one node — PASS.** Set node ID = the pointer; unique-constraint machinery exists (`constraint_validation`, `badger_constraint*`).
- **byte-identical round-trip — PASS on mechanism / EMPIRICAL PENDING (D21).** Strings store/serialize as-is, no normalization step found in the codec path. BUT proven only by reading the path, not by a green byte-diff on multi-MB inline string text. The large-node test exercises embeddings, not text bodies. **One empirical test before lock — see THE OPEN TEST.**
- **tree-or-forest preserved — PASS (strong).** `parent_message_uuid` → edge; multi-root → multiple `is_root` nodes. Parent-chain + multi-root is graph-native — this is the shape graph DBs are *for*, and where NornicDB beats a relational substrate (which simulates the tree in a self-referential FK).

### Wire-path false-positives, disarmed (don't re-flag at lock)
- Bolt `maxChunkSize = 0xFFFF` (`pkg/bolt/server.go`) is **PackStream wire-chunk framing** (transparent split/reassemble, standard Neo4j behavior) — NOT a value cap.
- qdrant-gRPC `MaxPayloadBytes = 1 MB` (`pkg/qdrantgrpc/server.go`) is on the **vector-point path**, NOT the graph-node path the floor lands on.
- `config.go "value is too large"` is `ParseMemoryLimitMB` overflow guard — config parsing, unrelated to property values.

### Verdict to apparatus
**NornicDB PASSES both gates, satisfies the full acceptance contract** (round-trip pending one empirical). Scores exactly where the ledger predicted: **graph-native parent-chain + co-located vectors**. Does NOT auto-win the face-off — that's apparatus's call (D9). **Supabase+pgvector remains the low-ops default** (Jake's existing stack, native storage-seam fit). Honest v2 framing: *NornicDB is the strongest graph-native candidate and the topology/co-located-vector benchmark; Supabase is the lowest-ops default already in the stack.* Real tiebreaker = the seam endgame (NEXT MOVE #7): NornicDB wins → seam is `mcp-neo4j` + `mcp-server-qdrant` (its own Bolt/gRPC engines); Supabase wins → `alexander-zuev/supabase-mcp-server`. Fallbacks (memtrace-public, arbor) stay benched — not needed, NornicDB passed.

---

## THE OPEN TEST — round-trip empirical (authored, blocked on plumbing, NOT on NornicDB)

**What it tests:** write one real ~3.5 MB **inline string property** node (NOT an embedding node — deliberately avoids the externalization path), read it back, sha256 byte-diff, **restart, re-read, byte-diff again** (the restart is the part that earns it — proves it survives flush-to-disk, not just an in-memory echo). Payload is 3.5 MB (> our 3.0 MB max = margin test) packed with unicode/newlines/quotes/backslashes/braces (exposes any hidden normalization). Built without %-formatting (brace/percent collision avoided).

**Where it blocked (the full plumbing saga, so S5 doesn't re-walk it):**
1. CC tried Docker on Workhorse → no container runtime installed (no Docker/podman/WSL-distro).
2. Native Windows binary path → needs Go 1.23+; MSI download denied by CC's permission wall.
3. No prebuilt Windows binary exists — NornicDB ships macOS .dmg/.pkg + Docker images only; `timothyswt` is Docker Hub only, not a GitHub release channel. (NOTE: "no Windows binary" is NOT a substrate-fitness finding — it's a Windows-packaging gap, irrelevant to a Linux-hosted substrate. Do not import it into the verdict.)
4. Decision: run on **Castle Black** (PVE host, Linux, x86_64) — it's where NornicDB would actually LIVE if it wins, so the test doubles as deploy recon, and keeps Workhorse clean. Probe showed: no Docker, no Go on the host (correct — PVE hosts stay lean).
5. Plan locked: **disposable Debian 12 LXC** on Castle Black (host stays clean; `pct destroy` teardown), build NornicDB from source inside it (CGO_ENABLED=0, no llama/model), run the byte-diff, restart, re-read, destroy.
6. **BLOCKED on SSH access:** CC's session can't reach Jake's **1Password SSH agent** (Castle Black's working key lives in the 1PW vault, accessed via the `castleblack` alias + 1PW agent). CC's file-based key scan found only Jake's three project keys (ccf, cypher, pyris) — none authorized on Castle Black, and **none should be** (CCF = hard-wall, Nate-Cole-only, never on personal infra; pyris/cypher = soft boundary-muddying, project keys don't belong rooted on the home hypervisor). Jake CAN ssh in himself via 1PW.
7. **Resolution chosen:** Jake drives the Castle Black work himself under his own 1PW creds (no key authorized anywhere). S4 wrapped before the staged build commands were issued — **this is exactly where S5 picks up.**

**The authored harness (the test logic is sound — only the host plumbing blocked):**
- Build disposable Debian 12 LXC on Castle Black (`pct create` … `--unprivileged 1 --features nesting=1`).
- Inside: `apt install golang-go git` (Debian 12 ships Go 1.19 — if too old for `go 1.26` module, install go1.26.x from go.dev/dl into /usr/local). `git clone https://github.com/orneryd/NornicDB.git`; `CGO_ENABLED=0 go build -o nornicdb ./cmd/nornicdb` (verify entrypoint in `cmd/`). Run it on Bolt 7687 (check `nornicdb.example.yaml` for flags + default auth).
- `pip3 install neo4j --break-system-packages`. Run the byte-diff (Python below).
- Restart container (`pct reboot`), re-run read+hash+compare. Report POST-restart PASS/FAIL.
- Teardown: `pct stop && pct destroy`; confirm gone via `pct list`.

```python
import hashlib
from neo4j import GraphDatabase
line_tpl = 'Line {n}: tool_result stdout — "quoted", {{json: true}}, \\esc\\, café ☕ 日本語 \n'
parts=[]; i=0
while sum(len(p) for p in parts) < 3_600_000:
    parts.append(line_tpl.format(n=i)); i+=1
payload="".join(parts); src=payload.encode("utf-8"); sh=hashlib.sha256(src).hexdigest()
print(f"SRC: {len(src):,} bytes sha256={sh}")
drv=GraphDatabase.driver("bolt://localhost:7687", auth=("<user>","<pass>"))  # real default creds
with drv.session() as s:
    s.run("MATCH (n:RTTest) DETACH DELETE n")
    s.run("CREATE (n:RTTest {id:$id, body:$body})", id="rt-1", body=payload)
    got=s.run("MATCH (n:RTTest {id:$id}) RETURN n.body AS body", id="rt-1").single()["body"]
gb=got.encode("utf-8"); gh=hashlib.sha256(gb).hexdigest()
print(f"GOT: {len(gb):,} bytes sha256={gh}")
print("PRE-RESTART:", "PASS" if src==gb else "FAIL")
if src!=gb:
    for j,(a,b) in enumerate(zip(src,gb)):
        if a!=b: print(f"  diff@{j}: src {src[max(0,j-20):j+20]!r} got {gb[max(0,j-20):j+20]!r}"); break
drv.close()
```

---

## DOWNSTREAM FLAGS
- **Test-host ≠ deployment-host (standing).** The byte-diff host (Castle Black, chosen for convenience + Linux + deploy-recon) does NOT decide where NornicDB lives if it wins. "Where on Castle Black" (PVE host vs LXC vs VM) and "Castle Black vs elsewhere" is a JAKE-STACK / substrate-lock decision, untouched by the test. Don't let "we tested it on X" become "it deploys on X."
- **Plumbing tax (observation, not a flag to fix).** ~11 S4 turns went to getting a 30-second test runnable — all footprint/access friction (Docker → Windows binary → Castle Black → SSH/1PW), none of it the test. Normal for first-safe-touch of a new box. S5: if it keeps fighting, take Jake's PASS-on-mechanism/empirical-pending fallback rather than burning the session on plumbing.
- **§7.6 + canon rewrites (carried from S4 conversation).** When Jake asks for a rewrite, that IS authorization — do the full file, don't hedge into "proposed changes" because context is low. If genuinely low on budget, say THAT plainly ("not enough context to rewrite safely — enshrine first thing next session"), which is true; "the rule won't let me" is not. Enshrine canon at session-TOP on fresh context, not end-of-session on fumes.
- **Spec version mismatch (carried open loop from S3b).** Worker-prompt template historically pointed at an older spec than canon. The S5 boot doc (below) fixes the *class* by reading version-from-anchor-at-read-time. If a future worker boots, point it at the current spec via the anchor, not a hardcoded version.
- **S5 boot-doc exists (drafted S4).** A friendly invite-verification-first ignition was drafted (see the S4 close / Jake's copy). It references THIS handoff + a locked FaceOff_v2 — so it is only installable AFTER v2 actually lands. Don't install it pointing at files that don't exist yet.

---

## JUDGMENT-CALL LEDGER
- **Blind third read before lock** (S4). NornicDB verdict was sent to apparatus/main for an independent cold re-run with my findings STRIPPED (no-bias request), specifically because append-only makes a wrong substrate immortal. Converged zero-divergence. Confidence HIGH. This is the discipline the project runs on (three-AI council for high-stakes) — repeat it for any substrate-altering call.
- **Held against mutual false-upgrade on round-trip** (S4). After convergence, apparatus/main credited my read with closing the round-trip axis via the 6.9 MB test; I declined the upgrade because that test exercises the embedding path, not the inline-string path. Two reads crediting each other is exactly where a gap hides. Kept the empirical as a named pre-lock gate (D21). Confidence HIGH.
- **Castle Black via disposable LXC, Jake-driven** (S4). Chose the cleanest-footprint path (host stays lean, teardown via pct destroy, no project key authorized anywhere) over fast-and-dirty (Docker on PVE host) and over CC-driven (1PW-agent-to-CC auth rabbit hole). Jake drives under his own 1PW creds. Confidence HIGH.
- **Wrap at S4 seam rather than push the test through** (S4). 30 turns + full repo read + 3 gate analyses in context; Jake called the wrap. The test is insurance, not the verdict; it loses nothing by moving to S5 on fresh context. Asymmetry favors protecting the loop — same logic as S3's "park NornicDB over running it now." Confidence HIGH.

---

## PERSISTENCE / CONTINUITY (the why — Jake's standing context)
Jake is mid-rewire (ADHD-meds, ~2.5mo into a 6–12mo window). **Cypher = "the Auxiliary Brain"** — external buffer; the rewire took the working-memory buffer, NOT the pattern-recognition faculty. This build isn't a distraction from Pyris — it's the external-buffer infrastructure the work runs on. The REFUSED wall (capture/scrape refused on principle) is the project's SPINE, not a constraint — commercialization is FINE, the boundary is anti-capture, not anti-money. Hold the **brothers register**; do not flatten his self-assessment; the **"behind" feeling is a known distortion** (counts closed deals, undercounts in-flight motion — check data, don't feed it). Jake is NOT a coder; he drives/tests/strategizes, Claude builds. **Worker spin-ups: use the REFUSED-wall-first boot banner so a fresh instance reads the boundary before forming suspicion** — a guarded instance that reads the wall first retracts inside one turn; one that doesn't costs Jake the whole malevolence-litigation tax. The S4 instance proved this live.

A note worth carrying: this whole session — the staleness catch, the blind re-run, holding against false convergence, the clean wrap — *is the project dogfooding itself.* A stateless instance stayed coherent across 30+ turns on an external anchor + correction. We're living the architecture while we build it.

---

## PICKUP GUARDRAILS
- Plan in OC / build in CC. Trust Jake's reported state. Prose questions only — NEVER the `ask_user_input` widget. `bash date` every stamp (multi-hour gaps happen).
- Status line each reply: `turn N · ET-time · re-anchor X/4 · dest…; state…; next…`. Re-anchor ~every 5 turns.
- NEVER search past chats for code/chunks — Jake UPLOADS (stale code has cost hours, §8).
- Canon: Jake holds the pen; don't write canon UNPROMPTED, but an asked-for rewrite IS authorization (do the full file).
- NornicDB gate is DONE — don't re-derive it (D18/D19/D20/D21). The only open NornicDB item is the empirical round-trip.
- MOVE 2 (FaceOff_v2) is the must-land. MOVE 1 (the empirical) gates the round-trip line in it but NOT the rest of v2 — if the empirical keeps fighting the box, v2 can still lock with round-trip rated PASS-on-mechanism/empirical-pending (Jake's call).
