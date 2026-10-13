---
title: "Second Brain That Compounds — Karpathy / Obsidian / Claude"
type: intelligence
status: active
tier: secondary
tags: []
last_updated: 2026-04-13
related: ["[[Intelligence/00-INDEX]]"]
---

# Second Brain That Compounds — Karpathy / Obsidian / Claude
*Flagged by Anthony — 2026-04-11 | Source: https://fabswill.com/blog/building-a-second-brain-that-compounds-karpathy-obsidian-claude/*

## Main Thesis
LLMs should **compile and maintain personal knowledge bases automatically** — not just answer questions. Every new source added compounds the value of everything already in the system through automatic cross-linking.

This is Andrej Karpathy's core insight applied as a workflow: your knowledge base should grow stronger over time, not just larger.

## The Five Core Functions
1. **Compile** — raw sources (transcripts, articles, notes) → structured articles
2. **Cross-link** — auto-connect related concepts via backlinks
3. **Index** — all content made searchable
4. **Lint** — health-check for gaps, inconsistencies, orphaned notes
5. **Answer** — query the full accumulated knowledge base

## The Superpower: Cross-Links Over Content
The author's key insight: individual articles matter less than their **interconnections**. An article on "Capability Overhang" automatically linking to "Token Budget Optimization" reveals relationships you'd never notice manually. The graph IS the intelligence.

## The Author's Implementation (Claude Code Skills)
- `/ingest-transcript` — captures YouTube transcripts with metadata
- `/wiki-compile` — extracts concepts, creates cross-linked wiki articles from raw input
- `/wiki-lint` — health-checks the knowledge base, flags gaps
- `wiki_search.py` — full-text search via SQLite

**Result:** 5 sources → 21 cross-linked articles in hours (vs. days manual).

## What This Means for the LaunchPad Brain

### What We Already Have Right
- Obsidian as the vault ✅
- `[[wiki links]]` syntax throughout Brain notes ✅
- Intelligence folder for dated captures ✅
- Apollo agents feeding it continuously ✅

### What We Could Add
1. **Auto-compile pipeline** — every new article/research drop Anthony sends → Claude processes it into a structured Brain note automatically (not just saved as raw text)
2. **Cross-link on write** — when saving any new note, scan existing Brain notes and add `[[links]]` to related concepts (we do this manually now, could be automated)
3. **Lint pass** — periodic audit of Brain notes for orphaned pages, missing links, stale context
4. **Ingest skill for video/transcript** — when Anthony drops a YouTube link or podcast, auto-transcribe and compile it into the Brain

### The Compound Effect
The Brain currently has 121 files. If every piece of content we create, every client insight, every trend brief, every meeting note gets auto-compiled with cross-links — by end of year the Brain becomes a strategic moat that's nearly impossible for competitors to replicate. This aligns directly with [[The Brain is the Moat]].

## Potential New Skill: `/brain-ingest`
A skill that:
1. Takes any URL or raw text
2. Extracts key concepts
3. Creates a structured Brain note
4. Auto-links to existing related notes
5. Updates the relevant index

This could be the `/brain-ingest` skill — the next evolution of the Brain Dump skill.

## Related Notes
- [[AI Marketing Team — Build Plan]]
- [[AI Systems — ChatGPT Extract]]
- [[AI Tools and Usage]]
