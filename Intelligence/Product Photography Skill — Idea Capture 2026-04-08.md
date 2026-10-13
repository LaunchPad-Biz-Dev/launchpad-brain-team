---
title: "Product Photography Skill — Idea Capture"
type: intelligence
status: active
tier: secondary
tags: []
last_updated: 2026-04-08
related: ["[[Intelligence/00-INDEX]]"]
---

# Product Photography Skill — Idea Capture
**Date:** 2026-04-08
**Source:** Anthony Mendoza via Apollo Slack DM
**Category:** New Skill / Agent Concept

---

## The Idea

Build an AI-powered product photography skill that handles everything from brand research to image generation — creating lifestyle shots, studio shots, and consistent product imagery without needing a physical shoot every time.

**Anthony's exact message (voice-to-text):**
> "I think creating a skill for product photography like lifestyle and staged shots would be amazing. If we could have a researcher tool scrape website and the brain for all the info and feed it brand guideline books and brand kits, then scrape the site for all the images of the product and create a folder for them. Then we can set up the prompt for the actual 'photo shoot' or shots of the products. It can be lifestyle with a model, studio shots of just product alone. We can talk angles, models, lighting, inside or outside, give info on the location etc. then save the info for consistency. But context here is the key. So there would have to be almost an interview process at first where when we set this up. The skill or agent begins to ask a lot of questions so that we get the best output possible. Earlier this week I sent in a lot of prompts or styles and we did research on how to get the best outputs I think we need to incorporate some of that into this."

---

## Skill Architecture

### Phase 1: Brand + Product Research
- Scrape client website for existing product images — build a reference folder
- Pull brand guidelines from Brain (colors, fonts, tone, visual style)
- Feed brand kit into the generation context

### Phase 2: Interview Process (Context Gathering)
The skill begins with a structured intake interview — asking questions before generating anything:

**Product Questions:**
- What is the product? Dimensions, materials, colors, finish?
- What mood/feeling should the photo convey?
- What does the product currently look like in existing photos?

**Shot Type Questions:**
- Studio (white/neutral background, product alone)?
- Lifestyle (product in use, with model)?
- Flat lay / overhead?
- Editorial (styled, artistic)?

**Scene Questions:**
- Indoor or outdoor?
- What environment? (kitchen, gym, beach, office, urban street, warehouse)
- Time of day / lighting? (golden hour, midday, studio strobe, soft natural)
- Props included? (complementary products, lifestyle items)

**Model Questions (if lifestyle):**
- Demographics of ideal model (age range, style, energy)
- Wardrobe direction
- Model interaction with product (holding, wearing, using, nearby)?

**Consistency Requirements:**
- Will this be a recurring campaign? (saves settings for future runs)
- Brand color dominance in the scene?
- Reference images from client or competitors to match vibe?

### Phase 3: Session Setup (Saved Context)
After the interview, save a "photo session brief" document for the client — locked settings that ensure all future generations match. This is the consistency layer.

### Phase 4: Image Generation
- Use Nano Banana (Gemini 3.1 Flash Image / MCP: nanobanana) for generation
- Generate multiple variants per shot type
- Organize outputs into a labeled folder: `creative/{client}/product-photography/{session-date}/`

---

## Connections to Existing Work
- [[Nano Banana Setup]] — image gen tool already connected via MCP
- We did prompt research earlier this week on getting best AI photo outputs — find those prompts and incorporate
- Anthony is a photographer/videographer — this skill should complement real shoots, not just replace them
- [[Brand With Us]] — BWU (print goods) is a natural first test client for this

---

## Research Needed
- Anthony mentioned "earlier this week I sent in a lot of prompts or styles and we did research on how to get the best outputs" — find those prompts in previous conversations or Brain notes and attach here
- Research: Nano Banana's best prompt structure for product photography
- Research: Google Antigravity (separate note — Anthony wants to learn what this is and how it works)

---

## Next Steps (When Ready)
- [ ] Find the prompt research Anthony referenced and capture it here
- [ ] Build the intake interview script (Phase 2 above)
- [ ] Test with BWU product images as first run
- [ ] Build the skill file at `marketing/skills/product-photography.md`
- [ ] Scope whether this is a skill or a full agent (lean: skill first, upgrade to agent if complex enough)
