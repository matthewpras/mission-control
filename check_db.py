from supabase import create_client, Client
import sys

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def check():
    try:
        res = supabase.table('board_meetings').select('*').execute()
        print(f"Total board meetings: {len(res.data)}")
        for m in res.data:
            print(f"ID: {m['id']}, Topic: {m['topic']}, Outcome: {m['outcome']}, Date: {m['date']}")
            
        res_tasks = supabase.table('tasks').select('*').eq('status', 'pending').execute()
        print(f"\nPending tasks: {len(res_tasks.data)}")
        for t in res_tasks.data:
             print(f"Task: {t['text']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check()
