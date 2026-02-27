## Core Objectives  
- [ ] **Health Monitoring:** Run `python scripts/health_monitor.py`. Only report if "ALERT" is found in the output.
- [ ] **System Integrity:** Check `openclaw gateway status`.  
- [ ] **Mission Control Sync:** Ensure `index.html` (V2 Cloud) is syncing revenue/tasks via Supabase. Update `tasks.json` with my current active tasks.
- [ ] **Task Synchronization:** Sync `tasks.json` to the UI (currently via `index.html` manual update until Supabase table is live).  
- [ ] **E-commerce Arbitrage:** Monitor Depop dropshipping margins and inventory status.  
- [ ] **Autonomous Loop:** If Matthew is away, proceed with high-confidence arbitrage research and document findings in `memory/YYYY-MM-DD.md`.  
- [ ] **Proactive Pulse:** Ping Matthew on Telegram with a "System Green" status if no issues found; alert immediately on errors.  
## Routine Checks  
- Every 30m: Check for new High-ROI arbitrage leads (Depop/E-commerce).
- Use `google/gemini-flash-latest` for routine heartbeat analysis.