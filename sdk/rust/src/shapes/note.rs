// DO NOT EDIT — generated from platform/ontology/shapes/note.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// Private text content, primarily for the author. Journal entries, PKM notes,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Note {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub is_pinned: Option<bool>,
    pub note_type: Option<String>,
}

pub static NOTE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "note".into(),
    plural: Some("notes".into()),
    description: Some("Private text content, primarily for the author. Journal entries, PKM notes,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("isPinned", FieldType::Boolean),
        FieldDef::optional("noteType", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("noteType".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
