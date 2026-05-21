---
title: birth
description: "A person's birth. The canonical event recording given/family names,"
sidebar:
  label: birth
---

A person's birth. The canonical event recording given/family names,
gender, and other birth-time particulars as of the moment of birth.

Per platform/README.md rule 1 (an event is a relationship; time and
place ride on it): birthdate is not a person field — it's this event's
`startDate`. Same for every name part and gender. See `person.yaml`'s
`derived:` block for how `joe —born_in→ birth(...)` projects to
`joe.givenName` etc.

Field semantics (cultural + legal grounding):
- `givenName` / `additionalName` / `familyName` — schema.org +
vCard 4.0 N tuple. "given" and "family" avoid Western "first/last"
bias (CJK names speak family first).
- `honorificPrefix` / `honorificSuffix` — "Dr", "Jr", "III", "PhD".
Suffixes matter for TSA Secure Flight if on government ID.
- `legalName` — verbatim string as on government ID. IATA PNR and
ICAO 9303 MRZ require this exact form; structured reconstruction
is lossy (diacritics stripped, hyphens vary).
- `maidenName` — cultural birth surname, often distinct from
`familyName` in Spanish-system (apellido materno) and similar
two-surname traditions. Used for genealogy + reunion search.
- `sortAs` — vCard SORT-AS equivalent for particled surnames
("van der Harten" sorts under H).
- `nameOrder` — rendering hint: "given-family" | "family-given" |
"patronymic".
- `phoneticGivenName` / `phoneticFamilyName` — Apple/Google
phonetic variants; matter for TTS and call-screening.
- `nickname` — casual / informal name in use at birth (rare; usually
populated on a `transition` event later in life).

| Metadata | Value |
|---|---|
| **Plural** | `births` |
| **Subtitle field** | `location` |
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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Person.birthDate / birthPlace](https://schema.org/birthDate)** — schema.org collapses birth into two flat fields on Person; we lift to an event-node so all birth particulars (name, gender, legal-doc form) co-locate per platform README rule 1.
- **[GEDCOM 7 INDI.BIRT](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html)** — Genealogy's canonical model: a typed INDIVIDUAL_EVENT with DATE, PLAC, ADDR sub-records. Our `birth` shape is the equivalent — sub-records map to event-base fields (startDate, location) plus the typed birth-particulars fields above.
- **[GEDCOM-X Fact (FactType=Birth)](https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md)** — FamilySearch's reified-fact model. We adopt the reified-event pattern; field set is richer (legalName + phonetics + nameOrder) for present-day identity-document interop.
