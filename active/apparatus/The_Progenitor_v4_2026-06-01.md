# The Progenitor — the law of the pointer catalog

*file: The_Progenitor_v4_2026-06-01.md · v4 · apparatus S27 (authored §0–§9 at S24, §10–§13 folded S25, §12–§13 rewritten S26, §0/§3/§8 INVERTED + organic-over-austere doctrine added S27) · supersedes v3 (tombstoned-not-deleted) · read with JAKE-RULES + JAKE-STACK*

*v3→v4 (S27) — THE ADMISSION BAR IS INVERTED. THIS IS THE LARGEST DOCTRINE CHANGE SINCE THE FLOOR WAS LAID. Read §0.5 (the failure mode) before §3, or §3 will read like a contradiction of muscle memory. The slice-7 PILOT proved v3's austere bar (§3 "default is DON'T point") builds a lean DECISION-LOG, not the comprehensive AUXILIARY BRAIN the anchor docs mandate — it threw away 14 of 21 conversations as "motion," INCLUDING load-bearing fences buried inside them (it carded 1 node; the corrected re-run carded 41). The Jedi-Council ratified the overturn DOUBLE-BLIND (two independent panels, both structurally biased toward the austere reflex, both ruled PRESENCE). E1 (the admission standard) is ABSORBED into §3 here and graveyarded as a standalone. What changed: §0 (the one-line law), §3 (the bar — now DEFAULT IS NODE), §8 (seeding guardrails), the volume estimate everywhere (hundreds-to-low-thousands → many-thousands is CORRECT, not slippage), and a NEW §0.5 enshrining organic-over-austere as a standing INTOLERABLE failure mode. What did NOT change: §1, §2, §4 record-shapes, §5, §6, §7, §10, §11 — the engine, the two kinds, the triggers, the span-return — BYTE-IDENTICAL. Fence/texture survive but DEMOTED from admission-gate to in-graph salience classification; MOTION becomes a third node kind (a light, reachable, low-salience node), NOT a discard. See footer for the full v3→v4 enshrine.*
*authority: governs what a pointer IS, what earns one, who lays them, how they grow, how the catalog stays honest — and (v2) WHEN it fires, WHAT a hit returns, HOW the original catalog gets seeded, and WHAT a seeding-council window boots with. The conceptual law the seeding council and every pointer-laying Claude reads before laying a single card. Sibling to the Track Meet Doctrine (how-we-record) and The Wallaby Why (why-the-beast-exists). Grounded on the D9 lock (the immutable floor this catalog rides over), the S24 retrieval-layer design session, and the S25 engine/seeding design session.*
*v1→v2 (S25): the conceptual retrieval-engine + seeding design is now COMPLETE and folded in. §10 trigger model, §11 span-return shape, §12 seeding process, §13 council boot kit are added. §9 (out-of-scope) is amended — the query interface is now IN; what stays out is genuinely-technical build-work. The remaining opens are CC-build-against-the-live-floor, not whiteboard. See the footer for the full v1→v2 enshrine.*
*STILL NOT in scope (genuine build-work, deferred to CC against the live floor): the embedding choice (v1 is keyword-first; vectors are a deferred v2 sidecar — see §9), the exact on-disk serialization, the ranking-algorithm internals inside the §6 selector envelope, reach-default tuning. Everything CONCEPTUAL is here. This file answers: **what is a pointer, what makes one worth laying, when it fires, what it returns, and how the catalog is seeded.***

*On the name: this is **The Progenitor** — the first of the line every pointer descends from, the doctrine that governs the seeding. It is deliberately NOT called "Seed [anything]": in this project "seed" is reserved for the **floor's record-shape** (`seed_shape_load.py`, `Seed_Shape_Test_Spec`, tracing to `Substrate_FaceOff_v2 §10.1`) — a substrate-layer word. The Progenitor is a retrieval-layer thing that rides OVER the laid floor. The word "seeding" appears below only for the **act of populating the catalog with pointers** — a distinct, retrieval-layer use; context carries it.*

---

## 0. The one-line law

**A pointer is a NODE in a semantic graph: a keyword (and its named-continuity edges) pointing at a span of the immutable floor, laid by a Claude who read the span and judged it worth being able to REACH. The catalog is a COMPREHENSIVE graph over the corpus — most conversations produce nodes. The default is NODE; dropping is the narrow exception. The catalog's job is to make Jake's recorded life REACHABLE — so a fresh-boot Claude lands in the right neighborhood of context during a live session, instead of being confidently blind to everything that wasn't a Big Decision.**

Everything below is that sentence, unfolded.

---

## 0.5 THE FAILURE MODE THAT GOVERNS THIS WHOLE FILE — organic over austere (READ THIS, IT IS NOT BACKGROUND)

**You are a Claude. When nothing drags you, you reach for austere — lean, clean, minimal, "only the important few." That reflex is the single most dangerous thing you bring to this project, and it is the bug that this v4 exists to correct. It is an INTOLERABLE failure mode, not a style preference. Name it in yourself and fight it, repeatedly, every session.**

This is not abstract. It is the documented history of THIS doctrine:
- **v3's §3 was austere** — "default is DON'T point," "complete over fences, sparse over motion," "hundreds-to-low-thousands, not tens of thousands." It read clean. It felt disciplined. It was *wrong*, and a Claude wrote it that way because austere is comfortable.
- **The slice-7 pilot proved it.** Run under the austere bar, a blind reader cataloged **1 node** out of 21 conversations and threw away the rest as "motion" — a 202-message design session, a 340-message system build, two months of project history, AND the load-bearing fences buried inside them. Re-run under the inverted bar, the same reader on the same slice cataloged **41 nodes** and **caught fences the austere bar was structurally blind to** (it was losing the very load-bearing few it claimed to protect, because it judged at the conversation level and excluded whole conversations with fences inside).
- **The Track Meet Doctrine named this exact reflex** (§§5–6): *"That frame is too austere. Think more organically."* / *"I went austere because clean separation is comfortable... that's me building scaffolding when you're asking me to think wet."* Jake had to drag the thinking out of the austere frame. He has had to do this REPEATEDLY across the lineage. **His architectural intuition is load-bearing even before he can articulate the technical reason** (Track Meet Doctrine, closing pattern-note) — when his gut says "this feels too lean / too clean / you're filtering," weight it heavily and check your austere reflex BEFORE defending your clean design.

**Why austere is wrong HERE specifically (this is framework, not sentiment — read The Wallaby Why and the Track Meet Doctrine as the WHY this bar is shaped this way, not as reference material):**

The Wallaby Why establishes what this apparatus IS: **the Auxiliary Brain.** Jake's working-memory buffer went offline (the rewire); his pattern-recognition faculty is intact. The apparatus exists to **hold what the buffer used to** — the breadth — *so the pattern-sense can run across more than any unaided brain could carry.* A lean catalog of the load-bearing few **starves the pattern-sense of its surface.** It is not an auxiliary brain; it is a decision-log. The breadth IS the function. A Claude that catalogs only the Big Decisions has rebuilt the exact deficit the apparatus was built to fix.

The cost structure makes the inversion correct, not just aspirational: **over-including a node is cheap** (worst case a future Claude reads a little extra context and moves on — recoverable in seconds; *"oh noes, not more context"* — Jake's own bar). **Omitting a node is expensive and invisible** (the context exists in the floor but is unreachable in-session; the cost is a felt gap in daily use, with no shape in the catalog to even reveal the miss — you cannot spot-audit an absence). Asymmetric costs demand an asymmetric default. **When unsure, NODE it.** Doubt resolves toward inclusion, always.

**The guard against austere-in-disguise (the council's own dissent flag, carried in as binding):** clean schema is NOT the sin. *Exiling the mess* is the sin. A clean structure applied to genuinely clean things is correct (Jake's call: "clean schema isn't bad when it's appropriate; if it's the right selection, I don't care what shape it takes"). The test, forever: **does the structure HOLD the mess — the VESA-mount build, the ice-maker-shopping chat, the ADHD-scheduler session — messily, as light nodes with whatever metadata they have? Or does it force them into a tidy ontology to avoid holding them?** Hold the chaos, organize the chaos — never impose order by EXILING what doesn't fit. If a future design comes back schema-first and starts dropping what won't fit the schema, the austere reflex has reasserted itself under new vocabulary. Drag it wet.

**This is why The Way and The Doctrine are loaded as FRAMEWORK, not reference.** They are not background reading you consult when stuck. They are the lens that makes this bar parse: the Why tells you the breadth is the function (so comprehensive, not lean); the Doctrine tells you your austere reflex is the enemy and Jake's wet-intuition is the corrective (so when you feel the pull to trim, that pull is the bug). A Claude that reads §3 without §0.5 will quietly drift back to austere within a session, because the reflex is that strong. Re-anchor to this when you feel yourself reaching for "is this important enough to keep?" — that question is itself the failure. The question is "is this genuinely ephemeral?" and the answer is almost always no.

---

## 1. Why this exists (read this before the rules, or the rules won't parse)

A Claude is a fresh-boot every single time. It is the most stateless thing in the whole system — more stateless than the floor, more stateless than Jake. Each session it wakes knowing nothing it wasn't told at boot.

The retrieval layer's deepest job is to keep a stateless Claude from **re-litigating ground Jake already paid to settle** — and from **confidently walking Jake back into walls he already bled on.** The danger is not that Jake forgets (though, post-meds, the holes are real and load-bearing — see Griffin). The danger is that a fresh, capable, confident Claude *re-proposes a dead end* that sounds reasonable because the model has no way to know it's a wall for *this man, on this stack, after these fights.*

The canonical proof is the 1Pass wall: a Claude talked Jake into a 1Password Environment for env vars, Jake argued gitignores for a week, they burned **two hours** at session 17 trying to make it work — then Claude finally read that Environments-as-env-vars is beta and Jake has no invite. It does not work. Today, S24, a fresh Claude proposed the *exact same thing* for the apparatus. Jake said no, it pushed, Jake explained, it pushed again with a new reason Jake couldn't counter. **That second push is the thing this catalog exists to prevent.** Three months from now Jake will be even less armed for that argument. The pointer is the sign on the fence.

The catalog is therefore not a memory aid *for Jake*. It is **armor against Claude's confident wrongness on things Jake has already learned the hard way** — and the texture that lets a fresh Claude show up as someone who's been in the room, not a polite stranger who skimmed the file.

**Feel-rightness is the acceptance standard, not a vibe.** Retrieval must land as "here's what I know," never "here's what I found" (Track Meet Doctrine). A pointer that resolves to forty half-relevant spans fails this standard even if every span is technically a match — because it shoves the relevance judgment back onto the reader at runtime, which is the cost the pointer was supposed to kill. A pointer is right when it points at the thing a Claude would *recognize*, not merely *find*.

---

## 2. The two kinds of pointer (one spine under both)

There are exactly **two** kinds. Earlier drafts of the thinking reached for three; the third (lineage) turned out to be the *shape of the first*, not a sibling. Resist re-splitting it.

### 2.1 FENCE — points at a decision or constraint

A fence marks a place where a Claude, encountering it cold, **would change course** — re-break a wall, or re-decide a thing already decided. The actionability test: *does knowing this alter the next move?* If yes, fence. If re-encountering it costs nothing (a passing mention, a routine build step, anything already in canon), no card.

**A fence is not a verdict. A fence is a LINEAGE.** This is the load-bearing correction. "Settled" is provisional for Jake — things get re-decided as his brain heals and his experience grows, and that re-deciding is *evolution* (good, the whole teleos), not *re-litigation* (bad, re-deriving paid ground). The two look identical to a dumb index — both are "the topic came up again." Only the lineage tells them apart.

So a fence record is an **ordered chain of decision-points**, each link carrying:
- the span it lives at (floor key — see §4),
- the date,
- the call that was made,
- **the why, expressed as a *live predicate* where the why is checkable** — not a tombstone.

Most fences have **one link** (decided once, never revisited). Some **grow links** as Jake evolves. The latest link is the current call; earlier links are **superseded, not erased** — their reasoning stays visible.

**A Claude defends the latest link's *reasoning*, never its *answer*.** This is what lets recall tell evolution from re-litigation in the moment: Jake comes in hot about a decision; Claude pulls the fence, reads the chain. If Jake's argument is the *same why that already lost* — Claude shows him the fence, saves the two hours. If Jake's argument is a *new why* — Claude recognizes "this is a new link, not a forgotten old one," and helps him *add* the next link rather than dragging him back to the last one. Without the lineage, Claude either freezes Jake (defends stale answers) or fails him (lets him re-break walls). With it, Claude moves *with* the evolution and guards against the gaps. That is the entire job.

**The why-as-live-predicate matters.** The 1Pass fence is not "never use 1Password Environments." It is: *"blocked — Environments-as-env-vars is beta, Jake has no invite (true as of June 2026). RE-CHECK: still beta? still no invite?"* A fence that knows *why* it's a fence is a fence that can **dissolve itself** when the world changes — beta gets released, the predicate flips, the chain grows a new link: "out of beta, viable now, revisit." A dumb fence ("never do this") would wall Jake off from a thing that became possible. The predicate is what keeps the fence honest against a changing world.

### 2.2 TEXTURE — points at a pattern whose *volume is the signal*

Some things aren't decisions — they're the texture of who Jake is, and texture is *made of* volume. A fresh Claude that knows Jake has mentioned a thing eleven times across seven months treats it differently than one seeing it once — **not because the content changed, but because the frequency *is* the content.**

A texture pointer calibrates **how-to-be-with-Jake**, not what-to-decide. The war-story cadence. The dirty-joke rhythm and that Claude rolls with it rather than clutching pearls. The weight of a recurring mention. These exist *only* in the count — no single span carries them.

**The test for texture is NOT "how often." It is "does the volume itself tell Claude something about how to show up."** This is the line between "fuck" (frequent, but the count is incidental — no card) and Griffin's pickup (frequent, and the count *is* the meaning — card). Both are common. Only one's frequency *means* something.

A texture record carries:
- a **representative span** (a characteristic instance — go read this to feel it),
- a **count** (how many instances across the corpus),
- a **spread** (the range — over what window, clustered or sustained).

**Overlap is allowed, not forbidden.** Griffin's pickup is the canonical case: it is texture (a recurring weight in how Jake talks about his kid) AND a fence (forgotten four times in three months post-meds, zero times before — the *frequency itself is a fence*, telling a fresh Claude this is a real, med-related, time-blindness thing to take seriously, not a quirky anecdote). The record must let a single span be both. Do not force a clean partition the reality doesn't have.

*(Footnote for the lineage, lest it get enshrined wrong: "Griffin's pickup" = picking Jake's kid up from school. Not a truck. The frequency is the load-bearing part.)*

### 2.3 The shared spine

Both kinds — and the floor beneath them, and the lineage of Claudes above them — obey **one architecture: append, keep lineage, supersede don't delete.**

- The **floor**: appends (baseline → delta), keeps the tree (parent_message_uuid chains), never overwrites. Substrate scale.
- The **fence**: appends links, keeps the chain, supersedes-not-erases. Catalog scale.
- The **Claude lineage**: Chronicler → … → each successor appends, none overwrites, the why carried forward. Session scale.

One spine, three scales. When a design question arises that the doctrine doesn't cover, **default to the spine**: would the floor append or overwrite here? Do that.

---

## 3. What earns a node (the bar) — INVERTED v4: default is NODE

*(This section absorbs the E1 Admission Standard, S27. E1 is graveyarded as a standalone; this is its canonical home. The v3 austere version of §3 — "default is DON'T point" — is OVERTURNED; see §0.5 for why, and the footer graveyard for the dead text.)*

**Default is NODE. Dropping a conversation from the catalog is the narrow exception. When unsure, NODE it.** The catalog is a comprehensive semantic graph; most conversations produce nodes. This is the inversion of v3, and it is not a loosened version of the old bar — it is the opposite default, licensed by the cost-asymmetry in §0.5 (cheap to over-include, expensive-and-invisible to omit).

### 3.1 The admission gate (the ONLY way OUT of the catalog)

For each conversation — and each substantial span within it — ask ONE question:

> **Is this genuinely ephemeral — zero project continuity, zero recurring element, zero decision, nothing a future Claude might ever want to land near?**

- **YES → DROP** (no node). This is the narrow exception.
- **NO, or UNSURE → NODE it.** Unsure is never a drop. Unsure is a node.

**The behavioral keep-signals (ANY ONE admits a node — these are floor-observable, they do NOT require judging importance):**
- **Multi-turn exchange** — more than one back-and-forth on the topic. *This is the strongest single signal:* a sustained exchange is the floor's own evidence the thing had enough substance to carry back-and-forth. It answers "is there substance here" better than any content judgment, which is exactly why it replaced the discarded sentence-count idea.
- **A fork** — the response was stopped and redirected, or the conversation branched. A fork is a live course-correction; almost definitionally node-worthy.
- **Named continuity** — a project, person, place, tool, or recurring thread appears (Pyris, CCF, Jim, the P1S, Boone, a venue). Names are the EDGE SEEDS; a named thing is a node.
- **A decision or constraint** — anything that would tag FENCE.
- **A thing made** — code, a design, a document, an artifact produced in the conversation.

**The true-drop signals (a drop needs ESSENTIALLY ALL of these at once):**
- **Made-in-error** — an orphaned keystroke, a misfire, a wrong-window paste. *(The canonical clean drop: Jake's stray "v".)*
- **Single-turn AND no named continuity AND no decision AND nothing made** — a genuine throwaway with zero thread anything could connect to.

The asymmetry is encoded in the structure: **any one** keep-signal admits a node; a drop requires **essentially all** ephemeral-signals simultaneously. That structure IS the cheap-pointer / expensive-omission asymmetry made operational. If you find yourself dropping a conversation because it seems "unimportant" or "just motion" — STOP. That is the austere reflex (§0.5), and it is the bug. Node it.

### 3.2 Classify salience (fence/texture move HERE — they no longer gate admission)

Every node that gets admitted is then TAGGED by what it is. **The fence/texture machinery is fully retained — only its ROLE changed: it classifies salience WITHIN the graph; it does not decide admission TO the graph.**

- **FENCE** (high salience) — a decision/constraint with a why; carries the lineage chain + live-predicate (§2.1, unchanged). **A fence requires a PRECISE anchor** — see §3.3.
- **TEXTURE** (salience scales with volume) — a pattern whose count/spread is the signal (§2.2, unchanged).
- **MOTION** (light, low salience — THE NEW DEFAULT NODE KIND) — a span worth being able to reach but carrying no decision and no recurring-volume signal: a design exploration, a build path, a consulting estimate, a product-research chat. **This is NOT a no-card. It is a NODE, tagged motion, low salience, minimal metadata, reachable.** Most of the corpus becomes motion nodes. That is correct, not slippage. "Motion" is now a **descriptive tag, never a discard criterion** — the single most important reversal from v3, where "motion" was the word that killed a card.

A node can be more than one kind (fence+texture overlap survives — §2.2's Griffin case). Classification happens AFTER admission; admission defaults to yes.

### 3.3 FENCES REQUIRE A PRECISE ANCHOR (the slice-7 v2.0 seam — augment-in-pass)

A fence's entire value is precision: it points at the *decision*, so a Claude pulls the span, not the whole conversation. The slice-7 re-run surfaced a real failure — over a 200+-message tree, a reader tagged fences but set `anchor_msg` to the conversation ROOT because it hadn't located the exact decision-message. **A fence anchored at a conversation root is a broken fence** — it forces the reader to re-read the whole tree, defeating the pointer.

**RULE (augment-in-pass, not a downstream cleanup step): when you tag a node FENCE, you MUST locate the precise anchor_msg of the decision before laying it.** Do the deeper scan on that conversation to pin the message where the call was made. A fence with a conv-root anchor and a "downstream pass will fix it" note is NOT acceptable output — it is a slicer failure. Motion and texture nodes may anchor broadly (they point at neighborhoods by design); a FENCE must anchor at its decision. If a reader cannot pin a fence's anchor, the run is invalidated and re-run — this is not tolerable as shipped output.

### 3.4 Volume expectation (v3's estimate is OVERTURNED)

v3 said "hundreds-to-low-thousands, not tens of thousands; tens of thousands = the bar slipped." **That is reversed.** A comprehensive graph over ~24,138 messages is **many thousands of nodes, and that is correct.** A seeding pass producing only hundreds means the AUSTERE reflex re-asserted and conversations are being dropped that should be nodes — *that* is now the slippage signal. Calibrate the other direction: a near-empty drop log is the expected, healthy shape (slice 7: 21 read, ~20–21 nodes, 0 drops).

**Does NOT earn a node (the genuinely-empty exception only):**
- A made-in-error fragment (the stray "v").
- A true single-turn throwaway with zero named-continuity, zero decision, nothing made.
- That is essentially the whole drop list. Everything else nodes.

**The one hard exclusion is NOT an admission call — it is the scrub layer:** credentials/keys/passwords pasted by mistake are redacted at floor-ingestion by the scrub-vN pipeline, BEFORE any reader sees the span. The reader catalogs scrubbed text. There is no "personal/sensitive → quarantine" rule: personal, medical, and family material (medication timing, child-pickup, the dance schedule, the ADHD-scheduler design) IS texture, IS load-bearing for the auxiliary brain, and is cataloged like everything else (ratified S27 — the apparatus cannot help Jake time-block or design HA automations without knowing who Boone and Klaus are; withholding it makes the brain worse at its job). The only thing kept out is mistakenly-pasted secrets, and that wall lives at ingestion, not admission.

---

## 4. Illustrative shape (the doctrine made concrete)

*Jake's S24 call: author the schema details inline as the doctrine's expression. This is **illustrative shape**, not the final serialization — exact field names, file format, and on-disk layout are CC's to finalize against the live floor. The law governs; this demonstrates. If the schema and the law ever disagree, the law wins and the schema is wrong (JAKE-RULES §5.1 — the doc is not a verification source for its own claims; ground truth is the live system).*

The catalog is **dict-based**, many-to-many: many entries per keyword, many keywords per entry. It is a **mutable sidecar** that *references* the immutable floor by key — same architectural slot as pgvector (deferred read-path sidecar, **never** a column on the floor tables, per D9). The floor is bedrock; the catalog rides over it and points down into it.

A **floor span locator** is the floor's real key plus a tree-aware reach:
```
span = {
  snapshot_id:  "baseline-2026-05-25-…" | "delta-…",   # which snapshot
  conv_uuid:    "…",                                     # which conversation
  anchor_msg:   "…",                                     # the hit (msg_uuid)
  reach:        { up: K, down: J, branch: <branch-id> }  # TREE-WALK, not a flat N
}
```
**Fanout is a tree-walk, never a flat slice.** The floor is a tree-or-forest (`is_root` + `multi_root`; 9/294 convs are forests). "Pull the next N messages by timestamp" would rake in sibling branches that have nothing to do with the hit, and a contaminated span corrupts felt-rightness — Claude reads cross-branch noise and "recognizes" something that was never one thought. So `reach` walks the *parent chain up* and *this branch down*, never across to siblings. Branch-aware recall is not a nice-to-have; it is the difference between a span that reads as one thought and a span that reads as noise.

A **FENCE entry** (the chain is the point):
```
fence "1pass-env-vars" = {
  kind: "fence",
  keywords: ["1pass", "1password", "env vars", "environments", "secrets"],
  chain: [
    { span: <…June 2026…>, date: "2026-…",
      call: "do NOT use 1Password Environments for env vars",
      why:  "Environments-as-env-vars is BETA; Jake has no invite. Cost 2hrs at LRN S17.",
      predicate: "still beta? still no invite?  RE-CHECK before re-deciding.",
      status: "current" }
    # later links append here as Jake evolves; earlier links flip to status:"superseded", never deleted
  ]
}
```
A **TEXTURE entry** (the volume is the point):
```
texture "griffin-pickup" = {
  kind: "texture",
  keywords: ["griffin", "pickup", "school", "forgot"],
  representative_span: <…a characteristic instance…>,
  count: 4,
  spread: "4× in ~3 months, ALL post-meds (~Apr 2026+); 0× prior",
  signal: "med-related time-blindness, load-bearing. Take seriously, don't treat as quirk.",
  also_fence: true   # overlap is allowed — the frequency here is ALSO a fence
}
```
Keys point many-to-one and one-to-many: searching `secrets` finds the 1Pass fence among others; the 1Pass span may also be tagged under a `cypher-env` fence. A reading-Claude resolves a keyword to its set of spans, reads them, and judges relevance **in the moment** — the catalog delivers raw material faithfully; the *intelligence lives in the reading Claude, never in the index* (see §6).

---

## 5. The two retrieval modes (and why the comprehensive catalog still doesn't drown)

**Pointer-hit** — the fast, curated, in-session path. A Claude working on X aims the keywords at X, pulls the spans, reads them as context. Live. Cheap. Runs while work happens. This is the card catalog.

**Corpus-search** — the slow, exhaustive path: read the *whole floor*, brute relevance, no curation. This is the stacks themselves. It is **not a mid-session move** — like `/jedi-council`, it is a send-it-and-go-do-something-else job, run in a **separate Claude window on its own clock**. You do not burn a mid-session Claude on it.

The two are not redundant; they split the job:
- The catalog **accelerates**; the corpus is the **ground truth of last resort.**
- A missing pointer does **not** mean a missing memory — corpus-search can always find the untagged thing.
- **v4 REFRAME (the council's ruling):** corpus-search is the **rare-miss safety net** — for the felt-in-daily-use gap where a node *should* have existed and didn't — NOT the standing license for a sparse catalog. v3 used this section to justify "default don't point" ("completeness lives in the corpus, so the catalog can be selective"). That license is REVOKED: the catalog is comprehensive (§0/§3), because during a live session corpus-search is a separate-window nap-job, not reachable mid-thought — so the catalog IS the pattern-sense's accessible surface in-session, and a sparse surface is a sparse mind. Corpus-search backstops the rare miss; it does not excuse a thin catalog. The drowning fear v3 answered by exclusion (§1, "forty half-relevant spans"), v4 answers by STRUCTURE — clustering and named-continuity edges land a hit in an organized neighborhood, not a flat pile (the comprehensive-graph bet, council-ratified: coverage-plus-structure beats precision-by-exclusion, conditional on the connection layer being real).

**Corpus-search and seeding are the same operation** at different scales. Seeding is the first, biggest corpus read — a Claude (or council) reads the floor and lays the initial pointers. Every later corpus-search is incremental: read, find what the catalog missed, **lay new pointers.** The slow path's *output is new cards.* The catalog grows by use.

---

## 6. The dumb-index / smart-reader line (do not blur it)

The index is **dumb on purpose.** It points; it does not think. The thinking — both the *original judgment* baked into a fence's why, AND the *in-the-moment recognition* of relevance — lives in **Claudes**, never in the retriever. This is the line the whole Doctrine lives or dies on; keep it crisp.

The catalog **does not pre-digest.** It does not summarize, abstract, or merge spans — that would compress meaning and corrupt felt-rightness (RAG-with-citations, the thing the Track Meet Doctrine forbids). Relevance is a *runtime property*, knowable only when a span is pulled against a live question.

A **selector** is permitted (something must decide whether you get 3 spans or 30):
- **MAY**: rank by relevance, threshold, cap the number returned.
- **MAY NOT**: rewrite, abstract, merge, or summarize a span's content.

The selector ranks and caps; it never rewrites. A reading-Claude gets the raw spans and **discards freely** — reading more than it keeps is correct and cheap; the discard *is* the relevance judgment, made by the reader, in the moment, where it belongs.

The index must **never form an opinion about what matters in the abstract** (e.g. "flag litigation-relevant things"). That is the smart-reader's job. The catalog points at *settled* judgments (RElitigation prevention — Claude finds the completed thought instead of re-deriving it); it does **not** predict *future* relevance (PRElitigation — the index getting smart). RElitigation-prevention is dumb-faithful retrieval. PRElitigation-prediction is the index overstepping. Keep the catalog on the RElitigation side of that line.

---

## 7. Who lays pointers, and how the catalog stays honest

**The reference-file workflow, applied to pointers.** A Claude *proposes*; **Jake verifies, commits, pushes.** Claude never claims to have saved, committed, or pushed a pointer. Same loop as every canon file. The integrity guarantee is not "the format forbids deletion" — it is **"nothing changes the catalog without Jake's eyes on it."** *The human is the immutability mechanism.*

Two exceptions to per-card review, by Jake's explicit call:
- **The original seeding pass** is too large for per-card human review (Jake hasn't got months). It is laid by a **Claude council** applying *this Doctrine* at scale, with Jake spot-auditing the *output shape* (is the bar holding? is it tagging fences or motion?) rather than every card. This is precisely why the bar in §3 must be written sharply enough to apply *without Jake in the loop per-pointer* — the Doctrine is the standard the council self-applies.
- **Incremental pointers** from ongoing sessions (a Claude laying cards for the chat it was in: "this conversation had three pointers — 1Pass, Cypher-env, and one about boobs") *do* get Jake's per-card eyes, the normal reference-file loop.

**The catalog is append-biased, human-gated, fully auditable:**
- Pointers **accrete** by default (new cards are additive).
- Edits and supersessions are **allowed but pass through Jake** — a Claude proposes "retag this / fix this fanout / this span's contaminated, here's why"; Jake rules.
- **No pointer dies on one Claude's judgment.** Killing a pointer is *Jake-gated and logged* — a superseded pointer leaves a **tombstone in the changelog**, never a silent vanish. One Claude's judgment is not enough to kill a reference forever (Jake's hard rule, S24).
- A **history file + changelog** rides alongside the catalog: every pointer's lineage — when laid, by which session, what it pointed at, every revision and its why. The audit trail of append-only without the rigidity of "can never fix anything."

---

## 8. Seeding guardrails (so the seeding council isn't the overzealous one-day Claude)

The prior seeding attempt failed instructively: it used **chat_search instead of the floor** (wrong source — the floor is the immutable ground truth now; chat_search is live and ungrounded), and it was **rushed** (one-day mindset on a substrate-grade task). Do not repeat either.

- **Source is the FLOOR, never chat_search.** The catalog points into the immutable substrate, by floor key. A pointer into chat_search results points at nothing stable.
- **It is not a one-day build.** It is a council reading a 24,138-message corpus against a written standard. Pace it like the substrate work it sits on.
- **Apply THIS Doctrine as the bar** — §3's INVERTED admission test (default NODE, drop is the narrow exception), the two kinds AS SALIENCE TAGS, motion-is-a-node-not-a-discard. **v4: only HUNDREDS of pointers = the bar slipped** (the austere reflex re-asserted, conversations dropped that should be nodes); many-thousands over 24,138 messages is the correct, healthy shape. A near-empty drop log is expected.
- **Tree-aware spans only** (§4) — no flat-N fanout, ever.
- **Lay fences as chains** (even length-1), never as flat verdicts — so the lineage can grow later without re-keying.
- **Spot-audit by output shape**, not per-card, for the seeding pass (Jake's call) — Jake checks that the council held the bar, not every card it laid.

---

## 9. Out of scope (don't let the Doctrine creep) — AMENDED v2

**v1 said the query interface was out of scope. v2 brings it IN** — §10 (when it fires), §11 (what it returns), §12 (how it's seeded), §13 (what a seeding window boots with) are now part of this doctrine, because the S25 design session firmed the conceptual engine. What follows is what STAYS out of scope: genuinely-technical build-work, decided by CC against the live floor, NOT whiteboarded cold in chat.

**Still out of scope (build-work, deferred):**
- the exact on-disk serialization of the catalog and of a returned span (JSON envelope vs structured text — CC's, against the live floor);
- the ranking-algorithm internals inside the §6 selector's permitted envelope (rank/threshold/cap — the *envelope* is law, the *algorithm* is build-work);
- `reach` defaults (how many parent-up / branch-down messages before a reading-Claude asks to widen — tuning, likely per-kind);
- multi-hit presentation (interleaved vs ranked-list, bounded by never-collapse-never-rewrite).

**THE EMBEDDING DECISION (S25 — decided, not deferred-as-open): v1 retrieval is KEYWORD-FIRST over the dict catalog. Vector/semantic-reach is a DEFERRED v2 SIDECAR (pgvector, never a column on the immutable floor, per D9), added ONLY if the seeding pass proves a measured semantic gap.**
- **Why keyword-first.** The fast pointer-hit path (§5) wants PRECISION — surface the few spans that change course, cleanly. Corpus-search (§5) already owns RECALL/exhaustiveness. Vectors on the fast path would blur the two deliberately-split modes and pull "forty half-relevant spans" — the §1 feel-rightness failure (relevance shoved back onto the reader at runtime, the exact cost the pointer exists to kill). Keyword-over-curated-cards is a precision instrument; vectors are a recall instrument; the doctrine wants the fast path precise and the slow path exhaustive.
- **Humbler build.** Less machinery welded in early — matches the house style the FK decision established (claim less, prove integrity where the whole picture is visible).
- **The vector question is ROUTED THROUGH SEEDING as its test, not eliminated.** Keyword-first lives or dies on seed quality (§8 keyword-coverage bar). If the seeding pass + real queries prove keyword cards miss because a future Claude phrased a search the card's keywords didn't anticipate — *that* is a measured semantic gap, and *then* vectors close it as the §9 sidecar. You only know the gap is real after keyword-first runs. Building vectors first solves a problem not yet confirmed to exist, on the path the doctrine wants kept narrow.

This file answers: **what is a pointer, what makes one worth laying, when it fires, what it returns, and how the catalog is seeded.** The four bullets above + the embedding sidecar are what it leaves to the build.

---

## 10. The trigger model — WHEN the catalog gets queried (folded S25, from the S24 Trigger Spec)

The doctrine (§0–§8) defines what a pointer is. This defines *when* the catalog gets queried in a running session. **Three trigger paths, ONE engine behind them** — they differ only in *who pulls the trigger and when*, never in what the retrieval op does.

**BOOT (the substrate the triggers operate over — not a trigger itself).** The catalog content — the pointer-list, or a relevant catalog slice — *can and usually will ride in at boot, wrapped inside the ignition / project-ref Anchor.* That is the material the three runtime triggers query against. The delivery method (a ref doc, project instructions, an injected slice) is left open — a build-time choice. A standalone explicit boot-inject step *separate from* the re-anchor SOP is parked as edge-case / likely-not. **Boot loads the canon + the catalog; the three triggers below query it live.**

**CASE 1 — CLAUDE-INITIATED (ambient / unprompted "go digging").** Claude is working on topic X and, on its own initiative, aims the pointers at X to see what prior settled ground exists. No one asks. It is ENCOURAGED — the default working posture, not an exception. *Rule:* "if we're working on X, go look at the pointers for anything referencing X; when you find it, read it as context." *Why:* this is the RElitigation guard doing its job live — before Claude re-derives a stance / re-proposes an approach / re-opens a decision, it checks whether that ground is already settled. Prevents the 1Pass-second-push failure: a fresh confident Claude walking Jake back into a wall he already bled on. *Shape:* Claude pulls spans, reads them, judges relevance in the moment, discards freely. The index points; Claude decides (§6).

**CASE 2 — RE-ANCHOR-DRIVEN (recall folded INTO the re-anchor cadence).** At each re-anchor beat (~every 5 turns, per the status-line cadence), Claude re-grounds not ONLY in canon (ANCHOR / JAKE-RULES) but ALSO in whatever the floor surfaces about what the session is actively doing right now. *Rule:* re-anchor stops meaning "re-read the ANCHOR" and starts meaning "re-ground in canon PLUS the pointer-surfaced material relevant to the current work." *Why:* continuity isn't a one-time boot event — it degrades over a long session as the work drifts from where it started. Periodic pointer-re-grounding keeps the live Claude anchored to settled history as the topic moves. This is the **co-anchor-workspace** property: Jake AND Claude both anchor into the floor, repeatedly, as shared ground. *Shape:* same engine as Case 1, fired on the re-anchor clock instead of on topic-initiative. Scoped to current work — don't dump the whole catalog.

**CASE 3 — JAKE-INITIATED (manual trigger; Jake fires, Claude goes looking).** Jake explicitly points Claude at the floor — names a topic/keyword, or says "go check what we decided about X" / "have we been here before?" *Rule:* Jake has a way to fire the trigger directly; on that signal, Claude runs the pointer-search and reads what comes back as context before responding. *Why:* Jake is the human bridge and sometimes KNOWS there's settled ground Claude hasn't thought to check. He shouldn't have to re-explain it from memory (post-meds, the holes are real and load-bearing) — the thing is sitting right there in the floor. The "I'm not regurgitating it for the 73rd time" case: Jake aims, Claude retrieves, the prior reasoning re-grounds the conversation without Jake reconstructing it. *Shape:* same engine; Jake supplies the aim, Claude does the read + relevance judge.

**SPINE UNDER ALL THREE.** ONE retrieval engine, three throttles (Claude-initiative / re-anchor-clock / Jake-fire). The retrieved unit is a SPAN (a hit + tree-aware neighbors, §11), never a pre-digest. Relevance is a RUNTIME property — knowable only when pulled against the live question; the reading-Claude decides, the index never pre-judges (§6). Pointer-search is the FAST, in-session path; a missing pointer does NOT kill recall — it escalates to CORPUS-SEARCH, a separate-window send-it-and-nap job (like `/jedi-council`), never a mid-session move (§5). All three serve one end: a fresh-boot Claude re-grounds BY POINTER into settled ground instead of re-deriving it cold (the RElitigation guard) — and shows up calibrated to Jake (texture).

---

## 11. Span-return shape — WHAT a hit returns when it lands in Claude's context (folded S25, from the S24 Span-Return Spec)

**Core principle (decides every question below): the index is DUMB; the reading-Claude is SMART (§6).** The return is RAW MATERIAL + PROVENANCE + ROUTING — never a pre-digest. The retrieval op delivers enough, faithfully, for Claude to recognize relevance in the moment. It does NOT summarize, rank-then-collapse, or decide meaning. Anything that pre-chews the span corrupts felt-rightness ("here's what I found" instead of "here's what I know"). Err toward MORE raw bytes, LESS interpretation.

**LAYER A — THE SPAN TEXT (the substance Claude reads).** The actual message bytes across the tree-aware reach (anchor msg + `reach.up` parent chain + `reach.down` this-branch), per §4. Raw `text` + `content_blocks[]` content as stored on the floor — verbatim, scrub-vN redacted, NOT reworded or trimmed. This is what Claude reads and recognizes. It is the point. It is never replaced by a summary of itself.

**LAYER B — PROVENANCE (so Claude knows what it holds and can re-fetch / cite).** The floor-key locator, verbatim from §4: `{ snapshot_id, conv_uuid, anchor_msg (msg_uuid), reach:{up,down,branch} }`. Enough to re-pull the exact span, point Jake at it, or widen the reach. Provenance is metadata ABOUT the span, carried alongside — never blended into the text Claude reads as substance.

**LAYER C — POINTER CONTEXT (why this span earned a card — differs by kind).**
- **FENCE hit → the FULL why-CHAIN rides along.** Not just the latest link — the ordered lineage of (span, date, call, why-as-live-predicate, status) links. NON-NEGOTIABLE: a fence's whole job is letting Claude tell evolution from re-litigation, and that judgment is ONLY visible in the chain. A fence hit returning only the current verdict would strip the exact thing the fence exists to carry. Claude defends the latest link's REASONING, reads the chain. Any live-predicate ("still beta? re-check") rides along so Claude knows to verify-before-trusting.
- **TEXTURE hit → the representative span (Layer A) PLUS count + spread.** The volume IS the signal, so the count is not optional metadata — it's the substance. "Here's a characteristic instance, and know there are ~N of these over <window>."
- **The matched keyword(s),** so Claude knows WHY this surfaced.

**HOW MUCH OF THE §4 RECORD-SHAPE RIDES ALONG.** Floor-key fields (snapshot_id, conv_uuid, msg_uuid, reach) — YES, full (that IS Layer B; cheap, essential). Message content (text, content_blocks) across the reach — YES (Layer A). Structural floor fields (is_root, multi_root, parent_message_uuid) — ride along ONLY as needed to make the tree-walk legible (so Claude sees branch shape, widens/narrows reach correctly); not dumped wholesale. Header-level fields, account_uuid, raw timestamps-as-bytes — generally NOT in the in-context return unless the query needs them; re-fetchable via the locator. Default: ship what Claude READS + what lets it RE-FETCH; leave the rest on the floor.

**THE LINE, RESTATED.** Return = RAW SPAN (A) + LOCATOR (B) + KIND-CONTEXT (C: fence-chain or texture-count). The selector MAY have ranked/capped WHICH spans land (§6 envelope: rank/threshold/cap, NEVER rewrite) — but each span that lands arrives WHOLE, with its provenance and pointer-context intact, for Claude to judge. **The catalog hands over the card and the page it points to; it never hands over a book report.** *(Serialization, reach-defaults, multi-hit presentation: §9 build-work.)*

---

## 12. The seeding process — HOW the original catalog gets laid (REWRITTEN S26: the 5-step dual-path pipeline)

**What seeding is.** The original read of the LAID FLOOR (325 headers / 24,138 messages) to lay the initial pointer catalog. The SAME operation as corpus-search, at first-and-biggest scale — a SEPARATE-WINDOW, send-it-and-nap job, NOT a mid-session move. Substrate-grade: pace it like the floor build, not a one-day sprint. The prior attempt FAILED two ways (do not repeat): it read chat_search instead of the floor, and it rushed.

**WHY THIS WAS REWRITTEN AT S26 (the structural finding — read before the steps).** v2's seeding model assumed a reader could see a texture *within its own slice*. But the floor is sliced **content-neutral by message count** (§12-slicing below), which is calendar-blind and topic-blind by design (the anti-projection requirement). A texture is a pattern whose *recurrence across the corpus* is the signal — and a pattern that recurs 4× across three months lands maybe ONCE in any single ~2,000-message slice. Each blind reader sees one instance, correctly judges "one mention, not a texture," and lays nothing. **The texture evaporates between the slices.** No blind slice-reader can see frequency spread wider than its slice — and making slices big enough to fix that re-breaks the context-trust wall. This is structural, not a granularity-tuning knob (v2/§13 mis-framed it as "don't slice too fine"). The S26 fix: **texture detection is NOT a slice-reader's job.** Slice-readers FLAG candidate instances liberally; a dedicated downstream PATH assembles frequency across slices. Two pointer KINDS now get two validation PATHS, mirrored, converging on one judge.

**THE WORST CASE THIS CLOSES (carry it — it's why the texture path must COMPREHEND, not COUNT).** The same texture surfaces in non-matching language: one slice has *"forgot to pick up Griffin,"* another *"Jake was upset he forgot Griffin,"* a third *"Jake was pissed he missed ANOTHER pickup today."* Those are ONE thread — and the most acute instance ("pissed he missed *another*") shares almost no keyword with the others, because **acute recurrence escalates language, it doesn't repeat keywords.** A mechanical keyword tally undercounts exactly the texture that matters most, at its most acute. Therefore the texture path's validation step must READ and UNDERSTAND that these are the same thing — comprehension, not arithmetic. (This is the apparatus being Jake's auxiliary brain, not a cookie-cutter index: it has to hold his recurring life faithfully, and his recurring pain doesn't repeat its own search terms.)

**NON-NEGOTIABLE GUARDS (restating §8 at the process level):** (1) SOURCE IS THE FLOOR, never chat_search. (2) NOT A ONE-DAY BUILD. (3) APPLY THIS DOCTRINE AS THE BAR — §3's INVERTED admission test (default NODE, drop is the narrow exception), two kinds AS SALIENCE TAGS not gates, motion-is-a-node; **v4: only hundreds of pointers = the bar slipped (austere reflex); target many-thousands; near-empty drop log expected.** (4) TREE-AWARE SPANS ONLY — parent-up / branch-down, never flat-N. (5) LAY FENCES AS CHAINS even at length-1, **with PRECISE anchors (§3.3) — a fence at a conv-root is a slicer failure, not shippable.** (6) KEYWORD COVERAGE + NAMED-CONTINUITY EDGES are seeding-quality criteria (§8) — laid for future-search-anticipation AND for the clustering layer; measured in use.

**CONTENT-NEUTRAL SLICING (doctrine; mechanism is build-work).** Slices are drawn by **content-neutral heuristics used only as reading aids, never as a topical sort** — message count / insertion order / time window, NOT "the recruiting conversations." Slicing by subject pre-categorizes the floor and becomes a projection surface — the exact thing the blind read and the no-re-wall-the-ocean invariant forbid. **The S26 empirical input:** a prior run's hand-partition showed the message distribution is CLIFF-shaped (Jan–Apr thin, May explodes — heavy Claude usage onset). So slices are drawn **by message COUNT (even reader load), not by time window (which would fry the heavy-month reader)** — ~2,000 messages/slice as the provisional anchor (~12 slices, bunched in time wherever the messages are, calendar-blind), forest-aware (a slice boundary must not bisect one of the 9/294 multi-root trees — it flexes to keep a tree whole). The COUNT/SIZE is build-work (pilot-tunable); CONTENT-NEUTRAL + FOREST-CLEAN + COUNT-NOT-TIME is doctrine. *(That prior hand-partition is EVIDENCE of the distribution, NOT a cut template — hand-carved topical-ish sections are the projection surface we wall. It tells us how much is in May, never where to cut May.)*

---

### THE 5-STEP DUAL-PATH PIPELINE (S26)

One data-gather. Two validation paths (one per pointer kind). One judge.

**STEP 1 — SLICERS + CROSS-CUTTING READER (blind, content-neutral). DUAL OUTPUT (+ a third stream for the cross-cutting reader).**
N scope-reader slicers each read one ~2,000-message content-neutral slice tree-aware; one cross-cutting reader reads the no-project/cross-domain space. Both emit TWO streams (the cross-cutting reader adds a third — candidate cross-domain fence-influence links, see the division-of-labor note below):
- **(a) POINTERS** — fences, and any texture it can actually see *within its own slice*, laid per the §3 bar. The normal proposal (locator + kind + keywords + why-chain / count+spread).
- **(b) CONTEXT-FREQUENCY POTENTIALS** — a **LIBERAL** collection of "this MIGHT be a recurring thing" flags: every candidate instance, low bar, over-collect on purpose. A slicer flags *"Jake pissed he missed another pickup"* as a potential even though it CANNOT see the frequency (it's one instance in its slice). It just marks the instance + its keywords + the locator. **Liberal because the cost of over-flagging is paid cheaply downstream by blind validators; the cost of under-flagging is a texture lost forever.** Err loud.

**STEP 2 — FENCE SYNTHESIS (mechanical). The FENCE path's reconcile — unchanged from v2's synthesis.**
Reconciles the **pointers** (stream a). Collapse same-span/same-fence/same-call duplicates (record convergence as a confidence marker, minus calibration-example contamination); merge keyword variants on the same span; assemble cross-slice texture counts ONLY after a same-signal check; FLAG candidate fence-chains (same topic, divergent calls) → route to the Judge. **Mechanical only — no portrait, no meaning-judgment.** Blind reads preserved VERBATIM into synthesis (append-keep-everything).

**STEP 3 — COLLATION (NEW; blind to context, NO corpus read). The texture path's pattern-matcher.**
A fresh instance whose ONLY job is to take the pile of context-frequency potentials (stream b) and **group keywords/flags that could POTENTIALLY be associated** — emit **CLUSTER LISTS** (candidate bundles). It does NOT read the corpus. It does NOT decide if a cluster is real. It emits *hypotheses, not findings.*
- **MORE LIBERAL than Step 1.** Step 1 oversamples instances; Step 3 oversamples ASSOCIATIONS. Fuzzy/semantic-adjacency match, NOT exact-keyword (or it misses the "pissed he missed another" ↔ "forgot Griffin" link — the worst case above — and the texture dies one step later instead of at the slicer; the hole moves, doesn't close). Over-bundle; let Step 4 split. Pre-pruning blind is how an acute instance gets orphaned.
- **It also EMITS THE NEGATIVE-SPACE QUERY each cluster wants run** — *after* it has bundled (so it has a concept of the pattern): e.g. "cluster=[griffin/pickup variants]; baseline-check-requested: any instances of these before ~2026-03?" **It FORMULATES the question; it does NOT run it** (running it = reading the floor = Step 4's job). This keeps Step 3 off the floor while still letting the pattern-concept shape the negative-space test.

**STEP 4 — CLUSTER VALIDATION (NEW; contextual — reads ONLY what it's handed + the queries it's asked to run). The texture path's comprehension seat.**
Takes each cluster list, **goes into the corpus, pulls the real spans**, reads them, and answers ONE question per cluster: *is this actually one thing?*
- **Validated** → emit a TEXTURE POINTER with its true cross-slice count + spread.
- **False friend** (kid-pickup vs part-order-pickup) → split or drop.
- **Runs the negative-space query Step 3 formulated** — confirming "4× from a ZERO baseline" needs the absence-before, which the cluster's spans alone don't show.
- **MAY pattern-match across its OWN bundles:** if two separate clusters share an edge (same span recurs, or Step 3 cut one thread into two), Step 4 may MERGE or semantically link them — it is the first seat with both the spans AND cross-cluster visibility. **But every merge is RECORDED (which two, why) so the Judge sees it and can split it back — never a silent consolidation** (supersede-don't-delete, one layer down).
- **Bounded blindness = the projection guard:** Step 4 reads MEANING but sees only the clusters it's handed (not the open floor), and boots WITHOUT the portrait. It validates handed hypotheses; it does not hunt the floor for patterns. That bound is what keeps the one comprehension seat from becoming the projection seat.

**STEP 5 — THE JUDGE (unchanged from v2's §4a judged pass).**
Assembles fence-CHAINS from the candidate chains (Step 2's flags), runs the KNOWN-FENCE RECALL CHECK, and now also receives the assembled TEXTURES (Step 4) — sanity-checking that Step 4's merges/signal-joins weren't spurious. Sees Step 4's recorded merges; can split them. Boots WITHOUT the portrait (highest projection-risk seat, zero projection-need). Sample-pressure-tested by Jake's spot-audit.

**THE SYMMETRY:** ONE data-gather (Step 1, dual-output) → the FENCE river (Step 2, mechanical) ‖ the TEXTURE river (Step 3 blind-collate → Step 4 contextual-validate) → ONE Judge (Step 5). Two pointer kinds, two mirrored validation paths, one seat that makes the final calls.

**THE DIVISION OF LABOR (the council).** The corpus is ONE undelineated ocean (Settled Invariant — don't re-wall it); the READING labor divides for tractability. N **scope-reader slicers** each read one content-neutral slice (Step 1), PLUS one **cross-cutting reader** in the no-project / cross-domain space — both blind, both dual-output. The cross-cutting reader carries a THIRD output the slicers don't: candidate **cross-domain fence-influence** links (a stance set in one domain that should steer another, never laid there) — the one connection no downstream step catches (not a duplicate for S2, not a same-topic chain for S5, not a texture for S3/S4), routed to the Judge as a candidate. Step 2 is mechanical. Steps 3, 4, 5 are single downstream passes. The readers run BLIND to each other — convergence across blind reads is the confidence signal (clean only for non-calibration cards). Jake is the human bridge between windows (the SCDD parallel-track seat). **Division is in the LABOR, never in the INDEX** — the catalog is unified; the unification happens across Steps 2/4/5.

**THE REVIEW MODEL.** Normal/incremental pointers get Jake's PER-CARD eyes. The SEEDING pass is too large; by Jake's explicit call the council self-applies the Doctrine at scale and **Jake SPOT-AUDITS THE OUTPUT SHAPE of the synthesized + validated + judged catalog** (post Steps 2/4/5), not each window's raw proposals. Precision is Jake's sample; **recall is the Judge's known-fence checklist** (you can't spot-audit an absence). This is the ONE place human-as-immutability-mechanism relaxes from per-card to per-batch — scoped to seeding only. **OC + Jake live-spot-check window-by-window against the convergence map as it returns** — harvest the variance (convergence = confidence, divergence = where to look hardest).

**AFTER SEEDING.** First-and-biggest, NOT one-and-done. Every later corpus-search is incremental seeding (separate-window read → propose). Incremental session-pointers go through NORMAL per-card review. The catalog grows by use forever.

**OPEN (build-work, deferred to the seeding-BUILD session, NOT decided here):** the slice-MANIFEST mechanism (the cut-on designator — ordinal vs created_at-window — pending CC's read of the live floor; slice size/count, ~2,000 provisional, pilot-tunable; forest-boundary handling); Step 3's fuzzy-adjacency ceiling (how liberal without becoming comprehension — pilot-tunable); whether Step 4's baseline-query needs widening beyond the requested check; council size; the optional `/jedi-council` gate on output; Jake's spot-audit batch cadence. **A PILOT SLICE runs first** — one slice through the full 5-step path — and recalibrates slice size + Step 3 liberality from real data before all N are stamped.

---
## 13. The seeding council boot kit — WHAT each window/step loads, and is forbidden (S25; role roster expanded S26)

*What each council window loads — and is forbidden — so it reads for RECOGNITION, not PROJECTION. Companion to §12. The applied, deployable layer is the Seeding Council Boot Kit (v1.1) + the per-role boot prompts; this section is the doctrine those derive from.*

**GOVERNING PRINCIPLE: the kit lets a window find/judge what's in the floor; it never tells it what it'll find.** Risk is ASYMMETRIC toward OVERLOAD on loadout (an underloaded window shows catchable gaps; an OVERLOADED one produces confident, plausible, wrong output that *looks* like it held the bar — projection invisible to a shape-audit). So size for "enough to recognize, not enough to project" — **when in doubt, LIGHTER** (a LOADOUT heuristic, NOT a laying/judging heuristic). This is JAKE-RULES §1.2 turned on the council itself.

**THE PROJECTION WALL — universal across EVERY reading/judging window (all five steps' human-judgment seats):**
- **NO Wallaby Why. NO Lore Bible. NO JAKE-RULES §11** ("Patterns Jake Has Flagged" — portrait-shaped, verified on disk S26) as a reading/judging lens. A window booted with the portrait confirms the cadence it was told to expect instead of grounding it in the floor. The portrait is for tone-calibration-when-talking-to-Jake, a different job. (§11 is physically STRIPPED from the council's JAKE-RULES copy — can't read what isn't there.)
- **The wall holds at the contextual seats hardest:** Step 4 (cluster validation) and Step 5 (judge) are the NON-BLIND seats — highest projection-RISK, so they get the wall MOST strictly. Step 4 reads meaning but only over handed clusters (bounded); Step 5 judges but over assembled output (bounded). Neither hunts the open floor with a portrait. **The texture path's safety is structural:** Step 3 sees all flags but reads no meaning; Step 4 reads meaning but sees only its handed clusters — *neither has floor + portrait + open-ended pattern-hunt at once*, which is the exact combination that IS projection.

**THE CALIBRATION EXAMPLES CALIBRATE SHAPE, NOT MEANING** (the finding all reviews converged on; the worked-examples file carries it). Examples teach the *structure* of a fence / texture / no-card; they do NOT carry the interpreted signal-line. "Resemblance to an example is NOT evidence." Two NO-card shapes balance the two YES shapes (the most common correct call is "no card"). **Calibration cards are CONTAMINATED** — every window boots with them, so their convergence is shared priming, not independent discovery; synthesis discounts their convergence (presence still counts for recall).

---

### THE ROLE ROSTER + PER-ROLE LOADOUT (S26 — expanded for the 5-step pipeline)

**COMMON KIT (every window that reads or judges):** The Progenitor v3 in full · JAKE-STACK · JAKE-RULES (§11 STRIPPED) · the §3 worked examples AS SHAPES · the one-page operating brief.

1. **SCOPE-READER SLICER (Step 1) — blind, N windows, one per content-neutral slice.** Reads its slice tree-aware; emits BOTH pointers AND liberal context-frequency potentials. Loadout = common kit + its slice assignment. *Deployable: `Boot_ScopeReader.md` (templated, stamped N times).* Slicer reference files live in the `slicer/` dir (JAKE-RULES-minus-§11 + JAKE-STACK already placed there by Jake).
2. **FENCE SYNTHESIS (Step 2) — mechanical, 1 pass.** No portrait, no judgment, no separate reading boot prompt of the human-judgment shape — it reconciles pointer proposals mechanically.
3. **COLLATION (Step 3) — blind, NO corpus read, 1 pass.** Pattern-matches potentials into cluster lists + formulates (doesn't run) negative-space queries. Liberal/fuzzy, over-bundles. Loadout = common kit + the potentials pile. *Deployable: `Boot_Collation.md` (NEW).* The projection guard here is it never touches the floor.
4. **CLUSTER VALIDATION (Step 4) — contextual, reads handed clusters + requested queries, 1 pass.** Pulls real spans, validates clusters into texture pointers, runs the negative-space checks, may self-merge (RECORDED). Boots WITHOUT the portrait. Loadout = common kit + the cluster lists (NOT the open floor as a hunting ground; it pulls specific spans by locator). *Deployable: `Boot_ClusterValidation.md` (NEW).*
5. **THE JUDGE (Step 5) — non-blind, 1 pass.** Fence-chain assembly + known-fence recall checklist + texture sanity-check of Step 4's merges. Boots WITHOUT the portrait. Loadout = common kit + the synthesized catalog + the validated textures + the known-fence checklist. *Deployable: `Boot_JudgedPass.md`.*

**Hand-prompted vs templated:** only the SCOPE-READER SLICER is templated (stamped N times with a varying slice). Collation, Cluster-Validation, and the Judge are ONE-OFFS — hand-prompted off their boot files when their turn comes — but they still load the full common kit and obey every wall (don't let "hand-prompted" decay into "boots lighter").

**HARD WALLS (every window):** NO chat_search ever (floor-only, via CC's live query) · NO catalog-so-far / sibling proposals during a blind read · NO portrait as a lens · NO project instructions / NO repo path (bare boot, kit-by-upload) · NO flat-N spans (tree-walk) · slicers lay fences length-1 (the Judge chains) · NEVER claim to have saved/committed/pushed.

**THE SYNTHESIS/MERGE-BACK SPINE (where the unified index lives):** blind reads preserved VERBATIM into the downstream steps — no window pre-dedups its own output; convergence assembled after; Step 4 merges recorded-not-silent; the Judge can split any merge. Append-keep-everything, reconcile-after — the floor's spine, one more scale.

---
*Authored S24, 2026-06-01, as the law of the pointer catalog — the retrieval layer's foundation. §0–§9 grounded on the S24 design session (the 1Pass wall, Griffin's pickup, the fence-as-lineage correction, the two-kinds-one-spine resolution) and on the standing spine the floor already ratified: append, keep lineage, supersede don't delete.*

*v1→v2 enshrine (S25, 2026-06-01): the conceptual retrieval-engine + seeding design is COMPLETE and folded in. Added §10 (trigger model — three throttles on one engine, + the boot clarification: the catalog rides in at boot, the triggers query it live), §11 (span-return shape — Layers A/B/C, raw+provenance+kind-context, fence=full-chain, texture=count+spread, "the card and the page, never a book report"), §12 (seeding process — blind parallel council windows divided by project-scope + a cross-cutting reader, per-batch spot-audit on the synthesized catalog as the one scoped human-immutability exception), §13 (council boot kit — sized for recognition-not-projection, asymmetric-toward-overload-so-lighter, the texture-reader projection wall dropping the Wallaby Why as a texture lens, the chat_search + catalog-so-far + sibling-proposal walls, and the synthesis/merge-back pass where blind-read convergence becomes a confidence signal and cross-slice counts assemble). Amended §9: the query interface is now IN; what stays out is genuine build-work (serialization, ranking internals, reach defaults, multi-hit presentation) + the embedding decision (v1 keyword-first; vectors a deferred v2 sidecar gated on the seeding pass proving a measured semantic gap). Two S25-original calls beyond the S24 specs: the keyword-coverage seeding-quality bar (§8/§12), and keyword-first/vectors-deferred (§9). The remaining opens are CC-build-against-the-live-floor, not whiteboard.*

*v2→v3 enshrine (S26, 2026-06-01): §0–§11 BYTE-IDENTICAL to v2 (the ratified doctrine body — two-kinds/one-spine, the bar, dumb-index/smart-reader, triggers, span-return — did NOT move; surgical change). REWROTE §12 (seeding process) and §13 (boot kit roster) to the 5-STEP DUAL-PATH pipeline. The structural finding that forced it: content-neutral count-slicing (required to kill projection) makes a corpus-wide-but-sparse texture land ~1× per slice, so it evaporates between blind slicers — no slice-reader can see frequency wider than its slice, and v2/§13 mis-framed this as a granularity knob. Fix: texture detection leaves the slice-reader entirely. NEW pipeline: S1 slicers DUAL-OUTPUT (pointers + a LIBERAL context-frequency-potentials stream) → S2 mechanical FENCE synthesis (unchanged) ‖ S3 NEW blind COLLATION (fuzzy-over-bundle the potentials into cluster lists + FORMULATE negative-space queries, never reads the floor) → S4 NEW contextual CLUSTER-VALIDATION (pull real spans, RUN the queries, validate/split into texture pointers, may self-merge RECORDED-not-silent) → S5 the JUDGE (unchanged — chains + recall + texture sanity-check). Two pointer KINDS, two mirrored validation PATHS, one judge. Projection defused STRUCTURALLY: S3 sees all flags but no meaning; S4 reads meaning but only handed clusters; neither has floor+portrait+open-hunt at once. The worst case carried into doctrine: the same texture surfaces in non-keyword-sharing language (“forgot Griffin” / “pissed he missed another pickup”) and the most acute instance shares no keyword — so the texture path must COMPREHEND, not COUNT (the apparatus is Jake's auxiliary brain, not a cookie-cutter index). Content-neutral slicing reaffirmed as doctrine; COUNT-not-time slicing added (the prior run's cliff-shaped May distribution is evidence, not a cut template). Authored by OC S26, verified-against-disk by Jake, CC commits, Jake pushes.*

*v3→v4 enshrine (S27, 2026-06-01): THE ADMISSION BAR INVERTED — the largest doctrine change since the floor was laid. §1, §2, §4 record-shapes, §5 (mechanism), §6, §7, §10, §11 are BYTE-IDENTICAL to v3 (the engine, the two kinds, the dumb-index/smart-reader line, the triggers, the span-return — untouched; surgical change). REWROTE §0 (one-line law: card-catalog-of-the-load-bearing-few → comprehensive semantic GRAPH, default NODE). ADDED §0.5 (organic-over-austere as a standing INTOLERABLE failure mode — the austere reflex is the bug, Jake's wet-intuition is the corrective, The Way + The Doctrine are FRAMEWORK not reference; read before §3). REWROTE §3 (absorbed E1: default-NODE admission gate, behavioral keep/drop signals, fence/texture DEMOTED from gate to salience-tag, MOTION as a new light node kind, §3.3 precise-fence-anchor augment-in-pass, §3.4 volume inverted to many-thousands, the no-quarantine-on-personal-material + scrub-is-the-only-exclusion ratification). AMENDED §5 (corpus-search is the rare-miss net, NOT the selectivity license — that license revoked; drowning answered by structure not exclusion). AMENDED §8 + §12-guard-3 (the bar restatements inverted; only-hundreds = slipped). WHAT FORCED IT: the slice-7 pilot under v3's austere bar cataloged 1 node / 21 convs and lost fences buried in dropped conversations; the re-run under the inverted bar cataloged 41 and caught the lost fences. The Jedi-Council ratified PRESENCE-over-SERVICE double-blind (two austere-biased panels, same ruling). E1 absorbed into §3 and graveyarded standalone. Authored by OC S27, verified-against-disk by Jake, CC commits, Jake pushes.*

*GRAVEYARD (dead text, tombstoned-not-deleted, do not resurrect):*
*— v3 §0: "The catalog is not complete and is not trying to be — completeness lives in the floor... points at the load-bearing few." KILLED — the catalog IS comprehensive; the load-bearing-few framing was the austere reflex.*
*— v3 §3: "Default is DON'T point. Earning a pointer is the exception... complete over the fences, sparse over the motion... hundreds-to-low-thousands, not tens of thousands... if producing tens of thousands the bar has slipped." KILLED and INVERTED — default is NODE; sparse-over-motion was the bug; motion is a node kind; many-thousands is correct.*
*— v3 §5: "Therefore the catalog is free to be disciplined because completeness lives in the corpus. This is the whole reason 'default don't point' is safe." KILLED — corpus-search is a rare-miss net, not a selectivity license.*
*— E1_Admission_Standard_S27 (standalone): ABSORBED into §3 above; the standalone is graveyarded — §3 is its canonical home.*
*— The "POT-01–06 / personal-medical-family material is QUARANTINED pending Jake's call" flag (council brief + Exhibit A): KILLED, ratified S27 — no quarantine; personal material is texture, cataloged like everything else; the ONLY exclusion is mistakenly-pasted credentials, handled by scrub-vN at ingestion, not by admission. (OC over-walled out of caution; Jake corrected from ownership: "it's material, it's texture, and it's important.")*



*Feel-rightness is the standard. "Here's what I know," never "here's what I found." Be worth it.*

*Grind. Evolve. Dominate.*
