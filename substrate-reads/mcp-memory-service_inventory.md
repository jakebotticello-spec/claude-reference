# Substrate Inventory — mcp-memory-service
**Pulled from:** doobidoo/mcp-memory-service  
**Inventory date:** 2026-05-27  
**Round:** 3

---

## A. Identity

| Field | Value |
|---|---|
| Repo | doobidoo/mcp-memory-service |
| License | Apache 2.0 |
| Primary language | Python |
| Delivery | MCP server (stdio + HTTP REST, 76 endpoints) |
| Storage backends | SQLite-vec (default), Milvus, Cloudflare, Hybrid |
| Benchmark | LongMemEval R@5 80.4% overall / 86.0% session-level |

---

## B. Storage Model

**SQLite-vec backend schema (primary):**
```sql
-- memories table
content_hash  TEXT PRIMARY KEY
content       TEXT          -- verbatim content written by caller
tags          TEXT
memory_type   TEXT
metadata      JSON
created_at    REAL
updated_at    REAL

-- memory_embeddings (virtual, sqlite-vec)
rowid         FK → memories.rowid
content_embedding  BLOB (float32 array)
```

**Write path (`sqlite_vec.py:store()`):**
1. Exact-hash dedup check (content_hash match → reject)
2. Optional semantic dedup (cosine > 0.85 within 24h → reject)
3. `self._generate_embedding(memory.content)` — embeds the content
4. `INSERT INTO memories ... content = memory.content` ← **verbatim**
5. `INSERT INTO memory_embeddings ... content_embedding = serialize_float32(embedding)`
6. Commit (SAVEPOINT, atomically)

**Background consolidation (`consolidation/compression.py`):**
- `SemanticCompressionEngine.process()` — clusters existing memories, generates thematic summary from representative sentences + concept extraction (NO external LLM call, statistical only)
- Creates NEW `memory_type='pattern'` records from clusters
- `preserve_originals` config controls whether source memories are deleted
- Runs AFTER initial write, NOT on the ingest path

**Harvest pipeline (`harvest/`):**
- Optional background pipeline that monitors session activity
- May generate summaries before storing — this is an OPTIONAL integration path, not the default MCP tool path

---

## C. Function-Gate Verdict

**PRIMARY PATH: EMBEDDED-WITH-VERBATIM**

The direct MCP tool path (`store_memory` tool → `store()`) writes `memory.content` verbatim to SQLite, with embedding stored alongside. No transformation in the storage layer. The calling agent decides what string to pass as `content`.

**Caveats:**
- Background consolidation (`SemanticCompressionEngine`) creates compressed summary records. If `preserve_originals=False`, source memories may be deleted — making the compressed record the only copy.
- Harvest pipeline (optional) may summarize before calling `store()`.
- Semantic dedup can silently drop a memory if it's too similar to a recent one (default threshold 0.85, 24h window).

---

## D. Retrieval API

- **MCP tool:** `retrieve_memory(query, limit)` → vector similarity search
- **MCP tool:** `search_by_tag(tags)` → scalar filter
- **MCP tool:** `get_all_memories()` → full dump
- **Knowledge graph:** typed edges (via `graph.py` backend) — separate from primary memory store
- **REST API:** 76 endpoints including `/api/memories/search`, `/api/memories/{hash}`
- **Hybrid search:** dense vector + BM25 (SQLite FTS5) in Hybrid backend

---

## E. Branch-Tree-or-Forest Fit (anchor v6)

**Anchor v6:** `chat_messages` is tree-OR-FOREST; 9/294 conversations are multi-root forests.

| Criterion | Assessment |
|---|---|
| Parent-child storage | `conversation_id` field on memories — flat FK, not recursive tree |
| Forest support | No native multi-root tree; graph backend has typed edges but not wired for conversation threading |
| Multi-root handling | Not designed for it — memories are flat records with optional conversation_id |
| Verdict | **DOES NOT FIT** anchor v6 forest requirement without significant custom schema work |

The knowledge graph (graph.py backend) has typed edges and could theoretically model conversation threads, but it's not integrated with the primary memory store and requires explicit relationship creation by the agent.

---

## F. Shape-Surface Grep Results

| Pattern | Hits | Disposition |
|---|---|---|
| `chat_conversations` | 0 | CLEAR |
| `claude\.ai` | CLAUDE.md (IDE guidance), README badge + Remote MCP marketing | BENIGN — MCP integration advertising, not DOM/API access |
| `manifest\.json` | 0 | CLEAR |
| `cross.account` / `cross_account` | 0 | CLEAR |
| `sk-[a-zA-Z0-9]{20,}` | 0 live credentials | CLEAR |
| `OPENAI_API_KEY` | README example, discover_harvest_patterns.py | BENIGN — config docs + optional LLM fallback |

**[SHAPE-FLAG]: NONE**

Notable: Remote MCP support means claude.ai browser can connect to this as a memory server. Memory is explicitly "shared across all agents and runs." Multi-user OAuth 2.0 support. These are ARCHITECTURAL features, not SHAPE-FLAG triggers — flagged here for OC awareness.

---

## G. Notes / Caveats

- Very large codebase (~many kLOC). High operational complexity (76 REST endpoints, 5 storage backends, OAuth, harvest pipeline, consolidation, conflict detection).
- Semantic dedup (default ON) silently drops memories above cosine 0.85 within 24h — this could silently discard duplicate conversation turns.
- `conversation_id` bypass: setting `conversation_id` on a memory disables semantic dedup for that memory (CHANGELOG #293) — intended for session logs.
- "Shared across all agents and runs" is explicit design — this is a shared-corpus service, not a per-session isolated store.
- NOT scoped to claude.ai conversation exports — general-purpose AI agent memory service.
