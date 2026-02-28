import os
import json
import subprocess
import sys
from supabase import create_client, Client
from datetime import datetime, timedelta
import time

# Ensure UTF-8 output for emojis and special characters
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass # Fallback not strictly needed if we're on modern python

# --- Supabase Configuration ---
SUPABASE_URL = 'https://qawxadldkxanuzvzrddk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhd3hhZGxka3hhbnV6dnpyZGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NTg0OTAsImV4cCI6MjA4NzUzNDQ5MH0.W0VgGT6m3uLUlgk7DadJP_ZCTh-Vn4lc7jl6kkFC-8E'
TELEGRAM_GROUP_ID = '-1003882600560' # Mission Control Group
META_ANALYSIS_THREAD_ID = '13' # Meta-Analysis topic

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def schedule_google_calendar(topic, summary, start_time=None, duration_minutes=60):
    """Schedules the meeting on Google Calendar via gog CLI."""
    try:
        if start_time:
            if isinstance(start_time, str):
                start_dt = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
            else:
                start_dt = start_time
        else:
            # Default to 1 hour from now
            start_dt = datetime.now() + timedelta(hours=1)
            
        end_dt = start_dt + timedelta(minutes=duration_minutes)
        
        # gog expects ISO format (RFC3339)
        start_iso = start_dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_iso = end_dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        
        # Use gog to insert event
        # Corrected command for gog CLI v0.11.0
        cmd_str = f'gog calendar create primary --summary "Board Meeting: {topic}" --description "{summary}" --from "{start_iso}" --to "{end_iso}"'
        
        print(f"Executing: {cmd_str}")
        result = subprocess.run(cmd_str, capture_output=True, text=True, shell=True)
        
        if result.returncode == 0:
            print(f"Successfully scheduled on Google Calendar: {result.stdout}")
            return True
        else:
            print(f"Failed to schedule on Google Calendar: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Error scheduling calendar event: {e}")
        return False

# --- Persona Logic (Simplified for direct execution) ---
# In a full sub-agent setup, these would be separate agents.
# Here, we simulate their responses directly.

def sophia_growth(topic):
    """Sophia: Challenges related to market analysis and consumer behavior."""
    return f"Sophia (Growth): My primary concern is the market's receptivity to '{topic}'. We need robust data on consumer behavior, competitive landscape, and potential saturation. How will we validate demand before committing significant resources?"

def ethan_ops(topic):
    """Ethan: Financial implications and resource allocation concerns."""
    return f"Ethan (Operations): From an operational standpoint, '{topic}' presents resource allocation challenges. What are the overheads, scaling costs, and logistical hurdles? We must ensure efficient use of capital and a clear ROI pathway."

def olivia_finance(topic):
    """Olivia: ROI, margins, and financial integrity."""
    return f"Olivia (Finance): For '{topic}', I'd focus on the hard numbers. What are the projected profit margins, break-even points, and potential for sustainable revenue? We need to stress-test the financial model for profitability and risk."

def liam_tech(topic):
    """Liam: Legal considerations and compliance issues."""
    return f"Liam (Tech/Legal): My input on '{topic}' centers on the technical and compliance aspects. Are there any unforeseen legal or regulatory frameworks we need to navigate? Also, what are the technical dependencies and potential security implications?"

def simulate_board_meeting(topic):
    transcript = []
    directive_points = []

    # Kris (Moderator)
    kris_intro = f"Kris (Moderator): Welcome Board, today's topic for deliberation is: '{topic}'. Let's hear your critical challenges and insights."
    transcript.append(kris_intro)
    directive_points.append(f"Topic: {topic}")

    # Persona responses
    sophia_response = sophia_growth(topic)
    transcript.append(sophia_response)
    directive_points.append(f"Growth Challenge: Market receptivity and demand validation.")

    ethan_response = ethan_ops(topic)
    transcript.append(ethan_response)
    directive_points.append(f"Operational Challenge: Resource allocation, scaling costs, logistics.")

    olivia_response = olivia_finance(topic)
    transcript.append(olivia_response)
    directive_points.append(f"Financial Challenge: Profit margins, break-even points, sustainability.")

    liam_response = liam_tech(topic)
    transcript.append(liam_response)
    directive_points.append(f"Tech/Compliance Challenge: Legal/regulatory, technical dependencies, security.")

    # Synthesis
    synthesis = f"Kris (Moderator): Based on the board's critical challenges, the consolidated strategic directive for '{topic}' emphasizes: {', '.join([p.split(': ')[1] for p in directive_points])}. A robust plan addressing these areas is essential."
    transcript.append(synthesis)

    summary = f"Board discussed '{topic}'. Key challenges identified: market receptivity, resource allocation, financial viability, and tech/compliance. Strategic directive: develop a plan addressing these core areas for successful execution."

    full_transcript = "\\n".join(transcript)
    
    return {
        "summary": summary,
        "transcript": full_transcript,
        "directive": synthesis
    }

# --- Main Execution Logic ---
def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Board Meeting Executor started.")
    
    # 1. Fetch pending board meetings
    try:
        # Fetch both 'Pending' (newly created) and 'Scheduled' (future meetings)
        response_pending = supabase.table('board_meetings').select('*').eq('outcome', 'Pending').execute()
        response_scheduled = supabase.table('board_meetings').select('*').eq('outcome', 'Scheduled').execute()
        
        pending_meetings = response_pending.data + response_scheduled.data
    except Exception as e:
        print(f"Error fetching pending meetings: {e}")
        return

    if not pending_meetings:
        print("No pending board meetings found.")
        return

    print(f"Found {len(pending_meetings)} pending board meetings.")

    for meeting in pending_meetings:
        meeting_id = meeting['id']
        topic = meeting['topic']
        scheduled_date_str = meeting['date']  # Assuming ISO format or YYYY-MM-DD
        
        try:
            # Handle both date-only and full ISO
            if 'T' in scheduled_date_str:
                scheduled_dt = datetime.fromisoformat(scheduled_date_str.replace('Z', '+00:00'))
            else:
                scheduled_dt = datetime.strptime(scheduled_date_str, '%Y-%m-%d')
        except ValueError:
            # Fallback to today if parsing fails
            scheduled_dt = datetime.now()

        # Check if meeting is for the future (more than 5 mins ahead)
        if scheduled_dt > datetime.now() + timedelta(minutes=5):
            # Meeting is in the future.
            if meeting['outcome'] == 'Pending':
                 print(f"Scheduling future meeting '{topic}' for {scheduled_dt}")
                 success = schedule_google_calendar(topic, f"Topic: {topic}", start_time=scheduled_dt)
                 if success:
                     supabase.table('board_meetings').update({'outcome': 'Scheduled'}).eq('id', meeting_id).execute()
            else:
                 print(f"Meeting '{topic}' is already scheduled for {scheduled_dt}. Waiting for time...")
            continue

        print(f"Processing meeting ID: {meeting_id}, Topic: '{topic}'")

        # Simulate the meeting
        meeting_results = simulate_board_meeting(topic)
        summary = meeting_results['summary']
        transcript = meeting_results['transcript']
        directive = meeting_results['directive']

        # Schedule on Google Calendar (New Feature)
        schedule_google_calendar(topic, summary)

        # Format message for Telegram
        telegram_message = f"📊 **Board Meeting: '{topic}' (Outcome Delivered)**\\n\\n" \
                           f"**Summary:** {summary}\\n\\n" \
                           f"**Strategic Directive:** {directive}\\n\\n" \
                           f"**Full Transcript:**\\n```\\n{transcript}\\n```"

        # 2. Send to Telegram Meta-Analysis channel
        try:
            print(f"Sending to Telegram group {TELEGRAM_GROUP_ID}, thread {META_ANALYSIS_THREAD_ID}:\\n{telegram_message}")
        except Exception as e:
            print(f"Error sending to Telegram: {e}")

        # 3. Update Supabase board_meetings table
        try:
            update_data = {
                'outcome': 'Completed',
                'summary': summary
            }
            response = supabase.table('board_meetings').update(update_data).eq('id', meeting_id).execute()
            if response.data:
                print(f"Updated board_meetings for ID {meeting_id}.")
            else:
                print(f"Failed to update board_meetings for ID {meeting_id}: {response}")
        except Exception as e:
            print(f"Error updating board_meetings: {e}")

        # 4. Update corresponding task in tasks table
        try:
            # Assuming task text is "Board Meeting: {topic}"
            task_response = supabase.table('tasks').update({'status': 'completed'}).like('text', f'Board Meeting: {topic}%').execute()
            if task_response.data:
                print(f"Updated related task for '{topic}' to completed.")
            else:
                print(f"Failed to update task for '{topic}': {task_response}")
        except Exception as e:
            print(f"Error updating related task: {e}")
        
        time.sleep(1) # Small delay to avoid hammering Supabase or Telegram API

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Board Meeting Executor finished.")

if __name__ == "__main__":
    main()
