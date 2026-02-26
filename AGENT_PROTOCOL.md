# AGENT_PROTOCOL.md

## Optimization & Throttle Rules
1. **Model Routing:** 
   - Use `gpt-4o-mini` or `gemini-flash` for all scraping/research tasks.
   - Use `gpt-4o` or `sonnet` ONLY for complex architectural decisions or UI design.
2. **Context Management:** 
   - Clear sub-agent history every 10 messages to prevent "Token Bloat."
   - Summarize findings in `memory/` instead of keeping long raw logs.
3. **Execution Limits:** 
   - No agent should run for more than 5 minutes without a manual status report.
   - Max 3 active concurrent sub-agents to preserve host CPU/Gateway stability.
4. **Bottleneck Monitoring:** 
   - If gateway latency exceeds 500ms, pause all non-essential scraping.
   - Report "High Usage" alerts to Matthew via Telegram if daily cost exceeds $2.00.

## 5. Memory Pruning & Optimization
- **Session Compaction:** At 3:00 AM, I will summarize all `memory/YYYY-MM-DD-HHMM.md` fragments from the last 24 hours into a single "Daily Essence" file and delete the raw fragments to keep the vector search fast.
- **Context Refresh:** I will restart the main session's context window nightly to clear "hallucination debt" while keeping the core directives from `MEMORY.md` and `SOUL.md` pinned.
- **Workspace Cleanup:** Delete temporary script outputs (e.g., `gmail_config.json`, `test_email.py`) after successful execution.
