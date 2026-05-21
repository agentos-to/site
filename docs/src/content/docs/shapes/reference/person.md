---
title: person
description: "A real human. People are actors — they can own accounts, hold roles,"
sidebar:
  label: person
---

A real human. People are actors — they can own accounts, hold roles,
attend meetings, get involved in events. Resolved from contacts, message
senders, meeting attendees, etc.

Per platform/README.md rule 1 (an event is a relationship; time and
place ride on it), the person node carries IDENTITY only — `url` and
the standard `id`. Everything that describes the person at a moment
lives on a typed event:

joe —born_in→  birth(...)        # birthdate, given/family/legal name, gender, ...
joe —changed→  transition(...)   # subsequent name/gender/identity changes
joe —lived_at→ place {from, to}  # residences, time-bracketed via link_vals
joe —worked_at→ org {from, to}   # roles, same dated-link pattern

Read-side ergonomics: `derived:` block walks events at read time and
projects current values (latest by startDate; tie-break = max link id)
onto the node JSON. So `joe.givenName` Just Works without storing it
anywhere on the person node.

Write-side ergonomics: `shortcuts:` block expands `data.create({shape:
person, birthdate: ..., givenName: ...})` into a nested birth event
automatically. No per-shape engine code; the expansion table is
codegen-emitted from this YAML.

Name model + cultural grounding (CJK family-first, Spanish two-surname,
Icelandic patronymic, IATA PNR/ICAO 9303 legal-name verbatim) lives on
`birth.yaml` and `transition.yaml`. See those shapes + their prior_art
blocks for the field semantics.

| Metadata | Value |
|---|---|
| **Plural** | `people` |
| **Subtitle field** | `about` |
| **Identity (any)** | `url` |
| **Also** | [`actor`](/shapes/reference/actor/) |

## Fields

| Field | Type |
|---|---|
| `url` | `string` |
| `notes` | `text` |
| `about` | `text` |

## Inherited

From [`actor`](/shapes/reference/actor/):

| Field | Type |
|---|---|
| `actorType` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Person](https://schema.org/Person)** — Our givenName / familyName / additionalName / honorificPrefix / honorificSuffix live on `birth.yaml` (and `transition.yaml`), not on the person node itself — schema.org's `birthDate` lives on the `--born_in--> birth { startDate }` relationship per rule 1. We diverge by modeling accounts[] as a first-class relation rather than sameAs URLs.
- **[vCard 4.0 (RFC 6350) §6.2.2 N property + §5.9 SORT-AS](https://datatracker.ietf.org/doc/html/rfc6350#section-6.2.2)** — The N property is `family;given;additional;prefixes;suffixes`, each comma-multi-valued. Round-trips exactly through the birth event's structured name fields.
- **[W3C i18n — Personal names around the world](https://www.w3.org/International/questions/qa-personal-names)** — Canonical reference for why "first/last" is a Western bias. CJK names put family first. Spanish uses two surnames. Icelandic uses patronymics without family names. The birth event's `nameOrder` field captures the rendering rule; structured fields stay neutral.
- **[FOAF (Friend of a Friend)](http://xmlns.com/foaf/spec/)** — Original social-graph vocabulary. Largely superseded by schema.org but still a reference for account-centric modeling.

## Skills that produce this shape

- [goodreads](/skills/reference/media/goodreads/) — `get_author`, `get_person`, `search_people`, `list_friends`, `resolve_email`, `list_following`, `list_followers`
- [google-contacts](/skills/reference/productivity/google-contacts/) — `list_contacts`, `search_contacts`, `get_contact`, `create_contact`, `update_contact`
- [united](/skills/reference/logistics/united/) — `get_profile`
- [whatsapp](/skills/reference/comms/whatsapp/) — `list_persons`
