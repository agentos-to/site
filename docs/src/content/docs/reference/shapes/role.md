---
title: role
description: "A person's position at an organization (job title, board seat, etc.)."
sidebar:
  label: role
---

A person's position at an organization (job title, board seat, etc.).
Links a person to an organization with a time range.

Example sources: Apple Contacts, LinkedIn (via enrichment)

| | |
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
| `person` | [`person`](/docs/reference/shapes/person/) |
| `organization` | [`organization`](/docs/reference/shapes/organization/) |
