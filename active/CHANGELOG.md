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
## 2026-05-24 — SD22 (3D Recipes nightly archiver + retroactive SD21 cam-migration log)

**Scope:** JAKE-STACK §5 (new archiver subsection); plus the retroactive SD21 cam-migration entry below, logged this session.

**Change(s):**
- **JAKE-STACK §5** — added the **3D Recipes Nightly Archiver** as standing infra: `Archive-3DRecipes.ps1` (v1.0) sweeps any `C:\3D Recipes` top-level folder >30 days cold to `D:\3D-Backups\<name>` nightly at 01:00, then junction-relinks the C: path (opens/slices in place; bytes on D:). Task `3DRecipesNightlyArchive`, one hour ahead of the 02:00 NAS backup so the move settles before the mirror walks. Backup unaffected — `nightly_nas_backup.bat v7.2` already carries `/XJ`, so it skips the junctions and stores the archived content once via the D: mirror (no double-store). Escape-hatch `$Exclude` list documented but NOT yet coded.
- **Retroactive log:** the SD21 go2rtc cam migration (entry below) never landed in the reference layer — caught at SD22 session start and logged so a next-Claude reading §3 doesn't believe the old ffmpeg/HLS pipeline is live.

**Why:** Keeps the 3D Recipes SSD lean without breaking any slicer paths, and closes the SD21 doc-lag.

## 2026-05-23 — SD21 (Printer cam: ffmpeg→HLS retired, migrated to go2rtc WebRTC) — logged retroactively SD22

**Scope:** JAKE-STACK §3 (VM 100 / go2rtc), §4 (Workhorse IP), §7 (camera / Tapo ceiling); Lore Bible §5.

**Change(s):**
- **JAKE-STACK §3** — camera pipeline migrated ffmpeg→HLS → go2rtc WebRTC. `server.js` v3.3 (camera pull removed; now serves dashboard, printer MQTT/WS, `/api/config`, `/api/printer`, kiosk routers only); new go2rtc subsection (binary, `go2rtc.yaml`/`go2rtc.env`, systemd service, ports :1984/:8555, passthrough/no-transcode). Frozen-but-flowing note marked historical/pipeline-retired — go2rtc immunity to the Tapo wedge UNPROVEN. Stale ffmpeg systemd-SIGTERM + floor-metrics facts scrubbed (current state = current state).
- **JAKE-STACK §4** — pinned Workhorse `.238` (surfaced via a go2rtc consumer `remote_addr`).
- **JAKE-STACK §7** — documented the Tapo C111 ~2-pull RTSP ceiling as a standing constraint (root cause of the SD21 black-screen marathon — VLC was the 3rd puller); camera now served via go2rtc WebRTC.
- **Lore Bible §5** — added "The Diagnostic Tool Became the Bug" (VLC as the 3rd RTSP puller starving go2rtc; the codec investigation was a red herring on a starved feed).

**Why:** The frozen-but-flowing ffmpeg pipeline that opened the whole cam saga is retired; cam is on go2rtc WebRTC — single-puller, sub-second, phone-friendly. The afternoon's codec theory was a red herring; the real cause was the 2-pull ceiling.

## 2026-05-23 — Cypher S8 (self-citation rule + the doc-is-an-echo scar)

**Scope:** JAKE-RULES §5.1; Lore Bible §5.

**Change(s):**
- **JAKE-RULES §5.1** — appended the self-citation reinforcement: a document is not a verification source for its own claims (least of all one you authored); ground truth is the live system (the dashboard, `railway variables`, the running process, the file on disk), never the doc that describes it.
- **Lore Bible §5** — added "The Dashboard Is Ground Truth, The Doc Is An Echo": CC confirmed an injected Railway var off a self-authored CLAUDE.md §7 note (itself sourced from a handoff "likely"), shipping a silent-no-op guard + a false fact into the source-of-truth doc; the live dashboard (`RAILWAY_ENVIRONMENT_NAME`/`_ID`, no bare form) disproved it in two clicks.

**Why:** The pattern bit twice in one session and the second time shipped an actual error into CLAUDE.md. Bound to a rule so future-Claude (OC and CC) doesn't re-buy it.

## 2026-05-23 — Cypher S7 (universal layer: §2 CC-delivery rules + new §17 session-close process)

**Scope:** JAKE-RULES §2 (two additions), new JAKE-RULES §17, downstream renumber (§17→§18, §18→§19); Lore Bible §5 (deferred entry, landed 5-24).

**Change(s):**
- **§2 — OC→CC delivery default** (above Non-CC workflows): OC hands CC instruction sets as a single chat code block by default; the lone exception is a kickoff embedding whole code files (nested `ts`/`sql` fences break inside an outer block) → deliver each file as its own block, or fall back to a single self-contained `.md` and say so. Token-economy: don't build a file when a block does the job.

- **§2 — CC change-manifest rule** (section end): CC closes every turn with a tight manifest — files touched + why; commands + pass/fail (output only on error); **anything off the approved plan called out explicitly** (the shiny-thing tripwire, §6 surgical-changes); stopped-here/next. "Verbose" banned as the default — it reconstructs the turn + dumps raw output and burns the Max allowance as per-turn context-rent. Pairs with plan-mode (§7) as prevention.

- **§17 — new section: Session Close & Handoff Generation.** Codifies the end-of-session bundle: (1) tactical handoff file [PK + archive], (2) separate proposed-reference-changes file [→ rules repo on approval], (3) project-centric reference artifacts [PK + archive], (4) in-chat next-session handoff prompt [code block, generated last]. Four operating principles: verbose-is-mandate, downstream-flags (name the horizon), honest judgment-call ledger (call/reasoning/confidence/source), infra sweep (route incidental system/subscription/hardware finds into JAKE-STACK/Lore via the proposals file).

- **Renumber:** former §17 Stale Rules Graveyard → §18; former §18 The Why → §19.
- **Lore Bible §5** (Pattern Stories) — added "The Layer-Boundary Blind Spot": `/jedi-council` had 4 of 5 reviewers (incl. the Security Auditor) miss the cross-tenant FK gap that lived below the RLS layer everyone verified; only the schema-first specialist caught it. *Deferred from S7; landed in the 5-24 consolidation pass.*

**Why:** §17 is the package-out mirror of §15/§16's load-in — it closes the persistence loop so next-Claude picks up seamlessly instead of reverse-engineering state. It was earned over many sessions of frustration with the state of current-Claude's project ignorance and context confabulation.  The §2 rules came out of the S7 1b build: delivery-format token economy, and the standing per-turn drift-catch that's repeatedly caught CC chasing shiny things mid-build.

## 2026-05-22 — SD20b (Afternoon/evening: LRN filing window verified + cam frozen-but-flowing diagnosed)

**Scope:** JAKE-RULES §10/§11, JAKE-STACK §3 (TheNightsWatch), Lore Bible, litigation status (LRN).

**Change(s):**
- **JAKE-RULES §10** — added "File freshness ≠ live data."
- **JAKE-RULES §11** — extended "Jake's eyes beat Claude's math" with the ground-truth / don't-relitigate reinforcement.
- **JAKE-STACK §3 (VM 100)** — corrected stale `server.js` v3.1→v3.2 + added `index.html` (SD20a rework was unlogged); documented the ffmpeg SIGTERM slow-kill hang (>90s) + queued `KillMode=mixed`/`TimeoutStopSec=10`; added the frozen-but-flowing standing risk + planned content-freshness watchdog.
- **Lore Bible** — added "File Freshness Was a Lie" (§5 Hardware & Build).
- **LRN filing window verified:** Reno Justice Court, Washoe County NV via eFileNV (Tyler Odyssey), 24/7 submission; filing type CC25O ($2,500.01–$5,000.00); original returned 4/24 "Rejected" (generic reason); RJC civil requires Summons + civil cover sheet for a new case; Memorial Day Mon 5/25 closes court — clerk review resumes Tue 5/26. v3a packet NOT yet reviewed.

**Why:** Cam feed froze (frozen-but-flowing ffmpeg). First ~40 min went to a misdiagnosis built on file-freshness checks that measure file mtime, not video content — that lesson is now a rule. LRN window was the SD20b top-Mandatory groundwork; packet review deferred (cam ate the session).

**Project status snapshot (as of 5-22-26):**
- **Active:** Pyris Consulting, CCF Recruiting, Cypher (LIVE on public internet; 3 infra phases + S1b schema/migrations to usable)
- **Active litigation:** LRN (v3a — filing window verified; needs packet review [complaint + summons + civil cover sheet] before refile)
- **Hardware:** Castle Black panic = thermal, confirmed stable; cam feed frozen-but-flowing (specimen held for AM diagnosis); HUSBZB-1 in hand (Phase 8 gated, NOT by PSU); Bills sign nearly glued (LEDs next)
- **Joint partnership:** Polarity (with Jim Donio)
- **Completed:** GloTwp (Steve Acito owes marketing in trade)

---
---

## 2026-05-22 — Cypher S2–S5 (Re-root correction + Railway deploy bring-up + 1a CLOSED)

**Scope:** Cypher repo root structure, Railway deploy config, `code/package.json` dependency layout. Correction of false-state claims logged in S2. Phase 1a deployment.

**Change(s):**

- **1a CLOSED — multi-tenant foundation is live (S5).** All three subdomains route correctly over live Let's Encrypt certs, deploy Active, SPA renders ("Cypher / Phase 1a — Foundation"):
  - `cypher.ethosteleos.dev` → 200, `cypher_tenant` / `tenant`
  - `ordo.ethosteleos.dev` → 200, `ordo_tenant` / `tenant`
  - `jango.ethosteleos.dev` → 200, `ordo_tenant` / `landlord`
  - Host-header middleware resolves `(tenant, view)` correctly for all three, including jango → ordo_tenant/landlord. (Note: jango's *hard 403* for non-landlords is not yet exercised — `/healthz` is unauthed; the role-gated rejection lands with auth in 1b.)
- **The build break, fixed (S5):** moved `vite` + `@vitejs/plugin-react` from `devDependencies` to `dependencies` in `code/package.json`. Root cause: S4's `NODE_ENV=production` service variable makes `npm ci` skip devDependencies → `vite` not installed → `vite build` exits 127 (`sh: 1: vite: not found`). Confirmed deterministic via two full build logs ~4h apart (12:36 + 16:24), identical failure both times. `@types/*` and `typescript` correctly stayed devDeps (esbuild strips types at build; `tsc` only runs in the `typecheck` script). Commit: `fix(build): move vite + plugin-react to dependencies so prod npm ci installs them`.
- **Re-root LANDED (S4).** Repo restructured to `code/` + `docs/` subdirs at root; committed node_modules purged from the tree; Railway Root Directory set to `/code`. Verified three ways: force-push moved 28 objects / 55 KiB (vs. the 21 MiB node_modules-laden fetch), GitHub tree correct, build got past the mis-root death. HEAD `b599ac3`. This killed the 10+ hour `Failed to read app source directory` failure.
- **Deploy config corrected (S4).** `NODE_ENV=production` set (was unset → app ran the dev branch in a prod container, bound :8080). Explicit `PORT=3000` service variable set and all four Railway domains aligned to port 3000 (were split 8080/3000 across routes). `railway.json healthcheckPath` confirmed it MUST stay `/` — `/healthz` is host-gated and would 404 Railway's probe.
- **§4 loose end CLOSED:** `git push -u origin main` set the upstream tracking ref for `main` (re-init had wiped it).

**Corrections to prior record:**

- **S2 logged false state.** S2 claimed the deploy had succeeded and certs/docs were good; none of it held (re-root hadn't landed, certs were hostname-mismatched, build was dead at the mis-root). Corrected here per the standing anti-confabulation rule — an uncorrected changelog is itself a confabulation source (JAKE-RULES §5).

**Learnings logged:**

- **`NODE_ENV=production` touches `npm ci`, not just runtime.** Prod env drops devDependencies at install time. Any build tooling that must run during a prod build belongs in `dependencies`, not `devDependencies`. This was the link that broke S4's "config changes don't alter the build" reasoning and cost the back half of S4 plus the open of S5.
- **Build-path rule (refined S5).** Code reaches the repo one of two ways: CC writes it in-repo, or OC delivers a single self-contained file (download or tarball). OC never hands Jake multi-file edits or folder-structure to assemble by hand. Single-file download is fine — the line is multiple files / building structure.
- **Ground-truth-before-theory paid off (reinforces §5 / §7).** S5 opened leaning "Railway build-infra, nothing to fix" off S4's truncated log. The full streamed log killed that lean on the first read — deterministic exit 127 at `vite build` across two attempts. Refresh-first + pull-the-real-log did exactly what the rule promises.

**Why:** S4 closed RED at a ~9s image-build failure with the cause unconfirmed, leaning Railway infra; the deploy had been blocked 10+ hours across the re-root saga. S5 pulled the full build log, found the one-line dep-location bug (vite as a devDep under prod install), fixed it, and closed 1a — green build, `Cypher listening on :3000 [production]`, Active, three subdomains verified, SPA rendering.

**Cypher 1b prerequisite flagged (not yet done):** Railway Variables holds only `NODE_ENV` + `PORT` — no secrets. Before 1b's DB-backed tenant lookup ships, the 1PW `Cypher: Dev` secrets (Supabase URL/anon/service_role, both Anthropic keys, `OAUTH_ENC_KEY`) must reach Railway or prod crashes on boot the same way it did today, different missing piece. `OAUTH_ENC_KEY` not yet generated (CC generates it during 1c scaffolding).

**Project status snapshot (as of 5-22-26):**
- **Active:** Pyris Consulting, CCF Recruiting, **Cypher (Phase 1a CLOSED — 1b next)**
- **Active litigation:** LRN (complaint v3a ready to file)
- **Joint partnership:** Polarity (with Jim Donio)
- **Completed:** GloTwp (Steve Acito owes marketing in trade)
- **Dead:** RecruitMail (slated for rename + integration into CCF)

---

## 2026-05-22 — SD20 (Universal-layer file maintenance)

**Scope:** `claude-reference/active/JAKE-RULES.md` (§16, §17), `claude-reference/active/JAKE-STACK.md` (§1, §7).

**Change(s):**

- **JAKE-RULES §16 — session-start retrieval method changed.** Orchestrator-Claude now pulls the rule files via the codeload tarball (`codeload.github.com/.../tar.gz/refs/heads/main`) instead of `web_fetch` against the raw.githubusercontent.com CDN. Added a **mandatory footer-date freshness tripwire**: after pulling, compare each file's `Last updated:` footer against the latest day-state handoff; if older, re-pull or stop, never operate off a suspected-stale file (§5).
- **JAKE-RULES §17 — graveyard entry added** for the dead raw-CDN retrieval method, so future-Claude doesn't re-suggest it.
- **JAKE-STACK §1 (Workhorse) — monitor info added.** Three-monitor station documented: 48" Decogear ultrawide, 29" LG, 27" HP.
- **JAKE-STACK §7 (3D print stack) — printer hardware corrected.** Heater block now reflects the OEM Bambu Hotend assembly (supersedes the off-brand interchangeable-nozzle block carried in prior context — the OEM-first-for-critical-tolerance lesson from the Hotend Saga).

**Why:** Universal-layer hygiene. The retrieval-method fix removes a recurring stale-file friction at session start — the raw CDN edge-caches and had served copies 2+ versions behind real HEAD (cost time SD19→SD20); codeload serves the git archive at HEAD, never cache-stale. The JAKE-STACK corrections bring standing infrastructure in line with reality.

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
