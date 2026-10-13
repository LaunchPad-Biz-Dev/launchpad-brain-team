# Laptop Migration — Setup and Architecture
*Captured: 2026-07-23*

> **Superseded on 2026-08-12.** The "MacBook (laptop)" below turned out to be the MacBook Air,
> which was replaced by a MacBook Pro 16" M2 Max and **erased/retired on 2026-08-12**. The
> two-machine architecture and the no-agents-on-the-laptop rule still hold — only the laptop
> hardware changed. Hostnames here are also stale (the Mini answers to `Thomass-Mac-mini-2`).
> Current fleet of record: [[Device Fleet]].

## What This Is
Anthony is setting up a **MacBook (laptop)** as a secondary machine alongside the **Mac Mini ("Thomass-Mini")**, which remains the primary agentic host. The goal is a two-machine setup where the laptop can reach into the Mini for agentic work without duplicating the always-on automation.

---

## Two-Machine Architecture

| Role | Machine | Hosts |
|---|---|---|
| Always-on brain | Mac Mini "Thomass-Mini" | All 10 launchd agents, crontab, apollo-listener, brain-dump, slack-inbox, trend-scanner, morning-briefing, etc. |
| Secondary / mobile | MacBook (laptop) | Claude Code CLI, VS Code, Obsidian, Tailscale — NO agents, NO crontab |

**Critical rule:** Do NOT install the launchd agents or crontab on the laptop. Double-firing risk (two morning briefings, two Slack listeners, etc.). The laptop reaches into the Mini via Tailscale/SSH for agentic work.

---

## Current Status (2026-07-23)

- ✅ **launchpad-brain vault** backed up to private GitHub repo: `github.com/Anthony-launchpad/launchpad-brain` (75 commits, history intact)
- ✅ **Full backup created** at `~/claude-migration/full-backup.tgz` on the Mini (14M, contains secrets — **never share publicly, stays local on Mini**)
- ✅ **Share bundle** at `~/claude-migration/share-bundle.tgz` (7K, clean, safe to send)
- ✅ **Inventory** at `~/claude-migration/INVENTORY.md`
- ✅ **setup-laptop.sh** script created and saved to `launchpad-automation/scripts/setup-laptop.sh`
- ✅ **backup-obsidian-vault.sh** script saved to `launchpad-automation/scripts/backup-obsidian-vault.sh`
- ⏳ **Laptop setup** — pending (Anthony has backup.tgz, needs to run `setup-laptop.sh`)
- ⏳ **Obsidian Sync** — vault connected on Mini; laptop will use "Open vault from Obsidian Sync" after cloning

---

## Mini Inventory (2026-07-23 snapshot)

- **Host:** Thomass-Mini — macOS 14.6.1, Apple Silicon (arm64)
- **Core tooling:** Homebrew 5.1.12 · Node v25.9.0 · Python 3.9.6 (+ brew python@3.11) · Claude Code CLI 2.1.116 · Tailscale 1.98.5 · git 2.39.5
- **Claude Code plugins:** skill-creator, figma, zapier, build-with-wordpress
- **Subagent (user-level):** proposal-invoice-agent
- **Skill (user-level):** graphify
- **Settings:** effort=high, theme=light
- **MCP servers (project-scoped):** nanobanana (uvx), google-drive (local OAuth), meta-ads (hosted OAuth), google-ads (local venv in vendor/), tiktok-ads (local python in vendor/)

---

## What Won't Port Cleanly to the Laptop

1. **Vendored MCP servers** — `vendor/google_ads_mcp` (venv) and `vendor/tiktok-ads` need to be rebuilt on the laptop. `meta-ads` (hosted) and `nanobanana` (uvx) port fine.
2. **`.mcp.json` + `.claude/mcp-clients/*`** — gitignored, live in full-backup.tgz only. Must be copied manually.
3. **Google Drive OAuth credential** — `~/.config/google-drive-mcp/credentials.json` must be copied from backup or re-authed.
4. **hostname is `Thomass-Mini`** — any script hardcoding that name needs the laptop's hostname.

---

## Obsidian Two-Machine Setup

- **On Mini:** "Open folder as vault" → `~/launchpad-brain/LaunchPad Brain`. Then Settings → Sync → Create new remote vault "LaunchPad Brain" → upload.
- **On Laptop:** "Open vault from Obsidian Sync" → select "LaunchPad Brain" remote → downloads everything.
- Git = durable history/backup. Obsidian Sync = live edits between machines. They coexist without conflict.

---

## SSH / Tailscale Access (Laptop → Mini)

After `setup-laptop.sh` runs:
```
ssh mini     # reaches Thomass-Mini via Tailscale
```
`~/.ssh/config` entry added by the script:
```
Host mini
    HostName thomass-mini
    User anthony
```
Verify on Mini: System Settings → General → Sharing → Remote Login: ON.

---

## Related
- [[AI-OS-Architecture]] — full agent/automation architecture
- Scripts: `launchpad-automation/scripts/setup-laptop.sh`, `launchpad-automation/scripts/backup-obsidian-vault.sh`
