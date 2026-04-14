---
title: person
description: "A real human. People are actors — they can own accounts, hold roles, attend meetings."
sidebar:
  label: person
---

A real human. People are actors — they can own accounts, hold roles, attend meetings.
Resolved from contacts, message senders, meeting attendees, etc.

Example sources: Apple Contacts, WhatsApp, PostHog, iMessage (inferred from handles)

| Metadata | Value |
|---|---|
| **Plural** | `people` |
| **Subtitle field** | `about` |
| **Also** | [`actor`](/docs/shapes/reference/actor/) |

## Fields

| Field | Type |
|---|---|
| `firstName` | `string` |
| `lastName` | `string` |
| `middleName` | `string` |
| `nickname` | `string` |
| `birthday` | `datetime` |
| `notes` | `text` |
| `gender` | `string` |
| `about` | `text` |
| `joinedDate` | `datetime` |
| `lastActive` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `accounts` | [`account[]`](/docs/shapes/reference/account/) |
| `roles` | [`role[]`](/docs/shapes/reference/role/) |
| `location` | [`place`](/docs/shapes/reference/place/) |
| `website` | [`website`](/docs/shapes/reference/website/) |

## Inherited

From [`actor`](/docs/shapes/reference/actor/):

| Field | Type |
|---|---|
| `actorType` | `string` |

## Skills that produce this shape

- [goodreads](/docs/skills/reference/media/goodreads/) — `get_author`, `get_person`
- [goodreads](/docs/skills/reference/media/goodreads/) — `search_people`, `list_friends`, `resolve_email`, `list_following`, `list_followers`
- [google-contacts](/docs/skills/reference/productivity/google-contacts/) — `list_contacts`, `search_contacts`
- [google-contacts](/docs/skills/reference/productivity/google-contacts/) — `get_contact`, `create_contact`, `update_contact`
- [whatsapp](/docs/skills/reference/comms/whatsapp/) — `op_list_persons`
- [posthog](/docs/skills/reference/web/posthog/) — `list_persons`, `search_persons`
- [posthog](/docs/skills/reference/web/posthog/) — `get_person`
