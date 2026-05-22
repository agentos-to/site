// DO NOT EDIT — generated from platform/ontology/shapes/health-biomarker.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// The *definition* of a measurable health quantity — TSH, LDL cholesterol,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct HealthBiomarker {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub analyte_type: Option<String>,
    pub category: Option<String>,
    pub description: Option<String>,
    pub loinc_code: Option<String>,
    pub measure: Option<String>,
}

pub static HEALTH_BIOMARKER: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "health-biomarker".into(),
    plural: Some("health-biomarkers".into()),
    description: Some("The *definition* of a measurable health quantity — TSH, LDL cholesterol,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("analyteType", FieldType::String),
        FieldDef::optional("category", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("loincCode", FieldType::String),
        FieldDef::optional("measure", FieldType::String),
    ],
    identity_any: vec!["loincCode".into(), "measure".into()],
    display: Some(DisplaySpec {
        subtitle: Some("category".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
