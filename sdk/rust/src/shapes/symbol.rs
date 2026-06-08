// DO NOT EDIT — generated from platform/ontology/shapes/symbol.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A code symbol — one named thing in a source surface: an MCP tool/op, a
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Symbol {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub kind: Option<String>,
    pub lang: Option<String>,
    pub signature: Option<String>,
    pub source_line: Option<i64>,
    pub source_path: Option<String>,
    pub summary: Option<String>,
    pub urn: Option<String>,
}

pub static SYMBOL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "symbol".into(),
    plural: Some("symbols".into()),
    description: Some("A code symbol — one named thing in a source surface: an MCP tool/op, a".into()),
    icon: Some("code".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("lang", FieldType::String),
        FieldDef::optional("signature", FieldType::Text),
        FieldDef::optional("sourceLine", FieldType::Integer),
        FieldDef::optional("sourcePath", FieldType::String),
        FieldDef::optional("summary", FieldType::Text),
        FieldDef::optional("urn", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("signature".into()),
        body: Some("summary".into()),
        highlights: vec!["kind".into(), "lang".into(), "sourcePath".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
