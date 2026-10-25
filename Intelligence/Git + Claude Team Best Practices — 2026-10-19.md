---
title: Git + Claude Team Best Practices for Agency Project Work
type: research
status: active
tier: synthesis
tags: [brain, claude-team, git, knowledge-base, process]
last_updated: 2026-10-19
related: ["[[Client Note Schema]]", "[[Claude Team Setup Guide]]", "[[Project Instructions by Role]]", "[[Brain Standards]]", "[[Intelligence/00-INDEX]]"]
---

# Git + Claude Team Best Practices for Agency Project Work (research, 2026-10-19)

Question from Anthony: are we filing the git Brain and the Claude Team accounts the right way for a
marketing agency, and how do we get the most out of them? Web research, checked against what is built.

## Verdict

The structure we have matches the strongest pattern in the field: an LLM-maintained wiki with
immutable raw sources, an index, a log and a schema file (Karpathy's "LLM wiki"), fed by capture-only
contributors and curated by one filer. Four things should change, all small: per-client Claude projects
for the heavy clients, a confidentiality line in the base instructions, a weekly lint pass, and keeping
the team out of git entirely.

## What the field says, and where we stand

**1. One Project per client, not one giant project.** Every agency source agrees: a dedicated Project per
brand holding voice guide (with a banned-words list), audience, competitors, goals; a single "Marketing"
project produces generic output. Our role-based projects attach the whole Brain. Fix: for each person's
5 to 8 active clients, a per-client project built from the **same GitHub repo with file selection**
(only `Projects/{Client}.md`, `Context/`, and that role's `Skills/` notes). Small, fresh, synced. The
role project stays for cross-client work.

**2. Small, current knowledge beats big knowledge.** Projects hold about 200k tokens in context; past
that Claude switches to RAG mode (search, up to 10x capacity) and one user report shows it switching at
13 files. In RAG mode a fact is used only if retrieval finds it. Implication: per-client projects with a
handful of notes get everything loaded; a whole-Brain project gets searched. Both are useful; know which
one you are in (the UI shows a RAG indicator).

**3. Project instructions: general role and rules only.** Anthropic's guidance via third parties: keep
instructions to context, key guidelines, Claude's role; put task detail in the chat so the context budget
goes to knowledge. Ours fit. Agency sources add one rule we lacked: make Claude **confirm which client it is
working on before reading or writing**, and treat every client's material as confidential to that client.
Added to the base instructions 2026-10-19.

**4. Memory is personal and project-scoped; it is not a shared brain.** On Team, each project has its own
memory, teammates never see each other's, and admins only get an on/off switch. So the only shared memory
is the Brain, and the only way a person's learning reaches it is a capture step. That confirms the daily-dump
→ nightly filing design. Also confirmed by test 2026-10-19: a scheduled task cannot search past chats but
can compile from memory.

**5. Git is the barrier for non-developers, so remove it from their path.** Docs-as-code teams that put
non-engineers on git either added a visual editor over the repo or found that "nobody outside the team
could read the docs." Obsidian-git groups report constant merge conflicts. Our answer already matches the
recommended shape: the team reads (Claude project knowledge, Obsidian clone as the rendered layer) and
captures (daily dump to Drive); only the Mini commits. Keep `_inbox/` optional. Never ask the team to
resolve a merge.

**6. The LLM-wiki pattern has four operations: ingest, compile, query, lint.** We have ingest (Raw/,
brain-ingest), compile (brain-compile, nightly filing), query (brain-query, graphify). We lack a regular
**lint**: broken links, notes missing schema sections, `last_updated` older than 90 days on an active
client, contradictions between a client note and a playbook. `brain-link-density.py` covers links only.
Proposed: a Sunday lint that writes a short report to `Intelligence/` and queues fixes.

**7. Capture vs curate is the organizing principle.** Several writers of this pattern describe the same
split: contributors never edit the wiki directly; they drop sources; the LLM compiles. Anthony's instinct
("let each account commit and have its AI file correctly") is the one thing to resist: four filers with
no shared state produce duplicates and conflicts. One filer, one rulebook (Step 6.6 + Client Note Schema).

## Recommended changes (priority order)

1. **Per-client projects for heavy clients** via repo file selection. Recipe in [[Project Instructions by Role]].
2. **Confidentiality + client-confirmation rule** in the base instructions. Done 2026-10-19.
3. **Weekly Brain lint** (schema sections, stale notes, orphans, contradictions). To build; proposal queued.
4. **Team never touches git.** Read in Claude or Obsidian, capture by daily dump. `_inbox/` stays optional.
5. **Measure the loop.** Weekly Team Pulse reports dumps received, lines filed, Brain gaps fixed. If dumps per
   person per week drop below 3, the capture step is failing and the fix is on our side, not theirs.

## Sources

- https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
- https://www.spotdev.co.uk/blog/claude-projects-team-knowledge
- https://www.coderhouse.com/en/articles/how-to-use-claude-projects-for-teams
- https://limelightmarketing.com/claude-for-marketing-teams/
- https://www.getpassionfruit.com/blog/claude-projects-for-marketing-teams
- https://xponent21.com/insights/claude-for-marketers-when-to-use-chat-projects-cowork-or-code/
- https://www.anthropic.com/news/memory
- https://denser.ai/blog/llm-wiki-karpathy-knowledge-base/
- https://angelo-lima.fr/en/karpathy-second-brain-obsidian-claude-en/
- https://engineering.grab.com/facilitating-docs-as-code-with-markdown
- https://dev.to/mrbantsevich/we-moved-all-our-docs-into-git-then-nobody-outside-the-team-could-read-them-663
- https://forum.obsidian.md/t/team-colaboration/69608
