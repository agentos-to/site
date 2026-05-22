// DO NOT EDIT — generated from platform/ontology/shapes/health-lab.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A clinical laboratory or testing facility — the place that processes a
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct HealthLab {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub accreditation: Option<String>,
    pub actor_type: Option<String>,
    pub ccn: Option<String>,
    pub clia_number: Option<String>,
    pub industry: Option<String>,
    pub lab_type: Option<String>,
    pub npi: Option<String>,
}

pub static HEALTH_LAB: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "health-lab".into(),
    plural: Some("health-labs".into()),
    description: Some("A clinical laboratory or testing facility — the place that processes a".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("accreditation", FieldType::String),
        FieldDef::optional("actorType", FieldType::String),
        FieldDef::optional("ccn", FieldType::String),
        FieldDef::optional("cliaNumber", FieldType::String),
        FieldDef::optional("industry", FieldType::String),
        FieldDef::optional("labType", FieldType::String),
        FieldDef::optional("npi", FieldType::String),
    ],
    also: vec!["organization".into()],
    identity_any: vec!["cliaNumber".into(), "url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("labType".into()),
        image: Some("image".into()),
        highlights: vec!["headquarters".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
