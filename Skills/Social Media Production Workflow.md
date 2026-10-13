---
title: "Social Media Production Workflow"
type: skill
status: active
tier: primary
tags: [social-media, cynthia, kyle, abril, workflow, automation-target, ghl, notion, google-drive]
last_updated: 2026-05-18
related: ["[[Cynthia Hernandez]]", "[[Kyle Fuller]]", "[[Abril Rodriguez]]", "[[Arija Imendia]]", "[[David Canizalez]]", "[[Ral Luna]]", "[[Munzelle Jazz]]", "[[n8n Workflow Roadmap]]", "[[Brain Standards]]", "[[Skills/00-INDEX]]"]
source: "Captured 2026-05-18 from Anthony — verbatim process map"
---

# Social Media Production Workflow

**The end-to-end process for producing and publishing social media content across 13+ client accounts.** This is the authoritative documentation. Any agent or n8n workflow that touches social media production reads this first.

Owner: [[Cynthia Hernandez]] (production lead) + [[Kyle Fuller]] (video) + [[Abril Rodriguez]] (oversight)

---

## The 3 Phases

```
Phase 1: IDEATION       →   Phase 2: CREATION        →   Phase 3: POSTING
(briefs)                    (graphics + video + photo)    (Cynthia owns)
Cynthia + Kyle + Abril      Designers + Editors           Cynthia + GHL
```

---

## Phase 1 — Ideation

**Owners:** Cynthia + Kyle + Abril
**Output:** 2-3 briefs per client per month

1. The team meets to ideate content for each client for the upcoming month
2. They produce up to 3 briefs per client:
   - **Graphics brief** (always)
   - **Video brief** (always)
   - **Photography brief** (sometimes — only when shoots are needed)

Briefs live in Notion. Each brief identifies the deliverable count, theme, target platforms, and any campaign tie-ins.

---

## Phase 2 — Creation

### 2A. Graphic Design Track

**Owners:** [[Cynthia Hernandez]] (briefs + QC) + [[Arija Imendia]] + [[David Canizalez]] (production)

1. Cynthia creates a Notion task with the graphic design brief
2. Notion task assigned to a designer (Arija or David)
3. Designer uses **Canva** or **Adobe Illustrator**
4. Designer uploads completed graphic to the client's **Google Drive folder**
5. Cynthia QCs in Drive — checks for:
   - Wrong logos
   - Bad-quality photos
   - Typos
   - Wrong brand colors
   - Anything off-brand
6. If revisions needed → Cynthia comments directly on the file in Drive
7. Designer addresses comments, uploads as `v2` (or `v3`, etc.)
8. Cycle repeats until QC passes
9. When passed → content sits in Drive ready for Posting (Phase 3)

### 2B. Video Track

**Owners:** [[Kyle Fuller]] (shooter + QC) + [[Ral Luna]] + [[Munzelle Jazz]] (editors)

1. Kyle creates a Notion task when starting work on the brief
2. Kyle shoots the content with clients per his brief
3. Kyle uploads raw footage to Google Drive
4. Kyle sends the raw footage to editors with:
   - The initial content brief
   - A separate edit brief (how he wants it cut)
5. Editors (Ral + Munzelle) divide the work and track progress on the Notion board
6. When edits are ready, Kyle reviews
7. Kyle documents revisions — **on Notion preferred** (for tracking) or Slack
8. Editors apply revisions and re-upload
9. Cycle repeats until QC passes
10. When passed → content sits in Drive ready for Posting (Phase 3)

### 2C. Photography Track *(when applicable)*

Same shape as video — shoot, upload raw, edit if needed, QC, file in Drive.

---

## Phase 3 — Posting (Apollo owns, Cynthia approves)

**Owner:** 🤖 Apollo (autonomous), with [[Cynthia Hernandez]] approval
**Goal of automation:** collapse this entire phase from "manual juggling across tools" to "Cynthia briefs Apollo, then approves what he produces."

---

### 🗂️ Drive Folder Convention — the APPROVED rule (adopted 2026-05-18)

**Every client's shared Drive folder follows this structure for content that's ready to post:**

```
{Client} (shared Drive)
├── GRAPHICS/
│   └── {Month YY'}/                  (e.g. May 26')
│       ├── (raw + revision versions)
│       └── APPROVED/                 ← ONLY content in here is ready to post
└── VIDEOS/
    └── {Month YY'}/
        ├── (raw + revision versions)
        └── APPROVED/                 ← ONLY content in here is ready to post
```

**Rules:**
1. Content must pass QC (Phase 2A or 2B) **before** moving into `APPROVED/`
2. **The move into `APPROVED/` IS the signal Apollo can post it.** Anything not in `APPROVED/` is invisible to Apollo.
3. Only Cynthia (or the QC owner per content type) moves files into `APPROVED/` — designers and editors do NOT
4. Once posted, files stay in `APPROVED/` for the month — don't move them again
5. Empty `APPROVED/` folder = nothing for Apollo to do → he reports back "no approved content found"

---

### 🤖 Apollo's automated steps (Workflow 01)

When a Notion task with `Task type = 📱Social Media Calendar` is assigned to Apollo:

1. Read the task's **Month property** (NOT the task name — task names like "June 26' Content Calendar" can be misleading; the Month field is canonical)
2. Locate the client's shared Drive by name (no registry needed — Apollo has access to all client drives)
3. Navigate `{Client}/GRAPHICS/{Month YY'}/APPROVED/` for graphics, `{Client}/VIDEOS/{Month YY'}/APPROVED/` for videos (or both depending on content type checked in brief)
4. Upload each approved file to GHL Media Library via `ghl-media-upload.sh` with the client's sub-account token
5. Generate caption + hashtags per file using Content Creator agent loaded with client's brand voice from `Brain/Projects/{Client}.md`
6. Create draft post in GHL Social Planner with:
   - Right accounts per client (from `get-account` call)
   - Right post type per platform (TikTok=video only, IG/FB=carousel OK, LinkedIn=single image)
   - Caption in body, hashtags in followUpComment for IG
7. Write the GHL Social Planner URL into the Notion task's `Content Calendar Link` field
8. Update Notion task status: `Not started` → `In production` (on pickup) → `Needs Team Review` (when drafts ready)
9. **Send Slack notification to `#social-media-management`** with:
   - Client name + month
   - Draft count + platforms
   - **Link to the Notion task** (so Cynthia clicks straight through to review)
   - Format: `🤖 {Client} {Month} content drafts ready for QC — {count} posts across {platforms}. Review: {Notion task link}`

### Current manual steps (today — pre-automation, for reference)

1. Cynthia goes to the client's Google Drive folder
2. Identifies content that has passed QC
3. **Manually downloads** each file
4. **Uploads to GHL Media Library** (per client sub-account)
5. From Media Library → adds to **Social Media Planner** under the Marketing tab in GHL
6. For each post, Cynthia configures:
   - **Caption** (must match brand voice per client)
   - **Hashtags** (per brand strategy)
   - **Social media accounts selected** (only the platforms the client is active on)
   - **Post type per platform** (video for TikTok, carousel for IG/FB, single image for LinkedIn, etc.)
   - **Tags or collabs** if the brief specifies them or if they make sense for the post
7. Cynthia visually confirms against brand guidelines per client
8. Cynthia checks the contracted post count for the month

### Critical rules (NEVER violate)

1. **All content must follow brand guidelines per client.** Each client's brand voice, color palette, typography, and content pillars are documented in `Brain/Projects/{Client}.md`. The Brand Compliance agent enforces this.
2. **All content must match contracted post count.** Each client has a guaranteed monthly post count per their package.
   - **MORE than the contract = fine** (over-deliver is good)
   - **LESS than the contract = NEVER allowed** (contractual short = breach)
   - Any discrepancy must trigger a notification
3. **Right post type per platform.** TikTok only accepts video. Carousels go to IG + FB only. LinkedIn = professional single images. GBP = local-focused content.
4. **Drafts first, never direct-publish.** All posts created as drafts in GHL Social Planner. Cynthia/Abril reviews before scheduling.

---

## Tools used in the workflow

| Tool | Purpose | Owner |
|---|---|---|
| **Notion** | Briefs, task assignment, content calendar, edit tracking | Cynthia, Kyle, designers, editors |
| **Canva** | Graphic design | Arija, David |
| **Adobe Illustrator / Creative Suite** | Advanced graphic design | Arija, David |
| **Google Drive** | Source-of-truth file storage, QC review, comments | Everyone |
| **GoHighLevel (GHL)** | Media Library + Social Media Planner = scheduling/publishing | Cynthia |
| **Sprout Social** | *(Legacy — being phased out toward GHL-first?)* | Cynthia |
| **Slack** | Revision communication (Notion preferred for video tracking) | Kyle, editors, Cynthia |

> **TODO clarify with Cynthia:** is Sprout Social still in active use or is the workflow fully migrating to GHL? The Social Media Poster agent is GHL-only.

---

## Content Count Verification — The Contractual Tripwire

Every client has a monthly post count baked into their package (see `Brain/Context/Packages and Pricing.md` and each client's `Projects/{Client}.md` Section 6).

**The rule:** at any point in the month, Cynthia must know:
- How many posts have been **scheduled** so far this month
- How many posts have been **published** so far this month
- How many remain to meet the contract
- Whether we're on pace, over-pace, or under-pace

Today this is checked manually. The n8n automation target: compute this on a weekly cadence + alert the moment we're projected to fall short.

---

## Approval / Feedback Loop *(Track C — automate LATER)*

The revision back-and-forth between Cynthia / Kyle, the designers/editors, and clients is its own bottleneck. The pieces:

- **Internal QC:** Cynthia comments on Drive files, designers/editors respond, re-upload
- **Client approval:** Some clients review content before scheduling — handled per-client via email, GHL chat, or Slack guest channels
- **Revision routing:** When a client wants changes, Cynthia must:
  1. Document what the client wants
  2. Route it to the right designer/editor
  3. Track that the revision happened
  4. Re-QC the result
  5. Re-upload to GHL

**Why we're parking this for now:** automating this requires Phase 2 of the n8n roadmap (communication ingestion). Once Slack + email + Notion + Drive comments are all flowing into the Brain via n8n, we can build a "revision feedback loop" workflow that auto-routes revisions, tracks them, and notifies the right people.

→ See [[n8n Workflow Roadmap]] — circle back to this once Workflows #06-09 ship (Slack, Email, Drive Comments → Brain).

---

## Why this doc exists

This is the operational source-of-truth for social media production at Launchpad. Every agent that touches Cynthia's pipeline reads this. Every n8n workflow that automates a piece of it references this. When Cynthia (or a future replacement) needs to onboard someone new, they read this first.

If the process changes, **update this doc** — never let drift happen silently.
