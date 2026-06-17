// DO NOT EDIT — generated from platform/ontology/shapes/class.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A scheduled, bookable group activity — gym classes, workshops, courses.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Class {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub activity_type: Option<String>,
    pub all_day: Option<bool>,
    pub capacity: Option<i64>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub ical_uid: Option<String>,
    pub is_full: Option<bool>,
    pub properties: Option<serde_json::Value>,
    pub recurrence: Option<Vec<String>>,
    pub show_as: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub spots_remaining: Option<i64>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub timezone: Option<String>,
    pub visibility: Option<String>,
}

pub static CLASS: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "class".into(),
    plural: Some("classes".into()),
    description: Some("A scheduled, bookable group activity — gym classes, workshops, courses.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("activityType", FieldType::String),
        FieldDef::optional("allDay", FieldType::Boolean),
        FieldDef::optional("capacity", FieldType::Integer),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("isFull", FieldType::Boolean),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("spotsRemaining", FieldType::Integer),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    also: vec!["event".into()],
    display: Some(DisplaySpec {
        subtitle: Some("activityType".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/EducationEvent".into(), url: Some("https://schema.org/EducationEvent".into()), notes: Some("schema.org's closest peer for a bookable class. Our instructor = performer; capacity = maximumAttendeeCapacity; spotsRemaining ≈ remainingAttendeeCapacity.".into()) },
        PriorArtDef { source: "schema.org/ExerciseAction".into(), url: Some("https://schema.org/ExerciseAction".into()), notes: Some("Fitness-specific vocabulary: activityType ≈ exerciseType; venue matches directly as location.".into()) },
        PriorArtDef { source: "Mindbody Public API (class schedules)".into(), url: Some("https://developers.mindbodyonline.com/PublicDocumentation/V6".into()), notes: Some("Practical API mirror. Our capacity/spotsRemaining/isFull come from Mindbody's MaxCapacity/TotalBooked/IsWaitlistAvailable.".into()) },
    ],
    ..ShapeDef::default()
});
