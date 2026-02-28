# MODEL_CONFIG.md - Model Roles & Strategy

## Configuration (2026-02-27)

| Role | Model ID | Usage |
| :--- | :--- | :--- |
| **Primary (Brain)** | `google/gemini-3.1-pro-preview` | Enhanced "Dynamic Thinking." Best for complex coding and multi-step planning. |
| **Secondary (Speed)** | `google/gemini-3-flash-preview` | **Use for 90% of tasks.** Optimized for tool-calling and long-context retention. |
| **Legacy/Stable** | `google/gemini-flash-latest` | Ultimate fallback if 3-series previews encounter rate limits. |

## Directives
- Default to **Secondary (Speed)** for general operations, quick queries, and standard tool use.
- Switch to **Primary (Brain)** for architectural decisions, deep debugging, or complex code generation.
