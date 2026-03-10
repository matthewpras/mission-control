import requests
import json

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

def check_table(table_name):
    response = requests.get(f"{SUPABASE_URL}/rest/v1/{table_name}?select=*", headers=headers)
    if response.status_code == 200:
        print(f"Table '{table_name}' exists and has {len(response.json())} rows.")
        return True
    else:
        print(f"Table '{table_name}' check failed: {response.status_code}")
        return False

if __name__ == "__main__":
    check_table("leads")
    check_table("intel")
    check_table("tasks")
    check_table("board_meetings")
