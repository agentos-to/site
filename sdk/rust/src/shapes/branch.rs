// DO NOT EDIT — generated from platform/ontology/shapes/branch.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A git branch.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Branch {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub ahead: Option<i64>,
    pub behind: Option<i64>,
    pub commit: Option<String>,
    pub is_current: Option<bool>,
    pub is_remote: Option<bool>,
    pub upstream: Option<String>,
}

pub static BRANCH: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "branch".into(),
    plural: Some("branches".into()),
    description: Some("A git branch.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("ahead", FieldType::Integer),
        FieldDef::optional("behind", FieldType::Integer),
        FieldDef::optional("commit", FieldType::String),
        FieldDef::optional("isCurrent", FieldType::Boolean),
        FieldDef::optional("isRemote", FieldType::Boolean),
        FieldDef::optional("upstream", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("commit".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
