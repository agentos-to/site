// DO NOT EDIT — generated from platform/ontology/shapes/tag.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A tag or label — Gmail label, Todoist label, GitHub label, git tag,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Tag {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub annotated: Option<bool>,
    pub color: Option<String>,
    pub hash: Option<String>,
    pub tag_type: Option<String>,
}

pub static TAG: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "tag".into(),
    plural: Some("tags".into()),
    description: Some("A tag or label — Gmail label, Todoist label, GitHub label, git tag,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("annotated", FieldType::Boolean),
        FieldDef::optional("color", FieldType::String),
        FieldDef::optional("hash", FieldType::String),
        FieldDef::optional("tagType", FieldType::String),
    ],
    identity: vec!["name".into()],
    display: Some(DisplaySpec {
        title: Some("name".into()),
        subtitle: Some("tagType".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
