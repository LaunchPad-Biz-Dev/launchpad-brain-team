---
title: "n8n Orchestration Layer"
type: skill
status: active
tier: primary
tags: [n8n, automation, infrastructure, layer-3]
last_updated: 2026-05-18
related: ["[[index]]", "[[CLAUDE]]", "[[Frontmatter Spec]]", "[[Skills/00-INDEX]]"]
---

# n8n Orchestration Layer

**Adopted 2026-05-18** per Stanley Chen webinar findings. n8n is our Layer 3 (Automation) plumbing engine. It handles deterministic data movement between tools and only calls Claude when judgment is needed — cutting our token spend hard.

---

## What n8n is in our stack

| Layer | Role | Where |
|---|---|---|
| Layer 1 (Context) | The Brain | `~/launchpad-brain/` |
| Layer 2 (Skills) | Claude agents + skills | `~/launchpad-automation/.claude/` |
| **Layer 3 (Automation)** | **n8n + cron + MCP webhooks** | **n8n on `localhost:5678`** |

---

## When to use n8n vs Claude vs cron

| Use n8n when | Use Claude when | Use cron when |
|---|---|---|
| Moving data between tools (GHL → Slack, Notion → Brain) | The step requires reasoning, judgment, writing, or creative output | A scheduled task is purely a trigger (run X every day at 7 AM) |
| The same workflow runs many times the same way | The output differs by context and needs synthesis | The job is a single command on a schedule |
| You need a webhook receiver | You need a content generation or analysis pass | Pure timing |

**Hybrid is the gold path.** n8n moves the data, calls Claude for the judgment step, then keeps moving. Example: IG prospecting flow — n8n scrapes via Apify + filters + scores → calls Claude to write the personalized DM → n8n writes to GHL + pings Slack.

---

## Running n8n

```bash
# Start
~/launchpad-automation/scripts/n8n-start.sh

# Stop
~/launchpad-automation/scripts/n8n-stop.sh

# UI
open http://localhost:5678

# Logs
tail -f ~/launchpad-automation/logs/n8n.log
```

n8n runs with `--tunnel` so webhooks from external services (GHL, Stripe, etc.) can reach it without exposing your Mac to the internet directly. The tunnel URL is printed in the logs at startup.

---

## Where workflows live

- **Active workflows:** stored inside n8n's SQLite DB at `~/.n8n/database.sqlite`
- **Exported JSON backups:** `~/launchpad-automation/n8n-workflows/` — every workflow gets exported on save for git tracking
- **Credentials:** encrypted in `~/.n8n/`, never committed

---

## First workflow (built 2026-05-18)

**Name:** GHL New Contact → Slack Notification (Launchpad)
**Why first:** Validates the most-important integration (GHL) end-to-end. Stakes are low — wrong fire = harmless Slack ping. Right fire = team gets surfaced hot leads instantly.

**Flow:**
1. **Webhook trigger** — GHL "new contact" event from Launchpad sub-account
2. **Filter** — Only proceed if `tag includes "hot lead"` OR `source = "Growth Audit"`
3. **Format** — Build message: contact name, source, tags, GHL contact URL
4. **Slack send** — Post to `#ai-team-updates`

**Next workflows in queue:**
- IG cold prospecting daily 20 (Apify scrape → score → Claude DM draft → GHL write)
- CRM hygiene daily sweep (dedupe + score + reactivation queue)
- Growth Audit landing page submit → CRM contact → Slack ping
- Notion → Brain sync (migrate from cron)

---

## Rules

1. **n8n owns the plumbing. Claude owns the judgment.** Don't put reasoning logic in n8n nodes — call Claude for that step.
2. **Every workflow has a test fixture.** Before turning it on, send a test webhook and watch it execute. Capture screenshots.
3. **Every workflow is exported to git.** On save, export JSON to `n8n-workflows/{slug}.json` for version control.
4. **Credentials never get committed.** Use n8n's encrypted credential store; document only the credential NAME, not the secret.
5. **No production workflow runs without a Slack notification on failure.** Add an error trigger that pings `#ai-team-updates` if any step throws.
