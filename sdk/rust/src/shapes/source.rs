// DO NOT EDIT — generated from platform/ontology/shapes/agentos/source.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A content source — where skills, themes, shapes, and wallpapers live.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Source {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub address: String,
    pub description: Option<String>,
    pub enabled: Option<bool>,
    pub last_synced: Option<String>,
    pub scanner: Option<String>,
    pub source_id: Option<String>,
}

pub static SOURCE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "source".into(),
    plural: Some("sources".into()),
    description: Some("A content source — where skills, themes, shapes, and wallpapers live.".into()),
    icon: Some("📦".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::required("address", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("enabled", FieldType::Boolean),
        FieldDef::optional("lastSynced", FieldType::Datetime),
        FieldDef::optional("scanner", FieldType::String),
        FieldDef::optional("sourceId", FieldType::String),
    ],
    identity: vec!["address".into()],
    display: Some(DisplaySpec {
        subtitle: Some("sourceId".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
