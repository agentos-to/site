---
title: Shape design principles
description: Higher-order principles for shape design. Extracted from practice, updated as we learn.
---

Higher-order principles for shape design. Extracted from practice, updated as we learn.

For the tactical reference (field types, format, display rules), see the [Ontology overview](/docs/ontology/overview/).

## 1. A shape describes what something IS, not where it came from

A book is a book. Not a "Goodreads book" or an "Amazon book." The shape defines intrinsic properties. The skill defines the source.

## 2. No counts on shapes

`worksCount`, `employeeCount`, `memberCount`, `subscriberCount`, `itemCount` — none of these should be stored fields. They're either:
- **Computable** from graph structure (count of `book --writtenBy--> person` edges), or
- **Unreliable** because different sources disagree (LinkedIn says 5000 employees, PitchBook says 4800)

The graph is not a global source of truth. Whoever provided the count is probably already outdated. Delete count fields. If the engine needs a count, it can query the graph.

## 3. A shape earns its existence by having unique fields

If shape B has no fields beyond what shape A already has, B might not need to exist. The relationship between entities (edges) can express the role.

- `author` with no unique fields → just `person` with `book --writtenBy--> person` edges
- `shelf` with only `isExclusive` beyond `list` → questionable. Is it just a `list` of books?

The `also` chain should add meaningful fields at each level. If a child shape is empty, it might be a tag (a label on an entity) rather than a shape (a type definition).

## 4. Shapes are nouns, edges are verbs

- "A person" is a shape. "A person authored a book" is an edge.
- "An account" is a shape. "A person owns an account" is an edge.
- "A book" is a shape. "A platform rates a book 4.2" is an edge with values.

When you're tempted to add a field that describes what the entity DID or what HAPPENED to it — that's probably an edge.

## 5. Lists are lists

Shelf, playlist, album, folder, collection, calendar — these are all lists with different names. The structure is identical: a container with an ordered set of items.

When two shapes are identical except for the name, that's a signal. Maybe they're the same shape with a `listType` field. Maybe they're tags on a generic `list`. We don't have the answer yet — this is an open design question.

## 6. Platform-specific data lives on edges, not entities

A book's rating on Goodreads is a property of the Goodreads-book relationship, not the book.
A person's karma on Reddit is a property of the Reddit-account relationship, not the person.
A product's Prime eligibility is a property of the Amazon-product relationship, not the product.

The graph supports edge values (`set_edge_val`). Use them.

## 7. Identity should be universal when possible

ISBN identifies a book across all platforms. A domain name identifies a domain universally. An email address identifies an account universally.

When a universal identifier exists, use it. When only platform-specific IDs exist, use `identity: [platform, id]`.

## 8. Dates are events

A person's birthday is an event: "this person was born on this date." An organization's founding is an event: "this company was founded on this date." Modeling dates as events enables timeline views — "what happened on April 5?" returns births, foundings, meetings, launches, all in one query.

This doesn't mean every date field becomes a full event entity today. `birthday` and `founded` can stay as fields for now. But the direction is: important dates become events linked to entities, not fields on entities.

## 9. Edges are bidirectional

The graph supports `inverse_name` on relationship types. If a person authored a book (`person --write--> book`), the book shows "written by person" (`book <--write-- person`). Both directions exist in the graph. Shapes declare one direction in `relations`; the engine resolves the other.

When a skill creates an edge in one direction, the inverse is automatically queryable. "Show me all books written by this person" and "Show me who wrote this book" are the same edge traversed in opposite directions.

## 10. Principles evolve

These principles are extracted from practice, not prescribed from theory. As we build more skills and model more domains, we'll discover new patterns and refine these. The test is always: does this make the ontology more useful and more universal?
