// DO NOT EDIT — generated from platform/ontology/shapes/meeting.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A calendar meeting — an event with virtual meeting details and transcripts.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Meeting {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub all_day: Option<bool>,
    pub calendar_link: Option<String>,
    pub conference_provider: Option<String>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub ical_uid: Option<String>,
    pub is_virtual: Option<bool>,
    pub meeting_type: Option<String>,
    pub meeting_url: Option<String>,
    pub phone_dial_in: Option<String>,
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

pub static MEETING: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "meeting".into(),
    plural: Some("meetings".into()),
    description: Some("A calendar meeting — an event with virtual meeting details and transcripts.".into()),
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
        FieldDef::optional("calendarLink", FieldType::Url),
        FieldDef::optional("conferenceProvider", FieldType::String),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("isVirtual", FieldType::Boolean),
        FieldDef::optional("meetingType", FieldType::String),
        FieldDef::optional("meetingUrl", FieldType::Url),
        FieldDef::optional("phoneDialIn", FieldType::String),
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
    out: vec![
        EdgeDef { label: "transcribed_by".into(), to: Some("transcript".into()), from: None, card: Cardinality::One },
    ],
    also: vec!["event".into()],
    display: Some(DisplaySpec {
        subtitle: Some("location".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "RFC 5545 VEVENT + conference property (RFC 7986)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc7986#section-5.11".into()), notes: Some("Our meetingUrl ≈ CONFERENCE URI; phoneDialIn = tel: URI in CONFERENCE feature=PHONE; conferenceProvider ≈ CONFERENCE LABEL.".into()) },
        PriorArtDef { source: "schema.org/Event — location.VirtualLocation".into(), url: Some("https://schema.org/VirtualLocation".into()), notes: Some("Our isVirtual triggers VirtualLocation; meetingUrl ≈ VirtualLocation.url.".into()) },
        PriorArtDef { source: "Google Calendar Event conferenceData".into(), url: Some("https://developers.google.com/calendar/api/v3/reference/events".into()), notes: Some("Practical API mirror. Our conferenceProvider ≈ conferenceData.conferenceSolution.name; meetingUrl = entryPoints[uri].".into()) },
    ],
    ..ShapeDef::default()
});
