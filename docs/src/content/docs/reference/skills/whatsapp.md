---
title: WhatsApp
description: "Read WhatsApp messages from local macOS database"
sidebar:
  label: whatsapp
---

**Category:** `comms` · **Capabilities:** `sql` · **Website:** https://www.whatsapp.com/

## Returns shapes

- [`conversation`](/docs/reference/shapes/conversation/) — from `op_get_conversation`
- [`conversation[]`](/docs/reference/shapes/conversation/) — from `op_list_conversations`
- [`message`](/docs/reference/shapes/message/) — from `op_get_message`
- [`message[]`](/docs/reference/shapes/message/) — from `op_list_messages`, `op_search_messages`
- [`person[]`](/docs/reference/shapes/person/) — from `op_list_persons`

## Connections

- **`db`**

## Readme

Read WhatsApp messages from the local macOS database. Read-only access to message history.

## Requirements

- **macOS only** — Reads from local WhatsApp database
- **WhatsApp desktop app** — Must be installed and logged in

## Conversation IDs

Conversations use numeric IDs (SQLite primary keys like `880`, `899`). Always use the `id` returned by `list_conversations` — these are **not** JIDs.

## Common Tasks

- **Get active chats:** `list_conversations` (default — non-archived only)
- **Get archived chats:** `list_conversations` with `archived: true`
- **Get unread messages:** `list_messages` with `unread: true` (no conversation_id needed)
- **Get group participants:** `list_persons` with `conversation_id` param
- **Search messages:** `search_messages` with `query` param

## Contact Identifiers

WhatsApp uses two identifier formats:
- **JID:** `12125551234@s.whatsapp.net` (phone-based, used for DMs)
- **LID:** `opaque_id@lid` (server-assigned, newer format)

The `list_persons` operation resolves both formats to phone numbers when available via the contacts database.

## Entity Model

- **person** — the human, with phone number and name from contacts
- **account** — their WhatsApp identity (JID/LID), linked to person via `claim` relationship
- **conversation** — a chat thread, with `participant` → account reference for the DM partner
- **message** — a text message, with `from` → account reference for the sender

This means: person → claims → account → sends → message. Traverse the graph to connect messages to people.

## Notes

- `is_outgoing: true` indicates messages you sent
- Incoming messages include a `from` account reference for the sender's WhatsApp identity
- Media-only messages (images, voice notes) without text are excluded from message queries
- All timestamps are ISO 8601 format
