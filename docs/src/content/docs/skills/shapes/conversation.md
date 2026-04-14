---
title: conversation
description: "A message thread — an iMessage chat, WhatsApp group, email thread, Claude"
sidebar:
  label: conversation
---

A message thread — an iMessage chat, WhatsApp group, email thread, Claude
transcript, etc. Contains messages and links to participants.

Example sources: iMessage, WhatsApp, Gmail, Claude Code

| Metadata | Value |
|---|---|
| **Plural** | `conversations` |
| **Subtitle field** | `text` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `isGroup` | `boolean` |
| `isArchived` | `boolean` |
| `unreadCount` | `integer` |
| `messageCount` | `integer` |
| `accountEmail` | `string` |
| `cwd` | `string` |
| `gitBranch` | `string` |

## Relations

| Relation | Target |
|---|---|
| `platform` | [`product`](/docs/reference/shapes/product/) |
| `participant` | [`actor[]`](/docs/reference/shapes/actor/) |
| `message` | [`message[]`](/docs/reference/shapes/message/) |
| `in` | [`folder`](/docs/reference/shapes/folder/) |

## Skills that produce this shape

- [granola](/docs/reference/skills/productivity/granola/) — `op_list_conversations`
- [granola](/docs/reference/skills/productivity/granola/) — `op_get_conversation`
- [claude](/docs/reference/skills/ai/claude/) — `list_conversations`, `search_conversations`, `list_conversations_cli`
- [claude](/docs/reference/skills/ai/claude/) — `get_conversation`, `read_conversation_cli`
- [mimestream](/docs/reference/skills/comms/mimestream/) — `list_conversations`
- [mimestream](/docs/reference/skills/comms/mimestream/) — `get_conversation`
- [imessage](/docs/reference/skills/comms/imessage/) — `op_list_conversations`
- [imessage](/docs/reference/skills/comms/imessage/) — `op_get_conversation`
- [gmail](/docs/reference/skills/comms/gmail/) — `list_conversations`
- [gmail](/docs/reference/skills/comms/gmail/) — `get_conversation`
- [whatsapp](/docs/reference/skills/comms/whatsapp/) — `op_list_conversations`
- [whatsapp](/docs/reference/skills/comms/whatsapp/) — `op_get_conversation`
