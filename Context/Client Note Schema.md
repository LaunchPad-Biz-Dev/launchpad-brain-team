---
title: Client Note Schema
type: infrastructure
status: active
tier: curated
tags: [brain, schema, projects, filing]
last_updated: 2026-10-19
related: ["[[Brain Standards]]", "[[Frontmatter Spec]]", "[[Projects/00-INDEX]]", "[[Claude Team Setup Guide]]"]
---

# Client Note Schema

Every client lives in exactly one note: `Projects/{Client}.md`. It is the unit the team's Claude reads
before any client work, and the unit the nightly filing writes into. Both only work if every note has
the same sections in the same order. This is the contract.

## Sections (in this order)

| Section | Owner | What goes here |
|---|---|---|
| `## Status` | Anthony / Apollo | Active, paused, churned. Start date. Package. |
| `## Company Info` | Onboarding | Industry, locations, website, entity, what they sell. |
| `## Contact Info` | Onboarding | Decision maker, approver, day-to-day contact. No personal numbers for non-contacts. |
| `## Package & Services` | Anthony | What we deliver, cadence, contracted posting days (the CMD rubric). |
| `## Team Roster` | Anthony | Who at Launchpad owns what for this client. |
| `## Brand Guidelines` | Creative | Voice, tone, colors, fonts, hashtag rules, do-not-say list, approved examples. |
| `## Content Pillars` | Strategy | Viral vs evergreen pillars, platform strategy. |
| `## CRM & Systems (GoHighLevel)` | Systems | Location ID, calendars, funnels, automations. Never tokens. |
| `## Ad Spend` / `## Ad Reporting Requirements` | Ads | Budgets, platforms, result type (calls / forms / sales / awareness). |
| `## Preferences & Corrections` | **Nightly filing** | One dated line per thing the client or team wants a certain way, and every time the Brain was wrong. `- (2026-10-19, via Cynthia) Blue hearts only, never red.` |
| `## Decisions` | **Nightly filing** | One dated line per decision, with who decided. |
| `## Activity Log` | **Nightly filing** | One dated line per day a teammate touched the client: what shipped, where it lives. Newest first. |
| `## Open Items` | **Nightly filing** | What is blocked or waiting, on whom, since when. Remove a line only when it closes (dated). |
| `## Sync Log` | notion-brain-sync | Automated. Do not hand-edit. |

The four **nightly filing** sections are where team daily dumps land (brain-dump Step 6.6). They are
append-only and dated. Anything that becomes permanent truth (a standing preference, a changed package)
gets promoted up into the owning section by Apollo or Anthony, with the dated line left in place.

## Rules

1. One client, one note. Sub-notes (campaign briefs, decks) link from it; they do not replace it.
2. Never delete. Corrections go next to the old line with a date; the old line gets `(superseded 2026-10-19)`.
3. Dated lines use `(YYYY-MM-DD, via Name)` so the team's Claude can judge freshness and source.
4. Section names are exact. The filing step and the team instructions look for them by name.
5. Missing sections were back-filled empty on 2026-10-19. Empty is fine; wrong name is not.
