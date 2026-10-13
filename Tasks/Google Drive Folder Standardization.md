---
title: Google Drive Folder Standardization
type: task
status: needs-decision
tier: secondary
created: 2026-04-21
owner: Anthony (decision) → Emigen (execution) OR Client Onboarding Agent (automation)
priority: high — prerequisite for Creative Designer + Video Production agents
related: ["[[Tasks/00-INDEX]]"]
---

# Google Drive Folder Standardization

## What
Lock in a single, consistent Google Drive subfolder structure that every client's shared drive will use. Then either (a) have Emigen audit existing clients and create missing folders, or (b) build the auto-create step into the Client Onboarding Agent first.

## Why
For the AI marketing team to function, agents need to know **where to find brand assets and approved examples** and **where to save generated content**. Today, each client's drive has a shared folder but internal organization varies. Without standardization:
- Creative Designer agent can't reliably pull logos, fonts, mood boards
- Video Production agent can't reliably pull raw footage or reference clips
- No consistent home for "approved examples" that agents should mimic
- Every client requires custom path-mapping = doesn't scale

This is a **prerequisite for Creative Designer and Video Production agents** to ship.

## Proposed Standard Structure (per client)
1. **Brand Assets** — logos, brand guides, fonts
2. **Graphics** — design files, social media graphics
3. **Videos** — raw footage, edited videos, clips
4. **Photos** — raw photos, edited photos
5. **Mood Boards & Style Library** — mood boards, visual references, inspiration
6. **Approved Examples** — top-performing content, client-approved samples
7. **Login Credentials** — stored securely (consider whether this belongs in Drive or in a password manager; flag for Anthony)

## Decisions Needed from Anthony
1. **Does the 7-folder structure above work, or adjust?** (e.g., split Videos into Raw/Edited/Clips sub-subfolders? Separate "Templates"? Should Login Credentials even live in Drive?)
2. **Rollout path — pick one:**
   - **Option A:** Emigen manually audits all 18 active clients, creates missing folders this week. Fast, but manual.
   - **Option B:** Build auto-create logic into Client Onboarding Agent first, then backfill existing clients via the agent. Slower start, scales to every new client automatically.
   - **Option C:** Both — Emigen handles existing 18 now, agent handles every future client.
3. **Who owns the audit checklist** once structure is locked?

## Blockers
- Need Anthony's sign-off on folder names before any client drives are touched
- If going Option B/C: need Client Onboarding Agent spec updated to include Drive folder creation step (scope + OAuth perms to create subfolders in client drives)

## Done Criteria
- Folder structure documented in Brain (this note → moved to Context or Onboarding once locked)
- Every active client's Drive has all standard folders present
- New-client onboarding automatically creates the structure
- Creative Designer + Video Production agents have verified path conventions they can rely on

## Suggested Next Action
Anthony to answer: **"Ready to lock in the folder structure and have Emigen standardize existing clients, or should we build this into the Client Onboarding Agent first?"**

Once answered, this note gets promoted — either to `Onboarding/Client Drive Setup SOP.md` (if Emigen-led) or to the Client Onboarding Agent spec (if agent-led).

## Related
- [[AI Team Prep — Client Context Gaps]]
- [[AI Marketing Team — Build Plan]] (if exists)
- CLAUDE.md rules re: Creative Designer + Video Production agents
