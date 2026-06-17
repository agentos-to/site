// DO NOT EDIT — generated from platform/ontology/shapes/website.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A published website (not a single page — see webpage for that).
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Website {
    pub name: String,
    pub text: Option<String>,
    pub url: String,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub anonymous: Option<bool>,
    pub claim_token: Option<String>,
    pub claim_url: Option<String>,
    pub status: Option<String>,
    pub version_id: Option<String>,
}

pub static WEBSITE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "website".into(),
    plural: Some("websites".into()),
    description: Some("A published website (not a single page — see webpage for that).".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::required("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("anonymous", FieldType::Boolean),
        FieldDef::optional("claimToken", FieldType::String),
        FieldDef::optional("claimUrl", FieldType::Url),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("versionId", FieldType::String),
    ],
    identity: vec!["url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("url".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/WebSite".into(), url: Some("https://schema.org/WebSite".into()), notes: Some("Our url-as-identity matches; ownedBy ≈ publisher; domain relation ≈ url host.".into()) },
        PriorArtDef { source: "WHOIS (RFC 3912)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc3912".into()), notes: Some("Our expiresAt/domain source from WHOIS records; claimToken has no direct WHOIS peer (HERE.NOW-specific).".into()) },
        PriorArtDef { source: "RFC 7033 WebFinger (host-meta)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc7033".into()), notes: Some("Website metadata discovery. Our claimUrl parallels /.well-known/host-meta patterns.".into()) },
    ],
    ..ShapeDef::default()
});
