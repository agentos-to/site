// DO NOT EDIT — generated from platform/ontology/shapes/community.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An online community — a subreddit, Facebook group, or similar.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Community {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub allow_crypto: Option<bool>,
    pub member_count: Option<i64>,
    pub privacy: Option<String>,
    pub subscriber_count: Option<i64>,
}

pub static COMMUNITY: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "community".into(),
    plural: Some("communities".into()),
    description: Some("An online community — a subreddit, Facebook group, or similar.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("allowCrypto", FieldType::Boolean),
        FieldDef::optional("memberCount", FieldType::Integer),
        FieldDef::optional("privacy", FieldType::String),
        FieldDef::optional("subscriberCount", FieldType::Integer),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("text".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
