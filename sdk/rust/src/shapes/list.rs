// DO NOT EDIT — generated from platform/ontology/shapes/list.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A list — the universal ordered (or not) collection. Folders, menus,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct List {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub arrangement: Option<String>,
    #[serde(rename = "default_view")]
    pub default_view: Option<String>,
    #[serde(rename = "icon_size")]
    pub icon_size: Option<i64>,
    pub is_default: Option<bool>,
    pub is_public: Option<bool>,
    pub item_count: Option<i64>,
    pub list_id: Option<String>,
    pub list_type: Option<String>,
    #[serde(rename = "member_shape")]
    pub member_shape: Option<String>,
    #[serde(rename = "ordering_mode")]
    pub ordering_mode: Option<String>,
    pub path: Option<String>,
    pub privacy: Option<String>,
    #[serde(rename = "sort_by")]
    pub sort_by: Option<String>,
}

pub static LIST: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "list".into(),
    plural: Some("lists".into()),
    description: Some("A list — the universal ordered (or not) collection. Folders, menus,".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("arrangement", FieldType::String),
        FieldDef::optional("default_view", FieldType::String),
        FieldDef::optional("icon_size", FieldType::Integer),
        FieldDef::optional("isDefault", FieldType::Boolean),
        FieldDef::optional("isPublic", FieldType::Boolean),
        FieldDef::optional("itemCount", FieldType::Integer),
        FieldDef::optional("listId", FieldType::String),
        FieldDef::optional("listType", FieldType::String),
        FieldDef::optional("member_shape", FieldType::String),
        FieldDef::optional("ordering_mode", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("privacy", FieldType::String),
        FieldDef::optional("sort_by", FieldType::String),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
