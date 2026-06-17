// DO NOT EDIT — generated from platform/ontology/shapes/credential.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A credential held by AgentOS — the graph descriptor that mirrors one
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Credential {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub domain: String,
    pub identifier: String,
    pub item_type: String,
    pub last_verified: Option<String>,
    pub obtained_at: Option<String>,
    pub refreshable: Option<bool>,
    pub source: Option<String>,
    pub store_row_id: Option<i64>,
}

pub static CREDENTIAL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "credential".into(),
    plural: Some("credentials".into()),
    description: Some("A credential held by AgentOS — the graph descriptor that mirrors one".into()),
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
        FieldDef::required("identifier", FieldType::String),
        FieldDef::required("itemType", FieldType::String),
        FieldDef::optional("lastVerified", FieldType::Datetime),
        FieldDef::optional("obtainedAt", FieldType::Datetime),
        FieldDef::optional("refreshable", FieldType::Boolean),
        FieldDef::optional("source", FieldType::String),
        FieldDef::optional("storeRowId", FieldType::Integer),
    ],
    identity: vec!["domain".into(), "identifier".into(), "itemType".into()],
    display: Some(DisplaySpec {
        subtitle: Some("source".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "OAuth 2.0 Token Introspection (RFC 7662)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc7662".into()), notes: Some("RFC 7662 describes token metadata as a separate addressable resource from the token itself (active, exp, iss, sub, scope). Same split here: descriptor is queryable graph metadata, encrypted value is retrieved by a separate call (`auth_store.read` by identifier). Our obtainedAt/expiresAt/lastVerified mirror iat/exp/auth_time.".into()) },
        PriorArtDef { source: "FIDO Metadata Service (MDS3)".into(), url: Some("https://fidoalliance.org/metadata/".into()), notes: Some("FIDO separates authenticator metadata from the authenticator itself — metadata is queryable, the cryptographic material is not. Mirrors our descriptor/vault split.".into()) },
        PriorArtDef { source: "macOS Keychain SecItem attributes".into(), url: Some("https://developer.apple.com/documentation/security/keychain_services/keychain_items/item_attribute_keys_and_values".into()), notes: Some("Keychain separates `kSecAttr*` (metadata — server, account, creation/modification dates) from `kSecValueData` (the secret). Attributes are queryable without decrypting the value. Our fields map: kSecAttrServer → domain, kSecAttrAccount → identifier, kSecAttrCreationDate → obtainedAt, kSecAttrModificationDate → lastVerified.".into()) },
        PriorArtDef { source: "schema.org/DigitalDocument (WebAuthn credentials stored as)".into(), url: Some("https://schema.org/DigitalDocument".into()), notes: Some("Weak alignment — schema.org has no native credential type. Cited only to note that existing web ontologies deliberately stop short of secret material; descriptor-only is the established pattern.".into()) },
    ],
    ..ShapeDef::default()
});
