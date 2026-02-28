import requests
import json

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

response = requests.get(f"{SUPABASE_URL}/rest/v1/board_meetings?select=*", headers=headers)
if response.status_code == 200:
    data = response.json()
    if data:
        print(f"Columns: {list(data[0].keys())}")
    else:
        # Try to get column names via OpenAPI spec if possible, or just insert a dummy
        print("Table is empty.")
        # Attempt a dummy insert to see error or columns
        dummy = {"topic": "dummy"}
        res = requests.post(f"{SUPABASE_URL}/rest/v1/board_meetings", headers=headers, json=dummy)
        print(f"Insert status: {res.status_code}")
        print(f"Insert response: {res.text}")
else:
    print(f"Error: {response.status_code}")
