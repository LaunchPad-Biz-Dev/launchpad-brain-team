---
date: 2026-04-07
type: idea
status: queued — needs scoping session
tier: secondary
tags: [ai-os, sales-team, initiative, launchpad]
related: ["[[Intelligence/00-INDEX]]"]
---

# AI Sales Team — Initiative Capture

> Anthony's idea from 4/7: "I also want to start building another folder similar to how we have marketing but it to be focused on sales and create an AI sales team."

## The Idea
Build a dedicated AI sales team structure alongside the existing AI marketing team. Same architecture as `marketing/` — agents, skills, output folders — but focused entirely on sales workflow.

## Context
Launchpad's current AI OS covers:
- **Marketing**: Content, Creative, Campaign Strategy, Research, Social Media, Video, Brand Compliance, Data Analysis
- **Sales**: Nothing yet — entirely manual

The sales cycle at Launchpad is: Content → **Leads** → **Systems** (follow up + convert). AI covers Content well now. The Leads and Systems phases (sales) are the next frontier.

## What an AI Sales Team Could Cover
- Lead qualification and scoring
- Outreach copy (DMs, email sequences, proposals)
- CRM management and pipeline tracking (GHL)
- Follow-up sequence automation
- Proposal generation from client context
- Sales call prep briefs
- Post-call action item capture
- Objection handling scripts and rebuttals

## Potential Agent Roster (Preliminary)
- **Lead Qualifier** — Scores inbound leads, routes to appropriate follow-up
- **Outreach Copywriter** — Cold DMs, email sequences, LinkedIn messages
- **Proposal Generator** — Builds proposals from client context + package info
- **Sales Data Analyst** — Pipeline performance, conversion rates, close ratios
- **CRM Manager** — Maintains GHL pipeline hygiene, follow-up task creation

## Folder Structure (Proposed)
```
sales/
  agents/
  skills/
  output/
    leads/
    proposals/
    outreach/
    pipeline-reports/
  context/
```

## Next Steps
1. Scoping session with Anthony to define which sales workflows AI should own first
2. Map current manual sales process (who does what today)
3. Identify highest-ROI starting point (probably proposal generation or outreach)
4. Build Phase 1 agent + skill

## Reference Material

### 100M Leads — Alex Hormozi (2026-04-08)
Anthony shared this book via Slack DM on April 8, 2026. File ID: F09QNGB3QNR (18.9 MB PDF, shared in Apollo DM channel).
His intent: "Read this book and let me know your thoughts. One of our next big endeavors will be building a sales team. We have a problem at Launchpad with not having enough sales and need to work on generating more leads so we can sell more. I want to create a solid agent network for sales and arm it with strong skills so we can 10x our business."
Key framing: Hormozi's lead generation principles should inform the agent architecture — specifically outreach volume, offer clarity, and conversion optimization. Pull core frameworks when scoping Phase 1 agent build.

## Related Notes
- [[Core Framework]] — the Content → Leads → Systems model
- [[Launchpad Business Development]]
- [[AI Agent Build — April 2026]]
