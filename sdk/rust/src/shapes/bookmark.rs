// DO NOT EDIT — generated from platform/ontology/shapes/bookmark.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A pointer into the graph — the universal shortcut. A bookmark is a
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Bookmark {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub handle: Option<String>,
}

pub static BOOKMARK: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "bookmark".into(),
    plural: Some("bookmarks".into()),
    description: Some("A pointer into the graph — the universal shortcut. A bookmark is a".into()),
    icon: Some("🔖".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("handle", FieldType::String),
    ],
    identity: vec!["points_to".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
