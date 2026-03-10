# EmberMist Customer Acquisition Strategy
**Date:** March 2026
**Framework:** Hybrid Organic-to-Paid (The "Spark" Loop)

## Division of Labor
This strategy relies on separating high-leverage technical automation from high-leverage human aesthetic judgment.

*   **Kris (AI Chief of Staff):** Creative Director, Data Analyst, API Ad Manager.
*   **Matthew (Human Operator):** Production, Native CapCut Editing, Organic Distribution (to leverage in-app trending audio).

## The Automation Loop
1.  **Ideation (Automated):** Kris analyzes current TikTok/Reels trends for home decor/wellness and generates 5 specific video concepts per week. This includes the hook text, visual angles, and caption formulas.
2.  **Creation (Manual):** Matthew shoots the raw clips (using the prime-sourced sample) and edits them natively in CapCut/TikTok to ensure native transitions and fonts.
3.  **Distribution (Manual):** Matthew posts the videos organically to TikTok and Instagram Reels, attaching the latest trending audio to bypass API restrictions.
4.  **Amplification (Automated via API):** 
    *   Kris monitors organic performance metrics via API (or regular CSV exports if API is rate-limited).
    *   **Trigger:** If an organic video crosses a baseline metric (e.g., >500 views in the first hour, or a high engagement rate), Kris automatically triggers a TikTok Spark Ad API call (or Meta equivalent) to inject a $50/day test budget behind the winning creative.
    *   **Scaling:** Winners are scaled aggressively; losers are killed automatically based on ROAS data pulled from Shopify.

## Bottleneck Mitigations
*   **Video Editing:** Avoid programmatic video generation (ffmpeg) to prevent the "bot aesthetic." Keep edits native.
*   **Ad Platform Anti-Bot:** Bypass web UI completely. All automated ad buying will be routed through the Meta Graph API and TikTok Marketing API.
*   **Audio Trends:** Avoid auto-posting tools (Buffer/Later) that strip trending audio. Manual posting is required for algorithmic traction.
