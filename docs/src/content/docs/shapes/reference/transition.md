---
title: transition
description: "An identity change — name, gender, religion, sports team, anything"
sidebar:
  label: transition
---

An identity change — name, gender, religion, sports team, anything
identity-shaped — recorded as a point-in-time event. The event captures
the post-change state using the same canonical field names as `birth`;
unfilled fields = "this transition didn't touch that field."

Per platform/README.md rule 1, the date the change took effect rides
on the event (`startDate`). The verb is `changed`:

joe —changed→ transition(givenName: "Joey", startDate: 2010-06-01)

Resolver projection: `person.givenName` walks both `born_in → birth`
and `changed → transition`, picks the latest by `startDate`, returns
the projected field. See `person.yaml` `derived:` block.

Same field set as `birth` (single source of vocabulary for name +
gender + nickname). Future identity axes (religion, race, pronoun,
sports-team affiliation) land here as new optional fields without
touching the resolver — `derived:` bindings on `person.yaml` add
matching `latest:` arms as new dimensions are introduced.

Not jurisdiction-flavoured. A transition may be a legal act (deed
poll, GRC, passport amendment), an administrative filing (Singapore
ICA Change of Particulars), or a non-legal self-identification (going
by a nickname, social-only gender change). The act's legal character,
if any, rides on links from this event to authority/document nodes —
out of scope V1.

| Metadata | Value |
|---|---|
| **Plural** | `transitions` |
| **Subtitle field** | `startDate` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `givenName` | `string` |
| `additionalName` | `string` |
| `familyName` | `string` |
| `honorificPrefix` | `string` |
| `honorificSuffix` | `string` |
| `legalName` | `string` |
| `maidenName` | `string` |
| `sortAs` | `string` |
| `nameOrder` | `string` |
| `phoneticGivenName` | `string` |
| `phoneticFamilyName` | `string` |
| `gender` | `string` |
| `nickname` | `string` |

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

| Relation | Target |
|---|---|
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `concerns` | [`person`](/shapes/reference/person/) |
| `created_by` | [`person`](/shapes/reference/person/) |
| `held_at` | [`place`](/shapes/reference/place/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `organized_by` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Event Sourcing (Fowler)](https://martinfowler.com/eaaDev/EventSourcing.html)** — Past-tense events as facts; entity state = fold over the event stream. `transition` is the past-tense event-node; the `latest:` resolver is the fold. Reuses canonical field names — no `new_*` prefix per the event-sourcing convention.
- **[Palantir Foundry — Action Log Objects](https://www.palantir.com/docs/foundry/announcements/2022-10/index.html)** — Palantir reifies every mutation as a queryable Action Log Object — same shape as our reified `transition` event. They type Actions per-mutation (`AssignEmployee` etc.); we collapse to one umbrella shape with optional fields for agent-OS ergonomics (operations not known in advance).
- **[IMO / GISIS maritime registry — particulars change](https://gisis.imo.org/public/default.aspx)** — 50-year-old domain proves the pattern: stable identifier (IMO number) + canonical property names + reified change events (name/flag/owner change). `Person.id` ↔ `Ship.imo`; `transition.gender` ↔ a `flag_change` on a ship.
- **[FHIR R5 HumanName.use + HumanName.period](https://hl7.org/fhir/datatypes.html#HumanName)** — FHIR encodes dated names via multi-value on the Patient (no event-node). We lift the same pattern to an event-node because the change has its own date + place + authority context worth capturing as a first-class graph entity.
- **[Wikidata P735/P734/P21 + P580/P582 qualifiers](https://www.wikidata.org/wiki/Property:P735)** — Property statements with start-time/end-time qualifiers. Validates "reuse canonical field name + date positions in time".
