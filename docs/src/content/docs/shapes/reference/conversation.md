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
| `platform` | [`product`](/docs/shapes/reference/product/) |
| `participant` | [`actor[]`](/docs/shapes/reference/actor/) |
| `message` | [`message[]`](/docs/shapes/reference/message/) |
| `in` | [`folder`](/docs/shapes/reference/folder/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0 context/inReplyTo](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-context)** — Conversations are AS2 contexts — the thread that groups replies. Our participant[] ≈ to/cc/audience.
- **[Matrix Room (m.room)](https://spec.matrix.org/latest/client-server-api/#room-events)** — Practical thread model. Our isGroup ≈ room.join_rules; unreadCount ≈ unread_notifications.highlight_count.
- **[Gmail API — Thread resource](https://developers.google.com/gmail/api/reference/rest/v1/users.threads)** — Our messageCount ≈ messages.length; unreadCount derived from UNREAD labels on Thread messages.

## Skills that produce this shape

- [granola](/docs/skills/reference/productivity/granola/) — `op_list_conversations`
- [granola](/docs/skills/reference/productivity/granola/) — `op_get_conversation`
- [claude](/docs/skills/reference/ai/claude/) — `list_conversations`, `search_conversations`, `list_conversations_cli`
- [claude](/docs/skills/reference/ai/claude/) — `get_conversation`, `read_conversation_cli`
- [mimestream](/docs/skills/reference/comms/mimestream/) — `list_conversations`
- [mimestream](/docs/skills/reference/comms/mimestream/) — `get_conversation`
- [imessage](/docs/skills/reference/comms/imessage/) — `op_list_conversations`
- [imessage](/docs/skills/reference/comms/imessage/) — `op_get_conversation`
- [gmail](/docs/skills/reference/comms/gmail/) — `list_conversations`
- [gmail](/docs/skills/reference/comms/gmail/) — `get_conversation`
- [whatsapp](/docs/skills/reference/comms/whatsapp/) — `op_list_conversations`
- [whatsapp](/docs/skills/reference/comms/whatsapp/) — `op_get_conversation`
