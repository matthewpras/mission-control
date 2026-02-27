import requests
import json

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

tables = ["revenue", "leads", "agents", "board_meetings", "tasks"]

results = {}

for table in tables:
    try:
        # Get last 5 entries for each table
        response = requests.get(f"{SUPABASE_URL}/rest/v1/{table}?select=*&order=created_at.desc&limit=5", headers=headers)
        if response.status_code == 200:
            results[table] = response.json()
        else:
            results[table] = f"Error {response.status_code}"
    except Exception as e:
        results[table] = str(e)

print(json.dumps(results, indent=2))
