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
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
| `isOutgoing` | `boolean` |
| `isStarred` | `boolean` |
| `conversationId` | `string` |

## Relations

| Relation | Target |
|---|---|
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `sent_by` | [`actor`](/shapes/reference/actor/) |
| `in` | [`conversation`](/shapes/reference/conversation/) |
| `replies_to` | [`message`](/shapes/reference/message/) |
| `attaches` | [`file[]`](/shapes/reference/file/) |

## Used as a base by

- [`email`](/shapes/reference/email/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0 Note/Activity](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-note)** — Closest open standard for generic messages. Our from ≈ actor; inConversation ≈ context/conversation; repliesTo ≈ inReplyTo.
- **[Matrix m.room.message](https://spec.matrix.org/latest/client-server-api/#mroommessage)** — Practical cross-platform message event schema. Our isOutgoing has no Matrix analog (sender identity instead); repliesTo ≈ m.relates_to rel_type m.thread/m.in_reply_to.
- **[XMPP (RFC 6121) message stanza](https://datatracker.ietf.org/doc/html/rfc6121)** — IETF instant-messaging baseline. from/to/thread correspond to our from/inConversation; no standardized isStarred.

## Skills that produce this shape

- [claude](/skills/reference/ai/claude/) — `import_conversation`
- [imessage](/skills/reference/comms/imessage/) — `list_messages`, `search_messages`, `get_message`
- [whatsapp](/skills/reference/comms/whatsapp/) — `list_messages`, `search_messages`, `get_message`, `send_message`, `send_media`
