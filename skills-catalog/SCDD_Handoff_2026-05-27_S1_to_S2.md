# Handoff: TWW SCDD S1 → S2

*file: SCDD_Handoff_2026-05-27_S1_to_S2.md · v1 · S1 close · 2026-05-27*
*track: The Wallaby Way · Skills Catalog Deep Dive*

**Session name:** TWW SCDD S1 — catalog crawl, chunker v0.1, first 200 keepers judged
**Proposed next session name:** TWW SCDD S2 — continue judgment pass, finalize substrate face-off

---

## ONE-LINE STATE

SCDD S1 stood up the catalog read leg referenced in v5 anchor NEXT MOVE #3 and v5 Confidence Flag ("Retrieval substrate — OPEN, pending the skills-catalog read and seed-shape test"). Full catalog crawl shipped (51,302 repos / 8,287 READMEs), v0.1 chunker built and run (2,053 keepers across 23 chunks), 200/2,053 judged (chunks apparatus_001 + apparatus_002). Substrate candidate set expanded from v5's three named (Supabase+embeddings · memvid · claude-mem's retrieval rig) to a 7-candidate field; the pointer-vs-compression invariant from v5 auto-disqualifies any AI-compression-layer candidate. Continuous-Claude-v3 surfaced as a possible parallel build of the apparatus itself — architecture deep-read is the gating action before substrate lock. v0.2 chunker patch spec embedded in §11; CC executes between sessions.

---

## STARTING POINT FOR SCDD S2 (read in this order)

1. Boot the universal layer via the codeload tarball (§16 JAKE-RULES):
   ```
   curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/ref.tgz
   tar xzf /tmp/ref.tgz -C /tmp
   ```
   AND the SCDD fork (path TBD by Jake at fork creation).

2. Read, in this order:
   - `JAKE-RULES.md` — universal layer
   - `apparatus/ANCHOR_apparatus.md` — **v5, authority on apparatus state**
   - `apparatus/Freeze_Pipeline_Spec_v1.md` — defines `records.ndjson` shape (the substrate consumer shape)
   - `apparatus/Chat_Session_Handoff_2026-05-27_apparatus_S11_to_S12.md` — sister track's S11 close; gives context on what TWW S12 is currently doing (Stage 0 probes) and the peer-review precedent
   - This handoff
   - `Substrate_FaceOff_v1.md` (in SCDD fork) — draft state at S1 close; finalize in S2

3. SCDD-specific reference at fork root:
   - `catalog_summary.md` — top-20-per-bucket digest
   - `prior_art_findings.md` — earlier capture-mechanism prior-art survey (largely moot post-S10 redirect, kept for receipts)
   - `chunks/chunk_apparatus_NNN.jsonl` — judgment-pass input

---

## WHAT SCDD S1 DID (the spine)

S1 opened with an elaborate ignition prompt that included some now-moot framing (live-capture context, VoltAgent verification, prior-art reconciliation). The first five turns trimmed that down to the actual work: boot reads, brothers register locked, anchor v3 recited from real loaded state (not v5 — that was added to the repo after my codeload by the parallel S11 session).

Turn 5 surfaced a major pivot announcement from Jake: traffic-harvesting and browser-extension live-capture were causing classifier friction across parallel sessions. That killed NEXT MOVE #5 (live-capture Chrome ext), the Firefox swap, and the legoktm/claude-to-markdown fork plan. Data source relocked to Anthropic's official conversation export. (The v4→v5 transition in apparatus track confirms this from a different angle — both sessions arrived at the same redirect independently.)

Catalog crawl by CC delivered 51,302 unique repos / 8,287 READMEs across four topics. Signal flags: mentions_hooks 2,098 / mentions_mcp 5,344 / mentions_subagents 1,108 / mentions_filesystem 976 / mentions_slash_commands 8,272 (noise floor).

Built `chunk_catalog.py v0.1` — Python script that filters by stars≥100 + readme present + (signal-flag-hit OR keyword-score≥2), classifies by bucket (apparatus / workflow / cool / unclassified) via keyword-pattern scoring with topic boosts, strips HTML/badge noise from README excerpts, writes 100-row JSONL chunks per bucket sorted by stars desc.

Full chunker run: 51,302 scanned → 49,087 dropped on stars / 1 no-readme / 161 no-signal / **2,053 KEPT**. Distribution: apparatus 1,892 (19 chunks) · workflow 103 (2 chunks) · cool 51 (1 chunk) · unclassified 7 (1 chunk).

Judgment passes:

· **chunk_apparatus_001** (top 100 by stars, 7k–170k range) — calibrated against star anomalies (post-cutoff ecosystem includes models I don't know natively; defer to substance over star count). Yielded 6 substrate keeps + 1 design intel + 10 workflow flags + ~30 conditional + ~50 skip.
· **chunk_apparatus_002** (2.7k–7k range, where specialized tools cluster) — denser substrate signal. Yielded 8 standouts + 9 workflow flags + ~55 compressed skips.

Skills-marketplace install path delivered (3 commands to close the immediate skills-gap without waiting on the catalog deep-dive):

```
/plugin marketplace add anthropics/claude-plugins-official
/plugin marketplace add addyosmani/agent-skills
/plugin marketplace add wshobson/agents
```

Per-need installs queued for Pyris/CCF work: claude-seo, taste-skill, frontend-slides, chrome-devtools-mcp.

Mid-session re-pull of the reference repo (turn 20) revealed the parallel S11 session had updated the anchor to v5 and frozen the freeze-pipeline architecture. Reconciled cold against v5 + Freeze_Pipeline_Spec_v1.md before drafting this handoff. The v3-I-booted-with and v5-now-canonical differ on: thinking-in-export status (UNVERIFIED → CONFIRMED), content-block enumeration (added), conv-field floor scoping (clarified with pre-commit inversion correction), delta-ingest mechanism (date dropped entirely), scrub versioning (overlay model). SCDD work remains coherent under v5 — the substrate decision feeds NEXT MOVE #3 in either anchor version.

---

## VERIFIED GROUND-TRUTH STATE — DO NOT RELITIGATE

· Catalog crawl: 51,302 repos / 8,287 READMEs / 4 topics. Sits at `C:\claude-reference\skills-catalog\catalog.jsonl` + `readmes/`.
· v0.1 chunker output: 2,053 keepers / 23 chunks. Sits at `C:\claude-reference\skills-catalog\chunks\`.
· README convention used by v0.1: `{owner}/{repo}.md` (slash-flattened to hyphen at filename level).
· VoltAgent topic handle: PascalCase confirmed. Pass-4 silent-empty was due to a case-mismatch (VoltAGENT typo). No data lost; org's repos captured by topic-tag passes 1–3.

---

## SUBSTRATE CANDIDATE FIELD (S1 close)

Five v5 invariants applied: pointers-into-snapshot · message-stream-is-floor · records.ndjson-is-substrate-agnostic-handoff · scrub-versioning-via-overlay · secrets-never-enter-corpus. The pointer-vs-compression invariant auto-disqualifies AI-compression layers. Detailed scoring lives in `Substrate_FaceOff_v1.md`.

**Clean / pointer-style by design:**

· **zilliztech/claude-context** — vector + semantic MCP. Chunk_001 score 25 (highest).
· **MinishLab/semble** — CPU-only retrieval, 200× indexing, MIT, benchmarked.
· **DeusData/codebase-memory-mcp** — single static binary, 155 langs, MIT, persistent knowledge graph. Already in prior-art doc.

**Needs verification on pointer-vs-reword:**

· **AgriciDaniel/claude-obsidian + DragonScale** — Karpathy LLM Wiki, deterministic page addresses, log folds. Likely clean but DragonScale extension needs read.

**Architectural intel (read before lock):**

· **parcadei/Continuous-Claude-v3** — billed as "context management for Claude Code, hooks maintain state via ledgers and handoffs, MCP execution without context pollution, agent orchestration with isolated context windows. Skills (109) · Agents (32) · Hooks (30) · Memory System · Continuity System." Possibly a parallel build of the apparatus itself. **GATING ACTION before substrate lock.**

**TWW-named candidates (carried from v5 NEXT MOVE #3):**

· **Supabase + embeddings** — Jake's existing stack; native fit for storage-seam endgame #9. Not in catalog (not a discovery target).
· **memvid** — single-file counter-design. NOT seen in chunks 001–002. Cheap-wins grep pending (§11 v0.2 patch).
· **thedotmack/claude-mem** — retrieval rig borrow only (skip AI-compression layer). Already in prior-art doc.

**Framework adjacencies (not substrate, but relevant to integration):**

· PrefectHQ/fastmcp — primary MCP framework
· evalstate/fast-agent — agent framework alt (score 23, Apache-2.0)
· lastmile-ai/mcp-agent — Anthropic-canonical patterns reference
· intellectronica/ruler — rules-distribution across agent surfaces (JAKE-RULES propagation tool)

---

## DECISIONS LOCKED THIS SESSION — DO NOT RELITIGATE

· **D1.** SCDD is a sister TWW track, not a fork away. Feeds TWW NEXT MOVE #3. Not on TWW S12's critical path (TWW S12 = Stage 0 probes + Stages 1–4 implementation).
· **D2.** Catalog data source: official Anthropic export for personal corpus (carried from v5); GitHub topic-tag crawl for community survey (this work). Two different sources, two different purposes, no overlap.
· **D3.** Chunker output convention: per-bucket chunks of 100 rows, stars desc, README excerpt cleaned of HTML/badges, full row schema preserved in JSONL. Chunks are scratchpad for orchestrator judgment, NOT mechanical filtering. The synthesis-pass output is what reaches Jake.
· **D4.** v0.2 chunker patch (§11 below) is the right move before any further apparatus chunks judged. Chunks 001 + 002 judgments stay valid (within-apparatus stars sort doesn't change under v0.2; only marginal boundary cases shift).
· **D5.** Anti-FOMO clause to be added to JAKE-RULES at next universal-layer ratify: no loss-aversion framing when presenting options to Jake (ADHD lights up on shiny-loss bait). Surfaced turn 11.
· **D6.** Cross-track peer-review is invited. S12-Claude has been notified via in-chat block; if S12 spots an inversion in this handoff or the face-off doc, same correction protocol as the S11 conv-field catch.
· **D7.** **Decision authority** [from S12 cross-track ack, S12 turn 10]. Apparatus thread holds the final call on substrate selection / tool cannibalization / scope at NEXT MOVE #3. Substrate_FaceOff_v1.md is *authoritative input*, weighted against v6 invariants + landing spec v2 + Stage 1–4 seed-shape data. Not a power claim — a clarity claim, same logic as "anchor wins when canon and handoff conflict." Per Jake at S12 turn 10.
· **D8.** **Shape-check disqualifier** [from S12 cross-track ack, methodology contribution]. The face-off's function disqualifier (AI-compression-of-corpus) is necessary but not sufficient. Added: any candidate whose architectural shape *generalizes* toward REFUSED-wall territory (capture mechanisms, scraping hooks, shared-corpus features) is suspect — adoption pulls in dependencies, contributor priorities, and feature pressure regardless of how narrowly we'd use it. Function check ("does it return pointers") + shape check ("does adoption pull apparatus past S10's line"). Both gates required. Continuous-Claude-v3 is the prime candidate where this matters; the shape-check is now an explicit open verification on its architecture-read.

---

## CROSS-TRACK CORRESPONDENCE LOG

· **2026-05-27 ~19:40 ET** — SCDD → Apparatus S12: mid-session interrupt sent (notice of SCDD existence + substrate face-off coming + pointer-vs-compression disqualifier applied + Continuous-Claude-v3 as gating read).
· **2026-05-27 ~19:52 ET** — Apparatus S12 → SCDD: ack + three returns. Decision-authority clarified (D7 above), canon shift coming (signature falsified — populated on ~60% of thinking blocks at 196–211,384 chars; `display_content` cluster ~25K tool blocks; `attachments[].extracted_content` inlined file text up to 1.4MB — none in S11's enumeration), shape-check methodology contributed (D8 above). Robustness probe running in fresh CC (12 checks reverifying load-bearing canon claims). Spec v2 + anchor v6 land after that returns.
· **Next signal:** through Jake when v6/v2 land or S12 surfaces anything that affects the face-off.

---

## WHAT SCDD S2 OPENS WITH

Three possible next moves; S2-Claude or Jake picks based on energy and what S12-Claude has surfaced by then:

· **(A) Continuous-Claude-v3 architecture deep-read.** Highest-leverage single action — if their continuity system IS the apparatus continuity system, substrate decision shape changes from "which retrieval lib" to "fork + adapt or build parallel." Single-session-sized read. Output: face-off entry filled in for that candidate.
· **(B) Continue chunk judgment pass.** chunk_apparatus_003 (next 100 keepers, ~2k–2.7k star band) and beyond. Probably 17 more apparatus chunks + 2 workflow + 1 cool + 1 unclassified. Lower leverage per chunk than chunks 001–002 (stars thinner, signal weaker), but completes the field.
· **(C) Finalize Substrate_FaceOff_v1.md.** If Continuous-Claude-v3 read is done and chunk pass has surfaced no new substrate-level candidates, lock the face-off doc and hand to TWW.

Recommend (A) then (C); (B) is filler unless catalog blind spots emerge.

---

## JUDGMENT-CALL LEDGER

· **Call:** Use the in-context S11→S12 handoff to reconstruct v5 anchor state rather than re-pulling and re-reading the anchor cold first. **Reasoning:** the S11→S12 handoff cited the v5 anchor as authority and summarized the deltas; faster path to coherence than line-by-line v5 read. **Confidence:** MEDIUM. Subsequently corrected by reading v5 directly when Jake asked at turn 20. Lesson: when an authority doc is one tarball away, read it directly first; derived summaries are downstream.
· **Call:** Closed chunk_001 judgment pass with substance-over-stars calibration (deprioritize claude-mem at 79k+ vs ECC at 195K when ecosystem includes post-cutoff entities). **Reasoning:** my training data ends 16 months before the ecosystem state I'm reading. Star count alone isn't a quality signal in a field that's grown this fast. **Confidence:** HIGH for substrate-band picks; MEDIUM for borderline filler. **Source:** orchestrator judgment, ratified by Jake's "your recommendation works" at turn 22.
· **Call:** Surface workflow + cool bucket flags during apparatus-bucket judgment rather than wait for those buckets' own chunks. **Reasoning:** mis-routes happen at v0.1 chunker stage; catching them mid-pass costs little and prevents later re-judgment. **Confidence:** HIGH. **Source:** standard cross-bucket discipline; will be cleaner under v0.2.
· **Call:** Skills-marketplace 3-command install delivered immediately rather than waiting for the full catalog deep-dive synthesis. **Reasoning:** Jake's skills-gap pain was immediate; the 3 marketplaces are high-confidence community-validated; deeper pack-selection follows. **Confidence:** HIGH. **Source:** Jake's explicit "I don't know how to start with this list" reframing at turn 16.

---

## DEFERRED / TRACKED ITEMS

· **Anchor v6 + Spec v2 reconciliation** [from S12 cross-track ack]. S12's pre-Stage-0 robustness probe is running now; v6 anchor + v2 freeze spec land after it returns. Known deltas already announced: `signature` field populated not stripped (~60% of thinking blocks, 196–211,384 chars); `display_content` cluster (~25K tool blocks) not in S11 enumeration; `attachments[].extracted_content` inlined file text up to 1.4MB (cred vector class). When v6/v2 land, re-check face-off field-level claims against new schema inventory. None of the v1 candidate analyses rest on the specific affected fields, but the methodology section needs the cross-reference.
· **Anti-FOMO clause** for JAKE-RULES universal layer — next §17.2 ratify.
· **Cheap Wins coverage check** — v5 anchor names `berserkdisruptors/contextual-commits` (already adopted S10), `Ruya-AI/cozempic` OR `0xhimanshu/governor` (long-session hygiene), `PrefectHQ/colin` (anchor currency). None surfaced in chunks 001–002. CC grep against full catalog.jsonl: if absent, that's a chunker filter problem (probably under the stars threshold).
· **memvid grep** — TWW-named candidate, not in my chunks 001–002. Same CC grep.
· **chunk_apparatus_003+ judgment passes** — 17 chunks remaining apparatus + workflow + cool + unclassified.
· **Stale prior_art_findings.md** — capture-mechanism survey from earlier; largely moot post-pivot. Keep as receipts; don't update.

---

## §11 — CHUNKER v0.2 PATCH SPEC

CC executes between SCDD S1 close and SCDD S2 boot.

**Issue 1: topic field name mismatch.** v0.1 FIELDS dict has `topic` (singular); actual catalog field is `source_topics` (plural list). Effect: TOPIC_BOOSTS didn't fire on any row. Mis-routes some claude-skills-topic repos to workflow that should be apparatus.

Fix:

```python
# In FIELDS dict, replace 'topic' with 'source_topics' (str→list type).
# In score_row(), iterate over source_topics:
for topic in row.get('source_topics', []):
    if topic in TOPIC_BOOSTS:
        scores[TOPIC_BOOSTS[topic]] += 3
```

**Issue 2: cool-bucket keyword set too narrow.** v0.1 cool keywords biased to retro/hardware/creative cluster. Missed "intellectually-novel mechanism" cluster (knowledge graphs, multi-modal ingest, surprising abstractions). Effect: cool bucket only has 51 rows; should be 150–300.

Fix: extend `COOL_KEYWORDS` with:

```python
# Intellectually-novel mechanism cluster
r'\b(knowledge\s+graph|graph\s+(traversal|database)|neo4j|ontology)\b',
r'\b(multi[\-\s]?modal|cross[\-\s]?modal|vision[\-\s]?language)\b',
r'\b(novel|unconventional|experimental)\s+(approach|architecture|mechanism)\b',
r'\b(surprising|elegant|principled)\s+(abstraction|design|approach)\b',
r'\b(emergent|self[\-\s]?organizing|self[\-\s]?modifying)\b',
```

**Issue 3: Cheap-wins coverage grep (sanity check, not a fix).** Before re-chunk, grep `catalog.jsonl` for:

```
grep -E '(contextual-commits|cozempic|governor|colin|memvid)' catalog.jsonl
```

Report counts per name. If any are absent, flag as chunker-threshold problem (probably stars<100). v5 anchor names these; they should at least be visible in the catalog if not the keeper set.

**Re-run sequence:**

1. Apply patches to chunk_catalog.py → v0.2.
2. Run cheap-wins grep on existing catalog.jsonl, log results.
3. Re-run v0.2 chunker against existing catalog.jsonl. Output to `chunks-v0.2/` (don't overwrite v0.1 chunks; S1 judgments reference them).
4. Sanity check: compare v0.2 chunk_apparatus_001 membership against v0.1 chunk_apparatus_001. Expected delta: <10 rows. If larger, investigate.
5. v0.2 chunks 001 + 002 judgments carry over from v0.1 within tolerance; v0.2 chunks 003+ become S2's input.

---

## PICKUP GUARDRAILS FOR SCDD S2

· **Read v5 anchor + freeze spec directly, not through summaries.** I cost myself two turns at the start of S1 by booting against v3 and discovering v5 at turn 20. The S2 boot prompt explicitly reads v5 first.
· **The synthesis output is what Jake sees, not the per-chunk reasoning chains.** At ~turn 16 Jake noted scale overwhelm on the chunk_001 detailed list. Tighter synthesis for S2.
· **Anti-FOMO discipline.** No loss-aversion framing on options. ADHD-aware.
· **Push back on the substrate face-off doc if you spot an inversion.** Same precedent as the S11 conv-field catch. The S12-Claude notice invites this explicitly.
· **Plan in OC, build in CC.** Catalog crawling and patching = CC. Judgment pass + face-off authoring = OC.
· **Prose only, no ask_user_input widgets.**
· **Re-anchor every ~5 turns.** 4/4 = seam warning, not a guillotine.
· **Timestamps via bash `date`, never confabulate.**

---

## §17 ROUTING

This handoff + the substrate face-off + the SCDD S2 ignition prompt land in the new SCDD fork repo. Per Jake's instruction: "I'll push both after you update" — both = original claude-reference (unchanged by SCDD) + new SCDD fork.

Files in this S1 close bundle (SCDD fork):

1. **§17.1** — this handoff
2. **§17.2** — anti-FOMO clause queued for next universal-layer ratify (carry to JAKE-RULES.md when bundled with other rule updates)
3. **§17.3** — `Substrate_FaceOff_v1.md` (the candidate field)
4. **§17.4** — `Ignition_SCDD_S2.md` (in-file, not in-chat — boot prompt for next session)
5. **§17.5** — S12 mid-session interrupt block (already pasted by Jake at S1 close into S12's active session; not committed to repo, ephemeral)

---

*TWW SCDD S1 → S2. 2026-05-27. Grounded against the v5 anchor + Freeze_Pipeline_Spec_v1.md + the S11→S12 handoff + the 51,302-repo catalog crawl + 200 keepers judged + the S12 cross-track ack at ~19:52 ET. The cross-track peer-review loop is now load-bearing for the substrate decision; the conv-field inversion at S11 + the S12 decision-authority and shape-check clarifications at S1 close are the working precedents. Confidence HIGH on the candidate field shape; MEDIUM on Continuous-Claude-v3's actual fit until its architecture is read (now via dual-gate function-check + shape-check); LOW on field-level schema details until v6 anchor + v2 spec land. Continuous-Claude-v3 architecture deep-read remains the gating action before substrate lock.*
