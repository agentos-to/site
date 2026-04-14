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

| Metadata | Value |
|---|---|
| **Plural** | `financial_accounts` |
| **Subtitle field** | `last4` |
| **Also** | [`account`](/docs/shapes/reference/account/) |

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

From [`account`](/docs/shapes/reference/account/):

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
| `followers` | [`account[]`](/docs/shapes/reference/account/) |
| `follows` | [`account[]`](/docs/shapes/reference/account/) |
| `owner` | [`person`](/docs/shapes/reference/person/) |
| `platform` | [`product`](/docs/shapes/reference/product/) |
