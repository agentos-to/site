---
title: health-procedure
description: "A procedure — a clinical action performed on the body. Surgeries"
sidebar:
  label: health-procedure
---

A procedure — a clinical action performed on the body. Surgeries
("septoplasty"), diagnostic scans ("ankle MRI", "colonoscopy"),
therapies ("physiotherapy course"). The thing that was *done*, as
opposed to a health-condition (what you have) or a health-observation
(a value measured).

`also: [event]` — a procedure IS an event: it happened at a time, at a
place, involving people (surgeon, radiologist). Unlike an immunization,
a procedure can span time, so it uses the event's startDate/endDate for
multi-session courses (a physiotherapy course) and `performedDate` for
point procedures.

A procedure usually addresses a health-condition (the septoplasty
treats the deviated septum). That `treats` link lets you ask "what was
done about the 2016 stomach problem".

`bodySite` is a plain string — anatomy is not modeled as its own shape
(see health-condition for the rationale).

CPT (billing) and SNOMED CT (clinical) both code procedures —
`cptCode` / `snomedCode` are the join keys.

`name` (inherited via event) is the procedure name — "Septoplasty".

| Metadata | Value |
|---|---|
| **Plural** | `health-procedures` |
| **Subtitle field** | `performedDate` |
| **Identity (any)** | `cptCode`, `snomedCode`, `id` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `performedDate` | `datetime` |
| `procedureType` | `string` |
| `bodySite` | `string` |
| `outcome` | `string` |
| `status` | `string` |
| `cptCode` | `string` |
| `snomedCode` | `string` |
| `findings` | `text` |
| `followUp` | `text` |

## Relations

| Relation | Target |
|---|---|
| `treats` | [`health-condition`](/shapes/reference/health-condition/) |
| `performed_by` | [`person`](/shapes/reference/person/) |
| `ordered_by` | [`person`](/shapes/reference/person/) |
| `performed_at` | [`health-lab`](/shapes/reference/health-lab/) |
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

- **[HL7 FHIR R5 — Procedure](https://www.hl7.org/fhir/procedure.html)** — The resource for an action performed on a patient. performedDate ≈ occurrenceDateTime/occurrencePeriod; status ≈ status; bodySite ≈ bodySite; outcome ≈ outcome; findings ≈ report + note; `treats` link ≈ reason; performer ≈ performer.actor. `orderedBy` ≈ basedOn → ServiceRequest.requester — the clinician who ordered the study, which on imaging/scopes is rarely the one who performs it.
- **[CPT — Current Procedural Terminology (AMA)](https://www.ama-assn.org/practice-management/cpt)** — The US procedure code system used for billing. cptCode is the identity on insurance claims and operative records (septoplasty 30520, colonoscopy 45378).
- **[SNOMED CT — Procedure axis](https://www.snomed.org/)** — SNOMED's procedure hierarchy provides the clinical (non-billing) code. FHIR Procedure.code is SNOMED-coded; snomedCode is the join key to the clinical ontology.
