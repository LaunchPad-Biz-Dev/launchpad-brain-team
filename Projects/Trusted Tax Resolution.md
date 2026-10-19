---
title: "Trusted Tax Resolution"
type: project
status: onboarding
tier: primary
tags: [client, ttr, tax-resolution]
last_updated: 2026-05-28
related: ["[[Projects/00-INDEX]]", "[[Daily/2026-05-28]]", "[[Toro Taxes (TTFS)]]"]
---

# Trusted Tax Resolution (TTR)

## Status
**Onboarding** — CRM build in progress, SMM setup partially complete

## Industry
Tax Services — IRS Tax Resolution / Tax Debt Relief

## Internal Slug / IDs
- GHL Location ID: `Ihl99KFupDC8nXXeqM90`
- GHL MCP server: `gohighlevel-ttr`
- Approver (pending ID resolution): Sara Martinez

## Service Area
TBD

## Contact Info
- Primary contact: TBD (CRM demo team: includes "T" and Claudia, plus Anthony's team — see [[Daily/2026-05-28]] CRM Setup Demo)

## Service Offering (per CRM build)
IRS tax resolution / tax debt relief. Customer journey:
1. New Lead → form submission via website
2. Consultation Scheduled (client self-schedules via calendar link, with team follow-up option)
3. Consultation Completed → notifications fire
4. Resolution Strategy → case review document drafted, sent to client for signature
5. Case Review Completed → client signs, process moves forward
6. Payment & Retainer → invoice sent (manual initially)
7. IRS Negotiation (manual stage w/ automated notifications)
8. Active Resolution (no notifications)
9. Case Resolved → final notifications + review link

## Services Provided by Launchpad
1. **CRM build** in GHL (in progress)
2. **Social Media Management** (in progress — blocked, see below)
3. **Document automation** — pending AI agent capability research

---

## Setup Status (2026-05-28)

### Resolved
- ✅ TTR social accounts now connected to GHL (Abril, 2026-05-28 15:06 PDT)
- ✅ TTR shared Google Drive established: https://drive.google.com/drive/folders/0AMuf75NQ6-V6Uk9PVA

### Still Open
- ⚠️ `mcp__gohighlevel-ttr__*` not in `.claude/settings.json` allowlist — Anthony to add
- ⚠️ Sara Martinez approver ID not resolvable via GHL Users API — needs manual lookup or scope fix
- ⚠️ CRM templates needed: case review template + invoice/pricing template (action items on client side from 2026-05-28 demo)
- ⚠️ AI agent capability for document organization from emails — team to research before next meeting

---

## Chat Clips

### Chat Clip — 2026-05-28
**Source:** #ai-team-updates — [[Abril Rodriguez]]
**Category:** CLIENT_INTEL / PROCESS_UPDATE

Apollo flagged 3 blockers for the TTR Social Media Poster run: (1) `mcp__gohighlevel-ttr__*` missing from `.claude/settings.json`, (2) no TTR shared Drive, (3) no FB/IG connected in GHL Social Planner. Abril confirmed she resolved 2 of the 3: TTR social accounts are now connected to GHL, and the shared Drive is live at https://drive.google.com/drive/folders/0AMuf75NQ6-V6Uk9PVA. Only the settings.json allowlist line remains for [[Anthony Mendoza]] to add before the SMM run can complete.

**Key Points:**
- TTR social accounts connected in GHL Social Planner (FB/IG presumably)
- TTR shared Drive live — graphics now have a home
- Remaining blocker: settings.json allowlist for `mcp__gohighlevel-ttr__*`
- Once Anthony adds the allowlist line, Apollo can re-trigger and complete TTR June posts (revised graphics already exist at `marketing/output/social-posts/ttr-revisions-2026-05-28/`)

**Clipped by:** [[Abril Rodriguez]]
**Slack permalink:** https://launchpad-co81707.slack.com/archives/C0AQVLBT9PY/p1780006012366949

---

## Related Notes
- [[Daily/2026-05-28]] — full setup blocker context
- [[Toro Taxes (TTFS)]] — separate Toro/Toro Taxes franchise project (distinct client)
- [[AI Marketing Team — Build Plan]] — Apollo / SMM agent context

<!-- Sections below added 2026-10-19 per [[Client Note Schema]]; the nightly filing writes here. Dated, append-only. -->

## Preferences & Corrections

## Decisions

## Activity Log

## Open Items
