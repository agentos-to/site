// DO NOT EDIT — generated from platform/ontology/shapes/project.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A project that groups tasks. Tasks belong to projects.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Project {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub color: Option<String>,
    pub parent_id: Option<String>,
    pub state: Option<String>,
}

pub static PROJECT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "project".into(),
    plural: Some("projects".into()),
    description: Some("A project that groups tasks. Tasks belong to projects.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("color", FieldType::String),
        FieldDef::optional("parentId", FieldType::String),
        FieldDef::optional("state", FieldType::String),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("state".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
