---
title: Ontology overview
description: Shapes are agentOS's ontology. A shape declares what a record looks like — field names, types, relations to other records, display rules.
---

Shapes are agentOS's ontology. A shape declares what a record looks like — field names, types, relations to other records, display rules. Think of shapes as **ISO standards**: skills that *write* to the graph and apps that *read* from it agree on the shape of a `message`, a `product`, a `person`. The engine itself is shape-agnostic — it's a generic entity store.

Shapes live in `shapes/*.yaml`. They exist to:

1. **Document the ontology** — so skill authors and app authors agree on field names, types, and relations.
2. **Drive codegen** — `generate.py` turns YAML into typed classes in `skills-sdk/agentos/_generated.py` (Python `TypedDict`) and `apps-sdk/src/shapes.ts` (TypeScript interfaces).
3. **Stay human-reviewable** — PR review catches bad field design before it ships.

The engine doesn't load shape YAML. Skills return conformant dicts; apps read whatever is in the graph. If no skill has ever returned a `post`, there is no `post` anywhere — the YAML is the standard, the graph is the data.

## Authoring a shape

1. **Write the YAML** in [`shapes/<name>.yaml`](https://github.com/agentos-to/site/tree/main/docs/shapes) — the source of truth for the ontology.
2. **Run codegen** so SDK consumers get updated types:
   ```bash
   python generate.py             # Python + TypeScript
   ```
3. **Use it in a skill** — `@returns("your_shape")` + return a conformant dict.
4. **That's it.** No engine restart, no graph seeding, no "push shape to graph" step. The YAML is the standard; skills comply; the engine moves data through.

To update a shape, edit the YAML and re-run codegen. Renaming or removing fields is a breaking change — update consumers at the same time.

## Format

```yaml
# A purchasable item. Base type for book and aircraft.
#
# Example sources: Amazon, Uber Eats (grocery), Open Food Facts
product:
  plural: products                    # UI plural form
  subtitle: brand                     # field used as row subtitle in list views
  also: [other_shape]                 # "a product is also a ..." (optional, transitive)
  identity: [platform, id]            # dedupe keys for upsert (optional)
  fields:
    price:           string           # formatted price
    priceAmount:    number           # numeric price for math
    currency:        string
    categories:      string[]
    available:       boolean
  relations:
    brand:           brand             # single relation → brand
    manufacturer:    organization      # single relation → organization
    tagged:          tag[]             # array relation → tag nodes
```

Shape YAML is a single top-level key (the shape name) containing metadata + `fields` + `relations`. Top-level metadata keys: `plural`, `subtitle`, `icon`, `also`, `identity`, `identity_any`.

### `also` (tag implication)

Declares that this shape is also another shape. An email is also a message. A book is also a product. When the engine tags a record with `email`, it transitively applies `message` too. Both shapes' fields contribute to the record's type context.

`also` is transitive: if A is also B and B is also C, then A is also B and C.

### Field types

| Type | Stored as | Notes |
|------|-----------|-------|
| `string` | text | Short text |
| `text` | text | Long text, FTS eligible |
| `integer` | digits | Parsed from strings, floats truncated |
| `number` | decimal | Parsed from strings |
| `boolean` | true/false | Coerced from 1/0, "yes"/"no", "true"/"false" |
| `datetime` | ISO 8601 | Unix timestamps auto-converted, human dates parsed |
| `url` | text | Stored as-is, rendered as clickable link |
| `string[]` | JSON array | Each element coerced to string |
| `integer[]` | JSON array | Each element coerced to integer |
| `json` | JSON string | Opaque blob, no coercion |

### Standard fields

These are available on every record without declaring them in a shape:

| Field | Type | Purpose |
|-------|------|---------|
| `id` | string | Record identifier |
| `name` | string | Primary label |
| `text` | text | Short summary |
| `url` | url | Canonical link |
| `image` | url | Thumbnail |
| `author` | string | Creator |
| `published` | datetime | Temporal anchor |
| `content` | text | Long body text (FTS, stored separately) |

### Relations

Relations declare connections to other records. Keys are edge labels, values are target shapes (`shape` or `shape[]` for arrays).

When a skill returns a nested dict under a relation key, the engine extracts it as a child node and creates an edge from parent to child. See [Typed references](#typed-references-entity-relationships) below.

### Identity

`identity` declares the keys used to dedupe records. When two different skill calls return the same `[platform, id]`, the engine upserts instead of creating duplicates.

```yaml
message:
  identity: [platform, id]   # all keys must match to count as the same record
  identity_any: [email]       # OR: any single key in this list is sufficient
```

Use `identity` for compound keys (must all match) and `identity_any` for alternative keys (any one matches). Most shapes use `identity: [platform, id]` — the external service's native identifier scoped by the platform it came from.

### Subtitle, plural, icon

- `subtitle` — the field name to display as a secondary label in list views (e.g. `subtitle: brand` on product shows the brand under the name).
- `plural` — the plural form of the shape name (e.g. `products` for `product`). Used by UI and by `agent-sdk shapes` listings.
- `icon` — optional icon name for UI rendering.

---

## Design Principles

Tactical principles — concrete patterns for field types, relations, and display. Use the [review checklist](#review-checklist) below after writing or editing a shape. For the higher-order framing ("a shape describes what something IS, not where it came from"), see [Shape design principles](/docs/ontology/shape-design-principles/).

### 1. Entities over fields

If a field value is itself a thing with identity, it should be a **relation to another shape**, not a string field.

**Bad:** `shipping_address: string` (an address is a thing)
**Good:** `shipping_address: place` (a relation to a place record)

**Bad:** `email: string` on a person (an email is an account)
**Good:** `accounts: account[]` relation on person

Ask: *"Could this field value have its own page?"* If yes, it's a relation.

### 2. Separate identity from role

A person doesn't *have* a job title. A person *holds a role* at an organization for a period of time. The role is the relationship, not a field on the person.

**Bad:** `job_title: string` on person
**Good:** `role: role[]` relation where the role record carries title, organization, start_date, end_date

Same pattern applies to education, membership, authorship. If it has a time dimension or involves another entity, it's a role/relationship, not a field.

### 3. Currency always accompanies price

Any field representing a monetary amount needs a companion currency field. Never assume USD.

**Bad:** `price_amount: number` alone
**Good:** `price_amount: number` + `currency: string`

### 4. URLs that reference other things are relations

The standard `url` field is the record's own canonical link. But URLs that point to *other things* should be relations to the appropriate shape.

**Bad:** `website: url` on an organization (a website is its own entity)
**Good:** `website: website` relation

**Bad:** `external_url: url` on a post (the linked page is a thing)
**Good:** `links_to: webpage` relation

Ask: *"Is this URL the record itself, or does it point to something else?"*
- Record's own link: keep as `url` (standard field)
- Points to another thing: make it a relation

### 5. Keep shapes domain-agnostic

A shape should describe the *kind of thing*, not the *source it came from*. Flight details don't belong on an offer shape. Browser-specific fields don't belong on a webpage shape.

**Bad:** `total_duration: integer`, `flights: json`, `layovers: json` on offer (that's a flight, not an offer)
**Good:** offer has price + currency + offer_type. Flight is its own shape. Offer relates to flight.

### 6. Use `also` for genuine "is-a" relationships

`also` means tag implication: tagging a record with shape A also tags it with shape B. Use it when querying by B should include A.

**Good uses:**
- `email` also `message` (querying messages should include emails)
- `video` also `post` (querying posts should include videos)
- `book` also `product` (querying products should include books)
- `review` also `post` (querying posts should include reviews)

**Bad uses:**
- Don't use `also` just because shapes share some fields
- Don't create deep chains (A also B also C also D) — keep it shallow

### 7. Author is a shape, not just a string

The standard `author` field is a string for convenience. But when the author is a real entity with their own identity (a book author, a blog writer, a video creator), use a relation to the `author` or `account` shape.

**Quick attribution:** `author: "Paul Graham"` (standard string field)
**Rich attribution:** `written_by: author` or `posted_by: account` (relation)

Both can coexist — the string is for display, the relation is for traversal.

### 8. Address/Place is structured, not a string

Physical locations should be a `place` shape with structured fields (name, street, city, region, postal_code, country, coordinates). Inspired by Mapbox's geocoding model.

### 9. Playlists, shelves, and lists belong to accounts

Any collection (playlist, shelf, list, board) should have a `belongs_to: account` relation. Collections are owned.

### 10. Use ISO standards for standardized values

When a field represents something with an international standard, use the standard code:

- **Human languages** — ISO 639-1 codes (`en`, `es`, `ja`, `pt-BR`). Applies to transcript.language, webpage.language, content language fields. NOT programming languages (those use conventional names like `Python`, `Rust`).
- **Countries** — ISO 3166-1 alpha-2 codes (`US`, `GB`, `JP`). Use `country_code` field.
- **Currencies** — ISO 4217 codes (`USD`, `EUR`, `JPY`). Use `currency` field.
- **Timezones** — IANA timezone names (`America/New_York`, `Europe/London`).

Don't enforce via enum (too many values). Document the convention and let `agentos test` flag non-compliant values. Run `agent-sdk validate` to check skill return dicts against their declared shape.

### 11. Separate content from context (NEPOMUK principle)

A video is a file. The social engagement around it is a post. A transcript is text. The meeting it came from is the context. Don't mix artifact properties with social properties on the same shape.

**Bad:** `video` has view_count, like_count, comment_count, posted_by (those are social context)
**Good:** `video` is a file with duration + resolution. A `post` contains the video and carries the engagement.

Ask: *"If I downloaded this to my hard drive, which fields would still make sense?"* Those are the artifact fields. Everything else is context that belongs on a wrapper entity.

### 12. Comments are nested posts, not a separate shape

A comment is a post that `replies_to` another post. A reply to a message is still a message. Don't create separate shapes for nested versions of the same thing — use the `replies_to` relation to express the hierarchy.

### 13. Booleans describe state, relations describe lineage

`is_fork: boolean` tells you nothing. `forked_from: repository` tells you the lineage. If a boolean implies a relationship to another entity, model the relationship instead.

**Bad:** `is_fork: boolean` (from what?)
**Good:** `forked_from: repository` (the source is traversable)

### 14. Booleans that encode direction are really relationships

`is_outgoing: boolean` on a message means "I sent this." But that information already lives in the `from: account` relation — if the `from` account is the user, it's outgoing. Don't duplicate relationship semantics as boolean flags.

**Bad:** `is_outgoing: boolean` on message
**Good:** `from: account` relation — direction is derived by comparing `from` to the current user

Same pattern: `is_sent`, `is_received`, `is_mine` — all derivable from a directional relation.

### 15. Booleans that encode cardinality are derivable

`is_group: boolean` on a conversation means "has more than two participants." That's not state — it's a count. Don't store what you can derive from the structure.

**Bad:** `is_group: boolean` on conversation
**Good:** `participant: account[]` relation — `is_group` is `len(participants) > 2`

Same pattern: `has_attachments` (derive from `attachment: file[]`), `has_unread` (derive from messages), `is_empty` (derive from children).

### 16. Source data doesn't dictate shape

A skill's source (API, database, scrape) returns whatever it returns. That doesn't constrain the shape. The Python function is the transformation boundary — it takes raw source data and returns shape-native dicts.

Apple Contacts gives flat strings: `Organization: Anthropic`, `Title: Engineer`. That doesn't mean person gets `organization: string`. It means the skill transforms those strings into a `roles: role[]` typed ref.

**Bad:** "The API returns `platform: string`, so the shape needs a `platform` field"
**Good:** "What kind of thing is this? Model it correctly. The skill transforms source data to fit."

Design shapes for the domain, not for the source. Every skill file is a template — other agents copy the patterns they see.

### 17. Model life like LinkedIn, not like a spreadsheet

People have roles at organizations. Roles have titles, departments, start dates, end dates. Education is a role at a school. Membership is a role in a community. Authorship is a role on a publication.

The LinkedIn mental model: a person has a timeline of positions, each connecting them to an organization with a title and time range. This is principle #2 made concrete.

```
person --roles--> role[] --organization--> organization
                         --title: "Engineer"
                         --department: "Research"
                         --start_date: 2024-01-15
                         --end_date: null (current)
```

This applies broadly: board membership, team membership, project assignment, course enrollment. If a relationship has a time dimension or a title, it's a role.

---

## Review Checklist

After writing or editing a shape, ask yourself:

- [ ] **Fields or relations?** For each string field, ask: *"Is this value itself an entity?"* If yes, make it a relation.
- [ ] **Currency with price?** Every monetary amount has a currency companion.
- [ ] **URLs audited?** Is each URL the record's own link, or does it point to another entity?
- [ ] **Domain-agnostic?** Would this shape make sense for a different source providing the same kind of thing?
- [ ] **`also` justified?** Does the `also` chain represent genuine "is-a" relationships that aid cross-type queries?
- [ ] **Author modeled correctly?** Is the author a string (quick attribution) or a relation (traversable entity)?
- [ ] **Addresses structured?** Are locations/addresses relations to place, not inline strings?
- [ ] **Collections owned?** Do lists/playlists/shelves have a `belongs_to` relation?
- [ ] **Roles, not fields?** Are time-bounded relationships (jobs, education, membership) modeled as role relations, not person fields?
- [ ] **Display makes sense?** Are the right fields in title/subtitle/columns for this shape?
- [ ] **Content vs context?** If this is a media artifact, are social metrics on a wrapper post instead?
- [ ] **Nesting via reply_to?** Is a "sub-type" really just this shape with a parent relation?
- [ ] **ISO standards?** Are languages (ISO 639-1), countries (ISO 3166-1), currencies (ISO 4217) using standard codes?
- [ ] **Booleans or relations?** Does any boolean imply a relationship? (`is_fork` → `forked_from`)
- [ ] **Direction booleans?** Is `is_outgoing`/`is_sent` derivable from a `from` relation?
- [ ] **Cardinality booleans?** Is `is_group`/`has_attachments` derivable from counting a relation?
- [ ] **Source-independent?** Did you design for the domain, or did the API shape leak into the schema?
- [ ] **Roles modeled as LinkedIn?** Are jobs/education/memberships `role[]` relations with title + org + time range?

---

## Returning shape-native data from operations

When an operation declares `returns: email[]`, the Python function returns dicts whose keys match the shape. The shape is the contract — no separate mapping layer sits between the Python code and the engine.

```yaml
# shapes/email.yaml
email:
  also: [message]
  fields:
    from_email: string
    to: string[]
    cc: string[]
    labels: string[]
    thread_id: string
  relations:
    from: account
    conversation: conversation
  display:
    title: name
    subtitle: from_email
    date: datePublished
```

```python
# gmail.py — @returns points at the shape, function returns email-shaped dicts directly
from agentos import returns, connection

@returns("email")
@connection("gmail")
async def get_email(*, id: str, **params) -> dict:
    return {
        "id": msg_id,
        "name": subject,              # standard field
        "text": snippet,              # standard field
        "url": web_url,               # standard field
        "published": date,            # standard field
        "content": body_text,         # standard field (FTS)
        "from_email": sender,         # shape-specific field
        "to": recipients,             # shape-specific field
        "labels": label_ids,          # shape-specific field
    }
```

The Python code does the field mapping — it transforms raw API responses into shape-native dicts. Standard fields (`id`, `name`, `text`, `url`, `image`, `author`, `published`, `content`) are available on every shape without declaring them.

### Canonical fields

The renderer resolves entity display from standard fields. Every Python return should populate as many of these as the source data supports — they drive consistent previews, detail views, and search results across all skills.

| Field           | Purpose                                          |
|-----------------|--------------------------------------------------|
| `name`          | Primary label / title                            |
| `text`          | Short summary or snippet for preview rows        |
| `url`           | Clickable link                                   |
| `image`         | Thumbnail / hero image                           |
| `author`        | Creator / brand / owner                          |
| `published` | Temporal anchor                                  |
| `content`       | Long body text (stored separately, FTS-indexed)  |

Not every entity has all of these — a product may have no `published`, an order may have no `image`. Map what the source provides; skip what doesn't apply.

### Typed references (entity relationships)

To create linked entities and graph edges, return **flat** nested dicts (no wrapper). The relation key in the YAML shape declares the target type; the nested dict is the child record.

```python
@returns("email")
def get_email(*, id: str, **params) -> dict:
    return {
        "id": msg_id,
        "name": subject,
        # Single relation — shape YAML says `from: account`,
        # so a flat dict here becomes: email --from--> account
        "from": {
            "id": sender_email,
            "handle": sender_email,
            "displayName": sender_name,
        },
        # Array relation — shape YAML says `to: account[]`,
        # so a flat list here becomes: email --to--> account (one edge per recipient)
        "to": [
            {"id": addr, "handle": addr, "displayName": name}
            for addr, name in recipients
        ],
    }
```

**Polymorphic children — `_tag` hint.** If a relation target is a supertype (like `participant: actor[]`, where an actor might be a person OR an organization OR an agent), the child dict can include a `_tag` key to override the declared target:

```python
return {
    "id": thread_id,
    "name": thread_title,
    # shape YAML: participant: actor[]
    "participant": [
        {"_tag": "person",       "id": "joe",       "name": "Joe"},
        {"_tag": "organization", "id": "anthropic", "name": "Anthropic"},
    ],
}
```

**Identity — `_identity` hint.** For child records, the engine decides dedupe keys from the YAML shape's `identity` declaration. If you want to override or be explicit, include `_identity` with a list of field names:

```python
"from": {
    "_identity": ["platform", "id"],
    "platform": "gmail",
    "id": msg_id,
    "handle": sender_email,
}
```

A relation is collapsed to null if none of its identity fields survive — partial data doesn't create ghost entities.

---

## Validation

Shape conformance is checked statically, pre-commit.

`agent-sdk validate` parses Python return dict literals via AST and warns if keys don't match the declared shape. It:

- Loads shape YAML from [`shapes/`](https://github.com/agentos-to/site/tree/main/docs/shapes)
- Walks each skill's `*.py` files looking for `@returns("shape")`-decorated functions
- Checks every dict literal the tool returns against the shape's declared fields + relations
- Flags unknown keys, missing identity fields (`id` / `name`), and scalar-fields-that-should-be-relations

Runs automatically on every commit via pre-commit hook. Run manually:

```bash
agent-sdk validate                 # audit every skill under cwd
agent-sdk validate claude          # single skill by id or directory
agent-sdk validate --all           # walk the whole skills/ tree
agent-sdk validate --sandbox       # only the banned-import sandbox check

# Or without install:
python3 -m agentos validate --all
```

Dict-literal returns get checked statically. Helper functions, dynamic construction, and composition through `_call` aren't caught here — integration testing via MCP is the catch-all. If a tool ships bad data, fix the tool and add a regression test.

The engine itself does **not** validate shapes at runtime. It's a generic entity store — it accepts whatever dict shape a skill returns and stores it. Conformance is a contract between skill authors, app authors, and PR review, not a runtime check.

---

## Prior Research

Our ontology research lives in [Research → Ontology](/docs/research/ontology/relationship-modeling/). It's exploratory, not authoritative — some pieces are outdated — but contains principles and platform analysis worth consulting when designing new shapes.

### Entity & Ontology Research
- [Schema entities](/docs/research/ontology/schema-entities/) — Core entity type definitions, OGP foundation, hypotheses on note vs article
- [Schema relationships](/docs/research/ontology/schema-relationships/) — Relationship type catalog and design patterns
- [Open Graph Protocol](/docs/research/ontology/open-graph-protocol/) — OGP types, why flat beats hierarchical
- [Google structured data](/docs/research/ontology/google-structured-data/) — Schema.org structured data patterns

### Platform Research
- [Google Takeout](/docs/research/platforms/google-takeout/) — 72 Google products analyzed for entity types (Contacts, Calendar, Drive, Gmail, Photos, YouTube, Maps, Chrome, Pay, Play)
- [Facebook Graph](/docs/research/platforms/facebook-graph/) — Facebook Graph API entity model
- [FamilySearch](/docs/research/platforms/familysearch/) — GEDCOM X genealogical data model (two relationship types + qualifiers, computed derivations, source citations)

### Relationship Research
- [Genealogical relationships](/docs/research/ontology/genealogical-relationships/) — Family relationship modeling patterns
- [Relationship modeling](/docs/research/ontology/relationship-modeling/) — General relationship design
- [Schema.org relationships](/docs/research/ontology/schema-org-relationships/) — Schema.org relationship types
- [OGP relationships](/docs/research/ontology/ogp-relationships/) — OGP relationship patterns
- [No-orphans constraint](/docs/research/ontology/no-orphans-constraint/) — Why every entity needs at least one connection

### Systems Research
- [Outcome entity](/docs/research/ontology/outcome-entity/) — Outcome/goal entity modeling
- [PKM community](/docs/research/context/pkm-community/) — Personal knowledge management patterns
- [Semantic file systems](/docs/research/context/semantic-file-systems/) — NEPOMUK and semantic desktop research
