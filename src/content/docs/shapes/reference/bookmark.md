---
title: bookmark
description: "A pointer into the graph. Bookmarks are the universal sidebar primitive"
sidebar:
  label: bookmark
---

A pointer into the graph. Bookmarks are the universal sidebar primitive
in the Browser — the user (or the engine, at install time) writes a
bookmark, the Browser surfaces it. Recursive uniformity: even the UI's
chrome is graph data (A23 in the athena plan).

A bookmark's `address` is a graph URI. Today the grammar is small but
extensible:
"?shape=X"       → list rows of shape X
"?shape=*"       → list shape counts (graph overview)
"node/<id>"      → open a single entity's detail view

Position controls sidebar order (ascending). When two bookmarks share
a position the tie-break is created_at ascending.

| Metadata | Value |
|---|---|
| **Plural** | `bookmarks` |
| **Subtitle field** | `address` |
| **Identity** | `address` |

## Fields

| Field | Type |
|---|---|
| `address` | `string` |
| `position` | `integer` |
| `icon` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Browser bookmarks (Mosaic / Netscape Navigator hotlist)](https://en.wikipedia.org/wiki/Bookmark_(digital))** — Direct precedent. A bookmark is a name + a URL; the URL is the contract; the browser doesn't care what's behind it. We replace HTTP URLs with graph URIs; everything else maps 1:1.
- **[Finder sidebar / Windows Explorer Quick Access](https://support.apple.com/guide/mac-help/customize-the-finder-sidebar-mchlp3014/mac)** — OS file managers use a bookmark sidebar as their universal navigation primitive (My Computer, Documents, Network). We treat every shape the same way — bookmark to a graph URI, no FS bias.
