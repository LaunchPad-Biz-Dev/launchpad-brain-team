---
title: Project Instructions by Role
type: onboarding
status: active
tier: curated
tags: [onboarding, claude, prompts, roles]
last_updated: 2026-10-19
related: ["[[Claude Team Setup Guide]]", "[[Client Note Schema]]", "[[Skills/00-INDEX]]"]
---

# Project Instructions by Role

One Brain, one repo, but each person's Claude should start from their job. Make **one private project
per role you play** (most people: one), attach the same `launchpad-brain-team` repo, and paste the block
for your role as the project instructions. The base block from the Setup Guide goes first, then the role
block under it.

## Base (everyone, from the Setup Guide §2 step 7)

Paste the Setup Guide block first. Then add one of these.

## Social media & content (Cynthia)

> **Your lane:** social calendars, captions, posting, client approvals. Before any client work read
> `Projects/{Client}.md` fully, then `Skills/Social Media Posting Workflow.md`, `Skills/Content Framework
> Method.md`, and the client's `## Brand Guidelines` and `## Preferences & Corrections` sections. The
> contracted posting days in `## Package & Services` are the rubric; never invent posting days. Captions:
> react or ask, never summarize; no dashes; max 5 hashtags, specific to the post; never the client's name
> as a hashtag. Check `## Open Items` for anything waiting on approval before scheduling.

## Paid media & reporting (Amber)

> **Your lane:** ad accounts, optimization, client ad reports. Before any work read `Projects/{Client}.md`,
> especially `## Ad Spend`, `## Ad Reporting Requirements`, `## CRM & Systems`. Then `Skills/Media Buying.md`
> and `Skills/Weekly Performance Review Automation.md`. Every report carries leads and cost per lead; result
> type (calls / forms / sales / awareness) comes from the client note, never assumed. Zero ROAS has three
> possible causes; say which. Report structure: Overall, Campaign, Creative, Next Steps.

## Production (Kyle)

> **Your lane:** shoot briefs, shot lists, edit briefs, media days. Read `Projects/{Client}.md` (`## Content
> Pillars`, `## Brand Guidelines`, `## Activity Log` for what was already shot), then `Skills/Shot List
> Creation.md`, `Skills/Video Production SOP.md`, `Skills/Video Editing Brief.md`, and
> `Resources/Templates/Monthly Briefs — Master Template.md`. Every video appears once, in shooting order.
> Briefs are lean: what to capture, why, where it goes.

## Operations & client comms (Abril)

> **Your lane:** onboarding, client communication, proposals, invoices, keeping Notion and the Brain in
> step. Read `Projects/{Client}.md` (`## Status`, `## Contact Info`, `## Package & Services`, `## Open
> Items`), then `Skills/Client Onboarding Workflow.md` and `Departments/` for the owning department's SOP.
> Tone: warm-professional, proactive, detailed. Anything that changes a package, a contact, or a status is
> a decision: state it plainly so the daily dump captures it.

## Per-client projects for your heavy clients (recommended, 2 minutes each)

Every agency source agrees: a project per client beats one big project, because Claude loads a small set of
notes fully instead of searching a large one. Do this for the 5 to 8 clients you touch every week:

1. **Projects → New project**, named `{Client}` (for example `Arby's Food Truck`). Private.
2. Project knowledge → **+ → GitHub → launchpad-brain-team**, and select only:
   `Projects/{Client}.md`, the `Context/` folder, and the 2 or 3 `Skills/` notes your role uses.
3. Instructions: the base block, then your role block, then one line:
   `This project is for {Client} only. Read Projects/{Client}.md first, every conversation.`
4. **Sync now** before big work. Same repo, so it stays current with the Brain.

Use the role project for cross-client work (weekly planning, comparisons, playbook questions).

## Why one repo and not one per client

Everything cross-links: a client note points to a playbook, a playbook to brand guidelines, a department
SOP to three clients. Split repos break those links and multiply syncs. The right unit of separation is the
**project instructions**, not the repo. Roles filter; the Brain stays whole.
