---
title: "Frontmatter Spec — Brain Note Standard"
type: infrastructure
status: active
tier: primary
tags: [system, standard, frontmatter]
last_updated: 2026-05-18
related: ["[[index]]", "[[CLAUDE]]", "[[Context/00-INDEX]]"]
---

# Frontmatter Spec — Brain Note Standard

**Adopted 2026-05-18.** Adds the `tier` field to all Brain notes so agents (especially brain-query) can rank retrieval by priority. Adopted from attn:seeker webinar — see comparison note in Intelligence/.

---

## Required fields (every Brain note)

```yaml
---
title: "Note Title in Quotes"
type: project | context | intelligence | infrastructure | daily | reference | skill | team | playbook
status: active | archived | draft
tier: primary | secondary
tags: [tag1, tag2]
last_updated: YYYY-MM-DD
related: ["[[Other Note]]", "[[Another Note]]"]
---
```

---

## `tier` rules — which value to use

### `tier: primary`
Files agents should ALWAYS be aware of. Loaded first by brain-query, indexed by graphify as top-level nodes.

- `index.md`, `CLAUDE.md`, `log.md`
- Anything in `Projects/` (active client notes + project MOCs)
- Anything in `Context/` (core framework, brand guidelines, playbooks, specs)
- `Onboarding/` master docs
- `Sales Playbook.md`
- Team roster top-level docs
- Frontmatter specs, system docs

### `tier: secondary`
Files relevant only when specifically needed. Loaded by brain-query only when a query routes there.

- `Intelligence/` notes (research, comparisons, webinar synthesis)
- `Daily/` notes (dated logs)
- `Raw/` (unprocessed captures)
- `_archive/` (historical, kept for reference but not active)
- `Tasks/` (transient)
- `Strategic Partners/` (reference data)
- `Resources/` (lookup material)

### Default
If unsure: `tier: secondary`. Promote to primary when a file proves load-bearing.

---

## How agents should use `tier`

- **brain-query** — when matching multiple files, primary tier outranks secondary at equal relevance
- **graphify** — primary tier renders as larger nodes in the visual map
- **brain-lint** — flags any note without a tier field
- **agents** — when loading client context, always include the client's primary project note + Context/Core Framework.md + any explicitly cited primary files. Never load all secondary files unless a query routes there.

---

## Backfill — 2026-05-18

A backfill script ran on 2026-05-18 to add `tier` to every Brain note that lacked it. Files were classified by folder per the rules above. Manual promotions can happen any time — just edit the file.

Script: `~/launchpad-automation/scripts/brain-tier-backfill.py`
