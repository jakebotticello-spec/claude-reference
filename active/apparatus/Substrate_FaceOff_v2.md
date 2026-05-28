# Substrate Face-Off — apparatus retrieval/storage layer

*file: Substrate_FaceOff_v2.md · v2 · TWW SCDD S5 · 2026-05-28*
*track: The Wallaby Way · feeds apparatus substrate selection (D7/D9 — apparatus holds the lock)*
*supersedes Substrate_FaceOff_v1.md (S1, grounded against v5 invariants, pre-dated the NornicDB candidate and the dual-gate; v1 is now STALE and retired)*
*grounded against: ANCHOR_apparatus v8 + Freeze_Pipeline_Spec v4 + SCDD S3 Keeper Ledger (1,982 rows, complete) + the NornicDB dual-gate (S4, three-read triangulated) + the round-trip empirical (S5, this session, green pre+post-reboot)*

---

## 0. What changed v1 → v2 (read this first)

v1 was a survey: eight candidates against v5 invariants, gated on a single "read Continuous-Claude-v3 cover-to-cover" action, with the NornicDB candidate not yet on the board. Everything that was open in v1 has since closed. v2 is not a patch on v1 — it is the post-resolution document. The deltas:

- **The candidate field is settled at population scale.** SCDD S3 judged all 1,982 apparatus-primary catalog rows against the locked bar. Result: every face-off candidate re-derived, every S2 disqualifier re-derived, **zero new candidates that expand the locked field.** The anti-FOMO question ("did Anthropic's ecosystem surface something we missed") is answered empirically — no. The field below is the field. Stop re-broadening it (anchor INVARIANT; ledger GRAND TOTALS).
- **NornicDB entered, was dual-gated, and passed.** It did not exist as a named candidate in v1. It is now the strongest graph-native candidate and the topology/co-located-vector benchmark (D18).
- **The round-trip axis is empirically closed (this session).** v1 had no such test; the S4 verdict rated round-trip PASS-on-mechanism / empirical-pending (D21). As of S5 it is **PASS, byte-identical, proven across a cold reboot** (§6.4). The last hedge on the NornicDB acceptance contract is gone.
- **The gating action is resolved.** v1's gate (the Continuous-Claude-v3 read) is closed: it is NOTABLE-DQ (compresses corpus — fails §3.1). It is not a fork target. The decision is no longer "fork vs build" — it is a substrate selection between a graph-native benchmark and a low-ops default, both passing both gates.
- **The seam endgame is mapped.** v1 deferred the storage-seam (MCP connector) question entirely. v2 names the concrete connector per outcome (§9).
- **Canon re-grounded v5 → v8 / spec v1 → v4.** The three pending-schema-revision items v1 flagged (signature, display_content, attachments.extracted_content) all landed and are reflected in the consumer shape (§2).

---

## 1. Purpose and authority

The freeze pipeline (`Freeze_Pipeline_Spec_v4.md`) produces `records.ndjson` — a substrate-agnostic, scrubbed, append-only floor. This document evaluates candidate substrates against that consumer shape and against anchor invariants (v8), and makes a **recommendation**.

**Authority (unchanged from v1 §9, re-affirmed):** This doc is *authoritative input* to the substrate decision; it does **not** unilaterally lock the substrate. The lock sits with the apparatus thread (D7/D9), weighted at decision time against current anchor invariants, the current spec, and seed-shape data against the real archive. Same logic as "anchor wins when canon and handoff conflict": the canonical decision sits with the track that owns implementation. SCDD's job is to broaden + verify the field, apply both gates, surface open verifications, run the empirical where one is cheap and decisive, and recommend. **SCDD ran the empirical this session (§6) — that is SCDD doing its job, not SCDD taking the lock.** The lock is still apparatus's to ratify.

---

## 2. Inputs — what the substrate must consume

Per `Freeze_Pipeline_Spec_v4.md` Stage 4, re-grounded against v8 population findings:

- **Per-message records:** `{snapshot_id, scrub_version, conv_uuid, msg_uuid, parent_message_uuid, sender, created_at, updated_at, text, content_blocks, attachments, files, is_root}`. Append-only ndjson. `conv_name` is NOT carried (S12 propagation correction — symmetric with the `name`/`summary` floor-scoping drop).
- **Per-conversation headers:** `{record_type, snapshot_id, scrub_version, conv_uuid, created_at, updated_at, account_uuid, message_count, has_branches, multi_root}`. Conv-level `name` AND `summary` both dropped (S11 floor-scoping; both are user-/model-affected, neither is floor).
- **Branch + forest preservation:** every node lands as its own record with its real `parent_message_uuid`. No flattening, no branch selection. **`chat_messages` is tree-OR-forest** (9/294 convs in the existing archive carry 2–6 sentinel roots); `is_root` per-message + `multi_root` per-conversation handle the forest case explicitly. The substrate must preserve both branching and multi-root structure verbatim.
- **Scrub-version aware:** records carry their `scrub_version`; the substrate must tolerate cross-version pointer comparison as the scrub regex set evolves via `scrub-vN/` overlays. Sealed snapshots never re-scrub in place.
- **Thinking blocks are floor-grade content** alongside `text` — stored at equal fidelity. `signature` (populated on ~60% of thinking blocks, base64 cryptographic provenance, up to ~211K chars) is carried as an opaque string.

### 2.1 The size envelope the substrate must clear (settled at population scale, v8)

- **Max record size: 3.0 MB**, driven by `tool_result.content[].text` (NOT attachments — corrects the S12 suspicion). 19 records exceed 1 MB; **0 exceed 5 MB** in the existing archive.
- **p99 record ≈ 221 KB.** The 3.0 MB max is the gate-against figure; the typical record is three orders smaller.
- **`display_content` is NOT a universal mirror:** 84.4% of tool blocks are strip-safe, but 15.6% (`CARRIES_UNIQUE`) hold file text recoverable nowhere else in the record. The floor keeps everything; selective strip is a deferred load-time transform, not a storage-layer concern. **Storage-volume implication:** the substrate stores the full `display_content` for the 15.6%, so volume estimates must count it.
- **`attachments[].extracted_content`:** inlined file text (observed up to 1.4 MB), a cred-vector class handled upstream by the scrub. Substrates that hand off to MCP retrieval inherit a clean floor; substrates that ingest blob content directly must verify cred-cleanliness propagates (it does — scrub is a hard gate at Stage 2/3, verify-clean halts ingest on any hit).

**The acceptance bar that falls out of this:** a candidate must store a single ~3 MB inline string property, return it byte-identical, preserve a forest, and resolve a pointer to exactly one node — durably, across restart. That bar is what §6 tests.

---

## 3. Disqualifier rules (both gates required — unchanged from v1, re-stated)

### 3.1 Function gate — no AI-compression of the corpus

Any candidate whose value-add is **AI-compression / rewording / summarization / consolidation of the corpus at the storage layer** is auto-disqualified. The floor must be verbatim; compression is a drift vector inside the one artifact whose entire job is no-drift (the dead seed drifted 152× under exactly this failure mode).

This does NOT disqualify a candidate that wraps an AI-compression *retrieval* layer around a verbatim *storage* layer. The line: **storage holds verbatim; retrieval may do anything as long as it returns pointers, not reworded text.**

### 3.2 Shape gate — no REFUSED-wall violation by adoption-shape

Any candidate whose architectural shape *generalizes* toward REFUSED-wall territory is suspect, regardless of how narrowly apparatus would use it. The wall (capture mechanisms, scraping hooks, shared-corpus features) was drawn on principle at S10; adopting a tool whose shape pulls past that line creates inbound pressure — through dependencies, contributor priorities, feature requests, upgrades — to use the parts we said we wouldn't.

Shape-check questions: capture mechanisms (extension hooks, network intercepts, undocumented-endpoint scrapers)? scraping hooks (live page/DOM reads against rendered claude.ai/claude.com)? shared-corpus features (multi-account ingest, cross-account index, social/community layers)? does the architecture push from "personal grounding loop on sanctioned own-export" toward "general-purpose conversation hoarder"? Any yes is a flag, even if apparatus would only use the narrow subset.

**This gate has teeth — it is not theoretical.** The S3 dig dropped **19 real tools** on shape (§7.3): HTTP MITM proxies, CC-traffic tracers, browser-capture rigs, shared-corpus team-memory products. The wall describes live ecosystem shapes, not a hypothetical.

---

## 4. The candidate field (settled — S2 survey + S3 population dig, complete)

The field is closed. 1,982 rows judged; 13 GEMs, ~105 NOTABLE, ~33 NOTABLE-DQ, 19 SHAPE-FAIL, ~18 LEAKED-IP. What follows is the decision-relevant subset: the substrate contenders, the retrieval rigs, the seam connectors, and the fallbacks. The full ledger is `SCDD_S3_Keeper_Ledger_2026-05-28.md`.

### 4.1 NornicDB (orneryd/NornicDB, ~750★) — the graph-native benchmark — DUAL-GATE PASS

- **License/stack:** MIT · Go 1.26 · BadgerDB LSM storage backend · Neo4j-Bolt + qdrant-gRPC compatible · sub-ms HNSW vector search. Tested this session at **v1.1.2**.
- **Function gate (§3.1): PASS (clean).** A message = a node; `text`/`content_blocks` store as string/JSON properties. Property validation is a TYPE gate, not a SIZE gate — any string passes regardless of length; no compression/summarization anywhere on the write path. It is a database, not an AI-compressor.
- **Shape gate (§3.2): PASS.** Passive datastore: data in, queries out. No capture/scrape/harvest surface — REFUSED-wall signatures (`chat_conversations`, claude.ai endpoints, `browser.extension`) absent from the tree. Two privacy positives: default embedding is **local** (Ollama/local-GGUF; OpenAI is opt-in, so the corpus doesn't egress to embed) and **replication is off by default** (standalone single-node). Adopting it creates zero inbound pressure toward the wall.
- **Retention gate: PASS (rare double).** (a) No GC/decay by default — `decayEnabled` is zero-value false, retention policies are not auto-loaded, and decay here is a read-path *ranking score*, not storage eviction (even ON it down-weights, it does not delete). (b) Mapping-immunity by construction — the pointer carries `snapshot_id`, so the same message in two exports is two distinct nodes, never two versions of one node; we never issue an update, so MVCC versioning never engages and decay/GC has nothing to act on. **Immortality rides the modeling, not the engine** (temporal-MVCC correctly NEUTRAL).
- **Dead-weight: DING (tie-breaker, not DQ).** Carries temporal-MVCC, decay-reconcile, retention-policy, embedding/K-means scheduler, Heimdall (built-in LLM), and GPU paths — all unused for verbatim graph storage + pointer retrieval + co-located vectors. Heavier binary than a single-static-binary candidate. Correctness-neutral; ranking tie-breaker only.
- **Acceptance contract: 4/4** (one was empirical-pending at S4; closed this session — see §6):
  - 3.0 MB record lands inline — PASS. `maxNodeSize` (50KB) only externalizes embedding vectors; the body stays inline. Binding per-node ceiling is ~16 MiB (`walMaxEntrySize`, the WAL anti-corruption guard), which our 3.0 MB max clears ~5.3× (~75× at p99). **No content-block split adapter needed** (the pre-vetted D16 adapter is CLEARED).
  - pointer → exactly one node — PASS. Node ID = the pointer; unique-constraint machinery exists.
  - **byte-identical round-trip — PASS, EMPIRICALLY PROVEN (S5, §6).** Was PASS-on-mechanism / pending at S4.
  - tree-or-forest preserved — PASS (strong). `parent_message_uuid` → edge; multi-root → multiple `is_root` nodes. This is the shape graph DBs are *for*, and where NornicDB beats a relational substrate that simulates the tree in a self-referential FK.
- **Verdict:** strongest graph-native candidate; the topology + co-located-vector benchmark. Does **not** auto-win (D9 — apparatus's call). Scores exactly where the ledger predicted.
- **Lock-time invariants if NornicDB wins (D20 — HARD config gates, not reliance on defaults):**
  - `decay` OFF, `auto_links` OFF, `retention_enabled` false, `kmeans` OFF, `auto_tlp` OFF, `heimdall` OFF.
  - **⚑ Sharpened this session:** the shipped `nornicdb.example.yaml` sets `decay_enabled: true`, `auto_links_enabled: true`, and `embedding.enabled: true` — i.e. the *code* default is safe but the *example config a user would copy* is NOT. A copy-paste deploy would silently enable a 2-second decay worker and an embedder that both touch frozen nodes. D20 is therefore not optional hygiene; it is a load-bearing gate against an immortal-GC landmine that the vendor's own example would walk you into. Pin every toggle explicitly at launch (flag or env), never inherit the yaml.

### 4.2 Supabase + pgvector — the low-ops default — DUAL-GATE PASS

- **Source/license:** Jake's existing stack · Apache-2.0 (Supabase) / PostgreSQL.
- **Function gate: PASS (clean).** Each row = one record; no compression. Append-only at row level. Branch preservation clean (`parent_message_uuid` column). Scrub-version clean (column).
- **Shape gate: PASS.** Database substrate; no capture/scrape shape. Pre-existing in Jake's stack. Adoption introduces zero REFUSED-wall pressure.
- **Trade-offs:** PRO — native fit for the storage-seam endgame; auth/backup/ops already solved; Postgres is forever; lowest operational surface because it's already running. CON — the conv tree is simulated in a self-referential FK rather than stored graph-native; vector recall over interleaved branches needs a seed-shape check; embedding choice (model/dimension/cost) is its own decision tree.
- **Verdict:** the lowest-ops default already in the stack. The honest framing for the apparatus lock: **NornicDB is the strongest graph-native candidate and the benchmark; Supabase is the lowest-ops default already in the stack.** This is a genuine engineering trade (graph-native fidelity vs operational simplicity), not a winner-and-also-rans.

### 4.3 Retrieval rigs (storage-agnostic — borrow the rig, not a storage opinion)

- **zippoxer/recall (186★) — the one conversation-native GEM in the entire dig.** Verbatim FTS + resume directly over Claude conversation records. fn-CLEAN (verbatim), shape-CLEAN (local own-data). Directly borrowable retrieval rig for `records.ndjson`. **Open: validate §3.2 against the real records.ndjson shape before borrowing** (escalation #1).
- **thedotmack/claude-mem (79k★)** — retrieval rig borrowable; compression layer must be actively skipped per §3.1 (not just unused).
- **MinishLab/semble (4.4k★)** — CPU-only fast search, MIT; conv-stream adapter needed (currently code-oriented).
- **oraios/serena (24.7k★), zilliztech/claude-context (11.6k★)** — pointer-style code-retrieval archetype; reinforcers, code-domain.

### 4.4 Alternative substrates (passed both gates; benched behind the two leads)

- **DeusData/codebase-memory-mcp (2.7k★, C, MIT)** — single-static-binary knowledge graph; the cleanest ops story in the field (zero deps); KG model maps well to the conv tree. CON: C codebase is harder to fork (falls to CC, not Jake); conv-stream adapter needed. The lightweight alternative if a single-binary ops story ever outweighs graph-native features.
- **doobidoo/mcp-memory-service (1.9k★)** — verbatim storage + KG; forest-fit needs a custom schema.

### 4.5 ⚑ Temporal-graph fallbacks (pre-vetted; only relevant if NornicDB had failed — it didn't)

- **memtrace-public (bi-temporal KG, ZERO-LLM mechanical)** — FALLBACK #1.
- **arbor (graph-native deterministic, MCP-native)** — FALLBACK #2.
- **open-ontologies** — FALLBACK #3 (from S2).

These stay benched. NornicDB passed; the fallbacks are insurance, not contenders.

---

## 5. Comparison matrix

Both gates required. ✓ passes · ✓✓ strong · ? unverified · — n/a · ✗ fails.

| Candidate | Fn (§3.1) | Shape (§3.2) | Branch/forest | 3MB inline | Round-trip | Ops | Role |
|---|---|---|---|---|---|---|---|
| **NornicDB** | ✓ | ✓ | ✓✓ graph-native | ✓ (~5.3× headroom) | ✓✓ **empirical (S5)** | MED (ding: dead weight) | **Graph-native benchmark** |
| **Supabase + pgvector** | ✓ | ✓ | ✓ (FK-simulated) | ✓ | ✓ (Postgres) | LOW (Jake's stack) | **Low-ops default** |
| recall (rig) | ✓ | ✓ verify | — (rig) | — | — | LOW | Conv-native retrieval rig |
| claude-mem (rig only) | ✓ rig | ✓ | ✓ | — | — | MED | Rig, compression-skip |
| codebase-memory-mcp | ✓ | ✓ | ✓✓ | ? | ? | LOWEST (static bin) | Benched alt-substrate |
| memtrace-public / arbor | ✓ | ✓ | ✓ | ? | ? | LOW | Benched fallbacks |

---

## 6. The round-trip empirical — RAN AND PASSED (S5, this session)

This is the section v1 could not contain and the S4 verdict left open as the one named pre-lock gate (D21). It is now closed.

### 6.1 Why this test, specifically

All three S4 reads rated byte-identical round-trip PASS *on mechanism* but flagged the identical residual: the repo's existing large-node test (`badger_large_embedding_txn_test.go`, ~6.9 MB node) exercises the **embedding-externalization** path (ChunkEmbeddings → separate keys), NOT the **inline multi-MB string-property** path that our floor's size-driver (`tool_result.content[].text`) actually uses. Distinct code paths. Two reads crediting each other for closing the axis is exactly where a gap hides (judgment-call ledger, S4) — so the empirical was held as a hard pre-lock gate rather than assumed. Append-only makes a wrong substrate immortal; a normalization bug discovered after lock is a permanent corruption. The test is cheap insurance against an expensive, irreversible failure.

### 6.2 Method (inert by construction)

A disposable Debian 13 LXC on Castle Black (the PVE host where NornicDB would live if it wins — so the test doubled as deploy recon; teardown via `pct destroy`, host stays clean). Built from source, `CGO_ENABLED=0` (pure-Go, no llama/GPU — we don't need embeddings for a storage test), `-tags noui` (headless, sidesteps the `ui/dist` embed dependency). Server launched **maximally inert**, confirmed by NornicDB's own startup log: auth, MCP, Heimdall, BM25, vector search, embeddings, decay, and auto-links **all OFF**. This matters — any background worker (embedder, indexer, decay) touching the test node between write and read would contaminate the byte-diff, making a mismatch ambiguous (storage corruption vs. a worker rewrite). The store was motionless: data in, sits, data out, nothing else moving.

### 6.3 Payload (adversarial)

A single inline string property, **4,122,695 bytes** — ~1.37× the 3.0 MB max record ceiling (deliberate margin), packed with the content classes most likely to expose hidden normalization: double quotes, `{json: true}` braces, `\esc\` backslashes, newlines, and multibyte UTF-8 (`café ☕ 日本語`). The byte count exceeding the 3.6 MB string-length target confirms the multibyte characters were counted as raw bytes.

### 6.4 Result — GREEN, both halves

```
=== EVIDENCE BLOCK — round-trip empirical, 2026-05-28 20:28:43 UTC ===
binary:                71,533,267 bytes, NornicDB v1.1.2
payload:               4,122,695 bytes (~1.37× the 3.0MB max record ceiling)
pre-restart  sha256:   21347a69592575748172107bd97e66c6b14285bc853a3df343ca0a4c477ca107
post-restart sha256:   21347a69592575748172107bd97e66c6b14285bc853a3df343ca0a4c477ca107
on-disk vlog after reboot: 4,123,037 bytes (000002.vlog)
inert config (per startup log): auth/mcp/heimdall/bm25/vector/embeddings/decay/auto-links ALL off
PRE-RESTART:  PASS ✅
POST-RESTART: PASS ✅ — byte-identical across a full container reboot
```

- **Pre-restart:** write → read → hash. 4,122,695 bytes in, 4,122,695 out, sha256 identical. Zero normalization on the inline-string path through quotes/braces/backslashes/emoji/CJK/newlines.
- **Post-restart (the half that earns it):** full `pct reboot 999` — server process killed, filesystem flushed, container cold-booted, BadgerDB re-opened the on-disk store from scratch — then read the node back. sha256 still identical. **Proves durability across flush-to-disk-and-reload, not just an in-memory echo.**
- **Physical D19 confirmation (bonus):** the ~4.1 MB body landed in `000002.vlog` (BadgerDB value-log) at 4,123,037 bytes and survived the reboot intact — the verdict's prediction that 3 MB+ values route to vlog (>1 MB ValueThreshold) confirmed on disk, not just in code.

### 6.5 What this closes

D21 closes empirically. The NornicDB acceptance contract is **4/4 with no hedge remaining**. The round-trip line in this document now reads *empirically proven (byte-identical, pre+post-reboot, v1.1.2)* and no longer carries the PASS-on-mechanism / empirical-pending qualifier. D18's last open cell is filled.

**Scope honesty (carried from the S4 downstream flag):** the test was run on Castle Black for convenience + Linux + deploy-recon. "We tested it on X" is NOT "it deploys on X." Where NornicDB lives if it wins (PVE host vs LXC vs VM vs elsewhere) is a separate JAKE-STACK / substrate-lock decision, untouched by this test. The plumbing tax to get a 30-second test runnable (Docker-absent → no Windows binary → Castle Black → SSH/1PW → in-container shell) was normal first-touch friction on a new box and is not a substrate-fitness finding.

---

## 7. Resolved closures (so they are not re-litigated)

### 7.1 v1's gating action — RESOLVED

**parcadei/Continuous-Claude-v3** (v1's cover-to-cover gating read) is **NOTABLE-DQ — compresses corpus (fails §3.1).** It is not a fork target. The substrate decision is therefore NOT "fork an existing apparatus vs build" — it is a clean substrate selection between §4.1 and §4.2. v1 §6/§7's entire scenario tree is obsolete.

### 7.2 Disqualified families (NOTABLE-DQ — DO NOT RESURFACE)

Four DQ families, all violating verbatim-no-discard: (1) Karpathy-LLM-wiki synthesis (claude-obsidian, the llm-wiki cluster, swarmvault, hyperresearch); (2) compression-of-corpus (Continuous-Claude-v3, headroom, memvid/claude-brain `.mv2`, MEM8/smart-tree, MegaMemory); (3) cognitive-decay / forgetting-curve / Mem0-class (vestige, YourMemory, shodh-memory, heimdall); (4) consolidation/abstraction (graph-memory triples-transform, roampal, prism-coder). **memvid specifically** — v1 carried it as "locate + read"; it is now closed DQ (`.mv2` compresses). Do not re-open.

### 7.3 SHAPE-FAILs in the wild (the §3.2 gate is real — 19 dropped + flagged)

Traffic interception/MITM (Charles-mcp, claude-tap, ccproxy, claude-inspector, mcp-reticle, DrissionPageMCP); browser/computer-use capture (stealth-browser-mcp, byob, flowlens, native-devtools-mcp, claude-conversation-extractor); shared-corpus/multi-user (hivemind, egregore, Grov, omem, agentlogs, eion, im4codes, ogham). These are the live ecosystem shapes the REFUSED wall describes. Their existence is the argument for the wall, not against it.

### 7.4 Anti-FOMO — CLOSED at population scale

The S3 dig judged all 1,982 apparatus-primary rows and found **zero candidates that expand the locked field**. Every face-off candidate and every S2 DQ re-derived independently. The "Anthropic could add something we missed" worry is killed empirically (anchor INVARIANT; ledger GRAND TOTALS). The field in §4 is the field.

---

## 8. Recommendation

The candidate field has collapsed to a genuine two-way engineering trade, both passing both gates, both with the acceptance contract satisfied (NornicDB's now empirically, Supabase's by Postgres's nature):

- **NornicDB** — strongest graph-native fidelity. The parent-chain/forest is stored as a graph rather than simulated; vectors are co-located; round-trip is empirically proven at 1.37× the max record size across a cold reboot. Cost: a heavier binary with unused subsystems (ding, not DQ) and a hard requirement to pin the example-config landmines off at lock (D20).
- **Supabase + pgvector** — lowest operational surface. Already in Jake's stack; auth/backup/ops solved; native fit for the storage-seam endgame. Cost: the tree is FK-simulated, and branch-aware vector recall wants a seed-shape check.

**SCDD's recommendation to apparatus:** carry both into the lock decision as co-leads, framed honestly as fidelity-vs-ops. The deciding input should be the **seed-shape test on the real archive** (§10) — append-only means an un-ratified substrate choice is immortal, so the only fully honest verdict is the real `records.ndjson` ingested and queried at scale on each lead. Absent a reason to prefer graph-native fidelity *now*, the low-ops default (Supabase) is the safer first lock with NornicDB as the proven upgrade path, because the seam connectors exist for both (§9) and the round-trip proof means NornicDB can be adopted later without re-opening the storage-integrity question. **The lock is apparatus's (D9).**

---

## 9. Storage-seam endgame (the MCP connector per outcome)

The substrate talks to the orchestrator through an MCP connector. The S3 dig pre-identified the concrete connector for each outcome (engine-path GEMs), so the seam is not a fresh search after the lock:

- **If Supabase wins:** `alexander-zuev/supabase-mcp-server` (822★) — Supabase MCP with migration versioning + query exec. The strongest practical seam find; matches the default stack.
- **If NornicDB wins:** its own engines are individually MCP-served — `neo4j-contrib/mcp-neo4j` (949★, Neo4j-Bolt = NornicDB's Bolt engine) + `qdrant/mcp-server-qdrant` (1.4k★, qdrant-gRPC = NornicDB's vector engine). Two official connectors cover its two protocols.

On-path Postgres-ops references if Supabase wins: `call518/MCP-PostgreSQL-Ops`, `timescale/tiger-cli`, `qdrant/skills`.

---

## 10. Open verifications (carried to apparatus / next SCDD)

1. **Seed-shape test on the real archive** — the final commit gate for whichever lead(s) advance. Ingest real `records.ndjson` (the 5-28 export delta fixture: 1,337 net-new msgs is a ready slice) and query at scale. Append-only ⇒ this is the only honest verdict. GATING for the lock.
2. **recall §3.2 validation** against the real records.ndjson shape before any rig borrow (escalation #1).
3. **kept (egroup-labs, 100★)** — GEM-or-SHAPE-FAIL hinges ENTIRELY on whether its multi-platform ingest is export-based (GEM #2) or browser-scrape (SHAPE-FAIL). **Do NOT borrow its ingest until verified** (escalation #2).
4. **shared-memory borderline re-gate** — eion/ogham/imcodes/mainline: single-user-multi-tool vs actual multi-user reclassify (escalation #4).
5. **Supabase branch-aware vector recall** — do embeddings get confused by interleaved branches? (only if Supabase advances to seed-shape).

---

## 11. What this doc deliberately does not cover

- The retrieval interface design — substrate-specific, after lock.
- Embedding choice (if Supabase wins) — its own decision tree.
- Per-project anchor passes — built on top of the substrate.
- Index design over the substrate — substrate-dependent.
- The raw.json wipe-vs-retain invariant — that is an **anchor** decision (open at the top of ANCHOR v8's invariants), not a FaceOff decision. **See the downstream hook in §13** — it interacts with Jake's S5 standing posture and should be ratified at the anchor enshrine.

---

## 12. Convergence observation (carried from anchor v8 §12 / S14)

Three independent function-fail candidates in the dig split the same way the apparatus does: a raw-immutable layer and a derived-queryable layer. The difference is they **compress** the derived layer; **we keep verbatim pointers.** No public repo stores verbatim-by-pointer-into-an-immutable-snapshot — they all extract/summarize/compress. The mechanics are borrowable; the *model* is ours. The round-trip proof (§6) is part of why the verbatim model is viable where others compressed: we demonstrated that a real graph engine stores multi-MB verbatim bodies losslessly and durably, so the compression those projects reach for is not a storage necessity — it is a choice we decline.

---

## 13. Downstream flags (protect the timeline)

- **⚑ raw.json wipe-vs-retain + Jake's S5 export-delete posture (NEW, this session).** At S5 Jake stated a standing posture: delete the Anthropic export off disk after processing — *"Anthropic has my export on demand, I don't need to hold 'em."* This is Path A's logic (kill unscrubbed-cred-at-rest; the scrubbed snapshot is the floor; re-export if raw is ever truly needed) applied one level up to the export bundle itself. **Recommendation: ratify Path A at the anchor enshrine** (wipe raw.json after Stage 3 verify-PASS; invariant text already says "raw wiped" — Path A makes code match canon). This is consistent with the stated posture and with the project's whole cred stance ("an immortalized cred is the failure mode"; a sealed-but-present unscrubbed raw is that, one chmod away). **Jake's call to confirm at enshrine** — flagged here, not silently applied.
- **example-config landmine (NEW, §4.1).** If NornicDB wins, D20's pin-everything-off is mandatory at lock specifically because the shipped `nornicdb.example.yaml` enables decay + auto-links + embeddings. Will bite a copy-paste deploy. Carry into the lock-time config invariant.
- **test-host ≠ deployment-host (§6.5).** "Tested on Castle Black" is not "deploys on Castle Black." Don't let it become so by default.
- **seed-shape test is the real lock gate (§10).** This doc proves the *storage primitive* is sound on both leads; it does NOT substitute for ingesting the real archive at scale. The lock should not happen on this doc alone.
- **canon authored at session-top next time.** This v2 was authored at S5 on explicit Jake authorization for a full-file rewrite. It folds everything current as of 2026-05-28. The next canon mutation should still follow the enshrine-on-fresh-context discipline.

---

## 14. Judgment-call ledger (this document)

- **Authored v2 as a full-file rewrite, not a v1 patch** (S5). v1 was grounded against v5 invariants, pre-dated the NornicDB candidate and the dual-gate, and gated on a now-resolved read. A patch would have buried live canon under stale scaffolding. Jake gave explicit full-file authorization. Confidence HIGH.
- **Recommended Supabase as the safer first lock with NornicDB as a proven upgrade path** (§8). This is a recommendation, not a verdict — the lock is apparatus's (D9). Reasoning: lowest ops, already in stack, and the round-trip proof + existing seam connectors mean NornicDB can be adopted later without re-opening storage integrity. A reader who weights graph-native fidelity higher *now* could reasonably lock NornicDB first; both are defensible. ~70% on "Supabase-first is the lower-regret path," explicitly deferred to apparatus + the seed-shape test. Source: the dual-gate verdict + this session's empirical + the §9 seam map.
- **Path A recommended on raw.json** (§13) — derived from Jake's stated S5 posture, flagged for ratification not applied. Confidence that it matches Jake's intent: HIGH (he said it plainly this session); confidence it's the right call: HIGH (consistent with the whole cred stance). Still Jake's pen at enshrine.
- **Round-trip rated empirically closed** (§6) — based on the captured evidence block from Jake's own terminal this session (PRE==POST, 4,122,695 bytes, full reboot). This is the strongest evidence class available (live byte-diff across cold reload), not a code-read. Confidence HIGH.

---

*TWW SCDD S5 close. Supersedes v1. Grounded against ANCHOR v8 + Freeze_Pipeline_Spec v4 + the complete 1,982-row S3 ledger + the three-read NornicDB dual-gate + the S5 round-trip empirical (green, pre+post-reboot, byte-identical at 1.37× max record size). The substrate field is settled; the storage primitive is proven on the graph-native lead; the lock is apparatus's to ratify on the seed-shape test. Be worth the lineage.*
