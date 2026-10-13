---
title: "Contracted Monthly Deliverables"
type: context
status: active
tier: primary
tags: [contracts, deliverables, social-media, automation-input]
last_updated: 2026-10-08
related: ["[[Social Media Production Workflow]]", "[[Packages and Pricing]]", "[[n8n Workflow Roadmap]]", "[[Context/00-INDEX]]"]
source: "https://www.notion.so/22bb01f77d6d8031aab2d09279d49ead (Notion: Social Media Posting Schedule SOP)"
---

# Contracted Monthly Deliverables

**The minimum content count per client per month. NEVER deliver less than these numbers — contractual breach.** Over-delivery is fine, under-delivery is not.

This table is the **input data for n8n Workflow #05** (Weekly Contract Count Check). When any client is projected to fall short, `#admin-ish` gets pinged.

Last refreshed 2026-05-18 from Notion SOP. Verify monthly against active contracts.

---

## 📅 LIVE Posting Calendar — the canonical scheduling source

The exact per-client, day-of-month posting schedule lives in Notion:
**[Content Monthly Deliverables 🚀](https://www.notion.so/263b01f77d6d802ca9c8fe76c5a98dd0)** — page ID `263b01f77d6d802ca9c8fe76c5a98dd0`.

Each client has a day-of-month grid showing exactly which dates get a Graphic and which get a Video, plus their platforms and content approver. The `social-media-poster` agent reads this **live on every run** (Step 4) — it is NEVER cached.

**Maintenance practice:** the team adds new clients and edits cadences on that page over time. The agent self-checks each run — if a client it's processing isn't on the page, or is on the page but missing from our GHL/Drive wiring, it flags it. Additionally, review that page during the **weekly Brain maintenance** to catch new clients before their first task lands, and reconcile any cadence changes here.

**CCS posting calendar** (Ultimate — 24 Graphics / 16 Videos · IG/FB/TikTok · approver Terrance):
- Graphic + Video on days: 2, 3, 5, 6, 9, 10, 12, 13, 16, 17, 19, 20, 23, 24, 26, 27
- Graphic only on days: 4, 8, 11, 14, 15, 18, 21, 25
- No Sunday posts.

---

---

## ⚠️ 2026-10-08 — the table below is STALE vs the live Notion page

Read live from **[Content Monthly Deliverables 🚀](https://www.notion.so/263b01f77d6d802ca9c8fe76c5a98dd0)** on 2026-10-08 while scheduling November videos. Two clients disagree with the table in this note:

| Client | This note says | Notion (live) says |
|---|---|---|
| **Toro Taxes Franchises** | 8 videos / 8 graphics | **4 videos / 14 graphics** (Custom) |
| **Taco Bell Cantinas** | 4 videos / 8 graphics | **10 videos / 10 graphics** (Essential) |

**The Notion page wins** — this note's own header says so, and it is the page the agent is told to read live every run. Leaving the table below untouched for Anthony/Cynthia to reconcile rather than editing counts I cannot verify against the contracts.

**The Notion page also carries a day-of-WEEK grid per client that this note does not**, and that grid is what actually drives scheduling:

- **Toro Taxes:** videos on **Saturday** (one per week, 4/mo). Graphics Mon/Tue/Thu.
- **Taco Bell Cantinas:** videos on **Wed + Fri every week, plus Tuesday in weeks 1 and 3** (10/mo). Graphics Mon + Thu, plus Tuesday in weeks 2 and 4.

The week rows are **weekday positions, not dates** — the 1–31 numbers in the grid are a generic month template. See [[feedback_contracted_posting_cadence]].


## Active Client Deliverables

| Client | Package | Videos | Graphics | Social Posts |
|---|---|---|---|---|
| **Ben Nadig Law** | Comprehensive | 16 | 10 | 26 |
| **Matsuda Nadig Law** | Comprehensive | 16 | 10 | 26 |
| **Continental Currency Services** | Ultimate Business Builder | 16 | 24 | 40 |
| **Blue Mountain Energy** | Ultimate Business Builder | 16 | 24 | 40 |
| **Toro Taxes** | Essential Growth | 8 | 8 | 16 |
| **Arby's Food Truck** | Essential | 4 | 8 | 12 |
| **Taco Bell Cantinas** | Essential | 4 | 8 | 12 |
| **Brand With Us** | Essential | 4 | 4 | 8 |
| **LaunchPad Business Development** | Essential | 4 | 4 | 8 |
| **Sobel Westex** | Digital Advertising | varies (UGC quarterly) | varies (seasonal) | none |

---

## Notes

- **Social Posts** = total monthly post count across all platforms
- **Videos + Graphics** rolls up into Social Posts but they're tracked separately
- **Sobel Westex** is ad-only; no social posting commitment in their contract
- **Other active clients** (365 Plumbing, Upbeat Health, Afshar Law, Muller Masks, Wamen Garage Doors, Toro Taxes Franchise Sales, Matsuda Nadig Van Law) — counts to confirm with Cynthia. This list may be stale.

---

## How Apollo uses this

Workflow #05 runs Sundays 6 PM. It:
1. Queries GHL Social Planner per client for scheduled + published count this month
2. Looks up the client's contracted count from this doc
3. If `actual < contracted` AND days remaining in month are insufficient to catch up → fire alert in `#admin-ish`
4. Sends a digest to Cynthia + Abril regardless ("you're on pace" / "you're ahead" / "you're behind")

---

## Maintenance

When a client signs/cancels/upgrades:
1. Update this doc immediately
2. Verify it matches `Brain/Projects/{Client}.md` Section 6 (Platform Strategy)
3. Verify it matches the contract in PandaDoc / GHL invoicing
