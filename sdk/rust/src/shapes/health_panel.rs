// DO NOT EDIT — generated from platform/ontology/shapes/health-panel.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A panel — a named grouping of biomarkers ordered and reported together.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct HealthPanel {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub all_day: Option<bool>,
    pub arrangement: Option<String>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    #[serde(rename = "default_view")]
    pub default_view: Option<String>,
    pub description: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub fasting: Option<bool>,
    pub ical_uid: Option<String>,
    #[serde(rename = "icon_size")]
    pub icon_size: Option<i64>,
    pub is_default: Option<bool>,
    pub is_public: Option<bool>,
    pub item_count: Option<i64>,
    pub list_id: Option<String>,
    pub list_type: Option<String>,
    #[serde(rename = "member_shape")]
    pub member_shape: Option<String>,
    #[serde(rename = "ordering_mode")]
    pub ordering_mode: Option<String>,
    pub panel_code: Option<String>,
    pub path: Option<String>,
    pub privacy: Option<String>,
    pub properties: Option<serde_json::Value>,
    pub recurrence: Option<Vec<String>>,
    pub show_as: Option<String>,
    #[serde(rename = "sort_by")]
    pub sort_by: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub timezone: Option<String>,
    pub visibility: Option<String>,
}

pub static HEALTH_PANEL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "health-panel".into(),
    plural: Some("health-panels".into()),
    description: Some("A panel — a named grouping of biomarkers ordered and reported together.".into()),
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
        FieldDef::optional("arrangement", FieldType::String),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("default_view", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("fasting", FieldType::Boolean),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("icon_size", FieldType::Integer),
        FieldDef::optional("isDefault", FieldType::Boolean),
        FieldDef::optional("isPublic", FieldType::Boolean),
        FieldDef::optional("itemCount", FieldType::Integer),
        FieldDef::optional("listId", FieldType::String),
        FieldDef::optional("listType", FieldType::String),
        FieldDef::optional("member_shape", FieldType::String),
        FieldDef::optional("ordering_mode", FieldType::String),
        FieldDef::optional("panelCode", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("privacy", FieldType::String),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("sort_by", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "performed_at".into(), to: Some("health-lab".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "documented_in".into(), to: Some("file".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "concerns".into(), to: Some("person".into()), from: None, card: Cardinality::One },
    ],
    also: vec!["list".into(), "event".into()],
    display: Some(DisplaySpec {
        subtitle: Some("startDate".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "HL7 FHIR R5 — DiagnosticReport".into(), url: Some("https://www.hl7.org/fhir/diagnosticreport.html".into()), notes: Some("A dated panel is a DiagnosticReport: a set of observations grouped under one report with an effective date and a performer. Our `contains` links (from `list`) ≈ DiagnosticReport.result; effectiveDate ≈ effectiveDateTime; performedAt ≈ performer.".into()) },
        PriorArtDef { source: "LOINC — Panels and Forms".into(), url: Some("https://loinc.org/panels/".into()), notes: Some("LOINC defines panel codes and their member observables (CBC panel 58410-2 enumerates hemoglobin, hematocrit, WBC, …). panelCode plus the contains→biomarker links mirror a LOINC panel definition.".into()) },
        PriorArtDef { source: "schema.org/MedicalTest".into(), url: Some("https://schema.org/MedicalTest".into()), notes: Some("Lighter-weight precedent — a diagnostic test with usedToDiagnose / normalRange. Our panel is the grouping; biomarkers and health-reference-range carry the observable detail and the ranges.".into()) },
    ],
    ..ShapeDef::default()
});
