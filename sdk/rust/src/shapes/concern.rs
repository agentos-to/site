// DO NOT EDIT — generated from platform/ontology/shapes/concern.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// What a person is going through — the felt, lived thing they'd name when
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Concern {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub all_day: Option<bool>,
    pub category: Option<String>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub ical_uid: Option<String>,
    pub intensity: Option<String>,
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

pub static CONCERN: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "concern".into(),
    plural: Some("concerns".into()),
    description: Some("What a person is going through — the felt, lived thing they'd name when".into()),
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
        FieldDef::optional("category", FieldType::String),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("intensity", FieldType::String),
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
    also: vec!["event".into()],
    identity_any: vec!["name".into()],
    display: Some(DisplaySpec {
        subtitle: Some("category".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Psychology Today — \"Issues\" (therapist directory facet)".into(), url: Some("https://www.psychologytoday.com/us/therapists".into()), notes: Some("The directory's \"Issues\" filter IS this axis — Anxiety, Depression, Grief, Trauma and PTSD, Relationship Issues, Self Esteem, Life Transitions, ~25 values. It is what a client searches by and what a therapist lists as a specialty — the dual reading this shape encodes.".into()) },
        PriorArtDef { source: "Case formulation / \"presenting concern\" (clinical psychology)".into(), url: Some("https://psychology.iresearchnet.com/counseling-psychology/counseling-process/clinical-presenting-issues/".into()), notes: Some("Modern client-centered practice prefers \"presenting concern\" over \"presenting problem\" — it honors how the client frames their experience rather than pathologizing it diagnosis-first. The shape name and its first-person framing follow that lineage.".into()) },
        PriorArtDef { source: "HL7 FHIR R5 — Condition (deliberately NOT used here)".into(), url: Some("https://www.hl7.org/fhir/condition.html".into()), notes: Some("The clinical sibling lives in health-condition (SNOMED/ICD coded). concern is the experiential counterpart that exists without a clinician. A concern MAY link to a health-condition when a diagnosis is on record, but never requires one.".into()) },
    ],
    ..ShapeDef::default()
});
