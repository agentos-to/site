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
    ..ShapeDef::default()
});
