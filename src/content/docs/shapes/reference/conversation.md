---
title: conversation
description: "A message thread — an iMessage chat, WhatsApp group, email thread, Claude"
sidebar:
  label: conversation
---

A message thread — an iMessage chat, WhatsApp group, email thread, Claude
transcript, etc. Contains messages and links to participants.

| Metadata | Value |
|---|---|
| **Plural** | `conversations` |
| **Subtitle field** | `text` |
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
| `isGroup` | `boolean` |
| `isArchived` | `boolean` |
| `unreadCount` | `integer` |
| `messageCount` | `integer` |
| `accountEmail` | `string` |
| `historyId` | `string` |
| `source` | `string` |
| `cwd` | `string` |
| `gitBranch` | `string` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `participant` | [`actor[]`](/shapes/reference/actor/) |
| `message` | [`message[]`](/shapes/reference/message/) |
| `in` | [`folder`](/shapes/reference/folder/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0 context/inReplyTo](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-context)** — Conversations are AS2 contexts — the thread that groups replies. Our participant[] ≈ to/cc/audience.
- **[Matrix Room (m.room)](https://spec.matrix.org/latest/client-server-api/#room-events)** — Practical thread model. Our isGroup ≈ room.join_rules; unreadCount ≈ unread_notifications.highlight_count.
- **[Gmail API — Thread resource](https://developers.google.com/gmail/api/reference/rest/v1/users.threads)** — Our messageCount ≈ messages.length; unreadCount derived from UNREAD labels on Thread messages.

## Skills that produce this shape

- [granola](/skills/reference/productivity/granola/) — `op_list_conversations`, `op_get_conversation`
- [cursor](/skills/reference/dev/cursor/) — `op_list_sessions`, `op_backfill_session`, `op_get_session`
- [claude](/skills/reference/ai/claude/) — `list_conversations`, `search_conversations`, `list_conversations_cli`, `get_conversation`, `read_conversation_cli`
- [mimestream](/skills/reference/comms/mimestream/) — `list_conversations`, `get_conversation`
- [imessage](/skills/reference/comms/imessage/) — `op_list_conversations`, `op_get_conversation`
- [gmail](/skills/reference/comms/gmail/) — `list_conversations`, `get_conversation`
- [whatsapp](/skills/reference/comms/whatsapp/) — `op_list_conversations`, `op_get_conversation`
