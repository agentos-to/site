---
title: organization
description: "A company, nonprofit, or other organization. Organizations are actors — they"
sidebar:
  label: organization
---

A company, nonprofit, or other organization. Organizations are actors — they
can be attributed as "who" in the graph alongside people and agents.

Example sources: extracted from various skills (email domains, product manufacturers, etc.)

| Metadata | Value |
|---|---|
| **Plural** | `organizations` |
| **Subtitle field** | `industry` |
| **Identity** | `url` |
| **Also** | [`actor`](/docs/shapes/reference/actor/) |

## Fields

| Field | Type |
|---|---|
| `industry` | `string` |
| `founded` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `member` | [`person[]`](/docs/shapes/reference/person/) |
| `domain` | [`domain`](/docs/shapes/reference/domain/) |
| `website` | [`website`](/docs/shapes/reference/website/) |
| `headquarters` | [`place`](/docs/shapes/reference/place/) |

## Inherited

From [`actor`](/docs/shapes/reference/actor/):

| Field | Type |
|---|---|
| `actorType` | `string` |

## Used as a base by

- [`airline`](/docs/shapes/reference/airline/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Organization](https://schema.org/Organization)** — Our industry ≈ naics/isicV4 (loosely); founded = foundingDate; member[] = member; headquarters = location (or subOrganization with a Place).
- **[vCard 4.0 KIND=org (RFC 6350)](https://datatracker.ietf.org/doc/html/rfc6350)** — Organization-as-contact. Our website/domain ≈ URL; headquarters ≈ ADR. Thinner than schema.org for industry/founded.
- **[Wikidata (Organization, Q43229)](https://www.wikidata.org/wiki/Q43229)** — Cross-reference identity. Useful for deduping; no direct field alignment but industry maps to P452 (industry) and founded to P571 (inception).
