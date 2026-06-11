---
title: qualification
description: "An earned qualification — a degree, professional license, board"
sidebar:
  label: qualification
---

An earned qualification — a degree, professional license, board
certification, fellowship, trade license, or certificate. The unifying
primitive for "something a person acquired that attests to a
competency": an MBBS, an FRCS fellowship, a US medical license, a bar
admission, a PE license, a barber's license.

One shape, not many — `category` discriminates. Every credential
ontology that spans the full breadth (schema.org
EducationalOccupationalCredential, CTDL, Open Badges) uses a single
type with a category field; LinkedIn's Education-vs-Licenses split is
a UI artifact, not an ontology.

Two organizations, deliberately distinct (CTDL proves the split):
- granted_by — the body that ISSUED this instance: the university
that conferred the degree, the state board that issued the license.
- governed_by — the body that ACCREDITS / LICENSES / REGULATES the
credential type. Often the same org as granted_by; often not — a US
medical license is granted by a state board but governed by
statute / the FSMB.

Renewal is not a new node: a renewed license is the same qualification
with `status` flipped and `expiresOn` advanced.

Not the auth `credential` shape — that is an encrypted vault secret.
A qualification carries nothing secret; it is a public attestation.

`name` (inherited) is the display label — "Bachelor of Medicine,
Bachelor of Surgery", "FRCS (Edinburgh)", "California Medical License".

| Metadata | Value |
|---|---|
| **Plural** | `qualifications` |
| **Subtitle field** | `category` |
| **Identity (any)** | `identifier` |

## Fields

| Field | Type |
|---|---|
| `category` | `string` |
| `identifier` | `string` |
| `status` | `string` |
| `renewalPeriod` | `string` |
| `level` | `string` |
| `validIn` | `string` |
| `verificationUrl` | `url` |

## Relations

| Relation | Target |
|---|---|
| `held_by` | [`person`](/shapes/reference/person/) |
| `granted_by` | [`organization`](/shapes/reference/organization/) |
| `governed_by` | [`organization`](/shapes/reference/organization/) |
| `in` | [`practice`](/shapes/reference/practice/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org EducationalOccupationalCredential](https://schema.org/EducationalOccupationalCredential)** — Single credential class with a credentialCategory discriminator; recognizedBy, validFor, validIn, educationalLevel. Person.hasCredential links the holder — our `held_by` link.
- **[CTDL — Credential Transparency Description Language (Credential Engine)](https://credreg.net/ctdl/terms/CredentialType)** — The most thorough credential ontology — a Credential superclass with ~40 subtypes and four distinct org roles (ownedBy / offeredBy vs accreditedBy / regulatedBy / recognizedBy). The source for splitting `granted_by` from `governed_by`; we collapse the regulator family into one link — four roles is over-modeled for a personal graph.
- **[W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/)** — Separates the issuer + validFrom / validUntil (the issuing act) from credentialSubject (the claim); credentialStatus models revocation — our `status` covers revoked / suspended, which schema.org omits.
- **[Open Badges 3.0 (1EdTech)](https://www.imsglobal.org/spec/ob/v3p0/impl)** — Achievement.achievementType enum (Certificate, Certification, Degree, License, Badge, MicroCredential) — confirms one shape plus a category enum across every credential kind.
- **[LinkedIn Licenses & Certifications](https://www.linkedin.com/help/linkedin/answer/a567169)** — Real-world minimal field set — name, issuing organization, issue date, expiration date, credential ID, credential URL. Its Education / Licenses UI split is the seam this shape unifies.
