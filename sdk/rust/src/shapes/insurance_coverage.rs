// DO NOT EDIT — generated from platform/ontology/shapes/insurance_coverage.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A single benefit line within an insurance policy — the unit at which a
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct InsuranceCoverage {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub coinsurance: Option<f64>,
    pub copay: Option<f64>,
    pub currency: Option<String>,
    pub deductible: Option<f64>,
    pub limit: Option<f64>,
    pub limit_basis: Option<String>,
    pub notes: Option<String>,
    pub out_of_pocket_max: Option<f64>,
    pub requires_preauth: Option<bool>,
    pub requires_referral: Option<bool>,
    pub waiting_period_months: Option<f64>,
}

pub static INSURANCE_COVERAGE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "insurance_coverage".into(),
    plural: Some("insurance_coverages".into()),
    description: Some("A single benefit line within an insurance policy — the unit at which a".into()),
    icon: Some("list-checks".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("coinsurance", FieldType::Number),
        FieldDef::optional("copay", FieldType::Number),
        FieldDef::optional("currency", FieldType::String),
        FieldDef::optional("deductible", FieldType::Number),
        FieldDef::optional("limit", FieldType::Number),
        FieldDef::optional("limitBasis", FieldType::String),
        FieldDef::optional("notes", FieldType::Text),
        FieldDef::optional("outOfPocketMax", FieldType::Number),
        FieldDef::optional("requiresPreauth", FieldType::Boolean),
        FieldDef::optional("requiresReferral", FieldType::Boolean),
        FieldDef::optional("waitingPeriodMonths", FieldType::Number),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("limit".into()),
        highlights: vec!["limit".into(), "requiresPreauth".into(), "requiresReferral".into(), "deductible".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "HL7 FHIR R5 — InsurancePlan.coverage.benefit & Coverage.costToBeneficiary".into(), url: Some("https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.coverage.benefit".into()), notes: Some("FHIR models a benefit with a type + a list of limits, and cost- sharing (copay/coinsurance/deductible) on Coverage.costToBeneficiary. Our limit/limitBasis ≈ benefit.limit{value,code}; copay/coinsurance/ deductible/outOfPocketMax ≈ costToBeneficiary value/type. FHIR's benefit.requirement (free-text access conditions) is split here into the queryable gates requiresPreauth / requiresReferral plus prose in notes — and the verbatim clause on the evidenced_by link.".into()) },
        PriorArtDef { source: "ACORD — Coverage / Limit / Deductible".into(), url: Some("https://www.acord.org/standards-architecture/reference-architecture".into()), notes: Some("ACORD Coverage carries Limit (with a basis: per-occurrence, aggregate, per-person) and Deductible. Our limit + limitBasis + deductible map directly; this is the P&C side (auto, renters, umbrella) that FHIR's health framing doesn't cover.".into()) },
        PriorArtDef { source: "US Summary of Benefits and Coverage (SBC)".into(), url: Some("https://www.cms.gov/marketplace/about/oversight/other-insurance-protections/summary-benefits-coverage-sbc-resources".into()), notes: Some("The federally-standardized consumer benefit summary: deductible, out-of-pocket maximum, copay, coinsurance per service category. Our health-line field set mirrors the SBC columns.".into()) },
    ],
    ..ShapeDef::default()
});
