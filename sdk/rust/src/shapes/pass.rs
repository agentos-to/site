// DO NOT EDIT — generated from platform/ontology/shapes/pass.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A fixed-quantity right-of-access — a bundle of entries, a multi-day
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Pass {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub all_day: Option<bool>,
    pub boarding_group: Option<String>,
    pub checkin_status: Option<String>,
    pub currency: Option<String>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub gate: Option<String>,
    pub ical_uid: Option<String>,
    pub is_all_day_pass: Option<bool>,
    pub name_on_ticket: Option<String>,
    pub price: Option<f64>,
    pub properties: Option<serde_json::Value>,
    pub purchased_quantity: Option<i64>,
    pub quantity: Option<i64>,
    pub recurrence: Option<Vec<String>>,
    pub seat_assignment: Option<String>,
    pub show_as: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub terminal: Option<String>,
    pub ticket_class: Option<String>,
    pub ticket_number: Option<String>,
    pub timezone: Option<String>,
    pub use_count: Option<i64>,
    pub visibility: Option<String>,
}

pub static PASS: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "pass".into(),
    plural: Some("passes".into()),
    description: Some("A fixed-quantity right-of-access — a bundle of entries, a multi-day".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("allDay", FieldType::Boolean),
        FieldDef::optional("boardingGroup", FieldType::String),
        FieldDef::optional("checkinStatus", FieldType::String),
        FieldDef::optional("currency", FieldType::String),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("gate", FieldType::String),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("isAllDayPass", FieldType::Boolean),
        FieldDef::optional("nameOnTicket", FieldType::String),
        FieldDef::optional("price", FieldType::Number),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("purchasedQuantity", FieldType::Integer),
        FieldDef::optional("quantity", FieldType::Integer),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("seatAssignment", FieldType::String),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("terminal", FieldType::String),
        FieldDef::optional("ticketClass", FieldType::String),
        FieldDef::optional("ticketNumber", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("useCount", FieldType::Integer),
        FieldDef::optional("visibility", FieldType::String),
    ],
    also: vec!["event".into()],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("status".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
