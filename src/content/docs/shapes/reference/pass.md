---
title: pass
description: "A fixed-quantity right-of-access — a bundle of entries, a multi-day"
sidebar:
  label: pass
---

A fixed-quantity right-of-access — a bundle of entries, a multi-day
window, a day-pass, a ride voucher, a 10-class punch card, a
concert ticket. Anything with a quantifiable claim count and a
consumption lifecycle (active → depleted / expired / cancelled).

Distinct from `membership`: a membership is open-ended and often
recurring. A pass is finite — it depletes, expires, or both. A
membership may *grant* passes (e.g. "your annual gives you 24 guest
passes a year").

Distinct from `invitation`: an invitation confers the *right to
join* something; a pass confers the *right to use* something that
may have already been granted.

Distinct from `offer`: an offer is pre-purchase ("buy a 10-class
pack for $150"); a pass is post-purchase ("you have 7 classes
remaining on this pack").

Covers: gym class packs, yoga punch cards, day passes, season
tickets (a pass bundle), concert tickets, transit passes
(single-ride or period), ski lift tickets, guest passes bundled
with a membership.

Identity: [at, id] — one pass per (namespace, platform id).
Standard fields inherited: id, name, url, image, published, content.
published = purchasedDate.
name = human-readable pass type ("Fitness 10-Pack", "Day Pass",
"Section 109, Row 12").

| Metadata | Value |
|---|---|
| **Plural** | `passes` |
| **Subtitle field** | `status` |
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
| `status` | `string` |
| `purchasedDate` | `datetime` |
| `startEffectiveDate` | `datetime` |
| `endEffectiveDate` | `datetime` |
| `quantity` | `integer` |
| `purchasedQuantity` | `integer` |
| `useCount` | `integer` |
| `isAllDayPass` | `boolean` |
| `depletedDate` | `datetime` |
| `price` | `number` |
| `currency` | `string` |
| `ticketNumber` | `string` |
| `nameOnTicket` | `string` |
| `seatAssignment` | `string` |
| `boardingGroup` | `string` |
| `ticketClass` | `string` |
| `gate` | `string` |
| `terminal` | `string` |
| `checkinStatus` | `string` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `account` | [`account`](/shapes/reference/account/) |
| `holder` | [`person`](/shapes/reference/person/) |
| `grantedBy` | [`membership`](/shapes/reference/membership/) |
| `type` | [`product`](/shapes/reference/product/) |
| `location` | [`place`](/shapes/reference/place/) |
| `for` | [`leg`](/shapes/reference/leg/) |
| `reservation` | [`reservation`](/shapes/reference/reservation/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Ticket](https://schema.org/Ticket)** — schema.org's peer for a claim-check right-of-entry. Our purchasedDate = issuedAt; holder = underName; price matches directly. Ticket is event-bound; we generalize to any right-of-use.
- **[Mindbody Services (pricing options)](https://developers.mindbodyonline.com/PublicDocumentation/V6)** — Gym-industry reference. Our quantity/purchasedQuantity/ useCount/depletedDate are lifted from Mindbody's ClientService.Remaining / Count / DateCompleted.
- **[GTFS fare rules / IATA fare basis](https://gtfs.org/documentation/schedule/reference/#fare_productstxt)** — Transit-pass vocabulary: single-ride, day-pass, period-pass all fit `isAllDayPass` + `startEffectiveDate` + `endEffectiveDate`.

## Skills that produce this shape

- [united](/skills/reference/logistics/united/) — `register_seats`
- [austin-boulder-project](/skills/reference/fitness/austin-boulder-project/) — `get_my_passes`
