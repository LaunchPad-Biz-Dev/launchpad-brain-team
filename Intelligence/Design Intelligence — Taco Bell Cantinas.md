---
title: "Design Intelligence — Taco Bell Cantinas"
type: intelligence
status: active
tier: secondary
tags: []
last_updated: 2026-04-11
related: ["[[Intelligence/00-INDEX]]"]
---

# Design Intelligence — Taco Bell Cantinas

> **Client:** Taco Bell Cantina (@tacobellcantinas)
> **Created:** 2026-04-11
> **Purpose:** Cross-agent design knowledge. Records style decisions, iteration history, and rules learned through design sessions.

---

## Current Approved Visual System (v2 — April 2026)

**Core Principle:** Photo is the HERO. Text ENHANCES, never competes.

- Text-to-photo ratio: 15-25% text / 75-85% photo
- Typography: Bold condensed sans-serif, all caps, white on dark, 48-68pt headlines
- Text placement: Negative space only — study each photo to find dark zones
- Logo: Small TBC lockup, bottom corner, white
- Photography: Real client photos only, warm/moody/nightlife color grading, flash aesthetic
- Format: 1080x1350px (4:5) for feed

**Caption style:** Wingstop-short (1-2 sentences), lowercase casual, zero brand speak.

---

## Iteration History

### 2026-04-10/11 — May Stills Development (4 rounds)

**Round 1 — REJECTED:** Canva AI generated generic template-style layouts. Purple gradient backgrounds, text floating in separate zone above photo, photo boxed in and small. Looked nothing like the brand.

**Round 2 — REJECTED:** Massive typography filling 60%+ of frame as background, subjects barely visible through the letters. NYC deli / MELTED burger / KFC Treats style. Anthony initially requested this direction based on Pinterest references, but the execution was too text-heavy for TBC's photo-first brand.

**Round 3 — REJECTED (partially):** Overcorrected — text became too subtle, tiny and tucked in corners. Photo was hero but text disappeared. The iMessage format concept was the closest to the sweet spot.

**Round 4 — APPROVED:** Found the middle ground. Photo fills the frame, text at 20-25% occupying negative space, stacked typography with hero word creates hierarchy without overwhelming. Apple Music widget overlay added cultural context. Prompt used real client photo as input with specific text placement based on photo composition analysis.

**Key Learning:** The agent must READ the actual photo and identify natural negative space before deciding text placement. Generic placement rules (always lower third, always centered) don't work — each photo has different dark zones.

---

## Style Rules (Stabilized)

These rules have been tested across multiple iterations and are considered stable:

1. Real client photos only — never AI-generated restaurant/food images
2. Text in negative space of actual photo composition
3. 15-25% text ratio (below 15% = too subtle, above 30% = too overwhelming)
4. Bold condensed sans-serif, all caps, white, 48-68pt
5. No gradient backgrounds, no template layouts, no text floating in separate zones
6. Caption style: 1-2 sentences, lowercase, casual, zero brand speak
7. Dark/nightlife aesthetic for 80%+ of content

## Style Rules (Still Evolving)

These need more data points:

1. Stacked typography with hero word — approved once but needs more testing
2. Native UI formats (iMessage, Apple Music) — approved once, very creative, needs more data
3. Annotated/diagram humor — referenced but not yet executed for TBC

---

## Prompt Engineering Notes

- Nano Banana nb2 + thinking_level high produces the best results
- Using real photos as `input_image_path_1` is critical — don't generate base photography
- File paths with spaces break Nano Banana — use staging folder with clean filenames
- Describe text placement RELATIVE to the specific photo's composition, not generically
- "Editorial social media graphic" is a reliable format anchor in prompts

---

## Key Resources

- **Style Guide:** `~/launchpad-automation/marketing/output/creative/taco-bell-cantina/style-guide.md`
- **Design Finals:** Google Drive > Taco Bell Cantina > Graphic Design > {Month} 
- **Photo Library:** Google Drive folder `1o2jC826LnRxOmtL98uJaZpvJzsJynFYO` (March Grad 2026)
- **Canva Reference File:** Design ID `DAGp_lLPDMU` (207 pages, master working file)
- **Canva Brand Kit:** `kAGvVSRwU_4`
- **Brain Note:** `Projects/Taco Bell Cantinas.md`
- **Notion Portal:** https://www.notion.so/1f1b01f77d6d806e9965ee69d21956ec
- **Pinterest Board (Abril's):** https://www.pinterest.com/abrilr0867/tbc/

---

*Related: [[Taco Bell Cantinas]] . [[DRG]]*
