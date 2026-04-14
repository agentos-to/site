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
| `platform` | [`product`](/docs/shapes/reference/product/) |
| `from` | [`actor`](/docs/shapes/reference/actor/) |
| `inConversation` | [`conversation`](/docs/shapes/reference/conversation/) |
| `repliesTo` | [`message`](/docs/shapes/reference/message/) |
| `toolCalls` | [`tool_call[]`](/docs/shapes/reference/tool_call/) |

## Used as a base by

- [`email`](/docs/shapes/reference/email/)

## Skills that produce this shape

- [claude](/docs/skills/reference/ai/claude/) — `import_conversation`
- [imessage](/docs/skills/reference/comms/imessage/) — `op_list_messages`, `op_search_messages`
- [imessage](/docs/skills/reference/comms/imessage/) — `op_get_message`
- [whatsapp](/docs/skills/reference/comms/whatsapp/) — `op_list_messages`, `op_search_messages`
- [whatsapp](/docs/skills/reference/comms/whatsapp/) — `op_get_message`
