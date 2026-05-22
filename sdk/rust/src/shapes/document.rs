// DO NOT EDIT — generated from platform/ontology/shapes/document.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A document — any human-readable text content with structure and authorship.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Document {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub abstract_: Option<String>,
    pub content_type: Option<String>,
    pub encoding: Option<String>,
    pub filename: Option<String>,
    pub format: Option<String>,
    pub kind: Option<String>,
    pub language: Option<String>,
    pub line_count: Option<i64>,
    pub mime_type: Option<String>,
    pub path: Option<String>,
    pub sha: Option<String>,
    pub size: Option<i64>,
    pub table_of_contents: Option<String>,
    pub word_count: Option<i64>,
}

pub static DOCUMENT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "document".into(),
    plural: Some("documents".into()),
    description: Some("A document — any human-readable text content with structure and authorship.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("abstract", FieldType::Text),
        FieldDef::optional("contentType", FieldType::String),
        FieldDef::optional("encoding", FieldType::String),
        FieldDef::optional("filename", FieldType::String),
        FieldDef::optional("format", FieldType::String),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("language", FieldType::String),
        FieldDef::optional("lineCount", FieldType::Integer),
        FieldDef::optional("mimeType", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("sha", FieldType::String),
        FieldDef::optional("size", FieldType::Integer),
        FieldDef::optional("tableOfContents", FieldType::Text),
        FieldDef::optional("wordCount", FieldType::Integer),
    ],
    also: vec!["file".into()],
    display: Some(DisplaySpec {
        subtitle: Some("contentType".into()),
        body: Some("abstract".into()),
        highlights: vec!["datePublished".into(), "author".into(), "wordCount".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
