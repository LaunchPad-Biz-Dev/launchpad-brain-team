---
title: "Outbound Launch Plan — Action List (2026-08-12)"
type: department
status: active
tier: primary
tags: [sales, outbound, launch-plan, emigen, action-list]
last_updated: 2026-08-12
related: ["[[Sales Department]]", "[[Ideal Client Profile]]", "[[AI Outbound Sales Team — Full Scope Handoff 2026-08-12]]", "[[Departments/00-INDEX]]"]
---

# Outbound Launch Plan — Action List

**Created:** 2026-08-12
**Goal:** first real cold contacts inside 14 days; sustained outbound running without Anthony's daily involvement.
**Owners:** Emigen (infrastructure, accounts, human safeguard) · Anthony (AI, agents, data layer)

---

## The operating model

Auto-send is ON for cold email from a dedicated outbound domain. Anthony is **not** an inline gate. Emigen is the safeguard — but *not* by reading every message, which would recreate the same bottleneck one person down.

### Emigen's safeguard role (~30–45 min/day)

| When | What she does |
|---|---|
| **Once, before launch** | Approve the 4 email templates + the audit report format. Re-approve only when a template changes. |
| **Before each batch's first run** | **Data-truth check** — pull 5 prospects from the batch, confirm the scraped claim is actually true (they really are running graphics-only, they really have 38 reviews). This is the critical gate: with auto-send on, a false claim goes out unread. |
| **Daily, 15 min** | Random audit of 5 sent messages. Log anything wrong. Three errors in a week = pause the batch and tell Anthony. |
| **Daily, 4:00 PM** | Work the Tier B queue — high-value ($2M+ / 15+ employees) or low-confidence drafts the system flags instead of sending. Approve, edit, or kill. |
| **Ongoing** | First-line reply triage. Opt-outs and OOO auto-handled. "No" gets logged. **Anything warm goes straight to Anthony, immediately.** |
| **Ongoing** | Owns the sending accounts — domains, inboxes, DNS records, deliverability dashboard. |

**Rule she enforces above all others:** no message asserts a fact about a prospect unless that fact came from a real scrape on file. Not inferred, not estimated, not generated.

---

## TRACK A — Emigen (infrastructure, no AI required)

Start immediately. Nothing else compresses the domain clock.

- [ ] **A1. Buy 2 aged domains** (registered 6+ months ago) close to `launchpadbizdev.com` — e.g. `getlaunchpadbd.com`, `launchpadgrowth.co`. Aged, not fresh: domain age is itself a spam signal. *Blocks everything downstream.*
- [ ] **A2. Buy 3 pre-warmed inboxes** on those domains, or Google Workspace seats + a warmup tool. Pre-warmed cuts time-to-send from ~30 days to ~10.
- [ ] **A3. Set SPF, DKIM, and DMARC** on both domains. Non-negotiable — without these, everything lands in spam regardless of warmup.
- [ ] **A4. Start warmup the day inboxes are live.** Do not send real mail during warmup.
- [ ] **A5. Buy email verification credits** (NeverBounce or ZeroBounce) — needed to turn owner names into deliverable addresses.
- [ ] **A6. Confirm the unsubscribe/opt-out mechanism** works end-to-end and writes back to the CRM. CAN-SPAM is a hard limit.
- [ ] **A7. Set up the deliverability dashboard** — track open rate and bounce rate per domain. Warning thresholds: opens under 45%, bounces over 2.5%.

**Never touched:** the main `launchpadbizdev.com` sending domain, and Anthony's main Meta profile.

---

## TRACK B — Anthony + Apollo (AI + data layer)

- [ ] **B1. Wire the ad-signal scrapers.** This is the gap — the ad layer has *never fired*. The one real audit on file (Evolution Air Conditioning, 4/21) has `meta_ads: null` and `google_ads: null`. See tool decisions below.
- [ ] **B2. Add Facebook Page ID resolution** — `business name → FB Page → page_id → Ad Library query`. Keyword search is unreliable; page_id is exact. This is the specific missing step the audit file names.
- [ ] **B3. Wire PageSpeed Insights** — free Google API, ~20 minutes. Currently `null` in the audit.
- [ ] **B4. Build the NSCB enrichment step** — company name in, owner name out (see decision below).
- [ ] **B5. Build the 25-prospect proof list.** Verified owner name + verified ad-format signal + GMB score, for 25 real Vegas home-services companies. **This is the gate: if we can't produce 25 accurate rows, we don't send anything.**
- [ ] **B6. Update agent prompts for auto-send.** They still say draft-only and will contradict the new model.
- [ ] **B7. Write the 4-touch sequence** against real data from the proof list, not templates in the abstract.
- [ ] **B8. Wire Tier B routing** — high-value or low-confidence drafts go to Emigen's 4 PM queue instead of auto-sending.
- [ ] **B9. Hot-reply alerting** to Anthony's phone.

---

## TRACK C — This week, zero warmup

Email cannot contact anyone for ~10 days. These can start Monday.

- [ ] **C1. Turn on `ig-cold-prospecting`** — already built. 20 prospects/day, personalized DM scripts, manual send, no ban risk. 10–15 min/day.
- [ ] **C2. Decide who sends the IG DMs.** Must be from Anthony's account per standing rule. If Anthony won't do 15 min/day, this doesn't run — say so now rather than discover it in week three.
- [ ] **C3. Run 5 Growth Audits** on the best names from the proof list and deliver them live. This is the highest-conversion motion we have and it needs zero infrastructure.

---

## Ad library tooling — decisions

The signal that matters most ("running graphics but no video," "running Meta but no Google") depends entirely on this layer.

| Platform | Tool | Why | Cost |
|---|---|---|---|
| **Google Ads** | **SerpApi Google Ads Transparency Center API** | Structured, legitimate, returns creative format (text / image / video) plus first-and-last-shown dates. Directly answers the format-gap signal. | 250 free searches/mo — enough at our volume |
| **Meta** | **Apify Meta Ad Library actor** (already wired) | No official API path exists for US commercial ads — the Meta API only returns political/issue ads outside the EU/UK. Scraping the public UI is the only route. | ~$0.15–0.40 per audit |
| **Meta (cross-check)** | **BigSpy free tier** | Independent database to sanity-check Apify output before we trust it in an auto-sent claim | Free tier |
| **TikTok** | TikTok Creative Center / Commercial Content Library | Lower priority; add after Meta + Google are proven | Free |

**Worth knowing:** Meta's platform terms restrict automated collection. Scraping the public Ad Library is standard industry practice and the data is public by regulatory design, but it is not officially sanctioned. Two mitigations: cross-check anything we assert, and keep scraping infrastructure isolated from the main Meta profile.

**The useful shortcut:** several of the 11 signals need no Meta data at all — GMB (works today), website and PageSpeed (free), Google ads (SerpApi), hiring signals. We can ship an accurate audit with zero Meta dependency and add Meta once it's verified.

---

## Decision-maker sourcing

**For home services — trades verticals:**
1. **Nevada State Contractors Board license search** — searchable by company name, returns the *qualified individual* and principals by name. Every HVAC, plumbing, roofing, electrical, and garage-door business in our target set is legally required to appear. Free, public, authoritative.
2. **Nevada SOS entity search** — officers, managing members, registered agent.
3. **Clark County / City of Las Vegas business licenses** — owner of record.
4. Then: email pattern inference (`first@`, `first.last@`, `f.last@`) → verification → deliverable address.

**For Law, Real Estate, Health, Auto, Business Services:** LinkedIn / Apollo / Clay, where profile density is high. Trades are the exception, not the rule.

The Evolution audit already pulled owner "Dennis Cope," so part of this works today.

---

## Sequencing

```
Day 0    A1–A3 (domains, inboxes, DNS)        ← start today, longest clock
Day 0–2  B1–B4 (scrapers + enrichment)
Day 2–3  B5 (25-prospect proof list)          ← GATE: accurate or we stop
Day 3    C1–C3 (IG + live audits start)       ← first real contacts this week
Day 3–5  B6–B9 (auto-send, Tier B, alerting)
Day 4    Emigen data-truth check on batch 1
Day 10   First cold email sends, 8–10/inbox/day
Day 14   Target volume, 25–30/day
Day 30   First honest read on reply rate
```

---

## Honest expectations

At 25–30 touches/day (~600/month), against our own benchmark of 1,000 → 35 replies → 12 qualified → 4–6 calls → 1–2 clients:

- ~21 total replies/month (including "no")
- ~7 qualified
- ~3 booked audits
- **~1 new client/month, ~$500–900 added MRR**

Cold at this volume is an annuity, not a windfall — roughly $8,400 of added run-rate over twelve months before any upsell. Reaching 2–4 clients/month requires 70–115 touches/day, meaning 8–12 inboxes and ~$500–700/mo of infrastructure.

**Cold is a supplement to referral, not the path to $75k/mo.** Referral is still 80% of revenue and still the highest-return thing on the board.

---

*Created 2026-08-12.*
