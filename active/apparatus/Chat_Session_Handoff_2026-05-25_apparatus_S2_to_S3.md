# Handoff: apparatus S2 — Ratify + Re-architect (Brain-Soup) → S3: Archive-Fed Corpus Excavation

**One-line state:** CORPUS v1 + 7 track anchors ratified; the corpus model was re-architected mid-session from "partitioned by track" to **one undelineated body with per-project anchor-neurons as the index** (brain-soup); next is the CC-on-disk archive excavation that builds that body.

---

## Session record (what actually happened, incl. what went sideways)

S2 was the ratification-and-standup session for the Wallaby Way memory loop. It ran the loop live (boot → recite the address → re-anchor every ~5 turns → wrap-at-seam) as its own first real test.

- **Booted clean** off `ANCHOR_apparatus.md` v1 + JAKE-RULES (codeload, freshness tripwire green), corpus left cold. Recited the address; Jake nodded.
- **Ratified CORPUS v1** (`CORPUS.md`, 26 entries): fence held — excavator not architect, secrets clean (var-names kept, values redacted), honestly self-tagged (summary-sourced entries flagged, windowed quotes marked). The verbatim-vs-source check was handed to Jake (he was in the rooms; Claude wasn't). Two open items surfaced: a Printer-anchor quote ("it's just grease, don't worry about it") untraceable in corpus entry 4 → **source-or-strike**; and the LRN **business-court / $1,515 / Second Judicial District** verdict (a 5-24 fact) **missing from the corpus**, which only holds the older Justice-vs-District diagnosis + the $127.40 cost.
- **Ratified the 7 track anchors** (CastleBlack, CCF, Cypher, DayState, LRN, Printer, Pyris) for shape / invariants-with-why / corpus-traceability / flag-honesty. Pointer-chain test passed (Cypher's owner-key invariant traces to corpus entry 17; Pyris reconnections → entry 5; etc.). LOW-confidence flags on CCF punch-list / Printer live-state / Pyris per-contact were honest, not laundered.
- **LRN entry-3 sensitivity** confirmed kept as-is (Jake: nothing in it hurts him per the recent NY Supreme Court ruling).
- **`Track_Meet_Doctrine.md` rename finalized** (was `Cypher_Architecture_Discussion_2026-05-11.md`) — the canonical genesis name; pointer/file edits pending.
- **Cross-project visibility catch (Jake):** all prior excavators ran *inside the Cypher project*, so `conversation_search` only saw Cypher chats — that's why CCF/Pyris read stale. The hot layer (git + codeload) already crosses projects for free; only the cold-corpus bootstrap and the boot-directive install are project-bound.
- **Chose Option B (the full Anthropic data archive) over Option A (15 per-scope excavators)** — verbatim-by-copy instead of snippet-reconstruction, takes Jake off the bus instead of 15 hand-runs, rehearses the endgame (CC reads/writes programmatically). A demoted to fallback for archive gaps.
- **§5.1 fired live:** CC inspected the 348MB archive and **falsified the planned partitioner** — `conversations.json` carries **no project↔conversation field** (UUID searches hit only incidental prose). The gate paid for itself; we'd have built the whole partition on a field that doesn't exist. Claude owned that the bad assumption was written into the kickoff *in the same document that warned against asserting export format from memory.*
- **Jake's content-driven ruling**, then **the bigger turn:** Jake reframed the corpus as **brain-soup** (one undelineated body) and anchors as **neurons/guideposts** pointing into it. Claude re-read the S1 genesis chat and confirmed: this is **S1 canon, not drift** — S1 explicitly said *"corpus without anchor is un-navigable noise; anchor = an index into it."* The **`track`-column partition was Claude's drift**, introduced two turns earlier; it re-walls the one-body corpus. Killed.
- **#3 — the presence layer:** Claude conjured the third brain element — the booted mind that runs on soup+neurons, the one part that can't be stored, only booted warm; the boot/recite loop is its mechanism, the lineage its workaround for not persisting.
- **Wrapped at the design→build seam** (re-anchor 4/4 fired ~turn 18).

---

## Verified ground-truth state — DO NOT RELITIGATE

- **Corpus = ONE undelineated indexed body. Anchors = the index/neurons into it, cited by pointer.** No `track` partition, no track-column, no locked vocabulary. (S1 canon; Claude's partition idea is dead.)
- **`conversations.json` has NO project↔conversation linkage** (CC-verified on 348MB). Partition is content/anchor-driven, never field-driven.
- **Option B (archive) is the build path.** A = fallback for gaps only. Don't re-propose 15 chats.
- **Compiled, not synthesized** — verbatim entries gathered untouched; nothing reworded.
- **`memories.json` is navigation, never a quoted source** (it's synthesized). Verbatim comes from `conversations.json` only.
- **Secret-scrub is a hard gate** ahead of any ingest — the S11 leaked cred is in the raw archive.
- **Storage target is deferred** (needed only at ingest, post-ratification). SQL does not exist yet and shouldn't until the seed shape is proven. B does not need the Supabase MCP seam.
- **Apparatus stays decoupled from Cypher's live schema.**
- **CORPUS v1 stands** as template + calibration target. The 7 anchors stand.
- **`Track_Meet_Doctrine.md` is the canonical genesis name.**

---

## Open — ordered next steps

1. **Run S3** (archive excavation, CC-on-Workhorse). Ignition prompt delivered at close, Phase-1 corrected to the brain-soup model.
2. **Decide storage target** in parallel (lean: new Supabase project for a clean role-sandbox; alt: `apparatus` schema in Cypher's project).
3. **Per-project anchor-discovery passes** — 7 walled tracks each in their own project; `meta` + LRN from the archive.
4. **Schema-from-seed-shape → ratify → CC ingest.**
5. **Land the rename** — Jake renames the file; correct the CORPUS entry-6 pointer; propagate in CLAUDE.md + boot prompts.

---

## Downstream flags (will bite later if dropped)

- **(Schema/ingest pass)** The corpus is undelineated, so the schema is a **flat addressable body** (id · date · source · decision-label · verbatim · flags), with anchors holding **pointer-lists** to entry IDs. An entry can be cited by many anchors (congeniality). Do **not** build a `track` partition key — that was killed. The earlier `text[]`-vs-join question dissolves with it.
- **(S3 spawn)** S3 runs as a **non-project chat** (cross-project job; don't box it). Upload the spec + `CORPUS.md` + `ANCHOR_apparatus.md` v2 at spawn — non-project chats have no PK. JAKE-RULES self-pulls via codeload.
- **(Anchor discovery)** The 7 walled anchors get discovered per-project; that needs the boot directive **installed in each project's instructions** (one-time). `meta`/LRN can't be — no wall — so they come from the archive in S3.
- **(CORPUS calibration)** S3 Phase-5 must resolve the two open ratification items (LRN business-court entry; Printer grease quote) against the real archive rooms.
- **(Rename orphans)** Archived handoffs cite the old genesis filename; they'll orphan on rename. Tolerable (plastic layer) — the durable citation is the CORPUS entry + anchor.

---

## Judgment-call ledger (the non-obvious calls · reasoning · confidence · source)

- **Adopted brain-soup (undelineated corpus) over Claude's own track-partition.** Reasoning: matches S1 canon verbatim ("an index into it"), and partition kills cross-domain recall. Confidence: **HIGH.** Source: live S1 genesis re-read this session + Jake's framing.
- **Chose B (archive) over A (15 excavators).** Reasoning: verbatim-by-copy, off-the-bus, endgame-rehearsal. Confidence: **HIGH** on the logic; **MEDIUM** pending CC Phase-0 archive-completeness verify. Source: this session; gated honestly.
- **Storage target deferred, leaning new Supabase project.** Reasoning: clean role-sandbox away from Cypher's locked owner-key model; fold-in later is a dump-and-load, not a migration. Confidence: **MEDIUM** (a real tradeoff, Jake's infra call). Source: this session.
- **Per-project anchor discovery for the 7 walled tracks.** Reasoning: project wall = cleaner relevance than content-guessing a blob. Confidence: **HIGH** for walled tracks; the meta/LRN-from-archive split is the honest patch for wall-less tracks. Source: this session + the project-scoping catch.

---

## Deferred / tracked items (each with its home)

- Storage-target decision → **before ingest** (step 4 / parallel).
- `track` schema shape → **the schema-from-seed pass** (flat body + pointer-lists; NOT a partition).
- Universal-layer cat-1/cat-2 sweep → **after corpus + anchors** (was the dead Cypher-only sibling; now archive-fed cross-project).
- Boot-directive install per project → **the per-project anchor-discovery pass.**
- Proposed reference-layer changes (project-scoped-search rule; the §5.1 export-format war story) → **`Proposed_Reference_Changes_S2_2026-05-25.md`**, Jake lands to the git rules repo.

---
*apparatus S2 → S3. Generated by S2 orchestrator-Claude; Jake routes. Verbose by mandate (§17.5a) — optimize next-Claude's time-to-productive.*
