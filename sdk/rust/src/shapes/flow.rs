// DO NOT EDIT — generated from platform/ontology/shapes/flow.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A process / swim-lane — actors across ordered steps. The universal shape
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Flow {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub goal: Option<String>,
    pub status: Option<String>,
    pub trigger: Option<String>,
}

pub static FLOW: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "flow".into(),
    plural: Some("flows".into()),
    description: Some("A process / swim-lane — actors across ordered steps. The universal shape".into()),
    icon: Some("workflow".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("goal", FieldType::Text),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("trigger", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("goal".into()),
        highlights: vec!["trigger".into(), "status".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
