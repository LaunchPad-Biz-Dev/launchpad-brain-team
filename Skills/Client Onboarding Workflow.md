---
title: "Skill: Client Onboarding Workflow"
type: skill
status: active
tier: secondary
tags: []
last_updated: 2026-04-03
related: ["[[Skills/00-INDEX]]"]
---

# Skill: Client Onboarding Workflow

**Owner:** Abril Rodriguez (Creative Director)
**Supporting:** Amber Nardo (Systems/CRM), Anthony Mendoza (Strategy)
**Timeline:** 14 business days from signed proposal to launch-ready
**Source:** Notion SOP + Client Onboarding Stages

---

## Overview

This skill defines the complete client onboarding process from signed proposal to first campaign launch. It serves two purposes:
1. **Human SOP** — Step-by-step guide for the team to follow
2. **Agent Blueprint** — Structured enough that an AI agent can execute the automatable steps and flag the human-required ones

---

## Phase 1: Pre-Onboarding Setup (Days 1–2)

### 1.1 Create Google Shared Drive
**Who:** Abril or Emigen
**Automatable:** Yes

Create a new Shared Drive named exactly as the client's business name. Add these subfolders:

```
[Client Name]/
├── Login Credentials/
├── Brand Assets/
│   ├── Logos/
│   └── Brand Kit/
├── Videos/
│   └── [Month YY']/
│       ├── Raw/
│       └── Edited/
├── Photos/
│   └── [Month YY']/
└── Graphics/
    └── [Month YY']/
```

**File naming convention for edited videos:**
`[ClientAbbrev] [Month] [Clip#]-[Revision#]`
Example: `SCJ March 1-1`, `SCJ March 1-2`

**Drive members to add:**
- Abril Rodriguez (Manager)
- Antonia Andrade (Manager)
- Anthony Mendoza (Manager)
- Robert Quaintance (Manager)
- Arija Imendia (Content Manager)
- David Canizalez (Content Manager)

### 1.2 Create Client Portal in Notion
**Who:** Abril or Emigen
**Automatable:** Yes

Duplicate the CLIENT TEMPLATE in the LP Client Dashboard > Client Portals database. The portal includes:
- Content Overview board
- Quarterly Plan section
- Quick Links (Book With Us, Google Drive, Content Calendar, Reports, CRM Training, Launchpad Command Center)
- Meet Your Team section
- Deliverable Tracker

**Quick Links to configure:**
- Google Drive URL → link to the new Shared Drive
- Book With Us → client's GHL booking link
- Content Calendar → client's content calendar link
- CRM Training → `launchpadbizdev.notion.site/CRM...`
- Command Center → `app.commandcentercrm.com/`

### 1.3 Create Obsidian Brain Profile
**Who:** AI Agent (future) or Abril
**Automatable:** Yes

Create a markdown file in `/LaunchPad Brain/Projects/[Client Name].md` with this template:

```markdown
# [Client Name]

## Status
**Onboarding**

## Industry
[Industry]

## Package
[Package Name]

## Ad Spend
[Monthly ad spend or —]

## Start Date
[Date signed]

## Contact Info
- **Primary Contact:** [Name, Role]
- **Phone:** [Number]
- **Email:** [Email]
- **Address:** [Address]
- **Website:** [URL]

## Company Info
[Brief description of the business]

## Social Media
- **Instagram:** [URL]
- **Facebook:** [URL]
- **TikTok:** [URL]
- **Google Business:** [URL]
- **LinkedIn:** [URL]
- **YouTube:** [URL]
- **Yelp:** [URL]

## Brand Guidelines
- **Brand Archetype:** [Archetype]
- **Tagline:** [Tagline]
- **Brand Voice:** [Description]
- **Tone:** [Description]
- **Colors:** [Hex codes]
- **Typography:** [Fonts]
- **Visual Direction:** [Description]
- **Content Pillars:** [List]
- **Content Buckets:** [List]
- **Do's:** [List]
- **Don'ts:** [List]

## Target Audience
- **Primary:** [Description]
- **Secondary:** [Description]
- **Geographic Focus:** [Area]

## Content Strategy
- **Monthly Deliverables:** [Videos, Graphics, Ads, CRM campaigns]
- **Shoot Cadence:** [Frequency]
- **Platform Strategy:** [Per-platform approach]
- **Content Focus Split:** [Percentages if applicable]

## Systems & CRM
- **GHL Sub-Account:** [Created / Pending]
- **Pipeline Stages:** [List]
- **Automations:** [Active automations]
- **A2P Registration:** [Status]

## Google Drive
[Link to Shared Drive]

## Notion Portal
[Link to Notion client portal]

---
*Created during onboarding — [Date]*
```

### 1.4 Draft & Send Welcome Email
**Who:** Abril
**Automatable:** Partially (template auto-fill, human review before send)

Welcome email must include:
- Introduction to the Launchpad team
- Overview of the onboarding process
- Link to the Branding Questionnaire
- Link to the Business Information Form
- Link to schedule the onboarding meeting
- Google Drive collaboration link
- Mention of brand asset upload request (hex colors, guidelines, fonts, logos)

---

## Phase 2: Onboarding Meetings (Days 3–5)

### 2.1 First Meeting — Process Overview
**Who:** Abril + relevant team
**Automatable:** No (human meeting)

**Agenda:**
- Walk through the client portal in Notion
- Review the Google Shared Drive structure
- Connect social platforms (Facebook, Instagram, TikTok)
- Collect login credentials and platform access
- Set communication expectations (WhatsApp/Slack group, response times)
- Review the Branding Questionnaire responses

**Data to collect:**
- [ ] All social media login credentials
- [ ] Facebook Business Manager access (Partner access)
- [ ] Instagram credentials
- [ ] TikTok credentials
- [ ] Google Ads access
- [ ] Google Business Profile access
- [ ] Website access / CMS login
- [ ] Domain registrar (GoDaddy, etc.) access
- [ ] Existing brand assets (logos, fonts, color codes)
- [ ] Primary point of contact name + phone + email
- [ ] Secondary contact (if applicable)
- [ ] Preferred communication channel
- [ ] Business hours

### 2.2 Second Meeting — Discovery / Brand Deep Dive
**Who:** Abril + Anthony (strategy)
**Automatable:** No (human meeting, but transcript → agent can extract)

**Topics to cover:**
- Brand story and origin
- Mission, vision, values
- Target audience (who they serve, demographics, psychographics)
- Competitors and differentiation
- Tone and voice preferences
- Visual preferences (show examples, get reactions)
- Goals for marketing (awareness, leads, sales, hiring, etc.)
- Pain points and past marketing experiences
- Key services/products to promote
- Seasonal considerations
- Content comfort level (are they on camera? who is the face?)

**Data to capture for the Brain:**
- [ ] Brand archetype
- [ ] Tagline / slogan
- [ ] Brand voice description
- [ ] Color palette (hex codes)
- [ ] Typography preferences
- [ ] Visual direction (photography style, mood)
- [ ] Content pillars
- [ ] Target audience profiles
- [ ] Competitors
- [ ] Unique selling propositions
- [ ] Services/products to highlight
- [ ] Content do's and don'ts

---

## Phase 3: Create Client Assets & Strategy (Days 5–10)

### 3.1 Brand Kit Creation
**Who:** Arija or David (Graphic Design)
**Automatable:** No (creative work)
**Due:** Days 1–3 of this phase

Deliverables:
- Logo variations (PNG, transparent background, square format)
- Color palette document
- Typography guide
- Brand kit slide deck (5 slides or less)
- Social kit: Profile pictures (IG, FB), Cover photos (FB), Story highlight icons
- Mood board (Canva)

### 3.2 Quarterly Plan
**Who:** Abril + Anthony
**Automatable:** Partially (template generation, human strategy)

The quarterly plan includes:
- Client overview and brand role
- Scope and deliverables (monthly totals)
- Primary objectives for the quarter
- Q-1 review and insights (for existing clients)
- Quarterly focus areas
- Narrative arc (monthly themes)
- Content buckets mapped to pillars
- Quarterly deliverables (hard totals)
- Process updates (approval workflow, posting cadence)
- Monthly preview snapshots

### 3.3 Team Briefing
**Who:** Abril
**Automatable:** Partially (brief generation from brain data)

Brief the full team on the new client:
- Creative team: brand kit, visual direction, content buckets
- Video team: shoot schedule, content types, tone
- Systems team: CRM setup requirements, automation needs
- Social team: platforms, posting cadence, hashtag strategy

---

## Phase 4: Implementation (Days 8–12)

### 4.1 Content Setup
**Who:** Cynthia (Social), Arija/David (Design), Robert/Kyle (Video)
**Automatable:** Partially

- [ ] Social media audit of existing accounts
- [ ] Profile optimization (bios, profile photos, links, username consistency)
- [ ] Connect accounts to Sprout Social (or scheduling tool)
- [ ] First round of graphics created
- [ ] First video shoot scheduled
- [ ] Content calendar created for Month 1

### 4.2 Lead Generation Setup
**Who:** Amber (Systems/Ads)
**Automatable:** Partially

- [ ] Ad accounts created/connected (Meta, Google, TikTok as needed)
- [ ] Initial campaign structures built
- [ ] Retargeting audiences configured
- [ ] Pixel/conversion tracking installed on website
- [ ] Landing pages created (if applicable)

### 4.3 Systems & CRM Setup
**Who:** Amber
**Automatable:** Partially

- [ ] GHL sub-account created
- [ ] Pipeline stages configured
- [ ] A2P registration initiated (for SMS)
- [ ] Website form automations connected
- [ ] Facebook/Instagram lead automations built
- [ ] Calendar booking system set up with automated reminders
- [ ] Welcome/nurture sequences created
- [ ] Long-term follow-up sequences (Fast Five, then 10/30/60/90/180/365 day cadence)
- [ ] Review request automation configured

### 4.4 CRM Training
**Who:** Amber
**Automatable:** No (training session)

- Schedule in-person or Zoom training (60 min)
- Walk through system usage, pipeline, automations
- Demonstrate calendar booking, lead notifications
- Cover mobile app setup for client

---

## Phase 5: Launch (Days 12–14)

### 5.1 Final Review
**Who:** Abril + Anthony
**Automatable:** Partially (checklist verification)

Pre-launch checklist:
- [ ] Brand kit approved by client
- [ ] Social profiles optimized and connected
- [ ] Content calendar approved for Month 1
- [ ] First batch of content created and scheduled
- [ ] CRM fully built and tested
- [ ] Ad campaigns ready to launch
- [ ] Client trained on CRM
- [ ] All automations tested with sample data
- [ ] Google Business Profile verified
- [ ] Google review link ready to share

### 5.2 Go Live
**Who:** Full team
**Automatable:** No (coordinated launch)

- First posts go live
- Ad campaigns activated
- CRM automations turned on
- Client moved from "Onboarding" to "Active" status in Notion
- Obsidian Brain profile status updated to "Active"

---

## Data Collection Master Checklist

This is the complete list of information needed for a fully seeded client profile. Use this to ensure nothing is missed during onboarding.

### Business Information
- [ ] Legal business name
- [ ] DBA / brand name (if different)
- [ ] Industry / vertical
- [ ] Year founded
- [ ] Business description (2-3 sentences)
- [ ] Physical address(es)
- [ ] Phone number(s)
- [ ] Email address(es)
- [ ] Website URL
- [ ] Hours of operation
- [ ] Service area / geographic focus
- [ ] Key services or products
- [ ] Unique selling propositions

### Contract & Package
- [ ] Package level (Essential / Comprehensive / Ultimate / Ads Only / Creative Only / A La Carte)
- [ ] Monthly retainer amount
- [ ] Monthly ad spend budget
- [ ] Contract start date
- [ ] Contract term length
- [ ] Specific deliverables (videos/mo, graphics/mo, ads, CRM campaigns)
- [ ] Shoot cadence (monthly shoots, frequency)

### Team & Contacts
- [ ] Primary contact (name, role, phone, email)
- [ ] Secondary contact (name, role, phone, email)
- [ ] Decision maker for approvals
- [ ] Who is the "face" of the brand (on-camera talent)
- [ ] Preferred communication channel (WhatsApp / Slack / Email)

### Brand Identity
- [ ] Brand archetype
- [ ] Tagline / slogan
- [ ] Mission statement
- [ ] Brand story / origin
- [ ] Brand voice (3-5 descriptors)
- [ ] Tone guidelines
- [ ] Color palette (hex codes)
- [ ] Typography (heading font, body font, accent font)
- [ ] Logo files uploaded to Drive
- [ ] Visual direction / photography style
- [ ] Content do's
- [ ] Content don'ts
- [ ] Competitor brands (2-3)

### Target Audience
- [ ] Primary audience (demographics + psychographics)
- [ ] Secondary audience
- [ ] Geographic targeting
- [ ] Pain points the audience has
- [ ] What motivates them to buy/engage

### Social Media & Digital
- [ ] Instagram handle + credentials
- [ ] Facebook page + Business Manager access
- [ ] TikTok handle + credentials
- [ ] LinkedIn page (if applicable)
- [ ] YouTube channel (if applicable)
- [ ] Google Business Profile + verification status
- [ ] Yelp page (if applicable)
- [ ] Website CMS access
- [ ] Domain registrar access
- [ ] Google Ads account
- [ ] Meta Ads account
- [ ] TikTok Ads account

### Systems
- [ ] GHL sub-account created
- [ ] Pipeline stages defined
- [ ] A2P registration status
- [ ] Automations list (welcome, nurture, follow-up, review)
- [ ] Calendar/booking link

---

## Future Onboarding Agent Blueprint

**Goal:** Once the onboarding form is completed in Notion, an AI agent automatically handles the setup steps so the team can focus on creative and strategy work.

### What the Agent Should Do Automatically:
1. **Read** the completed onboarding form from Notion
2. **Create Google Shared Drive** with the standard folder structure
3. **Create Notion Client Portal** from the template, populate Quick Links
4. **Create Obsidian Brain profile** using the template above, pre-filled with all available data
5. **Generate welcome email draft** pre-filled with client info and links
6. **Create GHL sub-account** and configure default pipeline
7. **Set up initial content calendar** template for Month 1
8. **Notify the team** via Slack with a summary of the new client

### What the Agent Should Flag for Humans:
- Missing data fields (brand colors, logos, credentials not yet provided)
- Brand kit creation needed (assign to Arija or David)
- Discovery meeting not yet scheduled
- CRM training not yet scheduled
- Any credentials still pending from client

### What Stays Human-Only:
- Discovery meeting and brand deep dive
- Brand kit design and creative direction
- Quarterly plan strategy
- Content creation (video, photo, graphics)
- CRM training session
- Client relationship management

### Technical Requirements:
- Notion MCP (read onboarding form, create portal from template)
- Google Drive API (create shared drive, folders, set permissions)
- GHL API (create sub-account, pipeline, automations)
- Slack MCP (send team notifications)
- File system access (create Obsidian Brain markdown files)
- Scheduled trigger (watch for new "Signed" status in Notion pipeline)

### Trigger:
When a client's status changes to "Signed & Paid" in the Notion pipeline, the agent activates and begins the automated setup sequence.

---

## Related
- [[New Client Onboarding Process]]
- [[CRM and GHL Workflow]]
- [[Content Workflow — Shoot to Post]]
- [[Packages and Pricing]]
- [[Sales Department]] — Sales pipeline and handoff process
- [[Sales Playbook — Scripts and Objection Handling]] — Pre-sale scripts and process
- [[Launchpad Brand Guidelines]]
