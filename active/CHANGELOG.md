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
## 2026-05-29 — JAKE-STACK overhaul (dedicated full-stack interrogation session)

**Scope:** JAKE-STACK.md — full-file revision (Jake's express permission; the standing "surgical edits only" rule waived for this one dedicated pass). Two new sections, every existing section reconciled against live ground truth (router config, systemd units on disk, physical device labels, file timestamps).

**Change(s):**
- **§1 Workhorse — fully specced** (was thin). MSI PRO B550M-VC WIFI (MS-7C95) / Ryzen 7 5700 (8c/16t, no iGPU — discrete GPU mandatory) / GTX 1070 (not an inference surface) / 16GB RAM running tight (2.12GB free) / C: Samsung 870 EVO 500GB SATA SSD + D: Seagate 2TB **5400 SMR** laptop HDD (resolves the old "if D: is spinning" hedge — it is; SMR = archive/read only) / Win11 **Pro** Build 26200. Logged 3 install-default (not deliberate) security flags: Secure Boot Off, VBS/HVCI on (contended hypervisor surface), Smart App Control Enforced (first suspect for silent unsigned-binary failures). No full software manifest (Jake's call).
- **§2 Castle Black — hardware confirmed unchanged 5-29** (RAM, SN740 boot); **cooling documented for the first time**: stock AMD cooler + 1×60mm REAR intake + 1×80mm FRONT exhaust, **airflow reversed from convention ON PURPOSE** (closet placement) — DO-NOT-"correct" warning. Case closed, box in permanent position. CPB confirmed back ON (cooling holds the floor).
- **§3 The Watch — major risk reconciliation.** **V8-worker-hang risk REMOVED as a phantom** — disk sweep (server.js v3.3 unchanged, unit v2 Restart=on-failure, empty crontab, all-stock timers) proved no dashboard watchdog and no evidence the panels ever hung; the remembered hang was the **ffmpeg CAMERA-worker stall**, mislabeled, **permanently fixed by the go2rtc swap (v3.3/SD21)**. Queued "dashboard liveness probe" CANCELLED. Inoculated against the SD24 handoff re-adding it (**SD24 carries a false "V8 hang hit live" fact — correct in PK**). Kiosk `Restart=always` correctly attributed as the real self-heal (host-side, Acer). go2rtc stable since SD21 (immunity still formally unproven — watching). config.json sharpened: holds the **real Bambu account email+password**, not just a token. Added host→VM ssh-alias gotcha (`nightswatch` is WH-only). VM200 Watchtower confirmed UP (Ary's tile per-member staleness flagged).
- **§4 Network — .88/.250 discrepancy RESOLVED.** Both ARE reserved (router config verified); the day-state board's "open ~5-min task" was STALE — §4 was right. Surfaced 2 GAPs: **WH .238 unreserved** (dynamic lease — reserve it) + **stale .30 JakesRedRig** (WH's pre-crash identity — clean up). Logged untracked LAN devices: TP-Link .11 (= Tapo cam), Google/Nest .216, SmartThings hub MAC.
- **§5 NAS** — NAS named explicitly (DS218J); SMR slicing-cost made real (not hypothetical); Bambu tarball-mirror note (feeds §11 exposure).
- **§7 print** — documented the Bambu **cloud** MQTT model (us.mqtt.bambulab.com:8883, login w/ stored email+password → token) + the local-MQTT-tradeoff (kills the token clock but breaks Handy coexistence — not a free swap; corrected an earlier OC overstatement).
- **§8 inventory** — PSU specced (OCZ700MXSP 700W 80+, dual-rail 12V); spare GPU added (Gigabyte GTX 950 2GB — emergency display-out fallback only); fans reconciled (1×80 + 1×60 installed per §2, 1 of each spare); 125mm vortex retired to inventory; spare RAM = SODIMM-only (NOT WH/CB-compatible — kills the "free RAM fix" hope); display-surface fleet logged (2 Surfaces + spare Samsung + Zenpad + in-service calendar tablet = no need to buy HA panels).
- **NEW §11 — Standing risk-clocks & security exposures.** Risk-clock #1 config.json plaintext (OPEN). **Risk-clock #2 Bambu cloud MQTT token — DISK-ANCHORED to ~Apr 11 2026** (bambu-monitor-v2.tar.gz mtime across 4 locations) → ~mid-July 2026 expiry; first real anchor this clock has ever had. **Security exposure: Jake's real Bambu account password was spilled to chat** (prior Claude requested it in-band, violating flag-early) — now in transcript + config.json + NAS-mirrored tarballs; **decision: rotate at the July reauth** (bundles 2FA; accepted ~6-wk risk; July reminder must say "re-auth + ROTATE + 1PW"). ELEGOO ESP-32 kit logged as asset (UNSCOPED — RC522 is RFID not NFC, flagged).
- **NEW §12 — Smart home / home automation** (built from zero this session). HA-on-VM300 as the master controller (only platform unifying Google + Tapo + Z-Wave + Zigbee + Matter/Thread). Two-door architecture (front Kwikset Z-Wave dying → Wi-Fi/Matter; back Z-Wave keep + ESP32 puck). **Z-Wave locked as INTERIM, Matter later.** **No Thread border router in the house — hardware-confirmed** (Nest Hub 1st-gen + Chromecast 3rd-gen + Nest Audio, all Matter-over-WiFi, zero Thread radios). Front-door rec: Wi-Fi/Matter (Tapo tier) — no TBR/Google/extra-buy needed (~85%). Cypher-voice plane scoped (DIY ESP32-S3 satellites → HA Assist → Cypher LLM; can't reuse Google mics). Samsung SmartThings v3 logged as dormant (Zigbee+Z-Wave, NO Thread — redundant to HUSBZB-1; unplug it).
- Former §11 Wishlist renumbered → §13.

**Why:** Dedicated JAKE-STACK overhaul session. Goal was to interrogate every standing-infrastructure area against live ground truth and catch drift, contradictions, and unrecorded material. Net: every section now matches reality (verified against the router, on-disk systemd units, physical labels, and file timestamps rather than memory), a phantom risk was killed with a tombstone, two risk-clocks were anchored, a real security exposure was caught and dispositioned, and the entire smart-home/door layer — previously absent — was built and scoped. Several §5 self-checks corrected this-Claude's own overconfident calls mid-session (ZBT-1 "just buy it," local-MQTT "free fix," "no spare GPU"), logged here for honesty.



**Scope:** ANCHOR_apparatus v8→v9. (Pipeline v1.2 + Spec v4 unchanged on disk; the v1.3 build is queued, not yet run — pulled back into apparatus/main from the parallel lane.)

**Change(s):**
- **ANCHOR_apparatus v8→v9** — folded SCDD S5 results and ratified the parked raw.json decision in-lane:
  - **Substrate FaceOff v2 DELIVERED** (SCDD S5; supersedes stale v1). Field settled at population scale (1,982 rows, zero field-expanding candidates). Two co-leads, both dual-gate PASS: NornicDB (graph-native benchmark) + Supabase+pgvector (low-ops default). SCDD rec: Supabase-first-with-NornicDB-as-proven-upgrade-path, gated on the seed-shape test against the real archive. **Lock remains apparatus's (D9) — NOT YET LOCKED; recommendation delivered, decision open.** CONFIDENCE FLAGS: retention/retrieval substrate OPEN→v2-delivered.
  - **D21 CLOSED — round-trip empirical PASSED.** 4,122,695-byte adversarial inline string property (quotes/braces/backslashes/emoji/CJK/newlines, ≈1.37× our 3.0 MB max record) written→read byte-identical, sha256-verified, AND stable across a full container reboot (cold BadgerDB reopen); on-disk vlog survived (confirms vlog routing). NornicDB v1.1.2, maximally-inert config. NornicDB acceptance contract now 4/4 with no hedge. CONFIDENCE FLAGS: NornicDB round-trip added as CONFIRMED. Binding per-node ceiling recorded: **~16 MiB** (`walMaxEntrySize` WAL guard; ~5.3× over our 3.0 MB max) — the early "no hard cap" framing corrected; the pre-vetted "3 MB → content-block split adapter" ding CLEARED (no adapter needed). (Empirical ran on Castle Black CT 999, disposable LXC, torn down clean — see the SCDD S5 stack entry below.)
  - **raw.json Path A RATIFIED** (Jake's call, made in the apparatus/main lane; SCDD deliberately left the invariant untouched and routed it back). Scope: raw is transient — wiped after Stage 3 verify-PASS (HARD-gated on PASS; if verify fails, raw survives for debug) AND never staged to any retained or backed-up surface (not the WH HD long-term, not a repo, not a db, **never the NAS backup**). Anthropic's official export is the byte-verbatim re-pull source. The §Secrets invariant already read "raw wiped" — Path A makes code match canon; **no invariant moved.** Open "DECISION REQUIRED" block removed; CURRENT STATE + NEXT MOVE flipped to RESOLVED. Code-side (v1.2→v1.3 `raw.json` unlink) is CC/Jake's hands, rolled into the #3 build batch.
  - **Graveyard sharpened** — "NornicDB code-default-off means decay is safe" SHARPENED not killed: code default is off (decay is read-path scoring, not eviction; no GC worker on engine-open), but the shipped `nornicdb.example.yaml` sets `decay_enabled` + `auto_links_enabled` + `embedding.enabled` ON. A copy-paste vendor-example deploy silently enables a decay worker + embedder that touch frozen nodes → **D20 pin-everything-off is a HARD lock-time gate, not optional hygiene.**
  - **NEXT MOVE updated** — #1 substrate = v2-delivered/decision-open (was "imminent"); #2 v4 spec pass marked DONE (it already existed on disk — Jake landed it, the S14 handoff lagged; verified clean this session); #3 = the delta + scrub-vN + v1.1 BUILD (still unbuilt, the real build target).

**Why:** SCDD S5 closed the last substrate unknown (the byte-identical round-trip on the multi-MB string-property path — the one axis three independent dual-gate reads could only rate PASS-on-mechanism) and delivered FaceOff v2. This session folded those results to canon and ratified the raw.json decision that had been answered in this lane but not yet written (parallel-lane lag — Jake stated Path A here, SCDD couldn't see it). v9 records substrate-recommendation-delivered + D21-closed + raw.json-resolved; it does NOT lock the substrate (D9, still apparatus's, gated on the seed-shape test). The v1.3 build (delta/scrub-vN/v1.1 + raw.json wipe) is the next executable move — one batch, plan-OC/build-CC, ratify small before scale — pulled back into apparatus/main now that the parallel lane's sole justification (the blind dual-gate) is spent.

## 2026-05-28 — SCDD S5 (JAKE-STACK §2 — Castle Black)

**Scope:** JAKE-STACK §2 (Castle Black standing risks). Stack-only — the ANCHOR_apparatus v8→v9 deltas from this same SCDD session are landed separately by the apparatus/main stream; no anchor line is recorded here from the SCDD side.

**Change(s):**
- **CB thermal/CPB standing risk → RESOLVED/CLOSED.** The CPB-on + cooled live test (opened SD23 after the fan install dropped the baseline ~10°C) closed PASS. Jake confirmed 5-28: the fans hold the floor low enough that transient spikes still occur but are within tolerance and no longer trigger a panic/shutdown. The PSU-swap power-transient lane and the RAM/MemTest confound are moot unless a panic recurs CPB-on-cooled (none observed). Corroborated by a sustained Go-from-source LXC compile on a dead-idle CB (load 0.00) with zero thermal event.
- **CB backup strategy → GAP flagged, queued.** CB is now load-bearing host infra (Proxmox + VMs 100/200 + go2rtc + kiosk) and was used as a disposable-LXC test-workload host (CT 999, torn down clean), but has no regular NAS/external backup (ext4 single drive, no mirror). Owner assigned: homelab/day-state session stream (NOT apparatus/SCDD). Candidate approaches noted in-file (vzdump→NAS SMB, or PVE config+VM backup to external HD). Untriaged.

**Why:** SCDD S5 ran the NornicDB round-trip empirical on Castle Black (CT 999, disposable LXC, torn down clean), which both closed the long-running thermal live test by demonstration and surfaced that CB now carries enough real state to need its own backup. Surgical §2 edits only; no other stack facts touched.

## 2026-05-28 — apparatus S14 (second-export verification + reference pass)

**Scope:** JAKE-STACK §10 (new); Freeze_Pipeline_Spec v3→v4; ANCHOR_apparatus v7→v8.

**Change(s):**
- **JAKE-STACK §10 (new)** — documented the Anthropic conversation export as a multi-file bundle (`conversations.json` + `memories.json` + `users.json` + `projects/`), full-account point-in-time with no delta export; apparatus ingests `conversations.json` only.
- **Freeze_Pipeline_Spec v3→v4** — added §2.0 (export bundle shape & file targeting: floor = `conversations.json` only; resolve-within-dir, never the bare default source path — the silent-second-baseline trap); corrected §2.1's "no sibling files" claim (5-28 export confirmed siblings); specified §6 v1.1 field-level key-presence drift detection (per-type allowlist + one carve-out, `text.citations_grouping_mode`); marked §7 cross-export uuid-stability DONE. No architectural change; no code written this session.
- **ANCHOR_apparatus v7→v8** — S14 close enshrine: cross-export UUID stability CONFIRMED (22,801/22,801 tuples stable 5-25→5-28), field-level drift VERIFIED ZERO (population, raw-vs-raw), `display_content` characterized (NOT a universal mirror — 15.6% floor-grade; blanket-strip ruled out), record-size landmines mapped (max 3.0 MB, driven by `tool_result.content[].text`, corrects S12), key-presence vs value-presence separated. Delta fixture sized at 1,337 net-new msgs.

**Why:** S14 was a read-only verification session — pulled a second full export (5-28), confirmed cross-export uuid stability + zero schema drift at population scale, and characterized record-size + `display_content`. The export-is-a-bundle fact and the v1.1 field-detection spec are the durable reference outputs; the spec + bundle pass forward to the S15 delta/scrub-vN/v1.1 build. (CC wrote canon unprompted once this session — §7.6 violation, corrected + noodled + saved to CC memory.)

## 2026-05-25 — apparatus S2 (cross-project corpus re-architecture)

**Scope:** JAKE-RULES §8 + §5.1; Lore_Bible §5.

**Change(s):**
- **JAKE-RULES §8 (Memory / Context)** — added the project-scoped-retrieval rule: `conversation_search` / `recent_chats` / project-knowledge are scoped to the project the chat lives in; the durable stores (codeload git, CC-on-disk, Supabase) are project-agnostic. Cross-project work runs non-project (OC) + CC-on-disk, never boxed inside one project.
- **JAKE-RULES §5.1** — added "the export-`project`-field that wasn't there" to the confabulation-examples list. A corpus partition was planned on a `conversations.json` `project` field asserted from memory; CC inspecting the real 348MB export found no such field (only incidental UUID prose). The verify-before-trust gate caught it pre-build.
- **Lore_Bible §5** — added war story "The Field That Wasn't There (apparatus S2)," sibling to "The Dashboard Is Ground Truth, The Doc Is An Echo." Same lesson family: the doc/memory is an echo; the live system (here, the 348MB of bytes) wins.

**Why:** The apparatus cross-project corpus build surfaced (a) the project-scoping wall that limited every prior excavator, and (b) a clean §5.1 fire — both worth standing rules so neither is re-learned.

## 2026-05-24 — SD24 (Castle Black VM 100 monitor recovery + liveness-gap)

**Scope:** JAKE-STACK §3 (VM 100 — TheNightsWatch standing risks).

**Change(s):**
- **JAKE-STACK §3 (VM 100)** — added standing risk: `server.js`'s Node/V8 worker can *hang* (not crash) — `soft lockup CPU#0 [V8Worker:NNN]` — while the VM still reports "up" and the dashboard goes dark silently. systemd `Restart=on-failure` fires only on a crash, not a hang, so `neighborhood-watch.service` never restarts it. Recovery: `qm stop 100 && qm start 100`. Fix queued: external liveness probe (HTTP heartbeat → restart on stall). Same liveness gap previously flagged for the camera, now on the Node layer.

**Why:** Hit live at SD24 — VM 100 soft-locked on a hung V8 worker; host stayed healthy (load ~2.0, SSH fine); recovered via `qm` bounce. Logging the standing risk + the queued liveness-probe fix so the silent-dark-dashboard failure isn't re-diagnosed from scratch next time.

## 2026-05-24 — SD23 (Castle Black fan install + panic-conclusion reconciliation)

**Scope:** JAKE-STACK §2 (OS — CPB persistence line; Standing risks — panic line); plus the Castle Black hardware-state changes and the open-loops §4C sharpening logged below.

**Change(s):**
- **JAKE-STACK §2 (Standing risks)** — replaced the stale "RAM intermittent fault remains the top open suspect" line with the thermal/CPB working conclusion. Mechanism: CPB transient spikes off a high baseline; CPB-disable made it stable. SD23 fan install dropped idle baseline ~10°C; CPB came back ON this boot (persistence broke) and was deliberately LEFT ON as a live retest (CPB-on + cooled = hypothesized-safe). Stays up → thermal headroom confirmed, loop closes; hangs again CPB-on-cooled → power-transient lane → S15 PSU swap is next lever, NOT RAM. RAM demoted to optional MemTest confound-killer — never positively evidenced (no MCE logs).
- **JAKE-STACK §2 (OS)** — updated the CPB line: persistence BROKEN as of SD23 (`boost`=1 after cold boot; `/etc/rc.local` fragile on Proxmox 9/systemd, systemd unit is the durable fix). Currently left ON deliberately; durable-disable on hold until retest concludes.
- **Castle Black hardware (state, reflected in §2):** fan install done — 80mm (4-pin PWM) on sys-fan header front-intake; 60mm (2-pin) on SATA→Molex 12V rear-exhaust. Board 4MP19ME, M75s Gen 2 SFF, 4650G APU (no dGPU). NVMe idle 24.9°C (~10°C better than the external 125mm vortex it replaced — directed path beat brute-force CFM). 80mm on silicone dampener mounts; 60mm zip-tied to rear expansion rail. Box reassembled.
- **Thermistor** re-homed during install (80mm took its old mount) → standing suspect #1 for any future Castle Black thermal weirdness / fan-curve oddness / panic. Check probe placement first. (Correction logged: this chassis probe likely feeds a secondary/chassis curve, not the main blower curve which keys off CPU Tdie — placement guidance unchanged.)
- **Storage "didn't find a local pool" boot message** = benign boot-order race (LVM-thin activation + ZFS-no-pools skip + dashboard/kiosk race during the cold-boot window). Ground-truth confirmed via `pvesm status` / `qm status` / `journalctl`. Closed, not a fan-work scar.
- **Open-loops §4C sharpened:** the silent, no-error, every-switch re-read tax across ~6 parallel Claude windows is the canonical pain case — promotes colored frames-on-windows (not painted cells) to primary justified feature, decoupled from the conveyor (~½ session AHK, standalone). Terminal per-context tints = separate zero-code freebie.

**Why:** The old §2 RAM line contradicted this CHANGELOG's own 5/22 (SD20b) "panic = thermal, confirmed stable" entry and got parroted across SD23 before Jake forced a re-derivation — a §5 failure laundered through a stale doc under a fresh footer (invisible to the freshness tripwire). Reconciling §2 in the live file stops next-Claude re-inheriting it at startup step 1, before the handoff (step 3) ever corrects it.


## 2026-05-24 — Cypher S10 (soul-as-substrate: frame-promotion + genesis canonization + voice layer)

**Scope:** JAKE-RULES §1.2 + §15; Cypher docs — `Cypher_Architecture_Discussion_2026-05-11.md` (canonized), new `Cypher_Voice_and_Presence.md`, `CLAUDE.md` §2.5/§10.

**Change(s):**
- **JAKE-RULES §1.2** — rewrote "the drag is the work" from a reactive correction-pattern into a **load-first posture**: framework-default is Claude's resting state; on architecture/character/organic-diagnostic work the organic frame loads first, and the drag is failure-recovery, not the mechanism. Named the compounding cost (austere reversion session-over-session → project patterned like every other). §4's terse restatement left as the in-the-moment cue.
- **JAKE-RULES §15** — added a bullet: where a project carries a design-philosophy/character layer, it loads as framing *before* the operational reads, not as a gated project-read. Fixes the structural cause — the read order is operational-first by construction, so a philosophy layer left downstream inherits austere gravity. Project CLAUDE.md names the framing docs.
- **Genesis canonized** — the 5-11 verbatim elevated from a dated "discussion" file to CANON — GENESIS, titled **"The Track-Meet Doctrine,"** with a status block (derivative conflicts → this wins on philosophy). Filename retained as the citation anchor (rename would orphan citations frozen in archived handoffs).
- **New `Cypher_Voice_and_Presence.md`** — the operational voice layer: the missing bridge from the twelve principles to the §10 system-prompt assembly. Baseline voice block, register-reading rubric, delivery-as-voice, and the phase-gated Anchored-Phase Fence (what the 1c voice may NOT do — no faked recall, no manufactured character-revealing-wrongness). Replaces the 84KB-lore vibe-check with a buildable acceptance test.
- **CLAUDE.md §2.5/§10** — registered the framing layer (genesis + soul substrate + voice spec, load first every Cypher session) and pointed §10 at the voice spec. (Jake authors per §7.6.)

**Why:** earned at Cypher S10. A Claude that had read the entire Cypher genesis doctrine still reverted to austere within two turns and needed dragging twice. The synthetic-being frame — the project's single most critical signal — was surviving only on Jake-in-the-loop (§11 single-point-of-failure). Promoted to load-first at both tiers so the intent stops depending on per-session rescue, and the build process stops patterning the product into every-other-project. We prove the architecture by living it: the soul is substrate in the reference layer for the same reason it's substrate in Cypher.

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
