# AgriciDaniel/claude-obsidian + DragonScale — Structural Inventory
Generated: 2026-05-27 | Session: TWW SCDD S2 prep round 2

DragonScale is IN-REPO — no separate pull required.
DragonScale files: `bin/setup-dragonscale.sh`, `docs/dragonscale-guide.md`, `wiki/concepts/DragonScale Memory.md`, `skills/wiki-fold/`, `scripts/allocate-address.sh`, `scripts/tiling-check.py`, `scripts/boundary-score.py`

---

## A. Repo Basics

**License**: MIT — "Copyright (c) 2026 AgriciDaniel (AI Marketing Hub)" (source: `LICENSE`)

**Last commit**: 2026-05-28 — "chore(assets): add 1280x640 social preview card"

**Top-level tree (depth 3)**:
```
AgriciDaniel/claude-obsidian/
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── .cursor/rules/claude-obsidian.mdc
├── .github/
│   ├── ISSUE_TEMPLATE/ (bug_report.md, feature_request.md)
│   ├── workflows/ (test.yml)
│   └── pull_request_template.md
├── .obsidian/
│   ├── plugins/ (calendar, obsidian-banners, obsidian-excalidraw-plugin, thino)
│   └── snippets/ (ITS-Dataview-Cards.css, ITS-Image-Adjustments.css, vault-colors.css)
├── .raw/
│   ├── .gitkeep
│   ├── .manifest.json           # delta tracker + DragonScale address_map
│   └── claude-obsidian-ecosystem-research.md  # sample source doc
├── .vault-meta/
│   ├── locks/
│   ├── address-counter.txt
│   └── legacy-pages.txt
├── _templates/                  # Obsidian Templater templates
├── agents/
│   ├── verifier.md              # pre-commit audit agent
│   ├── wiki-ingest.md           # parallel batch sub-agent
│   └── wiki-lint.md
├── assets/diagrams/             # architecture SVGs
├── bin/                         # 5 setup scripts
│   ├── setup-vault.sh
│   ├── setup-dragonscale.sh
│   ├── setup-retrieve.sh
│   ├── setup-mode.sh
│   └── setup-obsidian-git.sh
├── commands/                    # slash command entry points
├── docs/
│   ├── audits/
│   ├── dragonscale-guide.md     # DragonScale operational guide
│   └── (other guides)
├── hooks/
│   └── hooks.json               # SessionStart + Stop + PostToolUse hooks
├── scripts/
│   ├── allocate-address.sh      # DragonScale Mech 2: flock-guarded address counter
│   ├── boundary-score.py        # DragonScale Mech 4: frontier graph scorer
│   ├── tiling-check.py          # DragonScale Mech 3: embedding dedup
│   ├── wiki-lock.sh
│   ├── wiki-mode.py
│   └── detect-transport.sh
├── skills/
│   ├── autoresearch/SKILL.md
│   ├── canvas/SKILL.md
│   ├── defuddle/SKILL.md
│   ├── obsidian-bases/SKILL.md
│   ├── obsidian-markdown/SKILL.md
│   ├── save/SKILL.md
│   ├── think/SKILL.md
│   ├── wiki/SKILL.md
│   ├── wiki-cli/SKILL.md
│   ├── wiki-fold/SKILL.md       # DragonScale Mech 1: log rollup
│   ├── wiki-ingest/SKILL.md     # INGEST ENTRY POINT
│   ├── wiki-lint/SKILL.md
│   ├── wiki-mode/SKILL.md
│   ├── wiki-query/SKILL.md
│   └── wiki-retrieve/SKILL.md
├── tests/                       # 9 hermetic test suites (~1240 assertions)
├── wiki/
│   ├── canvases/
│   ├── concepts/                # seeded: LLM Wiki Pattern, Hot Cache, DragonScale Memory
│   ├── entities/                # seeded: Andrej Karpathy
│   ├── folds/                   # DragonScale fold pages land here
│   ├── meta/                    # dashboard, retrieval benchmarks
│   └── sources/
├── .gitignore
├── AGENTS.md
├── ATTRIBUTION.md
├── CHANGELOG.md
├── CLAUDE.md
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── README.md
└── WIKI.md
```

**Total file count**: 211

**Total LOC**: ~40,939 (excluding .png, .gif, .svg, .mp4 binary media)

---

## B. README + Architecture Docs

### README.md (verbatim)

See the full README verbatim in `substrate-reads/claude-obsidian/README.md` (677 lines). Key structural sections:

- "You drop sources. Claude reads them, extracts entities and concepts, updates cross-references, and files everything into a structured Obsidian vault."
- Architecture: "Sources land in `.raw/`. The `/wiki-ingest` agent reads each source, extracts entities and concepts, files them into the appropriate `wiki/` subfolder (per active methodology mode), and updates the index, log, and hot cache."
- DragonScale: "Optional opt-in extension (`bash bin/setup-dragonscale.sh`) that adds four memory mechanisms: log folds (rollup of past entries), deterministic page addresses, semantic tiling lint, and boundary-first autoresearch."
- Multi-writer: "Per-file advisory locks (v1.7+)" for parallel agents.

Architecture docs with verbatim content:
- `docs/dragonscale-guide.md` (operational guide)
- `wiki/concepts/DragonScale Memory.md` (design spec)
Both are in the repo; read at inventory time.

---

## C. Base claude-obsidian Ingest Path — THE KEY QUESTION

**Face-off open verification**: "Base claude-obsidian 'drops sources, agent reads them, extracts entities' suggests SOME rewriting on ingest."

### Ingest entry point: `skills/wiki-ingest/SKILL.md` (Single Source Ingest section)

```
## Single Source Ingest

Trigger: user drops a file into `.raw/` or pastes content.

Steps:

1. **Read** the source completely. Do not skim.
2. **Discuss** key takeaways with the user. Ask: "What should I emphasize?
   How granular?" Skip this if the user says "just ingest it."
3. **Create** source summary in `wiki/sources/`. Use the source frontmatter
   schema from `references/frontmatter.md`. Assign an address per the
   **Address Assignment** section below.
4. **Create or update** entity pages for every person, org, product, and repo
   mentioned. One page per entity. Assign addresses to new entity pages.
5. **Create or update** concept pages for significant ideas and frameworks.
   Assign addresses to new concept pages.
6. **Update** relevant domain page(s) and their `_index.md` sub-indexes.
7. **Update** `wiki/overview.md` if the big picture changed.
8. **Update** `wiki/index.md`. Add entries for all new pages.
9. **Update** `wiki/hot.md` with this ingest's context.
10. **Append** to `wiki/log.md` (new entries at the TOP):
    ## [YYYY-MM-DD] ingest | Source Title
    - Source: `.raw/articles/filename.md`
    - Summary: [[Source Title]]
    - Pages created: [[Page 1]], [[Page 2]]
    - Pages updated: [[Page 3]], [[Page 4]]
    - Key insight: One sentence on what is new.
11. **Check for contradictions.** If new info conflicts with existing pages,
    add `> [!contradiction]` callouts on both pages.
```

**"What Not to Do" section (verbatim)**:
```
- **Source files under `.raw/` are immutable.** Do not modify the files that
  users drop there (articles, transcripts, images). The `.raw/.manifest.json`
  delta tracker and its `address_map` (DragonScale Mechanism 2) are the only
  files under `.raw/` that `wiki-ingest` itself maintains. Treat every other
  file under `.raw/` as read-only source content.
```

**How-to-think appendix** (from SKILL.md):
```
| 7 | FEEL | A page that compounds — useful in 6 months, not just today.
            Skip filler; favor synthesis over transcription.
| 8 | ACCEPT | Not every claim is wiki-worthy. Editorial judgment is part of
               ingest, not a bug to remove.
```

### What the ingest writes to the vault

- **`wiki/sources/<slug>.md`**: a source *summary* page — Claude's extracted summary of the source, NOT the original content.
- **`wiki/entities/<Name>.md`**: LLM-generated entity pages (one per person/org/product).
- **`wiki/concepts/<Concept>.md`**: LLM-generated concept pages (one per significant idea).
- **`wiki/log.md`**: appended metadata entry (ingest operation log, not source content).
- **`wiki/hot.md`**: updated session context cache.
- **`wiki/index.md`**: updated master catalog.

### Does it preserve the original source file?

YES — but only in `.raw/`. The original source file is placed in `.raw/` and treated as **immutable/read-only**. The vault wiki pages (the searchable/queryable content) are ALL LLM-generated.

### FUNCTION-GATE VERDICT — Base layer

**FAIL (REWORDED/EXTRACTED)**. The base ingest layer writes LLM-generated summaries, entity extractions, and concept pages to the wiki — not verbatim copies of the source. Original sources are preserved in `.raw/` but this directory is hidden from Obsidian's indexing and is not the queryable layer. The SKILL.md explicitly instructs: "favor synthesis over transcription," "editorial judgment is part of ingest." A single source creates 8-15 wiki pages whose content is entirely LLM-authored.

---

## D. DragonScale Extension — Log Folds

**DragonScale is in-repo** (no separate pull). Activated via `bash bin/setup-dragonscale.sh`.

### Log fold data structure: `skills/wiki-fold/SKILL.md`

```
---
name: wiki-fold
description: "Rollup of wiki log entries into meta-pages. Reads the last 2^k
entries from wiki/log.md, writes a structurally-idempotent fold page to
wiki/folds/ that links back to children. Extractive summarization (no
invention). Dry-run by default, stdout-only; commit mode writes..."
---

# wiki-fold: Extractive Log Rollup

Implements a bounded subset of Mechanism 1 from [[DragonScale Memory]]:
flat fold over raw `wiki/log.md` entries.

A fold is **additive**: child log entries and their referenced pages are
never modified, moved, or deleted. A fold is **extractive**: every outcome
and theme in the output must be traceable to a specific child log entry.
No invented facts, no synthesis beyond what the child entries support.
```

**Fold ID format** (deterministic):
```
fold-k{K}-from-{EARLIEST-DATE}-to-{LATEST-DATE}-n{COUNT}
```
Example: `fold-k3-from-2026-04-10-to-2026-04-23-n8`

### Are log folds VERBATIM appends of incoming data?

**NO. Log folds are COMPRESSED extractive rollups.**

What a log fold processes: `wiki/log.md` entries — which are themselves **metadata** about past ingest operations (dates, operation types, page lists, one-line key insights). NOT the original source content.

What a log fold writes: a meta-page in `wiki/folds/` that compresses the log entries further with "extractive summarization." The SKILL.md constrains:
- "Every outcome bullet and theme bullet must cite a specific child entry or a quoted line from that entry."
- "Count checks" enforced — mismatches are dry-run blockers
- "No merging across entries without naming them"

But "extractive" here means extractive from log metadata, not verbatim. The fold condenses 2^k log entries into a structured rollup page. Original source content is NOT touched.

### FUNCTION-GATE VERDICT — DragonScale log folds

**COMPRESSED** (extractive rollup, not verbatim). Log folds summarize log.md metadata entries into a structured fold page. The input data being folded is itself metadata (not source content), and the fold output is a further compression of that metadata. No original source content passes through the fold operator.

**Note**: "Extractive" in the SKILL.md means facts are drawn from child log entries only (no invention), NOT that the fold content is a verbatim copy. Extractive ≠ verbatim.

---

## E. Multi-Agent System

### Multi-agent entry point: `agents/wiki-ingest.md`

```yaml
---
name: wiki-ingest
description: >
  Parallel batch ingestion agent for the Obsidian wiki vault. Dispatched
  when multiple sources need to be ingested simultaneously. Processes one
  source fully (read, extract, file entities and concepts, update index)
  then reports what was created and updated.
model: sonnet
maxTurns: 30
tools: Read, Write, Edit, Glob, Grep, Bash
---
```

### Is multi-agent local-only or shared/networked?

**LOCAL-ONLY orchestration.** Multiple parallel sub-agents run within one user's Claude Code session on one vault. Evidence:

1. `tools: Read, Write, Edit, Glob, Grep, Bash` — no network/cloud tools in the sub-agent.
2. The orchestrator dispatches sub-agents to process sources in parallel and then aggregates (updates index/log/hot after all agents finish).
3. The multi-writer safety (per-file advisory locking via `scripts/wiki-lock.sh`) is designed to prevent PARALLEL AGENTS on ONE USER'S VAULT from trampling each other — not cross-user or cross-account.
4. README FAQ: "Can multiple people edit the same vault safely? Yes (v1.7+). Per-file advisory locking..." — this is about the same vault being written by parallel agents (from one session), not multi-user.
5. Operational policy in DragonScale spec: "Access control: Out of scope. This is a single-user vault."

No shared corpus, no cross-account features, no cloud sync built into the plugin.

**No [SHAPE-FLAG] on multi-agent.**

---

## F. Vault File Scale

At 22,801 messages × 294 conversations:

The ingest unit is a **conversation** (one source document = one `.raw/` file = one ingest). The wiki-ingest skill produces 8-15 wiki pages per source.

Under **Generic mode** (default):
- `wiki/sources/<slug>.md` — one per conversation → **294 files**
- `wiki/entities/<Name>.md` — one per unique entity across ALL conversations. Deduplicated. If 294 conversations mention a shared set of ~50-300 unique people/orgs → **50–300 files**
- `wiki/concepts/<Concept>.md` — one per unique concept. If 294 conversations produce ~30-200 unique concepts → **30–200 files**
- Meta files: `index.md`, `log.md`, `hot.md`, `overview.md`, `_index.md` files → **~10 files**
- Optional fold pages in `wiki/folds/` if DragonScale activated → **variable**

**Estimated total wiki file count**: 384–804 files (roughly 400-800 files, well within filesystem norms).

Under **Zettelkasten mode**: flat timestamped files (`wiki/20260517123456-<slug>.md`). Same file count, flat directory instead of subdirectories.

The 22,801 individual messages are NOT separate ingest units — they are MESSAGE CONTENT within 294 conversations. Each conversation → one source file → one source summary page.

**.raw/ directory**: 294 source files (the original conversation exports, immutable).

---

## G. Shape-Surface Grep

Run against full extracted tree at `substrate-reads\claude-obsidian\`:

| Pattern | Hits | Classification |
|---------|------|----------------|
| `chat_conversations` | 0 | expected good ✓ |
| `claude\.ai` | 0 | expected good ✓ |
| `browser extension\|webextension\|content script` | 2 hits | **BENIGN** — both reference the [Obsidian Web Clipper](https://obsidian.md/clipper) browser extension (a legitimate clip-to-vault tool published by Obsidian team). Not DOM interception, not Claude.ai network monitoring. |
| `intercept\|mitm\|proxy` | hits in minified plugin JS + 1 metaphorical ("proxy for user intent") | **BENIGN** — minified JS in bundled Obsidian plugins (Thino, obsidian-banners); "proxy" is metaphorical in wiki-query skill. No network interception code in claude-obsidian skills/scripts. |
| `scrape\|scraping` | 4 hits | **BENIGN** — all in wiki/ content pages describing competitor/research notes about web scraping tools (not claude-obsidian code). One in modes.md describes `.raw/` as a place for "scraped pages" (user's own scraped data). |
| `multi.user\|shared.corpus\|cross.account` | 2 hits | **BENIGN** — one in SECURITY.md (security policy boilerplate), one in retrieval-benchmark query set ("What CRDT algorithm does the vault use for simultaneous multi-user editing?" — a benchmark test query, not a feature). |

No [SHAPE-FLAG] items. All hits are benign context.
