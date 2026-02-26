import os
import subprocess

# This script is a wrapper for the Council Audit
# It collects data and then spawns a sub-agent to analyze and message.

COLLECTOR = r"C:\Users\matthew prasanth\.openclaw\workspace\scripts\health_council_collector.py"

def main():
    # Run collector
    result = subprocess.run(["python", COLLECTOR], capture_output=True, text=True, encoding='utf-8', errors='ignore')
    data = result.stdout
    
    # Task for the Council Sub-agent
    task = f"""You are the Platform Health Council. Analyze this system data and deliver 9 numbered recommendations to Telegram (8528907054). 
    Context: {data}"""
    
    # Spawn the council sub-agent
    subprocess.run(["openclaw", "sessions", "spawn", "--task", task, "--mode", "run"], shell=True)

if __name__ == "__main__":
    main()
