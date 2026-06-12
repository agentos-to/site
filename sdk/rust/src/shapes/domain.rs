// DO NOT EDIT — generated from platform/ontology/shapes/domain.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A registered domain name. Also auto-created from email sender/recipient addresses.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Domain {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub auto_renew: Option<bool>,
    pub nameservers: Option<Vec<String>>,
    pub registrar: Option<String>,
    pub status: Option<String>,
}

pub static DOMAIN: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "domain".into(),
    plural: Some("domains".into()),
    description: Some("A registered domain name. Also auto-created from email sender/recipient addresses.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("autoRenew", FieldType::Boolean),
        FieldDef::optional("nameservers", FieldType::StringList),
        FieldDef::optional("registrar", FieldType::String),
        FieldDef::optional("status", FieldType::String),
    ],
    identity: vec!["name".into()],
    display: Some(DisplaySpec {
        subtitle: Some("registrar".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "RFC 1035 (Domain Names)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc1035".into()), notes: Some("Canonical domain-name syntax + nameservers + TTL. Our nameservers are NS records for the apex.".into()) },
        PriorArtDef { source: "RFC 3912 (WHOIS)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc3912".into()), notes: Some("Our registrar/status/expiresAt/autoRenew come from WHOIS response fields.".into()) },
    ],
    ..ShapeDef::default()
});
