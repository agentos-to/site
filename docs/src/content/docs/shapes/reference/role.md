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
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `title` | `string` |
| `department` | `string` |
| `roleType` | `string` |

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

- **[schema.org/Role + OrganizationRole](https://schema.org/OrganizationRole)** — Our title = roleName; startDate/endDate match; department ≈ name of a subOrganization; person/organization = Role's nested pattern.
- **[FOAF + Bio vocabularies (position)](http://vocab.org/bio/0.1/.html)** — Period-of-employment modeling. Our startDate/endDate ≈ bio:date; roleType has no FOAF peer.
