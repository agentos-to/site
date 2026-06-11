// DO NOT EDIT — generated from platform/ontology/shapes/agentos/service.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A service — a named interface the engine brokers between strangers.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Service {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub description: Option<String>,
    pub params: Option<serde_json::Value>,
    pub returns: Option<String>,
}

pub static SERVICE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "service".into(),
    plural: Some("services".into()),
    description: Some("A service — a named interface the engine brokers between strangers.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("params", FieldType::Json),
        FieldDef::optional("returns", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "defaults_to".into(), to: Some("app".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("description".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
