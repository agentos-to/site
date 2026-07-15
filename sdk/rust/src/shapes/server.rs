// DO NOT EDIT — generated from platform/ontology/shapes/server.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A remote host / administrative endpoint — the connection record a
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Server {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub database: Option<String>,
    pub hostname: String,
    pub path: Option<String>,
    pub port: Option<i64>,
    pub protocol: String,
    pub secret_ref: Option<String>,
    pub username: String,
}

pub static SERVER: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "server".into(),
    plural: Some("servers".into()),
    description: Some("A remote host / administrative endpoint — the connection record a".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("database", FieldType::String),
        FieldDef::required("hostname", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("port", FieldType::Integer),
        FieldDef::required("protocol", FieldType::String),
        FieldDef::optional("secretRef", FieldType::String),
        FieldDef::required("username", FieldType::String),
    ],
    identity: vec!["hostname".into(), "protocol".into(), "username".into()],
    display: Some(DisplaySpec {
        subtitle: Some("hostname".into()),
        highlights: vec!["protocol".into(), "hostname".into(), "username".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "1Password \"Server\" item category".into(), url: Some("https://support.1password.com/item-categories/".into()), notes: Some("The direct source. 1P's Server item holds URL/hostname, username, password, and admin console fields. We keep hostname + username as graph face data and route the password/key into secrets (secretRef only), matching how 1P scopes the concealed fields.".into()) },
        PriorArtDef { source: "OpenSSH ssh_config / RFC 4251".into(), url: Some("https://man.openbsd.org/ssh_config".into()), notes: Some("HostName / Port / User are exactly our hostname / port / username; IdentityFile (the private key) is the secret we sideband. protocol generalizes ssh_config to the other admin transports (rdp, sftp, smb).".into()) },
        PriorArtDef { source: "RFC 3986 URI authority (scheme://user@host:port/path)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc3986#section-3".into()), notes: Some("Our protocol/username/hostname/port/path decompose the URI authority + path components. We keep them as separate fields (not a single URL string) so identity keys and connection tooling can read them without re-parsing, and so the userinfo secret never lands in a stored URL.".into()) },
    ],
    ..ShapeDef::default()
});
