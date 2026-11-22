---
date: 2026-11-17
tags: [automation, token-efficiency, infrastructure, needs-human-input]
related: ["[[Intelligence/00-INDEX]]"]
---

# Automation Token-Waste Audit — 2026-11-17

Triggered by Anthony's Slack DM (2026-11-16 20:38, voice-to-text, garbled): "Pause on dumps and action[s] that cause excess token usage that [aren't] working and notate it so I can fix them later."

## What I checked
- `crontab -l` — only weekly Brain maintenance jobs (brain-snapshot, brain-link-density, brain-map, brain-graphify-update). Low frequency, no sign of waste.
- All `com.launchpad.*` launchd plists + `logs/runs/scheduled/*.json` — bbc-ops, morning-briefing, trend-scanner, notion-brain-sync, slack-inbox, carousel-monitor, brain-dump, ads-reports-monthly all show `exit:0` on their most recent run today, no cost field populated.
- `logs/alerts.log` (last few hours) — repeated exit-75 (preflight-auth failure) across morning-briefing, trend-scanner, shumi-anime-scanner, notion-brain-sync, bbc-ops. Per `scripts/preflight-auth.sh`, exit 75 means the run is skipped for ~$0.02 before any real work starts — this is cheap, not "excess."
- `ps aux` — no stuck/zombie `claude -p` processes. One long-lived **interactive VS Code Claude Code session (PID 1238) has been open since 2026-11-02 — 15 days, 163 min CPU time.** This is real standing resource use on the 8 GB Mini (see `project_mac_mini_host_constraints` memory: "close idle interactive sessions on the Mini when you are done with them"). Not a scheduled "dump," but worth closing if not in active use.

## What I could NOT confirm
No scheduled job shows a clear "burns a lot of tokens AND isn't working" signature from available data — `logs/runs/agents/` (where per-run `costUsd` is supposed to be tracked, per `scripts/RUNNER.md` §1) has been **empty since Oct 21**, so there's no per-run cost telemetry to point at a specific culprit. This is itself a gap: we can't actually see which scheduled runs are expensive right now.

## Candidates flagged for Anthony to confirm (none paused yet — didn't want to guess and kill something that's fine)
1. **Recurring Claude auth outage** (3rd distinct occurrence since 11-14, recurring again today 11-17 ~17:44) — not token-expensive per attempt, but it's firing the same preflight-skip across 5 scheduled jobs repeatedly. See `project_claude_subscription_access_disabled_2026_11_14`.
2. **shumi-anime-scanner** — failing exit-75 on nearly every attempt today specifically because of #1. Genuinely "not working" right now, but cost per attempt is ~$0.02, not excess.
3. **kb-weekly-refresh** — never run once (no log ever written). Dead, not wasteful (zero cost), just never installed per `RUNNER.md` §5.2.
4. **Idle VS Code Claude Code session since 11-02** — host resource use, not Claude API token spend.

## Open question for Anthony
Which specific run(s) felt like "excess token usage" to you? If you can name one (or paste a cost number you saw), I can pause that specific launchd/cron job immediately. Also flagging: the `logs/runs/agents/` cost-tracking directory being empty since Oct 21 means we're currently flying blind on real per-run cost — worth fixing so this kind of ask is answerable from data next time.
