---
title: "Client Delivery Portal"
type: project
status: idea
tier: secondary
tags: [productions, product-idea, delivery, callsheet]
last_updated: 2026-08-12
related: ["[[Projects/00-INDEX]]", "[[Callsheet System]]", "[[Skills/Callsheet Generation]]", "[[Launchpad Productions]]"]
---

# Client Delivery Portal

## Status
**Idea — captured 2026-08-12.** Not scoped, not scheduled. Raised by Anthony while building the
TBC Allegiant callsheet.

## The idea
A hosted Launchpad site where production callsheets live as real web pages — one per shoot, per
client. Clickable and shareable the way the current HTML artifacts are, but owned by us at a
Launchpad URL instead of being loose files.

The part that makes it a product rather than a file cabinet: **after the shoot, the Pic-Time
gallery gets embedded into the same page.** The brief and the delivery become one continuous
artifact the client keeps.

## Why it matters
Right now a shoot produces three disconnected things — a brief somewhere, a gallery link in an
email, and an invoice. The client experiences them as separate admin. One persistent page per shoot
turns that into a single thing they can return to, forward internally, and associate with Launchpad
rather than with a file transfer service.

It also compounds: every past shoot becomes a live portfolio entry we already built as a byproduct
of doing the work.

## What exists today
- [[Callsheet System]] — working HTML templates (photo + video), a build script that inlines images
  for offline use, and one shipped example (TBC Allegiant, 2026-08-13)
- Pages currently publish as Claude Artifacts, which are private-by-default and awkward to share
  with people outside a Claude account — the main reason to move to our own hosting

## Open questions
- Host where? Static site, or a page type inside the existing Launchpad site?
- Auth: public unlisted URLs, or per-client login? Unlisted is probably enough and far cheaper.
- Does Pic-Time support iframe embedding on a custom domain, or does this need their API?
- Does the checklist stay per-device, or does a shared production view become worth building?
- Who maintains it — is this an Iker build?

## Next step if picked up
Scope the smallest version: one static page per shoot at a Launchpad URL, manually published from
the existing build script, with a Pic-Time embed slot. Prove the client reaction before building
any auth or CMS.

---

*Related: [[Callsheet System]] · [[Skills/Callsheet Generation]] · [[Launchpad Productions]] · [[Content Workflow — Shoot to Post]]*

<!-- Sections below added 2026-10-19 per [[Client Note Schema]]; the nightly filing writes here. Dated, append-only. -->

## Preferences & Corrections

## Decisions

## Activity Log

## Open Items
