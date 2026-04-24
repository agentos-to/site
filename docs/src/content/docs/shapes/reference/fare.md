---
title: fare
description: "The priced class-of-service unit for a transport journey — the BASE"
sidebar:
  label: fare
---

The priced class-of-service unit for a transport journey — the BASE
PRICE per passenger before taxes and fees. Works for any mode that
has a notion of "fare class":
- airline: Basic Economy / Economy / Business / First (with IATA
fareBasisCode identifying the exact rule)
- rail: Coach / Business / First / Sleeper / Rail Pass
- bus: Standard / Premium / Rapid
- transit: zone 1 / zone 2 / off-peak / peak
- taxi/rideshare: UberX / Uber Black / Share (fareAmount lives on
`trip` instead — one-off, not a class)
- ferry: Walk-on / Vehicle / Cabin

Why this is its own shape:
A booking price is not atomic — it decomposes into (base fare) +
(N tax/fee lines). The base fare itself has structure: a provider
rule identifier, a branded product name, a class of service, and
policy flags (refundable, changeable). Modeling fare as its own
node lets booking_offer / reservation all reference the same fare
identity, and lets N `tax_line` nodes hang off it via back-edges.

Relationship to adjacent shapes:
- `offer` / `booking_offer` — purchasable bundle; carries 1+ fare
- `reservation` — post-booking; same fare persists as priced ticket
- `pass` — per-passenger-per-leg boarding credential; its
`ticketClass` is the single-letter projection of `bookingCode`
(airline), or just the class name (rail/bus)
- `tax_line` — N tax/fee items that price alongside this fare

Identifier (provider-opaque rule code):
Airlines use IATA fare basis codes (LAA0AQBN, etc.) — first char is
the RBD/booking class; remainder is the airline's ATPCO pointer.
Rail uses operator-specific tier codes. Transit uses zone labels.
We store whatever the provider gave us in `identifier`; `bookingCode`
is the single-letter form airlines + some rail systems use.

| Metadata | Value |
|---|---|
| **Plural** | `fares` |
| **Subtitle field** | `fareFamily` |
| **Identity** | `at`, `identifier` |

## Fields

| Field | Type |
|---|---|
| `identifier` | `string` |
| `bookingCode` | `string` |
| `productType` | `string` |
| `fareFamily` | `string` |
| `class` | `string` |
| `basePrice` | `number` |
| `currency` | `string` |
| `passengerType` | `string` |
| `milesEarned` | `integer` |
| `pointsEarned` | `integer` |
| `components` | `integer` |
| `refundable` | `boolean` |
| `changeable` | `boolean` |
| `restrictions` | `string[]` |
| `conditions` | `json` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `for` | [`trip`](/shapes/reference/trip/) |
| `legs` | [`leg[]`](/shapes/reference/leg/) |
| `offer` | [`offer`](/shapes/reference/offer/) |
| `reservation` | [`reservation`](/shapes/reference/reservation/) |
| `taxLines` | [`tax_line[]`](/shapes/reference/tax_line/) |
| `earnsInto` | [`membership`](/shapes/reference/membership/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[IATA Fare Basis Code / ATPCO filings](https://en.wikipedia.org/wiki/Fare_basis_code)** — Airline canonical. First char = RBD/booking class (our `bookingCode`); remainder = airline-proprietary pointer into ATPCO-filed fare rules (our `identifier` as opaque string, `conditions` for the rule blob). Codes are 3-8 chars; we don't parse beyond the first char.
- **[IATA NDC FareDetail / FareComponent](https://developer.iata.org/en/ndc/)** — NDC's FareDetail.FareComponent carries FareBasis.FareBasisCode, FareBasis.RBD, Price.BaseAmount, FareRules.Penalty, and CabinType.CabinTypeCode. Our identifier/bookingCode/basePrice/ class/refundable map directly.
- **[Duffel Offer Slice / fare_basis_code](https://duffel.com/docs/api/v2/offers)** — Duffel surfaces fare_basis_code on each slice's segments along with cabin_class, cabin_class_marketing_name (our fareFamily), and passenger-level base_amount. Our basePrice = base_amount; class = cabin_class; fareFamily = cabin_class_marketing_name.
- **[Amtrak / Rail Europe fare types](https://www.amtrak.com/routes/fares)** — Non-airline generalization. Amtrak fares are Saver / Value / Flexible / Premium / Business / First / Acela First / Acela First Refundable — their tier codes fit `identifier`; their names fit `fareFamily`; their rules fit `refundable`/ `changeable`/`restrictions`.
- **[GTFS fare_products.txt (transit)](https://gtfs.org/documentation/schedule/reference/#fare_productstxt)** — Open transit standard for fare products. Their fare_product_id = our identifier; fare_product_name = fareFamily; amount = basePrice; currency_code = currency. rider_category matches passengerType (adult/child/senior/student).
- **[schema.org/Offer price + FlightReservation](https://schema.org/FlightReservation)** — schema.org's Offer.price + Offer.priceCurrency align with our basePrice + currency. schema.org has no fare-basis concept; NDC and GTFS fill that gap.
