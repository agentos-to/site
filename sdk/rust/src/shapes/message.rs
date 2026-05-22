// DO NOT EDIT — generated from platform/ontology/shapes/message.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A single message in a conversation. Base type — email extends this via `also`.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Message {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub conversation_id: Option<String>,
    pub is_outgoing: Option<bool>,
    pub is_starred: Option<bool>,
}

pub static MESSAGE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "message".into(),
    plural: Some("messages".into()),
    description: Some("A single message in a conversation. Base type — email extends this via `also`.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("conversationId", FieldType::String),
        FieldDef::optional("isOutgoing", FieldType::Boolean),
        FieldDef::optional("isStarred", FieldType::Boolean),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("from".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
