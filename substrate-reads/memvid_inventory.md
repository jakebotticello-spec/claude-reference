# memvid/claude-brain — Structural Inventory
Generated: 2026-05-27 | Session: TWW SCDD S2 prep round 2

---

## Task 1 Step 0 — Locate: 4 memvid hits in catalog.jsonl

| Stars | Owner/Repo | Description |
|-------|-----------|-------------|
| **498** | **memvid/claude-brain** ← CANONICAL | Give Claude Code photographic memory in ONE portable file. No database, no SQLite, no Chromium… |
| 35 | memvid/maw | Crawl any website into a single searchable file. Query it forever, offline. |
| 9 | angrysky56/emotion_ai | The Aura Emotion AI system has chroma with a local embedding model, memvid qr code mp4 inf… |
| 2 | fa-ina-tic/memvid-rag | local, multimodal rag agent for claude code |

**Canonical selection**: `memvid/claude-brain` (498 stars, same org as "memvid" project owner, directly addresses the Claude Code memory use case).

---

## A. Repo Basics

**License**: MIT — "Copyright (c) 2025 Memvid" (source: `LICENSE`)

**Last commit**: 2026-01-19 — "Auto-install deps when scripts run (v1.0.11)"

**Top-level tree (depth 3)**:
```
memvid/claude-brain/
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── release.yml
├── commands/
│   ├── ask.md
│   ├── recent.md
│   ├── search.md
│   └── stats.md
├── dist/                      # compiled JS (tsup output)
│   ├── hooks/
│   │   ├── hooks.json
│   │   ├── post-tool-use.js (.map)
│   │   ├── session-start.js (.map)
│   │   ├── smart-install.js (.map)
│   │   └── stop.js (.map)
│   ├── scripts/
│   │   ├── ask.js (.map)
│   │   ├── find.js (.map)
│   │   ├── stats.js (.map)
│   │   └── timeline.js (.map)
│   ├── index.d.ts
│   ├── index.js (.map)
│   └── scripts/utils.js (.map)
├── hooks/
│   └── hooks.json
├── skills/
│   ├── memory/SKILL.md
│   └── mind/SKILL.md
├── src/
│   ├── __tests__/
│   │   ├── index.test.ts
│   │   └── mind-lock.test.ts
│   ├── core/
│   │   └── mind.ts             # main engine
│   ├── hooks/
│   │   ├── hooks.json
│   │   ├── post-tool-use.ts    # observation capture hook
│   │   ├── session-start.ts
│   │   ├── smart-install.ts
│   │   └── stop.ts
│   ├── scripts/
│   │   ├── ask.ts
│   │   ├── find.ts
│   │   ├── stats.ts
│   │   ├── timeline.ts
│   │   └── utils.ts
│   ├── utils/
│   │   ├── compression.ts      # ENDLESS MODE compression
│   │   ├── helpers.ts
│   │   └── memvid-lock.ts
│   ├── index.ts
│   └── types.ts
├── .gitignore
├── .install-version
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── package.json               # @memvid/sdk ^2.0.149 dep
├── pnpm-lock.yaml
├── tsconfig.json
└── tsup.config.ts
```

**Total file count**: 66

**Total LOC**: ~390K (inflated by dist/ compiled bundles and pnpm-lock.yaml; src/ TypeScript source is ~1,100 lines)

---

## B. README + Architecture Docs

### README.md (verbatim)

```
<div align="center">

<img src="logo.png" alt="Claude Brain" width="320" />

### Give Claude Code photographic memory.

[![GitHub stars](https://img.shields.io/github/stars/memvid/claude-brain?style=social)](https://github.com/memvid/claude-brain)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br />

https://github.com/user-attachments/assets/b57cb3db-576b-4c1f-af92-95796ba3fb5b

<br />

**[Install in 30 seconds](#installation)** · [How it Works](#how-it-works) · [Commands](#commands) · [Full Demo](https://youtu.be/uRT0CMdK0yg)

</div>

<br />

## The Problem

```
You: "Remember that auth bug we fixed?"
Claude: "I don't have memory of previous conversations."
You: "We spent 3 hours on it yesterday"
Claude: "I'd be happy to help debug from scratch!"
```

**200K context window. Zero memory between sessions.**

You're paying for a goldfish with a PhD.

<br />

## The Fix

```
You: "What did we decide about auth?"
Claude: "We chose JWT over sessions for your microservices.
        The refresh token issue - here's exactly what we fixed..."
```

One file. Claude remembers everything.

<br />

## Installation

```bash
# One-time setup (if you haven't used GitHub plugins before)
git config --global url."https://github.com/".insteadOf "git@github.com:"
```

```bash
# In Claude Code
/plugin add marketplace memvid/claude-brain
```

Then: `/plugins` → Installed → **mind** Enable Plugin → Restart.

Done.

<br />

## How it Works

After install, Claude's memory lives in one file:

```
your-project/
└── .claude/
    └── mind.mv2   # Claude's brain. That's it.
```

No database. No cloud. No API keys.

**What gets captured:**
- Session context, decisions, bugs, solutions
- Auto-injected at session start
- Searchable anytime

**Why one file?**
- `git commit` → version control Claude's brain
- `scp` → transfer anywhere
- Send to teammate → instant onboarding

<br />

## Commands

**In Claude Code:**
```bash
/mind stats                       # memory statistics
/mind search "authentication"     # find past context
/mind ask "why did we choose X?"  # ask your memory
/mind recent                      # what happened lately
```

Or just ask naturally: *"mind stats"*, *"search my memory for auth bugs"*, etc.

<br />

## CLI (Optional)

For power users who want direct access to their memory file:

```bash
npm install -g memvid-cli
```

```bash
memvid stats .claude/mind.mv2           # view memory stats
memvid find .claude/mind.mv2 "auth"     # search memories
memvid ask .claude/mind.mv2 "why JWT?"  # ask questions
memvid timeline .claude/mind.mv2        # view timeline
```

[Full CLI reference →](https://docs.memvid.com/cli/cheat-sheet)

<br />

## FAQ

**How big is the file?**
Empty: ~70KB. Grows ~1KB per memory. A year of use stays under 5MB.

**Is it private?**
100% local. Nothing leaves your machine. Ever.

**How fast?**
Sub-millisecond. Native Rust core. Searches 10K+ memories in <1ms.

**Reset memory?**
`rm .claude/mind.mv2`

---

Built on **[memvid](https://github.com/memvid/memvid)** - the single-file memory engine
```

No separate architecture doc found. README is the only top-level documentation.

---

## C. Storage Layer

**Single-file design**: CONFIRMED. Storage is one file: `.claude/mind.mv2`.

> "No database. No cloud. No API keys." (README)
> "One file. Claude remembers everything." (README)

**Format**: `.mv2` — custom binary format handled by `@memvid/sdk` (version `^2.0.149`). README describes a "Native Rust core." The SDK is a closed-source npm package; the on-disk format is not documented in this repo.

**Write entry point** — `mind.remember()` in `src/core/mind.ts:192-233`:

```typescript
async remember(input: {
  type: ObservationType;
  summary: string;
  content: string;
  tool?: string;
  metadata?: Record<string, unknown>;
}): Promise<string> {
  const observation: Observation = {
    id: generateId(),
    timestamp: Date.now(),
    type: input.type,
    tool: input.tool,
    summary: input.summary,
    content: input.content,
    metadata: {
      ...input.metadata,
      sessionId: this.sessionId,
    },
  };

  const frameId = await this.withLock(async () => {
    return this.memvid.put({
      title: `[${observation.type}] ${observation.summary}`,
      label: observation.type,
      text: observation.content,       // <-- the content field becomes `text` in the frame
      metadata: { ... },
      tags: [observation.type, observation.tool].filter(Boolean) as string[],
    });
  });
  ...
  return frameId;
}
```

**Is content stored VERBATIM or compressed?** → **COMPRESSED** (conditionally).

The `post-tool-use.ts` hook (PostToolUse event) calls `compressToolOutput()` from `src/utils/compression.ts` BEFORE calling `mind.remember()`:

```typescript
// ENDLESS MODE: Compress large outputs to ~500 tokens
const { compressed, wasCompressed, originalSize } = compressToolOutput(
  tool_name,
  tool_input,
  effectiveOutput
);
// ...
const content = compressed.length > MAX_OUTPUT_LENGTH
  ? compressed.slice(0, MAX_OUTPUT_LENGTH) + "\n... (compressed)"
  : compressed;

await mind.remember({
  type: observationType,
  summary,
  content,     // compressed content, not raw tool output
  tool: tool_name,
  metadata,
});
```

Compression thresholds (`src/utils/compression.ts`):
- `COMPRESSION_THRESHOLD = 3000` chars — outputs smaller than this stored as-is
- `TARGET_COMPRESSED_SIZE = 2000` chars — compressed target

Compression strategy per tool type:
- **Read**: extracts imports, exports, function signatures, class names, error patterns + first 10 / last 5 lines
- **Bash**: extracts error lines, success lines, first 10 / last 5 lines
- **Grep**: summarizes file count + match count, shows first 10 matches
- **Glob**: groups by directory, shows top 5 dirs + 15 sample filenames
- **Edit/Write**: records filename + "Changes applied successfully" + first 500 chars

**Conclusion**: Content is NOT stored verbatim for large outputs. The ENDLESS MODE compression intentionally discards the bulk of tool outputs, preserving only structural extracts.

---

## D. Retrieval Layer

**Search** — `mind.search()` in `src/core/mind.ts:238-259`:
```typescript
async search(query: string, limit = 10): Promise<MemorySearchResult[]> {
  const results = await this.memvid.find(query, { k: limit, mode: "lex" });
  return (results.frames || []).map((frame: any) => ({
    observation: {
      id: frame.metadata?.observationId || frame.frame_id,
      timestamp: frame.metadata?.timestamp || 0,
      type: frame.label as ObservationType,
      tool: frame.metadata?.tool,
      summary: frame.title?.replace(/^\[.*?\]\s*/, "") || "",
      content: frame.text || "",        // the stored (possibly compressed) text
      metadata: frame.metadata,
    },
    score: frame.score || 0,
    snippet: frame.snippet || frame.text?.slice(0, 200) || "",
  }));
}
```

Returns: pointers + stored text (the compressed content written by `remember()`). Not re-expanded to original.

**Ask** — `mind.ask()`:
```typescript
const result = await this.memvid.ask(question, { k: 5, mode: "lex" });
return result.answer || "No relevant memories found.";
```

Mode: lexical (`mode: "lex"`) — no vector/semantic search in the current SDK calls.

**Index location**: in-file, inside the `.mv2` binary (no external index files observed).

---

## E. Scaling

From README FAQ:
- Empty file: ~70KB
- Growth: ~1KB per memory
- "A year of use stays under 5MB"
- "Searches 10K+ memories in <1ms" (lexical, Rust core)

No benchmarks for query latency at specific record counts beyond "10K+ in <1ms."

**Branch/tree support**: None. Flat-record only. No parent/child API visible in the TypeScript source. Every memory is an independent frame.

---

## F. Shape-Surface Grep

Run against full extracted tree at `substrate-reads\memvid\`:

| Pattern | Hits | Status |
|---------|------|--------|
| `chat_conversations` | 0 | expected good ✓ |
| `claude\.ai` | 0 | expected good ✓ |
| `browser extension\|webextension\|content script` (case-insensitive) | 0 | expected good ✓ |
| `intercept\|mitm\|proxy` (case-insensitive, excl. node_modules) | 0 | expected good ✓ |
| `scrape\|scraping` (case-insensitive) | 0 | expected good ✓ |
| `multi.user\|shared.corpus\|cross.account` (case-insensitive) | 0 | expected good ✓ |

All zero hits per category. No [SHAPE-FLAG] items.
