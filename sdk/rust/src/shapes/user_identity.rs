// DO NOT EDIT — generated from platform/ontology/shapes/user_identity.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An identity claim — "the engine-level user X identifies as person:Y
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct UserIdentity {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub active: Option<bool>,
    #[serde(rename = "person_node_id")]
    pub person_node_id: Option<String>,
    #[serde(rename = "user_id")]
    pub user_id: Option<String>,
    #[serde(rename = "volume_id")]
    pub volume_id: Option<String>,
}

pub static USER_IDENTITY: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "user_identity".into(),
    plural: Some("user_identities".into()),
    description: Some("An identity claim — \"the engine-level user X identifies as person:Y".into()),
    icon: Some("user".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("active", FieldType::Boolean),
        FieldDef::optional("person_node_id", FieldType::String),
        FieldDef::optional("user_id", FieldType::String),
        FieldDef::optional("volume_id", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("volume_id".into()),
        highlights: vec!["person_node_id".into(), "active".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Solid (Tim Berners-Lee)".into(), url: Some("https://solidproject.org/faq".into()), notes: Some("Solid Pod ↔ WebID is the per-user identity model. A Solid user owns one personal pod whose WebID is the authoritative identity; cross-pod identity is a single relation. We split: User is engine state; Person is graph content; user_identity is the explicit bridge that can be many-to-many across volumes.".into()) },
        PriorArtDef { source: "Unix/macOS — /etc/passwd vs /Users/<u>".into(), url: Some("https://en.wikipedia.org/wiki/Passwd".into()), notes: Some("OS users (engine.db::users) and home directories (~/.agentos/users/<u>.db) follow the Unix convention. The identity *within* the home is content the home owns.".into()) },
    ],
    ..ShapeDef::default()
});
