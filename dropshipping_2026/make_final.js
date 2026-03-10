const fs = require('fs');
let html = fs.readFileSync('dropshipping_2026/EmberMist_Report_v2.html', 'utf8');
const imgBase = fs.readFileSync('dropshipping_2026/cover_image.png').toString('base64');
html = html.replace('src="cover_image.png"', 'src="data:image/png;base64,' + imgBase + '"');
html = html.replace('<style>', '<style>\n@media print { * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; } }\n');
fs.writeFileSync('dropshipping_2026/EmberMist_Report_Final.html', html);

let scriptHtml = fs.readFileSync('dropshipping_2026/EmberMist_TikTok_Scripts.html', 'utf8');
scriptHtml = scriptHtml.replace('<style>', '<style>\n@media print { * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; } }\n');
fs.writeFileSync('dropshipping_2026/EmberMist_TikTok_Scripts_Final.html', scriptHtml);
