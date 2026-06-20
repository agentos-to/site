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
    pub arrangement: Option<String>,
    pub collected_at: Option<String>,
    #[serde(rename = "default_view")]
    pub default_view: Option<String>,
    pub description: Option<String>,
    pub fasting: Option<bool>,
    #[serde(rename = "icon_size")]
    pub icon_size: Option<i64>,
    pub is_default: Option<bool>,
    pub is_public: Option<bool>,
    pub item_count: Option<i64>,
    pub list_id: Option<String>,
    pub list_type: Option<String>,
    #[serde(rename = "member_shape")]
    pub member_shape: Option<String>,
    pub ordered_at: Option<String>,
    #[serde(rename = "ordering_mode")]
    pub ordering_mode: Option<String>,
    pub panel_code: Option<String>,
    pub path: Option<String>,
    pub privacy: Option<String>,
    pub received_at: Option<String>,
    pub reported_at: Option<String>,
    #[serde(rename = "sort_by")]
    pub sort_by: Option<String>,
    pub verified_at: Option<String>,
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
        FieldDef::optional("arrangement", FieldType::String),
        FieldDef::optional("collectedAt", FieldType::Datetime),
        FieldDef::optional("default_view", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("fasting", FieldType::Boolean),
        FieldDef::optional("icon_size", FieldType::Integer),
        FieldDef::optional("isDefault", FieldType::Boolean),
        FieldDef::optional("isPublic", FieldType::Boolean),
        FieldDef::optional("itemCount", FieldType::Integer),
        FieldDef::optional("listId", FieldType::String),
        FieldDef::optional("listType", FieldType::String),
        FieldDef::optional("member_shape", FieldType::String),
        FieldDef::optional("orderedAt", FieldType::Datetime),
        FieldDef::optional("ordering_mode", FieldType::String),
        FieldDef::optional("panelCode", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("privacy", FieldType::String),
        FieldDef::optional("receivedAt", FieldType::Datetime),
        FieldDef::optional("reportedAt", FieldType::Datetime),
        FieldDef::optional("sort_by", FieldType::String),
        FieldDef::optional("verifiedAt", FieldType::Datetime),
    ],
    also: vec!["list".into()],
    timed: Some("self".into()),
    display: Some(DisplaySpec {
        subtitle: Some("collectedAt".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "HL7 FHIR R5 — DiagnosticReport".into(), url: Some("https://www.hl7.org/fhir/diagnosticreport.html".into()), notes: Some("A dated panel is a DiagnosticReport: a set of observations grouped under one report with an effective date and a performer. Our `contains` links (from `list`) ≈ DiagnosticReport.result; collectedAt ≈ Specimen.collection.collectedDateTime (effectiveDateTime); orderedAt ≈ the ServiceRequest.authoredOn; receivedAt ≈ Specimen.receivedTime; reportedAt ≈ DiagnosticReport.issued; verifiedAt ≈ the report verification stamp; performedAt ≈ performer.".into()) },
        PriorArtDef { source: "LOINC — Panels and Forms".into(), url: Some("https://loinc.org/panels/".into()), notes: Some("LOINC defines panel codes and their member observables (CBC panel 58410-2 enumerates hemoglobin, hematocrit, WBC, …). panelCode plus the contains→biomarker links mirror a LOINC panel definition.".into()) },
        PriorArtDef { source: "schema.org/MedicalTest".into(), url: Some("https://schema.org/MedicalTest".into()), notes: Some("Lighter-weight precedent — a diagnostic test with usedToDiagnose / normalRange. Our panel is the grouping; biomarkers and health-reference-range carry the observable detail and the ranges.".into()) },
    ],
    ..ShapeDef::default()
});
