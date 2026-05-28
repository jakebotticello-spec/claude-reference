# Substrate Inventory — contextplus
**Pulled from:** forloopcodes/contextplus  
**Inventory date:** 2026-05-27  
**Round:** 3

---

## A. Identity

| Field | Value |
|---|---|
| Repo | forloopcodes/contextplus |
| License | MIT |
| Primary language | TypeScript |
| Delivery | MCP server (npx/bunx, stdio) |
| Storage | In-memory property graph + JSON persistence (`.mcp_data/memory-graph.json`) |
| Domain | CODE INTELLIGENCE — not conversation memory |

---

## B. Storage Model

**In-memory property graph with JSON persistence (`src/core/memory-graph.ts`):**

```typescript
interface MemoryNode {
  id: string               // "mn-{timestamp}-{random}"
  type: NodeType           // "concept" | "file" | "symbol" | "note"
  label: string            // human-readable name
  content: string          // verbatim content stored here
  embedding: number[]      // embedding vector stored alongside
  createdAt: number
  lastAccessed: number
  accessCount: number
  metadata: Record<string, string>
}

interface MemoryEdge {
  id: string
  source: string           // node ID
  target: string           // node ID
  relation: RelationType   // relates_to | depends_on | implements | references | similar_to | contains
  weight: number
  createdAt: number
  metadata: Record<string, string>
}
```

**Write path (`upsertNode()`):**
1. Check for existing node with same label+type
2. If exists: update content, lastAccessed, accessCount, metadata; re-embed
3. If new: create MemoryNode with verbatim `content` + embedding from `fetchEmbedding(label + content)`
4. `graph.nodes[node.id] = node` (in-memory)
5. `scheduleSave(rootDir)` → debounced 500ms write to `.mcp_data/memory-graph.json`

**Edge creation:**
- Explicit: `createRelation(rootDir, sourceId, targetId, relation, weight)`
- Auto-similarity: any two nodes with cosine ≥ 0.72 get a `similar_to` edge automatically (via `addInterlinkedContext`)
- Edge decay: `weight * exp(-DECAY_LAMBDA * daysSinceCreation)` where DECAY_LAMBDA = 0.05

**Persistence:** single JSON file at `{rootDir}/.mcp_data/memory-graph.json` with `nodes` and `edges` dictionaries.

---

## C. Function-Gate Verdict

**EMBEDDED-WITH-VERBATIM**

`upsertNode()` stores the `content` parameter verbatim in the node's `content` field. The embedding is generated from `label + content` and stored alongside in the same node object. Both verbatim content and embedding are persisted to the JSON file.

No transformation, summarization, or compression occurs in the write path. The calling agent provides the content string; contextplus stores it as-is.

**Domain caveat:** contextplus is a CODE INTELLIGENCE tool, not a conversation memory tool. Its node types (`concept`, `file`, `symbol`, `note`) and primary tools (`get_context_tree`, `semantic_code_search`, `get_blast_radius`) are designed for navigating codebases, not storing conversation content.

---

## D. Retrieval API

- **`search_memory_graph(query, maxDepth, topK, edgeFilter)`** — embedding similarity search + graph traversal to 1st/2nd-degree neighbors
- **`retrieve_with_traversal(startNodeId, maxDepth, edgeFilter)`** — walk outward from a known node, scored by decay and depth
- **`upsert_memory_node`** — create/update node
- **`create_relation`** — create typed edge
- **`prune_stale_links`** — remove edges below decay threshold, orphan nodes
- **`add_interlinked_context`** — bulk-add nodes with auto-similarity linking
- Retrieval is MCP-native (tools exposed to AI agents directly)

---

## E. Branch-Tree-or-Forest Fit (anchor v6)

**Anchor v6:** `chat_messages` is tree-OR-FOREST; 9/294 conversations are multi-root forests.

| Criterion | Assessment |
|---|---|
| Parent-child storage | `contains` edge type could model parent-child |
| Forest support | Graph edges are bidirectional; multiple roots possible |
| Multi-root handling | Graph has no concept of "roots" — any node can relate to any node |
| Node type for conversations | None — types are concept/file/symbol/note |
| Verdict | **DOES NOT FIT** — graph structure exists but is not designed for conversation threading; no conversation-native schema |

The property graph could theoretically be adapted, but this would require custom node types and application logic not present in contextplus. The domain mismatch (code intelligence vs. conversation memory) makes this a poor fit without significant re-engineering.

---

## F. Shape-Surface Grep Results

| Pattern | Hits | Disposition |
|---|---|---|
| `chat_conversations` | 0 | CLEAR |
| `claude\.ai` | 0 | CLEAR |
| `manifest\.json` | 0 | CLEAR |
| `cross.account` / `cross_account` | 0 | CLEAR |
| `sk-[a-zA-Z0-9]{20,}` | 0 live credentials | CLEAR |
| `OPENAI_API_KEY` | README (config examples), embeddings.ts (env var read) | BENIGN — provider config |

**[SHAPE-FLAG]: NONE**

---

## G. Notes / Caveats

- WRONG DOMAIN for this use case. contextplus is designed for code navigation, not conversation storage. Its tools (AST parsing, blast radius, file skeleton) have no equivalent for chat data.
- Graph decay: edges lose weight over time. Long-dormant relationships auto-prune via `prune_stale_links`. For static conversation archives this would require disabling decay entirely.
- Auto-similarity linking (cosine ≥ 0.72) could create many spurious edges across conversation messages that happen to be semantically similar — noise rather than signal for a conversation corpus.
- JSON persistence scales poorly: the entire graph is loaded into memory and re-written atomically on every change.
- Embedding provider: Ollama (local, nomic-embed-text default) or OpenAI-compatible API.
