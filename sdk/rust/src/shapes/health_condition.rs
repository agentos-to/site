// DO NOT EDIT — generated from platform/ontology/shapes/health-condition.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A health condition — a diagnosis, problem, symptom, or family-history
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct HealthCondition {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub all_day: Option<bool>,
    pub body_site: Option<String>,
    pub clinical_area: Option<String>,
    pub clinical_status: Option<String>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub ical_uid: Option<String>,
    #[serde(rename = "icd10Code")]
    pub icd10code: Option<String>,
    pub mitigation: Option<String>,
    pub properties: Option<serde_json::Value>,
    pub proximity: Option<String>,
    pub recurrence: Option<Vec<String>>,
    pub severity: Option<String>,
    pub show_as: Option<String>,
    pub snomed_code: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub timezone: Option<String>,
    pub verification_status: Option<String>,
    pub visibility: Option<String>,
}

pub static HEALTH_CONDITION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "health-condition".into(),
    plural: Some("health-conditions".into()),
    description: Some("A health condition — a diagnosis, problem, symptom, or family-history".into()),
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
        FieldDef::optional("bodySite", FieldType::String),
        FieldDef::optional("clinicalArea", FieldType::String),
        FieldDef::optional("clinicalStatus", FieldType::String),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("icd10Code", FieldType::String),
        FieldDef::optional("mitigation", FieldType::Text),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("proximity", FieldType::String),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("severity", FieldType::String),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("snomedCode", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("verificationStatus", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    also: vec!["event".into()],
    identity_any: vec!["snomedCode".into(), "name".into()],
    display: Some(DisplaySpec {
        subtitle: Some("clinicalStatus".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
