# CCv3 Structural Inventory
## parcadei/Continuous-Claude-v3
Generated: 2026-05-27 (SCDD S2 prep)

---

## A — Repo Basics

| Field | Value |
|-------|-------|
| License | MIT |
| Last commit | 2026-01-26 `fix(update): sync Python hooks in addition to TypeScript` |
| SHA | d07ff4b06b62f43771bc0c927d0211b734d6149e |
| Branch | main (one branch, one remote) |
| Clone depth | 1 (shallow) |
| Total files (excl .git) | 943 |
| Total LOC (excl .git) | ~169,843 |

**Directory tree (depth 3):**
```
continuous-claude-v3/
├── .claude/
│   ├── agents/          34 files (32 .md + .json pairs, some .json only)
│   ├── backup/          archived hooks (braintrust-correlation-attempt)
│   ├── braintrust-extractor.lock
│   ├── chrome/          chrome-native-host (Claude desktop app native bridge)
│   ├── hooks/           src/ (TypeScript) + dist/ (compiled JS) + .sh + .py
│   ├── rules/           12 policy .md files
│   ├── scripts/         Python utility scripts (recall, status, tldr_stats)
│   ├── servers/         MCP server implementations (8 servers)
│   ├── skills/          109 SKILL.md files organized by capability
│   ├── transcripts/     1 session .jsonl transcript (ses_4529dec3fffe4...)
│   └── settings.json    (not in repo — user-generated on install)
├── .claude/backup/      archived old hook config
├── docker/
│   └── init-schema.sql  PostgreSQL 4-table schema
├── docs/
│   ├── ARCHITECTURE.md
│   ├── TLDR.md
│   ├── hooks/README.md
│   └── skills/README.md
├── opc/
│   ├── packages/tldr-code/   5-layer code analysis tool
│   └── scripts/
│       ├── agentica/          Claude proxy + Agentica SDK integration
│       ├── braintrust/        session analysis
│       ├── cc_math/           SymPy, Z3, SciPy, Pint runners
│       ├── core/              recall_learnings, store_learning, memory_daemon
│       └── setup/             wizard (12-step install), update script
└── README.md
```

---

## B — README + Architecture Docs

**Core premise:** Transforms Claude Code into a continuously-learning system. Three layers:
- **Skills (109):** modular capabilities triggered by natural language via skill-activation hook
- **Agents (32):** specialized sub-sessions spawned via Task tool
- **Hooks (30):** intercept lifecycle events (SessionStart, PreToolUse, PostToolUse, UserPromptSubmit, SubagentStop, SessionEnd)

**Architecture motto:** "Compound, don't compact." Extract learnings automatically, start fresh with full context.

**Data layers:**
1. TLDR 5-layer code analysis (AST → CallGraph → CFG → DFG → PDG), ~95% token savings
2. PostgreSQL + pgvector + FAISS semantic index
3. Filesystem handoffs (YAML) + continuity ledgers (Markdown)

**Installation:** Python wizard (`uv run python -m scripts.setup.wizard`) deploys 32 agents, 109 skills, 30 hooks, starts Docker PostgreSQL container.

---

## C — Memory System

### Storage Layer

**Backend:** PostgreSQL with pgvector extension (Docker container, local)
**Fallback:** SQLite at `~/.claude/cache/memory.db`

**Table:** `archival_memory`
```sql
id          UUID PRIMARY KEY
session_id  TEXT NOT NULL
agent_id    TEXT
content     TEXT NOT NULL            -- synthesized learning text
metadata    JSONB DEFAULT '{}'
embedding   vector(1024)             -- BGE-large-en-v1.5 embeddings
created_at  TIMESTAMPTZ DEFAULT NOW()
```
Indexes: session_id, (session_id, agent_id), created_at DESC, FTS gin index on content.

### Ingest Path

```
Session active → heartbeat updates sessions.last_heartbeat
Session ends   → heartbeat goes stale (>5 min)
               → memory_daemon.py wakes (background process, PID file at ~/.claude/memory-daemon.pid)
               → daemon spawns headless Claude (claude -p, Sonnet)
               → Claude reads session JSONL transcript thinking blocks
               → extracts learnings to archival_memory with BGE embeddings
               → next session sees matches via memory-awareness hook
```

Explicit ingest also available via `store_learning.py --type WORKING_SOLUTION|ARCHITECTURAL_DECISION|... --content "..." --confidence high|medium|low`

### Retrieval API

```bash
# Default: hybrid RRF (text BM25 + vector cosine combined)
cd opc && uv run python scripts/core/recall_learnings.py --query "authentication patterns" [--k N]

# Text-only (fast, no embeddings)
... --text-only

# Vector-only (higher similarity scores)
... --vector-only
```

**Return format:** Raw content text of matched learnings (NOT pointers to external files or corpus).

**[DUAL-GATE NOTE — FUNCTION CHECK]:** Memory returns synthesized learning content, not pointers to source documents. The daemon uses headless Claude to analyze and compress session transcripts into learning entries. This is an AI-compression-of-corpus pattern, not a pointer-returning retrieval substrate.

---

## D — Continuity System

### Handoff Format

**Storage:** Filesystem. Location: `thoughts/shared/handoffs/<session-name>/<YYYY-MM-DD_HH-MM>-<slug>.yaml`

**YAML schema:**
```yaml
---
date: 2026-01-08T15:26:01+0000
session_name: feature-x
status: complete
---

# Handoff: Feature X Implementation

## Task(s)
| Task | Status |
|------|--------|
| Design API | Completed |

## Next Steps
1. Add retry logic
```

**Also stored in PostgreSQL** `handoffs` table with vector(1024) embedding for semantic recall across sessions.

**Continuity Ledger (within-session):** `thoughts/ledgers/CONTINUITY_<topic>.md` — Markdown checklist tracking session goal, completed, in-progress, blockers. Deprecated in favor of YAML handoffs.

**Hook integration:** `pre_compact_continuity.py` auto-saves on context compaction. `session_start_continuity.py` loads most recent handoff and injects full content (~400 tokens) at session resume/clear/compact.

---

## E — Hooks Inventory

**Stated count:** 30. **Files found:** 30 `.sh` + 9 `.py` + 6 `.ts` source files (TypeScript compiled to dist/). Some overlap (sh wrapper + compiled ts). README count of 30 refers to the logical hook count.

### Shell hooks (30 files):
| Hook | Event | Purpose |
|------|-------|---------|
| session-start-continuity.sh | SessionStart | Loads YAML handoff, starts TLDR+memory daemons |
| session-register.sh | SessionStart | Registers session in PostgreSQL, cross-terminal awareness |
| session-start-tldr-cache.sh | SessionStart | Warms TLDR code analysis cache |
| session-start-dead-code.sh | SessionStart | Dead code detection on session start |
| session-symbol-index.sh | SessionStart | Builds symbol index |
| arch-context-inject.sh | SessionStart/PreToolUse | Injects architecture context |
| tldr-read-enforcer.sh | PreToolUse (Read) | Returns L1+L2+L3 analysis instead of raw file |
| smart-search-router.sh | PreToolUse (Grep) | Routes grep to TLDR semantic search or ast-grep |
| tldr-context-inject.sh | PreToolUse | Adds code analysis context to agent prompts |
| file-claims.sh | PreToolUse (Edit/Write) | Cross-terminal file locking |
| pre-tool-use-broadcast.sh | PreToolUse | Broadcast to peer sessions |
| path-rules.sh | PreToolUse | Path sandbox enforcement |
| import-validator.sh | PreToolUse | Import validation before edits |
| signature-helper.sh | PreToolUse | Function signature lookup |
| post-edit-diagnostics.sh | PostToolUse (Edit) | Runs pyright + ruff after file edits |
| post-edit-notify.sh | PostToolUse | Notifies peer sessions of edits |
| handoff-index.sh | PostToolUse | Indexes new handoff files to PostgreSQL |
| impact-refactor.sh | PostToolUse | Runs impact analysis after refactors |
| import-error-detector.sh | PostToolUse | Detects import errors post-edit |
| edit-context-inject.sh | PostToolUse | Injects diff context |
| typescript-preflight.sh | PostToolUse | TypeScript type checking |
| compiler-in-the-loop.sh | PostToolUse | Compiler feedback during implementation |
| compiler-in-the-loop-stop.sh | Stop | Compiler check on Stop |
| skill-activation-prompt.sh | UserPromptSubmit | Injects skill suggestions based on user intent |
| memory-awareness.sh | UserPromptSubmit | Surfaces relevant past learnings |
| persist-project-dir.sh | UserPromptSubmit | Ensures CLAUDE_PROJECT_DIR is set |
| pre-compact-continuity.sh | PreCompact | Auto-saves handoff before compaction |
| session-end-cleanup.sh | SessionEnd | Cleanup: kills orphaned processes, stale locks |
| session-outcome.sh | SessionEnd | Records session outcome metrics |
| auto-handoff-stop.py | Stop | Auto-creates handoff on Stop event |

### Python hooks (additional):
- `braintrust_hooks.py` — Braintrust LLM tracing (session_start, session_end, user_prompt_submit, post_tool_use, stop spans via `https://api.braintrust.dev`). Optional, requires BRAINTRUST_API_KEY.
- `session_start_continuity.py` — Python port of session-start-continuity.sh with TLDR daemon + memory daemon management
- `premortem-suggest.py` — Suggests premortem risk analysis before large operations
- `hook_launcher.py` — Infrastructure: executes hooks from project root for correct path resolution

**[SHAPE-FLAG CHECK — HOOKS]:** No claude.ai DOM/network surface found. No browser extension. No content script. `chrome-native-host` is the Claude desktop app native messaging bridge (wraps `claude --chrome-native-host`); it is the target side of native messaging, not a browser extension injecting into claude.ai. All hooks operate on: local filesystem, local TLDR daemon, local PostgreSQL, external APIs (Braintrust, pyright/ruff).

---

## F — Agents Inventory

**Stated count:** 32. **Files found:** 34 distinct names (some .json-only, some .md-only, most paired).

| Agent | Role | Key Tools |
|-------|------|-----------|
| aegis | Security review | Read, Bash |
| agentica-agent | Build Python agents with Agentica SDK | Read, Bash, Write |
| arbiter | Test validation | Read, Bash, Write |
| architect | Feature planning + API integration | Read, Bash, Write, WebSearch |
| atlas | Validation (plans, contracts) | Read, Bash |
| braintrust-analyst | Session analysis via Braintrust replay | Bash |
| chronicler | Changelog + documentation writer | Read, Write |
| context-query-agent | Context/memory queries | Read, Bash |
| critic | Code review with critique | Read |
| debug-agent | Issue investigation via logs/search | Read, Bash, Grep |
| herald | Announcements, status reports | Read, Write |
| judge | Final review arbitration | Read |
| kraken | TDD implementation (checkpoint/resume) | Read, Write, Edit, Bash |
| liaison | Communication between agents/teams | Read, Write |
| maestro | Multi-agent orchestration (Pipeline/Swarm/Jury) | Task |
| memory-extractor | Extracts learnings from session transcripts | Read, Bash |
| onboard | Analyzes existing codebase, creates ledger | Read, Bash, Write |
| oracle | External research (web, docs, APIs) | Read, Bash, WebSearch |
| pathfinder | External repository analysis | Read, Bash, WebSearch |
| phoenix | Refactoring + migration planning | Read, Bash |
| plan-agent | Lightweight planning with research | Read, Bash, WebSearch |
| plan-reviewer | Validates plans against best practices | Read |
| profiler | Performance profiling + race conditions | Read, Bash |
| research-codebase | Documents codebase as-is | Read, Glob, Grep |
| review-agent | Code review | Read |
| scout | Codebase exploration (TLDR-aware) | Read, Bash, Glob, Grep |
| scribe | Documentation writer | Read, Write |
| sentinel | Security/safety guard | Read |
| session-analyst | Analyzes past session transcripts | Read, Bash |
| sleuth | Bug investigation, root cause | Read, Bash, Grep |
| spark | Lightweight fixes and quick tweaks | Read, Write, Edit, Bash |
| surveyor | Architecture survey | Read, Glob |
| validate-agent | Validates implementations | Read, Bash |
| warden | Refactoring/migration plan review (no tools) | — |

**[SHAPE-FLAG CHECK — AGENTS]:** No claude.ai DOM/network access. Oracle uses `WebSearch` (standard Claude Code tool) for general web research. Firecrawl agents use Firecrawl API (scrapes arbitrary web content, not claude.ai). No browser automation. No multi-account or shared-corpus patterns. Cross-terminal coordination is single-user multi-terminal via PostgreSQL sessions table.

---

## G — Shape-Surface Grep Results

| Pattern | Files | Assessment |
|---------|-------|------------|
| `chat_conversations` | 0 | Clear |
| `claude\.ai` (DOM/network) | 125 files | All are documentation references, badge URLs, tool descriptions. Zero DOM access, zero network intercept. |
| browser extension manifest.json | 0 | Clear |
| `intercept\|mitm\|proxy` | `chrome-native-host` only | Claude desktop app native messaging bridge — NOT interception. Wraps `claude --chrome-native-host`. |
| `scrape` | firecrawl_scrape.py, firecrawl_scrape/SKILL.md | External Firecrawl API for general web scraping. No claude.ai targeting. |
| `multi.user\|shared.corpus` | 0 | Cross-terminal coordination is single-user only. |

**No SHAPE-FLAG raised.** All hits are benign (documentation, external APIs, Claude desktop app bridge).

---

## H — MCP Execution Mechanism

CCv3 ships 8 custom MCP server implementations under `.claude/servers/`:

| Server | Purpose | External Dependency |
|--------|---------|-------------------|
| `ast-grep` | AST-based structural code search and refactoring | `ast-grep` CLI |
| `fetch` | HTTP fetch (web content retrieval) | httpx |
| `firecrawl` | Web crawling + scraping (crawl, map, extract, search) | Firecrawl API (requires API key) |
| `git` | Git operations (add, commit, diff, log, status, etc.) | git CLI |
| `morph` | WarpGrep fast codebase search + LLM-powered edits | Morph API |
| `nia` | Library documentation search + code grep | NIA API (requires API key) |
| `perplexity` | AI-powered web search (ask, reason, research) | Perplexity API (requires API key) |
| `qlty` | Code quality (70+ linters, fmt, smells, metrics) | qlty CLI |
| `repoprompt` | Token-efficient codebase context builder | RepoPrompt (local) |

**Execution mechanism:** Each server is a Python module. Tools are invoked via `call_mcp_tool("<server>__<tool>", params)` from agent code. Registered in Claude Code's MCP config (populated by wizard). All run as local subprocesses — no remote execution, no browser-side access.

External API calls: Firecrawl, Morph, NIA, Perplexity, Braintrust — all are standard HTTPS API integrations, all optional (wizard configures API keys). None access claude.ai.

---

## Summary for Dual-Gate Evaluation

**Function gate (does it return pointers):** FAILS.
- `recall_learnings.py` returns synthesized learning text content, not pointers to external documents or corpus entries.
- The daemon uses headless Claude to analyze session JSONL transcripts and compress them into learning entries stored in `archival_memory.content`.
- This is AI-compression-of-corpus: Claude reads transcripts → produces summary learnings → stores in DB → later sessions retrieve the summaries.
- Per the pointer-vs-compression invariant: this pattern auto-disqualifies as retrieval substrate.

**Shape gate:** For user evaluation. CCv3 is a comprehensive development environment (109 skills, 32 agents, 30 hooks, TLDR analysis, formal math) — adoption scope well beyond a retrieval substrate component. The memory system is one of ~7 core systems; it cannot be extracted without the full stack (PostgreSQL Docker, TLDR daemon, wizard install).

**One element that does return pointers:** The handoff system (`session_start_continuity.py`) loads YAML handoff files by path and injects their content. The `handoffs` PostgreSQL table stores `file_path` pointers. But this is the continuity system (between-session state transfer), not a retrieval substrate.
