---
title: analytics_event
description: "A product analytics action — a single user interaction tracked by PostHog."
sidebar:
  label: analytics_event
---

A product analytics action — a single user interaction tracked by PostHog.
NOT a life event — see event.yaml for births, marriages, etc.

Example sources: PostHog

| Metadata | Value |
|---|---|
| **Plural** | `analytics_events` |

## Fields

| Field | Type |
|---|---|
| `distinctId` | `string` |
| `properties` | `json` |
| `currentUrl` | `url` |

## Relations

| Relation | Target |
|---|---|
| `person` | [`person`](/docs/reference/shapes/person/) |
