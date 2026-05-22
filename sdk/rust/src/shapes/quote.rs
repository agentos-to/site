// DO NOT EDIT — generated from platform/ontology/shapes/quote.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A notable quote. Attribution is a graph relationship, not a field —
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Quote {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub context: Option<String>,
    pub year: Option<i64>,
}

pub static QUOTE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "quote".into(),
    plural: Some("quotes".into()),
    description: Some("A notable quote. Attribution is a graph relationship, not a field —".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("context", FieldType::String),
        FieldDef::optional("year", FieldType::Integer),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("year".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
