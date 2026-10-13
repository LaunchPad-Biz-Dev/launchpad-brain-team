---
title: "Brain Standards — The Rulebook"
type: infrastructure
status: active
tier: primary
tags: [system, standard, governance, master-rules]
last_updated: 2026-05-18
related: ["[[index]]", "[[CLAUDE]]", "[[Frontmatter Spec]]", "[[Core Framework]]", "[[Context/00-INDEX]]"]
sources: ["Stanley Chen (attn:seeker) — Build Your AI Brain webinar 2026-05-14", "Andrej Karpathy — AI-Driven Second Brain (techstrong.ai)", "Andrej Karpathy LLM Wiki via Nick Spisak (aimaker.substack.com)"]
---

# Brain Standards — The Rulebook

**The single source of truth for how the LaunchPad Brain is built, maintained, and grown.**
Adopted 2026-05-18. Synthesizes Stanley Chen's attn:seeker AI Brain framework, Andrej Karpathy's second-brain methodology, and our existing Launchpad architecture.

Every agent reads this before creating, editing, or filing a Brain note. Every human follows it when adding context. If a rule conflicts with how an agent or person wants to act, **this doc wins**.

---

## 1. Mental Model — The Two Frames

### Frame A: 3-Layer System (Stanley)
| Layer | What | Where |
|---|---|---|
| **Layer 1 — Context** | Knowledge (the Brain) | `~/launchpad-brain/LaunchPad Brain/` |
| **Layer 2 — Skills** | Procedures (agents + skills) | `~/launchpad-automation/.claude/` |
| **Layer 3 — Automation** | Triggers (cron + n8n + webhooks) | `~/launchpad-automation/scripts/` + n8n Cloud |

### Frame B: 3-Zone Knowledge Flow (Karpathy)
Every piece of information in the Brain lives in one of three zones — and **knowing which zone a note belongs to determines what an agent is allowed to do with it.**

| Zone | Purpose | Folders | Mutability |
|---|---|---|---|
| **🟥 Sources (immutable)** | Raw captured material — transcripts, articles, meeting notes, scraped data | `Raw/`, `Daily/` (the daily-log entries themselves), `Resources/` | **NEVER edit**. Append-only. Source of all downstream work. |
| **🟦 Curated (human-owned)** | Decisions, context, playbooks, brand voice, client specifics | `Projects/`, `Context/`, `Teams/`, `Departments/`, `Anthony/`, `Onboarding/`, `Sales Playbook.md` | Humans edit. Agents propose changes via Slack, never auto-edit. |
| **🟪 Synthesis (LLM-owned)** | Derived knowledge — research, trend briefs, query results, cross-note synthesis | `Intelligence/`, `Skills/` (skill specs), `_archive/` | Agents can write here freely. Humans review, promote good synthesis to Curated when it stabilizes. |

**Why this matters:** an agent must check the zone before deciding whether it can edit a note. Modifying a Source = data loss. Modifying a Curated note silently = trust loss. Modifying a Synthesis note = expected and good.

---

## 2. Folder Structure & Where Things Go

```
LaunchPad Brain/
├── CLAUDE.md            (Brain navigation guide for AI — read on every session)
├── index.md             (master MOC — primary entry point)
├── log.md               (chronological event log — append-only)
├── Sales Playbook.md    (canonical sales process — Curated)
│
├── Anthony/             🟦 Curated — Personal brand + strategic vision
├── Context/             🟦 Curated — Core framework, brand guidelines, specs
├── Departments/         🟦 Curated — Departmental playbooks
├── Onboarding/          🟦 Curated — Client onboarding process
├── Projects/            🟦 Curated — Active client context (one note per client)
├── Sales Playbook.md    🟦 Curated — Sales process
├── Teams/               🟦 Curated — Team member context
│
├── Daily/               🟥 Sources — Dated daily logs (append-only)
├── Raw/                 🟥 Sources — Unprocessed captures (transcripts, scrapes)
├── Resources/           🟥 Sources — Reference material, lookups
├── Strategic Partners/  🟥 Sources — Partner reference data
│
├── Intelligence/        🟪 Synthesis — Research, trend briefs, query results
├── Skills/              🟪 Synthesis — Skill specs, workflow docs
├── Tasks/               🟪 Synthesis — Transient task plans
│
└── _archive/            🟪 Synthesis (graveyard) — Historical, kept for reference
```

### Decision tree — where does this note go?

1. **Is it raw captured material?** → Sources zone (Raw/Daily/Resources)
2. **Does a human own its truth?** (a client, a brand decision, a process) → Curated zone (Projects/Context/Teams/etc.)
3. **Is it derived from other notes?** (research, synthesis, AI output) → Synthesis zone (Intelligence/Skills/Tasks)
4. **Unsure?** → `Intelligence/` (default for ambiguous synthesis)

---

## 3. Frontmatter Standard

Every note must start with valid YAML frontmatter. Spec: [[Frontmatter Spec]].

```yaml
---
title: "Note Title in Quotes"
type: project | context | intelligence | infrastructure | daily | reference | skill | team | playbook | raw | archive
status: active | archived | draft
tier: primary | secondary
tags: [tag1, tag2]
last_updated: YYYY-MM-DD
related: ["[[Note A]]", "[[Note B]]"]
---
```

**`zone` field (optional but recommended for new notes):** `sources | curated | synthesis` — explicit zone declaration so agents don't have to infer from folder.

**`source` field for Synthesis notes:** When a Synthesis note is derived from a Source, link the source: `source: "[[Raw/Webinar Transcript 2026-05-14]]"`.

---

## 4. Linking Rules — The Most Important Part

A Brain without dense links is a pile of files. **Every note should link to at least 2 others.** Both Stanley and Karpathy emphasized this: the value of the Brain comes from the connections, not the files.

### Three linking mechanisms — use all three

| Mechanism | When | How |
|---|---|---|
| **`related:` frontmatter** | Static, structural links — "this note IS related to those notes" | List 2-5 `[[Note Name]]` entries. Never leave `related: []` empty unless the note is intentionally orphaned. |
| **Inline `[[wikilinks]]`** | Contextual mentions inside the body — "as discussed in [[Note X]]" | Drop them naturally as you write. Don't force them, but never miss an opportunity. |
| **Folder MOC backlink** | "This note belongs to this folder's map" | Every note's folder `00-INDEX.md` should list it. The MOC is the spine of the folder. |

### Rule: No orphans

A note with `0 inbound + 0 outbound links` is an orphan. Orphans are invisible to brain-query and graphify. **Every note must either be linked, archived, or deleted.** Run brain-lint to find them.

### Rule: Backlink before file-back

When a Synthesis note (e.g. an Intelligence/ brief) is created from Sources, add a `[[Synthesis Note]]` link inside the relevant Source notes. This creates the bidirectional path Karpathy emphasizes — sources point at the synthesis they fed into.

---

## 5. MOCs (Maps of Content)

Every folder has a `00-INDEX.md` that serves as the folder's hub note. It must:

1. Have `type: moc` in frontmatter
2. Have `tier: primary` (always primary)
3. Link to every active note in the folder (Synthesis MOCs can omit archived items)
4. Group links by sub-category if the folder has >30 entries
5. Be kept current — when a note is added/renamed/archived, update the MOC

**The brain-lint skill checks for MOC drift.** Run it weekly.

`index.md` at the Brain root is the master MOC — it links to every folder MOC.

---

## 6. Note Atomicity — How Big Should a Note Be?

**Default: atomic.** One concept per note, one decision per note, one client per note.

- ✅ `[[Animus Xthlete]]` — one client, one note
- ✅ `[[Trend Brief — 2026-05-14]]` — one day's trends
- ✅ `[[GHL Token Architecture]]` — one technical decision

**Exceptions where bigger is fine:**
- Daily logs (one note per day, contains many small entries)
- Comprehensive playbooks (Sales Playbook.md, Core Framework.md)
- Reference docs that are useful read end-to-end (Frontmatter Spec.md, this doc)

**Hard limit: if a note tops 800 lines, consider splitting.** The longer a note gets, the more tokens it costs to load.

---

## 7. Ingestion Workflow — How New Content Gets In

Karpathy's pattern, adapted for us:

```
External event → Source zone (Raw/ or Daily/) → Brain Ingest skill → Synthesis (Intelligence/) → Curated promotion (manual, when stable)
```

| Source | Where it lands first | Who processes it |
|---|---|---|
| Meeting transcript (Fireflies) | `Raw/transcripts/YYYY-MM-DD — meeting-name.md` | `brain-ingest` skill extracts action items + files into `Intelligence/` |
| Article / web research | `Raw/articles/YYYY-MM-DD — title.md` | `brain-ingest` summarizes + links into Intelligence/ |
| Daily log entry | `Daily/YYYY-MM-DD.md` (append) | `brain-dump` skill at end of day |
| Slack capture (`chat clip that`) | Append to relevant existing note OR new note in correct zone | Apollo (real-time) |
| Slack DM to Apollo | `Raw/inbox/YYYY-MM-DD HH:MM — sender.md` | `brain-ingest` classifies + files |
| Notion sync | Mapped to existing folder by content | `notion-brain-sync` skill (cron, 2x daily) |
| Client onboarding | `Projects/{Client}.md` (new) + linked into `Projects/00-INDEX.md` | `client-onboarding` agent |

**Rule for Sources:** never edited after capture. If correction is needed, add a dated update note below, link from the original.

---

## 8. AI Interaction Rules — What Agents Can and Can't Do

| Action | Sources 🟥 | Curated 🟦 | Synthesis 🟪 |
|---|---|---|---|
| Read | ✅ Always | ✅ Always | ✅ Always |
| Write new note | ❌ Only via brain-ingest with explicit source attribution | ❌ Only via authorized agent (client-onboarding, etc.) with human approval | ✅ Freely |
| Edit existing note | ❌ Never | ⚠️ Only with explicit human approval; otherwise propose change via Slack | ✅ Freely |
| Delete note | ❌ Never | ❌ Never without explicit human approval | ⚠️ Only if note is stale + no backlinks |
| Add `[[wikilinks]]` to existing note | ⚠️ Append a backlinks section only | ✅ When obvious connection | ✅ Freely |
| Update `related:` frontmatter | ⚠️ Append only | ✅ When new connection found | ✅ Freely |
| Add to MOC (`00-INDEX.md`) | n/a | ✅ When new note added to folder | ✅ When new note added to folder |
| Run `brain-lint` | ✅ Always | ✅ Always | ✅ Always |

**The Brain Compliance rule:** Before ANY edit to a Curated zone note, an agent must:
1. Check the file's `tier:` (primary = extra caution)
2. Identify the zone
3. If zone = Curated and edit is non-trivial → propose in Slack, don't auto-apply
4. If zone = Synthesis → proceed but log in `log.md`

---

## 9. Maintenance — What Keeps the Brain Healthy

### Automatic
- **Weekly git snapshot** — Mondays 7 AM via `scripts/brain-snapshot.sh`
- **Notion → Brain sync** — 2x daily via `notion-brain-sync` skill

### On-demand (run as needed)
- **`brain-map.py`** — regenerates the folder/tier/orphan summary. Run after bulk edits.
- **`brain-graphify-update.sh`** — rebuilds the graphify knowledge graph. Run after meaningful additions.

### Weekly review (Anthony, 15 min Sundays)
- Check `_brain-map.md` for: new orphans, missing-fm count, folder skew
- Run `brain-lint` skill via Claude → review proposed fixes
- Promote any Synthesis notes that have stabilized into Curated

### Quarterly audit
- Re-run the Stanley-comparison pass: are we still on standards? Has anything drifted?
- Archive stale Synthesis notes (>6 months old, no inbound links)

---

## 10. Graph View — Visual Standards

Obsidian Graph View should be configured with color groups for instant visual diagnosis:

| Color | Group | Path filter |
|---|---|---|
| 🟧 Orange | Projects (active clients) | `path:Projects/` |
| 🟦 Blue | Context (foundational) | `path:Context/` |
| 🟪 Purple | Intelligence (synthesis) | `path:Intelligence/` |
| 🟩 Green | Daily (recent activity) | `path:Daily/` |
| 🟨 Yellow | Skills (operations) | `path:Skills/` |
| 🩷 Pink | Teams (humans) | `path:Teams/` OR `path:Departments/` OR `path:Strategic Partners/` |
| 🟥 Red | Anthony (founder) | `path:Anthony/` |
| ⬜ Grey | Archive | `path:_archive/` |

Settings → Graph view → Groups → add each rule. Config persists in `.obsidian/graph.json` (auto-saved).

---

## 11. The 5 Brain Skills — When to Use Each

| Skill | Use when |
|---|---|
| **`brain-query`** | Asking the Brain a question — synthesis, lookup, comparison |
| **`brain-ingest`** | Bringing new raw material in (transcript, article, capture) |
| **`brain-compile`** | Generating a synthesized report from multiple notes |
| **`brain-lint`** | Health check — orphans, missing frontmatter, stale MOCs, broken links |
| **`brain-dump`** | End-of-day knowledge capture into Brain |
| **`notion-brain-sync`** | Pulling Notion updates into the Brain |
| **`/graphify query`** | Fast graph traversal across nodes — "what links X to Y" |

**Rule:** Agents must use one of these skills, NEVER grep-crawl the vault.

---

## 12. The Big-Picture Rules

1. **Sources are immutable.** Append updates, never overwrite.
2. **Every note links to at least 2 others.** No orphans.
3. **Agents read freely, edit cautiously.** Zone determines edit rights.
4. **MOCs are the spine.** Every folder has one; keep it current.
5. **Atomic notes by default.** One concept = one note.
6. **Token efficiency is non-negotiable.** Use brain-query and /graphify, never grep.
7. **The Brain compounds.** Every query is a chance to file new synthesis.
8. **When in doubt, default to Intelligence/** with `tier: secondary` — promote later.
9. **Standards are version-controlled.** This doc is the source of truth. Update it when standards change; never let drift happen silently.

---

## Changelog

- **2026-05-18** — Initial version. Combines Stanley Chen attn:seeker webinar framework + Andrej Karpathy second-brain methodology + existing LaunchPad Brain build. Author: Anthony + Claude (Apollo session).
