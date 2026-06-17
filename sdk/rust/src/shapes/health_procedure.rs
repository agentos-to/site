// DO NOT EDIT — generated from platform/ontology/shapes/health-procedure.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A procedure — a clinical action performed on the body. Surgeries
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct HealthProcedure {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub all_day: Option<bool>,
    pub body_site: Option<String>,
    pub cpt_code: Option<String>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub findings: Option<String>,
    pub follow_up: Option<String>,
    pub ical_uid: Option<String>,
    pub outcome: Option<String>,
    pub performed_date: Option<String>,
    pub procedure_type: Option<String>,
    pub properties: Option<serde_json::Value>,
    pub recurrence: Option<Vec<String>>,
    pub show_as: Option<String>,
    pub snomed_code: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub timezone: Option<String>,
    pub visibility: Option<String>,
}

pub static HEALTH_PROCEDURE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "health-procedure".into(),
    plural: Some("health-procedures".into()),
    description: Some("A procedure — a clinical action performed on the body. Surgeries".into()),
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
        FieldDef::optional("cptCode", FieldType::String),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("findings", FieldType::Text),
        FieldDef::optional("followUp", FieldType::Text),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("outcome", FieldType::String),
        FieldDef::optional("performedDate", FieldType::Datetime),
        FieldDef::optional("procedureType", FieldType::String),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("snomedCode", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    also: vec!["event".into()],
    identity_any: vec!["cptCode".into(), "snomedCode".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("performedDate".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "HL7 FHIR R5 — Procedure".into(), url: Some("https://www.hl7.org/fhir/procedure.html".into()), notes: Some("The resource for an action performed on a patient. performedDate ≈ occurrenceDateTime/occurrencePeriod; status ≈ status; bodySite ≈ bodySite; outcome ≈ outcome; findings ≈ report + note; `treats` link ≈ reason; performer ≈ performer.actor. `orderedBy` ≈ basedOn → ServiceRequest.requester — the clinician who ordered the study, which on imaging/scopes is rarely the one who performs it.".into()) },
        PriorArtDef { source: "CPT — Current Procedural Terminology (AMA)".into(), url: Some("https://www.ama-assn.org/practice-management/cpt".into()), notes: Some("The US procedure code system used for billing. cptCode is the identity on insurance claims and operative records (septoplasty 30520, colonoscopy 45378).".into()) },
        PriorArtDef { source: "SNOMED CT — Procedure axis".into(), url: Some("https://www.snomed.org/".into()), notes: Some("SNOMED's procedure hierarchy provides the clinical (non-billing) code. FHIR Procedure.code is SNOMED-coded; snomedCode is the join key to the clinical ontology.".into()) },
    ],
    ..ShapeDef::default()
});
