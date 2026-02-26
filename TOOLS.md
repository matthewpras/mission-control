# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Email
- **Address**: `kris.sentinel.control@gmail.com`
- **SMTP**: `smtp.gmail.com:465` (SSL/TLS)
- **Login**: `kris.sentinel.control@gmail.com`
- **App Password**: `pjgb qxvm gnkz pqso`
- **Note**: Credentials stored for automated briefing delivery.

### Telegram
- **Primary Chat ID**: `8528907054` (Matthew Prasanth)
- **Mission Control Group**: `-1003882600560`
- **Topics Mapping**:
  - 📅 **Daily Brief**: threadId `9`
  - 🤝 **CRM**: threadId `10`
  - 📧 **Email**: threadId `11`
  - 🧠 **Knowledge Base**: threadId `12`
  - 📊 **Meta-Analysis**: threadId `13`
  - 🎥 **Video Ideas**: threadId `14`
  - 💰 **Earnings**: threadId `15`
  - ⚠️ **Cron Updates (Failures)**: threadId `16`
  - 🔒 **Financials (LOCKED)**: threadId `17`
  - 🏥 **Health**: threadId `18`
  - 🛍️ **Depop/E-comm**: threadId `19`
  - 🏠 **Real Estate**: threadId `20`
  - 🛠️ **Mission Control**: threadId `21`
  - 📂 **File Vault**: threadId `22`
- **Note**: Always use numeric IDs for targeting; display names are not supported.

### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### Mission Control Automation
- **Add Pipeline Lead**: `python scripts/add_lead.py --title "Title" --category "Cat" --profit 100`
- **Health Monitor**: `python scripts/health_monitor.py`

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
