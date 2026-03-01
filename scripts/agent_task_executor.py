import os
import re
import subprocess
import sys
import time
from datetime import datetime
from supabase import create_client, Client

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# --- Supabase Configuration ---
SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def poll_and_execute():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Agent Task Executor checking for pending tasks...")
    
    try:
        # Fetch pending tasks that follow the [AGENT: id] pattern
        response = supabase.table('tasks').select('*').eq('status', 'pending').execute()
        tasks = response.data
    except Exception as e:
        print(f"Error fetching tasks from Supabase: {e}")
        return

    if not tasks:
        # print("No pending tasks found.")
        return

    processed_count = 0
    for task_obj in tasks:
        task_id = task_obj['id']
        task_text = task_obj.get('text', '')
        
        # Check if it's an agent dispatch command
        match = re.match(r'\[AGENT:\s*([^\]]+)\]\s*(.*)', task_text)
        if not match:
            continue
        
        agent_id = match.group(1).strip()
        command = match.group(2).strip()
        
        print(f"Found task for agent '{agent_id}': {command}")
        
        # Execute via OpenClaw CLI
        # Usage: openclaw agent --agent <id> --message <text>
        try:
            print(f"Spawning session for {agent_id}...")
            # We use --deliver if we want it to potentially reply back to a channel if configured, 
            # but for background tasks we usually just want it to run.
            # Using shell=True on Windows for reliability with the 'openclaw' command
            result = subprocess.run(
                f'openclaw agent --agent "{agent_id}" --message "{command}"',
                capture_output=True,
                text=True,
                shell=True
            )
            
            if result.returncode == 0:
                print(f"Successfully triggered task for {agent_id}.")
                # Mark as completed in Supabase
                supabase.table('tasks').update({'status': 'completed'}).eq('id', task_id).execute()
                processed_count += 1
            else:
                print(f"Failed to trigger task for {agent_id}: {result.stderr}")
                
        except Exception as e:
            print(f"Exception during task execution: {e}")

    if processed_count > 0:
        print(f"Successfully processed {processed_count} agent tasks.")

if __name__ == "__main__":
    poll_and_execute()
