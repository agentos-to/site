---
title: account
description: "A user's presence on a platform — their GitHub handle, Gmail address, etc."
sidebar:
  label: account
---

A user's presence on a platform — their GitHub handle, Gmail address, etc.
Created by most skills. Links a person to their platform-specific identity.

Identity: [issuer, identifier] — one node per platform+handle combo.
issuer = platform domain (e.g. "github.com", "gmail.com")
identifier = platform-specific handle (e.g. "joecontini", "joe@adavia.com")

Example sources: GitHub, Gmail, WhatsApp, iMessage, Reddit, Hacker News, PostHog

| | |
|---|---|
| **Plural** | `accounts` |
| **Subtitle field** | `identifier` |
| **Identity** | `issuer`, `identifier` |

## Fields

| Field | Type |
|---|---|
| `issuer` | `string` |
| `identifier` | `string` |
| `handle` | `string` |
| `displayName` | `string` |
| `email` | `string` |
| `phone` | `string` |
| `bio` | `text` |
| `accountType` | `string` |
| `color` | `string` |
| `isActive` | `boolean` |
| `joinedDate` | `datetime` |
| `lastActive` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `platform` | [`product`](/docs/reference/shapes/product/) |
| `owner` | [`person`](/docs/reference/shapes/person/) |
| `follows` | [`account[]`](/docs/reference/shapes/account/) |
| `followers` | [`account[]`](/docs/reference/shapes/account/) |

## Used as a base by

- [`financial_account`](/docs/reference/shapes/financial_account/)

## Skills that produce this shape

- [goodreads](/docs/reference/skills/goodreads/) — `get_profile`
- [moltbook](/docs/reference/skills/moltbook/) — `me_account`, `get_account`
- [amazon](/docs/reference/skills/amazon/) — `whoami`
- [chase](/docs/reference/skills/chase/) — `check_session`
- [chase](/docs/reference/skills/chase/) — `get_accounts`
- [copilot-money](/docs/reference/skills/copilot-money/) — `load_accounts`
- [greptile](/docs/reference/skills/greptile/) — `list_members`
