---
title: "AI Marketing Team — Build Plan"
type: intelligence
status: active
tier: secondary
tags: []
last_updated: 2026-04-04
related: ["[[Intelligence/00-INDEX]]"]
---

# AI Marketing Team — Build Plan

**Created:** 2026-04-04
**Status:** In Progress
**Owner:** Anthony Mendoza
**Support:** Emigen Lagman (AI project point person)

---

## Vision

Build a multi-client AI marketing team using Claude Code that can create on-brand content for Launchpad and all current/future clients with minimal revisions. Unlike single-brand setups, this system must handle client onboarding, multi-client context switching, and cross-reference Obsidian Brain, Notion, and Google Drive per client.

---

## Agent Roster (9 Agents)

| # | Agent | Role | Key Skills / Responsibilities |
|---|-------|------|------------------------------|
| 1 | **Client Onboarding Agent** | Setup | Auto-builds client context package from Notion, Google Drive, Slack, website, social profiles. Creates Brain note from [[Client Context Template]]. |
| 2 | **Data Analyst** | Analytics | Campaign reporting, performance dashboards, data visualization |
| 3 | **Content Creator** | Content | Marketing content across formats — blog posts, captions, email, lead magnets. Heavy video content focus. |
| 4 | **Market Researcher** | Research | Market research, competitive analysis, trend identification, audience insights |
| 5 | **Creative Designer** | Design | Visual content, social creatives, carousels. References mood boards and style libraries per client. |
| 6 | **Campaign Strategist** | Strategy | Campaign planning, executional briefs, messaging, taglines, quarterly plans |
| 7 | **Brand Compliance Agent** | QA | Reviews ALL agent output against client brand guidelines before delivery. Last gate before anything goes out. |
| 8 | **Social Media Poster** | Distribution | Formats content calendar into GHL Advanced bulk upload CSV. Platform-specific sizing, tone, and voice. Knows which platforms each client uses. |
| 9 | **Video Production Agent** | Video | Shot lists, edit briefs, clip cutting direction for Opus.ai, content ideation. Collaborates with human Content Creator (Kyle). Understands content purpose: viral (trends/sounds/skits) vs evergreen (educate/entertain/empathy). |

---

## Architecture Decisions

### Multi-Client Routing
- Each client has a standardized context note in the Brain (from [[Client Context Template]])
- Agents load the relevant client context based on the task
- File structures, folder naming, and references are consistent across all clients

### Agent Task Board
- **Separate from current Notion workflow** — doesn't touch the human team's existing databases
- Clearly labeled as AI Agents / LP Agents
- Gradual integration over time as trust builds
- See: [[Gradual AI Integration]] (feedback memory)

### Notion ↔ Brain Sync
- **Notion → Brain** (primary): Scheduled sync agent runs on cadence, scans Notion databases for changes, updates Brain notes
- **Brain → Notion**: Agents write to Notion directly when producing deliverables
- **Google Drive → Brain**: Set once during onboarding, updated if reorganized

### GHL Integration
- All clients have GHL CRM sub-accounts under Launchpad's agency account
- Social Media Poster agent uses **Advanced Format** CSV for bulk upload
- Columns: postAtSpecificTime, content, link, imageUrls, gifUrl, videoUrls + stories, reels, shorts, GBP, tags, category, first comment, watermark
- Max 90 posts per CSV import

### Visual References
- Mood boards (Canva, Pinterest, Notion) linked in every client context note
- Shot lists and production briefs linked per client
- Agents reference these for visual style, not just text descriptions
- Standardized location needed — currently scattered (known gap being fixed)

---

## Test Plan

**Phase 1: Test with Launchpad + Launchpad University**
- Launchpad is the first full client context (own brand, full access to all assets)
- LP University — community + courses + certifications platform, teaches Content/Leads/Systems framework
- Course content in GHL, video transcriptions available from Descript
- Test each agent against real LP marketing tasks before rolling out to clients

**Phase 2: Roll out to 1-2 Tier 1 clients**
- 365 Plumbing, Taco Bell Cantinas, or Sobel Westex (closest to agent-ready)
- Validate multi-client context switching

**Phase 3: Full rollout**
- All active clients
- Client Onboarding Agent handles new client setup

---

## Prerequisites / Current Status

### Completed ✅
- [[Client Context Template]] created (Resources)
- [[Client Context Audit — 2026-04-04]] completed (Intelligence)
- Notion tracker created: [AI Team Prep — Client Context Gaps](https://www.notion.so/338b01f77d6d81cd85ced604b8ad0d99)
- Emigen assigned as point person, task lists distributed
- Slack messages drafted to Emigen, Abril, Cynthia, Amber

### In Progress 🔄
- Client context gap filling (Emigen leading, deadline April 9)
- Launchpad's own client context being built for testing
- Google Drive folder structure standardization (reminder set)

### Not Started ⏳
- AI OS folder structure build
- Agent and skill creation
- Notion ↔ Brain sync agent
- Agent task board in Notion

---

## Key Insight from Anthony

> "There are a lot of holes in what we do because everything is either so scattered, named improperly, or incomplete."

The AI marketing team build is surfacing operational gaps that existed before AI. Fixing these gaps improves both the human and AI workflows. This is not just an AI project — it's an operational upgrade.

---

## Related
- [[Client Context Template]]
- [[Client Context Audit — 2026-04-04]]
- [[Active Clients Overview]]
- [[New Client Onboarding Process]]
- [[Content Workflow — Shoot to Post]]
- [[Packages and Pricing]]
