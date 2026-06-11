// DO NOT EDIT — generated from platform/ontology/shapes/agentos/subscription.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A standing subscription — a durable intent to stream live entities, re-armed on every engine boot.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Subscription {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub app: String,
    pub op: String,
    pub target: Option<String>,
}

pub static SUBSCRIPTION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "subscription".into(),
    plural: Some("subscriptions".into()),
    description: Some("A standing subscription — a durable intent to stream live entities, re-armed on every engine boot.".into()),
    icon: Some("rss".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::required("app", FieldType::String),
        FieldDef::required("op", FieldType::String),
        FieldDef::optional("target", FieldType::String),
    ],
    identity: vec!["app".into(), "op".into()],
    display: Some(DisplaySpec {
        subtitle: Some("target".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
