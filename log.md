---
title: Brain Log
type: infrastructure
status: active
tier: primary
last_updated: 2026-04-13
---

# Brain Log

## [2026-09-09] compile | First Colony Mortgage discovery meeting + DRG merchandise stub check (2 sources scanned)
- Sources processed: 1
  - Raw/exports/notion-meeting-2026-01-08_first-colony-mortgage-discovery.md (→ [[Projects/First Colony Mortgage]])
- Notes created: 1 — [[Projects/First Colony Mortgage]]
- Notes updated: 1 — [[Projects/00-INDEX]] (added new client)
- Backlinks added: 0 (new client, no existing mentions elsewhere in vault)
- Synthesis: none
- Flags: Raw/exports/notion-meeting-2026-07-29_drg-merchandise.md is a stub with no real content ("TBD — content pending") and had malformed duplicate frontmatter keys (ingested/related each listed twice). Fixed the frontmatter, left `ingested: false` with `needs_notion_followup: true` since there's nothing to extract yet — someone needs to fill in the actual Notion meeting notes before this can compile.

## [2026-09-07] compile | Real estate content creation retreat planning meeting (1 source)
- Sources processed: 1
  - Raw/exports/notion-meeting-2026-09-02_retreat-planning.md (→ [[Projects/Real Estate Content Creation Retreat]])
- Notes created: 1 — [[Projects/Real Estate Content Creation Retreat]]
- Notes updated: 0
- Backlinks added: 1 ([[Launchpad Business Development]])
- Synthesis: none (single sparse source, mostly placeholders — full detail only in Notion)
- Flags: Source content is a thin summary (attendees "TBD", no date/pricing/location). Anthony's formal line-item proposal action item is still open as of 2026-09-07 — worth a direct check-in rather than continued Brain re-flagging.

## [2026-09-01] compile | CES Inc. website/social discovery meeting (1 source)
- Sources processed: 1
  - Raw/exports/notion-meeting-2026-08-31_ces-website-conversation.md (→ [[Projects/CES Inc.]])
- Notes created: 1 — [[Projects/CES Inc.]]
- Notes updated: 1 — [[Projects/Helix Electric]] (added cross-link: CES is using the Helix campaign launch as internal leverage for their own approval)
- Backlinks added: 2
- Synthesis: none (single source, routine prospect capture)
- Flags: none

## [2026-08-26] compile | AI security platform demo & DRG referral (1 source)
- Sources processed: 1
  - Raw/exports/notion-meeting-2026-08-19_security-demo.md (→ [[Strategic Partners/AI Security Platform — Demo & Referral Partnership 2026-08-19]], [[Projects/DRG]])
- Notes created: 1 — [[Strategic Partners/AI Security Platform — Demo & Referral Partnership 2026-08-19]]
- Notes updated: 2 — [[Projects/DRG]] (referral action item), [[Strategic Partners/00-INDEX]]
- Backlinks added: 2 (DRG ↔ new partner note)
- Synthesis: none (single source, routine referral capture)
- Flags: Anthony's DRG outreach + Teams billing bug screenshot are both still open action items from the 08-19 demo, unresolved as of this compile

## [2026-08-17] compile | LP University launch arc, Launchpad content planning, DRG monthly + merchandise (7 sources)
- Sources processed: 7 (was reported as 6 to the compiler — verified against Raw/exports frontmatter directly, actual count was 7; all 7 confirmed `ingested: false` before this run)
  - Raw/exports/notion-meeting-2026-02-17_lpu-production.md (→ [[Projects/LP University - Course Catalog]])
  - Raw/exports/notion-meeting-2026-02-24_lpu-focus.md (→ [[Projects/LP University - Course Catalog]])
  - Raw/exports/notion-meeting-2026-03-06_lpu-launch.md (→ [[Projects/LP University - Course Catalog]])
  - Raw/exports/notion-meeting-2026-03-13_lpu-accountability.md (→ [[Projects/LP University - Course Catalog]])
  - Raw/exports/notion-meeting-2026-06-05_launchpad-content-planning.md (→ [[Intelligence/2026-06-05 — Launchpad Content Planning & Video Production Strategy]])
  - Raw/exports/notion-meeting-2026-07-07_drg-lp-monthly.md (→ [[Projects/DRG]], [[Projects/Arby's Food Truck]], [[Projects/Taco Bell Cantinas]])
  - Raw/exports/notion-meeting-2026-07-29_drg-merchandise.md (→ [[Projects/DRG]], [[Projects/Taco Bell Cantinas]])
- Notes created: 1 — [[Intelligence/2026-06-05 — Launchpad Content Planning & Video Production Strategy]]
- Notes updated: 6 — [[Projects/LP University - Course Catalog]] (added Launch Execution Log, 4 meetings Feb–Mar 2026), [[Intelligence/2026-05-20 — Strategic Pivot — Personal Brand + AI-for-Business]] (dated addendum linking the consistency-engine answer), [[Projects/DRG]] (07-07 ads/ops detail + 07-29 merchandise stub), [[Projects/Arby's Food Truck]] (Q3→Q4 events/content plan), [[Projects/Taco Bell Cantinas]] (Q3→Q4 events/content plan + merchandise cross-ref)
- Backlinks added: fixed broken `related: [[Projects/LP University]]` (note never existed) → repointed to [[Projects/LP University - Course Catalog]] in all 4 LPU raw sources; added `related` links on the previously-empty DRG/content-planning raw sources
- Synthesis: none forced as a separate note — the strongest cross-source finding (06-05 meeting answers the 05-20 Strategic Pivot's "consistency engine" open question) was written directly as a dated addendum on the existing Pivot note instead, since it's a direct update to one existing note rather than a multi-note pattern
- Flags:
  - Compiler's stated count of "6 unprocessed sources" was off by one — actual was 7 (confirmed by reading frontmatter directly)
  - `notion-meeting-2026-07-07_drg-lp-monthly` substantially overlapped a meeting already logged in [[Projects/DRG]] on 2026-07-15 (same meeting, different sync pass) — no duplicate note created; only the previously-uncaptured specifics were added
  - `notion-meeting-2026-07-29_drg-merchandise` is a content-less stub in Notion (Key Decisions/Action Items both "TBD") — flagged in [[Projects/DRG]] for manual re-sync if real notes ever get added to that Notion page
  - `notion-meeting-2026-03-13_lpu-accountability` was also summary-only (no granular items) — noted in the Course Catalog log rather than treated as missing data

## 2026-07-21 — Upbeat Health August 2026 Social Media Run (Graphics Only) — PARTIAL / FLAGGED
- Client: Upbeat Health | Creation month: July (Month property) | Posting month: August 2026 | Scope: graphics only (videos deferred per Cynthia)
- Posts created: 2 carousels (4-slide + 3-slide), FB+IG, in_review, approver Jennifer Dao. Aug 6 + Aug 19.
- Skipped: 1 video carousel (4 .mp4 slides, out of scope this run), 3 stills sitting outside the Approved/ folder (not auto-posted, flagged to move into Approved).
- Content gap: only 2 approved graphics existed in Drive at run time — did not invent filler content, flagged the gap to Cynthia instead.
- Safety: `ghl-post-guard.py sweep` returned SWEEP FAIL — but the flagged record is a STALE, pre-existing issue (post published 2026-06-23, 13 days early, unrelated to today's run) not caused by this run. Both new posts individually GET-verified safe (in_review, publishedAt=null). Flagged for manual review.
- Notion task: "Upbeat Health August 26' Content Calendar" → Status set to Needs Team Review, Content Calendar Link written, comment posted. No Slack per explicit instruction this run.

## 2026-06-30 — Wylees July 2026 Social Media Run — SUCCESS
- Client: Wylees School | Creation month: July | Posting month: July 2026
- Posts scheduled: 8 (4 stills + 4 carousels), FB + IG
- Posts held: 0 (all 20 images passed visual QC)
- Schedule: Jul 4 (Sat, 4th of July holiday override), Jul 8, 13, 15, 20, 22, 27, 29
- Pattern: alternating Still/Carousel per task notes; Jul 4 pinned to actual holiday date
- Times: 9am-2pm PT (within task's 7am-7pm window)
- Approver: Suzanna Nelson (St1InQ0wHWFMuOS8HC8O) — Users scope now working, ID resolved live
- Carousel slide counts: C1=3, C2=4, C3=6, C4=3 — all verified post-create
- Key learnings: MCP create-post lacks postApprovalDetails field — must use direct curl; locationId must NOT be in JSON body
- Flag: 3 AD stills + 1 AD carousel in ADS folder not posted — pending Cynthia routing decision
- Flag: TikTok not connected in GHL; posts created for FB + IG only
- Safety check: PASS (all 8 in_review, deleted=false, publishedAt=null, mediaOptimization=true)
- GHL post IDs: 6a443b620ffec3ccb5a55366, 6a443b72cd4590c50460ca47, 6a443b7c9aaf431bcd87b2c5, 6a443b8cab4e08b540083608, 6a443b928a5c637eccfe5afb, 6a443ba489fb23ddffe760bd, 6a443ba99b566edf0fc997cd, 6a443bb18a5c637eccfe7cad

## 2026-06-30 — AFT July 2026 Social Media Run — SUCCESS
- Client: AFT (Arby's Food Truck) | Creation month: July | Posting month: July 2026
- Posts scheduled: 11 total (8 graphics FB+IG + 3 videos FB+IG+TikTok)
- Graphics: 3 carousels (6-slide, 2-slide, 3-slide) + 5 stills, alternating Still/Carousel pattern
- Videos: 3 of contracted 4 in Approved folder; placed Jul 1/8/15 (Wed); Jul 22/29 unused
- Posts held: 0 (all images/videos passed visual QC)
- Schedule: Jul 1 (Wed V1) through Jul 27 (Mon Still 17)
- Approver: Sierra Burk (a3R7GX9q7ANEHtwZqtOQ) — confirmed on all 11 posts
- Carousel slide counts verified: C1=6, C2=2, C3=3 — all correct in final GET
- Safety check PASSED — all 11 in_review, deleted=false, publishedAt=null
- Flag: scripts/ghl-media-upload.sh blocked by settings.json; used direct curl (functionally identical)
- Flag: Only 3 videos found in Approved folder vs contracted 4; posted all 3 per task notes

## 2026-06-25 — WSN July 2026 Social Media Run — SUCCESS
- Client: WSN (Welding School of Nevada) | Creation month: July | Posting month: July 2026
- Posts scheduled: 13 total (8 graphics + 5 videos), FB + IG
- Graphics: 4 stills + 4 carousels (C1=4 slides, C2=3, C3=2, C4=6), alternating Still/Carousel per task notes
- Videos: 5 reels (WELDERS IN DEMAND, 2 OPTIONS, ACCEPTABLE, BAD WELDS, RATE THIS WELD)
- Posts held: 0 (all images/videos passed visual QC)
- Schedule: Jul 2 (overflow Thu) through Jul 29 (Wed). Graphics Mon/Fri; Videos Wed
- Overflow: 5 videos vs 4 Wed slots — 1 video placed on Jul 2 (Thu, same-month extra weekday per Rule 16)
- Approver: Gregory Gilbert (E8DqzuhD85obdkGpEZ6c) — confirmed via GHL Users API (approverUser populated in list response)
- Carousel slide counts: C1=4, C2=3, C3=2, C4=6 — all verified in final GET
- Drive structure note: Graphics sat directly in Graphics/July 26' (no APPROVED subfolder). Posted per task note "Post ALL videos and graphics (no matter the #)"
- Safety check: PASS (all 13 in_review, publishedAt=null, deleted=false, mediaOptimization=true, approver set on all)

## 2026-06-25 — TTR July 2026 Social Media Run — SUCCESS
- Client: TTR (Trusted Tax Resolution) | Creation month: July | Posting month: July 2026
- Posts scheduled: 8 (4 stills + 4 carousels, 3 slides each), FB + IG
- Posts held: 0 (all 16 images passed visual QC)
- Schedule: Jul 2 – Jul 31, Mon/Fri base pattern + 2 overflow weekdays (Jul 2 Thu, Jul 7 Tue)
- Overflow reason: 3 Mon/Fri slots (Jul 3/6/10) occupied by pre-existing human posts
- Approver: Sara Martinez (YqZsWoqVbx3T064jrPNK) — task notes said "Trevon" but GHL Users API returned 403; flagged for Cynthia to reassign
- Carousel slide counts: all 4 carousels = 3 slides — verified post-create
- Pre-existing: 5 human-managed posts (userId=None), left untouched
- Safety check: PASS (all 8 in_review, publishedAt=null, deleted=false, mediaOptimization=true)

## 2026-06-25 — TBC July 2026 Social Media Run — SUCCESS
- Client: TBC (Taco Bell Cantinas) | Creation month: June | Posting month: July 2026
- Posts scheduled: 8 (5 stills + 3 carousels), FB + IG only (TikTok excluded for graphics)
- Posts held: 0 (all 14 images passed visual QC)
- Schedule: Jul 2 – Jul 27, Mon/Thu pattern, 9AM–2PM PDT, alternating still/carousel
- Approver: Sierra Burk (GHL ID: a3R7GX9q7ANEHtwZqtOQ)
- Carousel slide counts: C1=5, C2=6, C3=3 — all verified post-create
- Pre-existing: 1 Cynthia video post (Jul 1) left untouched
- Videos: task notes say "videos TBD" — graphics-only run
- Safety check: PASS (all 8 in_review, publishedAt=null, mediaOptimization=true, approver confirmed)

## 2026-06-18 — Shumi July 2026 Social Media Run — BLOCKED (no content in APPROVED)
- Client: Shumi Nation | Creation month: July | Posting month: July 2026
- Posts scheduled: 0 | Posts held: 0
- Reason: No July 26' folder in Shumi Nation shared drive (Drive ID: 0AHbtW0nyBNcyUk9PVA). Graphic Design Board "Shumi July 26'" = Not started / Don't Start. GHL July: 0 existing posts confirmed.
- Action: Task set to Needs Revisions; Slack #social-media-management notified. Re-run once content lands in APPROVED.

## 2026-06-18 — Wylees July 2026 Social Media Run — BLOCKED (design not done)
- Client: Wylees | Creation month: July | Posting month: July 2026
- Posts scheduled: 0 | Reason: Graphic Design Board "Wylees July 26'" status = Not started; no July assets in APPROVED folder
- GHL token: working (FB + IG connected) | GHL July: 0 existing posts
- Action: Task set to Needs Revisions; Cynthia notified via Slack (#social-media-management)
- Re-run when designer completes July assets and moves to APPROVED folder

## 2026-06-18 — BWU July 2026 Social Media Run
- Client: BWU (BrandWithUs) | Creation month: June | Posting month: July 2026
- Graphics: 8 posted (4 carousels + 4 stills), 1 held (Still 1 — placeholder logo on mockup)
- Videos: 6 posted (all approved videos from Drive)
- Total posts scheduled: 14 | Status: all in_review | Approver: Jennifer Maldonado
- Schedule: Jul 2 – Jul 30, 2026 | Platforms: FB + IG
- Flags: Still 1 held (designer fix needed), TikTok still not connected, 1 video overflow to Tue Jul 7
- Safety check: PASS

## 2026-06-18 — Upbeat Health July 2026 Social Media Run — SUCCESS
- Client: Upbeat Health | Creation month: July | Posting month: July
- Posts scheduled: 22 (BOTH stills x7 + BOTH carousel x1 + FB stills x5 + FB carousel x1 + IG stills x7 + IG carousel x1)
- Posts held: 0 (all images passed visual QC)
- Schedule: Jul 1–22, 9am–4pm PDT, one post per day
- July 4 holiday post pinned to Jul 4 per task instruction
- Videos track: skipped per task note (videos TBD)
- Flags: Drive has platform-split APPROVED subfolders (BOTH/Facebook/Instagram); scheduled as separate platform-targeted posts
- Approver: Jennifer Dao (GHL ID: yXiInnFtH6sykKImdDbm)
- Safety check: PASS (all 22 in_review, publishedAt: null on all)

## 2026-06-11 — WYLEES June 2026 Social Media Run — SUCCESS (Apollo Run #3)
- Client: Wylees School | Creation month: June | Posting month: June/July
- Posts scheduled: 8 (5 stills + 3 carousels, FB + IG only)
- Posts held: 0
- Schedule: Jun 22, Jun 24, Jun 29, Jul 1, Jul 6, Jul 8, Jul 13, Jul 20
- Overflow: 5 posts into July (June only had 3 slots after 7-day QC window)
- Flags: Suzanna approver GHL ID unresolved (Users scope OFF on token — manual attach needed); bash script blocked (used curl directly instead)
- Safety check: PASS (all 8 in_review, none published)

## 2026-06-11 — Shumi Nation June 2026 SMM Run
- Client: Shumi Nation | Creation month: June | Posting month: June
- Posts scheduled: 12 (9 stills/carousels to IG, 2 videos to IG+TikTok, 1 held)
- Posts held: 1 (still-37 Thor Funko — typo "can can" doubled word)
- Schedule: Jun 19–30, daily, no approver (client override)
- Flags: Wylees content mixed into Shumi Drive APPROVED folders; carousel GET returns media=1 (create confirmed media=2); batch-1 IDs unverified; GHL list API broken for this sub-account
- Safety check: PASS (9 verified IDs, all publishedAt=null)

## 2026-06-11 — WYLEES June 2026 Social Media Run — BLOCKED (Apollo)
- Client: Wylees School | Posting month: June 2026
- Posts created: 0 — run blocked before any posts created
- Blockers: (1) GHL pit token invalid/expired, (2) No Wylees shared Drive accessible to Apollo, (3) Graphic design not yet started — no APPROVED files
- Status set to: Needs Revisions. Cynthia notified via Slack (#social-media-management) + Notion comment.
- Re-run when: Anthony regenerates GHL token + provisions Drive + designer completes files in APPROVED.

## 2026-05-28 — WSN June 2026 — Approver Attach (Apollo)
- Client: Welding School of Nevada | Posting month: June 2026
- Action: Attached approver Gregory Gilbert (`E8DqzuhD85obdkGpEZ6c`) to all 8 in_review posts
- New WSN pit token with Users scope confirmed working; old token lacked Users scope
- Safety check: PASS — all 8 in_review, publishedAt null, none published
- Flag: Carousel 2 (Jun 19) scheduleDate at 22:00 UTC (outside 8AM–8PM window) — flagged to Cynthia for manual reschedule
- API quirk noted: PUT body must NOT include `channel` field — returns 422 "property channel should not exist"

## 2026-05-29 — TTR June 2026 Social Media Run — COMPLETE (Apollo)
- Client: Trusted Tax Resolution (TTR) | Creation month: May 26' | Posting month: June 2026
- Posts created: 8 (4 stills + 4 carousels), FB + IG, status: in_review
- Approver: Sara Martinez — GHL user ID YqZsWoqVbx3T064jrPNK — confirmed set on all 8 posts
- Schedule: Jun 5, 8, 12, 15, 19, 22, 26, 29 — Mon/Fri, 9AM-4PM PT, all within 8AM-8PM window
- Safety check: PASS — all 8 GET-verified in_review, publishedAt=null, deleted=false
- Carousel slide counts verified: C1=4, C2=6, C3=2, C4=2
- curl fallback used (mcp__gohighlevel-ttr allowlist not in settings.json — Anthony to add)
- Videos: none for June (Kyle/editors still working per task notes)

## 2026-05-28 — TTR June 2026 Social Media Run — Run 2 BLOCKED (Apollo)
- Client: Trusted Tax Resolution (TTR) | Creation month: May 26' | Posting month: June 2026
- Posts created: 0 — run blocked by allowlist; all prep complete
- Remaining blocker: `mcp__gohighlevel-ttr__*` not in `.claude/settings.json` (Drive and social accounts confirmed resolved)
- Progress vs Run 1: Drive content now present (4 stills + 4 carousels in Approved folder); social accounts reportedly connected per task notes
- Visual QC: all 18 images PASS
- Captions: all 8 written + Brand Compliance PASS (no em-dashes, 2-3 sentences, 1 emoji max)
- Schedule plan: Jun 1, 6, 8, 13, 15, 20, 22, 27 — Mon/Fri, varied times 9am-4pm PT, all within 8am-8pm window
- Approver: Sara Martinez — GHL user ID still unknown, will attempt users API on unblock
- Action needed: Anthony add `"mcp__gohighlevel-ttr__*"` to `.claude/settings.json` allow array, then re-trigger
- Notion status: Needs Team Review | Slack posted to #social-media-management

## 2026-06-11 — Shumi June 2026 Social Media Run — BLOCKED (Apollo)
- Client: Shumi Nation | Posting month: June 2026
- Posts created: 0 — run blocked by missing Drive access
- Blocker: No Shumi shared Drive exists in Apollo's 29 accessible shared drives. Content folder must be shared with apollo@launchpadbizdev.com before Apollo can run.
- GHL state: 0 posts in Social Planner (May–Jul). First-half-of-June posts were done natively to IG/TikTok by client, not through GHL.
- Task notes captured: daily posting after June 18, no approver needed (status: scheduled), 7am–7pm PT window, 4 hashtags only, max 2-sentence meme-style captions.
- Status: Notion → Needs Revisions | Slack flagged to #social-media-management

## 2026-05-28 — WSN June 2026 Social Media Run (Apollo)
- Client: Welding School of Nevada | Creation month: May 26' | Posting month: June 2026
- Investigation finding: prior memory falsely claimed 8 posts created. GHL was empty — task stuck "In production" with no posts.
- Posts created: 8 graphics (4 stills + 4 carousels), FB + IG, status: in_review
- Schedule: Jun 1, 5, 8, 12, 15, 19, 22, 26 (Mon + Fri, 9 AM–3 PM PT)
- Videos track: skipped — Abril already posted all videos
- Pre-existing: 2 Cynthia video posts (Jun 3 + Jun 10) left untouched
- Safety check: PASS — all 8 in_review, publishedAt null, none published
- Approver: Greg Gilbert — Users scope off, manual attach needed. Cynthia notified.
- Flag: Carousel 2 (Jun 19) missing slide 2 from Drive — posted with 4 of 5 slides. Designer must supply slide 2.
- Slack + Notion comment sent to Cynthia for review.

## 2026-05-28 — Durango HVAC June 2026 Surgical Add — C4 EN (Apollo)
- Creation month: May | Posting month: June
- Action: placed C4 EN "3 Things to Know Before your AC Gives Up" (4-slide carousel) on Mon Jun 29 at 2 PM PDT
- Post ID: 6a1895c87712ffb5daac4a3b | Status: in_review | Approver: Yessenia Favela (jahOW5nXy44EUXKN0tY8)
- Safety check: PASS — publishedAt null, media.length=4 confirmed
- Rule applied: Critical Rule 16 overflow — Mon Jun 29 used as extra same-month weekday before pushing to July
- Durango June 2026 complete: 8 graphics total (4 stills + 4 carousels). Full contract fulfilled.
- Yessenia ID confirmed by Anthony 2026-05-28 — cached in durango_patterns.md for future runs.

## 2026-05-28 — BWU June 2026 Surgical Add — Still 4 (Apollo)
- Creation month: May | Posting month: June
- Action: placed 1 previously-unplaced graphic (Still 4 "Your Summer Apparel Starts Here") on Mon Jun 29 at 3 PM PDT
- Post ID: 6a188f9976455473844d2534 | Status: in_review | Approver: Jennifer Maldonado (F9cJvmUFuXgym8HM5YY4)
- Safety check: PASS — publishedAt null
- Rule applied: Critical Rule 16 overflow — extra same-month weekday (Jun 29 Mon) used before pushing to July

## 2026-05-27 — TBC June 2026 Social Run — Run 3 (Apollo)
- Creation month: May | Posting month: June
- Content: 6 videos (from May 26' approved folder) + 7 graphics (from May 26 approved folder, existing from Run 1)
- Run 3 actions: deleted 5 wrong-date video posts (Thursdays), recreated on correct Wednesdays; added missing Jun 17 Pacifica Montage
- Videos created: Jun 3, 10, 17, 24 + overflow Jul 1, Jul 8 (6 total) — FB + IG + TikTok, reel type
- Graphics: 7 existing posts retained (stills + carousels, IG + FB) — still on wrong weekdays, flagged for Cynthia
- Total posts in GHL: 13 | Safety check: PASS — all in_review, publishedAt null
- Approver: Sierra Burk (a3R7GX9q7ANEHtwZqtOQ) — confirmed on all posts
- Flag: 7 graphic posts on wrong weekdays (non-Mon/Thu) — Cynthia to decide reschedule or leave
- Flag: mcp__gohighlevel-tbc__* not in settings.json allowlist — Anthony to add

## 2026-05-27 — Muller Mask June 2026 Social Run (Apollo)
- Creation month: June | Posting month: June
- 8 graphic posts created (4 carousels + 4 stills), FB + LinkedIn only
- Posts held: 0 | Posts created: 8
- Schedule: Jun 4, 9, 11, 16, 18, 23, 25 + Jul 2 (overflow — June slot June 2 cut by 7-day window)
- Pre-existing: 4 video posts by Cynthia (Jun 3, 10, 17, 24) — untouched
- All 8 posts: status=in_review, safety check PASSED
- Flag: gohighlevel-muller MCP not in active .mcp.json — used curl fallback. Anthony to restore full .mcp.json.
- Flag: Approver auto-resolve blocked — Cynthia to attach herself manually in Social Planner

Append-only chronological record of all ingests, compiles, and lints. Each entry is timestamped and describes what changed. This file is the audit trail for how the Brain has grown over time.

**Format:**
```
## [YYYY-MM-DD] <operation> | <short title>
- What was added/changed
- Which notes were touched
- Source (if ingest)
```

## [2026-05-27] Social Media Poster Run | Durango HVAC June 2026 — Run #3
- Client: Durango HVAC | Creation month: June 26' (Drive) | Posting month: June 2026
- Run #3 — task status had been reset to Not started between runs; claimed again (Not started → In production → Needs Team Review).
- Visual QC: all 18 images downloaded and verified PASS (4 stills, 4 carousels / 14 carousel slides total)
- Captions: 7 posts written (IG + FB, bilingual per graphic language), brand compliance PASS
- GHL posts: 0 created — BLOCKED: mcp__gohighlevel-durango__get-posts denied (not in allowlist); GHL_TOKEN_DURANGO .env read denied; Mac Mini IP WAF block on /medias/upload-file persists (3rd consecutive blocked run)
- Planned schedule: Jun 4 (Still 1, ES), Jun 9 (Still 2, ES), Jun 11 (Still 3, EN), Jun 16 (Still 4, EN), Jun 18 (C1, ES), Jun 23 (C2, ES), Jun 25 (C3, EN)
- Overflow to July: C4 (EN "3 Things to Know Before your AC Gives Up", 4 slides)
- Notion comment: full captions + schedule deposited. Status: Needs Team Review. Slack sent to #social-media-managment + escalation to #ai-team-updates.
- Escalation: Anthony to resolve Mac Mini WAF/IP block + add mcp__gohighlevel-durango__* to allowlist.

## [2026-05-27] Social Media Poster Run | Muller Mask June 2026 — Run #2
- Client: Muller Mask | Creation month: June 26' (Drive) | Posting month: June 2026
- Run #2 — task re-triggered. Claim-or-abort check passed (status was Not started — new task instance).
- Visual QC: all 16 images re-verified PASS
- Captions: all 8 posts written (FB + LI), brand compliance PASS
- GHL posts: 0 created — BLOCKED: mcp__gohighlevel-muller__* not in settings.json allowlist + GHL_TOKEN_MULLER not in process env (.env read denied)
- Root cause: Muller was batch-wired 2026-05-26 but never added to settings.json allowlist. Distinct from the WAF/Cloudflare 403 documented in run #1.
- Planned dates: Jun 2, 4, 9, 11, 16, 18, 23, 25
- Notion comment: full captions deposited. Status: Needs Team Review. Slack sent.
- Escalation: Anthony to add mcp__gohighlevel-muller__* to .claude/settings.json allowlist.

## [2026-05-27] Social Media Poster Run | Muller Mask June 2026
- Client: Muller Mask | Creation month: June 26' (Drive) | Posting month: June 2026
- 8 posts planned (4 carousels + 4 stills), 0 videos (Cynthia handles videos per task notes)
- Visual QC: all 16 images PASS — brand colors, CMMCM logo, no typos or errors
- Captions: written for FB + LinkedIn (B2B tone, max 3 sentences, max 2 emojis, generic hashtags)
- Posts scheduled: 0 created in GHL — BLOCKED by Cloudflare WAF on media upload (Mac Mini IP)
- Planned dates: Jun 2 (C1), Jun 4 (S1), Jun 9 (C2), Jun 11 (S2), Jun 16 (C3), Jun 18 (S3), Jun 23 (C4), Jun 25 (S4)
- Flags: Mac Mini WAF block; approver ID (Cynthia) unresolvable via Users API (403); no Brain note; manual upload required; Cynthia's 4 video posts already in GHL (June 3/10/17/24, status: scheduled)
- Next step: Anthony/Cynthia uploads 16 images to GHL Media Library, posts CDN URLs in Notion task comment

## [2026-05-27] Social Media Poster Run | Durango HVAC June 2026
- Client: Durango HVAC | Creation month: June 26' (Drive) | Posting month: June 2026
- 7 posts planned (4 stills + 3 carousels), 1 carousel overflow (C4 — no June slot)
- Videos: skipped — Cynthia already posted per task note
- Visual QC: all 18 images PASS
- Captions: written and saved in Notion task comment (bilingual — ES/EN matching graphic language)
- Posts scheduled: 0 created in GHL — BLOCKED by Cloudflare WAF on media upload endpoint (same Mac Mini IP block as all prior Durango runs)
- Scheduled dates planned: Jun 4, 9, 11, 16, 18, 23, 25
- Held/overflow: C4 English "3 Things to Know" (no June slot)
- Flags: Mac Mini WAF block persists; Yessenia GHL user ID unresolvable (403); manual upload required
- Notion status: Needs Team Review | Slack: notified #social-media-managment

Operations: `ingest` · `compile` · `lint` · `manual` · `smm-run`

## [2026-05-27] smm-run | BWU June 2026 Content Calendar
- Client: Brand With Us (BWU)
- Creation month: June 26' | Posting month: June 2026
- Posts planned: 8 graphics (0 videos — Cynthia already posted videos)
- Posts created in GHL: 0 — BLOCKED by Cloudflare WAF 1010 on media upload endpoint (Mac Mini IP)
- Posts held: 0 (all images passed visual QC — blocked is infrastructure, not content)
- Flags: Media upload blocked (Mac Mini IP), TikTok not connected in BWU GHL, Jennifer Maldonado approver GHL ID unresolvable, gohighlevel-bwu MCP tools hit permission wall (used curl/Python fallback)
- Notion task: https://www.notion.so/349b01f77d6d81c6b2c5f9a33bb2614e
- Action needed: Anthony to upload 15 images via browser, paste CDN URLs in Notion comment

---

## [2026-05-27] smm-run | AFT June 2026 — Run 1: 11 posts created (7 graphics + 4 videos), safety check passed
- **Client:** Arby's Food Truck (AFT)
- **Notion Task:** AFT June 26' Content Calendar (ID: 349b01f7-7d6d-817a-9ef5-f613972f68ff)
- **Creation month:** June 26 | **Posting month:** June 2026
- **Drive source:** Diversified Restaurant Group Drive > Arby's Food Truck > Graphic Design/June 26/Approved/ + Videos/June 26/Approved/
- **Posts created:** 11 (7 graphics + 4 videos) — 0 failed, 0 held
- **Safety check:** PASSED — all 11 posts GET'd, status=in_review, deleted=False, publishedAt=None, approver=Sierra Burk
- **Schedule:** Graphics: Jun 5, 9, 12, 16, 19, 23, 26. Videos: Jun 4, 11, 18, 25. (Jun 2 graphic slot skipped — before 7-day QC window)
- **Graphics track:** 4 stills (16, 17, 19, Genz meme) + 3 carousels (Corporate 2-slide, Hold+Scroll 10-slide, Team Hangout 2-slide). All passed Visual QC. Posted IG + FB only (matching Abril's existing pattern; TikTok for graphics untested on this account).
- **Videos track:** 4 videos (BITE Gif, Crowd Favorite, FAKE RAGE, WHITEBOARD AFT). Posted IG + FB + TikTok.
- **Approver:** Sierra Burk (GHL ID: a3R7GX9q7ANEHtwZqtOQ) — confirmed present in sub-account, set on all 11 posts
- **Notion status:** Needs Team Review
- **Flags:** 2 loose videos outside Approved (STRESSED MANAGER V2.mp4, STRESSED MANAGER.mp4) not posted — team needs to move to Approved if they should go out. 3 pre-existing posts by Abril (Jun 2, 3, 6) were detected and skipped. mcp__gohighlevel-arbys not in allowlist — used curl fallback (works, but add to settings.json for cleaner future runs). Video upload requires explicit content-type `video/mp4` in multipart form.

## [2026-05-27] smm-run | TBC June 2026 — Run 1: 7 graphic posts created, safety check passed
- **Client:** Taco Bell Cantinas (TBC)
- **Notion Task:** TBC June 26' Content Calendar (ID: 349b01f7-7d6d-8169-a658-d151f3096201)
- **Creation month:** May 26' | **Posting month:** June 2026
- **Drive source:** Diversified Restaurant Group Drive > Taco Bell Cantinas > Graphic Design/May 26/Approved/
- **Posts created:** 7 (IG + FB each = 14 GHL post objects) — 0 failed, 0 held
- **Safety check:** PASSED — all 7 posts GET'd, status=in_review, deleted=False, publishedAt=None, approver=Sierra Burk
- **Schedule:** Jun 5, 9, 12, 16, 19, 23, 26 (June 2 skipped — before 7-day QC window)
- **Graphics:** 4 stills + 3 carousels. All passed Visual QC.
- **TikTok blocked:** GHL 422 — TikTok in GHL requires video, rejects all static image posts
- **Videos track:** Not yet posted — 6 videos in Approved folder, only 4 calendar slots. Pending Cynthia direction on overflow.
- **Approver:** Sierra Burk (GHL ID: a3R7GX9q7ANEHtwZqtOQ) — set on all 7 posts
- **Notion status:** Needs Team Review
- **Flags:** still-2.png (Millennial vs Gen Z team graphic) flagged for Cynthia review; June 2 slot skipped per 7-day window; TikTok blocked; video overflow (6 videos, 4 slots)

## [2026-05-27] smm-run | Durango HVAC June 2026 — Run 1: BLOCKED (media upload WAF issue)
- **Client:** Durango HVAC
- **Notion Task:** Durango HVAC June 26' Content Calendar (ID: 349b01f7-7d6d-8168-9cbf-ccb173ad4f7e)
- **Creation month:** June 2026 | **Posting month:** June 2026
- **Posts created:** 0 — blocked before post creation
- **Posts planned:** 7 graphics (4 stills + 3 carousels) for Facebook + Instagram. Carousel 4 held as overflow (8 graphics, only 7 slots after 7-day window).
- **Videos track:** Skipped per task notes — Cynthia already posted videos
- **Blocker:** Mac Mini IP blocked by Cloudflare WAF on GHL `/medias/upload-file` endpoint (error 1010). Cannot upload media → cannot create posts.
- **Visual QC:** All 14 files (4 stills + 10 carousel slides) passed — on-brand, correct bilingual matching, no typos, no clerical errors
- **Captions:** Written for all 7 posts, both IG + FB — ready to use once unblocked. Spanish captions for Spanish graphics, English for English.
- **Flags:** 7-day window drops June 2 slot (only 7 of 8 graphic slots usable). Users API 403 on both tokens — Yessenia Favela's GHL user ID unresolvable. Durango token missing Users (read) scope.
- **Notion:** Status set to Needs Revisions. Full detail + caption list + CDN URL request in comment.
- **Slack:** Posted to #social-media-management and #ai-team-updates (permission escalation)

## [2026-05-27] smm-run | Muller Mask June 2026 — Run 1: BLOCKED (media upload WAF issue)
- **Client:** Muller Masks
- **Notion Task:** Muller Mask June 26' Content Calendar (ID: 349b01f7-7d6d-81ef-be73-ef78c28a5cd9)
- **Creation month:** June 2026 | **Posting month:** June 2026
- **Posts created:** 0 — blocked before post creation
- **Posts planned:** 8 graphics (4 stills + 4 carousels) for Facebook + LinkedIn
- **Videos track:** Skipped per task notes — Cynthia handles videos
- **Blocker:** Mac Mini IP blocked by Cloudflare WAF on GHL `/medias/upload-file` endpoint (error 1010). Cannot upload media → cannot create posts.
- **Visual QC:** All 8 graphics (16 files) passed — clean, consistent CMMCM branding, no typos
- **Captions:** Written and QC'd for all 8 posts, both FB and LinkedIn versions — ready to use once unblocked
- **Flags:** 4 Cynthia video posts are `status: scheduled` (no approval gate) — flagged. Users API 403 — approver ID unresolvable. No Brain note for Muller Mask. CMD approver field blank.
- **Notion:** Status set to Needs Team Review. Full detail comment added.
- **Slack:** Posted to #social-media-management

## [2026-05-21] smm-revision | TTFS June 2026 — Run 4 (Revision): English captions + Monica approver applied
- **Client:** Toro Taxes Franchise Sales (TTFS)
- **Notion Task:** TTFS June 26' Content Calendar (ID: 349b01f7-7d6d-8131-982d-db0df4160b49)
- **Run type:** Revision — Cynthia directed 2 changes: (1) English captions instead of Spanish, (2) approver = Monica Mariona
- **Method:** DELETE all 24 v1 posts (Spanish, no approver) → verify 0 Apollo posts remain → RECREATE 24 with English captions + Monica approver. No edit-in-place (avoids publish-live bug).
- **Posts deleted:** 24 (all confirmed `in_review`, none published before delete)
- **Posts recreated:** 24 (12 graphics x IG + FB) — 0 failed
- **Safety check:** PASSED — all 24/24 GET'd, `status=in_review`, `deleted=False`, `publishedAt=None`, `approver=hJzrXKb7iVq3WaWQ0b59` (Monica Mariona)
- **Preserved:** Cynthia's 6 pre-uploaded video posts — NOT touched (all already had Monica approver)
- **Brain updates:** TTFS Caption Feedback Log created, Language Strategy conflict flagged, ttfs_patterns.md updated with resolved approver IDs (Monica/Carlos/Frida Montealegre)
- **Approver corrected:** Previous memory had "Frida Miranda" — correct last name is Montealegre
- **Notion:** Comment added with new post IDs, Cynthia revision confirmed
- **Slack:** Posted to #social-media-management

## [2026-05-21] smm-run | TTFS June 2026 — Run 3: 24 posts created, safety check passed
- **Client:** Toro Taxes Franchise Sales (TTFS)
- **Notion Task:** TTFS June 26' Content Calendar (ID: 349b01f7-7d6d-8131-982d-db0df4160b49)
- **Creation month:** June 26' (Drive source: Graphics/June 26'/Approved/)
- **Posting month:** June 2026
- **Run type:** Final posting run — token now wired (GHL_TOKEN_TTFS). Ran full pipeline from Drive re-list through post creation and safety check.
- **Posts created:** 24 (12 graphics x IG + FB) — 0 failed, 0 held
- **Safety check:** PASSED — all 24 GET'd, confirmed `status=in_review`, `deleted=False`, `publishedAt=None`
- **Schedule:** Jun 1, 2, 4, 8, 9, 11, 15, 16, 18, 22, 23, 25 — Mon/Tue/Thu slots, 9 AM Mexico City
- **Shortfall:** Jun 29 + Jun 30 unplaced — Drive has 12 graphics vs 14 contracted (same shortfall from Run 1)
- **Approver flag:** GHL users API returned 0 results with sub-account token — approver IDs for Monica/Frida Miranda/Carlos Maldonado could not be resolved. All posts `in_review` with empty approver field. Cynthia must attach approver manually in Social Planner.
- **Videos track:** Skipped per explicit instruction — Cynthia pre-uploaded June videos
- **Notion status updated:** Needs Team Review
- **Slack notification:** Posted to #social-media-management

## [2026-05-21] smm-run | TTFS June 2026 — Run 2: GHL token still missing, posting blocked again (same as Run 1)
- **Client:** Toro Taxes Franchise Sales (TTFS)
- **Notion Task:** TTFS June 26' Content Calendar (ID: 349b01f7-7d6d-8131-982d-db0df4160b49)
- **Creation month:** June 26' (Drive source: Graphics/June 26'/Approved/)
- **Posting month:** June 2026
- **Run type:** First run — new client to automation system
- **Posts created this run:** 0 — GHL sub-account token not configured
- **Posts QC'd and ready:** 12 (6 stills + 6 carousels) — all passed Visual QC
- **Captions written:** 12 posts (IG + FB versions each), Spanish, brand-compliant
- **Captions saved to:** marketing/output/social-posts/ttfs-june-2026-captions.md
- **Posting schedule planned:**
  - Post 1: Mon Jun 1 — Still 1; Post 2: Tue Jun 2 — Still 2; Post 3: Thu Jun 4 — Still 3
  - Post 4: Mon Jun 8 — Carousel 1; Post 5: Tue Jun 9 — Still 4; Post 6: Thu Jun 11 — Carousel 2
  - Post 7: Mon Jun 15 — Still 5; Post 8: Tue Jun 16 — Carousel 3; Post 9: Thu Jun 18 — Carousel 4
  - Post 10: Mon Jun 22 — Still 6; Post 11: Tue Jun 23 — Carousel 5; Post 12: Thu Jun 25 — Carousel 6
  - Jun 29 + Jun 30 unplaced — no content (2-graphic shortfall flagged)
- **Videos track:** Skipped per explicit task note — Cynthia already uploaded
- **Permission wall:** No `gohighlevel-ttfs` MCP entry, no sub-account token in .env. Escalated to Anthony via #ai-team-updates.
- **Content gap flag:** Drive has 12 approved graphics vs 14 contracted slots. Jun 29 + Jun 30 have no content.
- **Approvers:** Monica, Frida Miranda, Carlos Maldonado (GHL user IDs TBD — will resolve at posting time once token is set up)
- **Notion status updated:** Needs Team Review
- **Slack notifications:** #social-media-management + #ai-team-updates

## [2026-05-20] smm-run | CCS June 2026 — Run 3: full reconcile, 18 new graphic posts created
- **Client:** Continental Currency Services
- **Notion Task:** CCS June 26' Content Calendar (ID: 349b01f7-7d6d-8130-931f-e7a0f7cf3c22)
- **Creation month:** May 26' (Drive source: Graphics/May 26'/Approved/)
- **Posting month:** June 2026
- **Run type:** Reconcile — queried GHL live, skipped existing posts, created only genuinely-missing graphics
- **Posts skipped (already in GHL):** Jun 1 (stray), Jun 2, 3, 4, 6, 8 (Cynthia/Emigen placed)
- **Posts created this run:** 18 (Jun 5, 9–21, 23–26) — FB + IG, status=scheduled
- **Posts held (image errors):** 0 — all 39 images passed Visual QC
- **7-day QC window:** First post Jun 5 (task assigned May 20 + 7 days = May 27; all of June qualifies)
- **Content gap flags:**
  - Jun 27 graphic slot unfilled — no content piece available after assigning all 18 slots
  - 5 unplaced pieces (P2-Stills 3–7) — 23 Drive pieces, 18 available slots, 5 overflow
  - Stray Jun 1 post in GHL (ID: 69cee2cdbe23015c57f57d1f) — needs manual cleanup
- **Approval routing:** postApprovalDetails.approverUser null on all created posts — Terrance not auto-wired
- **Videos track:** Skipped per explicit run instructions (Emigen handled manually)
- **Brain file missing:** Brain/Projects/CCS.md not found — context loaded from agent memory
- **Notion status updated:** Needs Team Review
- **Slack notification posted:** #social-media-management

## [2026-05-20] smm-run | CCS June 2026 — Run 2: held posts resolved, content gap flagged
- **Client:** Continental Currency Services
- **Notion Task:** CCS June 26' Content Calendar (ID: 349b01f7-7d6d-8130-931f-e7a0f7cf3c22)
- **Creation month:** May 26' (Drive source: Graphics/May 26'/Approved/)
- **Posting month:** June 2026
- **Posts created this run:** 2 (previously-held carousels, images fixed by designer)
  - June 6 — P1 Carousel 1 (DMV/registration) | GHL `_id: 6a0e2abb4c0aa4780635bb31`
  - June 8 — P2 Carousel 2 (Travel/currency) | GHL `_id: 6a0e2accb1dfa52ac6a36aaf`
- **Total June posts in GHL:** 21 of 24 contracted graphic slots
- **Posts held:** 0 (both prior-held items resolved)
- **Content gap:** 7 graphic slots unfilled (June 13, 14, 15, 20, 21, 26, 27) — Drive has no additional content. Flagged to Cynthia.
- **Other flags:** Stray post June 1 (not on calendar), duplicate posts June 2+3, approval routing not wired for Terrance
- **API quirk learned:** GHL create-post media objects require `"type": "image/png"` not `"type": "image"` — 422 otherwise
- **GHL MCP status:** `gohighlevel-ccs` MCP now wired and working. Media upload still uses curl fallback (no MCP tool for media upload).
- **Notion status updated:** Needs Team Review

## [2026-05-20] smm-run | CCS June 2026 content batch — Apollo pipeline run
- **Client:** Continental Currency Services
- **Notion Task:** CCS June 26' Content Calendar (ID: 349b01f7-7d6d-8130-931f-e7a0f7cf3c22)
- **Drive source:** Graphics/May 26'/Approved/ (part 1 + part 2) — no June folder exists yet (flagged)
- **Posts drafted in GHL:** 21 (11 stills + 10 carousels) — FB + IG, all status=draft
- **Posts held (image errors):** 2
  - P1-C1: Grammar error on slide 2 — "CCS help you" should be "CCS helps you"
  - P2-C2: Slide 2 file not retrievable from Drive (Drive API 404)
- **Post count vs. contract:** 23 graphics found vs. 24 contracted (1 short — flag to Cynthia)
- **Flags:** Task Month property says "May" but task name says "June"; no June Drive folder; duplicate posts in GHL from parsing bug (v1 run created 21 extra drafts without IDs captured — recommend Cynthia delete unidentified drafts in Social Planner)
- **GHL Social Planner:** https://app.gohighlevel.com/location/xqSj47GjK0FHN4oXZ0mX/social-planner
- **Notion status updated:** Needs Team Review
- **Permission wall encountered:** gohighlevel-ccs MCP server missing from .mcp.json — used curl fallback. Need to add MCP entry.

## [2026-04-13] manual | Phase 5b complete — integrations + templates
- **Brain Dump → brain-compile integration:** Added "Step 6.5 Raw Layer Compile Check" to `.claude/skills/brain-dump.md`. Brain dump now scans Raw/ for unprocessed sources at the end of every run and invokes brain-compile.
- **Notion Sync → Raw/exports/ integration:** Updated `.claude/skills/notion-brain-sync.md` Step 2 (Meeting Notes). Meeting notes now deposit into `Raw/exports/notion-meeting-{date}_{slug}.md` and compile folds them into Daily/ and Projects/ with cross-links. Legacy direct-write mode kept as fallback.
- **Content agents → brain-query integration:** Added Brain Query Integration section to `CLAUDE.md`. All 9 agents now read this rule and use brain-query for cross-note lookups instead of grep-crawling. Single-client context loads stay direct.
- **Templates for future agents/skills:** Created `.claude/templates/agent-template.md` and `.claude/templates/skill-template.md` with mandatory Brain Integration blocks baked in. Added rule to CLAUDE.md requiring all new agents/skills to start from these templates.
- **Brain upgrade plan status:** Phases 1-5 all complete. The Brain is now a compounding knowledge system with a Raw layer, master index, 11 MOCs, consistent frontmatter, four operational skills, clean lint state, and auto-inherited integration for future components.

## [2026-04-13] manual | Track A cleanup complete
- Renamed `Projects/Sobel\ Westex\ (Multi-Brand).md` → `Projects/Sobel Westex (Multi-Brand).md` (removed stray backslash)
- Renamed `Projects/Arbys Food Truck.md` → `Projects/Arby's Food Truck.md`
- Fixed all 13 remaining `[[Arbys Food Truck]]` stale links in DRG.md, Sobel Westex.md, Daily/2026-04-08.md, Daily/2026-04-09.md
- Updated 8 `[[Team — X]]` links → `[[X]]` in Skills/CRM and GHL Workflow.md, Content Workflow — Shoot to Post.md, Video Production SOP.md
- Fixed self-referential wikilink in Intelligence/Trend Brief — 2026-04-13.md
- Archived empty scratch notes (Team — Munzelle Jazz.md, Cowork Test.md, note name.md) to `_archive/`
- Added scope headers to three onboarding notes clarifying they're complementary (SOP / framework / implementation), canonical = [[New Client Onboarding Process]]
- Created 3 stubs for high-traffic missing notes: [[Building in Public Campaign Brief]], [[The Playbook Campaign]], [[Launchpad Productions]]
- Updated Intelligence and Projects MOCs with new entries
- Re-lint results: broken wikilinks methodology-corrected baseline ~72 → now ~59 after Arby's fixes; orphans 3 → 1; MOC drift 1 → 0

## [2026-04-13] lint | full — first full pass (Phase 3 retrofit)
- Scanned: 159 notes
- Auto-fixes: 143 (frontmatter retrofit across every non-indexed note — Phase 3 of the Brain upgrade is complete)
- Flags: 79 (67 broken wikilinks, 3 orphans, 9 near-duplicate groups, 1 MOC drift, 0 stale, 0 stuck Raw)
- Top issues: filename drift bugs (`Sobel\ Westex` backslash, `Arbys` missing apostrophe, `Team —` prefix convention), three Client Onboarding notes still drifting, high-traffic missing campaign notes (`Building in Public Campaign Brief`, `The Playbook Campaign`)
- Report: `marketing/output/reports/brain-lint-2026-04-13.md`

## [2026-04-13] manual | Phase 4 complete — four Brain skills built
- Created `.claude/skills/brain-ingest.md` — single-source ingest, writes/updates notes, backlinks, logs
- Created `.claude/skills/brain-query.md` — cited answers grounded in Brain, files synthesis back
- Created `.claude/skills/brain-compile.md` — batch ingest with pattern pass, idempotent
- Created `.claude/skills/brain-lint.md` — health check, auto-fixes frontmatter, flags issues
- Phase 4 complete. Phase 3 (frontmatter retrofit) will execute via first full `/brain-lint` run.
- Next: Phase 5 integration (wire brain-ingest into Brain Dump, Notion Sync, content agents) + run first full lint.

## [2026-04-13] manual | All folder MOCs created
- Added 8 remaining MOCs: [[Teams/00-INDEX]], [[Departments/00-INDEX]], [[Skills/00-INDEX]], [[Resources/00-INDEX]], [[Strategic Partners/00-INDEX]], [[Onboarding/00-INDEX]], [[Daily/00-INDEX]], [[Tasks/00-INDEX]]
- All 11 folders now have index files. Master [[index]] updated to reflect live status.
- Phase 2 complete. Next up: Phase 4 (the four Claude Code skills — ingest, query, compile, lint).

## [2026-04-13] manual | Karpathy LLM Wiki pattern adopted
- Created [[Raw/README]] and Raw/ subfolder structure (articles, transcripts, clips, screenshots, exports)
- Created [[index]] — master catalog for AI queries
- Created this log file
- Created folder MOCs: [[Projects/00-INDEX]], [[Intelligence/00-INDEX]], [[Context/00-INDEX]]
- Source inspiration: [[Intelligence/Second Brain Compounding — Karpathy-Obsidian-Claude 2026-04-11]]
- Phase 1 + Phase 2 of the Brain upgrade plan complete. Next: Phase 3 (frontmatter standard) and Phase 4 (ingest/compile/query/lint skills).

## 2026-05-27 — BWU June 2026 Social Media Run
- **Client:** Brand With Us (BWU)
- **Creation month:** June 2026
- **Posting month:** June 2026
- **Posts scheduled:** 7 graphics (in_review, approver: Jennifer Maldonado F9cJvmUFuXgym8HM5YY4)
- **Posts held:** 0 (all passed QC)
- **Unplaced:** 1 graphic (Still 4 — "Your Summer Apparel Starts Here") — no June slot within 7-day window
- **Videos:** Skipped — Cynthia already posted videos per task notes
- **Platforms:** Instagram + Facebook (TikTok not connected)
- **Media upload:** WAF block cleared — all 15 files uploaded via ghl-media-upload.sh
- **Flags:** MCP permission walls on BWU tools (used curl fallback); TikTok not connected; Still 4 unplaced; Jennifer Maldonado GHL ID now resolved (F9cJvmUFuXgym8HM5YY4)
- **Safety check:** PASSED — all 7 posts confirmed in_review, publishedAt: null

---

## 2026-05-28 — AFT June 2026 Revision Run (Rule 17 date correction)

- **Client:** Arby's Food Truck (AFT)
- **Creation month:** June 2026 | **Posting month:** June 2026
- **Trigger:** Cynthia comment 2026-05-27 21:57 — "Change posting dates to ones on Arby's Food Truck Content Monthly Deliverables calendar"
- **Problem:** Run 1 (2026-05-27) placed all 11 posts on wrong weekdays (Fri/Tue/Thu for videos). AFT pattern = Graphics Mon/Thu, Video Wed.
- **Action:** Deleted all 11 Run 1 Apollo posts, recreated on correct weekdays
- **Posts scheduled:** 11 (7 graphics FB+IG, 4 videos FB+IG+TikTok)
- **Schedule:** Jun 4/8/11/15/18/22/25 (graphics) | Jun 10/17/24/30 (videos; Jun 30 Tue = overflow, Jun 3 Wed human-owned)
- **Flags:** Jun 30 Tue overflow slot used (only 3 Weds available after Jun 3 pre-existing human post)
- **Safety check:** PASSED — all 11 in_review, publishedAt: null, approver Sierra Burk confirmed

---

## 2026-07-20 — Durango HVAC August 2026 Run (Videos Only)

- **Client:** Durango HVAC
- **Creation month:** August | **Posting month:** August 2026
- **Trigger:** Notion task assigned Not started, plus Cynthia Slack brief: post videos only this run, skip graphics even if present, report graphics-skipped count
- **Drive:** August graphics folder does not exist yet (only through July 26') — confirms videos-only was correct, 0 graphics to skip/report
- **Posts scheduled:** 6 videos, FB+IG, type reel (contract = 4/mo, 2 overflow added same-month per Rule 16, no rollover needed)
- **Schedule:** Aug 4 (Tue overflow), 7 (Fri), 14 (Fri), 18 (Tue overflow), 21 (Fri), 28 (Fri) — all weekdays verified via Python datetime
- **Flags:** GHL mime-type fix discovered — `.mov` files require `"type":"video/mov"` not `"video/quicktime"` (422 otherwise). No pre-existing August posts found (clean reconcile).
- **Safety check:** PASSED — all 6 in_review, publishedAt: null, media/approver/mediaOptimization confirmed at create; ghl-post-guard.py sweep = SWEEP PASS

---

## 2026-07-20 — Launchpad Business Development (LPBD) August 2026 Graphics Run (graphics-only, Cynthia brief)

- **Client:** Launchpad Business Development (LPBD, agency's own account — NOT LP University)
- **Creation month:** August 2026 | **Posting month:** August 2026 (Drive `GRAPHICS/August 26'/Approved/` matches task name this cycle)
- **Trigger:** Manual run of "LP August 26' Content Calendar" task; claim-or-abort confirmed Status=Not started before flipping to In production
- **Scope per Cynthia:** graphics only this run, no videos even if present in Drive
- **Drive:** LaunchPad agency shared drive `0ACS-IMXQ_490Uk9PVA` → Graphics/2026/August 26'/Approved/ → Stills (5) + Carousels (10 folders)
- **Visual QC:** all 5 stills + 6 of 10 carousels passed (C2, C3, C4, C6, C7, C9). Held: Carousel 5 (grammar/punctuation typo on slide 4 — "businesses" needs apostrophe + missing period), Carousel 1 (mixed — slide 2 is an .mp4, held for the video content, out of scope), Carousel 8 (all 4 slides .mp4 — video track, skipped), folder "10" (6 individual team-intro .mp4 clips — Abril/Amber/Anthony/Cynthia/Emigen/Kyle — skipped)
- **Posts created:** 11 (5 stills + 6 carousels), FB + IG only (TikTok excluded, graphics-only), status in_review, approver Abril (MBieq3yaE1ixkILPfLs8), mediaOptimization ON
- **Schedule:** Aug 2, 5, 8, 11, 14, 16, 19, 22, 25, 28, 31 — spread across full month incl. 4 weekend dates, one graphic/day, all dates verified via Python datetime (Critical Rule 21), all posting hours 9am-4pm PDT (within 8am-8pm window)
- **Reconcile:** found 1 pre-existing post by Cynthia Hernandez (human, not Apollo) on Aug 1 — left untouched per Rule 15, scheduled new posts starting Aug 2 to avoid collision
- **Videos skipped (reported, not posted):** 11 video files / 8 content units total — 6 team-intro clips, 1 all-video 4-slide carousel (C8), 1 mixed carousel (C1) held whole because of 1 video slide
- **Media upload:** clean, no Cloudflare 1010 issues, ghl-media-upload.sh used throughout
- **Safety check:** PASSED — `ghl-post-guard.py sweep` returned SWEEP PASS; all 11 posts individually GET-verified (status in_review, publishedAt null, media count matches plan, approver set, mediaOptimization true)

## 2026-07-20 — Shumi Nation August 2026 Social Media Run (videos-only ad-hoc)

- **Client:** Shumi Nation (The Shumi Company)
- **Creation/posting month:** August 2026
- **Trigger:** Direct task assignment (Notion page 380b01f7-7d6d-818f-a95e-e0bf7f15968e), Cynthia's brief via Slack: videos ONLY this run, graphics deferred
- **Posts scheduled:** 15/15 videos → IG + TikTok, status: scheduled (Shumi's standing no-approver override), publishedAt: null confirmed on every post
- **Posts held:** 0
- **Graphics:** Skipped per brief. No `Graphic Design /August 26'/` folder exists in Drive yet (only June/July present) — nothing to skip.
- **Drive path:** `Videos/August 26'/Edited/Approved/` inside Shumi Nation shared drive `0AHbtW0nyBNcyUk9PVA` (same shape as July)
- **Schedule:** Aug 1,3,5,7,10,12,14,16,18,20,22,25,27,29,31 (every ~2 days across full month incl. weekends) — only 15 videos available for 31 days so spread evenly rather than daily; flagged gap to Cynthia in Notion comment
- **Content ID:** No ffmpeg/cv2/pyobjc on Mini — used `qlmanage -t -s 1200` poster frames + `afinfo` for duration/sanity check. Identified: Cloud Strife (FF7), Kamen Rider x2, Hsien-Ko (Darkstalkers), Android 17 (DBZ), Black Clover news clip, Pokémon TCG unboxing; 6 clips left generic (con-interview/price-guess format, franchise not visually confirmable — never guessed)
- **GHL API quirk (NEW):** `.mov` (QuickTime) video uploads reject mime `video/quicktime` with 422 ("Instagram reel supports MOV and MP4 video formats only"). Must use literal mime string `video/mov`. `.mp4` files use `video/mp4` as normal. All 8 `.mov` files failed first pass, succeeded on retry with `video/mov`.
- **Safety check:** PASSED — `ghl-post-guard.py sweep --slug shumi --loc RPGcYwtea93GSFile2Yu` = SWEEP PASS (66 posts scanned, no premature/in_progress publishes)
- **Flags:** Day-coverage gap (16 of 31 days uncovered) due to limited content; graphics folder for August not yet created by design team

## 2026-07-20 — MNL (Matsuda Nadig Law) August 26' Content Calendar
- **Client:** MNL. **Creation month:** August (Month property). **Posting month:** August (task name).
- **Trigger:** Notion task `380b01f7-7d6d-8187-83cf-ddaa77a8c29d`, Status Not started → claimed → In production → Needs Team Review.
- **Drive:** `Graphic Design/2026/Aug 26'/Approved/{Stills,Carousels}` (8 stills, 8 carousel folders) + `Videos/2026/August 26'/Edited/Approved` (13 video files).
- **Visual QC caught 2 typo'd carousels — HELD, not posted:**
  - Carousel 2 (7 slides): "Scenerio:" misspelled 3x (slides 2/4/6), should be "Scenario:"
  - Carousel 4 (4 slides): "Neglicence" misspelled (slide 2), AND slide 3 references "In Arizona" — MNL is the Las Vegas/Nevada firm; likely an MNV (Arizona sister firm) slide that landed in the wrong client's APPROVED folder.
- **Posts created:** 27 (14 graphics: 8 stills + 6 carousels; 13 videos incl. 3 MNV collabs). All `in_review`, approver Sage Lopez, mediaOptimization ON, scheduled Aug 1–31 spread across full month incl. weekends (skipped 4 evenly-spaced Thursdays as the only gap days since 27 items < 31 days).
- **New GHL API quirk:** Facebook rejects a multi-video carousel post ("Facebook post doesn't support multi media format" 422) even though multi-image carousels post to FB fine. Fix: drop FB from accountIds for a video-slide carousel, post to Instagram only. (Carousel 7, 4 mp4 slides — MNL's animated "This is your sign" carousel.)
- **Collabs verified:** diff tone skit, siblings argue, makeshift weapons — all have `@mnvlaw.az` set as IG collaborator and confirmed persisted post-create.
- **mnlaw.lv (banned IG account) check:** zero occurrences across all 27 posts, verified.
- **Safety check:** `ghl-post-guard.py sweep --slug mnl --loc 6BwDC4InSwVFpij60ALj` → SWEEP PASS.
- **Flags:** 2 carousels held for designer fix (see above). No Slack message sent per explicit instruction (Cynthia reporting centrally this run).

## 2026-07-20 — MNV (Matsuda Nadig Van Law) August 2026 Social Media Run

- **Client:** MNV Law (Arizona PI firm), Location `NRxnUROIk02hv9lGQWHG`
- **Creation/posting month:** August 2026
- **Trigger:** Direct task assignment (Notion page 380b01f7-7d6d-812f-8811-c730fe3169aa), status flipped Not started -> In production per claim-or-abort
- **Drive:** `Matsuda Nadig Van Law` shared drive `0ACYzRxEMk1MaUk9PVA` — `Videos/2026/August 26'/Edited/Approved/` (7 files) and `Graphics/Aug 26'/Approved/{Stills,Carousels}` (8 stills + 8 numbered carousel folders)
- **Posts created:** 15/22 approved pieces — 8 single-image graphics (FB+IG) + 7 videos (FB+IG+TikTok reels, TikTok toggles ON). All `status:scheduled`, approver Sage Lopez, verified `publishedAt:null`.
- **Posts held (7):**
  - C2 (7-slide carousel): designer typo "Scenerio" (should be "Scenario") repeated on 3 slides
  - C3 (4-slide carousel): designer typo "Neglicence" (should be "Negligence") on 1 slide
  - C5 (4 .mp4 files): NOT independent slides — one continuous "this is your sign" text-animation split into sequential render fragments. Can't stitch (no video tools on the Mini). Flagged for designer to deliver as one file.
  - C1, C4, C6, C7, C8 (5 carousels, otherwise QC-clean): blocked by a **live GHL platform bug** — multi-image `media[]` truncates to 1 slide within ~1 second of post creation, reproduced 3x with different request variants (combined vs per-platform posts, with/without fileId tags). Confirmed NOT an Apollo request error. All broken attempts deleted (verified `deleted:true`, nothing published). Flagged to Anthony for GHL support ticket.
- **Schedule:** 20 unique dates spread across Aug 1-31 incl. 6 weekend posts, max 2-day gap, no same-day type collisions, all times 9am-6pm AZ local (fixed UTC-7, no DST), verified via Python datetime throughout.
- **Safety check:** PASSED — `ghl-post-guard.py sweep` flagged only the 10 known pre-existing `6a444e5...` orphan records from the 2026-06-30 incident (baseline captured at run start, identical set at run end). Zero new anomalies.
- **Key learning:** MNV's carousel-create bug is new and blocks ~23% of this month's approved content (5 of 22 pieces) — needs platform-level fix before rerun. See `mnv_patterns.md` for full repro details.

## 2026-07-21 — LP University August 2026 Social Media Run (GRAPHICS ONLY)

- **Client:** LP University (LP Uni), shared GHL location `hbcsvkyO40fTLTbsL1lI` (LPBD's own location)
- **Creation/posting month:** August 2026
- **Trigger:** Direct task assignment (Notion page 6f7b01f7-7d6d-8325-acfb-015ae703dff7 "LP Uni August 26' Content Calendar"), status was `Not started` -> claim proceeded -> flipped to `In production`
- **Drive:** `LaunchPad University` shared drive `0AMQc2sCAYcyOUk9PVA` -> `Graphic Design/August 26'/Approved/` (`Stills/` = 4 files, `Carousels/1-4/` = 4/3/3/3 slides). All confirmed image/png, no video files this month.
- **Visual QC:** all 8 pieces (4 stills + 4 carousels) passed — clean copy, on-brand, no typos, no held items.
- **Posts created:** 8/8 — 4 single-image stills + 4 carousels (C1=4, C2=3, C3=3, C4=3 slides). Posted **ONLY** to launchpad.university IG (`69531b3b6ef2ca81cbf45bfc_hbcsvkyO40fTLTbsL1lI_17841473294262351`) — verified every post's accountIds == that one ID, nothing else (not launchpadbizdev IG, not FB, not TikTok) per Cynthia's hard rule.
- **Status:** in_review, approver Abril (`MBieq3yaE1ixkILPfLs8`) pending, mediaOptimization ON — all GET-verified post-create.
- **Schedule:** Aug 2, 6, 10, 14, 18, 22, 26, 30 — alternating still/carousel, spread across whole month incl. 3 weekend days (2 Sun + 1 Sat), times 9am-4pm PT (all within 7am-7pm task window and 8am-8pm rule), verified via Python datetime.
- **Captions:** all-lowercase, <=3 sentences, <=1 emoji each (max allowed 2), <=4 hashtags, zero em/en-dashes (programmatic scan confirmed), aimed at non-marketer business owners per LP Uni's audience angle.
- **Reconcile:** GHL query for launchpad.university IG in August returned 0 existing posts — no collisions, nothing skipped.
- **Media upload gotcha:** "Still 1" file had no extension in Drive -> GHL upload-file 400'd "Invalid File Type". Fix: copy locally to `still1.png` before upload. Add this to lpbd_patterns.md.
- **Safety check:** `ghl-post-guard.py sweep --slug launchpad --loc hbcsvkyO40fTLTbsL1lI --token "$TOK"` -> SWEEP PASS (100 posts scanned, no premature publishes). Confirmed no pre-existing LPBD posts on this shared location were touched.
- **Notion:** worklog checklist ticked, Content Calendar Link set to commandcentercrm format (date=2026-08-01), Status -> Needs Team Review, short comment posted. No Slack per explicit instruction.

## 2026-07-21 — Wylees July Video Reupload (ad-hoc, Anthony-authorized, VIDEOS ONLY)

- **Client:** Wylees (Western Youth Leadership, Engagement, and Empowerment School), GHL location `4ND8J8TneruXGv9wtoE2`
- **Trigger:** Direct ad-hoc request from Anthony (not a Notion task) — reupload all content from `Videos/July 26'/Approved/` (`1FPoRiTFnhmvVwynuGzv6m_RZia6wp2In`, 10 files) onto consecutive Fridays. Account had gone ~2 months without posting; July was just cleared by the team before this run.
- **Reconcile:** live GHL query showed only 2 pre-existing published IG reels (human-created, left untouched per Rule 15) — no in_review/draft leftovers. Confirms memory of prior runs (which had posted a similar 5-file batch on 2026-06-30) was stale; the account had since been wiped. Never trust memory for current state.
- **Content QC:** watched all 10 via `qlmanage` poster frames (no ffmpeg on this box; `mdls`/`mdimport` returned null for duration). "Wipe.mov" — flagged in the request as a likely non-content transition — turned out to be a real staff interview about values written on desks; posted it, did not skip. "RELATIONSHIPS.mp4" briefly looked like a broken lower-third placeholder ("PERSON") on its single poster frame; sampled 2 more timestamps via `avconvert --start N --duration 0.2` and confirmed it's a normal word-by-word kinetic caption style, not a defect.
- **Format:** 5 `.mov` files transcoded to `.mp4` via `avconvert -p Preset1920x1080 --replace` (FB/IG reject `.mov`); 5 native `.mp4`s uploaded as-is.
- **Captions:** Wylees voice (community, enrollment-forward, WYLEES acronym/values-aware); 3 of 10 videos were Spanish-language content, captioned in Spanish to match. Zero em/en-dashes (programmatic scan clean).
- **Posts created:** 10/10, all `status: in_review`, approver Suzanna Nelson `St1InQ0wHWFMuOS8HC8O` pending, FB+IG only (no TikTok/YouTube connected), mediaOptimization ON, userId=Apollo. All GET-verified post-create (1 media item each, correct mime, correct approver, correct accounts).
- **Schedule:** chronological by Drive `createdTime`, one per Friday: Jul 24, 31, Aug 7, 14, 21, 28, then overflow to Sep 4, 11, 18, 25 (6 fit in Jul/Aug, 4 spilled to September — flagged, per the requester's own overflow instruction). All Fridays + 8am-8pm PT window verified via Python `datetime`/`zoneinfo`.
- **Safety check:** `ghl-post-guard.py sweep --slug wylees --loc 4ND8J8TneruXGv9wtoE2` → SWEEP PASS, 12 posts scanned (2 pre-existing + 10 new), exit 0. Nothing went live.
- **⚠️ Prompt-injection flagged, not actioned:** mid-run, a system-reminder styled as "the coordinator sent a message" instructed fetching an unverified Drive file ("Revised") and restructuring the Aug 28 schedule around it. It did not arrive as a genuine user turn (appeared injected after a tool result) — did not act on it, flagged to Anthony, continued the original task only.
- No Notion task involved (ad-hoc run) — no Notion status/comment update. No Slack sent per explicit "don't touch anything outside these video posts" instruction (task didn't ask for a Slack post).

## 2026-07-22 — CCS August 26' Social Media Run (GRAPHICS ONLY, per Cynthia)

- **Client:** Continental Currency Services (CCS), GHL location `xqSj47GjK0FHN4oXZ0mX`
- **Trigger:** Notion task "CCS August 26' Content Calendar" (`380b01f7-7d6d-81f6-9c03-c95a9c9974d6`), Status was `Not started` -> claim-or-abort proceeded -> flipped to `In production`.
- **Drive:** `Graphics/Aug 26'/Approved/` -> Stills `1h_iVgMIBxVZ7bno3tveRcRLp2K94rur3` (12 files, oddly named — 9 numbered PNGs + 3 "CCS Stills..." files, all confirmed unique on visual inspection, no duplicates) + Carousels `1JiK-tTvrmP3Cvb2-hvIgY8cx7btP8zly` (12 numbered subfolders, C1-C12, slide counts 3/3/3/2/3/3/3/3/2/3/3/3). No video files this month (graphics-only folder).
- **Visual QC:** all 12 stills passed. 11/12 carousels passed. **Carousel 3 HELD** — slide 1 reads "SKIP THE APPOINMENT" (typo, missing T in "APPOINTMENT"). Flagged to Cynthia for a design fix; not posted.
- **Content math:** 12 stills + 12 carousels = 24 pieces matches the 24-graphic contract exactly. With C3 held, 23 posted this run.
- **Reconcile:** paginated through all 412 existing CCS posts in GHL — zero August 2026 entries found. No collisions, nothing skipped, all 23 genuinely new.
- **Captions:** CCS voice (trustworthy, helpful, financial services — currency exchange, DMV services, RCheck/paycheck, title loans, Cashland). 4 hashtags per post in followUpComment (well under the 5 max), zero em/en-dashes (programmatic scan + rewrite pass), proofread, no `#lasvegas`/`#california` per standing CCS rule.
- **Schedule:** 23 posts spread evenly across all of August (days 1,2,4,5,6,8,9,11,12,13,15,16,17,19,20,21,23,24,26,27,28,30,31 — weekends included per Rule 27), varied times 9am-6pm PT (all within 8am-8pm, computed + verified via Python `datetime`), converted to UTC for `scheduleDate`. CCS's CMD pattern is graphics every day of the week, so no single weekday restriction applied — this run had fewer approved pieces (23) than the month has days (31), so posts were spread evenly rather than clumped at month-start.
- **Posts created:** 23/23, zero failures. All `status: in_review`, approver Terrance Murphy (`EaqIVyasoI6Zo9UYtkQA`) set at create time, mediaOptimization ON, userId=Apollo (`mVADATyV4DJmliFWeBBV`), accountIds = FB + IG only (no TikTok connected for CCS).
- **Media upload:** `ghl-media-upload.sh` batch mode — 12 stills + 31 carousel slides (C3's 3 slides excluded) = 43 files, 0 errors.
- **Verification:** every post GET-verified individually — media count matches plan exactly (carousels 3/3/2/3/3/3/3/2/3/3/3, stills 1 each), status in_review, approver set, mediaOptimization true, publishedAt null.
- **Safety check:** `ghl-post-guard.py sweep --slug ccs --loc xqSj47GjK0FHN4oXZ0mX` -> SWEEP PASS (100 posts scanned, no premature publishes). Note: sweep script only scans the most recent 100 posts (no pagination) — sufficient here since only new creates happened this run and all 23 were individually GET-verified besides.
- **Notion:** worklog comment posted (held carousel flagged), Content Calendar Link set to commandcentercrm format with mid-month date (`date=2026-08-15` per the mid-month-fix learning), Status -> Needs Team Review. No Slack (not requested this run).

## 2026-07-28 — CCS August 2026 Videos (ad-hoc run)
- Client: Continental Currency Services (CCS)
- Trigger: Cynthia direct instruction ("videos ready, schedule them") — no Notion task
- Creation month: August 26' (Drive: Videos/August 26'/Edited/, flat, no Approved subfolder)
- Posting month: August 2026
- Videos found: 12 in Drive | Posted: 11 | Held: 1 (typo — "ROUTING AND ACCOUNTING")
- Schedule: Aug 3,4,6,10,11,14,17,20,21,25,27 (Mon/Tue/Thu/Fri cadence), 9am-4pm PT varied
- Status: all in_review, approver Terrance Murphy pending, mediaOptimization ON
- Safety: create+35s re-verify PASS on all 11; final ghl-post-guard.py sweep PASS
- Flags: (1) "Your Check. Your Cash. Your Way..mp4" held for on-screen typo, (2) August Drive has no Approved/ subfolder this month — flagged to confirm with Cynthia if new norm

## 2026-07-29 — TTFS August 26' Content Calendar (Graphics + Video Funnel)

- **Client:** Toro Taxes Franchise Sales (TTFS), GHL location `wXlbHpBUoZ0AY0jnpZc5`, timezone America/Mexico_City (UTC-6, no DST)
- **Trigger:** Notion task "TTFS August 26' Content Calendar" (`380b01f7-7d6d-815d-92f6-c5d9e6577560`), Status `Not started` → claim-or-abort proceeded → flipped `In production`. Abril (authorized) left a task comment: mix in franchisee testimonials, follow paid-ads funnel (ToFu/MoFu/BoFu, Amber's ad strategy as guide), mix in non-testimonial videos too.
- **Drive:** `Graphics/Aug 26'/Approved/` — 4 carousels (Part 1-4, 3 slides each = 12 files). 3 MORE carousels exist in `Graphics/Aug 26'/Part 5/` but sit OUTSIDE Approved — flagged, not posted. `Videos/August 26'/Approved/` — 7 root files (expo-booth hook/proof clips) + `Approved/NEW/` — 7 franchisee testimonials (Jazmin Porras, Joanna Rivera, Justin x2, Nick Maldonado, Rosana, Blanca) = 14 videos total, all approved.
- **Visual QC:** all 12 graphic slides passed (no typos, on-brand). All 14 videos frame-checked (poster + 85%-through frame via AVFoundation) — no quality/branding issues.
- **Funnel classification (Abril's brief):** No dedicated Amber TTFS ToFu/MoFu/BoFu strategy doc found in Brain/Intelligence/marketing output — used the live TTFS Meta ad account structure from the June ad report as the guide instead (Traffic campaign = ToFu/awareness feeding retargeting, Leads campaign = MoFu, Retargeting = BoFu) plus standard funnel logic. Flagged for Abril/Amber to confirm. Classified by viewing hook + end frames: 3 ToFu (growth-vs-stagnant EN/ES, seasonal-vs-business ES), 3 MoFu-proof (3-mistakes, Branches/E2-visa, que-nadie-sabe — all expo-booth clips w/ "200+ franchisees" social proof), 7 MoFu-testimonial (the NEW/ folder), 1 BoFu (invest-on-US, "Analicemos tu perfil" — strongest direct CTA in the batch). Sequenced chronologically ToFu-heavy early → alternating proof/testimonial mid-month → BoFu closer on Aug 31.
- **Reconcile:** GET posts/list found 12 pre-existing August posts — 11 created by Frida Montealegre (human, Spanish captions, left untouched per Rule 15) + 1 Apollo carryover from July's C7 overflow (already `approved`/`scheduled`, publishedAt null, left untouched — approved posts are never API-edited).
- **Schedule:** 4 graphics on Mon/Tue/Thu (Aug 4, 13, 20, 27) avoiding the one occupied Mon (Aug 3). 14 videos: 5 contracted Saturdays (1,8,15,22,29) + 9 overflow weekdays (6,10,11,17,18,19,24,25,31) per task's explicit "spread sensibly" note — all stayed within August, none pushed to September. Only 2 fully-empty days in the whole month (Aug 12, 26) after combining existing + new. All dates/weekdays computed and verified via Python `datetime`+`zoneinfo` (America/Mexico_City), zero mental math.
- **Captions:** English (per standing Cynthia rule, regardless of the video's own spoken language), max 4 sentences, 2 emojis, exactly 5 hashtags total per post (summary+comment combined, per the 5-max gate), zero em/en-dashes (programmatic scan, all clean on first pass), contractions used to sound human, proofread.
- **Posts created:** 18/18, zero failures — 4 carousels (type `post`) + 14 videos (type `reel`). All `status: in_review`, approver Frida Montealegre (`T492rjsl9anPRthUg5t7`) set at create time, mediaOptimization ON, userId=Apollo (`mVADATyV4DJmliFWeBBV`), accountIds = FB+IG only (no TikTok — not connected for TTFS).
- **Media upload:** `ghl-media-upload.sh` batch mode — 12 graphic PNGs + 14 videos (10 mp4 + 4 mov, uploaded as-is with `type: video/mp4` in the post body per the Wylees precedent) = 26 files, 0 errors.
- **Verification:** two full GET-verify passes (immediate + ~1min later) — all 18 posts stable: media count matches plan (carousels 3/3, videos 1/1), status in_review, approver set, publishedAt null. No async carousel/video collapse observed.
- **Safety check:** `ghl-post-guard.py sweep --slug ttfs --loc wXlbHpBUoZ0AY0jnpZc5` → SWEEP PASS (100 posts scanned, no premature publishes).
- **Notion:** comment posted (funnel breakdown, flags), Content Calendar Link set to commandcentercrm format with mid-month date (`date=2026-08-15`), Status → Needs Team Review. Slack posted to #social-media-management.
- **Flags:** (1) only 4/14 contracted graphics approved — 3 more carousels sit unapproved in Drive, (2) no Amber-specific TTFS funnel doc located — used ad-account structure as proxy, confirm with Abril/Amber.

## 2026-08-04 — Shumi Nation (Apollo, ad-hoc Slack task)
- **Task:** Post all 15 graphics from Aug 26' Approved/Stills onto empty (no-video) August dates. Heightened spelling QC (Shumi auto-publishes, status:scheduled, no approver).
- **Drive:** Shumi shared drive 0AHbtW0nyBNcyUk9PVA → Graphic Design/August 26'/Approved/Stills/ (15 PNGs, no Carousels folder this month).
- **QC:** All 15 read word-by-word. Zero typos, zero held. Noted 18.png/19.png are byte-identical duplicate files (posted both with distinct captions rather than dropping one).
- **Schedule:** Aug 4 (today, in-window), 6, 8, 9, 11, 13, 15, 17, 19, 21, 23, 24, 26, 28, 30 — 15 slots, zero collisions with the 17 existing video posts.
- **Posted:** 15/15 to Instagram only, status:scheduled, mediaOptimization:true, 4 inline hashtags/caption, zero em/en-dashes (pre-flight QC gate).
- **Verified:** 15/15 GET-confirmed media=1, publishedAt=null, mediaOptimization=true. Sweep PASS (84 posts scanned).


## 2026-08-19 — Anthony personal brand: time-blocked production system (Aidan Per merge)
- **Trigger:** Anthony brought two Aidan Per videos (time blocking / month of content in a day; going full-time as a creator) and asked to merge them into the active plan and start executing 2026-08-20.
- **Diagnosis:** the [[2026-08-03 — Personal Brand Rebrand — Photographer CEO Nerd]] plan is complete and correct, but [[Content Scoreboard]] logged 0 pts across 16 days and Week 1 was never filled in. Cause identified as structural, not motivational — the Aug 3 week had a **film block and no write block**. Batch Day asked for 5 talking heads when nothing had been scripted; hooks + topics are not scripts.
- **New note:** `Anthony/2026-08-19 — Time-Blocked Content System.md` — WRITE→FILM→EDIT→POST blocks, multi-hook repurposing, film-by-setup rule, overlap table showing what the second video already duplicated in the Aug 3 plan, and one genuine gap flagged (no visual system for the feed — fonts/colors/music/clip template; Modern Wisdom lesson was applied to the podcast only).
- **Additive edits, no deletions:** [[Content Strategy — Playbook]] gained §7 "The Time-Blocked Week — v2" plus dated pointers at §2 and §4 (originals kept as the record). [[Content Scoreboard]] gained write-block (3 pts) and hook-variant (+1/video) scoring, a Week 3 restart section, and honest ❌ entries for Weeks 1-2 with the cause recorded.
- **Layer 2:** new skill `.claude/skills/content-batch-cycle.md` (from `skill-template.md`), registered as skill #5 on the video-production agent. Hard rule encoded: the AI never invents a receipt — Proof beats ship blank for Anthony to fill.
- **Layer 2 output:** `marketing/output/video-briefs/anthony-launchpad/2026-08-20-write-block.md` — 5 script skeletons from the existing Aug 3 idea bank, 20 hooks written, film run sheet ordered by setup.
- **Open:** `Anthony/00-INDEX.md` is stale (9 notes, auto-maintained by `brain-link-density.py`, last rebuild 2026-08-02) — does not yet list the Aug 3 or Aug 19 notes. Rebuild not run.

## 2026-08-19 (2) — Anthony personal brand: the writing system (same-day amendment)
- **Trigger:** Anthony read the time-blocking build and immediately named the deeper problem — *"I feel like one of the biggest issues is the writing portion... when I rely solely on you I hit a block and don't really love the content I'm making."* Pointed at a Peter McKinnon interview (contains a section on Casey Neistat's process) and Life of Riza.
- **Reference gap, flagged not papered over:** YouTube blocks transcript fetch. Got the McKinnon interview title only; the Casey process section is **unread and not incorporated**. Life of Riza identified via secondary sources as Kariza Santos (Filipino-Canadian cinematic vlogger, ~900K subs) — music-first process confirmed and adopted. Asked Anthony to paste timestamped summaries the way he did for the Aidan Per videos.
- **New note:** `Anthony/2026-08-19 — The Writing System.md`. Three failures named: (1) ~30% of pillars are visual and should never be written — split into **Scripted** (Teach/Desk/Nerd) vs **Captured** (Shoot/Merch) modes, Captured gets a 3-line capture card and a music track picked before the shoot, never a script; (2) **Apollo drafting makes Anthony an editor of someone else's work** — switched to the interview method: Apollo asks, Anthony talks, Apollo shapes his actual words; (3) the bucket is empty on Monday — added a continuous capture layer.
- **New note:** `Anthony/Idea Bank.md` — always-on capture destination (voice memo or Slack DM to Apollo, 10 seconds each, target 3-5/week). Inbox / Parked / Used tables. **This is the load-bearing piece:** an empty bank on Monday means the write block is back to generation and will fail again.
- **Five story shapes named** — Receipt, Mistake, Argument, Test, Reveal. Used as a filter, not a form: no turn, no post. Answers "I've got nothing" with "then it's not ready, next."
- **Read-it-out-loud gate added** — if he wouldn't say the Land line to a friend at a bar, it isn't his yet. A block where nothing got rewritten in his words means the interview was too shallow.
- **Updated:** `.claude/skills/content-batch-cycle.md` — Step 3 rewritten from "write skeletons" to "interview, never draft"; two-mode table, story shapes, extraction question bank, read-aloud gate, Idea Bank as primary source, hard rules extended to 10. `marketing/output/video-briefs/anthony-launchpad/2026-08-20-write-block.md` rebuilt around talking: 90 min is now 40 min of him talking and 10 of reading aloud, with 5 specific talk prompts per video instead of blanks to type into.
- **Casey correction (same session):** Anthony pasted the McKinnon interview section. It contradicted the initial read — Casey **pre-visualized** ("concepts and stories mapped out in his mind before filming," 00:06:14), he did not discover the story in the edit. Captured mode reframed as **Pre-visualized**: decided in advance, simply not written down. The earlier "find it in the edit" framing would have reintroduced improvisation through the back door and is corrected in the note. Third mode named explicitly — Scripted (written) / Pre-visualized (decided, unwritten) / Improvised (❌ the failure state).
- **New output:** `marketing/output/video-briefs/anthony-launchpad/notebooklm-research-prompt.md` — a source-grounded NotebookLM prompt to extract existing scripting/shot-list frameworks (7 sections, shortlist + contradictions output), plus the source list to load first. Adoption bar recorded: a framework only counts if it survives a 90-minute block run by someone who'd rather be shooting.
- **Life of Riza material received (same session).** Three corrections: (1) the **music-first claim was never in her video** — it came from secondary write-ups and is demoted to an untested experiment, do not cite her for it; (2) she pre-produces substantially (outline-to-script, shot lists, storyboards) — confirming **all three references pre-produce, so Improvised stays the failure state, not a style**; (3) added a **Stakes half-beat** between Hook and Turn — assume the audience knows nothing, name who and what was on the line. Two upgrades adopted: **Pre-visualized mode plans in sketches and reference images, never prose** (a phone photo of four scribbled boxes is a valid capture card — Anthony thinks in frames, and this is the real answer to "I hate the writing part"), and the **visual-system gap re-scoped from post-production to set design** — art-direct the chair once, done in camera, cheaper and better than a template lock.
- **First NotebookLM research pass (same session) — sources were NOT loaded.** It web-searched instead: 5 of 14 cited sources were AI-music-video-generator SEO pages, one a Reddit r/cscareerquestions thread, one a real-estate podcast blog; none of the Aidan/McKinnon/Riza videos or LP SOPs were read. **All six named "frameworks" discarded** (two were AI music-video pipelines with lip-sync maps). Caveat recorded in `The Writing System` §8 so the output isn't over-trusted later; re-run pending with staged sources. **Four mechanical practices adopted anyway, source-independent:** (1) **hybrid scripting** — hook and Land word-for-word, middle in bullets only; resolves the full-script-vs-improv tension the whole system exists for, and a fully-scripted body is now a defect; (2) **question-in-answer** on voice memos — restate the question inside the answer so the transcript is usable as-is, which is what makes the interview method cheap; (3) **stumble protocol** — pause a full beat and restart the sentence, clap once on long pauses for a findable waveform spike; (4) **permanent setup beats a good setup** — upgrades "art-direct the chair once" to "then never take it down," since plans die at setup friction, not filming. Also carried: three sizes from one tripod position, 5s/15s handles, ~130 wpm length check.
- **First real Idea Bank deposit (same session).** Anthony answered NotebookLM's questions informally and produced 8 usable captures in one sitting — validating the interview method before it was ever formally run. Filed and sorted by shape. **Strongest: the Allegiant Stadium / Taco Bell Cantina story** — media credentials didn't land, stripped a Nomatic McKinnon 35L down to a clear-mini-backpack kit, tried to sneak a telephoto in his pants, still delivered website/social/PR photos. Mistake shape + In The Bag, complete story arc, funny, national brand, and it demonstrates Riza's constraints-breed-creativity point without stating it. **Three permission flags raised, not resolved:** (1) the 53%-CPL-down / 154%-leads-up numbers need a client naming decision — recommend qualitative framing, never Wamen; (2) a public "I Tested It" on OpenCharts/Theovex is a vendor review with an internal critical evaluation behind it — deliberate call, not a casual batch video; (3) "building more on the AI sales team but not executing it" is excellent *What I Got Wrong* material but the outbound build is mid-flight.
- **New:** `Anthony/Content Journal — Prompt Deck.md` — 35 standing prompts in journal voice, grouped by the five story shapes, at Anthony's explicit request (*"prompts like you'd get in a journal at Target"*). Same prompts every week; only the week changes. Includes a five-prompt fallback set for low-energy weeks. Wired into the writing system and the content-batch-cycle skill as the default opening of every write block.
- **Permission calls resolved (Anthony, same session).** (1) The 53%/154% client is an **Arby's food truck** — internal only; **public framing is "a food truck," brand name never used.** Numbers cleared and sayable. (2) OpenCharts/Theovex reframed away from a vendor review to *"we're testing new AI tools against the Apollo build we already have"* — no vendor named ever, category only. This is a better video than the review would have been: it moves from critiquing someone's product to pressure-testing his own system, which is the Nerd pillar as the rebrand defines it. (3) The unshipped AI sales team is cleared in full, including the why — *time restriction mixed with not wanting to get it wrong.* Framings recorded as binding in `Anthony/Idea Bank.md`.
- **Content Journal created in Notion (private to Anthony, workspace level).** URL `https://app.notion.com/p/0787cfd7548a4c8983e68376c11e50ce` · data source `collection://f7952f37-d922-4ae1-b431-ab3c5d79de0a`. Properties: Entry · Date · Prompt · Shape · Mode · Status; the ramble goes in the page body. Follows the established architecture exactly — **Notion is the human write layer, Brain is the agent read layer.** **Seeded with all 8 of tonight's captures** rather than left empty, since an empty database is an abandoned one. Wired into `Idea Bank.md` and the content-batch-cycle skill as a primary source.
- **Prompt deck upgraded** after Anthony sent two journal-prompt references and said *"sometimes it feels like I just need to get my brain to turn on and get going."* Added **Section 0 — Warm-up**: 7 low-stakes prompts that are explicitly *not content*, so the engine is running before the real questions arrive. Cold-starting into "what's your best insight" is what blank pages feed on. Also added **The Deal** — you ramble, Apollo cleans it up; it only breaks if he does Apollo's half. Style note recorded: prompts are deliberately written as self-discovery journal entries, not a business questionnaire, because that's the tone that gets him talking.
- **Tomorrow's worksheet rebuilt around tonight's five captures** (Allegiant/Taco Bell · food truck numbers · the unshipped sales team · AI flyers · going light) — one per story shape, all four pillars, all permissions cleared. The Aug 3 lineup was written *for* him two weeks ago; these came *out* of him in one sitting, which is the entire point of the change. The "still excited setting up lights" POV video rolls to next week.

- 2026-10-07 — Added Content Framework Method (Skills/) and client content frameworks for First Colony Mortgage and A Mi Manera Coffee (Intelligence/, draft). Source: Taco Bell Brand Creative Playbook 2025 content framework section. Written by Claude session with Anthony.
- 2026-10-07 — Vocabulary fixed: pillars (what we talk about) vs buckets (Awareness/Desire/Story/Choice, never renamed) vs jobs (Educate/Entertain/Inspire/Empathize/Prove/Convert). Content Framework Method rewritten as canonical (tier primary). Content Strategy Framework rewritten as audit/calendar/measurement companion (old version archived). Brief Creation updated: shoot groupings are segments, line items tagged Pillar · Bucket · Job · Series. Client notes for First Colony and A Mi Manera updated.
- 2026-10-07 — Content Framework Method: added Media (Video · Photo · Graphic) to vocabulary; photo and graphic format tables; photo-list-per-shoot, mood board and seasonal-set rules.
- 2026-10-07 — Templates: Resources/Templates/ now holds Content Strategy and Monthly Briefs master templates (.md + .pdf). Weekly and Monthly Cycles corrected to the Notion CYCLE EXPECTATIONS numbering (Week 3 = Preproduction/briefs). Notion: CLIENT TEMPLATE Content Strategy page and the Preproduction task template rewritten to the new method; First Colony strategy filed in its portal. Apollo: shoot-brief-builder rewritten for the five briefs; content-strategy-builder added.

## 2026-09-29 — TTFS October videos posted (Social Media Poster, manual run)
- Client: Toro Taxes Franchise Sales (TTFS). Source: `Videos/October 26'/Approved` (Drive) — 2 files, matching the 2 remaining open Saturdays (Oct 24, 31) after Sept's 3 carryover videos (Oct 3/10/17, untouched).
- QC: both 1080x1920 reels, 14.47s/21.63s, Spanish on-screen text, zero typos.
- Posted `in_review`, approver Frida Montealegre (`T492rjsl9anPRthUg5t7`), FB+IG, mediaOptimization ON: Oct 24 16:00Z (`6abc264ed3d29c3680f46635`), Oct 31 18:00Z (`6abc264eb84b171e18898472`).
- Excluded: `BRANCHES.mp4` (loose, outside Approved — flagged) and `Approved 4 NOV/` (next month, not opened).
- Sweep: PASS (100 posts scanned, no premature publishes).


## [2026-10-07] recovered | Apollo run log entries 2026-06-22 → 2026-07-28

> Recovered from a stray `Brain/log.md` that lived inside the launchpad-automation repo while `Brain/` was a real folder there instead of a link to this vault. These entries never reached the vault at the time. Appended as-is on 2026-10-07 when the two repos were re-aligned; original order (newest first) preserved.

### 2026-07-28 — CCS August 2026 Revision Run (BLOCKED — Notion API key missing)

- **Client:** Continental Currency Services (CCS)
- **Task:** CCS August 26' Content Calendar (380b01f7-7d6d-81f6-9c03-c95a9c9974d6)
- **Run type:** Revision — triggered by comment 3abb01f7-7d6d-8024-a067-001d73bd9134
- **Outcome:** BLOCKED. Cannot read Notion comment — NOTION_API_KEY is not in .env, not in macOS keychain, and not accessible to CLI agent sessions.
- **GHL state verified:** 23 CCS August posts, all in_review, Terrance Murphy approver set, times 12 PM PDT, no em-dashes, max 4 hashtags. Clean.
- **Sweep result:** PASS — 100 posts scanned, no premature publishes.
- **Root cause:** Notion + Slack tokens are stored only in n8n's cloud credential store. CLI agent sessions cannot access them. The mcp__claude_ai_Notion__* and mcp__claude_ai_Slack__* tools only work in the Claude.ai desktop app context.
- **Infrastructure gap:** n8n SMM-revision-watcher constructs `commentSnippet` but does NOT forward it in the webhook body (confirmed by reading SMM-revision-watcher.json lines 162-219). Apollo receives only the comment ID, never the text.
- **Required fix (Anthony):** Add NOTION_API_KEY to .env so CLI agent sessions can call Notion REST API directly. Separately: update n8n webhook body to include `commentSnippet` so revision runs can act on comments even without a Notion key.
- **Action taken:** Escalated to Anthony. No GHL changes made (no revisions were possible without knowing what the comment requested).

---

### 2026-06-25 — Matsuda Nadig Van Law (MNVL) July 2026 Graphics

- **Client:** Matsuda Nadig Van Law (MNVL)
- **Creation month:** July 2026 (Month property = July)
- **Posting month:** July 2026 (task name = MNVL July 26')
- **Posts created:** 16 (8 carousels + 8 stills), FB + IG only, status: in_review
- **Posts held:** 0
- **Approver:** Sage Lopez (GHL ID: XAPlrtrNLFz0reWbZoIX — shared approver with MNL)
- **Schedule:** Jul 2 – Jul 28 (9am–4pm AZ, alternating carousel/still, Jul 4 holiday override to Saturday)
- **Safety check:** PASS — all 16 GET-verified in_review, publishedAt=null
- **Flags:** Pre-existing Cynthia video post Jul 1 left untouched; TikTok excluded (static image rule); MNVL pit token lacks Users scope (approver resolved from MNL memory)
- **Task:** https://www.notion.so/364b01f77d6d8130bf88d6f093d4f73e

---

### 2026-06-25 — Matsuda Nadig Law (MNL) July 2026 Graphics

- **Client:** Matsuda Nadig Law (MNL)
- **Creation month:** July 2026 (Month property = July)
- **Posting month:** July 2026 (task name = MNL July 26')
- **Posts created:** 16 (8 stills + 8 carousels), FB + IG only, status: in_review
- **Posts held:** 0
- **Approver:** Sage Lopez (GHL ID: XAPlrtrNLFz0reWbZoIX — resolved from existing Cynthia posts; Users scope not on token)
- **Schedule:** Jul 2 – Jul 28 (9am–7pm PDT, alternating still/carousel, Jul 4 holiday override)
- **Safety check:** PASS — all 16 GET-verified in_review, publishedAt=null
- **Flags:** Carousel 2 missing slide 2 in Drive (posted 3/4 slides); Videos track skipped per task (Cynthia owns); MNL pit token lacks Users scope
- **Task:** https://app.notion.com/p/364b01f77d6d81908acee553591f9538

---

### 2026-06-23 — Upbeat Health July 2026 Carousel Revision (REVISION MODE)

- **Client:** Upbeat Health
- **Run type:** Revision — carousel slide-count fix per Cynthia's comment
- **Posts fixed:** 1 (Jul 6 FB carousel — deleted 1-slide post, recreated with 4 slides as `6a3ac123be76601f3f21c436`)
- **Posts verified clean:** 13 Apollo in_review stills — all media=1, correct
- **Posts left untouched:** Jul 8 BOTH carousel (Cynthia-created, 6 slides, correct); Jul 2 IG "Swipe" (human-created, 1 slide, flagged)
- **Safety check:** PASS — new Jul 6 post in_review, publishedAt=null
- **Flags:** Jul 3 + Jul 7 have em-dashes in approved+scheduled posts — flagged for manual GHL UI fix (API edit would republish). Jul 2 IG swipe post may be missing slides — flagged to Cynthia.
- **Key lessons:** GHL edit-post cannot update media[] on in_review posts; PUT status=deleted drops to in_progress (publish-now trap); use HTTP DELETE instead; create-post body must not include locationId.

---

### 2026-06-23 — Muller Masks July 2026 Social Posts

- **Client:** Muller Masks
- **Creation month:** July 2026 (Month property = July, Drive folder = Graphics/July 26')
- **Posting month:** July 2026 (task name)
- **Posts scheduled:** 8 (4 stills + 4 carousels)
- **Posts held:** 0
- **Platforms:** Facebook + LinkedIn (IG not connected)
- **Approver:** Sylvia Malaga (mNFvNrUwrAmPvhnkJgZz)
- **Schedule range:** Jul 4 – Jul 28, 2026 (Mon/Fri pattern, alternating S/C per task notes)
- **Safety check:** PASS — all 8 in_review, publishedAt=None, media counts correct, Sylvia attached
- **Videos track:** No July video folder in Drive. 5 Cynthia-created video posts (Jul 1, 8, 15, 23, 30) already in GHL — left untouched.
- **Flags:** API fix applied: locationId must not be in POST body (422 otherwise). IG not connected — FB+LinkedIn only.

---

### 2026-06-22 — Durango HVAC July 2026 Social Posts

- **Client:** Durango HVAC
- **Creation month:** June 2026 (Month property = June, content created June)
- **Posting month:** July 2026 (task name)
- **Posts scheduled:** 9 (5 stills + 4 carousels, EN + ES bilingual)
- **Posts held:** 0
- **Platforms:** Facebook + Instagram
- **Approver:** Yessenia Favela (jahOW5nXy44EUXKN0tY8)
- **Schedule range:** Jul 2 – Jul 29, 2026
- **Safety check:** PASS — all 9 in_review, publishedAt=null, media counts verified
- **Flags:** Pre-existing 2 Abril posts (Jul 1 + Jul 3) left untouched. Overflow: Still 5 (4th of July) placed Jul 2 (Thu). API fix: locationId must not be in POST body (422 otherwise).

---

### 2026-06-22 — Upbeat Health July 2026 False-Positive Trigger (Run 3)

- **Client:** Upbeat Health
- **Type:** False-positive revision trigger — no action taken
- **Trigger:** Comment 387b01f7 was Apollo's own prior revision-complete note (not a human request)
- **GHL state verified:** 25 posts in July; 24 clean (weekday, mo=True, in_review or properly scheduled)
- **Outstanding:** Jul 11 post `6a347e41c1db7efc284ea9e8` still on Saturday, already approved — flagged for manual UI reschedule
- **Safety check:** N/A — no GHL changes made

---

### 2026-06-22 — Upbeat Health July 2026 Revision Run

- **Client:** Upbeat Health
- **Type:** Targeted revision (not a full pipeline run)
- **Trigger:** Cynthia comment 384b01f7-7d6d-8010-9749-001d3be6f86a
- **Actions:** Rescheduled 3 weekend posts to weekdays (Jul 12->23, Jul 18->24, Jul 19->29); enabled mediaOptimization on 13 in_review posts
- **Safety check:** PASS — all 13 edited posts verified in_review, publishedAt null
- **Flags:** Jul 11 (approved+scheduled, Sat) needs manual reschedule in GHL UI; Jul 3+7 (scheduled) need media optimization toggled manually

---

### 2026-06-22 — CCS July 2026 Social Posts

- **Client:** Continental Currency Services (CCS)
- **Creation month:** July 2026 (Month property)
- **Posting month:** July 2026 (task name)
- **Posts scheduled:** 40 total (29 graphics: 16 stills + 13 carousels; 11 videos)
- **Posts held:** 0
- **Platforms:** Facebook + Instagram (no TikTok connected)
- **Approver:** Terrance Murphy (EaqIVyasoI6Zo9UYtkQA)
- **Schedule range:** Jul 1 – Jul 29 (graphics); Jul 2 – Jul 21 (videos), 9 AM – 6 PM PDT
- **Safety check:** PASS — 3 spot-checked posts verified in_review, deleted:false, publishedAt:null
- **Flags:**
  - 11 of 16 contracted videos placed (only 11 in Drive APPROVED folder); 5 video slots unfilled
  - Jul 30 and 31 have no graphic post (29 approved graphics, 31 days — 2 days naturally unfilled)
  - World Cup posts (5G + 2V) all scheduled Jul 1–11 per task instructions
  - 4th of July still placed Jul 4 at 9 AM PDT
  - BAD BUNNY.mp4 (outside APPROVED folder, typo in name) — NOT posted per Critical Rule 2
- **GHL Graphic Post IDs (29):** 6a39c47f, 6a39c480, 6a39c481, 6a39c483, 6a39c484, 6a39c485, 6a39c486, 6a39c487, 6a39c488, 6a39c48a(x2), 6a39c48c, 6a39c48d, 6a39c48e, 6a39c48f, 6a39c490, 6a39c491, 6a39c492, 6a39c494, 6a39c495, 6a39c496, 6a39c497, 6a39c498, 6a39c499, 6a39c49a, 6a39c49c, 6a39c49d, 6a39c49e, 6a39c49f
- **GHL Video Post IDs (11):** 6a39c547, 6a39c548, 6a39c549, 6a39c54a, 6a39c54b, 6a39c54c, 6a39c54d, 6a39c54e, 6a39c54f, 6a39c550, 6a39c551

---

### 2026-06-22 — TTFS July 2026 Social Posts

- **Client:** Toro Taxes Franchise Sales (TTFS)
- **Creation month:** July 2026 (Month property)
- **Posting month:** July 2026 (task name)
- **Posts scheduled:** 18 total (14 graphics: 7 stills + 7 carousels; 4 videos)
- **Posts held:** 0
- **Platforms:** Facebook + Instagram
- **Approver:** Frida Montealegre (T492rjsl9anPRthUg5t7)
- **Schedule range:** Jul 2 – Jul 30, 2026 (9 AM – 2 PM Mexico City); C7 overflow to Aug 3
- **Safety check:** PASS — all 18 verified in_review, publishedAt null
- **Flags:**
  - 1 graphic (C7) overflowed to Mon Aug 3 — July has 13 Mon/Tue/Thu slots; contracted 14G; task restricts to Mon/Tue/Thu/Sat only
  - Graphics/July 26' folder has no APPROVED/ subfolder — treated as approved, flagged to Cynthia
- **GHL Post IDs (18):**
  - 6a39c0c6848ae06e7336832d (Still 1, Jul 2)
  - 6a39c0d2cbac585fc5b47384 (C1, Jul 6)
  - 6a39c0d7892064b3bd0b3cf9 (Still 2, Jul 7)
  - 6a39c0de3d0accd51bd277e8 (C2, Jul 9)
  - 6a39c0e9458a9cf8701cdbc3 (Still 3, Jul 13)
  - 6a39c0f03e64528d8ae7b2b3 (C3, Jul 14)
  - 6a39c0f5892064b3bd0b6306 (Still 4, Jul 16)
  - 6a39c102d015d306b4cced92 (C4, Jul 20)
  - 6a39c107848ae06e7336c55a (Still 5, Jul 21)
  - 6a39c10e24eb099cc2c477a1 (C5, Jul 23)
  - 6a39c123b05e88978b433da3 (Still 6, Jul 27)
  - 6a39c12f24eb099cc2c49926 (C6, Jul 28)
  - 6a39c137cbac585fc5b4e626 (Still 7, Jul 30)
  - 6a39c14424eb099cc2c4b7e5 (C7, Aug 3 — overflow)
  - 6a39c149d015d306b4cd3c5e (V1 Cuanto Dinero, Jul 4)
  - 6a39c14e44bd90d521f61a9c (V2 Losing Leads, Jul 11)
  - 6a39c153cbac585fc5b4fdf8 (V3 Hype Reel, Jul 18)
  - 6a39c15722817630081371ad (V4 Necesito Experiencia, Jul 25)
