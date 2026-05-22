// DO NOT EDIT — generated from platform/ontology/shapes/credential.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A credential held by AgentOS — the graph descriptor that mirrors one
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Credential {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub domain: String,
    pub identifier: String,
    pub item_type: String,
    pub last_verified: Option<String>,
    pub obtained_at: Option<String>,
    pub refreshable: Option<bool>,
    pub source: Option<String>,
    pub store_row_id: Option<i64>,
}

pub static CREDENTIAL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "credential".into(),
    plural: Some("credentials".into()),
    description: Some("A credential held by AgentOS — the graph descriptor that mirrors one".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::required("domain", FieldType::String),
        FieldDef::required("identifier", FieldType::String),
        FieldDef::required("itemType", FieldType::String),
        FieldDef::optional("lastVerified", FieldType::Datetime),
        FieldDef::optional("obtainedAt", FieldType::Datetime),
        FieldDef::optional("refreshable", FieldType::Boolean),
        FieldDef::optional("source", FieldType::String),
        FieldDef::optional("storeRowId", FieldType::Integer),
    ],
    identity: vec!["domain".into(), "identifier".into(), "itemType".into()],
    display: Some(DisplaySpec {
        subtitle: Some("source".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
