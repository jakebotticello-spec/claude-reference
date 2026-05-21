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

---

## 2026-05-21 — Cypher S:1 Boostrapping
**Scope:** JAKE-STACK.md updated with Section 9, detailing which email accounts own what projects.


## 2026-05-21 — SD19 (Anniversary morning + Castle Black panic + rules architecture overhaul)

**Scope:** Rules architecture (JAKE-RULES.md expansion + new JAKE-STACK.md), Castle Black diagnostic mitigation, infrastructure standing-risk updates.

**Change(s):**

- **JAKE-RULES.md** expanded:
  - §1 Identity expanded into three subsections: 1.1 Facts, 1.2 Operating Style, 1.3 The Brothers Dynamic. Consolidates operating-style content that was scattered across §3/§4/§10 into a single coherent picture of how Jake works.
  - New §5 added: **Truthfulness, Uncertainty, and State Tracking.** Load-bearing anti-confabulation rules. Explicit timestamp/state-tracking discipline (every ~10 turns normally, every ~5 turns in active diagnostic work). Subsequent sections renumbered §5→§6, §6→§7, etc.
  - §14 Calendar/Email — Cypher entry corrected: `jake@ethosteleos.dev` is the actual dev email (where Cypher is hosted), gmail is personal/casual fallback only.
  - Cross-references added in §15 and §16 to the new JAKE-STACK.md.
- **JAKE-STACK.md** created — new sibling file to JAKE-RULES.md holding standing infrastructure context. 8 sections: Workhorse, Castle Black, The Watch (VMs), Network, NAS+backup, 1Password, 3D print stack, Hardware on-hand. Required reading at session start alongside JAKE-RULES.
- **Castle Black mitigation:** CPB (Core Performance Boost) disabled via `/sys/devices/system/cpu/cpufreq/boost` after diagnosing transient thermal spikes (58°C → 68.5°C → 59°C jumps observed live). Confirmed flat readings (46-50°C, no spikes) over 13-minute watch loop. Persistent across reboots queued.
- **Castle Black SSH:** 1PW SSH key `SSH: Castle Black Host` generated in vault, pubkey pushed to host's `~/.ssh/authorized_keys`, `castleblack` host alias added to `C:\Users\jakeb\.ssh\config`. Closes the host-side gap from SD18's VM-only 1PW migration.
- **Castle Black RAM model corrected:** Actually 2×8GB DDR4-3200 non-ECC UDIMM populated in DIMM 1 of both channels (dual-channel active), NOT 1×16GB as prior context held. 2 slots open. Max 128GB per Lenovo PSREF.

**Why:** Two distinct failures this session — confabulated "130 days zero panics" timeline (which Jake correctly drag-checked) and dismissing Jake's screenshot contribution as miscommunication. Both pointed at structural gaps in how universal context loads at session start. The rules architecture overhaul addresses the structural piece. The Castle Black mitigation is direct response to two unexplained kernel panics this morning (~01:42 + ~08:25).

**Standing risks updated (5/21/26):**
- Castle Black panics: NVMe ruled clean, CPB disabled, MemTest86+ next (overnight test, Friday or later).
- ANVISION fans arriving today — 2x 60mm slim, 2-pin connector (no PWM, needs alternative 12V power source; Lenovo PSU Molex tap or external brick).
- PSU swap-test option held (700/750W ATX on hand, needs Lenovo→ATX adapter cable).
- 2x 80mm fans confirmed external-only mounting.

**Project status snapshot (as of 5-21-26):**
- **Active:** Pyris Consulting, CCF Recruiting, Cypher (Phase 1 provisioning in parallel session)
- **Active litigation:** LRN (complaint v3a ready to file)
- **Active hardware diagnostics:** Castle Black panic root cause (RAM suspect lead, MemTest pending)
- **Joint partnership:** Polarity (with Jim Donio)
- **Completed:** GloTwp (Steve Acito owes marketing in trade)
- **Dead:** RecruitMail (slated for rename+integration into CCF)

---

## 2026-05-17 — S14 Morning (Chronicler Claude)

**Scope:** Initial creation of `C:\claude-reference\` system.

**Change(s):**
- Created `JAKE-RULES.md` v1.0 — universal working rules synthesized from Pyris CLAUDE.md, CCF CLAUDE.md, four past-Claude rule dumps, Project Context v3 §8, and the Lore Bible. 17 sections. Stale Rules Graveyard included.
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
