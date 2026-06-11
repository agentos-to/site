// DO NOT EDIT — generated from platform/ontology/shapes/activity.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An immutable change event — a graph mutation, skill run, search, or load.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Activity {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub action: Option<String>,
    pub all_day: Option<bool>,
    pub changed_keys: Option<Vec<String>>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub duration: Option<f64>,
    pub end_date: Option<String>,
    pub ical_uid: Option<String>,
    pub properties: Option<serde_json::Value>,
    pub recurrence: Option<Vec<String>>,
    pub show_as: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub success: Option<bool>,
    pub timezone: Option<String>,
    pub tool_name: Option<String>,
    pub visibility: Option<String>,
}

pub static ACTIVITY: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "activity".into(),
    plural: Some("activities".into()),
    description: Some("An immutable change event — a graph mutation, skill run, search, or load.".into()),
    icon: Some("activity".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("action", FieldType::String),
        FieldDef::optional("allDay", FieldType::Boolean),
        FieldDef::optional("changedKeys", FieldType::StringList),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("duration", FieldType::Number),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("success", FieldType::Boolean),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("toolName", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "in".into(), to: Some("mcp_session".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "filed_in".into(), to: Some("list".into()), from: None, card: Cardinality::One },
    ],
    also: vec!["event".into()],
    display: Some(DisplaySpec {
        subtitle: Some("action".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
