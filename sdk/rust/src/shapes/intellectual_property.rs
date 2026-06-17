// DO NOT EDIT — generated from platform/ontology/shapes/intellectual_property.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A registered or pending intellectual-property right — a trademark,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct IntellectualProperty {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub category: Option<String>,
    pub filing_basis: Option<String>,
    pub identifier: Option<String>,
    pub mark: Option<String>,
    pub nice_class: Option<Vec<i64>>,
    pub register: Option<String>,
    pub renewal_period: Option<String>,
    pub status: Option<String>,
    pub valid_in: Option<String>,
    pub verification_url: Option<String>,
}

pub static INTELLECTUAL_PROPERTY: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "intellectual_property".into(),
    plural: Some("intellectual_properties".into()),
    description: Some("A registered or pending intellectual-property right — a trademark,".into()),
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
        FieldDef::optional("filingBasis", FieldType::String),
        FieldDef::optional("identifier", FieldType::String),
        FieldDef::optional("mark", FieldType::String),
        FieldDef::optional("niceClass", FieldType::IntegerList),
        FieldDef::optional("register", FieldType::String),
        FieldDef::optional("renewalPeriod", FieldType::String),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("validIn", FieldType::String),
        FieldDef::optional("verificationUrl", FieldType::Url),
    ],
    identity_any: vec!["identifier".into()],
    display: Some(DisplaySpec {
        subtitle: Some("category".into()),
        highlights: vec!["identifier".into(), "status".into(), "granted_by".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Wikidata — trademark (Q167270) / registered trademark (Q111048186)".into(), url: Some("https://www.wikidata.org/wiki/Q167270".into()), notes: Some("Trademark is a subclass of `intellectual property right` and of `mark`; holder via `owned by` (P127). registered-vs-pending is a status of one type, not a separate type — our `status` field.".into()) },
        PriorArtDef { source: "WIPO Standard ST.96 — Trademark Components".into(), url: Some("https://www.wipo.int/standards/en/st96/v8-0/release_notes.html".into()), notes: Some("Canonical IP-office XML model. Source for mark, identifier, register, niceClass, status. Splits schemas by Trademark / Patent / Design Components — confirms `category` as the discriminator across one `intellectual_property` concept.".into()) },
        PriorArtDef { source: "WIPO Standard ST.87 — IP event codes".into(), url: Some("https://www.wipo.int/standards/en/".into()), notes: Some("Standard lifecycle-event vocabulary (KeyEventCode). The filed/published/granted/lapsed milestones are dated links to the granting office, not node fields — events-as-links rule 1.".into()) },
        PriorArtDef { source: "Nice Classification (Nice Agreement 1957; NCL 13-2026)".into(), url: Some("https://www.wipo.int/en/web/classification-nice".into()), notes: Some("45-class system (1-34 goods, 35-45 services). `niceClass` is an integer[] of class numbers — a standard code. ADAVIA is Class 42.".into()) },
        PriorArtDef { source: "USPTO — trademark process & intent-to-use basis".into(), url: Some("https://www.uspto.gov/trademarks/basics/trademark-process".into()), notes: Some("Lifecycle and the use-vs-intent-to-use fork. Source for the `status` value set and `filingBasis`.".into()) },
        PriorArtDef { source: "schema.org/Intangible, schema.org/Brand".into(), url: Some("https://schema.org/Intangible".into()), notes: Some("Weak alignment — schema.org has no Trademark type; `Brand` is the marketing concept, not the legal right. Cited to mark the gap web ontologies leave: the IP right needs its own shape.".into()) },
    ],
    ..ShapeDef::default()
});
