---
title: health-lab
description: "A clinical laboratory or testing facility — the place that processes a"
sidebar:
  label: health-lab
---

A clinical laboratory or testing facility — the place that processes a
blood draw, runs an assay, and issues results. Quest Diagnostics,
LabCorp, a hospital lab, a Singapore screening clinic, a travel-health
center.

`also: [organization]` — a lab IS an organization (which is in turn an
actor). Same pattern as `airline`: an airline is also an organization,
adding only airline-specific fields. health-lab adds only the fields
that matter for a testing facility, and inherits name / industry /
headquarters / website from organization.

A lab matters in this graph because it is the issuer of reference
ranges (health-reference-range.issuingLab) and the performer of panels
(health-panel.performedAt). Two labs running the same test can report
different reference intervals — the lab is the identity that explains
that divergence.

`name` (inherited from organization→actor) is the lab name —
"Quest Diagnostics", "Fullerton Health".

| Metadata | Value |
|---|---|
| **Plural** | `health-labs` |
| **Subtitle field** | `labType` |
| **Identity (any)** | `cliaNumber`, `url` |
| **Also** | [`organization`](/shapes/reference/organization/) |

## Fields

| Field | Type |
|---|---|
| `cliaNumber` | `string` |
| `npi` | `string` |
| `ccn` | `string` |
| `labType` | `string` |
| `accreditation` | `string` |

## Inherited

From [`organization`](/shapes/reference/organization/):

| Field | Type |
|---|---|
| `actorType` | `string` |
| `industry` | `string` |

| Relation | Target |
|---|---|
| `for` | [`person[]`](/shapes/reference/person/) |
| `headquartered_at` | [`place`](/shapes/reference/place/) |
| `on` | [`domain`](/shapes/reference/domain/) |
| `online_at` | [`website`](/shapes/reference/website/) |
| `subsidiary_of` | [`organization`](/shapes/reference/organization/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/MedicalOrganization / DiagnosticLab](https://schema.org/DiagnosticLab)** — schema.org's DiagnosticLab is a MedicalOrganization subtype, which is an Organization subtype — exactly our also:[organization] chain. Our labType refines what schema.org leaves implicit.
- **[CLIA — Clinical Laboratory Improvement Amendments](https://www.cms.gov/medicare/quality/clinical-laboratory-improvement-amendments)** — cliaNumber, npi (the organizational/type-2 National Provider Identifier), and ccn (the Medicare CMS Certification Number) are all CMS-issued identifiers a US testing facility carries. cliaNumber is the canonical identity for a US clinical lab.
- **[HL7 FHIR R5 — Organization (role: laboratory)](https://www.hl7.org/fhir/organization.html)** — FHIR models a lab as an Organization with a laboratory role code, not a distinct resource — consistent with our also:[organization]. FHIR Observation.performer / DiagnosticReport.performer reference it; our health-panel.performedAt and health-reference-range. issuingLab links are the same linkage.
