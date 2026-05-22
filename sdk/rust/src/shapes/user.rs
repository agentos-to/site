// DO NOT EDIT — generated from platform/ontology/shapes/user.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// An AgentOS user — the seat at this machine. Carries the user's
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct User {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub actor_type: Option<String>,
    pub os_username: Option<String>,
    pub primary_user: Option<bool>,
}

pub static USER: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "user".into(),
    plural: Some("users".into()),
    description: Some("An AgentOS user — the seat at this machine. Carries the user's".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("actorType", FieldType::String),
        FieldDef::optional("osUsername", FieldType::String),
        FieldDef::optional("primaryUser", FieldType::Boolean),
    ],
    also: vec!["actor".into()],
    identity_any: vec!["osUsername".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
