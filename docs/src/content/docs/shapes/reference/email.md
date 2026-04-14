---
title: email
description: "An email message. Emails are also messages — querying by 'message'"
sidebar:
  label: email
---

An email message. Emails are also messages — querying by "message"
returns emails alongside WhatsApp, iMessage, etc.
RFC headers (message_id, in_reply_to, references) enable threading.
Domain relations auto-extracted from sender/recipient addresses.

| Metadata | Value |
|---|---|
| **Plural** | `emails` |
| **Subtitle field** | `author` |
| **Identity** | `platform`, `id` |
| **Also** | [`message`](/docs/shapes/reference/message/) |

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
| `from` | [`account`](/docs/shapes/reference/account/) |
| `to` | [`account[]`](/docs/shapes/reference/account/) |
| `cc` | [`account[]`](/docs/shapes/reference/account/) |
| `bcc` | [`account[]`](/docs/shapes/reference/account/) |
| `domain` | [`domain`](/docs/shapes/reference/domain/) |
| `toDomain` | [`domain[]`](/docs/shapes/reference/domain/) |
| `ccDomain` | [`domain[]`](/docs/shapes/reference/domain/) |
| `tag` | [`tag[]`](/docs/shapes/reference/tag/) |

## Inherited

From [`message`](/docs/shapes/reference/message/):

| Field | Type |
|---|---|
| `isOutgoing` | `boolean` |

| Relation | Target |
|---|---|
| `inConversation` | [`conversation`](/docs/shapes/reference/conversation/) |
| `platform` | [`product`](/docs/shapes/reference/product/) |
| `repliesTo` | [`message`](/docs/shapes/reference/message/) |
| `toolCalls` | [`tool_call[]`](/docs/shapes/reference/tool_call/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[RFC 5322 (Internet Message Format)](https://datatracker.ietf.org/doc/html/rfc5322)** — Supersedes RFC 2822. Our messageId/inReplyTo/references/replyTo map directly to Message-ID/In-Reply-To/References/Reply-To headers; toRaw/ccRaw/bccRaw are the literal header values.
- **[RFC 2369 + RFC 8058 (List headers, one-click unsubscribe)](https://datatracker.ietf.org/doc/html/rfc2369)** — Our unsubscribe/unsubscribeOneClick/listId are List-Unsubscribe/List-Unsubscribe-Post/List-ID. RFC 8058 defines the one-click POST semantics.
- **[Gmail API Message resource](https://developers.google.com/gmail/api/reference/rest/v1/users.messages)** — Practical API mirror. Our sizeEstimate and isUnread/isStarred/isDraft/isSent/isTrash/isSpam correspond to Gmail's sizeEstimate and labelIds (UNREAD, STARRED, DRAFT, SENT, TRASH, SPAM).

## Skills that produce this shape

- [mimestream](/docs/skills/reference/comms/mimestream/) — `list_emails`, `search_emails`, `get_email`
- [gmail](/docs/skills/reference/comms/gmail/) — `list_email_stubs`, `list_emails`, `search_emails`, `list_drafts`, `get_email`, `get_draft`, `send_email`, `reply_email`, `forward_email`, `modify_email`, `trash_email`, `untrash_email`, `create_draft`, `update_draft`, `send_draft`
