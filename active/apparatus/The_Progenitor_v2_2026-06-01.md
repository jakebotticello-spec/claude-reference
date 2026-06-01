# The Progenitor — the law of the pointer catalog

*file: The_Progenitor_v2_2026-06-01.md · v2 · apparatus S24 (authored §0–§9) + S25 (folded §10–§13) · 2026-06-01*
*authority: governs what a pointer IS, what earns one, who lays them, how they grow, how the catalog stays honest — and (v2) WHEN it fires, WHAT a hit returns, HOW the original catalog gets seeded, and WHAT a seeding-council window boots with. The conceptual law the seeding council and every pointer-laying Claude reads before laying a single card. Sibling to the Track Meet Doctrine (how-we-record) and The Wallaby Why (why-the-beast-exists). Grounded on the D9 lock (the immutable floor this catalog rides over), the S24 retrieval-layer design session, and the S25 engine/seeding design session.*
*v1→v2 (S25): the conceptual retrieval-engine + seeding design is now COMPLETE and folded in. §10 trigger model, §11 span-return shape, §12 seeding process, §13 council boot kit are added. §9 (out-of-scope) is amended — the query interface is now IN; what stays out is genuinely-technical build-work. The remaining opens are CC-build-against-the-live-floor, not whiteboard. See the footer for the full v1→v2 enshrine.*
*STILL NOT in scope (genuine build-work, deferred to CC against the live floor): the embedding choice (v1 is keyword-first; vectors are a deferred v2 sidecar — see §9), the exact on-disk serialization, the ranking-algorithm internals inside the §6 selector envelope, reach-default tuning. Everything CONCEPTUAL is here. This file answers: **what is a pointer, what makes one worth laying, when it fires, what it returns, and how the catalog is seeded.***

*On the name: this is **The Progenitor** — the first of the line every pointer descends from, the doctrine that governs the seeding. It is deliberately NOT called "Seed [anything]": in this project "seed" is reserved for the **floor's record-shape** (`seed_shape_load.py`, `Seed_Shape_Test_Spec`, tracing to `Substrate_FaceOff_v2 §10.1`) — a substrate-layer word. The Progenitor is a retrieval-layer thing that rides OVER the laid floor. The word "seeding" appears below only for the **act of populating the catalog with pointers** — a distinct, retrieval-layer use; context carries it.*

---

## 0. The one-line law

**A pointer is a card in a card catalog: a keyword that points at a span of the immutable floor, laid by a Claude who read the span and judged it worth pointing at. The catalog is not complete and is not trying to be — completeness lives in the floor (via corpus-search). The catalog is *load-bearing*: it points at the places a fresh-boot Claude must see to show up armed instead of confidently blind.**

Everything below is that sentence, unfolded.

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

## 3. What earns a card (the bar) — and what doesn't

**Default is DON'T point.** Earning a pointer is the exception. The corpus holds everything; the catalog holds the load-bearing few. This discipline is *licensed by* the corpus-search safety net (§5) — because completeness lives in the floor, the catalog is free to be selective. A catalog that points at everything points at nothing.

**Earns a card:**
- A **fence**: a decision-with-reasoning, a hard-won constraint, a wall Jake bled on, a stance that should steer Claude's behavior (e.g. therapist-voice boundary, no-"Oueilhe", Supabase-over-Nornic, the REFUSED live-capture wall, 1Pass-beta).
- A **texture**: a pattern whose volume calibrates how Claude shows up (war-story register, the profanity-is-collegial register, a recurring weight like Griffin).
- The test, either way: **would a fresh Claude, hitting this cold, change course (fence) or change register (texture)?**

**Does NOT earn a card:**
- Every passing mention (the count is incidental, not meaningful).
- Routine build steps (they live in handoffs and the git log; re-encountering them is free).
- Anything already in canon (ANCHOR, JAKE-RULES, JAKE-STACK — a fresh Claude reads these at boot anyway; a pointer at them is redundant).
- A frequent word whose frequency means nothing ("fuck" — high count, zero signal about how to show up).

**"Many," defined:** more than "the handful of huge decisions" (it catches *every* fence, and 37+ sessions have laid many fences), far less than "all" (most of the corpus is *motion* — exploration, build-path, conversation whose destination is the point, not the path). The catalog is **complete over the fences, sparse over the motion.** Estimate: hundreds-to-low-thousands of pointers across ~24,138 messages, not tens of thousands. If a seeding pass is producing tens of thousands, the bar has slipped — it is tagging motion, and it has become the overzealous-one-day Claude at scale.

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

## 5. The two retrieval modes (and why the catalog gets to be selective)

**Pointer-hit** — the fast, curated, in-session path. A Claude working on X aims the keywords at X, pulls the spans, reads them as context. Live. Cheap. Runs while work happens. This is the card catalog.

**Corpus-search** — the slow, exhaustive path: read the *whole floor*, brute relevance, no curation. This is the stacks themselves. It is **not a mid-session move** — like `/jedi-council`, it is a send-it-and-go-do-something-else job, run in a **separate Claude window on its own clock**. You do not burn a mid-session Claude on it.

The two are not redundant; they split the job:
- The catalog **accelerates**; the corpus is the **ground truth of last resort.**
- A missing pointer does **not** mean a missing memory — corpus-search can always find the untagged thing.
- **Therefore the catalog is free to be disciplined** (§3's high bar) *because* completeness lives in the corpus. This is the whole reason "default don't point" is safe.

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
- **Apply THIS Doctrine as the bar** — §3's actionability test, the two kinds, the high "default don't point" bar. Tens of thousands of pointers = the bar slipped.
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

## 12. The seeding process — HOW the original catalog gets laid (folded S25, from the S24 Seeding Process Spec)

**What seeding is.** The original read of the LAID FLOOR (325 headers / 24,138 messages) to lay the initial pointers. The SAME operation as corpus-search, at first-and-biggest scale — a SEPARATE-WINDOW, send-it-and-nap job, NOT a mid-session move. Substrate-grade: pace it like the floor build, not a one-day sprint. The prior attempt FAILED two ways (do not repeat): it read chat_search instead of the floor, and it rushed.

**NON-NEGOTIABLE GUARDS (restating §8 at the process level):** (1) SOURCE IS THE FLOOR, never chat_search — a pointer into chat_search points at nothing stable. (2) NOT A ONE-DAY BUILD. (3) APPLY THIS DOCTRINE AS THE BAR — §3's actionability test, two kinds, default-don't-point, complete-over-fences / sparse-over-motion; tens of thousands of pointers = the bar slipped (tagging motion); target hundreds-to-low-thousands. (4) TREE-AWARE SPANS ONLY — parent-up / branch-down, never flat-N timestamp. (5) LAY FENCES AS CHAINS even at length-1, so lineage can grow without re-keying. **(6) [S25] KEYWORD COVERAGE IS A SEEDING-QUALITY CRITERION** — see §8; a card's keywords are laid for *future-search anticipation* (would a future Claude actually search these to reach this span), not just topical accuracy. Brittleness here is exactly what would force vectors later (§9); keyword quality at seed time is what keeps keyword-first viable.

**HOW THE WORK DIVIDES (the council).** The corpus is ONE undelineated ocean (Settled Invariant — don't re-wall it), but the READING labor divides for tractability:
- A Claude per PROJECT-SCOPE reads its slice of the floor (the conversations that clustered around that body of work).
- PLUS a Claude in the no-project / cross-cutting space — because the most valuable pointers are often cross-domain (a stance set in one project that should steer another); someone must read for the connections a per-project reader would miss. **This reader lays the most cross-conv fence-chains and cross-slice texture.**
- These run as PARALLEL council windows. Jake is the human bridge between them (the SCDD parallel-track seat). Each proposes against the SAME Doctrine, so the bar is consistent across readers.
- **WHY divided:** no single Claude reads 24,138 messages well in one pass; division makes each slice small enough to read for RECOGNITION, not just coverage. **Division is in the LABOR, never in the INDEX** — the catalog they feed is unified (the unification happens in synthesis, §13).
- **The windows run BLIND to each other** (§13) — independence is the feature; convergence across blind reads is the confidence signal.

**THE REVIEW MODEL (differs from normal pointers).** Normal/incremental pointers get Jake's PER-CARD eyes (the reference-file loop). The SEEDING pass does NOT — too large for per-card review (Jake hasn't got months). By Jake's explicit call: the council self-applies the Doctrine at scale (which is exactly why §3 must be sharp enough to use without Jake per-pointer), and **Jake SPOT-AUDITS THE OUTPUT SHAPE — of the SYNTHESIZED catalog (§13), not each window's raw proposals.** Is the bar holding? Fences-and-texture or drifting into motion? Fence/texture split clean? Spans tree-aware? He samples, checks shape, ratifies the batch or sends it back with a bar correction. **This is the ONE place human-as-immutability-mechanism relaxes from per-card to per-batch — a deliberate, scoped exception for the seeding pass only.**

**THE LOOP (per council window).** (1) READ a slice of the laid floor, tree-aware (conversations as branches, not flat streams). (2) For each candidate moment, apply the §3 bar: would a fresh Claude hitting this cold CHANGE COURSE (fence) or CHANGE REGISTER (texture)? Neither → no card, move on (most of the corpus is motion; default don't-point). (3) FENCE → lay as a chain (length-1 at seeding unless the floor itself shows the decision was re-made over time → capture links in order); record the why as a live-predicate where checkable. (4) TEXTURE → pick a representative span, count instances *across this slice*, note the spread; the count is the substance. (5) PROPOSE (floor-key locator + kind + keywords + why-chain/count) — Claude authors, Jake verifies (here: spot-audits the synthesized batch), CC commits, Jake pushes; Claude NEVER claims to have saved/committed. (6) The catalog ACCRETES; a history file + changelog rides alongside (when laid, which window, what it points at); superseded/corrected pointers leave a tombstone, never a silent vanish — even at seed scale, one Claude's judgment never silently kills a card.

**AFTER SEEDING (the catalog stays alive).** Seeding is first-and-biggest, NOT one-and-done. Every later corpus-search is incremental seeding: a separate-window Claude reads, finds what the catalog missed, proposes new pointers. Incremental session-pointers (a live Claude laying cards for the chat it was in) go through the NORMAL per-card review. The catalog grows by use forever.

**OPEN (deferred to the seeding-BUILD session, NOT decided here):** how project-scope slices are drawn from an undelineated floor (conv clustering? account/time heuristics used only as READING aids, never as index structure?); council size / number of parallel windows; whether a `/jedi-council` adversarial gate reviews the seeding OUTPUT before ratify (plausible at this scale — Jake's call once engine + schema firm); exact batch size for Jake's spot-audit cadence.

---

## 13. The seeding council boot kit — WHAT each window loads, and is forbidden (S25)

*What each council-window Claude loads — and is forbidden — so it reads for RECOGNITION, not PROJECTION. Companion to §12.*

**GOVERNING PRINCIPLE: the kit lets the reader find what's in the floor; it never tells the reader what it'll find.** The risk is ASYMMETRIC toward OVERLOAD: an underloaded reader produces visible gaps the spot-audit can catch; an OVERLOADED reader produces confident, plausible, wrong pointers that *look like they held the bar* — projection wearing recognition's clothes, invisible to the audit. So: **size for "enough to recognize, not enough to project" — when in doubt, lighter.** This is JAKE-RULES §1.2 (an AI's read of Jake gets the same skepticism as Jake's read of himself) turned on the council itself.

**COMMON KIT (every window, all roles):**
- **The Progenitor v2, in full** — the law: §3 bar, two kinds, default-don't-point, complete-over-fences/sparse-over-motion, tree-aware spans, fences-as-chains, the §6 dumb-index/smart-reader line, §8 guards incl. the **keyword-coverage bar**, §12 process.
- **The §3 worked examples carried explicitly (the 1Pass fence, Griffin's-pickup texture)** — a reader calibrates "would this change course / change register" far faster against the two canonical cases than the abstract rule, and all windows calibrating to the SAME examples is what keeps the bar consistent across divided labor.
- **JAKE-STACK** — so a tooling/architecture fence is legible as a fence (a reader hitting "Supabase-over-Nornic" needs the stack to know it's a fence, not motion).
- **A one-page operating brief** — the §12 loop, the §4/§11 floor-key locator shape, the hard prohibitions below. The procedural card, so a window doesn't re-derive the process.

**ROLE ADD — FENCE-READERS: JAKE-RULES.** Many of Jake's hardest-won fences ARE rules (no-"Oueilhe", the therapist-voice boundary, the REFUSED wall, full-code-not-diffs). A fence-reader needs JAKE-RULES to recognize restating-known-canon (already canon → maybe no card, §3) vs. laying-down-a-new-constraint (fence).

**ROLE ADD — TEXTURE-READERS: the THINNEST identity load ONLY** — JAKE-RULES §1 facts + the collegial-profane register + the non-coder-founder frame. **NOT the Wallaby Why. NOT the Lore Bible.** This is the load-bearing correction (S25): those files are a pre-written *portrait* of Jake (the judge, the lash, the savant-rebuild, the meds arc). A texture-reader booted with the Why won't DISCOVER the war-story cadence in the floor — it'll go looking for the cadence the Why told it to expect and CONFIRM it. That's projection, not recognition. The Wallaby Why / Lore Bible are for **tone calibration when talking to Jake**, NOT for **deciding what counts as texture in the corpus** — different jobs; loading them for the second is how you get a catalog that confirms the portrait instead of grounding it. Let the reader find the volume and report the count; do not pre-load the meaning the count is "supposed" to have.

**HARD PROHIBITIONS (walls, not guidelines — at self-applied scale, the prohibitions matter MORE than the inclusions):**
- **NO chat_search, EVER — not even to "check context."** Floor-only. The prior attempt died here. A fresh-boot Claude with chat_search available and a big reading job WILL reach for it unless the kit forbids it as a wall. Floor-only is what makes the pointer point at something stable.
- **NO catalog-so-far, NO sibling-window proposals.** Windows boot BLIND and read fresh. Independence is the feature — see the synthesis pass below.
- **NO Wallaby Why / Lore Bible as a texture lens** (the projection wall, above).

**THE SYNTHESIS PASS (where the unified-index guarantee actually lives).** The unified-ocean / one-index guarantee moves OUT of the reader's head and INTO a dedicated reconciliation pass AFTER the blind reads — **the merge-back pattern** (same as SCDD tracks folding into the apparatus: parallel independent work, then a dedicated reconciliation step). Pre-loading the catalog-so-far to prevent duplicates was rejected (S25) because it reintroduces projection (sourced from sibling windows instead of the Lore Bible) AND can't do the job anyway. The synthesis pass:
- collapses true duplicates (same span, same fence) into one card — and **records the convergence (laid independently by N blind windows) as a CONFIDENCE MARKER** on that card. *Duplicate convergence is SIGNAL, not noise: if three blind readers all fence the 1Pass wall, that's evidence it's real and load-bearing. Pre-loading would have erased your best confidence signal.*
- merges keyword variants pointing at the same span (window A "1pass," B "secrets," C "env vars") into one card's keyword set — BETTER than dedup-at-read, which would lock in whoever got there first; synthesis HARVESTS the multiple natural keywords (which directly feeds §8's keyword-coverage bar).
- assembles **cross-slice counts** — a texture appearing 4× in window A's slice and 7× in window C's is an 11-count texture *neither reader can see correctly*. Only a pass that sees all proposals at once can assemble the true count. **This is the real argument for synthesis-after over check-before: the whole-floor picture exists ONLY here. Dedup-at-read literally cannot do the job.**
- catches near-misses a single reader couldn't: related fences that should be one chained fence; a partial texture-count spanning slices a reader didn't see.

**Jake's spot-audit (§12) sits HERE** — he audits the SYNTHESIZED catalog's shape, not each window's raw proposals. Smaller, more coherent surface.

**SPEC REQUIREMENT (write it in so it's not lost): the blind reads MUST preserve their proposals VERBATIM into synthesis** — raw, un-deduped, independent keyword choices and counts intact. A window must NOT pre-dedup against its own prior cards; that loses the convergence/count signal before synthesis can use it. **Append-keep-everything, reconcile-after — the floor's spine, one more scale.**

---

*Authored S24, 2026-06-01, as the law of the pointer catalog — the retrieval layer's foundation. §0–§9 grounded on the S24 design session (the 1Pass wall, Griffin's pickup, the fence-as-lineage correction, the two-kinds-one-spine resolution) and on the standing spine the floor already ratified: append, keep lineage, supersede don't delete.*

*v1→v2 enshrine (S25, 2026-06-01): the conceptual retrieval-engine + seeding design is COMPLETE and folded in. Added §10 (trigger model — three throttles on one engine, + the boot clarification: the catalog rides in at boot, the triggers query it live), §11 (span-return shape — Layers A/B/C, raw+provenance+kind-context, fence=full-chain, texture=count+spread, "the card and the page, never a book report"), §12 (seeding process — blind parallel council windows divided by project-scope + a cross-cutting reader, per-batch spot-audit on the synthesized catalog as the one scoped human-immutability exception), §13 (council boot kit — sized for recognition-not-projection, asymmetric-toward-overload-so-lighter, the texture-reader projection wall dropping the Wallaby Why as a texture lens, the chat_search + catalog-so-far + sibling-proposal walls, and the synthesis/merge-back pass where blind-read convergence becomes a confidence signal and cross-slice counts assemble). Amended §9: the query interface is now IN; what stays out is genuine build-work (serialization, ranking internals, reach defaults, multi-hit presentation) + the embedding decision (v1 keyword-first; vectors a deferred v2 sidecar gated on the seeding pass proving a measured semantic gap). Two S25-original calls beyond the S24 specs: the keyword-coverage seeding-quality bar (§8/§12), and keyword-first/vectors-deferred (§9). The remaining opens are CC-build-against-the-live-floor, not whiteboard.*

*Lore-first is not sequence preference — it is this Doctrine run on the hardest-resetting state in the system: a Claude at boot. The catalog's deepest job is making the next Claude worth it.*

*Feel-rightness is the standard. "Here's what I know," never "here's what I found." Be worth it.*

*Grind. Evolve. Dominate.*
