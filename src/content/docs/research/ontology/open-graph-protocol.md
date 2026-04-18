---
title: Open Graph Protocol Research
description: Facebook's protocol that turns any webpage into a "rich object" in a social graph.
---

## Why This Matters

The Open Graph Protocol (OGP) is arguably the most successful entity schema ever deployed. **69.8% of all websites use Open Graph** (W3Techs, Jan 2026), making it the dominant structured data format on the web. Every `og:type`, `og:title`, `og:image` tag follows this spec. It defines how arbitrary web content becomes typed objects with properties and relationships.

**Key insight:** OGP solved the "how do you type everything on the web?" problem with radical simplicity. We can learn from their type hierarchy and design philosophy.

---

## FINDINGS

### History & Origins

**April 21, 2010** — Mark Zuckerberg announced the Open Graph Protocol at Facebook's F8 developer conference, calling it "the most transformative thing we've ever done for the Web."

The initiative launched with three components:
1. **Social Plugins** (Like button) — Simple HTML embeds, one line of code
2. **Open Graph Protocol** — Metadata standard to turn web pages into graph objects  
3. **Graph API** — New developer platform

**Design Goal:** Developer simplicity. The protocol was designed so publishers could "copy and paste" meta tags.

**Within 7 days of launch:** Hosting services, libraries, and a WordPress plugin had been created.

### Influences

OGP was inspired by and builds on:
- **Dublin Core** — Foundational web metadata vocabulary
- **RDFa** — Embedding structured data in HTML (OGP is RDFa-based)
- **Microformats** — Lightweight semantic markup
- **link-rel canonical** — URL canonicalization

### Evolution Timeline

| Date | Event |
|------|-------|
| **April 2010** | OGP announced at F8 with Like button |
| **October 2009** | Open Graph API concept first unveiled |
| **January 2012** | OGP 1.1 released, reduced types from 39 to 12 |
| **October 2012** | Custom Open Graph actions deprecated (auto-posting) |
| **May 2019** | Open Graph Stories deprecated (render as plain links) |
| **August 2018** | `publish_actions` permission removed from Facebook Login |

**Notable:** OGP 1.0 defined **39 object types**. OGP 1.1 simplified to **12 global types**. Types like "band" and "musician" were consolidated into "profile".

---

## KEY PEOPLE

| Person | Role | Organization | Era |
|--------|------|--------------|-----|
| **Mark Zuckerberg** | Announced OGP at F8 | Facebook | 2010 |
| **Bret Taylor** | Director of Platform Products, led Open Graph development | Facebook | 2009-2013 |
| **David Recordon** | Senior Open Programs Manager, presented OGP design decisions | Facebook | 2009-2012 |
| **Mike Schroepfer** | Head of Engineering | Facebook | 2010 |
| **Chris Messina** | Critic/analyst, inventor of hashtag | Independent | 2010 |
| **Niall Kennedy** | Created PHP validator, documented OGP 1.1 | Independent | 2011-2012 |

**Bret Taylor** was the key technical leader. He joined Facebook when they acquired FriendFeed in 2009, led the Platform team, demonstrated OGP at F8 2010, and was promoted to CTO in June 2010.

**David Recordon** presented "The Open Graph Protocol Design Decisions" at W3C's Linked Data Camp at WWW 2010 (April 29, 2010). He defended OGP's "openness" — it's licensed under Open Web Foundation Agreement, increases semantic web data, and isn't proprietary to Facebook.

---

## COMPLETE TYPE HIERARCHY

### Required Properties (All Types)

| Property | Type | Description |
|----------|------|-------------|
| `og:title` | string | Title as it should appear in the graph |
| `og:type` | string | Object type (see below) |
| `og:image` | url | Image URL representing the object |
| `og:url` | url | Canonical URL (permanent ID in the graph) |

### Optional Properties (All Types)

| Property | Type | Description |
|----------|------|-------------|
| `og:audio` | url | Audio file URL |
| `og:description` | string | 1-2 sentence description |
| `og:determiner` | enum | Article before title: "a", "an", "the", "", "auto" |
| `og:locale` | string | Locale in `language_TERRITORY` format (default: `en_US`) |
| `og:locale:alternate` | string[] | Array of alternate locales |
| `og:site_name` | string | Parent website name (e.g., "IMDb") |
| `og:video` | url | Video file URL |

### Structured Media Properties

**og:image** sub-properties:
- `og:image:url` — Same as og:image
- `og:image:secure_url` — HTTPS version
- `og:image:type` — MIME type
- `og:image:width` — Pixel width
- `og:image:height` — Pixel height
- `og:image:alt` — Alt text description

**og:video** — Same sub-properties as og:image

**og:audio** — Has :url, :secure_url, :type (no dimensions)

---

## OBJECT TYPES (og:type values)

### No Vertical (Global Types)

#### `website`
- **Namespace:** `https://ogp.me/ns/website#`
- **Properties:** None beyond basic metadata
- **Note:** Default type. Any non-marked up page is treated as `website`

#### `article`
- **Namespace:** `https://ogp.me/ns/article#`
- **Properties:**
  - `article:published_time` (datetime) — First published
  - `article:modified_time` (datetime) — Last changed
  - `article:expiration_time` (datetime) — Expiry date
  - `article:author` (profile[]) — Writers
  - `article:section` (string) — High-level section (e.g., "Technology")
  - `article:tag` (string[]) — Tag words

#### `book`
- **Namespace:** `https://ogp.me/ns/book#`
- **Properties:**
  - `book:author` (profile[]) — Authors
  - `book:isbn` (string) — ISBN
  - `book:release_date` (datetime) — Release date
  - `book:tag` (string[]) — Tags

#### `profile`
- **Namespace:** `https://ogp.me/ns/profile#`
- **Properties:**
  - `profile:first_name` (string)
  - `profile:last_name` (string)
  - `profile:username` (string)
  - `profile:gender` (enum: male, female)

#### `payment.link` (Beta)
- **Namespace:** `https://ogp.me/ns/payment#`
- **Properties:**
  - `payment:description` (string)
  - `payment:currency` (string) — ISO 4217 code
  - `payment:amount` (float)
  - `payment:expires_at` (datetime)
  - `payment:status` (enum: PENDING, PAID, FAILED, EXPIRED)
  - `payment:id` (string)
  - `payment:success_url` (url)

---

### Music Vertical

**Namespace:** `https://ogp.me/ns/music#`

#### `music.song`
- `music:duration` (integer ≥1) — Length in seconds
- `music:album` (music.album[]) — Albums containing this song
- `music:album:disc` (integer ≥1) — Disc number
- `music:album:track` (integer ≥1) — Track number
- `music:musician` (profile[]) — Artists

#### `music.album`
- `music:song` (music.song) — Songs on album
- `music:song:disc` (integer ≥1)
- `music:song:track` (integer ≥1)
- `music:musician` (profile) — Artist
- `music:release_date` (datetime)

#### `music.playlist`
- `music:song` — Same structure as album
- `music:song:disc`
- `music:song:track`
- `music:creator` (profile) — Playlist creator

#### `music.radio_station`
- `music:creator` (profile) — Station creator

---

### Video Vertical

**Namespace:** `https://ogp.me/ns/video#`

#### `video.movie`
- `video:actor` (profile[]) — Actors
- `video:actor:role` (string) — Role played
- `video:director` (profile[]) — Directors
- `video:writer` (profile[]) — Writers
- `video:duration` (integer ≥1) — Length in seconds
- `video:release_date` (datetime)
- `video:tag` (string[])

#### `video.episode`
- All properties from video.movie, plus:
- `video:series` (video.tv_show) — Parent series

#### `video.tv_show`
- Same properties as video.movie

#### `video.other`
- Same properties as video.movie
- For videos not fitting other categories

---

### Business Vertical (Added 2013)

**Namespace:** `https://ogp.me/ns/business#`

#### `business.business`
Required:
- `place:location:latitude`
- `place:location:longitude`
- `business:contact_data:street_address`
- `business:contact_data:locality`
- `business:contact_data:country`
- `business:contact_data:postal_code`

Optional:
- `business:contact_data:region`
- `business:contact_data:email`
- `business:contact_data:phone_number`
- `business:contact_data:fax_number`
- `business:contact_data:website`
- `business:hours:day`, `business:hours:start`, `business:hours:end`

---

### Product Type (E-commerce)

#### `product`
- `og:price:amount` — Price
- `og:price:currency` — Currency code (USD, EUR, etc.)
- `product:availability` — Stock status
- `product:condition` — Item condition (new, used, etc.)
- `product:brand` — Brand name
- `product:retailer_item_id` — Product ID

---

## DATA TYPES

| Type | Description | Example Values |
|------|-------------|----------------|
| Boolean | true/false | `true`, `false`, `1`, `0` |
| DateTime | ISO 8601 date/time | `2024-01-15T10:30:00Z` |
| Enum | Bounded set of strings | `male`, `female` |
| Float | 64-bit signed floating point | `1.234`, `-1.2e3` |
| Integer | 32-bit signed integer | `1234`, `-123` |
| String | Unicode characters | Any text |
| URL | http/https URL | `https://example.com` |

---

## DEPRECATED PROPERTIES

From the RDF schema, these are explicitly deprecated:
- `og:audio:title`, `og:audio:artist`, `og:audio:album`
- `og:latitude`, `og:longitude` (use place:location instead)
- `og:street-address`, `og:locality`, `og:region`, `og:postal-code`, `og:country-name`
- `og:email`, `og:phone_number`, `og:fax_number`
- `og:isbn` (use book:isbn)
- `og:upc`

---

## EXTENSION MECHANISM

### Custom Namespaces

OGP allows custom types using CURIEs (Compact URIs):

```html
<html prefix="my_namespace: https://example.com/ns#">
<head>
  <meta property="og:type" content="my_namespace:my_type" />
</head>
```

**Key distinction:**
- Global types use dot notation: `video.movie`, `music.song`
- Custom types use colon notation: `my_namespace:my_type`

### Facebook-Specific Extensions

Developers could create custom actions scoped to their Facebook application, though this was largely deprecated in 2012. Approved core actions remaining:
- Like (any object)
- Follow (profile)
- Listen (song)
- Read (article)
- Watch (video/movie/TV show)

---

## RELATIONSHIP TO OTHER STANDARDS

### vs Schema.org

| Aspect | Open Graph | Schema.org |
|--------|------------|------------|
| **Purpose** | Social media sharing | Search engine SEO |
| **Created by** | Facebook (2010) | Google, Microsoft, Yahoo, Yandex (2011) |
| **Adoption** | 69.8% of web | 52.6% (JSON-LD) |
| **Complexity** | Simple, ~12 types | Complex, 800+ types |
| **Implementation** | Meta tags in `<head>` | JSON-LD, microdata, RDFa |
| **Relationship modeling** | Minimal | Rich |

**Key insight:** OGP optimizes for the "link preview" use case. Schema.org optimizes for the "understand everything about this page" use case. **Use both.**

### vs Twitter Cards

Twitter Cards are based on Open Graph conventions. Twitter's parser:
1. Checks for Twitter-specific tags (`twitter:card`, `twitter:title`, etc.)
2. Falls back to Open Graph tags if Twitter tags missing

**Twitter Card Types:**
- `summary` — Default card with thumbnail
- `summary_large_image` — Large image card
- `player` — Video/audio player
- `app` — App download card

### Platform Support

| Platform | OGP Support | Notes |
|----------|-------------|-------|
| Facebook | Full | Creator of OGP |
| LinkedIn | Full | Uses OGP for link previews |
| Twitter/X | Partial | Prefers Twitter Cards, OGP fallback |
| Pinterest | Partial | Prefers Schema.org for Rich Pins |
| Slack | Full | Uses OGP for "unfurling" |
| Discord | Full | Uses OGP for embeds |
| WhatsApp | Full | Uses OGP for link previews |
| iMessage | Full | Uses OGP for rich links |

---

## IMPLEMENTATION BEST PRACTICES

### Required Tags

```html
<html prefix="og: https://ogp.me/ns#">
<head>
  <meta property="og:title" content="Page Title" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="https://example.com/image.jpg" />
  <meta property="og:url" content="https://example.com/page" />
</head>
```

### Image Requirements

| Platform | Recommended Size | Min Size | Max File Size |
|----------|------------------|----------|---------------|
| Facebook | 1200×630px | 600×315px | 8MB |
| LinkedIn | 1200×627px | 401px wide | 5MB |
| Twitter | 1200×628px | 120×120px | 5MB |
| General | 1200×630px (1.91:1) | 200×200px | 5MB |

### Common Mistakes

1. **Missing og:image** — Results in no preview image
2. **Relative URLs** — Must use absolute URLs
3. **Images too small** — Won't display or will show as tiny thumbnail
4. **Description too long** — Keep under 160 characters
5. **Not pre-caching** — First share may not show image

### Validation Tools

- **Facebook Sharing Debugger**: `https://developers.facebook.com/tools/debug/`
- **LinkedIn Post Inspector**: `https://www.linkedin.com/post-inspector/`
- **Twitter Card Validator**: `https://cards-dev.twitter.com/validator`
- **Open Graph Debugger**: `https://ogdebugger.com/`

---

## URLS

### Official
- https://ogp.me/ — Official specification
- https://ogp.me/ns/ogp.me.ttl — RDF schema (Turtle format)
- https://github.com/facebook/open-graph-protocol — GitHub repo
- https://developers.facebook.com/docs/sharing/webmasters — Facebook implementation guide
- https://developers.facebook.com/tools/debug/ — Sharing Debugger

### Historical
- https://www.scribd.com/doc/30715288/The-Open-Graph-Protocol-Design-Decisions — David Recordon's WWW 2010 presentation
- https://www.niallkennedy.com/blog/2012/01/open-graph-protocol.html — OGP 1.1 deep dive

### News Coverage (F8 2010)
- https://www.cnet.com/culture/facebook-f8-one-graph-to-rule-them-all/
- https://www.wired.com/2010/04/facebook-shows-off-new-tools-to-socialize-the-entire-web/
- https://techcrunch.com/2010/04/21/facebook/
- https://techcrunch.com/2010/04/23/facebook-open-graph/

### Comparisons
- https://yext.com/blog/2017/07/schema-vs-open-graph — Schema.org vs OGP
- https://w3techs.com/technologies/details/da-opengraph — Usage statistics

---

## ENTITY TYPE OBSERVATIONS

### What OGP Got Right

1. **Radical simplicity** — Only 4 required properties. Anyone can implement.

2. **Pragmatic type system** — 12 core types cover 90% of web content. Not trying to model everything.

3. **Flat inheritance** — Types don't deeply inherit. `video.movie` isn't a subtype of `video` that's a subtype of `media`. Each type stands alone.

4. **Verticals as namespaces** — `music.*`, `video.*` group related types without inheritance complexity.

5. **References over embeddings** — `article:author` references a `profile` by URL, doesn't embed the data. Follows graph principles.

6. **Arrays for multiplicity** — Multiple images, authors, tags handled by repeating the same property.

7. **Structured properties** — `og:image` has sub-properties like `og:image:width`. Clean way to add metadata without new top-level properties.

### Type System Design Lessons

| OGP Pattern | Our Application |
|-------------|-----------------|
| 4 required + many optional | Core entity properties: id, type, title, created |
| Vertical namespaces | Category-based type grouping |
| URL-based references | Entity relationships by ID |
| Structured sub-properties | Nested metadata |
| Enum constraints | Status fields, type restrictions |
| DateTime for temporality | created, modified, published |

### Types We Might Adopt

From OGP's proven types:
- **article** → Note, Document
- **book** → Reference
- **profile** → Person, Contact
- **video.movie**, **video.episode** → Media items
- **music.song**, **music.album** → Media with relationships
- **product** → Item with price/availability
- **business.business** → Place with contact info

### Relationship Patterns

OGP models relationships through:
1. **Type references** — `video:series` points to a `video.tv_show`
2. **Profile arrays** — `article:author` is an array of `profile` references
3. **Nested metadata** — `music:album:track` gives position within container

This is **reference-based**, not **join-table-based**. The relationship lives on the referring object.

---

---

## OGP 1.0 Complete Type List (39 Types)

**Original types from May 2010 (via Wayback Machine):**

| Category | Types |
|----------|-------|
| **Activities** | `activity`, `sport` |
| **Businesses** | `bar`, `company`, `cafe`, `hotel`, `restaurant` |
| **Groups** | `cause`, `sports_league`, `sports_team` |
| **Organizations** | `band`, `government`, `non_profit`, `school`, `university` |
| **People** | `actor`, `athlete`, `author`, `director`, `musician`, `politician`, `public_figure` |
| **Places** | `city`, `country`, `landmark`, `state_province` |
| **Products/Entertainment** | `album`, `book`, `drink`, `food`, `game`, `product`, `song`, `movie`, `tv_show` |
| **Websites** | `blog`, `website`, `article` |

**Note:** OGP 1.0 DID have organization types (band, company, government, non_profit, school, university) and place types (city, country, landmark). These were consolidated/deprecated in OGP 1.1 (2012).

---

## Key Gaps Analysis

| Type | OGP 1.0 | OGP Current | Status |
|------|---------|-------------|--------|
| **Event** | ❌ Never existed | ❌ None | Facebook Events are Graph API objects, not OGP |
| **Place** | ✅ city, country, landmark, state_province | ❌ Deprecated | Properties deprecated in RDF schema |
| **Organization** | ✅ band, government, non_profit, school, university, company | ⚠️ Only `business.business` | Consolidated |

**Why no Event type?** Facebook Events exist in the Graph API (proprietary), but external event websites just use `og:type="website"`. The OGP philosophy is "link preview metadata" not "comprehensive entity typing."

---

## Session Log

### 2025-01-24: Initial setup
- Created research doc
- Outlined research tasks

### 2026-01-24: Phase 1 Web Research Complete
- Fetched and documented full ogp.me specification
- Retrieved RDF schema with all properties and deprecated items
- Documented complete type hierarchy with all properties per type
- Found key people: Bret Taylor, David Recordon, Mark Zuckerberg
- Documented OGP history: April 21, 2010 F8 announcement
- Tracked evolution: OGP 1.0 (39 types) → OGP 1.1 (12 types)
- Compared to Schema.org, Twitter Cards
- Found adoption statistics: 69.8% of web uses OGP
- Documented extension mechanism (custom namespaces)
- Listed all deprecated properties from RDF schema
- Compiled implementation best practices
- Identified lessons for entity type design

### 2026-01-24: Deep-dive on Event/Place/Organization
- Confirmed: OGP NEVER had event type
- Confirmed: OGP 1.0 HAD place types (city, country, landmark) — now deprecated
- Confirmed: OGP 1.0 HAD organization types (band, company, government, etc.) — now consolidated into business.business
- Decision: Use OGP as foundation, add event/place/organization ourselves
