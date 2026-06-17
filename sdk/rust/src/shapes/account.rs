// DO NOT EDIT — generated from platform/ontology/shapes/account.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A user's presence within a namespace — their GitHub handle, Gmail address,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Account {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub account_type: Option<String>,
    pub bio: Option<String>,
    pub color: Option<String>,
    pub display: Option<String>,
    pub display_name: Option<String>,
    pub email: Option<String>,
    pub handle: Option<String>,
    pub identifier: String,
    pub is_active: Option<bool>,
    pub issuer: Option<String>,
    pub joined_date: Option<String>,
    pub last_active: Option<String>,
    pub last_profile_fetch: Option<String>,
    pub metadata: Option<serde_json::Value>,
    pub phone: Option<String>,
    pub user_id: Option<String>,
}

pub static ACCOUNT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "account".into(),
    plural: Some("accounts".into()),
    description: Some("A user's presence within a namespace — their GitHub handle, Gmail address,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("accountType", FieldType::String),
        FieldDef::optional("bio", FieldType::Text),
        FieldDef::optional("color", FieldType::String),
        FieldDef::optional("display", FieldType::String),
        FieldDef::optional("displayName", FieldType::String),
        FieldDef::optional("email", FieldType::String),
        FieldDef::optional("handle", FieldType::String),
        FieldDef::required("identifier", FieldType::String),
        FieldDef::optional("isActive", FieldType::Boolean),
        FieldDef::optional("issuer", FieldType::String),
        FieldDef::optional("joinedDate", FieldType::Datetime),
        FieldDef::optional("lastActive", FieldType::Datetime),
        FieldDef::optional("lastProfileFetch", FieldType::Datetime),
        FieldDef::optional("metadata", FieldType::Json),
        FieldDef::optional("phone", FieldType::String),
        FieldDef::optional("userId", FieldType::String),
    ],
    identity: vec!["at".into(), "identifier".into()],
    display: Some(DisplaySpec {
        subtitle: Some("identifier".into()),
        ..DisplaySpec::default()
    }),
    groups: vec![
        FieldGroupDef { name: "Identity".into(), fields: vec!["identifier".into(), "handle".into(), "displayName".into(), "email".into(), "phone".into()] },
        FieldGroupDef { name: "Profile".into(), fields: vec!["bio".into(), "accountType".into(), "color".into(), "isActive".into()] },
        FieldGroupDef { name: "Activity".into(), fields: vec!["joinedDate".into(), "lastActive".into(), "lastProfileFetch".into()] },
        FieldGroupDef { name: "Technical".into(), fields: vec!["userId".into(), "issuer".into(), "metadata".into()] },
    ],
    prior_art: vec![
        PriorArtDef { source: "ActivityPub Actor model".into(), url: Some("https://www.w3.org/TR/activitypub/".into()), notes: Some("Account id is a URL; Server/Application/Operator are separate Actor objects. We adopt the same separation but ground each in graph nodes rather than URLs, so node lifecycle (rebrand, merge) propagates to all referencing accounts.".into()) },
        PriorArtDef { source: "schema.org Offer.seller union".into(), url: Some("https://schema.org/Offer".into()), notes: Some("seller: Person | Organization. The `actor` shape (which `at` and `operator` target) is our existing union of person/org/agent — same pattern.".into()) },
        PriorArtDef { source: "OpenID Connect Core 1.0 (`iss`/`sub`)".into(), url: Some("https://openid.net/specs/openid-connect-core-1_0.html".into()), notes: Some("OIDC keeps issuer as opaque URL because there's no shared graph across token issuers. We have a graph; we replace the URL with a graph node, gaining mutability and traversal at the cost of requiring a node to exist before an account can reference it. Trade is worth it.".into()) },
        PriorArtDef { source: "WebFinger (RFC 7033)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc7033".into()), notes: Some("Resolves issuer+identifier pairs to profile metadata. Our identifier aligns with WebFinger's acct: URI scheme (user@host), but the `host` part becomes a graph node (not a string).".into()) },
        PriorArtDef { source: "vCard 4.0 (RFC 6350)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc6350".into()), notes: Some("Defines displayName/email/phone/org in contact cards. We adopt vCard's contact semantics for the human-readable fields.".into()) },
    ],
    ..ShapeDef::default()
});
