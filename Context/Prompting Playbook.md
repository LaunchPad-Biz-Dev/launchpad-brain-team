---
title: "Prompting Playbook — How We Prompt Apollo and Claude Code"
type: context
status: active
tier: primary
tags: [system, prompting, ai-os, layer-2, standard]
last_updated: 2026-08-28
related: ["[[AI-OS-Architecture]]", "[[Brain Standards]]", "[[Device Fleet]]", "[[Core Framework]]", "[[Context/00-INDEX]]"]
---

# Prompting Playbook

**Adopted 2026-08-28.** The prompt layer of the AI OS — how we ask the system for work.

The full playbook and the working commands live in the **repo**, not here. Prompts are Layer 2 (procedure), so per the layer rule they belong with the agents and skills. This note is the pointer plus the parts that are durable business knowledge.

| What | Where |
|---|---|
| The playbook | `~/launchpad-automation/PROMPTING.md` |
| The commands | `~/launchpad-automation/.claude/commands/` |
| Shareable page (team) | https://claude.ai/code/artifact/c2f70c6d-647f-4e78-bb56-74ad99a7c632 |

---

## Why it exists

Agents and skills were built out to seventeen and twenty-six respectively, but the layer between them and the person typing was never built. Every session re-typed its framing by hand, and the best prompts we had were one-off `*-NEXT-SESSION.md` files that worked once and were never reused.

The governing idea: **whatever the prompt leaves open is what comes back wrong.**

---

## The two modes — the load-bearing distinction

The single biggest split in how we prompt. A prompt written for one mode fails in the other.

| | **Attended** (Anthony at the keyboard) | **Unattended** (Mini · n8n · cron) |
|---|---|---|
| At ambiguity | **Ask.** A question costs thirty seconds. | **Interpret → flag → proceed →** escalate at the end. |
| Cost of a wrong guess | One correction | A whole bad run, discovered later |
| Blocked step | Stop and ask | Finish everything else, escalate at the end |

A prompt that stalls waiting for an answer nobody is there to give is a silent failure — the worst kind, because it looks like nothing happened. Every prompt should say which mode it is in. See [[Device Fleet]] — build on the laptop, run on the Mini.

---

## The seven parts of a strong prompt

1. **Role and decision boundary** — who it is, and where its authority stops
2. **Read these first, as paths** — naming the file prevents a vault crawl
3. **Decisions already made, with consequences** — a decision without its consequence gets silently reversed later
4. **Verbatim source, not a summary** — you cannot know in advance which detail the work depends on
5. **Constraints with the incident attached** — a rule with a date behind it survives; generic caution gets reasoned around
6. **Definition of done, and where it lands** — including what *partial* looks like
7. **Ambiguity policy** — see the two modes above

Reference example, and the doc this structure was reverse-engineered from: `GROWTH-AUDIT-FUNNEL-NEXT-SESSION.md`.

---

## The commands

| Command | Use it when |
|---|---|
| `/session-start` | Opening a session — state, handoff, orientation before work |
| `/handoff` | Closing a session — writes the NEXT-SESSION doc from real state |
| `/client-work` | Client delivery — context gate, reconcile, human gate, verify |
| `/apollo-run` | Authoring an unattended Mini or n8n prompt |
| `/new-component` | New agent or skill — interview first, template always |
| `/audit-component` | Pressure-testing something already built |
| `/sharpen` | Turning a rough prompt into one that works first try |

---

## Failure modes this encodes

Each was learned from a real incident, recorded so it is not re-learned:

- **Trusting memory as current state.** Agent memory holds learnings, never what exists right now. SMM run #2 trusted memory saying run #1 had posted the batch, created two posts, missed the rest. Always reconcile live.
- **Editing a GHL post without setting `status: in_review`.** Drops it to `in_progress`, which publishes live in seconds. Five CCS posts went live six weeks early on 2026-05-20.
- **Handing Anthony a draft instead of interviewing him.** *"When I rely solely on you I hit a block and don't really love the content I'm making."* (2026-08-19). A draft makes him an editor of someone else's work. For anything in his voice: interview, don't draft.
- **Softening what has not been tested.** "Built" and "has never once fired" are different facts. The Growth Audit read as complete for months while its central hook had never been observed by the system.
- **Starting a session cold.** Opening with the task instead of the state. The AI reconstructs context by guessing.

---

## Maintaining it

When a prompt produces a bad run, the fix goes in the prompt — not in someone's memory of it. If the lesson is durable, push it down a layer: into the agent spec, or into the relevant command, so it applies without anyone remembering to include it.

Same compounding pattern the Brain uses. Prompts are where it starts.

---

## Update log

- **2026-08-28** — Created. Seven commands committed to `launchpad-automation` (`4af85e1`). First live test: `/session-start growth-audit` caught that the Saturday event deadline in the Growth Audit handoff had gone stale — written "four days out" on 08-25, actually one day out on 08-28.
