---
title: "AI Security Platform — Demo & Referral Partnership"
type: strategic-partner
status: exploring
tier: secondary
tags: [security, compliance, referral, partnership, product-demo]
last_updated: 2026-08-19
related: ["[[Strategic Partners/00-INDEX]]", "[[Launchpad Business Development]]", "[[Projects/DRG]]"]
---

# AI Security Platform — Demo & Referral Partnership

## Status
**Exploring.** Demo held 2026-08-19; no signed agreement. Two open bugs blocking Launchpad's own internal adoption; one referral lead (DRG) identified as first test case.

## Who
- Platform Team (incl. **David**) demoed their AI security/compliance/governance platform to Anthony Mendoza and the Launchpad team.
- Relationship shape mirrors [[Remine Capital — Healthcare Division Partnership]]: Launchpad's role is **internal user + referral partner**, not equity/reseller (no commission terms discussed yet — unlike Remine, no comp structure has been negotiated).

## What the platform does
- **Secrets management** — encrypted API keys/credentials/infra configs, key rotation with version history, vault-passphrase access (platform itself cannot see user secrets), split-passphrase org recovery.
- **AI Gateway** — routes AI traffic through provider keys (e.g. Anthropic), issues member tokens with spend/frequency/model limits, response caching (same question in a time window = free), full request/response audit logging with export to the client's own telemetry.
- **Audit & Telemetry** — dashboard on errors/latency/spend/top users/models, per-key access audit, idle-session auto-logout.
- **Developer integrations** — CLI, SDK, and an **MCP server** specifically for AI agent workflows; scoped Personal Access Tokens (can be read-only).

## Why this matters for Launchpad
Positioned as an affordable alternative to Palo Alto Networks — aimed at organizations where leadership has no visibility into who's consuming AI/data internally. Best fit: compliance-heavy verticals (healthcare, finance, legal). This is directly relevant to Launchpad's own AI OS (this repo) — the gateway/audit layer is the kind of governance Launchpad doesn't currently have over its own MCP/agent stack.

## Referral Opportunity — DRG
- **[[Projects/DRG|DRG (Diversified Restaurant Group)]]** identified as the primary referral candidate — owns the majority of Taco Bell/Arby's locations Launchpad already serves, and DRG previously asked about **SOC 2 compliance** when implementing GHL.
- Action item (open, owed by Anthony): reach out to DRG's contact (Garrett) to connect them with the platform team.
- See DRG's Sync Log for the cross-linked flag.

## Open Issues (blocking before Launchpad relies on this internally)
1. **Teams billing display bug** — Anthony's account shows "Upgrade to Teams" even though already on the Teams plan. Anthony owes the platform team screenshots.
2. **Wiki sharing bug** — a wiki built in Anthony's personal workspace (imported Obsidian markdown) is not accessible from the Teams workspace, blocking team-wide sharing.

## Action Items
- [ ] Anthony — reach out to DRG (Garrett) re: platform referral
- [ ] Anthony — send Teams billing bug screenshots to platform team
- [ ] Platform team — fix Teams billing display bug
- [ ] Platform team — fix personal/Teams wiki sharing

## Sync Log
- **2026-08-26** — Ingested from Notion meeting export (`Raw/exports/notion-meeting-2026-08-19_security-demo.md`, synced 2026-08-20). First entry for this partner.

---

*Source: [[Raw/exports/notion-meeting-2026-08-19_security-demo]]*
