---
title: message
description: "A single message in a conversation. Base type — email extends this via also."
sidebar:
  label: message
---

A single message in a conversation. Base type — email extends this via `also`.
Querying by "message" returns emails alongside iMessages, WhatsApp messages,
Claude transcripts, etc.

Example sources: iMessage, WhatsApp, Claude Code; extended by email (Gmail, Mimestream)

| Metadata | Value |
|---|---|
| **Plural** | `messages` |
| **Subtitle field** | `from` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `isOutgoing` | `boolean` |
| `isStarred` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `platform` | [`product`](/docs/reference/shapes/product/) |
| `from` | [`actor`](/docs/reference/shapes/actor/) |
| `inConversation` | [`conversation`](/docs/reference/shapes/conversation/) |
| `repliesTo` | [`message`](/docs/reference/shapes/message/) |
| `toolCalls` | [`tool_call[]`](/docs/reference/shapes/tool_call/) |

## Used as a base by

- [`email`](/docs/reference/shapes/email/)

## Skills that produce this shape

- [claude](/docs/reference/skills/ai/claude/) — `import_conversation`
- [imessage](/docs/reference/skills/comms/imessage/) — `op_list_messages`, `op_search_messages`
- [imessage](/docs/reference/skills/comms/imessage/) — `op_get_message`
- [whatsapp](/docs/reference/skills/comms/whatsapp/) — `op_list_messages`, `op_search_messages`
- [whatsapp](/docs/reference/skills/comms/whatsapp/) — `op_get_message`
