---
title: health-panel
description: "A panel — a named grouping of biomarkers ordered and reported together."
sidebar:
  label: health-panel
---

A panel — a named grouping of biomarkers ordered and reported together.
CBC (complete blood count), CMP (comprehensive metabolic panel), Lipid
panel, Thyroid panel.

A panel is both a *catalog* concept (the standard set of biomarkers a
"CBC" includes) and, when dated, a *report* concept (the CBC drawn on
2024-03-20). When a panel node represents a specific dated draw,
`effectiveDate` is set, its `contains` links point to observations, and
`document` points to the report file. When it represents the abstract
catalog panel, `effectiveDate` is null and `contains` points to
biomarkers.

`also: [list]` — a panel IS a list: an ordered collection of biomarker
(definition) or observation (result) nodes, listType 'health-panel'.
This reuses the universal list machinery rather than inventing grouping.

FHIR models the dated form as a DiagnosticReport; the catalog form has
no single FHIR resource (closest is a definitional ServiceRequest).

`name` (inherited) is the panel name — "CBC", "Comprehensive Metabolic Panel".

| Metadata | Value |
|---|---|
| **Plural** | `health-panels` |
| **Subtitle field** | `startDate` |
| **Also** | [`list`](/shapes/reference/list/) · [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `panelCode` | `string` |
| `fasting` | `boolean` |
| `description` | `text` |

## Inherited

From [`list`](/shapes/reference/list/) · [`event`](/shapes/reference/event/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `arrangement` | `string` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `default_view` | `string` |
| `distinctId` | `string` |
| `endDate` | `datetime` |
| `icalUid` | `string` |
| `icon_size` | `integer` |
| `isDefault` | `boolean` |
| `isPublic` | `boolean` |
| `itemCount` | `integer` |
| `listId` | `string` |
| `listType` | `string` |
| `member_shape` | `string` |
| `ordering_mode` | `string` |
| `path` | `string` |
| `privacy` | `string` |
| `properties` | `json` |
| `recurrence` | `string[]` |
| `showAs` | `string` |
| `sort_by` | `string` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `status` | `string` |
| `timezone` | `string` |
| `visibility` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[HL7 FHIR R5 — DiagnosticReport](https://www.hl7.org/fhir/diagnosticreport.html)** — A dated panel is a DiagnosticReport: a set of observations grouped under one report with an effective date and a performer. Our `contains` links (from `list`) ≈ DiagnosticReport.result; effectiveDate ≈ effectiveDateTime; performedAt ≈ performer.
- **[LOINC — Panels and Forms](https://loinc.org/panels/)** — LOINC defines panel codes and their member observables (CBC panel 58410-2 enumerates hemoglobin, hematocrit, WBC, …). panelCode plus the contains→biomarker links mirror a LOINC panel definition.
- **[schema.org/MedicalTest](https://schema.org/MedicalTest)** — Lighter-weight precedent — a diagnostic test with usedToDiagnose / normalRange. Our panel is the grouping; biomarkers and health-reference-range carry the observable detail and the ranges.
