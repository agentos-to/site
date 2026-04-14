---
title: Facebook Entity Graph Research
description: Facebook has spent 20+ years building the world's largest social entity graph. What can we learn from their entity types, relationships, and evolution?
---

## Why This Matters

Facebook's graph connects:
- **3+ billion** user profiles
- **Hundreds of billions** of relationships
- Every type of social entity: people, pages, posts, photos, videos, events, places, groups, comments, reactions...

They've solved problems at scale we'll never face, but their **entity modeling decisions** are invaluable research.

---

## Key People

Engineers, researchers, and product leads behind Facebook's graph systems.

### Leadership & Architecture
| Person | Role | Project | Era |
|--------|------|---------|-----|
| Mark Zuckerberg | CEO, Architect | Social Graph concept | 2007+ |
| Bret Taylor | CTO | Platform, Open Graph Protocol | 2009-2012 |
| Mike Schroepfer | CTO | Infrastructure | 2013-2021 |
| David Recordon | Developer Advocate | Open Graph Protocol design | 2010 |

### Graph Search Team
| Person | Role | Project | Era |
|--------|------|---------|-----|
| Lars Rasmussen | Engineering Lead | Graph Search (ex-Google Maps) | 2011-2013 |
| Tom Stocky | Product Lead | Graph Search | 2011-2013 |

### TAO Paper Authors (USENIX ATC 2013)
| Person | Affiliation |
|--------|-------------|
| Nathan Bronson | Facebook |
| Zach Amsden | Facebook |
| George Cabrera III | Facebook |
| Prasad Chakka | Facebook |
| Peter Dimov | Facebook |
| Hui Ding | Facebook |
| Jack Ferris | Facebook |
| Anthony Giardullo | Facebook |
| Sachin Kulkarni | Facebook |
| Harry Li | Facebook |
| Mark Marchukov | Facebook |
| Dmitri Petrov | Facebook |
| Lovro Puzar | Facebook |
| Yee Jiun Song | Facebook |
| Venkat Venkataramani | Facebook |

### Unicorn Paper Authors (VLDB 2013)
| Person | Affiliation |
|--------|-------------|
| Michael Curtiss | Facebook |
| Iain Coney | Facebook |
| Jimmy Lennon | Facebook |
| Subbu Sivanen | Facebook |
| et al. | Facebook |

### Academic Research
| Person | Paper | Year |
|--------|-------|------|
| Johan Ugander | "Anatomy of the Facebook Social Graph" | 2011 |
| Brian Karrer | "Anatomy of the Facebook Social Graph" | 2011 |
| Lars Backstrom | "Anatomy of the Facebook Social Graph" | 2011 |
| Cameron Marlow | "Anatomy of the Facebook Social Graph" | 2011 |

---

## Key Research Areas

### 1. Open Graph Protocol
The `og:` meta tags that let any webpage become a "rich object" in Facebook's graph.

**Questions:**
- What object types does Open Graph define?
- How do they handle relationships between objects?
- What's required vs optional?
- How has it evolved since 2010?

**Source:** https://ogp.me/

### 2. Graph API Entity Types
The public API exposes their entity model.

**Known entity types (to verify/expand):**
- User
- Page
- Post
- Photo
- Video
- Album
- Comment
- Group
- Event
- Place/Location
- Link
- Application

**Questions:**
- What fields does each entity have?
- What relationship types exist (edges)?
- How do permissions/privacy work per entity?
- What's deprecated vs current?

**Source:** https://developers.facebook.com/docs/graph-api/reference

### 3. Social Graph Evolution
How has Facebook's graph changed over time?

**Key milestones to research:**
- 2007: Facebook Platform launches (apps can access graph)
- 2010: Open Graph Protocol introduced
- 2012: Timeline/structured life events
- 2013: Graph Search (natural language queries over graph)
- 2018+: Privacy changes post-Cambridge Analytica
- 2020s: Metaverse/Meta rebrand — new entity types?

### 4. Relationship Types (Edges)
Facebook calls relationships "edges." What types exist?

**Known edge types:**
- friend (bidirectional)
- follow (unidirectional)
- like
- member_of (group)
- attending (event)
- tagged_in
- author_of
- comment_on
- reaction_to

**Questions:**
- Are edges typed or just generic connections?
- Do edges have properties (timestamps, context)?
- How do they handle edge cardinality (one-to-one, one-to-many, many-to-many)?

### 5. The "Social Graph" Concept
Facebook popularized the term. What does it actually mean in their implementation?

**Research:**
- Original 2007 F8 presentation
- Academic papers on Facebook's architecture
- Engineering blog posts

---

## Comparison to Our Model

| Aspect | Facebook | Entity Experiments |
|--------|----------|-------------------|
| ID format | Numeric IDs (big integers) | NanoID (8 char random) |
| Core entity | User/Page | person/organization |
| Relationships | "Edges" with types | Typed relationships |
| Privacy | Per-entity, per-edge | TBD |
| Schema | Evolving, versioned | Experimental |

---

## Open Questions

1. **How does Facebook handle entity type evolution?** Adding new types, deprecating old ones?
2. **What's the relationship between User and Page?** Both are "actors" but different types
3. **How do they model "content" vs "container"?** Post vs Album vs Timeline
4. **What entity types exist for Marketplace, Dating, Workplace?** Vertical-specific entities?
5. **How do they handle "the same thing" across products?** A video on Facebook vs Instagram vs WhatsApp

---

## Research Queue

- [x] Open Graph Protocol specification deep-dive — **Complete**: Full type system documented (music, video, article, book, profile, website, payment.link) with all properties and namespaces
- [x] Graph API reference documentation analysis — **Complete**: User, Page, Post, Photo, Video, Album, Group, Event, Place, Comment schemas documented with all fields and edges
- [x] Facebook engineering blog posts on graph architecture — **Complete**: TAO, Unicorn, Dragon, Graph Search architecture documented
- [x] Academic papers on Facebook's social graph — **Complete**: "Anatomy of the Facebook Social Graph" (721M users, 68.7B friendships, 4.7 avg distance)
- [x] Comparison: Facebook Graph API vs Google's APIs vs Twitter's API — **Complete**: Entity type comparison table (User/Post/Place across platforms), ID formats, relationship models
- [x] Privacy/permission model for entities — **Complete**: Per-entity privacy, per-edge privacy, audience selector, mutual confirmation, API permission requirements
- [x] Instagram/WhatsApp entity integration (post-acquisition) — **Complete**: IG User/Media/Comment/Hashtag/Container, WhatsApp Message types, Threads User/Post, Accounts Center cross-product linking

---

## Sources to Investigate

### Official
- https://ogp.me/ — Open Graph Protocol
- https://developers.facebook.com/docs/graph-api — Graph API docs
- https://engineering.fb.com/ — Engineering blog

### Academic/Analysis
- "The Anatomy of the Facebook Social Graph" (2012 paper)
- "TAO: Facebook's Distributed Data Store for the Social Graph" (2013)
- Various reverse-engineering analyses

### Historical
- F8 2007, 2010, 2019 keynotes
- Zuckerberg's "social graph" presentations
- Open Graph launch announcements

---

---

## Findings

### Open Graph Protocol Complete Type System

**Official Source:** https://ogp.me/

The Open Graph Protocol defines a complete type system for representing objects in social graphs:

#### Required Properties (All Types)
- `og:title` — The object's title
- `og:type` — The object type (from list below)
- `og:image` — Image URL representing the object
- `og:url` — Canonical URL (permanent ID in graph)

#### Optional Properties (All Types)
- `og:audio` — Audio file URL
- `og:description` — 1-2 sentence description
- `og:determiner` — Article (a, an, the, "", auto)
- `og:locale` — Locale (default: en_US)
- `og:locale:alternate` — Array of other available locales
- `og:site_name` — Parent site name
- `og:video` — Video file URL

#### Music Types (Namespace: `https://ogp.me/ns/music#`)

| Type | Properties |
|------|------------|
| `music.song` | duration, album (array), album:disc, album:track, musician (profile array) |
| `music.album` | song, song:disc, song:track, musician, release_date |
| `music.playlist` | song, song:disc, song:track, creator (profile) |
| `music.radio_station` | creator (profile) |

#### Video Types (Namespace: `https://ogp.me/ns/video#`)

| Type | Properties |
|------|------------|
| `video.movie` | actor (profile array), actor:role, director (profile array), writer (profile array), duration, release_date, tag (string array) |
| `video.episode` | Same as movie + series (video.tv_show) |
| `video.tv_show` | Same as movie |
| `video.other` | Same as movie |

#### No-Vertical Types (Global)

| Type | Namespace | Properties |
|------|-----------|------------|
| `article` | `https://ogp.me/ns/article#` | published_time, modified_time, expiration_time, author (profile array), section, tag (string array) |
| `book` | `https://ogp.me/ns/book#` | author (profile array), isbn, release_date, tag (string array) |
| `payment.link` | `https://ogp.me/ns/payment#` | description, currency (ISO 4217), amount, expires_at, status (PENDING/PAID/FAILED/EXPIRED), id, success_url |
| `profile` | `http://ogp.me/ns/profile#` | first_name, last_name, username, gender (male/female) |
| `website` | `https://ogp.me/ns/website#` | (no additional properties) |

**Key Design Insight:** OGP uses vertical-specific namespaces to extend base properties. Any unmarked webpage defaults to `og:type website`. CURIEs allow custom types via prefix notation.

---

### TAO: Facebook's Distributed Data Store

**Core Architecture (USENIX ATC 2013):**
- 1 billion reads/second, millions of writes/second
- Tens of petabytes of data across thousands of machines
- 500:1 read-to-write ratio, optimized for reads
- Sub-millisecond read latencies (~1ms average)
- 99.99%+ availability

**Data Model:**
- **Objects (nodes):** 64-bit Object Identifiers (OID), typed with key-value data
- **Associations (edges):** Source ID, association type (atype), destination ID, timestamp, data
- Two objects can only have one association of the same type
- Association lists ordered by time

**Authors:** Nathan Bronson, Zach Amsden, George Cabrera III, Prasad Chakka, Peter Dimov, Hui Ding, Jack Ferris, Anthony Giardullo, Sachin Kulkarni, Harry Li, Mark Marchukov, Dmitri Petrov, Lovro Puzar, Yee Jiun Song, Venkat Venkataramani

### Graph API Entity Types (v24.0)

**Primary Entities:**
- User, Page, Post, Photo, Video, Album, Comment, Group, Event, Place, Application, LiveVideo, Reaction

**Reaction Types:** LIKE, LOVE, WOW, HAHA, SAD, ANGRY, THANKFUL, PRIDE, CARE, FIRE, HUNDRED

**Instagram Entities:** IG User, IG Media, IG Comment, IG Container, IG Hashtag

---

### Complete Facebook Graph API Entity Schemas

#### User Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | User's unique ID |
| name | string | Full name |
| first_name | string | First name |
| last_name | string | Last name |
| email | string | Email (requires permission) |
| birthday | string | Birthday (MM/DD/YYYY) |
| gender | string | Gender |
| link | url | Profile URL |
| picture | object | Profile picture |
| hometown | Page | Hometown |
| location | Page | Current city |
| relationship_status | string | See relationship types above |
| significant_other | User | Partner (if confirmed) |

**Edges:** /friends, /family (deprecated), /likes, /posts, /photos, /videos, /albums, /groups, /events, /accounts (pages managed)

#### Page Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Page ID |
| name | string | Page name |
| about | string | Short description |
| category | string | e.g., "Internet Company" |
| category_list | array | Multiple categories |
| description | string | Long description |
| website | url | External website |
| location | Location | Physical location |
| phone | string | Contact phone |
| fan_count | int | Number of likes |
| followers_count | int | Number of followers |
| overall_star_rating | float | 1-5 star rating |
| rating_count | int | Number of ratings |
| verification_status | string | Verified status |
| cover | CoverPhoto | Cover image |
| picture | ProfilePicture | Profile image |

**Edges:** /posts, /photos, /videos, /events, /feed, /ratings, /roles, /locations

#### Post Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Post ID |
| message | string | Text content |
| story | string | Auto-generated story text |
| created_time | datetime | Creation timestamp |
| updated_time | datetime | Last update timestamp |
| from | User/Page | Author |
| to | array | Target profiles |
| type | enum | link, status, photo, video, offer |
| status_type | string | More specific type |
| permalink_url | url | Permanent link |
| shares | object | Share count |
| privacy | Privacy | Privacy settings |
| place | Place | Tagged location |
| is_published | bool | Published status |
| is_hidden | bool | Hidden from timeline |

**Edges:** /comments, /reactions, /likes, /attachments, /sharedposts, /insights

#### Photo Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Photo ID |
| album | Album | Parent album |
| created_time | datetime | Upload timestamp |
| from | User/Page | Uploader |
| images | array | Different size URLs |
| width | int | Width in pixels |
| height | int | Height in pixels |
| name | string | Caption |
| link | url | Facebook link |
| picture | url | Thumbnail URL |
| source | url | Full-size URL |
| place | Place | Tagged location |

**Edges:** /tags (with x, y coordinates), /comments, /reactions, /likes

#### Video Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Video ID |
| created_time | datetime | Upload timestamp |
| description | string | Video description |
| title | string | Video title |
| from | User/Page | Uploader |
| length | float | Duration in seconds |
| source | url | Video file URL |
| picture | url | Thumbnail |
| embed_html | string | Embed code |
| format | array | Available formats |
| live_status | string | none, live, live_stopped |
| permalink_url | url | Permanent link |

**Edges:** /comments, /reactions, /likes, /tags, /thumbnails

#### Album Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Album ID |
| name | string | Album title |
| description | string | Description |
| count | int | Number of photos |
| type | enum | profile, mobile, wall, normal |
| cover_photo | Photo | Cover image |
| created_time | datetime | Creation timestamp |
| updated_time | datetime | Last update |
| from | User/Page | Creator |
| link | url | Facebook link |
| privacy | string | Privacy setting |

**Edges:** /photos, /comments, /likes, /picture

#### Group Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Group ID |
| name | string | Group name |
| description | string | Description |
| privacy | enum | OPEN, CLOSED, SECRET |
| created_time | datetime | Creation timestamp |
| updated_time | datetime | Last activity |
| owner | User | Creator |
| cover | CoverPhoto | Cover image |
| icon | url | Group icon |
| member_count | int | Number of members |
| is_community | bool | Community flag |

**Edges:** /members (deprecated), /admins, /feed, /photos, /videos, /events, /files

#### Event Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Event ID |
| name | string | Event title |
| description | string | Description |
| start_time | datetime | Start timestamp |
| end_time | datetime | End timestamp |
| timezone | string | Timezone name |
| place | Place | Venue |
| cover | CoverPhoto | Cover image |
| owner | User/Page | Host |
| is_canceled | bool | Cancellation status |
| attending_count | int | RSVP: attending |
| maybe_count | int | RSVP: maybe |
| declined_count | int | RSVP: declined |
| invited_count | int | Total invited |
| event_times | array | Recurring instances |
| ticket_uri | url | Ticket link |
| type | enum | private, public, group, community |

**Edges:** /attending, /maybe, /declined, /noreply, /photos, /videos, /feed

#### Place Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Place ID |
| name | string | Place name |
| location | Location | Geographic data |
| overall_rating | float | 1-5 stars |

**Location Object:**
| Field | Type | Description |
|-------|------|-------------|
| latitude | float | GPS latitude |
| longitude | float | GPS longitude |
| street | string | Street address |
| city | string | City name |
| state | string | State/province |
| zip | string | Postal code |
| country | string | Country name |
| located_in | string | Parent location ID |

#### Comment Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Comment ID |
| message | string | Comment text |
| created_time | datetime | Creation timestamp |
| from | User/Page | Author |
| parent | Comment | Parent comment (for replies) |
| attachment | Attachment | Media attachment |
| comment_count | int | Reply count |
| like_count | int | Like count |
| can_remove | bool | Can user remove |
| is_hidden | bool | Hidden status |

**Edges:** /comments (replies), /reactions, /likes

---

### Instagram Graph API Entity Types

#### IG User Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Instagram user ID |
| ig_id | int | Legacy Instagram ID |
| username | string | @handle |
| name | string | Display name |
| biography | string | Bio text |
| website | url | Profile link |
| followers_count | int | Follower count |
| follows_count | int | Following count |
| media_count | int | Post count |
| profile_picture_url | url | Avatar URL |
| shopping_product_tag_eligibility | bool | Can tag products |

**Edges:** /media, /stories, /live_media, /tags, /insights, /mentioned_media

#### IG Media Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Media ID |
| ig_id | string | Legacy Instagram ID |
| media_type | enum | IMAGE, VIDEO, CAROUSEL_ALBUM |
| media_product_type | enum | FEED, REELS, STORIES |
| caption | string | Caption text |
| timestamp | datetime | Post timestamp |
| permalink | url | Instagram link |
| media_url | url | Content URL |
| thumbnail_url | url | Video thumbnail |
| username | string | Owner's username |
| owner | IG User | Owner object |
| is_comment_enabled | bool | Comments allowed |
| comments_count | int | Comment count |
| like_count | int | Like count |
| shortcode | string | URL shortcode |
| children | array | Carousel children |

**Edges:** /comments, /insights, /children

#### IG Comment Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Comment ID |
| text | string | Comment text |
| timestamp | datetime | Creation timestamp |
| from | object | Author (id, username) |
| like_count | int | Like count |
| hidden | bool | Hidden status |
| user | IG User | Author user object |

**Edges:** /replies

#### IG Hashtag Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Hashtag ID (static, global) |
| name | string | Tag without # |

**Edges:** /recent_media, /top_media

**Limitation:** Max 30 unique hashtags per 7-day rolling window

#### IG Container Entity
Used for media publishing workflow.

| Field | Type | Description |
|-------|------|-------------|
| id | string | Container ID |
| status | enum | EXPIRED, ERROR, FINISHED, IN_PROGRESS, PUBLISHED |
| status_code | string | Error code if failed |
| copyright_check_status | object | Copyright check result |

---

### Threads API Entity Types

#### Threads User Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Threads user ID |
| username | string | @handle |
| name | string | Display name |
| threads_profile_picture_url | url | Avatar |
| threads_biography | string | Bio text |
| is_verified | bool | Verification badge |

#### Threads Post Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | Post ID |
| media_product_type | string | Always "THREADS" |
| media_type | enum | TEXT_POST, IMAGE, VIDEO, CAROUSEL_ALBUM, AUDIO, REPOST_FACADE |
| text | string | Post content |
| permalink | url | Thread link |
| timestamp | datetime | ISO 8601 |
| owner | string | User ID |
| username | string | Author's handle |
| shortcode | string | URL code |
| thumbnail_url | url | Video thumbnail |
| children | array | Carousel items |
| is_quote_post | bool | Quote post flag |
| quoted_post | string | Quoted post ID |

---

### WhatsApp Business API Entity Types

#### Message Entity
| Field | Type | Description |
|-------|------|-------------|
| id | string | WAMID (max 128 chars) |
| type | enum | text, image, video, audio, document, sticker, contacts, location, interactive, template |
| from | string | Sender phone number |
| timestamp | int | Unix timestamp |
| biz_opaque_callback_data | string | Custom tracking data |

**Message Types:**
- **text** — Simple text content
- **media** — Image, video, audio, document, sticker
- **contacts** — Contact cards
- **location** — Geographic coordinates
- **interactive** — Lists, reply buttons, product messages
- **template** — Pre-approved templates

**Status Values:** sent, delivered, read, failed, deleted

---

### Cross-Platform Comparison: Entity Models

| Aspect | Facebook/Meta | Twitter/X | Google |
|--------|---------------|-----------|--------|
| **Core User Entity** | User (64-bit ID) | User | Person (resourceName) |
| **Content Entity** | Post, Photo, Video | Tweet/Post | - |
| **Group Entity** | Group, Event | - | - |
| **Place Entity** | Place, Location | Place | Place |
| **Relationship Model** | Typed edges (TAO) | Follow relationship | contactGroups |
| **ID Format** | Numeric (64-bit) | Numeric (snowflake) | String (people/{id}) |
| **Privacy Model** | Per-entity + per-edge | Public/protected | Per-contact |

#### Twitter/X API v2 Entity Types
- **Post** (formerly Tweet): id, text, created_at, author_id, conversation_id, entities (hashtags, mentions, urls)
- **User**: id, name, username, created_at, description, verified, profile_image_url
- **Space**: id, state, title, host_ids, speaker_ids, participant_count
- **List**: id, name, description, owner_id, member_count, follower_count
- **Media**: media_key, type, url, duration_ms, height, width
- **Poll**: id, options, duration_minutes, end_datetime, voting_status
- **Place**: id, full_name, country, geo (coordinates)

#### Google People API Person Resource
- **names**: given, family, display
- **emailAddresses**: value, type
- **phoneNumbers**: value, type
- **addresses**: formatted, type
- **organizations**: name, title, department
- **birthdays**: date
- **photos**: url
- **relations**: person, type (spouse, child, etc.)
- **metadata**: source, primary flag

---

### Meta Cross-Product Integration

**Accounts Center:** Unified identity system linking Facebook, Instagram, WhatsApp, and Meta Horizon.

**Connected Experiences:**
1. **Cross-posting** — WhatsApp Status → Facebook/Instagram Stories
2. **Unified login** — Use one account to access others
3. **Profile sync** — Name, username, avatar synced across platforms
4. **Shopping** — Wishlists synced across Facebook/Instagram

**Entity Relationships Across Products:**
- Facebook User ↔ Instagram Account (linked in Accounts Center)
- Instagram User ↔ Threads User (automatic linking)
- WhatsApp number ↔ Facebook account (optional linking)
- All profiles can share a Meta Horizon avatar

**ID Namespacing:** Each product maintains its own ID space. Cross-product identity is managed through Accounts Center, not shared IDs.

### Graph Search (2013-2019)

- Launched January 2013, called Facebook's "third pillar"
- Natural language queries: "my friends in New York who like Jay-Z"
- Built by Lars Rasmussen and Tom Stocky (both ex-Google)
- Zuckerberg admitted in 2014 it "doesn't work" (worked less than half the time)
- Deprecated June 2019

### "Anatomy of Facebook Social Graph" Paper (2011)

- **721 million** active users, **68.7 billion** friendships
- 99.91% of users in single connected component
- Average pairwise distance: 4.7 (confirms "six degrees of separation")
- 5,000 friendship limit per user

### Platform Evolution Timeline

- **2007:** Facebook Platform launches at F8 with "social graph" concept
- **2010:** Open Graph Protocol announced, Like button (1B buttons in 24 hours)
- **2012:** Timeline with structured life events
- **2018:** Cambridge Analytica restrictions (87M users affected)
- **Current:** 3.07 billion monthly active users, 1 trillion+ edges

---

## Entity Type Implications

### Facebook's Entity Model Patterns

1. **64-bit IDs:** Universal identifier format across all entities
2. **Typed associations:** Relationships explicitly typed (friend, follow, like, etc.)
3. **Timestamps on edges:** Enables time-based ordering/filtering
4. **Privacy per-edge:** Visibility controlled at relationship level
5. **500:1 read optimization:** Entire architecture built for reads
6. **Product-specific namespaces:** Each Meta product (FB, IG, WA, Threads) has its own ID space
7. **Vertical-specific schemas:** OGP uses namespaces for music, video, article, book, profile verticals

### Entity Hierarchy

**Actors (can take actions):**
- Facebook: User, Page, Application
- Instagram: IG User
- Threads: Threads User
- WhatsApp: Phone number (as identity)

**Content (created by actors):**
- Facebook: Post, Photo, Video, Album, Comment, LiveVideo
- Instagram: IG Media, IG Comment, Stories, Reels
- Threads: Threads Post
- WhatsApp: Message (text, media, contact, location, interactive, template)

**Containers:**
- Facebook: Group, Event, Album, Page
- Instagram: IG Container (publishing workflow)

**Auxiliary:**
- Facebook: Place, Location, Reaction, Check-in (deprecated)
- Instagram: IG Hashtag

**Cross-Product:**
- Accounts Center (identity linkage)

### Complete Entity Type Taxonomy

| Category | Facebook | Instagram | Threads | WhatsApp |
|----------|----------|-----------|---------|----------|
| **Identity** | User, Page | IG User | Threads User | Phone/WAID |
| **Content** | Post, Photo, Video, LiveVideo | IG Media | Threads Post | Message |
| **Engagement** | Comment, Reaction | IG Comment | Reply | Read receipt |
| **Container** | Album, Group, Event | Stories, Carousel | - | Conversation |
| **Location** | Place, Location | - | - | Location message |
| **Discovery** | - | IG Hashtag | - | - |
| **Meta** | Application | IG Container | - | Template |

### Entity Properties Summary

**Universal fields across all entities:**
- `id` — Unique identifier (format varies by product)
- `created_time` / `timestamp` — Creation timestamp
- Permissions/privacy controls

**Actor-specific fields:**
- Name/username
- Profile picture
- Bio/about
- Verification status
- Follower/friend counts

**Content-specific fields:**
- Text/message/caption
- Media URL(s)
- Author/from/owner
- Engagement counts (likes, comments, shares)
- Permalink

**Container-specific fields:**
- Name/title
- Description
- Member/item count
- Privacy/visibility
- Cover image

### Recommended Entity Types for Our Schema

Based on Facebook's patterns, consider these entity categories:

| Our Type | Inspired By | Key Properties |
|----------|-------------|----------------|
| `person` | FB User, IG User, profile | name, username, avatar, bio |
| `organization` | FB Page | name, category, description, website |
| `post` | FB Post, IG Media, Threads Post | content, author, timestamp, media |
| `comment` | FB Comment, IG Comment | content, author, timestamp, parent |
| `media` | FB Photo, FB Video | type, url, dimensions, caption |
| `collection` | FB Album, FB Group | name, description, items |
| `event` | FB Event | name, start, end, location, host |
| `place` | FB Place, Location | name, coordinates, address |
| `hashtag` | IG Hashtag | name |

---

## Relationship Implications

### Complete Edge Type Taxonomy

#### Social Relationships

| Edge Type | Direction | Between | Properties |
|-----------|-----------|---------|------------|
| `friend` | Bidirectional | User ↔ User | created_time |
| `follow` | Unidirectional | User → User/Page | created_time |
| `member_of` | Unidirectional | User → Group | role (admin/moderator/member), joined_time |
| `attending` | Unidirectional | User → Event | rsvp_status (attending/maybe/declined) |
| `invited_to` | Unidirectional | User → Event | invited_by |
| `admin_of` | Unidirectional | User → Page/Group | role type |
| `blocked` | Unidirectional | User → User | created_time |

#### Family Relationships (Deprecated but informative)

| Edge Type | Inverse |
|-----------|---------|
| `mother` | `son`/`daughter` |
| `father` | `son`/`daughter` |
| `brother` | `brother`/`sister` |
| `sister` | `brother`/`sister` |
| `grandfather` | `grandson`/`granddaughter` |
| `grandmother` | `grandson`/`granddaughter` |
| `uncle` | `nephew`/`niece` |
| `aunt` | `nephew`/`niece` |
| `cousin` | `cousin` |

#### Romantic Relationships (Status-based)

| Status | Confirmation Required | Partner Field |
|--------|----------------------|---------------|
| Single | No | - |
| In a relationship | Yes | significant_other |
| Engaged | Yes | significant_other |
| Married | Yes | significant_other |
| In a civil union | Yes | significant_other |
| In a domestic partnership | Yes | significant_other |
| It's complicated | No | optional |
| In an open relationship | Yes | significant_other |
| Separated | No | - |
| Divorced | No | - |
| Widowed | No | - |

#### Content Relationships

| Edge Type | Direction | Between | Properties |
|-----------|-----------|---------|------------|
| `author_of` | Unidirectional | User/Page → Content | - |
| `comment_on` | Unidirectional | Comment → Content | - |
| `reply_to` | Unidirectional | Comment → Comment | - |
| `in_album` | Unidirectional | Photo/Video → Album | - |
| `posted_to` | Unidirectional | Post → User/Page/Group | - |
| `shared` | Unidirectional | Post → Post (original) | share_time |
| `mentions` | Unidirectional | Content → User | - |

#### Engagement Relationships

| Edge Type | Direction | Between | Properties |
|-----------|-----------|---------|------------|
| `liked` | Unidirectional | User → Content | created_time |
| `reacted` | Unidirectional | User → Content | reaction_type, created_time |
| `tagged_in` | Unidirectional | Content → User | x, y (for photos), created_time |
| `saved` | Unidirectional | User → Content | created_time, collection |

#### Location Relationships

| Edge Type | Direction | Between | Properties |
|-----------|-----------|---------|------------|
| `located_at` | Unidirectional | Page/Event → Place | - |
| `checked_in` | Unidirectional | User → Place | timestamp, message (deprecated) |
| `tagged_location` | Unidirectional | Content → Place | - |

#### Platform Relationships

| Edge Type | Direction | Between | Properties |
|-----------|-----------|---------|------------|
| `uses_app` | Unidirectional | User → Application | installed_time |
| `manages` | Unidirectional | User → Page | role |
| `linked_account` | Bidirectional | Account ↔ Account | platform |

### Key Design: Edges Have Properties

Facebook edges carry: association type, timestamp, optional data. This enables queries like "friends added in 2023" or "posts liked this week."

### TAO Association Rules

1. **Single association per type:** Two objects can have at most ONE association of the same type
2. **Timestamp required:** Every association has a creation timestamp
3. **Bidirectional = two associations:** Friend relationships create edges in BOTH directions
4. **Inverse types for bidirectional:** Uses different type IDs for each direction
5. **Optional data payload:** Associations can carry key-value data (e.g., family type name)

### Edge Cardinality Patterns

| Pattern | Example | Implementation |
|---------|---------|----------------|
| One-to-One | significant_other | Mutual confirmation required |
| One-to-Many | author → posts | Single direction |
| Many-to-Many | friends | Bidirectional edges |
| Self-referential | User → User (friend) | Same type on both ends |
| Polymorphic | User → (Post\|Photo\|Video) | Target can be multiple types |

### Recommended Relationship Types for Our Schema

Based on Facebook's patterns, consider these relationship categories:

| Category | Relationships |
|----------|---------------|
| **Social** | knows, follows, friends_with, blocked |
| **Family** | parent_of, child_of, sibling_of, spouse_of, relative_of |
| **Professional** | works_at, colleague_of, manages, reports_to |
| **Group** | member_of, admin_of, moderator_of |
| **Event** | attending, hosting, invited_to |
| **Content** | author_of, commented_on, replied_to, shared, mentioned_in |
| **Engagement** | liked, reacted_to, saved, tagged_in |
| **Location** | located_at, lives_in, born_in, visited |
| **Ownership** | owns, created, manages |

---

## Session Log

### 2025-01-24: Initial setup
- Created research doc
- Outlined key research areas
- Added key people section (Lars Rasmussen, Tom Stocky, Bret Taylor)
- Next: Subagent deep-dives on Open Graph Protocol and Graph API

### 2026-01-24: Phase 1 Web Research Complete
- TAO architecture: 1B reads/sec, 64-bit OIDs, typed associations
- Graph API entities: User, Page, Post, Photo, Video, Album, Comment, Group, Event, Place
- Graph Search history: 2013-2019, Lars Rasmussen/Tom Stocky
- "Anatomy" paper: 721M users, 68.7B friendships, 4.7 avg distance
- Platform evolution: 2007 Platform → 2010 Open Graph → 2018 Cambridge Analytica
- 40+ TAO/Unicorn paper authors documented

### 2026-01-24: Phase 2 - Relationship Deep-Dive
- Comprehensive relationship type taxonomy (romantic, family, follow)
- TAO association model details (typed edges, timestamps, bidirectional handling)
- Privacy model for relationships (audience selector, mutual confirmation)
- API evolution (v3.2 deprecations, Cambridge Analytica impact)
- Connection strength algorithms (dispersion metric)

### 2026-01-24: Comprehensive Entity Schema Research
**Open Graph Protocol Complete:**
- Full type system documented: music (song, album, playlist, radio_station), video (movie, episode, tv_show, other), article, book, profile, website, payment.link
- All properties per type with data types
- Namespace structure (vertical-specific URIs)

**Facebook Graph API v24.0 Entity Schemas:**
- Complete field documentation for: User, Page, Post, Photo, Video, Album, Group, Event, Place, Comment
- All edge types documented with properties
- Location object schema with GPS coordinates

**Instagram Graph API Entity Types:**
- IG User fields: id, username, biography, followers_count, media_count, etc.
- IG Media fields: media_type, caption, timestamp, comments_count, like_count, children
- IG Comment fields: text, timestamp, from, like_count
- IG Hashtag: id, name with recent_media edge
- IG Container: Publishing workflow entity with status tracking

**Threads API Entity Types:**
- Threads User: id, username, name, threads_profile_picture_url, threads_biography, is_verified
- Threads Post: media_type (TEXT_POST, IMAGE, VIDEO, CAROUSEL_ALBUM, AUDIO, REPOST_FACADE), text, permalink, is_quote_post

**WhatsApp Business API Entity Types:**
- Message entity with WAMID identifier
- Message types: text, image, video, audio, document, sticker, contacts, location, interactive, template
- Status tracking: sent, delivered, read, failed, deleted

**Cross-Platform Comparison:**
- Twitter/X API v2 entity types: Post, User, Space, List, Media, Poll, Place
- Google People API: Person resource with names, emails, phones, addresses, relations
- Documented differences in ID formats, relationship models, privacy approaches

**Meta Cross-Product Integration:**
- Accounts Center for unified identity
- Cross-posting capabilities (WhatsApp Status → Stories)
- Profile sync across Facebook, Instagram, Threads
- Product-specific ID namespaces

**Entity Type Implications Updated:**
- Complete taxonomy: Actors, Content, Containers, Auxiliary, Cross-Product
- Property summaries by category
- Recommended entity types for our schema

**Relationship Implications Updated:**
- Complete edge taxonomy: Social, Family, Romantic, Content, Engagement, Location, Platform
- TAO association rules (single per type, timestamps, bidirectional handling)
- Cardinality patterns (one-to-one, one-to-many, many-to-many, polymorphic)
- Recommended relationship types for our schema

---

## Relationship Modeling Deep-Dive

This section focuses specifically on how Facebook models **relationships between entities** — the edges in their social graph.

### Core Philosophy

Facebook's relationship model reveals key design decisions:

1. **Relationships are first-class objects** with their own properties (timestamp, type, metadata)
2. **Mutual vs unidirectional** is an explicit design choice per relationship type
3. **Privacy is per-relationship**, not just per-entity
4. **Relationships evolve over time** — status changes, metadata additions, API restrictions

---

### Relationship Categories

#### 1. Romantic/Status Relationships

The `relationship_status` field on User supports these values:

| Status | Notes |
|--------|-------|
| Single | Default/unspecified |
| In a relationship | Requires partner confirmation |
| Engaged | Requires partner confirmation |
| Married | Requires partner confirmation |
| In a civil union | Added ~2011 |
| In a domestic partnership | Added ~2011 |
| It's complicated | Classic Facebook ambiguity |
| In an open relationship | |
| Separated | |
| Divorced | Status change doesn't appear in Feed |
| Widowed | Added September 2009 |

**Key behaviors:**
- Partner must be a Facebook friend
- Both parties must confirm before relationship appears publicly
- Anniversary date can be added (day/month/year)
- Changing to Single/Divorced/Widowed is silent (no Feed story)
- Each person controls visibility independently via audience selector

**Historical note:** Zuckerberg conceived relationship status to track "whether you're having sex or aren't you" — originally a social discovery feature for college students.

#### 2. Family Relationships

The `/user/family` endpoint (deprecated after v3.2) returned family members with relationship types:

**Immediate Family:**
| Type | Inverse |
|------|---------|
| Mother | Son/Daughter |
| Father | Son/Daughter |
| Son | Mother/Father |
| Daughter | Mother/Father |
| Brother | Brother/Sister |
| Sister | Brother/Sister |

**Extended Family:**
| Type | Inverse |
|------|---------|
| Grandfather | Grandson/Granddaughter |
| Grandmother | Grandson/Granddaughter |
| Grandson | Grandfather/Grandmother |
| Granddaughter | Grandfather/Grandmother |
| Uncle | Niece/Nephew |
| Aunt | Niece/Nephew |
| Nephew | Uncle/Aunt |
| Niece | Uncle/Aunt |
| Cousin (male) | Cousin |
| Cousin (female) | Cousin |

**Implementation:** Family relationships are stored with a `relationship` field containing the text description. Required the `user_relationships` permission.

#### 3. Friend Relationships (Symmetric)

The core social relationship in Facebook — **bidirectional by design**.

**Characteristics:**
- Requires mutual acceptance (A sends request → B accepts)
- Creates edges in both directions in TAO
- 5,000 friend limit per user
- `/user/friends` endpoint only returns friends who also use the requesting app

**Termination:**
- Either party can unfriend (removes both edges)
- No notification sent to unfriended person
- "Take a Break" feature as softer alternative to unfriending
- Blocking is separate from unfriending (prevents all interaction)

#### 4. Follow Relationships (Asymmetric)

Introduced September 2011 as "Subscribe", renamed to "Follow" December 2012.

**Design:**
- One-way relationship (A follows B, B doesn't need to follow A)
- No acceptance required
- Only applies to public updates
- Four possible states between two users:
  1. Neither follows the other
  2. A follows B (not mutual)
  3. B follows A (not mutual)
  4. Mutual follows

**Evolution:** Facebook was historically symmetric (friend or nothing). Follow was added to compete with Twitter's asymmetric model and enable following public figures without the social contract of "friending."

#### 5. Group Membership

**Edge type:** User → Group (member_of)

**Properties:**
- Role: member, admin, moderator
- Joined timestamp
- Approved by (for closed/private groups)

**Access:** Groups API requires specific feature enablement post-2018.

#### 6. Page Relationships

**Likes (user → page):**
- Asymmetric (page doesn't "like back")
- `/user/likes` edge returns liked pages
- Includes `created_time` (when user liked)
- Music, books, movies, sports teams are special page-like types

**Admin/Manager (user → page):**
- `/user/accounts` edge for pages where user has a role
- Multiple role types (admin, editor, moderator, advertiser, analyst)

#### 7. Event Attendance

**Edge types:**
- attending (confirmed)
- maybe (tentative)
- declined
- invited (hasn't responded)

**Properties:**
- RSVP timestamp
- Invited by (which user sent the invite)

**Access:** Event attendance endpoints restricted to Facebook Marketing Partners for Users/Pages; Groups require admin token.

#### 8. Tagged Relationships

**Edge type:** Entity → User (tagged_in)

**Appears on:**
- Photos
- Posts
- Videos
- Check-ins (deprecated)

**Behavior:**
- Creates notification
- Subject can remove tag
- Privacy: tag visibility follows the content's privacy

---

### TAO Association Model

Facebook's TAO system stores relationships as **typed directed edges** called associations.

**Association structure:**
```
(source_id, association_type, destination_id, timestamp, data)
```

**Key design decisions:**

1. **At most one association per type between two objects**
   - You can't "like" something twice
   - Different types can coexist (like + comment on same post)

2. **Timestamps are required**
   - Enables "association lists" ordered by recency
   - Supports queries like "most recent comments" or "friends added this year"

3. **Bidirectional relationships use inverse types**
   - Friend relationship = two associations with inverse types
   - If A friends B: (A, friend, B) AND (B, friend, A)
   - Enables efficient queries from either direction

4. **No restrictions on type connections**
   - Any association type can theoretically connect any node types
   - Schema flexibility over strict validation

5. **Optional data payload**
   - Associations can carry additional key-value data
   - Example: family relationship stores the relationship name ("mother", "uncle")

---

### Relationship Metadata

#### Timestamps

Every relationship has temporal data:

| Relationship | Timestamp Meaning |
|-------------|-------------------|
| Friend | When friendship was confirmed |
| Follow | When follow started |
| Like | When page/content was liked |
| Group member | When user joined |
| Event attending | When RSVP was made |
| Tagged | When tag was created |

#### Anniversary Dates

For romantic relationships, users can specify:
- Anniversary date (day, month, year)
- Displayed on profile similar to birthday
- Friends receive anniversary reminders
- Added December 2009

#### Connection Strength (Internal)

Facebook calculates relationship strength using:

1. **Mutual friends** — Primary signal
   - 100+ mutual friends = 90%+ chance of knowing in real life
   - 1 mutual friend = ~50% chance
   - Users 42% more likely to accept requests from high-mutual-friend users

2. **Profile overlap**
   - Shared hometown, current city, schools, workplaces

3. **Interaction patterns**
   - Likes, comments, tags, wall posts
   - Two-way interactions 30% more predictive than passive engagement

4. **Dispersion metric** (research)
   - Measures whether mutual friends are themselves connected
   - High dispersion = stronger tie (romantic partners have dispersed networks)
   - Used to identify closest relationships in neighborhood

---

### Privacy Model for Relationships

#### Audience Selector

Relationship visibility controlled via standard Facebook audience options:
- **Public** — Anyone can see
- **Friends** — Only friends
- **Friends except...** — Exclude specific people
- **Specific friends** — Allowlist
- **Only me** — Hidden

#### Independent Control

Each person controls their own relationship visibility:
- A can show "In a relationship with B" publicly
- B can set the same relationship to "Only me"
- No requirement for matching privacy settings

#### Mutual Confirmation

Certain relationships require both parties to confirm:
- Romantic relationships (In a relationship, Engaged, Married, etc.)
- Family relationships

Until confirmed by both, relationship doesn't appear on either profile.

#### Silent Status Changes

Some status transitions don't create Feed stories:
- Changing to "Single"
- Changing to "Divorced"
- Removing relationship status entirely

This is intentional — Facebook recognizes relationship endings are sensitive.

---

### API Evolution and Restrictions

#### Pre-2018 (Open Access)

- `/user/friends` — Full friend list
- `/user/family` — Family relationships with types
- Apps could access friends of friends
- Extensive social graph data available to developers

#### Cambridge Analytica Impact (2018)

- 87 million users' data harvested via friends-of-friends access
- Facebook restricted API access dramatically

#### Post-v3.2 Deprecations

| Endpoint | Status |
|----------|--------|
| `/user/friends` | Only returns friends who use the app |
| `/user/family` | Removed entirely |
| `/user/relationship_status` | Returns no data |
| `/user/groups` | Requires approved use case |

#### Current State (v24.0)

Relationship data is largely inaccessible via API:
- Friend lists only return app-using friends
- Family relationships unavailable
- Relationship status field returns no data
- Most social edges require specific permissions and app review

---

### Implicit Relationships

Beyond explicit user-declared relationships, Facebook infers connections from:

#### Interaction-Based
- Frequent message exchanges
- Regular profile views
- Comment/like patterns
- Photo tag frequency

#### Proximity-Based
- Check-in co-occurrence
- Location data overlap
- Event co-attendance

#### Contact-Based
- Uploaded phone contacts
- Email contacts
- "People You May Know" derived connections

#### Platform-Derived
- Same-organization membership (Workplace)
- Game/app co-usage
- Group co-membership

---

### Key Takeaways for Entity Modeling

1. **Separate relationship types from relationship instances**
   - "friend" is a type; "Alice friends Bob" is an instance
   - Types define behavior (symmetric vs asymmetric, confirmation required, etc.)

2. **Timestamps on all relationships**
   - Enables temporal queries and ordering
   - Required for "since" semantics

3. **Metadata varies by relationship type**
   - Romantic: anniversary date
   - Family: relationship name
   - Event: RSVP status
   - Consider type-specific schemas

4. **Privacy is per-relationship, not per-entity**
   - Entity visibility and relationship visibility are independent
   - Both parties in a relationship may have different privacy settings

5. **Bidirectional ≠ Symmetric**
   - Bidirectional = edges in both directions (friend)
   - Symmetric = same relationship type both ways
   - Can have bidirectional asymmetric (A follows B, B follows A are independent)

6. **Relationship lifecycle matters**
   - Creation, confirmation, modification, termination
   - Each state transition may have different behaviors (notifications, Feed stories)

7. **API access ≠ Data existence**
   - Facebook has vastly more relationship data than they expose
   - Connection strength, inferred relationships, interaction patterns all exist internally

8. **Vertical-specific schemas are powerful**
   - OGP uses namespaces: music.*, video.*, article, book, profile
   - Each vertical has domain-specific properties
   - Base properties apply to all, vertical properties extend

9. **Entity IDs should be product-agnostic**
   - Each Meta product uses its own ID space
   - Cross-product identity is a separate concern (Accounts Center)
   - Don't couple entity IDs to a single platform

10. **Content types are hierarchical**
    - Base type (Post/Media) with specific subtypes (Photo, Video, Reel, Story)
    - `media_type` and `media_product_type` as discriminators
    - Enables polymorphic queries while maintaining type safety

11. **Engagement is first-class**
    - Reactions are typed (LIKE, LOVE, HAHA, etc.) not just counts
    - Each engagement is a relationship with timestamp
    - Enables queries like "things I liked this week"

12. **Containers vs Content**
    - Album contains Photos, Group contains Posts, Event has Attendees
    - Container relationships: contains, member_of, posted_to
    - Containers have counts, privacy, membership rules

13. **Publishing workflows**
    - IG Container pattern: create container → upload media → publish
    - Separates intent (container) from final content (published media)
    - Enables status tracking: IN_PROGRESS, ERROR, FINISHED, PUBLISHED

14. **Edge pagination is essential**
    - All collection edges use cursor-based pagination
    - Total counts are expensive (only available with summary=true)
    - Optimize for "most recent N" not "all"
