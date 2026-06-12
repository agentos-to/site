// DO NOT EDIT — generated from platform/ontology/shapes/conversation.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A message thread — an iMessage chat, WhatsApp group, email thread, Claude
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Conversation {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub account_email: Option<String>,
    pub cwd: Option<String>,
    pub git_branch: Option<String>,
    pub history_id: Option<String>,
    pub is_archived: Option<bool>,
    pub is_group: Option<bool>,
    pub message_count: Option<i64>,
    pub source: Option<String>,
    pub unread_count: Option<i64>,
}

pub static CONVERSATION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "conversation".into(),
    plural: Some("conversations".into()),
    description: Some("A message thread — an iMessage chat, WhatsApp group, email thread, Claude".into()),
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
        FieldDef::optional("cwd", FieldType::String),
        FieldDef::optional("gitBranch", FieldType::String),
        FieldDef::optional("historyId", FieldType::String),
        FieldDef::optional("isArchived", FieldType::Boolean),
        FieldDef::optional("isGroup", FieldType::Boolean),
        FieldDef::optional("messageCount", FieldType::Integer),
        FieldDef::optional("source", FieldType::String),
        FieldDef::optional("unreadCount", FieldType::Integer),
    ],
    out: vec![
        EdgeDef { label: "at_namespace".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "contains".into(), to: Some("message".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "in".into(), to: Some("list".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("text".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "ActivityStreams 2.0 context/inReplyTo".into(), url: Some("https://www.w3.org/TR/activitystreams-vocabulary/#dfn-context".into()), notes: Some("Conversations are AS2 contexts — the thread that groups replies. Our participant[] ≈ to/cc/audience.".into()) },
        PriorArtDef { source: "Matrix Room (m.room)".into(), url: Some("https://spec.matrix.org/latest/client-server-api/#room-events".into()), notes: Some("Practical thread model. Our isGroup ≈ room.join_rules; unreadCount ≈ unread_notifications.highlight_count.".into()) },
        PriorArtDef { source: "Gmail API — Thread resource".into(), url: Some("https://developers.google.com/gmail/api/reference/rest/v1/users.threads".into()), notes: Some("Our messageCount ≈ messages.length; unreadCount derived from UNREAD labels on Thread messages.".into()) },
    ],
    ..ShapeDef::default()
});
