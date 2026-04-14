---
title: brand
description: "A consumer brand. Extracted from product listings."
sidebar:
  label: brand
---

A consumer brand. Extracted from product listings.

Example sources: Amazon

| Metadata | Value |
|---|---|
| **Plural** | `brands` |
| **Subtitle field** | `tagline` |
| **Identity** | `url` |

## Fields

| Field | Type |
|---|---|
| `tagline` | `string` |
| `founded` | `datetime` |
| `country` | `string` |

## Relations

| Relation | Target |
|---|---|
| `ownedBy` | [`organization`](/docs/reference/shapes/organization/) |
| `website` | [`website`](/docs/reference/shapes/website/) |
