import os
import subprocess
import json

# This script is a wrapper for the Council Audit
# It collects data and then spawns a sub-agent to analyze and message.

COLLECTOR = r"C:\Users\matthew prasanth\.openclaw\workspace\scripts\health_council_collector.py"
TEMP_FILE = r"C:\Users\matthew prasanth\.openclaw\workspace\temp_health_council_report.json"

def main():
    # Run collector
    try:
        result = subprocess.run(["python", COLLECTOR], capture_output=True, text=True, encoding='utf-8', errors='ignore')
        data = result.stdout
        
        # Write to a temp file to avoid CLI length limits
        with open(TEMP_FILE, "w", encoding="utf-8") as f:
            f.write(data)
        
        # Task for the Council Sub-agent
        # We instruct the sub-agent to read the file itself.
        task = f"""You are the Platform Health Council. 
        1. Read the system data from '{TEMP_FILE}'.
        2. Analyze this data for health, code quality, and system integrity.
        3. Deliver 9 numbered recommendations to Telegram (8528907054).
        4. Delete the temp file when done."""
        
        # Spawn the council sub-agent
        subprocess.run(["openclaw", "sessions", "spawn", "--task", task, "--mode", "run"], shell=True)
        print("Health Council audit initiated via sub-agent.")

    except Exception as e:
        print(f"Error running Health Council audit: {e}")

if __name__ == "__main__":
    main()
