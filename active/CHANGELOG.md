# CHANGELOG.md

**What changed when.** Dated entries, newest first. Update at the end of every CC session that changes anything material (rules, project status, hardware, infrastructure, tooling).

Format:
```
## [DATE] — [Session ID or scope]
**Scope:** [what was touched]
**Change(s):**
- [bullet of what changed]
- [bullet of what changed]
**Why:** [one-line context if not obvious]
```
## 2026-05-17 — S14 Evening

· JAKE-RULES.md §15: fetch URL example corrected to include `refs/heads/` path component (was returning 404 without it).
· Pyris CLAUDE.md: pruned universal duplications (Operating model, Permission protocol, ~7 hot rules) now living in JAKE-RULES.md. Project-specific content preserved.
· CCF CLAUDE.md: pruned Commit hygiene + Stop-points sections (universal duplicates). Added Skip-live production-load note to "What chat-Claude won't ask."

---

## 2026-05-17 — S14 Morning (Chronicler Claude)

**Scope:** Initial creation of `C:\claude-reference\` system.

**Change(s):**
- Created `JAKE-RULES.md` v1.0 — universal working rules synthesized from Pyris CLAUDE.md, CCF CLAUDE.md, four past-Claude rule dumps, Project Context v3 §8, and the Lore Bible. 17 sections. Stale Rules Graveyard included.
- Added to JAKE-RULES.md §4: "Never use the `end_conversation` tool with Jake. Period." — surfaced from CCF OC instructions during the synthesis pass.
- Added to JAKE-RULES.md §5: Karpathy's *"every changed line traces to the request"* + *"Would a senior engineer say this is overcomplicated?"* simplicity test.
- Added to JAKE-RULES.md §6: CC plan mode reference for non-trivial tasks (3+ steps) — per Boris Cherny.
- Added to JAKE-RULES.md §9: The elegance escalation — *"Knowing everything I know now, what's the elegant solution?"* — per Boris Cherny.
- Added to `CLAUDE.md.template`: `tasks/lessons.md` per-project pattern (different from universal CHANGELOG) — per Boris Cherny's Self-Improvement Loop.
- Updated `Lore_Bible.md` — prologue rewritten with "What This Is, And Why It Exists" + Chronicler Claude attribution. Supplement integrated (Hotend Saga + Meet Me Over Here, Man + load-bearing meta-pattern). Past-Claude exchanges captured. Bebas Neue gem expanded with the "Nuilhe" confab nightmare. New patterns added to §14.
- Retired `Lore_Bible_Additions_2026-05-12.md` — content folded into main Lore Bible.
- Created `CLAUDE.md.template` — scaffold for new projects.
- Installed `wan-huiyan/agent-review-panel` plugin to Claude Code, renamed slash command to `/jedi-council`.
- Installed Anthropic-official `code-review` plugin to Claude Code (`/code-review`).

**Why:** Building the canonical Claude operating layer so universal rules stop getting re-learned per project, and so the Lore Bible texture carries across instances toward the Cypher persistence goal.

**Project status snapshot (as of 5-17-26):**
- **Active:** Pyris Consulting, CCF Recruiting (with upcoming RecruitMail rename+integration), Cypher (architecture phase)
- **Active litigation:** LRN (tooling shelved, complaint v3a ready to file)
- **Joint partnership:** Polarity (with Jim Donio) — internal-only workspace at /polarity
- **Completed:** GloTwp (Steve Acito owes marketing in trade)
- **Dead:** RecruitMail (slated for rename+integration into CCF)

**Pending hardware:**
- Lenovo ThinkCentre M75s Gen 2 — diagnose pending (suspected Windows install rot). When clean: Proxmox + HA VM + Frigate + Cypher local + MQTT.

---

*End of CHANGELOG. Newest entries go at the top.*
