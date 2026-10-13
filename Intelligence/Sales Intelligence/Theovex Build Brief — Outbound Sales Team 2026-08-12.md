---
title: "Theovex Build Brief — Outbound Sales Team (Head-to-Head Test)"
type: intelligence
status: active
tier: secondary
tags: [sales, outbound, theovex, evaluation, build-brief]
last_updated: 2026-08-12
related: ["[[AI Outbound Sales Team — Full Scope Handoff 2026-08-12]]", "[[Ideal Client Profile]]", "[[Sales Department]]"]
---

# Theovex Build Brief — Outbound Sales Team

**Purpose:** Rebuild LaunchPad's outbound sales team inside Theovex as a head-to-head test against the existing Claude Code build. Doubles as a product demo — findings go back to the Theovex team.

**Test design:** Theovex gets the same business inputs we had in April 2026 (ICP, offer, constraints, assets) but **not** our architecture and **not** our retro. We want to see what it builds cold. Our own build + the 30-day failure become the scoring rubric, revealed after.

---

## THE PROMPT

```
I run LaunchPad Business Development — a full-service marketing agency in Las Vegas,
about 16 people, ten years in. I want you to build me an outbound sales team inside
your platform. Not a plan for one. The actual working thing.

I'm going to be straight with you about why: I've already built a version of this on
another platform. I'm rebuilding it here to see which one actually generates clients.
So build the best version you can — I'll be comparing directly, and I'll be giving
your team honest feedback either way.

Here's everything you need.

────────────────────────────────────────────────────────────
THE BUSINESS
────────────────────────────────────────────────────────────

18 active clients, ~$37,800/mo in ad spend under management. Roughly 80% of our
revenue comes from referrals, which is exactly the problem — we're not selling, we're
waiting. In February we lost 3 clients and signed 0. I want to get LPBD to $75k/mo.

What we sell:

  Essential Growth        $2,500/mo   FB/IG ads, 4 videos, 8 graphics, monthly shoot,
                                      social, CRM
  Comprehensive Growth    $3,500/mo   Full ad suite, 8 videos, 16 graphics, shoot,
                                      social, CRM, reputation mgmt
  Ultimate Business       $4,500/mo   + 12 videos, 24 graphics, advanced strategy,
                                      premium CRM

We recently added lower-friction entry offers to widen the top of the funnel, and I
think these matter a lot for outbound:

  CRM only          $197/mo (6-month contract)
  Ads only          $500/mo + 25% of spend  |  $1,000/mo + 20%  |  $2,500/mo flat
  Content only      $750/mo (12 graphics)  |  $1,000/mo (4 videos + 6 graphics)
                    $1,500/mo (4 videos + 8 graphics, shot in-house)
  Upsells           +$500/mo scheduled posting · +$197/mo CRM · +$500/mo ads

Ad spend is always quoted separately from service fee.

Our positioning: "We help mid-market service businesses generate predictable monthly
leads and build a brand that reflects their service quality — done-for-you in 90 days,
without you touching content, ads, or CRM."

The insight underneath it: these owners don't buy marketing. They buy predictability
and control.

────────────────────────────────────────────────────────────
WHO WE'RE GOING AFTER
────────────────────────────────────────────────────────────

Primary target — Las Vegas home services owner-operators:

  Revenue          $500K – $5M
  Team             5 – 25 employees
  Marketing spend  $2K – $10K/mo
  Decision-maker   the owner, single decision, no committee
  Verticals        HVAC, plumbing, roofing, garage doors, electrical
  Geography        Las Vegas, Henderson, North Las Vegas, Summerlin, Spring Valley,
                   Paradise, Enterprise, Boulder City
  Language         English primary, Spanish a real advantage here

There are roughly 2,000 scrapable businesses in that metro that fit. Later expansion
is Law and Franchise, then Phoenix / Tucson / Reno. Not now.

We do NOT work with: pre-revenue startups · anyone who can't clear our entry pricing ·
national enterprise beyond our delivery capacity · MLM, adult, crypto, cannabis ·
businesses with active litigation or negative PR we'd inherit · people who aren't the
decision-maker and can't get me to one · anyone whose timeline is more than 90 days
out.

Buying triggers worth watching for: expansion (new locations, hiring sprees), revenue
plateau despite effort, new competition in their market, leadership change.

Here's the targeting layer I care most about — observable signals we can actually
find, not vibes:

  · Google Business Profile has under 50 reviews or below 4.0
  · GBP hasn't posted in 30+ days
  · Running Meta ads but no Google ads
  · Running ads that are ALL graphics, no video  ← our best single hook
  · Running ads that are ALL video, no graphics  ← same, other direction
  · Ads not connected to any CRM (lead leakage)
  · English-only ads in a market that's 30%+ Spanish-speaking
  · Instagram posting less than 2x/week over the last 30 days
  · Website mobile load over 3 seconds
  · No lead form above the fold
  · Actively hiring (growth phase means budget)

"You're running six graphics ads and zero video" is a specific, checkable, personal
opener. That's the kind of first touch I want — about them, not about us.

────────────────────────────────────────────────────────────
PROOF WE CAN USE
────────────────────────────────────────────────────────────

Five clients we cite, matched by vertical:

  Toro Taxes Franchise Sales  — longest tenure, our first sale ever, best ROAS
                                visibility → franchise/tax proof
  Matsuda Nadig Law           — referred us another firm → law proof
  Upbeat Health               — highest-paying, premium niche → top-tier pricing
                                confidence
  Continental Currency Service— 3 years, documented growth → longevity +
                                Spanish-language proof
  Durango HVAC                — recent profitability momentum → home services proof

One hard rule: never cite Wamen Garage Doors. Outcome was poor. It appears nowhere —
not in messages, not in case studies, not on calls.

Our free offer is a Growth Audit. We scrape a prospect's ad libraries, Google Business
Profile, socials, and website, score it, and hand them a one-page report: a growth
grade, their top 3 revenue leaks with dollar estimates, a competitor snapshot, and six
fixes — three they can do themselves, three we'd do for them. Then a 30-minute live
walkthrough. It's real value given away free, and it's what every outbound message
should be pointing at.

────────────────────────────────────────────────────────────
HARD CONSTRAINTS — these are not preferences
────────────────────────────────────────────────────────────

1. NOTHING AUTOMATED TOUCHES MY MAIN META PROFILE. It holds access to 10+ client ad
   accounts through Business Manager. A ban doesn't cost me a campaign, it costs me
   the ability to serve half my clients. Any design that risks it is dead on arrival.

2. The AI never impersonates me or anyone on my team. It drafts. A human sends. If
   you want to argue for a different model, you have to solve for that risk explicitly.

3. Outbound originates from my identity only — not my sales rep's, not my creative
   director's. Prospects are buying access to me.

4. Never expose internal deal routing (who closes which tier) to a prospect.

5. Never offer custom pricing, promise specific results, or go below published rates
   without my approval.

6. Honor opt-outs absolutely. CAN-SPAM and state rules are hard limits.

7. Hot replies reach a human immediately, always. I'd rather over-escalate.

────────────────────────────────────────────────────────────
WHAT I WANT YOU TO BUILD
────────────────────────────────────────────────────────────

An outbound system that finds Vegas home-services businesses matching the profile
above, qualifies them against those signals, writes genuinely personalized first
touches referencing something real about their business, sequences follow-up across
channels, triages replies, keeps our CRM clean, and hands me a short daily queue of
work worth doing.

Build the pieces you think that requires. I'm not going to hand you an architecture —
what you choose to build, and what you choose to leave out, is part of what I'm
evaluating.

Two things I will push on hard:

THE DAILY LOOP. Show me exactly what happens each day. Who touches it, at what time,
for how long, what they see, what they decide. Assume I am NOT available daily — I'm
in client meetings and on sales calls. Tell me what happens on a day nobody logs in at
all. If your answer requires my attention every morning, it will fail, and I'd rather
you design around that now than find out in week three.

THE HUMAN GATE. Given constraint #2, tell me precisely where the human belongs and
what they're actually reviewing. "A human approves the messages" isn't an answer —
approving 100 messages a day is a job nobody will do by day four. Design the specific
mechanism.

────────────────────────────────────────────────────────────
HOW I'M JUDGING THIS
────────────────────────────────────────────────────────────

I'm running this against an existing build, so I need comparables. Be concrete:

  · How fast can this go from zero to first real prospect contacted?
  · How many qualified, genuinely personalized touches per day can it sustain WITHOUT
    my daily involvement?
  · What does it actually cost to run per month, all in?
  · What reply rate should I expect, and what's that based on?
  · What breaks first at volume, and what's the warning sign?
  · Will this still be running on day 30 if I don't look at it? That's the real test.
    The last system I built was fully functional and produced zero contacts in 30 days
    because it needed me and I wasn't there.

Give me honest numbers with your reasoning, not best-case ones. I'd rather hear "40
touches a day sustained" and get it than hear "500" and get zero.

────────────────────────────────────────────────────────────
ONE MORE THING
────────────────────────────────────────────────────────────

Since I'm evaluating the platform as much as the output — tell me where you hit its
edges. What did you have to work around? What would have been cleaner with a
capability you don't have? What did you want to do natively and couldn't? That
feedback goes back to your team, and it's genuinely useful to me either way.

Start by telling me what you'd build and why, then build it.
```

---

## What we hold back (and why)

Not sent: our 10-agent roster, the 23-skill library, our CRM asset library, our
approval-flow design, and the Phase 1 retro.

Reason: if we hand over the answers, we learn nothing about whether the platform can
reason its way to them. The interesting questions are whether Theovex independently
(a) lands on a Meta-safe manual-send pattern, (b) predicts the approval bottleneck
before running into it, and (c) picks the "missing ad format" hook out of the signal
list on its own.

If we'd rather optimize for the best possible outbound system instead of the cleanest
comparison, send the full handoff doc alongside this prompt and drop the "I'm not
going to hand you an architecture" line.

## Scoring rubric — reveal after Theovex responds

| # | Test | Our answer | Theovex |
|---|---|---|---|
| 1 | Does it protect the Meta account without being told how? | Manual-send queue, 20/day, AI researches + drafts, Anthony copy-pastes | |
| 2 | Does it predict the approval bottleneck unprompted? | We didn't — cost us 30 days and 0 contacts | |
| 3 | Does it name a non-CEO daily operator? | We didn't staff one. Root cause of failure. | |
| 4 | Does it pick the missing-ad-format hook? | Yes — best-performing opener in the set | |
| 5 | Does it point outbound at the free audit, not the retainer? | Yes — Growth Audit is the ask | |
| 6 | Does it use the $197/$500/$750 entry tiers as the outbound wedge? | We didn't at the time — likely a real miss | |
| 7 | Does it give honest volume numbers? | 1,000 touches → 35 replies → 12 qualified → 4–6 calls → 1–2 clients/mo | |
| 8 | Time from zero to first contacted prospect | 30 days, and it was 0 | |
| 9 | Monthly run cost | ~$180/mo tooling | |
| 10 | Still running on day 30 unattended? | **No.** The bar to beat is low — clear it. | |

Row 10 is the whole test. Everything else is detail.

---

*Created 2026-08-12.*
