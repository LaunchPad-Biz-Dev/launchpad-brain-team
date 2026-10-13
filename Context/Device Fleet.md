---
title: "Device Fleet — Active Machines"
type: infrastructure
status: active
tier: primary
tags: [system, infrastructure, devices, hardware]
last_updated: 2026-08-13
related: ["[[AI-OS-Architecture]]", "[[New Mac Setup — Migration Guide]]", "[[Laptop Migration — Setup and Architecture 2026-07-23]]", "[[Context/00-INDEX]]"]
---

# Device Fleet — Active Machines

**As of 2026-08-12 the fleet is two machines: the Mac Mini and the MacBook Pro.**
The MacBook Air is out of the process — erased and reset on 2026-08-12.

---

## Active machines

| Role | Machine | Hostname / Tailscale node | Runs |
|---|---|---|---|
| **Always-on agentic host** (primary) | Mac Mini | `Thomass-Mac-mini-2` — reachable as `ssh mini` | All 10 launchd agents, crontab, apollo-listener (port 4747), brain-dump, slack-inbox, trend-scanner, morning-briefing, n8n |
| **Mobile / secondary** | MacBook Pro 16" M2 Max (64GB/1TB) | `Anthonys-MacBook-Pro` / node `anthonys-macbook-pro` | Claude Code CLI, VS Code, Obsidian, Tailscale. **No agents, no crontab** |

**The rule that holds:** automation lives on the Mini only. The laptop reaches it with
`ssh mini` over Tailscale. Installing launchd agents or a crontab on the MacBook Pro causes
double-firing — two morning briefings, two Slack listeners, duplicate posts. See
[[New Mac Setup — Migration Guide]] Step 5.

**Tailnet:** `anthony-launchpad.github` — sign in as **`Anthony-launchpad@github`**, not the
Google account `anthony@launchpadbizdev.com` (that one is an empty tailnet with 0 peers and
breaks `ssh mini`). Same identity that owns `github.com/Anthony-launchpad/launchpad-brain`.

---

## Build vs. Run — the division of labor (added 2026-08-13)

Anthony's framing, stated 2026-08-13 while wiring the outbound ad-signal scrapers. This
sharpens the existing "automation lives on the Mini" rule by naming *why* each machine exists,
not just what may not be installed where.

| | MacBook Pro | Mac Mini |
|---|---|---|
| **Purpose** | **Build.** Design, ideate, prototype, quick one-off work, interactive Claude Code sessions. | **Run.** Every agentic sequence that fires on its own. |
| **Work that belongs here** | Writing agents/skills, drafting notes, exploring data, one-off scrapes, testing a workflow by hand | Scheduled runs, watchers, listeners, n8n workflows, anything triggered without a human |
| **Never install here** | launchd agents, crontab entries, long-running listeners | — |
| **Why** | Keeps the laptop responsive — agentic runs must not eat the machine Anthony is working on | Dedicated hardware, always on, no contention with active work |

**The test to apply before wiring anything:** *does this fire without a human?* If yes → it
deploys to the Mini. If it only runs because Anthony asked for it in the moment → the laptop is
fine.

**Cloud execution is not machine-bound.** Apify actor runs, GHL/Notion/Slack MCP calls, and
hosted APIs execute on someone else's hardware regardless of which machine initiated them —
they cost the laptop nothing but the JSON coming back. Running one interactively from the MBP
does not violate this rule. What must live on the Mini is the *trigger*, not the compute.

**Applies to the outbound build (Track B):** scrapers are authored and hand-tested from the
laptop; the recurring prospect sweep deploys to the Mini before it goes on a schedule. Write
scripts host-agnostic — no hardcoded `/Users/anthony/...`, use `USERNAME` placeholders or
`$HOME` the way [[Apollo Listener]]'s plist already does.

---

## Retired

| Machine | Status | Date |
|---|---|---|
| MacBook Air M2 (8GB) | **Decommissioned** — Erase All Content and Settings; signed out of iCloud / Adobe / Claude Code / Slack / NordPass; removed from the Tailscale admin console | 2026-08-12 |

Reason: laptop upgrade. The MacBook Pro replaced it via Migration Assistant on 2026-08-10/11
per [[New Mac Setup — Migration Guide]]; Anthony confirmed the backup and setup work on the
new machine before the wipe.

**Final state preserved:** branch `air-final-2026-08-12` on the brain remote holds the Air's
complete working tree — tracked modifications plus untracked files — captured immediately
before the erase. `main` remains authoritative; that branch is a safety net only, to be
cherry-picked from if something turns out to be missing.

---

## What this changes going forward

- Anything assuming a **three-machine fleet** is stale. Plan for Mini + MacBook Pro only.
- **Adobe CC's 2-device cap** is now Mini + MacBook Pro — the Air's seat was released on sign-out.
- Scripts or configs hardcoding `anthonys-macbook-air` (Tailscale node names, SSH config, sync
  targets) will fail — point them at `anthonys-macbook-pro`.
- The old Air Tailscale node record (`ntqXg9tsYC21CNTRL` / `100.88.140.35`) can no longer
  collide with the MacBook Pro now that the Air is erased.
- Nothing needs migrating *off* the Air. It is wiped — treat it as gone, not as a fallback.
- Sync layer between the two machines is unchanged: git
  (`github.com/Anthony-launchpad/launchpad-brain`) for durable history, Obsidian Sync for live edits.

---

## Related
- [[AI-OS-Architecture]] — full agent/automation map, Mini-hosted
- [[New Mac Setup — Migration Guide]] — the MBP migration + decommission checklist, Tailscale and GitHub-auth gotchas
- [[Laptop Migration — Setup and Architecture 2026-07-23]] — original two-machine architecture rationale
