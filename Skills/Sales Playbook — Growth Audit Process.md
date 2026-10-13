---
title: "Sales Playbook — Growth Audit Process"
type: skill
status: active
tier: secondary
tags: [sales, lead-magnet, growth-audit, automation]
last_updated: 2026-04-21
related: ["[Sales Department]]", "[[Scoping Session 2026-04-21]]", "[[Ideal Client Profile]", "[[Skills/00-INDEX]]"]
---

# Sales Playbook — Growth Audit Process

**Purpose:** The Growth Audit is Launchpad's primary Phase 1 lead magnet. This doc is the repeatable process anyone on the sales team can run, plus the spec for the automated tool that scrapes the data.

**Positioning:** *"We'll show you what's leaking money AND what's weakening your brand. Free."*

**Two Tracks (A/B tested):**
- **Lead Track** — ROI-obsessed owners. Focuses on GBP, ads, conversion, lead response time.
- **Content Track** — brand-focused owners. Focuses on content pillars, consistency, authority signals.

Prospect picks at intake, or auditor diagnoses in 60 sec and recommends.

---

## The Auditor's Output (What the Prospect Sees)

### 1-Page PDF Report

- **Headline score:** "Launchpad Growth Grade: C+"
- **Top 3 leaks** ranked by estimated revenue impact ($X,000/mo lost)
- **Competitive snapshot** — 1–2 competitors in their metro doing better in X, Y, Z
- **Action plan:**
  - 3 fixes they can make themselves
  - 3 fixes Launchpad does for them
- **Next step CTA:** 15-min recommendation session

### 30-Min Live Delivery
Delivered via Zoom or Loom-recorded walkthrough. Human-delivered (Anthony, Abril, or Alex) to maximize trust and close rate. Auditor walks the prospect through findings live; ends with BAMFAM close.

---

## Data Points to Pull (by Category)

### Lead Track (Revenue-Focused)

| Category | What we check | Source | Automatable |
|---|---|---|---|
| **Meta Ads** | # active ads, video/graphic mix, languages, CTA destination (CRM link? Link in bio?), ad spend estimate | Meta Ad Library | ✅ Apify actor |
| **Google Ads** | # active ads, keyword intent, landing page alignment | Google Ad Transparency Center | ✅ Scraper |
| **TikTok Ads** | # active ads, format mix, audience targeting | TikTok Creative Center | ✅ Apify actor |
| **GMB Profile** | Claimed / verified, # reviews, avg rating, response rate to reviews, # photos, posting cadence, categories, open hours accuracy | Google Maps API + scrape | ✅ |
| **Website Conversion** | Page speed (Lighthouse), mobile-friendly, CTAs above the fold, lead form present, click-to-call on mobile, SSL | PageSpeed Insights + WebFetch | ✅ |
| **Lead Response Time** | Call main line + submit web form; time-to-response | Manual secret-shopper | ⚠️ Hybrid |
| **CRM Visible?** | Is there an opt-in? Thank-you page? Follow-up sequence visible? | Manual secret-shopper | ⚠️ Hybrid |
| **Reviews — Yelp / BBB** | Rating, review count, response rate | Scraper | ✅ |

### Content Track (Brand-Focused)

| Category | What we check | Source | Automatable |
|---|---|---|---|
| **IG** | Follower count, last post date, posting cadence (posts/week over 30/60/90 days), avg engagement rate, content pillar consistency, Reels vs static mix | Apify IG scraper | ✅ |
| **FB** | Page followers, last post, cadence, engagement, cross-posting from IG | Apify FB scraper | ✅ |
| **TikTok** | Follower count, last post, cadence, engagement, views trend line | Apify TikTok scraper | ✅ |
| **LinkedIn (service biz)** | Company page activity, leadership posting, employees advocating | Apify LinkedIn | ✅ |
| **YouTube** | Subscriber count, upload cadence, view distribution | Scraper | ✅ |
| **Blog / Website Content** | Last blog post date, total posts, topic coverage, SEO signals | WebFetch + scrape | ✅ |
| **Brand Authority** | Press mentions, awards, chamber memberships, Google Knowledge Panel | Web search + Grep | ✅ |
| **Bilingual Reach** | Any Spanish content? Audience comments in Spanish? | Apify scrape | ✅ |

---

## The Manual Process (Until Tool is Built)

**Estimated time:** 45 min research + 30 min call = **75 min per audit (fully manual)**.
**With tool (target):** 15 min human review + 30 min call = **45 min per audit**.

### Step 1 — Intake (5 min)
- Get business name, website URL, city
- Ask prospect: "Are you more focused on **generating more leads** (Lead Track) or **building stronger brand authority** (Content Track)?"
- If they can't pick, default to Lead Track (most common for Home Services)
- Book the audit delivery call 24–48 hours out

### Step 2 — Research (45 min manual / 15 min with tool)
Run all data-point checks above for the chosen track. Save notes in `sales/output/growth-audits/{business-name}-{date}/raw-notes.md`.

### Step 3 — Scoring (10 min)
Grade each category A–F based on rubric (below). Calculate weighted Growth Grade.

### Step 4 — Report Generation (10 min manual / 2 min with tool)
Generate the 1-page PDF using template. Name the top 3 leaks. Estimate revenue impact per leak.

### Step 5 — Delivery Call (30 min)
- Walk prospect through findings live (share screen)
- Anchor on the biggest leak first — the "oh s***" moment
- Give away implementation guidance for the 3 self-fix items
- Name what Launchpad would do for the other 3
- Close: *"Would it be useful to have a 15-min conversation about what working with us would look like?"*

### Step 6 — Follow-Up (5 min post-call)
- Send the PDF within 1 hour of call
- Log everything in GHL sub-account with tag `growth-audit-delivered`
- Book next-step call if warm; move to nurture sequence if not

---

## Scoring Rubric (Weighted)

### Lead Track Weights
- GMB: 25%
- Website conversion: 20%
- Paid Media: 20%
- Lead Response Time: 15%
- Reviews: 10%
- CRM visibility: 10%

### Content Track Weights
- IG: 25%
- Content consistency (cross-platform): 20%
- Brand authority signals: 20%
- LinkedIn (for B2B) OR FB (for local consumer): 15%
- TikTok: 10%
- YouTube/blog: 10%

### Grade bands
- A (90+): Strong, niche tuning only
- B (75–89): Solid, targeted fixes
- C (60–74): Real leaks, clear opportunity
- D (45–59): Multiple critical fixes needed
- F (<45): Foundational rebuild

**Most Home Services prospects will grade C or D.** That's the magnet's sweet spot — enough pain to act, enough foundation to improve.

---

## Growth Audit Tool — Automation Spec

**Goal:** Enter business name + website + city → scraper runs all data points in parallel → returns raw data + auto-generated draft report.

### Tool Architecture

**Input form (internal tool, built in Claude Code):**
- Business name (required)
- City (required)
- Website URL (required)
- IG handle (optional)
- Meta page ID (optional)
- Track: Lead / Content / Both

### Pipeline

1. **`growth-audit-scraper` skill** — fires all scrapers in parallel via Apify MCP
   - Calls Meta Ad Library actor
   - Calls Google Ad Transparency scraper
   - Calls TikTok Creative Center actor
   - Calls Apify IG/FB/TikTok/LinkedIn scrapers
   - Calls Google Maps GMB actor
   - Calls PageSpeed Insights API
   - Calls WebFetch for website analysis
   - Calls Yelp/BBB scrapers
   - Stores all raw data in `sales/output/growth-audits/{business}-{date}/raw-data.json`

2. **`growth-audit-scorer` skill** — reads raw-data.json, applies rubric, outputs `scores.json`

3. **`growth-audit-report-writer` skill** — generates `audit-report.pdf` using prospect's name + scores + template

4. **`growth-audit-secret-shopper` skill** — schedules 24-hour manual lead-response check (Alex/Abril confirms)

5. **`growth-audit-call-prep` skill** — generates `call-prep-notes.md` with internal talking points for live delivery

### Output folder structure

```
sales/output/growth-audits/
  {business-name}-{date}/
    raw-data.json           # all scraped data
    scores.json              # rubric scores
    audit-report.pdf         # the 1-pager for prospect
    call-prep-notes.md       # auditor internal notes
    talking-points.md        # live call script
    secret-shopper.md        # lead response test log
```

### Required MCPs (already available or pending)
- **Apify MCP** — connected, OAuth pending
- **Google Maps API** — need to add
- **PageSpeed Insights API** — need to add
- **WebFetch** — already available
- **GHL MCP** — for auto-logging the audit in the sub-account

### Build order
- Week 2 of Phase 1: v0.1 of scraper + scorer + report writer (static template)
- Week 3: Call prep + talking points generator
- Week 4: Secret shopper scheduling + full Notion integration

---

## Training: How to Run a Growth Audit (For Alex / Abril)

When a prospect is scheduled for an audit, you'll receive:
1. Calendar invite with Zoom link
2. Notion task card with prospect intake data
3. Growth Audit output folder (pre-run by the tool) with draft report + call-prep notes

**Preparation (15 min before call):**
- Review `call-prep-notes.md` — know the top 3 leaks
- Review their website + top 2 competitors' websites
- Customize the PDF with prospect's name if not pre-filled

**During call:**
- 2 min rapport, 3 min walk through findings at high level
- 20 min deep dive on top 3 leaks (share screen, narrate)
- 3 min action plan (what they can fix, what we'd fix)
- 2 min close + book next step

**After call:**
- Email PDF within 1 hour
- Log outcome in GHL sub-account
- Update Sales Mission Control dashboard

---

## Do's and Don'ts

### Do
- Give away every insight — hold nothing back
- Be specific ("your GBP response rate is 12%, industry benchmark is 60%")
- Estimate dollar impact where possible ("this alone is probably $3–5K/mo in lost revenue")
- Offer 3 self-fix actions before selling
- Reference the Case Study Quintet by vertical when appropriate

### Don't
- Don't pitch Launchpad services until minute 25+
- Don't use jargon (GMB = "your Google listing", not "GBP")
- **Don't cite [[Wamen Garage Doors]]** — outcome was not great, not a success story
- Don't overpromise ROI numbers without data backing
- Don't skip the "what you can fix yourself" section — that's what makes it feel genuine, not a sales pitch

---

*Saved: 2026-04-21. Revise after first 10 audits delivered with close-rate data.*
