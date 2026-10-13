---
title: "n8n Workflow Roadmap"
type: skill
status: active
tier: primary
tags: [n8n, automation, roadmap, layer-3, social-media-manager, communication-ingestion]
last_updated: 2026-05-18
related: ["[[n8n Orchestration Layer]]", "[[Brain Standards]]", "[[Social Media Production Workflow]]", "[[Cynthia Hernandez]]", "[[CLAUDE]]", "[[Skills/00-INDEX]]"]
---

# n8n Workflow Roadmap

**The master plan for every workflow we'll build in n8n.** Re-prioritized 2026-05-18: Cynthia's social-media-posting automation now leads as Phase 1 (Anthony's stated focus for the week).

n8n is the Layer 3 plumbing engine (per [[Brain Standards]]). It moves data between tools deterministically and only calls Claude when judgment is needed. Every workflow follows the rule: **n8n moves the data, Claude does the thinking, output lands somewhere actionable.**

n8n Cloud: `https://launchpadbizdev.app.n8n.cloud`

---

## Phase 1 — Social Media Posting Automation (CURRENT — Cynthia's bottleneck)

**Goal:** collapse Cynthia's posting phase from "manual juggling across Drive + GHL + Notion + Slack" to "approve in one place, watch it ship." Each workflow targets a specific manual step in [[Social Media Production Workflow]] Phase 3.

**Focus: Track A (per-platform scheduling/posting).** Track C (approval feedback loop with clients + designers) is parked for Phase 2 once communication ingestion lights up.

| # | Workflow | Trigger | What it does |
|---|---|---|---|
| **01** | **Drive "Approved" → GHL Media Library** | File added to `{Client}/Graphics/{Month}/AI Graphics/` or equivalent approved Drive folder | Downloads from Drive → uploads to GHL CDN via `ghl-media-upload.sh` → writes CDN URL + metadata back to Notion content calendar row |
| **02** | **Notion "Ready to Schedule" → GHL Draft Posts** | Notion content calendar row marked "Ready to Schedule" | Reads client brand voice from `Brain/Projects/{Client}.md` → builds caption + hashtags (Content Creator agent or pre-written in Notion) → selects right platforms per client → sets post type per platform → creates GHL draft via Social Media Poster |
| **03** | **Drafts Ready → Slack Notification** | Batch of drafts created for a client | Pings `#social-media-management` (Cynthia + Abril) with link to GHL drafts + summary (client, count, platforms) |
| **04** | **Cynthia Approves → Auto-Schedule** | Cynthia marks "approved" (tag in GHL, checkbox in Notion, or Slack reaction — TBD which feels best) | n8n schedules with platform-optimal posting times per client cadence; status → `scheduled` |
| **05** | **Weekly Contract Count Check** | Cron Sundays 6 PM | For each client: count scheduled + published this month, compare to contracted post count from `Brain/Projects/{Client}.md`, alert in `#admin-ish` if any client is projected short. (Contractual tripwire — see [[Social Media Production Workflow]] section "Critical rules") |
| **06** | **Performance Metrics → Notion Weekly Digest** | Cron Sundays 8 PM | Pull GHL `social-media-statistics` per client → write performance digest to Notion under client's "Reports" page → Slack summary to Cynthia + Abril |

**Build order:** 01 → 02 → 03 → 04 → 05 → 06

**Why 01 first:** highest manual time-savings (re-uploading is tedious), uses existing `ghl-media-upload.sh` script, no Notion dependency, validates the Drive↔GHL pattern end-to-end.

### Track C — parked until Phase 2

Revision feedback loop (Drive comments → designer notifications → re-QC) requires communication ingestion workflows from Phase 2. Will revisit once #08-09 ship and we can route Drive comments + Slack revision messages through the Brain. **TODO:** circle back after Phase 2 milestone.

---

## Phase 2 — Communication Ingestion (Anthony's big-vision capture layer)

Capture every conversation in the business into the Brain so we always know exactly where we stand on every client, every project, every decision. This is the "transparent business" pattern Stanley described in the webinar.

Each workflow follows: source fires → n8n catches → Claude classifies + summarizes per [[Brain Standards]] zone rules → output lands in right Brain folder + Slack ping if action needed.

| # | Workflow | Sources captured | Lands at |
|---|---|---|---|
| 07 | **Fireflies → Brain** *(start here — highest signal)* | Every Zoom/Meet/Phone call | `Raw/transcripts/` + action items in `Intelligence/` + Slack ping |
| 08 | **Slack channels → Brain** | All public + private channels | `Raw/slack/` + weekly synthesis in `Intelligence/` |
| 09 | **Slack DMs to Apollo → Brain** | DMs to Apollo | `Raw/inbox/` + brain-ingest classifies |
| 10 | **Notion meeting notes → Brain** | Notion pages tagged 'meeting' | `Raw/exports/notion-meeting-...` |
| 11 | **Notion general sync → Brain** | All workspace updates | Mapped to right folder by content |
| 12 | **Email → Brain** | Inbound + outbound business email | `Raw/email/` + thread synthesis |
| 13 | **GHL conversations → Brain** | SMS + GHL inbox threads | `Raw/ghl-convos/{contact}/` + per-client synthesis |
| 14 | **Loom → Brain** | Internal Looms with transcripts | `Raw/transcripts/` + Claude summary |
| 15 | **Voicemails → Brain** | Phone voicemails | `Raw/voicemails/` |
| 16 | **Drive Comments → Brain** | Comments on QC-stage Drive files | `Raw/drive-comments/` + revision routing (unblocks SMM Track C) |

---

## Phase 3 — Sales Infrastructure

Sales Team AI build — referrals + warm + cold + Growth Audit funnel. Was previously Phase 1; moved here to honor Anthony's stated weekly priority. Still high-value, just sequenced after SMM.

| # | Workflow | Trigger | Output |
|---|---|---|---|
| 17 | **GHL Hot Lead → Slack** *(JSON already built — debug pending)* | GHL webhook on new contact / tag added | `#ai-team-updates` Slack message |
| 18 | **Growth Audit Landing → CRM → Slack** | Landing form submit | GHL contact + Slack ping + calendar link sent |
| 19 | **IG Cold Prospecting Daily 20** | Cron 7 AM | Apify scrape → Claude DM → GHL + Slack queue |
| 20 | **CRM Hygiene Daily Sweep** | Cron 6 AM | Dedupe + score + reactivation queue |
| 21 | **New Booking → Meeting Prep Brief** | Calendar event 30 min before | Claude brief → Slack |

---

## Phase 4 — Operations & Lifecycle

| # | Workflow | Trigger | What it does |
|---|---|---|---|
| 22 | **PandaDoc Contract Signed → Onboarding** | PandaDoc webhook | Creates Brain project note, queues tasks in Notion, pings Abril |
| 23 | **Stripe Payment → Invoice Paid → Slack** | Stripe webhook | Marks invoice paid, posts to `#admin-ish`, schedules thank-you |
| 24 | **Weekly Status Report Builder** | Thursday 12 PM cron | Pulls Client Health + Workload + Billing → writes WSR to Notion |
| 25 | **Client Churn Signal** | Cron daily | Detects 14+ day silent clients → pings Anthony |
| 26 | **Birthday/Anniversary Outreach** | Cron daily | Pulls dates from GHL → drafts warm message for Anthony |

---

## Phase 5 — Compounding Intelligence

Use the rich data from Phases 1-4 to drive smarter operations.

| # | Workflow | Cadence |
|---|---|---|
| 27 | Stale Content Summarizer (Stanley's "summarise what's old" rule) | Monthly |
| 28 | Brain Dedup Sweep | Weekly |
| 29 | Client Health Score | Daily |
| 30 | Competitive Intel Watch | Daily Apify |
| 31 | Brain Query → Slack (Apollo answers in-thread) | On-demand |

---

## Build order (full)

```
Phase 1 (Cynthia's bottleneck): 01 → 02 → 03 → 04 → 05 → 06
Phase 2 (Communication):        07 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16
Phase 3 (Sales infra):          17 → 18 → 19 → 20 → 21
Phase 4 (Operations):           22 → 23 → 24 → 25 → 26
Phase 5 (Intelligence):         27 → 28 → 29 → 30 → 31
```

When Phase 1 ships (or even mid-Phase-1 if a quick win is available), we can opportunistically peel off #17 (GHL Hot Lead → Slack) since its JSON is already drafted.

---

## Process for each workflow

1. Identify the trigger (what event starts it?)
2. List the data needed (what fields do we extract?)
3. Decide where it lands in the Brain (per [[Brain Standards]] zone rules)
4. Decide if Claude is in the loop (only if reasoning required)
5. Build JSON in `~/launchpad-automation/n8n-workflows/` (version-controlled)
6. Import + wire credentials in n8n Cloud
7. Test with curl (fire sample event, watch it flow)
8. Activate
9. Document the spec in `Brain/Skills/n8n — XX <name>.md`

---

## Changelog

- **2026-05-18 (initial)** — 4 phases, Sales infra as Phase 1
- **2026-05-18 (restructure)** — Phase 1 is now Cynthia's SMM posting automation per Anthony's stated weekly priority. Sales infra moved to Phase 3. Communication ingestion (Phase 2) added Workflow #16 (Drive comments) so it can unblock SMM Track C.
