# Substrate Inventory — grepai
**Pulled from:** yoanbernabeu/grepai  
**Inventory date:** 2026-05-27  
**Round:** 3

---

## A. Identity

| Field | Value |
|---|---|
| Repo | yoanbernabeu/grepai |
| License | MIT |
| Primary language | Go |
| Delivery | CLI tool + MCP server |
| Storage backends | gob (file-based, default), PostgreSQL+pgvector, Qdrant |
| Domain | SEMANTIC CODE SEARCH — not conversation memory |
| Tagline | "grep for the AI era" |

---

## B. Storage Model

**Core types (`store/store.go`):**

```go
type Chunk struct {
    ID          string    // unique chunk identifier
    FilePath    string    // source file path
    StartLine   int       // line range start
    EndLine     int       // line range end
    Content     string    // verbatim code content
    Vector      []float32 // embedding vector stored alongside
    Hash        string    // hash of file
    ContentHash string    // SHA256 of raw content (path-independent)
    UpdatedAt   time.Time
}

type Document struct {
    Path     string    // file path
    Hash     string    // content hash
    ModTime  time.Time
    ChunkIDs []string  // chunk IDs for this file
}

type VectorStore interface {
    SaveChunks(ctx, chunks []Chunk) error
    DeleteByFile(ctx, filePath string) error
    Search(ctx, queryVector []float32, limit int, opts SearchOptions) ([]SearchResult, error)
    GetDocument(ctx, filePath string) (*Document, error)
    SaveDocument(ctx, doc Document) error
    ListDocuments(ctx) ([]string, error)
    Load(ctx) error
    Persist(ctx) error
    // ...stats, listing, chunk retrieval
}
```

**Write path (`grepai watch` / `grepai init`):**
1. File watcher detects changed source files
2. Chunker splits file into code chunks (line ranges)
3. Embedder calls configured provider (Ollama nomic-embed-text, LM Studio, or OpenAI) to get vector
4. `SaveChunks(ctx, chunks)` → stores Chunk with verbatim `Content` + `Vector`
5. `SaveDocument()` → stores Document metadata
6. `Persist()` → writes gob file to disk

**Content-addressed embedding cache:**
- `EmbeddingCache` interface: `LookupByContentHash(contentHash) ([]float32, bool, error)`
- If a chunk's content hash is already cached, reuses the existing embedding — avoids redundant API calls across git worktrees

---

## C. Function-Gate Verdict

**EMBEDDED-WITH-VERBATIM**

`SaveChunks()` stores each chunk with verbatim `Content` (the raw code text for that line range) alongside `Vector` (the embedding). No transformation, summarization, or extraction occurs in the write path.

The `ContentHash` field (SHA256 of raw content, path-independent) confirms content identity is preserved. The embedding cache lookup uses this hash — if the verbatim content is the same, the same embedding is reused; this is content-addressed deduplication, not content transformation.

**Domain caveat:** grepai chunks and embeds SOURCE CODE FILES, not conversation content. The chunking strategy (line ranges within files) is designed for code, not chat messages.

---

## D. Retrieval API

- **`grepai search "error handling"`** — semantic query → embedding → vector similarity → returns top-k chunks with content + score
- **`grepai trace callers "Login"`** — call-graph tracing (finds who calls a function)
- **MCP server mode** — exposes search as MCP tool for AI agents (Claude Code, Cursor, Windsurf)
- **`SearchOptions.PathPrefix`** — filter results by file path prefix
- Returns: Chunk content, file path, line range, similarity score

---

## E. Branch-Tree-or-Forest Fit (anchor v6)

**Anchor v6:** `chat_messages` is tree-OR-FOREST; 9/294 conversations are multi-root forests.

| Criterion | Assessment |
|---|---|
| Parent-child storage | None — flat chunk list with file/line positions |
| Forest support | None — Document contains a flat list of ChunkIDs |
| Multi-root handling | Not modeled |
| Verdict | **DOES NOT FIT** — no relational structure beyond file→chunk ownership |

grepai's data model is strictly hierarchical at file→chunk level with no support for cross-chunk relationships, let alone conversation threading or multi-root forests.

---

## F. Shape-Surface Grep Results

| Pattern | Hits | Disposition |
|---|---|---|
| `chat_conversations` | 0 | CLEAR |
| `claude\.ai` | CLAUDE.md (IDE guidance), work-issue.md (Claude Code link) | BENIGN |
| `manifest\.json` | 0 | CLEAR |
| `cross.account` / `cross_account` | 0 | CLEAR |
| `sk-[a-zA-Z0-9]{20,}` | 0 live credentials | CLEAR |
| `OPENAI_API_KEY` | init.go (error message: "set OPENAI_API_KEY"), configuration.md (example) | BENIGN — config docs |

**[SHAPE-FLAG]: NONE**

---

## G. Notes / Caveats

- WRONG DOMAIN for this use case. grepai indexes source code files. Applying it to conversation exports would require treating each message as a "file" — a severe impedance mismatch.
- File watcher (`grepai watch`) is designed to keep a live codebase index fresh — not applicable to a static corpus of exported conversations.
- The `trace callers` feature (call-graph tracing) has no analogue for conversation data.
- Embedding providers: Ollama (local), LM Studio (local), OpenAI (API) — same options as grepai's code search use case.
- MCP integration (`grepai search` as MCP tool) is the stated value prop for AI agents — "drastically reduces AI agent input tokens by providing relevant context."
- LOC estimate: ~2,000 Go LOC in src/ — small, clean codebase.
