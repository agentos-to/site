// DO NOT EDIT — generated from platform/ontology/shapes/health-observation.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A single measured health value at a point in time — "LDL = 95 mg/dL on
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct HealthObservation {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub all_day: Option<bool>,
    pub community: Option<String>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub external_url: Option<String>,
    pub flag: Option<String>,
    pub ical_uid: Option<String>,
    pub indexed_at: Option<String>,
    pub notes: Option<String>,
    pub post_id: Option<String>,
    pub properties: Option<serde_json::Value>,
    pub recurrence: Option<Vec<String>>,
    pub ref_high: Option<f64>,
    pub ref_low: Option<f64>,
    pub ref_text: Option<String>,
    pub result_type: Option<String>,
    pub score: Option<i64>,
    pub show_as: Option<String>,
    pub similarity: Option<f64>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub timezone: Option<String>,
    pub value: Option<f64>,
    pub value_text: Option<String>,
    pub visibility: Option<String>,
}

pub static HEALTH_OBSERVATION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "health-observation".into(),
    plural: Some("health-observations".into()),
    description: Some("A single measured health value at a point in time — \"LDL = 95 mg/dL on".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("allDay", FieldType::Boolean),
        FieldDef::optional("community", FieldType::String),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("externalUrl", FieldType::Url),
        FieldDef::optional("flag", FieldType::String),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("indexedAt", FieldType::Datetime),
        FieldDef::optional("notes", FieldType::Text),
        FieldDef::optional("postId", FieldType::String),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("refHigh", FieldType::Number),
        FieldDef::optional("refLow", FieldType::Number),
        FieldDef::optional("refText", FieldType::String),
        FieldDef::optional("resultType", FieldType::String),
        FieldDef::optional("score", FieldType::Integer),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("similarity", FieldType::Number),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("value", FieldType::Number),
        FieldDef::optional("valueText", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    also: vec!["result".into(), "event".into()],
    display: Some(DisplaySpec {
        subtitle: Some("startDate".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
