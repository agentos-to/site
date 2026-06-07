// DO NOT EDIT — generated from platform/ontology/shapes/step.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// One ordered act within a flow. A first-class node, not an array slot:
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Step {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub detail: Option<String>,
    pub position: Option<i64>,
    pub status: Option<String>,
}

pub static STEP: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "step".into(),
    plural: Some("steps".into()),
    description: Some("One ordered act within a flow. A first-class node, not an array slot:".into()),
    icon: Some("list-ordered".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("detail", FieldType::Text),
        FieldDef::optional("position", FieldType::Integer),
        FieldDef::optional("status", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("status".into()),
        body: Some("detail".into()),
        highlights: vec!["position".into(), "status".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
