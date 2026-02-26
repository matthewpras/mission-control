## [ERR-20260225-001] telegram_message_target

**Logged**: 2026-02-25T00:10:00-05:00
**Priority**: high
**Status**: pending
**Area**: config | message

### Summary
Failed to send Telegram messages due to invalid target names and "403 Forbidden" (bot not in chat).

### Error
```
403: Forbidden: bot is not a member of the channel chat
Unknown target "Matthew Prasanth" for Telegram. Hint: <chatId>
Action send requires a target.
```

### Context
- Command: `message(action=send, target="telegram", ...)`
- Parameters: Target was initially a generic string "telegram", then a display name "Matthew Prasanth".
- Environment: Telegram bot enabled via `openclaw.json`.

### Suggested Fix
1. Verify bot membership in target chat/group.
2. Use numeric `chatId` from `openclaw.json` (e.g., `8528907054`) instead of display names.
3. Check `groupAllowFrom` in `openclaw.json` to find valid targets.

### Metadata
- Reproducible: yes
- Related Files: openclaw.json
- See Also: LRN-20260225-001

---
