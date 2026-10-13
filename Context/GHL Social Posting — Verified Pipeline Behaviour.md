---
title: "GHL Social Posting — Verified Pipeline Behaviour"
type: context
status: active
tier: primary
tags: [social-media, apollo, ghl, automation, process]
last_updated: 2026-10-07
related: ["[[Context/SMM Posting Calendar Patterns]]", "[[Context/Social Media Workflow — Agency Current Process]]", "[[Context/Contracted Monthly Deliverables]]", "[[Context/00-INDEX]]"]
source: live-runs 2026-09-22 → 2026-09-30, Apollo + Anthony
---

# GHL Social Posting — Verified Pipeline Behaviour

Everything here was **confirmed on live runs or by controlled test**, not inferred. It exists because several of these were learned the expensive way. The operational detail for agents lives in `.claude/agent-memory/social-media-poster/ghl_api_quirks.md`; this note is the human-readable record of how the pipeline actually behaves.

---

## 1. Carousels — settled 2026-09-30

**Carousels post correctly. There is no content bug.** Slides upload, attach, and render with every slide in the planner. Verified by a controlled test on a live 4-slide LPBD carousel, with Anthony confirming the planner view.

**What is genuinely broken is our ability to VERIFY them after scheduling.** Once a post is `scheduled` or `published`, the GHL API exposes only **per-platform child records**. Each child holds exactly one media item, and the real parent post is not fetchable (`GET /posts/{parentPostId}` → HTTP 400).

| Post status | Does the API media count mean anything? |
|---|---|
| `in_review` | **Yes** — real and trustworthy |
| `scheduled` / `published` | **No** — always reads as 1, regardless of actual slides |

**Working rules:**
- Verify slide counts **before** scheduling, while the post is `in_review`.
- After scheduling, the **planner UI is the only source of truth**.
- **Never report a carousel collapse from an API media count.** This false alarm has been raised twice (2026-09-10, 2026-09-30). The second time it caused six carousels to be needlessly rebuilt and sent Anthony to hand-schedule two posts for nothing.
- A **PUT/edit** to an existing carousel *does* genuinely collapse it. That is why carousel changes are always **delete + recreate with the full media array**, never a PUT.
- **Always snapshot every slide's CDN URL before touching a carousel.** Cheap, and it has made every recovery possible.


### 1a. A different carousel failure — truncation at upload (2026-10-07)

Section 1 covers the *false alarm*: a healthy carousel that merely reads as `media: 1` after scheduling. There is a second, **real** failure that looks identical in the API and must not be dismissed as the same thing.

On Apex's October calendar, the Oct 26 post was genuinely a single image: only slide 1 of Carousel 3 had ever been uploaded, while slides 2 and 3 never were. It had sat that way since creation on 2026-09-25 and was invisible on the calendar, which showed a normal-looking post.

**How to tell the two apart:** the false alarm only ever appears on `scheduled`/`published` posts. A post still `in_review` reporting fewer slides than its Drive folder holds is a **real** truncation.

**The audit that caught it:** hash every posted image (16x16 grayscale perceptual hash) against every file in the Approved folder. Each single-image post should match a still at ~1.00. One that matches nothing is an orphan carousel slide. Cheaper and more reliable: reconcile the folder's still/carousel counts against the calendar before scheduling.

**Fix:** delete + recreate with the full media array — never a PUT. Note that `approver` is not a valid top-level key on create (422); it goes in `postApprovalDetails`, which is required for `status: in_review`.

**Standing instruction (Cynthia, 2026-10-07):** when a carousel cannot be uploaded in full, report it. Posting slide 1 alone and moving on "creates issues when things are posted."

---

## 2. Deletions are SOFT

A deleted post still returns a full, normal-looking body from `GET /posts/{id}`. The only tell is `deleted: true` plus a `deletedAt` timestamp; a live post has `deleted: false` and no `deletedAt`.

- Verify a deletion by reading the `deleted` flag, **not** by whether the GET succeeds.
- The list endpoint correctly excludes soft-deleted posts — so **a post vanishing from the list is real signal**, worth a direct GET to check.
- Useful side effect: a soft-deleted post still serves its `media`, `summary` and `accountIds`, which makes it a valid restore source.

---

## 3. Editing — delete + recreate, not PUT

A PUT can silently revert about a minute later, and it **wipes** `instagramPostDetails.collaborators`, `tiktokPostDetails` and `youtubePostDetails` unless every one is re-sent. Editing an already-approved post can also republish it early.

**Standard practice: delete + recreate**, re-sending `accountIds`, `media`, `type`, `userId` and all platform detail objects. Strip `null` values from those objects before POST, and never include a `caption` key inside `tiktokPostDetails` (422).

---

## 4. Approval timing — the failure that kills posts

**A post that is not approved before its scheduled date does not post late. It fails.** GHL records the reason as `"Post Approved after scheduled date"`, and the error sits on the per-platform child record, not the parent.

This is the single most common cause of dead content in our calendars. Consequences:
- Never leave `in_review` content sitting on a date that is about to pass.
- Past-dated `in_review` posts cannot be rescued in place — they must be recreated on a future date.
- When a client's approver is slow, either chase the approval or (with the client's agreement) schedule directly.
- Clients where Launchpad now schedules directly rather than routing for approval: **Durango** (Yessenia, 2026-09-30), **Dauntless videos** (Bryan, 2026-09-30), **Shumi** (no approval gate by client instruction).

---

## 5. API mechanics worth knowing

- `POST /posts/list` needs **`skip` and `limit` as STRINGS** (`"0"`, `"100"`) plus a `fromDate`/`toDate` range. Numeric values 422.
- Results live at **`results.posts`**, and a single GET at **`results.post`**.
- **Create requires a non-empty `userId`.** Where Apollo is not a user on the sub-account, using the approver's own ID works and does not auto-publish.
- Media upload cap is roughly **25MB for images** (larger ones 413; `sips -Z 2400` fixes them with no visible quality loss). Videos well over that have uploaded fine.
- **Tokens never touch disk or a shell argument.** Parse `.env` inside a single Python process. A run that wrote a token to `/tmp` could not then delete it and needed manual cleanup.

---

## 6. Sourcing content from Drive

- **Always reconcile the folder's file count against the contracted count** in Contracted Monthly Deliverables before posting. Drive's `search_files` has silently truncated a listing to five items with a hidden next-page token, which would have dropped a still and a carousel slide unnoticed.
- A gap in numbered files (1, 2, 4…) is a truncation signal, not a designer omission.
- **Only ever post from the exact posting-month Approved folder.** If it is empty or missing, stop and report — never fall back to the previous month. Two clients hit this on 2026-09-29 and both correctly stopped.
- Month folders are inconsistently named across clients (`October 26'`, `October 26`, `EDITED` vs `Edited`, `Approved 2`, `Approved 4 Oct`). Navigate from the client's Drive root; never rely on a global title search, which returns other clients' folders.
- **Revisions can arrive either way:** a new Drive file ID, or the same ID with different bytes. Check both — compare ID *and* size/checksum before assuming a fix did or didn't land.
- Files in `Edited/` but outside `Approved/`, and anything in a `Not posting/` folder, are out of scope.

---

## 7. Standing content rules confirmed or changed in Sept 2026

- **Hashtags go in the caption, never in a comment.** `followUpComment` stays empty. Max 5 per post. Global.
- **No em-dashes or en-dashes in captions** — but a dash baked into an approved graphic's artwork is fine and should not be flagged (Anthony, 2026-09-29). Judge client-authored caption text strictly; judge approved artwork leniently.
- **No brand-name hashtags** as a general rule.
- **BWU uses no location hashtags or Vegas references at all** — including venue and landmark names such as the Bellagio. BWU-specific; Dauntless and TBC deliberately do use Vegas tags.
- **MNL collabs with MNV only on general legal topics.** Anything Vegas or Nevada specific posts to MNL alone, since MNV is the Arizona-market presence.
- **Videos post as reels by default** for every client. If one cannot be a reel (horizontal, or over 90s), post it as a feed post and tell Anthony.
- **Captions react or add something the graphic does not already say** — they never restate it. Where a graphic lists a problem, the caption supplies the fix. Where a graphic lists signs or steps, a "save this" CTA earns its place; on a service or seasonal post it reads as filler.

---

## 8. QC standard

- Every image and every video frame is read word by word before posting, in both English and Spanish where relevant. **Spanish captions must carry correct accents** — English spellcheck passes `capacitacion` and `gustaria` happily.
- Any spelling error means the asset is **held, not fixed in the caption**, and reported with the exact misspelling.
- Before calling a burned-in title card a typo, **re-extract densely** — a mid-animation frame can look wrong when the finished text is correct (a "SAK A" frame that resolves to "SAKAMOTO" caused one false flag).
- Sourced third-party graphics (news stills, info cards) are judged leniently; a stale detail inside one is not a hold.
