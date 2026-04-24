---
title: tax_line
description: "A single tax, fee, or surcharge line item on a priced commerce"
sidebar:
  label: tax_line
---

A single tax, fee, or surcharge line item on a priced commerce
transaction — one row of the itemized tax/fee breakdown. Any booking
/ order / invoice with N taxes has N tax_line nodes.

Applies broadly: airline ticket taxes, hotel occupancy taxes, rental
car airport fees, restaurant service charges, sales tax, VAT/GST, any
line item that the merchant itemizes separately from the base price.

Why one-node-per-line (rather than `taxes: json[]` on the parent):
1. A single tax can recur per segment / per night / per item. Each
occurrence has its own amount and binding — they're not
aggregable without losing information. (Airline: US
Transportation Tax fires once per leg. Hotel: occupancy tax
fires once per night.)
2. Agent UIs want to show the full breakdown, not a lump-sum
"taxes and fees: $61". Nodes give display, query, and
provenance.
3. Taxes are imposed by third parties (governments, facilities),
not the selling merchant. `imposedBy` makes the authority chain
first-class.

Common tax/fee codes by domain:
airline: US, ZP, XF, AY, YQ, YR (IATA ILTATF list)
hotel: occupancy tax, tourism levy, resort fee
rental car: concession recovery fee, airport access fee
rideshare: booking fee, airport surcharge
commerce: sales tax (state), VAT, GST

Kind (tax | fee | surcharge):
- tax       — government-imposed (US, ZP, AY, VAT, GST, sales tax)
- fee       — facility / service charge (XF, resort fee, concession)
- surcharge — merchant-imposed (YQ fuel surcharge, resort fee)
Matters for refundability: taxes on unflown tickets are often
refundable by law; merchant surcharges often are not.

| Metadata | Value |
|---|---|
| **Plural** | `tax_lines` |
| **Subtitle field** | `description` |
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
| `code` | `string` |
| `description` | `string` |
| `amount` | `number` |
| `currency` | `string` |
| `kind` | `string` |
| `nature` | `string` |
| `country` | `string` |
| `appliesToIndex` | `integer` |
| `refundable` | `boolean` |
| `merchantImposed` | `boolean` |
| `rate` | `number` |
| `taxableAmount` | `number` |
| `inclusive` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `appliesTo` | [`fare`](/shapes/reference/fare/) |
| `offer` | [`offer`](/shapes/reference/offer/) |
| `reservation` | [`reservation`](/shapes/reference/reservation/) |
| `segment` | [`leg`](/shapes/reference/leg/) |
| `imposedBy` | [`actor`](/shapes/reference/actor/) |
| `location` | [`place`](/shapes/reference/place/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[IATA List of Ticket and Airport Taxes and Fees (ILTATF)](https://www.iata.org/en/publications/store/list-of-ticket-and-airport-taxes-and-fees/)** — Canonical 1500+ entry registry of 2-char airline tax codes, grouped AT (airport), PC (passenger charge), ST (stamp), TT (ticket), MT (misc). Our `code` = ILTATF code when applicable; `nature` corresponds to ILTATF's grouping.
- **[IATA NDC Tax / TaxBreakdown element](https://developer.iata.org/en/ndc/)** — NDC's Price structure carries Taxes/Tax with TaxCode, CollectionPoint, CountryCode, Nature, Amount, Description. Our code/country/nature/amount/description map 1:1. NDC's Nature enum (security, fuel, facility, tax) informs our values.
- **[schema.org/UnitPriceSpecification + PriceComponentTypeEnumeration](https://schema.org/UnitPriceSpecification)** — Generic commerce. priceComponentType ("Tax"), valueAddedTaxIncluded (our `inclusive`), priceCurrency. Lightweight; we add code, country, `imposedBy` to cover the authority-chain gap.
- **[UBL 2.1 / Peppol BIS Billing 3.0 — TaxSubtotal / TaxCategory](https://docs.peppol.eu/poacc/billing/3.0/)** — European eInvoicing. TaxSubtotal carries TaxableAmount, TaxAmount, Percent, TaxCategory/TaxScheme (VAT/GST). Our taxableAmount/amount/rate/nature align directly.
- **[Stripe Invoice tax_amounts[]](https://docs.stripe.com/api/invoices/object)** — Stripe's line-item tax_amounts[] carries amount, inclusive, tax_rate, taxability_reason, taxable_amount. Our inclusive/ rate/taxableAmount match; jurisdiction/jurisdiction_level inspired the country + `imposedBy` split.
- **[Shopify Order tax_lines[]](https://shopify.dev/docs/api/admin-rest/latest/resources/order)** — Minimal commerce model: price, rate, title, channel_liable. Our amount/rate/description map 1:1. Shopify allows multiple tax_lines per line item with same title + different rates — same pattern we need (US Transportation Tax recurring per segment). We disambiguate via appliesToIndex.
- **[Avalara / TaxJar tax breakdown](https://developer.avalara.com/)** — Commerce tax engines. Jurisdiction hierarchy (country / state / county / city / special) and combined tax rate. Informs the `imposedBy: actor` relation for layered jurisdictions (hotel occupancy + tourism + state sales tax, each their own line).
