---
date: 2026-11-09
type: synthesis
tags: [synthesis, notion-sync, data-quality, meeting-notes]
related: ["[[DRG]]", "[[Shumi Store]]", "[[Lucky RX]]", "[[Helix Electric]]"]
---

# Compile Synthesis — Notion Meeting Sync Stub Gap (2026-11-09)

## The Pattern
Compiled 6 unprocessed Notion meeting exports from `Raw/exports/` today (2026-11-09 brain-compile run). Of those 6, **4 carried zero real meeting content** — only metadata (date, attendee count, generic topic headers) with the actual summary/decisions/action-items fields either blank, boilerplate ("Full details to be ingested via brain-compile" / "See full meeting notes in Notion"), or explicitly flagged `needs_notion_followup: true`:

- `notion-meeting-2026-10-19_team-sync.md` — "Evening team sync," 6 attendees, zero content
- `notion-meeting-2026-10-19_one-on-one.md` — 2 attendees, zero content
- `notion-meeting-2026-10-26_team-meeting.md` — "Lucky RX context" inferred only from the URL, zero content
- `notion-meeting-2026-11-03_shumi-weekly.md` and `notion-meeting-2026-11-03_arbys-taco-bell-sync.md` — generic topic headers, no actual figures/decisions
- `notion-meeting-2026-10-27_video-production-coordination.md` — turned out to be a duplicate; the real content for that meeting was already captured in [[Helix Electric]]'s Activity Log on 2026-10-27 through a different path (same-day conversation capture), so this one cost nothing — but it confirms the raw Notion export itself carried no usable detail.

This is not a one-off: [[DRG]] already has an identical stub flagged from 2026-07-29 (`notion-meeting-2026-07-29_drg-merchandise`), where Key Decisions and Action Items literally read "TBD (Meeting note content pending)."

## Likely Cause (unverified)
The Notion-to-Brain sync is capturing the meeting *page metadata* (title, date, attendees, last-edited) reliably but not the actual page body for a subset of meetings — possibly ones where the Notion meeting-notes AI summary hadn't finished generating yet at sync time, or where the page structure doesn't match what the sync script expects to extract. Worth checking `notion-brain-sync` and `meeting-action-extractor` skill logic against one of these specific pages directly in Notion to confirm.

## Why It Matters
Every client note now treats these as logged meetings ("a sync happened on this date") but the Brain has **no actual decisions or action items** from roughly half of recent meeting syncs. Reflection-analyst and future agents reading these notes could assume more context exists than actually does. [[Lucky RX]] is a particular risk — that client already has a known cross-team content-misrouting problem (`project_lucky_rx_dm_misrouting` memory, 7+ instances unresolved since 09-21), and a Notion export that only weakly implies "a meeting happened with Lucky RX context" adds another ambiguous data point rather than a resolving one.

## Recommended Action
- Anthony or a future session should spot-check 2-3 of these Notion pages directly to see if real content exists there that the sync is failing to pull, vs. the meeting notes genuinely never got filled in by the human attendees.
- If it's a sync bug: fix extraction in the relevant skill.
- If it's attendees not filling in notes: this is a process gap, not a technical one — maybe worth a reminder nudge.

## Sources Compiled
- [[Raw/exports/notion-meeting-2026-11-03_shumi-weekly]] → [[Shumi Store]]
- [[Raw/exports/notion-meeting-2026-11-03_arbys-taco-bell-sync]] → [[DRG]]
- [[Raw/exports/notion-meeting-2026-10-26_team-meeting]] → [[Lucky RX]] (stub flag only)
- [[Raw/exports/notion-meeting-2026-10-27_video-production-coordination]] → [[Helix Electric]] (duplicate, no new content)
- `Raw/exports/notion-meeting-2026-10-19_team-sync.md` — no related entity, zero content, nothing to file
- `Raw/exports/notion-meeting-2026-10-19_one-on-one.md` — no related entity, zero content, nothing to file
