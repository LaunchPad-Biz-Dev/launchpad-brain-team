---
date: 2026-06-10
client: Arby's Food Truck (DRG — Diversified Restaurant Group)
type: Client Intel — IT/Governance Request
related: ["[[Intelligence/00-INDEX]]"]
---

# DRG — Garret Walti IT / Security Governance Request

**Who:** Garret Walti, IT/Security Head at DRG (parent company of Arby's Food Truck catering operation)
**Email thread:** Garret → Haley, Anthony, Sierra, Kelly, Alexa (May 21, 2026)
**Original request date:** Thu May 21, 2026 3:36 PM

## What Garret Asked For

Garret wants a walkthrough of the GHL CRM platform (Arby's Food Truck sub-account) from an IT/security and governance perspective before it scales further within the DRG organization. His stated areas:

1. What data will reside within the platform
2. How data is entering / leaving the system
3. Integration points with other platforms/systems
4. Access controls, SSO/MFA support, and user governance
5. Reporting/export capabilities and external visibility
6. Audit logging, compliance
7. Long-term operations and support as it scales within the organization

Meeting slots offered: Tuesday May 26 or Friday May 29 (via scheduling assistant or his booking link).

## Brief Already Prepared

Full IT/security briefing document created 2026-06-10:
`marketing/output/sales-guides/drg-garret-crm-it-governance-brief-2026-06-10.md`

Covers all 7 areas, cites official GHL help docs, includes:
- Quick-reference cheat sheet (1-page answers for every question)
- Honest-gap summary with mitigations pre-framed (no SAML, no blanket MFA enforcement, 60d audit retention, API token egress outside UI permissions)
- Meeting strategy: lead with SOC 2 Type II, volunteer the gaps before he finds them

## Key Facts to Know Going In

- **SOC 2 Type II certified Feb 2026** — offer report under NDA (Trust Center)
- **OIDC SSO yes / SAML no** — use OIDC app on their IdP (Okta/Entra)
- **No blanket login-MFA enforcement** on standard plan → mitigate via IdP/SSO layer or policy
- **Audit logs: 60-day rolling retention** — export regularly
- **DRG owns its data, full CSV/API portability**
- This sub-account can be migrated to a DRG-owned GHL agency if they ever part ways with Launchpad

## Follow-Ups to Commit in the Meeting

- [ ] Document Launchpad's internal access list for DRG (who at LP sees the sub-account)
- [ ] Request HL SOC 2 Type II report under NDA
- [ ] Confirm bulk-export limits + login-event auditing + uptime SLA in writing from HighLevel

## Related

- [[Arby's Food Truck]] — parent project note
- [[GHL MCP capabilities]] — what the platform can/can't do
