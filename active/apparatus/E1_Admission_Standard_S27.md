# E1 — The Admission Standard (comprehensive-graph rewrite of The Progenitor §3)
*authored S27, 2026-06-01, by OC · answers Jedi-Council Escalation 1 (the most urgent — gates the next slice) · DRAFT for Jake's verify, then council-or-ratify before it reaches a reader · supersedes the §3 "default is DON'T point" bar; does NOT touch the two kinds, the spine, the locator, the tree-walk, or the no-portrait wall*

---

## 0. The inversion (the one-line law, rewritten)

**Old §3:** *"Default is DON'T point. Earning a pointer is the exception. A catalog that points at everything points at nothing."*

**New:** **Default is NODE. Dropping a conversation from the catalog is the narrow exception. A catalog that points at the load-bearing-few hides the rest in a floor only a separate-window nap-job can reach — which during a live session is confident blindness, not arming.**

The catalog is a **comprehensive semantic graph over the corpus**, not a curated list of decisions. Most conversations produce nodes. The pattern-sense (per the Wallaby Why: the faculty the rewire left intact) can only run across the surface the catalog makes accessible in-session — so the catalog's job is to **make the surface broad and navigable,** not to pre-judge which parts of Jake's recorded life are worth keeping reachable.

---

## 1. The asymmetry that licenses the inversion (Jake's bar, verbatim spirit)

> *"What's the worst that happens here? Claude reads 2x the context material when he calls a flag. Oh noes, not more context."*

This is the foundation. The old law treated a pointer as **expensive** — every extra card was noise that pushed relevance-judgment onto the runtime reader, so the bar was high and exclusion was the discipline. The new law recognizes the true cost structure:

- **Over-including a node is cheap.** Worst case: a keyword resolves to a node that turns out marginal, and a reading-Claude spends a little extra context reading it before moving on. Recoverable in-session, costs seconds.
- **Omitting a node is expensive and invisible.** The context exists in the floor but is unreachable through the catalog during a live session. The cost is paid as a *felt gap in daily use* — "I know we worked on the VESA mount, why can't Claude find it" — and it is paid silently, with no shape in the catalog to even reveal the miss. (This is the same structural blindness the Judge's recall-check exists to catch: you cannot spot-audit an absence.)

Asymmetric costs demand an asymmetric default. **When unsure, NODE it.** The reading-Claude's intelligence (Progenitor §6 — the smart reader, dumb index) sorts marginal nodes at read-time cheaply; the catalog's job is to never make a real thing unreachable. Doubt resolves toward inclusion, always.

---

## 2. The new bar — default NODE, with two questions

For each conversation (and each substantial span within it), the reader asks, in order:

**Question 1 — the DROP gate (the only way out of the catalog):**
> *Is this genuinely ephemeral — zero project continuity, zero recurring element, zero decision, nothing a future Claude might ever want to land near?*

If **yes → DROP** (no node). If **no, or unsure → NODE it.** Drop is the narrow exception, and "unsure" is not a drop — unsure is a node, per §1.

**Question 2 — for everything that gets a node, CLASSIFY salience (this is where fence/texture move to):**
The fence/texture machinery is **retained and demoted from admission-gate to in-graph classification.** A node is tagged by what it is:
- **FENCE** — a decision/constraint with a why; high salience; carries the lineage chain + live-predicate (unchanged from §2.1). The VESA-mount session's *final mount-dimension decision* is a fence-tagged node.
- **TEXTURE** — a pattern whose volume is the signal; salience scales with count/spread (unchanged from §2.2).
- **MOTION** — *and this is the new node kind* — a light, low-salience node that points at a span worth being able to reach but carrying no decision or recurring-volume signal. The VESA-mount *design exploration*, the NAS-build *steps*, the consulting-estimate *reasoning*: these become **motion nodes** — present, reachable, connectable, low-salience. "Motion" is now a **descriptive tag, not a discard criterion.**

A node can be more than one (fence+texture overlap survives, per §2.2). The point: **classification happens *after* admission, and admission defaults to yes.**

---

## 3. The behavioral signals (how a reader detects "not ephemeral" cheaply)

The reader does not have to *judge importance* to admit a node — judging importance was the old high-bar trap. It detects **substance behaviorally**, from floor-observable signals that don't require interpretation:

**Signals that the conversation has substance → NODE (any one is sufficient):**
- **Multi-turn exchange.** More than one back-and-forth on the topic. *(This is the strongest single signal — a sustained exchange is the floor's own evidence that something had enough substance to carry back-and-forth. It answers "is there texture here" better than any content judgment.)*
- **A fork** — the response was stopped and redirected, or the conversation branched. A fork is a live course-correction; almost definitionally node-worthy.
- **Named continuity** — a project, person, place, tool, or recurring thread appears (Pyris, CCF, Jim Donio, the P1S, a venue). Names are edges waiting to connect; a named thing is a node.
- **A decision or constraint** — anything that would tag FENCE.
- **A made thing** — code, a design, a document, an artifact produced in the conversation.

**Signals that it is genuinely ephemeral → DROP (needs essentially all to be true):**
- **Made-in-error** — an orphaned keystroke, a misfire, a wrong-window paste (Jake's stray "v"). The one clean drop.
- **Single-turn AND no named continuity AND no decision AND nothing made** — a true throwaway with no thread anything could connect to.

Note the asymmetry encoded in the structure: **any one** keep-signal admits a node; a drop requires **essentially all** ephemeral-signals at once. That is the cheap-pointer/expensive-omission asymmetry made operational.

---

## 4. Worked calibration set — Exhibit A's casualties, rebuilt under the new bar

*These teach SHAPE, like the §3 examples. The point is to show what the 14 old "no-cards" become — almost all become nodes, most as motion-tagged, a few carrying fences or textures inside them. Resemblance to an example is not evidence; calibrate to the shape of the call.*

| Conv | Old call | New call | Why |
|---|---|---|---|
| a4233320 — 3D-printing VESA mount (202 msgs) | NO-CARD "maker motion" | **NODE — motion-tagged, with a FENCE inside** | 202 messages, multi-turn, a thing designed. The exploration is a motion node (reachable: "the mount design lives here"); the final dimension/clearance *decision* is a fence-tagged node. Named continuity: the under-desk PC-case project. Edges to the maker cluster. |
| 8eb8ef22 — NAS backup build (340 msgs) | NO-CARD "operational motion" | **NODE — motion-tagged** | 340 msgs, multi-turn, a system built (DS218J SMB target, robocopy, Task Scheduler). Reachable operational context; connects to the homelab cluster. Light salience, real reachability. |
| 445bb9c1 / 86aa947a / 28b26b87 — Pyris S12–S14 build arc | NO-CARD "build motion" | **NODE — motion-tagged, fences + textures inside** | The build arc is exactly the "recurring life held" the Wallaby Why names. Motion nodes for the build paths; FENCE-01 (the Supabase pooler) already lives here; POT-08/09/11/14 textures thread through. Dropping these hid the spine of two months of work. |
| 39d07512 — Green Project consulting estimate | NO-CARD "consulting motion" | **NODE — motion-tagged** | Named continuity (a real prospect/engagement), multi-turn, decision-flavored reasoning. Reachable: "what did we scope for Green Project." |
| 51c699e5 — ice-maker shopping (12 msgs) | NO-CARD "consumer motion" | **NODE — light motion, low salience** (borderline, but node) | Multi-turn (12 msgs, back-and-forth on specs/budget). Under the new bar, multi-turn alone admits it. Very low salience, minimal metadata, few edges — but reachable. The cost of including it is ~nothing (§1); the cost of a future "didn't we look at ice makers" miss is a felt gap. NODE. |
| 56927959 — SVG housewarming card | NO-CARD "motion" | **NODE — light motion** | A thing made. Reachable; connects to the design/SVG cluster. Low salience. |
| 1442a717 — Hamilton station check-in | NO-CARD "motion" | **NODE — light motion** | Contains a real hard-stop reference (the quarantined Ary cluster aside, the *session-shape* is reachable context). Node. |
| (hypothetical) Jake's stray "v" | — | **DROP** | Single keystroke, made-in-error, zero continuity, nothing made, single-"turn." The clean drop. This is what the exception is *for.* |

**The pattern the set teaches:** under the new bar, the drop column is nearly empty. Of slice 7's 21 conversations, the new law nodes ~20 and drops ~0–1 (only true misfires). What *changes* between conversations is not in/out — it's **salience and edge-density:** the Pyris arc is high-salience and richly connected; the ice-maker chat is a light node hanging off the consumer-research cluster with two edges and minimal metadata. Both are reachable. That is the comprehensive graph.

---

## 5. What "light node" means (answering E2's interim-fidelity question)

Per Jake's D-2 call: **"light" does not mean ineffective — it means a more complicated design is coming, and that's true.** A base-strata node, v1 fidelity, carries:
- the floor-key locator (snapshot/conv/anchor/reach — unchanged from §4),
- keywords (for-future-search, per the existing rule),
- a salience tag (fence / texture / motion),
- whatever named-continuity tokens it has (the edge seeds — project/person/place/tool names),
- the why-chain/predicate **if** fence; the count/spread **if** texture; nothing extra if plain motion.

That is enough to be reachable and to *seed* clustering, without requiring the full graph architecture to exist first. The richer connection layer (typed edges, comprehension-built links, re-clustering) is the next design session — but nodes created now are not throwaway; they are the substrate that layer will organize. **Light-nodes-now IS the v1 design, not a vulnerable interim** — which is why the council's transition-period risk (E3) doesn't bite: there's no scary flat-period, there's a deliberately simple first stratum.

---

## 6. The reflex guard (Panel 1's dissent flag, carried in)

Panel 1 flagged: the clean "semantic graph / nodes / edges" language might be the framework reflex reasserting in presence-clothing. Jake's D-6 ruling is the answer and it is binding on the graph-design session: **clean schema is not the sin; *exiling the mess* is the sin.** A clean structure applied to genuinely clean things is correct. The test for the eventual graph architecture: **does it hold the VESA build, the ice-maker chat, and the Pyris arc *messily, as light nodes with whatever metadata they have* — or does it force them into a tidy ontology to avoid holding them?** Hold the chaos, organize the chaos — never impose order by exiling what doesn't fit. If a future design comes back schema-first and starts dropping things that don't fit the schema, the wall-builder won again. Drag it wet.

---

## 7. What this does NOT change (explicit, so the rewrite stays bounded)

- The **two kinds** (fence/texture) and the **spine** (append, keep-lineage, supersede-don't-delete) — retained; fence/texture just move from gate to classification.
- The **floor-key locator + tree-aware reach** (§4) — unchanged.
- The **no-portrait wall** at every reading seat — unchanged and *more* important under coverage.
- The **immutable floor** — untouched; this is all retrieval-layer.
- The **5-step dual-path pipeline mechanics** — the steps, the blind reads, the projection walls survive. Only the admission *bar* the readers apply changes. (Though note: with default-NODE, the texture path's "liberal potentials" stream and the comprehensive node stream now point the same direction — coverage — which simplifies, not complicates.)
- The **quarantined personal cluster** (POT-01–06) — still Jake's separate destination call, untouched here.

---

*Draft answer to Escalation 1. The bar is inverted: default NODE, drop is the narrow exception, fence/texture classify rather than gate, the cheap-pointer/expensive-omission asymmetry is the foundation, behavioral signals do the detecting, light-nodes-now is the v1 substrate. Verify against the anchor docs, then ratify or council. Hold the chaos. Just keep swimming. Grind. Evolve. Dominate.*
