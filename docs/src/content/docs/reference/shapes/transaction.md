---
title: transaction
description: "A financial transaction — credit card charge, bank transfer, etc."
sidebar:
  label: transaction
---

A financial transaction — credit card charge, bank transfer, etc.

Example sources: Chase, Copilot Money

| | |
|---|---|
| **Plural** | `transactions` |
| **Subtitle field** | `category` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `amount` | `number` |
| `currency` | `string` |
| `balance` | `number` |
| `category` | `string` |
| `postingDate` | `datetime` |
| `pending` | `boolean` |
| `recurring` | `boolean` |
| `notes` | `string` |
| `type` | `string` |
| `details` | `json` |

## Relations

| Relation | Target |
|---|---|
| `account` | [`account`](/docs/reference/shapes/account/) |

## Skills that produce this shape

- [chase](/docs/reference/skills/chase/) — `get_transactions`
- [copilot-money](/docs/reference/skills/copilot-money/) — `fetch_transactions`
