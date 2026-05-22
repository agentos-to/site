// DO NOT EDIT — generated from platform/ontology/shapes/dns_record.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A DNS record for a domain. One domain has many records (A, CNAME, MX, TXT, etc.).
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct DnsRecord {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub domain: String,
    pub priority: Option<i64>,
    pub record_id: Option<String>,
    pub record_name: String,
    pub record_type: String,
    pub ttl: Option<i64>,
    pub type_: Option<String>,
    pub values: Option<Vec<String>>,
}

pub static DNS_RECORD: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "dns_record".into(),
    plural: Some("dns_records".into()),
    description: Some("A DNS record for a domain. One domain has many records (A, CNAME, MX, TXT, etc.).".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::required("domain", FieldType::String),
        FieldDef::optional("priority", FieldType::Integer),
        FieldDef::optional("recordId", FieldType::String),
        FieldDef::required("recordName", FieldType::String),
        FieldDef::required("recordType", FieldType::String),
        FieldDef::optional("ttl", FieldType::Integer),
        FieldDef::optional("type", FieldType::String),
        FieldDef::optional("values", FieldType::StringList),
    ],
    identity: vec!["domain".into(), "recordType".into(), "recordName".into()],
    display: Some(DisplaySpec {
        subtitle: Some("recordType".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
