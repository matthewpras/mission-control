import requests
import json
import os

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

def sync_leads():
    try:
        with open("concierge-engine/leads.json", "r") as f:
            data = json.load(f)
            people = data.get("people", [])
            
            for p in people:
                lead = {
                    "title": p["name"],
                    "category": "B2B Outreach",
                    "potential_profit": 500, # Base SEO article price
                    "status": "New",
                    "notes": f"Role: {p['title']} @ {p['organization']['name']}",
                    "link": p.get("linkedin_url", "")
                }
                
                response = requests.post(f"{SUPABASE_URL}/rest/v1/leads", headers=headers, json=lead)
                if response.status_code in [200, 201, 204]:
                    print(f"OK - Synced {p['name']} to Supabase")
                else:
                    print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Exception: {str(e)}")

if __name__ == "__main__":
    sync_leads()
