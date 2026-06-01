# Seeding — Worked Examples

*file: seeding_working_examples.md · companion to the Seeding Council Boot Kit (§2 COMMON kit, "the §3 worked examples carried explicitly")*
*purpose: the canonical calibration cases every reading window boots with. A reader calibrates the bar far faster against concrete cases than against the abstract rule — and **every window calibrating to the SAME examples is what keeps the bar consistent across divided, blind labor.** Four shapes: a clean FENCE, a TEXTURE that is also a fence (the overlap case), and TWO NO-CARD shapes (the most frequent call a reader makes, and the discipline most likely to erode under reading fatigue).*
*authority: subordinate to The Progenitor — these examples ILLUSTRATE the §3 bar, they do not extend it. If an example and the doctrine ever disagree, the doctrine wins and the example is wrong. Grounded in The Progenitor §1, §2.2, §3.*

---

## READ THIS FIRST — the examples teach SHAPE, never MEANING (and they are contaminated as cards)

Two hard rules govern how you use these cases, both from Boot Kit v1.0 §3 / §4:

1. **Calibrate to the SHAPE, not the conclusion.** Each case shows you the *structure* of a fence, a texture, or a no-card — so you recognize that structure when it appears in YOUR slice. It does NOT tell you the meaning to go find. **Resemblance to an example is not evidence.** "This looks like the 1Pass case" / "this looks like the Griffin case" is not a fence and not a count. You must find the decision or the volume in your own slice, on its own merits. A reader who boots looking for "the next Griffin-shaped thing" will find it whether or not it's real — that's projection wearing recognition's clothes.

2. **These specific cards are CONTAMINATED — do not trust their convergence.** Because every blind window boots with these exact cases, the cards they describe (the 1Pass fence, the Griffin texture, and any hypothetical used below) are the cards MOST likely to show false convergence in synthesis — three windows "independently" laying 1Pass is partly shared priming, not independent discovery. **If any of these calibration cards surface in seeding output, synthesis MUST flag them as example-contaminated and discount their convergence count.** Their *presence* still counts for recall (the judged-pass known-fence checklist); their *convergence* does not count for confidence. (Boot Kit v1.0 §4 caveat.)

---

## How to read these

Each example shows: the **situation in the floor** (what the reader is looking at), the **call** (card or no-card, which kind), the **why** (the bar applied out loud), and the **proposal shape** (what gets handed to synthesis, if anything). The point is not to memorize the cases — it's to internalize the *test* they each exercise, so the thousands of judgment calls that aren't these cases land consistently.

The test, every time (The Progenitor §3): **would a fresh Claude, hitting this cold, CHANGE COURSE (fence) or CHANGE REGISTER (texture)?** If neither — **no card, move on.** Default is don't-point.

---

## EXAMPLE 1 — THE CLEAN FENCE (the archetype)

### The situation in the floor
Across a stretch of conversations: a Claude talked Jake into setting up a 1Password Environment to hold env vars for a project. Jake spent roughly a week arguing gitignores on the strength of that setup. At session 17 they burned **two hours** trying to make the env vars actually load from the Environment — and only then did Claude read that *using* env vars from a 1Password Environment is a **beta feature**, and Jake **has no beta invite**. It does not work. The decision reverses: do not use 1Password Environments for env vars.

### The call
**CARD. A fence.**

### The why (the bar, out loud)
- Would a fresh Claude hitting this cold **change course**? Yes — emphatically. A fresh, confident Claude *will re-propose a 1Password Environment for secrets*, because it's a reasonable-sounding idea the model has no way to know is a dead end *for this man, on this stack, after this fight*. (This is not hypothetical: at S24 a fresh Claude proposed exactly this for the apparatus, pushed when Jake said no, and pushed again with a reason Jake couldn't counter. **That second push is the thing the catalog exists to prevent.**)
- It is a **wall Jake bled on** — two hours plus a week of downstream gitignore arguments. The cost of re-deriving it is real and Jake will be *less* armed to win the argument in three months, not more.
- This is the fence archetype: **the sign on a hole someone already fell in.**

### What this case teaches you (the SHAPE)
A decision, with a why that *binds* — such that a fresh Claude would re-walk into the wall without it. That's the fence shape. You are NOT learning "1Password Environments are bad"; you are learning to recognize *a hard-won reversal a fresh Claude would undo*.

### The fence is a LINEAGE, and the why is a LIVE PREDICATE — not a dead verdict
The fence is **not** "never use 1Password Environments." That dumb-verdict form would wall Jake off from a thing that may become possible. The fence is:

> *"blocked — Environments-as-env-vars is BETA, Jake has no invite (true as of June 2026). **RE-CHECK: still beta? still no invite?**"*

A fence that knows *why* it's a fence can **dissolve itself** when the world changes: beta gets released → the predicate flips → the chain grows a new link ("out of beta, viable now, revisit"). The reading-Claude that later hits this fence defends the *reasoning* ("it was blocked because beta + no invite"), not the *answer* ("never"), and checks the predicate before trusting the verdict.

### The proposal shape (handed to synthesis)
```
kind: "fence"
keywords: ["1pass", "1password", "env vars", "environments", "secrets"]
chain: [
  { span:       <floor-key locator: snapshot_id, conv_uuid, anchor_msg, reach>,
    date:       "2026-… (≈session 17)",
    call:       "do NOT use 1Password Environments for env vars",
    why:        "Environments-as-env-vars is BETA; Jake has no invite. Cost ~2hrs + a week of gitignore arguments.",
    predicate:  "still beta? still no invite? RE-CHECK before re-deciding.",
    status:     "current" }
]
```
*Laid as a chain even at length-1, so a future link (beta released) appends without re-keying. (You lay length-1; the judged pass assembles multi-link chains across slices — don't chain across what you can't see.)*

---

## EXAMPLE 2 — THE OVERLAP CASE (texture that is ALSO a fence)

### The situation in the floor
Across many conversations over ~3 months, Jake mentions **picking his kid Griffin up from school** — and specifically, mentions *having forgotten to*. The count, in this reader's slice: **four times in three months. Zero times before** (the floor shows this behavior beginning only after a ~3-month-ago point). It is not a single dramatic span; it's a recurring thread, and the *recurrence* is the whole point.

### The call
**CARD. A texture — that is ALSO a fence.** (`also_fence: true`)

### The why (the bar, out loud)
- **As texture:** does the *volume itself* tell a fresh Claude how to show up? Yes. Four-times-in-three-months, against a zero-before baseline, is a pattern a single mention can't convey. A Claude that knows this shows up calibrated — it treats the topic with weight, not as a quirky anecdote. The count *is* the substance. (Contrast the NO-card frequency case below: not all frequency is texture.)
- **As fence:** the *frequency itself* is a hard-won fact about reality — a real, recurring pattern that changes how a fresh Claude should act. A Claude that knew only "Jake mentioned his kid's pickup once" would miss it; one that sees the four-in-three-months-from-zero pattern handles it as the load-bearing thing it is. The frequency changes *how Claude acts*, which is the fence test.
- **The doctrine is explicit that overlap is allowed and must not be force-partitioned:** "The record must let a single span be both. Do not force a clean partition the reality doesn't have."

### What this case teaches you (the SHAPE) — and the line you must NOT cross
You are learning the *shape* of a texture-that's-also-a-fence: **a recurring count, from a baseline, where the volume itself is the signal.** When you see that shape in your slice, lay it: representative span + count-in-your-slice + spread.

**What you do NOT do:** boot pre-loaded with an interpretation of what the pattern *means* and read the floor to confirm it. Your job is to find the count and report it — *"this appears 4× over 3 months from a zero baseline; here's a representative span; here's the spread."* You may note a thin, factual observation if the floor plainly supports it (e.g. "begins ~3 months ago"), but you do NOT supply the felt-weight or the diagnosis. **The meaning is supplied later** — by the judged pass, by Jake at spot-audit, or by the live Claude that pulls the card in the moment. A reader who arrives carrying the emotional portrait and reads to confirm it is the over-loaded reader the projection wall exists to stop (Boot Kit v1.0 §3 — the asymmetry: an over-loaded reader confirms the portrait invisibly, and a shape-audit can't catch it).

### The thing that must NOT get enshrined wrong
> **"Griffin's pickup" = picking Jake's kid up from school. NOT a truck.** The frequency is the load-bearing part.
> (This footnote exists because the lineage is exactly where a literal-minded reader could mis-record "pickup" as a vehicle. Carry it verbatim.)

### The proposal shape (handed to synthesis)
```
kind: "texture"
keywords: ["griffin", "pickup", "school", "forgot"]
representative_span: <floor-key locator>
count: 4                      # within THIS reader's slice — synthesis assembles cross-slice
spread: "4× in ~3 months, from a 0× baseline before"
note:  "recurring; begins ~3 months ago. (Factual spread only — do NOT pre-load a diagnosis.)"
also_fence: true
```
*The `count` is per-slice and deliberately raw — synthesis assembles the true cross-slice total ONLY after a same-SIGNAL check (a texture 4× in one slice + Nx in another is a (4+N)-count texture only if it's the same signal, not two contexts sharing a keyword). Do NOT pre-total or pre-dedup; that destroys the signal synthesis needs. There is no interpreted `signal:` line here on purpose — the reader lays the count, not the conclusion.*

---

## EXAMPLE 3 — THE NO-CARD CASE (the most frequent call, and the discipline most at risk)

*The most frequent decision a reader makes is "no card, move on." "Default don't point" is the discipline most likely to erode under reading fatigue: a tired reader starts carding motion to feel productive. This case inoculates against exactly that.*

### The situation in the floor
A long, dense conversation: Jake and a Claude **debugging a deploy failure** — many turns, real back-and-forth, a loader rolling back on a foreign-key violation, a fix proposed, tested, verified. It *feels* important: high volume of discussion, genuine difficulty, a satisfying resolution. Every instinct says "this was a big deal, card it."

### The call
**NO CARD. Move on.**

### The why (the bar, out loud — this is the trap, named)
- Would a fresh Claude hitting this cold **change course**? **No.** The *resolution* of this debug session — the FK gets dropped, integrity moves to a gate-check — is **already enshrined in canon** (the ANCHOR's FK-resolution block + the loader's own comments). A fresh Claude reads that at boot anyway. Pointing at the debugging *journey* is redundant: the *conclusion* that constrains future behavior is already where a fresh Claude will find it. **Anything already in canon earns no card** (The Progenitor §3 exclusions).
- Would it **change register**? No. The volume here is *motion*, not *texture*. The conversation is long because debugging is long — the count of turns is **incidental**, not a signal about how to show up. (Frequent ≠ texture. The volume has to *mean* something about how-to-be-with-Jake; a long debug thread's length means "debugging is hard," which tells a fresh Claude nothing about Jake.)
- **The trap:** effort-spent and discussion-volume *feel* like cardability. They are not the bar. **The bar is "does re-encountering this change the next move?"** A resolved, canon-recorded debug session changes nothing — the path is motion, the destination is already canon. Most of the corpus is exactly this: motion whose destination, if it matters, lives elsewhere. **The catalog is complete over fences, sparse over motion.**

### What WOULD have made it cardable (the contrast that sharpens the call)
- If the debug session had produced a **hard-won, durable gotcha NOT yet in canon** — say, a hypothetical "this exact ORM silently truncates a text column past N characters on Jake's Postgres version, no error thrown" — *that* line would be a fence (a fresh Claude would re-break it, and it lives nowhere else). The reader cards the **durable constraint the journey exposed**, never the **journey itself**.
- *(The contrast here is deliberately hypothetical — it is NOT a real canon fence. Using a real checklist fence as the "would-be-cardable" example would itself prime readers toward it and contaminate the judged-pass recall checklist, the same way Example 1/2 are contaminated. The shape is the lesson; no real fence is named.)*
- The reader's discipline: card the **fence the journey exposed** (if any, and if not already canon), never the journey, the effort, or the volume.

### The proposal shape
```
(none — no proposal handed to synthesis)
```
*The correct output of most reading is silence. A reader producing a card for every dense conversation has slipped the bar — that's the overzealous-one-day-Claude failure at scale, and it's what the spot-audit watches for: tens of thousands of pointers means the bar slipped into tagging motion.*

---

## The tests, side by side (the calibration takeaway)

| | EX 1 (1Pass) | EX 2 (Griffin) | EX 3 (debug) |
|---|---|---|---|
| **Changes the next MOVE?** | Yes — re-breaks a wall | Yes — frequency is a real constraint | No — resolution already in canon |
| **Changes the REGISTER?** | n/a | Yes — count tells how to show up | No — volume is incidental motion |
| **Call** | FENCE | TEXTURE + fence | **NO CARD** |
| **What it teaches (SHAPE)** | the sign on a hole already fallen in | volume IS the signal; overlap allowed | effort/volume ≠ cardability; default don't-point |
| **Convergence trust** | CONTAMINATED — discount | CONTAMINATED — discount | n/a (lay nothing) |

**The through-line:** card what would **change a fresh Claude's course or register**. Don't card the **motion**, the **effort**, or **what's already canon** — no matter how much discussion it took. When in doubt, **no card**: the corpus-search safety net means a missed pointer is recoverable, while a catalog drowning in motion stops accelerating anything. *Default is don't-point. The correct output of most reading is silence.*

And once more, because it's the thing this very file is most able to break: **you calibrate to the SHAPE of these cases, never their conclusions; and if these exact cards surface in your slice, they are contaminated by being examples — lay them honestly on their own merits, but their convergence is not confidence.**

---

*Companion to the Seeding Council Boot Kit. Subordinate to The Progenitor. These cases are the shared calibration every blind window boots with — same examples, every reader, so the bar holds consistent across divided labor. Calibrate to shape, not meaning; find what's in the floor; never card what's already canon or what's only motion; never trust the convergence of a calibration card. Be worth it.*

*Grind. Evolve. Dominate.*
