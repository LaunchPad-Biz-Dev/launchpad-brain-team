---
title: "Client Shared Drive Registry"
type: context
status: active
tier: primary
tags: [drive, registry, automation-input, multi-client]
last_updated: 2026-05-19
related: ["[[Social Media Production Workflow]]", "[[n8n Workflow Roadmap]]", "[[Context/00-INDEX]]"]
---

# Client Shared Drive Registry

**The canonical list of every Launchpad-controlled Google Shared Drive — exact name + Drive ID.** Apollo + n8n workflows use this to find client content reliably.

**Use Drive IDs over names whenever possible** — IDs are stable and unique; names can be renamed without warning.

Pulled directly from Google Drive API on 2026-05-19.

---

## Client Shared Drives (active client work)

| Client | Exact Drive Name | Drive ID | Notes |
|---|---|---|---|
| 365 Plumbing of Nevada | `365 Plumbing of Nevada` | `0AM_YLY5g_C3_Uk9PVA` | |
| Absolute Stone | `Absolute Stone` | `0AG7RnHScZcsvUk9PVA` | |
| Afshar Law | `Afshar Law` | `0AFjF9VYBVyJ0Uk9PVA` | |
| Blue Mountain Energy HVAC | `Blue Mountain Energy HVAC ` | `0AE2UZnGKLh35Uk9PVA` | ⚠️ trailing space in name |
| Brand With Us (BWU) | `Brand With Us` | `0AB2J2LiKnsLHUk9PVA` | |
| **Continental Currency Services (CCS)** | `Continental Currency Services (CCS)` | `0AICReBRzBtPqUk9PVA` | ✅ Pilot client for n8n SMM Workflow 01 |
| Dejando Huellas de Amor | `Dejando Huellas de Amor` | `0ANZ4SPUA-WDDUk9PVA` | |
| Diversified Restaurant Group (Arby's / Taco Bell) | `Diversified Restaurant Group` | `0AHfLX5j_HM-RUk9PVA` | Likely houses Arby's + Taco Bell Cantinas content |
| Durango HVAC | `Durango HVAC` | `0ACi2WyPOrwN4Uk9PVA` | |
| Matsuda Nadig Law | `Matsuda Nadig Law` | `0ALT1UL01Ni4aUk9PVA` | |
| Matsuda Nadig Van Law | `Matsuda Nadig Van Law` | `0ACYzRxEMk1MaUk9PVA` | |
| Muller Masks | `Muller Masks` | `0AC_ofrOef3iMUk9PVA` | |
| NHCA | `NHCA` | `0AGYmSiL2ZzwZUk9PVA` | |
| Nulook | `Nulook` | `0ABs0lnnQtfhmUk9PVA` | |
| Sobel Westex | `Sobel Westex` | `0ADM8JlctGDzpUk9PVA` | Ad-only client per [[Contracted Monthly Deliverables]] |
| Toro Taxes Franchise Sales | `Toro Taxes Franchise Sales` | `0AIeIZQbJf0VgUk9PVA` | |
| Turfit | `Turfit` | `0AKIYvyyYPSsIUk9PVA` | |
| Upbeat Health | `Upbeat Health` | `0AJuwTe0XrDxsUk9PVA` | |
| Wamen Garage Doors | `Wamen Garage Doors` | `0AHH_RAbVyAzBUk9PVA` | ⚠️ Do-not-cite per memory — but drive still operational |
| Welding School of Nevada | `Welding School of Nevada` | `0ACAh6RJzEPPkUk9PVA` | |

---

## Internal / Launchpad Drives (not client-facing)

| Drive | Exact Name | Drive ID | Purpose |
|---|---|---|---|
| LaunchPad (Agency) | `LaunchPad` | `0ACS-IMXQ_490Uk9PVA` | Agency root drive |
| LaunchPad Productions | `LaunchPad Productions` | `0AJvMJxKCCLYtUk9PVA` | Video production entity |
| LaunchPad University | `LaunchPad University` | `0AMQc2sCAYcyOUk9PVA` | LPU course content |
| LaunchPad Podcasts | `Launchpad Podcasts` | `0AKYt1oe0auiuUk9PVA` | Podcast assets |
| LaunchPad Video Editor Assessments | `LaunchPad  Video Editor Assessments ` | `0AG8MVnkQ3kF7Uk9PVA` | ⚠️ double + trailing space |
| Editing Assets | `Editing Assets` | `0APj9Y2b7vsqBUk9PVA` | Shared editing resources |
| Promo Work | `Promo Work` | `0AKYbvlDtu5hUUk9PVA` | Promotional projects |
| **Apollo** | `Apollo` | `0ADC0dpa5kvoFUk9PVA` | ✅ Apollo's own drive — for outputs |

---

## Clients with Brain notes but no shared drive yet

These appear in the Notion client list / Deliverable Tracker but don't have a corresponding shared drive (or their drive name differs from the client name and needs mapping):

- Animus Xthlete
- Arby's Food Truck — may be under Diversified Restaurant Group
- Taco Bell Cantinas — may be under Diversified Restaurant Group
- Toro Taxes (vs Toro Taxes Franchise Sales) — confirm which is the active client
- LaunchPad Business Development — uses agency `LaunchPad` drive?
- KTG / Move to Freedom
- HombreX
- Vegas Medical Inc
- CarZone
- MH Collisions

**Action: Anthony to confirm drive→client mapping for each ambiguous case above.**

---

## How n8n workflows use this

Workflows reference Drive IDs (not names) in the `CLIENT_GHL_REGISTRY` JS object inside `n8n-workflows/SMM-01-apollo-content-pipeline.json`.

**Pattern in the workflow registry:**
```javascript
'CLIENT NAME (UPPERCASE)': {
  locationId: 'ghl-location-id',
  tokenEnvVar: 'GHL_TOKEN_NAME',
  driveSearchName: 'Exact Drive Name From This Doc',
  driveId: 'Drive_ID_From_This_Doc',   // preferred over search
  platforms: ['facebook', 'instagram']
}
```

Apollo navigates to `driveId` directly → no search needed → guaranteed match.

---

## Rule before onboarding a new client to n8n

1. ✅ Confirm exact drive name + ID is in this registry
2. ✅ Confirm Apollo (`apollo@launchpadbizdev.com`) has Content manager access to the shared drive
3. ✅ Confirm the drive has the standard folder structure (`GRAPHICS/{Month YY'}/APPROVED/` + `VIDEOS/{Month YY'}/APPROVED/`)
4. ✅ Add the client to the workflow's `CLIENT_GHL_REGISTRY` with their `driveId`

If any step is incomplete → workflow fails silently → DO NOT activate.

---

## Changelog

- **2026-05-19** — Pulled all 28 shared drive names + IDs from Google Drive API. Added Drive IDs as canonical references (more stable than names). Flagged ambiguous client→drive mappings.
- **2026-05-19** — Initial doc created during SMM Workflow 01 CCS pilot (found that "Continental Currency Services" alone doesn't match — actual name is "Continental Currency Services (CCS)").
