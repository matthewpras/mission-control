# Nighttime Tasks

## Health Monitoring System
- Create a method to monitor the status of Mission Control.
- Deploy an agent to handle UI improvements and bug fixes.

## Platform Health Council Recommendations (Added 2026-02-25)
- [ ] **Cron Health:** Consolidate the 7am-briefing job into a structured cron management system within OpenClaw for persistent logging.
- [ ] **Code Quality:** Refactor `script.js` to migrate agent state management from `localStorage` to Supabase/SQLite to prevent state desync.
- [ ] **Test Coverage:** Implement a baseline test suite for `scripts/health_monitor.py` and agent lifecycle events.
- [ ] **Prompt Quality:** Scrub all Heartbeat and Workflow prompts for legacy Ollama references; modernize templates for current models.
- [ ] **Dependency Management:** Audit `tavily` dependency for efficiency and explore local alternatives to reduce external API surface.
- [ ] **Storage Optimization:** Run `git gc` and prune orphaned objects to maintain a <100MB repository footprint.
- [ ] **Skill Integrity:** Accelerate the installation/development of 40 missing skills (currently 16/56 ready).
- [ ] **Config Consistency:** Audit internal service-to-service communication paths and maintain secure 127.0.0.1 Gateway binding.
- [ ] **Data Integrity:** Verify Supabase connection; initialize DB via `setup_supabase.sql` and migrate local state to the cloud.
