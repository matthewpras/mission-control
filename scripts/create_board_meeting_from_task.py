from supabase import create_client, Client
import datetime

SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get the task
task_text = 'Board Meeting: Create a detailed plan to reach $100 by March 5th goal.'
response = supabase.table('tasks').select('*').eq('text', task_text).execute()

if response.data:
    task = response.data[0]
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
    print("Task not found.")
