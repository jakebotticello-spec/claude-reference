# Substrate Inventory — memsearch
**Pulled from:** zilliztech/memsearch  
**Inventory date:** 2026-05-27  
**Round:** 3

---

## A. Identity

| Field | Value |
|---|---|
| Repo | zilliztech/memsearch |
| License | MIT |
| Primary language | Python |
| Delivery | CLI tool + MCP-compatible indexer |
| Storage backends | Markdown files (source of truth) + Milvus (shadow index) |
| Org | Zilliz (makers of Milvus) |

---

## B. Storage Model

**Two-layer architecture:**
1. **Source of truth:** `memory/YYYY-MM-DD.md` — daily Markdown files, append-only
2. **Shadow index:** Milvus collection — rebuildable from .md files at any time

**Milvus schema (`src/memsearch/store.py:MilvusStore._ensure_collection()`):**
```
chunk_hash       VARCHAR(64)   PRIMARY KEY (SHA256 of chunk content)
embedding        FLOAT_VECTOR  (dense, cosine)
content          VARCHAR(65535) -- verbatim text of the chunk from .md file
sparse_vector    SPARSE_FLOAT_VECTOR  -- BM25 auto-generated from content field
source           VARCHAR(1024) -- .md file path
heading          VARCHAR(1024)
heading_level    INT64
start_line       INT64
end_line         INT64
```

**Ingest pipeline (capture plugin):**
```
Parse last conversation turn
  → LLM (Anthropic haiku or configured provider) summarizes the turn
  → Append LLM-generated summary to memory/YYYY-MM-DD.md
  → memsearch index: chunk .md file → embed → upsert to Milvus
```

**`memsearch compact` command:**
- Separate, optional operation
- Runs LLM over existing chunks to produce further-compressed summaries
- Replaces chunk content in Milvus (dedup via chunk_hash)

**Search:** Hybrid — dense ANN (cosine) + BM25 sparse vector + RRF reranking

---

## C. Function-Gate Verdict

**COMPRESSED**

The LLM summarization step happens BEFORE the .md file write. What gets stored in the source of truth is the LLM-generated summary, NOT verbatim conversation content. The Milvus shadow index then stores chunks of those summaries.

Evidence:
- README capture flow diagram: `Parse last turn → LLM summarizes (haiku) → Append to memory/YYYY-MM-DD.md`
- `compact.py` uses `ANTHROPIC_API_KEY` — confirms LLM call in pipeline
- architecture.md and getting-started.md both document the LLM summarization step
- `memsearch compact` adds a second LLM compression pass on already-stored summaries

The Milvus `content` field stores verbatim text of .md chunks — but those chunks are themselves LLM summaries, not the original conversation turns.

---

## D. Retrieval API

- **CLI:** `memsearch search "query"` → hybrid dense+BM25 search against Milvus
- **MCP:** MCP server mode exposes search tool to agents
- **Source files:** .md files are human-readable and directly inspectable
- **Rebuild:** `memsearch index` reconstructs Milvus from .md files at any time
- **Filter:** source file path filter supported (per `SearchOptions.PathPrefix` analogue)

---

## E. Branch-Tree-or-Forest Fit (anchor v6)

**Anchor v6:** `chat_messages` is tree-OR-FOREST; 9/294 conversations are multi-root forests.

| Criterion | Assessment |
|---|---|
| Parent-child storage | None — linear date-based .md files |
| Forest support | None — flat append-only chronological log |
| Multi-root handling | Not modeled — single timeline stream |
| Verdict | **DOES NOT FIT** anchor v6 forest requirement |

The source of truth model is a daily .md file — completely flat. No conversation threading, no parent-child, no forest structure possible without custom schema extensions.

---

## F. Shape-Surface Grep Results

| Pattern | Hits | Disposition |
|---|---|---|
| `chat_conversations` | 0 | CLEAR |
| `claude\.ai` | CLAUDE.md (IDE guidance text only) | BENIGN |
| `manifest\.json` | 0 | CLEAR |
| `cross.account` / `cross_account` | 0 | CLEAR |
| `sk-[a-zA-Z0-9]{20,}` | 0 live credentials | CLEAR |
| `ANTHROPIC_API_KEY` | architecture.md, cli.md, getting-started.md, compact.py | BENIGN — documented config, not hardcoded |
| `OPENAI_API_KEY` | README, architecture.md (config examples) | BENIGN — provider config docs |

**[SHAPE-FLAG]: NONE**

---

## G. Notes / Caveats

- `memsearch compact` requires an LLM API key (Anthropic or OpenAI) — the COMPRESSED verdict applies even more strongly with compact enabled.
- Windows not supported for local Milvus Lite (milvus-lite has no Windows wheels); requires remote Milvus server on Windows.
- Milvus is explicitly described as "rebuildable shadow index" — the .md files are authoritative.
- `memsearch reset --yes` drops the Milvus collection entirely; re-index from .md files to restore.
- Embedding dimension mismatch guard: changing embedding providers requires reset + re-index.
- NOT designed for raw conversation storage — it is a "memory" layer that ingests curated summaries.
