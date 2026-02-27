import requests
from datetime import datetime

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

initial_tasks = [
    { "text": 'Operation Blank Slate: Pitching 4 streams to the Board.', "status": 'pending', "date": '2026-02-25', "link": None },
    { "text": 'Fix Mobile UI navigation visibility for iPhone.', "status": 'completed', "date": '2026-02-25', "link": None },
    { "text": 'First task: Deep-dive into strategic income streams.', "link": 'https://gist.github.com/mberman84/885c972f4216747abfb421bfbddb4eba', "status": 'pending', "date": '2026-02-25' }
]

response = requests.post(f"{SUPABASE_URL}/rest/v1/tasks", headers=headers, json=initial_tasks)

if response.status_code in [200, 201, 204]:
    print("OK - Successfully populated initial tasks in Supabase.")
else:
    print(f"Error - Failed to populate tasks: {response.status_code} - {response.text}")
