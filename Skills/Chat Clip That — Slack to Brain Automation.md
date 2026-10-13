---
title: "Chat Clip That — Slack + Meetings to Brain Automation"
type: skill
status: active
tier: secondary
tags: []
last_updated: 2026-04-03
related: ["[[Skills/00-INDEX]]"]
---

# Chat Clip That — Slack + Meetings to Brain Automation

This skill documents the "Chat Clip That" system — how the team captures ideas, decisions, and updates from Slack conversations AND meeting transcripts, automatically saving them to the Obsidian Brain and Notion.

---

## How It Works

Anyone on the team can say **"chat clip that"** in two places:

### In Slack
Say it in any channel or thread. The system picks up the conversation before your message.

### In Meetings
Say it during any recorded meeting. The system scans meeting transcripts in Notion and picks up what was being discussed when someone said it.

A scheduled task runs every 12 hours (9am and 9pm PST) and:

1. Searches all Slack channels for new "chat clip that" messages
2. Scans recent Notion meeting transcripts for "chat clip that" (and variations like "clip that", "let's clip that")
3. Reads the conversation/transcript context before each clip
4. Categorizes what was discussed
5. Saves it to the correct location in the Obsidian Brain
6. Saves it to the 💡 Ideas Scratch Pad in Notion (universal catch-all for ALL clips)
7. Routes it to additional Notion destinations based on category
8. Replies in Slack confirming where it was saved (for Slack clips)

---

## Categories

The system classifies each clip into one of these categories:

| Category | What It Is | Brain Destination | Notion Destination |
|---|---|---|---|
| **CONTENT_IDEA** | Content ideas, creative concepts, campaign brainstorms for a client | Projects/[Client].md | Client Brainstorm database |
| **PROCESS_UPDATE** | Changes to workflows, SOP improvements, new ways of doing things | Departments/ or Skills/ | Weekly Health Dashboard (for [[Abril Rodriguez]] to review) |
| **CLIENT_INTEL** | Client feedback, competitive insights, market observations | Intelligence/ + Projects/[Client].md | Client Health Tracker (Flags field) |
| **DECISION** | Decisions made during conversation | Daily/[date].md + Intelligence/ | Weekly Health Dashboard |
| **TEAM_NOTE** | Info about team members, assignments, role updates | Teams/[Person].md | Ideas Scratch Pad |
| **GENERAL** | Anything else worth saving | Intelligence/ | Ideas Scratch Pad |

**Note:** ALL clips — regardless of category — also go to the 💡 Ideas Scratch Pad so the team always has one central place to review everything.

---

## How to Use It

### For the Team
Just say **"chat clip that"** in any Slack channel or thread after a conversation you want captured. That's it. The system handles the rest.

Tips:
- Say it right after the relevant discussion — the system reads the messages BEFORE yours
- Works in any channel — public, private, DMs, group DMs
- Works in threads — great for clipping a specific thread discussion
- You'll get a confirmation reply showing exactly where it was saved

### Examples

**Content idea in #local-opps:**
> "Hey what if we did a behind-the-scenes series for Arby's food truck showing the prep before events?"
> "That's fire — we could do reels from each location"
> "chat clip that"
→ Saves to Projects/Arby's Food Truck.md + Notion Client Brainstorm

**Process improvement in #systems:**
> "We should start requiring a creative brief before any shoot — too many times we show up without a shot list"
> "chat clip that"
→ Saves to Skills/ or Departments/ + flags on Weekly Health Dashboard for [[Abril Rodriguez]] to review

**Client feedback in #client-updates:**
> "CCS said they loved the last round of social posts — especially the gold/navy color treatment. They want more of that direction."
> "chat clip that"
→ Saves to Projects/Continental Currency Service.md + Intelligence/

---

## Meeting Clips — How They Work

When someone says "chat clip that" during a recorded meeting:
1. The meeting gets transcribed and stored in Notion
2. The scheduled task scans recent meeting transcripts for "chat clip that" and variations
3. It reads the transcript context — what was being discussed in the minutes before
4. Categorizes, saves to Brain, and creates a row in the Ideas Scratch Pad with a link back to the meeting

### Meeting Clip Example

**During a client strategy meeting:**
> "What if we ran a geo-targeted TikTok campaign around the food truck schedule? People within 5 miles get a reel the day before each stop."
> "That's a great idea — chat clip that"
→ Saves to Projects/Arby's Food Truck.md + Client Brainstorm + Ideas Scratch Pad with meeting link

---

## Notion Destinations

- **💡 Ideas Scratch Pad** (collection://bf27bf46-a0bb-4ba9-84d4-8b28280a2532) — ALL clips go here, universal catch-all inside 🏢 Company Operations
- **Content Ideas** → Client Brainstorm database (collection://333b01f7-7d6d-8034-87f0-000be1b90fd5) inside the Content Brainstorm Dumpy page
- **Process Updates** → Weekly Health Dashboard (page ID: 337b01f7-7d6d-81b2-b455-cb2964d808b6) under "Process Updates for Review"
- **Client Intel** → Client Health Tracker (collection://cd38db5c-2969-4a9d-8211-0a606a9be738) Flags field
- **Decisions** → Weekly Health Dashboard under "Key Decisions This Week"

---

## Scheduled Task Details

- **Task ID:** `slack-chat-clip-that`
- **Schedule:** Every 12 hours — 9:00 AM and 9:00 PM PST
- **Scans:** All Slack channels + Notion meeting transcripts
- **Confirmation:** Replies in-thread with save locations (Slack clips)
- **Universal Log:** Every clip goes to the 💡 Ideas Scratch Pad regardless of category

---

## Related Notes
- [[Weekly and Monthly Cycles]] — Content cycle context for when ideas should be acted on
- [[Canva Design Workflow]] — If a content idea leads to a design task
- [[Content Workflow — Shoot to Post]] — If a content idea leads to a production task
- [[Company Org Chart 2026]] — Team structure for routing team notes

---

*Created 2026-04-03 | Updated 2026-04-03*
*Scheduled task: slack-chat-clip-that*
