// DO NOT EDIT — generated from platform/ontology/shapes/app.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An application — the one installable, launchable unit. System apps
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct App {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub account: Option<serde_json::Value>,
    pub color: Option<String>,
    pub composition: Option<serde_json::Value>,
    pub default_view: Option<String>,
    pub description: Option<String>,
    pub error: Option<String>,
    pub handles: Option<Vec<String>>,
    pub icon_role: Option<String>,
    pub is_system: Option<bool>,
    pub route: Option<String>,
    pub status: Option<String>,
}

pub static APP: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "app".into(),
    plural: Some("apps".into()),
    description: Some("An application — the one installable, launchable unit. System apps".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("account", FieldType::Json),
        FieldDef::optional("color", FieldType::String),
        FieldDef::optional("composition", FieldType::Json),
        FieldDef::optional("defaultView", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("error", FieldType::Text),
        FieldDef::optional("handles", FieldType::StringList),
        FieldDef::optional("iconRole", FieldType::String),
        FieldDef::optional("isSystem", FieldType::Boolean),
        FieldDef::optional("route", FieldType::String),
        FieldDef::optional("status", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "online_at".into(), to: Some("website".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "privacy_at".into(), to: Some("webpage".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "terms_at".into(), to: Some("webpage".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("description".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
