---
title: webpage
description: "A web page. Base type for search result. Also used for browser history"
sidebar:
  label: webpage
---

A web page. Base type for search result. Also used for browser history
and as a generic container when reading arbitrary URLs.

Example sources: Brave Browser, Firefox (history); Exa, Firecrawl, Curl (web reading)

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

## Skills that produce this shape

- [brave-browser](/docs/skills/reference/browsers/brave-browser/) — `list_webpages`, `search_webpages`
- [firecrawl](/docs/skills/reference/web/firecrawl/) — `read_webpage`
- [exa](/docs/skills/reference/web/exa/) — `read_webpage`
- [curl](/docs/skills/reference/web/curl/) — `read_webpage`
