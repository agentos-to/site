---
title: health-observation
description: "A single measured health value at a point in time — 'LDL = 95 mg/dL on"
sidebar:
  label: health-observation
---

A single measured health value at a point in time — "LDL = 95 mg/dL on
2024-03-20". The measurement, not the definition (health-biomarker) and
not the lab's catalog interval (health-reference-range).

An observation always carries its own value, and the value's UCUM unit
rides on the value itself — every memex val stores a unit alongside it,
so there is no separate `unit` field. The value is meaningless without
the unit (95 mg/dL is not 95 mmol/L). It links to its biomarker via a
`measures` link.

Reference range — TWO complementary mechanisms, on purpose:
1. SNAPSHOT fields (refLow / refHigh / refText) — the interval THIS
report actually printed, frozen onto the result. This is a
historical fact: it never changes, even if the lab later revises
its range. Always populated when the report stated a range.
2. An optional `reportedRange` link to a health-reference-range node,
set when that lab's interval is known as a first-class entity.
Lets you reconcile the result against the normalized range.
The snapshot is the fact; the link is the enrichment. Both can coexist.

`flag` (low / normal / high / critical) is DERIVED — a reader compares
`value` against the range. Stored as an optional convenience only; it
must never be the source of truth. Re-derive it; don't trust a frozen
copy. (The "derive don't declare" principle.)

`also: [result]` — an observation is a kind of result: a pointer to
something found, with find-time metadata.

`name` (inherited) is the display label, e.g. "LDL Cholesterol 95 mg/dL".

| Metadata | Value |
|---|---|
| **Plural** | `health-observations` |
| **Subtitle field** | `startDate` |
| **Also** | [`result`](/shapes/reference/result/) · [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `value` | `number` |
| `valueText` | `string` |
| `refLow` | `number` |
| `refHigh` | `number` |
| `refText` | `string` |
| `flag` | `string` |
| `status` | `string` |
| `notes` | `text` |

## Relations

| Relation | Target |
|---|---|
| `measures` | [`health-biomarker`](/shapes/reference/health-biomarker/) |
| `part_of` | [`health-panel`](/shapes/reference/health-panel/) |
| `evaluated_against` | [`health-reference-range`](/shapes/reference/health-reference-range/) |
| `documented_in` | [`file`](/shapes/reference/file/) |
| `concerns` | [`person`](/shapes/reference/person/) |

## Inherited

From [`result`](/shapes/reference/result/) · [`event`](/shapes/reference/event/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `community` | `string` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `distinctId` | `string` |
| `endDate` | `datetime` |
| `externalUrl` | `url` |
| `favicon` | `url` |
| `icalUid` | `string` |
| `indexedAt` | `datetime` |
| `postId` | `string` |
| `properties` | `json` |
| `recurrence` | `string[]` |
| `resultType` | `string` |
| `score` | `integer` |
| `showAs` | `string` |
| `similarity` | `number` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `timezone` | `string` |
| `visibility` | `string` |

| Relation | Target |
|---|---|
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `created_by` | [`person`](/shapes/reference/person/) |
| `held_at` | [`place`](/shapes/reference/place/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `organized_by` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[HL7 FHIR R5 — Observation](https://www.hl7.org/fhir/observation.html)** — The canonical resource for a measured value. value (with its UCUM unit) ≈ valueQuantity; effectiveDate ≈ effectiveDateTime; refLow/refHigh/refText ≈ the referenceRange backbone (the inline snapshot); flag ≈ interpretation; status ≈ status. `measures` ≈ code resolved to a biomarker. FHIR has no normalized-range link — our `reportedRange` link adds that.
- **[HL7 v2.x — OBX segment](https://hl7-definition.caristix.com/v2/HL7v2.5/Segments/OBX)** — The legacy lab-result segment most labs still emit. OBX-5 (value) and OBX-6 (units) together ≈ our value-with-unit; OBX-7 (reference range), OBX-8 (abnormal flag), OBX-14 (datetime) map to refText/ flag/effectiveDate. Confirms the snapshot field set against real lab feeds.
- **[LOINC](https://loinc.org/)** — The observation itself is not LOINC-coded — its `biomarker` is. The `measures` link carries the LOINC identity.
- **[UCUM — Unified Code for Units of Measure](https://ucum.org/)** — The unit on every numeric val (mg/dL, mmol/L, 10*3/uL) follows UCUM — the unit system FHIR mandates for Observation.valueQuantity, so observations round-trip into FHIR cleanly.

## Skills that produce this shape

- [health](/skills/reference/misc/health/) — `import_lab_report`
