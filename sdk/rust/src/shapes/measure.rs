// DO NOT EDIT — generated from platform/ontology/shapes/measure.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A single measured value about a subject, at a time — "LDL = 95 mg/dL on
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Measure {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub at: Option<String>,
    pub end: Option<String>,
    pub flag: Option<String>,
    pub notes: Option<String>,
    pub ref_high: Option<f64>,
    pub ref_low: Option<f64>,
    pub ref_text: Option<String>,
    pub start: Option<String>,
    pub status: Option<String>,
    pub value: Option<f64>,
    pub value_text: Option<String>,
}

pub static MEASURE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "measure".into(),
    plural: Some("measures".into()),
    description: Some("A single measured value about a subject, at a time — \"LDL = 95 mg/dL on".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("at", FieldType::Datetime),
        FieldDef::optional("end", FieldType::Datetime),
        FieldDef::optional("flag", FieldType::String),
        FieldDef::optional("notes", FieldType::Text),
        FieldDef::optional("refHigh", FieldType::Number),
        FieldDef::optional("refLow", FieldType::Number),
        FieldDef::optional("refText", FieldType::String),
        FieldDef::optional("start", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("value", FieldType::Number),
        FieldDef::optional("valueText", FieldType::String),
    ],
    timed: Some("self".into()),
    display: Some(DisplaySpec {
        subtitle: Some("at".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "HL7 FHIR R5 — Observation".into(), url: Some("https://www.hl7.org/fhir/observation.html".into()), notes: Some("The canonical resource for a measured value. value (with its UCUM unit) ≈ valueQuantity; at ≈ effectiveDateTime; refLow/refHigh/refText ≈ the referenceRange backbone (the inline snapshot); flag ≈ interpretation; status ≈ status. `measures` ≈ code resolved to a biomarker. FHIR has no normalized-range link — our `reportedRange` link adds that.".into()) },
        PriorArtDef { source: "HL7 v2.x — OBX segment".into(), url: Some("https://hl7-definition.caristix.com/v2/HL7v2.5/Segments/OBX".into()), notes: Some("The legacy lab-result segment most labs still emit. OBX-5 (value) and OBX-6 (units) together ≈ our value-with-unit; OBX-7 (reference range), OBX-8 (abnormal flag), OBX-14 (datetime) map to refText/flag/at.".into()) },
        PriorArtDef { source: "UCUM — Unified Code for Units of Measure".into(), url: Some("https://ucum.org/".into()), notes: Some("The unit on every numeric val (mg/dL, mmol/L, 10*3/uL) follows UCUM — the unit system FHIR mandates for Observation.valueQuantity, so measures round-trip into FHIR cleanly.".into()) },
    ],
    ..ShapeDef::default()
});
