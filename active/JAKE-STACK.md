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
· **Intermittent panics under investigation** — two unexplained hard hangs 5/21 AM (01:42 + ~08:25). NVMe ruled out. CPB-disable removed transient thermal spikes as a vector. RAM intermittent fault remains the top open suspect — MemTest86+ queued (overnight test).
· **PSU concern from S15** — two reboots under sustained ISO upload write load. Parked, not resolved. Spare 700/750W ATX on hand for swap-test (requires Lenovo→ATX adapter cable + 3D-printed bumpout).
· **Bambu cloud MQTT auth token** has a ~3-month silent expiration clock — no creation date logged historically.

---

## 3. The Watch — VMs on Castle Black

### VM 100 — TheNightsWatch
**Canonical lore name.** Hostname inside VM is still `neighborhood-watch`; multi-surface rename queued.

· **Role:** Dashboard server. Bambu camera HLS proxy. Status tiles. Life360 polling. Heartbeat receiver.
· **OS:** Ubuntu 24.04.4 LTS Server, Node v24.15 at `/usr/bin/node`
· **IP:** `192.168.50.88` (DHCP-reserved, MAC `BC:24:11:07:69:EF`)
· **SSH alias on Workhorse:** `nightswatch` (1PW agent)
· **Display name in Proxmox UI:** still `bambu-monitor` — cosmetic rename queued.
· **systemd unit:** `/etc/systemd/system/neighborhood-watch.service` v2. `NoNewPrivileges` dropped (broke ping via cap_net_raw strip in v1); other hardening preserved (`PrivateTmp`, `ProtectSystem=full`, `ProtectHome=read-only`, `ReadWritePaths` carve-out). `Restart=on-failure`, `RestartSec=5s`, `enable`d at boot.
· **VM specs:** 2 cores type=host, 4 GiB RAM, 20 GB virtio-scsi on local-lvm (iothread + discard + ssd emulation), i440fx + SeaBIOS. CD-ROM device still emulated (empty) — causes `ata_sff_pio_task` log noise; full removal needs VM bounce.
· **Code:** `/home/jake/neighborhood-watch/` — `server.js` v3.1, `life360.js` v1.2, `status.js` v2.4, `status.html` v2.2, `config.json`, `l360_token_test.js`
· **Standing risk:** `config.json` holds plaintext secrets (Bambu camera creds, Life360 token). 1PW Environment migration queued.
· **Floor metrics:** CPU ~102% of 2 cores (ffmpeg HLS transcoding — normal). RAM ~157 MB. Disk 36.1% of 9.75 GB.

### VM 200 — Watchtower
· **Role:** Life360 bot account host. Android-x86 9.0.
· **Boot order:** 1. TheNightsWatch boots at order 2 with 30s startup delay — gives Watchtower's Life360 app time to reconnect before polling starts.

### Dashboard endpoint
· `http://192.168.50.88:8765/status` — tiles: NAS · Last Backup · Router · Internet · Replicator (P1S) · Family (Life360)

### Kiosk service
· Castle Black now runs a status-kiosk.service (cage+cog→:8765/status) on tty1, driving the Acer. New standing infra.
· The two scars, for the lineage: WLR_DRM_DEVICES is colon-separated so PCI by-path names blow up — use card1 (+ a udev alias later if you want renumber-safety); and a kiosk service needs Conflicts=getty@tty1 or it can't wrestle DRM master off the console. Both cost us a cycle; both worth a Lore Bible line so the next Claude doesn't re-buy them.

---

## 4. Network

· **Router:** ASUS RT-AX55, `192.168.50.1`
· **DHCP reservations live:**
  · Castle Black `.250` — MAC `88:AE:DD:15:CA:D2`, label `CastleBlack`
  · TheNightsWatch `.88` — MAC `BC:24:11:07:69:EF`, label `TheBlackWatch` (typo, cleanup queued — should be `TheNightsWatch`)
  · NAS `.248` — pre-existing, label `NASBackup`
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
· **Camera:** Tapo C111 at `192.168.50.199` (powered independently — no longer USB-from-P1S, that failure mode is retired)

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

*Last updated: 5-22-26 by Jake. Revised home hardware stack (added monitor info), corrected printer hardware. Initial creation alongside JAKE-RULES.md expansion. Surgical edits only going forward.*
