// DO NOT EDIT — generated from platform/ontology/shapes/protocol.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A protocol or technical spec — git, bitcoin, ssh, smtp, oauth, etc.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Protocol {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub homepage: Option<String>,
    pub rfc: Option<String>,
    pub wikidata_id: Option<String>,
}

pub static PROTOCOL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "protocol".into(),
    plural: Some("protocols".into()),
    description: Some("A protocol or technical spec — git, bitcoin, ssh, smtp, oauth, etc.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("homepage", FieldType::Url),
        FieldDef::optional("rfc", FieldType::String),
        FieldDef::optional("wikidataId", FieldType::String),
    ],
    identity: vec!["name".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
