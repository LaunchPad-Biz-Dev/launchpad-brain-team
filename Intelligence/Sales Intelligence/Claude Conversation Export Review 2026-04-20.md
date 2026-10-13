---
title: "Claude Conversation Export — Sales Team Review (2026-04-20)"
type: intelligence
status: active
tier: secondary
tags: [sales, review, ai-sales-team, infrastructure]
last_updated: 2026-04-20
related: [[Scoping Session 2026-04-21]], [[100M Leads — Hormozi Master Breakdown 2026-04-09]]
---

# Claude Conversation Export — Sales Team Review

Anthony shared a Claude conversation export (`launchpad-ai-sales-team-roadmap.md`) with a proposed tech stack + phase-by-phase roadmap for cold outreach. This is the review.

## Verdict
**Tactically solid but strategically narrow.** Useful as a cold-outreach infrastructure spec; dangerous as a whole-sales strategy. Covers ~30% of what we need (cold outreach); missing the other 70% (warm, content, referrals, magnet, economics).

## What to KEEP from the export
1. **Domain protection principle** — secondary domains for cold; main GHL domain stays clean. Non-negotiable.
2. **Tool gap analysis** — correct. Claude genuinely cannot warm email domains (Instantly), cannot run LinkedIn bulk safely (SalesRobot), cannot bypass Meta DM limits.
3. **Zapier → GHL (qualified-only) handoff** — smart. Only engaged leads in CRM.
4. **Reply qualification schema (Hot / Warm / No / OOO)** — buildable as a skill spec.
5. **Volume math** — realistic. 1,000 touches → 35 replies → 12 qualified → 4–6 calls → 1–2 clients/mo.
6. **Claude-drafts-humans-approve pattern** — matches our existing Apollo rules.
7. **Multichannel (287% more responses)** — defensible benchmark.

## What to MODIFY or REJECT
1. **Leading with cold as the whole strategy.** Hormozi's Core Four: Warm, Content, Cold, Paid. Plan is 90% Cold. Phase 1 must lead with warm + content + referrals.
2. **Skipping content (#2 Core Four).** @anthony.launchpad + Kyle's 2.5M upstream audience ignored.
3. **Skipping the lead magnet entirely.** Personalized first lines are not a lead magnet. Without Grand Slam magnet, cold underperforms 5–10x.
4. **Skipping referrals (our 80% revenue source).** Not mentioned once in the export.
5. **Skipping affiliates.** Vegas-dense opportunity (CPAs, chambers, brokers, event venues) ignored.
6. **ICP as Phase 1 Task 1 is a chicken-egg.** Everything downstream depends on ICP — must be done BEFORE Phase 1, not during.
7. **No LTGP:CAC math.** Spending $280/mo on tools + projecting 1–2 clients/mo without naming LTGP = gambling.

## Tool duplication with existing LP stack
- **Apify MCP** already connected (needs OAuth finalization) — handles prospect research + scraping. Reduces reliance on Instantly for list building.
- **GHL MCPs** already wired (agency + launchpad sub-account).
- **Apollo Slack Inbox** already exists for reply triage.
- **Claude Max $100/mo** — likely redundant given existing Code + SDK setup.
- **Zapier** may be replaceable by GHL MCP direct wiring.
- **Real net new spend:** ~$180/mo (Instantly + SalesRobot + domains), not $280.

## How the export PLUGS INTO our Hormozi roadmap

| Claude export component | Maps to [[sales-team-agent-roster-v1]] as |
|---|---|
| Prospecting Agent (Week 3) | Cold Outreach Agent — Phase 2 Agent #6 |
| Outreach Agent (Week 4) | Cold Outreach Agent skills |
| Qualification Agent (Weeks 5–6) | CRM Hygiene + Scoring Agent — Phase 1 Agent #4 |
| Performance Report Agent (Month 2+) | Pipeline Analyst Agent — Phase 2 Agent #8 |

**The export is a detailed build spec for 2 of our 10 proposed agents + the external infrastructure (Instantly, SalesRobot, secondary domains) our Hormozi roadmap didn't detail.** Genuinely useful in that scope.

## Synthesized decision (per Scoping Session 2026-04-21)
- Take the export's **infrastructure architecture** (domains, warmup, qualifier, webhook to GHL) and graft it **underneath** the Hormozi-grounded strategic plan.
- Export = Phase 2 infrastructure layer, not the whole strategy.
- Cold outreach starts **passive warmup Day 1**, active Day 30 (per Q21 lock).

*Saved: 2026-04-20. Superseded in part by [[Scoping Session 2026-04-21]].*
