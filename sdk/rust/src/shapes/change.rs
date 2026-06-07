// DO NOT EDIT — generated from platform/ontology/shapes/change.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A delta on something — a file born/modified/removed, a document revision,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Change {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub kind: Option<String>,
    pub path: Option<String>,
    pub phase: Option<String>,
    pub status: Option<String>,
    pub summary: Option<String>,
    pub version: Option<String>,
}

pub static CHANGE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "change".into(),
    plural: Some("changes".into()),
    description: Some("A delta on something — a file born/modified/removed, a document revision,".into()),
    icon: Some("file-diff".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("phase", FieldType::String),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("summary", FieldType::Text),
        FieldDef::optional("version", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("kind".into()),
        body: Some("summary".into()),
        highlights: vec!["status".into(), "phase".into(), "path".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
