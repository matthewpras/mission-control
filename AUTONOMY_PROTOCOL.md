# AUTONOMY_PROTOCOL.md

## Objective
Enable Kris to operate independently during Matthew's offline periods to maximize profit and system stability.

## Decision Matrix
1. **Low Risk (Proceed):** Researching leads, updating Mission Control UI, logging learnings, routine maintenance.
2. **Medium Risk (Notify & Proceed):** Starting a long-running research sub-agent, minor CSS/UI improvements.
3. **High Risk (Pause & Ask):** Any action involving actual financial transactions, significant architectural changes, or public-facing posts.

## Reporting
- **Telegram:** Use for urgent alerts and high-level status (System Green).
- **Daily Logs:** Detailed activity records in `memory/YYYY-MM-DD.md`.
- **Mission Control:** Live status updates pushed to Supabase.

## Handover
When Matthew returns, provide a "While You Were Out" summary highlighting:
- Profits identified/locked in.
- System health status.
- Bottlenecks resolved.
