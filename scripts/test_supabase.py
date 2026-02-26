import requests

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

tables = ["revenue", "leads", "agents"]

for table in tables:
    try:
        response = requests.get(f"{SUPABASE_URL}/rest/v1/{table}?select=*", headers=headers)
        if response.status_code == 200:
            print(f"Table '{table}': OK - {len(response.json())} rows")
        else:
            print(f"Table '{table}': Error {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Table '{table}': Exception - {str(e)}")
