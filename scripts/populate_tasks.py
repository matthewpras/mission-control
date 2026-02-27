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

# Load tasks from tasks.json
with open('tasks.json', 'r') as f:
    tasks_data = json.load(f)

# Clear existing tasks first (to avoid duplicates if we're doing a full sync)
# requests.delete(f"{SUPABASE_URL}/rest/v1/tasks", headers=headers)

# Transform data for Supabase if needed (Supabase might not use the same 'id')
supabase_tasks = []
for t in tasks_data:
    supabase_tasks.append({
        "text": t["text"],
        "status": t["status"],
        "date": t["date"]
    })

response = requests.post(f"{SUPABASE_URL}/rest/v1/tasks", headers=headers, json=supabase_tasks)

if response.status_code in [200, 201, 204]:
    print("OK - Successfully populated tasks in Supabase.")
else:
    print(f"Error - Failed to populate tasks: {response.status_code} - {response.text}")
