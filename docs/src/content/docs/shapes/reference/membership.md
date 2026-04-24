---
title: membership
description: "A time-bounded right-of-belonging granted by an organization."
sidebar:
  label: membership
---

A time-bounded right-of-belonging granted by an organization.
The universal "you are part of X" primitive — gym memberships,
streaming subscriptions, coworking plans, AAA, professional bodies,
citizenships, religious affiliations, credit-card rewards status,
club memberships, union dues, library cards.

A membership answers three questions: who holds it (member), what
organization grants it (at), and what the current status is (status).
Plus the time window (startEffectiveDate / endEffectiveDate) and —
for commercial memberships — the billing cadence.

Distinct from `pass`: a membership is open-ended (until cancelled /
expired / revoked). A pass is a fixed bundle (10 classes, 30 days,
1 ride). A membership may *grant* passes.

Distinct from `offer`: an offer is pre-purchase ("join our gym for
$95/mo"); a membership is post-purchase ("you are a gym member").

Distinct from `role`: a role is held at an organization ("CTO at
Acme"). A membership is belonging ("Annual member of SF MoMA"). An
employee has a role; a season-ticket holder has a membership. Both
can coexist on the same (person, organization).

Subscriptions fold in cleanly: Spotify/Netflix/Anthropic all fit —
the plan is a product, the billing is recurring, status tracks
active/cancelled/past_due. Same shape.

Non-commercial memberships work too: `billingType` is null, `price`
is 0 or null, the lifecycle fields (startEffectiveDate etc.) and
status carry all the meaning.

Identity: [at, id] — one membership per (namespace, platform id).
Standard fields inherited: id, name, url, image, published, content.
published = startEffectiveDate (when the membership began).
name = human-readable tier or plan ("Annual Recurring: 21+ [ATX]",
"Spotify Premium Family", "US Citizen", "AAA Plus").
content = full description from the provider (often rich markdown).

| Metadata | Value |
|---|---|
| **Plural** | `memberships` |
| **Subtitle field** | `status` |
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
| `status` | `string` |
| `tier` | `string` |
| `startEffectiveDate` | `datetime` |
| `endEffectiveDate` | `datetime` |
| `nextBillDate` | `datetime` |
| `autoRenew` | `boolean` |
| `price` | `number` |
| `currency` | `string` |
| `billingType` | `string` |
| `useCount` | `integer` |
| `guestPassQuantity` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `account` | [`account`](/shapes/reference/account/) |
| `member` | [`person`](/shapes/reference/person/) |
| `plan` | [`product`](/shapes/reference/product/) |
| `location` | [`place`](/shapes/reference/place/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/ProgramMembership](https://schema.org/ProgramMembership)** — schema.org's canonical membership type. Our member = member; plan ≈ programName/membershipNumber; at ≈ hostingOrganization. ProgramMembership covers gym, loyalty, society memberships without requiring a billing cycle — matches our non-commercial framing.
- **[schema.org/Subscription](https://schema.org/Subscription)** — Streaming/SaaS subscriptions fit this shape — one model covers gym memberships and Spotify Premium. billingType maps to billingPeriod; autoRenew maps directly.
- **[Stripe Subscriptions API](https://docs.stripe.com/api/subscriptions)** — Practical API mirror for commercial memberships. Our status values (active/paused/cancelled/past_due) mirror Stripe Subscription.status. nextBillDate ≈ current_period_end.
- **[Mindbody Contracts/Memberships](https://developers.mindbodyonline.com/PublicDocumentation/V6)** — Gym-industry API. Our useCount, guestPassQuantity, startEffectiveDate / endEffectiveDate are lifted from Mindbody's Membership record shape.
- **[FOAF member / membershipClass](http://xmlns.com/foaf/spec/#term_member)** — Social-web vocabulary for "X is a member of Y". Our member ↔ at edge mirrors foaf:member; our tier ≈ foaf:membershipClass.

## Skills that produce this shape

- [united](/skills/reference/logistics/united/) — `get_mileageplus`
- [austin-boulder-project](/skills/reference/fitness/austin-boulder-project/) — `get_my_memberships`
