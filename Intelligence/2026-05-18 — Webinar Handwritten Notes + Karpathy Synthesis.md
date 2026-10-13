---
title: "Webinar Handwritten Notes + Karpathy Synthesis"
type: intelligence
status: active
tier: primary
tags: [ai-systems, brain, webinar, stanley-chen, karpathy, token-efficiency]
last_updated: 2026-05-18
related: ["[[2026-05-18 — attn-seeker Build Your AI Brain — Comparison + Adds]]", "[[Brain Standards]]", "[[CLAUDE]]", "[[Intelligence/00-INDEX]]"]
sources: ["Anthony's live notes during Stanley Chen webinar 2026-05-14", "Andrej Karpathy second-brain articles 2026-05-18"]
---

# Webinar Handwritten Notes + Karpathy Synthesis

Captured 2026-05-18 from Anthony's live note-taking during the Stanley Chen "Build Your AI Brain" webinar (2026-05-14) plus the Karpathy second-brain articles he sent.

These are the **operational lessons** — pair with the architectural comparison in [[2026-05-18 — attn-seeker Build Your AI Brain — Comparison + Adds]].

---

## Anthony's webinar Q&A capture

**Question Anthony asked Stanley:**
> "When you are feeding the brain with context using all the methods of communication, is there a way to do it so that it is not burning unnecessary tokens? Like how do you keep the brain dumps efficient as you scale?"

**Stanley's answer (verbatim from notes):**
> *"Only load what's relevant, summarise what's old, and cache what repeats. Also use md files instead of text files — that saves a LOT of tokens."*

This is the single most important operational rule we got from the webinar. It maps to three patterns we need to enforce:

| Pattern | What it means | How we implement |
|---|---|---|
| **Only load what's relevant** | Don't read whole folders. Use the graph / index first. | Already done — brain-query + graphify + tier ranking |
| **Summarise what's old** | After ~30/60/90 days, dated content should collapse into a synthesis | **NOT YET BUILT** — need a "summarize stale daily notes" automation |
| **Cache what repeats** | Same query asked twice = pull from cache, not re-synthesize | **NOT YET BUILT** — brain-query files back useful answers, but no explicit cache layer |
| **MD files not text** | Markdown is leaner and structured | Already done — entire Brain is .md |

---

## Other live capture from Anthony's notes

> "looks like im missing n8n right now"

→ Filed as gap. Already addressed today: n8n Cloud account set up, first workflow imported (01-ghl-hot-lead-to-slack). See [[2026-05-18 — attn-seeker Build Your AI Brain — Comparison + Adds]].

> "fireflies for conversation capture on zoom calls but keep notion for keeping transitions"

→ Workflow direction: **Fireflies = capture layer, Notion = handoff layer, Brain = knowledge layer**. Worth formalizing this in the [[Brain Standards]] ingestion workflow section.

> "make sure all content going into brain is md files so that we keep tokens as low as possible"

→ Already a rule. Reinforced.

---

## Karpathy's second-brain pattern (synthesis)

**Core quote:**
> *"Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase."*

That single line reframes the whole system. Humans don't manually edit the wiki — the LLM does. Humans direct the LLM, review the output, and maintain the source schema.

### What Karpathy actually does

| Element | What he uses | Maps to our build |
|---|---|---|
| **3-zone folder structure** | `sources/` (immutable) + `inbox/` (fleeting) + `wiki/` (LLM-synthesized) | Maps to our **Sources / Curated / Synthesis** zones — now formalized in [[Brain Standards]] |
| **CLAUDE.md as governance schema** | The `CLAUDE.md` at vault root instructs Claude how to maintain the wiki | We have this — `Brain/CLAUDE.md` |
| **`/ingest-url`** | Pulls a URL, summarizes, files into wiki, touches 5-15 related pages | We don't have this — **build this skill next** |
| **`/process-inbox`** | Classifies fleeting captures and files them | Partial — `brain-ingest` does this for Slack DMs; doesn't sweep inbox folder yet |
| **`/lint-wiki`** | Health checks: broken links, orphans, contradictions, gaps | We have `brain-lint` skill — verify it does all four checks |
| **Sources are immutable** | Raw captures never edited — append-only | Now codified in [[Brain Standards]] section 2 |
| **Compounding knowledge** | Each new source forces new connections that humans wouldn't manually find | This is the goal of the linking density work today |

### Where Karpathy went lighter than us

- He uses one general LLM (Claude/whatever) — we have 9 specialized agents
- He doesn't have a Brand Compliance gate
- He doesn't have per-client granularity (single `sources/` folder; we have one note per client)
- He uses "hacky Python scripts" — we have a more formalized skills + MCP architecture

### Where Karpathy goes deeper than us (worth borrowing)

- **Strict immutability of sources** — we treat this loosely; now codified
- **`/ingest-url` for web articles** — we have manual capture only; build this
- **Active deduplication** — Karpathy notes the LLM has to "reconcile duplicates again and again" because his system doesn't dedupe at ingest. Ours doesn't either. Worth adding a dedup check to brain-ingest.

---

## Action items from this capture

1. ✅ Codify zone model (Sources/Curated/Synthesis) in [[Brain Standards]] — done today
2. ✅ Configure Obsidian Graph View color groups — done today
3. 🟡 **NEW: Build `/ingest-url` skill** — pull web article, summarize, file into Intelligence/, link related notes
4. 🟡 **NEW: Build stale-content summarizer** — sweep old Daily/ and Intelligence/ entries; produce monthly synthesis notes
5. 🟡 **NEW: Add dedup check to `brain-ingest`** — before filing, check if similar note already exists
6. 🟡 **NEW: Verify `brain-lint` covers all 4 Karpathy checks** — broken links / orphans / contradictions / research gaps

Carry these into the next Brain hardening session.

---

## The big takeaway

Both Stanley and Karpathy converge on the same insight from different angles:

**The Brain's value is not the file count. It's the linking density × the routing efficiency × the synthesis quality.**

- Stanley: graph routing = 466× fewer tokens
- Karpathy: every new source creates connections you wouldn't manually find
- Us today: 237 notes, 13 orphans (5.5%), most `related: []` fields empty

We have the scaffolding. The next phase is **density** — make every note pull its weight in the graph.
