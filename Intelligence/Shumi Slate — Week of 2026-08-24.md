# Shumi Anime Scanner — Weekly Content Slate
**Week of 2026-08-24** · Prepared for [[Kyle Fuller]] · Client: [[Shumi Store]]

---

## Scan Summary

**Sources scanned:**
- Anime News Network, Crunchyroll News (page-shell only, no article content returned), MyAnimeList News — via WebFetch
- WebSearch: "anime news this week," "manga chapter news," "new anime announcement" (Aug 2026)
- X / Twitter via Grok — **not captured, Grok integration not wired in this session.** Logged per standing rule (`reference_x_via_grok.md`). Continued with remaining sources.
- TikTok via Apify (`clockworks/tiktok-hashtag-scraper`) — hashtags: #anitok, #anime, #onepiece, #jujutsukaisen — 60 videos pulled
- Instagram via Apify (`apify/instagram-hashtag-scraper`) — hashtags: #animefigures, #funkopop, #animememes — 30 posts pulled (recency-sorted, not engagement-ranked — see note below)
- WebSearch: release calendar for One Piece episode/manga schedule, JJK status, general Summer 2026 simulcast lineup

**Raw signals evaluated:** ~34
**Above threshold (14+):** 19
**Slated:** 11 (7 video + 4 graphic)

**IG data quality note:** The Instagram hashtag scraper returned latest posts, not top posts by engagement (platform API limitation for hashtag feeds). Most results were low-engagement reseller/individual-collector posts, not the tracked competitor list (Crunchyroll Store, Hot Topic, POP MART, Entertainment Earth, BoxLunch). This actually **reconfirms** the standing competitive insight in `Shumi Store.md`: dry product photography dominates the #animefigures tag at 0–5 likes. Treated as a competitive-landscape data point, not a top-posts ranking this week.

---

## This Week's Headline Story

Toei Animation dropped the biggest One Piece news of the year at **ONE PIECE DAY '26** (Aug 23): two new theatrical films confirmed — **ONE PIECE FILM GOD VALLEY** (Summer 2027) and **ONE PIECE FILM BAAD** (2029). The official announcement video hit 3.2M plays and 668.9K likes in under 24 hours with 7,174 comments. This is a top-tier, once-a-year-scale signal for a client whose product catalog skews heavily One Piece. Layer in: the manga just returned from a hiatus with a **back-to-back Chapter 1191 + 1192 release** (Aug 23), and **Episode 1176 "Gunko vs. the Straw Hats"** airs this Sunday (Aug 30) continuing the Elbaf arc. One Piece alone is carrying three distinct news cycles this week.

Second story: JJK content keeps moving big numbers on TikTok purely on edit/nostalgia format — the show itself is between seasons (S3 concluded March 2026, S4 in production, no new episodes this window), but Gojo/Sukuna/Megumi edits are still pulling 500K–2M+ plays on original-audio edits. This is a "the fandom doesn't need new canon to stay engaged" signal — good for evergreen/community content.

Third: **#anitok revival** is actively trending as its own micro-movement — creators explicitly reviving 2021-era anitok meme formats ("Make anitok great again," "we bringing anitok back," "anitok 2026 revival"). This is the community entry-point pillar the existing Brain notes flagged — worth riding this week while it's fresh.

---

## Signals Scored (14+ threshold)

| # | Signal | FR | V | VA | CR | Total | Bonus | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | One Piece Film God Valley + BAAD announcement | 5 | 5 | 5 | 5 | 20/20 | +2 (in-stock OP inventory) | TikTok @toeianimationofficial, 3.2M plays/668.9K likes/24hr |
| 2 | One Piece Ch. 1191/1192 double-chapter return | 5 | 4 | 3 | 4 | 16/20 | +2 | WebSearch/Gamerant, Shonen Jump #39 |
| 3 | One Piece Ep. 1176 "Gunko vs. Straw Hats" (airs Sun 8/30) | 5 | 4 | 4 | 4 | 17/20 | +2 | Crunchyroll schedule, Fandomwire |
| 4 | JJK edit trend (Sukuna/Gojo/Megumi, evergreen post-S3) | 5 | 3 | 4 | 4 | 16/20 | +2 | TikTok #jujutsukaisen, @mysticreign.ae 676.9K likes |
| 5 | #anitok revival community movement | 4 | 4 | 3 | 4 | 15/20 | — | TikTok #anitok, multiple Aug 20–23 posts |
| 6 | Gol D. Roger Funko grail post (ties to God Valley lore) | 5 | 3 | 4 | 3 | 15/20 | +2 | IG @funko_freak23 |
| 7 | MegaHouse Tobimas One Piece flying-pose figures (Dec '26) | 5 | 2 | 5 | 2 | 14/20 | +2 | IG @bandaicollectuk |
| 8 | Naruto/Minato bond edit (evergreen) | 5 | 3 | 3 | 3 | 14/20 | +2 | TikTok @.coldsar, 3.6M plays |
| 9 | JJK Gojo Hollow Purple LED 1/6 statue (visual reference only) | 5 | 2 | 5 | 2 | 14/20 | +2 | IG @nexocollectables |

**Bonus rule applied:** +2 for any signal touching a franchise Shumi currently stocks (One Piece, JJK, Naruto — all confirmed in `Shumi Store.md` catalog).

---

## What I Saw But Didn't Use (Below Threshold)

- **Attack on Titan edits** (14/20 borderline, cut for space — AOT is in the catalog but no fresh news this week, purely evergreen edit volume)
- **Dragon Ball evergreen memes** (12/20 — steady but no velocity this week)
- **Solo Leveling edit, 3.8M plays** (excluded — not a franchise Shumi stocks per catalog, no SKU bridge possible)
- **Persona 5 Royal Funko chase concepts** (excluded — not in Shumi's confirmed franchise list)
- **Rengoku vs. Akaza Flame Tiger 1/6 statue** (12/20 — premium competitor product, not tied to news, visual-only)
- **Bleach TYBW ongoing content** (not confirmed in Shumi's stocked franchise list — flagged for Kyle to verify with Nghia/Priscilla before building content around it; noted as open question)

---

## Video Ideas (7)

### 🎥 V1 — "They just announced the ONE PIECE GOD VALLEY movie"
**Format:** TikTok / IG Reel — 25–30 sec · **Suggested day:** Monday · **Urgency:** Post immediately, early-week — this news is <24hrs old at slate time and decays fast
**Driving signal:** Signal #1 — Score 20/20 + bonus. Toei's official reveal, 3.2M plays/24hr.
**Hook (0-3s):** Kyle, phone in hand, face genuinely shook: "Wait... they just confirmed the GOD VALLEY movie—"
**Beats:**
1. (0-4s) Reaction hook, hold phone up showing the announcement
2. (4-12s) Quick explainer: what God Valley is, why it's the biggest unanswered mystery in One Piece (Roger, Garp, Rocks D. Xebec, the Ancient Weapon)
3. (12-20s) Cut to counter — pick up Shumi's Gol D. Roger Funko, "this man is about to get his whole movie"
4. (20-26s) Text overlay: "Summer 2027. We have TIME to get ready." Pan across in-stock OP shelf
5. (26-30s) End card: "One Piece figures in stock now — link in bio"
**Trending audio:** Official Toei Animation announcement audio — sound ID `7677173394780982046` (duet/react format rides the original) OR flag as **needs sound match** if a reaction-specific trending sound emerges closer to shoot day — check TikTok trending page morning-of since this news is still fresh.
**Visual direction:** Shop counter, dark clean surface. Feature Gol D. Roger Funko + any Roger-era or Marine-era OP figures in stock. High energy, no overproduction — this is a "I need to tell you right now" video.
**Caption:** "They really said 'here's your God Valley movie' and just walked away 😭 Summer 2027 cannot come fast enough. Who else needs the full story NOW. One Piece figures in stock — link in bio. #onepiece #godvalley #anime #onepiecefunko #luffy"
**Why it works / Product bridge:** Biggest OP news of the year, direct line to Roger/God Valley-era figures already in stock. Highest urgency item on the slate.

---

### 🎥 V2 — "Predicting what Gunko does to the Straw Hats"
**Format:** TikTok / IG Reel — 20-25 sec · **Suggested day:** Saturday · **Urgency:** Post late-week — pre-hype ahead of Sunday's episode
**Driving signal:** Signal #3 — Score 17/20 + bonus. Episode 1176 airs Sunday 8/30, Elbaf arc.
**Hook (0-3s):** "Episode 1176 drops tomorrow and Gunko is about to do WHAT to the crew—"
**Beats:**
1. (0-4s) Hook + hold up a Straw Hat figure
2. (4-14s) Quick prediction rundown — what "Threat of the Arrow-Arrow Fruit" likely means for the fight, staying spoiler-safe (episode hasn't aired yet)
3. (14-20s) "Comment your prediction, I'll pin the best one after it airs"
4. (20-25s) End card: Elbaf-era figures in stock, "tune in with us tomorrow"
**Trending audio: needs sound match** — check trending countdown/hype sounds day-of, none identified in this scan cleanly tied to prediction-format content.
**Visual direction:** Straw Hat figures lined up, Elbaf-arc aesthetic (warmer, adventurous tones per brand visual notes).
**Caption:** "Episode 1176 drops tomorrow and I have THOUGHTS about what Gunko's about to do 👀 drop your prediction below, best one gets pinned after it airs. One Piece in stock now. #onepiece #elbaf #anime #luffy"
**Why it works / Product bridge:** Prediction format drives comments (engagement mechanic), sets up a natural Sunday/Monday follow-up next week. Straw Hat figures front and center.

---

### 🎥 V3 — "One Piece just dropped TWO chapters and nobody's okay"
**Format:** TikTok / IG Reel — 20 sec · **Suggested day:** Tuesday · **Urgency:** Post early-week — chapters dropped Sunday 8/23, this is peak discourse window
**Driving signal:** Signal #2 — Score 16/20 + bonus. Chapters 1191 + 1192 back-to-back after hiatus, Shonen Jump #39.
**Hook (0-3s):** Text overlay: "one piece skipped 2 weeks then dropped this—"
**Beats:**
1. (0-4s) Hook, Kyle mid-reaction face
2. (4-12s) Rapid recap of what happened in 1191 and 1192 (spoiler-light, hype-forward, not full breakdown)
3. (12-18s) "This is why we don't take breaks from One Piece"
4. (18-20s) End card: link in bio for OP figures
**Trending audio: needs sound match** — manga-recap format typically uses low original sound / no music, flag for Kyle's judgment on shoot day.
**Visual direction:** Simple talking-head over manga panel screenshots (if licensable) or just Kyle reacting, no panel reproduction risk — keep it commentary-only to avoid copyright issues on manga art reposts.
**Caption:** "One Piece skipped weeks then came back swinging with TWO chapters 😭 if you know you know. One Piece figures in stock now — link in bio. #onepiece #manga #anime #luffy"
**Why it works / Product bridge:** Manga audience is the most engaged, highest-intent segment. Early-week posting catches peak discourse.

---

### 🎥 V4 — "Sukuna vs. Gojo — who actually wins" (edit-format tier debate)
**Format:** TikTok / IG Reel — 20-25 sec · **Suggested day:** Wednesday · **Urgency:** Mid-week, evergreen debate slot
**Driving signal:** Signal #4 — Score 16/20 + bonus. JJK edit content still pulling 500K-2M+ plays despite no new episodes.
**Hook (0-3s):** "The JJK fandom will NEVER stop arguing about this—"
**Beats:**
1. (0-4s) Hook, quick cuts of Gojo and Sukuna figures set up face-to-face on the counter
2. (4-16s) Rapid-fire case for each side (Hollow Purple vs. Malevolent Shrine, no new commentary needed, community already knows the arguments — this is a "pick a side" format not an explainer)
3. (16-22s) "Comment your pick, we'll do a follow-up with the results"
4. (22-25s) End card: JJK figures in stock
**Trending audio:** **"original sound" by mysticreign** — sound ID `7675470995989252894` — currently powering Sukuna edit content (676.9K likes, posted Aug 18, still climbing this week)
**Visual direction:** Dark, high-contrast background per JJK aesthetic notes in brand guide. Side-by-side figure staging, dramatic lighting if possible.
**Caption:** "Sukuna or Gojo, who's actually taking this fight? We need receipts in the comments 👇 JJK figures in stock now. #jujutsukaisen #jjk #gojo #sukuna #anime"
**Why it works / Product bridge:** No-right-answer debate format is proven for comment volume (per existing content pillars doc). Keeps JJK inventory moving even with the show on hiatus between seasons.

---

### 🎥 V5 — "Bringing anitok back for one video"
**Format:** TikTok / IG Reel — 15-20 sec · **Suggested day:** Thursday · **Urgency:** Post this week — the revival trend is fresh (posts dated Aug 20-23), catch it before it peaks
**Driving signal:** Signal #5 — Score 15/20. #anitok revival community movement.
**Hook (0-3s):** Text overlay: "anitok revival, day 1" over throwback-style edit
**Beats:**
1. (0-4s) Deliberately 2021-coded edit style (jump cuts, "if you know you know" energy)
2. (4-12s) Quick nostalgia hits — old-school anime moments the community is resurfacing (AOT, DBZ throwbacks per this week's scan), no new commentary, let the format speak
3. (12-18s) Pull back to reveal it's shot in the Shumi store — "still here, still watching"
4. (18-20s) End card: "the classics are always in stock"
**Trending audio:** **"Dont like1" by 𝑵** — sound ID `7050216485842651910` — the exact throwback sound powering this revival (used on 5.9M-play and 1.2M-play posts already this cycle)
**Visual direction:** In-store shot, nostalgic color grade if editing allows. This is a community/culture play, not a product-first post — keep it earnest, not ironic (per brand voice rule).
**Caption:** "we heard anitok needed reviving so here we are 🫡 the classics never left. #anitok #anime #anitok2026 #animetiktok #otaku"
**Why it works / Product bridge:** Direct entry point for the community-building pillar — low product pressure, high fandom credibility. Builds the "we're fans first" positioning explicitly.

---

### 🎥 V6 — "The Minato and Naruto scene that still gets me"
**Format:** TikTok / IG Reel — 20 sec · **Suggested day:** Friday · **Urgency:** Evergreen — no expiry, backup-safe if another story breaks
**Driving signal:** Signal #8 — Score 14/20 + bonus. Naruto/Minato bond edit content, 3.6M plays.
**Hook (0-3s):** "Nobody talks about this Minato and Naruto moment enough—"
**Beats:**
1. (0-4s) Hook over Naruto figure shelf
2. (4-14s) Short emotional beat on the Minato/Naruto relationship — sincere, not analytical
3. (14-20s) End card: Naruto figures in stock, "your Naruto era has a home here"
**Trending audio: needs sound match** — sentimental/piano-style trending sound recommended, none confirmed in this scan; Kyle to check trending sounds day-of for an emotional-beat track.
**Visual direction:** Warm tones, Naruto shelf section, softer lighting than the JJK dark aesthetic.
**Caption:** "This is still one of the most slept-on father-son moments in anime and I will die on this hill. Naruto figures in stock — link in bio. #naruto #narutoshippuden #anime #minato"
**Why it works / Product bridge:** DBZ/Naruto flagged as reliable evergreen in existing Brain notes — low urgency, always performs, fills the week without competing for the OP/JJK spotlight.

---

### 🎥 V7 — "The Gol D. Roger figure just hit different after that announcement"
**Format:** IG Reel / TikTok — 20-25 sec · **Suggested day:** Sunday · **Urgency:** Evergreen/weekend capstone — ties back to V1's news for a full-week arc
**Driving signal:** Signal #6 — Score 15/20 + bonus. Gol D. Roger Funko grail framing, direct tie to God Valley film news.
**Hook (0-3s):** "This figure just became way more important" — hold up Roger Funko
**Beats:**
1. (0-4s) Hook, close-up on Roger figure
2. (4-14s) "3 figures I keep going back to" format — Roger + 2 other OP grails from the shelf, collector-culture framing, not sales pitch
3. (14-20s) Tie back: "and now we know we're getting his whole story"
4. (20-25s) End card: in-stock OP grails, link in bio
**Trending audio: needs sound match** — "shelf tour"/collector reveal format typically uses low-key original sound; no specific trending ID identified this scan.
**Visual direction:** Clean shelf photography per brand visual notes — dark background, scale shot if possible showing figure detail.
**Caption:** "This figure hit different after Sunday's announcement 🥹 3 One Piece grails we keep coming back to. In stock now — link in bio. #onepiece #goldroger #funkopop #onepiecefunko"
**Why it works / Product bridge:** Closes the week's One Piece arc (announcement → episode → manga → collector payoff), pure Figure Showcase/Collector Culture pillar, proven "from storage" format per existing scanner notes.

---

## Graphic Ideas (4)

### 🖼️ G1 — "GOD VALLEY IS COMING" announcement carousel
**Format:** IG carousel (4 slides) · **Suggested day:** Monday · **Urgency:** Post immediately alongside V1
**Driving signal:** Signal #1 — same news driver as V1, graphic companion for IG audience (Segment A collectors who scroll rather than watch).
**Slides:**
1. Bold type: "IT'S OFFICIAL." — Toei's God Valley film key art style treatment
2. "ONE PIECE FILM GOD VALLEY — Summer 2027"
3. "ONE PIECE FILM BAAD — 2029" + one-line context (Roger/Garp era)
4. Product slide: in-stock OP figures relevant to the Roger/God Valley era, "in stock now — link in bio"
**Visual direction:** Massive type per TBC layered-typography house style, dark background, product cutouts from real shumistore.com inventory photography — no stock imagery.
**Caption:** "We're getting the God Valley movie. Let that sink in. Summer 2027 — mark it. One Piece in stock now, link in bio. #onepiece #godvalley #anime #onepiecefunko"
**Product bridge:** Direct — Roger/Marine-era OP figures already in stock.

---

### 🖼️ G2 — "What just happened in Ch. 1191 + 1192" recap carousel
**Format:** IG carousel (5 slides) · **Suggested day:** Tuesday
**Driving signal:** Signal #2 — manga double-chapter return, Score 16/20.
**Slides:**
1. Title slide: "One Piece skipped 2 weeks then did THIS"
2. Recap slide 1 — Ch. 1191 beat (spoiler-light framing, "for the manga readers")
3. Recap slide 2 — Ch. 1192 beat
4. "Why it matters" — one line on Elbaf arc trajectory
5. Product slide: OP figures in stock, "link in bio"
**Visual direction:** Text-forward, minimal imagery to avoid manga-panel reproduction risk — pull key visual language (color, mood) rather than reprinting official art.
**Caption:** "Manga readers, we need to talk about 1191 and 1192 😭 One Piece in stock now — link in bio. #onepiece #manga #anime #luffy"
**Product bridge:** OP shelf, general.

---

### 🖼️ G3 — "New arrivals: MegaHouse Tobimas One Piece" static
**Format:** Static graphic (single image) · **Suggested day:** Thursday
**Driving signal:** Signal #7 — Score 14/20 + bonus. MegaHouse's flying-pose Tobimas line, December 2026 release, riding this week's overall OP wave.
**Visual direction:** Clean product-forward static — dark background, MegaHouse Tobimas figures (Straw Hat crew, flying poses) hero-lit. This is the one graphic that's allowed to be more product-first since it's genuinely new-arrival news, not a recycled SKU push. **Note:** Shumi's confirmed MegaHouse relationship is in the catalog — verify these exact SKUs are ones Shumi will actually carry before publishing; if not yet confirmed in-stock, reframe as "coming soon" rather than "in stock now."
**Caption:** "The Tobimas line is back and the Straw Hats have never looked this fun. Coming December. #onepiece #megahouse #anime #strawhatpirates"
**Product bridge:** Direct — new arrival, if Shumi confirms carrying this SKU.

---

### 🖼️ G4 — "Sukuna or Gojo" power ranking static
**Format:** Static graphic / IG carousel (3 slides) · **Suggested day:** Friday
**Driving signal:** Signal #4 companion — JJK edit trend, community debate pillar, pairs with V4.
**Slides (if carousel):**
1. "Sukuna or Gojo" bold type split-screen graphic
2. Quick case for each (2-3 words each side, meme-format)
3. Product slide: JJK Pop Up Parade / Nendoroid figures in stock
**Visual direction:** Dark JJK aesthetic, split-screen composition, high-contrast type.
**Caption:** "There's no wrong answer here (there's definitely a wrong answer). Sukuna or Gojo? JJK figures in stock now. #jujutsukaisen #jjk #gojo #sukuna"
**Product bridge:** JJK shelf.

---

## Trending Audio to Bookmark (Even If Unused Today)

- **"Dont like1" by 𝑵** — `7050216485842651910` — anitok revival throwback anchor sound, likely keeps climbing as the revival trend builds through next week
- **mysticreign original sound (Sukuna edit)** — `7675470995989252894` — still fresh (posted Aug 18), worth reusing for JJK content into next week
- **Toei Animation official announcement audio** — `7677173394780982046` — grab now while the God Valley news cycle is hot; utility drops fast after this week

---

## Strategic Notes

1. **One Piece is a three-headline week.** Film announcement + manga return + episode airing all land in the same 7-day window. This almost never happens — lean hard into OP this week even though it skews the slate 4-of-11 toward one franchise. Rebalance next week.
2. **JJK doesn't need new episodes to perform.** The fandom is sustaining massive edit volume on a concluded season purely through original-audio edit culture. This validates keeping JJK in weekly rotation as a reliable evergreen pillar, not just a "when S4 drops" play.
3. **#anitok revival is a live community movement, not a one-off meme.** Worth checking again next Monday — if it's still climbing, it may be worth a dedicated content week rather than one video.
4. **IG hashtag scraping under-delivers competitor intelligence.** This week's #animefigures/#funkopop pull returned reseller/individual-collector noise, not the tracked competitor list. Recommend Kyle manually spot-check Crunchyroll Store, Hot Topic, and POP MART's IG grids directly next run rather than relying solely on hashtag scrape for competitor read.
5. **MegaHouse Tobimas SKU needs a confirm-before-publish check.** G3 assumes Shumi will carry this exact new MegaHouse line — flagged in the idea itself, don't post without Nghia/Priscilla confirming inventory.

---

## Infrastructure / Process Notes

- **X/Grok signal not captured this run.** Per `reference_x_via_grok.md`, the Grok integration path is still unwired in this session (no matching tool found via search). Anthony: confirm whether/how Grok-on-X access should be wired for future scheduled runs, or whether this source should be formally dropped from the skill.
- **Apify actors used:** `clockworks/tiktok-hashtag-scraper` (60 items, ~$0.18 est.) and `apify/instagram-hashtag-scraper` (30 items pulled of 39 returned, ~$0.08 est.). No rate-limit or actor failures this run.
- **Crunchyroll News WebFetch returned no article content** (page-shell/JS-rendered issue, consistent with prior runs likely) — MAL and ANN WebFetch worked fine and covered the gap.

---

*Sources scanned: ANN (WebFetch, success), Crunchyroll News (WebFetch, no content — JS-rendered), MAL News (WebFetch, success), WebSearch x3, X via Grok (not captured), TikTok via Apify (60 items), IG via Apify (30 of 39 items) | Raw signals: ~34 | Above threshold (14+): 19 | Slated: 11*

*Prepared by Shumi Anime Scanner · 2026-08-24 · Next slate: 2026-08-31 · Questions → Anthony*
