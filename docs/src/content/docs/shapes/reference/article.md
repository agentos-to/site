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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Article](https://schema.org/Article)** — Our wordCount = wordCount; section = articleSection; language = inLanguage; publisher matches; publishedIn(website) ≈ isPartOf/publisher. readingTime has no direct property (often timeRequired in ISO 8601 duration).
- **[JATS (NISO Z39.96, Journal Article Tag Suite)](https://jats.nlm.nih.gov/)** — Scholarly-article XML standard. Our section ≈ <article-categories>/<subj-group>; language ≈ @xml:lang; publisher ≈ <publisher-name>. Heavier than needed for non-scholarly content.
- **[OpenGraph article:* properties](https://ogp.me/#type_article)** — Web-article metadata in the wild. Our section ≈ article:section; publisher ≈ article:publisher; language ≈ og:locale. No wordCount/readingTime in OG.
