// DO NOT EDIT — generated from platform/ontology/shapes/calendar.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A calendar — container for events.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Calendar {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub access_role: Option<String>,
    pub background_color: Option<String>,
    pub calendar_id: String,
    pub color: Option<String>,
    pub foreground_color: Option<String>,
    pub is_primary: Option<bool>,
    pub is_readonly: Option<bool>,
    pub source: Option<String>,
    pub timezone: Option<String>,
}

pub static CALENDAR: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "calendar".into(),
    plural: Some("calendars".into()),
    description: Some("A calendar — container for events.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("accessRole", FieldType::String),
        FieldDef::optional("backgroundColor", FieldType::String),
        FieldDef::required("calendarId", FieldType::String),
        FieldDef::optional("color", FieldType::String),
        FieldDef::optional("foregroundColor", FieldType::String),
        FieldDef::optional("isPrimary", FieldType::Boolean),
        FieldDef::optional("isReadonly", FieldType::Boolean),
        FieldDef::optional("source", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "at_namespace".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "owned_by".into(), to: Some("person".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "schedules".into(), to: Some("event".into()), from: None, card: Cardinality::Many },
    ],
    identity: vec!["at".into(), "calendarId".into()],
    display: Some(DisplaySpec {
        subtitle: Some("source".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
