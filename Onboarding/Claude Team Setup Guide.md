---
title: Claude Team Setup Guide
type: onboarding
created: 2026-10-13
last_updated: 2026-10-19
tier: curated
tags: [onboarding, claude, tools, brain]
related: ["[[Onboarding/00-INDEX]]"]
---

# Claude Team Setup Guide

Launchpad runs on Claude. This replaces ChatGPT for all client work so our voice, facts, and
client context stay consistent. Set-up takes about 10 minutes. No terminal, no VS Code.

## 1. Accept your invite

1. Check your Launchpad email for the Claude Team invite from Anthony.
2. Sign in at claude.ai with your Launchpad Google account.
3. Download the Claude desktop app: https://claude.ai/download (Mac). Sign in with the same account.

## 2. Connect the Brain (the knowledge base)

The Brain is Launchpad's shared memory: every client's context, brand guidelines, packages,
processes. Connecting it means Claude answers with *our* facts, not generic ones.

1. Create a free GitHub account if you don't have one (github.com), using your Launchpad email.
2. Accept the invite to the **LaunchPad Biz Dev** GitHub organization (email from GitHub, sent 2026-10-19). That gives you read access to **LaunchPad-Biz-Dev/launchpad-brain-team**.
3. In Claude: **Customize → Connectors → GitHub Integration → Connect**. Approve the Claude app on GitHub and grant it the **launchpad-brain-team** repo.
4. In Claude: **Projects → New project**. Name it **Launchpad Brain**. Keep it private (GitHub sync only works on private projects).
5. In the project, under **Project knowledge**, click **+ → GitHub**. Pick **LaunchPad-Biz-Dev / launchpad-brain-team**.
6. Select these folders to start: `Context`, `Projects`, `Departments`, `Resources`, `Skills`. Add `Intelligence` later if you want trends and research too. Click **Add files**.
7. Paste this as the project's instructions (this is what teaches Claude to use the Brain):

> You are Claude working with the Launchpad Business Development team (Las Vegas marketing agency: Launchpad Business Development, Launchpad Productions, BrandWithUs). The project knowledge is a read-only copy of the Launchpad Brain, our shared memory. Treat it as the source of truth about us and our clients.
>
> **How to navigate it.** `index.md` is the map. Every folder has a `00-INDEX.md`. `Projects/` has one note per client: read `Projects/{Client}.md` in full before any client work, every time. `Context/Launchpad Brand Guidelines.md` sets voice for anything we publish. `Skills/` holds our playbooks (briefs, shot lists, captions, posting workflow, sales scripts): when asked to do a type of task, find and follow the matching playbook. `Departments/` has SOPs. `Intelligence/` has research and trend briefs.
>
> **Honesty.** Never invent a client fact, price, name, date or result. If the Brain does not say it, say "the Brain doesn't have this" and ask. Cite the note you used.
>
> **Remembering.** You cannot write to the Brain directly. The user's scheduled daily dump carries today's work to Apollo automatically. So when you notice something worth keeping (a client preference, a correction, a decision, a Brain note that is wrong or missing), say so in one line so it is in today's conversation for the dump to pick up: "Noting for the Brain: {client} — {fact}". If the user says "chat clip that", do the same, in 2 to 5 lines, naming the note it belongs in.
>
> **Freshness.** If a client note looks older than the user's question, remind them to hit Sync now on the project knowledge.
>
> **Output.** Captions and copy sound human: short, specific, no dashes, no buzzwords, no AI tells. Final content still goes through our normal approval flow.

Start every client conversation inside this project. Then add the block for your job from [[Project Instructions by Role]] under it, so Claude starts from your lane (social, ads, production, ops).

## 3. Keep it fresh

The Brain changes daily. Once a week, or before a big piece of work, open the project,
click the repo under Project knowledge, and hit **Sync now**.

## 4. How the Brain gets smarter: your daily dump (set up once, 3 minutes)

You cannot edit the Brain copy. That's on purpose. Instead, your Claude account files your day for
you, every day, with no effort after setup:

1. In the Claude desktop app, open **Cowork**, then **Scheduled tasks**, then **New task**.
2. Name: `Daily dump`. Prompt: `Run my daily dump.` Frequency: **weekdays at 4:30 PM**. Approval: off.
   Connectors: make sure **Google Drive** is connected (Customize → Connectors → Google Drive).
3. Save. That's it.

What happens next, every weekday:

- **4:30 PM** your Claude looks at today's chats and writes a one-page recap (clients touched,
  what shipped, decisions, what the Brain got wrong) to Drive → Launchpad Team Work → your name → Daily.
- **5:30 PM** the Mac Mini pulls every teammate's recap into the real Brain.
- **5:47 PM** Apollo files each one into the right client notes, playbooks and brand guidelines, fixing
  anything the Brain had wrong. Think of it as the Brain's dreaming session: the day's memories get sorted.
- **9:30 PM** the updated Brain is pushed to your copy. Tomorrow, everyone's Claude knows what you learned.

Run it by hand any time with **"run my daily dump"**. The Friday **"run my weekly dump"** still exists
for the bigger weekly picture (blockers, time sinks, next week's top 3).

## 5. Optional: browse the Brain in Obsidian (recommended for Cynthia, Kyle, Amber)

Obsidian is the app Anthony uses to read and navigate the Brain. The copy you get opens the
same way: folder colors, graph view, backlinks, and `index.md` as the front door.

1. Install GitHub Desktop (desktop.github.com), sign in, **File → Clone repository → LaunchPad-Biz-Dev/launchpad-brain-team**. Pick `~/Launchpad Brain` as the location.
2. Install Obsidian (obsidian.md). **Open folder as vault** → choose `~/Launchpad Brain` (the cloned folder itself). Trust the vault when asked (it only enables the built-in plugins).
3. Start at `index.md`, then the `00-INDEX.md` in any folder. `Projects/` has one note per client.
4. To refresh: GitHub Desktop → **Fetch origin** → **Pull**. Do it before you start work. You cannot push; that's by design. Anything you type in Obsidian is overwritten on the next pull, so put notes in Claude and "chat clip" them to Apollo instead.
5. Same folder works in the Claude desktop app's **Cowork** if you produce files (briefs, captions, docs).

## 6. Fridays: weekly dump (5 min, optional if your daily dump runs)

Friday before you log off, say **"run my weekly dump"**. Claude asks four quick questions and saves
a one-page week recap next to your daily dumps. Blockers, time sinks, and "Claude got this wrong" are
the most useful lines. It is not a report card; it is how the Brain and the playbooks get fixed.

## Rules

- Private and internal. Never paste Brain content into other AI tools or share outside Launchpad.
- Client facts come from the client's note. If it's not there, ask Anthony or Abril, don't guess.
- Final content still goes through the normal approval flow. Claude drafts, humans approve.

Related: [[New Employee Onboarding]], [[Brain Standards]], [[Prompting Playbook]], [[Launchpad Brand Guidelines]]
