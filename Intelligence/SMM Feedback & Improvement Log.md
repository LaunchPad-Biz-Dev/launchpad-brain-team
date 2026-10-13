---
title: SMM Feedback & Improvement Log
type: intelligence
tags: [smm, social-media, apollo, process-improvement, cynthia]
created: 2026-06-23
related: ["[[SMM Posting Calendar Patterns]]", "[[Social Media Workflow — Agency Current Process]]", "[[Intelligence/00-INDEX]]"]
---

# SMM Feedback & Improvement Log

Living log of what Cynthia (SMM lead) flags, the fixes/revisions she requests, and — the point of this note — the **systemic change** that stops each from recurring so Apollo's posting pipeline gets more seamless over time.

**Owner:** Apollo logs here; Anthony + Cynthia drive the calendar work. Actionable per-run rules also live in agent memory `.claude/agent-memory/social-media-poster/` ([[cynthia_review_rules]] + per-client `*_patterns.md`). This note is the *why it keeps happening + how to remove it* layer.

Read each entry as: **Problem → Fix applied (where the rule now lives) → Seamless move (the upstream/automated change that removes the manual revision).**

---

## Recurring themes → systemic backlog

### 1. Calendar links not clickable / wrong destination — ✅ resolved
- **Problem:** Apollo wrote `app.msgsndr.com` links; Cynthia couldn't open them (LP GHL is white-labeled). Flagged 2026-06-18 + 2026-06-22.
- **Fix:** correct format `https://app.commandcentercrm.com/v2/location/{LOCATION_ID}/marketing/social-planner/planner?tab=calendar&date={YYYY-MM-01}`, written to the Notion "Content Calendar Link" field. In [[cynthia_review_rules]].
- **Seamless move:** ✅ standing default — every run writes the clickable link automatically.

### 2. Media optimization off on most clients — ✅ resolved
- **Problem:** posts weren't getting `mediaOptimization` → wrong format per platform. Flagged 2026-06-22 across clients.
- **Fix:** set `mediaOptimization=true` on every post (GET to verify; list endpoint hides the field). Already-approved posts can't be API-edited without republishing → flagged for manual UI toggle.
- **Seamless move:** ✅ now ON by default, every post, every client.

### 3. Schedule fidelity (right days, all content in-month, every slide) — ⚠️ partly open
- **Problem:** missed Wednesdays (BWU), Thursday videos that should be Wednesday, weekend posts that should be weekdays (Upbeat), overflow pushed to *next month* (TTFS C7 → Aug 3), carousel slides 2+ never posted (BWU June).
- **Fix:** post the exact calendar days; only move for holidays; post ALL in-month content (add an in-month weekday before spilling to next month); post every carousel slide. In [[cynthia_review_rules]].
- **Seamless move (OPEN):** the per-client cadence (e.g. BWU = Mon/Fri graphics + Wed video) lives in task-body notes + the **Content Monthly Deliverables** page. Apollo should treat that deliverables calendar as schedule source-of-truth and run a **pre-submit schedule check** (validate each post's day against the client pattern) before routing to the approver — would prevent most day-placement revisions.

### 4. False-positive revision triggers (channel/queue noise) — ✅ resolved
- **Problem:** the n8n revision watcher fired on Apollo's OWN comments (posted under Anthony's Notion identity via the MCP), looping no-op runs and burning the Mac Mini.
- **Fix:** content-signature filter published live 2026-06-23 (skip comments that self-label as Apollo / contain machine markers). See [[project_smm_revision_watcher_false_positives]].
- **Seamless move:** ✅ done + verified.

### 5. Run reliability — fast-fail loop — ⚠️ open
- **Problem:** CCS/TTFS new runs errored in ~10s for 3 hours (2026-06-22 ~20:00–22:00) before finally succeeding; each failed run left the task "Not started," so the :00 watcher re-fired it hourly.
- **Fix (OPEN):** root cause not yet captured — the listener only saves `stderr`, but the claude error went to `stdout`. Proposed: (a) listener logs `stdout` tail on failure + Slack-pings Anthony; (b) n8n marks the task "In production" the moment it fires so a dead run doesn't re-fire. Host is an 8GB soldered M2 Mini (can't add RAM) — moving n8n to n8n Cloud is the real relief.
- **Seamless move:** pending Anthony's go on the listener logging/alert change.

### 6. Drive structure gaps — ⚠️ open
- **Problem:** some July client folders had no `APPROVED/` subfolder (TTFS), so Apollo had to infer approval.
- **Fix:** flagged to Cynthia/designers per run.
- **Seamless move (OPEN):** standardize `{Client}/Graphics|Videos/{Month YY'}/APPROVED/` for every client; a Drive-structure pre-check could warn when a month folder lacks APPROVED before Apollo even starts.

---

## Session log (dated)

### 2026-06-23 — live session (Anthony + Cynthia working calendars)
Baseline set 2026-06-23 ~10:15 AM PDT. Apollo appends new problems/fixes/revisions Cynthia raises below.

**~10:06–10:12 AM PDT — Cynthia revision batch (Anthony driving, Apollo fixing):**
- **Upbeat** — a carousel on Jul 6 posted with only ONE slide. → Recurring (see theme #3; same as BWU June). Fix: revision run to rebuild with all slides.
- **CCS** — remove `#lasvegas` + `#california` hashtags. Fix: revision run + rule added to `ccs_patterns.md` (overrides the task-note examples that listed those tags).
- **Durango** — 4th of July graphic scheduled on Jul 2 → move to Jul 4 (holiday). AND link still not clickable. Fix: revision run + set the commandcentercrm link.
- **Muller** — graphics should be Mon/Fri; July videos need status `in_review` for Sylvia. Fix: revision run.

**Pattern insight (for seamless-ness):**
1. **Link fix didn't propagate to all clients.** I only set the commandcentercrm link on the 4 clients from yesterday's list — Durango/Muller still had old/no links, so Cynthia still couldn't click them. → *Seamless move:* one-time sweep to set the correct link on EVERY active client task, not just the ones being revised (agent now writes it by default, but existing tasks need backfill).
2. **Carousel-missing-slides keeps recurring** (BWU June, Upbeat July). This is the strongest candidate for an automated **pre-submit check**: compare each carousel post's slide count to the Drive carousel folder's file count and block/flag a mismatch before routing to the approver.

**~10:35 AM PDT — verification + new findings:**
- **Fixes landed:** CCS ✅ (43 hashtags removed), Durango ✅ (4th of July → Jul 4 + link set), Upbeat ✅ (Jul 6 carousel rebuilt w/ all 4 slides). Muller 🔧 running (graphics Sat/Tue → Mon/Fri + videos→in_review for Sylvia).
- **NEW — em-dashes slipped through on Upbeat Jul 3 + Jul 7** despite the no-em-dash standing rule, and those posts are already approved so Apollo can't API-fix them (would republish) → manual UI. *Seamless move:* strip em-dashes at caption GENERATION (never emit one); add a pre-submit caption lint that rejects any `—`.
- **NEW — Muller's fresh run placed graphics on Sat/Tue, not contracted Mon/Fri.** The pattern is in `muller_patterns.md` but the NEW-run agent didn't honor it → reinforce + the pre-submit schedule check (theme #3).
- **NEW — possible DOUBLE-ACTIVE watcher.** A Muller revision fired from the :30 poll at 17:30 UTC on Apollo's own run-complete comment, *after* the fixed watcher was published — most likely the OLD "SMM Revision Watcher" is still Active alongside the imported fixed one. Action: confirm old workflow is Inactive/deleted. Flagged to Anthony.
- **Meta-pattern:** "already approved" is now the main blocker — once a post is approved, Apollo can't safely edit it (republish risk), so every fix becomes a manual UI task. The seamless system gets QC RIGHT before approval: links, all carousel slides, no em-dashes, media-opt ON, correct days — all validated pre-submit.

**~10:50 AM PDT — two more findings:**
- 🔴 **CRITICAL — the agent can't reliably compute day-of-week.** The Muller revision claimed "all 8 graphics already on Mon/Fri" and skipped the reschedule — but they were on **Sat/Tue** (Jul 4=Sat, Jul 7=Tue). It mislabeled the weekdays in its own head and silently passed a wrong schedule. → *Seamless move (high priority):* NEVER trust the LLM's mental day-of-week math. Compute weekdays deterministically (Python/date util) and pass EXACT target dates. The pre-submit schedule check must use a real calendar, not a guess. Re-fired Muller with explicit target dates (Jul 3/6/10/13/17/20/24/27).
- **Durango video policy CHANGED:** Cynthia now wants Apollo to post Durango videos (Drive `Videos/July 26'/Approved`) on **Fridays** — overrides the old "Apollo doesn't post Durango videos" rule. Captured in `durango_patterns.md`. Posting now.
- **Watcher still double-firing (confirmed):** a Muller false-positive revision ran at 17:40 UTC off Apollo's own run-complete comment, *after* the fixed watcher was published → the OLD "SMM Revision Watcher" is still Active. Anthony to deactivate it.

**~11:14 AM PDT — Durango overflow videos (clean exception, not a defect):**
- Cynthia: post 2 more Durango videos ("WHY", "WHAT WE DOIN") on **Jul 18 + Jul 25 (Saturdays)** due to a video overflow. She gave exact dates + explicitly chose Sat. → Fixed (firing). *Note:* this is an authorized exception to the Friday rule, not a bug. Logged so the rule reads: Durango videos default Fridays, BUT honor Cynthia's explicit date overrides for overflow. Also note: she gave EXACT dates — that's the friction-free pattern (no weekday math needed).


---

## 📋 Session summary — 2026-06-23 (Anthony + Cynthia live calendar session)

**What got fixed today (per client):**
- **BWU** — Thursday videos → Wednesday; media optimization on all 14; clickable link.
- **CCS** — World Cup video Jul 18 → Jul 1; media optimization on all 40; removed #lasvegas + #california (43 tags); clickable link.
- **TTFS** — media optimization on all 18; C7 left on Aug 3 (Cynthia's call); clickable link.
- **Upbeat** — weekend posts → weekdays Jul 23-31; media optimization; Jul 6 carousel rebuilt with all 4 slides; clickable link. *(Manual-UI leftovers: Jul 2 IG carousel slides, Jul 3/7 em-dashes — approved posts Apollo can't API-edit.)*
- **Muller** — graphics rescheduled to true Mon/Fri (Jul 3/6/10/13/17/20/24/27); 5 videos → in_review for Sylvia; clickable link.
- **Durango** — 4th-of-July graphic Jul 2 → Jul 4; clickable link; **6 videos posted** (4 Fridays Jul 3/10/17/24 + 2 Saturday overflow Jul 18/25 per Cynthia).

**Standing rules captured in agent memory this session:** clickable-link = commandcentercrm format; media-optimization ON by default (all clients); CCS no #lasvegas/#california; Durango Apollo-posts-videos (Fridays, + honor explicit date overrides); per-client cadences reinforced.

**Prioritized systemic backlog (to make the pipeline seamless):**
1. **Pre-submit QC check** *(highest leverage)* — before routing to the approver, validate: carousel slide-count == Drive folder count; calendar link present + commandcentercrm domain; no em-dashes; mediaOptimization ON; **posting days correct vs a REAL calendar** (not LLM weekday math). Most of today's revisions would never have been needed.
2. **Deterministic date/weekday handling** — the agent mis-computed weekdays (claimed Sat/Tue posts were "Mon/Fri") and silently passed a wrong schedule. Never trust LLM day math; compute via a date util and pass exact target dates.
3. **One-time clickable-link backfill** across ALL active client tasks (the fix only reached clients being revised; Durango/Muller still had broken links until touched).
4. **Deactivate the OLD revision watcher** — still Active alongside the fixed one; fired Muller false-positives at 10:30/10:33/11:32. (Anthony, n8n.)
5. **Standardize Drive `APPROVED/` subfolders** per client/month (TTFS July had none).
6. **Listener failure logging** — capture stdout + Slack-alert on run failure (to diagnose the fast-fail loop) + n8n marks task "In production" on fire so a dead run doesn't re-fire hourly.

**Meta-insight:** once a post is *approved*, Apollo can't safely edit it via API (republish risk) → every late fix becomes a manual UI task. The whole value of the pre-submit QC check is getting it right BEFORE approval.

---

## 🚨🚨 2026-07-08 — SYSTEMIC: carousels collapse to 1 slide when bulk-approved in GHL
**Discovered:** LPBD + LP University July carousels were created correctly (verified full slide counts + sweep at creation on 2026-07-01). By 2026-07-08, EVERY not-yet-published carousel across BOTH accounts had collapsed to `media.length = 1`. Carousels that had already PUBLISHED kept all slides; only the not-yet-published ones broke.
**Root cause — CONFIRMED (corrects an earlier wrong guess):** It is **NOT n8n.** All 6 of our n8n workflows were checked — none edit or reschedule posts (they only create drafts + watch Notion). The GHL account has **0 posting categories/queues**, so it's not a GHL auto-schedule setting either. Forensics: **11 posts were all re-saved in one shot on 2026-07-06** (`updatedAt` = 2026-07-06), and all are now 1 slide. That signature = a **bulk approve / bulk reschedule done in the GHL Social Planner UI.** GHL collapses a carousel to a single slide on ANY re-save — API edit OR UI bulk action. So a human bulk-approving a batch that contained carousels silently broke all of them.
**Impact:** carousels scheduled to publish as single images. A major driver of Cynthia's 2026-07-08 dissatisfaction.
**Fixes SHIPPED 2026-07-08:**
1. **`scripts/carousel-monitor.py`** — pure-API snapshot-diff, scheduled 3×/day via launchd `com.launchpad.carousel-monitor`. Detects any post that lost slides since last run and Slack-alerts `#ai-team-updates` (LLM only fires on an actual collapse = cheap). Catches this within hours instead of a week. Watches all 16 SMM sub-accounts (`scripts/carousel-monitor-accounts.json`).
2. **Rules baked into the agent + [[cynthia_review_rules]]:** carousels are approved/rescheduled ONE AT A TIME (never bulk); Apollo never edits a carousel (delete+recreate only); posting times set at creation so no post-approval reschedule is needed.
**Still needs (behavioral, not code):** Cynthia/approvers must stop bulk-approving batches that contain carousels. Confirm with Cynthia she bulk-approved ~Jul 6. Collapsed carousels get rebuilt (delete+recreate from Drive) only once we know they won't be bulk-approved again — HOLD until Cynthia says go.

## 2026-07-08 — Process decision: n8n pipeline is the standard, Slack is for issues/revisions (Anthony)
The canonical SMM posting path is the **n8n "Apollo Content Pipeline"** (Notion task → assigned to Apollo → client Drive `APPROVED/` → drafts → Cynthia reviews → approves). **Slack is for flagging breakage + revisions only — NOT the work queue.** The 2026-07-01 drift (rapid ad-hoc posting off Slack) is what we're correcting. Ad-hoc Slack requests get routed back through the Notion task flow. Captured in the agent spec (Critical Rule 25) + [[cynthia_review_rules]] §11.

## 2026-07-08 — Process drift (Anthony feedback)
Apollo spent 2026-07-01 taking rapid ad-hoc SMM tasks off Slack (LPBD, LP Uni, MNL/MNV/TBC video work) instead of running the **structured Notion process** (task filled in → assigned to Apollo → post → review → approve). Combined with the carousel breakage + earlier live-post incidents (MNV, Wylees), Cynthia flagged we're "not working right." Lesson: **stay on the established process; don't freelance from Slack.** When Cynthia sends ad-hoc requests, still route them through the Notion task flow and QC gates rather than improvising. Slow down, tighten up, one task at a time. Related: [[project_smm_apollo_rampup]], [[feedback_smm_posting_times_and_days]].

---

## 🚨 2026-06-30 (eve) — INCIDENT: MNV videos published LIVE during a "delete" step
- **What happened:** the MNV video-mixup fix needed to REMOVE 5 MNL-leak reels (future-dated Jul 3/14/17/21/24). The run tried `PUT status=deleted` first → GHL flipped them to `in_progress` (publish-now) → all 5 published LIVE to MNV's real FB + IG (10 posts, `publishedAt` = today). Cynthia removed the IG ones by hand; FB copies stayed live. The run's own comment even noted the quirk *after* — i.e. it published, then "corrected" to HTTP DELETE.
- **Why it's bad:** wrong-client (MNL) videos went live on a client's real Instagram + Facebook. Pure client-facing damage + manual cleanup for Cynthia. Second near-miss the same day (Wylees in_review video flipped to in_progress on a date-edit; caught + halted).
- **Fixes applied (this session):**
  1. `ghl_api_quirks.md` — added a loud **REMOVAL PROTOCOL** at the very top: HTTP DELETE only (never PUT status=deleted), only date-EDIT future-dated single posts, MANDATORY GET-verify `publishedAt==null` + status not in_progress/published after EVERY op, STOP+alert if anything published, and "deleting a published GHL post does NOT remove it from FB/IG."
  2. `cynthia_review_rules.md` — corrected the calendar-link rule (the `filters=` blob is a REQUIRED date-range filter, not a stale-month trap; stripping it defaulted links to June). Canonical July blob saved.
- **Seamless move (OPEN, for Anthony):** the agent KNEW the quirk and still hit it → documentation alone isn't enough. Need a hard guardrail: (a) a removal helper script that ONLY does HTTP DELETE + post-verify, never PUT; (b) consider revoking the agent's ability to PUT `status` transitions entirely; (c) the Step 8.5 QC gate should run a final "nothing published" sweep over every touched post before the run reports success.

### 🔬 CONFIRMED ROOT CAUSE (forensic, 2026-07-01) — from sub-agent transcript `dfd6d0fa/.../agent-ac0c3c2c…jsonl` + GHL records
**Mechanism (exact):**
1. To delete the 5 MNL-leak videos, the sub-agent used **`PUT status:"deleted"`** (the edit-post MCP *offers* "deleted" as a status value — a trap). Its own reasoning: *"I'm setting status: deleted which is what I want."* GHL does not delete on that — it flips the post to **`in_progress` = publish-now**.
2. GHL's publisher then **spawned brand-new published post records** — createdAt `23:16:41`, one per platform (10 records = 5 posts × FB+IG) — and pushed them LIVE at `23:17–23:18`. The future July scheduleDates were ignored (in_progress = now).
3. The agent caught the flip mid-run and PUT the **originals** back to `in_review`, then HTTP-DELETEd the originals. But that's a **false rescue** — the publish had already fired and created SEPARATE live records with new IDs; recalling the original does nothing to them.
**Why Apollo reported "PASS" and only Cynthia caught it (the detection gap):**
- Apollo's safety check GET-verified the **specific post IDs it had edited** (the originals) → those correctly showed `deleted:true, publishedAt:null`. The check passed *truthfully but on the wrong records.*
- The 10 records that actually went live were **new IDs the agent never enumerated.** Apollo only ever queried GHL for IDs it already knew. Cynthia saw the real IG feed (ground truth). Nothing in the pipeline compared against the whole calendar or the live platform.
**Two stacked failures:** (1) trigger = `PUT status:deleted`; (2) blind spot = per-ID verification instead of a full-calendar "did anything publish?" sweep.
**Required process changes (proposed 2026-07-01):**
1. Deletes = **HTTP DELETE only**, enforced via a vetted `ghl-delete`/`ghl-safe-edit` helper the agent MUST call (so it physically cannot issue a status-PUT). Never transition a post through `in_progress`/`scheduled`/`deleted`-status.
2. **Full-calendar publish sweep** as the run's final gate: re-pull the ENTIRE client calendar, flag ANY post with `publishedAt` in the last ~30 min OR any future-dated post showing `published`/`in_progress`. If found → incident, do NOT report success, alert immediately.
3. **Independent watchdog** (cron/n8n every ~10–15 min across all client calendars): detect premature publishes (future-dated post now `published`, or anything stuck `in_progress`) → instant Slack alert to Anthony + Cynthia. Independent of the agent's own self-report — this is the layer that pages us in minutes instead of relying on Cynthia's eyes.
- **Calendar-link backfill — STILL OWED:** all active July client links currently point to June (I wrongly stripped the filter blob earlier today). Need to re-add the correct `filters={BLOB}&date=2026-07-01` to every client's "Content Calendar Link" property. Paused mid-incident.
