#!/usr/bin/env python3
"""
chunk_catalog.py
v0.2 / S12 / apparatus
Change notes:
  Issue 1 fix — catalog field is source_topics (list), not topic (string).
    FIELDS key renamed; blob construction and TOPIC_BOOSTS scoring now iterate
    over the list so all source topics score correctly.
  Issue 2 fix — extend BUCKET_KEYWORDS["cool"] with five regex blocks:
    knowledge-graph, multi-modal, novel/unconventional, surprising/elegant,
    emergent/self-organizing. Score=2 each (conservative; downstream judgment
    still owns final placement).

Pre-filters catalog (Medium tightness), cleans README excerpts, chunks by
primary bucket hint at 100 rows/chunk. Feeds the judgment seat (chat-Claude).
NOT a final classifier - bucket assignments are HINTS.

Filter (Medium):
  has_readme = true AND stars >= 100 AND
  ((any high-signal flag set: hooks, mcp, subagents, filesystem)
   OR (max bucket-keyword score >= 2))

Each chunk row:
  full_name, stars, language, license, topic, flags,
  description, readme_excerpt (cleaned, ~800 chars),
  bucket_scores (per bucket), primary_hint, matched_keywords (top 5)

Outputs (under --out, default skills-catalog/chunks-v0.2/):
  chunk_apparatus_NNN.jsonl
  chunk_workflow_NNN.jsonl
  chunk_cool_NNN.jsonl
  chunk_unclassified_NNN.jsonl  (flag-hit only, no keyword hit)
  manifest.md
  summary.md

Edit FIELDS / README_CONVENTIONS at top if your catalog schema differs.
"""

import argparse, json, re, sys
from pathlib import Path

# ---- schema (edit if catalog.jsonl uses different field names) -------------
FIELDS = {
    "full_name":      ["full_name", "repo", "name", "nameWithOwner"],
    "stars":          ["stars", "stargazers_count", "star_count"],
    "language":       ["language", "primary_language"],
    "license":        ["license", "license_spdx", "spdx_id"],
    "source_topics":  ["source_topics"],          # list in catalog — Issue 1 fix
    "topics":         ["topics", "topic_list", "tags"],
    "description":    ["description", "desc"],
}
HIGH_SIGNAL_FLAGS = ["mentions_hooks", "mentions_mcp", "mentions_subagents", "mentions_filesystem"]
ALL_FLAGS = HIGH_SIGNAL_FLAGS + ["mentions_chat_or_projects", "mentions_slash_commands"]

README_CONVENTIONS = [
    "{owner}__{repo}.md", "{owner}_{repo}.md", "{owner}-{repo}.md",
    "{owner}/{repo}.md", "{repo}.md",
]

CHUNK_SIZE = 100
MIN_STARS = 100
MIN_KEYWORD_SCORE = 2
EXCERPT_CHARS = 800

# ---- bucket keyword tables (same shape as triage script; tune here) -------
BUCKET_KEYWORDS = {
    "workflow": [
        (r"\bfractional\s+(coo|cmo|cto|cfo)\b", 5),
        (r"\b(scalability|playbook|sop)\b", 2),
        (r"\b(proposal|pitch\s+deck|business\s+plan)\b", 2),
        (r"\b(invoice|invoicing|stripe|payment|billing|subscription)\b", 2),
        (r"\b(contract|nda|legal\s+template)\b", 2),
        (r"\bcrm\b|\blead\s+(gen|capture|management)\b|\bsales\s+funnel\b", 3),
        (r"\bemail\s+(campaign|automation|outreach|template|sequence)\b", 3),
        (r"\b(cold\s+email|cold\s+outreach|newsletter)\b", 2),
        (r"\b(docx|pptx|xlsx|word\s+document|pdf\s+generation|mail\s+merge)\b", 2),
        (r"\b(seo|ga4|google\s+analytics|search\s+console|sitemap|json-ld|opengraph)\b", 3),
        (r"\b(wix|velo|wixdata|wix\s+studio)\b", 5),
        (r"\b(supabase|railway|porkbun|cloudflare\s+workers)\b", 2),
        (r"\b(calendar|scheduling|booking|appointment|calendly|cal\.com)\b", 2),
        (r"\b(journal|journaling|brain\s*dump|task\s+manager|pomodoro|adhd|gtd)\b", 2),
        (r"\b(notion|obsidian|logseq|roam|capacities)\b", 2),
        (r"\b(3d\s+print|bambu|prusa|openscad|fusion\s+360|stl|gcode)\b", 3),
        (r"\b(home\s*lab|nas|synology|tailscale|robocopy|samba|wireguard)\b", 3),
        (r"\b(booster\s+club|recruiting|nil\s+(deal|advisor)|hudl|maxpreps)\b", 3),
        (r"\b(n8n|zapier|make\.com|huginn|node-red|home\s*assistant)\b", 2),
    ],
    "apparatus": [
        (r"\b(persistent|long.term|conversation|chat|session|agent)\s+memory\b", 5),
        (r"\bmemory\s+(system|store|layer|bank|management|server)\b", 4),
        (r"\b(session|conversation)\s+(handoff|continuity|state|history|export|backup)\b", 5),
        (r"\b(snapshot|append.only|immutable\s+log)\b", 3),
        (r"\b(retrieval|rag|vector\s+(db|store|database|search)|embedding)\b", 4),
        (r"\b(chroma|qdrant|pinecone|weaviate|milvus|pgvector|lancedb)\b", 3),
        (r"\b(semantic\s+search|hybrid\s+search|fts5|full.text\s+search)\b", 3),
        (r"\b(mcp|model\s+context\s+protocol)\b", 3),
        (r"\b(mcp\s+server|mcp\s+client|fastmcp)\b", 4),
        (r"\b(claude|agent|session|tool|llm)\s+hook", 4),
        (r"\b(sessionstart|pretooluse|posttooluse|userpromptsubmit|stop)\s*hook", 6),
        (r"\bSKILL\.md\b", 5),
        (r"\bskill\s+(library|pack|registry|catalog|loader)\b", 4),
        (r"\b(subagent|sub.agent|multi.agent|agent\s+(orchestration|swarm))\b", 3),
        (r"\b(prompt\s+(library|management|engineering|registry)|system\s+prompt)\b", 2),
        (r"\b(anchor|ground.truth|drift\s+detection)\b", 3),
        (r"\b(chat\s+export|conversation\s+export|claude.ai\s+export|conversation\s+backup)\b", 4),
        (r"\b(codebase\s+(memory|context|index)|repo\s+index|symbol\s+graph|ast\s+search)\b", 4),
        (r"\b(token\s+counter|prompt\s+cache|context\s+cache)\b", 2),
    ],
    "cool": [
        (r"\b(stable\s+diffusion|comfyui|sdxl|flux|image\s+generation|text.to.image)\b", 3),
        (r"\b(text.to.speech|voice\s+clone|whisper|elevenlabs|coqui)\b", 3),
        (r"\b(video\s+generation|text.to.video|runway|pika|sora)\b", 3),
        (r"\b(music\s+generation|suno|udio|audiocraft|musicgen)\b", 3),
        (r"\b(roguelike|cellular\s+automaton|godot|unity\s+mcp|unreal\s+mcp)\b", 2),
        (r"\b(procgen|procedural\s+generation|terrain\s+gen|dungeon\s+gen)\b", 3),
        (r"\b(raspberry\s+pi|arduino|esp32|esp8266|micropython|circuitpython)\b", 2),
        (r"\b(robotics|ros2|drone|cnc|laser\s+cutter)\b", 2),
        (r"\b(arxiv|paper\s+qa|literature\s+review|citation\s+graph)\b", 3),
        (r"\b(bioinformatics|protein\s+fold|alphafold)\b", 2),
        (r"\b(visuali[sz]ation|interactive\s+demo)\b", 2),
        (r"\b(terminal\s+ui|tui|ascii\s+art|pixel\s+art|demoscene)\b", 2),
        (r"\b(local\s+llm|llama\.cpp|ollama|lm\s+studio|gguf|quantization)\b", 2),
        (r"\b(lora|qlora|fine.tuning|distillation)\b", 1),
        (r"\b(brain\s+(rewire|hack)|cognitive\s+(load|enhancement))\b", 2),
        # Issue 2 additions — v0.2
        (r"\b(knowledge\s+graph|graph\s+(traversal|database)|neo4j|ontology)\b", 2),
        (r"\b(multi[\-\s]?modal|cross[\-\s]?modal|vision[\-\s]?language)\b", 2),
        (r"\b(novel|unconventional|experimental)\s+(approach|architecture|mechanism)\b", 2),
        (r"\b(surprising|elegant|principled)\s+(abstraction|design|approach)\b", 2),
        (r"\b(emergent|self[\-\s]?organizing|self[\-\s]?modifying)\b", 2),
    ],
}

FLAG_BOOSTS = {"apparatus": {"mentions_hooks": 3, "mentions_mcp": 2,
                              "mentions_subagents": 2, "mentions_filesystem": 1}}
TOPIC_BOOSTS = {"apparatus": {"claude-skills": 3, "model-context-protocol": 2,
                               "mcp-server": 2, "claude-code": 1}}

# ---- README cleaning ------------------------------------------------------
RE_BADGE = re.compile(r"!\[[^\]]*\]\(https?://(?:img\.shields\.io|[^)]*?\.svg|[^)]*?/(?:actions|workflows|badges?)[^)]*)\)", re.I)
RE_IMG_MD = re.compile(r"!\[[^\]]*\]\([^)]+\)")
RE_HTML = re.compile(r"<[^>]+>")
RE_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
RE_MULTI_NL = re.compile(r"\n{3,}")
RE_TRAIL_WS = re.compile(r"[ \t]+\n")

def clean_readme(text):
    text = RE_BADGE.sub("", text)
    text = RE_IMG_MD.sub("", text)
    text = RE_HTML.sub("", text)
    text = RE_LINK.sub(r"\1", text)
    text = RE_TRAIL_WS.sub("\n", text)
    text = RE_MULTI_NL.sub("\n\n", text)
    return text.strip()

# ---- helpers --------------------------------------------------------------
def pluck(row, key):
    for f in FIELDS[key]:
        v = row.get(f)
        if v: return v
    return ""

def normalize_license(v):
    if isinstance(v, dict):
        return v.get("spdx_id") or v.get("name") or ""
    return str(v) if v else ""

def find_readme(readme_dir, owner, repo):
    for pattern in README_CONVENTIONS:
        p = readme_dir / pattern.format(owner=owner, repo=repo)
        if p.exists(): return p
    return None

# ---- main -----------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", default="skills-catalog/catalog.jsonl")
    ap.add_argument("--readmes", default="skills-catalog/readmes")
    ap.add_argument("--out",     default="skills-catalog/chunks-v0.2")
    ap.add_argument("--sample",  type=int, default=0)
    ap.add_argument("--min-stars", type=int, default=MIN_STARS)
    args = ap.parse_args()

    catalog_path = Path(args.catalog)
    readme_dir   = Path(args.readmes)
    out_dir      = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not catalog_path.exists():
        print(f"FATAL: catalog not found: {catalog_path}", file=sys.stderr); sys.exit(1)

    compiled = {b: [(re.compile(p, re.I), w) for p, w in pats]
                for b, pats in BUCKET_KEYWORDS.items()}

    # Tally counters
    total = scanned = no_readme = below_stars = no_signal = kept = 0
    buckets = {"apparatus": [], "workflow": [], "cool": [], "unclassified": []}
    used_convention = None

    print(f"Reading catalog: {catalog_path}", file=sys.stderr)
    with catalog_path.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if args.sample and line_no > args.sample: break
            total += 1
            try: row = json.loads(line)
            except json.JSONDecodeError: continue
            scanned += 1

            full_name = pluck(row, "full_name")
            owner, repo = (full_name.split("/", 1) + [""])[:2] if "/" in full_name else ("", full_name)
            stars = int(pluck(row, "stars") or 0)

            # Filter: stars
            if stars < args.min_stars:
                below_stars += 1; continue

            # Filter: has readme on disk
            rpath = find_readme(readme_dir, owner, repo)
            if not rpath:
                no_readme += 1; continue
            try:
                readme_raw = rpath.read_text(encoding="utf-8", errors="replace")
            except Exception:
                no_readme += 1; continue
            if not used_convention:
                used_convention = rpath.name

            # Issue 1 fix: source_topics is a list in the catalog
            source_topics = row.get("source_topics", [])
            if isinstance(source_topics, str):
                source_topics = [source_topics]

            # Score buckets against name + desc + source_topics + github topics + cleaned readme
            topics_val = pluck(row, "topics")
            topics_str = " ".join(topics_val) if isinstance(topics_val, list) else str(topics_val or "")
            source_topics_str = " ".join(source_topics)
            cleaned = clean_readme(readme_raw)
            blob = "\n".join([full_name, pluck(row, "description"), source_topics_str,
                              topics_str, cleaned[:20000]])

            scores = {}
            matched_kw = {}
            for bucket in ("workflow", "apparatus", "cool"):
                s, m = 0, []
                for pat, w in compiled[bucket]:
                    if pat.search(blob):
                        s += w
                        if len(m) < 5: m.append(pat.pattern[:50])
                for flag, boost in FLAG_BOOSTS.get(bucket, {}).items():
                    if row.get(flag): s += boost
                # Issue 1 fix: iterate over source_topics list for TOPIC_BOOSTS
                for t, boost in TOPIC_BOOSTS.get(bucket, {}).items():
                    if t in source_topics: s += boost
                scores[bucket] = s
                matched_kw[bucket] = m

            # Filter: signal-flag hit OR max keyword score >= MIN_KEYWORD_SCORE
            flag_hit = any(row.get(f) for f in HIGH_SIGNAL_FLAGS)
            max_score = max(scores.values())
            if not flag_hit and max_score < MIN_KEYWORD_SCORE:
                no_signal += 1; continue

            # Determine primary hint
            if max_score >= MIN_KEYWORD_SCORE:
                primary = max(scores, key=lambda b: scores[b])
                primary_matched = matched_kw[primary]
            else:
                primary = "unclassified"
                primary_matched = []

            enriched = {
                "full_name":       full_name,
                "stars":           stars,
                "language":        pluck(row, "language") or "",
                "license":         normalize_license(row.get("license", "")),
                "source_topics":   source_topics,
                "description":     (pluck(row, "description") or "")[:300],
                "flags":           {f: bool(row.get(f)) for f in ALL_FLAGS},
                "readme_excerpt":  cleaned[:EXCERPT_CHARS],
                "bucket_scores":   scores,
                "primary_hint":    primary,
                "matched_keywords": primary_matched,
            }
            buckets[primary].append(enriched)
            kept += 1

            if line_no % 5000 == 0:
                print(f"  ... {line_no:,} scanned, {kept:,} kept", file=sys.stderr)

    # Sort each bucket by stars desc, write chunks
    chunk_index = []
    for bname, items in buckets.items():
        items.sort(key=lambda r: -r["stars"])
        if not items: continue
        for i in range(0, len(items), CHUNK_SIZE):
            chunk = items[i:i + CHUNK_SIZE]
            n = (i // CHUNK_SIZE) + 1
            fname = f"chunk_{bname}_{n:03d}.jsonl"
            with (out_dir / fname).open("w", encoding="utf-8") as out:
                for r in chunk:
                    out.write(json.dumps(r) + "\n")
            chunk_index.append((bname, fname, len(chunk)))
            print(f"  wrote {fname}: {len(chunk)} rows", file=sys.stderr)

    # Manifest
    with (out_dir / "manifest.md").open("w", encoding="utf-8") as out:
        out.write("# Chunk Manifest\n\n")
        for bname in ("apparatus", "workflow", "cool", "unclassified"):
            bucket_chunks = [(f, n) for b, f, n in chunk_index if b == bname]
            total_in_bucket = sum(n for _, n in bucket_chunks)
            out.write(f"## {bname} ({total_in_bucket:,} rows, {len(bucket_chunks)} chunks)\n\n")
            for f, n in bucket_chunks:
                out.write(f"- `{f}` ({n} rows)\n")
            out.write("\n")

    # Summary
    with (out_dir / "summary.md").open("w", encoding="utf-8") as out:
        out.write("# Chunk Summary\n\n")
        out.write(f"- Catalog rows scanned: **{scanned:,}**\n")
        out.write(f"- Dropped (stars < {args.min_stars}): {below_stars:,}\n")
        out.write(f"- Dropped (no readme on disk): {no_readme:,}\n")
        out.write(f"- Dropped (no signal + no keyword hit): {no_signal:,}\n")
        out.write(f"- **Kept: {kept:,}**\n")
        out.write(f"- README convention used: `{used_convention}`\n\n")
        out.write("## Kept by primary hint\n\n")
        for bname in ("apparatus", "workflow", "cool", "unclassified"):
            out.write(f"- **{bname}**: {len(buckets[bname]):,}\n")

    print(f"\nDONE. Kept {kept:,} of {scanned:,} scanned.", file=sys.stderr)

if __name__ == "__main__":
    main()
