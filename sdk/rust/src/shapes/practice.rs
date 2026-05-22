// DO NOT EDIT — generated from platform/ontology/shapes/practice.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A field of practice or study — a discipline a person practices, or the
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Practice {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub aliases: Option<Vec<String>>,
    pub code: Option<String>,
    pub code_system: Option<String>,
    pub description: Option<String>,
}

pub static PRACTICE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "practice".into(),
    plural: Some("practices".into()),
    description: Some("A field of practice or study — a discipline a person practices, or the".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("aliases", FieldType::StringList),
        FieldDef::optional("code", FieldType::String),
        FieldDef::optional("codeSystem", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("parent".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
