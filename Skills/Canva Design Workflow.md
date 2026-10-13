---
title: "Canva Design Workflow"
type: skill
status: active
tier: secondary
tags: []
last_updated: 2026-04-03
related: ["[[Skills/00-INDEX]]"]
---

# Canva Design Workflow

This skill documents how Launchpad uses Canva and how AI agents can interact with it to support the design team.

---

## Overview

Canva is one of Launchpad's primary design tools alongside Adobe Creative Suite and CapCut. The team uses it for social media graphics, presentations, client deliverables, and quick-turn design work. The Canva MCP connector gives AI agents direct access to search, create, edit, export, and manage designs programmatically.

---

## Who Uses Canva

- [[Arija Imendia]] — Graphic Designer (primary Canva user for client graphics)
- [[David Canizalez]] — Graphic Designer (primary Canva user for client graphics)
- [[Cynthia Hernandez]] — Social Media Manager / Art Director (creates and schedules social content)
- [[Abril Rodriguez]] — Creative Director (reviews designs, provides feedback)
- [[Anthony Mendoza]] — CEO (presentations, proposals, pitch decks)

---

## What Canva Is Used For

- Social media post graphics (Instagram, Facebook, TikTok, LinkedIn)
- Story and Reel cover designs
- Client presentations and pitch decks
- Flyers, posters, and event materials
- Infographics and data visuals
- BrandWithUs print-ready designs (postcards, business cards)
- Internal documents and proposals
- Ad creatives for Meta, TikTok, Google campaigns

---

## Available AI Capabilities

### Search & Browse
- **search-designs**: Find existing designs by keyword — useful for locating client assets, past work, or templates
- **list-folder-items**: Browse Canva folder structure to find organized client files
- **list-brand-kits**: View available brand kits for on-brand design generation

### Create & Generate
- **generate-design**: AI-generate new designs (social posts, flyers, docs, reports, presentations, etc.)
- **generate-design-structured**: Create presentations from a reviewed outline (use after request-outline-review)
- **create-design-from-candidate**: Convert an AI-generated candidate into an editable Canva design
- **import-design-from-url**: Import external files (PDFs, images) as new Canva designs

### Read & Review
- **get-design**: Get design metadata (owner, title, URLs, thumbnail, dates, page count)
- **get-design-content**: Read text content from docs, presentations, social posts
- **get-design-pages**: List pages in a multi-page design with thumbnails
- **get-design-thumbnail**: Preview specific pages during editing
- **get-presenter-notes**: Read speaker notes from presentations
- **get-export-formats**: Check which export formats a design supports

### Edit
- **start-editing-transaction**: Begin an editing session on a design
- **perform-editing-operations**: Make changes (text edits, media replacement, formatting)
- **commit-editing-transaction**: Save all changes from the editing session
- **cancel-editing-transaction**: Discard changes without saving

### Export & Share
- **export-design**: Export designs as PDF, PNG, JPG, GIF, PPTX, or MP4
- **resize-design**: Resize designs to different formats (e.g., Instagram post → Story)

### Collaborate
- **comment-on-design**: Leave feedback comments on designs
- **list-comments**: View all comments on a design
- **list-replies**: View replies to a specific comment
- **reply-to-comment**: Respond to existing comments

### Organize
- **create-folder**: Create new folders in Canva
- **move-item-to-folder**: Organize designs into folders
- **search-folders**: Find folders by name
- **upload-asset-from-url**: Upload images/assets to Canva from URLs

---

## Workflow: Creating a Client Design

1. **Check brand kit**: Use `list-brand-kits` to find the client's brand kit (if one exists in Canva)
2. **Reference Brain**: Read the client's project note in [[Projects]] for brand guidelines, colors, fonts, tone
3. **Generate design**: Use `generate-design` with the brand kit ID and detailed query including client brand context
4. **Review candidates**: Present generated options — ask which to proceed with
5. **Create from candidate**: Use `create-design-from-candidate` to make it editable
6. **Edit if needed**: Start an editing transaction to refine text, swap images, adjust content
7. **Get approval**: Share thumbnail previews for internal review ([[Abril Rodriguez]] reviews all content)
8. **Export**: Export in the required format for the platform (PNG for social, PDF for print, PPTX for presentations)

---

## Workflow: Editing an Existing Design

1. **Find the design**: Use `search-designs` with keywords or `list-folder-items` to browse
2. **Start editing**: Call `start-editing-transaction` with the design ID
3. **Review current content**: The transaction response includes current content and thumbnails
4. **Make edits**: Use `perform-editing-operations` for text changes, media swaps, formatting
5. **Preview**: Use `get-design-thumbnail` to verify changes look correct
6. **Commit or cancel**: Save with `commit-editing-transaction` or discard with `cancel-editing-transaction`

---

## Workflow: Exporting for Delivery

1. **Check formats**: Use `get-export-formats` to see what's available for the design
2. **Export**: Use `export-design` with the right format:
   - Social media → PNG (1080x1080 for feed, 1080x1920 for stories)
   - Print materials → PDF (high quality)
   - Presentations → PPTX or PDF
   - Video content → MP4
   - Ad creatives → PNG or JPG
3. **Share link**: Provide the download URL to the team or client

---

## Integration with Content Cycle

Canva work maps to the [[Weekly and Monthly Cycles]]:

- **Week 1 (Report + Create)**: Create content calendars and creative briefs — may generate initial design concepts in Canva
- **Week 2 (Produce)**: Primary design production — [[Arija Imendia]] and [[David Canizalez]] create graphics in Canva from briefs
- **Week 3 (Review)**: [[Abril Rodriguez]] and [[Cynthia Hernandez]] review designs — comments and revision requests happen here
- **Week 4 (Schedule + Deliver)**: Final exports from Canva, assets delivered to clients or scheduled via Sprout Social

---

## Tips for AI Agents

- Always check if a client has a Canva brand kit before generating designs — on-brand output requires less revision
- When generating designs, include as much context as possible in the query: brand colors, tone, target audience, platform dimensions
- For presentations, use the `request-outline-review` → `generate-design-structured` flow for better results
- Never commit editing transactions without confirming with the user first
- When searching for designs, try the client name as a keyword first
- Export at the highest quality available unless file size is a concern
- Link exported assets back to the relevant client project note in the Brain

---

*Created 2026-04-03*
*Canva MCP connected — all tools verified available*
