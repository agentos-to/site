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
| `person` | [`person`](/docs/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[PostHog Events API](https://posthog.com/docs/api/events)** — Direct source: our distinctId/properties/currentUrl are PostHog's distinct_id/properties/$current_url.
- **[Segment Track Spec](https://segment.com/docs/connections/spec/track/)** — Generic product-analytics event model: event(name) + properties blob + user id. Our fields are compatible with Segment payloads.
- **[Google Analytics 4 Event Schema](https://developers.google.com/analytics/devguides/collection/protocol/ga4)** — GA4 is the other de-facto analytics event standard; our properties parallels GA4's event_params array.
