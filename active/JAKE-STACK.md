# JAKE-STACK.md

**Standing infrastructure Jake operates. Universal session context — required reading alongside JAKE-RULES.md.**

This file describes **WHAT exists.** JAKE-RULES describes **HOW to work with Jake.** Per-project CLAUDE.md describes a specific project's scope. Day-state handoffs describe tactical current state. This file is the substrate underneath all of that.

**Update cadence:** at the end of any session where standing infrastructure changes materially. Surgical edits only — never full rewrites. (This 5-29 revision is the exception: a dedicated full-stack interrogation session, Jake's express permission for a full rewrite.)

---

## 1. Workhorse — daily driver

· **Identity:** System name `JAKES_WORKHORSE`, user `jakeb`. MSI **PRO B550M-VC WIFI** (MS-7C95), BIOS H.E0 (9/2/2025), UEFI mode.
· **Role:** Primary workstation. Three-monitor station — 48" Decogear ultrawide, 29" LG widescreen, 27" HP widescreen. Jake's hands-on machine for everything.
· **CPU:** AMD Ryzen 7 5700 (8c/16t, Zen 3, ~3.7 GHz base). NOTE: 5700 **non-G** — iGPU fused off, **NO integrated graphics**; a discrete GPU is mandatory here.
· **GPU:** NVIDIA GeForce GTX 1070 (Pascal, 8GB GDDR5). Drives the 3-monitor setup. Pascal = security-only drivers now (past the feature-driver cutoff); **NOT a local-inference surface** — keep model work on cloud/API, not WH.
· **RAM:** 16 GB. Runs **tight** under the parallel-Claude + Claude Code + Bambu Studio + browser-cluster load (observed 2.12 GB free). B550M = 4 DIMM slots, up to 128 GB — headroom to grow when the parallel pool starts swapping. (Spare RAM on hand is SODIMM/laptop — NOT usable here; upgrade = a buy. See §8.)
· **OS:** Windows 11 **Pro**, Build 26200 (25H2-era).
· **Storage:**
  · **C: boot** — Samsung **SSD 870 EVO 500GB**, SATA SSD. ~465 GB usable, 55% free. Win11 set on Disk 0: EFI 200MB + C: + Recovery 794MB.
  · **D: "Cyl Storage"** — Seagate **ST2000LM007-1R8174**, 2TB, SATA HDD, 5400 RPM, 2.5" **SMR** laptop drive. 92% free. 3D-archiver `/MOVE` target + NAS-mirror D-Drive source. **SMR/5400 = archive-and-read workload only**; slicing off D: is slower than C: (this resolves the prior §5 "if D: is spinning" hedge — D: **is** spinning); **never put write-heavy/random-write load on D:** (SMR write-cliff).
· **Daily tooling:** Claude Code, Claude.ai (multiple parallel sessions), 1Password 8 (SSH agent + Environments), AHK macropad (VSD m18), Bambu Studio, browser cluster.
· **Standing background jobs (only these two — no full software manifest; regenerable via `winget list`):**
  · Scheduled task `WorkhorseNightlyNASBackup` (daily 02:00) — see §5
  · Scheduled task `3DRecipesNightlyArchive` (daily 01:00) — see §5
· **Install-default security posture (NONE deliberate — all Win11 25H2 install artifacts, per Jake):**
  · **Secure Boot: Off** (recorded state, no action).
  · **VBS/HVCI: on** (Win11 default). Hypervisor loaded → WH is a **contended hypervisor surface**. Reversible (Core Isolation off / `bcdedit /set hypervisorlaunchtype off`) IF WH ever needs to host VMs — but Castle Black is the VM host by design, so leave it. Don't propose running a competing hypervisor / local VM on WH without expecting friction.
  · **Smart App Control / App Control for Business: Enforced** (install-default). **FIRST suspect if an unsigned homelab binary or driver dies silently.** Toggle: Windows Security → App & browser control → Smart App Control.
· **Filesystem conventions:**
  · `C:\NASBackup\` — backup machinery, self-contained, `%~dp0` self-relative paths throughout
  · `C:\HA\` — homelab infrastructure files holding location
  · `C:\bambu-monitor\` — legacy local copy, retire-or-repoint queued (not load-bearing, just untidy)
  · `C:\Users\jakeb\.ssh\` — SSH config + known_hosts only; private keys live in 1PW now
  · `C:\3D Recipes` (C: SSD) + `D:\3D-Backups` (archiver target) + `C:\3D-Archive` (script home)
  · `D:\Workhorse_AllTheShit\` — catch-all on D: (e.g. `Bambu Baby Monitor` build artifacts live here)
  · Project-named folders, NOT Windows defaults. **Never assume `\downloads`** — Jake organizes by project (e.g. `C:\NASBackup\downloads\`)

---

## 2. Castle Black — Lenovo Proxmox host

### Physical
· Lenovo ThinkCentre M75s Gen 2 SFF (24/7-rated)
· AMD Ryzen 5 PRO 4650G (6c/12t, Zen 2)
· 16 GB RAM (2×8GB DDR4-3200 non-ECC UDIMM, DIMM 1 of both channels populated, dual-channel active, 2 slots open) — **confirmed unchanged 5-29**
· WD PC SN740 256 GB NVMe (stock boot drive — SMART health PASSED, 100% spare, 4% used) — **confirmed unchanged 5-29**
· **Cooling (installed — the config that CLOSED the thermal saga; case now closed, box in permanent position):**
  · CPU: **stock AMD cooler**
  · **1× 60mm** ANVISION slim-15mm, **REAR** over the empty expansion-slot ports = **INTAKE**
  · **1× 80mm**, **FRONT** internal chassis = **EXHAUST**
  · **Airflow is REVERSED from convention (rear-in / front-out) ON PURPOSE** — exploits where the box sits in the closet; the fresh air is behind it. **DO NOT "correct" to front-intake — the reversal is the point.**
  · NOTE: the 80mm was tagged "too large for SFF internal mount" in old §8 — Jake made it fit anyway. The inventory note was over-cautious; one 80mm **is** internally mounted. (Don't re-trust the old "too big" line.)
  · This rear-in/front-out pair = the ~10°C baseline drop that let CPB return on and closed the panic risk. Confirmed by the diagnostic period: case-off with the 125mm vortex blowing directly at the mobo held it until the permanent fans went in.
· **Location:** workshop closet, co-located with P1S/AMS2Pro, home-network gear, and the ~13yo Acer print-status monitor. KVM in line (HDMI run was 2 ft short of the Acer kiosk monitor).

### Identity
· **Hostname:** `thehoa.lan` ("the HOA of the LAN")
· **Static IP:** `192.168.50.250` (DHCP-reserved on RT-AX55, MAC `88:AE:DD:15:CA:D2`, label `CastleBlack`; shows as client name "MSFT 5 0" — Proxmox DHCPv6 prank)
· **SSH alias on Workhorse:** `castleblack` (via 1PW SSH agent — key generated in 1PW vault)
· **SSH note:** `ssh nightswatch` does NOT resolve **from** Castle Black — that alias lives only in Workhorse's 1PW-agent SSH config (§6). Host→VM scripting must use the IP (`192.168.50.88`) or a host-local alias, not the WH alias.

### OS
· Proxmox VE 9.1 bare metal, kernel 6.17.2-1-pve
· ext4 single drive (no mirror)
· SVM mode enabled in BIOS
· Secure Boot ON (kernel lockdown mode active — limits some hardware probing)
· CPB (Core Performance Boost) **back ON** at runtime (the SD23 fan install dropped the baseline ~10°C and CPB was re-enabled). History: was disabled via `/sys/devices/system/cpu/cpufreq/boost` during the thermal saga; no longer needed.

### Standing risks
· **Castle Black panics = thermal/CPB — RESOLVED/CLOSED (5/28, Jake-confirmed).** History: two hard hangs 5/21 AM (01:42 + ~08:25); NVMe ruled out; mechanism was CPB transient spikes off a high baseline. The SD23 fan install dropped the baseline ~10°C and CPB came back ON. The live test (CPB-on + cooled) **closed PASS:** Jake confirmed 5/28 the fans hold the floor low enough that spikes still occur but are within tolerance and no longer trigger a panic/shutdown. **The floor was lowered; the spikes are tolerable.** The power-transient/PSU-swap lane and the RAM/MemTest confound are both moot unless a panic recurs CPB-on-cooled (none observed). Corroborated 5/28 by a sustained Go-from-source LXC compile on a dead-idle box (load 0.00) with zero thermal event.
· **⚑ CB backup strategy — GAP, queued (5/28).** Castle Black is now load-bearing host infra (Proxmox + VMs 100/200 + go2rtc + kiosk) AND has been used as a disposable-LXC test-workload host (CT 999, torn down clean). It has **no regular backup to the NAS or an external drive** — ext4 single drive, no mirror. **Owner: homelab/day-state session stream.** Candidate approaches: Proxmox `vzdump` of the VMs to the NAS SMB share (`Jakes Backups`), or PVE-level config + VM backup to an external HD. Untriaged.

---

## 3. The Watch — VMs on Castle Black

### VM 100 — TheNightsWatch
**Canonical lore name.** Hostname inside VM is still `neighborhood-watch`; multi-surface rename queued. (The "TheBlackWatch" typo now appears in **4 places**: router DHCP client name, router host name, the systemd unit `Description`, and the rename backlog — see §4.)

· **Role:** Dashboard server. Status tiles. Life360 polling. Heartbeat receiver. Printer MQTT/WS. (Camera served by a co-located `go2rtc` WebRTC gateway — see below; no longer proxied through this server.)
· **OS:** Ubuntu 24.04.4 LTS Server, Node v24.15 at `/usr/bin/node`
· **IP:** `192.168.50.88` (DHCP-reserved, MAC `BC:24:11:07:69:EF`, router label `TheBlackWatch` [typo])
· **SSH alias on Workhorse:** `nightswatch` (1PW agent) — NOTE: WH-only; does not resolve from the CB host (see §2).
· **Display name in Proxmox UI:** still `bambu-monitor` — cosmetic rename queued.
· **systemd unit:** `/etc/systemd/system/neighborhood-watch.service` **v2** (verified on disk 5-29). `Restart=on-failure`, `RestartSec=5s`, enabled at boot. `NoNewPrivileges` dropped in v2 (broke ping via cap_net_raw strip in v1); other hardening preserved (`PrivateTmp`, `ProtectSystem=full`, `ProtectHome=read-only`, `ReadWritePaths=/home/jake/neighborhood-watch`). `Documentation=` line points at `https://...:8765/status` (https) while the kiosk curls `http` — cosmetic mismatch, both work.
· **VM specs:** 2 cores type=host, 4 GiB RAM, 20 GB virtio-scsi on local-lvm (iothread + discard + ssd emulation), i440fx + SeaBIOS. CD-ROM device still emulated (empty) — `ata_sff_pio_task` log noise; full removal needs a VM bounce.
· **Code:** `/home/jake/neighborhood-watch/` — `server.js` **v3.3 / SD21 (2026-05-23)** (verified on disk 5-29, unchanged), `life360.js`, `status.js`, `status.html`, `index.html` (cam tile reworked SD21), `config.json`, `l360_token_test.js`. v3.3: the ffmpeg→HLS camera pull was **removed**; `server.js` serves the dashboard, printer MQTT/WS, `/api/config`, `/api/printer`, and the kiosk routers only. Camera served by `go2rtc`. `index.html` cam tile consumes go2rtc WebRTC (raw `RTCPeerConnection` signaling).

### VM 100 — standing risks
· **`config.json` plaintext secrets — OPEN (risk-clock #1, confirmed 5-29).** Holds the **Bambu Lab account EMAIL + PASSWORD** (not merely a token) + Life360 token, in cleartext. Only Workhorse has had the 1PW treatment; VM100 is the open surface. (The go2rtc RTSP pass is already handled correctly — `go2rtc.env` `0600` via `${CAMERA_PASS}`, NOT in config.json.) Migration target: a 1PW Environment (`Personal: Homelab` per §6 naming lock), injected at service start — must respect the `ProtectHome=read-only` + `ReadWritePaths` sandbox (env-file or `op run` wrapper, not a home-dir write). **Urgency raised** now that we know it's the real account password (see §3 Bambu risk-clock + §11 security exposure).
· **V8-worker-hang risk — REMOVED 5-29 (was a phantom).** Disk sweep (server.js v3.3 unchanged, unit v2 `Restart=on-failure`, empty crontab, all-stock timers) found **no dashboard watchdog and no evidence the dashboard panels ever hung independently.** The hang Jake remembered was the **ffmpeg CAMERA-worker stall**, mislabeled as a Node/V8 hang — fixed permanently by the go2rtc swap (v3.3/SD21). The "queued dashboard liveness probe" is **CANCELLED** (it solved a problem that never existed). **DO NOT re-add from the SD24 handoff's "hit live, qm bounce" note — that event was the camera, not the panels.** (Killed by Jake + disk sweep, 5-29. The SD24 handoff carries a now-false "V8 worker hang hit live" fact — correct in PK so it stops re-seeding this.)
· **Historical — the ffmpeg "frozen-but-flowing" cam failure (SD20b; pipeline retired SD21; PERMANENTLY FIXED by go2rtc).** The old ffmpeg RTSP→HLS pull could wedge mid-stream with TCP still up — muxing the last frame forever, writing fresh `.ts` files full of a frozen frame, faster than realtime, ZERO log errors. **That pipeline is gone.** **go2rtc's own immunity to a Tapo-side wedge is still formally UNPROVEN** — but go2rtc has run continuously since the SD21 swap with **no wedge observed (Jake confirmed 5-29, "spinning constantly" with no issue).** Uptime ≠ proof of immunity; if the cam ever freezes under go2rtc, the content-freshness watchdog returns. Detector signature kept for that day: consecutive segments byte-identical in size + write cadence faster than ~1s, with all file-based checks green. **Watching.**

### go2rtc — camera WebRTC gateway (on VM 100, SD21)
· **Binary:** `/usr/local/bin/go2rtc` (v1.9.14, linux-amd64).
· **Config:** `/home/jake/go2rtc/go2rtc.yaml` — stream `printer` ← Tapo RTSP; `api.origin: "*"`; `webrtc.candidates: [192.168.50.88:8555]`. RTSP password via `${CAMERA_PASS}` from `/home/jake/go2rtc/go2rtc.env` (`0600`, jake) — NOT in the yaml.
· **Service:** systemd `go2rtc.service` (`User=jake`, enabled at boot, `Restart=on-failure`).
· **Ports:** Web UI `:1984`, WebRTC media `:8555`.
· **Footprint:** ~20 MB RAM idle, near-zero CPU (passthrough, no transcode).
· **go2rtc is the SOLE steady consumer of the Tapo** — see the §7 ~2-pull RTSP ceiling constraint.

### VM 200 — Watchtower
· **Role:** Life360 bot account host. Android-x86 9.0.
· **Status:** UP and working (confirmed 5-29 — family tiles live: Jake home 7:47a, Amber school 7:50a, Griffin current).
· **⚑ Per-member staleness flag (5-29):** Ary's tile showed "yesterday 7:52pm" when reality was "today 7:52am" — possible Life360 hiccup on her device, an AM/PM display parse issue, or an intermittent share drop. NOT a Watchtower-down condition (other members current). Watch.
· **Network:** NO DHCP reservation; not positively identifiable in the lease list (Android-x86 shows generic/blank vendor). Boot order 1; VM100 boots at order 2 with 30s startup delay so Watchtower's Life360 app reconnects before polling starts.

### Dashboard endpoint
· `http://192.168.50.88:8765/status` — tiles: NAS · Last Backup · Router · Internet · Replicator (P1S) · Family (Life360)

### Kiosk service (on Castle Black host, drives the Acer)
· `status-kiosk.service` (verified on disk 5-29): `cage` + `cog` → `:8765/status` on tty1, driving the Acer over HDMI. **`Restart=always` + `RestartSec=5`** + an `ExecStartPre` that blocks until `:8765/status` answers (`until curl -sf ...`). **This is what self-heals the "random kiosk hanging"** — a `cage`/`cog` display crash gets relaunched in 5s. (Host-side; SEPARATE from VM100. This is the fix Jake remembered — correctly attributed 5-29.)
· The two scars, for the lineage: `WLR_DRM_DEVICES` is colon-separated so PCI by-path names blow up — use `card1`; and a kiosk service needs `Conflicts=getty@tty1` or it can't wrestle DRM master off the console.

---

## 4. Network

· **Router:** ASUS RT-AX55, `192.168.50.1`
· **DHCP reservations LIVE (verified against router config 5-29 — exactly 3 in the manual-assignment table):**
  · **TheBlackWatch** `.88` — MAC `BC:24:11:07:69:EF` (typo: should be `TheNightsWatch` — wrong in 4 places: router client name, router host name, the systemd unit `Description`, rename backlog)
  · **NASBackup** `.248` — MAC `00:11:32:8E:E7:E6`
  · **CastleBlack** `.250` — MAC `88:AE:DD:15:CA:D2` (client name shows "MSFT 5 0" — Proxmox DHCPv6 prank)
· **.88/.250 DISCREPANCY — RESOLVED 5-29:** both ARE reserved. The day-state board's "DHCP reservation .88 (+.250) = open ~5-min task" was **STALE** — already done. §4 was correct.
· **⚑ GAP — Workhorse `.238` is NOT reserved.** It's a dynamic lease (MAC `FC:9D:05:04:E1:6B`), not in the manual table. WH is load-bearing (NAS backup source, go2rtc consumer, 1PW SSH origin) — **RESERVE `.238`.** [~5-min queued task, genuinely undone.]
· **⚑ CLEANUP — stale `.30 JakesRedRig`** (ASUS, MAC `04:D4:C4:03:9C:43`) = Workhorse's **OLD identity, pre-crash / pre-new-boot-drive.** SAME physical box now showing as `Jakes_Workhorse` @ `.238`. Remove the stale `.30` entry, reserve current `.238`. (NOT a separate machine; NOT related to Castle Black.)
· **Other devices on the LAN (from the lease list, not previously tracked):**
  · TP-Link device `.11` (MAC `84:D8:1B:64:B2:51`) — **the Tapo C111 printer cam** (see §7; cam IP for RTSP/go2rtc is `.199` — the `.11` is its other interface/identity; do not overwrite §7's `.199`)
  · Google/Nest device `.216` (MAC `14:C1:4E:47:93:B6`) — one of the smart-home Google devices (see §12)
  · Samsung SmartThings hub (MAC `28:6D:97:CC:24:70`) — dormant; should be unplugged (see §12)
· **DNS:** Cloudflare 1.1.1.1 / 1.0.0.1
· **Naming gotcha:** Proxmox VMs show as "MSFT 5 0" in the ASUS DHCP client list (DHCPv6 client identifier, Microsoft heritage). Set hostnames manually in the reservation form.

---

## 5. NAS + backup architecture

· **NAS:** Synology DS218J at `192.168.50.248`
· **Share name:** `Jakes Backups` (space, no apostrophe — verify with `net view` before assuming any name; cost ~90 min of SD18 debugging the wrong layer)
· **Backup code:** `C:\NASBackup\` on Workhorse — drop-and-go portable folder
  · `nightly_nas_backup.bat` v7.2
  · `generate_backup_summary.ps1` v3
  · `show_backup_summary.ps1` v2
  · `logs\` subdir
  · `downloads\` subdir (Jake's convention for inbound chat-delivered files)
· **Self-relative paths** via `%~dp0` (batch) and `$PSScriptRoot` (PowerShell) — move the folder, nothing breaks
· **UNC paths** to `\\192.168.50.248\Jakes Backups\Workhorse\{C-Drive,D-Drive}\` — replaces mapped-drive dependency for scheduled tasks
· **`cmdkey` credential:** Target `192.168.50.248`, User `Nightly` (capital N — Synology user list shows `Nightly` exactly)
· **v7.1 cmdkey pre-flight:** if the credential disappears from Credential Manager, fires heartbeat with `reason='credentials_missing'` and exits clean
· **Scheduled task:** `WorkhorseNightlyNASBackup`, `/sc daily /st 02:00 /it /f` — daily 2 AM, interactive-mode (no password since Workhorse is 24/7 with Jake logged in)
· **Heartbeat:** POSTs to `http://192.168.50.88:8765/api/backup/heartbeat` with reason field — surfaces on dashboard Last Backup tile. (This is a *reporting* heartbeat, NOT a watchdog — distinct from anything in §3.)
· **D: zero files in /MIR mode = legitimate "synchronized" state**, NOT failure. Earlier-session Claude misdiagnosed this once.
· **NOTE:** raw Bambu-monitor build tarballs are mirrored here (e.g. `bambu-monitor-v2.tar.gz` under both C-Drive and D-Drive Workhorse paths) — relevant to the §11 password-exposure remediation.

### 3D Recipes Nightly Archiver
Keeps `C:\3D Recipes` lean by sweeping cold model folders to D: while leaving the C: paths fully usable.

· **Script:** `C:\3D-Archive\Archive-3DRecipes.ps1` (v1.0, SD22). Logs in `C:\3D-Archive\logs\`. Portable — `$PSScriptRoot`-relative.
· **What it does:** nightly, any top-level folder in `C:\3D Recipes` whose newest file write is >30 days old gets `robocopy /E /MOVE`'d to `D:\3D-Backups\<name>`, then the old C: path is recreated as a **directory junction** into D:. Opens/slices/browses at its original C: path; bytes live on D:. Junctions need no admin.
· **Schedule:** Task Scheduler `3DRecipesNightlyArchive`, daily 01:00, `/it`. One hour ahead of the 02:00 NAS backup so the move settles before the mirror walks.
· **Backup interaction:** none needed. `nightly_nas_backup.bat v7.2` already has `/XJ` on both robocopy lines, so it skips the C: junctions and stores the archived content once via the D: mirror — no double-store.
· **Behavior to know:** any folder going 30 days without a file write auto-sweeps — including active projects sliced-from but not saved-to (Phoenix did this SD22; harmless via junction). Cost: slower slicing, and D: is confirmed a **5400 SMR HDD** (§1), so that cost is real, not hypothetical.
· **Escape hatch (NOT YET in the script):** to pin an active project to the C: SSD regardless of age, add a 2-line exclude list —
```powershell
$Exclude = @('Phoenix')   # active projects to keep on C: regardless of age
```
  and skip any folder whose `.Name` is in `$Exclude`. Wire this when a hot project needs SSD speed.

---

## 6. 1Password — identity infrastructure

· **Role:** Source of truth for SSH keys, secrets, environment variables. Replaces on-disk SSH keys and ad-hoc credential storage. **Only Workhorse has had the treatment so far — VM100's config.json is still plaintext (§3 risk-clock #1).**
· **Version:** app 8.12.21, `op` CLI installed via winget, desktop integration enabled
· **Vault structure (Personal):**
  · SSH keys: `SSH: Pyris GitHub`, `SSH: CCF Github`, `SSH: Cypher Github`, `SSH: The Night's Watch VM`, `SSH: Castle Black Host`
  · Environments: `Cypher: Dev` (created, populating as Cypher accrues secrets)
· **Naming conventions (locked):**
  · Environments: `Cypher: Dev`, `Cypher: Prod`, `Pyris: Website`, `Client: CCF`, `Personal: Homelab`
  · Tags only (for interactive-credential items like Porkbun, accountant, banking): `Pyris: Internal`
· **OpenSSH Authentication Agent disabled:** `Stop-Service ssh-agent; Set-Service ssh-agent -StartupType Disabled`. 1PW claims `\\.\pipe\openssh-ssh-agent`.
· **PowerShell `$PROFILE` emptied** — was auto-`ssh-add`'ing on-disk keys at every shell launch
· **On-disk private keys at `C:\Users\jakeb\.ssh\`:** legacy, scheduled for cleanup. Keep `.pub` files indefinitely; keep `config` and `known_hosts`.
· **Beta caveats logged:** 10-var-per-Environment cap, no search/sort across variables in UI, concurrency limits on local mounting.
· **SSH key import gotcha:** drag-drop on Windows imports as Document type (file attachment), invisible to the SSH agent. Use `+ New Item → SSH Key → Add Key` for proper categorization.

---

## 7. 3D print stack

· **Printer:** Bambu P1S (workshop closet, above Castle Black, below the ~13yo ACER status monitor at 1280×1024)
· **Slicer:** Bambu Studio (P1S uses X1C profile — no native P1S profile exists)
· **Heater block:** OEM Bambu Hotend assembly.
· **AMS:** AMS2 Pro, 4-slot. Has drying capabilities.
· **Camera:** Tapo C111 at `192.168.50.199` (powered independently — power-cycle is clean, doesn't touch the printer). Served to browsers via go2rtc WebRTC (sub-second; §3), NOT ffmpeg-HLS (retired SD21). (Also appears as a TP-Link device at `.11` in the lease list — §4.)
· **⚠️ ~2-pull RTSP ceiling — STANDING CONSTRAINT:** the C111 serves ~2 concurrent RTSP pulls; a 3rd starves/black-screens the others. go2rtc is the one steady puller, leaving ONE free slot (the phone Tapo app). Opening VLC, a 2nd native client, or any other heavy consumer = instant black for everyone — close one before ever concluding "the cam's broken." Root cause of the SD21 afternoon black-screen marathon (VLC left open = the 3rd puller). RTSP creds in `config.json` (plaintext) + `go2rtc.env` (`0600`).

### Bambu cloud MQTT — connection model (documented 5-29)
· The monitor connects to **Bambu's cloud MQTT broker `us.mqtt.bambulab.com:8883`** (NOT local/LAN MQTT). Chosen deliberately: the cloud has no simple REST "get printer status" endpoint — detailed temps/layers/progress only come via MQTT, and cloud MQTT avoids LAN-Only/Developer-Mode so the **Bambu Handy app keeps working**.
· **Flow:** `server.js` logs into `api.bambulab.com` with the stored **account email + password** → gets a token → connects cloud MQTT with that token. First login (Apr 11, 2026) required a **one-time 2FA code texted to Jake's phone**.
· **Risk-clock #2 — the token has a ~3-month silent expiry.** See §11.
· **Permanent-fix tradeoff (NOT a free swap):** switching to LOCAL MQTT (printer IP + LAN access code + serial) kills the token/expiry entirely — but costs LAN-Only/Dev-Mode and breaks Handy-app coexistence. Re-evaluate at token-rotation time; it's a real tradeoff, not an obvious win.

---

## 8. Hardware on-hand (parts inventory)

· **Spare PSU — OCZ700MXSP, 700W, 80 PLUS**, dual-rail 12V (25A/25A, 552W combined 12V), SN `0091...235756`. Earmarked for the Castle Black PSU-swap-test lane (currently **MOOT** — thermal closed via cooling; swap-test only revives if a panic recurs CPB-on-cooled). 700W is huge overkill for the M75s = fine for a diagnostic swap. Still needs a Lenovo→ATX adapter cable + 3D-printed bumpout to fit.
· **Spare GPU — Gigabyte GTX 950 2GB GDDR5** (`GV-N950D5-2GD` rev1.0). "Old shit" — 2015 budget card, well below the WH GTX 1070. VALUE = **emergency display-out fallback ONLY**: if the 1070 dies, this boots WH + drives monitors (degraded) until replaced. Not a perf/inference part.
· **Fans:** 1× 80mm spare remaining (one is installed as the CB front exhaust — §2); 1× 60mm ANVISION slim-15mm spare remaining (one is installed as the CB rear intake — §2).
· **125mm vortex fan w/ dimmer** — was the case-off diagnostic airflow during the CB thermal saga; **retired to inventory** once the permanent 60/80 pair went in (5-29).
· **Spare RAM — SODIMM/laptop only.** NOT compatible with Workhorse or Castle Black (both full-size DIMM). Memory upgrades require a buy.
· **OCZ Vertex 2 60GB** (install media)
· **Available drives:** PNY CS1311 240GB, Crucial BX500 240GB, Seagate Barracuda 750GB, WD Black 640GB, WD Caviar Green 1TB. (Plus the structural-support-column of HDDs accumulated over 25 years — see Lore.) Relevant to the §2 CB-backup-target decision.
· **A GIANT PILE OF MOTHERBOARD WIRES** accumulated over the last 25 years.
· **All sorts of other random shit.** Ask and Jake's probably got one on hand.

### Display surfaces / peripherals
· **Surface Pro 3 + Surface Pro 4** — cataloged for the WH/VM builds; also candidate HA wall-panels / voice-satellite displays.
· **Samsung tablet #1 — IN SERVICE.** Wall-mounted, running the digital-calendar HTML artifact (always-on pinned display). Infrastructure — has a live role.
· **Samsung tablet #2 (spare) + Asus Zenpad** — DORMANT. Candidate HA wall-panels / voice-satellite displays. Panel-stock, not in service.
· **Digital-calendar artifact** — a standalone HTML file (NOT a tablet app; built ~Mar 23, designed for an always-on pinned display). Separate from its display surface. Reference in near-chat-sessions (~Mar 23).
· **Nostromo N52** — functional. 2nd programmable input surface alongside the WH AHK macropad (VSD m18); candidate homelab/HA control pad.
· **Net takeaway:** a small fleet of dormant display surfaces (2 Surfaces + spare Samsung + Zenpad) + one proven in-service calendar tablet = **zero need to buy HA wall panels** when the smart-home layer goes live.

---

## 9. Email identity routing

Each working identity has a specific email address. Routing depends on whether the touch is **persona-side** (the project communicating with Jake-as-person) or **dev-side** (Jake as system operator).

### 9.1 Per-project map
· **Pyris** — `jake@pyrisconsulting.com` for everything (no split — single business identity).
· **CCF** — `jake@ccfrecruiting.com` (primary), `tech@ccfrecruiting.com` (tech-stack logins).
· **Cypher / Ordo / Jango** — split. See §9.2.
· **Personal default** — `jake.botticello@gmail.com`. (Also the Bambu Lab account email — see §11.)

### 9.2 Cypher persona / dev split
· **Persona-side touches → `jake.botticello@gmail.com`.** The project communicating with Jake-the-person. Daily nudges, anchored-fact reflections, balance-low alerts.
· **Dev-side touches → `jake@ethosteleos.dev`.** Jake as system operator. GCP project ownership, OAuth test-user identity for the Jango role, Anthropic console for the Cypher-tenant API key, infrastructure-vendor accounts.
· Jim's side has no split — `jim@ethosteleos.dev` for everything Ordo-related.

---

## 10. Anthropic conversation export (data source)

Requesting a data export from Anthropic yields a **multi-file bundle**, not a single file. Observed shape (5-28-26): `conversations.json` (the full message stream — the apparatus floor input), `memories.json` (model-generated cross-chat memory — derived, reworded, not verbatim), `users.json` (account reference), and a `projects/` folder (per-project metadata: name, description, prompt_template, docs).

· The export is **full-account point-in-time** — every request re-exports everything as of that moment; no incremental/delta export.
· Conversations deleted before an export will not appear in it. A sealed local snapshot is the only durable copy of since-deleted conversations.
· Apparatus ingests `conversations.json` **only**; the siblings are reference/derived and stay out of the floor. Targeting + drift handling live in apparatus canon (`Freeze_Pipeline_Spec` §2.0).

---

## 11. Standing risk-clocks & security exposures

### Risk-clock #1 — `config.json` plaintext secrets (OPEN)
VM100 `/home/jake/neighborhood-watch/config.json` holds the **Bambu Lab account email + password** + Life360 token in cleartext. Only Workhorse has had 1PW treatment. Migrate to a `Personal: Homelab` 1PW Environment, injected at service start (respect the `ProtectHome` sandbox — env-file or `op run`, not a home-dir write). See §3/§6.

### Risk-clock #2 — Bambu cloud MQTT token (CONFIRMED + DATED 5-29, disk-anchored)
· **Creation date: ~April 11, 2026 — DISK-CONFIRMED.** `bambu-monitor-v2.tar.gz` (the local→cloud MQTT switch build) is timestamped **4/11/2026 6:32 AM** across 4 locations (WH desktop, `D:\Workhorse_AllTheShit\Bambu Baby Monitor`, both NAS mirrors). The cloud-auth credential handoff happened in that same session. (Filesystem mtime + setup chat = ground truth, not a Claude's claim — §5.1 satisfied.)
· **Mechanism:** stored email+password → token from `api.bambulab.com` → cloud MQTT `us.mqtt.bambulab.com:8883`. One-time 2FA text on first login (Apr 11). ~3-month silent token expiry.
· **Clock (now real):** armed ~Apr 11 → expires **~mid-July 2026.** Watch window: early July. Reauth = re-run login → NEW 2FA text → fresh token.
· **Interim:** calendar reminder ~July 1, 2026 — wording must be **"re-auth + ROTATE password + put in 1PW,"** not just "re-auth" (see exposure below).
· **Permanent-fix tradeoff:** local MQTT kills the clock but breaks Handy coexistence (§7). Not a free swap.

### Security exposure — Bambu Lab account password spilled to chat (logged 5-29)
· Jake's **real** Bambu Lab account password (`jake.botticello@gmail.com`) was entered **into chat** during the Apr-11 cloud-MQTT setup, at a prior Claude's request (that Claude violated the flag-early rule — no warning given). Now exists in: chat transcript / any `conversations.json` export since 4/11; `config.json` plaintext on VM100; possibly inside `bambu-monitor-v2.tar.gz` across 4 backup locations incl. both NAS mirrors.
· **Severity:** highest *actual* severity item in the stack — a password unlocks the account itself (above the token clock).
· **Remediation = rotate.** A spilled password is only dangerous while valid; rotating makes every copy worthless (no need to scrub archives in a panic). Rotation also forces a fresh token → cleanly re-anchors risk-clock #2 to the rotation date.
· **Jake's decision (5-29):** rotate **at the next token reauth (~mid-July)**, not now — bundles the 2FA (Bambu is strict about new-device 2FA). **Accepted risk:** spilled password stays valid ~6 weeks. **Guardrail:** the July reauth MUST include rotation + route the new password through 1PW (not plaintext re-entry), or the spill rides another 3-month cycle.
· **Rules/Lore candidate:** "never enter a real account password into chat to configure a service — Claude scaffolds config.json with a PLACEHOLDER, Jake fills the secret locally/via 1PW." Flag-early teaching example.

### Asset log — ELEGOO ESP-32 Super Starter Kit (in hand, ~5-29) — UNSCOPED, do not plan
· Earmarked: back-door NFC-puck unlock + green/red lock-status light, riding the back Z-Wave lock via HUSBZB-1 → HA.
· The kit's onboard reader is an **RC522 = RFID/MIFARE, NOT full NFC.** If the build goes phone-tap, the read path needs rethinking (passive NFC tag in puck + phone-as-reader ≠ RC522 + fob). Footnote when scoped, not a decision.
· **Doubles as the training-wheels build for the DIY voice-satellite skill tree** (ESP32+ESPHome+HA common substrate — see §12). One ladder.

---

## 12. Smart home / home automation (NEW — built from interrogation 5-29)

**Master architecture:** **Home Assistant is the master controller** — the only platform that unifies Google + Tapo/TP-Link + Z-Wave + Zigbee + Matter/Thread under one roof. HA lives on **VM 300 (Castle Black, Phase 8, NOT live yet).** Devices report to HA; Google/Tapo are demoted to endpoints, not backbone (the "route around Google" principle, confirmed all session). Jake picked the right brain — it just isn't lit up yet.

### Radios
· **Z-Wave + Zigbee → HUSBZB-1 (OWNED).** Covers both door locks (while Z-Wave) + any Zigbee device. No buy.
· **Thread/Matter → only needed IF choosing Thread locks.** Candidate: HA Connect **ZBT-2** (~$35, the current first-class HA Thread border router). NOTE: ZBT-1 → Thread is HA-officially-discouraged (recommends Zigbee on it; Thread is manual/WIP; one-protocol-at-a-time). **The dormant Samsung SmartThings v3 is NOT a Thread border router** (see below) — does not zero this buy.

### Doors — TWO doors, distinct paths
· **Front door:** Kwikset Z-Wave lock, **dying batteries (~3 days)** because only Ary's PC is close enough for Z-Wave to reach it. Decided fix: replace with Wi-Fi/Matter, drop HUSBZB-1 from that door's path; tier not yet picked.
· **Back door:** keep the old Z-Wave lock (can't afford to replace) → rides HUSBZB-1 → HA → ESP32 NFC-puck + status-light operator on top (UNSCOPED — §11 asset log).
· **Z-WAVE IS INTERIM, NOT FINAL (locked 5-29):** keep both locks Z-Wave via HUSBZB-1 for now (afford-it tier); migrate to Matter when budget allows. **Known expiry** on the Z-Wave layer — at migration, the back-door ESP32 read-path gets re-architected (Z-Wave dependency retires). Don't treat Z-Wave as permanent infra.

### Front-door Matter path analysis (researched 5-29, HA docs current to 2026.5)
· A Thread border router is required **only** for Thread-based Matter locks; **Wi-Fi Matter locks need none** — HA is Matter-certified and controls Matter-over-WiFi natively.
· **There is NO Thread border router in the house — hardware-confirmed 5-29.** Every Google device ID'd: Nest Hub **1st-gen** (FCC `A4RH1A`, Fuchsia/Cast-based), Chromecast **3rd-gen** (HDMI puck), Nest Audio — all Matter-over-WiFi at best, **zero Thread radios.** No Nest Hub 2nd-gen / Hub Max / Nest Wifi Pro / Google TV Streamer anywhere. (Settled, do-not-relitigate — hardware-verified, not memory.)
· **The "Google TV Streamer for Thread" idea = "workable but not great"** (Jake's recalled verdict, confirmed): Google owns the Thread credentials → re-introduces the dependency the door arch avoids.
· **RECOMMENDATION (OC, ~85%):** for ONE front-door lock, **Wi-Fi/Matter (Tapo DL110 tier) is strongest** — no TBR, no Google, no immature-Thread UX, no extra buy. Reserve a ZBT-2 Thread backbone for IF the smart home grows many battery Thread devices. Don't buy Thread infra for a single door. (Aligns with don't-climb-the-price-ladder.) **Jake's tier decision: open.** Tiers in play: Tapo DL110 ~$100 / Aqara U200+ZBT-1 ~$200 / Yale Assure 2 premium.

### Voice control plane — "talk to Cypher, not Google" (scoped 5-29)
· **Cannot reuse Google mics** — the Nest mic is hard-locked to Google Assistant + Google cloud; no third-party mic tap exists. Requires voice hardware Jake owns.
· **DECISION: build ESP32-S3 voice satellites himself** (NOT HA Voice Preview buys).
· **Pipeline:** ESP32-S3 satellite → HA Assist (local wake word → STT → intent routed to an LLM = the **Cypher hook**) → HA controls all bridged devices **including** the Google ones. Jake talks to Cypher; Cypher reaches Google devices through HA; never uses Google's mic/assistant.
· **Skill-tree link:** ESP32+ESPHome+HA is the common substrate for BOTH the back-door puck AND the voice satellites — the door puck de-risks the voice project. One ladder.
· **Downstream flag:** whole-house voice coverage is the expensive part (≈1 satellite per room). Start 1–2 high-traffic rooms; don't blanket the house day one. Separate project layer from the locks — locks can ship on HA first.

### Google device inventory (all Matter-over-WiFi endpoints; demoted to speakers/cast/displays)
· Nest Hub 1st-gen (FCC `A4RH1A`) · Chromecast 3rd-gen · Nest Audio. Device `.216` (MAC `14:C1:4E:47:93:B6`) is one of these. Mics become irrelevant to the control plane once HA + Cypher-voice is live (could be muted/disabled).

### Dormant asset — Samsung SmartThings Hub v3
· M/N `IM6001-V3P`, SKU `GP-AEOHUBV3LUS`, MAC `28:6D:97:CC:24:70` (Aeotec-mfg, 2018). Radios: **Zigbee + Z-Wave Plus. NO Thread, NO Matter** (predates both).
· Does NOT provide a Thread border router (eventual Matter-over-Thread migration still needs a ZBT-2). Also **redundant** — its Zigbee + Z-Wave radios are exactly what the HUSBZB-1 already gives HA; a 2nd controller would just contend.
· History: bought years ago for a lock connection; failed to pair 2–3× in a week (likely cloud-dependence / range / enrollment), abandoned-but-powered since. Its cloud-hub failure is a data point FOR the local-first HA architecture.
· **DISPOSITION: unplug it** (idle for years, adding 2.4GHz/Zigbee RF noise). Keep only as a HUSBZB-1 stopgap spare; otherwise e-waste/sell.

### Tapo / TP-Link
· Tapo C111 printer cam (§7). Newer Tapo/TP-Link models are Matter-capable; route any of them through HA's local integration (drop the TP-Link cloud) once HA is live.

---

## 13. Homelab/Maker Wishlist
Rationale: §17.5d infra-sweep. 15 off-target-for-apparatus but in-wheelhouse finds surfaced in the catalog dig. Several are functional homelab infra. Full list + URLs in `apparatus_delta_menu_S3.xlsx` → "Personal Finds" sheet. Highlights:

- `esp32_nat_router` (the original NEED) · `esp-mcp` · `m5-paper-buddy` (ESP32/e-ink) — ESP32 lane
- `homebutler` (homelab-from-chat, single Go binary) · `tailclaude` (CC over your Tailscale) — homelab/network, both HIGH
- `mcp-3D-printer-server` (Bambu/P1S) · `freecad-mcp` · `blender-open-mcp` — 3D/maker lane
- `mcp-server-synology` (DS218J lane) · `mcp-arr` (NAS media) — NAS lane
- (skip `mikrotik-mcp` — RouterOS, not the RT-AX55)

---

*Last Update: 5-29-26 by Jake + JAKE-STACK overhaul Claude. **Full-file revision** (Jake's express permission) — dedicated stack-interrogation session. Changes: §1 Workhorse fully specced (MSI B550M / Ryzen 7 5700 no-iGPU / GTX 1070 / 16GB-tight / 870 EVO boot + 2TB SMR D: / Win11 Pro / 3 install-default security flags). §2 CB hardware confirmed unchanged + cooling documented (stock cooler + reversed-airflow 60mm-rear-intake/80mm-front-exhaust pair, case closed, permanent position). §3 V8-worker-hang risk REMOVED as a phantom (disk-verified; was the ffmpeg cam-worker stall fixed by go2rtc; SD24 handoff carries a false fact to correct in PK); kiosk Restart=always correctly attributed; go2rtc stable-but-immunity-unproven; config.json sharpened to real account creds; host→VM ssh-alias note. §4 .88/.250 discrepancy RESOLVED (day-state board was stale, §4 right); WH .238 unreserved GAP + stale .30 JakesRedRig cleanup; .11/.216/SmartThings devices logged. §5 NAS = DS218J explicit; SMR cost made real; tarball-mirror note. §7 Bambu cloud-MQTT model documented + local-MQTT tradeoff. §8 PSU specced (OCZ700MXSP 700W 80+), spare GPU added (GTX 950 fallback-only), fans reconciled to installed/spare, 125mm vortex retired, SODIMM-only RAM, display-surface fleet logged. NEW §11 risk-clocks & exposures (config.json OPEN; Bambu token disk-anchored to Apr-11 → ~mid-July expiry; password-spill exposure + rotate-at-July decision; ESP32 asset). NEW §12 smart-home (HA-as-master architecture, two-door interim-Z-Wave/Matter-later, no-TBR-confirmed, Wi-Fi-Matter front-door rec, Cypher-voice plane, Google inventory, SmartThings-v3 dormant). Former §11 Wishlist → §13.*

*Prior: 5-28-26 by Jake + SCDD S5 Claude. §2 — CB thermal/CPB RESOLVED/CLOSED; added CB-backup-strategy GAP. Surgical edits. Earned by the SCDD NornicDB round-trip empirical (CT 999 on CB, torn down clean).*

*Prior: 5-28-26 by Jake & Chronicler Claude (TWSS SCDD S3 Claude) to add "Homelab/Maker Wishlist" section.*

*Prior: 5-28-26 by apparatus S14 (Jake + orchestrator-Claude). §10 added — the Anthropic conversation export is a multi-file bundle, full-account point-in-time, no delta export; apparatus ingests `conversations.json` only. Surgical edit only.*

*5-24-26 by Jake + SD24 Claude. SD24 folded in: §3 V8-worker hang note [NOTE: this risk was REMOVED 5-29 as a phantom — see §3]. SD21+SD22: cam migrated off ffmpeg/HLS onto go2rtc/WebRTC; Workhorse .238 pinned; 3D Recipes Nightly Archiver added; Tapo C111 ~2-pull ceiling documented.*

*Prior: 5-22-26 by Jake. SD20b: corrected TheNightsWatch code versions, logged the ffmpeg SIGTERM slow-kill + frozen-but-flowing failure mode.*
