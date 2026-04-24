---
title: reservation
description: "A forward commitment to a future thing — a flight booking, a hotel"
sidebar:
  label: reservation
---

A forward commitment to a future thing — a flight booking, a hotel
stay, a dinner reservation, a rental car hold. Distinct from `order`
(commerce of goods) and `event` (a thing that happens).

A reservation has three defining properties:
1. A future start (and usually end) — you commit NOW to be THERE.
2. Consequences for not showing up — fees, forfeited fare, status
penalties. This is what separates a reservation from a casual plan.
3. An identity independent of payment — the PNR exists before the
ticket is issued and can survive ticket voiding / refund.

Design drawn from:
- Duffel / IATA NDC — the canonical top-level `Order` for flight
bookings. We name it `reservation` because Duffel's `Order`
conflates too much with our existing `order` shape (goods).
- schema.org/Reservation — vocabulary (reservationType, status,
reservedTicket, reservationFor) and the per-type specializations
(FlightReservation, LodgingReservation, FoodEstablishmentReservation).
- ActivityStreams — the principle that commitment lifecycle is best
captured as a stream of activities (booked, held, checked_in,
rebooked, cancelled) with timestamps and actors, rather than as a
single lossy enum. `status` gives the current state; the `activity`
back-edges give the history.

Multi-passenger semantics:
One PNR, N passengers, shared across flights/stays. `passengers` is
a simple `person[]` relation — no `traveler` join shape. Per-ticket
data (name-on-ticket, seat, ticket number) lives on `pass` (one per
passenger per flight/segment).

Payment:
`totalAmount`/`currency` capture the top-level price the reservation
is committed to. For commerce detail (fare breakdown, transactions,
payment method), point `order` at a separate `order` record. A
restaurant reservation has no `order`. A flight reservation has both
`reservation` (the PNR) and `order` (the itemized fare + transaction).

Consequences (refund/change policy):
`conditions` is a JSON blob for now — fare rules are a bottomless
pit and every carrier encodes them differently. Flatten to structured
fields (cancelFee, changeFee, voidWindow...) only once we're reasoning
over them in the UI.

| Metadata | Value |
|---|---|
| **Plural** | `reservations` |
| **Subtitle field** | `reservationType` |
| **Identity** | `at`, `reservationId` |

## Fields

| Field | Type |
|---|---|
| `reservationType` | `string` |
| `reservationId` | `string` |
| `status` | `string` |
| `bookingType` | `string` |
| `bookingTime` | `datetime` |
| `modifiedTime` | `datetime` |
| `startTime` | `datetime` |
| `endTime` | `datetime` |
| `partySize` | `integer` |
| `totalAmount` | `number` |
| `baseAmount` | `number` |
| `taxAmount` | `number` |
| `currency` | `string` |
| `checkinUrl` | `url` |
| `conditions` | `json` |
| `voidWindowEndsAt` | `datetime` |
| `availableActions` | `string[]` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `trips` | [`trip[]`](/shapes/reference/trip/) |
| `location` | [`place`](/shapes/reference/place/) |
| `event` | [`event`](/shapes/reference/event/) |
| `passengers` | [`person[]`](/shapes/reference/person/) |
| `underName` | [`person`](/shapes/reference/person/) |
| `account` | [`account`](/shapes/reference/account/) |
| `broker` | [`actor`](/shapes/reference/actor/) |
| `programMembership` | [`membership`](/shapes/reference/membership/) |
| `order` | [`order`](/shapes/reference/order/) |
| `tickets` | [`pass[]`](/shapes/reference/pass/) |
| `derivedFrom` | [`offer`](/shapes/reference/offer/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Reservation](https://schema.org/Reservation)** — Base vocabulary: reservationFor, reservationId, reservationStatus, reservedTicket, underName, bookingTime, modifiedTime, totalPrice, priceCurrency. We fold FlightReservation / LodgingReservation / FoodEstablishmentReservation into a single shape with a reservationType discriminator (AgentOS convention — see `trip.tripType`, `event.eventType`). Flight-specific fields (boardingGroup, seat) live on pass, not here.
- **[schema.org/ReservationStatusType](https://schema.org/ReservationStatusType)** — Extended beyond schema.org's ConfirmedCancelledHoldPending set to add `no_show` and `completed` — values that matter for post-hoc reasoning but schema.org lacks.
- **[Duffel Orders API](https://duffel.com/docs/api/v2/orders)** — Canonical flight-booking top-level entity. Our `reservationId` = booking_reference; `availableActions` = available_actions; `voidWindowEndsAt` = void_window_ends_at; `conditions` = conditions (change_before_departure, refund_before_departure). Duffel names the entity `Order`; we chose `reservation` to free up `order` for pure-commerce semantics.
- **[IATA NDC OrderViewRS](https://www.iata.org/en/programs/airline-distribution/retailing/ndc/)** — NDC normalizes passengers to a top-level PaxList referenced by ID. Our graph gets the same effect with `passengers: person[]` — people are first-class nodes and the same `person` can appear on many reservations. Services (seat, baggage, meal) live on `pass`.
- **[ActivityStreams 2.0 (Invite / Accept / Leave / Reject)](https://www.w3.org/TR/activitystreams-vocabulary/)** — Commitment lifecycle is an append-only stream of activities (booked, held, checked_in, rebooked, cancelled) rather than a single lossy enum. We use `status` for the snapshot and rely on back-edges from `activity` nodes for the history — the same pattern FEP-8a8e recommends for ActivityPub event-side state.
- **[FEP-8a8e Event interop](https://w3id.org/fep/8a8e)** — Splits supply-side status (on the event/flight) from demand-side status (on the attendee/passenger). We mirror this by keeping `status` on reservation (passenger-side) separate from any cancellation/delay state on the `flight` or `trip` itself.
- **[Valueflows / REA — Commitment](https://www.valueflo.ws/concepts/flows/)** — REA accounting framing: a reservation IS a commitment with provider, receiver, resourceConformsTo, quantity, and time window. Useful lens for future extension (hotel nights, car rental days).

## Skills that produce this shape

- [united](/skills/reference/logistics/united/) — `list_trips`, `get_cart`, `select_flight`, `register_traveler`
