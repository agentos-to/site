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
    identity: vec!["at".into(), "calendarId".into()],
    display: Some(DisplaySpec {
        subtitle: Some("source".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "RFC 5545 VCALENDAR".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc5545".into()), notes: Some("Our calendarId ≈ VCALENDAR's X-WR-CALID; timezone = X-WR-TIMEZONE; events relation mirrors VCALENDAR's VEVENT components.".into()) },
        PriorArtDef { source: "CalDAV (RFC 4791)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc4791".into()), notes: Some("CalDAV calendar collections define accessRole semantics (owner/writer/reader) that match our field directly.".into()) },
        PriorArtDef { source: "Google Calendar API CalendarList".into(), url: Some("https://developers.google.com/calendar/api/v3/reference/calendarList".into()), notes: Some("Practical API mirror. Our color/backgroundColor/foregroundColor, isPrimary, accessRole come from Google's CalendarList resource.".into()) },
    ],
    ..ShapeDef::default()
});
