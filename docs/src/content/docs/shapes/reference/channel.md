---
title: channel
description: "A content channel — typically a YouTube channel. Videos are uploaded to channels."
sidebar:
  label: channel
---

A content channel — typically a YouTube channel. Videos are uploaded to channels.

| Metadata | Value |
|---|---|
| **Plural** | `channels` |
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
| `banner` | `url` |
| `subscriberCount` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0 Collection](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection)** — A channel is a platform-specific Collection of media items. Our banner is channel branding; AS2 doesn't model that directly.
- **[YouTube Data API — Channel resource](https://developers.google.com/youtube/v3/docs/channels)** — Practical source. Our channel id/banner map to YouTube's channelId and brandingSettings.image.bannerExternalUrl.
- **[RSS 2.0 <channel>](https://www.rssboard.org/rss-specification)** — Original "channel" concept — a grouped feed with title, image, and items. Our channel is the same pattern for video.

## Skills that produce this shape

- [youtube](/skills/reference/media/youtube/) — `get_channel`, `get_avatar_channel`
