---
title: health-reference-range
description: "A lab-specific reference interval — the 'normal range' for a biomarker,"
sidebar:
  label: health-reference-range
---

A lab-specific reference interval — the "normal range" for a biomarker,
as established by ONE laboratory using ONE method for ONE population.

This shape exists because a reference range is NOT a property of the
analyte. The same biomarker has different ranges depending on the lab,
the instrument/assay, the reference population, and when the interval
was established. Real evidence: Singapore labs report tighter intervals
than US labs for the same analyte; two clinics in the same US city give
different ranges for the same test. Both are expected — CLSI EP28-A3c
makes every lab establish or verify its own intervals.

No mainstream clinical data model represents the reference range as a
first-class entity — FHIR inlines it on Observation.referenceRange,
OMOP inlines range_low/range_high columns, openEHR inlines it on the
data value. This shape fills that gap. FHIR's ObservationDefinition.
qualifiedInterval is the closest precedent and is the EXPORT projection
of this shape — store rich here, collapse lossy to FHIR for interchange.

Identity is the natural key from clinical reality: which analyte, which
lab, which method, which population, valid from when. Geography is NOT
a key field — it only matters insofar as it changed the lab's reference
population, which `issuingLab` + the population fields already capture.

`validFrom`/`validTo` is the field every standard omits and is the
whole point: a result from 2014 must be interpreted against the
interval that lab considered valid in 2014, not today's.

`name` (inherited) is a human label, e.g. "Quest LDL reference (adult male)".

| Metadata | Value |
|---|---|
| **Plural** | `health-reference-ranges` |
| **Subtitle field** | `refText` |
| **Identity** | `analyte`, `issuingLab`, `method`, `startDate` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `low` | `number` |
| `high` | `number` |
| `unit` | `string` |
| `refText` | `string` |
| `category` | `string` |
| `provenance` | `string` |
| `method` | `string` |
| `ageLow` | `number` |
| `ageHigh` | `number` |
| `sex` | `string` |
| `pregnancy` | `string` |
| `gestationalAge` | `string` |
| `fasting` | `boolean` |
| `timeOfDay` | `string` |

## Inherited

From [`event`](/shapes/reference/event/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `distinctId` | `string` |
| `endDate` | `datetime` |
| `icalUid` | `string` |
| `properties` | `json` |
| `recurrence` | `string[]` |
| `showAs` | `string` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `status` | `string` |
| `timezone` | `string` |
| `visibility` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[CLSI EP28-A3c — Defining, Establishing, and Verifying Reference Intervals](https://clsi.org/shop/standards/ep28/)** — The authoritative protocol. Each lab must establish (de novo, min n=120 per partition) or verify (min n=20) its own intervals. `provenance` (established/verified/manufacturer-claimed) comes directly from this guideline; it is why two same-instrument labs legitimately diverge.
- **[HL7 FHIR R5 — ObservationDefinition.qualifiedInterval](https://www.hl7.org/fhir/observationdefinition.html)** — The closest standard precedent — a reusable, multi-context interval. Our category maps to its rangeCategory; range to range; age/gestationalAge/sex to the same; condition ≈ our population fields. But qualifiedInterval has NO issuingLab and NO validity window — this shape adds both. qualifiedInterval is the lossy EXPORT projection of this shape, not its equal.
- **[HL7 FHIR R5 — Observation.referenceRange](https://www.hl7.org/fhir/observation.html)** — FHIR's other reference-range model — inlined on the result as a denormalized snapshot (low/high/normalValue/type/appliesTo/age/ text). health-observation keeps that snapshot too (its refLow/ refHigh fields); this shape is the normalized, reusable form the snapshot can point back to.
- **[OMOP CDM v5.4 — MEASUREMENT.range_low / range_high](https://ohdsi.github.io/CommonDataModel/cdm54.html)** — OMOP inlines range_low/range_high as columns on the measurement row — "no separate standalone table for reference ranges." Confirms the gap: no major model makes the range first-class.
