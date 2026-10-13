---
title: "GHL MCP Capability Matrix"
type: reference
status: active
tier: secondary
last_updated: 2026-04-20
related: "[[GHL Event Ticketing — Multi-Attendee Capture Architecture 2026-04-20]]"
related: ["[[Intelligence/00-INDEX]]"]
---

# GHL MCP Capability Matrix

**Purpose:** Definitive answer to "what can AI automate in GHL vs. what requires a human in the UI." Use this before scoping any GHL build so we know what's realistic to automate.

**MCP Connections Available (as of 2026-04-20):**
- `gohighlevel-agency` — agency-level access
- `gohighlevel-launchpad` — Launchpad BizDev sub-account (Location ID: `hbcsvkyO40fTLTbsL1lI`)

**Per-client sub-account MCPs still need to be wired** — see [[feedback_ghl_token_architecture]]. Each client with a GHL sub-account needs its own Private Integration Token + MCP entry before AI can operate on their data.

---

## TL;DR — The Big Picture

**AI CAN automate:**
- Contacts (full CRUD + tags + custom field values)
- Blogs (full CRUD — post creation, editing, publishing)
- Email templates (create + fetch)
- Conversations (send SMS, Email, WhatsApp, IG, FB messages; schedule messages)
- Social media posts (full CRUD across platforms)
- Opportunities (read + update, but NOT create)
- Payments + Orders (read only)
- Calendar events (read only)

**AI CANNOT automate — human UI work required:**
- Funnels / Landing pages (create, edit, design)
- **Surveys** (create slides, conditional logic, field mapping)
- Forms (create — only receive data via webhook)
- **Workflows / Automations** (create, edit triggers or actions)
- Products / Shopping cart / Checkout configuration
- Memberships / Communities / Portal access
- Email campaigns / drip sequences (scheduling + triggering)
- SMS campaigns (bulk)
- Custom field creation (only reading is supported)
- Calendar creation + availability configuration
- Users / Team member management
- Website builder
- Invoices / Estimates / Subscriptions (creation)

---

## FULL CAPABILITY MATRIX

### CONTACTS — Full CRUD ✅

| Capability | Available | Tool |
|---|---|---|
| Create contact | ✅ | `contacts_create-contact` |
| Upsert contact (dedupe on email) | ✅ | `contacts_upsert-contact` |
| Get single contact by ID | ✅ | `contacts_get-contact` |
| List contacts with pagination | ✅ | `contacts_get-contacts` |
| Update contact fields | ✅ | `contacts_update-contact` |
| Add tags | ✅ | `contacts_add-tags` |
| Remove tags | ✅ | `contacts_remove-tags` |
| Get contact's tasks | ✅ | `contacts_get-all-tasks` |
| Delete contact | ❌ | Not exposed |
| Merge contacts | ❌ | Not exposed |

**What this unlocks for automation:**
- AI can maintain contact hygiene (enrich, dedupe, update)
- AI can tag at scale based on rules (event attendance, engagement, source)
- AI can push fields from ChatGPT/external sources into GHL
- AI can manage pipeline contact lists via tags

---

### BLOGS — Full CRUD ✅

| Capability | Available | Tool |
|---|---|---|
| Create blog post (with HTML, SEO, scheduling) | ✅ | `blogs_create-blog-post` |
| Update blog post | ✅ | `blogs_update-blog-post` |
| Get single post | ✅ | `blogs_get-blog-post` |
| List posts by status (draft, scheduled, published) | ✅ | `blogs_get-blog-post` |
| List blog sites | ✅ | `blogs_get-blogs` |
| Check URL slug availability | ✅ | `blogs_check-url-slug-exists` |
| List authors | ✅ | `blogs_get-all-blog-authors-by-location` |
| List categories | ✅ | `blogs_get-all-categories-by-location` |
| Delete blog post | ❌ | Only ARCHIVED status via update |

**What this unlocks for automation:**
- AI can fully own blog publishing (draft, schedule, publish, update)
- AI can handle SEO metadata (slugs, canonical, image alt text)
- AI can batch-publish content calendars

---

### EMAILS — Template Only ⚠️

| Capability | Available | Tool |
|---|---|---|
| Create email template (builder, HTML, imported) | ✅ | `emails_create-template` |
| Fetch template list | ✅ | `emails_fetch-template` |
| Import from Mailchimp/ActiveCampaign/Kajabi | ✅ | `emails_create-template` with importProvider |
| Send one-off email to contact | ✅ | `conversations_send-a-new-message` (type: Email) |
| Schedule email | ✅ (via send-message) | `conversations_send-a-new-message` with scheduledTimestamp |
| Create email campaign (drip/sequence) | ❌ | Campaigns are workflow-driven; not exposed |
| Trigger a workflow-based email | ❌ | No workflow API |
| Delete template | ❌ | Not exposed |

**What this unlocks for automation:**
- AI can populate the template library so humans don't write from scratch
- AI can send one-off transactional emails (confirmations, follow-ups)
- AI can schedule future-dated messages
- ⚠️ Drip campaigns and workflow-triggered emails are HUMAN UI work

---

### CONVERSATIONS — Full Send + Read ✅

| Capability | Available | Tool |
|---|---|---|
| Send SMS | ✅ | `conversations_send-a-new-message` (type: SMS) |
| Send Email | ✅ | `conversations_send-a-new-message` (type: Email) |
| Send WhatsApp | ✅ | `conversations_send-a-new-message` (type: WhatsApp) |
| Send Instagram DM | ✅ | `conversations_send-a-new-message` (type: IG) |
| Send Facebook DM | ✅ | `conversations_send-a-new-message` (type: FB) |
| Send Live Chat | ✅ | `conversations_send-a-new-message` (type: Live_Chat) |
| Attach files to messages | ✅ | body_attachments array |
| Schedule message send | ✅ | body_scheduledTimestamp |
| Reply to thread | ✅ | body_threadId + body_replyMessageId |
| CC / BCC emails | ✅ | body_emailCc / body_emailBcc |
| Use template in message | ✅ | body_templateId |
| Search conversations | ✅ | `conversations_search-conversation` |
| Get messages from conversation | ✅ | `conversations_get-messages` |
| Delete message | ❌ | Not exposed |

**What this unlocks for automation:**
- AI can fully operate a CRM inbox — respond, route, escalate
- AI can send multi-channel outreach (cold SMS, follow-up email, WhatsApp)
- AI can schedule nurture touches
- ⚠️ Running bulk SMS campaigns (not 1:1) requires workflows in UI

---

### CALENDARS — READ ONLY ⚠️

| Capability | Available | Tool |
|---|---|---|
| Get calendar events in date range | ✅ | `calendars_get-calendar-events` |
| Get appointment notes | ✅ | `calendars_get-appointment-notes` |
| Create appointment | ❌ | Not exposed |
| Create calendar | ❌ | Not exposed |
| Update availability | ❌ | Not exposed |
| Cancel/reschedule appointment | ❌ | Not exposed |

**What this unlocks for automation:**
- AI can read calendar state for reporting, daily prep, conflict detection
- ⚠️ Booking + calendar setup = HUMAN UI work

---

### OPPORTUNITIES — Read + Update (No Create) ⚠️

| Capability | Available | Tool |
|---|---|---|
| Get single opportunity | ✅ | `opportunities_get-opportunity` |
| Search opportunities | ✅ | `opportunities_search-opportunity` |
| Update opportunity (stage, value, status) | ✅ | `opportunities_update-opportunity` |
| Get pipelines | ✅ | `opportunities_get-pipelines` |
| Create new opportunity | ❌ | Not exposed — significant gap |
| Create pipeline | ❌ | Not exposed |
| Delete opportunity | ❌ | Not exposed |

**What this unlocks for automation:**
- AI can move deals through stages, update values, report on pipelines
- ⚠️ Creating new opportunities from inbound leads = HUMAN or workflow-driven (not direct API)

---

### PAYMENTS — READ ONLY ⚠️

| Capability | Available | Tool |
|---|---|---|
| Get order by ID | ✅ | `payments_get-order-by-id` |
| List transactions | ✅ | `payments_list-transactions` |
| Create product | ❌ | Not exposed |
| Charge customer | ❌ | Not exposed |
| Issue refund | ❌ | Not exposed |
| Create subscription | ❌ | Not exposed |
| Configure checkout | ❌ | Not exposed |

**What this unlocks for automation:**
- AI can pull revenue data for reports and dashboards
- AI can verify order status to trigger downstream actions
- ⚠️ Everything payment-creation is HUMAN UI (Stripe/NMI/Authorize.net configuration + GHL product setup)

---

### SOCIAL MEDIA POSTING — Full CRUD ✅

| Capability | Available | Tool |
|---|---|---|
| Create post (IG, FB, LinkedIn, TikTok, YouTube, Twitter, GBP) | ✅ | `social-media-posting_create-post` |
| Edit scheduled post | ✅ | `social-media-posting_edit-post` |
| Get post details | ✅ | `social-media-posting_get-post` |
| List posts | ✅ | `social-media-posting_get-posts` |
| Get connected social accounts | ✅ | `social-media-posting_get-account` |
| Get social media statistics | ✅ | `social-media-posting_get-social-media-statistics` |
| Delete post | ❌ | Not exposed (may use edit to archive) |

**What this unlocks for automation:**
- AI can fully own social scheduling across all platforms
- AI can adjust scheduled posts before they fire
- AI can pull engagement stats for reporting
- This is the core of our Social Media Poster agent

---

### LOCATIONS (Sub-Accounts) — READ ONLY ⚠️

| Capability | Available | Tool |
|---|---|---|
| Get location details | ✅ | `locations_get-location` |
| Get custom fields list | ✅ | `locations_get-custom-fields` |
| Create new sub-account | ❌ | Not exposed |
| Create custom field | ❌ | Not exposed — significant gap |
| Update location settings | ❌ | Not exposed |

**What this unlocks for automation:**
- AI can discover the existing custom fields in a sub-account before writing to them
- ⚠️ Onboarding a new client's GHL setup = HUMAN UI work

---

## COMPLETELY MISSING FROM GHL API (Not Just Our MCP)

These are GHL platform-level gaps — no public API endpoint exists at all, so even a custom integration would hit a wall:

| Feature | Impact on Automation |
|---|---|
| **Funnels / Landing Pages** | Can't build or modify funnels via API — full UI build |
| **Surveys** (multi-slide, conditional logic) | Event registration, intake flows = UI-only |
| **Forms** (create) | Can only receive webhook data; form-builder = UI |
| **Workflows / Automations** (triggers + actions) | All automation logic = UI build |
| **Products / Catalog** | E-commerce setup = UI |
| **Shopping Cart / Checkout** | Payment UX config = UI |
| **Memberships / Courses / Communities** | Portal + course management = UI |
| **Email Campaigns / Drip Sequences** | Triggered campaign logic = UI (workflow-driven) |
| **Trigger Links** | UI only |
| **Custom Fields** (create) | Schema changes = UI |
| **Users / Team Members** | Access control = UI |
| **Attribution / UTM Tracking** | Setup = UI |
| **Reporting Dashboards** | Dashboard config = UI (can pull raw data to build our own) |

---

## PATTERN: When to Use AI vs. When to Use Human

### AI Does It End-to-End
- Content creation (blogs, captions, emails in template form)
- Social media scheduling
- Contact data hygiene (enrichment, dedupe, tagging)
- 1:1 outreach (SMS, email, DM)
- Reporting (pull data, analyze, format)

### AI Prepares, Human Configures in GHL UI
- Event ticketing systems (surveys, workflows, products)
- Onboarding automations (workflows, drip sequences)
- Portal/Community setup (memberships, channels)
- Checkout funnels (product setup, payment config)
- Custom field schemas (we can design, human creates)

### Human Only (No AI Value-Add)
- Initial GHL sub-account provisioning
- Stripe/NMI/Authorize.net connection
- Domain + DNS setup
- Team member invites + permissions

---

## IMPLICATIONS FOR AGENT DESIGN

**Content Creator Agent:** ✅ Can operate fully inside GHL via blogs + emails + conversations APIs.

**Social Media Poster Agent:** ✅ Can operate fully via social-media-posting APIs (per-client token required).

**Client Onboarding Agent:** ⚠️ Can read existing setup + design the structure, but cannot create the sub-account, custom fields, workflows, or products. Final build is human-executed.

**Campaign Strategist Agent:** ⚠️ Can design the campaign, write copy, prep templates. Actual workflow/drip automation build is human UI work.

**Data Analyst Agent:** ✅ Can pull from payments, contacts, opportunities, social stats, calendars — everything read-side is open.

**Brand Compliance / Content Creator handoff to GHL:** ✅ Once content is AI-approved, AI can push final copy into GHL email templates for scheduling.

---

## WHAT TO BUILD AROUND THIS

To extend GHL automation beyond these limits, the real paths are:

1. **Custom webhook + middleware** — Receive GHL events via webhook → process in Make.com/n8n/custom service → push back via the APIs we have (contact create, tag, send message).
2. **Browser automation (last resort)** — Puppeteer/Playwright scripts clicking through the GHL UI for one-time builds. Brittle. Not recommended unless repeatable + critical.
3. **GHL Marketplace App** — Build a marketplace app that exposes certain workflows to API; massive lift, only makes sense if we're productizing for dozens of clients.

For now: **accept the "AI designs, human builds" split and optimize handoff quality.** The scalable move is to make AI's design output so tight that a human's UI build time drops from hours to minutes.

---

## RELATED NOTES

- [[GHL Event Ticketing — Multi-Attendee Capture Architecture 2026-04-20]] — where we first hit these limits
- [[CUSS — Events System Architecture 2026-04-20]] — the CUSS-specific build
- [[feedback_ghl_token_architecture]] — per-client token model
- [[GHL Automation Setup]] — internal skill doc

---

*Source: Direct audit of mcp__gohighlevel-launchpad__* and mcp__gohighlevel-agency__* tool schemas as of 2026-04-20.*
