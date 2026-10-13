---
title: "n8n SMM Workflow 01 - Session End of Day 2026-05-19"
type: intelligence
status: active
tier: primary
tags: [n8n, smm, workflow-01, session-recap, resume-here, apollo]
last_updated: 2026-05-19
related: ["[[n8n Workflow Roadmap]]", "[[Social Media Production Workflow]]", "[[Client Drive Registry]]", "[[Contracted Monthly Deliverables]]", "[[Intelligence/00-INDEX]]"]
---

# n8n SMM Workflow 01 — Session End of Day 2026-05-19

**Where we are.** Built the scaffolding for Apollo's social media posting pipeline (Notion task → Drive walk → GHL drafts → Slack ping). Validated it end-to-end up through the Drive folder walk. Discovered Cynthia's actual content organization is more sophisticated than initially assumed — needs a smart organizer (Claude) to interpret the folder tree rather than deterministic n8n Code nodes.

**Paused** to resume fresh tomorrow with the right architecture.

---

## What's done (committed across both repos)

### Brain side
- `Context/Client Drive Registry.md` — All 28 Google Shared Drive names + IDs pulled directly from the Drive API. Canonical reference for n8n + future workflows.
- `Context/Contracted Monthly Deliverables.md` — Per-client contractual post counts (for the future contract tripwire workflow).
- `Skills/Social Media Production Workflow.md` — Complete Cynthia/Kyle/Abril 3-phase workflow with APPROVED folder convention documented.
- `Skills/n8n Workflow Roadmap.md` — Restructured: SMM is Phase 1, sales infra moved to Phase 3.
- `Skills/n8n Orchestration Layer.md` — n8n stack overview.
- Content Calendar Notion template body — full Apollo intake + worklog + Cynthia QC checklist.

### n8n side
- `n8n-workflows/SMM-01-apollo-content-pipeline.json` — 28-node workflow JSON. Imported into n8n Cloud at `launchpadbizdev.app.n8n.cloud`.
- All credentials wired up: Notion (Apollo), Google Drive (Apollo OAuth), Slack (Apollo bot), Anthropic API key, GHL_TOKEN_CCS env var.
- Apollo Notion seat created (`apollo@launchpadbizdev.com`, user ID `33dd872b-594c-81c7-bee2-000271eeb358`).
- CCS GHL token (``[REDACTED — live GHL token; read from .env, see [[feedback_api_key_security]]]``) stored in `.env` as `GHL_TOKEN_CCS`, tested with live API call (200 OK, returns FB + IG accounts).

### Test task
- `Notion: CCS June 26' Content Calendar` (page `349b01f7-7d6d-8130-931f-e7a0f7cf3c22`) assigned to Apollo, Task Type = `📱Social Media Calendar`, Month = May, Status = `Not started`.

---

## 11 bugs we patched along the way

For posterity, so we don't repeat:

| # | Bug | Fix |
|---|---|---|
| 1 | Node version blocked n8n install locally | Switched to n8n Cloud (avoids Node 25 vs 20-22 issue) |
| 2 | Notion `pageId` field used plain string | Must be resourceLocator `{__rl, value, mode}` format |
| 3 | IF operator `exists` not valid in n8n v2 | Use `notEmpty` instead |
| 4 | clientName extraction missed `client.name` (lowercase) | Added lowercase check first |
| 5 | Drive name "Continental Currency Services" didn't match | Actual name is `Continental Currency Services (CCS)` — parenthetical suffix |
| 6 | Em-dashes in node names got mangled on JSON paste import | Replaced all `—` with `-` (ASCII only) |
| 7 | Emoji in Notion filter `📱Social Media Calendar` mangled to `üü±...` | Moved task type filter out of Notion query into a JS Code node |
| 8 | "Drive list approved files" Resource was `File`, not `File/Folder` | Resource must be `fileFolder` for search operation |
| 9 | Apostrophe in `May 26'` broke Drive query (Drive uses `'` as string delimiter) | Search by `monthRaw` only (no apostrophe), filter exact name in resolve code |
| 10 | First test runs left task status as `In production`, blocking re-tests | Pattern: reset status to `Not started` between test runs |
| 11 | "Fields" parameter in Drive node misinterpreted as drive ID | Drive ID is a separate option; Fields is for response field selection |

---

## The architectural pivot (THE big realization from end of session)

**Cynthia's APPROVED folder structure is more nuanced than initially assumed:**

```
APPROVED/
├── 1 part/                       (optional — first half of month batch)
│   ├── Carousels/
│   │   ├── {post-1-name}/        ← each subfolder = 1 carousel post
│   │   │   ├── img1.png
│   │   │   └── img2.png
│   │   └── {post-2-name}/
│   └── Stills/
│       ├── still-1.png           ← each file = 1 single-image post
│       └── still-2.png
└── 2 part/                       (optional — second half batch)
```

Videos folder is usually flat (one file = one post) but may have parts.

**The realization:** trying to deterministically walk this structure in n8n Code nodes is fragile. The structure varies. Different clients may organize differently. This is exactly where Claude is better than rules.

**The right architecture (TOMORROW'S WORK):**

```
n8n: recursively list ALL files + folders under APPROVED → flat tree
  ↓
Claude (drive-content-organizer skill): "Given this Drive structure, return a posts array"
  ↓
Posts array: [
  { type: 'carousel', files: [...] },
  { type: 'still',    files: [...] },
  { type: 'video',    files: [...] }
]
  ↓
n8n: for each post → download → upload to GHL → caption → create draft
```

This is **Stanley's pattern**: n8n moves data, Claude does judgment.

---

## What to do FIRST when we resume tomorrow

1. **Open this note** to refresh context
2. **Reset the Notion test task** status to `Not started` (or ask Apollo to do it)
3. **Build the `drive-content-organizer` skill** in `Brain/Skills/drive-content-organizer.md`
   - Input: flat tree of files + folders from Drive
   - Output: structured posts array (type, files, suggested caption hints)
4. **Update the n8n workflow:**
   - Replace the current 3-step folder walk (track → month → APPROVED) with a single "recursive list under APPROVED" step
   - Add a Claude API node that takes the file tree, returns the posts list
   - Restructure the downstream loop to iterate posts (not single files) — supports multi-image carousels
5. **Update the caption prompt** to handle different post types (single image, carousel, video)
6. **Re-fire the test** end-to-end with CCS

---

## Where to find everything

- **n8n Cloud:** `https://launchpadbizdev.app.n8n.cloud`
- **Workflow JSON:** `~/launchpad-automation/n8n-workflows/SMM-01-apollo-content-pipeline.json`
- **CCS Drive ID:** `0AICReBRzBtPqUk9PVA`
- **CCS GHL Location ID:** `xqSj47GjK0FHN4oXZ0mX`
- **Apollo Notion user ID:** `33dd872b-594c-81c7-bee2-000271eeb358`
- **CCS test task ID:** `349b01f7-7d6d-8130-931f-e7a0f7cf3c22`
- **#social-media-management Slack channel:** `C08BZ7Y7JQ3`

---

## Non-blockers for tomorrow

- All 28 client drive IDs are in [[Client Drive Registry]] — no need to re-query
- Apollo's Drive access is set up
- Apollo's Notion seat is set up
- Brain has full context for any agent picking up this work

---

## Session counter

Hours invested today: ~6 (Brain hardening + n8n scaffolding + 11 bug patches + Drive structure discovery + architectural pivot).

Tomorrow estimate: ~1.5-2 hours to build the drive-content-organizer skill, restructure the workflow, and test end-to-end.
