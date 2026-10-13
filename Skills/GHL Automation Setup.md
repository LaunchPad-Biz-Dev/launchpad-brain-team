---
title: "Skill: GoHighLevel (GHL) Automation Setup"
type: skill
status: active
tier: secondary
tags: []
last_updated: 2026-04-04
related: ["[[Skills/00-INDEX]]"]
---

# Skill: GoHighLevel (GHL) Automation Setup

**Owner:** Amber Nardo (Systems Expert) + Anthony Mendoza
**Date Created:** 2026-04-04
**Status:** Documented from live implementations

---

## Overview

This skill documents how Launchpad builds and configures automation sequences in GoHighLevel for clients. GHL serves as the white-label CRM platform for client sub-accounts, and automations are central to scaling client communication.

---

## Pre-Setup Checklist

Before building any GHL automation, confirm:
- [ ] Client sub-account is created and configured
- [ ] Contact fields are set up (name, email, phone, custom fields)
- [ ] Pipeline stages are defined and mapped
- [ ] Integration points identified (email, SMS, booking calendar, forms)
- [ ] SMS/A2P registration completed for client (required for SMS automations)
- [ ] Booking calendar linked (if using appointment scheduling)

---

## Core Automation Types

### 1. Lead Capture & Immediate Follow-Up (Fast Five)

**Trigger:** Contact enters CRM (via form, import, or lead capture)

**Sequence:**
- **Hour 0 (Immediate):** Welcome email with value proposition
- **Hour 24:** Follow-up email with first resource/offer
- **Day 3:** SMS check-in asking about interest/pain point
- **Day 4:** Second email with case study or social proof
- **Day 5:** SMS with limited-time offer or urgency angle

**GHL Configuration:**
```
Workflow Name: "Fast Five — [Client Name]"
Trigger: Contact added to CRM
Conditions: New contact (not previously contacted)
Actions:
  1. Send Email (immediate)
  2. Wait 24 hours
  3. Send Email
  4. Wait 48 hours
  5. Send SMS
  6. Wait 24 hours
  7. Send Email
  8. Wait 24 hours
  9. Send SMS
  10. Tag contact: "Fast Five Complete"
  11. Move to next workflow (nurture sequence)
```

---

### 2. Pipeline Stage-Based Automation

**Purpose:** Different automation sequences based on where contact is in sales funnel

**Example: Anthony Bradley Fitness Pipeline**

**Stage 1: Application Submitted**
- Trigger: Contact completes application form
- Action: Send confirmation email, schedule discovery call, tag as "Discovery Pending"
- Duration: Until discovery call scheduled or 7 days pass

**Stage 2: Discovery Call Scheduled**
- Trigger: Contact books calendar slot
- Action: Send reminder email (24h before), prepare discovery brief
- Duration: Until call occurs

**Stage 3: Discovery Call Completed → Multiple Paths**

Path A - *Positive Interest:*
- Trigger: Contact responds positively OR Anthony tags as "Hot Lead"
- Action: Send product recommendation email → product link → wait for purchase
- Duration: 3 days before re-offer

Path B - *No Show:*
- Trigger: Contact doesn't attend scheduled call
- Action: Send apology email + reschedule link, move to "Reschedule" stage
- Duration: 5 days to reschedule before moving to nurture

Path C - *Positive But Not Ready:*
- Trigger: Contact says "interested but timing unclear"
- Action: Move to "Future Follow Up" stage, nurture sequence begins
- Duration: 30-day, 60-day, 90-day check-ins

Path D - *Not Interested:*
- Trigger: Contact explicitly declines or Anthony marks "Didn't Buy"
- Action: Move to "Didn't Buy Reoffer" stage, trigger reoffer automation
- Duration: 14-day reoffer attempt, then long-term nurture

---

### 3. Educational/Nurture Sequence (Multi-Month)

**Purpose:** Keep contacts engaged with valuable content, build trust, nurture over time

**Example: Anthony Bradley Fitness 12-Month Educational Campaign**

**Setup:**
```
Workflow Name: "12-Month Wellness Education — [Client Name]"
Trigger: Contact purchases product OR manually tagged "Nurture"
Conditions: None (runs for all in this segment)

Actions per month:
  1. Send Email (detailed educational content)
  2. Wait 2 days
  3. Send SMS (summary + link back to email)
  4. Wait 26 days (total 28-day month)
  5. Loop for next month (repeat 12 times)
  6. After month 12: Move to "Long-term Engagement" workflow
```

**Content Framework (per month):**
```
Month 1: Water/Hydration basics
Month 2: Sleep & recovery
Month 3: Foundational fitness principles
Month 4: Interval training
Month 5: Chia seeds & superfoods
Month 6: Muscle growth & progressive overload
... (through Month 12)
```

**Email Template Structure:**
```
Subject: [Month Theme] — Actionable Tip 💡

Hello {{contact.name}},

[Intro: Why this topic matters]

1. [Key Concept] 📌
2. [How-to / Benefit] 🎯
3. [Actionable Hack] 🚀

[Call to action: Blog link, community challenge, etc.]

[Signature: Anthony]
```

**SMS Template:**
```
💡 [Month Theme]: [1-line tip]. [Actionable advice]. Learn more at [link] 📧
```

---

### 4. Reoffer/Re-engagement Automation

**Purpose:** Bring back leads who didn't convert, with different angle or urgency

**Trigger:** Contact in "Didn't Buy" stage OR "Didn't Buy Reoffer" stage

**Sequence Structure:**

**Reoffer Round 1 (Immediate):**
- Day 0: Email with same offer, different framing (emphasize benefits they mentioned)
- Day 3: SMS with personal touch ("It's Anthony...")
- Day 7: Email with case study/social proof

**Reoffer Round 2 (14 days later):**
- Day 14: Email with same offer, new angle (e.g., if first was fitness, focus on health/wellness impact)
- Day 17: SMS with urgency/scarcity angle
- Day 21: Email with limited-time offer or pricing adjustment

**Reoffer Round 3 (90 days later):**
- Day 90: Email with results/proof from other clients
- Day 93: SMS with new offer or changed positioning
- Day 100: Final email before moving to long-term nurture

**GHL Configuration:**
```
Workflow Name: "Reoffer Automation — [Client Name]"
Trigger: Contact tagged "Didn't Buy"
Wait: 0 (immediate)

Round 1:
  1. Send Email: Reoffer (primary positioning)
  2. Wait 3 days
  3. Send SMS: Personal touch
  4. Wait 4 days
  5. Send Email: Social proof angle
  6. Wait 10 days (total 14 before Round 2)

Round 2:
  1. Send Email: Reoffer (different angle)
  2. Wait 3 days
  3. Send SMS: Urgency/scarcity
  4. Wait 4 days
  5. Send Email: Limited-time offer
  6. Wait 76 days (total 90 before Round 3)

Round 3:
  1. Send Email: Results/proof
  2. Wait 3 days
  3. Send SMS: New offer positioning
  4. Wait 7 days
  5. Send Email: Final re-engagement
  6. Tag: "Reoffer Complete" → Move to long-term nurture
```

---

### 5. Conditional Branching (Response-Based)

**Purpose:** Different automation paths based on contact response

**Example: "Did They Respond?" Automation**

**Setup:**
```
Workflow Name: "Qualification Branching — [Client Name]"
Trigger: Contact sent inquiry question

Conditional Split (Day 3):

  IF Contact replied/engaged:
    → Send Email: "That's great, {{contact.name}}!"
    → Recommend appropriate product tier
    → Send booking link
    → Tag: "Hot Lead — Positive Response"

  IF Contact did NOT reply:
    → Send Email: "Perhaps this got lost in the mix?"
    → Resend question with slightly different angle
    → Send SMS: Check-in reminder
    → Tag: "No Response — Follow Up Needed"
    → Wait 4 days, reassess

Continue workflow based on engagement level
```

---

## Personalization & Merge Tags

### Standard Contact Fields (GHL)
```
{{contact.firstName}}        — First name
{{contact.lastName}}         — Last name
{{contact.name}}             — Full name
{{contact.email}}            — Email address
{{contact.phone}}            — Phone number
{{contact.customField}}      — Custom field (varies by setup)
```

### Custom Fields to Set Up (per client)
- `Goal` — What client is trying to achieve
- `Budget` — Price point mentioned
- `Pain Point` — Primary challenge
- `Product Interested In` — Which service/product
- `Engagement Level` — Hot/Warm/Cold
- `Source` — How they found you (Facebook, referral, etc.)
- `Stage` — Current pipeline position

### Using Merge Tags in Emails/SMS
```
Email:
"Hi {{contact.firstName}},

I noticed you mentioned {{contact.goal}} as your main focus.
That's exactly what our {{contact.productInterested}} program addresses..."

SMS:
"Hey {{contact.firstName}}, quick question about {{contact.painPoint}}... 📲"
```

---

## Email vs. SMS Strategy

### Email (Primary for Detail)
- Longer content (500-800 words)
- Educational, multi-section
- Links to resources, booking pages, product pages
- Sent when contact has time to read (asynchronous)
- Best for: Education, detailed positioning, multiple offers

### SMS (Secondary for Urgency/Touchpoint)
- Brief, 1-3 lines max
- Call-to-action or conversation starter
- Sent 2-3 days after email
- Higher urgency tone (time-sensitive, personal)
- Best for: Check-ins, reminders, quick wins, scheduling

### Timing Pattern
```
Email + Wait 2-3 days → SMS → Wait 4-7 days → Email → Wait 2-3 days → SMS
```

This creates multiple touchpoints without overwhelming contact.

---

## Implementation Checklist

When building a new client automation:

- [ ] Define all pipeline stages and triggers
- [ ] Write email templates (2-3 iterations with client)
- [ ] Write SMS templates (short, conversational)
- [ ] Set up custom contact fields
- [ ] Create workflows in GHL UI (or via API)
- [ ] Set up merge tag replacements
- [ ] Test with internal contact (yourself)
- [ ] Verify email delivery (check spam)
- [ ] Verify SMS delivery (check formatting)
- [ ] Train client on monitoring/adjustments
- [ ] Document workflow in Brain (for next agent)
- [ ] Set 30-day review to assess performance

---

## Common Pitfalls & How to Avoid

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Too many emails** | Overwhelms contact, increases unsubscribe | Limit to 1 email + 1 SMS per 3-5 days |
| **Impersonal tone** | Lower engagement, feels mass-produced | Always use {{contact.firstName}}, reference previous interaction |
| **Unclear CTA** | Contact doesn't know what to do next | One clear CTA per email (book, click, reply) |
| **No follow-up logic** | Sequences run regardless of engagement | Build conditional paths (responded vs. didn't respond) |
| **Timing issues** | Send at odd hours, miss optimal engagement | Test send times (typically Tue-Thu 9-11am) |
| **Generic sequences** | Doesn't speak to client's specific need | Customize per product/pain point mentioned |

---

## Measuring Automation Success

**Metrics to Track (in GHL dashboard):**
- Open rate (target: 20-30%)
- Click rate (target: 5-10%)
- Reply rate (target: 5-15% for engagement emails)
- Conversion rate (varies by offer, target: 2-5%)
- Unsubscribe rate (target: <2%)

**Optimization Process:**
1. Run automation for 30 days
2. Review metrics in GHL
3. Identify low-performing emails (low open, high unsubscribe)
4. Adjust subject lines, sending times, or copy
5. Run A/B test (2 versions, different segments)
6. Implement winner, retire loser
7. Repeat every 30 days

---

## Related Notes
- [[Email and SMS Sequences]]
- [[CRM and GHL Workflow]]
- [[Systems Department]]
- [[AI Systems — ChatGPT Extract]]
