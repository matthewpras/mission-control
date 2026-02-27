import requests

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

lead = {
    "title": "Vintage Digital Cameras (Sony/Canon)",
    "category": "E-commerce",
    "potential_profit": 140.00,
    "status": "Researching",
    "notes": "Identified high-ROI stream (Avg 140% margin). Feb 2026 trend."
}

response = requests.post(f"{SUPABASE_URL}/rest/v1/leads", headers=headers, json=lead)

if response.status_code in [200, 201, 204]:
    print("OK - Successfully added Vintage Digicam lead to Supabase.")
else:
    print(f"Error - Failed to add lead: {response.status_code} - {response.text}")
