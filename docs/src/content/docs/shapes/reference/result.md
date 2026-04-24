---
title: result
description: "A search result — a pointer to something found. Not the thing itself."
sidebar:
  label: result
---

A search result — a pointer to something found. Not the thing itself.
A search might return webpages, products, people, articles — anything.
The result just carries search-specific metadata (when indexed, what type).

| Metadata | Value |
|---|---|
| **Plural** | `results` |
| **Subtitle field** | `url` |

## Fields

| Field | Type |
|---|---|
| `indexedAt` | `datetime` |
| `resultType` | `string` |
| `externalUrl` | `url` |
| `postId` | `string` |
| `score` | `integer` |
| `similarity` | `number` |
| `community` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[OpenSearch Description Document](https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md)** — Result-pointer model: each hit has a URL + metadata. Our resultType ≈ Url template's type attribute.
- **[Web Search API conventions (Brave/Bing)](https://api.search.brave.com/app/documentation/web-search/get-started)** — Practical source. Our indexedAt/resultType align with common fields across Brave, Bing, and Exa web APIs.

## Skills that produce this shape

- [moltbook](/skills/reference/media/moltbook/) — `search_posts`
- [brave](/skills/reference/web/brave/) — `search`
- [exa](/skills/reference/web/exa/) — `search`
