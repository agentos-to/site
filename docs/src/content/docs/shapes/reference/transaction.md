---
title: transaction
description: "A financial transaction — credit card charge, bank transfer, etc."
sidebar:
  label: transaction
---

A financial transaction — credit card charge, bank transfer, etc.

| Metadata | Value |
|---|---|
| **Plural** | `transactions` |
| **Subtitle field** | `category` |
| **Identity** | `at`, `id` |
| **Also** | [`event`](/shapes/reference/event/) |

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

## Inherited

From [`event`](/shapes/reference/event/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `distinctId` | `string` |
| `endDate` | `datetime` |
| `icalUid` | `string` |
| `properties` | `json` |
| `recurrence` | `string[]` |
| `showAs` | `string` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `status` | `string` |
| `timezone` | `string` |
| `visibility` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[OFX (Open Financial Exchange) STMTTRN](https://financialdataexchange.org/ofx)** — Direct source. Our amount/type/postingDate/balance map to STMTTRN TRNAMT/TRNTYPE/DTPOSTED/BALAMT.
- **[ISO 20022 payments messaging](https://www.iso20022.org/)** — Modern bank-messaging. Our currency = Ccy; category ≈ purpose code; details ≈ RemittanceInformation.
- **[Plaid Transactions API](https://plaid.com/docs/api/products/transactions/)** — Practical mirror. Our category/pending/recurring/notes match Plaid's category/pending/personal_finance_category/name fields.

## Skills that produce this shape

- [copilot-money](/skills/reference/finance/copilot-money/) — `fetch_transactions`
