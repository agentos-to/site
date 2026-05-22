// DO NOT EDIT — generated from platform/ontology/shapes/dimension.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A physical dimension — the abstract nature of a quantity, expressed as
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Dimension {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub amount: Option<i64>,
    pub current: Option<i64>,
    pub dimensionless: Option<bool>,
    pub key: String,
    pub label: Option<String>,
    pub length: Option<i64>,
    pub luminous: Option<i64>,
    pub mass: Option<i64>,
    pub temperature: Option<i64>,
    pub time: Option<i64>,
}

pub static DIMENSION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "dimension".into(),
    plural: Some("dimensions".into()),
    description: Some("A physical dimension — the abstract nature of a quantity, expressed as".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("amount", FieldType::Integer),
        FieldDef::optional("current", FieldType::Integer),
        FieldDef::optional("dimensionless", FieldType::Boolean),
        FieldDef::required("key", FieldType::String),
        FieldDef::optional("label", FieldType::String),
        FieldDef::optional("length", FieldType::Integer),
        FieldDef::optional("luminous", FieldType::Integer),
        FieldDef::optional("mass", FieldType::Integer),
        FieldDef::optional("temperature", FieldType::Integer),
        FieldDef::optional("time", FieldType::Integer),
    ],
    identity: vec!["key".into()],
    display: Some(DisplaySpec {
        subtitle: Some("label".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
