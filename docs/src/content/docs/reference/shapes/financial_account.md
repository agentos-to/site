---
title: financial_account
description: "A financial account — bank account, credit card, or investment account."
sidebar:
  label: financial_account
---

A financial account — bank account, credit card, or investment account.
Inherits platform identity fields from account. Financial-specific fields
(balance, credit limit, card type) live here, not on the generic account shape.

Example sources: Chase, Copilot Money

| | |
|---|---|
| **Plural** | `financial_accounts` |
| **Subtitle field** | `last4` |
| **Also** | [`account`](/docs/reference/shapes/account/) |

## Fields

| Field | Type |
|---|---|
| `accountNumber` | `string` |
| `routingNumber` | `string` |
| `last4` | `string` |
| `balance` | `number` |
| `available` | `number` |
| `creditLimit` | `number` |
| `minimumPayment` | `number` |
| `paymentDueDate` | `datetime` |
| `cardType` | `string` |
| `expiresAt` | `datetime` |
| `interestRate` | `number` |

## Inherited

From [`account`](/docs/reference/shapes/account/):

| Field | Type |
|---|---|
| `accountType` | `string` |
| `bio` | `text` |
| `color` | `string` |
| `displayName` | `string` |
| `email` | `string` |
| `handle` | `string` |
| `identifier` | `string` |
| `isActive` | `boolean` |
| `issuer` | `string` |
| `joinedDate` | `datetime` |
| `lastActive` | `datetime` |
| `phone` | `string` |

| Relation | Target |
|---|---|
| `followers` | [`account[]`](/docs/reference/shapes/account/) |
| `follows` | [`account[]`](/docs/reference/shapes/account/) |
| `owner` | [`person`](/docs/reference/shapes/person/) |
| `platform` | [`product`](/docs/reference/shapes/product/) |
