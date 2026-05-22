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
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("text".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
