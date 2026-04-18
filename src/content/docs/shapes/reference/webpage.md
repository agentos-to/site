---
title: webpage
description: "A web page. Base type for search result. Also used for browser history"
sidebar:
  label: webpage
---

A web page. Base type for search result. Also used for browser history
and as a generic container when reading arbitrary URLs.

| Metadata | Value |
|---|---|
| **Plural** | `webpages` |
| **Subtitle field** | `url` |
| **Identity** | `url` |

## Fields

| Field | Type |
|---|---|
| `visitCount` | `integer` |
| `lastVisitUnix` | `integer` |
| `contentType` | `string` |
| `error` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/WebPage](https://schema.org/WebPage)** — Our URL-as-identity matches schema.org's @id/url convention; contentType ≈ encodingFormat.
- **[HTTP semantics (RFC 9110)](https://datatracker.ietf.org/doc/html/rfc9110)** — Our contentType is the Content-Type response header; error ≈ non-2xx status text.
- **[Chrome history / WebExtensions History API](https://developer.chrome.com/docs/extensions/reference/api/history)** — Practical source. Our visitCount/lastVisitUnix lift from the history API's VisitItem structure.

## Skills that produce this shape

- [brave-browser](/skills/reference/browsers/brave-browser/) — `list_webpages`, `search_webpages`
- [firecrawl](/skills/reference/web/firecrawl/) — `read_webpage`
- [exa](/skills/reference/web/exa/) — `read_webpage`
- [curl](/skills/reference/web/curl/) — `read_webpage`
