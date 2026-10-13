---
title: "Skill: Email & SMS Sequences"
type: skill
status: active
tier: secondary
tags: []
last_updated: 2026-04-04
related: ["[[Skills/00-INDEX]]"]
---

# Skill: Email & SMS Sequences

**Owner:** Anthony Mendoza (Strategy), Amber Nardo (Implementation)
**Date Created:** 2026-04-04
**Status:** Live templates from client implementations

---

## Overview

This document contains email and SMS sequence templates used across Launchpad clients. These are battle-tested frameworks that can be customized per client/industry.

---

## Sequence Type: Product Purchase Confirmation (Multi-Email)

### Use Case
Client purchases a multi-component program (e.g., 6-Week Health is Wealth with 13 associated documents/videos).

### Strategy
Break 13 documents into 4 thematic sections, one email per section over 2-4 weeks. Each email introduces the section, highlights key benefits, provides actionable next steps.

### Email Templates

#### Email 1: Get Started / Introduction
**Send:** Immediately upon purchase

```
Subject: 🚀 Welcome to the 6-Week Health is Wealth Program!

Hello {{contact.name}},

Congratulations on taking the first step toward transforming your health and fitness!
We're thrilled to have you join the Health is Wealth community.

Over the next 6 weeks, you'll receive guidance, resources, and support across four key areas:
your mindset, your body, your mind, and your nutrition. Each week builds on the last, creating
a comprehensive approach to sustainable wellness.

📦 YOUR FIRST SECTION: GET STARTED

To kick things off, we've created three essential documents to help you prepare:

1. **Success Manual** — Your roadmap for the next 6 weeks
2. **Quickstart Checklist** — What to do in your first 48 hours
3. **Body Measurements Guide** — How to track your progress (it's more than the scale!)

These documents set the foundation for everything that follows. Download them, review them,
and keep the Success Manual handy—you'll reference it throughout the program.

🎯 YOUR NEXT STEPS

1. Read the Success Manual (15 minutes)
2. Complete the Quickstart Checklist
3. Take your initial body measurements
4. Prepare to dive into fitness next week

Stay tuned for the next email, where we'll empower your body with workout resources and accountability.

Remember: You've already made the hardest decision—to start. We've got you from here.

With gratitude,
{{team.signature}}

P.S. If you have any questions, reply to this email and we'll get back to you within 24 hours.
```

**SMS (Day 1):**
```
Hey {{contact.firstName}}! 🎉 Welcome to 6-Week Health is Wealth. Download your Success Manual,
Quickstart Checklist, and Body Measurements Guide to get started. [Link to downloads]
```

---

#### Email 2: Empower Your Body
**Send:** Day 7-10 after purchase

```
Subject: 💪 Let's Empower Your Body — Your Workout Plan Starts Now

Hello {{contact.name}},

Now that you've established your foundation, it's time to move your body—intentionally and effectively.

This section is all about building strength, endurance, and the habits that will serve you beyond
these 6 weeks. We've included three core resources:

1. **Health is Wealth Workouts** — Progressive exercises designed for all fitness levels
2. **Health is Wealth Coaching** — Expert guidance on form, intensity, and progression
3. **Accountability Partner Guide** — How to leverage support for consistency

🏋️ WHAT TO EXPECT

These workouts are designed to be done 4-5 days per week. Each session is 30-45 minutes and requires
minimal equipment (dumbbells, resistance bands, bodyweight options included).

The key to success in this section: consistency over perfection. You don't need to be
perfect—you need to be consistent.

🎯 YOUR NEXT STEPS

1. Review the Workout Plan and schedule 4-5 sessions this week
2. Watch the Coaching Videos (especially the form guides—these save injuries)
3. Identify your accountability partner (friend, family, or our community forum)
4. Log your first workout

Look out for our next email where we delve into empowering your mind with proven mindset practices.

You're doing great. Stick with it.

With momentum,
{{team.signature}}

P.S. Feeling sore? That's a sign the program is working. Review the Recovery Guide in your Success Manual.
```

**SMS (Day 7):**
```
💪 Time to move! Your workout plan + coaching videos are ready. Start with the form guide—proper
form = better results. Log your first session: [Link]
```

---

#### Email 3: Empower Your Mind
**Send:** Day 14-17 after purchase

```
Subject: 🧠 The Hidden Advantage — Master Your Mindset

Hello {{contact.name}},

Physical transformation starts with mental transformation. The strongest body can't override a weak mindset,
and that's what this section addresses.

Inside, you'll find:

1. **Purpose Worksheet** — Define why you're doing this (hint: it's deeper than "lose weight")
2. **Limiting Beliefs Framework** — Identify and reframe the stories holding you back
3. **Daily Affirmation Practice** — 6-week progressive mindset protocol

🧭 WHY THIS MATTERS

Studies show that mindset is the #1 predictor of program success—even more than genetics or age.
The people who win are the ones who've aligned their identity with their goals.

That's what these tools do.

🎯 YOUR NEXT STEPS

1. Spend 20 minutes on the Purpose Worksheet (deep reflection required)
2. Identify 3 limiting beliefs that have held you back
3. Review the Affirmation Practice and pick one to start this week
4. Journal your thoughts (even 5 minutes daily helps)

You've now covered Body (Week 1-2) and Mind (Week 2-3). Next week, we tackle Fuel—the nutrition
framework that will amplify your workouts and support sustainable results.

You're halfway through the foundation. The best part comes next.

With belief,
{{team.signature}}

P.S. Remember: Mindset work isn't "fluffy." It's the operating system that determines whether you stick
with the program. Treat it seriously.
```

**SMS (Day 14):**
```
🧠 Your mind is your superpower. Complete the Purpose Worksheet + pick one affirmation to practice.
Your results depend on this. [Link]
```

---

#### Email 4: Empower Your Fuel
**Send:** Day 21-24 after purchase

```
Subject: 🥗 Your Nutrition Blueprint — Fueling Results

Hello {{contact.name}},

You're over halfway through the program. Your mind is stronger. Your body is more resilient.
Now let's make sure you're fueling both properly.

This final section includes:

1. **Carb Cycling Guide** — Optimize energy and recovery
2. **Meal Prep Framework** — Nutrition simplified
3. **Macro Tracking Basics** — Understand what your body needs

🎯 NUTRITION WITHOUT OBSESSION

Here's what we believe: Nutrition should support your lifestyle, not consume it. These tools
are designed to make healthy eating automatic, not stressful.

You won't find calorie counting or deprivation here—you'll find a system that works.

📋 YOUR NEXT STEPS

1. Read the Carb Cycling Guide and identify which protocol fits your schedule
2. Prep your first 3 days of meals using the Meal Prep Framework
3. Download the Tracking Sheet (optional, but recommended for first 2 weeks)
4. Stock your pantry with the approved ingredient list

CONGRATULATIONS

You now have the complete Health is Wealth system: a mindset foundation, a body transformation
protocol, and a sustainable nutrition strategy. These aren't separate pieces—they're integrated.

Over the next 6 weeks, check in with your Success Manual when you feel stuck. Reference your
Purpose Worksheet when motivation dips. Trust the process.

The results are coming.

With conviction,
{{team.signature}}

P.S. You have access to our private community forum for accountability and support. Post your wins,
ask questions, and celebrate others' progress. [Link to forum]
```

**SMS (Day 21):**
```
🥗 Nutrition isn't complicated—it's just intentional. Your Carb Cycling Guide + Meal Prep Framework
are ready. Start prepping: [Link]
```

---

## Sequence Type: Monthly Educational Campaign (12-Month Example)

### Use Case
Ongoing engagement automation for customers to stay connected, learn new concepts, and prevent churn.

### Strategy
One email + one SMS per month covering complementary wellness topics. Email is detailed/educational.
SMS is brief summary + curiosity driver. Designed to run 12 months post-purchase.

### Template Framework (Repeating Monthly)

**Email Template Structure:**
```
Subject: [EMOJI] [Month Theme] — [Specific Benefit/Outcome]

Hello {{contact.name}},

[Brief context: Why this topic matters right now in the journey]

1. **[Key Concept 1]** [EMOJI]: [Explanation + benefit]
2. **[Key Concept 2]** [EMOJI]: [How-to / application]
3. **[Action Hack]** [EMOJI]: [Specific, doable action they can take this week]

[Deeper exploration / resource link]

[Community invitation or challenge]

Stay Healthy,
{{team.signature}}

[P.S. / Bonus tip]
```

**SMS Template Structure:**
```
[EMOJI] [Month Theme]: [1-line core concept]. [1-line action]. Learn more at [link] [EMOJI]
```

### Month-by-Month Content Calendar

#### Month 1: Hydration
**Email Subject:** 💦 Hydration: Unlock the Fountain of Youth and Vitality

**Email Body:**
```
Hello {{contact.name}},

This month, we're diving into the essential elixir of life: Water!

1. **Why Hydration Matters** 💦: Staying hydrated helps with energy levels, skin health,
digestion, and overall performance. Most people mistake thirst for hunger—or miss critical
hydration windows entirely.

2. **How Much to Drink?** 📊: General advice is the 8x8 rule—eight 8-ounce glasses per day—
but it varies depending on your activity level and individual needs. A better approach: drink
half your body weight (in ounces) daily, plus 16 oz per 30 minutes of exercise.

3. **Hydration Hacks** 🚀:
   - **Flavor Your Water**: Add a splash of lemon, cucumber, or mint (without added sugar)
   - **Use a Tracker**: Apps or water bottles with time markers keep you accountable
   - **Pair Hydration with Habits**: Drink water when you wake, before meals, and after workouts
   - **Listen to Your Body**: Thirst is a late signal—aim to stay ahead of it

Challenge: This week, experiment with one of these hacks and notice how you feel.
More energy? Better focus? Clearer skin? Report back in our community forum.

Quench your thirst for knowledge on our [blog](link). Share your hydration wins on
[Instagram](link).

Stay Hydrated,
Anthony Bradley
Elite Health Nutrition

P.S. Pro tip: Infuse your water the night before. You'll actually drink it because it tastes good.
```

**SMS:**
```
💦 Drink up for health & vitality! Aim for half your body weight (oz) per day.
Try lemon-infused water or use a tracker app. Learn more: [link]
```

---

#### Month 2: Sleep & Recovery
**Email Subject:** 😴 Master Sleep — Your Secret Weapon for Fitness & Health

**Email Body:**
```
Hello {{contact.name}},

You can't out-supplement poor sleep. This month, we're fixing your recovery foundation.

1. **Sleep's Impact on Fitness** 🏋️: Your muscles don't grow in the gym—they grow during sleep.
Growth hormone peaks during deep sleep. Poor sleep disrupts testosterone, cortisol, and hunger
hormones. One bad night affects your next 72 hours.

2. **The Sleep Science Basics** 🔬:
   - Aim for 7-9 hours nightly (consistency matters more than total hours)
   - Sleep in 90-minute cycles—aim for 4-6 complete cycles
   - Deep sleep (stage 3) is when repair happens—you need 20-30% of total sleep as deep sleep

3. **Sleep Hacks** 😴:
   - **Consistent Bedtime**: Go to bed + wake up at the same time (even weekends)
   - **Cool Dark Room**: 65-68°F (18-20°C) is optimal
   - **No Screens 1 Hour Before Bed**: Blue light disrupts melatonin
   - **Limit Caffeine After 2pm**: It has a 6-hour half-life
   - **Evening Routine**: 30 minutes of wind-down signals your body it's sleep time

Challenge: Pick ONE sleep hack this week. Track your sleep quality (mental clarity, energy)
versus your baseline.

Share your sleep wins in our community.

Rest Well,
Anthony Bradley

P.S. If you're an early riser, adjust your bedtime—don't sacrifice hours. Consistency > wake time.
```

**SMS:**
```
😴 Sleep = muscle growth. Aim for 7-9 hours nightly, consistent times, cool dark room.
Your workouts depend on your recovery. Track it: [link]
```

---

#### Month 3: Progressive Overload
**Email Subject:** 💪 Elevate Muscle Growth with Progressive Overload — The Science Behind Gains

**Email Body:**
```
Hello {{contact.name}},

Muscles adapt. Do the same workout at the same weight forever? You plateau. This month's topic:
how to keep progressing.

1. **What is Progressive Overload?** 🎯: Gradually increasing stress on your muscles through
added weight, more reps, shorter rest periods, or increased volume. Your body adapts—then you
push again.

2. **Why It Matters** 📈: Without progressive overload, you maintain fitness but don't build it.
This is why some people look the same after a year of training—they're not progressing.

3. **Progressive Overload Methods** 🚀:
   - **Add Weight**: Increase dumbbells by 5-10 lbs when you hit target reps
   - **Add Reps**: If you did 10 reps at 30 lbs, next week aim for 11-12
   - **Reduce Rest**: Shorten recovery between sets (builds endurance + metabolic stress)
   - **Increase Frequency**: Add an extra set to existing exercises
   - **Improve Form**: Deeper range of motion = more muscle recruitment

Challenge: Pick ONE exercise this week. Track the weight/reps/rest time. Next week, increase
one variable by 5-10%. Notice how your body responds.

The gains are in the progression, not the routine.

Progressive Mind,
Anthony Bradley

P.S. Strength gains come before muscle gains. Don't be frustrated if the scale doesn't move
while your lifts climb. You're building.
```

**SMS:**
```
💪 Plateau breaker: Progressive overload. Add weight, reps, or reduce rest. Your muscles
adapt—keep pushing. Track your progress: [link]
```

---

#### Months 4-12 (Brief Outline)
```
Month 4:  🥗 Carb Cycling — Optimize Energy & Results
Month 5:  🌱 Chia Seeds & Superfoods — Nutrient Density Decoded
Month 6:  🧬 Macro Tracking — Understanding Protein, Carbs, Fats
Month 7:  🧘 Mindfulness & Stress — The Cortisol Factor
Month 8:  🔥 HIIT Workouts — High Intensity Training Explained
Month 9:  🏃 Running & Cardio — Building Aerobic Capacity
Month 10: 💊 Supplements That Matter — Evidence-Based, No Hype
Month 11: 🎯 SMART Goal Setting — Structure for Sustained Progress
Month 12: 🎉 Celebrate & Reflect — Review Wins, Set New Targets
```

Each month follows the same structure: Why It Matters → How It Works → 3 Actionable Hacks → Email + SMS

---

## Sequence Type: Lead Qualification & Reoffer

### Use Case
Contact initially said no, or hasn't responded. Different versions based on their response pattern.

#### Reoffer V1: Initial Outreach (Same Offer, Different Angle)

**Email (Day 0):**
```
Subject: 👋 {{contact.firstName}}, Let's Find Your Perfect Program

Hello {{contact.name}},

I've been thinking about our conversation and realized you might be overthinking this.

The truth is: you don't need the most expensive program to get results. You need the *right*
program for your current situation. That's exactly what we've built here.

We have three options:
- **10-Day Total Detox** ($97) — Quick reset, see how you feel
- **28-Day Kickstart** ($297) — Build momentum, real results
- **6-Week Health is Wealth** ($597) — The complete transformation system

All three work. All three deliver. The question is: what fits your life right now?

When I work with clients who are on the fence, I always ask: "What would it take to know this
is right for you?" That's what I want to know.

What's holding you back? Budget? Time? Not sure it'll work? Let's talk about it.

Book a time here: [Calendar Link]

Or just reply to this email. I read every message personally.

You deserve to feel your best. Let's get you there.

- Anthony

P.S. The longer you wait, the longer until you feel the results. What's stopping you?
```

**SMS (Day 3):**
```
Hey {{contact.firstName}}, it's Anthony! 🙌 I've been thinking about our chat and crafted something
special for you. Let's talk about an offer tailored to your goals. Book a time here: [link].
Excited to catch up! 💪
```

---

#### Reoffer V2: Health-Focused Angle (14 Days After First Offer)

**Email (Day 14):**
```
Subject: ❤️ {{contact.firstName}}, Your Health is Worth the Investment

Hello {{contact.name}},

I trust this email finds you well!

I've been reflecting on a lot of conversations I have with clients, and a theme keeps coming up:
"I wish I'd started sooner." Not about money. About time. About their health.

Here's the reality: You can't buy time. But you *can* invest in feeling better *right now*.

Every day you wait is a day you're not:
- Waking up with energy
- Feeling confident in your body
- Moving without pain
- Showing up fully for your family and business

I built these programs because I watched too many people put their health last.

Your health isn't a luxury item. It's the foundation for everything else.

What if we started with just 10 days? See how you feel. Get a win. Then decide what's next.

10-Day Total Detox → $97 → Real Results

Book a time to chat: [Calendar Link]

The best time to plant a tree was 20 years ago. The second best time is now.

Let's get you started,
Anthony

P.S. I'm serious about this. Reply if you have questions. No sales pitch—just conversation.
```

**SMS (Day 17):**
```
Hey {{contact.firstName}}, 🌻 I've been thinking about your wellness journey and designed an offer
just for you. Small investment, big results. Book here: [link]
```

---

#### Reoffer V3: Social Proof / Results Angle (90 Days After First Offer)

**Email (Day 90):**
```
Subject: 🎯 {{contact.firstName}} — See What Your Peers Accomplished in 6 Weeks

Hello {{contact.name}},

I wanted to reach out because I've seen some incredible transformations in the last quarter,
and I kept thinking about you.

Here's what's happened:

- **Sarah** (49, busy mom): Lost 14 lbs, sleeps better, runs a half-marathon next month.
  Started with the 10-day detox just to "try it."

- **Mike** (42, entrepreneur): Cut his morning coffee from 4 cups to 1. Energy is through the roof.
  Says it's changed how he shows up in his business.

- **James** (38, desk job): Fit back into clothes from college. His kids asked why he "looks
  different." That's when he knew it was working.

These aren't gym rats or health influencers. They're regular people who decided their health
mattered enough to start.

Most started with doubts. All ended with results they didn't expect.

This could be you.

Here's what I suggest: Start with the 10-Day Total Detox. Prove to yourself it works. Then
decide what's next. The 6-week program will still be there, but you'll join it as a believer,
not a skeptic.

Ready? Book here: [Calendar Link]

You're closer than you think,
Anthony

P.S. The only thing better than starting 90 days ago is starting today.
```

**SMS (Day 93):**
```
🎯 Real people, real results. Check out what your peers accomplished: [results link].
Ready to be next? Start here: [link]
```

---

## Sequence Type: Non-Responder / Re-engagement

### Use Case
Contact received offer but never responded. Escalate urgency.

#### Email 1 (Day 3 - Check-in):
```
Subject: ❓ {{contact.firstName}}, Are You Still Interested?

Hi {{contact.name}},

I sent an email a few days ago and haven't heard back. I know you're busy—most people are.

I just wanted to check in and make sure you got it. (Sometimes emails end up in spam—it happens.)

Here's the quick version: We've built a program to help people like you feel better without
taking over your life. Three options to fit your situation.

Still interested? Reply to this email or book a time: [Calendar Link]

If now's not the right time, that's okay too. Just let me know so I'm not sending you stuff
you don't want.

- Anthony
```

#### SMS (Day 5 - Push):
```
Hey {{contact.firstName}}, just checking in! Let's find the right program for you to kickstart
your fitness journey. 💪🏼 - **Anthony** [Link]
```

#### Email 2 (Day 10 - Urgency):
```
Subject: ⏰ {{contact.firstName}}, Don't Let This Slip Away

Hi {{contact.name}},

Quick reality check: {{contact.firstName}}, don't let your fitness goals slip away.

Every day you delay is a day you could've felt better, had more energy, or moved without pain.

I get it—life is busy. But that's exactly why these programs exist: to fit *into* your life,
not require you to overhaul it.

One 10-day program. See how you feel. Then decide.

Ready? [Calendar Link] or reply to this.

Let's go,
Anthony

P.S. This special offer expires soon. Don't regret waiting.
```

---

## Personalization Tips

### Dynamic Fields to Always Include
- `{{contact.firstName}}` — Use first name only in casual contexts
- `{{contact.name}}` — Use full name in formal openings
- `{{contact.goal}}` — If captured, reference their stated goal
- `{{contact.painPoint}}` — If known, address directly
- `{{team.signature}}` — Consistent signing (Anthony, team name, etc.)

### Tone Adjustments
**For Fitness/Health Brands:** Inspirational, actionable, results-focused
**For B2B/Services:** Professional, ROI-focused, case study-heavy
**For Lifestyle/Community:** Warm, relatable, inclusive

### A/B Testing
Test subject lines, send times, CTA buttons. Document results. Implement winners.

---

## Related Notes
- [[GHL Automation Setup]]
- [[CRM and GHL Workflow]]
- [[Veronica AI Assistant]]
- [[AI Systems — ChatGPT Extract]]
