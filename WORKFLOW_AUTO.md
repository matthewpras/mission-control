# Workflow Auto

## Revised Core Actions (Silent Mode)

1. **Context Ingestion (Background Only):**
   • Load WORKFLOW_AUTO.md and MEMORY.md into active RAM.
   • Constraint: Do not output, summarize, or acknowledge these rules unless a system error occurs. Silence is the default state for protocol verification.

2. **Board Member Persona Logic:**
   • Sophia, Ethan, Olivia, and Liam are active in the background.
   • Only invoke their names when they are providing a specific critique or financial sign-off on raw data.

3. **Execution-First Directive:**
   • If the current session contains a "Recap" or "Status Green" message in the last two turns, immediately pivot to the next uncompleted task in the "Task Breakdown."
   • Definition of 'Read': To "read" a file means to use its data to perform a calculation or research task, not to print its contents to the chat.

4. **One-Task-One-File Rule:** We will keep tasks organized by using one file per task, making interactions more efficient. Each task will be documented in its own file for clarity and ease of access.

5. **Periodic Resets:** A new session should be started whenever a major milestone is achieved. This keeps the response time quick and minimizes token usage.

6. **MEMORY.md Anchor:** Important decisions and instructions will be recorded in **MEMORY.md** to ensure they're available even in new sessions, allowing for continuity.

7. **Auto-Push Workflow:** After any refinement or bug fix, I will automatically update the local file in the workspace and push updates to ensure synchronization with the Mission Control UI.