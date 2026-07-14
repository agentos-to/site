// DO NOT EDIT — generated from platform/ontology/shapes/activity.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An immutable change event — a graph mutation or shell window op.
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
    pub caller: Option<String>,
    pub changed_keys: Option<Vec<String>>,
    pub created: Option<i64>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub deleted: Option<i64>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub ical_uid: Option<String>,
    pub properties: Option<serde_json::Value>,
    pub record: Option<serde_json::Value>,
    pub recurrence: Option<Vec<String>>,
    pub show_as: Option<String>,
    pub source: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub target_shape: Option<String>,
    pub target_volume: Option<String>,
    pub timezone: Option<String>,
    pub updated: Option<i64>,
    pub visibility: Option<String>,
}

pub static ACTIVITY: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "activity".into(),
    plural: Some("activities".into()),
    description: Some("An immutable change event — a graph mutation or shell window op.".into()),
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
        FieldDef::optional("caller", FieldType::String),
        FieldDef::optional("changedKeys", FieldType::StringList),
        FieldDef::optional("created", FieldType::Integer),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("deleted", FieldType::Integer),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("record", FieldType::Json),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("source", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("targetShape", FieldType::String),
        FieldDef::optional("targetVolume", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("updated", FieldType::Integer),
        FieldDef::optional("visibility", FieldType::String),
    ],
    also: vec!["event".into()],
    display: Some(DisplaySpec {
        subtitle: Some("action".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "ActivityStreams 2.0".into(), url: Some("https://www.w3.org/TR/activitystreams-core/".into()), notes: Some("AS2's Create/Update/Delete activities match our action values. We diverge by tracking changedKeys explicitly instead of encoding full object replacement.".into()) },
    ],
    ..ShapeDef::default()
});
