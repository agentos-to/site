---
title: Digital Spaces in Ontology Standards
description: A comprehensive structured summary of how existing ontologies model digital/virtual spaces.
---

Here's a comprehensive structured summary of how existing ontologies model digital/virtual spaces:

---

## 1. Schema.org — VirtualLocation and Place

**URL:** https://schema.org/VirtualLocation | https://schema.org/Place

### The Key Design Decision: Separate Branches

Schema.org made a deliberate architectural choice: **physical and virtual locations are NOT unified.** They live in completely separate branches of the type hierarchy:

```
Thing
├── Place                    (physical — "entities with fixed, physical extension")
│   ├── Accommodation
│   ├── CivicStructure       (Airport, Museum, Park, Library...)
│   ├── LandmarksOrHistoricalBuildings
│   ├── LocalBusiness         (Restaurant, Store, etc.)
│   ├── Residence
│   └── TouristAttraction
│
└── Intangible
    └── VirtualLocation      (digital — "an online or virtual location")
```

### VirtualLocation

- **Type:** `schema:VirtualLocation`
- **Parent:** `Thing > Intangible` (NOT Place)
- **Status:** "new" area, still seeking implementation feedback
- **Definition:** "An online or virtual location for attending events"
- **Properties:** Inherits only from `Thing` — `name`, `url`, `description`, `identifier`, `image`. No geo properties, no containment relationships, no address.
- **Source issue:** https://github.com/schemaorg/schemaorg/issues/1842

### Place

- **Type:** `schema:Place`
- **Definition:** "Entities that have a somewhat fixed, physical extension"
- **Rich properties:** `geo`, `latitude`, `longitude`, `address`, `containedInPlace` / `containsPlace` (nested containment), `maximumAttendeeCapacity`, `openingHoursSpecification`, `publicAccess`
- **Equivalent to:** `cmns-loc:Location`

### Hybrid Events

Schema.org bridges the physical/virtual gap only through **Events**, not through a unified location model:

- `Event.location` accepts **both** `Place` AND `VirtualLocation` (as an array for hybrid events)
- `Event.eventAttendanceMode` has three values:
  - `OnlineEventAttendanceMode`
  - `OfflineEventAttendanceMode`
  - `MixedEventAttendanceMode`

### Assessment

VirtualLocation is **extremely thin** — basically a URL with a name. It has no containment model, no notion of "spaces within spaces," no capacity, no access control. It was designed for "where do I tune in to this webinar?" not for modeling digital community spaces. The asymmetry is stark: Place has ~30 dedicated properties; VirtualLocation has zero dedicated properties beyond what Thing provides.

---

## 2. ActivityPub / ActivityStreams 2.0

**URL:** https://www.w3.org/TR/activitystreams-vocabulary/#dfn-place

### Place Object Type (Physical Only)

ActivityStreams defines a `Place` object type with geographic properties:

- **Type:** `as:Place`
- **Extends:** `Object`
- **Properties:** `accuracy`, `altitude`, `latitude`, `longitude`, `radius`, `units`
- **Used in activities:** `Arrive`, `Leave`, `Travel` (geo-social activities)

This is **purely physical**. There is no `VirtualPlace` or `DigitalSpace` equivalent in the core spec.

### How Digital Spaces Are Actually Modeled

The fediverse models digital spaces not as "places" but as **Actors** and **Collections**:

| Concept | AS2 Type | How It Works |
|---------|----------|-------------|
| Instance/Server | Not typed — implied by domain | The server itself is the "space" |
| User | `Person` actor | Has `inbox`, `outbox`, `followers`, `following` |
| Group/Community | `Group` actor | Receives posts, re-announces to followers |
| Channel/Feed | `Collection` / `OrderedCollection` | Ordered sets of objects |

### Fediverse Enhancement Proposals (FEPs)

The community is actively extending the vocabulary for community spaces:

- **FEP-1b12: Group Federation** — Formalizes `Group` actor type for forum categories. Groups maintain follow relationships and `Announce` content to followers. (https://docs.nodebb.org/activitypub/fep/1b12/)
- **FEP-1d80: Feed Actor** — New actor type for *collections of Groups* (developed by PieFed, Lemmy, Mbin). Needed because `Group` wasn't sufficient for hierarchical community organization.
- **FEP-400e** — Publicly-appended content (how posts get added to Group collections)

### places.pub (Social Web Foundation)

**URL:** https://places.pub/

A project that **bridges physical places into ActivityPub** by exposing OpenStreetMap data as AP objects. Each OSM location gets an HTTPS URL (`https://places.pub/{node|way|relation}/{id}`) and becomes a followable ActivityPub Place object. Uses a mix of vocabularies: ActivityStreams, GeoJSON, Dublin Core Terms, vCard.

### Assessment

ActivityPub has **no concept of digital space as a place.** Digital spaces are modeled as *actors* (entities that can send/receive) or *collections* (bags of objects). The "where content lives" question is answered by "which actor's outbox contains it" rather than "which place is it located in." This is a fundamentally different metaphor — the space IS the actor.

---

## 3. SIOC (Semantically-Interlinked Online Communities)

**URL:** http://rdfs.org/sioc/spec/ | http://rdfs.org/sioc/ns#

### The Most Relevant Ontology for Your Question

SIOC is the **only major ontology specifically designed to model online community spaces.** It has no physical location concept at all — it's digital-only.

### Core Class Hierarchy

```
Space           — "A data Space which is the location of a set of Container data"
├── Site        — "A Site can be the location of an online community or set of communities"
│
Container       — "An area in which content Items are contained"
├── Forum       — "A discussion area on which Posts or entries are made"
│   └── Thread  — "A container for a series of threaded discussion Posts or Items"
│
Item            — "Something which can be in a Container"
├── Post        — "An article or message that can be posted to a Forum"
│
Community       — "A high-level concept that defines an online community"
UserAccount     — "A user account in an online community site"
Usergroup       — "A set of UserAccounts whose members have a common purpose"
Role            — "A function of a UserAccount within a scope"
```

### Key Properties (Space/Container Model)

| Property | Domain | Range | Description |
|----------|--------|-------|-------------|
| `has_space` | Site | Space | Links a site to its data space |
| `space_of` | Space | Site | Inverse |
| `has_host` | Container | Site | The Site that hosts this Container |
| `host_of` | Site | Container | Inverse |
| `has_container` | Item | Container | The Container an Item belongs to |
| `container_of` | Container | Item | Inverse |
| `has_parent` | Container | Container | Parent Container (nesting!) |
| `parent_of` | Container | Container | Inverse |
| `has_member` | Community | UserAccount | |
| `has_moderator` | Forum | UserAccount | |
| `has_creator` | Item | UserAccount | |
| `has_reply` | Item | Item | Threading |
| `reply_of` | Item | Item | Inverse |

### SIOC Types Module (Subclasses)

**Forum subtypes:** `ArgumentativeDiscussion`, `ChatChannel`, `MailingList`, `MessageBoard`, `Weblog`

**Container subtypes:** `AddressBook`, `AnnotationSet`, `AudioChannel`, `BookmarkFolder`, `Briefcase`, `EventCalendar`, `ImageGallery`, `ProjectDirectory`, `ResumeBank`, `ReviewArea`, `SubscriptionList`, `SurveyCollection`, `VideoChannel`, `Wiki`

**Post subtypes:** `BlogPost`, `BoardPost`, `Comment`, `InstantMessage`, `MailMessage`, `WikiArticle`

### Relationship to Physical Places

**None.** SIOC is purely digital. It does not model physical locations at all, nor does it attempt to bridge to them. The `Space` class in SIOC means "data space" (a namespace/scope for content), not a physical or even metaphorically spatial concept.

### Assessment

SIOC is the richest existing model for "digital spaces as containers for community interaction." Its **Container hierarchy with nesting** (`has_parent`/`parent_of`) is exactly the kind of structure needed for modeling spaces-within-spaces. However, it's from the Semantic Web era (~2007-2018) and sees limited adoption today. It was designed for interoperability between forums, blogs, and mailing lists — not for modern platforms like Discord, Slack, or Reddit.

---

## 4. FOAF (Friend of a Friend)

**URL:** https://xmlns.com/foaf/spec/

### Relevant Concepts

FOAF focuses on **people and their relationships**, not spaces. But it has a few relevant concepts:

| Concept | Type | Purpose |
|---------|------|---------|
| `foaf:OnlineAccount` | Class | An account in an online service |
| `foaf:Document` | Class | Any document (web page, etc.) |
| `foaf:Group` | Class | A collection of agents |
| `foaf:based_near` | Property | "A location that something is based near" (geo, not digital) |
| `foaf:account` | Property | Links Agent to OnlineAccount |
| `foaf:accountServiceHomepage` | Property | The service where the account exists |
| `foaf:homepage` | Property | Links Agent to their web page |
| `foaf:weblog` | Property | Links Person to their blog |

### Relationship to Digital/Physical

`foaf:based_near` is geographic (uses `geo:SpatialThing`). There's no `foaf:based_in_digital_space` equivalent. FOAF models *people who exist in digital spaces* but not the spaces themselves. The closest it gets is `OnlineAccount` + `accountServiceHomepage`, which says "this person has an account on this service" — the service homepage is the weakest possible proxy for "digital space."

### Assessment

FOAF is complementary to SIOC (they were designed to work together). FOAF describes who; SIOC describes where. Neither models physical location in a way that bridges to digital.

---

## 5. Dublin Core

**URL:** https://dublincore.org/specifications/dublin-core/dcmi-terms/

### Spatial Concepts

| Concept | URI | Purpose |
|---------|-----|---------|
| `dcterms:spatial` | `http://purl.org/dc/terms/spatial` | Spatial characteristics of a resource |
| `dcterms:coverage` | `http://purl.org/dc/terms/coverage` | Spatial or temporal topic of a resource |
| `dcterms:Location` | `http://purl.org/dc/terms/Location` | "A spatial region or named place" |
| DCMI Point | Encoding scheme | Lat/long point |
| DCMI Box | Encoding scheme | Bounding box |

### Digital Location?

**No.** Dublin Core's spatial concepts are explicitly geographic — named places from gazetteers, geographic coordinates, bounding boxes. The `dcterms:Location` class is defined as "a spatial region or named place" and all encoding schemes (Point, Box) are geographic coordinate systems.

Dublin Core **does not** model URLs, URIs, or digital addresses as "locations." A resource can have a `dcterms:spatial` of "Boston, MA" but there's no standard pattern for `dcterms:spatial` of "the #general channel in the Cursor Discord."

### Assessment

Dublin Core treats location as metadata *about* resources, not as a first-class entity. It answers "where is this resource relevant?" not "what is this digital space?" No bridge to digital.

---

## 6. W3C / Spatial Data on the Web

**URL:** https://www.w3.org/2021/sdw/

### Working Group Status

The **Spatio-temporal Data on the Web Working Group** (joint W3C/OGC) produces:

- **Semantic Sensor Network Ontology** (W3C Recommendation)
- **Time Ontology in OWL** (W3C Recommendation)
- **Spatial Data on the Web Best Practices**
- **GeoSPARQL** (from OGC)

### Digital Location Work

**Essentially none.** The entire working group is focused on physical geography — sensors, earth observation, geospatial data. The **Locations and Addresses Community Group** reviews location vocabularies (GeoSPARQL, NeoGeo, schema.org) but is focused on physical addresses and geocoding.

There is **no W3C working group or specification** for modeling virtual/digital locations as spatial entities.

### Assessment

The W3C spatial work is entirely about physical space. Digital location is simply not in scope.

---

## 7. Academic/Applied Research — Digital Public Spaces

### New Public's Digital Spaces Directory

**URL:** https://newpublic.substack.com/p/introducing-our-digital-spaces-directory

A catalog of 200+ digital social products, classified by:

| Dimension | Values |
|-----------|--------|
| **Entity Type** | Digital Space, Infrastructure for Spaces, Federated Infrastructure |
| **Interaction Format** | (not enumerated in public docs) |
| **Business Model** | (various) |
| **Stage** | Maturity level |
| **Open Source** | Yes/No |
| **Civic Signals** | Which of the 14 apply |

The three-way **Entity Type** split is interesting: it distinguishes the *space itself* from *infrastructure that hosts spaces* from *federated infrastructure*. This is a meta-taxonomy — it classifies the platform architecture, not the space within it.

### Civic Signals Framework (New\_Public + Center for Media Engagement, UT Austin)

**URL:** https://mediaengagement.org/research/civic-signals-the-qualities-of-flourishing-digital-spaces/

14 signals in 4 building blocks — these describe **qualities** of spaces, not spatial structure:

| Building Block | Signals |
|----------------|---------|
| **Welcome** | 1. Invite everyone to participate, 2. Ensure safety, 3. Humanize others, 4. Secure information |
| **Connect** | 5. Cultivate belonging, 6. Bridge groups, 7. Strengthen local ties, 8. Make power accessible |
| **Understand** | 9. Elevate shared concerns, 10. Show reliable information, 11. Build civic competence, 12. Promote thoughtful conversation |
| **Act** | 13. Boost community resilience, 14. Support civic action |

### All Tech Is Human — "Healthy Digital Public Spaces"

**URL:** https://alltechishuman.org/healthyspaces

Collaborated with New Public on the Digital Spaces Directory. Uses the same taxonomy. Their contribution is more on the policy/practice side than on formal ontology.

### Assessment

The academic/applied work treats digital spaces as **sociological phenomena to be evaluated**, not as **entities to be modeled in a graph.** The taxonomies are about *qualities* (Civic Signals) and *platform categories* (Directory), not about spatial structure or containment. There's no ontology here — it's a classification framework.

---

## Summary Table

| Standard | Digital Space Concept | Relation to Physical | Containment Model | Status |
|----------|----------------------|---------------------|-------------------|--------|
| **Schema.org** | `VirtualLocation` (under Intangible) | **Separate branch** from Place. Bridged only via Event.location | None | Thin; URL + name only |
| **ActivityStreams** | None (spaces = Actors) | `Place` is physical only; digital = `Group`/`Collection` actors | Actor has inbox/outbox/collections | Active; FEPs extending |
| **SIOC** | `Space` > `Site`; `Container` > `Forum` > `Thread` | **No physical model at all** | Yes! `has_parent`/`parent_of` nesting | Rich but dated (2007-2018) |
| **FOAF** | `OnlineAccount` (person-centric) | `based_near` is geographic only | None | Complementary to SIOC |
| **Dublin Core** | None | `dcterms:spatial` = geographic only | None | Metadata about resources |
| **W3C SDW** | None | Physical geography only | GeoSPARQL spatial relations | No digital scope |
| **Civic Signals** | "Digital Space" (entity type in directory) | Separate concept; Signal 7 bridges to "local ties" | None (quality framework) | Applied research |

---

## Key Insight for AgentOS

**No existing standard unifies physical and digital spaces under a common model.** Everyone who has tried has either:

1. **Kept them separate** (Schema.org: Place vs VirtualLocation in different branches)
2. **Modeled only digital** (SIOC: rich digital-only model)
3. **Modeled only physical** (Dublin Core, W3C SDW, GeoSPARQL)
4. **Used a completely different metaphor** (ActivityPub: spaces are actors, not locations)

The closest to a unified model is SIOC's `Container` concept — an abstract "area in which content Items are contained" — which could theoretically apply to a physical room or a digital channel. But SIOC never actually models physical containers; it just uses spatial metaphors for digital ones.

If you're thinking about a unified `Place` entity that can represent both a coffee shop AND a Discord channel, that would be genuinely novel in the ontology space.
