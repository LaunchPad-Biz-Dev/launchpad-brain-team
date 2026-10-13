# Shumi Anime Scanner — Weekly Content Slate
**Week of 2026-08-31** · Prepared for [[Kyle Fuller]] · Client: [[Shumi Store]]

---

## Scan Summary

**Sources scanned:**
- Anime News Network, MyAnimeList News — via WebFetch (Crunchyroll News returned page-shell only, no article content — third week in a row, likely JS-rendered and unreachable via WebFetch; flagging for Anthony to confirm if a dedicated fetch path is worth building)
- WebSearch: "anime news this week," "manga chapter news," "JUJUFEST 2026," "One Piece Remake Netflix," "Burger King Dragon Ball Super," "One Piece episode schedule September 2026" (Aug 2026)
- X / Twitter via Grok — **not captured, Grok integration still not wired in this session.** Logged per standing rule (`reference_x_via_grok.md`). Continued with remaining sources.
- TikTok via Apify (`clockworks/tiktok-hashtag-scraper`) — hashtags: #anitok, #anime, #onepiece, #jujutsukaisen — 60 videos pulled
- Instagram via Apify (`apify/instagram-hashtag-scraper`) — hashtags: #animefigures, #funkopop, #animememes — 60 posts pulled (recency-sorted, not engagement-ranked — see data quality note below)
- WebSearch: release calendar for One Piece episode/manga schedule, JJK Season 4 status, Pokémon/Burger King crossover timing

**Raw signals evaluated:** ~31
**Above threshold (14+):** 17
**Slated:** 11 (7 video + 4 graphic)

**IG data quality note (third consecutive week):** The Instagram hashtag scraper again returned latest posts, not top posts by engagement (platform API limitation for hashtag feeds). Most results were low-engagement reseller/individual-collector posts and unrelated fandoms (Genshin, Vocaloid, Hazbin Hotel), not the tracked competitor list (Crunchyroll Store, Hot Topic, POP MART, Entertainment Earth, BoxLunch). One useful hit: a Sabo P.O.P. CB EX figure post referencing One Piece chapters 1191-1193 spoiler content, confirming manga-side One Piece momentum is bleeding into figure-collector IG. TikTok remained the reliable engagement-ranked source this week — leaned on it for scoring.

---

## This Week's Headline Story

Two five-year-anniversary-scale franchise moments landed back-to-back this week, both squarely in Shumi's stocked-franchise wheelhouse. **JUJUFEST 2026** (Aug 29, marking JJK's 5th anime anniversary) dropped the **first-ever teaser trailer and key visual for Jujutsu Kaisen Season 4: The Culling Game Part 2** — Sukuna submerged in dark water, reaching toward camera, with the line "Do you remember? I told you that you'd get to see something interesting." The official TikTok drop hit **3.4M plays / 989.5K likes / 158.6K shares in under 48 hours**, the single biggest velocity signal of the week bar none. No air date yet, but the fandom doesn't need one — this is pure hype-cycle content.

Running in parallel: **One Piece's Netflix "remake" (WIT Studio, dir. Masashi Koizuka)** got new first-look poster art and confirmed its **February 2027** release window — 7 episodes covering the manga's first 50 chapters. Reaction is genuinely split ("we're still mid-Elbaf and they're remaking the START already?") which makes this a built-in debate format, not just a news read. Layer in that **One Piece Episode 1176 ("Gunko vs. the Straw Hats")** aired this past Sunday to strong edit volume ("HOLY SMOKES TOEI COOKED" — 272K plays), and One Piece is once again carrying two distinct storylines in one week: the remake debate and the ongoing Elbaf arc high.

Third story, and genuinely novel for a merch-store client: **Burger King and Toei Animation are relaunching Dragon Ball Super toys nationwide starting Tuesday, September 1** — the first BK/Dragon Ball toy tie-in in over 25 years. Six figures (Goku, SSB Goku, Vegeta, SSB Vegeta, Beerus, Piccolo), a redesigned crown, and a "Super Saiyan Sauce." This is a rare crossover moment that's both anime news AND inherently visual/shootable — Kyle grabbing the toys in person on launch day is a stronger hook than anything scraped off social.

---

## Signals Scored (14+ threshold)

| # | Signal | FR | V | VA | CR | Total | Bonus | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | JJK Season 4 "Culling Game Part 2" Sukuna super-teaser reveal | 5 | 5 | 5 | 5 | 20/20 | +2 (JJK in-stock) | TikTok @jujutsukaisen_en, 3.4M plays/989.5K likes/48hr |
| 2 | One Piece Netflix Remake (WIT Studio) new poster + Feb 2027 confirm | 5 | 4 | 5 | 4 | 18/20 | +2 | WhatsOnNetflix, CBR, community debate |
| 3 | Burger King x Dragon Ball Super toy collab (launches Tue 9/1, US) | 5 | 4 | 5 | 4 | 18/20 | +2 | ANN, Dexerto, CBR — first BK/DB collab in 25+ yrs |
| 4 | One Piece Ep. 1176 "Gunko vs. Straw Hats" edit surge (aired Sun 8/30) | 5 | 4 | 4 | 4 | 17/20 | +2 | TikTok #onepiece, multiple edits 70K-350K plays |
| 5 | JJK Gojo/Sukuna/Yuta edit trend (evergreen, S4 hype halo) | 5 | 4 | 4 | 4 | 17/20 | +2 | TikTok #jujutsukaisen, @spiderlilyedit_s 1.5M plays |
| 6 | #anitok revival community movement (ongoing, sustained volume) | 4 | 3 | 3 | 4 | 14/20 | — | TikTok #anitok, multiple Aug 20-31 posts |
| 7 | One Piece God Valley movie momentum (carrying from last week, Roger/Gaban lore) | 5 | 2 | 4 | 3 | 14/20 | +2 | TikTok @roscoefiasco, @blindredsamurai |
| 8 | Sabo P.O.P. CB EX figure post referencing ch. 1191-1193 spoilers | 5 | 2 | 3 | 2 | 12/20 | +2 | IG @banbro.oficial — below threshold, noted below |
| 9 | Pokémon: Wild Card film announced (CloverWorks, 2027) | 3 | 4 | 3 | 3 | 13/20 | — | ANN, MAL — below threshold, secondary franchise for Shumi |

**Bonus rule applied:** +2 for any signal touching a franchise Shumi currently stocks (One Piece, JJK, Dragon Ball — all confirmed in `Shumi Store.md` catalog).

---

## What I Saw But Didn't Use (Below Threshold)

- **Sabo P.O.P. CB EX figure / ch. 1191-1193 spoilers** (12/20 — real signal but too niche/text-heavy for a standalone idea; folded into G4 as a supporting figure pull instead)
- **Pokémon: Wild Card movie announcement** (13/20 — Pokémon is in Shumi's broader catalog but not a shonen-core franchise; borderline, cut for space this week since three bigger stories already filled the slate)
- **Naruto/Minato nostalgia edits** (evergreen, no fresh velocity this week — same signal flagged last week, still true)
- **Attack on Titan mobile game shutdown (Sept 28)** (industry news, not a content hook — no product angle, low community resonance beyond "rip")
- **Peter Cullen (Optimus Prime VA) passing** (major industry news but not anime/Shumi-relevant — Transformers not in catalog)

## Trending Audio to Bookmark (Even If Unused Today)

- **JUJUTSU KAISEN Official teaser sound** — ID `7678661552580414221` — used in V1, but still climbing; safe to reuse across multiple JJK posts this week without feeling repetitive since it's the "official" sound
- **"MONTAGEM PEGADORA - Slowed"** by Rubikdice & Chilx & WAA — ID `7613503368071596033` — driving the Nami vs. Gunko One Piece edit (243K plays), good high-energy option for any Elbaf-arc cut
- **Toei Animation official OP God Valley sound** — ID `7677173394780982046` — past its initial 24hr peak from last week but still being used in fresh edits 8 days later; durable, not urgent
- **anitok legacy audio "sin"** — ID `7308179250174069536` — the recurring nostalgia-format sound anchoring the #anitok revival movement; grab if doing any 2021-throwback format video

---

## Video Ideas (7)

---

### 🎥 V1 — "They just showed us Sukuna's face and I need everyone to see this"
**Format:** TikTok / IG Reel — 20-25 sec · **Suggested day:** Monday (today) · **Urgency:** Post immediately, early-week — teaser dropped Aug 29, still inside peak discourse window
**Driving signal:** Signal #1 — Score 20/20 + bonus. JUJUFEST reveal, 3.4M plays/989.5K likes/48hr, biggest velocity signal of the week.
**Hook (0-3s):** Kyle, phone up, dead serious: "They just dropped the Culling Game Part 2 teaser and I am NOT okay—"
**Beats:**
1. (0-4s) Reaction hook, hold phone showing the Sukuna teaser visual
2. (4-10s) Quick explainer: what Culling Game Part 2 covers (Hakari vs. Kashimo, Tsukumo vs. Kenjaku), why Sukuna's silence breaking matters
3. (10-16s) Cut to counter — pick up a Shumi Sukuna/Gojo figure, "5 years of JJK and he's STILL the scariest thing in anime"
4. (16-22s) Text overlay: "No air date yet. We're not ready either." Pan across in-stock JJK shelf
5. (22-25s) End card: "JJK figures in stock now — link in bio"
**Trending audio:** **JUJUTSU KAISEN Official teaser sound** — ID `7678661552580414221` — use the actual official audio, it's the moment itself
**Visual direction:** Dark, moody lighting to match the teaser's underwater aesthetic — dim the shop lights if possible, or shoot on a dark backdrop. Feature Sukuna, Gojo, or Yuji figures currently in stock.
**Caption:** "They said 'you'd get to see something interesting' and then showed us THIS 😭 5 years of JJK and Sukuna still ends us. No air date yet but we're already not okay. JJK figures in stock — link in bio. #jjk #jujutsukaisen #sukuna #anime #cullingGame"
**Why it works / Product bridge:** Single biggest velocity signal scanned this week, directly in Shumi's stocked-franchise wheelhouse. Highest urgency item on the slate.

---

### 🎥 V2 — "Wait, they're remaking One Piece already?? Let's talk about it"
**Format:** TikTok / IG Reel — 30-35 sec (debate/hot-take format) · **Suggested day:** Thursday 9/3 · **Urgency:** Mid-week — story is still fresh (news broke 8/30-31) and the debate has legs through the week
**Driving signal:** Signal #2 — Score 18/20 + bonus. Netflix confirmed Feb 2027 release, WIT Studio, split fan reaction.
**Hook (0-3s):** "Okay so Netflix just confirmed the One Piece remake poster and I have THOUGHTS—"
**Beats:**
1. (0-5s) Hook, hold up phone with the new poster/first-look image
2. (5-14s) Lay out the facts: WIT Studio (AoT, Spy x Family), Feb 2027, 7 episodes covering the first 50 chapters, airing while the ORIGINAL anime is still mid-Elbaf
3. (14-24s) Present both sides fast: "New fans finally get an easy entry point" vs. "we're still watching Luffy fight Imu right now, this is WILD timing" — genuine debate energy, no forced conclusion
4. (24-30s) Cut to shelf — "Either way, the OG story needs the OG figures" — pan Straw Hat crew figures
5. (30-35s) End card: comment your take + "One Piece figures in stock — link in bio"
**Trending audio:** Needs sound match — this is a talking-head debate format, use a low-key trending "hot take" sound if one's live day-of, otherwise original audio works fine for this format
**Visual direction:** Straight-to-camera, Kyle talking, minimal cuts. Counter or shop background. End on Straw Hat figure lineup, warm tones.
**Caption:** "Netflix really said 'new One Piece anime, but make it 2027' while Luffy is still out here fighting Imu 💀 New fans win, longtime fans are torn. Where do you land? One Piece figures in stock now — link in bio. #onepiece #onepieceremake #anime #luffy #netflix"
**Why it works / Product bridge:** Community/Debate pillar — no right answer, comment section engine. Direct bridge to core OP inventory.

---

### 🎥 V3 — "One Piece just did it again (Gunko vs. Straw Hats recap)"
**Format:** TikTok / IG Reel — 20 sec · **Suggested day:** Saturday 9/5 · **Urgency:** Late-week — bridges last Sunday's episode into hype for the next one
**Driving signal:** Signal #4 — Score 17/20 + bonus. Episode 1176 edit surge, multiple posts 70K-350K plays in 48hrs.
**Hook (0-3s):** Text overlay over Elbaf-style figure shot: "Sunday's episode broke anitok again"
**Beats:**
1. (0-4s) Hook text + fast cuts of Elbaf-era figures in stock
2. (4-10s) Kyle recapping the Gunko vs. Straw Hats beats in hype-narrator voice — no spoiler-heavy detail, just "did you SEE that"
3. (10-16s) "If a REGULAR episode goes this hard, imagine God Valley" — tie back to last week's movie news, keep the thread alive
4. (16-20s) End card: "New episode drops again soon — figures in stock now"
**Trending audio:** **"MONTAGEM PEGADORA - Slowed"** by Rubikdice & Chilx & WAA — ID `7613503368071596033` — same audio driving the top-performing Nami/Gunko edit this week
**Visual direction:** High energy, quick cuts, Elbaf-arc figures front and center (Nami, Zoro, Gunko if stocked, or general Straw Hat lineup).
**Caption:** "If THIS is what a normal episode looks like, imagine God Valley in 2027 🔥 Elbaf has been non-stop since it started. One Piece figures in stock now — link in bio. #onepiece #elbaf #anime #luffy #onepieceanime"
**Why it works / Product bridge:** Evergreen-leaning but timely; keeps the God Valley/Elbaf narrative thread alive from last week without repeating it.

---

### 🎥 V4 — "We tried the Burger King Dragon Ball toys on launch day"
**Format:** TikTok / IG Reel — 25-30 sec · **Suggested day:** Tuesday 9/1 · **Urgency:** Post day-of — collab launches nationwide this exact day, first-mover window is short
**Driving signal:** Signal #3 — Score 18/20 + bonus. First BK x Dragon Ball toy collab in 25+ years, launches 9/1 US-wide.
**Hook (0-3s):** Kyle holding up a BK bag: "It's been 25 years since Burger King did Dragon Ball toys and today's the day—"
**Beats:**
1. (0-4s) Hook, holding the bag/box
2. (4-12s) Unbox on camera — reveal whichever figure(s) they got (Goku, SSB Goku, Vegeta, SSB Vegeta, Beerus, or Piccolo), genuine reaction
3. (12-20s) Quick size/quality comparison next to a Shumi DBZ figure on the shelf — "cute for $5... but if you want the REAL detail"
4. (20-26s) Text overlay: "6 figures total, one per meal, while supplies last"
5. (26-30s) End card: "Real Dragon Ball figures — always in stock, no combo required. Link in bio"
**Trending audio:** Needs sound match — check trending "unboxing reveal" sounds morning-of 9/1; this is fresh enough that the right sound may not exist yet
**Visual direction:** Half shot in/with BK packaging, half back at the shop counter next to premium DBZ figures for the comparison beat. Playful, not mean-spirited toward BK — this is a fun crossover moment, not a takedown.
**Caption:** "It's been 25 YEARS since Burger King did Dragon Ball toys and we had to try it 🍔🐉 Cute concept, but you know where to go for the real detail. In stock now, no combo required — link in bio. #dragonball #dragonballsuper #burgerking #anime #funko"
**Why it works / Product bridge:** Rare novel crossover with a hard launch date inside the slate week — first-mover content opportunity most competitors won't have queued up. Direct comparison bridge to Shumi's own DBZ stock.

---

### 🎥 V5 — "Anitok really is coming back and I'm here for it"
**Format:** TikTok / IG Reel — 15-20 sec · **Suggested day:** Sunday 9/6 · **Urgency:** Evergreen/ongoing — sustained volume all month, not a single-day spike
**Driving signal:** Signal #6 — Score 14/20. Sustained community movement, multiple Aug 20-31 posts in the 40K-190K play range.
**Hook (0-3s):** Text overlay: "anitok in 2021 vs anitok right now"
**Beats:**
1. (0-4s) Split-screen or quick-cut format: old-school anime edit style vs. current shop content
2. (4-10s) Kyle talking directly to camera: "the anitok revival is real and we're not mad about it — bring back the chaos"
3. (10-16s) Quick shelf pan set to nostalgic edit-style pacing
4. (16-20s) End card: "we've been here the whole time. Shop the community's favorites — link in bio"
**Trending audio:** **anitok legacy audio "sin"** — ID `7308179250174069536` — the anchor sound for the whole revival trend
**Visual direction:** Lean into a slightly lo-fi, 2021-nostalgic edit aesthetic on purpose — contrast with Shumi's usual clean shots for this one post.
**Caption:** "anitok said we're bringing it back and we are SO unwell about it 🙏 the community never left, it just went quiet for a minute. Shop community favorites — link in bio. #anitok #anime #anitokrevival #animecommunity #weeb"
**Why it works / Product bridge:** Community entry-point pillar — low commercial pressure, high brand-affinity payoff. Good closer for the week.

---

### 🎥 V6 — "Ranking every JJK sorcerer we'd actually want on our team"
**Format:** TikTok / IG Reel — 30 sec (tier-list/debate format) · **Suggested day:** Friday 9/4 · **Urgency:** Mid-to-late week, rides the Season 4 hype wave started by V1
**Driving signal:** Signal #5 — Score 17/20 + bonus. Sustained JJK edit volume, @spiderlilyedit_s "Early?" post alone hit 1.5M plays this week.
**Hook (0-3s):** "Season 4 has us thinking about this way too hard — tier list time"
**Beats:**
1. (0-5s) Hook + quick title card "JJK Sorcerer Tier List"
2. (5-22s) Fast tier reveal (S/A/B tiers) using figures as the visual — Gojo, Sukuna, Yuta, Nanami, Megumi, Hakari — genuine hot takes, invite disagreement
3. (22-27s) "Fight us in the comments" energy, direct camera address
4. (27-30s) End card: "Build your own roster — figures in stock, link in bio"
**Trending audio:** JJK official teaser sound (same as V1) works as a callback, or any current tier-list format trending sound — check morning-of
**Visual direction:** Clean, well-lit product-forward shots since figures ARE the visual content here. Line figures up in tier order on the counter.
**Caption:** "We know this is going to start a fight but here's our JJK sorcerer tier list 😤 Season 4 hype has us feral. Tell us we're wrong. Figures in stock — link in bio. #jjk #jujutsukaisen #gojo #anime #tierlist"
**Why it works / Product bridge:** Community/Debate pillar, product-forward by design since the figures ARE the ranking device — one of the strongest direct product bridges on the slate.

---

### 🎥 V7 — "Counting down to God Valley with the man who was there"
**Format:** TikTok / IG Reel — 20 sec · **Suggested day:** Saturday 9/5 · **Urgency:** Evergreen backup — carries last week's momentum, no expiration pressure
**Driving signal:** Signal #7 — Score 14/20 + bonus. Continued God Valley/Roger-era edit activity, @blindredsamurai Gaban lore post 293K plays.
**Hook (0-3s):** Pick up a Gol D. Roger or Rocks-era figure: "This man was AT God Valley..."
**Beats:**
1. (0-4s) Hook holding the figure
2. (4-12s) Quick lore hit: God Valley incident, Roger/Rocks/Garp connection, why the 2027 movie is such a big deal for long-time fans
3. (12-18s) Pan to other Roger-era/Marine-era figures in stock
4. (18-20s) End card: "Summer 2027 can't come fast enough — shop the era now, link in bio"
**Trending audio:** Toei official God Valley sound — ID `7677173394780982046` — still valid, callback to the original announcement
**Visual direction:** Warm, reverent tone — this is "collector lore" content, slower pacing than the news-reaction pieces.
**Caption:** "The man was literally AT God Valley 😭 Summer 2027 needs to hurry up. Shop the era while we wait — link in bio. #onepiece #godvalley #rogerpirates #anime #luffy"
**Why it works / Product bridge:** Evergreen/Collector Culture pillar — safe backup if a scheduling gap opens, still on-trend.

---

## Graphic Ideas (4)

---

### 🖼️ G1 — "Everything We Know: JJK Season 4 Culling Game Part 2"
**Format:** IG Carousel (6 slides) · **Suggested day:** Wednesday 9/2 · **Urgency:** Post mid-week, rides V1's momentum into a save-able reference post
**Driving signal:** Signal #1 — same driving story as V1, reformatted as an evergreen-leaning info carousel (high save rate per brand's Anime Education pillar).
**Slides:**
1. Title slide: "JJK Season 4: Culling Game Part 2 — Everything We Know" over the Sukuna teaser key art style (dark, moody)
2. "It's official" — JUJUFEST 2026 reveal, 5th anniversary of the anime
3. Who's fighting: Hakari vs. Kashimo, Tsukumo vs. Kenjaku teased in the trailer
4. Sukuna's line: "Do you remember? I told you that you'd get to see something interesting." — quote card
5. Behind the scenes: Takeru Sato directing, Studio MAPPA returning, no air date yet
6. CTA slide: JJK figures in-stock shelf shot, "Get ready. Shop JJK now — link in bio"
**Visual direction:** Dark navy/black palette to match the teaser's underwater aesthetic, bold white/red type for the Sukuna quote slide.
**Caption:** "Saving you the doom-scroll — here's everything confirmed about JJK Season 4 so far 🖤 Swipe through, then go get ready. JJK figures in stock now — link in bio. #jjk #jujutsukaisen #sukuna #anime #cullinggame"
**Product bridge:** CTA slide is a direct shelf shot of in-stock JJK inventory.

---

### 🖼️ G2 — "The One Piece Takeover of 2027" (timeline carousel)
**Format:** IG Carousel (5 slides) · **Suggested day:** Thursday 9/3 · **Urgency:** Pairs with V2's debate video, same-story reinforcement
**Driving signal:** Signal #2 — reframes the remake news as part of a bigger "One Piece is everywhere in 2027" story, using existing Brain knowledge of the Live Action Season 3 (Alabasta) and Movie 16 in development.
**Slides:**
1. Title: "2027 is going to be a LOT of One Piece"
2. "The Remake" — Netflix, WIT Studio, Feb 2027, first 50 chapters
3. "The Movie" — ONE PIECE FILM GOD VALLEY, Summer 2027
4. "The Live Action" — Season 3 "Alabasta" also confirmed for 2027
5. CTA slide: "One era. Every format. Shop the OG story now — link in bio" over Straw Hat shelf shot
**Visual direction:** Clean grid/timeline layout, One Piece red/gold color cues, use official poster art where available (screenshot-and-credit or recreate as text-forward graphic if licensing art isn't cleared for direct use).
**Caption:** "2027 is shaping up to be the biggest year in One Piece history and we are NOT ready 🏴‍☠️ New remake, new movie, new live action season. Shop the story now — link in bio. #onepiece #onepieceremake #godvalley #anime #luffy"
**Product bridge:** CTA slide direct shelf shot.

---

### 🖼️ G3 — "BK Got the Toy. We've Got the Detail." (comparison static/carousel)
**Format:** IG static or 2-slide carousel · **Suggested day:** Tuesday 9/1 · **Urgency:** Post day-of alongside V4 — same launch-day window
**Driving signal:** Signal #3 — same story as V4, formatted as a punchy comparison graphic for the feed.
**Slides (if carousel):**
1. Split-image: BK Dragon Ball toy vs. a premium Shumi DBZ figure, playful "which one though" framing
2. "Both are fun. Only one's staying on the shelf." — CTA with in-stock DBZ figures + shumistore.com
**Visual direction:** Bright, fun, not shading Burger King — this is a "we see you and we love it too" post, playful comparison not a takedown. High-contrast product photography for the Shumi figure side.
**Caption:** "BK really brought Dragon Ball toys back after 25 years and honestly? Respect 🐉🍔 But if you want the one that's staying on the shelf forever, we got you. In stock now — link in bio. #dragonball #dragonballsuper #burgerking #anime #funko"
**Product bridge:** Direct, playful comparison — highest commercial-intent graphic on the slate.

---

### 🖼️ G4 — "This Week's Elbaf Drop" (weekly new arrivals, evergreen format)
**Format:** IG static or carousel (product-count dependent) · **Suggested day:** Friday 9/4 · **Urgency:** Evergreen — recurring weekly format per brand strategy
**Driving signal:** Signal #7 + Signal #8 (Sabo P.O.P. spoiler chatter, below-threshold but folded in here) — general Elbaf/Roger-era collector momentum rather than one single news item.
**Slides:**
1. "This Week's Drop" title card over new-arrivals product shot
2. Feature 2-4 recent Elbaf-arc or Roger-era figures currently in stock (pull live list from shumistore.com/collections/one-piece)
3. CTA: "New week, new shelf. Shop it all — link in bio"
**Visual direction:** Clean product photography, dark background per the brand's established high-contrast style, consistent with the "Drop of the week" recurring format noted in Shumi Store.md.
**Caption:** "This week's shelf update is heavy on Elbaf energy 🔥 New arrivals up now, first come first served. Shop the drop — link in bio. #onepiece #elbaf #anime #funkopop #newarrivals"
**Product bridge:** This IS the product post — habitual-following format per brand strategy, builds the "check Shumi every week" behavior.

---
## Convention Note

**San Japan (San Antonio, Henry B. González Convention Center) runs Sep 4-6 — inside this slate week.** Per `Shumi Store.md`, live event coverage is client-side (Nghia's team) with shot lists from Launchpad — this scanner doesn't produce event content, but flagging the overlap so Kyle/Abril can confirm a shot-list brief is already in motion for San Japan if it isn't yet.

---

## Strategic Notes

**1. Two five-year-anniversary-scale reveals landed in the same 48-hour window.** JJK's Culling Game Part 2 teaser and One Piece's Netflix remake news both broke Aug 29-31. This is an unusually dense news week — the slate leans harder on "news lead" content than a typical week and lighter on pure evergreen filler as a result. Expect next week to cool off; don't be surprised if the Sept 7 slate skews back toward evergreen/collector content.

**2. The Burger King collab is a rare first-mover opportunity — move fast.** Most competitor merch accounts won't have this queued for launch day (9/1). If Kyle can get to a BK location that morning, V4/G3 posted same-day beats anything reactive posted 3-4 days later.

**3. Crunchyroll News remains unreadable via WebFetch for the third straight week.** The page returns only a title shell with no article content — likely JS-rendered and not crawlable by the current fetch method. Recommend either dropping it from the source rotation or finding an RSS/API alternative; right now it's a wasted call every Monday.

**4. IG hashtag scraper data quality issue persists.** Third consecutive week of recency-sorted (not engagement-sorted) results dominated by resellers and off-brand fandoms. TikTok is carrying the scoring load. Worth flagging to Anthony whether a different Apify actor or a curated competitor-account-specific scrape would perform better than broad hashtag scraping for IG specifically.

**5. Grok/X integration is still not wired after 14+ weeks of this skill running.** Every week's log carries the same "not captured" note. If this isn't a near-term priority, worth formally deprioritizing the line item in the skill spec rather than repeating the same flag weekly — Anthony's call.

---

*Sources scanned: ANN, MAL (Crunchyroll News unreadable), WebSearch news/schedule queries, X via Grok (not wired), TikTok via Apify, IG via Apify | Raw signals: 31 | Above threshold (14+): 17 | Slated: 11*
