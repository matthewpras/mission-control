# Executive Reporter (executive-reporter)

Creates highly polished, executive-level business reports in PDF format with AI-generated cover visuals.

## Trigger
Use this skill when the user asks for a "polished PDF," "executive report," "pitch deck," or "business plan."

## Workflow / Protocol
1. **Content Generation**: Draft the full report content (Executive Summary, Financials, Market Analysis, Strategy, etc.) based on the user's prompt.
2. **Cover Image Generation**: 
   - Call the `exec` tool to run `nano-banana-pro` (Gemini 3 Pro Image) via `uv run`. 
   - Prompt it for a photorealistic, cinematic, high-quality image relevant to the product or topic. 
   - Save the image (e.g., `cover_image.png`) to the workspace.
3. **HTML Construction (Strict CSS & Base64)**: 
   - Write a Node.js script (e.g., `make_report.js`) that reads the raw HTML template and injects the generated image directly as a Base64 string (`data:image/png;base64,...`) to avoid local pathing errors.
   - **Crucial Design Elements**: 
     - Font: Inter (`https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap`).
     - CSS Print Media: MUST inject `<style>@media print { * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; } }</style>` to prevent the PDF engine from stripping background colors and highlights.
     - Elements: Use `.highlight-box` for key takeaways, `.data-grid` for financial metrics, and clean tables for comparisons.
4. **PDF Export (Native Edge Headless Engine)**: 
   - DO NOT use the OpenClaw `browser` tool or `md-to-pdf` (they fail on Windows spaces and Puppeteer proxy drops). 
   - Use the `exec` tool to invoke Microsoft Edge natively via PowerShell:
     ```powershell
     & "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --print-to-pdf="C:\Users\matthew prasanth\.openclaw\workspace\report_output.pdf" "C:\Users\matthew prasanth\.openclaw\workspace\report_input.html"
     ```
5. **Finalization**: 
   - Send the finalized PDF to the user via the `message` tool (`channel: "telegram"`).
   - Delete the temporary HTML files and build scripts to keep the workspace clean.
