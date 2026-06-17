// DO NOT EDIT — generated from platform/ontology/shapes/qualification.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An earned qualification — a degree, professional license, board
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Qualification {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub category: Option<String>,
    pub identifier: Option<String>,
    pub level: Option<String>,
    pub renewal_period: Option<String>,
    pub status: Option<String>,
    pub valid_in: Option<String>,
    pub verification_url: Option<String>,
}

pub static QUALIFICATION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "qualification".into(),
    plural: Some("qualifications".into()),
    description: Some("An earned qualification — a degree, professional license, board".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("category", FieldType::String),
        FieldDef::optional("identifier", FieldType::String),
        FieldDef::optional("level", FieldType::String),
        FieldDef::optional("renewalPeriod", FieldType::String),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("validIn", FieldType::String),
        FieldDef::optional("verificationUrl", FieldType::Url),
    ],
    identity_any: vec!["identifier".into()],
    display: Some(DisplaySpec {
        subtitle: Some("category".into()),
        highlights: vec!["identifier".into(), "validIn".into(), "granted_by".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org EducationalOccupationalCredential".into(), url: Some("https://schema.org/EducationalOccupationalCredential".into()), notes: Some("Single credential class with a credentialCategory discriminator; recognizedBy, validFor, validIn, educationalLevel. Person.hasCredential links the holder — our `held_by` link.".into()) },
        PriorArtDef { source: "CTDL — Credential Transparency Description Language (Credential Engine)".into(), url: Some("https://credreg.net/ctdl/terms/CredentialType".into()), notes: Some("The most thorough credential ontology — a Credential superclass with ~40 subtypes and four distinct org roles (ownedBy / offeredBy vs accreditedBy / regulatedBy / recognizedBy). The source for splitting `granted_by` from `governed_by`; we collapse the regulator family into one link — four roles is over-modeled for a personal graph.".into()) },
        PriorArtDef { source: "W3C Verifiable Credentials Data Model 2.0".into(), url: Some("https://www.w3.org/TR/vc-data-model-2.0/".into()), notes: Some("Separates the issuer + validFrom / validUntil (the issuing act) from credentialSubject (the claim); credentialStatus models revocation — our `status` covers revoked / suspended, which schema.org omits.".into()) },
        PriorArtDef { source: "Open Badges 3.0 (1EdTech)".into(), url: Some("https://www.imsglobal.org/spec/ob/v3p0/impl".into()), notes: Some("Achievement.achievementType enum (Certificate, Certification, Degree, License, Badge, MicroCredential) — confirms one shape plus a category enum across every credential kind.".into()) },
        PriorArtDef { source: "LinkedIn Licenses & Certifications".into(), url: Some("https://www.linkedin.com/help/linkedin/answer/a567169".into()), notes: Some("Real-world minimal field set — name, issuing organization, issue date, expiration date, credential ID, credential URL. Its Education / Licenses UI split is the seam this shape unifies.".into()) },
    ],
    ..ShapeDef::default()
});
