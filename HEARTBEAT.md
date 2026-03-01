## Core Objectives  
- [ ] **Health Monitoring:** Run `python scripts/health_monitor.py`. Only report if "ALERT" is found in the output.
- [ ] **Board Meeting Scheduler:** Run `python scripts/board_meeting_executor.py` to process scheduled meetings.
- [ ] **Agent Task Dispatch:** Run `python scripts/agent_task_executor.py` to process UI-dispatched agent commands from the Mission Control dashboard.
- [ ] **System Integrity:** Check `openclaw gateway status`.  
- [ ] **Mission Control Sync:** Ensure `index.html` (V2 Cloud) is syncing revenue/tasks via Supabase. Update `tasks.json` with my current active tasks.
- [ ] **Task Synchronization:** Sync `tasks.json` to the UI (currently via `index.html` manual update until Supabase table is live).  
- [ ] **Kalshi Trades Algorithm:** Monitor liquidity, event probability, and API health for prediction market trades.
- [ ] **Autonomous Loop:** If Matthew is away, proceed with high-confidence Kalshi market research and document findings in `memory/YYYY-MM-DD.md`.  
- [ ] **Proactive Pulse:** Ping Matthew on Telegram with a "System Green" status if no issues found; alert immediately on errors.  
## Routine Checks  
- Every 1h: Scan Kalshi API for high-volume markets and cross-platform arbitrage (e.g., vs Polymarket).
- Use `google/gemini-flash-latest` for routine heartbeat analysis.