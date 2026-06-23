// DO NOT EDIT — generated from platform/ontology/shapes/symbol.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A symbol — one named thing in the contract surface: an MCP tool/op, or an
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
    description: Some("A symbol — one named thing in the contract surface: an MCP tool/op, or an".into()),
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
    prior_art: vec![
        PriorArtDef { source: "Language Server Protocol — DocumentSymbol / SymbolKind".into(), url: Some("https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentSymbol".into()), notes: Some("SymbolKind (Function/Struct/Interface/Method/Module…) is the canonical `kind` enum; DocumentSymbol's name + detail + range → our name + signature + sourcePath/sourceLine.".into()) },
        PriorArtDef { source: "LSIF — Language Server Index Format".into(), url: Some("https://microsoft.github.io/language-server-protocol/specifications/lsif/0.6.0/specification/".into()), notes: Some("LSIF persists hover/definition/references as a graph of monikers across files — exactly our `urn` + calls/called_by trail, made queryable.".into()) },
        PriorArtDef { source: "schema.org/SoftwareSourceCode + ctags".into(), url: Some("https://schema.org/SoftwareSourceCode".into()), notes: Some("codeRepository/programmingLanguage → lang; ctags' (tag, file, kind) triple is the minimal symbol-index prior art for sourcePath + kind.".into()) },
    ],
    ..ShapeDef::default()
});
