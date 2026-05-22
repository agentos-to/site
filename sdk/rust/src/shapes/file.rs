// DO NOT EDIT — generated from platform/ontology/shapes/file.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A file — source code, attachment, download, or any discrete digital artifact.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct File {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub encoding: Option<String>,
    pub filename: Option<String>,
    pub format: Option<String>,
    pub kind: Option<String>,
    pub line_count: Option<i64>,
    pub mime_type: Option<String>,
    pub path: Option<String>,
    pub sha: Option<String>,
    pub size: Option<i64>,
}

pub static FILE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "file".into(),
    plural: Some("files".into()),
    description: Some("A file — source code, attachment, download, or any discrete digital artifact.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("encoding", FieldType::String),
        FieldDef::optional("filename", FieldType::String),
        FieldDef::optional("format", FieldType::String),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("lineCount", FieldType::Integer),
        FieldDef::optional("mimeType", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("sha", FieldType::String),
        FieldDef::optional("size", FieldType::Integer),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("path".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
