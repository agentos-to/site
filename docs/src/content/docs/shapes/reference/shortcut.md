---
title: shortcut
description: "A named alias that expands to a location URI at parse time."
sidebar:
  label: shortcut
---

A named alias that expands to a location URI at parse time.
Simple name -> target mappings. No patterns, no regex.
Built-in shortcuts (limbo, search, help, web, files) are seeded at boot.
Skills can register shortcuts (reddit, youtube, etc).
Users can create, modify, or delete any shortcut.

Structural input (URLs, domains, absolute paths) is handled by the normalizer
before shortcut lookup — shortcuts don't need pattern matching.

| Metadata | Value |
|---|---|
| **Plural** | `shortcuts` |
| **Subtitle field** | `target` |
| **Identity** | `name` |

## Fields

| Field | Type |
|---|---|
| `name` | `string` |
| `target` | `string` |
| `filter` | `string` |
| `builtin` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `skill` | [`skill`](/docs/shapes/reference/skill/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Unix shell aliases (bash/zsh)](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/alias.html)** — Our name→target expansion follows the alias pattern. builtin vs user-created parallels shell builtins vs. rc-file aliases.
- **[Vannevar Bush — "As We May Think" (1945, associative trails)](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/)** — Named trails through the memex. Our named shortcut-to-URI mapping is a mechanized version of Bush's trail idea.
- **[RFC 3986 URI Generic Syntax](https://datatracker.ietf.org/doc/html/rfc3986)** — Our target is a URI (location URI). Shortcut names resolve to RFC 3986-compliant references.
