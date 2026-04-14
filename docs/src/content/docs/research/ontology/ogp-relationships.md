---
title: "Open Graph Protocol: Relationship Modeling"
description: How OGP models relationships between entities — patterns, limitations, and lessons.
---

## Summary

Open Graph Protocol uses a **URL-based reference model** for relationships. Objects link to other objects by including the target's canonical URL as a property value. This is simple but limited — relationships are uni-directional, have no custom types, and require both ends to exist as crawlable web pages.

**Key insight:** OGP's relationship model is designed for the "link preview" use case, not comprehensive entity modeling. It answers "who made this?" and "what contains this?" — not "how do these things relate in general?"

---

## How OGP Expresses Relationships

### The Core Pattern: URL References

Every relationship in OGP follows the same pattern:

```html
<meta property="[namespace]:[relationship]" content="[URL of target object]" />
```

The target URL must be a page with its own OGP markup (including `og:type`). The relationship is **from** the current page **to** the target.

**Example: Article with Author**
```html
<!-- On the article page -->
<meta property="og:type" content="article" />
<meta property="article:author" content="https://example.com/people/jane-doe" />

<!-- On Jane Doe's profile page -->
<meta property="og:type" content="profile" />
<meta property="profile:first_name" content="Jane" />
<meta property="profile:last_name" content="Doe" />
```

The article references the author's profile URL. The profile page has no back-reference to the articles — the relationship is **uni-directional**.

### Arrays: Multiple Relationships

When an object has multiple targets of the same relationship type, repeat the meta tag:

```html
<meta property="video:actor" content="https://example.com/people/actor-1" />
<meta property="video:actor" content="https://example.com/people/actor-2" />
<meta property="video:actor" content="https://example.com/people/actor-3" />
```

The first tag has precedence in case of conflicts.

### Structured Sub-Properties: Relationship Metadata

Some relationships support metadata about the relationship itself:

```html
<!-- Song on an album -->
<meta property="og:type" content="music.song" />
<meta property="music:album" content="https://example.com/albums/abbey-road" />
<meta property="music:album:disc" content="1" />
<meta property="music:album:track" content="7" />
```

The sub-properties (`music:album:disc`, `music:album:track`) describe the relationship, not the target object. This is OGP's only mechanism for relationship metadata.

---

## Complete Relationship Vocabulary

### Content → Creator Relationships

| Property | On Type | Target Type | Description |
|----------|---------|-------------|-------------|
| `article:author` | article | profile[] | Writers of the article |
| `book:author` | book | profile[] | Authors of the book |
| `music:musician` | music.song, music.album | profile[] | Artist(s) |
| `music:creator` | music.playlist, music.radio_station | profile | Curator/creator |
| `video:actor` | video.* | profile[] | Actors in the video |
| `video:director` | video.* | profile[] | Directors |
| `video:writer` | video.* | profile[] | Writers/screenwriters |

### Part-Of Relationships (Containment)

| Property | On Type | Target Type | Metadata |
|----------|---------|-------------|----------|
| `music:album` | music.song | music.album[] | `:disc`, `:track` |
| `music:song` | music.album | music.song | `:disc`, `:track` |
| `video:series` | video.episode | video.tv_show | None |

### Generic Relationships

| Property | On Type | Target Type | Description |
|----------|---------|-------------|-------------|
| `og:see_also` | any | any[] | Related content URLs |

---

## Part-Of Relationships In Depth

### Music: Song ↔ Album

OGP explicitly models the bidirectional containment relationship between songs and albums — but each side must declare it independently.

**From the Song's perspective:**
```html
<meta property="og:type" content="music.song" />
<meta property="og:title" content="Come Together" />
<meta property="music:album" content="https://example.com/albums/abbey-road" />
<meta property="music:album:disc" content="1" />
<meta property="music:album:track" content="1" />
<meta property="music:musician" content="https://example.com/artists/the-beatles" />
```

**From the Album's perspective:**
```html
<meta property="og:type" content="music.album" />
<meta property="og:title" content="Abbey Road" />
<meta property="music:song" content="https://example.com/songs/come-together" />
<meta property="music:song:disc" content="1" />
<meta property="music:song:track" content="1" />
<meta property="music:musician" content="https://example.com/artists/the-beatles" />
```

**Note from the spec:** The `music:song:disc` and `music:song:track` properties are described as "The same as `music:album:disc` but in reverse" — explicitly acknowledging the bidirectional nature.

### Video: Episode → Series

Episodes link to their parent series:

```html
<meta property="og:type" content="video.episode" />
<meta property="og:title" content="The One Where No One's Ready" />
<meta property="video:series" content="https://example.com/shows/friends" />
```

**Note:** There's no `video.tv_show:episode` property. The series doesn't enumerate its episodes in OGP — only episodes point to their series. This is **uni-directional containment**.

---

## Profile Relationships

### Profile as a Target Type

The `profile` type is OGP's representation of a person. It has minimal properties:

- `profile:first_name` — Given name
- `profile:last_name` — Family name
- `profile:username` — Unique identifier
- `profile:gender` — male/female enum

**Critically:** Profile has NO outbound relationship properties. A profile page cannot declare:
- "I authored these articles"
- "I acted in these movies"
- "I created these playlists"

All relationships **point to** profiles, never **from** profiles.

### Why This Matters

OGP's profile model is **identity-centric**, not **graph-centric**. A profile is a destination for links, not a node in a bidirectional graph. This reflects OGP's design philosophy: it's metadata for sharing, not a social network data model.

---

## The `og:see_also` Pattern

The only generic relationship property is `og:see_also`:

```html
<meta property="og:see_also" content="https://example.com/related-article-1" />
<meta property="og:see_also" content="https://example.com/related-article-2" />
```

**Characteristics:**
- Untyped — no way to specify *why* the content is related
- Uni-directional — targets don't know they're being referenced
- Array — multiple related URLs allowed
- Any-to-any — works between any object types

**Use cases:**
- "Related articles" sections
- Cross-referencing between pages
- Supplementary content links

---

## Bidirectional vs Unidirectional Links

### OGP's Model: Declaration-Based

OGP relationships are fundamentally **uni-directional by default**. Each page declares what it links TO, with no automatic inverse.

**To create bidirectional relationships:**
1. Page A declares a link to Page B
2. Page B declares a link back to Page A
3. A crawler/consumer must fetch both pages to know the relationship is mutual

### The Album ↔ Song Exception

Music is the only vertical where the spec explicitly provides "reverse" properties:

| Forward (on Song) | Reverse (on Album) |
|-------------------|--------------------|
| `music:album` | `music:song` |
| `music:album:disc` | `music:song:disc` |
| `music:album:track` | `music:song:track` |

This is OGP's only true bidirectional relationship pattern.

### What's Missing

OGP has no:
- **Inverse property declarations** — No way to say "if A has property X pointing to B, B automatically has property Y pointing to A"
- **Relationship symmetry** — No way to express "A is related to B" such that B is also related to A
- **Relationship validation** — No enforcement that both ends declare the relationship

---

## Relationship Metadata Patterns

### Position in Container

The only relationship metadata OGP supports is **position within a container**:

```html
music:album:disc   → Which disc (for multi-disc albums)
music:album:track  → Track number on that disc
music:song:disc    → Same, from album's perspective
music:song:track   → Same, from album's perspective
```

### Role in Relationship

For video actors, there's a single metadata property:

```html
<meta property="video:actor" content="https://example.com/people/tom-hanks" />
<meta property="video:actor:role" content="Forrest Gump" />
```

The `:role` sub-property must immediately follow the `video:actor` it describes.

### What's Missing

OGP cannot express:
- **Relationship dates** — When did the relationship start/end?
- **Relationship strength** — Primary author vs. contributor
- **Relationship context** — In what capacity? Under what circumstances?
- **Custom metadata** — Arbitrary key-value pairs on relationships

---

## Limitations for Relationship Modeling

### 1. Fixed Relationship Types

You cannot create custom relationship types. The vocabulary is fixed:
- `article:author`, `video:actor`, `music:musician`... and that's it.

Want to express "inspired by", "remix of", "translated from", "parody of"? Not possible in standard OGP.

### 2. No Relationship Between Arbitrary Types

Most relationships are restricted to specific type combinations:
- `article:author` only works on `article` type objects
- `video:series` only works on `video.episode` type objects

There's no general-purpose "this object relates to that object" beyond `og:see_also`.

### 3. Targets Must Exist and Be Crawlable

Every relationship target must be:
- A valid, resolvable URL
- A page with its own OGP markup
- Accessible to crawlers

You cannot reference:
- Objects that don't have web pages
- Private/authenticated content
- Objects by ID instead of URL
- Objects on other systems

### 4. No Inverse Relationships

When an article declares its author, the author's profile has no knowledge of this. There's no mechanism to:
- Auto-generate inverse relationships
- Query "what articles did this author write?"
- Validate relationship consistency

### 5. No Relationship Queries

OGP is a declaration format, not a query system. To answer "what songs are on this album?", you'd need to:
1. Crawl every song page on the internet
2. Check which ones declare `music:album` pointing to this album
3. Aggregate the results

This is impractical — hence Spotify, Apple Music, etc. use their own databases, not OGP.

### 6. Shallow Relationship Chains

OGP doesn't support relationship traversal:
- Song → Album → Artist works (two hops)
- But there's no "Song → Artist" direct property
- No way to express transitive relationships

### 7. No Temporal Relationships

All relationships are "current state." No way to express:
- "This was the author at time of publication"
- "This actor played this role from 2010-2015"
- Historical relationships vs current relationships

---

## How Platforms Extend OGP

### Facebook: Custom Actions (Deprecated)

Facebook once allowed apps to define custom actions that created relationships:
- "Joe **listened to** Abbey Road"
- "Jane **cooked** Pasta Carbonara"

These created user → object relationships in Facebook's social graph. The feature was largely deprecated by 2012 due to spam concerns and auto-posting backlash.

### Pinterest: Schema.org Preference

Pinterest Rich Pins use Schema.org markup instead of OGP for relationships:
- Recipe ingredients and instructions
- Product availability and pricing
- Article author and publish dates

Pinterest found Schema.org's richer vocabulary better suited for commerce and content relationships.

### Spotify: Proprietary APIs

Music services ignore OGP's music vocabulary in favor of their own APIs:
- Spotify Web API has full relationship modeling
- Artist discographies, album tracks, playlists
- OGP is only used for share preview metadata

### The Pattern

Platforms use OGP for **display metadata** (title, image, description) but their own systems for **relationship data**. OGP's relationship model is too limited for real applications.

---

## Comparison: OGP vs Schema.org Relationships

| Aspect | Open Graph | Schema.org |
|--------|------------|------------|
| **Relationship types** | ~15 fixed | 1,500+ properties |
| **Custom relationships** | Via namespaces (rarely used) | Extension mechanism |
| **Inverse declarations** | Manual only | `inverseOf` property |
| **Relationship metadata** | Position only | Full property support |
| **Multi-hop traversal** | Not supported | Designed for it |
| **Target types** | Must match expected type | Flexible typing |
| **URL requirement** | Always URLs | IDs, URLs, or embedded |

---

## Lessons for Entity Modeling

### What OGP Got Right

1. **URL-based identity** — Objects have permanent, resolvable IDs (canonical URLs)
2. **Simple reference syntax** — Just include the target URL
3. **Array support** — Multiple authors, multiple albums, etc.
4. **Sub-property pattern** — Relationship metadata via `:property` syntax
5. **Type-constrained relationships** — `article:author` must point to `profile`

### What We Should Improve

1. **Bidirectional by design** — If A → B, automatically B ← A with inverse property
2. **Custom relationship types** — Not limited to predefined vocabulary
3. **Richer relationship metadata** — Dates, roles, strength, context
4. **ID-based references** — Don't require URLs for everything
5. **Relationship queries** — "Find all things that relate to X"
6. **Temporal awareness** — Relationships can have time bounds

### Pattern Adoption Table

| OGP Pattern | Adopt? | Notes |
|-------------|--------|-------|
| URL references | Adapt | Use entity IDs, not URLs |
| Repeat for arrays | Yes | Simple and clear |
| Sub-properties for metadata | Yes | `:role`, `:position` pattern |
| Fixed relationship vocab | No | Need extensibility |
| Uni-directional by default | No | Bidirectional is more useful |
| Type-constrained targets | Partial | Soft constraints, not hard |

---

## Key Takeaways

1. **OGP is metadata, not a graph database** — It's designed for link previews, not relationship queries

2. **Relationships are one-way declarations** — Each page says what it links to; no automatic inverses

3. **Profile is a sink, not a source** — People are targets of relationships, not declarers

4. **Containment is the richest pattern** — Album/song relationships have the most metadata support

5. **Real applications use proprietary systems** — Spotify, Facebook, Pinterest all layer their own relationship models on top of (or instead of) OGP

6. **Simplicity came at a cost** — OGP's adoption came from simplicity, but that simplicity limits expressiveness

---

## References

- https://ogp.me/ — Official specification
- https://ogp.me/ns/ogp.me.ttl — RDF schema
- https://developers.facebook.com/docs/opengraph/music/ — Music vertical docs
- https://developers.facebook.com/docs/sharing/webmasters/ — Webmaster guide
- https://www.scribd.com/doc/30715288/The-Open-Graph-Protocol-Design-Decisions — Original design decisions (2010)
