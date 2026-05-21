---
title: theme
description: "An OS theme — a named knob-vector over its family's structure."
sidebar:
  label: theme
---

An OS theme — a named knob-vector over its family's structure.
A theme is data, not code: it picks a value for each of its family's
knobs (`style`, `startMenu`) and bundles a set of assets (fonts,
sounds, wallpaper, icons). It ships NO css and NO structure — the
family (commons/themes/<family>/family.ts) owns those.

Themes are reference data: each `<family>/<theme>/theme.ts` on disk is
extracted into `commons/themes/themes.manifest.json`, and the theme
seeder (core/crates/core/src/sources/themes.rs) upserts one graph node
per theme. The user's `pref:ui.themeId` selects the active theme; the
theme's `style` / `startMenu` are the default knob values, overridable
per-knob via `pref:ui.style` / `pref:ui.startMenu`.

Identity: themeId — unique per source namespace ("windows-xp",
"windows-98"). Every field below is what the seeder writes to the
node; the Rust `Theme` struct is GENERATED from this list
(docs/generate.py), so the seeder cannot write an undeclared val. The
theme's `ontology` block (its product + bundled assets) and its knob
var-groups are NOT node fields — the seeder turns `ontology` into
separate nodes + links, and knob var-groups are frontend-only code.

| Metadata | Value |
|---|---|
| **Plural** | `themes` |
| **Subtitle field** | `family` |
| **Identity** | `themeId` |

## Fields

| Field | Type |
|---|---|
| `themeId` | `string` |
| `family` | `string` |
| `description` | `text` |
| `style` | `string` |
| `startMenu` | `string` |
| `defaultBackgroundColor` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[System theme APIs (macOS NSAppearance, Windows WinUI)](https://developer.apple.com/documentation/appkit/nsappearance)** — OS-level theme abstraction. Our `family` parallels NSAppearance.Name (aqua, darkAqua) and Windows theme families.
