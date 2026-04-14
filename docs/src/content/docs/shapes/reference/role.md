---
title: role
description: "A person's position at an organization (job title, board seat, etc.)."
sidebar:
  label: role
---

A person's position at an organization (job title, board seat, etc.).
Links a person to an organization with a time range.

| Metadata | Value |
|---|---|
| **Plural** | `roles` |
| **Subtitle field** | `name` |

## Fields

| Field | Type |
|---|---|
| `title` | `string` |
| `department` | `string` |
| `roleType` | `string` |
| `startDate` | `datetime` |
| `endDate` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `person` | [`person`](/docs/shapes/reference/person/) |
| `organization` | [`organization`](/docs/shapes/reference/organization/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Role + OrganizationRole](https://schema.org/OrganizationRole)** — Our title = roleName; startDate/endDate match; department ≈ name of a subOrganization; person/organization = Role's nested pattern.
- **[FOAF + Bio vocabularies (position)](http://vocab.org/bio/0.1/.html)** — Period-of-employment modeling. Our startDate/endDate ≈ bio:date; roleType has no FOAF peer.
