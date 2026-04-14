---
title: actor
description: "Base type for anything that can be attributed as 'who did this' in the graph."
sidebar:
  label: actor
---

Base type for anything that can be attributed as "who did this" in the graph.
Not used directly — person, organization, and agent extend it via `also`.

| Metadata | Value |
|---|---|
| **Plural** | `actors` |
| **Subtitle field** | `actorType` |

## Fields

| Field | Type |
|---|---|
| `actorType` | `string` |

## Used as a base by

- [`agent`](/docs/shapes/reference/agent/)
- [`organization`](/docs/shapes/reference/organization/)
- [`person`](/docs/shapes/reference/person/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[FOAF Agent](http://xmlns.com/foaf/spec/#term_Agent)** — FOAF Agent is the base class for Person, Organization, and Group. Our actorType mirrors FOAF's agent taxonomy.
- **[ActivityStreams 2.0 Actor](https://www.w3.org/TR/activitystreams-vocabulary/#actor-types)** — AS2 defines Actor types (Person, Organization, Group, Service, Application). Our agent ≈ Service/Application.
