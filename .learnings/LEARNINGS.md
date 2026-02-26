## [LRN-20260225-001] telegram_targeting_config

**Logged**: 2026-02-25T00:10:00-05:00
**Priority**: medium
**Status**: pending
**Area**: config | message

### Summary
Always check `openclaw.json` for valid Telegram `chatId`s when display names fail.

### Details
The Telegram plugin does not resolve human display names like "Matthew Prasanth". It requires specific numeric IDs or usernames. The `openclaw.json` file (typically in `~\.openclaw\`) contains these IDs in the `channels.telegram.groupAllowFrom` field.

### Suggested Action
Before attempting proactive messaging, cross-reference the target with the `openclaw.json` configuration to ensure the ID is valid and allowed.

### Metadata
- Source: error
- Related Files: openclaw.json
- Tags: telegram, config, targeting
- See Also: ERR-20260225-001

---
