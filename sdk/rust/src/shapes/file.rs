// DO NOT EDIT — generated from platform/ontology/shapes/file.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

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
    identity_any: vec!["sha".into(), "url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("path".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "IANA Media Types (RFC 6838)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc6838".into()), notes: Some("Our mimeType follows type/subtype syntax (text/plain, application/pdf). Canonical source for format identification.".into()) },
        PriorArtDef { source: "schema.org/DigitalDocument".into(), url: Some("https://schema.org/DigitalDocument".into()), notes: Some("Our filename ≈ name; size ≈ contentSize; mimeType ≈ encodingFormat.".into()) },
        PriorArtDef { source: "Git Internals (blob objects)".into(), url: Some("https://git-scm.com/book/en/v2/Git-Internals-Git-Objects".into()), notes: Some("Our sha is a Git blob SHA-1 (40-hex). Git's content-addressable model underlies our repo-file identity.".into()) },
    ],
    ..ShapeDef::default()
});
