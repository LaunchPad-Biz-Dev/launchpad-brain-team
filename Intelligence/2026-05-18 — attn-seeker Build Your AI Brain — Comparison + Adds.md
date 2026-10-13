---
title: "attn:seeker Build Your AI Brain — Comparison + Adds"
type: intelligence
status: active
tier: secondary
tags: [ai-systems, brain, n8n, webinar, stanley-chen]
last_updated: 2026-05-18
related: ["[[index]]", "[[CLAUDE]]", "[[Intelligence/00-INDEX]]"]
source: "Stanley Chen / attn:seeker webinar 2026-05-14 — recording: https://youtu.be/pQ1V2nunf0Y"
download_pack: "~/Downloads/build-your-ai-brain-v2/"
---

# attn:seeker AI Brain — Comparison + Adds

**Goal of this note:** keep what we have, add only what closes real gaps, get to implementation faster. NOT a rebuild.

---

## Their model (in 3 lines)

- **Layer 1: Context** — markdown files about the business (company, services, team, tone, clients, audience) with YAML frontmatter
- **Layer 2: Skills** — one file per repeatable task (proposal-writer, meeting-prep, email-drafter). Format: What it does / Context files it reads / Inputs / Steps / Output / Rules
- **Layer 3: Automation** — n8n workflows + scheduled tasks that trigger skills without a human

**Their 5 Levels of AI:** Search engine → Prompt engineer → Brain (context) → Body (skills) → Autonomy. Stanley says most people live at L2; Launchpad is solidly at L3-L4 already.

---

## Stanley's stack (theirs)

| Tool | Purpose |
|---|---|
| Claude Code (terminal + app) | LLM brain |
| Cursor + VS Code | Editor |
| **n8n** | Automation engine — 20+ live workflows |
| **graphify** (Python) | Builds a knowledge graph map from the brain folder |
| **Obsidian** | Visualize the graph + edit notes |
| **Ollama** | Local models for classification/routing + sensitive data |
| **Qdrant** | Vector DB for semantic search |
| Fireflies | Transcripts |
| Stripe webhooks → n8n | Sales triggers |
| Git → Vercel | Version control + deploy of their "Attention OS" dashboard |
| Microsoft 365 | Email/calendar/teams |
| Attio | CRM |

---

## Our stack (ours, today)

| Tool | Purpose |
|---|---|
| Claude Code (Opus 4.7) | LLM brain |
| Obsidian | Brain visualization + editing |
| **9 specialized agents** | content, design, strategy, research, data, video, compliance, social poster, client-onboarding (+ sales agents) |
| **Brain Query skill** | LLM-routed retrieval (reads index first, narrows to MOCs, returns cited synthesis) |
| **Templates** | agent-template.md + skill-template.md required for new builds |
| MCP servers | GHL (3 sub-accounts), Slack, Notion, Google Drive, Canva, Apify, Nano Banana |
| Schedule skill (cron) | Time-based automation |
| **No n8n** | Gap |
| **No graphify** | Gap |
| **No git on Brain** | Gap (confirmed today) |
| **No local model / vector DB** | Not urgent |

---

## Direct comparison

| Area | attn:seeker | Launchpad | Verdict |
|---|---|---|---|
| 3-layer mental model | Explicit (Context/Skills/Automation) | Implicit — we have it, we don't label it | **ADOPT the language** in CLAUDE.md so the team has a shared mental model |
| Brain location | Local folder + Obsidian | Local folder + Obsidian (246 files) | Tied |
| YAML frontmatter | doc_type, owner, tier | title, type, status, last_updated, tags, related | We have it. **Add `tier` (primary/secondary) so brain-query can prioritize** |
| Knowledge map | graphify (deterministic Python tool) | brain-query skill (LLM-based) | Different approaches. Brain-query is smarter; graphify is faster + free. **Add graphify as a complement, not a replacement** |
| Skill format | Lean 6-section template | Heavier with Brain Integration block | Ours is more thorough. Theirs is more usable. **Keep ours, but borrow the leanness for net-new skills** |
| Automation engine | n8n (20+ workflows) | Cron via Schedule skill + Claude reasoning loops | **Big gap. Add n8n for deterministic plumbing — keep Claude for judgment** |
| Brain version control | Git → snapshots → rollback | **None** | **ADD: `git init` the Brain, weekly snapshot, audit trail** |
| Local models | Ollama for classification/routing | None | Future, not urgent |
| Vector DB | Qdrant | None | Future, not urgent |
| Custom dashboards | "Attention OS" — Next.js/Vercel | Mission Control (Phase A done, Phase B pending) | We're catching up — same direction |
| Multi-workspace | 4 subworkspaces (agency, OS, brand, web) | One consolidated Brain | Different — ours is fine |
| Compliance gate | None visible | **Brand Compliance Agent** as final gate | **We win here. Keep.** |
| Specialized agents | Few personas (Kevin, Kim, Connor) | 9 specialized agents | **We win here. Keep.** |
| Client granularity | Single client-roster.md | Per-client `Projects/{Client}.md` notes | **We win here. Keep.** |

---

## What we already do BETTER than them — keep, do not change

1. **Brand Compliance Agent** as a final gate on all output
2. **9 specialized agents** instead of one big assistant with personas
3. **Per-client Project notes** (`Brain/Projects/{Client}.md`) — way more granular than their single client-roster.md
4. **Brain Query skill** — smarter retrieval than a static graph
5. **Templates for both agents AND skills** — they only template skills
6. **Apollo Slack identity + channel routing rules** — more developed comms layer
7. **Intelligence folder** for cross-client research synthesis
8. **MCP-first architecture** — direct tool integration vs everything going through n8n

---

## What's worth ADDING (priority-ordered)

### Tier 1 — Do this week (cheap, high leverage)

1. **`git init` the Brain + commit** — 5 minutes. Adds rollback. Stanley's #1 safeguard.
   - Set up weekly auto-commit via cron
2. **Adopt the 3-layer language in CLAUDE.md** — Frame Context = Brain, Skills = `.claude/skills/` + agents, Automation = cron + (soon) n8n. Gives the team shared vocabulary.
3. **Extend frontmatter to include `tier: primary | secondary`** on Brain files — lets brain-query rank results. ~30 min script + manual review of top files.

### Tier 2 — Do in next 2 weeks (real lift, real ROI)

4. **n8n as the orchestration layer** — Already on our radar. The webinar confirmed it's the right call. Hybrid pattern: n8n handles deterministic plumbing, calls Claude only for the reasoning step. Targets:
   - CRM hygiene daily sweep
   - IG cold prospecting daily 20
   - Growth Audit landing → CRM → Slack ping
   - Notion → Brain sync
5. **Install graphify on the Brain** — `pip install graphifyy && python3 -m graphify .` → adds knowledge-graph map alongside brain-query. Costs nothing.
6. **Token-efficiency pass** — Stanley claimed 466× reduction by routing via map vs whole-folder reads. Run brain-lint, audit index.md routing, ensure agents call brain-query instead of grep-crawling.

### Tier 3 — Future (don't do yet)

7. **Local model (Ollama) for sensitive data** — relevant if we onboard a finance/healthcare client with strict privacy
8. **Vector DB (Qdrant)** — only valuable once Brain hits ~1000+ files (we're at 246)

---

## What NOT to do

- ❌ Do not restart or copy their folder structure on top of ours — our `Projects/Context/Intelligence/Daily/Anthony/Departments/Teams/...` is more mature than their 6-file Layer 1
- ❌ Do not flatten our 9 agents into one persona-driven assistant
- ❌ Do not drop the Brand Compliance gate
- ❌ Do not run automations through Claude when n8n + API call would do the same thing for free

---

## Key Stanley quotes worth remembering

- *"Every business runs on conversations and content. AI handles the 70% admin in between."*
- *"The brain needs to know everything to do everything. If there are limits, scope the context accordingly."*
- *"Most AI failure isn't AI capability — it's unclear problem definition."*
- *"Token usage is always cheaper than human time. But a good system map cuts token usage 466×."*
- *"Define what privacy and security mean for YOUR business first. Then design around it."*

---

## Open questions for the build

- Should we run n8n self-hosted (free, more setup) or n8n Cloud ($20/mo, faster start)?
- When we git-version the Brain, do we want a private GitHub repo or just local git?
- Do we want to keep brain-query as the primary retrieval and use graphify only for visualization, or use both depending on the query?
