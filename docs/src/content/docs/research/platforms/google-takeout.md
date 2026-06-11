---
title: Google Takeout Entity Research
description: Using Google's 72 products as inspiration for entity types. What entities live in each product? What relationships exist?
---

**Source:** https://takeout.google.com/

---

## Why This Matters

Google has spent 25 years building products that manage human information. Their Takeout export reveals what they consider the atomic units of each domain. This is invaluable research for entity modeling.

**Our goal:** For each product, identify:
1. What entities exist?
2. What relationships connect them?
3. Do we need new entity types, or do existing ones cover it?

---

## Key People

Product leads, engineers, and designers behind Google's products.

| Person | Role | Product | Era |
|--------|------|---------|-----|
| Paul Buchheit | Creator, Engineer | Gmail, AdSense prototype | 2001-2006 |
| Brian Rakowski | VP Product Management | Gmail, Chrome, Android, Pixel | 2002-present |
| Sundar Pichai | Product Lead → CEO | Chrome, Drive, Android | 2008-present |
| Vic Gundotra | SVP | Google+, Photos precursor | 2010-2014 |
| Bradley Horowitz | VP Product | Google Photos, Streams | 2015-present |
| Anil Sabharwal | VP Engineering | Google Photos, Drive, Docs Mobile | 2015-present |
| Dave Besbris | VP Engineering | Google+ | 2014-2015 |
| Brian Fitzpatrick | Founder | Data Liberation Front, Google Takeout | 2007-2011+ |
| Bret Taylor | Product Lead | Google Maps, Google Local | 2003-2007 |
| Lars Rasmussen | Co-creator | Google Maps, Google Wave | 2004-2010 |
| Jeff Dean | Senior Fellow | Infrastructure (Bigtable, MapReduce) | 1999-present |
| Sanjay Ghemawat | Senior Fellow | Infrastructure (Bigtable, GFS, MapReduce) | 1999-present |
| Steve Chen | Co-founder | YouTube | 2005-2011 |
| Chad Hurley | Co-founder, CEO | YouTube | 2005-2010 |
| Jawed Karim | Co-founder | YouTube | 2005 |

### Key People Details

**Paul Buchheit (Gmail)**: Google's 23rd employee, hired in 1999. Began developing Gmail in August 2001, creating the first version in a single day by reusing code from Google Groups. Used JavaScript/AJAX to create the fast, dynamic interface. Also developed the AdSense prototype and suggested Google's "Don't be evil" motto. Left Google in 2006 to co-found FriendFeed with Bret Taylor (acquired by Facebook in 2009). Later became a Y Combinator partner.

**Brian Rakowski**: Google's first Associate Product Manager (2002). Started on Gmail team until late 2004. Spent 8 years leading Chrome product management, then moved to Android, then Pixel phones in 2017. Stanford graduate in symbolic systems and psychology.

**Bradley Horowitz**: Joined Google in 2008 as VP of Product for consumer apps, overseeing Gmail, Docs, Calendar, Talk, Voice, Picasa, Orkut, and Blogger. Conceived Google+ with Vic Gundotra (2011). Took over Google Photos and Streams in March 2015. Previously studied computer vision in grad school, co-founded Virage (video metadata), and oversaw Yahoo's Flickr acquisition.

**Anil Sabharwal (Google Photos)**: Led the team that conceived, built, and launched Google Photos in May 2015. Grew it to 500M monthly users in 2 years, reaching 1 billion users by summer 2019. Previously led Google Drive and Docs mobile teams. Now VP of Connectivity & Communications (Duo, Messages, Project Fi). Moved to Sydney in 2018 as Google Australia engineering site lead.

**Brian Fitzpatrick (Data Liberation Front)**: Founded Google's Data Liberation Front around 2007. Created Google Takeout (released June 28, 2011). Also created Google's Transparency Report. Joined Google in 2005 from Chicago. Philosophy: data liberation prevents engineering complacency. The Data Liberation Front partnered with Facebook, Microsoft, and Twitter in 2018 to create the Data Transfer Project.

**Bret Taylor (Google Maps)**: Joined Google in 2003. Led the team that co-created Google Maps and Google Local. Left in 2007 to co-found FriendFeed (CEO 2007-2009). After Facebook acquired FriendFeed, became Facebook CTO (2010-2012), creating Open Graph, App Center, and the Like button. Later founded Quip (acquired by Salesforce), became Salesforce co-CEO, Twitter board chairman, and now co-founder of AI startup Sierra and OpenAI chairman.

**Lars Rasmussen (Google Maps)**: Danish computer scientist with PhD from UC Berkeley. Co-founded Where 2 Technologies in Sydney (2003) with brother Jens. Google acquired it in 2004 as foundation for Google Maps. Led Google Wave project (discontinued 2010). Left Google for Facebook in 2010 where he led Graph Search. Now angel investor based in Athens.

**Jeff Dean & Sanjay Ghemawat (Infrastructure)**: Met at DEC research labs before joining Google in 1999. Co-designed MapReduce, Bigtable, Google File System, and Protocol Buffers. Only two employees with Senior Fellow title (Google's highest technical level). Won 2012 ACM Prize in Computing.

---

## Current Entity Types (from entity-experiments)

| Type | Description |
|------|-------------|
| `person` | A human |
| `organization` | Group (company, band, team) |
| `place` | A location |
| `product` | Something you use (software, tool) |
| `concept` | Idea or pattern |
| `work` | Creative output (book, song, article) |
| `webpage` | Web source with URL |
| `quote` | Notable saying |

**From apps-repo brainstorming:**
- `task` — unit of work
- `event` — calendar event
- `message` — chat/email message
- `conversation` — thread of messages
- `file` — document or media
- `note` — freeform text
- `project` — container for tasks
- `calendar` — container for events
- `label` — tag/category
- `contact` — person with contact info (subset of person?)

---

## Tier 1: Core, Universal, Entity-Rich

These products are used by almost everyone and contain rich, well-structured entities.

| Product | Likely Entities | Relationships | Research Status |
|---------|-----------------|---------------|-----------------|
| **Contacts** | person, organization | person↔organization (works_at) | ✅ Done |
| **Calendar** | event, calendar, person | event↔calendar, event↔person (attendees) | ✅ Done |
| **Drive** | file, folder | file↔folder (contains), file↔person (owner, shared_with) | ✅ Done |
| **Gmail/Mail** | message, conversation, person, file | message↔conversation, message↔person (from/to), message↔file (attachment) | ✅ Done |
| **Google Photos** | photo, video, album, person, place | photo↔album, photo↔person (faces), photo↔place | ✅ Done |
| **Keep** | note, task, label | note↔label, note↔person (collaborator) | ✅ Done |
| **Tasks** | task, list | task↔list, task↔task (subtasks) | ✅ Done |
| **YouTube** | video, channel, playlist, comment, person | video↔channel, video↔playlist, comment↔video, comment↔person | ✅ Done |
| **Maps (your places)** | place, visit, activitySegment | visit↔place, activitySegment↔place | ✅ Done |

---

## Tier 2: Valuable Entities, More Niche

These products have clear entities but serve more specific use cases.

| Product | Likely Entities | Relationships | Research Status |
|---------|-----------------|---------------|-----------------|
| **Chrome** | bookmark, history_entry | bookmark↔folder, history↔webpage | ✅ Done |
| **Google Chat** | message, conversation, person | message↔conversation, conversation↔person | ✅ Done |
| **Blogger** | post, blog, comment, label | post↔blog, comment↔post, post↔author, post↔label | ✅ Done |
| **Fit/Fitbit** | workout, sleep_record, health_metric | workout↔place, metric↔date | ✅ Done |
| **Google Pay/Wallet** | transaction, pass, loyaltyCard, eventTicket | pass↔event, pass↔person, loyaltyCard↔organization | ✅ Done |
| **Play Books** | book, highlight, note, bookmark | highlight↔book, note↔book, book↔author | ✅ Done |
| **Play Store** | app, purchase, subscription, review | app↔review, purchase↔app, subscription↔app | ✅ Done |
| **Play Movies & TV** | movie, tvshow, episode, watchActivity | episode↔tvshow, watchActivity↔movie | ✅ Done |
| **Podcasts** | podcast, episode, subscription | episode↔podcast, subscription↔podcast | ✅ Done |
| **Reminders** | reminder | reminder↔date, reminder↔place | ✅ Done |
| **Voice** | phoneCall, voicemail, textMessage | call↔person, voicemail↔person, message↔conversation | ✅ Done |
| **Timeline** | location_history, visit | visit↔place, visit↔date | ✅ Done (with Maps) |
| **Saved** | saved_item, collection | savedItem↔collection, savedItem↔webpage | ✅ Done |
| **Profile** | person (self) | — | ⬜ TODO |
| **Purchases & Reservations** | order, reservation, delivery | order↔product, reservation↔place, delivery↔order | ✅ Done |
| **Messages** | sms, mms, rcsMessage | message↔person, message↔conversation | ✅ Done |

---

## Tier 3: Settings-Heavy, Developer Tools, Sparse Entities

These are primarily configuration or developer-focused. Lower priority for entity research.

| Product | Notes | Research Status |
|---------|-------|-----------------|
| **Access Log Activity** | Activity logs, meta-data | ⬜ Skip |
| **Alerts** | Subscriptions/preferences | ⬜ Skip |
| **Arts & Culture** | Favorites, galleries | ⬜ TODO |
| **Assignments/Classroom** | Educational: courses, assignments, submissions | ⬜ TODO |
| **Canvas/Cursive** | Drawings (work subtype?) | ⬜ Skip |
| **Discover** | Preferences/follows | ⬜ Skip |
| **Embark** | Supplier enrollment | ⬜ Skip |
| **Firebase Dynamic Links** | Developer tool | ⬜ Skip |
| **Gemini** | Gems (AI assistants?) | ⬜ TODO |
| **Google Account** | Account activity | ⬜ Skip |
| **Google Ads** | Advertiser data | ⬜ Skip |
| **Google Business Profile** | Business data | ⬜ TODO |
| **Google Cloud Search** | Search metadata | ⬜ Skip |
| **Google Developers** | Developer profile | ⬜ Skip |
| **Google Earth** | Projects, features, places | ⬜ TODO |
| **Google Feedback** | Feedback reports | ⬜ Skip |
| **Google Finance** | Portfolios, watchlists | ⬜ TODO |
| **Google Help Communities** | Q&A contributions | ⬜ Skip |
| **Google Meet** | Meeting data | ⬜ TODO |
| **Google One** | Membership data | ⬜ Skip |
| **Google Shopping** | Reviews | ⬜ Skip |
| **Google Store** | Purchases, reviews | ⬜ Skip |
| **Google Translator Toolkit** | Documents | ⬜ Skip |
| **Google Workspace Marketplace** | App metadata | ⬜ Skip |
| **Groups** | Groups, memberships | ⬜ TODO |
| **Home App** | Devices, rooms, homes | ⬜ TODO |
| **Journal** | Journal entries (note subtype) | ⬜ TODO |
| **My Activity** | Activity logs | ⬜ Skip |
| **My Maps** | Custom maps, features | ⬜ TODO |
| **News** | Preferences | ⬜ Skip |
| **NotebookLM** | Notebooks, sources | ⬜ TODO |
| **Personal Safety** | Safety data | ⬜ Skip |
| **Phone Audio** | Recordings, transcripts | ⬜ TODO |
| **Pinpoint** | Uploaded files | ⬜ Skip |
| **Pixel** | Device diagnostics | ⬜ Skip |
| **Recorder** | Audio recordings | ⬜ TODO |
| **Search Contributions** | Ratings, reviews | ⬜ Skip |
| **Search Notifications** | Subscriptions | ⬜ Skip |
| **Street View** | Uploaded images | ⬜ Skip |
| **Workspace Studio** | Workflows | ⬜ Skip |

---

## Candidate New Entity Types

Based on initial scan, these might need dedicated types (vs. existing or subtypes):

| Candidate | Why | Existing Alternative? |
|-----------|-----|----------------------|
| `event` | Calendar events, meets, reservations | — (new type) |
| `task` | Tasks, reminders | — (new type) |
| `message` | Email, chat, SMS, voicemail | — (new type) |
| `conversation` | Thread/container for messages | collection? |
| `file` | Drive files, photos, videos | work subtype? |
| `transaction` | Purchases, payments | — (new type?) |
| `bookmark` | Saved links | webpage with relationship? |
| `health_record` | Fit/Fitbit data | — (new type?) |
| `device` | Home devices, phones | product subtype? |

---

## Research Protocol

For each Tier 1/2 product:

1. **Export format**: What file format does Google use? (JSON, MBOX, iCal, etc.)
2. **Schema**: What fields are exported?
3. **Entities**: What are the atomic units?
4. **Relationships**: How do entities connect?
5. **Mapping**: How does this map to our types?

---

## Research Queue

### Priority 1 (Tier 1) — COMPLETE ✅
- [x] Contacts — People API, vCard/JSContact formats documented
- [x] Calendar — iCal format, jCal RFC, API architecture documented
- [x] Drive — Metadata JSON, sharing limitations documented
- [x] Gmail/Mail — MBOX format, threading, architecture documented
- [x] Google Photos — JSON sidecar metadata, Spanner backend documented
- [x] Keep — Note/list JSON structure, API fields documented
- [x] Tasks — Full JSON schema, subtask hierarchy documented
- [x] YouTube — Watch history JSON, subscriptions CSV documented
- [x] Maps/Timeline — Semantic Location History fully documented

### Priority 2 (Tier 2) — COMPLETE ✅
- [x] Chrome — History JSON format documented
- [x] Google Chat/Hangouts — JSON structure documented
- [x] Blogger — Atom XML export, API JSON schema documented
- [x] Fit/Fitbit — JSON export documented
- [x] Google Pay/Wallet — Pass types (Event, Loyalty, Transit, Flight) fully documented
- [x] Play Books — Drive sync export, third-party tools documented
- [x] Play Store — Data Portability API schema (Installs, Purchases, Subscriptions) documented
- [x] Play Movies & TV — My Activity export format documented
- [x] Podcasts — OPML export format, service shutdown migration documented
- [x] Reminders — JSON export structure documented
- [x] Voice — HTML export, parsing tools documented
- [x] Timeline — (Same as Maps, fully documented)
- [x] Saved — CSV export with collections structure documented
- [x] Purchases & Reservations — Gmail schema.org markup (Order, FlightReservation, ParcelDelivery) documented
- [x] Messages — Android Backup, third-party XML export documented

---

---

## Findings

### GOOGLE TAKEOUT OVERVIEW

**Data Liberation Front History**: Founded by Brian Fitzpatrick around 2007 with the mission to make it easy for users to move data in and out of Google products. Google Takeout launched June 28, 2011 after 4 years of development. Now supports 57+ products. In 2018, partnered with Facebook, Microsoft, and Twitter to create the Data Transfer Project for cross-platform data portability.

**Data Portability API**: Google now offers a programmatic Data Portability API (developers.google.com/data-portability) that allows third-party apps to request user authorization to export data. Supports time-based access (30 or 180 days), time filters for requesting specific date ranges (as of Feb 2025), and requires app verification before release.

---

### EXPORT FORMATS BY PRODUCT

#### 1. GOOGLE CONTACTS
**Export Formats**: CSV, vCard (.vcf)

**vCard Standard (RFC 6350)**: Defines fields for formatted/structured names, delivery addresses, email addresses, phone numbers, photos, logos, audio clips.

**JSON Representations**:
- **jCard (RFC 7095)**: Direct JSON mapping of vCard format
- **JSContact (RFC 9553)**: Newer JSON alternative (May 2024), redesigned data model with better clarity and extensibility

**People API Fields** (resourceName identifies the person):
- `resourceName`, `etag` — Identifiers
- `names[]` — Structured name data
- `addresses[]` — Delivery addresses
- `emailAddresses[]`, `phoneNumbers[]` — Contact methods
- `photos[]`, `urls[]` — Visual and web presence
- `organizations[]` — Work/company info
- `birthdays[]`, `genders[]` — Demographics
- `biographies[]`, `occupations[]`, `skills[]` — Professional
- `relations[]` — Family/relationship links
- `memberships[]` — Contact groups
- `externalIds[]` — Cross-system identifiers

**Entity Types**: Person, Organization
**Key Relationships**: person↔organization (works_at), person↔person (relations)

---

#### 2. GOOGLE CALENDAR
**Export Formats**: iCalendar (.ics), JSON (limited)

**iCalendar Fields (RFC 5545)**:
- Event start/end time
- Recurrence rules (RRULE)
- Invitees and response statuses
- Title, description, location
- Creation/modification timestamps

**JSON Format**: Only exported for Meeting Breakout configurations

**jCal (RFC 7265)**: Industry standard for JSON representation of iCalendar data (not native Google export)

**Google Calendar API Architecture**:
- REST+JSON API since 2011
- Uses RFC 5545 recurrence standards (shared with Microsoft, Apple)
- Backend: Google Spanner database
- Cache layers: Cache Storage, IndexedDB (offline mode), CDN
- Services: Heartbeat, eventing (pub/sub for webhooks), notifications

**Entity Types**: Event, Calendar, Person (attendees)
**Key Relationships**: event↔calendar, event↔person (organizer, attendee), event↔event (recurring)

---

#### 3. GOOGLE DRIVE
**Export Formats**: Original file formats + JSON metadata

**Metadata JSON Fields**:
- `photoTakenTime` — Timestamp
- `header` — Product name
- `title` — File summary

**Important Limitations**:
- Sharing/permissions NOT preserved in Takeout
- No folder structure preservation for permissions
- Processing time varies (minutes to days)

**Entity Types**: File, Folder, Person (owner, collaborator)
**Key Relationships**: file↔folder (contains), file↔person (owned_by, shared_with)

---

#### 4. GMAIL
**Export Formats**: MBOX, PST (via Vault)

**MBOX Format (RFC 4155)**:
- Each message starts with "From " separator line (email + timestamp)
- Full message headers and body follow
- Messages terminated by empty line
- All labels collapsed into single folder (labels NOT converted to mailboxes)

**Gmail Architecture**:
- Microservices architecture across distributed data centers
- Storage: Colossus distributed file system + Bigtable NoSQL database
- Caching: Fan-Out Write (metadata on send), Write-Through Cache, Cache-Aside
- Search: Uses Google Search technology for rapid email search
- Threading: Conversation-based (linear path, not tree)

**Conversation Threading (Gmail API)**:
- Thread resources group replies with original messages
- Only latest message, immediate parent, and first message initially visible
- Quoted text hidden by default
- Messages cannot be archived individually (only threads)

**Vault Export** includes:
- MBOX/PST file with messages
- Separate metadata file correlating messages with Google's server data

**Entity Types**: Message, Conversation (Thread), Person, File (attachment)
**Key Relationships**: message↔conversation, message↔person (from, to, cc, bcc), message↔file (attachment)

---

#### 5. GOOGLE PHOTOS
**Export Formats**: Original image/video files + JSON sidecar metadata

**JSON Metadata Structure** (per photo):
```json
{
  "title": "IMG_1234.jpg",
  "description": "User caption",
  "photoTakenTime": {
    "timestamp": "1234567890",
    "formatted": "Jan 1, 2020, 12:00:00 PM UTC"
  },
  "creationTime": { ... },
  "photoLastModifiedTime": { ... },
  "geoData": {
    "latitude": 37.7749,
    "longitude": -122.4194,
    "altitude": 0,
    "latitudeSpan": 0,
    "longitudeSpan": 0
  },
  "geoDataExif": { ... },
  "googlePhotosOrigin": { ... }
}
```

**Folder Organization**:
- Date-based folders (e.g., 2020-09-01)
- Album folders by name
- Photos may appear in both date AND album folders (duplicates)

**Known Issues**:
- EXIF data stripped from files, stored only in JSON sidecars
- Inconsistent JSON filename patterns (filename.jpg.json OR filename.json)
- Timestamps sometimes missing or malformed

**Google Photos Architecture**:
- Backend: Google Spanner (4 trillion photos/videos, 1B+ users)
- "People, Places, and Things" graph structure (mirrors Knowledge Graph organizing principles)
- Face Groups: ML clustering of similar faces (not identification)
- Dozens of Flume batch pipelines for AI/ML processing
- 99.999% availability via Spanner's automatic sharding

**Entity Types**: Photo, Video, Album, Person (face group), Place
**Key Relationships**: photo↔album, photo↔person (appears_in), photo↔place (taken_at)

---

#### 6. GOOGLE KEEP
**Export Formats**: JSON

**JSON Structure (from Keep API)**:
```json
{
  "name": "notes/abc123",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "trashed": false,
  "title": "Note title (max 1000 chars)",
  "body": {
    "text": { "text": "Note content (max 20000 chars)" },
    "list": {
      "listItems": [{
        "text": "Item text (max 1000 chars)",
        "checked": false,
        "childListItems": [...]
      }]
    }
  },
  "color": "DEFAULT|RED|ORANGE|YELLOW|GREEN|TEAL|BLUE|CERULEAN|PURPLE|PINK|BROWN|GRAY",
  "labels": [...],
  "attachments": [...],
  "permissions": [...]
}
```

**Exported Data**:
- Note content (text, list items)
- Attachments (voice recordings, drawings, images)
- Color, pinned/archived state
- Collaborators
- Labels

**Entity Types**: Note, Task (list items), Label, Person (collaborator)
**Key Relationships**: note↔label, note↔person (collaborator), note↔note (if nesting supported)

---

#### 7. GOOGLE TASKS
**Export Formats**: JSON

**JSON Structure (Tasks API)**:
```json
{
  "kind": "tasks#task",
  "id": "abc123",
  "etag": "\"xyz\"",
  "title": "Task name (max 1024 chars)",
  "updated": "2024-01-01T00:00:00Z",
  "selfLink": "https://...",
  "parent": "parent_task_id",
  "position": "00000000000000000001",
  "notes": "Description (max 8192 chars)",
  "status": "needsAction|completed",
  "due": "2024-01-15T00:00:00Z",
  "completed": "2024-01-14T12:00:00Z",
  "deleted": false,
  "hidden": false,
  "links": [{
    "type": "email|related",
    "description": "Link description",
    "link": "https://..."
  }],
  "webViewLink": "https://...",
  "assignmentInfo": { ... }
}
```

**Key Fields**:
- `parent` — For subtask hierarchy
- `position` — Lexicographical ordering string
- `status` — Only "needsAction" or "completed"
- `due` — Date only (no time), RFC 3339

**Entity Types**: Task, TaskList
**Key Relationships**: task↔tasklist, task↔task (subtask)

---

#### 8. YOUTUBE
**Export Formats**: JSON (history), CSV (subscriptions, playlists)

**Watch History (JSON)**:
Located at: `Takeout/YouTube and YouTube Music/history/watch-history.json`
```json
{
  "header": "YouTube",
  "title": "Watched [Video Title]",
  "titleUrl": "https://www.youtube.com/watch?v=...",
  "subtitles": [{"name": "Channel Name", "url": "..."}],
  "time": "2024-01-01T12:00:00.000Z",
  "products": ["YouTube"],
  "activityControls": ["YouTube watch history"]
}
```

**Subscriptions (CSV)**:
Located at: `Takeout/YouTube and YouTube Music/subscriptions/subscriptions.csv`
```
Channel Id,Channel Url,Channel Title
UC1JTQBa5...,http://www.youtube.com/channel/UC1JTQBa5...,Channel Name
```

**Playlists**: CSV format

**Video Metadata (Data Portability API)**:
- Video ID, duration, language, category
- Description, channel ID, privacy status
- Upload timestamp
- Available in original format or MP4

**Entity Types**: Video, Channel, Playlist, Comment, Subscription
**Key Relationships**: video↔channel (uploaded_by), video↔playlist, subscription↔channel

---

#### 9. GOOGLE MAPS / TIMELINE
**Export Formats**: JSON (Semantic Location History, Records.json, Settings.json)

**Folder Structure**:
```
Semantic Location History/
├── 2022_JANUARY.json
├── 2022_FEBRUARY.json
└── ...
Records.json
Settings.json
Timeline Edits.json
```

**Semantic Location History JSON Structure**:
```json
{
  "timelineObjects": [
    {
      "activitySegment": {
        "startLocation": {
          "latitudeE7": 414083590,
          "longitudeE7": 21704229,
          "sourceInfo": {"deviceTag": 1114211210}
        },
        "endLocation": { ... },
        "duration": {
          "startTimestamp": "2022-03-03T12:22:24Z",
          "endTimestamp": "2022-03-03T12:43:34Z"
        },
        "distance": 2640,
        "activityType": "IN_BUS",
        "confidence": "HIGH",
        "activities": [
          {"activityType": "IN_BUS", "probability": 85.68},
          {"activityType": "WALKING", "probability": 8.42}
        ],
        "transitPath": {
          "transitStops": [{
            "placeId": "ChIJWey1zMWipBIRiNQSzpI4EDQ",
            "address": "...",
            "name": "Stop Name"
          }],
          "name": "H8",
          "hexRgbColor": "009EE0",
          "linePlaceId": "..."
        }
      }
    },
    {
      "placeVisit": {
        "location": {
          "latitudeE7": 414036299,
          "longitudeE7": 21743558,
          "placeId": "ChIJk_s92NyipBIRUMnDG8Kq2Js",
          "address": "...",
          "name": "La Sagrada Familia",
          "semanticType": "TYPE_SEARCHED_ADDRESS"
        },
        "duration": { ... },
        "placeConfidence": "HIGH_CONFIDENCE",
        "visitConfidence": 95,
        "otherCandidateLocations": [...]
      }
    }
  ]
}
```

**Activity Types**:
WALKING, DRIVING, IN_BUS, IN_PASSENGER_VEHICLE, IN_SUBWAY, IN_TRAIN, IN_TRAM, CYCLING, STILL, FLYING, BOATING, HIKING, RUNNING, SKIING, SWIMMING, etc.

**Semantic Types** (for places):
- TYPE_HOME — User's designated home
- TYPE_WORK — User's designated work
- TYPE_SEARCHED_ADDRESS — Previously searched
- TYPE_ALIASED_LOCATION — User-labeled place

**Coordinates**: Stored as latitudeE7/longitudeE7 (degrees × 10^7, integer)

**Entity Types**: Place, Visit, ActivitySegment, TransitStop
**Key Relationships**: visit↔place, activitySegment↔place (start, end), transitStop↔transitLine

---

#### 10. CHROME
**Export Formats**: JSON

**Browsing History JSON Structure**:
```json
{
  "Browser History": [{
    "url": "https://example.com",
    "title": "Page Title",
    "favicon_url": "https://...",
    "page_transition": "LINK|TYPED|AUTO_BOOKMARK|...",
    "time_usec": 1234567890123456,
    "client_id": "abc123",
    "ptoken": "..."
  }]
}
```

**Exported Data**: History, bookmarks, autofill, dictionary, extensions, search engines

**Limitation**: No way to re-import exported history back into Chrome

**Entity Types**: HistoryEntry, Bookmark, Folder
**Key Relationships**: bookmark↔folder, historyEntry↔webpage

---

#### 11. GOOGLE CHAT / HANGOUTS
**Export Formats**: JSON

**Hangouts.json Structure**:
- Located in "Hangouts" subfolder
- ~10% actual messages, ~90% metadata
- Contains: participant IDs, conversation IDs, read status, timestamps

**Parsing Tools**:
- hangoutparser.jay2k1.com (web-based, exports to HTML/text/XML/XLSX/CSV)
- Various GitHub tools for CLI parsing

**Entity Types**: Message, Conversation, Person (participant)
**Key Relationships**: message↔conversation, conversation↔person (participant)

---

#### 12. GOOGLE FIT
**Export Formats**: JSON

**Exported Data**: Activities, daily summaries, sessions, steps

**Entity Types**: Workout, HealthMetric, SleepRecord
**Key Relationships**: workout↔place, metric↔date

---

#### 13. BLOGGER
**Export Formats**: Atom XML (Takeout), JSON (API)

**Takeout Export**: Each blog is exported as a separate Atom.xml file within a zip archive. The Atom format contains all posts, comments, and metadata in XML structure.

**Blogger API JSON Schema** (v3):

**Posts Resource**:
```json
{
  "kind": "blogger#post",
  "id": "post_id_string",
  "blog": { "id": "blog_id" },
  "published": "RFC3339 datetime",
  "updated": "RFC3339 datetime",
  "url": "https://...",
  "title": "Post title (text)",
  "content": "Post content (may contain HTML)",
  "author": {
    "id": "author_id",
    "displayName": "Author Name",
    "url": "profile_url",
    "image": { "url": "avatar_url" }
  },
  "labels": ["tag1", "tag2"],
  "replies": {
    "totalItems": 5,
    "selfLink": "https://..."
  },
  "location": {
    "name": "Location name",
    "lat": 37.7749,
    "lng": -122.4194,
    "span": "lat_span,lng_span"
  },
  "status": "LIVE|DRAFT|SCHEDULED"
}
```

**Comments Resource**:
```json
{
  "kind": "blogger#comment",
  "id": "comment_id",
  "post": { "id": "post_id" },
  "blog": { "id": "blog_id" },
  "published": "RFC3339 datetime",
  "updated": "RFC3339 datetime",
  "content": "Comment text",
  "author": {
    "id": "author_id",
    "displayName": "Commenter Name",
    "url": "profile_url",
    "image": { "url": "avatar_url" }
  },
  "inReplyTo": { "id": "parent_comment_id" }
}
```

**API Data Model**: Five resource types — Blogs, Posts, Comments, Pages, Users

**Note**: Blogger JSON API v2.0 was discontinued September 30, 2024. Applications must use v3.

**Entity Types**: Blog, Post, Comment, Page, Author (Person)
**Key Relationships**: post↔blog, comment↔post, comment↔comment (replies), post↔author, post↔label

---

#### 14. GOOGLE PAY / WALLET
**Export Formats**: JSON (Takeout), PDF statements (pay.google.com)

**Takeout Export**: Wallet activity (tap-to-pay, P2P transfers) exported as JSON. Must be converted for spreadsheet analysis.

**Google Wallet API Pass Types**:
- **FlightClass/FlightObject** — Boarding passes
- **EventTicketClass/EventTicketObject** — Event tickets
- **LoyaltyClass/LoyaltyObject** — Loyalty/rewards cards
- **TransitClass/TransitObject** — Transit passes
- **OfferClass/OfferObject** — Coupons/offers
- **GenericClass/GenericObject** — Generic passes

**EventTicketObject JSON Structure**:
```json
{
  "id": "ISSUER_ID.OBJECT_ID",
  "classId": "ISSUER_ID.EVENT_CLASS_ID",
  "state": "ACTIVE",
  "ticketHolderName": "John Doe",
  "ticketNumber": "TICKET123",
  "ticketType": { "defaultValue": { "language": "en-us", "value": "General Admission" }},
  "faceValue": { "currencyCode": "USD", "units": "50" },
  "seatInfo": {
    "seat": { "defaultValue": { "language": "en-us", "value": "9" }},
    "row": { "defaultValue": { "language": "en-us", "value": "L" }},
    "section": { "defaultValue": { "language": "en-us", "value": "45" }},
    "gate": { "defaultValue": { "language": "en-us", "value": "7C" }}
  },
  "barcode": { "type": "QR_CODE", "value": "BARCODE_VALUE" },
  "validTimeInterval": { "start": "...", "end": "..." }
}
```

**EventTicketClass JSON Structure**:
```json
{
  "id": "ISSUER_ID.EVENT_CLASS_ID",
  "issuerName": "Event Organizer",
  "eventName": { "defaultValue": { "language": "en-US", "value": "Concert Name" }},
  "venue": {
    "name": { "defaultValue": { "language": "en-US", "value": "Stadium Name" }},
    "address": { "defaultValue": { "language": "en-US", "value": "123 Main St" }}
  },
  "dateTime": { "start": "2024-04-12T19:30" },
  "reviewStatus": "APPROVED"
}
```

**LoyaltyObject JSON Structure**:
```json
{
  "id": "ISSUER_ID.OBJECT_ID",
  "classId": "ISSUER_ID.LOYALTY_CLASS_ID",
  "accountName": "John Doe",
  "accountId": "1234567890",
  "loyaltyPoints": {
    "label": "Points",
    "balance": { "int": "1500" }
  },
  "barcode": { "type": "QR_CODE", "value": "..." },
  "state": "ACTIVE"
}
```

**TransitObject JSON Structure**:
```json
{
  "id": "ISSUER_ID.OBJECT_ID",
  "classId": "ISSUER_ID.TRANSIT_CLASS_ID",
  "ticketNumber": "TKT12345",
  "passengerType": "SINGLE_PASSENGER",
  "passengerNames": "John Doe",
  "tripId": "TRIP001",
  "ticketStatus": "ACTIVE",
  "ticketLeg": {
    "originName": { "defaultValue": { "language": "en", "value": "Station A" }},
    "destinationName": { "defaultValue": { "language": "en", "value": "Station B" }},
    "originStationCode": "STA",
    "destinationStationCode": "STB"
  },
  "ticketSeat": { "seat": "12A", "coach": "3" },
  "fareClass": "ECONOMY"
}
```

**Class-Object Architecture**: All passes use a two-tier model:
- **Class** = shared template (event details, venue, issuer)
- **Object** = individual pass (seat, holder name, barcode)

**Entity Types**: Transaction, Pass (with subtypes: BoardingPass, EventTicket, LoyaltyCard, TransitPass, Offer), PaymentMethod
**Key Relationships**: pass↔event, pass↔person (holder), transaction↔person, transaction↔merchant, loyaltyCard↔organization

---

#### 15. PLAY BOOKS
**Export Formats**: Proprietary (synced to Google Drive), requires third-party conversion

**Official Export Method**: Enable "Save notes, highlights and bookmarks in Google Drive" in Play Books settings. Creates files in "Play Books Notes" folder.

**Exported Data** (via Drive sync):
- Highlights (text selections)
- Notes (user annotations)
- Bookmarks (saved positions)
- Reading progress

**Known Issues**:
- No native JSON export
- Proprietary format requires conversion tools
- Third-party tools: google-books-highlights-export, play-books-notes, highlights-convert

**Entity Types**: Book, Highlight, Note, Bookmark, ReadingProgress
**Key Relationships**: highlight↔book, note↔book, bookmark↔book, book↔author

---

#### 16. PLAY STORE
**Export Formats**: JSON (via Data Portability API)

**Installs Object**:
```json
{
  "doc": {
    "title": "App Name",
    "documentType": "APPLICATION"
  },
  "deviceAttribute": {
    "model": "Pixel 7",
    "manufacturer": "Google",
    "carrier": "T-Mobile"
  },
  "firstInstallationTime": "2024-01-15T10:30:00Z",
  "lastUpdateTime": "2024-06-20T14:22:00Z"
}
```

**Purchases Object**:
```json
{
  "doc": { "title": "App Name", "documentType": "APPLICATION" },
  "invoicePrice": "$4.99",
  "purchaseState": "COMPLETED",
  "purchaserName": "John Doe",
  "paymentMethodTitle": "Visa •••• 1234",
  "purchaseTime": "2024-01-15T10:30:00Z",
  "userLanguageCode": "en",
  "userCountry": "US",
  "giftInfo": {
    "senderName": "Jane Doe",
    "recipientEmail": "john@example.com",
    "giftMessage": "Enjoy!",
    "giftCode": "GIFT123"
  }
}
```

**Subscriptions Object**:
```json
{
  "doc": { "title": "Service Name", "documentType": "SUBSCRIPTION" },
  "expirationDate": "2025-01-15T00:00:00Z",
  "renewalDate": "2025-01-15T00:00:00Z",
  "pricing": { "price": "$9.99", "period": "MONTHLY" },
  "state": "ACTIVE",
  "userChangeRecord": { "type": "REACTIVATION", "timestamp": "..." }
}
```

**Additional Objects**: Library, Devices, Redemptions, Play User Settings, Play Points, Promotions, Play Grouping

**Entity Types**: App, Purchase, Subscription, Device, Review, LibraryItem
**Key Relationships**: app↔review, purchase↔app, subscription↔app, install↔device, review↔person

---

#### 17. PLAY MOVIES & TV
**Export Formats**: JSON/HTML (via My Activity)

**Activity Export Structure**:
```json
{
  "header": "Google Play",
  "title": "Watched Inception",
  "titleUrl": "https://play.google.com/store/movies/details?id=...",
  "subtitles": [{ "name": "Movie details" }],
  "time": "2024-01-15T20:30:00.000Z",
  "products": ["Google Play Store/Movies"],
  "activityControls": ["Web & App Activity"]
}
```

**Data Includes**:
- Watch history (movies, TV episodes)
- Purchases
- Watchlist items
- Ratings (if available through activity)

**Note**: No dedicated schema reference; data exported through My Activity schema.

**Entity Types**: Movie, TVShow, Episode, WatchlistItem, WatchActivity
**Key Relationships**: episode↔tvshow, watchActivity↔movie, watchlistItem↔movie, purchase↔movie

---

#### 18. GOOGLE PODCASTS
**Export Formats**: OPML (subscriptions), JSON (activity via Takeout)

**Service Status**: Google Podcasts shut down; data migration available until July 29, 2024. Subscriptions exportable to YouTube Music or OPML file.

**OPML Export Structure** (RFC compliant):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
  <head>
    <title>Google Podcasts Subscriptions</title>
    <dateCreated>Sat, 24 Jan 2026 12:00:00 GMT</dateCreated>
    <ownerEmail>user@gmail.com</ownerEmail>
  </head>
  <body>
    <outline text="Podcast Name" type="rss" xmlUrl="https://feed.url/rss" />
    <outline text="Another Podcast" type="rss" xmlUrl="https://another.feed/rss" />
  </body>
</opml>
```

**Activity Export** (via Takeout):
- Playback history
- Episode progress
- Subscription activity

**Entity Types**: Podcast (show), Episode, Subscription, PlaybackProgress
**Key Relationships**: episode↔podcast, subscription↔podcast, playbackProgress↔episode

---

#### 19. GOOGLE REMINDERS
**Export Formats**: JSON (via Takeout)

**Exported Data**:
- Title
- Created time
- Status (archived, upcoming, active)
- Expiration/due date
- Recurrence information
- Source application (Keep, Calendar, etc.)
- Location (if location-based reminder)

**Entity Types**: Reminder
**Key Relationships**: reminder↔date, reminder↔place, reminder↔person (assignee)

**Note**: Reminders are task-like entities with additional location and time triggers.

---

#### 20. GOOGLE VOICE
**Export Formats**: HTML (Takeout), requires parsing to JSON/CSV

**Takeout Structure**:
- Individual HTML files per call/conversation
- Separate folders for Calls, Greetings
- vCard files for contacts (Phones.vcf)
- Voicemail audio files
- Image files from MMS

**Call Types Exported**:
- Placed calls
- Received calls
- Missed calls
- Voicemails (with audio + transcription)
- Text messages (SMS/MMS)
- Recorded calls

**Parsing Tools**:
- google-voice-takeout-parser (Python)
- voice2json (converts to JSON)
- gvoice-sms-takeout-xml (converts to XML for SMS Backup & Restore)
- googlevoicelog (Bash script → CSV)

**Typical Parsed JSON Structure**:
```json
{
  "type": "voicemail",
  "phoneNumber": "+1234567890",
  "timestamp": "2024-01-15T10:30:00Z",
  "duration": 45,
  "transcription": "Hey, call me back when you get a chance...",
  "audioFile": "voicemail_001.mp3"
}
```

**Entity Types**: PhoneCall, Voicemail, TextMessage (SMS/MMS), PhoneNumber
**Key Relationships**: call↔person, voicemail↔person, message↔person, message↔conversation

---

#### 21. GOOGLE SAVED (Collections)
**Export Formats**: CSV (items), IMAGE (uploaded images)

**CSV Structure**:
| Field | Description | Example |
|-------|-------------|---------|
| collection_description | Collection description | "Trip planning for Antarctica" |
| title | Saved item title | "Wrigley Field" |
| note | User note | "Nice to tour even if no game" |
| item_content_url | URL of saved item | "https://www.google.com/maps/place/..." |
| tags | Semi-colon separated tags | "🌸 Date night;⛷ Ski resorts" |
| comment | Comment on item | "Top rated motherboard" |

**Sources**: Items saved from Google Search, Maps, Shopping, Images

**Entity Types**: SavedItem, Collection
**Key Relationships**: savedItem↔collection, savedItem↔webpage, savedItem↔place

---

#### 22. PURCHASES & RESERVATIONS
**Export Formats**: Extracted from Gmail via schema.org markup (JSON-LD/Microdata)

**Gmail parses emails** containing schema.org markup to extract:
- Flight reservations
- Hotel reservations
- Restaurant reservations
- Event tickets
- Package deliveries
- Orders

**Order Schema** (schema.org/Order):
```json
{
  "@context": "http://schema.org",
  "@type": "Order",
  "merchant": { "@type": "Organization", "name": "Amazon.com" },
  "orderNumber": "123-4567890-1234567",
  "priceCurrency": "USD",
  "price": "29.99",
  "orderStatus": "http://schema.org/OrderProcessing",
  "orderDate": "2024-01-15T10:30:00-08:00",
  "acceptedOffer": {
    "@type": "Offer",
    "itemOffered": {
      "@type": "Product",
      "name": "Google Chromecast",
      "sku": "B00DR0PDNE",
      "image": "https://..."
    },
    "price": "29.99",
    "priceCurrency": "USD",
    "eligibleQuantity": { "@type": "QuantitativeValue", "value": "1" }
  },
  "customer": { "@type": "Person", "name": "John Smith" },
  "billingAddress": { "@type": "PostalAddress", "streetAddress": "..." }
}
```

**FlightReservation Schema**:
```json
{
  "@context": "http://schema.org",
  "@type": "FlightReservation",
  "reservationNumber": "ABC123",
  "reservationStatus": "http://schema.org/ReservationConfirmed",
  "underName": { "@type": "Person", "name": "John Doe" },
  "reservationFor": {
    "@type": "Flight",
    "flightNumber": "UA123",
    "airline": { "@type": "Airline", "name": "United Airlines" },
    "departureAirport": { "@type": "Airport", "iataCode": "SFO" },
    "arrivalAirport": { "@type": "Airport", "iataCode": "LAX" },
    "departureTime": "2024-03-15T08:00:00",
    "arrivalTime": "2024-03-15T09:30:00"
  },
  "airplaneSeat": "12A",
  "airplaneSeatClass": "Economy"
}
```

**ParcelDelivery Schema**:
```json
{
  "@context": "http://schema.org",
  "@type": "ParcelDelivery",
  "carrier": { "@type": "Organization", "name": "FedEx" },
  "trackingNumber": "1234567890",
  "trackingUrl": "https://...",
  "expectedArrivalUntil": "2024-01-20T12:00:00-08:00",
  "deliveryAddress": { "@type": "PostalAddress", "streetAddress": "..." },
  "itemShipped": { "@type": "Product", "name": "Google Chromecast" },
  "partOfOrder": { "@type": "Order", "orderNumber": "123456" }
}
```

**Entity Types**: Order, Reservation (with subtypes: FlightReservation, HotelReservation, RestaurantReservation, EventReservation), Delivery
**Key Relationships**: order↔product, order↔merchant, reservation↔person, reservation↔place, delivery↔order

---

#### 23. GOOGLE MESSAGES
**Export Formats**: Android Backup (encrypted), Third-party XML

**Android Backup**: Messages included in native Android backup system. End-to-end encrypted messages also backed up.

**Third-party Export** (SMS Backup & Restore XML format):
```xml
<sms protocol="0" 
     address="+1234567890" 
     date="1705320600000" 
     type="1" 
     body="Message text here"
     read="1"
     status="-1" />
```

**RCS Messages**: Supported by third-party apps like SMS Backup & Restore.

**No Native Takeout Support**: Google Messages data not directly exportable via Google Takeout.

**Entity Types**: SMS, MMS, RCSMessage, Conversation
**Key Relationships**: message↔conversation, message↔person (sender/recipient), message↔attachment

---

### MY ACTIVITY SCHEMA (Cross-Product)

**Google's Data Portability API** exports activity records across products with this unified schema:

```json
{
  "header": "YouTube|Search|Maps|Google Ads|Google Play",
  "title": "Watched...|Searched for...|Visited...",
  "titleUrl": "https://...",
  "subtitles": [{"name": "...", "url": "..."}],
  "description": "Extra context",
  "time": "2023-08-23T03:49:28.734Z",
  "products": ["YouTube", "Search"],
  "details": "From Google Ads",
  "activityControls": "YouTube watch history|Web & App Activity",
  "locationInfos": "Location data",
  "imageFile": "image.jpg",
  "audioFiles": ["audio.mp3"],
  "attachedFiles": ["file.pdf"]
}
```

**Resource Groups**:
- myactivity.youtube
- myactivity.maps
- myactivity.search
- myactivity.myadcenter
- myactivity.shopping
- myactivity.play

---

### GOOGLE KNOWLEDGE GRAPH

**Architecture**:
- Database of billions of facts about people, places, things
- Extracts structured data from unstructured web content
- Three main processes: Information extraction, Linking, Analysis

**Enterprise Knowledge Graph**:
- Entity Reconciliation API for semantic clustering/deduplication
- Converts relational data to RDF triples
- Supports schema.org types (Person, Organization, LocalBusiness)
- Handles graphs with billions of nodes, trillions of links

**Knowledge Graph Search API**:
- Read-only access
- Uses schema.org types
- JSON-LD compliant

---

### INFRASTRUCTURE NOTES

**Bigtable** (Storage Layer):
- Sparse, distributed, persistent multi-dimensional sorted map
- Indexed by row key, column key, timestamp
- Used by 60+ Google products including Gmail, Analytics, YouTube, Earth
- Published OSDI 2006 (Chang, Dean, Ghemawat et al.)

**Spanner** (Database):
- Distributed relational database with synchronous Paxos replication
- 2B+ requests/second at peak, 6+ exabytes data
- 99.999% availability
- Used by Google Photos for all metadata

**Gmail Storage**:
- Combines Bigtable + Colossus distributed file system
- Handles highly variable workloads (mailboxes vary 4 orders of magnitude)
- Fan-out write on send, write-through cache for metadata

---

## Entity Type Implications

### ENTITY TYPE OBSERVATIONS

Based on research, here are the key entity types discovered across Google products:

#### Core Entity Types (Universal)

| Entity Type | Properties | Found In |
|-------------|------------|----------|
| **Person** | name, email, phone, address, photo, organization, relations, birthdate | Contacts, Gmail, Photos, Calendar, Chat |
| **Message** | content, timestamp, from, to, attachments, thread_id | Gmail, Chat, Hangouts, Voice |
| **Conversation/Thread** | participants, messages[], timestamp | Gmail, Chat, Hangouts |
| **Event** | title, start, end, recurrence, attendees[], location, description | Calendar |
| **File** | name, mimeType, size, owner, created, modified, parent_folder | Drive, Photos |
| **Note** | title, content, color, labels[], collaborators[], created, modified | Keep |
| **Task** | title, notes, due, status, parent, position, links[] | Tasks, Keep |
| **Place** | name, address, placeId, coordinates, semanticType | Maps, Timeline, Photos |

#### Media Entity Types

| Entity Type | Properties | Found In |
|-------------|------------|----------|
| **Photo** | filename, timestamp, geoData, description, faces[], album | Photos |
| **Video** | id, title, duration, channel, category, privacy | YouTube, Photos |
| **Album** | name, photos[], coverPhoto | Photos |
| **Channel** | id, name, url | YouTube |
| **Playlist** | name, videos[], owner | YouTube |

#### Location/Activity Entity Types

| Entity Type | Properties | Found In |
|-------------|------------|----------|
| **Visit** | location, duration, confidence, semanticType | Timeline |
| **ActivitySegment** | startLocation, endLocation, duration, activityType, distance, confidence | Timeline |
| **TransitStop** | placeId, name, address, coordinates | Timeline |

#### Behavioral Entity Types

| Entity Type | Properties | Found In |
|-------------|------------|----------|
| **HistoryEntry** | url, title, timestamp, page_transition | Chrome |
| **Bookmark** | url, title, folder, created | Chrome |
| **Subscription** | channelId, channelTitle | YouTube |
| **ActivityRecord** | header, title, time, products, activityControls | My Activity |

#### Container/Organizational Entity Types

| Entity Type | Properties | Found In |
|-------------|------------|----------|
| **Folder** | name, parent, children[] | Drive, Chrome Bookmarks |
| **Calendar** | name, owner, timezone | Calendar |
| **TaskList** | name, tasks[] | Tasks |
| **Label/Tag** | name, color | Keep, Gmail |
| **ContactGroup** | name, members[] | Contacts |

---

### KEY CROSS-PRODUCT PATTERNS

1. **Unified Identity via People API**: Google merges person data across products using verified email, phone, or profile URLs as linking identifiers

2. **Activity as First-Class Entity**: My Activity schema provides a unified model for user actions across all products (header → title → time → products)

3. **Place as Cross-Product Entity**: Places appear in Maps, Timeline, Photos, Calendar, and Keep with consistent placeId references

4. **Timestamp Standardization**: All products use ISO 8601 timestamps (e.g., "2023-08-23T03:49:28.734Z")

5. **Coordinates**: Stored as E7 format (degrees × 10^7) for precision without floating point issues

6. **Confidence Scores**: Location/activity data includes confidence levels (HIGH/MEDIUM/LOW or 0-100 probability)

---

### PROPOSED NEW ENTITY TYPES FOR OUR SYSTEM

Based on Google's modeling across all Tier 1 and Tier 2 products:

#### Core Entity Types (High Priority)

| Proposed Type | Rationale | Found In |
|---------------|-----------|----------|
| `event` | Calendar events are distinct from tasks (have duration, location, attendees) | Calendar, Wallet |
| `task` | Tasks have status, due dates, subtask hierarchy | Tasks, Keep |
| `reminder` | Task-like but with time/location triggers | Reminders |
| `message` | Messages have sender/recipient, thread relationships | Gmail, Chat, Voice, Messages |
| `conversation` | Thread/container for related messages | Gmail, Chat, Voice, Messages |
| `visit` | Location-based stays at places with duration | Timeline |
| `activity` | User actions with timestamp, product context | My Activity |
| `subscription` | Following/watching relationship to entity | YouTube, Podcasts |

#### Media & Content Entity Types

| Proposed Type | Rationale | Found In |
|---------------|-----------|----------|
| `podcast` | Podcast show (series level) | Podcasts |
| `episode` | Individual podcast episode | Podcasts |
| `movie` | Film work | Play Movies |
| `tvshow` | Television series | Play Movies |
| `book` | E-book or audiobook | Play Books |
| `highlight` | Text selection annotation | Play Books |
| `annotation` | User note on content | Play Books |

#### Commerce & Transaction Entity Types

| Proposed Type | Rationale | Found In |
|---------------|-----------|----------|
| `order` | E-commerce transaction | Purchases & Reservations |
| `reservation` | Booking (flight, hotel, restaurant, event) | Purchases & Reservations |
| `delivery` | Package shipment tracking | Purchases & Reservations |
| `transaction` | Financial transaction | Google Pay |
| `purchase` | App/content purchase | Play Store |
| `app` | Mobile/web application | Play Store |

#### Pass & Credential Entity Types

| Proposed Type | Rationale | Found In |
|---------------|-----------|----------|
| `pass` | Generic digital pass | Google Wallet |
| `boardingPass` | Flight boarding pass | Google Wallet |
| `eventTicket` | Event admission ticket | Google Wallet |
| `loyaltyCard` | Rewards program membership | Google Wallet |
| `transitPass` | Public transit ticket | Google Wallet |

#### Communication Entity Types

| Proposed Type | Rationale | Found In |
|---------------|-----------|----------|
| `phoneCall` | Voice call record | Voice |
| `voicemail` | Voicemail recording with transcription | Voice |
| `sms` | SMS text message | Voice, Messages |

#### Content Organization Entity Types

| Proposed Type | Rationale | Found In |
|---------------|-----------|----------|
| `blog` | Blog container | Blogger |
| `post` | Blog post | Blogger |
| `savedItem` | Bookmarked/saved content | Saved |
| `collection` | User-created grouping | Saved |

---

### RELATIONSHIP TYPES DISCOVERED

#### Person-Centric Relationships

| Relationship | From | To | Example |
|--------------|------|----|---------|
| `attended_by` | event | person | Calendar attendees |
| `organized_by` | event | person | Calendar organizer |
| `from` / `to` | message | person | Email sender/recipients |
| `author_of` | person | post | Blog post author |
| `holder_of` | person | pass | Wallet pass holder |
| `subscribed_to` | person | channel/podcast | YouTube/Podcast subscriptions |
| `visited` | person | place | Timeline visits |
| `member_of` | person | conversation | Chat participants |
| `purchased_by` | order | person | E-commerce customer |
| `reserved_for` | reservation | person | Flight/hotel guest |

#### Content Relationships

| Relationship | From | To | Example |
|--------------|------|----|---------|
| `contains` | folder | file | Drive hierarchy |
| `contains` | blog | post | Blog structure |
| `contains` | tvshow | episode | TV series episodes |
| `contains` | podcast | episode | Podcast episodes |
| `contains` | album | photo | Photo albums |
| `tagged_with` | note/post | label | Keep/Blogger labels |
| `appears_in` | person | photo | Face recognition |
| `taken_at` | photo | place | Geo-tagged photos |
| `parent_of` | task | task | Subtask hierarchy |
| `reply_to` | comment | comment | Nested comments |
| `highlight_of` | highlight | book | Book annotations |

#### Transaction Relationships

| Relationship | From | To | Example |
|--------------|------|----|---------|
| `order_contains` | order | product | Order line items |
| `sold_by` | order | organization | Merchant |
| `delivered_by` | delivery | organization | Carrier |
| `part_of_order` | delivery | order | Shipment tracking |
| `for_event` | eventTicket | event | Concert tickets |
| `issued_by` | pass | organization | Pass issuer |
| `installed_on` | app | device | App installations |

#### Location Relationships

| Relationship | From | To | Example |
|--------------|------|----|---------|
| `located_at` | event | place | Event venue |
| `origin` | activitySegment | place | Travel start |
| `destination` | activitySegment | place | Travel end |
| `saved_place` | savedItem | place | Saved locations |

---

### CROSS-PRODUCT PATTERNS SUMMARY

1. **Class-Object Architecture** (Google Wallet): Separates shared template (Class) from individual instances (Object). Good pattern for passes, tickets, memberships.

2. **Activity as Universal Logging**: My Activity schema provides unified model for user actions across all products. Consider `activity` as a meta-entity type.

3. **Schema.org for Email Parsing**: Gmail uses schema.org markup (JSON-LD/Microdata) to extract structured entities from emails. Our schema should align with schema.org types.

4. **OPML for Subscriptions**: Industry standard for podcast/RSS subscriptions. Consider supporting import/export.

5. **Two-Tier Pass System**: Wallet passes demonstrate how to model entities that have both shared (template) and unique (instance) properties.

---

## Relationship Implications

*(See "RELATIONSHIP TYPES DISCOVERED" section above)*

---

## URLs and Resources

### Official Google Documentation
- https://takeout.google.com/ — Google Takeout main page
- https://developers.google.com/data-portability — Data Portability API documentation
- https://developers.google.com/data-portability/schema-reference — Schema references for all products
- https://developers.google.com/data-portability/schema-reference/my_activity — My Activity schema
- https://developers.google.com/data-portability/schema-reference/youtube — YouTube schema
- https://developers.google.com/people — People API (Contacts)
- https://developers.google.com/people/api/rest/v1/people — Person resource schema
- https://developers.google.com/photos/library/reference/rest/v1/mediaItems — Photos MediaItem schema
- https://developers.google.com/workspace/keep/api/reference/rest/v1/notes — Keep notes schema
- https://developers.google.com/workspace/tasks/reference/rest/v1/tasks — Tasks schema
- https://developers.google.com/workspace/gmail/api/guides/threads — Gmail threading
- https://developers.google.com/maps/documentation/places/web-service/place-id — Place IDs
- https://developers.google.com/maps/documentation/places/web-service/place-types — Place types
- https://developers.google.com/knowledge-graph — Knowledge Graph API
- https://cloud.google.com/enterprise-knowledge-graph/docs/overview — Enterprise Knowledge Graph
- https://support.google.com/accounts/answer/3024190 — How to download your Google data

### Standards and RFCs
- https://www.rfc-editor.org/rfc/rfc6350 — vCard Format Specification
- https://www.rfc-editor.org/rfc/rfc7095 — jCard: JSON Format for vCard
- https://www.rfc-editor.org/rfc/rfc9553 — JSContact: JSON for Contact Data (2024)
- https://www.rfc-editor.org/rfc/rfc7265 — jCal: JSON Format for iCalendar
- https://www.rfc-editor.org/rfc/rfc4155 — MBOX Media Type

### Location History Format (Community Documentation)
- https://locationhistoryformat.com/ — Comprehensive Google location history format guide
- https://locationhistoryformat.com/reference/semantic/ — Semantic Location History JSON schema
- https://locationhistoryformat.com/guides/general-structure/ — General structure guide
- https://locationhistoryformat.com/reference/records/ — Records.json format

### Google Engineering Resources
- https://research.google.com/archive/bigtable-osdi06.pdf — Bigtable paper (Dean, Ghemawat et al.)
- https://research.google.com/teams/perception — Google Perception team (Photos ML)
- https://cloud.google.com/blog/products/databases/google-photos-builds-user-experience-on-spanner — Photos on Spanner
- https://cloud.google.com/spanner — Spanner database documentation
- https://ai.google/facial-recognition/ — Google's approach to facial recognition
- https://blog.google/products/photos/how-google-photos-best-take-works — Best Take ML feature

### Historical Articles
- https://time.com/43263/gmail-10th-anniversary/ — Gmail launch story (Paul Buchheit)
- https://www.wired.com/2008/09/mf-chrome/ — Chrome development story (Brian Rakowski)
- https://www.fastcompany.com/90380618/how-google-photos-joined-the-billion-user-club — Photos growth story
- https://dataliberation.blogspot.com/2011/06/data-liberation-front-delivers-google.html — Takeout launch
- https://arstechnica.com/tech-policy/2010/03/why-google-makes-it-easy-to-leave-google/ — Data Liberation philosophy
- https://www.theverge.com/a/sundars-google/google-photos-google-io-2015 — Google Photos origin story

### Wikipedia References
- https://en.wikipedia.org/wiki/Paul_Buchheit — Gmail creator
- https://en.wikipedia.org/wiki/Bret_Taylor — Google Maps co-creator
- https://en.wikipedia.org/wiki/Lars_Rasmussen_(software_developer) — Google Maps co-creator
- https://en.wikipedia.org/wiki/Bradley_Horowitz — Google Photos VP
- https://en.wikipedia.org/wiki/Jeff_Dean — Google Senior Fellow
- https://en.wikipedia.org/wiki/Sanjay_Ghemawat — Google Senior Fellow
- https://en.wikipedia.org/wiki/History_of_YouTube — YouTube founding story
- https://en.wikipedia.org/wiki/Google_Data_Liberation_Front — Data Liberation Front

### Tools and Parsers
- https://github.com/seanbreckenridge/google_takeout_parser — Python Takeout parser
- https://github.com/srahimeen/google-takeout-metadata-fix-go — Fix Photos metadata
- https://hangoutparser.jay2k1.com/ — Hangouts JSON decoder (web)
- https://github.com/StarGeekSpaceNerd/Metadata_Reference/blob/master/Photos.google.com.md — Photos metadata reference
- https://pypi.org/project/google-takeout-parser/ — google-takeout-parser PyPI package
- https://github.com/purarue/google_takeout_parser — Google Takeout parser (purarue fork)

### Blogger API
- https://developers.google.com/blogger/docs/2.0/json/getting_started — Blogger JSON API Getting Started
- https://developers.google.com/blogger/docs/2.0/json/reference — Blogger API Reference
- https://developers.google.com/blogger/docs/3.0/reference/posts — Blogger Posts Resource (v3)
- https://github.com/cheshrkat/blogger-archive-converter — Blogger XML converter

### Google Wallet API
- https://developers.google.com/wallet — Google Wallet API documentation
- https://developers.google.com/wallet/reference/rest — Wallet REST API Reference
- https://developers.google.com/wallet/reference/rest/v1/eventticketobject — EventTicketObject
- https://developers.google.com/wallet/reference/rest/v1/loyaltyobject — LoyaltyObject
- https://developers.google.com/wallet/reference/rest/v1/transitobject — TransitObject
- https://developers.google.com/wallet/tickets/boarding-passes/overview/how-classes-objects-work — Passes architecture

### Google Voice Parsing
- https://github.com/moshekaplan/google-voice-takeout-parser — Voice Takeout parser
- https://github.com/davidgilson/googlevoicelog — Voice to CSV script
- https://github.com/SLAB-8002/gvoice-sms-takeout-xml — Voice to XML converter

### Gmail Markup (schema.org)
- https://developers.google.com/gmail/markup/overview — Gmail markup overview
- https://developers.google.com/gmail/markup/reference/order — Order schema
- https://developers.google.com/workspace/gmail/markup/reference/parcel-delivery — ParcelDelivery schema
- https://developers.google.com/gmail/markup/reference/flight-reservation — FlightReservation schema
- https://schema.org/Order — Schema.org Order type
- https://schema.org/FlightReservation — Schema.org FlightReservation type

### OPML Specification
- https://opml.org/spec2.opml — OPML 2.0 specification
- https://microformats.org/wiki/OPML — OPML wiki

### Play Books Tools
- https://github.com/amagee/google-books-highlights-export — Highlights export
- https://github.com/mammuth/play-books-notes — Play Books notes API

### Data Portability API Schemas
- https://developers.google.com/data-portability/schema-reference/play — Play Store schema
- https://developers.google.com/data-portability/schema-reference/save — Saved collections schema

---

## Session Log

### 2025-01-24: Initial triage
- Created research doc
- Sorted 72 products into 3 tiers
- Identified candidate new entity types
- Added key people section
- Next: Subagent deep-dives on Tier 1 products

### 2025-01-24: Phase 1 Web Research Complete
**Extensive web research completed on:**
- Google Takeout export formats (JSON, MBOX, iCal, CSV, vCard)
- Data Portability API schemas
- All Tier 1 products: Contacts, Calendar, Drive, Gmail, Photos, Keep, Tasks, YouTube, Maps
- Selected Tier 2 products: Chrome, Chat/Hangouts, Fit
- Google infrastructure: Bigtable, Spanner, Knowledge Graph

**Key findings:**
1. **Unified Activity Schema**: Google has a cross-product activity record format (My Activity) that could inform our entity design
2. **People API as Entity Hub**: Google uses People API to unify person entities across products via verified identifiers
3. **Semantic Location History**: Rich entity model with Place Visits, Activity Segments, Transit Paths
4. **E7 Coordinate Format**: Coordinates stored as integers (degrees × 10^7) across products
5. **JSON Sidecar Pattern**: Photos metadata stored separately from files, must be recombined

**Key people researched:** 15+ engineers and product leads documented with roles and contributions

---

### 2026-01-24: Phase 2 — Tier 2 Products Complete ✅

**Extensive web research completed on all remaining Tier 2 products:**

1. **Blogger** — Atom XML export (Takeout), JSON API schema for Posts/Comments documented. Five resource types: Blogs, Posts, Comments, Pages, Users.

2. **Google Pay/Wallet** — Full pass type architecture documented:
   - EventTicketClass/EventTicketObject (concerts, sports, etc.)
   - LoyaltyClass/LoyaltyObject (rewards cards with points/balance)
   - TransitClass/TransitObject (train/bus passes)
   - FlightClass/FlightObject (boarding passes)
   - Class-Object two-tier architecture: templates + instances

3. **Play Books** — No native JSON export. Syncs to Google Drive in proprietary format. Third-party tools required for conversion. Entities: Book, Highlight, Note, Bookmark.

4. **Play Store** — Data Portability API schema fully documented:
   - Installs (app, device, timestamps)
   - Purchases (item, price, state, payment method)
   - Subscriptions (expiration, renewal, pricing)
   - Library, Devices, Redemptions, Play Points, Promotions

5. **Play Movies & TV** — Exported via My Activity schema. Watch history, purchases, watchlist all use unified activity record format.

6. **Google Podcasts** — OPML export for subscriptions (industry standard). Service shut down; migration to YouTube Music available.

7. **Google Reminders** — JSON export including title, status, recurrence, location-based triggers.

8. **Google Voice** — HTML export (thousands of individual files). Parsing tools convert to JSON/CSV. Entities: PhoneCall, Voicemail, TextMessage.

9. **Google Saved** — CSV export with collections structure. Fields: collection_description, title, note, item_content_url, tags, comment.

10. **Purchases & Reservations** — Gmail schema.org markup parsing documented:
    - Order schema (merchant, items, price, status)
    - FlightReservation schema (passenger, flight, seat)
    - ParcelDelivery schema (carrier, tracking, delivery address)

11. **Google Messages** — Android Backup system. No native Takeout export. Third-party apps export to XML format.

**Key Architecture Discoveries:**

1. **Class-Object Pattern** (Wallet): Separates shared template from individual instances. Powerful for passes, tickets, memberships.

2. **Schema.org Integration**: Gmail parses emails using schema.org types (Order, FlightReservation, ParcelDelivery). Our schema should align.

3. **OPML as Standard**: Industry standard for subscription lists. Worth supporting for import/export.

4. **Activity Unification**: My Activity provides cross-product activity logging. Consider `activity` as meta-entity.

**Entity Types Added:**
- Media: podcast, episode, movie, tvshow, book, highlight, annotation
- Commerce: order, reservation, delivery, transaction, purchase, app
- Passes: pass, boardingPass, eventTicket, loyaltyCard, transitPass
- Communication: phoneCall, voicemail, sms
- Content: blog, post, savedItem, collection

**Relationship Types Added:**
- holder_of (person↔pass)
- for_event (eventTicket↔event)
- issued_by (pass↔organization)
- order_contains (order↔product)
- delivered_by (delivery↔organization)
- highlight_of (highlight↔book)
- installed_on (app↔device)

**URLs Added to SEED_DATA.md:** 30+ new research URLs

**Research Status:**
- ✅ Tier 1: Complete (9/9 products)
- ✅ Tier 2: Complete (15/16 products, Profile skipped as minimal entity value)
- ⬜ Tier 3: Low priority, settings-heavy products
