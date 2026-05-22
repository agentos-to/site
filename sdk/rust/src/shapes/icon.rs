// DO NOT EDIT — generated from platform/ontology/shapes/icon.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A small graphic intended for UI use — toolbar buttons, file-type
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Icon {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub component: Option<String>,
    pub copyright_year: Option<i64>,
    pub coverage: Option<String>,
    pub date_created: Option<String>,
    pub description: Option<String>,
    pub dimension: Option<i64>,
    pub format: Option<String>,
    pub language: Option<String>,
    pub license: Option<String>,
    pub purpose: Option<String>,
    pub style: Option<String>,
    pub tags: Option<Vec<String>>,
}

pub static ICON: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "icon".into(),
    plural: Some("icons".into()),
    description: Some("A small graphic intended for UI use — toolbar buttons, file-type".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("component", FieldType::String),
        FieldDef::optional("copyrightYear", FieldType::Integer),
        FieldDef::optional("coverage", FieldType::String),
        FieldDef::optional("dateCreated", FieldType::Date),
        FieldDef::optional("description", FieldType::String),
        FieldDef::optional("dimension", FieldType::Integer),
        FieldDef::optional("format", FieldType::String),
        FieldDef::optional("language", FieldType::String),
        FieldDef::optional("license", FieldType::String),
        FieldDef::optional("purpose", FieldType::String),
        FieldDef::optional("style", FieldType::String),
        FieldDef::optional("tags", FieldType::StringList),
    ],
    also: vec!["creative_work".into()],
    identity_any: vec!["component".into(), "url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("purpose".into()),
        image: Some("image".into()),
        body: Some("description".into()),
        highlights: vec!["datePublished".into(), "published_by".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
