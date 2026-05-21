---
title: health-biomarker
description: "The *definition* of a measurable health quantity — TSH, LDL cholesterol,"
sidebar:
  label: health-biomarker
---

The *definition* of a measurable health quantity — TSH, LDL cholesterol,
hemoglobin A1c. NOT a measurement (that's health-observation), and NOT a
reference range (that's health-reference-range).

A biomarker is the reusable, lab-neutral template: what is measured,
what clinical category it belongs to, what it means. One biomarker,
many observations, many reference ranges. It carries no unit — the
unit is a per-observation fact (it rides on each observation's value),
because one analyte is reported in different units by different labs.

Deliberately, a biomarker carries NO reference range. A range is not a
property of the analyte — it depends on the lab, method, and population
(see health-reference-range). "LDL cholesterol" is defined once here;
Quest's LDL range and a Singapore lab's LDL range are two separate
health-reference-range nodes, both pointing back to this biomarker.

LOINC is the universal code system for lab observables — `loincCode` is
the join key to the rest of the medical world. Two labs reporting "TSH"
under different local names both map to LOINC 3016-3. LOINC identifies
the observable ONLY; it never carries a range.

`name` (inherited) is the display label, e.g. "LDL Cholesterol".

| Metadata | Value |
|---|---|
| **Plural** | `health-biomarkers` |
| **Subtitle field** | `category` |
| **Identity (any)** | `loincCode`, `measure` |

## Fields

| Field | Type |
|---|---|
| `measure` | `string` |
| `category` | `string` |
| `loincCode` | `string` |
| `analyteType` | `string` |
| `description` | `text` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[HL7 FHIR R5 — ObservationDefinition](https://www.hl7.org/fhir/observationdefinition.html)** — FHIR's ObservationDefinition is the reusable definition of an observable, separate from the Observation that records a value. Our measure/category map to its code + quantitativeDetails. We deliberately do NOT include its qualifiedInterval — reference ranges are their own shape (health-reference-range).
- **[LOINC — Logical Observation Identifiers Names and Codes](https://loinc.org/)** — The universal code system for lab and clinical observations. loincCode is the join key — every lab observable has a LOINC code (TSH 3016-3, LDL 2089-1, HbA1c 4548-4). LOINC identifies the observable only; it carries no reference range.
