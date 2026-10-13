---
title: "Callsheet Generation"
type: skill
status: active
tier: primary
tags: [production, shotlist, callsheet, apollo]
last_updated: 2026-08-12
related: ["[[Skills/00-INDEX]]", "[[Skills/Shot List Creation]]", "[[Callsheet System]]"]
---

# Callsheet Generation

## Purpose
Turn a vague shoot request into a field-usable callsheet: an interactive, offline HTML page the
shooter works live on the floor and the client can read as a deliverable.

**Triggers:** "shot list for", "callsheet", "shoot brief", "brief for the [X] shoot",
"what are we shooting", a Notion production task assigned to Apollo.

**Requested by:** Anthony, Kyle, Cynthia, Abril, or Robert.

This skill produces the document. [[Shot List Creation]] holds the underlying shot-type
vocabulary — talking heads, B-roll, POV, skits, drone — and is the reference for *what kinds of
shots exist*. This skill is *how we ship the brief*.

---

## Step 1 — Establish the facts before writing anything

Do not draft from the request alone. Requests arrive vague ("pics for social, drinks, employees")
and the value is in what gets pinned down.

**Always verify externally:**
- **Event timing.** If the shoot attaches to a game, opening, concert or match — search for the
  actual date and start time. Do not trust the brief. On the TBC Allegiant shoot the crew window
  was 3–6pm and gates opened at 3:00pm, which meant zero clean-plate time. That single fact
  reshaped the whole document and it was not in the request.
- **Venue.** Indoor or outdoor, domed or open, what the light will actually be.
- **Sunset / golden hour** if any exterior is wanted.

**Always ask the requester (or state as an assumption if they're unreachable):**
1. Who is shooting, and is there a second body?
2. Exact call time and wrap time.
3. Any hard exclusions? (TBC was "no food" — that kind of constraint reframes entire blocks.)
4. What are the deliverables and when are first selects due?
5. Any talent, staff, or products that must appear?

**Always read from the brain before drafting:**
- `Projects/{Client}.md` — brand guidelines, contacts, package, team roster
- `Intelligence/Design Intelligence — {Client}.md` if it exists — the approved visual system,
  grade, typography, text ratio, caption style
- Prior callsheets for the same client

Never invent brand specifics. If the approved grade or feed format isn't recorded, ask.

---

## Step 2 — Pick the template

From [[Callsheet System]] in `Resources/Callsheet System/`:

- `callsheet-photo.template.html` — stills. Coverage matrix, clean vs populated, ratio passes.
- `callsheet-video.template.html` — motion. Sequences, movement/lens/duration/audio per row,
  audio plan.

Shoot is both? Build both and run them as separate lists. Do not merge — the photographer and
videographer work at different tempos and a merged list slows both down.

---

## Step 3 — Fill it

Replace every `{{TOKEN}}`. Add or delete shot rows freely; the block skeleton is a starting point,
not a fixed form. Keep each shot row **specific enough to execute without asking a question** —
"Wide, left 45°, concourse as a leading line" beats "wide shot of the store."

**Rules that make a callsheet good rather than long:**

1. **Every shot maps to a deliverable.** If you can't name where a frame lands, cut the row.
2. **Priority stack is real.** Rank the blocks. Shoots lose time and someone has to decide what
   gets dropped — decide it in advance, not at 5pm.
3. **Run of show is timed against reality.** Anchor it to the event clock, not to round numbers.
   Mark the peak-energy window with `class="peak"`.
4. **Hero shots get shot ten ways.** Say so explicitly on the one frame that carries the campaign.
5. **Name what not to shoot.** Exclusions prevent more bad frames than instructions produce good
   ones.
6. **Leave negative space.** If design places text in the photo, the brief must tell the shooter to
   compose empty dark zones. Otherwise every frame comes back unusable for graphics.
7. **Flag gaps honestly.** If the reference board can't support a required ratio or subject, say so
   in the internal version.

---

## Step 4 — Reference images

Embed them. Never ship a callsheet that depends on links — the shooter is standing in a venue with
no signal, and a Pinterest link is useless there.

```bash
# downscale
sips -s format jpeg -s formatOptions 62 -Z 460 raw.jpg --out images/R1.jpg
```

Then caption each one with **what it actually is**, not what the sender labelled it. Open every
image and look at it. On the TBC shoot the client's three groups were mislabelled — the "at the
cantina" set was actually guest-energy QSR nightlife, and the single most useful frame in the whole
board was buried in the group labelled "food in the stadium."

Each reference gets: a code, a one-line description of the actual content, and the shot codes it
maps to.

---

## Step 5 — Build and route

```bash
python3 build-callsheet.py filled.html images/ "Client — Callsheet YYYY-MM-DD.html"
```

**Two versions, always:**

| Version | Contains | Goes to |
|---|---|---|
| **Internal** | Everything — production gaps, release fallbacks, access problems, blunt notes | Anthony, crew |
| **Client-ready** | Same shot list, internal commentary stripped | Client, and anyone in the room with them |

**Stripping for client-ready** means removing anything written *about* the client rather than *to*
them. Specifically: "their explicit ask", "client-specified", "the client wants", critiques of the
reference board, release-friction workarounds, and build/meta notes about the page itself. Keep the
substance, change the voice. The clearances section stays — it reads as internal but it is the ask
list *for* the client and it's the section that gets the crew what they need on the day.

**Format by recipient:**

- **Anthony** — HTML file plus a published Artifact. He wants the interactive checklist and a link.
- **Kyle · Cynthia** — Notion page or PDF. Convert the filled content to Notion blocks via the
  Notion MCP (`notion-create-pages`), or print the HTML to PDF in light mode. They live in Notion;
  don't hand them a raw HTML file.
- **Client** — the client-ready HTML file, emailed or dropped in Drive. Opens anywhere, no account,
  works offline.

**Save every finished callsheet** to `Projects/{Client}/` in the brain as markdown alongside the
HTML, with the internal notes intact. That markdown is the record; the HTML is the instrument.

---

## Step 6 — After the shoot

- Archive the checked-off callsheet with the footage.
- Note which shots were missed and why — that feeds the next brief for the same client.
- If a new pattern worked, add it to the template rather than only to that one document.

---

## Quality bar

A callsheet is done when a shooter who wasn't in any planning conversation could execute the whole
day from it without asking a question. If any row would prompt "what do you mean by that", it isn't
finished.

---

## Related Notes
- [[Shot List Creation]] — shot-type vocabulary and category templates
- [[Callsheet System]] — the templates, build script, and worked example
- [[Brief Creation]] — the creative brief that informs the shot list
- [[Video Production SOP]] — general production process
- [[Content Workflow — Shoot to Post]] — how shot lists feed editing
- [[Client Delivery Portal]] — where this system is heading
