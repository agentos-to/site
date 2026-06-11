---
title: health-condition
description: "A health condition — a diagnosis, problem, symptom, or family-history"
sidebar:
  label: health-condition
---

A health condition — a diagnosis, problem, symptom, or family-history
concern. "Asthma", "deviated septum", "seborrheic dermatitis", or a
family risk like "aortic aneurysm in extended family".

`proximity` is what makes one shape cover both personal conditions and
family history: 'self' = a condition you have; 'father' / 'mother' /
'sibling' / 'extended-family' = a hereditary concern. FHIR splits these
into Condition vs FamilyMemberHistory; we deliberately unify them,
because for a personal health graph "what runs in my family" and "what
I have" are the same question asked at different proximities. (Joe's
prior LifeOS `concerns` table already modeled it exactly this way.)

`also: [note]` — a condition is a kind of note: private text content
about your health, authored by you. It can reference other notes and
carry free-form body content (history, mitigation plan).

`bodySite` is a plain string. Anatomy is NOT modeled as its own shape —
a personal health graph has too few distinct sites for an anatomy
ontology to earn its keep. If that changes, a structured body-structure
shape can be added as a purely additive migration.

SNOMED CT is the universal clinical terminology — `snomedCode` is the
join key (asthma = 195967001). ICD-10-CM is the billing/diagnosis code.

`name` (inherited) is the condition name — "Asthma", "Deviated Septum".

| Metadata | Value |
|---|---|
| **Plural** | `health-conditions` |
| **Subtitle field** | `clinicalStatus` |
| **Identity (any)** | `snomedCode`, `name` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `clinicalStatus` | `string` |
| `verificationStatus` | `string` |
| `proximity` | `string` |
| `bodySite` | `string` |
| `severity` | `string` |
| `snomedCode` | `string` |
| `icd10Code` | `string` |
| `clinicalArea` | `string` |
| `mitigation` | `text` |

## Relations

| Relation | Target |
|---|---|
| `concerns` | [`person`](/shapes/reference/person/) |
| `evidenced_by` | [`file[]`](/shapes/reference/file/) |

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

| Relation | Target |
|---|---|
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `created_by` | [`person`](/shapes/reference/person/) |
| `held_at` | [`place`](/shapes/reference/place/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `organized_by` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[HL7 FHIR R5 — Condition](https://www.hl7.org/fhir/condition.html)** — The resource for a problem/diagnosis. Our clinicalStatus, verificationStatus, severity, bodySite, onsetDate, abatementDate map directly. proximity='self' is a plain FHIR Condition.
- **[HL7 FHIR R5 — FamilyMemberHistory](https://www.hl7.org/fhir/familymemberhistory.html)** — FHIR's separate resource for hereditary risk. We fold it in via proximity — proximity='father'|'extended-family' makes a condition node a family-history entry. FamilyMemberHistory.condition ≈ this node; FamilyMemberHistory.relationship ≈ our proximity. Deliberate divergence from FHIR's two-resource split.
- **[SNOMED CT](https://www.snomed.org/)** — The universal clinical terminology. snomedCode is the canonical identity (asthma 195967001, eczema 43116000). FHIR Condition.code is SNOMED-coded; this is the join key to the wider clinical world.
- **[ICD-10-CM](https://www.cdc.gov/nchs/icd/icd-10-cm.htm)** — The diagnosis/billing code system. icd10Code captures the code when it appears on an insurance claim or discharge summary — complements (does not replace) SNOMED.
