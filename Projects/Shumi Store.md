---
title: Shumi Store
type: client
status: active-onboarding
tags: [client, anime, ecommerce, creative-only, new-client-2026-05]
last_updated: 2026-06-18
related: ["[[Kyle Fuller]]", "[[Abril Rodriguez]]", "[[Brand With Us]]", "[[Projects/00-INDEX]]"]
---

# Shumi Store

> Stub note created 2026-05-27 alongside the [[Shumi Anime Scanner]] skill. Full onboarding intake (content strategy doc, full brand kit, calendar) is owed by Launchpad team — Kyle Fuller lead, Abril Rodriguez ops. Expand this note as those deliverables land.

## Quick Facts

| Field | Value |
|---|---|
| **Legal/brand name** | Shumi Toys & Gifts (DBA "The Shumi Company" on IG) |
| **Etymology** | Shumi (趣味) = "hobby" in Japanese |
| **Website** | https://shumistore.com/ |
| **Instagram** | https://www.instagram.com/shumination/ (handle: @shumination) |
| **Physical store** | West Covina, California |
| **Signed** | 2026-05-19 |
| **Package** | Custom. ⚠️ **CORRECTION 2026-06-18:** earlier "creative-only — client posts" framing is OUTDATED. Shumi **has a GHL sub-account** and Apollo schedules its posts like any other SMM client. (Old note flagged, not deleted, per Brain rules.) |
| **GHL wired** | ✅ Yes. Token `GHL_TOKEN_SHUMI` + `GHL_LOCATION_SHUMI` in `.env`; MCP snippet `.claude/mcp-clients/shumi.json` (generated 2026-06-18 — was missing, which caused the SMM pipeline to skip Shumi). Server name `gohighlevel-shumi`. |
| **Status** | 🟡 Onboarding — multiple client-side access blockers; content strategy + calendar still owed |
| **Client contact** | Nghia Hoang |
| **Launchpad lead** | [[Kyle Fuller]] |
| **Launchpad ops** | [[Abril Rodriguez]] |
| **Media day** | Scheduled post-2026-06-01 (when Nghia returns) |

> **2026-06-18 — SMM pipeline fix.** Shumi's July Content Calendar task wasn't running because (a) it was assigned to **Cynthia, not Apollo** (the n8n watcher only fires Apollo-assigned tasks), (b) it was stuck in **"In production"** (watcher only fires "Not started"), and (c) Shumi had **no MCP snippet** and wasn't in the listener's client-detection map. Fixes: generated `shumi.json` from `.env`, made the listener auto-discover all client snippets, and added `scripts/sync-client-mcp.sh` so `.env` is the single source of truth. The `tags: creative-only` in frontmatter is now stale — leaving for Anthony to confirm before removing.

## What They Sell

Anime & pop-culture collectibles. Multi-franchise, shonen-heavy:

- **Franchises:** Naruto, One Piece, My Hero Academia, Jujutsu Kaisen, Demon Slayer, Dragon Ball Z, Haikyu — plus Marvel, DC, Disney, Pokémon
- **Product types:** Funko POPs, Nendoroids, Pop Up Parade figures, FiGPiN, blind boxes, plushies, pop protectors, apparel (tees), stickers, accessories
- **Price range:** ~$14.99–$39.99+ (premium exclusives higher)

## Target Customer

Gen Z + millennial anime collectors. Range from casual fans (blind box impulse buyers) to serious collectors (chasing variants/exclusives). Community-minded — they care about the fandom, not just the product.

## Brand Voice

- Casual, enthusiast-to-enthusiast — "we're fans first"
- Community-forward — "Shumi cultivates a community that shares happiness"
- Authentic-product positioning (vs. bootleg market)
- Not corporate, not ironic — earnest hype is fine
- Japanese word "Shumi" = built-in cultural credibility, use it

## Content Strategy (per 2026-05-19 onboarding meeting)

**Strategic shift documented:** *"Move from product-only posts to community-building content (anime news/memes leading into product showcases). Will use website inventory for graphics/carousels. Kyle handles trend content from Vegas. Live event coverage handled by client with shot-list briefs from Launchpad team."*

What this means for content:
1. **Anime news + memes lead** — products follow. Don't open with the SKU.
2. **Website inventory = source for graphics** — products we already have on shumistore.com are fair game for any carousel/static.
3. **Vegas-based trend content** — Kyle Fuller produces from Vegas, not the West Covina store.
4. **Live event coverage** = client-side (Nghia's team) with shot lists from us.

Platforms in scope: **TikTok + Instagram** (daily posting). Other platforms (YouTube, X) — not active under this engagement.

## Open Blockers (as of 2026-05-22 Weekly Health Report)

- TikTok login access — goes to Priscilla's email, not Launchpad
- Microsoft Teams generic email setup — pending
- Shopify access — pending
- Content strategy doc — owed to client by Launchpad
- Content calendar — owed to client by Launchpad
- Rebrand evaluation — requested by client

## GHL Sub-Account (added 2026-06-01)

- **Location ID:** `RPGcYwtea93GSFile2Yu`
- **Token env:** `GHL_TOKEN_SHUMI` (pit-format)
- **MCP server:** `gohighlevel-shumi` (allowlist entry committed)
- **Connected social accounts (verified live 2026-06-01):**
  - Instagram (`shumination`) — id `6a1dcdc63947916f3b2a2b01_RPGcYwtea93GSFile2Yu_17841406735834998`
  - TikTok ("The Shumi Company") — id `6a1dcf32518563b35069d9d7_RPGcYwtea93GSFile2Yu_000ZLZe0M1r39OAo76zqjGZRZG7efFUI_business`
- **No Facebook** (by brand strategy — IG + TikTok only)
- **Content Approver:** Priscilla — GHL user ID UNRESOLVED. Token Users scope is OFF; Anthony to enable in GHL Settings > Integrations > Private Integrations.
- **SMM Calendar tasks (Notion):** "Shumi June 26' Content Calendar" (`372b01f77d6d80998c17ed184e87b915`) + "Shumi Content Calendar July 26'" (`372b01f77d6d80c88392c6ea985c1250`) — both stub templates, briefs not yet filled.
- **Agent memory:** `.claude/agent-memory/social-media-poster/shumi_patterns.md`
- **Open blocker for Apollo run:** shared Drive folder not yet provisioned for Apollo access — Anthony to share or provide explicit Drive URL.

## Linked Skills / Automation

- [[Shumi Anime Scanner]] — weekly anime niche trend scanner (X, Reddit, IG, TikTok, anime news) running every Monday 7 AM PT, producing a Weekly Content Slate of 7 video + 4 graphic ideas for TikTok + IG. Output → `marketing/output/reports/shumi/shumi-slate-week-of-YYYY-MM-DD.md`.

## Sources

- Onboarding meeting 2026-05-19 (in Notion meeting notes; referenced from [[Weekly Health Report - 2026-05-22]])
- Site analysis 2026-05-27 (WebFetch of shumistore.com)
- [[Daily/2026-05-27]] roster snapshot

---

## Deep Context — 2026-06-01

> Added by Client Onboarding Agent. Sources: Notion onboarding transcript (365b01f7), SHUMI STORE portal (366b01f7), shumistore.com full site scan, Shumi Anime Scanner slates (2026-05-27 + 2026-06-01), Weekly Health Reports 2026-05-22 + 2026-05-29, competitor web research.

---

### Leadership + Org Structure

- **CEO:** Nghia Hoang (nghia.hoang@shumistore.com) — main client contact, prefers mobile-friendly Kanban approvals, not long review meetings
- **COO:** Priscilla L. — content approver in GHL, also owns TikTok login credentials
- **Ryan (Florida)** — external contractor; manages Klaviyo newsletter + blog content for major shows (Anime Expo, San Diego Comic-Con). Gap: doesn't cover regular ongoing content between events. That gap is exactly what Launchpad fills.
- **Gary** — referenced in onboarding as returning from travel post-6/1; associated with media day scheduling. Role unclear — confirm with Nghia.
- **Phone:** +1 (818) 259-6440
- **LinkedIn:** https://www.linkedin.com/company/the-shumi-company

---

### Company Facts (corrected/expanded)

- **Founded:** 2017 (per Notion portal — previously listed as unknown)
- **HQ:** Alhambra, California (portal says Alhambra; store/storefront is West Covina CA — likely different addresses for HQ vs retail)
- **Physical store hours:** Mon–Sat 11AM–8PM PST; Sun 11AM–7PM PST
- **Branding age:** Current brand has been in place ~7 years (per onboarding transcript)
- **Wholesale division:** Shumi Distribution (separate entity — operates alongside retail)
- **Primary sales channels (ranked by traffic per onboarding):**
  1. Target marketplace
  2. Walmart marketplace
  3. TikTok Shop
  4. Facebook Shop / Instagram Shop (lower traffic)
  5. shumistore.com (direct — this is what Launchpad content should drive)
- **E-commerce platform:** Shopify
- **Newsletter platform:** Klaviyo (managed by Ryan)
- **Inventory:** "Warehouse full of inventory but lacks visibility" — key strategic insight from Nghia. The product exists; the problem is awareness and discoverability.
- **Upcoming licensing launch:** Nghia referenced an upcoming exclusive licensing deal that will give Shumi unique products competitors can't carry. Details TBD — ask Nghia for more context when available. <!-- NEEDS: licensing deal details — what franchise/manufacturer? timeline? -->

---

### Product Catalog — Full Breakdown

**Manufacturers carried:**
Funko, Bandai (Banpresto, Tamashii Nations), Good Smile Company (Nendoroid, Pop Up Parade), FuRyu, SEGA, Taito, Aniplex, Megahouse, Kotobukiya, Hasbro, Loungefly, POP MART, FiGPiN, MJ Studio

**Categories:**
- Funko POPs (standard + exclusives + 10" jumbos + Pop Plus + SODA + Blacklight)
- Nendoroids (chibi-style articulated figures, $50–$70 range)
- Pop Up Parade (Good Smile mid-tier, $30–$50)
- Banpresto / SEGA / FuRyu / Taito prize figures ($20–$40)
- Blind boxes (POP MART, Sonny Angel, MOFUSAND, anime-specific series)
- Plushies + plush keychains ($10–$25)
- FiGPiN (enamel pin figures, $15–$30)
- Pop protectors (utility item — recurring revenue play)
- Stickers + accessories
- Apparel (tees — limited range)
- Exclusives (310 total listed; 96 in stock as of site scan)

**Price architecture:**
- Entry: $5.99–$14.99 (stickers, keychains, mini blind boxes)
- Core: $15.99–$29.99 (most Funko POPs, prize figures, blind box series)
- Mid-premium: $30–$49.99 (Pop Up Parade, Nendoroids, premium exclusives)
- High-end: $50–$70+ (Nendoroids, limited Hello Kitty 50th anniversary at $49.99, premium scale figures)
- Flat rate shipping: $5 (US contiguous)

**Top franchise coverage (confirmed on site):**
One Piece, Naruto, Jujutsu Kaisen, My Hero Academia, Demon Slayer, Dragon Ball Z/Super, Haikyu, Attack on Titan, Pokémon, Marvel, DC, Disney, Gundam, Astro Boy, Sonic, Sanrio/Hello Kitty

**Signature / featured product types (Nghia confirmed pushing):**
- Blind boxes (impulse buy, gift play, community "pull" content)
- Sonny Angel (lifestyle/gifting crossover, not purely anime — broader audience)
- Weekly new arrivals (Shopify website stock = accurate for content planning)

**Exclusives inventory note:** 214 of 310 exclusives are sold out or pre-order — suggests strong demand and sell-through. High proportion of One Piece and Naruto exclusives. Most exclusive SKUs are Funko variants (glow, flocked, blacklight, unmasked).

---

### Brand Voice — Calibrated

**Core identity phrase (from About page):** "Together at Shumi, our team is dedicated to fostering unforgettable experiences with fans and collectors."

**Voice descriptors (high-conviction):**
- Enthusiast-to-enthusiast — write as a fellow fan, not a retailer
- Community-forward — "we" not "you should buy"
- Earnest hype — genuine excitement is fine, irony is not
- Approachable authority — knows the fandom deeply, explains things clearly
- Culturally grounded — "Shumi" (趣味 = hobby) is a real Japanese word, lean into it naturally

**Tone spectrum:**
- Hype: high (product drops, episode reactions, news breaks)
- Humor: medium (memes and playful takes, not sarcasm)
- Educational: medium (lore explainers, "who is" posts, character spotlights)
- Emotional: low-medium (save for milestone episodes, community moments)
- Corporate: zero — do not sound like a store ad

**Language to USE:**
- "We're fans first"
- "Your [franchise] era has a home at Shumi"
- "The community" (not "our customers" or "our followers")
- "In stock now at shumistore.com" (direct, no fluff)
- Character names used casually — assume the audience knows them
- "Drop" for product arrivals (not "now available" or "shop now")
- "Grab" not "purchase"
- Franchise-specific slang is fine (e.g. "Nakama," "Plus Ultra," "Believe It" — use contextually, not forced)

**Language to AVOID:**
- "Shop our collection" (generic retail)
- "Limited time offer" / "Don't miss out" (pressure tactics)
- "Officially licensed merchandise" (assumed, doesn't need saying)
- "We have something for everyone" (vague)
- "Anime lovers" or "anime fans" as the subject (talk to them directly)
- Em dashes (global rule — Critical Rule 19)
- Formal punctuation in captions — keep it casual

**Tone calibration vs competitor set:**
- Less ironic than Hot Topic (HT leans into alt/edgy; Shumi is earnest)
- More community than Crunchyroll Store (CR is an arm of a corporation; Shumi is a store run by fans)
- More personality than Entertainment Earth (EE is catalog-driven; Shumi has opinions)
- More accessible than AmiAmi (AmiAmi targets import collectors; Shumi targets casual-to-serious US collectors)
- More culturally specific than POP MART US (POP MART is lifestyle/art toy; Shumi is anime-specific)

**Existing blog voice signal (from Ryan's blog content):**
- Conversational, emoji-inclusive headlines
- Ranked lists + episode breakdowns dominant
- "That broke our hearts," "together at Shumi" — collaborative, emotional resonance
- Series reviewed: Re:Zero, Studio Bones overview, Witch Hat Atelier, Daemons of the Shadow Realm — not just mainstream, has indie/niche credibility

---

### Content Pillars

**5 pillars — 60/40 viral vs evergreen split**

**Viral / Trend-Responsive (60%)**

1. **Anime News Reaction** — Break news fast. Episode drops, season confirmations, casting announcements, manga chapter moments. Format: 20–30 sec reaction reel. Hook: "Did you see what just happened in [show]?" Kyle on camera, product bridge on end card. Franchises to prioritize: JJK, One Piece, MHA, Demon Slayer, DBZ, Naruto (based on scanner signal volume).

2. **Product Drop + Reveal** — New inventory arrivals, especially exclusives and new Funko waves. Lead with the product as news, not as a sales pitch. "The new One Piece Funko wave just dropped and we need to talk about Saint Saturn's 10-inch beast form." Drives direct conversion. Highest commercial intent of any pillar.

3. **Community / Debate Format** — Tier lists, power rankings, "who's the strongest," fandom arguments. No right answer = comment section ignites. Pairs naturally with figure display. Key recurring formats: JJK power ranking, "best arc" debates, Big 3 slander, character birthday spotlights.

**Evergreen / Retention-Building (40%)**

4. **Figure Showcase + Collector Culture** — "3 figures I keep going back to," shelf checks, unboxing reveals, figure photography. The "from storage" format (264K plays, 19.6K likes observed by scanner) is proven. Audience: serious collectors who stay engaged between new releases.

5. **Anime Education + Lore** — Character profiles, arc explainers, lore timelines ("God Valley — Why It Matters"). High save rate. Blog content (Ryan's output) is the written layer; social is the short-form layer. Positions Shumi as the knowledgeable friend, not just the store.

**Content mix signals from Apollo scanner (two-week pattern):**
- JJK dominates video signal (highest TikTok volume, most episode urgency)
- One Piece dominates graphic/carousel signal (chapter drops + product waves)
- Anitok revival = community entry point (use to onboard new followers)
- DBZ + Naruto = reliable evergreen (low urgency, always works)
- MHA spikes around Netflix drops and figure releases

---

### Audience Segments

**Segment A — The Serious Collector**
- Age: 20–32
- Platforms: IG primary (figure photography, carousel lore), TikTok secondary
- Behavior: tracks exclusives, chases variants/sold-outs, researches before buying
- Pain point: hard to find specific exclusives; don't want bootlegs; care about authenticity
- Desire: grail figures, exclusive drops, store they can trust
- Content that works: exclusives inventory posts, figure reveal carousels, product comparison
- CTA that works: "In stock now — link in bio" (direct, respects their research mindset)

**Segment B — The Casual Fan / Impulse Buyer**
- Age: 16–28
- Platforms: TikTok primary, IG secondary
- Behavior: follows the current season, buys after seeing a post, gifting occasions (birthdays, holidays)
- Pain point: doesn't know where to buy; price-sensitive; intimidated by the collector world
- Desire: something cool from their favorite show at a reasonable price
- Content that works: anime news reactions, "what to get [show] fans" gift guides, blind box reveals
- CTA that works: "Only $14.99 at shumistore.com" (price + direct link removes friction)

**Segment C — The Gift Buyer**
- Age: 25–45 (often parents, partners, friends buying for the fan in their life)
- Platforms: likely finds Shumi via Google/TikTok/Target/Walmart marketplace
- Behavior: doesn't know franchises well, needs guidance, price sensitive to mid-range
- Pain point: doesn't know if something is "good" or "the right one"
- Desire: curated, clear recommendations; approachable store
- Content that works: "best gifts for [show] fans," Sonny Angel gift guides, blind boxes (low-risk gift)
- CTA that works: "$5 flat rate shipping" + "gift-ready" framing
- Note: Sonny Angel inventory is a direct bridge to this segment (non-anime, gift-focused product line)

**Platform behavior split:**
- TikTok: Segment B dominant. Short-form, trend-reactive, new audience acquisition. Under 30 sec performs best. Entry point for the brand.
- Instagram: Segment A + C. Carousels for collectors (saves/shares), statics for gift season, Reels for news reaction. Longer dwell time per post.
- Shopify: All three segments post-social funnel. Target/Walmart = Segment B/C entry via marketplace.

---

### Visual Identity

**Current state (7-year-old brand, rebrand evaluation in progress):**
- Website aesthetic: clean white background, minimal design, grid-based product display
- Logo: "Shumi Toys & Gifts" centered wordmark (approximate 140px width on site)
- Typography: modern sans-serif for nav/product titles; no decorative or display type observed
- Color palette: site uses white primary with accent colors drawn from product imagery — no strong brand color system identified from web scan <!-- NEEDS: exact hex codes from brand kit — Nghia to provide logos + brand guidelines per onboarding action items -->
- Vibe: functional/clean vs branded/emotional — the current site doesn't communicate the brand personality well. This is the gap the rebrand evaluation is trying to close.

**Photo style observed (blog + product pages):**
- Product photography: clean studio shots on white or neutral backgrounds
- No lifestyle photography or in-store environment shots on site (those are for social)
- Blog uses anime screenshot/key art + character imagery (licensed promotional assets)

**What photo style should look like for social (inferred from scanner competitor analysis):**
- Clean, high-contrast product shots on dark backgrounds (obsidian/navy) — used by @astop_cultureszone (Akihabara) and top-performing IG animefigures posts
- In-store wide shots for community/anitok content — the Shumi retail space is a visual asset
- Kyle on camera for video — personal face builds parasocial community faster than faceless brand
- Scale shots (show figure size vs hand/other object) for 10" jumbos and premium figures
- Dark aesthetic for JJK/dark anime content; warmer tones for One Piece/MHA/collector culture

**Rebrand note (flagged by Nghia in onboarding):**
- Client open to rebrand if it elevates the brand
- Team to provide rebrand proposal
- Priority: the brand name and Japanese etymology ("趣味") are strong assets — any rebrand should lean into them, not away from them
- Risk flag: "Shumi Nation" branding (used on GHL, Instagram) differs from "Shumi Toys & Gifts" (legal/site). If a rebrand happens, name consolidation should be part of the scope.

---

### Competitive Landscape

**Direct competitors (US anime collectibles e-commerce, overlapping audience):**

1. **Crunchyroll Store / Right Stuf Anime** (store.crunchyroll.com) — The 800-lb gorilla. Backed by Sony, official licensing for hundreds of titles, free shipping over $75. What they do well: brand recognition, streaming tie-in, exclusive products. What they don't: no personality, corporate voice, no community content. Differentiation opportunity: Shumi is the friend who knows anime; Crunchyroll Store is the kiosk.

2. **Hot Topic** (hottopic.com/anime) — Mass-market alt-retail. Anime is one of many verticals alongside music, gaming, TV. Heavy discounting (20% off sitewide is standard). What they do well: physical retail presence, mainstream franchise licensing, teen price points. What they don't: no depth, no collector credibility, everything is on clearance. Differentiation: Shumi is for fans who take collecting seriously; Hot Topic is for casual merch buyers.

3. **POP MART US** (popmart.com/us) — Blind box specialists, art toy positioning, strong Gen Z lifestyle presence. What they do well: the blind box experience (pull mechanic, FOMO, community of "pulls"), aspirational brand, social content. What they don't: not anime-specific — IP roster skews toward POP MART originals and non-anime characters. Differentiation: Shumi carries POP MART product but adds the anime community context POP MART lacks. Shumi can do "best blind boxes for [franchise] fans" content that POP MART can't credibly do.

4. **Entertainment Earth** (entertainmentearth.com) — Specialty collector retailer, catalog-driven, pre-order focus. What they do well: deep exclusives catalog, early pre-order access, collector-grade product pages. What they don't: zero personality, no content, sterile brand. Differentiation: Shumi knows its customers by name (figuratively); Entertainment Earth treats them as order numbers.

5. **Local/regional anime shops** (e.g. Mercari/eBay resellers, local convention booths) — The long tail. Competitive on price and locality for West Covina/LA area. What they do well: impulse buys at events, face-to-face community. What they don't: no consistent online presence, no curation. Differentiation: Shumi has the brand, the warehouse depth, and the content engine that local sellers can't build.

**Key competitive insight (from scanner IG scan):** 7 of 10 top #animefigures IG posts belong to competitors doing dry product photography with 0–2 likes. "Anime news + memes lead, products follow" strategy is unoccupied at scale. This is Shumi's wedge.

---

### Lead-Gen + CTA Patterns

**What works for this brand (inferred from audience + product mix):**

- **Restock alerts** — High-demand sold-out exclusives (Dracule Mihawk, Zoro Nothing Happened, Gojo Satoru) have a built-in waitlist audience. "Back in stock" posts + "DM us for restock alerts" builds a direct opt-in channel.
- **Blind box pull reveals** — "Pull with us" content (open a blind box on camera) drives comments, shares, saves. Blind box mystery = built-in engagement mechanic. Ties to FOMO purchase behavior.
- **Episode drop tie-ins with product CTAs** — Scanner confirms this is the highest-conversion content pattern. Episode airs → post goes up same day → "figure is in stock" end card → link in bio. Short window (24–48 hrs peak) but high intent.
- **Convention/event coverage** — Shumi attends Fanome, Riverside, Fan Expo Denver, Anime Expo, San Diego Comic-Con. Event content = community trust signal + urgency (booth number, limited inventory at event). Event posts drive both online and booth traffic.
- **Giveaway mechanics** — Scanner observed @nin_nin_game giveaway driving 2.2K comments (10–50x standard engagement). A Shumi giveaway around a grail figure (sold-out exclusive) or blind box mystery bundle would spike followers + engagement. Use sparingly — reserve for milestone moments.
- **"Drop of the week" recurring format** — Weekly new arrivals series (every Monday or Friday). Builds habitual following. Audience knows to check Shumi for what landed.
- **TikTok Shop integration** — Already connected. Native TikTok shop links on product videos bypass the "link in bio" friction for TikTok-first buyers. Priority for video content that has direct SKU bridge.

**What does NOT fit this brand:**
- Discount/coupon-led CTAs (erodes collector-grade positioning)
- Generic "shop now" without a product-specific hook
- Newsletter hard-sell (Klaviyo is already in place; don't double-up without coordination with Ryan)
- YouTube (not in scope per onboarding — no active engagement under this contract)

---

### Event Coverage Context

Per onboarding transcript, Shumi attends conventions actively:
- Events confirmed as of May 2026: **Fanome** (week of 5/19), **Riverside** (week of 5/26), **Fan Expo Denver** (week of 5/26)
- Major annual events: **Anime Expo** (July, LA) and **San Diego Comic-Con** (July) — Ryan handles blog content for these
- Some events booked 6 months out; others are last-minute additions
- **Shot list + brief model:** Nghia/store team shoots at events, Launchpad provides shot list + brief. Event posts include booth number and map location.
- Convention content = highest-authenticity content Shumi can produce (fan interactions, booth atmosphere, exclusive drops, cosplay, panels)

---

### Open Questions for Nghia / Priscilla / Kyle

Items that would meaningfully improve agent output if answered:

1. **Brand colors (hex codes)** — Current brand kit not yet delivered. Needed for: every graphic, every template, every Canva build. Priority: HIGH.
2. **Rebrand scope** — Is this a logo refresh, full visual identity overhaul, or name change? Timeline? Who is leading the design side?
3. **Licensing deal** — What franchise/manufacturer? When does it launch? This is a major content and PR moment if timed right.
4. **Gary's role** — Who is Gary? What does he do for Shumi? Mentioned in the media day context.
5. **Shopify access** — Has view-only access been granted yet? Needed for: Segment-level performance data, top SKUs to feature in content, restock timing.
6. **Sonny Angel strategy** — Is Shumi leaning into Sonny Angel as a standalone content category or keeping it as a secondary/gift item? (Sonny Angel has its own TikTok community — could be a separate content lane.)
7. **TikTok Shop product tagging** — Which SKUs are currently live in TikTok Shop? Can Apollo tag products in video posts via GHL? This changes the CTA strategy for TikTok content.
8. **Convention calendar 2026** — Full list of events Shumi is attending (with dates). Needed for: content calendar planning, event shot list briefs, pre-event hype posts.
9. **Warehouse inventory depth** — Are there specific franchises where Shumi is overstocked and wants to move inventory? (Nghia said "warehouse full" — knowing what's overstocked vs what's selling would let Apollo prioritize content to inventory reality.)
10. **Priscilla's GHL user ID** — Still unresolved due to Users scope blocker. Anthony to add Users scope to GHL token.

---

### Onboarding Status Update — 2026-06-01 Team Brief

- **Production status:** 16 posts created, uploaded to Drive, ready to schedule via GHL CRM. Currently posting daily.
- **Remaining work:** 15 more graphics needed to complete month-end content.
- **Content approver update:** Nia is being added as GHL CRM user for content approvals (Priscilla also copied). Action item: Amber to add Nia to GHL, forward to Priscilla.
- **Brand meeting needed:** Schedule with Nia/Priscilla to discuss brand preferences and mascot feedback. Client raised concerns about "AI look" of mascot — needs direct conversation before visual templates are finalized.
- **Profile picture + current branding:** Stay as-is for now. Do not swap logo or avatar until brand meeting happens.
- **Content buckets confirmed:** anime news, memes, giveaways/promos, product showcases.
- **Launch definition:** Shumi is NOT considered launched until ads are running.
- **Microsoft CRM integration:** Completed.
- **Key challenge:** Very niche anime content requires detailed ideation and specific graphic layouts for designers — account requires more pre-brief work than average.

---

### Data Sources Used

- Notion: Onboarding meeting notes `365b01f7-7d6d-80f2-ab55-e8a3345c3e49` (May 19, 2026)
- Notion: SHUMI STORE portal `366b01f7-7d6d-8046-a397-da92be67b502`
- Notion: Shumi Store (NEW) health tracker `369b01f7-7d6d-814c-8dab-f095b9d1b2c3`
- Notion: CMD page `263b01f7-7d6d-802c-a9c8-fe76c5a98dd0` (posting schedule confirmed)
- Brain: Weekly Health Reports 2026-05-22 + 2026-05-29
- Brain: Shumi Anime Scanner slates `marketing/output/reports/shumi/shumi-slate-week-of-2026-05-27.md` + `...2026-06-01.md`
- Web: shumistore.com (homepage, collections/all, collections/exclusives, blogs/news, pages/about-us)
- Web: store.crunchyroll.com, hottopic.com/anime, competitor research
- SMM Poster memory: `.claude/agent-memory/social-media-poster/shumi_patterns.md`

---

## Sync Log

- **2026-06-29** — Notion-to-Brain sync re-verified: Status=Onboarding, Package=Custom, Ad Spend=$0, Start=2026-05-19. No field changes. Current Deliverables section refreshed.
- **2026-06-26** — Notion-to-Brain sync verified all fields current: Status=Onboarding, Package=Custom, Ad Spend=$0, Start=2026-05-19. No updates required.
- **2026-06-18** — Status updated from "At Risk (new)" to "Onboarding" (synced from Notion Client Portals, confirmed Package: Custom, Ad Spend: $0)

<!-- Sections below added 2026-10-19 per [[Client Note Schema]]; the nightly filing writes here. Dated, append-only. -->

## Preferences & Corrections

## Decisions

## Activity Log

## Open Items
