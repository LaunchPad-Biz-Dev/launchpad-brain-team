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
7. Paste this as the project's instructions:

> You are working with the Launchpad Business Development team (Las Vegas marketing agency). Before answering anything about a client, read that client's note in `Projects/`. Follow `Context/Launchpad Brand Guidelines.md` for voice. Never invent client facts: if a note doesn't say it, say you don't know. Keep captions human, short, no dashes, no buzzwords.

Start every client conversation inside this project.

## 3. Keep it fresh

The Brain changes daily. Once a week, or before a big piece of work, open the project,
click the repo under Project knowledge, and hit **Sync now**.

## 4. Adding knowledge to the Brain

You cannot edit the Brain copy. That's on purpose. When you learn something worth keeping
(a client preference, a correction, a decision), tell Apollo in Slack: **"chat clip that"**
or DM Apollo the note. It goes into the real Brain and shows up in your copy on the next sync.

## 5. Optional: browse the Brain in Obsidian (recommended for Cynthia, Kyle, Amber)

Obsidian is the app Anthony uses to read and navigate the Brain. The copy you get opens the
same way: folder colors, graph view, backlinks, and `index.md` as the front door.

1. Install GitHub Desktop (desktop.github.com), sign in, **File → Clone repository → LaunchPad-Biz-Dev/launchpad-brain-team**. Pick `~/Launchpad Brain` as the location.
2. Install Obsidian (obsidian.md). **Open folder as vault** → choose `~/Launchpad Brain` (the cloned folder itself). Trust the vault when asked (it only enables the built-in plugins).
3. Start at `index.md`, then the `00-INDEX.md` in any folder. `Projects/` has one note per client.
4. To refresh: GitHub Desktop → **Fetch origin** → **Pull**. Do it before you start work. You cannot push; that's by design. Anything you type in Obsidian is overwritten on the next pull, so put notes in Claude and "chat clip" them to Apollo instead.
5. Same folder works in the Claude desktop app's **Cowork** if you produce files (briefs, captions, docs).

## 6. Fridays: run your weekly dump (5 min)

Before you log off Friday, open Claude and say **"run my weekly dump"**. Claude looks back at
your week, asks four quick questions, writes a one-page recap, and saves it to
**Google Drive → LaunchPad → Launchpad Team Work → your name**. First time only, turn on the
Google Drive connector (**Customize → Connectors → Google Drive → Connect**).

It is not a report card. Blockers, time sinks, and "Claude got this wrong" are the most useful
lines. Apollo reads every dump Monday, fixes the Brain, and flags blockers to Anthony.

## Rules

- Private and internal. Never paste Brain content into other AI tools or share outside Launchpad.
- Client facts come from the client's note. If it's not there, ask Anthony or Abril, don't guess.
- Final content still goes through the normal approval flow. Claude drafts, humans approve.

Related: [[New Employee Onboarding]], [[Brain Standards]], [[Prompting Playbook]], [[Launchpad Brand Guidelines]]
