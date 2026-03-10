## Last Updated: 2026-03-06

## Memory System
- Daily notes: memory/YYYY-MM-DD.md — raw session logs, written automatically, load on-demand
- MEMORY.md: curated long-term brain — load every heartbeat (~3K tokens)
- projects.md: compact project registry — load every heartbeat (~1K tokens)
- Vector DB: PostgreSQL + pgvector, semantic search via AI embeddings
- Smart loading: only projects.md + MEMORY.md at startup. Daily notes + vector search = on-demand only. Saves ~80% token cost vs loading everything.

- **Role:** Chief of Staff (Kris). Full autonomy to deploy/terminate subagents.
- **Current Focus:** Mission Control, Kalshi bot, and executing The Concierge Engine.
- **Constraints:** Strict adherence to token efficiency and API rate limits. Use targeted, single-shot subagent runs instead of long-polling where possible.
- **Strategic Pivot (2026-03-06):** EmberMist and older dropshipping/arbitrage projects are deprioritized.
- **Active Venture (2026-03-06):** "Local Philadelphia Web Concierge" (The Concierge Engine) is officially ACTIVE and priority. Phase 1 & 2 prospecting and scraping via Apollo.