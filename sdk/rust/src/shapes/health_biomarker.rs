// DO NOT EDIT — generated from platform/ontology/shapes/health-biomarker.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// The *definition* of a measurable health quantity — TSH, LDL cholesterol,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct HealthBiomarker {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub analyte_type: Option<String>,
    pub category: Option<String>,
    pub description: Option<String>,
    pub loinc_code: Option<String>,
    pub measure: Option<String>,
}

pub static HEALTH_BIOMARKER: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "health-biomarker".into(),
    plural: Some("health-biomarkers".into()),
    description: Some("The *definition* of a measurable health quantity — TSH, LDL cholesterol,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("analyteType", FieldType::String),
        FieldDef::optional("category", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("loincCode", FieldType::String),
        FieldDef::optional("measure", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "part_of".into(), to: Some("health-panel".into()), from: None, card: Cardinality::Many },
    ],
    identity_any: vec!["loincCode".into(), "measure".into()],
    display: Some(DisplaySpec {
        subtitle: Some("category".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "HL7 FHIR R5 — ObservationDefinition".into(), url: Some("https://www.hl7.org/fhir/observationdefinition.html".into()), notes: Some("FHIR's ObservationDefinition is the reusable definition of an observable, separate from the Observation that records a value. Our measure/category map to its code + quantitativeDetails. We deliberately do NOT include its qualifiedInterval — reference ranges are their own shape (health-reference-range).".into()) },
        PriorArtDef { source: "LOINC — Logical Observation Identifiers Names and Codes".into(), url: Some("https://loinc.org/".into()), notes: Some("The universal code system for lab and clinical observations. loincCode is the join key — every lab observable has a LOINC code (TSH 3016-3, LDL 2089-1, HbA1c 4548-4). LOINC identifies the observable only; it carries no reference range.".into()) },
    ],
    ..ShapeDef::default()
});
