// Initial Agent Data
const initialAgents = [
    {
        id: 'kris-001',
        name: 'Kris',
        role: 'Sentinel / Researcher',
        status: 'online',
        model: 'Gemini 2.0 Flash',
        lastActive: new Date().toLocaleString(),
        description: 'Primary workspace agent and strategic researcher. Handles real estate and arbitrage analysis.',
        capabilities: ['Arbitrage Research', 'Market Analysis', 'System Maintenance', 'Memory Management'],
        activityLog: ['Connected to Telegram', 'Analyzed MTR trends', 'Updated Mission Control UI'],
        performance: 'High - optimized for context-aware research.'
    },
    {
        id: 'ollama-002',
        name: 'Ollama-Llama',
        role: 'Local Pulse Monitor',
        status: 'online',
        model: 'Llama 3.2 3B',
        lastActive: '5m ago',
        description: 'Local monitoring agent for heartbeat checks and system health.',
        capabilities: ['Heartbeat Monitoring', 'Local File Audits', 'Gateway Probing'],
        activityLog: ['Logged heartbeat', 'Checked gateway status'],
        performance: 'Stable - running on local resources.'
    },
    {
        id: 'arbitrage-003',
        name: 'ArbiBot',
        role: 'Market Scraper',
        status: 'busy',
        model: 'GPT-4o-mini',
        lastActive: '12m ago',
        description: 'Specialized bot for scraping Depop and e-commerce platforms for ROI leads.',
        capabilities: ['Web Scraping', 'Price Comparison', 'Trend Spotting'],
        activityLog: ['Scanned Depop for suede bags', 'Identified 3 high-ROI leads'],
        performance: 'Efficient - high volume processing.'
    }
];

const initialDecisions = [
    { date: '2026-02-24', question: 'Drop-shipping vs Inventory?', summary: 'Pivoted to drop-shipping for Depop to minimize risk.', consulted: 'Matthew, Kris' },
    { date: '2026-02-24', question: '2026 Trend Focus', summary: 'Identified "Prep 3.0" and "Mob Wife" as key aesthetics.', consulted: 'Kris, ArbiBot' }
];

// Initialize Data
let agents = JSON.parse(localStorage.getItem('mc_agents')) || initialAgents;
let decisions = JSON.parse(localStorage.getItem('mc_decisions')) || initialDecisions;
let selectedAgentId = null;

function saveData() {
    localStorage.setItem('mc_agents', JSON.stringify(agents));
    localStorage.setItem('mc_decisions', JSON.stringify(decisions));
}

// Tab Switching
function switchTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    
    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
    
    if (tabId === 'command-center') renderCommandCenter();
}

// Render Command Center
function renderCommandCenter() {
    const grid = document.getElementById('agent-grid');
    grid.innerHTML = agents.map(agent => `
        <div class="card" onclick="openDetailPanel('${agent.id}')">
            <h3>${agent.name} <span class="status-dot status-${agent.status}"></span></h3>
            <p><strong>Role:</strong> ${agent.role}</p>
            <p><strong>Model:</strong> ${agent.model}</p>
            <p><strong>Last Active:</strong> ${agent.lastActive}</p>
        </div>
    `).join('');

    const decisionsList = document.getElementById('decisions-list');
    decisionsList.innerHTML = decisions.map(d => `
        <li class="decision-item">
            <strong>${d.date}</strong>: ${d.question}
            <p>${d.summary}</p>
            <small>Consulted: ${d.consulted}</small>
        </li>
    `).join('');
}

// Detail Panel
function openDetailPanel(agentId) {
    selectedAgentId = agentId;
    const agent = agents.find(a => a.id === agentId);
    const panel = document.getElementById('detail-panel');
    const content = document.getElementById('agent-details');
    
    content.innerHTML = `
        <h2>${agent.name}</h2>
        <p><strong>Role:</strong> ${agent.role}</p>
        <hr style="border:0; border-top:1px solid #334155; margin:15px 0;">
        <p>${agent.description}</p>
        
        <h3>Capabilities</h3>
        <ul>${agent.capabilities.map(c => `<li>${c}</li>`).join('')}</ul>
        
        <h3>Recent Activity</h3>
        <ul id="agent-activity-log">${agent.activityLog.map(log => `<li>${log}</li>`).join('')}</ul>
        
        <h3>Performance</h3>
        <p>${agent.performance}</p>
    `;
    
    panel.classList.add('active');
}

function closeDetailPanel() {
    document.getElementById('detail-panel').classList.remove('active');
}

// Modal
function openTaskModal() {
    document.getElementById('send-task-modal').style.display = 'block';
}

function closeModal() {
    document.getElementById('send-task-modal').style.display = 'none';
}

function submitTask() {
    const taskText = document.getElementById('task-area').value;
    if (taskText && selectedAgentId) {
        const agent = agents.find(a => a.id === selectedAgentId);
        agent.activityLog.unshift(`Task Sent: ${taskText}`);
        agent.lastActive = 'Just now';
        saveData();
        
        // Refresh UI
        openDetailPanel(selectedAgentId);
        renderCommandCenter();
        
        document.getElementById('task-area').value = '';
        closeModal();
        alert('Task sent to ' + agent.name);
    }
}

// Init
document.addEventListener('DOMContentLoaded', () => {
    renderCommandCenter();
});
