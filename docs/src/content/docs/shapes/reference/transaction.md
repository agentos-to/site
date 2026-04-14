---
title: transaction
description: "A financial transaction — credit card charge, bank transfer, etc."
sidebar:
  label: transaction
---

A financial transaction — credit card charge, bank transfer, etc.

Example sources: Chase, Copilot Money

| Metadata | Value |
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
| `account` | [`account`](/docs/shapes/reference/account/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[OFX (Open Financial Exchange) STMTTRN](https://financialdataexchange.org/ofx)** — Direct source. Our amount/type/postingDate/balance map to STMTTRN TRNAMT/TRNTYPE/DTPOSTED/BALAMT.
- **[ISO 20022 payments messaging](https://www.iso20022.org/)** — Modern bank-messaging. Our currency = Ccy; category ≈ purpose code; details ≈ RemittanceInformation.
- **[Plaid Transactions API](https://plaid.com/docs/api/products/transactions/)** — Practical mirror. Our category/pending/recurring/notes match Plaid's category/pending/personal_finance_category/name fields.

## Skills that produce this shape

- [chase](/docs/skills/reference/finance/chase/) — `get_transactions`
- [copilot-money](/docs/skills/reference/finance/copilot-money/) — `fetch_transactions`
