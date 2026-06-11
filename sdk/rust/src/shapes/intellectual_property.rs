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
    out: vec![
        EdgeDef { label: "held_by".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "granted_by".into(), to: Some("organization".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "covers".into(), to: Some("creative_work".into()), from: None, card: Cardinality::One },
    ],
    identity_any: vec!["identifier".into()],
    display: Some(DisplaySpec {
        subtitle: Some("category".into()),
        highlights: vec!["identifier".into(), "status".into(), "granted_by".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
