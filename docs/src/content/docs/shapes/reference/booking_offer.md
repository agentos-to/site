---
title: booking_offer
description: "A signed, itemized, fully-priced commitment presented to a human for"
sidebar:
  label: booking_offer
---

A signed, itemized, fully-priced commitment presented to a human for
final approval before it becomes irreversible. The last artifact shown
to the user: "here is the exact thing, the exact price, the exact
card — do you approve? You have 5 minutes."

The pre-commit review object. Generic across domains:
- flight round-trip (this session's driving example)
- hotel stay checkout
- concert / event ticket purchase
- restaurant reservation with prepay
- rental car hold with deposit
- meal delivery order just before placing
- crypto invoice (CoinGate-style)
All share the same pre-commit moment: priced, itemized, assigned to a
buyer, pending explicit human approval, with a short TTL.

Lifecycle:
offer          -> "flights $412, valid 15 min"        (search result)
booking_offer  -> "flights $412 + $78 tax, Joe,       (review page)
Visa ****4242, expires 5 min"
reservation    -> "PNR ABC123, confirmed"             (post-commit)
transaction    -> "$490 charged to ****4242"          (post-charge)

Distinct from `offer`:
offer is anonymous pricing (pre-purchase price advertisement); a
booking_offer has chosen passengers, chosen payment, itemized
taxes, and a signature the provider can verify on commit.

Distinct from `reservation`:
no PNR / confirmation number exists yet, no charge has happened,
can simply expire with no consequences (reservations can't).

Why sign it:
An agent orchestrating a browser session can lie ("user confirmed")
to the provider. A signed booking_offer lets us verify on submit
that the exact shape the user approved matches what we're about to
commit. Tampering breaks the signature. Inspired by WebAuthn's
clientDataJSON: the RP signs (challenge, origin, type); we sign
(cartId, itineraryHash, total, expiresAt).

Why expire:
Prices drift, inventory churns, cards get blocked. Providers give
the agent a short window (typically 5-20 min) in which the quoted
price is guaranteed. After expiresAt, re-prepare.

Domain-specific data lives on the relations, not on this shape:
- seat assignments, aircraft, fare basis → flight / trip / pass
- hotel room type, bed config → reservation / pass
- event seat section → pass
booking_offer itself stays domain-neutral: it's a priced commitment.

| Metadata | Value |
|---|---|
| **Plural** | `booking_offers` |
| **Subtitle field** | `totalAmount` |
| **Identity** | `at`, `cartId` |

## Fields

| Field | Type |
|---|---|
| `cartId` | `string` |
| `referenceNumber` | `string` |
| `status` | `string` |
| `preparedAt` | `datetime` |
| `presentedAt` | `datetime` |
| `approvedAt` | `datetime` |
| `expiresAt` | `datetime` |
| `currency` | `string` |
| `baseAmount` | `number` |
| `taxAmount` | `number` |
| `feesAmount` | `number` |
| `totalAmount` | `number` |
| `itineraryHash` | `string` |
| `signature` | `string` |
| `signatureAlg` | `string` |
| `signedBy` | `string` |
| `checkoutUrl` | `url` |
| `confirmEndpoint` | `url` |
| `isRefundable` | `boolean` |
| `isChangeable` | `boolean` |
| `hasVoidWindow` | `boolean` |
| `voidWindowEndsAt` | `datetime` |
| `conditions` | `json` |
| `blob` | `string` |
| `review` | `string` |
| `contactEmail` | `string` |
| `contactPhone` | `string` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `derivedFrom` | [`offer`](/shapes/reference/offer/) |
| `trips` | [`trip[]`](/shapes/reference/trip/) |
| `reservedItems` | [`pass[]`](/shapes/reference/pass/) |
| `buyers` | [`person[]`](/shapes/reference/person/) |
| `guests` | [`person[]`](/shapes/reference/person/) |
| `underName` | [`person`](/shapes/reference/person/) |
| `paymentMethod` | [`payment_method`](/shapes/reference/payment_method/) |
| `billingAddress` | [`place`](/shapes/reference/place/) |
| `fares` | [`fare[]`](/shapes/reference/fare/) |
| `taxLines` | [`tax_line[]`](/shapes/reference/tax_line/) |
| `account` | [`account`](/shapes/reference/account/) |
| `membership` | [`membership`](/shapes/reference/membership/) |
| `broker` | [`actor`](/shapes/reference/actor/) |
| `becameReservation` | [`reservation`](/shapes/reference/reservation/) |
| `becameTransaction` | [`transaction`](/shapes/reference/transaction/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Duffel Offers API (pre-Order priced shape)](https://duffel.com/docs/api/offers/schema)** — Duffel's Offer is the "priced, held, about-to-become-an-order" state. Our baseAmount/taxAmount/totalAmount/currency map to Duffel's base_amount/tax_amount/total_amount/total_currency; expiresAt = offer.expires_at. Duffel rolls taxes into a single aggregate — we split them into tax_line[] nodes.
- **[IATA NDC OfferPriceRQ / OfferPriceRS](https://developer.iata.org/en/ndc/)** — NDC's OfferPrice is the mandatory "price this exact shape with these exact passengers" step between Shop and OrderCreate. Our guests[] mirror NDC's PaxList; taxLines[] mirror Taxes/ TaxSummary; signature mirrors OfferPriceRS's ShoppingResponseID that the airline expects back on OrderCreateRQ.
- **[Stripe Checkout Session](https://docs.stripe.com/api/checkout/sessions/object)** — Canonical "about-to-charge" object. Our cartId ≈ session.id; expiresAt ≈ session.expires_at; totalAmount ≈ session.amount_total; paymentMethod relation mirrors session.payment_method. Stripe assumes line_item shape; we use domain-specific relations (trips/reservedItems) instead.
- **[Shopify Draft Order](https://shopify.dev/docs/api/admin-graphql/latest/objects/DraftOrder)** — Shopify's non-binding pre-order — validates the "cart with a reference number that can be invoiced and converted" pattern. Our referenceNumber ≈ DraftOrder.name; becameReservation / becameTransaction mirror DraftOrder -> Order conversion.
- **[WebAuthn clientDataJSON + signed assertion](https://www.w3.org/TR/webauthn-3/)** — Precedent for "the thing the user saw is what got signed." WebAuthn signs (challenge, origin, type); we sign (cartId, itineraryHash, total, expiresAt). Our itineraryHash plays the role of WebAuthn's challenge — a commitment the verifier can match against the submitted shape.
- **[CoinGate Invoice (short-TTL priced blob)](https://developer.coingate.com/reference/order-statuses)** — Validates the short-TTL pattern outside airlines. CoinGate invoices carry id, price locked ~20 min, and status (new, pending, paid, expired, canceled). Our status enum matches — pre-commit objects need expiry as a first-class terminal.
- **[schema.org/Order + schema.org/Invoice](https://schema.org/Order)** — schema.org models Offer -> Order -> Invoice. booking_offer sits between Offer and Order — a priced, itemized, signed proposal awaiting explicit human commit. Our baseAmount + taxAmount + totalAmount align with UBL 2.1 LegalMonetaryTotal.

## Skills that produce this shape

- [united](/skills/reference/logistics/united/) — `prepare_booking`
