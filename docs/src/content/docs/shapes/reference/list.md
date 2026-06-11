---
title: list
description: "A list — the universal ordered (or not) collection. Folders, menus,"
sidebar:
  label: list
---

A list — the universal ordered (or not) collection. Folders, menus,
playlists, albums, the desktop, the tray, the primary launcher, the
wallpapers album, agent task queues, search-result snapshots,
Memex trails — all are `list` nodes with different listType +
ordering_mode. One shape, one renderer dispatch, one context-menu
router, one CLI vocabulary.

`ordering_mode` is a CLOSED ENUM — the renderer branches on it:
linear     → vertical list (top-to-bottom) or horizontal strip;
link.position = { linear: integer }
spatial    → icon grid (col,row → x,y in CSS px);
link.position = { spatial: { col: int, row: int } }
unordered  → icon wrap, view-time sort via sort_by;
link.position absent
temporal   → timeline / reverse-chrono feed;
link.position = { temporal: { datetime: string } }

`listType` is an OPEN STRING — **content semantics only**. What KIND
of container: 'folder' (default, generic), 'playlist' (music linear
queue), 'album' (music release), 'gallery' (image grid), 'shelf'
(read-it-later), 'tag' (flat classifier), 'search-snapshot' (saved
query results), 'task-queue', etc.

Shell position is NOT a listType. The desktop, tray, launchers, and
wallpapers folder are ALL `listType: 'folder'` with `id: 'desktop'` /
`'tray'` / `'primary-launcher'` / `'wallpapers'`. The theme's renderer
dispatches on `id` to apply specialized chrome (wallpaper+icons for
id='desktop', bottom strip for id='tray', etc.) — never on listType.
Nothing in the engine branches on listType either; it is a render hint.

| Metadata | Value |
|---|---|
| **Plural** | `lists` |
| **Subtitle field** | `name` |
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
| `id` | `string` |
| `listId` | `string` |
| `listType` | `string` |
| `ordering_mode` | `string` |
| `member_shape` | `string` |
| `privacy` | `string` |
| `isDefault` | `boolean` |
| `isPublic` | `boolean` |
| `itemCount` | `integer` |
| `arrangement` | `string` |
| `default_view` | `string` |
| `icon_size` | `integer` |
| `sort_by` | `string` |
| `path` | `string` |

## Relations

| Relation | Target |
|---|---|
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `belongs_to` | [`account`](/shapes/reference/account/) |
| `contains` | `node[]` |
| `backed_by` | [`image`](/shapes/reference/image/) |

## Used as a base by

- [`health-panel`](/shapes/reference/health-panel/)
- [`playlist`](/shapes/reference/playlist/)
- [`shelf`](/shapes/reference/shelf/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/ItemList](https://schema.org/ItemList)** — listType ≈ itemListOrder; contains ≈ itemListElement; isPublic ≈ publicAccess.
- **[ActivityStreams 2.0 Collection / OrderedCollection](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection)** — contains[] ≈ items; ordering_mode='linear' ≈ OrderedCollection, ordering_mode='unordered' ≈ Collection.
- **[WinFS Item / FolderMember](https://learn.microsoft.com/en-us/archive/msdn-magazine/2004/january/winfs-lets-users-search-and-manage-files-based-on-content)** — WinFS unified Folder + Contact + Photo under a single Item base, with FolderMember as a holding link. Our list-with-contains is the same pattern: one shape, one link mechanism, view-time projections handle the "I want it to look like an album" case.
- **[Vannevar Bush — As We May Think (Memex trails)](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/)** — A Memex trail is a named, ordered list of associative jumps. A `list` with ordering_mode='linear' and contains-bookmarks IS Bush's trail. Foundational precedent for the everything-is-a-list thesis.
- **[POSIX / Single Unix Specification (directories)](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html)** — listType='folder' with optional `path` field mirrors a POSIX directory. The engine treats it as a list; the filesystem mirror is a projection, not a separate primitive.

## Apps that produce this shape

- [amazon](/apps/reference/logistics/amazon/) — `list_lists`, `get_list`
