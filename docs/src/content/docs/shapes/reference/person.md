---
title: person
description: "A real human. People are actors — they can own accounts, hold roles, attend meetings."
sidebar:
  label: person
---

A real human. People are actors — they can own accounts, hold roles, attend meetings.
Resolved from contacts, message senders, meeting attendees, etc.

| Metadata | Value |
|---|---|
| **Plural** | `people` |
| **Subtitle field** | `about` |
| **Also** | [`actor`](/shapes/reference/actor/) |

## Fields

| Field | Type |
|---|---|
| `firstName` | `string` |
| `lastName` | `string` |
| `middleName` | `string` |
| `nickname` | `string` |
| `birthday` | `datetime` |
| `notes` | `text` |
| `gender` | `string` |
| `about` | `text` |
| `joinedDate` | `datetime` |
| `lastActive` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `accounts` | [`account[]`](/shapes/reference/account/) |
| `roles` | [`role[]`](/shapes/reference/role/) |
| `location` | [`place`](/shapes/reference/place/) |
| `website` | [`website`](/shapes/reference/website/) |

## Inherited

From [`actor`](/shapes/reference/actor/):

| Field | Type |
|---|---|
| `actorType` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Person](https://schema.org/Person)** — Our firstName/lastName = givenName/familyName; nickname = additionalName/alternateName; birthday = birthDate; about = description. We diverge by modeling accounts[] as a first-class relation rather than sameAs URLs.
- **[vCard 4.0 (RFC 6350)](https://datatracker.ietf.org/doc/html/rfc6350)** — Contact-card canonical. Our fields map to FN/N/NICKNAME/BDAY/NOTE; our accounts[] ≈ IMPP/X-SOCIALPROFILE; location ≈ ADR.
- **[FOAF (Friend of a Friend)](http://xmlns.com/foaf/spec/)** — Original social-graph vocabulary. foaf:Person with givenName/familyName/nick/homepage; foaf:account ≈ our accounts[]. Largely superseded by schema.org but still a reference for account-centric modeling.

## Skills that produce this shape

- [goodreads](/skills/reference/media/goodreads/) — `get_author`, `get_person`, `search_people`, `list_friends`, `resolve_email`, `list_following`, `list_followers`
- [google-contacts](/skills/reference/productivity/google-contacts/) — `list_contacts`, `search_contacts`, `get_contact`, `create_contact`, `update_contact`
- [whatsapp](/skills/reference/comms/whatsapp/) — `op_list_persons`
- [posthog](/skills/reference/web/posthog/) — `list_persons`, `search_persons`, `get_person`
