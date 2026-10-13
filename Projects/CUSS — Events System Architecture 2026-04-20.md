---
title: "CUSS — Events System Architecture"
type: project-sub
status: in-review
tier: primary
parent: "[[CUSS]]"
related: "[[GHL Event Ticketing — Multi-Attendee Capture Architecture 2026-04-20]]"
last_updated: 2026-04-20
related: ["[[Projects/00-INDEX]]"]
---

# CUSS — Events System Architecture

**Context:** Repeatable event ticketing/portal system inside GHL. Flagship event: **2026 Underground** (July 19–22, 2026, Washington DC, 1,500+ attendees, CULTure theme). Team built solution for "sell N tickets, capture each attendee" using product-per-quantity workaround + two-step transfer flow.

**Points of Contact:** Ryan Stankovic, Buel Collins, Zach Christensen
**Live Funnel:** https://funnel.startcussing.com/home-4366

---

## The Team's Current Architecture (as of 2026-04-20)

### Customer Journey
Landing Page → Ticket Selection → Payment → Confirmation → Form Submission → Ticket Transfer (if multi) → Portal Access → Event Participation

### Two-Step Funnel
1. **Event Landing Page** — event details, CTA "Get Tickets"
2. **Checkout Flow** — collects user info, ticket quantity selector, dynamic payment routing

### Payment System (The Workaround)
- Separate product created per quantity tier (1 ticket, 2 tickets, 3 tickets, 4 tickets)
- User selection routes to correct payment link dynamically
- **Solves GHL's "1 ticket per purchase" native limitation**

### Workflows
1. **Order Submitted (main)** → Confirmation email + portal access link
2. **Multi-Ticket Conditional** → If qty ∈ {2,3,4}, send ticket transfer email + form
3. **Ticket Transfer Form** → Inbound webhook creates N-1 additional contacts + grants portal access
4. **Ticket Transfer Confirmation** → Success email with event link
5. **Payment Confirmation** → Tag `Paid Attendee` + portal access + final confirmation

### KPIs Tracked
- Total ticket purchases
- Multi-ticket purchase rate
- Payment completion rate
- Ticket transfer completion rate
- Portal access engagement

---

## My Assessment — What's Working

1. **Product-per-quantity is the right hack.** It sidesteps GHL's missing per-attendee payment logic entirely. Clean execution.
2. **Two-step flow (buy → transfer) is the proven community pattern.** Matches what Latenode / GHL community landed on.
3. **Inbound webhook for contact creation** is the correct technical choice — gives us control over field mapping, tagging, dedupe logic.
4. **Reusability baked in from day one** — funnel/workflow/portal structure designed to duplicate. Big win for future events.
5. **Portal access as the reward mechanic** — ties event purchase to CUSS membership funnel. Smart upsell path.

---

## Gaps / Risks to Pressure-Test Monday

### A. Scalability — Ticket Quantity Cap
**Current:** Products go 1 → 4.
**Risk:** CUSS audience is CU C-suite bringing teams. Likely asks: "I need 8 seats for our ops team" or "My CUSO wants to bring 12." Hard cap at 4 means manual handling for every group order above that. At 1,500 attendees, group buys will happen a lot.
**Options:**
- Extend to 1 / 2 / 5 / 10 / Team (custom invoice) tiers
- Add group-sales email CTA for 5+
- Build a 5+ custom quote workflow

### B. Ticket Transfer Abandonment
**Current:** Buyer gets transfer email after multi-ticket purchase. If they never fill it out, N-1 attendees don't exist in GHL.
**Risk:** Event team shows up with incomplete attendee list. Buyer's teammates may not even know they have a ticket.
**Mitigation to add:**
- 24hr nudge: "You still have X unregistered tickets"
- 72hr nudge with urgency
- Day-of-event fallback: show buyer's name on all N tickets with "Transfer at check-in"

### C. Duplicate Attendee Handling
**Risk:** If transferred-to email already exists in GHL (CUSS member, newsletter subscriber, past event attendee), the webhook behavior matters.
**Decision needed:**
- Update existing contact (add event tag, don't create duplicate) — recommended
- Create duplicate — bad data hygiene
- Error out — bad UX

### D. Self-Attendee Confusion
**Current:** Buyer purchases 4 tickets. Are they attending? Do they fill out transfer form with 3 others, or 4?
**Need:** Clear copy in transfer email ("You have 3 additional tickets to assign — you're already counted").

### E. Calendar File (.ics)
**Not mentioned in brief.** Every confirmation email for a 4-day conference should include a calendar attachment or "Add to Calendar" link. Google/Apple/Outlook.

### F. Access Tiers & VIPs
**Unclear:** Is there a VIP tier, speaker tier, sponsor tier? Different portal visibility? Different email flows?
**Risk:** Tag structure and portal access logic needs to handle this before launch or becomes a rebuild later.

### G. Check-In / Day-Of Ops
**Not addressed.** 1,500 people, 4 days, 200 sessions. Without QR codes / scan-in / badge printing, the team will be hunting attendee lists on phones at registration.
**Options:**
- Lightweight: attendee list CSV exported from GHL, manual check-in at door
- Medium: QR code in confirmation email, free scan app (QRCheckIn, iVvy Free)
- Real: integrate with Whova / Bizzabo / Hi.Events for check-in only

### H. Refund / Cancellation Flow
**Not mentioned.** If attendee cancels, we need to:
- Revoke portal access
- Remove `Paid Attendee` tag
- Update attendee count for capacity tracking
- Issue Stripe refund

### I. Post-Event Lifecycle
**Partially addressed** ("make event access private for next event").
**Missing:**
- Post-event survey (NPS + feedback)
- Session recording delivery (via portal? email? paid on-demand?)
- "Alumni" tag for 2026 Underground attendees → feeds future event pre-sales + CUSS membership upsell
- Content repurpose loop (talks → white papers → podcast clips)

### J. Brand & Copy on Landing Page
Quick look at funnel.startcussing.com:
- Event city (DC) vs. footer contact address (Boulder City, NV) — should be visually separated or one might be misread as event location
- No visible early-bird pricing → weakens urgency
- Copy "Magic is believing in yourself" is CULTure theme but feels soft for CU C-suite audience — consider A/B against something more credibility-forward
- Brand color check: does the page hold CUSS red #ED1B23 + black/white consistently, or is Underground/CULTure running its own visual identity?

### K. KPI Dashboard
**Current:** KPIs listed but no mention of where they're surfaced.
**Risk:** If they live in GHL reports scattered across 4 different screens, the team won't check them. Consolidate into a single dashboard (GHL reporting widget or Looker Studio).

### L. Reusability Template
**Good intent stated.** But execution matters:
- Is this being saved as a GHL Snapshot?
- Are brand elements parameterized (event name, date, colors) so one template themes easily?
- Who owns the "clone for next event" process — Kyle? Abril? CUSS team?

---

## Questions for Monday Meeting (Organized)

### Site / Design
1. Should early-bird pricing show on landing page, or intentionally hidden until checkout?
2. Is CULTure a sub-brand with its own palette, or does it run CUSS red/black/white?
3. Can we clean up the event-city vs. business-address display to avoid confusion?
4. Do we need a mobile-first audit on the funnel before going live?

### Payment & Ticketing
5. What's the hard cap on tickets per purchase? Is 4 enough for expected group sizes?
6. How do we handle 5+ ticket groups — extend products, or custom-invoice path?
7. Is there a VIP / sponsor / speaker tier with separate payment flow?
8. Refund / cancellation workflow — what's the policy and automation?

### Ticket Transfer Flow
9. If buyer purchases 4, do they fill out 3 attendee forms (self + 3) or 4? Copy should make it obvious.
10. Abandoned transfer nudges — 24hr, 72hr, day-of? Agreed cadence?
11. Duplicate email handling in webhook — update existing contact or create new?
12. Does confirmation + transfer success email include .ics calendar file?

### Portal & Access
13. What access tiers exist post-purchase (attendee, VIP, speaker, sponsor)?
14. Does portal access persist post-event, or get locked to "Alumni" view?
15. Does event attendance feed into CUSS membership upsell?

### Operations & Day-Of
16. How does the team handle check-in at the venue? QR codes, printed lists, badge printing?
17. Who owns the attendee list during event week — Ryan, Buel, Zach?
18. What's the dashboard for live sales tracking during event week?

### Post-Event
19. Post-event survey workflow — in plan?
20. Session recording distribution plan — portal, email, on-demand?
21. Alumni tag + feed into 2027 Underground pre-sale?

### Reusability
22. Will this be saved as a GHL Snapshot template?
23. Parameterization — event name, date, colors, products as variables so cloning is fast?
24. Who owns the "clone for next event" SOP?

---

## Recommended Pre-Monday Tightening (Optional)

If the team wants a punchier Monday walkthrough, three quick wins:
1. **Add 24hr abandoned-transfer nudge workflow** — 20min build, saves a real day-of headache.
2. **Add .ics calendar file to confirmation email** — 15min add, massive UX win for a 4-day conference.
3. **Draft the "Alumni" post-event tag flow** — closes the loop and shows the CUSS upsell mechanic.

---

## Related Notes
- [[GHL Event Ticketing — Multi-Attendee Capture Architecture 2026-04-20]] — generic research on this GHL gap, three options compared
- [[CUSS]] — parent client context
