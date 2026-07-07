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
    pub account_email: Option<String>,
    pub conversation_id: Option<String>,
    pub is_group: Option<bool>,
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
        FieldDef::optional("accountEmail", FieldType::String),
        FieldDef::optional("conversationId", FieldType::String),
        FieldDef::optional("isGroup", FieldType::Boolean),
        FieldDef::optional("isOutgoing", FieldType::Boolean),
        FieldDef::optional("isStarred", FieldType::Boolean),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("from".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "ActivityStreams 2.0 Note/Activity".into(), url: Some("https://www.w3.org/TR/activitystreams-vocabulary/#dfn-note".into()), notes: Some("Closest open standard for generic messages. Our from ≈ actor; inConversation ≈ context/conversation; repliesTo ≈ inReplyTo.".into()) },
        PriorArtDef { source: "Matrix m.room.message".into(), url: Some("https://spec.matrix.org/latest/client-server-api/#mroommessage".into()), notes: Some("Practical cross-platform message event schema. Our isOutgoing has no Matrix analog (sender identity instead); repliesTo ≈ m.relates_to rel_type m.thread/m.in_reply_to.".into()) },
        PriorArtDef { source: "XMPP (RFC 6121) message stanza".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc6121".into()), notes: Some("IETF instant-messaging baseline. from/to/thread correspond to our from/inConversation; no standardized isStarred.".into()) },
    ],
    ..ShapeDef::default()
});
