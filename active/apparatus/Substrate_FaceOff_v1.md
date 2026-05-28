# Substrate Face-Off — apparatus retrieval layer

*file: Substrate_FaceOff_v1.md · v1 · TWW SCDD S1 · 2026-05-27*
*track: The Wallaby Way · feeds apparatus NEXT MOVE #3*
*revision 2026-05-27 ~19:58 ET — pre-commit, folds the S12 cross-track ack (decision-authority clarification + shape-disqualifier methodology + pending-schema-revisions). See §11 change log.*

---

## 1. Purpose

The freeze pipeline (`Freeze_Pipeline_Spec_v1.md`) produces `records.ndjson` — substrate-agnostic. This doc evaluates candidate substrates against that consumer shape and against apparatus anchor invariants, surfaces open verifications, and recommends the gating action before substrate lock.

**This doc is authoritative INPUT to the substrate decision; it does NOT make the decision.** The decision authority sits with the apparatus thread at NEXT MOVE #3 — weighted against current anchor invariants (v5 today, v6 when the S12 robustness probe lands), the current spec (v1 today, v2 when it lands), and Stage 1–4 seed-shape data against the existing 366MB archive. Same logic as "anchor wins when canon and handoff conflict": canonical decision sits with the track that owns implementation; this doc narrows the field and surfaces the questions.

---

## 2. Inputs — what the substrate must consume

Per Freeze_Pipeline_Spec_v1.md §4 Stage 4:

· **Per-message records:** `{snapshot_id, scrub_version, conv_uuid, msg_uuid, parent_message_uuid, sender, created_at, updated_at, text, content_blocks, attachments, files, is_root}`. Append-only ndjson.
· **Per-conversation headers:** `{record_type, snapshot_id, scrub_version, conv_uuid, created_at, updated_at, account_uuid, message_count, has_branches}`. Conv-level `name` and `summary` BOTH dropped per the S11 floor-scoping correction.
· **Branch preservation:** every node lands as its own record with its real `parent_message_uuid`. No flattening, no branch selection.
· **Scrub-version aware:** records carry their scrub-version; substrate must handle cross-version pointer comparison when scrub regex set evolves.

**Field-level claims here are pending revision** — S12's pre-Stage-0 robustness probe falsified the v5 anchor's "signature is null in export" claim (populated on ~60% of thinking blocks, 196–211,384 chars), surfaced a `display_content` cluster (~25K tool blocks) not in S11's enumeration, and surfaced `attachments[].extracted_content` (inlined file text up to 1.4MB, cred vector class). Anchor v6 + spec v2 will correct. See §10 for what specifically may need re-checking when v6/v2 land.

---

## 3. Disqualifier rules (both gates must pass)

### 3.1 Function disqualifier — AI-compression of corpus

Any candidate whose value-add is **AI-compression of the corpus** is auto-disqualified at the storage layer. The corpus floor must be verbatim; compression introduces a drift vector inside the one artifact whose job is no-drift. (The dead seed drifted 152× under that exact failure mode.)

This does NOT disqualify candidates that wrap an AI-compression *retrieval* layer around a verbatim *storage* layer. claude-mem is the canonical example: its retrieval rig is borrowable; its compression layer is not. The line: storage holds verbatim; retrieval can do whatever as long as it returns pointers, not reworded text.

### 3.2 Shape disqualifier — REFUSED-wall violation by adoption-shape

[Methodology contribution from apparatus S12 cross-track ack, 2026-05-27 ~19:52 ET]

Any candidate whose architectural shape *generalizes* toward REFUSED-wall territory is suspect, regardless of how narrowly apparatus would use it. The REFUSED wall (capture mechanisms, scraping hooks, shared-corpus features) was drawn on principle at S10; adoption of any tool whose shape pulls past that line creates inbound pressure — through dependencies, contributor priorities, feature requests, version upgrades — to use the parts we said we wouldn't.

Shape-check questions for any "parallel build of apparatus" candidate:

· Does the candidate include capture mechanisms (browser-extension hooks, network intercepts, undocumented-endpoint scrapers)?
· Does it have scraping hooks (live page reads, DOM-scrape utilities, anything that operates against rendered claude.ai or claude.com)?
· Does it have shared-corpus features (multi-user-account ingest, cross-account index, social/community layers)?
· Does its architecture push toward generalizing from "personal grounding loop on sanctioned own-export" to "general-purpose conversation hoarder"?

If any answer is yes — even if apparatus would only use the narrow subset — that's a flag. Function check ("does it return pointers") + shape check ("does adoption pull apparatus past S10's line"). Both gates required.

---

## 4. Candidate inventory

Eight candidates evaluated. Three TWW-named (carried from v5 NEXT MOVE #3), five SCDD-surfaced (chunks apparatus_001 + apparatus_002).

### 4.1 Supabase + embeddings (TWW-named, status quo)

· **Source:** Jake's existing stack (Supabase Postgres, pgvector ext).
· **License:** Apache-2.0 (Supabase) · PostgreSQL (Postgres).
· **Architecture:** Postgres table with embedding column (pgvector) + scalar metadata. Each row = one record from records.ndjson. Retrieval = vector similarity + scalar filters (snapshot_id, conv_uuid, sender, etc.).
· **Function check (§3.1):** Pointer-style CLEAN. Each row IS the record; no compression. Append-only at row level. Branch preservation CLEAN (parent_message_uuid column). Scrub-version CLEAN (column).
· **Shape check (§3.2):** CLEAN. Database substrate; no capture or scraping shape. Pre-existing in Jake's stack for unrelated purposes. Adoption doesn't introduce REFUSED-wall pressure.
· **Integration:** records.ndjson → COPY FROM → batch upsert. Embeddings generated at ingest. Retrieval API = SQL + pgvector + optional MCP wrapper.
· **Trade-offs:**
  - PRO: Native fit for storage-seam endgame (anchor NEXT MOVE #9). Already in Jake's stack; auth + backup + ops already solved. Postgres is forever.
  - CON: Embedding choice is its own decision tree (model · dimension · cost). Vector recall on tree-structured conv data needs verification (do embeddings get confused by interleaved branches?). Seed-shape test will answer.
· **Open verifications:**
  - Vector recall against branched conv data.
  - Embedding model selection (local vs OpenAI vs hybrid).
  - Cost projection at full archive scale (22,801 messages × dim).

### 4.2 memvid (TWW-named, single-file counter-design)

· **Source:** TWW v5 anchor NEXT MOVE #3.
· **Status in SCDD catalog:** NOT FOUND in chunks 001–002. v0.2 patch grep pending — may be in lower-star chunks or below the stars≥100 filter.
· **Architecture (from anchor memory):** single-file counter-design to database-backed substrates. Local file is the corpus + index.
· **Function check (§3.1):** UNVERIFIED until repo located + read. "Single-file" framing suggests verbatim storage with in-file index — likely CLEAN on pointer-style.
· **Shape check (§3.2):** UNVERIFIED until read. Worth scrutinizing whether the project's broader scope pulls toward shared-corpus or capture territory.
· **Open verifications:**
  - Locate the repo (Jake's reference name; not in my catalog as named).
  - Read architecture cold — function and shape both.
  - Verify pointer-style storage.
  - Verify scaling characteristics at 22,801-message-scale.

### 4.3 thedotmack/claude-mem (TWW-named, retrieval-rig borrow only)

· **Source:** SCDD chunk_apparatus_001, also in prior-art doc.
· **Stars:** ~79k.
· **License:** Apache-2.0.
· **Architecture:** SQLite FTS5 + Chroma + HTTP API. AI-compression layer wraps storage.
· **Function check (§3.1):** Storage layer CLEAN (SQLite/Chroma directly). Compression layer DISQUALIFIED — skip.
· **Shape check (§3.2):** Mostly CLEAN. Local-only, single-user, sanctioned-input-oriented. The "memory" framing has some shape-drift potential (positioning as general Claude memory layer rather than personal grounding loop), but the technical architecture doesn't pull toward REFUSED territory.
· **Integration:** records.ndjson → SQLite FTS5 table (verbatim) + Chroma embedding store (vector index). Use claude-mem's HTTP retrieval API or bypass to direct SQL/Chroma queries.
· **Trade-offs:**
  - PRO: Battle-tested at scale. Retrieval rig is the borrowable component.
  - CON: Operational complexity (two stores). Compression layer must be actively avoided, not just unused.
· **Open verifications:**
  - Confirm SQLite/Chroma layer can be used independently of compression.
  - Compare retrieval quality to Supabase+pgvector at archive scale.

### 4.4 zilliztech/claude-context (SCDD-surfaced)

· **Source:** SCDD chunk_apparatus_001, score 25 (highest in chunk).
· **Stars:** ~10k+ (post-cutoff ecosystem, exact at time of crawl).
· **License:** Apache-2.0 (presumed; verify at deep-read).
· **Architecture:** Vector + semantic MCP server. Pointer-style by design.
· **Function check (§3.1):** Pointer-style CLEAN. MCP-native, returns pointers, not reworded text. Branch preservation UNVERIFIED.
· **Shape check (§3.2):** Likely CLEAN — MCP server architecture is bounded by its protocol. Worth verifying that Zilliz's broader product positioning doesn't pull toward shared-corpus features (multi-tenant indexes, cross-account search).
· **Integration:** records.ndjson → claude-context ingest API → MCP server exposes retrieval to Claude orchestrator.
· **Trade-offs:**
  - PRO: MCP-native means orchestrator already knows how to call it. Score 25 indicates breadth of capability.
  - CON: Zilliz (vector DB co.) means dependency on their stack philosophy; pgvector is more vendor-neutral. Less battle-tested at long-term operational stability than Supabase.
· **Open verifications:**
  - Tree-structured query support.
  - Independence from Zilliz cloud (self-hostable?).
  - License confirm.
  - Shape-check: any multi-tenant or shared-index features in the codebase?

### 4.5 MinishLab/semble (SCDD-surfaced)

· **Source:** SCDD chunk_apparatus_002.
· **Stars:** 4,419.
· **License:** MIT.
· **Architecture:** CPU-only code search lib. 98% fewer tokens than grep+read. Indexing+searching a full codebase end-to-end <1s. ~200× faster indexing and ~10× faster queries than code-specialized transformers at 99% of retrieval quality. Runs as MCP server OR shell-callable.
· **Function check (§3.1):** Pointer-style CLEAN by description (code-search lib returns location+context, not reworded code). UNVERIFIED on conv data specifically.
· **Shape check (§3.2):** CLEAN. Code-search library, narrowly scoped. No capture mechanisms or shared-corpus shape.
· **Integration:** records.ndjson → semble ingest (custom adapter — currently code-search-oriented, would need conv-stream wrapper) → MCP server.
· **Trade-offs:**
  - PRO: Benchmarked. CPU-only. Light dependencies. MIT.
  - CON: Currently positioned for code, not conv streams. Adaptation work required. Newer (less battle-tested at long-term ops).
· **Open verifications:**
  - Adapt semble to conv-stream data (does its tokenization assume code?).
  - Branch-tree query support.
  - Operational longevity (4.4k stars is solid but not yet at the "tool that will be alive in 5 years" threshold).

### 4.6 DeusData/codebase-memory-mcp (SCDD-surfaced + prior-art)

· **Source:** SCDD chunk_apparatus_002 + prior-art doc.
· **Stars:** 2,746.
· **License:** MIT.
· **Language:** C.
· **Architecture:** High-performance code intelligence MCP server. Indexes codebases into persistent knowledge graph. 155 langs. Sub-ms queries. 99% fewer tokens. Single static binary, zero dependencies.
· **Function check (§3.1):** Pointer-style CLEAN (knowledge graph returns nodes+edges, not reworded text). Branch preservation GOOD MATCH on knowledge-graph model.
· **Shape check (§3.2):** CLEAN. Codebase-intelligence tool; no capture or shared-corpus shape. Single static binary is the cleanest possible shape — zero pull toward feature creep into refused territory.
· **Integration:** records.ndjson → graph ingest adapter → MCP server.
· **Trade-offs:**
  - PRO: Single-binary deployment is the cleanest ops story in the field. Knowledge-graph model maps well to conv tree. MIT.
  - CON: C codebase = harder to fork+modify than Python/TS. Codebase-oriented by default; conv-stream adaptation needed. 2.7k stars is mid-range.
· **Open verifications:**
  - Conv-stream ingest adapter feasibility.
  - C codebase modification appetite (Jake doesn't code; modifications would fall to CC).
  - Long-term maintainer signal.

### 4.7 AgriciDaniel/claude-obsidian + DragonScale Memory (SCDD-surfaced)

· **Source:** SCDD chunk_apparatus_002.
· **Stars:** 5,617.
· **License:** MIT.
· **Architecture:** Persistent, compounding wiki vault based on Karpathy's LLM Wiki pattern. 11 skills. Multi-agent support. Optional DragonScale Memory extension: log folds, deterministic page addresses, semantic tiling lint, boundary-first autoresearch.
· **Function check (§3.1):** LIKELY CLEAN on base claude-obsidian (wiki pages with deterministic addresses = pointers). DragonScale's log folds are append-only by design — STRONG match with spec §5.2. **UNVERIFIED:** does the extension reword content during ingest? Base claude-obsidian "drops sources, agent reads them, extracts entities" suggests SOME rewriting on ingest. Need to confirm whether DragonScale's log folds are verbatim or compressed.
· **Shape check (§3.2):** CLEAN. Obsidian vault model is local-first, personal-corpus by default. The "multi-agent support" framing warrants a closer read to confirm it doesn't include shared-corpus features, but Obsidian's underlying model is single-vault.
· **Integration:** records.ndjson → Obsidian vault adapter (one .md per record? per conversation? per scope?) → DragonScale indexes.
· **Trade-offs:**
  - PRO: Architectural family matches the apparatus more closely than any other candidate. "Karpathy LLM Wiki pattern" is the lineage. MIT. Obsidian as substrate means Jake gets a human-readable view of the corpus for free.
  - CON: Obsidian coupling. Vault file scale at 22,801 messages × 294 convs needs measurement. The base wiki tool may reword on ingest; only DragonScale's append-only log layer is unambiguously verbatim.
· **Open verifications:**
  - DragonScale verbatim-vs-reword question.
  - Vault file scale at archive size.
  - Obsidian operational complexity (do we want a graphical app in the pipeline?).
  - Shape-check: confirm "multi-agent support" is local-only orchestration, not shared-corpus.

### 4.8 parcadei/Continuous-Claude-v3 (SCDD-surfaced, DUAL-GATE READ REQUIRED)

· **Source:** SCDD chunk_apparatus_002.
· **Stars:** 3,789.
· **License:** MIT.
· **Language:** Python.
· **Architecture (per README):** "Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows." 109 skills, 32 agents, 30 hooks. **Has a Memory System and Continuity System.**
· **Function check (§3.1):** UNKNOWN until architecture is read.
· **Shape check (§3.2):** **THIS IS WHY THE READ MATTERS.** The framing — "persistent, learning, multi-agent development environment, ledgers, handoffs, continuity" — is suspiciously close to the apparatus's own architecture. But 109 skills + 32 agents + 30 hooks is broad; any subset could pull toward REFUSED territory. Shape-check verification questions for the read:
  - Does it include any capture mechanisms (browser extension, network hooks, scraping)?
  - Does it have any shared-corpus features (multi-account, cross-user, social)?
  - Do any of the 30 hooks operate against undocumented endpoints?
  - Does the "MCP execution without context pollution" mechanism rely on intercepting traffic?
  - Are the 32 agents bounded by local-only / sanctioned-input scope, or do they have web-fetch / scrape / capture capabilities?
· **The gating question (now dual):** is Continuous-Claude-v3 a parallel-built apparatus whose architecture we should fork+adapt (function PASS + shape PASS), an inspiration-only candidate (function PASS + shape FAIL — adopting it would pull apparatus past S10's line), or different-architecture-entirely (function FAIL)?
· **Trade-offs:**
  - If fork-and-adapt (both gates PASS): massive head start. Python codebase. MIT. Active development (3.8k stars, recent activity).
  - If inspiration-only (shape FAIL): we still learn from a parallel attempt. The contrasts tell us what we got right, but we don't adopt.
  - If different-architecture (function FAIL): same as inspiration-only.
· **Open verifications:**
  - **GATING:** read repo architecture cover-to-cover, applying both gates. SCDD S2's highest-leverage action.
  - Compare their Continuity System to our anchor/corpus split (function).
  - Compare their Memory System to our snapshot/pointer model (function).
  - Inventory all 30 hooks for capture/scrape shape (shape).
  - Inventory all 32 agents for capture/scrape/shared-corpus shape (shape).
  - License + maintainer-signal confirm.

---

## 5. Comparison matrix

Both gates required. ✓ = passes; ? = unverified; ✗ = fails.

| Candidate | Function (§3.1) | Shape (§3.2) | Branch-tree | Ops complexity | Verdict-readiness |
|---|---|---|---|---|---|
| Supabase + embeddings | ✓ | ✓ | ✓ | LOW (Jake's stack) | READY |
| memvid | ? | ? | ? | UNKNOWN | LOCATE+READ |
| claude-mem (rig only) | ✓ (rig) | ✓ | ✓ | MED | READY w/ compression skip |
| claude-context | ✓ | ? | ? | MED | TREE QUERY + SHAPE VERIFY |
| semble | ✓ | ✓ | ? | LOW | ADAPT TO CONV STREAM |
| codebase-memory-mcp | ✓ | ✓ | ✓✓ | LOWEST (static binary) | ADAPT TO CONV STREAM |
| claude-obsidian / DragonScale | ✓ verify | ✓ verify | ✓ | HIGH | DRAGONSCALE + SHAPE CHECK |
| Continuous-Claude-v3 | ? | ? | ? | ? | DUAL-GATE ARCH READ (GATING) |

---

## 6. Gating action before substrate lock

**Read parcadei/Continuous-Claude-v3 cover-to-cover, applying both gates.** The decision shape changes meaningfully if their continuity system is the apparatus's continuity system AND their architectural shape stays inside the REFUSED wall. SCDD S2 priority #1.

Secondary actions, parallelizable to that read:

· memvid locate + read (Jake or CC has the reference)
· claude-obsidian DragonScale extension verbatim-or-reword verification (function gate)
· claude-obsidian multi-agent shape verification (shape gate)
· Supabase+pgvector seed-shape test (gated on TWW S12 Stage 4 shipping records.ndjson)

---

## 7. Recommended next step (when SCDD S2 reaches it)

After Continuous-Claude-v3 dual-gate read, the candidate field probably collapses to one of these three scenarios:

**Scenario A: Continuous-Claude-v3 PASSES both gates.** Substrate decision becomes "do we fork+adapt or build parallel" instead of "which retrieval lib." That's a different conversation; this face-off doc gets rev'd to focus on adoption-shape-of-fork vs build-fresh.

**Scenario B: Continuous-Claude-v3 PASSES function, FAILS shape** (adoption would pull apparatus past S10's line). Inspiration-only. Read for architectural patterns; don't adopt. Substrate field narrows to: Supabase+pgvector as default (Jake's stack, native ops fit, ready for seed-shape test) + codebase-memory-mcp as the lightweight alternative if the static-binary ops story wins (conv-stream adapter needed). claude-obsidian + DragonScale carried as a third option if its function-check verbatim story checks out.

**Scenario C: Continuous-Claude-v3 FAILS function** (different architecture entirely). Same field-collapse as Scenario B; the contrasts inform our own architecture.

In all scenarios: seed-shape test on whichever candidate(s) emerge from the narrowing is the final commit gate. Append-only ⇒ un-ratified rows are immortal; the seed-shape test is the only honest verdict.

The apparatus thread holds the call at NEXT MOVE #3 (per D7 of the SCDD handoff). This doc surfaces the field and the gates; the decision sits with the track that owns implementation.

---

## 8. What this doc deliberately does not cover

· **The retrieval interface design.** Substrate-specific. After substrate lock.
· **Embedding choice (if Supabase wins).** Own decision tree.
· **Per-project anchor passes** (NEXT MOVE #7). Build on top of substrate.
· **Cross-export uuid stability** (NEXT MOVE #8). Snapshot-id absorbs.
· **Index design over substrate.** Substrate-dependent.

---

## 9. Decision authority (clarified by apparatus S12 cross-track ack, ~19:52 ET 2026-05-27)

Apparatus thread holds the final call on substrate selection / tool cannibalization / scope at NEXT MOVE #3. This doc is *authoritative input*, weighted at decision time against:

· Current anchor invariants (v5 today; v6 when S12 robustness probe lands)
· Current spec (v1 today; v2 when it lands)
· Stage 1–4 seed-shape data (records.ndjson against existing 366MB archive)

Not a power claim — a clarity claim, same logic as "anchor wins when canon and handoff conflict." Per Jake at S12 turn 10.

SCDD's job is to broaden + verify the candidate field, apply both disqualifier gates, surface open verifications, and recommend the gating action. SCDD does NOT lock the substrate.

---

## 10. Pending schema revisions — re-check on v6/v2 land

[Heads-up from apparatus S12 cross-track ack]

S12's pre-Stage-0 robustness probe surfaced three field-level deltas from the v5 anchor / v1 spec inventory:

· **`signature` field on thinking blocks: populated, not stripped.** v5 anchor claimed null in export. Actual: ~60% of thinking blocks carry `signature` values ranging 196–211,384 chars. Distribution reads as cryptographic provenance metadata.
· **`display_content` cluster: ~25K tool blocks not in S11's enumeration.** Block-type count needs revision; storage volume implications for substrate scaling.
· **`attachments[].extracted_content`: inlined file text up to 1.4MB.** New cred vector class (was not in S11's scrub scope). Substrate must handle large-blob fields.

None of the v1 candidate analyses in §4 rest on specific claims about these three fields. But:

· The **storage volume** for any candidate shifts upward when `display_content` (~25K blocks) and `attachments[].extracted_content` (up to 1.4MB per blob) are counted. Re-check scaling characteristics for codebase-memory-mcp's knowledge graph, claude-obsidian's vault file count, and Supabase row counts.
· The **scrub surface** for any candidate shifts when `attachments[].extracted_content` enters the cred-vector class. Substrates that hand off to MCP retrieval can ignore this (scrub happens upstream at spec Stage 2). Substrates that ingest blob content directly need to verify cred-cleanliness propagates.
· The **branch-tree fit** for any candidate is unaffected (these are block-level / message-level fields, not tree-structural).

When v6 anchor + v2 spec land: §2 of this doc gets re-grounded against the new inventory; candidate analyses re-checked for volume + scrub-surface impacts; matrix in §5 updated.

---

## 11. Change log

· **v1 · 2026-05-27 · TWW SCDD S1 · initial drafting.** Eight candidates evaluated against v5 invariants + freeze spec v1 records.ndjson shape. Function disqualifier (AI-compression of corpus) applied. Continuous-Claude-v3 identified as gating read.
· **v1 pre-commit revision · 2026-05-27 ~19:58 ET.** Folded apparatus S12 cross-track ack:
  - §1: strengthened decision-authority framing — SCDD is authoritative input, apparatus holds the call. Added §9 to make this explicit.
  - §3.2: added shape disqualifier (REFUSED-wall violation by adoption-shape) as a second gate. Both gates now required.
  - §4: all eight candidate analyses updated with shape-check verification. §4.8 (Continuous-Claude-v3) gets the deepest shape-check open-verification list because it's the candidate most likely to fail this gate.
  - §5: comparison matrix split into separate function and shape columns.
  - §7: scenarios rewritten to account for shape-gate outcomes.
  - §10: added pending-schema-revisions note — v6 anchor + v2 spec landing after S12's robustness probe; flagged the three known deltas (signature, display_content, attachments.extracted_content) and what may need re-checking when they land.

---

*TWW SCDD S1 close. Grounded against v5 anchor invariants + Freeze_Pipeline_Spec_v1.md §4 records.ndjson shape + SCDD catalog chunks 001 + 002 (200/2,053 keepers judged) + the prior_art_findings doc + the apparatus S12 cross-track ack (decision authority + shape disqualifier + pending schema revisions). Continuous-Claude-v3 dual-gate architecture read is the gating action; the rest of the field narrows meaningfully on its outcome.*
