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
    ..ShapeDef::default()
});
