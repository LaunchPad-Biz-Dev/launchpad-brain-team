---
title: Brain Master Index
type: infrastructure
status: active
tier: primary
last_updated: 2026-05-18
related: ["[[CLAUDE]]", "[[Brain Standards]]", "[[Frontmatter Spec]]"]
---

# LaunchPad Brain — Master Index

The master catalog of everything in the Brain. This file is the AI's entry point when running queries, ingests, or compiles. Folder MOCs are auto-maintained by `brain-link-density.py`; manually update this file when adding new folders.

**Total folders:** 14 · **Total files:** 239 · **Last audit:** 2026-05-18
**Graph:** 5,300 nodes · 5,043 edges · 374 communities · **0 orphans**

See [[CLAUDE]] for navigation rules, [[Brain Standards]] for the full rulebook, [[Frontmatter Spec]] for note schema.

---

## Folder MOCs (Maps of Content)

🟦 **Curated zone** — human-owned truth:
- [[Projects/00-INDEX]] — Active and archived client projects (47)
- [[Context/00-INDEX]] — Core framework, brand guidelines, company context (12)
- [[Anthony/00-INDEX]] — Personal brand + strategic vision (4)
- [[Teams/00-INDEX]] — Team member profiles and roles (16)
- [[Departments/00-INDEX]] — Department-level context and operating cadence (6)
- [[Onboarding/00-INDEX]] — Client and employee onboarding processes (4)

🟥 **Sources zone** — immutable raw material:
- [[Raw/00-INDEX]] — Transcripts, articles, exports, screenshots
- [[Daily/00-INDEX]] — Dated daily logs (34)
- [[Resources/00-INDEX]] — Templates and reusable assets (3)
- [[Strategic Partners/00-INDEX]] — External partner reference data (1)

🟪 **Synthesis zone** — LLM-generated:
- [[Intelligence/00-INDEX]] — Research, trend briefs, strategy extracts (71)
- [[Skills/00-INDEX]] — Skill definitions and playbooks (25)
- [[Tasks/00-INDEX]] — Transient task plans (2)
- [[Tasks/00-INDEX]] — Active tasks and backlog (Notion is source of truth)

---

## Top-Level Files

- [[CLAUDE]] — Master instructions for AI operating the Brain
- [[Sales Playbook]] — Core sales process and scripts
- [[log]] — Chronological changelog of ingests and updates

---

## Raw Layer

- [[Raw/README]] — Rules for the immutable source layer
  - `articles/` — Web clips and research
  - `transcripts/` — Meeting and call transcripts
  - `clips/` — Reference social posts and designs
  - `screenshots/` — Visual references
  - `exports/` — ChatGPT/Notion/bulk data exports

---

## How to Use This Index

**For AI agents:**
1. Start here when answering queries against the Brain
2. Use folder MOCs to narrow scope before reading individual notes
3. Update this index whenever a new note is added via `/brain-ingest`

**For humans:**
- Skim folder MOCs to find what exists
- Use the graph view in Obsidian to see emergent connections
- Run `/brain-lint` periodically to catch stale entries

---

## Recent Additions

- 2026-09-07 — Compiled 1 source, created 1 note ([[Projects/Real Estate Content Creation Retreat]]), updated 0
- 2026-09-09 — Compiled 1 source, created 1 note ([[Projects/First Colony Mortgage]]), 1 source left pending (empty DRG merchandise stub, flagged for Notion follow-up)

*This section is append-only and maintained by `/brain-ingest`. See [[log]] for the full chronological record.*

- 2026-04-13 — Added Raw layer, master index, and folder MOCs (Karpathy LLM wiki pattern)
- 2026-09-01 — Compiled 1 source (CES Inc. website/social discovery meeting), created 1 note ([[Projects/CES Inc.]]), updated 1 note ([[Projects/Helix Electric]])
- 2026-08-17 — Compiled 7 sources (LP University launch meetings x4, Launchpad content planning, DRG monthly + merchandise), created 1 note, updated 6 notes
- 2026-08-26 — Compiled 1 source (AI security platform demo & DRG referral), created 1 note, updated 2 notes
