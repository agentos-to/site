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

- [brave-browser](/docs/reference/skills/browsers/brave-browser/) — `list_webpages`, `search_webpages`
- [firecrawl](/docs/reference/skills/web/firecrawl/) — `read_webpage`
- [exa](/docs/reference/skills/web/exa/) — `read_webpage`
- [curl](/docs/reference/skills/web/curl/) — `read_webpage`
