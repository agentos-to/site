---
title: search
description: "A search query and its results. Every search is a graph entity with click"
sidebar:
  label: search
---

A search query and its results. Every search is a graph entity with click
tracking — re-searching shows previously-found results first.

| Metadata | Value |
|---|---|
| **Plural** | `searches` |
| **Subtitle field** | `query` |
| **Identity** | `query` |

## Fields

| Field | Type |
|---|---|
| `query` | `string` |
| `searchedAt` | `datetime` |
| `searchCount` | `integer` |
| `resultCount` | `integer` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[OpenSearch Description (Url templates)](https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md)** — Our query field is the searchTerm in OpenSearch's Url template. resultCount ≈ totalResults header.
- **[schema.org/SearchAction](https://schema.org/SearchAction)** — Our query + searchedAt ≈ SearchAction.query + startTime. searchCount is AgentOS-specific (reuse telemetry).
