---
title: icon
description: "A small graphic intended for UI use — toolbar buttons, file-type"
sidebar:
  label: icon
---

A small graphic intended for UI use — toolbar buttons, file-type
stamps, taskbar entries, status indicators.

Distinguished from `image` (general-purpose photographs / screenshots
/ artwork) by:
- small, fixed size (typically 16 / 24 / 32 / 48 px square)
- role-specific `purpose` field (back / forward / my-computer / ...)
- can be a React component (Vite-resolvable module path), not just
a file on disk

One shape for both file-backed icons (SVG / PNG) and component-backed
icons (React). The `format` field discriminates; consumers branch on
`format == 'react-component'` to load the component, otherwise treat
`url` as a fetchable asset URL.

An icon is a creative_work (its designer matters, its license matters)
but NOT generally a file — component-backed icons live inside a JS
bundle and have no standalone file artifact. File-backed icons can be
joined to their file entry via a separate link if/when needed.

| Metadata | Value |
|---|---|
| **Plural** | `icons` |
| **Subtitle field** | `purpose` |
| **Identity (any)** | `component`, `url` |
| **Also** | [`creative_work`](/shapes/reference/creative_work/) |

## Fields

| Field | Type |
|---|---|
| `dimension` | `integer` |
| `format` | `string` |
| `url` | `string` |
| `component` | `string` |
| `purpose` | `string` |
| `style` | `string` |

## Inherited

From [`creative_work`](/shapes/reference/creative_work/):

| Field | Type |
|---|---|
| `copyrightYear` | `integer` |
| `coverage` | `string` |
| `dateCreated` | `date` |
| `description` | `string` |
| `language` | `string` |
| `license` | `string` |
| `tags` | `string[]` |

| Relation | Target |
|---|---|
| `contributed_by` | [`person[]`](/shapes/reference/person/) |
| `held_by` | [`person`](/shapes/reference/person/) |
| `published_by` | [`actor`](/shapes/reference/actor/) |
| `written_by` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/ImageObject](https://schema.org/ImageObject)** — Icons could be modeled as ImageObject — we chose a distinct shape because the role-specific `purpose` field has no counterpart on ImageObject (which is purpose-agnostic by design) and because component-backed icons aren't fetchable as image URLs.
- **[Iconify metadata](https://iconify.design/)** — Iconify treats icons as named entries within an icon set, each with a category and tags. Our `purpose` field plays the same role as Iconify's category; our `style` plays the same role as Iconify's iconset style attribute (filled / outline / pixel).
- **[Material Symbols metadata](https://fonts.google.com/icons)** — Material Symbols ship as a variable icon font with `fill`, `weight`, `grade`, and `optical-size` axes. Our shape doesn't model variable axes (Material Symbols would be one font, not one icon-per-glyph) — we model icons that live OUTSIDE icon fonts.
- **[macOS / Windows system icon naming](https://learn.microsoft.com/en-us/windows/win32/uxguide/vis-icons)** — Both platforms standardize on role-named icons (e.g. "back", "forward", "close") rather than file-named icons. Our `purpose` field follows the same convention; theme authors register icons by their semantic role, not by a filename slug.
