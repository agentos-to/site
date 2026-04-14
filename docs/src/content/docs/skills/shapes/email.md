---
title: email
description: "An email message. Emails are also messages — querying by 'message'"
sidebar:
  label: email
---

An email message. Emails are also messages — querying by "message"
returns emails alongside WhatsApp, iMessage, etc.

Example sources: Gmail, Mimestream
RFC headers (message_id, in_reply_to, references) enable threading.
Domain relations auto-extracted from sender/recipient addresses.

| Metadata | Value |
|---|---|
| **Plural** | `emails` |
| **Subtitle field** | `author` |
| **Identity** | `platform`, `id` |
| **Also** | [`message`](/docs/reference/shapes/message/) |

## Fields

| Field | Type |
|---|---|
| `subject` | `string` |
| `messageId` | `string` |
| `inReplyTo` | `string` |
| `isUnread` | `boolean` |
| `isStarred` | `boolean` |
| `isDraft` | `boolean` |
| `isSent` | `boolean` |
| `isTrash` | `boolean` |
| `isSpam` | `boolean` |
| `hasAttachments` | `boolean` |
| `accountEmail` | `string` |
| `sizeEstimate` | `integer` |
| `references` | `string` |
| `replyTo` | `string` |
| `deliveredTo` | `string` |
| `attachments` | `json` |
| `toRaw` | `string` |
| `ccRaw` | `string` |
| `bccRaw` | `string` |
| `unsubscribe` | `string` |
| `unsubscribeOneClick` | `boolean` |
| `manageSubscription` | `string` |
| `listId` | `string` |
| `isAutomated` | `boolean` |
| `precedence` | `string` |
| `mailer` | `string` |
| `returnPath` | `string` |
| `authResults` | `string` |
| `bodyHtml` | `text` |

## Relations

| Relation | Target |
|---|---|
| `from` | [`account`](/docs/reference/shapes/account/) |
| `to` | [`account[]`](/docs/reference/shapes/account/) |
| `cc` | [`account[]`](/docs/reference/shapes/account/) |
| `bcc` | [`account[]`](/docs/reference/shapes/account/) |
| `domain` | [`domain`](/docs/reference/shapes/domain/) |
| `toDomain` | [`domain[]`](/docs/reference/shapes/domain/) |
| `ccDomain` | [`domain[]`](/docs/reference/shapes/domain/) |
| `tag` | [`tag[]`](/docs/reference/shapes/tag/) |

## Inherited

From [`message`](/docs/reference/shapes/message/):

| Field | Type |
|---|---|
| `isOutgoing` | `boolean` |

| Relation | Target |
|---|---|
| `inConversation` | [`conversation`](/docs/reference/shapes/conversation/) |
| `platform` | [`product`](/docs/reference/shapes/product/) |
| `repliesTo` | [`message`](/docs/reference/shapes/message/) |
| `toolCalls` | [`tool_call[]`](/docs/reference/shapes/tool_call/) |

## Skills that produce this shape

- [mimestream](/docs/reference/skills/comms/mimestream/) — `list_emails`, `search_emails`
- [mimestream](/docs/reference/skills/comms/mimestream/) — `get_email`
- [gmail](/docs/reference/skills/comms/gmail/) — `list_email_stubs`, `list_emails`, `search_emails`, `list_drafts`
- [gmail](/docs/reference/skills/comms/gmail/) — `get_email`, `get_draft`, `send_email`, `reply_email`, `forward_email`, `modify_email`, `trash_email`, `untrash_email`, `create_draft`, `update_draft`, `send_draft`
