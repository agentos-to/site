// DO NOT EDIT — generated from platform/ontology/shapes/grant.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A permission to broker a call — caller × service × account × shapes.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Grant {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub account: String,
    pub caller: String,
    pub decided_at: Option<String>,
    pub requested_at: Option<String>,
    pub service: String,
    pub shapes: Option<Vec<String>>,
    pub shapes_key: String,
    pub status: Option<String>,
}

pub static GRANT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "grant".into(),
    plural: Some("grants".into()),
    description: Some("A permission to broker a call — caller × service × account × shapes.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::required("account", FieldType::String),
        FieldDef::required("caller", FieldType::String),
        FieldDef::optional("decidedAt", FieldType::Datetime),
        FieldDef::optional("requestedAt", FieldType::Datetime),
        FieldDef::required("service", FieldType::String),
        FieldDef::optional("shapes", FieldType::StringList),
        FieldDef::required("shapesKey", FieldType::String),
        FieldDef::optional("status", FieldType::String),
    ],
    identity: vec!["caller".into(), "service".into(), "account".into(), "shapesKey".into()],
    display: Some(DisplaySpec {
        subtitle: Some("status".into()),
        ..DisplaySpec::default()
    }),
    groups: vec![
        FieldGroupDef { name: "Scope".into(), fields: vec!["caller".into(), "service".into(), "account".into(), "shapes".into()] },
        FieldGroupDef { name: "Status".into(), fields: vec!["status".into(), "requestedAt".into(), "decidedAt".into()] },
    ],
    prior_art: vec![
        PriorArtDef { source: "OAuth 2.0 Device Authorization Grant (RFC 8628)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc8628".into()), notes: Some("Human consent is asynchronous: the client gets a structured \"go get approval\" signal, polls/retries after the human acts. NEEDS_GRANT + grants.request/approve mirrors that — the grant node is the durable consent record, not a side-channel dialog.".into()) },
        PriorArtDef { source: "Delegated Agent Authorization Protocol (DAAP)".into(), url: Some("https://datatracker.ietf.org/doc/html/draft-mishra-oauth-agent-grants-00".into()), notes: Some("Agent grants as first-class objects with approve/deny and an audit trail — same pending|approved|denied lifecycle; we keep the axes local (caller × service × account × shapes) instead of issuing a bearer token.".into()) },
        PriorArtDef { source: "Android runtime permissions / iOS TCC prompts".into(), url: Some("https://developer.android.com/guide/topics/permissions/overview".into()), notes: Some("Capability access fails closed until the human grants; the denial carries enough structure to re-request. Host OS TCC is a different principal (engine vs app) — see engine-capabilities.".into()) },
    ],
    ..ShapeDef::default()
});
