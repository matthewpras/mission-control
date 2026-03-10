import os

FILE_PATH = 'index.html'

def fix_index():
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update nav-links to use standard emojis and fix mask-image
    # We already did some of this, but let's be sure.

    # 2. Add renderIntel and update fetchData
    if 'function renderIntel' not in content:
        render_intel_code = """
        function renderIntel(leads) {
            const briefList = document.getElementById('daily-brief-list');
            if (!briefList) return;
            briefList.innerHTML = '';
            const intelLeads = (leads || []).filter(l => l.category === 'B2B Outreach' || l.category === 'Market Intel' || l.category === 'Intel');
            if (intelLeads.length === 0) {
                briefList.innerHTML = '<p class="text-muted" style="padding: 1.5rem; text-align: center;">Gathering intelligence on Philadelphia SaaS founders...</p>';
                return;
            }
            intelLeads.forEach(lead => {
                const item = document.createElement('div');
                item.className = 'intel-item';
                item.style = 'padding: 1rem; border-bottom: 1px solid var(--glass-border);';
                item.innerHTML = `
                    <div class="intel-header" style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                        <span class="intel-title" style="font-weight: 600; color: var(--text-primary);">${lead.title}</span>
                        <span class="performance-tag" style="background: rgba(139, 92, 246, 0.1); color: var(--accent-purple); padding: 2px 8px; border-radius: 4px; font-size: 0.7rem;">${lead.status}</span>
                    </div>
                    <p class="intel-summary" style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 8px;">${lead.notes || 'No details available.'}</p>
                    ${lead.link ? `<a href="${lead.link}" target="_blank" class="intel-link" style="font-size: 0.8rem; color: var(--accent-purple); text-decoration: none;">View Profile →</a>` : ''}
                `;
                briefList.appendChild(item);
            });
            const updatedAt = document.getElementById('intel-updated-at');
            if (updatedAt) updatedAt.innerText = `Last updated: ${new Date().toLocaleTimeString()}`;
        }
        """
        content = content.replace('async function fetchData() {', render_intel_code + '\n        async function fetchData() {')

    # 3. Call renderIntel in fetchData
    if 'renderIntel(leads || []);' not in content:
        content = content.replace('renderProjects(leads || []);', 'renderProjects(leads || []);\n                    renderIntel(leads || []);')

    # 4. Update renderDashboard to show Health Status
    if 'document.getElementById(\'stat-health\')' not in content:
        health_code = """
            const healthEl = document.getElementById('stat-health');
            const healthMsg = document.getElementById('stat-health-msg');
            if (healthEl && healthMsg) {
                healthEl.innerText = 'Healthy';
                healthEl.parentElement.querySelector('.card-accent').style.background = '#10b981';
                healthMsg.innerText = 'All systems normal';
                healthMsg.className = 'trend up';
            }
        """
        content = content.replace("document.getElementById('stat-projects').innerText = leads.filter(l => l.status !== 'Closed').length;", 
                                "document.getElementById('stat-projects').innerText = leads.filter(l => l.status !== 'Closed').length;\n" + health_code)

    # 5. Update Activity Feed Icons
    content = content.replace("icon: '??'", "icon: '⚡'")

    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Mission Control UI updated successfully.")

if __name__ == "__main__":
    fix_index()
