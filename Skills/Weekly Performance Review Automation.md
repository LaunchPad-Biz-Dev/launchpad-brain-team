---
title: "Skill: Weekly Performance Review Automation"
type: skill
status: active
tier: secondary
tags: []
last_updated: 2026-04-03
related: ["[[Skills/00-INDEX]]"]
---

# Skill: Weekly Performance Review Automation

## What This Does
Every Friday, this agent automatically:
1. Reads all new submissions from the Launchpad Weekly Check-In form in Notion
2. Updates each team member's note in the Obsidian Teams folder with that week's entry
3. Flags anything that needs Anthony's attention
4. Creates a weekly summary in the Intelligence folder

## Notion Source
Weekly Update Form: https://www.notion.so/launchpadbizdev/72b5d97d3b3645e5ac11b9ae989e490d
Data Source ID: collection://e8dba2a0-8450-4473-9b03-de3b90d9c069

## Form Fields Captured
- Employee Name
- Week Ending (date)
- Overall Status — On Track / At Risk / Off Track
- Workload Rating — Light / Manageable / A bit heavy / Overwhelming
- Projects This Week
- Review your work
- Need Support — Yes / No
- Support Details (if Yes)
- Next Week Priorities
- Meeting Agenda Items
- Additional Comments

## Flagging Rules
Automatically flag a submission when ANY of these are true:
- Overall Status = At Risk or Off Track
- Need Support = Yes
- Workload Rating = Overwhelming

## Output 1 — Update Team Member Note in Obsidian
For each submission, append a new weekly entry to the relevant file in Teams/:

### Entry Format
---
## Week of [Week Ending Date]
**Status:** [Overall Status]
**Workload:** [Workload Rating]
**Projects:** [Projects This Week]
**Work Review:** [Review your work]
**Next Week:** [Next Week Priorities]
**Meeting Agenda:** [Meeting Agenda Items]
**Needs Support:** [Yes/No] — [Support Details if yes]
**Notes:** [Additional Comments]
⚠️ FLAGGED — [reason] (only if flagged)
---

## Output 2 — Weekly Intelligence Summary
Create a new note in Intelligence/ named:
Weekly Review — [Week Ending Date].md

Include:
- Summary of all submissions
- List of flags with employee name and reason
- Patterns (e.g. multiple people overwhelmed = systemic issue)
- Meeting agenda items compiled from all submissions
- Anthony's action items based on flags

## Existing Notion Views to Leverage
- All Submissions — full history grouped by week
- This Week — filtered to current week only
- Needs Support — filtered to support requests only (already built!)

## Build Requirements
- Claude Code agent with Notion MCP connected
- Scheduled to run every Friday at end of day (e.g. 5pm PST)
- Reads from Notion Weekly Update Form database
- Writes to Obsidian launchpad-brain/Teams/ folder
- Writes weekly summary to Obsidian launchpad-brain/Intelligence/ folder

## Status
⏳ PLANNED — Ready to build when Claude Code agent setup begins

## Related
- [[Teams]] (all team member notes)
- [[Intelligence]] (weekly summaries will live here)
- Notion Weekly Update Form (source data)
