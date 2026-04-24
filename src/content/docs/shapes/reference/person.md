---
title: person
description: "A real human. People are actors — they can own accounts, hold roles, attend meetings."
sidebar:
  label: person
---

A real human. People are actors — they can own accounts, hold roles, attend meetings.
Resolved from contacts, message senders, meeting attendees, etc.

Name model (aligned with schema.org/Person + vCard 4.0 N property +
Google/Apple Contacts):
- `givenName` / `familyName` / `additionalName` — the structured parts.
"given" and "family" avoid Western "first/last" assumptions: in CJK
names, the family name is SPOKEN FIRST.
- `honorificPrefix` / `honorificSuffix` — "Dr", "Jr", "III", "PhD".
TSA Secure Flight requires suffixes if they appear on government ID.
- `legalName` — the full name exactly as on government ID. Source of
truth for airline tickets (IATA PNR), passports (ICAO 9303). Structured
reconstruction is lossy (diacritics stripped, hyphens vary); keep the
verbatim string.
- `preferredName` — what the person actually wants to be called.
Distinct from `nickname` (casual only). Important for trans and
chosen-name contexts where `givenName` on ID differs from daily use.
- `maidenName` — cultural birth surname; used for genealogy, reunion
search, Spanish-system apellido materno.
- `sortAs` — vCard SORT-AS equivalent for last-names-with-particles
("van der Harten" sorts under "H"; "de la Cruz" under "C").
- `nameOrder` — rendering hint: "given-family" (default) | "family-given"
(CJK) | "patronymic" (Russian/Icelandic).
- `phoneticGivenName` / `phoneticFamilyName` — Apple/Google phonetic
variants; matters for TTS and call-screening on non-Latin names.

`name` (standard field inherited from every shape) is the display form —
a single rendered string like "Dr. Giuseppe Efisio Contini, PhD".

| Metadata | Value |
|---|---|
| **Plural** | `people` |
| **Subtitle field** | `about` |
| **Also** | [`actor`](/shapes/reference/actor/) |

## Fields

| Field | Type |
|---|---|
| `givenName` | `string` |
| `familyName` | `string` |
| `additionalName` | `string` |
| `honorificPrefix` | `string` |
| `honorificSuffix` | `string` |
| `legalName` | `string` |
| `preferredName` | `string` |
| `maidenName` | `string` |
| `nickname` | `string` |
| `sortAs` | `string` |
| `nameOrder` | `string` |
| `phoneticGivenName` | `string` |
| `phoneticFamilyName` | `string` |
| `birthday` | `datetime` |
| `notes` | `text` |
| `gender` | `string` |
| `about` | `text` |

## Relations

| Relation | Target |
|---|---|
| `accounts` | [`account[]`](/shapes/reference/account/) |
| `roles` | [`role[]`](/shapes/reference/role/) |
| `memberships` | [`membership[]`](/shapes/reference/membership/) |
| `passes` | [`pass[]`](/shapes/reference/pass/) |
| `location` | [`place`](/shapes/reference/place/) |
| `website` | [`website`](/shapes/reference/website/) |

## Inherited

From [`actor`](/shapes/reference/actor/):

| Field | Type |
|---|---|
| `actorType` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Person](https://schema.org/Person)** — Our givenName / familyName / additionalName / honorificPrefix / honorificSuffix map directly. schema.org has no `middleName` (additionalName is the slot); no `firstName`/`lastName` either — those are informal Wikipedia-style labels, not spec. birthday ≈ birthDate; about ≈ description. We diverge by modeling accounts[] as a first-class relation rather than sameAs URLs.
- **[vCard 4.0 (RFC 6350) §6.2.2 N property + §5.9 SORT-AS](https://datatracker.ietf.org/doc/html/rfc6350#section-6.2.2)** — The N property is `family;given;additional;prefixes;suffixes`, each comma-multi-valued. Our five structured fields round-trip exactly. sortAs mirrors RFC 6350's SORT-AS parameter for particled surnames ("van der Harten" sorts under H).
- **[Google People API Name resource](https://developers.google.com/people/api/rest/v1/people#Name)** — Google uses givenName / familyName / middleName / honorificPrefix / honorificSuffix + phoneticGivenName / phoneticFamilyName + displayName + unstructuredName. We follow the same naming, using schema.org's `additionalName` where Google says `middleName` (schema.org wins for multi-value support).
- **[Apple CNContact](https://developer.apple.com/documentation/contacts/cncontact)** — Apple exposes givenName / middleName / familyName + phonetic* variants + nameSuffix / namePrefix + previousFamilyName (≈ maidenName). Same shape as Google; reinforces the field set.
- **[IATA PNR NM field + ICAO Doc 9303 (MRZ)](https://en.wikipedia.org/wiki/Machine-readable_passport)** — Airline ticketing and passport MRZ require a specific string form (SURNAME/GIVENNAME TITLE, all caps, Latin-only, diacritics stripped, 30-char limits). Structured parts can't losslessly reconstruct this; we store it verbatim in `legalName`.
- **[W3C i18n — Personal names around the world](https://www.w3.org/International/questions/qa-personal-names)** — Canonical reference for why "first/last" is a Western bias. CJK names put family first. Spanish uses two surnames. Icelandic uses patronymics without family names. The `nameOrder` field captures the rendering rule; structured fields stay neutral.
- **[FOAF (Friend of a Friend)](http://xmlns.com/foaf/spec/)** — Original social-graph vocabulary. foaf:Person with givenName/familyName/nick/homepage; foaf:account ≈ our accounts[]. Largely superseded by schema.org but still a reference for account-centric modeling.

## Skills that produce this shape

- [goodreads](/skills/reference/media/goodreads/) — `get_author`, `get_person`, `search_people`, `list_friends`, `resolve_email`, `list_following`, `list_followers`
- [google-contacts](/skills/reference/productivity/google-contacts/) — `list_contacts`, `search_contacts`, `get_contact`, `create_contact`, `update_contact`
- [united](/skills/reference/logistics/united/) — `get_profile`
- [whatsapp](/skills/reference/comms/whatsapp/) — `op_list_persons`
