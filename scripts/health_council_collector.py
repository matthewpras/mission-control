import os
import json
import subprocess
import glob
import sys
from datetime import datetime

# Configuration
WORKSPACE_ROOT = r"C:\Users\matthew prasanth\.openclaw\workspace"
TELEGRAM_TARGET = "8528907054"

def run_command(cmd):
    try:
        # Use shell=True for Windows commands and handle encoding
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def get_council_context():
    context = {}
    
    # 1. Cron Job Health
    context['cron_jobs'] = run_command("openclaw cron list")
    
    # 2. Code Quality (Sample files)
    js_files = glob.glob(os.path.join(WORKSPACE_ROOT, "*.js"))
    py_files = glob.glob(os.path.join(WORKSPACE_ROOT, "scripts", "*.py"))
    md_files = glob.glob(os.path.join(WORKSPACE_ROOT, "*.md"))
    context['code_samples'] = []
    for f in (js_files + py_files + md_files)[:8]:
        try:
            with open(f, 'r', encoding='utf-8', errors='ignore') as file:
                context['code_samples'].append({
                    "file": os.path.relpath(f, WORKSPACE_ROOT), 
                    "content": file.read(1500)
                })
        except:
            continue
            
    # 3. Prompt Quality
    heartbeat_path = os.path.join(WORKSPACE_ROOT, "HEARTBEAT.md")
    if os.path.exists(heartbeat_path):
        with open(heartbeat_path, 'r', encoding='utf-8') as f:
            context['heartbeat_prompt'] = f.read()

    # 4. Dependencies
    pkg_json = os.path.join(WORKSPACE_ROOT, "package.json")
    if os.path.exists(pkg_json):
        with open(pkg_json, 'r') as f:
            context['dependencies'] = json.load(f).get('dependencies', {})

    # 5. Storage
    context['storage'] = run_command("git count-objects -vH")

    # 6. Skill Integrity
    context['skills'] = run_command("openclaw skills list")
    
    # 7. Data Integrity (Check if DB setup exists)
    context['db_setup'] = os.path.exists(os.path.join(WORKSPACE_ROOT, "setup_supabase.sql"))

    return context

if __name__ == "__main__":
    data = get_council_context()
    print(json.dumps(data, indent=2))
