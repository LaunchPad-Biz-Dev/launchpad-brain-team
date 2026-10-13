# SMM Posting Calendar Patterns

**Purpose:** Fast lookup of each client's weekly posting cadence (which days of the week get a Graphic vs a Video). The Social Media Poster agent reads this FIRST in Step 4 before falling back to the Content Monthly Deliverables (CMD) page.

**Why this exists:** The CMD page in Notion is a generic WEEKLY DAY-OF-WEEK TEMPLATE, NOT a list of calendar dates. Its day numbers (1, 2, 3...) just identify cells in a 7-col × 4-row grid — they map to **day of week**, not to dates of the month.

## CMD-page translation rule

| CMD day number | Day of week |
|---|---|
| 1, 8, 15, 22, 29 | Sunday |
| 2, 9, 16, 23, 30 | Monday |
| 3, 10, 17, 24, 31 | Tuesday |
| 4, 11, 18, 25 | Wednesday |
| 5, 12, 19, 26 | Thursday |
| 6, 13, 20, 27 | Friday |
| 7, 14, 21, 28 | Saturday |

So "Day 9 = Graphic" on the CMD page means **Mondays = Graphic** — i.e. find every Monday in the target month and schedule a graphic there.

## How to use this doc

1. Look up the client below to get their graphic + video weekdays.
2. Find all those weekdays in the posting month (calendar lookup).
3. Apply the 7-day QC window: first post ≥ task-assignment date + 7 days.
4. Fill slots in order; if more approved content than slots, **fill extra weekdays in the SAME month first, THEN push to next month** per Critical Rule 16. Post ALL approved content — never leave a still or carousel unplaced.
5. Every `scheduleDate` must land in the **8 AM – 8 PM client-local window** per Critical Rule 18. Use GHL recommended times inside that window; vary across the batch.

If the client isn't in this table, derive their pattern from the CMD page (`263b01f77d6d802ca9c8fe76c5a98dd0`) using the translation table above, then add a row here so future runs are faster.

---

## Global SMM rules (apply to every client) — added 2026-05-28 after Cynthia QC

These three rules are non-negotiable across every client run. They're written here because the agent reads this doc on every run.

1. **Posting hours: 8 AM – 8 PM client local time. Always.** Banned: 3 AM, 5 AM, 7 AM, 10 PM, 11 PM, midnight. Use GHL recommended times where surfaced; default mix otherwise = 9/11/12/2/4/6 (vary across batch).
2. **Em-dashes (`—` U+2014) and en-dashes (`–` U+2013) are BANNED in every caption.** Programmatic scan before Brand Compliance. Cynthia flagged this on CCS, BWU, TTFS, Muller in May 2026. Rewrite with periods, commas, colons, parentheses — anything but a dash.
3. **Post ALL approved content.** If normal cadence weekdays are full in the posting month, add extra weekdays in the same month before pushing to next month. The "Your Summer Apparel Starts Here" BWU still (2026-05-27) is the cautionary example — never leave content stranded.

---

## Per-client patterns

| Client | Graphic weekdays | Video weekdays | Contracted (per CMD) |
|---|---|---|---|
| **AFT (Arby's Food Truck)** | Mon, **Fri** | spread across month (10/mo) | 8G + **10V** (videos upped from 4 → 10 on 2026-07-29, Anthony) |
| **Apex Tax & Advisory** | Mon, Fri | Wed | 8G + 4V |
| **Afshar Law** | Mon, Wed | Fri | 8G + 4V |
| **BWU (Brand With Us)** | Mon, Fri | Wed | 8G + 4V |
| **Dauntless Boxing** | Mon, Fri | Wed | 8G + 4V |
| **Carnival Home** | ads-only — Apollo does not post (CMD-of-record: Wed, Fri G / Mon V — 4G + 4V) | — | — |
| **CCS (Continental Currency Services)** | Sun, Mon, Tue, Wed, Thu, Fri, Sat | Mon, Tue, Thu, Fri | 24G + 16V |
| **Durango HVAC** | Mon, Wed | Fri | 8G + 4V |
| **Launchpad** | Mon, Wed, Fri (+ Sun 8, 22) | Tue, Thu, Sat (+ Sun 1, 15, 29) | **15G + 15V (Custom)** |
| **LP University** | **Tue, Thu** (see note) | Wed | 8G + 4V |
| **Matsuda Nadig Law (MNL)** | Mon, Tue, Wed, Thu | Tue, Fri | 16G + 8V |
| **Matsuda Nadig Van Law (MNV)** | Mon, Tue, Wed, Thu | Tue, Fri | 16G + 8V |
| **Muller Masks** | Mon, Fri | Wed | 8G + 4V |
| **Princess Luxury Bed** | ads-only — Apollo does not post (CMD-of-record: Wed, Fri G / Mon V — 4G + 4V) | — | — |
| **Shumi Nation** | Mon, Wed, Fri (+ some Sun) | Tue, Thu, Sat (+ some Sun) | 15G + 15V |
| **TBC (Taco Bell Cantina)** | Mon, Thu | spread across month (10/mo) | 8G + **10V** (videos upped from 4 → 10 on 2026-07-29, Anthony) |
| **Toro Taxes Franchise Sales (TTFS)** | Mon, Tue, Thu | Sat | 14G + 4V |
| **Travel & Leisure** | ads-only — Apollo does not post (CMD-of-record: Wed, Fri G / Mon V — 4G + 4V) | — | — |
| **Trusted Tax** | Mon, Fri | Wed | 8G + 4V |
| **Upbeat Health** | Sun–Sat (every day) | Sun–Sat (every day) | 24G + 30V |
| **Welding School of Nevada** | Mon, Fri | Wed | 8G + 4V |
| **Wylees School** | Mon, Wed | Fri | 8G + 4V |

**TTFS note:** task-level instructions override this — TTFS June 2026 posted Mon/Tue/Thu graphics on June 2/9/16/etc per explicit task notes (which match the pattern above).

---

## Maintenance

- This doc replaces ad-hoc agent guessing about dates.
- If a client's cadence changes on the CMD page, update the matching row here.
- If a client is added to the CMD page, derive their pattern + add a row here.
- Keep it brief — one row per client. Detail belongs on the CMD page itself.

*Updated 2026-07-22: AFT graphics corrected Mon/**Thu** → Mon/**Fri** — Cynthia corrected AFT to Friday (not Thursday) on 2026-06-30; this table was stale and had caused an Aug run to land on Thursdays (fixed same day). NEVER schedule AFT graphics on Thursday.*

*Created 2026-05-27 after Cynthia flagged TBC posts landing on wrong weekdays (agent had been reading CMD day numbers as literal dates of month).*

*Updated 2026-07-20: corrected the **Launchpad** row. It listed 8G+4V on Mon/Fri (Essential), but the live CMD page has Launchpad on the **Custom** package at 15G+15V with a near-daily cadence. Cynthia confirmed 30 posts/month on 2026-07-20. Stale rows like this are why the CMD page is the source of truth and the Brain table is only a fast lookup: when they disagree, CMD wins and the row gets fixed.*

*Updated 2026-05-28 to match the live CMD page exactly: added Shumi Nation, Trusted Tax, Welding School of Nevada, Wylees School; corrected CCS to include Sunday graphics; corrected Upbeat to Sun–Sat every day; preserved the ads-only override for Carnival Home, Princess Luxury Bed, and Travel & Leisure but recorded their CMD-of-record patterns in case they reactivate organic posting.*

### Client notes on this table (verified 2026-09-30 against the live CMD page)

- **Durango HVAC is the odd one out among the Essential clients** — graphics land **Mon + Wed** with video on **Friday**, whereas Apex, BWU, Dauntless and most other Essentials are **Mon + Fri** graphics with a **Wednesday** video. Easy to cross-wire; check before scheduling.
- **LP University graphics run Tue + Thu, NOT the Mon + Fri the CMD page shows.** LP Uni and LPBD share one GHL location and one content calendar, so Anthony split them by weekday (2026-08-21): **LPBD graphics Mon/Wed/Fri, LP Uni graphics Tue/Thu.** Following CMD literally would collide the two brands on the same days. LP Uni posts go to the `launchpad.university` IG ONLY.
- **CCS weekend graphics are not spread evenly** — the CMD grid puts Sun + Sat graphics in weeks 2 and 3 only. In practice: fill all weekday slots first, then use weekends for the remainder.
- **TBC alternates on Tuesday** — Tue is a video slot in weeks 1 and 3, a graphic slot in weeks 2 and 4. Mon + Thu are always graphics; Wed + Fri always video.

### Overflow rule (Anthony, 2026-09-29)
If a month's approved folder holds **more content than the cadence has slots for**, put the extras on a **Saturday or Sunday in the same month** and **tell Anthony which ones went to a weekend**. Never scatter overflow onto random weekdays, and never roll it into the next month while same-month days remain.
