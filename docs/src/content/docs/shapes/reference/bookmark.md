---
title: bookmark
description: "A pointer into the graph — the universal shortcut. A bookmark is a"
sidebar:
  label: bookmark
---

A pointer into the graph — the universal shortcut. A bookmark is a
name + a target; the target is the contract. Bookmarks are wrapped
by `list --contains--> bookmark` links so the SAME bookmark can live
in three lists (the desktop, the primary launcher, a user's pinned
items) at three different positions with three different name
overrides — the per-list metadata lives on the contains-link, not
on the bookmark.

Identity is `[target]`: one bookmark per addressable target. List
membership comes from the --contains--> link, not from bookmark
uniqueness. The bookmark's own icon comes from its target; per-list
overrides ride on the contains-link as icon_override.

`handle` makes a bookmark a resolvable symlink: `read({id: handle})`
finds no literal node, derefs the handle → this bookmark → points_to
target (across the mount boundary when points_to carries to_volume).
A literal node id always wins (Unix collision rule); the handle only
resolves a miss. One bookmark per target → at most one handle per node.

| Metadata | Value |
|---|---|
| **Plural** | `bookmarks` |
| **Subtitle field** | `name` |
| **Identity** | `points_to` |

## Fields

| Field | Type |
|---|---|
| `name` | `string` |
| `handle` | `string` |

## Relations

| Relation | Target |
|---|---|
| `points_to` | `node` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Browser bookmarks (Mosaic / Netscape Navigator hotlist)](https://en.wikipedia.org/wiki/Bookmark_(digital))** — Direct precedent. A bookmark is a name + a target; the target is the contract; the surface doesn't care what's behind it. We replace HTTP URLs with graph node references; everything else maps 1:1.
- **[macOS alias / Windows .lnk file](https://en.wikipedia.org/wiki/Alias_(Mac_OS))** — OS-level shortcut primitive. Same shape: name + target. Per- instance position is handled by the parent folder/desktop in both — for us that lives on the contains-link.
- **[Finder sidebar / Windows Explorer Quick Access](https://support.apple.com/guide/mac-help/customize-the-finder-sidebar-mchlp3014/mac)** — OS file managers use a bookmark sidebar as their universal navigation primitive (My Computer, Documents, Network). We treat every shape the same way — bookmark to any graph node, no FS bias.
