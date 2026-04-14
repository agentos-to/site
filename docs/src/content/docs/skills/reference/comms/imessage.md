---
title: iMessage
description: "Send and read iMessages and SMS from macOS Messages app"
sidebar:
  label: imessage
---

| Metadata | Value |
|---|---|
| **Category** | `comms` |
| **Capabilities** | `shell`, `sql` |
| **Website** | <https://support.apple.com/messages> |

## Returns shapes

- [`conversation`](/docs/shapes/reference/conversation/) — from `op_get_conversation`
- [`conversation[]`](/docs/shapes/reference/conversation/) — from `op_list_conversations`
- [`message`](/docs/shapes/reference/message/) — from `op_get_message`
- [`message[]`](/docs/shapes/reference/message/) — from `op_list_messages`, `op_search_messages`

## Connections

- **`db`**

## Readme

Send and read iMessages and SMS from the macOS Messages app.

## Requirements

- **macOS only** — Reads from local Messages database, sends via Messages.app
- **Full Disk Access** — System Settings → Privacy & Security → Full Disk Access (for reading)
- **Automation permission** — System Settings → Privacy & Security → Automation → allow Terminal to control Messages.app (for sending)
- **imsg CLI** — `brew tap steipete/tap && brew install imsg` (for sending)

## Sending Messages

Send uses [imsg](https://github.com/steipete/imsg) by [Peter Steinberger](https://github.com/steipete) — a native Swift CLI that talks to Messages.app via public macOS APIs and AppleScript. No private APIs, stable across macOS versions.

Recipients can be:
- Phone numbers in E.164 format: `+14155551234`
- Email addresses registered with Apple ID: `user@example.com`

```bash
# Send via API
curl -X POST http://localhost:3456/use/imessage/message.send \
  -H "X-Agent: cursor" \
  -H "Content-Type: application/json" \
  -d '{"to": "+14155551234", "text": "Hello from AgentOS!"}'
```

## Handles

iMessage handles are already in E.164 format for phone numbers (`+12025551234`) or email addresses.
This enables direct matching with WhatsApp contacts for social graph deduplication.

## Features

- **Send** messages via iMessage or SMS
- **List** all conversations
- **Get** messages from a conversation  
- **Search** across all messages
