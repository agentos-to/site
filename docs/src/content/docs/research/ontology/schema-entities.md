---
title: Entity Schema
description: Source of truth for entity types, properties, and type design principles.
---

This file defines what entity types exist in our graph. For relationships, see `schema-relationships.md`.

---

## Core Philosophy: Entity-First, Not Hierarchical

**We are entity-first.** This means:

1. **Flat types, not hierarchies** — A book IS a book. It doesn't "extend" CreativeWork.
2. **Types are labels, not classes** — Entities can have multiple types
3. **Relationships express connections** — "book relates_to creative_work" not "book inherits from creative_work"
4. **No inheritance tax** — No deep `Thing > CreativeWork > Book` chains

### Why Not Hierarchical?

Research (2026-01-24) found:

| System | Approach | Finding |
|--------|----------|---------|
| **Neo4j** | Flat labels | Types are tags, not classes. No inheritance. |
| **Dgraph** | Flat labels | Multiple types per entity. No inheritance mechanism. |
| **Wikidata** | Hierarchical (P31/P279) | **"Large-scale conceptual disarray"** — circular dependencies, type confusion |
| **Schema.org** | Deep hierarchy | 827 types in `Thing > ... > ...` chains — hard to maintain |
| **OGP** | Flat + dot notation | `video.movie` groups without inheritance. 69.8% web adoption. |

**Conclusion:** Entity-first systems (Neo4j, Dgraph, OGP) use flat types. Hierarchical systems (Wikidata, Schema.org) have documented problems. We follow the entity-first approach.

---

## Foundation: Open Graph Protocol

We use **OGP as our primary influence** because:

1. **69.8% web adoption** — The web has voted
2. **Radical simplicity** — 17 types cover most content
3. **Entity-first** — Flat types, no inheritance
4. **Import-friendly** — Extract from web with minimal transformation
5. **Battle-tested** — Facebook reduced 39→17 types based on real usage

### OGP Types (Current Spec)

| Namespace | Types |
|-----------|-------|
| **Global** | `website`, `article`, `book`, `profile` |
| **music.\*** | `music.song`, `music.album`, `music.playlist`, `music.radio_station` |
| **video.\*** | `video.movie`, `video.episode`, `video.tv_show`, `video.other` |
| **Business** | `business.business`, `product` |

### OGP 1.0 Types (Historical — 39 types)

OGP originally had more types that were consolidated:

| Category | Types (now deprecated/consolidated) |
|----------|-------------------------------------|
| **Organizations** | `band`, `government`, `non_profit`, `school`, `university`, `company` |
| **People** | `actor`, `athlete`, `author`, `director`, `musician`, `politician`, `public_figure` |
| **Places** | `city`, `country`, `landmark`, `state_province`, `bar`, `cafe`, `hotel`, `restaurant` |
| **Activities** | `activity`, `sport` |
| **Groups** | `cause`, `sports_league`, `sports_team` |

### OGP Gaps (We Need to Add)

| Gap | Why | OGP Status |
|-----|-----|------------|
| `event` | Calendar events, meetings | Never existed in OGP |
| `place` | Standalone locations | Existed in 1.0, now deprecated |
| `organization` | Companies, bands, institutions | Existed in 1.0 as separate types, now just `business.business` |

---

## Our Type System (OGP-Inspired)

### Core Principles

1. **IDs are random** — NanoID (8 chars), not paths or slugs
2. **Types are flat labels** — No inheritance
3. **Multiple types allowed** — An entity can be `[book, product]`
4. **Relationships are first-class** — As important as entities (see `schema-relationships.md`)
5. **Properties are flexible** — Core fields defined; `data` JSON holds the rest
6. **OGP data preserved** — Import stores original `og:*` in `data.og`

### Entity Structure

```json
{
  "id": "abc12345",
  "types": ["article"],
  "name": "As We May Think",
  "created_at": "2026-01-24T12:00:00Z",
  "data": {
    "published": "1945-07",
    "author": "Vannevar Bush",
    "og": {
      "og:type": "article",
      "og:title": "As We May Think",
      "og:url": "https://..."
    }
  }
}
```

---

## Type Definitions

### Content Types (from OGP)

#### `article`
News article, blog post, essay.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Title |
| `types` | string[] | yes | `["article"]` |
| `data.published_time` | datetime | no | Publication date |
| `data.author` | string | no | Author name (or relationship) |
| `data.section` | string | no | Category/section |
| `data.tags` | string[] | no | Tags |
| `data.url` | string | no | Source URL |

**OGP equivalent:** `og:type="article"`, `article:published_time`, `article:author`, `article:section`, `article:tag`

---

#### `book`
A published book.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Title |
| `types` | string[] | yes | `["book"]` |
| `data.isbn` | string | no | ISBN |
| `data.release_date` | date | no | Publication date |
| `data.author` | string | no | Author name |

**OGP equivalent:** `og:type="book"`, `book:isbn`, `book:release_date`, `book:author`

---

#### `person`
A human being. OGP calls it "profile" (page-centric); we use "person" (entity-centric).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Display name |
| `types` | string[] | yes | `["person"]` |
| `data.first_name` | string | no | First name |
| `data.last_name` | string | no | Last name |
| `data.username` | string | no | Username/handle |
| `data.born` | date | no | Birth date |
| `data.died` | date | no | Death date |
| `data.roles` | string[] | no | What they do |

**OGP equivalent:** `og:type="profile"`, `profile:first_name`, `profile:last_name`, `profile:username`

**Decision:** Use `person` not `profile`. Profile is page-centric; person is entity-centric.

---

### Music Types (from OGP)

#### `music.song`
A single track/recording.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Song title |
| `types` | string[] | yes | `["music.song"]` |
| `data.duration` | integer | no | Length in seconds |
| `data.album` | string | no | Album name (or relationship) |
| `data.track` | integer | no | Track number |

**OGP equivalent:** `og:type="music.song"`, `music:duration`, `music:album`, `music:album:track`

---

#### `music.album`
A collection of songs.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Album title |
| `types` | string[] | yes | `["music.album"]` |
| `data.release_date` | date | no | Release date |
| `data.musician` | string | no | Artist name |

**OGP equivalent:** `og:type="music.album"`, `music:release_date`, `music:musician`

---

#### `music.playlist`
A curated list of songs.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Playlist title |
| `types` | string[] | yes | `["music.playlist"]` |
| `data.creator` | string | no | Curator name |

---

### Video Types (from OGP)

#### `video.movie`
A film.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Movie title |
| `types` | string[] | yes | `["video.movie"]` |
| `data.duration` | integer | no | Length in seconds |
| `data.release_date` | date | no | Release date |
| `data.director` | string | no | Director name |

**OGP equivalent:** `og:type="video.movie"`, `video:duration`, `video:release_date`, `video:director`

---

#### `video.episode`
A TV episode.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Episode title |
| `types` | string[] | yes | `["video.episode"]` |
| `data.series` | string | no | Series name (or relationship to video.tv_show) |

**OGP equivalent:** `og:type="video.episode"`, `video:series`

---

#### `video.tv_show`
A TV series.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Series title |
| `types` | string[] | yes | `["video.tv_show"]` |

---

### Business Types (from OGP)

#### `product`
Something you can buy/use.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Product name |
| `types` | string[] | yes | `["product"]` |
| `data.price` | number | no | Price |
| `data.currency` | string | no | Currency code |
| `data.availability` | string | no | In stock, etc. |
| `data.url` | string | no | Product URL |

**OGP equivalent:** `og:type="product"`, `product:price:amount`, `product:price:currency`

---

#### `organization`
A company, band, institution, team, group. (OGP 1.0 had separate types — now consolidated)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Organization name |
| `types` | string[] | yes | `["organization"]` |
| `data.org_type` | string | no | `company`, `band`, `university`, `government`, `nonprofit`, `group` |
| `data.founded` | year | no | Year founded |
| `data.url` | string | no | Website |

**OGP equivalent:** `og:type="business.business"` (partial), or historical types

**Note:** Groups (Facebook Groups, Google Groups, etc.) are `organization` with `org_type: group`.

---

#### `website`
Default web page type.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Site/page title |
| `types` | string[] | yes | `["website"]` |
| `data.url` | string | yes | URL |
| `data.description` | string | no | Description |

**OGP equivalent:** `og:type="website"` (default)

---

### Our Additions (OGP Gaps)

#### `event`
A calendar event, meeting, scheduled occurrence. OGP never had this.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Event title |
| `types` | string[] | yes | `["event"]` |
| `data.start` | datetime | yes | Start time |
| `data.end` | datetime | no | End time |
| `data.location` | string | no | Location name |
| `data.description` | string | no | Description |
| `data.recurrence` | string | no | RFC 5545 RRULE |

**References:** Google Calendar, Facebook Events (Graph API), Schema.org Event

---

#### `place`
A location. OGP 1.0 had `city`, `country`, `landmark` — now deprecated.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Place name |
| `types` | string[] | yes | `["place"]` |
| `data.place_type` | string | no | `city`, `country`, `venue`, `landmark` |
| `data.latitude` | number | no | Latitude |
| `data.longitude` | number | no | Longitude |
| `data.address` | string | no | Street address |

**References:** Google Maps, OGP 1.0 place types

---

#### `concept`
An idea, pattern, methodology. Not in OGP.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Concept name |
| `types` | string[] | yes | `["concept"]` |
| `data.description` | string | no | Explanation |

**Status:** EXPERIMENTAL — see Joe's Hypotheses below.

---

## Personal Knowledge Types (Beyond OGP)

These types emerge from PKM research, Google Takeout analysis, and real-world usage patterns. OGP was designed for web content sharing — these fill gaps for personal knowledge management.

### `note`
Freeform personal capture. The atomic unit of PKM.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Title (can be auto-generated) |
| `types` | string[] | yes | `["note"]` |
| `data.content` | string | no | Note body (markdown) |
| `data.color` | string | no | Visual color coding |
| `data.pinned` | boolean | no | Pinned state |

**Research source:** Google Keep, Obsidian, PKM community research

---

### `task`
An action item with status, due date, and hierarchy.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Task title |
| `types` | string[] | yes | `["task"]` |
| `data.status` | string | yes | `pending`, `in_progress`, `completed`, `cancelled` |
| `data.due` | datetime | no | Due date |
| `data.completed_at` | datetime | no | When completed |
| `data.priority` | string | no | `high`, `medium`, `low` |

**Research source:** Google Tasks, Todoist, Things — all have: title, notes, due, status, parent, position

**Note:** Tasks have a lifecycle (pending → complete) and support subtask hierarchy via `part_of` relationships. Distinct from events (which have duration and attendees).

---

### `message`
A communication from one party to another.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Subject line (if any) |
| `types` | string[] | yes | `["message"]` |
| `data.content` | string | no | Message body |
| `data.sent_at` | datetime | yes | When sent |
| `data.channel` | string | no | `email`, `sms`, `chat`, `dm` |

**Research source:** Gmail (MBOX), Google Chat, Facebook Messages

**Relationships:**
- `from` → person (sender)
- `to` → person[] (recipients)
- `part_of` → conversation/thread
- `reply_to` → message (threading)
- `attachment` → file[]

---

### `conversation`
A container for related messages. Linkable and shareable.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Subject/title |
| `types` | string[] | yes | `["conversation"]` |
| `data.channel` | string | no | `email`, `slack`, `imessage`, `whatsapp` |
| `data.started_at` | datetime | no | First message time |

**Research source:** Gmail threads, Slack channels, WhatsApp groups, iMessage

---

### `thread`
A sub-conversation within a larger context. Distinct from `conversation`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Thread topic |
| `types` | string[] | yes | `["thread"]` |
| `data.channel` | string | no | Platform/context |

**Research source:** Reddit threads, YouTube comment threads, Slack threads, email threads

**Examples:**
- Reddit: A post spawns comment threads
- YouTube: A comment spawns reply threads  
- Slack: A message spawns a thread
- Email: Replies create a thread (via In-Reply-To headers)
- iMessage: Inline replies create sub-threads

**Relationships:**
- `part_of` → conversation (parent context)
- `started_by` → message (root message)
- Messages `part_of` → thread

---

### `quote`
A notable saying with speaker attribution and source provenance.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | The quote text |
| `types` | string[] | yes | `["quote"]` |
| `data.context` | string | no | When/where it was said |

**Research source:** Wikiquote, Goodreads, quote attribution patterns

**Critical distinction:**
- **Speaker** — Who said it (FDR)
- **Source** — Where you found it (a biography)
- **Author of source** — Who wrote the source (Jean Edward Smith, not FDR)

**Relationships:**
- `spoken_by` → person (the speaker)
- `appears_in` → work (the source where you found it)
- `authored_by` → person (author of the source, if different from speaker)

---

### `highlight`
A personal extraction from a source with position/context.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | The highlighted text |
| `types` | string[] | yes | `["highlight"]` |
| `data.position` | string | no | Location in source (page, timestamp, etc.) |
| `data.color` | string | no | Highlight color |

**Research source:** Kindle highlights, Readwise, Hypothesis, PDF annotations

**Relationships:**
- `extracted_from` → book/article/video (the source)
- `created_by` → person (who highlighted it)

**Distinction from quote:** A highlight is personal (you extracted it). A quote is canonical (attributed to a speaker).

---

### `comment`
A response to another entity (post, video, article, etc.).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Comment text (first line as name) |
| `types` | string[] | yes | `["comment"]` |
| `data.content` | string | yes | Full comment text |
| `data.posted_at` | datetime | yes | When posted |

**Research source:** YouTube, Facebook, Reddit, blog comments

**Relationships:**
- `comment_on` → any (what it's responding to)
- `authored_by` → person
- `reply_to` → comment (for nested comments)

---

## Proposed Types (Research Complete, Pending Approval)

Based on subagent research (2026-01-24). These have been researched but not yet added to the schema.

### `podcast.show`

The podcast series — analogous to `video.tv_show`. Following OGP dot notation.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Show title |
| `types` | string[] | yes | `["podcast.show"]` |
| `data.description` | string | no | Show description |
| `data.author` | string | no | Primary creator/host name |
| `data.show_type` | enum | no | `episodic` (any order) or `serial` (sequential) |
| `data.explicit` | boolean | no | Contains explicit content |
| `data.language` | string | no | ISO language code |
| `data.category` | string[] | no | Apple Podcasts categories |
| `data.image` | string | no | Artwork URL |
| `data.feed_url` | string | no | RSS feed URL |
| `data.website` | string | no | Show website |

**Research source:** Apple Podcasts RSS, Spotify API, Podcast 2.0 namespace, Schema.org PodcastSeries

**Relationships:**
- Episodes `part_of` → show
- `host_of` → person (with role)
- `published_by` → organization (podcast network)

---

### `podcast.episode`

A single episode — analogous to `video.episode`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Episode title |
| `types` | string[] | yes | `["podcast.episode"]` |
| `data.description` | string | no | Show notes |
| `data.duration` | integer | no | Length in seconds |
| `data.published` | datetime | no | Release date |
| `data.episode_number` | integer | no | Episode number |
| `data.season_number` | integer | no | Season number |
| `data.episode_type` | enum | no | `full`, `trailer`, or `bonus` |
| `data.audio_url` | string | no | Enclosure URL (MP3/M4A) |
| `data.transcript_url` | string | no | Transcript file URL |
| `data.guid` | string | no | RSS GUID for import tracking |

**Research source:** Apple Podcasts RSS, Spotify API, Podcast 2.0 namespace, Schema.org PodcastEpisode

**Relationships:**
- `part_of` → podcast.show
- `host_of` → person
- `guest_on` → person

**Import:** Parse RSS with iTunes + Podcast 2.0 namespaces. Store original RSS in `data.rss`.

---

### `review`

A user assessment of another entity with an optional rating.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Review title/headline |
| `types` | string[] | yes | `["review"]` |
| `data.content` | string | no | Review body text |
| `data.rating` | number | no | Rating value (e.g., 4) |
| `data.rating_max` | number | no | Scale maximum (e.g., 5) |
| `data.posted_at` | datetime | yes | When posted |
| `data.helpful_count` | integer | no | Helpful/useful votes |
| `data.verified` | boolean | no | Verified purchase/experience |
| `data.spoiler` | boolean | no | Contains spoilers |
| `data.aspect` | string | no | What facet is rated (food, service) |
| `data.pros` | string[] | no | Positive points |
| `data.cons` | string[] | no | Negative points |

**Research source:** Schema.org Review, Amazon, Goodreads, IMDB, Yelp, Rotten Tomatoes

**Relationships:**
- `review_of` → any (what's being reviewed: book, movie, product, place)
- `authored_by` → person

**Why not `comment`?** Reviews have structured rating data, engagement metrics (helpful votes), verification flags, and aggregate into ratings. Comments are just text.

**Aggregate ratings:** Computed from individual reviews, not stored separately.

---

### `activity` — REJECTED

**Recommendation:** Do NOT add `activity` as an entity type.

**Reasoning:**
1. Most activities are already captured implicitly:
   - Highlights have `created_by` and `created_at`
   - Comments have `comment_on` and `posted_at`
   - Messages have `sent_at` and sender/recipient relationships
2. Relationships with timestamps cover most cases (e.g., `joe --[watched, {at: "2026-01-24"}]--> movie_x`)
3. Schema.org's 100+ Action types is over-engineered
4. Follows the "compute don't store" principle from FamilySearch

**Alternative:** Use timestamped relationship types:
- `watched` with `{at, duration, completion}`
- `listened_to` with `{at, duration, play_count}`
- `read` with `{at, started_at, finished_at}`

**Exception:** If we need play counts/aggregations, consider specific types (`music.listen`) not generic `activity`.

---

## Threading Research Summary

**Recommendation:** Keep both `conversation` and `thread` — they serve different purposes.

| Type | Use Case | Example |
|------|----------|---------|
| `conversation` | Top-level venue | Email inbox, Slack channel, WhatsApp group |
| `thread` | Discussion topic/sub-conversation | Slack thread, Reddit post, email thread |

**Key insight:** The distinction is containment hierarchy:
- `conversation` = the venue (channel, chat, inbox)
- `thread` = the discussion (may be the whole conversation or a sub-part)

**Universal relationship:** `reply_to` is the primitive across all platforms.

**Platform mapping examples:**
- Reddit: Post is `[thread]`, comments `reply_to` each other, `part_of` the post
- Slack: Channel is `[conversation]`, threaded replies spawn `[thread]` entities
- Email: Mailbox is `[conversation]`, JWZ-reconstructed chains are `[thread]` entities

**Store platform-specific metadata in `data.threading`:**
```json
{
  "data": {
    "threading": {
      "platform": "slack",
      "thread_ts": "1234567890.000000"
    }
  }
}
```

---

## Entity Gap Analysis (2026-01-24)

Cross-referencing our schema against research from Google Takeout, Facebook Graph, Schema.org, OGP, and PKM community.

### Tier 1: Added Above (High Confidence)

| Entity | Research Source | Notes |
|--------|-----------------|-------|
| `note` | Google Keep, PKM research | Freeform capture — different from structured `article` |
| `task` | Google Tasks, PKM research | Has status, due, subtask hierarchy, lifecycle |
| `message` | Gmail, Chat, Facebook | Has from/to, thread relationship, attachments |
| `conversation` | Gmail threads, Slack, WhatsApp | Container for messages — linkable |
| `thread` | Reddit, YouTube, Slack, email | Sub-conversations within conversations |
| `quote` | README, Wikiquote | Speaker vs author vs source distinction |
| `highlight` | Readwise, Kindle, Hypothesis | Personal extraction with position |
| `comment` | YouTube, Facebook, Reddit | Response entity, supports nesting |

### Tier 2: Under Consideration

| Entity | Research Source | Question | Current Thinking |
|--------|-----------------|----------|------------------|
| `channel` | YouTube, Podcasts | Distinct type or `organization` with `org_type: channel`? | Probably `organization` |
| `podcast` / `podcast.episode` | Google Takeout, web content | Missing from OGP — growing content category | Likely needed |
| `post` | Facebook Graph | Social media posts — is this just `article` subtype? | Probably `article` with `data.format: post` |
| `group` | Facebook, Google Groups | Distinct or `organization` with `org_type: group`? | **Decided:** `organization` with `org_type: group` |
| `review` | Google, Schema.org | User assessment of another entity | Likely needed |
| `recipe` | Schema.org (popular type) | Common web content | Probably `article` with structure |
| `visit` | Google Timeline | Location stay with duration | Maybe `event` subtype? |
| `activity` | Google My Activity | User action with timestamp | Schema.org has 100+ Action types — avoid? |

### Tier 3: Probably Not Separate Types

| Entity | Why Skip | Alternative |
|--------|----------|-------------|
| `album` (photo) | Covered by relationships | `photo` `part_of` collection entity |
| `device` | Rare use case | `product` with subtype |
| `health_record` | Very domain-specific | `data.health` on generic entities |
| `tag` / `label` | Implementation detail | Properties, not entities |
| `file` | Too generic | Use specific types (`note`, `photo`, etc.) or `data.file_path` |

---

## Joe's Hypotheses (To Challenge Later)

### On `concept` type

**Hypothesis:** `concept` as an explicit type may be wrong. Concepts are abstractions that emerge from clustering and relationships in the graph, not atomic entities you create directly.

**Current thinking:** Keep `concept` for now but mark as experimental. Ideas, methodologies, and patterns might be better represented as:
- Tags/properties on other entities
- Emergent clusters from graph analysis
- Notes that evolve into something more structured

**Open question:** What makes something a "concept" vs a well-linked "note"?

### On `note` vs `article`

**Hypothesis:** Everything published started as a note. Publishing is a relationship, not a type change.

- A `note` becomes "published" when it has `published_to` relationships
- An `article` on the web is just a note with `data.url` and `published_to: website`
- This unifies personal capture with published content

**Implication:** Maybe `article` is redundant? Or `article` is specifically for web imports where we don't have the original note?

### On threading

**Hypothesis:** Threading is more complex than a single `conversation` type suggests.

- Reddit: post → comments → replies (tree structure)
- Email: messages → thread (linear with quotes)
- Slack: channel → messages → threads (two-level)
- iMessage: conversation → messages → inline threads (emerging)
- YouTube: video → comments → replies (two-level)

**Current approach:** `conversation` and `thread` as separate types, connected via `part_of`. Threads can be part of conversations. Messages can be part of threads or directly part of conversations.

### On `related_to`

**Hypothesis:** `related_to` is too vague to be useful. Every relationship should have a specific type.

- If we can't name the relationship, we don't understand it yet
- Better to have many specific types than one catch-all
- Exception: AI-extracted relationships where type is uncertain (use with `confidence`)

**For family relationships specifically:** Joe said "related_to is bullshit" — FamilySearch proves you only need two primitives (`couple`, `parent_child`) and compute everything else.

---

## OGP Import Pipeline

When importing from web:

1. **Extract `og:*` meta tags** from page
2. **Map `og:type` to our type**
3. **Create entity** with `data.og` containing original OGP data
4. **Extract relationships** (article:author → created_by, etc.)

### Type Mapping

| OGP Type | Our Type |
|----------|----------|
| `website` | `website` |
| `article` | `article` |
| `book` | `book` |
| `profile` | `person` |
| `video.movie` | `video.movie` |
| `video.episode` | `video.episode` |
| `video.tv_show` | `video.tv_show` |
| `music.song` | `music.song` |
| `music.album` | `music.album` |
| `music.playlist` | `music.playlist` |
| `product` | `product` |
| `business.business` | `organization` |

---

## Research Summary

### Key Findings (2026-01-24)

**Entity-first is validated:**
- Neo4j, Dgraph use flat labels (no inheritance)
- Wikidata's hierarchy is documented as problematic
- OGP's flat approach has 69.8% web adoption

**OGP as foundation:**
- 17 types cover 70% of web
- Simplicity was intentional design choice
- Import-friendly for web data

**OGP gaps we fill:**
- `event` — never existed
- `place` — deprecated from 1.0
- `organization` — consolidated from 6 types into `business.business`

**Beyond OGP (PKM/Personal Data):**
- `note`, `task`, `message`, `conversation`, `thread` — core PKM types
- `quote`, `highlight`, `comment` — content extraction and response

### Key People Who Built These Systems

| Person | System | Known For |
|--------|--------|-----------|
| Bret Taylor | OGP | Open Graph Protocol, Like button |
| David Recordon | OGP | OGP design decisions |
| R.V. Guha | Schema.org | CycL, RSS, RDF, Schema.org |
| John Giannandrea | Knowledge Graph | Built Google KG |
| Nathan Bronson | TAO | Facebook's graph database |

---

## References

- [Open Graph Protocol](https://ogp.me/) — 69.8% web adoption, our primary influence
- [Schema.org](https://schema.org/) — Reference only (avoid hierarchy)
- [Wikidata](https://www.wikidata.org/) — Q-numbers for identity
- [Neo4j](https://neo4j.com/) — Flat labels, entity-first
- [TAO Paper](https://www.usenix.org/conference/atc13/technical-sessions/presentation/bronson) — Facebook's graph store

---

## Related Files

- **schema-relationships.md** — Relationship types and patterns
- **SEED_DATA.md** — Sample entities to populate
- **research/** — Deep dives on specific systems

---

## Research Proposals (2026-01-24)

> **Divergent thinking phase.** Everything from Google Takeout and Facebook Graph research goes here. We'll converge and cull later.

### Media Entity Types

These fill gaps in OGP's content types, especially for audio and newer media formats.

#### `podcast.show` ✅ (Already proposed above)

#### `podcast.episode` ✅ (Already proposed above)

#### `photo`
A photograph. Distinct from generic `file` — has geo, faces, albums.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Filename or caption |
| `types` | string[] | yes | `["photo"]` |
| `data.taken_at` | datetime | no | Photo timestamp |
| `data.latitude` | number | no | GPS latitude |
| `data.longitude` | number | no | GPS longitude |
| `data.width` | number | no | Width in pixels |
| `data.height` | number | no | Height in pixels |
| `data.camera` | string | no | Camera/device |

**Research source:** Google Photos, Facebook Photo, Instagram IG Media

**Relationships:**
- `appears_in` ← person (faces)
- `part_of` → album
- `taken_at` → place

---

#### `video`
A video file. Already partially covered by OGP's `video.*` but we may need a standalone type for user-generated content.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Title |
| `types` | string[] | yes | `["video"]` |
| `data.duration` | integer | no | Length in seconds |
| `data.thumbnail` | string | no | Thumbnail URL |
| `data.width` | number | no | Width in pixels |
| `data.height` | number | no | Height in pixels |

**Research source:** YouTube, Google Photos, Facebook Video, Instagram IG Media (VIDEO type)

**Open question:** Is this redundant with `video.movie`, `video.episode`? Maybe `video` is the generic type, and `video.movie` etc. are specific forms?

---

#### `audio`
An audio file or recording. Not well-covered by OGP (only `music.*`).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Title/filename |
| `types` | string[] | yes | `["audio"]` |
| `data.duration` | integer | no | Length in seconds |
| `data.transcript` | string | no | Transcription text |

**Research source:** Google Voice (voicemails), Threads (AUDIO type), Google Recorder

**Use cases:** Voice memos, voicemails, audio messages, recordings.

---

### Communication Entity Types

#### `phone_call`
A voice call record. Distinct from `message` — has duration, no text content.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Auto-generated ("Call with X") |
| `types` | string[] | yes | `["phone_call"]` |
| `data.direction` | enum | yes | `inbound`, `outbound`, `missed` |
| `data.duration` | integer | no | Length in seconds |
| `data.started_at` | datetime | yes | Call start time |

**Research source:** Google Voice

**Relationships:**
- `from` → person (caller)
- `to` → person (recipient)
- `recording` → audio (if recorded)

---

#### `voicemail`
A voicemail message with audio and transcription.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Auto-generated or first line of transcript |
| `types` | string[] | yes | `["voicemail"]` |
| `data.transcript` | string | no | Transcription text |
| `data.duration` | integer | no | Length in seconds |
| `data.received_at` | datetime | yes | When received |

**Research source:** Google Voice

**Relationships:**
- `from` → person (caller)
- `to` → person (recipient)
- `audio_file` → audio

**Open question:** Is this just `message` with `channel: voicemail` and an audio attachment? Or distinct enough to be its own type?

---

### Commerce & Transaction Entity Types

#### `order`
An e-commerce order/purchase.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Order number or summary |
| `types` | string[] | yes | `["order"]` |
| `data.order_number` | string | no | External order ID |
| `data.status` | enum | no | `processing`, `shipped`, `delivered`, `cancelled` |
| `data.total` | number | no | Total amount |
| `data.currency` | string | no | ISO currency code |
| `data.ordered_at` | datetime | yes | Order timestamp |

**Research source:** Gmail schema.org parsing (schema.org/Order), Google Play Store

**Relationships:**
- `contains` → product[] (line items)
- `purchased_by` → person
- `sold_by` → organization (merchant)
- `shipped_via` → delivery

---

#### `reservation`
A booking for a future event/service.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Reservation summary |
| `types` | string[] | yes | `["reservation"]` |
| `data.reservation_type` | enum | no | `flight`, `hotel`, `restaurant`, `event`, `car` |
| `data.confirmation_number` | string | no | Booking reference |
| `data.status` | enum | no | `confirmed`, `cancelled`, `pending` |
| `data.start_time` | datetime | no | Check-in/arrival time |
| `data.end_time` | datetime | no | Check-out/departure time |

**Research source:** Gmail schema.org parsing (FlightReservation, HotelReservation, etc.)

**Relationships:**
- `reserved_for` → person
- `at` → place (venue/hotel)
- `for` → event (if event reservation)

---

#### `delivery`
A package shipment being tracked.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | "Package from X" |
| `types` | string[] | yes | `["delivery"]` |
| `data.tracking_number` | string | no | Carrier tracking ID |
| `data.carrier` | string | no | FedEx, UPS, USPS, etc. |
| `data.status` | enum | no | `in_transit`, `out_for_delivery`, `delivered` |
| `data.expected_by` | datetime | no | Expected delivery date |
| `data.delivered_at` | datetime | no | Actual delivery time |

**Research source:** Gmail schema.org parsing (ParcelDelivery)

**Relationships:**
- `part_of` → order
- `delivered_to` → place (address)
- `shipped_by` → organization (carrier)

---

#### `transaction`
A financial transaction (payment, transfer).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Transaction description |
| `types` | string[] | yes | `["transaction"]` |
| `data.amount` | number | yes | Amount |
| `data.currency` | string | yes | ISO currency code |
| `data.direction` | enum | yes | `credit`, `debit` |
| `data.timestamp` | datetime | yes | When occurred |
| `data.method` | string | no | Card, bank, etc. |

**Research source:** Google Pay/Wallet

**Relationships:**
- `from` → person/organization
- `to` → person/organization
- `for` → order/product

---

### Pass & Credential Entity Types

Google Wallet's Class-Object pattern is interesting: templates (Class) vs instances (Object). We might adopt this.

#### `pass`
Generic digital pass. Could be subtyped or use `pass_type` discriminator.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Pass title |
| `types` | string[] | yes | `["pass"]` |
| `data.pass_type` | enum | no | `boarding_pass`, `event_ticket`, `loyalty`, `transit`, `coupon`, `generic` |
| `data.barcode` | string | no | Barcode/QR data |
| `data.barcode_type` | enum | no | `QR_CODE`, `AZTEC`, `PDF_417`, `CODE_128` |
| `data.valid_from` | datetime | no | Start of validity |
| `data.valid_until` | datetime | no | End of validity |
| `data.status` | enum | no | `active`, `expired`, `redeemed`, `void` |

**Research source:** Google Wallet (EventTicketObject, LoyaltyObject, TransitObject, FlightObject)

**Relationships:**
- `held_by` → person
- `issued_by` → organization
- `for_event` → event (if event ticket)
- `for_transit` → transit route/line

**Open question:** Should we have separate types (`boarding_pass`, `event_ticket`, `loyalty_card`) or one `pass` with discriminator? Google uses separate types. Leaning toward discriminator for simplicity.

---

#### `loyalty_card` (Alternative to pass discriminator)
Rewards program membership.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Program name |
| `types` | string[] | yes | `["loyalty_card"]` |
| `data.member_id` | string | no | Membership number |
| `data.points_balance` | integer | no | Current points |
| `data.tier` | string | no | Membership tier |

**Research source:** Google Wallet LoyaltyObject

**Relationships:**
- `held_by` → person
- `program_of` → organization

---

### Content Organization Entity Types

#### `blog`
A blog container. Holds posts.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Blog title |
| `types` | string[] | yes | `["blog"]` |
| `data.description` | string | no | Blog description |
| `data.url` | string | no | Blog URL |

**Research source:** Blogger (Blog resource)

**Relationships:**
- `authored_by` → person
- `published_by` → organization
- Contains posts via `part_of` relationship

---

#### `post`
A social media post or blog post. Distinct from `article`?

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Title (if any) |
| `types` | string[] | yes | `["post"]` |
| `data.content` | string | no | Post text |
| `data.posted_at` | datetime | yes | Publication time |
| `data.platform` | string | no | Source platform |
| `data.permalink` | string | no | Permanent URL |

**Research source:** Facebook Post, Blogger Post, Instagram IG Media, Threads Post

**Relationships:**
- `authored_by` → person
- `part_of` → blog/page/group
- `comment_on` ← comment[]
- `mentions` → person[]
- `tagged_at` → place

**Open question:** Is `post` redundant with `article`? Maybe:
- `article` = long-form, has title, structured (news, essays, blog posts)
- `post` = short-form, social media, ephemeral (tweets, status updates)

---

#### `saved_item`
A bookmarked/saved piece of content.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Title of saved item |
| `types` | string[] | yes | `["saved_item"]` |
| `data.url` | string | no | Source URL |
| `data.note` | string | no | User annotation |
| `data.saved_at` | datetime | yes | When saved |

**Research source:** Google Saved, Chrome Bookmarks, Facebook Saved

**Relationships:**
- `saved_by` → person
- `saved_from` → webpage/article
- `part_of` → collection

---

#### `collection`
A user-created grouping of items.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Collection name |
| `types` | string[] | yes | `["collection"]` |
| `data.description` | string | no | Description |

**Research source:** Google Saved (collections), Chrome bookmark folders, Facebook Collections

**Relationships:**
- `created_by` → person
- Contains items via `part_of` relationship

---

### Location & Activity Entity Types

#### `visit`
A stay at a location with duration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Auto-generated from place name |
| `types` | string[] | yes | `["visit"]` |
| `data.arrived_at` | datetime | yes | Arrival time |
| `data.departed_at` | datetime | no | Departure time |
| `data.confidence` | number | no | 0-100 confidence score |

**Research source:** Google Timeline (placeVisit)

**Relationships:**
- `visitor` → person
- `at` → place

**Open question:** Is this an `event` subtype? Or distinct because it's inferred/tracked rather than scheduled?

---

#### `trip` / `activity_segment`
A movement between places (transit, walk, drive).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Auto-generated |
| `types` | string[] | yes | `["trip"]` |
| `data.mode` | enum | no | `walking`, `driving`, `transit`, `cycling`, `flying` |
| `data.started_at` | datetime | yes | Start time |
| `data.ended_at` | datetime | no | End time |
| `data.distance` | number | no | Distance in meters |

**Research source:** Google Timeline (activitySegment)

**Relationships:**
- `traveler` → person
- `from` → place (origin)
- `to` → place (destination)

---

### Social Entity Types (from Facebook)

#### `reaction`
A typed response to content (beyond simple like).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Reaction type name |
| `types` | string[] | yes | `["reaction"]` |
| `data.reaction_type` | enum | yes | `like`, `love`, `haha`, `wow`, `sad`, `angry`, `care` |
| `data.reacted_at` | datetime | yes | When reacted |

**Research source:** Facebook Reactions

**Open question:** Is this better modeled as a relationship with metadata rather than an entity? e.g., `person --[reacted_to {type: "love", at: "..."}]--> post`

Leaning toward relationship, not entity. Reactions don't have identity beyond the relationship.

---

#### `hashtag`
A discoverable tag.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Tag text (without #) |
| `types` | string[] | yes | `["hashtag"]` |

**Research source:** Instagram IG Hashtag, Twitter

**Relationships:**
- `tagged_with` ← post/photo/video

**Open question:** Is this an entity or just a property/label? Instagram treats it as an entity with its own ID. But for us, maybe `data.hashtags: ["tag1", "tag2"]` on content is simpler?

---

### Meta/Platform Entity Types

#### `app`
A software application.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | App name |
| `types` | string[] | yes | `["app"]` |
| `data.developer` | string | no | Developer name |
| `data.platform` | enum | no | `android`, `ios`, `web`, `desktop` |
| `data.version` | string | no | Current version |
| `data.category` | string | no | App category |

**Research source:** Google Play Store (App)

**Relationships:**
- `developed_by` → organization
- `installed_by` → person (relationship with device)

**Open question:** Is this just `product` with `product_type: app`? Probably yes.

---

### Device Entity Type

#### `device`
A hardware device.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | yes | Device name |
| `types` | string[] | yes | `["device"]` |
| `data.device_type` | enum | no | `phone`, `tablet`, `computer`, `tv`, `speaker` |
| `data.manufacturer` | string | no | Manufacturer |
| `data.model` | string | no | Model name |

**Research source:** Google Play Store (Devices), Google Home

**Relationships:**
- `owned_by` → person
- `runs` → app[]

**Open question:** Is this `product` with properties? Devices have serial numbers, OS versions, installed apps — more than typical products. Probably worth keeping separate.

---

### Health Entity Types (Low Priority)

#### `workout`
An exercise session.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string | yes | NanoID |
| `name` | string | no | Workout type/name |
| `types` | string[] | yes | `["workout"]` |
| `data.activity_type` | enum | no | `running`, `cycling`, `swimming`, `walking`, `gym` |
| `data.started_at` | datetime | yes | Start time |
| `data.ended_at` | datetime | no | End time |
| `data.duration` | integer | no | Duration in seconds |
| `data.distance` | number | no | Distance in meters |
| `data.calories` | number | no | Calories burned |

**Research source:** Google Fit

**Relationships:**
- `performed_by` → person
- `at` → place (gym, route)

---

### Summary: Proposed Entity Types (Comprehensive)

| Category | Types | Status |
|----------|-------|--------|
| **Core (OGP)** | article, book, person, website, product, event, place, organization, concept | ✅ Defined |
| **Music (OGP)** | music.song, music.album, music.playlist | ✅ Defined |
| **Video (OGP)** | video.movie, video.episode, video.tv_show | ✅ Defined |
| **PKM** | note, task, message, conversation, thread, quote, highlight, comment | ✅ Defined |
| **Podcast** | podcast.show, podcast.episode | ✅ Proposed |
| **Review** | review | ✅ Proposed |
| **Media** | photo, video (generic), audio | 🆕 Proposed |
| **Communication** | phone_call, voicemail | 🆕 Proposed |
| **Commerce** | order, reservation, delivery, transaction | 🆕 Proposed |
| **Passes** | pass (with discriminator) OR boarding_pass, event_ticket, loyalty_card, transit_pass | 🆕 Proposed |
| **Content Org** | blog, post, saved_item, collection | 🆕 Proposed |
| **Location** | visit, trip | 🆕 Proposed |
| **Platform** | app, device | 🆕 Proposed (maybe product subtypes) |
| **Health** | workout | 🆕 Low priority |

### Open Design Questions

1. **`post` vs `article`** — Are these distinct types or is `post` just short-form `article`?

2. **`photo` vs `video` vs generic media** — Separate types or one `media` type with discriminator?

3. **`pass` types** — One `pass` with `pass_type` discriminator or separate types?

4. **Reactions as entities or relationships?** — Leaning toward relationships with metadata.

5. **Hashtags as entities or properties?** — Leaning toward properties on content.

6. **`app` and `device`** — Subtypes of `product` or distinct?

7. **`visit` and `trip`** — Are these `event` subtypes or distinct?

8. **`voicemail`** — Is this `message` with channel/attachment or distinct?

---

## Key Design Patterns from Research

### 1. Class-Object Pattern (Google Wallet)
Separate **templates** (shared structure) from **instances** (individual items). Could apply to:
- Event tickets (event class → individual tickets)
- Loyalty programs (program → memberships)
- Subscriptions (plan → user subscriptions)

### 2. Vertical-Specific Namespaces (OGP)
Use dot notation for domain-specific types: `music.song`, `video.movie`, `podcast.episode`. Keeps types flat while grouping related concepts.

### 3. Discriminator Fields
Instead of many types, use one type with a discriminator:
- `message` with `channel: email|chat|sms|voicemail`
- `media` with `media_type: photo|video|audio`
- `pass` with `pass_type: boarding_pass|event_ticket|loyalty`

### 4. Schema.org Alignment
Gmail parses schema.org from emails. Our types should map cleanly:
- `order` ↔ schema.org/Order
- `reservation` ↔ schema.org/Reservation
- `delivery` ↔ schema.org/ParcelDelivery

### 5. Activity as Meta-Entity
Google's My Activity provides cross-product activity records. Pattern:
```json
{
  "header": "product_name",
  "title": "action description", 
  "time": "timestamp",
  "products": ["source_products"]
}
```

We rejected `activity` as a type, but the pattern of "timestamped action on entity" is valuable — model as relationships with timestamps.

### 6. Container vs Content
Facebook distinguishes:
- **Containers:** Group, Album, Event, Page (have members/items)
- **Content:** Post, Photo, Video, Comment (created by actors)

Our parallel:
- **Containers:** conversation, thread, collection, blog, album
- **Content:** message, note, article, photo, comment

---

## Design Principles from Research (2026-01-24)

> **Synthesis of key learnings across all research sources.** These principles should guide the convergence phase.

### Principle 1: Entity-First, Not Hierarchical

**Source:** Neo4j, Dgraph, OGP, Wikidata critique

- Types are labels, not classes
- No inheritance trees (avoid Schema.org's 827-type hierarchy)
- Entities can have multiple types
- Flat structure with dot-notation grouping (OGP pattern: `music.song`, `video.movie`)

### Principle 2: OGP as Foundation, Fill the Gaps

**Source:** OGP research, web adoption data (69.8%)

- OGP's 17 types cover 70% of web content
- Fill gaps: `event`, `place`, `organization` (deprecated from OGP 1.0)
- Add PKM types: `note`, `task`, `message`, `conversation`, `thread`
- Preserve original OGP data in `data.og` on import

### Principle 3: Discriminator Fields Over Type Proliferation

**Source:** Google Wallet, OGP, Schema.org lessons

- One `pass` type with `pass_type: boarding_pass | event_ticket | loyalty`
- One `message` type with `channel: email | chat | sms`
- One `media` type with `media_type: photo | video | audio`
- Keeps type count manageable, properties flexible

### Principle 4: Class-Object Pattern for Templates

**Source:** Google Wallet

- Separate shared templates (Class) from individual instances (Object)
- Event ticket: EventTicketClass (venue, date) + EventTicketObject (seat, holder)
- Useful for: tickets, loyalty programs, subscriptions

### Principle 5: Schema.org Alignment for Import

**Source:** Gmail, schema.org research

- Gmail parses schema.org from emails (Order, FlightReservation, ParcelDelivery)
- Our types should map cleanly for import
- Supports web data extraction via JSON-LD

### Principle 6: Index Layer, Not File System Replacement

**Source:** WinFS post-mortem, Spotlight success, Baloo

- Don't build a "semantic file system"
- Build an index/query layer over existing files
- Purpose-built storage per entity type
- Graceful degradation if indexing fails

### Principle 7: AI Extracts, Humans Confirm

**Source:** PKM community research, semantic file systems

- Manual tagging fails at scale (users abandon after months)
- AI extraction is consistent regardless of user state
- Extracted entities carry `confidence` scores
- Humans confirm important entities

### Principle 8: Simplicity Wins Adoption

**Source:** OGP vs Schema.org, FOAF, CommonMark vs full Markdown

- OGP: 4 required properties, 69.8% adoption
- Schema.org: 827 types, 52.6% adoption (despite Google backing)
- Simple vocabularies get adopted; complex ones don't
- Start minimal, extend later

---

## Entity Type Summary (Pre-Convergence)

### Tier 1: Core Types (High Confidence)

| Category | Types | Source |
|----------|-------|--------|
| **Core (OGP)** | article, book, person, website, product | OGP spec |
| **OGP Gaps** | event, place, organization, concept | OGP 1.0 + our additions |
| **Music (OGP)** | music.song, music.album, music.playlist | OGP spec |
| **Video (OGP)** | video.movie, video.episode, video.tv_show | OGP spec |

### Tier 2: PKM Types (High Confidence)

| Category | Types | Source |
|----------|-------|--------|
| **PKM Core** | note, task, message, conversation, thread | PKM research, Google Takeout |
| **Content** | quote, highlight, comment, review | Readwise, Goodreads, YouTube |
| **Podcast** | podcast.show, podcast.episode | Apple Podcasts, Spotify |

### Tier 3: Extended Types (Medium Confidence)

| Category | Types | Source |
|----------|-------|--------|
| **Media** | photo, video (generic), audio | Google Photos, YouTube |
| **Communication** | phone_call, voicemail | Google Voice |
| **Commerce** | order, reservation, delivery, transaction | Gmail schema.org |
| **Passes** | pass (with discriminator) | Google Wallet |
| **Content Org** | blog, post, saved_item, collection | Blogger, Google Saved |
| **Location** | visit, trip | Google Timeline |

### Tier 4: Low Priority / Maybe Later

| Entity | Status | Notes |
|--------|--------|-------|
| device | Maybe | Could be `product` with properties |
| app | Maybe | Could be `product` with `product_type: app` |
| workout | Low priority | Domain-specific |
| reaction | Skip | Model as relationship with metadata |
| hashtag | Skip | Model as property on content |

---

## Universal Metadata Patterns (2026-01-24)

> **Abstracted from FamilySearch/GEDCOM research.** These patterns apply universally across entities, relationships, and properties — not just genealogy.

### Open Question: Granularity Level

**Where do we apply these patterns?**

| Level | Meaning | Example |
|-------|---------|---------|
| **Entity-level** | One provenance/evidence per entity | "This person came from GEDCOM import" |
| **Property-level** | Each property has its own metadata | "Birthdate from census (secondary), death date from certificate (primary)" |

**FamilySearch does property-level** — each fact has its own sources, confidence, status.

**Current leaning:** Property-level (more granular, more accurate, FamilySearch-proven pattern)

**Tradeoff:** More complexity, but better fidelity. Worth it for knowledge graphs where source quality matters.

---

### Pattern 1: Evidence Quality

**Source:** FamilySearch QUAY system, GEDCOM X

Two orthogonal dimensions:

| Dimension | What it measures | Scale |
|-----------|------------------|-------|
| **Quality** | How good is the underlying evidence? | 0-3 (unreliable → primary) |
| **Confidence** | How certain are we this is true? | 0.0-1.0 |

**Why both matter:**

| Scenario | Quality | Confidence |
|----------|---------|------------|
| Tabloid article claims X | Low (unreliable source) | High (we know what it says) |
| Damaged primary document | High (original source) | Low (barely readable) |
| AI extraction from reliable source | High | Medium (AI uncertainty) |
| Bible says event X happened | Low (religious text) | High (text clearly states it) |

**Schema:**

```yaml
evidence:
  quality: enum
    - 0: unreliable    # Hearsay, rumors, unverified
    - 1: questionable  # Circumstantial, secondary interpretation
    - 2: secondary     # Derived from primary, official but not original
    - 3: primary       # Original document, firsthand account
  confidence: float    # 0.0-1.0
  method: enum
    - manual           # Human entered
    - imported         # From external source
    - ai_extracted     # AI determined
    - computed         # Derived from other data
    - inferred         # Logical inference
```

**Use cases:**
- Genealogy: Census record (quality: 2, secondary) vs birth certificate (quality: 3, primary)
- Research: Peer-reviewed paper (quality: 3) vs blog post (quality: 1)
- Investigation: Eyewitness account (quality: 3) vs rumor (quality: 0)
- AI: "Extracted with 85% confidence from a primary source"

---

### Pattern 2: Temporal Precision

**Source:** GEDCOM 7 date modifiers

Not all dates are exact. We need to represent uncertainty without forcing false precision.

**Schema:**

```yaml
temporal:
  # Core value
  value: datetime           # ISO 8601 (best approximation)
  
  # Precision modifier
  modifier: enum
    - exact                 # We know this precisely
    - about                 # ABT - approximately
    - estimated             # EST - educated guess
    - calculated            # CAL - computed from other data
    - before                # BEF - happened before this date
    - after                 # AFT - happened after this date
  
  # For ranges
  range:
    start: datetime
    end: datetime
    type: enum [between, from_to, or]  # BET, FROM/TO, OR
  
  # Original text (preserves source)
  original: string          # "about 1850", "Q2 2025", "during the Renaissance"
```

**Examples:**

| Scenario | Representation |
|----------|----------------|
| Exact date | `{ value: "2024-01-15", modifier: "exact" }` |
| Approximate | `{ value: "1850-01-01", modifier: "about", original: "about 1850" }` |
| Before | `{ value: "1900-01-01", modifier: "before", original: "before 1900" }` |
| Range | `{ range: { start: "1848", end: "1852", type: "between" }, original: "between 1848 and 1852" }` |
| Vague | `{ value: "1400-01-01", modifier: "about", original: "during the Renaissance" }` |

**Where this applies:**
- Birthdates, death dates (genealogy)
- Event dates (history, calendar)
- Publication dates (articles, books)
- Any temporal property in the schema

---

### Pattern 3: Provenance (Source Attribution)

**Source:** FamilySearch source citations, GEDCOM X

Everything should be traceable to where it came from.

**Schema:**

```yaml
provenance:
  source: entity_id | url | text   # What's the source?
  contributor: entity_id           # Who added this? (person or system)
  method: enum                     # How was it determined?
    - manual
    - imported
    - ai_extracted
    - computed
    - inferred
  created_at: datetime             # When was it added?
  modified_at: datetime            # When was it last changed?
  quality: 0-3                     # Evidence quality (from Pattern 1)
  status: enum                     # Verification status
    - unverified                   # Not yet checked
    - verified                     # Human confirmed
    - challenged                   # Disputed
    - disproven                    # Known to be false
```

**Examples:**

| Scenario | Provenance |
|----------|------------|
| Manual entry | `{ contributor: "user_joe", method: "manual", status: "verified" }` |
| Web import | `{ source: "https://...", method: "imported", quality: 2 }` |
| AI extraction | `{ method: "ai_extracted", contributor: "system", status: "unverified" }` |
| Computed | `{ method: "computed", source: "derived from parent relationships" }` |
| GEDCOM import | `{ source: "family.ged", method: "imported", contributor: "user_joe" }` |

**Where this applies:**
- Entities: "Where did we learn about this person/place/organization?"
- Relationships: "Who said these two things are connected?"
- Properties: "What's the source for this birthdate/event/claim?"

---

### Pattern 4: Aliases (Multiple Names)

**Source:** FamilySearch names with types, Facebook Graph

Any entity can have multiple names over time.

**Schema:**

```yaml
entity:
  name: string              # Canonical/display name
  names:
    - value: string         # The name
      type: enum            # Type of name
        - primary           # Main/current name
        - birth             # Name at birth
        - married           # Name after marriage
        - former            # Previous name
        - legal             # Legal/official name
        - nickname          # Informal name
        - alias             # Alternative name
        - stage             # Stage/pen name
        - dba               # "Doing business as" (organizations)
        - maiden            # Pre-marriage name
        - religious         # Religious/adopted name
      valid_from: temporal  # When this name started (optional)
      valid_until: temporal # When this name ended (optional)
      provenance: provenance # Where we learned this (optional)
```

**Examples:**

| Entity Type | Aliases |
|-------------|---------|
| Person | Birth name, married name, nickname, stage name, pen name |
| Organization | Legal name, DBA, abbreviation, former name ("Facebook" → "Meta") |
| Place | Official name, local name, historical name ("Peking" → "Beijing") |
| Product | Product name, SKU, model number, codename |

**Example person:**

```yaml
person:
  id: "abc123"
  name: "John Smith"  # Display name
  names:
    - value: "John Robert Smith"
      type: "birth"
    - value: "Johnny"
      type: "nickname"
    - value: "J.R. Smith"
      type: "professional"
    - value: "John Smith-Jones"
      type: "married"
      valid_from: { value: "2020-06-15", modifier: "exact" }
```

---

### Putting It Together

A fully-attributed property might look like:

```yaml
person:
  id: "abc123"
  name: "John Smith"
  
  birthdate:
    value:
      value: "1850-01-01"
      modifier: "about"
      original: "abt 1850"
    evidence:
      quality: 2           # Secondary (census record)
      confidence: 0.8
      method: "imported"
    provenance:
      source: "1850 US Census, Page 42"
      contributor: "user_joe"
      status: "verified"
```

This is verbose but captures exactly what we know and how we know it. For most properties, we'd use simpler representations and only add full attribution where it matters.

---

## Next Steps (Convergence Phase)

1. **Prioritize Tier 1 + Tier 2** — These are the core schema
2. **Resolve Open Design Questions** — See "Open Design Questions" section above
3. **Decide on discriminator patterns** — Which types use discriminators vs separate types?
4. **Define import mappings** — OGP → our types, schema.org → our types
5. **Decide on granularity level** — Entity-level vs property-level metadata (leaning property-level)
6. **Spec the data model** — SQLite schema, JSON representation
7. **Build seed data** — See `SEED_DATA.md`
