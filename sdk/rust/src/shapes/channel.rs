// DO NOT EDIT — generated from platform/ontology/shapes/channel.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A content channel — typically a YouTube channel. Videos are uploaded to channels.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Channel {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub banner: Option<String>,
    pub subscriber_count: Option<i64>,
}

pub static CHANNEL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "channel".into(),
    plural: Some("channels".into()),
    description: Some("A content channel — typically a YouTube channel. Videos are uploaded to channels.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("banner", FieldType::Url),
        FieldDef::optional("subscriberCount", FieldType::Integer),
    ],
    out: vec![
        EdgeDef { label: "at_namespace".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("subscriberCount".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
