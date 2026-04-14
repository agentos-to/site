---
title: article
description: "A published written work — essay, news article, blog post, paper, newsletter."
sidebar:
  label: article
---

A published written work — essay, news article, blog post, paper, newsletter.
NOT necessarily a social post. "As We May Think" (1945) is an article with
no engagement metrics. A blog post shared on HN is both an article AND a
post — the skill tags it with both shapes.

article and post are siblings, not parent-child. When something is both
(a modern blog post with comments), it gets both tags.

Example sources: Exa (web articles), Firecrawl, future RSS integration

| Metadata | Value |
|---|---|
| **Plural** | `articles` |
| **Subtitle field** | `author` |

## Fields

| Field | Type |
|---|---|
| `wordCount` | `integer` |
| `readingTime` | `integer` |
| `section` | `string` |
| `language` | `string` |

## Relations

| Relation | Target |
|---|---|
| `publisher` | [`organization`](/docs/shapes/reference/organization/) |
| `publishedIn` | [`website`](/docs/shapes/reference/website/) |
