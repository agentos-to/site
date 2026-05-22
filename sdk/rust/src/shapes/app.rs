// DO NOT EDIT — generated from platform/ontology/shapes/app.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An application — something the shell can spawn as a window. Includes
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct App {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub default_view: Option<String>,
    pub handles: Option<Vec<String>>,
    pub icon_role: Option<String>,
    pub is_system: Option<bool>,
    pub route: Option<String>,
}

pub static APP: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "app".into(),
    plural: Some("apps".into()),
    description: Some("An application — something the shell can spawn as a window. Includes".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("defaultView", FieldType::String),
        FieldDef::optional("handles", FieldType::StringList),
        FieldDef::optional("iconRole", FieldType::String),
        FieldDef::optional("isSystem", FieldType::Boolean),
        FieldDef::optional("route", FieldType::String),
    ],
    identity: vec!["id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
