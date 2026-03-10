import requests
import json
import time

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

def update_agent_status(agent_id, status, activity):
    data = {
        "status": status,
        "activity": activity
    }
    
    try:
        response = requests.patch(f"{SUPABASE_URL}/rest/v1/agents?agent_id=eq.{agent_id}", headers=headers, json=data)
        if response.status_code in [200, 201, 204]:
            print(f"OK - Updated status for {agent_id}")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Exception: {str(e)}")

if __name__ == "__main__":
    update_agent_status("kris-sentinel", "online", [
        "Clearing .git/index.lock",
        "Initialized The Concierge Engine (B2B SEO)",
        "Syncing tasks to Supabase",
        "Autonomous Mission: B2B Agency Launch Phase 1"
    ])
