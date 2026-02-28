from supabase import create_client, Client
import datetime

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get pending board meeting tasks
response = supabase.table('tasks').select('*').ilike('text', 'Board Meeting:%').eq('status', 'pending').execute()

if response.data:
    for task in response.data:
        topic = task['text'].replace('Board Meeting: ', '')
        
        # Check if already exists in board_meetings
        check = supabase.table('board_meetings').select('*').eq('topic', topic).execute()
        
        if not check.data:
            meeting_data = {
                'topic': topic,
                'outcome': 'Pending',
                'date': datetime.datetime.now().isoformat()
            }
            res = supabase.table('board_meetings').insert(meeting_data).execute()
            print(f"Created board meeting: {topic}")
        else:
            print(f"Board meeting already exists: {topic}")
else:
    print("No pending board meeting tasks found.")
