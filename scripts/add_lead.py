import argparse
import requests
import sys

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

def add_lead(title, category, profit, status, notes, link):
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }

    lead = {
        "title": title,
        "category": category,
        "potential_profit": float(profit) if profit else 0,
        "status": status,
        "notes": notes,
        "link": link
    }

    try:
        response = requests.post(f"{SUPABASE_URL}/rest/v1/leads", headers=headers, json=lead)
        if response.status_code in [200, 201, 204]:
            print(f"OK - Added lead: {title}")
            return True
        else:
            print(f"Error {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print(f"Exception: {str(e)}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a lead to Mission Control Pipeline")
    parser.add_argument("--title", required=True, help="Lead title")
    parser.add_argument("--category", default="Arbitrage", help="Lead category")
    parser.add_argument("--profit", default=0, help="Potential profit")
    parser.add_argument("--status", default="New", help="Status (New, Researching, Active, Closed)")
    parser.add_argument("--notes", default="", help="Lead notes")
    parser.add_argument("--link", default="", help="Relevant link")

    args = parser.parse_args()
    
    if add_lead(args.title, args.category, args.profit, args.status, args.notes, args.link):
        sys.exit(0)
    else:
        sys.exit(1)
