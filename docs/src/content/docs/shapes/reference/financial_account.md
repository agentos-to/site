---
title: financial_account
description: "A financial account — bank checking/savings, brokerage, crypto wallet, etc."
sidebar:
  label: financial_account
---

A financial account — bank checking/savings, brokerage, crypto wallet, etc.
Distinct from `account` (platform identity): one login can grant access to
many financial_accounts. A DBS login owns USD, SGD, and GBP accounts; each
is a separate financial_account node, accessed via the same login.

Identity is graph-native: (at, identifier). `at` is a relation to the
institution (Chase Bank, DBS, Coinbase) — an organization or product node.
`identifier` is typically the masked account number (or last4 if that's
all the provider shares). Relation-keyed identity means bank mergers
(First Republic → Chase) don't fragment the account; the edge moves, the
node persists.

| Metadata | Value |
|---|---|
| **Plural** | `financial_accounts` |
| **Subtitle field** | `last4` |
| **Identity** | `at`, `identifier` |

## Fields

| Field | Type |
|---|---|
| `identifier` | `string` |
| `accountId` | `string` |
| `accountNumber` | `string` |
| `routingNumber` | `string` |
| `last4` | `string` |
| `currency` | `string` |
| `accountType` | `string` |
| `balance` | `number` |
| `available` | `number` |
| `creditLimit` | `number` |
| `minimumPayment` | `number` |
| `paymentDueDate` | `datetime` |
| `cardType` | `string` |
| `expiresAt` | `datetime` |
| `interestRate` | `number` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `accessedVia` | [`account`](/shapes/reference/account/) |
| `owner` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[OFX (Open Financial Exchange)](https://financialdataexchange.org/ofx)** — Bank-feed canonical. Our accountNumber / routingNumber / balance / available map to OFX BANKACCTFROM / LEDGERBAL / AVAILBAL.
- **[ISO 20022 Financial Messaging](https://www.iso20022.org/)** — Modern bank-messaging standard. Our last4 / cardType / creditLimit / interestRate align with ISO 20022 Card / Account components.
- **[schema.org/BankAccount](https://schema.org/BankAccount)** — Our accountNumber ≈ accountId; balance / available are accountMinimumInflow / accountOverdraftLimit loosely; cardType fits schema.org/CreditCard.
- **[1Password Bank Account item](https://1password.com/)** — 1P's Bank Account category holds institution + account number + routing + type — same shape. Their Crypto Wallet and Credit Card are separate categories; we treat them as different `accountType` values on the same shape for now, splitting only if the field diversity forces it.

## Skills that produce this shape

- [copilot-money](/skills/reference/finance/copilot-money/) — `load_accounts`
