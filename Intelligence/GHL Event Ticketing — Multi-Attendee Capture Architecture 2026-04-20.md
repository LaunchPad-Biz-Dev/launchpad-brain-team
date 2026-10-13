---
title: "GHL Event Ticketing — Multi-Attendee Capture Architecture 2026-04-20"
type: intelligence
status: active
tier: secondary
tags: []
last_updated: 2026-05-18
related: ["[[Intelligence/00-INDEX]]"]
---

# GHL Event Ticketing — Multi-Attendee Capture Architecture

**Date:** 2026-04-20
**Context:** Client portal build — stuck on ticketing. Using Products section to sell tickets, but when buyer purchases multiple (e.g., 10), there's no native way to capture info for each attendee, turn them into contacts, and tag per event.
**Goal:** Mini Eventbrite built inside GHL.

---

## The Core GHL Gap (Confirmed)

GHL's Products + Shopping Cart Mode supports multi-quantity purchase, but the transaction creates **one contact** (the buyer). The `Order Submitted` workflow trigger exposes product name, quantity, and price as custom values — but GHL has **no native mechanism to loop N times** and create N contacts from a single order.

- **Array Functions** (Premium workflow action) can filter/sort/map arrays — but **cannot iterate to trigger N actions**. Confirmed via GHL docs.
- **Class Booking Calendar + Add Guests** — closest native option. Can require guest name/email, charges per attendee, decrements seats. But: guest entries are attached to the appointment, they do NOT automatically become full contacts with rich custom fields, tags, and workflow entry.
- **Multi-ticket with unique ID per attendee** is a top-requested feature on ideas.gohighlevel.com — confirmed GHL gap, not something we missed.

---

## Three Architecture Options (Ranked)

### Option A — Pure GHL (Post-Purchase Attendee Registration Funnel)
**Stays entirely inside GHL. No third-party tools. Highest client ownership.**

**Flow:**
1. Buyer purchases N tickets via Products order form (Shopping Cart Mode, `Allow multiple quantity` enabled).
2. `Order Submitted` trigger fires workflow:
   - Tag buyer with `event-{name}-buyer` and `tickets-purchased-{N}`
   - Store `quantity_purchased` and `tickets_remaining = N` as custom fields on buyer contact
   - Send confirmation email with CTA: **"Register Your Attendees →"** linking to post-purchase funnel page with buyer contact ID as URL param
3. Post-purchase funnel page contains an **Attendee Registration Form** that captures ONE attendee at a time (First Name, Last Name, Email, Phone, dietary/notes — whatever event needs).
4. Form submission triggers second workflow:
   - Create Contact (new attendee) with event tag `event-{name}-attendee`
   - Add custom field `ticket_group_owner = {buyer contact ID}` to link attendee back to buyer
   - Decrement buyer's `tickets_remaining` by 1 (Math workflow action)
   - If `tickets_remaining > 0` → send buyer back to form with "N tickets left to register"
   - If `tickets_remaining = 0` → fire completion workflow, email buyer + internal team with full attendee list
5. Attendee list for event = filter contacts by `event-{name}-attendee` tag.

**Pros:** No third-party cost. Full GHL ownership. Client can manage everything inside their portal.
**Cons:** Buyer has to submit the form N times (one per attendee). UX is "register next attendee" loop, not a single dynamic form. If buyer abandons after 3 of 10, we need a nudge workflow.
**Nudge workflow:** 24hr delay after purchase → if `tickets_remaining > 0`, email "You still have X unregistered tickets, complete registration here."

---

### Option B — GHL + Make.com (Middleware Loop Iterator)
**Best UX. Attendees captured in one dynamic form. Adds one external tool.**

**Flow:**
1. Buyer purchases N tickets in GHL (same as Option A, step 1).
2. `Order Submitted` webhook → Make.com scenario.
3. Make.com generates a **single-use registration URL** with quantity embedded as a param, emails it to buyer.
4. Registration URL points to a Jotform/Tally/Typeform with **repeating attendee sections** (dynamic rows based on quantity). Jotform and Tally both support this natively; GHL forms do not.
5. Form submission → Make.com iterator splits the response array into N individual attendee records.
6. Make.com loops: for each attendee, create a GHL contact via API with event tag + `ticket_group_owner` custom field linking to buyer.
7. Completion: Make.com sends buyer + internal team the final attendee list.

**Pros:** One-submit UX for the buyer. Cleanest experience. Easy to scale to other events.
**Cons:** ~$9/mo Make.com plan. Form lives outside GHL (though it can be embedded in a GHL funnel via iframe). One more tool for the client to understand.

---

### Option C — Third-Party Ticketing Bridge (Ticket Tailor or Hi.Events)
**Use a purpose-built ticketing platform, sync to GHL.**

**Flow:**
1. Event created in Ticket Tailor (free tier up to ~$1/ticket) or Hi.Events (open source, self-hosted, free).
2. Attendees buy tickets on the ticketing platform's hosted checkout — which **natively captures each attendee's info at purchase time** (this is the whole reason ticketing platforms exist).
3. Integration (Integrately/Appy Pie/Zapier) with trigger `New Ticket Purchase` → creates one GHL contact per attendee, maps name/email/ticket type/event name, tags automatically.
4. GHL workflows take over for follow-up, reminders, CRM.

**Pros:** Solves the capture problem natively. Ticketing platforms handle edge cases (refunds, QR codes, check-in apps, seat maps). Proven pattern.
**Cons:** Purchase happens off the client's GHL portal (breaks the "single portal" vision). Adds platform fees. Requires integration subscription.

---

## Recommendation

**Start with Option A** if the goal is "keep it all in GHL" and buyer UX tolerating N form submissions is acceptable. Most B2B / team-event cases this is fine — the person buying 10 tickets for their team is happy to register 10 people in a loop, especially with a clear counter and saved progress.

**Move to Option B** if buyer UX becomes a friction point or you see abandoned registrations. Make.com + Tally adds ~$20/mo total and makes it one submit.

**Only use Option C** if the client is running frequent high-volume events and needs real ticketing features (QR check-in, assigned seating, refunds, waitlists). For simple workshops/classes/meetups, it's overkill.

---

## Key Build Details

**Custom fields needed on Contact:**
- `tickets_purchased` (number)
- `tickets_remaining` (number)
- `ticket_group_owner` (contact ID — links attendee back to buyer)
- `event_name` (text)
- `ticket_type` (text — GA, VIP, etc.)

**Tags to create (per event):**
- `event-{event-slug}-buyer`
- `event-{event-slug}-attendee`
- `event-{event-slug}-vip` (if tiered)
- `event-{event-slug}-registered` / `event-{event-slug}-incomplete-registration`

**Workflows needed:**
1. Post-purchase → confirmation + attendee registration CTA
2. Attendee form submission → create contact + decrement counter + check completion
3. Abandoned registration nudge (24hr / 72hr)
4. Completion → send attendee list to buyer + internal team
5. Pre-event reminder sequence (tag-based, fires on all event attendees)

**Funnel pages needed:**
1. Event landing / checkout
2. Post-purchase thank you with "Register Attendees" CTA
3. Attendee registration form (one attendee, loop N times)
4. Registration complete page

---

## GHL Webhook Note (2026)

The legacy `X-WH-Signature` header deprecates **July 1, 2026**. Webhooks will be signed only with `X-GHL-Signature` after that. Any Make.com/Zapier scenarios we build must validate against the new header or will break. Worth flagging to any middleware we use.

---

## Open Questions for Anthony

1. How big are the events? (Affects Option A vs B vs C calculus.)
2. Is per-attendee payment ever needed, or always flat "buy N at $X"? (Class Booking Calendar becomes relevant if per-attendee payment varies.)
3. Do we need QR code check-in at events, or is a digital attendee list enough?
4. Does the client need refund/cancellation handling per attendee, or per order?
5. How often will the client run events? One-off vs monthly vs weekly affects whether we productize this as a reusable template.

---

## Sources

- [GHL: Add Guests & Per-Attendee Payments in Calendars](https://help.gohighlevel.com/support/solutions/articles/155000005180-add-guests-features-in-calendar-bookings)
- [GHL: Class Booking Calendars](https://help.gohighlevel.com/support/solutions/articles/155000003554-how-to-create-a-class-booking-calendar-seats-capacity-availability-explained-)
- [GHL: Shopping Cart Mode (V2 Funnels)](https://help.gohighlevel.com/support/solutions/articles/48001221440-shopping-cart-mode-in-one-and-two-step-order-forms-v2-funnels-only-)
- [GHL: Order Submitted workflow trigger](https://help.gohighlevel.com/support/solutions/articles/155000003535-workflow-trigger-order-submitted)
- [GHL: Array Functions (Premium)](https://help.gohighlevel.com/support/solutions/articles/155000001466-workflow-action-array-functions-premium-)
- [GHL: Inbound Webhook Premium Trigger](https://help.gohighlevel.com/support/solutions/articles/48001237383-how-to-use-the-inbound-webhook-workflow-premium-trigger)
- [GHL: Webhook Integration Guide](https://marketplace.gohighlevel.com/docs/webhook/WebhookIntegrationGuide/index.html)
- [Latenode Community: Multi-attendee booking automation in GHL](https://community.latenode.com/t/multi-attendee-booking-automation-in-gohighlevel-need-help-with-contact-creation-and-appointment-linking/24085)
- [GHL Ideas: Event Calendar w/ Ticketing + Payment (requested feature)](https://ideas.gohighlevel.com/scheduling-calendar/p/event-calendar-wticketing-payment-processing)
- [Ticket Tailor ↔ GHL via Integrately](https://integrately.com/integrations/gohighlevel/ticket-tailor)
- [Hi.Events (open source Eventbrite alternative)](https://hi.events/)

---

## Related Brain Notes

- [[GHL token architecture]] — reminder that client portal tokens differ from agency
- [[GHL approval workflow TODO]] — tie-in to broader GHL buildout priorities
