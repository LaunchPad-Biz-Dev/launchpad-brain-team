# Shumi Weekly Content Slate — Week of 2026-10-12

Prepared for [[Kyle Fuller]] · Client: [[Shumi Store]] · Prepared by: Shumi Anime Scanner (Apollo)

---

## Scan Summary

| Source | Status | Notes |
|---|---|---|
| Anime News Network / WebFetch | ✅ Captured | Oct 5–12 headlines pulled |
| WebSearch (news/manga/calendar) | ✅ Captured | NYCC 2026 coverage, manga schedule, episode calendar |
| X via Grok | ❌ Not captured — Grok integration pending | No xAI/Grok tool wired into this session. Logged per standing rule ([[reference_x_via_grok]]) — do not substitute Apify X scrapers. Flag for Anthony to confirm integration before next run. |
| TikTok via Apify (clockworks/tiktok-hashtag-scraper) | ✅ Captured | 7 hashtags requested (#anitok #anime #otaku #naruto #onepiece #myheroacademia #jjk), 6/7 scraped successfully (1 hashtag returned partial), 84 videos, cost ≈ $0.25 |
| Instagram via Apify (scraping_solutions/instagram-hashtag-scraper-pro-no-cookies) | ✅ Captured | 6 hashtags (#anime #animememes #animefigures #funkopop #naruto #onepiece), 72 posts, cost ≈ $0.09 |
| Release calendar | ✅ Captured | Oct 13–19 window checked; no major Shumi-franchise episode drops this specific week, but heavy manga/announcement news compensates |

**Raw signals evaluated:** ~28 distinct story/trend clusters derived from 156 scraped items + news pulls
**Above threshold (14+):** 9
**Slated:** 11 (7 video + 4 graphic)

---

## Top Signals (Scored)

| # | Signal | FR | V | VA | CR | Total | Bonus | Used in |
|---|---|---|---|---|---|---|---|---|
| 1 | **Naruto: Shadow Rising** — new manga announced at NYCC, Kishimoto drawing again | 5 | 5 | 4 | 5 | 19/20 | +2 (Naruto stock) | V1, G1 |
| 2 | **JJK trio remix AMV** (shondoii) — 19M plays / 5.1M diggs, sound still climbing | 5 | 5 | 5 | 5 | 20/20 | +2 (JJK stock) | V2 |
| 3 | **One Piece Ch.1195** — Sanji awakens Conqueror's Haki (Oct 11 drop) | 5 | 5 | 4 | 5 | 19/20 | +2 (OP stock) | V3 |
| 4 | **One Piece Elbaph arc anime** — new OP/ED songs + Loki cast reveal (Oct 11) | 5 | 4 | 4 | 4 | 17/20 | +2 (OP stock) | G3 |
| 5 | **"Big 3 Are Back"** — One Piece + Naruto + Bleach all active simultaneously in 2026 | 5 | 4 | 3 | 5 | 17/20 | — | V4 |
| 6 | **Naruto × Ninku crossover** — 4-ep anime, 20th anniversary, dir. Noriyuki Abe | 5 | 4 | 4 | 4 | 17/20 | +2 (Naruto stock) | V5 |
| 7 | **Akatsuki hoodie "Comment Itachi" CTA** — 144K likes / 4,219 comments on a one-line caption | 5 | 3 | 3 | 5 | 16/20 | — | G2 |
| 8 | **Gojo/Sukuna JJK edits** — consistent 15K–100K+ digg range across multiple creators | 5 | 4 | 4 | 4 | 17/20 | +2 (JJK stock) | V6 |
| 9 | **MHA 10th anniversary revival** (Sept 24 confirm resurging ahead of Jump Festa) | 5 | 3 | 3 | 4 | 15/20 | +2 (MHA stock) | V7 |
| 10 | Naruto 26th anniversary (Oct 9) nostalgia wave | 5 | 3 | 3 | 4 | 15/20 | +2 | G4 |

---

## What I Saw But Didn't Use (Below Threshold)

- **Dr. Stone: Terraforming sequel greenlit** — FR:2 V:3 VA:2 CR:3 = 10/20. Not a Shumi-stocked franchise; cut.
- **One-Punch Man S3 Part 2 confirmed (Jan 2027)** — FR:2 V:3 VA:2 CR:3 = 10/20. Not core catalog; cut, bookmark for Jan.
- **DBZ Goku/Vegeta meme content** — FR:4 V:2 VA:3 CR:3 = 12/20. No fresh news hook this week, pure evergreen — held for a slower week.
- **Funko/blind box unboxing culture (general)** — FR:4 V:2 VA:4 CR:3 = 13/20. Strong visual but no specific trigger this week — bank for Figure Showcase pillar next cycle.
- **Marvel/Kadokawa manga partnership, Gundam Seed Freedom Zero, Apothecary Diaries film** — not Shumi franchise fits (no stock overlap).

## Competitor Scan Note

This week's hashtag pulls (#anime, #animefigures, #funkopop, #animememes) surfaced mostly fan-edit/meme accounts and small independent resellers (e.g. a Bahrain Funko reseller, an Argentina giveaway account) rather than the tracked competitor set (Crunchyroll Store, Hot Topic, POP MART, Entertainment Earth, Tokyo Otaku Mode). Hashtag-feed scraping doesn't reliably surface big retail accounts' owned posts — that requires direct account-level scraping. **Recommend:** next cycle, add a direct profile scrape of the 5 tracked competitor handles rather than relying on hashtag discovery alone. One format worth stealing regardless of source: the simple "Comment [character name]" CTA post (akatsukizipup, 144K likes/4.2K comments) — low production, high comment-bait, works for merch accounts specifically.

---

# Video Ideas (7)

## 🎥 V1 — "Kishimoto is drawing Naruto again — here's what we know about Shadow Rising"

**Format:** TikTok / IG Reel — 30–40 sec
**Suggested post day:** Monday (today — peak discourse window, story broke 24–48hrs ago and is still climbing)
**Urgency:** Post early-week
**Driving signal:** NARUTO: SHADOW RISING manga announced at NYCC (Oct 10–11), Masashi Kishimoto confirmed drawing again, more details at Jump Festa Dec 19–20. TikTok: "Naruto is officially getting a new manga we are so back" — 998.9K plays/204.5K diggs (@woven.void); "new naruto manga how we feeling" — 792K plays/211.9K diggs (@akxtskii). IG: multiple posts same week, one at 4,350 likes (@pixeltwelve), Indonesian-language post at 1,494 likes with heavy comment engagement asking fans to vote which storyline they want. Score 19/20 (FR:5 V:5 VA:4 CR:5) +2 bonus.
**Hook (0-3s):** Kyle holds up a Naruto Funko/figure, text overlay: "Kishimoto is drawing Naruto again. I need a minute."
**Beats:**
1. (0-4s) Hook line + figure in hand
2. (4-12s) Recap: NYCC announcement, "Naruto: Shadow Rising," Kishimoto himself on art, more info December at Jump Festa
3. (12-22s) Kyle reacts — genuine fan energy, not corporate: "we've been here since Gear 1... I mean since Chapter 1"
4. (22-30s) Ask the audience: "Team 7 reunion story or totally new arc? Comment your theory"
5. (30-38s) End card: Naruto figures/Funko in stock, "link in bio"
**Trending audio:** Needs sound match — no single breakout sound tied to this story yet (posts used personal "original sound" tracks). Use a moody/hype instrumental bed; revisit next week once a dedicated "Shadow Rising" sound emerges.
**Visual direction:** Shop counter or dark backdrop, Naruto Funko/Pop Up Parade figures from current in-stock SKUs front and center. Warm orange/black palette (classic Naruto branding).
**Caption:** "Kishimoto said 'I'm not done yet' and the whole fandom just sat up straight 😭 Naruto: Shadow Rising just got announced at NYCC — more details drop at Jump Festa in December. What story do you want it to tell? Naruto figures in stock now — link in bio. #naruto #narutoshadowrising #anime #narutomanga #shonenjump #animenews #shumi"
**Why it works / Product bridge:** Rides the single biggest anime story of the week; bridges directly into in-stock Naruto Funko/figures without opening on the SKU.

---

## 🎥 V2 — "POV: the JJK trio but it's the remix everyone's using"

**Format:** TikTok / IG Reel — 15–20 sec
**Suggested post day:** Monday (grab the sound now — it's climbing, not peaked)
**Urgency:** Post early-week
**Driving signal:** @shondoii's "Buggin x New Jeans" JJK trio remix AMV — 19M plays / 5.1M diggs / 285K shares, posted Sept 28, still actively spreading three weeks later. Score 20/20 (FR:5 V:5 VA:5 CR:5) +2 bonus.
**Hook (0-3s):** Quick cuts of Gojo, Geto, Shoko figures lined up on the shelf, timed to the drop in the remix.
**Beats:**
1. (0-3s) Beat-synced figure reveal — Gojo first
2. (3-8s) Geto, then Shoko — each cut lands on the beat
3. (8-14s) Full trio lineup shot, Kyle mouthing the hook lyric
4. (14-18s) Text overlay: "the trio we didn't deserve"
5. (18-20s) End card: JJK Pop Up Parade figures in stock, link in bio
**Trending audio:** **"original sound" by shondoii** — `musicId 7691115217656269586` — 19M plays and climbing, exactly the kind of sound Kyle should film over before it peaks.
**Visual direction:** Clean shelf lineup shot, dark/moody lighting (JJK's dark aesthetic per brand guidelines). Fast cuts, no dead air.
**Caption:** "the trio we didn't deserve 🖤 JJK Pop Up Parade figures in stock now — link in bio. #jjk #jujutsukaisen #gojo #geto #shoko #anime #animefigures #shumi"
**Why it works / Product bridge:** Borrows a proven, still-rising sound instead of waiting for a new trend; direct shelf-to-camera product tie-in.

---

## 🎥 V3 — "Sanji just awakened Conqueror's Haki and nobody's ready"

**Format:** TikTok / IG Reel — 25–35 sec
**Suggested post day:** Wednesday (chapter 1195 dropped Oct 11, discourse peaks days 2–4 before Ch.1196 preview takes over Oct 18)
**Urgency:** Mid-week
**Driving signal:** One Piece Chapter 1195 (Oct 11) — Sanji's Conqueror's Haki awakening. TikTok: "Sanji's Self-Deprecation" edit tagged #onepiece1195 — 392.4K plays/100.1K diggs (@maviiiofficial). IG: Whitebeard/Ace Marineford nostalgia edit tied to same wave — 1,063 likes (@zoanopx). Score 19/20 (FR:5 V:5 VA:4 CR:5) +2 bonus.
**Hook (0-3s):** Text overlay over a Sanji figure: "we waited HOW long for this"
**Beats:**
1. (0-4s) Hook + Sanji figure close-up
2. (4-14s) Recap chapter 1195 moment — Sanji's Conqueror's Haki awakening, no spoiler specifics beyond what's public
3. (14-24s) Kyle reaction — genuine hype, "the slander arc is OVER"
4. (24-30s) Text overlay: "no spoilers, just screaming"
5. (30-35s) End card: Sanji / Straw Hat figures in stock
**Trending audio:** **zsy's "original sound"** — `musicId 7695505795772975874` — used in his Oct 11 Shanks/Whitebeard clash edit, 325.3K plays, very fresh and actively used in the One Piece edit community right now.
**Visual direction:** Warm tones (per brand guidelines — warmer palette for One Piece/collector culture). Sanji figure front and center if in stock; otherwise Straw Hat crew lineup.
**Caption:** "Sanji's Conqueror's Haki just dropped in Chapter 1195 and the whole fandom is SCREAMING 😭🔥 No spoilers, just reactions. One Piece figures in stock now — link in bio. #onepiece #sanji #onepiece1195 #luffy #anime #animefigures #shumi"
**Why it works / Product bridge:** Highest-conversion content pattern per Brain notes — chapter drops → same-week reaction → in-stock figure CTA.

---

## 🎥 V4 — "The Big 3 are ALL back in 2026 — rank them"

**Format:** TikTok / IG Reel — 30–45 sec
**Suggested post day:** Thursday (mid-week community debate peak)
**Urgency:** Mid-week
**Driving signal:** "Big 3 Are Back" narrative — One Piece (Elbaph Arc airing), Naruto (Shadow Rising manga + Ninku crossover anime), Bleach (TYBW: The Calamity premiered July) all simultaneously active for the first time in years. IG: @xo.cuts "THE BIG 3 ARE BACK IN 2026" post — 966 likes/35 comments; companion "THE BIG 3 ERA IS NEVER DYING" post — 530 likes/17 comments. Score 17/20 (FR:5 V:4 VA:3 CR:5).
**Hook (0-3s):** Kyle holding three figures (one per franchise), text overlay: "name a better era. I'll wait."
**Beats:**
1. (0-5s) Hook — three figures lined up, Kyle smirking
2. (5-20s) Rapid-fire case for each: Luffy/One Piece (Elbaph arc live), Naruto (Shadow Rising just announced), Ichigo/Bleach (TYBW finale this year)
3. (20-35s) Direct-to-camera ask: "drop your Big 3 ranking in the comments — I already know it's gonna be chaos"
4. (35-42s) End card: all three franchises' figures in stock
**Trending audio:** Needs sound match — this is a voiceover/talking-head format, audio-independent. No music bed required beyond a light beat.
**Visual direction:** Clean three-figure lineup, even lighting so all three franchises read equally — no favoritism in framing.
**Caption:** "One Piece. Naruto. Bleach. ALL active in 2026. We are so back 🐐 Drop your Big 3 ranking below. In stock now — link in bio. #big3anime #onepiece #naruto #bleach #anime #animecommunity #shumi"
**Why it works / Product bridge:** Community/Debate pillar — no right answer, comment section ignites; triple product bridge in one post.

---

## 🎥 V5 — "Naruto × Ninku is happening and here's why it matters"

**Format:** TikTok / IG Reel — 25–30 sec
**Suggested post day:** Thursday
**Urgency:** Mid-week
**Driving signal:** Naruto × Ninku 4-episode crossover anime announced at NYCC (Oct 10), directed by Noriyuki Abe, celebrating how Ninku inspired Kishimoto to become a manga artist. TikTok: "New Naruto series announced at New York Comic Con!" — 797K plays/85.8K diggs (@theamazingcstew). Score 17/20 (FR:5 V:4 VA:4 CR:4) +2 bonus.
**Hook (0-3s):** Text overlay: "Naruto's creator just crossed over with the anime that MADE him a mangaka"
**Beats:**
1. (0-4s) Hook line
2. (4-14s) Explain: Ninku inspired Kishimoto to draw manga; 20th-anniversary 4-episode crossover now confirmed, directed by Noriyuki Abe (also directed Naruto Shippuden)
3. (14-22s) Kyle reaction: "this is the kind of crossover you don't see coming"
4. (22-28s) End card: Naruto figures in stock
**Trending audio:** Needs sound match — no specific sound surfaced for this story; use a nostalgic/reflective instrumental.
**Visual direction:** Naruto figures with a "legacy" framing — side-by-side with older-era packaging/art if available in-store.
**Caption:** "Naruto × Ninku. A 20th-anniversary crossover nobody called but everyone wants. Naruto figures in stock now — link in bio. #naruto #ninku #anime #animenews #shonen #shumi"
**Why it works / Product bridge:** News-first format, builds anticipation ahead of the actual episode drop; direct Naruto product bridge.

---

## 🎥 V6 — "Gojo vs Sukuna: who actually wins the figure shelf?"

**Format:** TikTok / IG Reel — 20–30 sec
**Suggested post day:** Friday
**Urgency:** Evergreen / backup
**Driving signal:** Consistent high-engagement Gojo and Sukuna edits across the week — Sukuna "omfg i cannot defend this man" (60.8K plays/15.4K diggs), Gojo "ON MY MIND" edit (131.6K plays/29.1K diggs). Score 17/20 (FR:5 V:4 VA:4 CR:4) +2 bonus.
**Hook (0-3s):** Split-screen: Gojo figure left, Sukuna figure right. Text: "pick a side."
**Beats:**
1. (0-4s) Split-screen hook
2. (4-16s) Rapid case for each — Kyle narrates power/visual appeal/fan-favorite status
3. (16-24s) Direct ask: "comment GOJO or SUKUNA — losers restock the shelf" (playful)
4. (24-28s) End card: both figures in stock
**Trending audio:** "just score it" by OsamaSon — used in the viral Sukuna post (60.8K plays), a known general-purpose hype sound already circulating in the JJK edit community.
**Visual direction:** Dark, moody lighting consistent with JJK's dark aesthetic; split-screen or side-by-side shelf shot.
**Caption:** "Gojo or Sukuna — no in-between. Both in stock now, link in bio. #jjk #gojo #sukuna #jujutsukaisen #anime #animefigures #shumi"
**Why it works / Product bridge:** Community/Debate pillar, zero news dependency so it's a safe mid/late-week slot; doubles down on JJK's strongest-performing character pairing this week.

---

## 🎥 V7 — "It's been 10 years of My Hero Academia — shelf check"

**Format:** TikTok / IG Reel — 20–25 sec
**Suggested post day:** Saturday
**Urgency:** Evergreen / anchor
**Driving signal:** MHA 10th anniversary revival confirmed (Sept 24) — global concert tour + Jump Festa 2027 Super Stage reveal expected, hype resurging ahead of December. Steady mid-tier engagement across the week's #myheroacademia scrape (consistent 20K–560K play range across a dozen+ posts). Score 15/20 (FR:5 V:3 VA:3 CR:4) +2 bonus.
**Hook (0-3s):** Kyle picks up a Deku figure: "10 years. TEN YEARS."
**Beats:**
1. (0-4s) Hook
2. (4-14s) Quick anniversary recap — global concert tour, Jump Festa reveal expected December
3. (14-20s) Shelf check — pan across MHA figures in stock
4. (20-25s) End card: "which era hit hardest for you?"
**Trending audio:** Needs sound match — no breakout MHA-specific sound surfaced this week; use a nostalgic/warm instrumental.
**Visual direction:** Warm-toned shelf shot per brand guidelines (MHA/collector culture gets warmer tones vs. JJK's dark palette).
**Caption:** "My Hero Academia just hit 10 years and the hype train for the anniversary reveal is already leaving the station 🚂 Which era hit hardest for you? MHA figures in stock — link in bio. #myheroacademia #mha #deku #anime #animefigures #shumi"
**Why it works / Product bridge:** Evergreen anchor per Brain notes (MHA spikes around drops/anniversaries); safe Saturday slot that doesn't depend on same-week news.

---

# Graphic Ideas (4)

## 🖼️ G1 — "Everything we know about Naruto: Shadow Rising" (IG Carousel, 6 slides)

**Suggested post day:** Tuesday
**Urgency:** Post early-week (second touch on this week's biggest story, different format from V1)
**Driving signal:** Same as V1 — NARUTO: SHADOW RISING announcement. Carousel format lets the save/share mechanic work for collectors who want the full recap (per Segment A behavior — researches before buying/engaging).
**Slides:**
1. Title card: "NARUTO: SHADOW RISING — everything we know"
2. "Announced at New York Comic Con, Oct 2026"
3. "Masashi Kishimoto is drawing again — his first new Naruto art in years"
4. "Full details drop at Jump Festa '27 — December 19–20"
5. "Naruto, Sasuke, Sakura, Kakashi all teased"
6. CTA slide: "Naruto figures in stock now at shumistore.com — which story do you want to see? Comment below."
**Visual direction:** Naruto orange/black palette, clean typography-forward slides (per current visual identity — modern sans-serif, no decorative type). Character silhouettes or confirmed art if licensing allows.
**Caption:** "Kishimoto said he wasn't done telling Naruto's story 😭 Swipe for everything confirmed so far about Shadow Rising. Naruto figures in stock now — link in bio. #naruto #narutoshadowrising #anime #narutomanga #shumi"
**Product bridge:** Direct — Naruto figures/Funko tied to the single hottest story of the week.

---

## 🖼️ G2 — "Comment your favorite Akatsuki member" (IG/TikTok static or carousel)

**Suggested post day:** Tuesday
**Urgency:** Evergreen, low-lift
**Driving signal:** Akatsuki hoodie merch post — "Comment 'Itachi' if you need one!" — 144,213 likes / 4,219 comments (@akatsukizipup). A proven low-production, high-comment-bait mechanic worth stealing for Shumi's own Akatsuki/Naruto merch. Score 16/20 (FR:5 V:3 VA:3 CR:5).
**Visual:** Clean flat-lay or product shot of Shumi's Akatsuki-adjacent Naruto merch (apparel, figures, pins — whatever's in stock), with large text overlay: "Comment your Akatsuki member. We'll tell you what to grab."
**Caption:** "Drop your favorite Akatsuki member below 👇 we'll match you with something from the shelf. #akatsuki #naruto #anime #animemerch #shumi"
**Product bridge:** Direct — this format IS the product bridge, engineered for comment volume that algorithmically boosts reach.
**Why it works:** Steals a proven external mechanic (144K likes on a one-line caption) rather than guessing at a new format.

---

## 🖼️ G3 — "One Piece Elbaph Arc just got its new OP & ED — plus a cast reveal" (IG static)

**Suggested post day:** Wednesday
**Urgency:** Mid-week (pairs with V3's One Piece day)
**Driving signal:** One Piece Elbaph Arc anime — new opening theme "Luminous" by Aina the End, new ending theme, and voice cast reveal for new character Loki (Oct 11 Japanese-language announcement, surfaced multiple times in IG scrape — @zeyra.play, @quranxj, @pauranik_bharat posts). Score 17/20 (FR:5 V:4 VA:4 CR:4) +2 bonus.
**Visual:** Clean announcement-style graphic — "ONE PIECE: ELBAPH ARC" headline, new theme song names, PV screenshot if licensing allows. Warm One Piece palette.
**Caption:** "One Piece's Elbaph Arc just dropped new theme songs AND a cast reveal for Loki 🏴‍☠️ The Straw Hats are not slowing down in 2026. One Piece figures in stock — link in bio. #onepiece #elbaph #luffy #anime #animenews #shumi"
**Product bridge:** Straw Hat crew figures/Funko, direct tie to the active anime arc.

---

## 🖼️ G4 — "Naruto turned 26 this week — which era are you?" (IG Carousel, nostalgia)

**Suggested post day:** Sunday
**Urgency:** Evergreen / low-urgency cap
**Driving signal:** Naruto's 26th anniversary (Oct 9) — nostalgia wave across the week's scrape ("Happy birthday to the GOAT," animation study posts referencing the anniversary). Score 15/20 (FR:5 V:3 VA:3 CR:4) +2 bonus.
**Slides:**
1. Title: "26 years of Naruto 🍥"
2. "Which era are you: Part 1 nostalgia or Shippuden power scaling?"
3. Character era comparison (young Naruto vs. adult Naruto)
4. CTA: "Tell us your era in the comments — Naruto figures in stock, link in bio"
**Visual direction:** Nostalgic framing, orange/black palette, "then vs now" comparison format.
**Caption:** "26 years since Naruto first aired and we're STILL not over it 🧡 Which era are you — Part 1 or Shippuden? Naruto figures in stock now — link in bio. #naruto #narutoanniversary #anime #narutoshippuden #shumi"
**Product bridge:** Naruto figures, low-urgency Sunday evergreen slot that closes the week.

---

## Trending Audio to Bookmark (Even If Unused Today)

- **shondoii's JJK trio remix** — `musicId 7691115217656269586` — used in V2, still climbing (19M plays as of this scan). Grab footage this week before it peaks.
- **zsy's One Piece edit sound** — `musicId 7695505795772975874` — used in V3, very fresh (posted Oct 11).
- **"just score it" by OsamaSon** — general JJK-edit-community hype sound, used in V6, worth keeping in the back pocket for any JJK content this month.

---

*Sources scanned: ANN, WebSearch (news/manga/calendar), TikTok via Apify (84 videos, 6/7 hashtags), Instagram via Apify (72 posts, 6/6 hashtags) | X via Grok: not captured — integration pending | Raw signal clusters: ~28 | Above threshold (14+): 9 | Slated: 11 (7 video + 4 graphic)*

*Prepared by Shumi Anime Scanner · 2026-10-12 · Next slate: 2026-10-19 · Questions → @anthony.launchpad*
