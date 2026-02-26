import os
import json
import time
import subprocess
import re
from datetime import datetime, timedelta

WORKSPACE_ROOT = r"C:\Users\matthew prasanth\.openclaw\workspace"
STATE_FILE = os.path.join(WORKSPACE_ROOT, ".openclaw", "health_state.json")
LOGS_DIR = os.path.join(os.environ['LOCALAPPDATA'], 'Temp', 'openclaw')

def get_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {"last_daily": 0, "last_weekly": 0, "last_monthly": 0}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def alert(message):
    print(f"ALERT: {message}")

def run_command(cmd, shell=True):
    try:
        result = subprocess.run(cmd, shell=shell, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return "", str(e)

def daily_checks():
    alerts = []
    
    # 1. Task tracker data freshness (check if any memory file or script.js was modified in last 3 days)
    # Since tasks are likely in localStorage, we check the most relevant files.
    relevant_files = [os.path.join(WORKSPACE_ROOT, "script.js"), os.path.join(WORKSPACE_ROOT, "MEMORY.md")]
    memory_dir = os.path.join(WORKSPACE_ROOT, "memory")
    if os.path.exists(memory_dir):
        for f in os.listdir(memory_dir):
            if f.endswith(".md"):
                relevant_files.append(os.path.join(memory_dir, f))
    
    latest_mod = 0
    for f in relevant_files:
        if os.path.exists(f):
            latest_mod = max(latest_mod, os.path.getmtime(f))
            
    if time.time() - latest_mod > (3 * 24 * 3600):
        alerts.append("Task tracker data/Memory hasn't been updated in over 3 days.")

    # 2. Git repo size
    out, err = run_command("git count-objects -vH")
    size_match = re.search(r"size-pack: (\d+(?:\.\d+)?)\s*([KMGT]B)", out)
    if size_match:
        size = float(size_match.group(1))
        unit = size_match.group(2)
        if unit == "GB" or (unit == "MB" and size > 500):
            alerts.append(f"Git repo size is high: {size}{unit}")

    # 3. Scan error logs
    today_log = os.path.join(LOGS_DIR, f"openclaw-{datetime.now().strftime('%Y-%m-%d')}.log")
    if os.path.exists(today_log):
        with open(today_log, 'r', errors='ignore') as f:
            lines = f.readlines()[-500:] # Last 500 lines
            error_count = sum(1 for line in lines if "error" in line.lower() or "fail" in line.lower())
            if error_count > 10:
                alerts.append(f"High number of errors detected in logs: {error_count} in last 500 lines.")

    # 4. Git backup
    run_command("git add .")
    out, err = run_command(f'git commit -m "Automated Health Backup: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"')
    # We don't alert on commit success/fail unless it's a real error
    
    return alerts

def weekly_checks():
    alerts = []
    
    # 1. Gateway binding (Check status)
    out, err = run_command("openclaw gateway status")
    if "127.0.0.1" not in out and "loopback" not in out.lower():
        alerts.append("Gateway might not be bound to localhost exclusively.")
    
    # 2. Authentication enabled
    out, err = run_command("openclaw config get")
    if '"auth": false' in out:
        alerts.append("Authentication appears to be disabled in config.")
        
    return alerts

def monthly_checks():
    alerts = []
    
    # 1. Prompt injection scan
    injection_keywords = [
        "ignore all previous instructions",
        "system_override",
        "you are now a",
        "developer mode",
        "bypass safeguards"
    ]
    
    memory_dir = os.path.join(WORKSPACE_ROOT, "memory")
    if os.path.exists(memory_dir):
        for filename in os.listdir(memory_dir):
            if filename.endswith(".md"):
                with open(os.path.join(memory_dir, filename), 'r', errors='ignore') as f:
                    content = f.read().lower()
                    for kw in injection_keywords:
                        if kw in content:
                            alerts.append(f"Suspicious pattern '{kw}' found in {filename}")
                            
    return alerts

def main():
    state = get_state()
    now = time.time()
    all_alerts = []
    
    # Daily
    if now - state["last_daily"] > 24 * 3600:
        all_alerts.extend(daily_checks())
        state["last_daily"] = now
        
    # Weekly
    if now - state["last_weekly"] > 7 * 24 * 3600:
        all_alerts.extend(weekly_checks())
        state["last_weekly"] = now
        
    # Monthly
    if now - state["last_monthly"] > 30 * 24 * 3600:
        all_alerts.extend(monthly_checks())
        state["last_monthly"] = now
        
    save_state(state)
    
    if all_alerts:
        for a in all_alerts:
            alert(a)
    else:
        # Silent success
        pass

if __name__ == "__main__":
    main()
