// DO NOT EDIT — generated from platform/ontology/shapes/event.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// Something that happens — at a time, optionally at a place, involving people.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Event {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub all_day: Option<bool>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub ical_uid: Option<String>,
    pub properties: Option<serde_json::Value>,
    pub recurrence: Option<Vec<String>>,
    pub show_as: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub timezone: Option<String>,
    pub visibility: Option<String>,
}

pub static EVENT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "event".into(),
    plural: Some("events".into()),
    description: Some("Something that happens — at a time, optionally at a place, involving people.".into()),
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
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("startDate".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/Event".into(), url: Some("https://schema.org/Event".into()), notes: Some("Core event type. Our startDate/endDate map 1:1; eventType is free-form vs. schema.org's subtype hierarchy (Concert, Conference, BusinessEvent). organizer/location match directly.".into()) },
        PriorArtDef { source: "RFC 5545 (iCalendar) VEVENT".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc5545".into()), notes: Some("Our icalUid is their UID; recurrence is their RRULE; status maps to STATUS (TENTATIVE/CONFIRMED/CANCELLED); showAs ≈ TRANSP; involves[] ≈ ATTENDEE.".into()) },
        PriorArtDef { source: "ActivityStreams 2.0 Event".into(), url: Some("https://www.w3.org/TR/activitystreams-vocabulary/#dfn-event".into()), notes: Some("Fediverse inbox format. Thinner than iCal — no native recurrence or showAs; our involves[] ≈ attendees via as:Relationship.".into()) },
    ],
    ..ShapeDef::default()
});
