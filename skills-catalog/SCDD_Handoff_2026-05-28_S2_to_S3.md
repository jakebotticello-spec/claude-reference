# Handoff: SCDD S2 → S3

*file: SCDD_Handoff_2026-05-28_S2_to_S3.md · v1 · S2 close · 2026-05-28 09:06 ET*
*repo path: `skills-catalog/` · commit alongside SCDD_Handoff_2026-05-27_S1_to_S2.md (do not delete the S1 doc)*

**Session name:** S2 — Substrate face-off field-build + full COOL-category exhaustive dive
**Proposed next session name:** S3 — NornicDB dual-gate + face-off v2 lock → workflow/apparatus-delta judgment

---

## ONE-LINE STATE

S2 booted against v5/v1, folded apparatus v6 anchor + Freeze_Pipeline_Spec_v2 + S12→S13 handoff mid-session (re-pull protocol fired correctly at turn 5); closed the Continuous-Claude-v3 dual-gate read (function FAIL — compresses corpus via headless-Claude into BGE-embedded archival_memory); expanded + judged the substrate face-off to **6 viable candidates** with **NornicDB surfaced as a NEW lead candidate (not yet dual-gated)**; diagnosed + fixed the cool-bucket suppression bug (chunker v0.2→v0.3, multi-label scoring); and **fully judged the entire COOL category** (459 candidates across 5 chunks) into a **145-row GEM+NOTABLE menu** delivered as `cool_gems_menu.xlsx`. Apparatus is now the **waiting consumer** — records.ndjson seed exists, the only thing between it and ingest is the substrate pick, and the face-off is the gating input (D9). S3 opens on the NornicDB dual-gate → face-off v2 lock → hand to apparatus, then workflow + apparatus-delta judgment.

---

## SYSTEM NARRATIVE

SCDD (Skills Catalog Deep Dive) is the sister TWW track to apparatus-build. Apparatus builds Jake's stateless-Claude memory system off Anthropic's **official conversation export** (the REFUSED wall around live-capture is permanent — see apparatus ANCHOR GRAVEYARD). SCDD's job is to mine a 51,302-repo GitHub crawl (8,287 READMEs, 4 topics) for: (1) **apparatus** — substrate/memory/retrieval candidates feeding apparatus NEXT MOVE #3; (2) **workflow** — tools that reduce friction in Jake's day-to-day; (3) **cool** — intellectually-novel mechanisms + hidden gems. SCDD broadens + verifies + recommends; per **D7**, SCDD does NOT lock the substrate — apparatus does, at NEXT MOVE #3. The face-off doc is authoritative INPUT, not the decision.

Catalog data lives on Jake's box: `C:\claude-reference\skills-catalog\` (NOT in the reference repo — chunk files don't push). The reference repo (`jakebotticello-spec/claude-reference`, pulled via codeload) holds canon: JAKE-RULES, apparatus ANCHOR/spec/handoffs, the Substrate_FaceOff doc, and SCDD handoffs.

**Jake is not a coder.** Claude builds, Jake deploys/tests/strategizes. He's an architect-brained, ADHD/parallel-process operator running Pyris (fractional COO consulting) + CCF Recruiting, with a hardware/maker streak (Bambu P1S, ESP32 home lab, NAS). The cool-dive GEM bar was explicitly calibrated to *Jake-utility*, not just novelty: structure-visualization, file management, templating, friction-removal, and his actual side-projects (Bills podcast, brand work, client analytics) all count as GEM-worthy.

---

## WHAT S2 DID

### 1. Canon refresh (mid-session)
· Booted v5 anchor / v1 spec / S11→S12 handoff.
· Re-pulled at turn 5; **v6 anchor + Freeze_Pipeline_Spec_v2 + S12→S13 handoff had landed.** Folded per mid-session protocol.
· Concrete deltas absorbed: `signature` populated not stripped; `chat_messages` is **tree-OR-FOREST** (9/294 multi-root); `display_content` ~25K blocks, `attachments[].extracted_content` up to 1.4MB; cred-baseline up (RTSP 97→177, Postgres 55→76, OpenAI 6→10, +10 `sk-ant-` incl. one in a thinking block); sampling-floor invariant added.

### 2. Continuous-Claude-v3 dual-gate read — CLOSED
· **Function gate: FAIL.** `recall_learnings.py` spawns headless Claude to compress session JSONL thinking blocks into BGE-embedded `archival_memory.content`. AI-compression-of-corpus → auto-DQ on the pointer-vs-compression invariant.
· **Shape gate: CLEAN-but-irrelevant** (function alone disqualifies). chrome-native-host = Anthropic-sanctioned desktop messaging; Firecrawl = general web, not claude.ai-targeted; no shared-corpus surface; single-user developer shape. No REFUSED-wall pressure.
· **Result: Scenario C field collapse** per face-off §7. v3 does not gate apparatus.

### 3. Substrate face-off — field built + judged (NOT yet locked)
**6 VIABLE:**
| Candidate | Archetype | Function | Shape | Notes |
|---|---|---|---|---|
| Supabase + pgvector | Postgres+vector | PASS | PASS | Default; native to Jake's stack; per-message-native (1 row/record, `parent_message_uuid` column) |
| claude-mem rig | SQLite FTS+Chroma+API | PASS | PASS | Battle-tested; requires compression-skip discipline |
| codebase-memory-mcp | static-binary KG | PASS | PASS | Cleanest ops; conv-stream adapter needed (ingest-unit mismatch) |
| claude-context | vector DB MCP | PASS | ?(likely) | MCP-native; tree-query defer to seed-shape |
| semble | CPU-only code-search adapter | PASS | PASS | Fastest; conv-stream adapter needed |
| mcp-memory-service | sqlite-vec memory MCP | PASS | PASS | EMBEDDED-WITH-VERBATIM; multi-framework |

**DISQUALIFIED (function-fail / compress):** Continuous-Claude-v3, memvid, claude-obsidian, DragonScale, memsearch, headroom.

**NEW LEAD CANDIDATE — NOT YET DUAL-GATED:** **NornicDB** (`orneryd/NornicDB`, 750★) — Graph+Vector+**Temporal MVCC**, Neo4j Bolt + qdrant gRPC compatible, sub-ms HNSW. Maps the records.ndjson shape cleanly: node-per-message, edge=`parent_message_uuid`, `multi_root`=multiple roots, temporal MVCC=`snapshot_id` versioning for free. **Surfaced from the cool dive (chunk 2). This is the concrete payoff of NOT locking the face-off early — it's exactly the "novel architecture hiding below the fold" Jake predicted.** Must dual-gate before lock.

**Three more structural/temporal-graph data points (from cool dive):** memtrace-public (bi-temporal graph, ZERO LLM calls — function-pass-likely, code-domain), arbor (deterministic graph code-intel, no embeddings), open-ontologies (RDF/OWL, versioned, single binary). The temporal/structural-graph category now has **4 function-passing data points** — it's a real category, not a one-off.

**Two shape-fail examples (shared-corpus):** eion, ogham-mcp — clean illustrations of §3.2 single-user-shape violation.

### 4. Chunker v0.2 → v0.3 (multi-label scoring fix)
· **Diagnosis (H2 confirmed):** v0.2 winner-take-all scoring + apparatus keyword/boost asymmetry (4–6pts + FLAG/TOPIC boosts vs cool's 2–3pts no boosts) buried **410 cool rows + 486 workflow rows** in the apparatus pile. The §11 Issue-1 fix (topic boosts fire) cannibalized Issue-2's intent (expand cool). H1 falsified — cool keywords were firing, just never won.
· **Fix (v0.3):** independent per-category scores, overlap allowed, no winner-take-all. `no_category.jsonl` for completeness (nothing discarded).
· **v0.3 distribution:** apparatus 1,982 · workflow 554 · cool 459 · no_category 0 · overlap 806. (cool went 49→459, a 9.4× recovery.)
· Output at `chunks-v0.3/` on Jake's box (apparatus/20 chunks, workflow/6, cool/5). chunks-v0.2/ untouched.

### 5. COOL category — FULLY JUDGED (COMPLETE)
· All 5 cool chunks (459 candidates, 169k★→100★) judged with the Jake-calibrated GEM frame.
· **145 keepers: 39 GEMs + 106 Notables.** FLAG/PASS discarded per Jake's instruction. Leaked-IP repos dropped per Jake's instruction.
· Delivered as **`cool_gems_menu.xlsx`** — 18 use-categories, GEM rows amber-shaded, autofilter + frozen header, live COUNTIFS summary sheet. Zero formula errors.
· **Top categories:** Orchestration & Multi-Agent (24), Structure & Code Viz (15), Knowledge/Context PKM (15), Substrate/Memory (12). **Thesis confirmed:** gems cluster around *seeing structure* + *parallel-agent orchestration* — exactly what the apparatus-only pass was blind to.
· **Standout personal hit:** `mcp-3D-printer-server` (Bambu control via Claude). **Spine of use-this-week gems:** Graphify, oh-my-mermaid, claudemap, collab-public, Claude Octopus, kandev, taskdog, tufte-data-viz, mcp-3D-printer-server.

---

## CROSS-TRACK CORRESPONDENCE LOG

**[apparatus S13 → SCDD S2, mid-session]** Apparatus implemented Stages 1–4 + produced first real baseline snapshot. records.ndjson shape now **LOCKED and REAL** (not hypothetical):
· Per-message: `{snapshot_id, scrub_version, conv_uuid, msg_uuid, parent_message_uuid, sender, created_at, updated_at, text, content_blocks[], attachments[], files[], is_root}`
· Per-conv header: `{record_type:"conversation_header", snapshot_id, conv_uuid, created_at, updated_at, account_uuid, message_count, has_branches, multi_root}`
· 23,095 records (294 headers + 22,801 messages). Pointer = `(snapshot_id, conv_uuid, msg_uuid)`. Interleaved header→messages→header. NO name/summary (ratified out as non-floor).
· Substrate ingests **already-scrubbed** data (273 redactions, verify-clean PASS over 673,871 strings, zero residual). Substrate candidates drop their own cred-handling requirement.
· Apparatus is the **waiting consumer** — Stages 0–4 complete; only the substrate pick stands between it and seed-shape ingest. Per **D9**, apparatus holds the selection call; the face-off is authoritative input.
· **Ask:** flag any candidate whose natural ingest unit is NOT per-message (conv-level / arbitrary-chunk), since records.ndjson is per-message + per-conv-header.

**[SCDD S2 → apparatus, reply — relay to apparatus thread]**
· v3 read is **already CLOSED** (function FAIL) — does not gate apparatus.
· **Ingest-unit answer:** per-message-native clean fit = Supabase+pgvector, claude-mem rig, mcp-memory-service. **Granularity MISMATCH (flagged)** = codebase-memory-mcp, claude-context, semble (code-domain; the "conv-stream adapter" tag IS the ingest-unit mismatch). **NEW: NornicDB** maps the shape cleanly (node-per-message, edge=parent, multi_root=roots, temporal=snapshot) — strongest structural fit, pending dual-gate.
· records.ndjson concrete shape upgrades face-off §3.2 from hypothetical to real validation against the pointer tuple. Cred-scrub-upstream noted; dropped from substrate matrix.

---

## DECISIONS (continuing D-series)

· **D7 (carried):** SCDD does NOT lock the substrate. Apparatus does at NEXT MOVE #3. Face-off = authoritative input.
· **D9 (carried, from apparatus S13):** Apparatus holds the substrate-selection call; SCDD's face-off is the gating input.
· **D10 (new):** Chunker moves to **multi-label scoring** permanently (v0.3). Buckets are non-exclusive; a repo can be apparatus AND cool AND workflow. Winner-take-all is retired — it was structurally biased toward apparatus.
· **D11 (new):** **Nothing is discarded at the chunker level.** Rows clearing no threshold go to `no_category.jsonl`, not the bin. (Jake: "I didn't spend hours pulling this together just to discard 80% of the results.")
· **D12 (new):** Cool-category curation tiers = GEM / NOTABLE / FLAG / PASS. **GEM bar is Jake-utility-calibrated, not novelty-only** — structure-viz, file-mgmt, templating, friction-removal, and Jake's actual projects all qualify. FLAG/PASS are not retained in deliverables; leaked-IP repos are dropped entirely (Jake's standing call).
· **D13 (new):** The substrate face-off will not lock until **NornicDB is dual-gated** — it's the strongest structural fit surfaced and locking without it would repeat the exact early-lock error the exhaustive dive was meant to prevent.

---

## FILE MANIFEST / DEPLOY STATE

**Reference repo (`claude-reference`, codeload pull):**
· `active/JAKE-RULES.md` — universal layer
· `active/apparatus/ANCHOR_apparatus.md` — **v6** (current)
· `active/apparatus/Freeze_Pipeline_Spec_v2.md` — **v2** (current)
· `active/apparatus/Chat_Session_Handoff_2026-05-27_apparatus_S12_to_S13.md`
· `active/apparatus/Substrate_FaceOff_v1.md` — **NEEDS v2** (see priority stack)
· `skills-catalog/SCDD_Handoff_2026-05-27_S1_to_S2.md`
· `skills-catalog/SCDD_Handoff_2026-05-28_S2_to_S3.md` — **THIS FILE (commit it)**

**Jake's box (`C:\claude-reference\skills-catalog\`, local only — does not push):**
· `catalog.jsonl` (51,302 rows source)
· `chunks-v0.1/`, `chunks-v0.2/` (frozen — S1 judgments reference v0.1)
· `chunks-v0.3/` — apparatus/20 chunks · workflow/6 · cool/5 · no_category.jsonl · overlap_report.jsonl (**current judgment input**)
· `substrate-reads/` — inventories: continuous-claude-v3, memvid, claude-obsidian, mcp-memory-service, memsearch, contextplus, grepai (+ ccv3_inventory.md, etc.)

**Outputs delivered to Jake:**
· `cool_gems_menu.xlsx` — 145 GEM+NOTABLE, 18 categories, 2 sheets. (Not committed to repo; it's a Jake deliverable.)

---

## PRIORITY STACK FOR S3

1. **NornicDB dual-gate** (gates everything downstream). Pull `orneryd/NornicDB`, run function gate (does it store verbatim + return pointers, or compress?) and shape gate (capture/scrape/shared-corpus? REFUSED-wall pressure?). Validate ingest-unit against records.ndjson (node-per-message expected clean).
2. **Lock `Substrate_FaceOff_v2.md`** — fold all S2 verdicts (§4.2/4.7/4.8 closes, §4.9 mcp-memory-service, §4.10 archetype-redundant absorbed, NornicDB entry + verdict, §5 matrix, §6 DONE, §7 Scenario C, §10 reconcile v6/v2 + add ingest-unit gate + cred-scrub-upstream, §11 changelog v2, §12 architectural-convergence observation). Then hand to apparatus track (D7/D9).
3. **WORKFLOW category** — 554 candidates (6 chunks), never judged. Same exhaustive tiered treatment as cool; same xlsx menu deliverable.
4. **APPARATUS DELTA** — 1,582 candidates not covered by chunks 001–004, against the v0.3 set. Continue apparatus judgment from where S1+S2 left off.

Recommend 1→2 first (apparatus is the waiting consumer; seed data exists; this unblocks them). 3 and 4 are independent tracks Jake can sequence after.

---

## §12 ARCHITECTURAL CONVERGENCE OBSERVATION (for face-off close)

Three function-fail candidates (ccv3, claude-obsidian, memvid) independently split into **raw-preserved-immutable / derived-queryable-layer** — the same split as apparatus's `raw.json` sealed + `scrub-vN/` overlays. The disagreement is purely *what the derived layer holds*: they compress/embed/reword; apparatus derives verbatim pointers (`records.ndjson`). The pointer-vs-compression invariant is the single principled call that separates apparatus from a convergent design pattern — not a contrarian choice. Carry this into the face-off v2 as §12.

---

## WHAT SCDD S3 OPENS WITH

Per the priority stack: **(1) NornicDB dual-gate → (2) face-off v2 lock → hand to apparatus.** Then Jake's pick of (3) workflow category or (4) apparatus delta. Recommend 1→2 immediately — apparatus is blocked on the substrate pick and the seed data already exists.

---

## DO NOT

· Re-litigate the live-capture refusal (apparatus REFUSED wall is permanent).
· Re-open winner-take-all chunking (D10 — multi-label is permanent).
· Discard any catalog rows (D11).
· Retain FLAG/PASS or leaked-IP in deliverables (D12).
· Lock the face-off before NornicDB is dual-gated (D13).
· Search past sessions/chats for code files — ask Jake to upload (standing JAKE-RULE).
· Confabulate timestamps — `bash date` every status stamp.
· Boot against summaries — read v6 anchor / v2 spec cold.

## QUEUED (tracked, not forgotten)

· workflow category exhaustive judgment (554).
· apparatus-delta judgment (1,582, v0.3 set).
· memtrace-public / arbor / open-ontologies — secondary substrate reads IF NornicDB fails its gates (temporal-graph fallbacks).
· The cool menu's apparatus-tagged cluster cross-references the face-off — keep them linked.

---

*SCDD S2 close. v6 anchor + v2 spec are canon. The cool category is complete and delivered. NornicDB is the open thread that gates the face-off lock. Apparatus is waiting.*
