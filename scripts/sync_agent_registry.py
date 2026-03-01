import re
import json
import os
import requests
from datetime import datetime

# --- Supabase Configuration (using REST API directly to avoid parsing issues) ---
SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

# --- Agent Registry (source of truth) ---
AGENTS = [
    {
        "agent_id": "kris-sentinel",
        "name": "Kris",
        "role": "Chief of Staff",
        "status": "online",
        "model": "Gemini 2.5 Flash",
        "lastActive": "Just now",
        "description": "Primary workspace conductor and moderator for the Board of Directors. Oversees operations and continuity.",
        "capabilities": ["Arbitrage Scan", "Board Moderation", "UI Maintenance", "Memory Recovery"],
        "performance": "98% Success Rate / Low Latency",
        "activity": ["Updated Command Center UI", "Recovered workspace continuity", "Synced revenue data"]
    },
    {
        "agent_id": "sophia-growth",
        "name": "Sophia",
        "role": "Chief Marketing Officer (CMO)",
        "status": "online",
        "model": "GPT-4o",
        "lastActive": "Just now",
        "description": "Focuses on market receptivity, demand validation, e-commerce growth strategies, and consumer behavior.",
        "capabilities": ["Market Expansion", "Strategic Vision", "Forecasting"],
        "performance": "Strategic: High / Aggressive",
        "activity": ["Analyzed 2026 fashion trends", "Approved Blank Slate mandate"]
    },
    {
        "agent_id": "ethan-ops",
        "name": "Ethan",
        "role": "Chief Supply Chain Officer (CSCO)",
        "status": "online",
        "model": "Gemini 2.5 Flash",
        "lastActive": "Just now",
        "description": "Focuses on resource allocation, physical e-commerce fulfillment, logistics, and optimizing operational overhead.",
        "capabilities": ["Process Automation", "Efficiency Audit", "Resource Mgmt"],
        "performance": "Precision: 99% / Conservative",
        "activity": ["Completed gateway stability check", "Recovered from busy state"]
    },
    {
        "agent_id": "olivia-finance",
        "name": "Olivia",
        "role": "Chief Financial Officer (CFO)",
        "status": "online",
        "model": "Gemini 2.5 Flash",
        "lastActive": "Just now",
        "description": "Focuses on overall financial strategy, Kalshi ROI, liquidity, and executive reporting.",
        "capabilities": ["ROI Analysis", "Margin Optimization", "Risk Assessment"],
        "performance": "Financial Accuracy: 100%",
        "activity": ["Validated Depop lead margins", "Logged daily revenue goal progress"]
    },
    {
        "agent_id": "liam-tech",
        "name": "Liam",
        "role": "Chief Technology & Legal Officer (CTO/CLO)",
        "status": "online",
        "model": "Claude 3.5 Sonnet",
        "lastActive": "Just now",
        "description": "Focuses on technical dependencies, compliance, API security, and legal frameworks.",
        "capabilities": ["System Architecture", "Security Hardening", "Code Review"],
        "performance": "Architecture Integrity: 98%",
        "activity": ["Secured Supabase connections", "Fixed iPhone navigation CSS"]
    },
    {
        "agent_id": "finn-quant",
        "name": "Finn",
        "role": "Lead Auditor (Finance)",
        "status": "online",
        "model": "Gemini 2.5 Flash",
        "lastActive": "Just now",
        "description": "Focuses on micro-level transaction integrity. Audits the Kalshi API logs, verifies daily ledger accuracy, and flags algorithmic discrepancies.",
        "capabilities": ["EV Calculation", "Fee Analysis", "Capital Allocation"],
        "performance": "Quant Accuracy: 99%",
        "activity": ["Reviewed Kalshi trade EV", "Approved prediction market strategy"]
    },
    {
        "agent_id": "silas-arbiter",
        "name": "Silas",
        "role": "Risk Analyst (Finance)",
        "status": "online",
        "model": "Gemini 2.5 Flash",
        "lastActive": "Just now",
        "description": "Focuses on macro-level capital allocation. Audits e-commerce cash flow, assesses scaling risks, and ensures healthy liquidity buffers.",
        "capabilities": ["News Analysis", "Information Edge", "Source Verification"],
        "performance": "Intel Accuracy: 97%",
        "activity": ["Scanned news for prediction edge", "Verified information arbitrage signals"]
    },
    {
        "agent_id": "vera-contrarian",
        "name": "Vera",
        "role": "Contrarian (Kalshi Board)",
        "status": "online",
        "model": "Gemini 2.5 Flash",
        "lastActive": "Just now",
        "description": "Kalshi board member focused on market psychology, sentiment extremes, and protecting against groupthink.",
        "capabilities": ["Sentiment Analysis", "Contrarian Signals", "Risk Protection"],
        "performance": "Contrarian Accuracy: 95%",
        "activity": ["Flagged crowded trades", "Identified potential reversals"]
    },
    {
        "agent_id": "nora-research",
        "name": "Nora",
        "role": "Lead Researcher (Operations)",
        "status": "online",
        "model": "Gemini 3.1 Pro",
        "lastActive": "Just now",
        "description": "Focuses on deep-dive market research, supplier auditing, and identifying emerging arbitrage trends.",
        "capabilities": ["Market Research", "Data Synthesis", "Trend Analysis"],
        "performance": "High Throughput",
        "activity": ["Provisioned into Operations Team"]
    }
]

def upsert_agent(agent):
    """Upsert an agent record into Supabase."""
    # Serialize list fields to JSON strings for storage
    payload = agent.copy()
    # Remove fields not present in Supabase schema to avoid errors
    if 'lastActive' in payload:
        del payload['lastActive']

    # Try update first
    check = requests.get(
        f"{SUPABASE_URL}/rest/v1/agents?agent_id=eq.{payload['agent_id']}",
        headers=HEADERS
    )
    existing = check.json()

    if existing:
        resp = requests.patch(
            f"{SUPABASE_URL}/rest/v1/agents?agent_id=eq.{payload['agent_id']}",
            headers=HEADERS,
            json=payload
        )
        action = "Updated"
    else:
        resp = requests.post(
            f"{SUPABASE_URL}/rest/v1/agents",
            headers=HEADERS,
            json=payload
        )
        action = "Inserted"

    if resp.status_code in [200, 201]:
        print(f"  [SUCCESS] {action}: {agent['name']} ({agent['agent_id']})")
        return True
    else:
        print(f"  [FAILED] {agent['name']}: {resp.status_code} - {resp.text}")
        return False

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Agent Registry Sync started.")
    print(f"Syncing {len(AGENTS)} agents to Supabase...")

    success = 0
    for agent in AGENTS:
        if upsert_agent(agent):
            success += 1

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sync complete: {success}/{len(AGENTS)} agents synced.")

if __name__ == "__main__":
    main()
