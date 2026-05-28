# JAKE-STACK.md

**Standing infrastructure Jake operates. Universal session context — required reading alongside JAKE-RULES.md.**

This file describes **WHAT exists.** JAKE-RULES describes **HOW to work with Jake.** Per-project CLAUDE.md describes a specific project's scope. Day-state handoffs describe tactical current state. This file is the substrate underneath all of that.

**Update cadence:** at the end of any session where standing infrastructure changes materially. Surgical edits only — never full rewrites.

---

## 1. Workhorse — daily driver

· **Role:** Primary workstation. Three-monitor station. Jake's hands-on machine for everything.  48" ultrawidescreen (Decogear), 29" widescreen (LG), 27" widescreen (HP).
· **OS:** Windows 11.
· **Daily tooling:** Claude Code, Claude.ai (multiple parallel sessions), 1Password 8 (SSH agent + Environments), AHK macropad (VSD m18), Bambu Studio, browser cluster.
· **Filesystem conventions:**
  · `C:\NASBackup\` — backup machinery, self-contained, `%~dp0` self-relative paths throughout
  · `C:\HA\` — homelab infrastructure files holding location
  · `C:\bambu-monitor\` — legacy local copy, retire-or-repoint queued (not load-bearing, just untidy)
  · `C:\Users\jakeb\.ssh\` — SSH config + known_hosts only; private keys live in 1PW now
  · Project-named folders, NOT Windows defaults. **Never assume `\downloads`** — Jake organizes by project (e.g., `C:\NASBackup\downloads\`)

---

## 2. Castle Black — Lenovo Proxmox host

### Physical
· Lenovo ThinkCentre M75s Gen 2 SFF (24/7-rated)
· AMD Ryzen 5 PRO 4650G (6c/12t, Zen 2)
· 16 GB RAM (2×8GB DDR4-3200 non-ECC UDIMM, DIMM 1 of both channels populated, dual-channel active, 2 slots open)
· WD PC SN740 256 GB NVMe (stock boot drive — SMART health PASSED, 100% spare, 4% used)
· **Location:** workshop closet above P1S, KVM in line (HDMI run was 2 ft short of Acer kiosk monitor)

### Identity
· **Hostname:** `thehoa.lan` ("the HOA of the LAN")
· **Static IP:** `192.168.50.250` (DHCP-reserved on RT-AX55, MAC `88:AE:DD:15:CA:D2`, label `CastleBlack`)
· **SSH alias on Workhorse:** `castleblack` (via 1PW SSH agent — key generated in 1PW vault)

### OS
· Proxmox VE 9.1 bare metal, kernel 6.17.2-1-pve
· ext4 single drive (no mirror)
· SVM mode enabled in BIOS
· Secure Boot ON (kernel lockdown mode active — limits some hardware probing)
· CPB (Core Performance Boost) disabled at runtime via `/sys/devices/system/cpu/cpufreq/boost` — eliminates transient thermal spikes. Persistent via `/etc/rc.local` (or systemd unit).

### Standing risks
· **Castle Black panics = thermal/CPB, working conclusion (5/22, holding).** Two hard hangs 5/21 AM (01:42 + ~08:25). NVMe ruled out. Mechanism: CPB transient spikes off a high baseline. **CPB-disable made it stable; SD23 fan install dropped the baseline ~10°C and CPB came back ON this boot — now running as a live test (CPB-on + cooled = the hypothesized-safe condition).** Uptime over coming days decides it: stays up → thermal headroom confirmed, loop closes. Hangs again CPB-on-cooled → power-transient lane → PSU swap (see below), NOT RAM. RAM was never positively evidenced (no MCE logs) — demoted from "top suspect" to optional overnight MemTest confound-killer.
· **Bambu cloud MQTT auth token** has a ~3-month silent expiration clock — no creation date logged historically.

---

## 3. The Watch — VMs on Castle Black

### VM 100 — TheNightsWatch
**Canonical lore name.** Hostname inside VM is still `neighborhood-watch`; multi-surface rename queued.

· **Role:** Dashboard server. Status tiles. Life360 polling. Heartbeat receiver. Printer MQTT/WS. (Camera is served by a co-located `go2rtc` WebRTC gateway — see below; it is no longer proxied through this server.)
· **OS:** Ubuntu 24.04.4 LTS Server, Node v24.15 at `/usr/bin/node`
· **IP:** `192.168.50.88` (DHCP-reserved, MAC `BC:24:11:07:69:EF`)
· **SSH alias on Workhorse:** `nightswatch` (1PW agent)
· **Display name in Proxmox UI:** still `bambu-monitor` — cosmetic rename queued.
· **systemd unit:** `/etc/systemd/system/neighborhood-watch.service` v2. `NoNewPrivileges` dropped (broke ping via cap_net_raw strip in v1); other hardening preserved (`PrivateTmp`, `ProtectSystem=full`, `ProtectHome=read-only`, `ReadWritePaths` carve-out). `Restart=on-failure`, `RestartSec=5s`, `enable`d at boot.
· **VM specs:** 2 cores type=host, 4 GiB RAM, 20 GB virtio-scsi on local-lvm (iothread + discard + ssd emulation), i440fx + SeaBIOS. CD-ROM device still emulated (empty) — causes `ata_sff_pio_task` log noise; full removal needs VM bounce.
· **Code:** `/home/jake/neighborhood-watch/` — `server.js` v3.3, `life360.js` v1.2, `status.js` v2.4, `status.html` v2.2, `index.html` (cam tile reworked SD21), `config.json`, `l360_token_test.js`. **v3.3 (SD21):** the ffmpeg→HLS camera pull was **removed** — `server.js` now serves the dashboard, printer MQTT/WS, `/api/config`, `/api/printer`, and the kiosk routers only. The camera is served by `go2rtc` (see below). `index.html` cam tile rewritten to consume go2rtc WebRTC (raw `RTCPeerConnection` signaling). `.bak.sd21` rollbacks of both on the VM.
· **Standing risk:** `config.json` holds plaintext secrets (Bambu camera creds, Life360 token). 1PW Environment migration queued.
· **Standing risk — V8 worker can hang (not crash); systemd won't catch it.** `server.js`'s Node/V8 worker can soft-lock (`soft lockup CPU#0 [V8Worker:NNN]`) while the VM still reports "up" — the dashboard/status pages go dark silently. `Restart=on-failure` fires only on a *crash*, not a *hang*, so `neighborhood-watch.service` never restarts it. Recovery: `qm stop 100 && qm start 100` from the host (or restart the service inside the VM). Fix queued: an external liveness probe (HTTP heartbeat → restart on stall) — same liveness gap flagged for the camera, now on the Node layer. (SD24: hit live; host stayed healthy [load ~2.0, SSH fine], recovered via `qm` bounce.)
· **Historical risk — the ffmpeg "frozen-but-flowing" cam failure (SD20b; pipeline retired SD21).** The old ffmpeg RTSP→HLS pull could wedge mid-stream with the TCP connection still up — ffmpeg muxing the last frame forever, writing fresh `.ts` *files* full of a frozen *frame*, faster than realtime, with ZERO log errors. That pipeline is **gone** as of the go2rtc migration. **It is UNPROVEN whether go2rtc is immune to the same Tapo-side wedge** — if the cam freezes under go2rtc, the content-freshness watchdog idea returns. Detector signature, kept for that day: consecutive segments **byte-identical in size** + write cadence faster than ~1s, with all file-based checks (`find -newermt`, mtimes, segment count) reporting green because they measure the file, not the frame.

### go2rtc — camera WebRTC gateway (on VM 100, SD21)
· **Binary:** `/usr/local/bin/go2rtc` (v1.9.14, linux-amd64).
· **Config:** `/home/jake/go2rtc/go2rtc.yaml` — stream `printer` ← Tapo RTSP; `api.origin: "*"` (cross-origin from the `:8765` dashboard); `webrtc.candidates: [192.168.50.88:8555]`. RTSP password injected via `${CAMERA_PASS}` from `/home/jake/go2rtc/go2rtc.env` (`0600`, jake) — **NOT** in the yaml.
· **Service:** systemd `go2rtc.service` (`User=jake`, enabled at boot, `Restart=on-failure`).
· **Ports:** Web UI `:1984`, WebRTC media `:8555`.
· **Footprint:** ~20 MB RAM idle, near-zero CPU (passthrough, no transcode — far lighter than the old ffmpeg HLS transcode).
· **go2rtc is now the SOLE steady consumer of the Tapo** — see the §7 ~2-pull RTSP ceiling constraint.

### VM 200 — Watchtower
· **Role:** Life360 bot account host. Android-x86 9.0.
· **Boot order:** 1. TheNightsWatch boots at order 2 with 30s startup delay — gives Watchtower's Life360 app time to reconnect before polling starts.

### Dashboard endpoint
· `http://192.168.50.88:8765/status` — tiles: NAS · Last Backup · Router · Internet · Replicator (P1S) · Family (Life360)

### Kiosk service
· Castle Black now runs a status-kiosk.service (cage+cog→:8765/status) on tty1, driving the Acer.
· The two scars, for the lineage: WLR_DRM_DEVICES is colon-separated so PCI by-path names blow up — use card1 (+ a udev alias later if you want renumber-safety); and a kiosk service needs Conflicts=getty@tty1 or it can't wrestle DRM master off the console. Both cost us a cycle; both worth a Lore Bible line so the next Claude doesn't re-buy them.

---

## 4. Network

· **Router:** ASUS RT-AX55, `192.168.50.1`
· **DHCP reservations live:**
  · Castle Black `.250` — MAC `88:AE:DD:15:CA:D2`, label `CastleBlack`
  · TheNightsWatch `.88` — MAC `BC:24:11:07:69:EF`, label `TheBlackWatch` (typo, cleanup queued — should be `TheNightsWatch`)
  · NAS `.248` — pre-existing, label `NASBackup`
  · Workhorse `.238` — surfaced SD21 via a go2rtc consumer `remote_addr`; confirm/reserve if not already.
· **DNS:** Cloudflare 1.1.1.1 / 1.0.0.1
· **Naming gotchas:** Proxmox VMs show up in ASUS DHCP client list as "MSFT 5 0" (Proxmox's DHCPv6 client identifier includes that string — Microsoft heritage prank). Set hostnames manually in the reservation form.

---

## 5. NAS + backup architecture

· **NAS:** Synology at `192.168.50.248`
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
· **v7.1 cmdkey pre-flight:** if credential disappears from Credential Manager, fires heartbeat with `reason='credentials_missing'` and exits clean
· **Scheduled task:** `WorkhorseNightlyNASBackup`, `/sc daily /st 02:00 /it /f` — daily 2 AM, interactive-mode (no password since Workhorse is 24/7 with Jake logged in)
· **Heartbeat:** POSTs to `http://192.168.50.88:8765/api/backup/heartbeat` with reason field — surfaces on dashboard Last Backup tile
· **D: zero files in /MIR mode = legitimate "synchronized" state**, NOT failure. Earlier-session Claude misdiagnosed this once.

### 3D Recipes Nightly Archiver

Keeps `C:\3D Recipes` lean by sweeping cold model folders to D: while leaving the C: paths fully usable.

· **Script:** `C:\3D-Archive\Archive-3DRecipes.ps1` (v1.0, SD22). Logs in `C:\3D-Archive\logs\`. Portable — `$PSScriptRoot`-relative.
· **What it does:** nightly, any top-level folder in `C:\3D Recipes` whose *newest file write* is >30 days old gets `robocopy /E /MOVE`'d to `D:\3D-Backups\<name>`, then the old C: path is recreated as a **directory junction** into D:. The folder still opens / slices / browses at its original C: path; the bytes live on D:. Junctions need no admin.
· **Schedule:** Task Scheduler `3DRecipesNightlyArchive`, daily 01:00, `/it` (interactive, runs in Jake's session). One hour ahead of the 02:00 NAS backup so the move settles before the mirror walks.
· **Backup interaction:** none needed. `nightly_nas_backup.bat v7.2` already has `/XJ` on both robocopy lines, so it skips the junctions on C: and stores the archived content once via the D: mirror — no double-store.
· **Behavior to know:** *any* folder going 30 days without a file write auto-sweeps — including active projects that are sliced-from but not saved-to (Phoenix did this SD22; harmless via junction). The only real cost is slower slicing if D: is a spinning disk.
· **Escape hatch (NOT YET in the script):** to pin an active project to the C: SSD regardless of age, add a 2-line exclude list —
```powershell
$Exclude = @('Phoenix')   # active projects to keep on C: regardless of age
```
  and skip any folder whose `.Name` is in `$Exclude`. Wire this when a hot project needs SSD speed.

---

## 6. 1Password — identity infrastructure

· **Role:** Source of truth for SSH keys, secrets, environment variables. Replaces on-disk SSH keys and ad-hoc credential storage.
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

· **Printer:** Bambu P1S (workshop closet, above Castle Black, below Status Monitor monitor (~13 yo ACER, 1280x1024)
· **Slicer:** Bambu Studio (P1S uses X1C profile — no native P1S profile exists)
· **Heater block:** now OEM Bambu Hotend assembly.
· **AMS:** standard 4-slot.  AMS2Pro. Has drying capabilities.
· **Camera:** Tapo C111 at `192.168.50.199` (powered independently — power-cycle is clean, doesn't touch the printer). **Served to browsers via go2rtc WebRTC** (sub-second; see §3 go2rtc subsection), NOT ffmpeg-HLS (retired SD21). **⚠️ ~2-pull RTSP ceiling — STANDING CONSTRAINT:** the C111 serves ~2 concurrent RTSP pulls; a 3rd starves/black-screens the others. go2rtc is the one steady puller, leaving ONE free slot (the phone Tapo app). Opening VLC, a 2nd native client, or any other heavy consumer = instant black for everyone — close one before ever concluding "the cam's broken." This ceiling was the root cause of the SD21 afternoon black-screen marathon (VLC left open = the 3rd puller). RTSP creds in `config.json` (plaintext) + `go2rtc.env` (`0600`).

---

## 8. Hardware on-hand (parts inventory)

· Spare 700/750W ATX PSU (for Lenovo swap-test; requires Lenovo→ATX adapter cable + 3D-printed bumpout)
· 2x 80mm fans (external-only — too large for SFF chassis internal mount)
· 1x 125mm vortex fan with dimmer switch (current diagnostic-mode closet airflow, NOT permanent)
· ANVISION 60mm 2-pack (arriving 5/21/26 — slim 15mm thick, dual ball bearing, 2-pin 2.5mm connector, 17.6 CFM @ 4000 RPM @ 30.7 dBA)
· OCZ Vertex 2 60GB (install media)
· PNY CS1311 240GB, Crucial BX500 240GB, Seagate Barracuda 750GB, WD Black 640GB, WD Caviar Green 1TB (available drives)
· A GIANT PILE OF MOTHERBOARD WIRES ACCUMULATED OVER THE LAST 25 YEARS
· The structural support-column of hard drives accumulated over the last 25 years - reference in LORE.md
· All sorts of other random shit.  Ask and Jake's probably got one on hand.

## 9. Email identity routing

Each working identity has a specific email address. Routing depends on whether the touch is **persona-side** (the project communicating with Jake-as-person) or **dev-side** (Jake as system operator).

### 9.1 Per-project map

· **Pyris** — `jake@pyrisconsulting.com` for everything (no split — single business identity).
· **CCF** — `jake@ccfrecruiting.com` (primary), `tech@ccfrecruiting.com` (tech-stack logins).
· **Cypher / Ordo / Jango** — split. See §9.2.
· **Personal default** — `jake.botticello@gmail.com`.

### 9.2 Cypher persona / dev split

Cypher and Ordo are personal tools (Cypher) and operator-facing tools (Ordo, Jango). The address depends on which surface is acting:

· **Persona-side touches → `jake.botticello@gmail.com`.** The project communicating with Jake-the-person. Daily nudges, anchored-fact reflections, balance-low alerts, anything where the project is the speaker and Jake is the human listener.
· **Dev-side touches → `jake@ethosteleos.dev`.** Jake as system operator. GCP project ownership, OAuth test-user identity for the Jango role, Anthropic console for the Cypher-tenant API key, infrastructure-vendor accounts.

Same human, two surfaces. The split mirrors how Jake thinks about Cypher-as-tool vs Cypher-as-system.

Jim's side has no split — `jim@ethosteleos.dev` for everything Ordo-related.

---

## 10. Anthropic conversation export (data source)

Requesting a data export from Anthropic yields a **multi-file bundle**, not a single file. Observed shape (5-28-26): `conversations.json` (the full message stream — the apparatus floor input), `memories.json` (model-generated cross-chat memory — *derived*, reworded, not verbatim), `users.json` (account reference), and a `projects/` folder (per-project metadata: name, description, prompt_template, docs).

· The export is **full-account point-in-time** — every request re-exports everything as of that moment; there is no incremental/delta export option.
· Conversations deleted from the account before an export will not appear in it. A sealed local snapshot is therefore the only durable copy of since-deleted conversations.
· Apparatus ingests `conversations.json` **only**; the siblings are reference/derived and stay out of the floor. Targeting + drift handling live in apparatus canon (`Freeze_Pipeline_Spec` §2.0).

## 11. Homelab/Maker Wishlist
Rationale: §17.5d infra-sweep. 15 off-target-for-apparatus but in-wheelhouse finds surfaced in the catalog dig. Several are functional homelab infra (NAS/Tailscale/homelab-control). Full list + URLs in apparatus_delta_menu_S3.xlsx → "Personal Finds" sheet. Highlights to memorialize:

- esp32_nat_router (the original NEED) · esp-mcp · m5-paper-buddy (ESP32/e-ink) — ESP32 lane
- homebutler (homelab-from-chat, single Go binary) · tailclaude (CC over your Tailscale) — homelab/network, both HIGH
- mcp-3D-printer-server (Bambu/P1S) · freecad-mcp · blender-open-mcp — 3D/maker lane
- mcp-server-synology (DS218J lane) · mcp-arr (NAS media) — NAS lane
- (skip mikrotik-mcp — RouterOS, not the RT-AX55)

---

*Last Update: 5-28-26 by Jake & Chronicler Claude (TWSS SCDD S3 Claude) to add "Homelab/Maker Wishlist" section.


*Prior: 5-28-26 by apparatus S14 (Jake + orchestrator-Claude). §10 added — the Anthropic conversation export is a multi-file bundle (`conversations.json` + `memories.json` + `users.json` + `projects/`), full-account point-in-time, no delta export; apparatus ingests `conversations.json` only. Earned by the 5-28 second-export pull. Surgical edit only.

*5-24-26 by Jake + SD24 Claude. SD24 folded in: §3 — added VM 100 standing risk: `server.js` V8 worker can hang (not crash), invisible to systemd `Restart=on-failure`; recover via `qm stop/start 100`; external liveness-probe fix queued. Prior 5-24-26 — SD21 + SD22 folded in: §3 — printer cam migrated off ffmpeg/HLS onto go2rtc/WebRTC (server.js v3.3, camera pull removed; new go2rtc subsection; frozen-but-flowing note marked historical/pipeline-retired with go2rtc immunity UNPROVEN; stale ffmpeg systemd + floor-metrics facts scrubbed). §4 — pinned Workhorse `.238`. §5 — added the 3D Recipes Nightly Archiver. §7 — documented the Tapo C111 ~2-pull RTSP ceiling as a standing constraint. Surgical edits only going forward.*

*Prior: 5-22-26 by Jake. SD20b: corrected TheNightsWatch code versions (server.js v3.2 + index.html), logged the ffmpeg SIGTERM slow-kill + frozen-but-flowing failure mode.*
