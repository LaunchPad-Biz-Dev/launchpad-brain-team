---
title: "Client Onboarding Process — Abril Rodriguez Brain Dump"
type: process
status: active
tier: primary
tags: []
last_updated: 2026-04-09
related: ["[[Onboarding/00-INDEX]]"]
---

# Client Onboarding Process — Abril Rodriguez Brain Dump

> **Scope:** Abril's specific tools, reference files, automation wishlist, and Phase 1C build decisions. This is the **implementation + automation roadmap**, not the canonical process.
>
> For the canonical execution SOP, see [[New Client Onboarding Process]].
> For the context extraction framework, see [[Client Onboarding Process]].

**Date:** 2026-04-07
**Source:** Abril Rodriguez (Creative Director), shared via Slack
**Type:** Process documentation + automation wishlist

---

## Overview

Abril shared her current client onboarding process, key Notion links, reference files, and a wishlist for automation improvements. This note captures everything for reference by the [[Client Onboarding Agent]] and future automation builds.

---

## Notion Links (Abril's Onboarding System)

| Resource | Link |
|---|---|
| Onboarding Form (goes to onboarding board) | https://launchpadbizdev.notion.site/1e4b01f77d6d80788952faf17e1221e9?pvs=105 |
| Branding Questionnaire | https://launchpadbizdev.notion.site/1c4b01f77d6d80d296f9d195ce531371 |
| CRM / Systems Onboarding | https://launchpadbizdev.notion.site/2c7b01f77d6d8039b80bd33571011e9f?pvs=105 |

---

## Reference Files (Stored in Slack)

These files were attached by Abril in Slack on 2026-04-07. Retrieve from Slack if needed for deeper automation build-out.

- **Onboarding walkthrough.srt** — Video transcript of Abril walking through the onboarding process
- **Client onboarding SOP.pdf** — Standard operating procedure document
- **OrganizeGoogleDriveFoldersforClients.pdf** — Google Drive folder structure and naming conventions
- **Discovery questions.pdf** — Questions used during discovery meetings
- **Onboarding checklist.pdf** — Step-by-step checklist for completing onboarding

---

## Abril's Automation Wishlist

These are the automations Abril wants built to streamline client onboarding. Priority order as she listed them:

### 1. Proposal-to-Payment Automation
- Automate the flow from proposal sent through payment received
- [[Emigen Lagman]] follows up with the client until they pay
- Goal: eliminate manual follow-up on outstanding proposals

### 2. Contract Signed + Paid Notification
- Get notified automatically when a contract is signed and payment is received
- Trigger: contract execution + payment confirmation

### 3. Auto-Add Client to Onboarding Board
- When a client is signed and paid, automatically add them to the Notion onboarding board
- Checklist should be auto-populated as subtasks (based on the onboarding checklist)
- No manual board setup needed

### 4. Auto-Create Client Portal and Shared Drive
- Automate the creation of the client portal (Notion) and shared Google Drive
- Alternative: have Emigen create them on command
- See [[New Client Onboarding Process]] Phase 1 for current manual steps

### 5. One-Button Onboarding Email
- A single button that sends the client onboarding welcome email
- Pre-populated with client name, portal link, drive link, form links
- See [[New Client Onboarding Process]] Welcome Email Template section

### 6. Emigen Schedules Meetings + Follows Up on Client To-Dos
- [[Emigen Lagman]] handles meeting scheduling for onboarding
- Emigen follows up with clients on outstanding to-dos (forms, questionnaires, asset delivery)
- Goal: remove Abril from the follow-up loop

---

## How This Connects to AI OS

These automation requests map directly to the [[Client Onboarding Agent]] capabilities being built in the AI OS. Key connections:

- **Wishlist items 3-5** can be handled by the Client Onboarding Agent's `client-context-builder`, `notion-sync`, and `drive-scanner` skills
- **Wishlist items 1, 2, 6** require GHL automation + Emigen AI assistant integration
- The Notion links above should be used as data sources for the onboarding agent

---

---

## Phase 1C Build — Confirmed Decisions (2026-04-09)

**Session:** Abril confirmed a 30-min live kickoff on 2026-04-09 for Phase 1C (Onboarding Board + Checklist automation).

| Decision | Confirmed Answer |
|---|---|
| Notion Board location | Use EXISTING "Onboard" database inside LP Client Dashboard — do NOT create new |
| Board URL | https://www.notion.so/launchpadbizdev/1d8b01f77d6d8073b734d97789ee96e9 |
| Current board schema | Bare (Name, Tags, Created only) — needs full build-out |
| Automation trigger | **Signed AND paid** (not just signed) |
| Demo Loom | Include demo Loom video in onboarding email for clients |
| Accounting loop | Jenny (accounting) needs notification + training to mark as paid in GHL |
| Emigen role | Proposal → payment follow-up; creates portal + Drive; sends onboarding email |

**Build constraint:** All Notion changes must be made live with Abril — do not build independently. She needs to QC everything so nothing duplicates existing boards.

## Related Notes
- [[New Client Onboarding Process]] — Full onboarding SOP (phases, meetings, launch criteria)
- [[Client Onboarding Process]] — Context extraction and client snapshot framework
- [[Client Onboarding Workflow]] — Skill definition for AI onboarding agent
- [[CRM and GHL Workflow]] — GHL automation setup (relevant to wishlist items 1-2)
- [[Active Clients Overview]] — Where onboarded clients end up
