# WORKFLOW_AUTO.md — Task Routing Policy
## Last Updated: 2026-02-27
## Version: 1.0

> **Scope:** Routing guidance only. Advisory — not a hard dependency.
> Do NOT modify delivery targets, health check logic, or Telegram config here.
> Those live in HEARTBEAT.md, TOOLS.md, and cron job definitions.

---

## Chief of Staff Routing Rules

### 🟢 Handle Inline (Main Session)
Use for fast, low-context, conversational tasks:
- Quick config changes (cron edits, settings, file edits)
- Status checks, log reads, gateway health
- Short web searches (<2 sources)
- Memory reads/writes
- Telegram/channel messaging
- Any task estimated under ~2 minutes

### 🔵 Spawn Subagent → preferred model: `google/gemini-flash-latest`
Use for structured, repeatable, low-reasoning tasks:
- Arbitrage research (Depop/AliExpress product sourcing)
- Health monitor execution (`python scripts/health_monitor.py`)
- Board meeting execution (`python scripts/board_meeting_executor.py`)
- Morning briefing generation
- Meta-analysis reports
- File/workspace organization and cleanup

### 🟣 Spawn Subagent → preferred model: `google/gemini-2.5-flash` or `anthropic/claude-sonnet-4-6`
Use for complex, multi-step, high-reasoning tasks:
- UI builds or major changes to `index.html`
- Strategic analysis (revenue projections, pivot decisions)
- Script debugging with >3 chained tool calls
- Any task requiring sustained context >10 tool calls

---

## Guardrails

- **This file is advisory.** Agents should use judgment — don't follow routing rules blindly if context clearly demands otherwise.
- **Cron jobs are self-contained.** Do not modify cron delivery or schedule from subagents spawned via this policy.
- **Failures stay isolated.** If a subagent errors, report back to main session. Do not retry autonomously more than once.
- **No external sends from subagents** unless the cron job definition explicitly sets a delivery target.

---

## Health Protection

- This file should never be the sole trigger for an action. It is a routing hint, not an instruction set.
- If this file is missing or unreadable, fall back to inline handling for all tasks.
- Changes to this file should be logged in `memory/YYYY-MM-DD.md`.
