---
title: message
description: "A single message in a conversation. Base type — email extends this via also."
sidebar:
  label: message
---

A single message in a conversation. Base type — email extends this via `also`.
Querying by "message" returns emails alongside iMessages, WhatsApp messages,
Claude transcripts, etc.

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
| `platform` | [`product`](/shapes/reference/product/) |
| `from` | [`actor`](/shapes/reference/actor/) |
| `inConversation` | [`conversation`](/shapes/reference/conversation/) |
| `repliesTo` | [`message`](/shapes/reference/message/) |
| `toolCalls` | [`tool_call[]`](/shapes/reference/tool_call/) |

## Used as a base by

- [`email`](/shapes/reference/email/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0 Note/Activity](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-note)** — Closest open standard for generic messages. Our from ≈ actor; inConversation ≈ context/conversation; repliesTo ≈ inReplyTo.
- **[Matrix m.room.message](https://spec.matrix.org/latest/client-server-api/#mroommessage)** — Practical cross-platform message event schema. Our isOutgoing has no Matrix analog (sender identity instead); repliesTo ≈ m.relates_to rel_type m.thread/m.in_reply_to.
- **[XMPP (RFC 6121) message stanza](https://datatracker.ietf.org/doc/html/rfc6121)** — IETF instant-messaging baseline. from/to/thread correspond to our from/inConversation; no standardized isStarred.

## Skills that produce this shape

- [claude](/skills/reference/ai/claude/) — `import_conversation`
- [imessage](/skills/reference/comms/imessage/) — `op_list_messages`, `op_search_messages`, `op_get_message`
- [whatsapp](/skills/reference/comms/whatsapp/) — `op_list_messages`, `op_search_messages`, `op_get_message`
