// DO NOT EDIT — generated from platform/ontology/shapes/unit.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A unit of measure — a concrete scale for a quantity. mg/dL, USD, pascal,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Unit {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub iso4217: Option<String>,
    #[serde(rename = "iso4217Numeric")]
    pub iso4217numeric: Option<String>,
    pub kind: Option<String>,
    pub label: Option<String>,
    pub log_base: Option<f64>,
    pub minor_exponent: Option<i64>,
    pub qudt_unit_iri: Option<String>,
    pub si_digital_framework_uri: Option<String>,
    pub symbol: Option<String>,
    pub to_base_factor: Option<f64>,
    pub to_base_offset: Option<f64>,
    pub ucum_code: Option<String>,
    pub un_cefact_common_code: Option<String>,
    pub wikidata_id: Option<String>,
}

pub static UNIT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "unit".into(),
    plural: Some("units".into()),
    description: Some("A unit of measure — a concrete scale for a quantity. mg/dL, USD, pascal,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("iso4217", FieldType::String),
        FieldDef::optional("iso4217Numeric", FieldType::String),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("label", FieldType::String),
        FieldDef::optional("logBase", FieldType::Number),
        FieldDef::optional("minorExponent", FieldType::Integer),
        FieldDef::optional("qudtUnitIri", FieldType::String),
        FieldDef::optional("siDigitalFrameworkUri", FieldType::String),
        FieldDef::optional("symbol", FieldType::String),
        FieldDef::optional("toBaseFactor", FieldType::Number),
        FieldDef::optional("toBaseOffset", FieldType::Number),
        FieldDef::optional("ucumCode", FieldType::String),
        FieldDef::optional("unCefactCommonCode", FieldType::String),
        FieldDef::optional("wikidataId", FieldType::String),
    ],
    identity_any: vec!["ucumCode".into(), "siDigitalFrameworkUri".into(), "iso4217".into()],
    display: Some(DisplaySpec {
        subtitle: Some("symbol".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "UCUM — Unified Code for Units of Measure".into(), url: Some("https://ucum.org/ucum".into()), notes: Some("ucumCode is the primary working identity — case-sensitive variant (mg is not MG; h hour is not H henry). Compositional, and the de-facto healthcare standard (FHIR Quantity mandates it, LOINC and HL7 use it). Machine-readable database: ucum-essence.xml.".into()) },
        PriorArtDef { source: "BIPM — SI Digital Framework / SI Reference Point".into(), url: Some("https://www.si-digital-framework.org/".into()), notes: Some("Launched March 2024 by the BIPM CIPM Task Group on the Digital SI. Publishes resolvable persistent URIs for SI units, prefixes, and defining constants (base namespace si-digital-framework.org/SI/ units/), served as TTL plus a JSON/XML API. The most authoritative source for SI units — treaty-level. siDigitalFrameworkUri carries it; null for non-SI units, and that null is meaningful.".into()) },
        PriorArtDef { source: "UN/CEFACT Recommendation 20 — Codes for Units of Measure Used in International Trade".into(), url: Some("https://unece.org/trade/uncefact/cl-recommendations".into()), notes: Some("Around 700 short codes (KGM kilogram, MTR metre, LTR litre, CEL degree Celsius). Rev 17 (2021), freely downloadable as XLSX or genericode XML. schema.org's unitCode property uses exactly these codes — unCefactCommonCode is the interop join key.".into()) },
        PriorArtDef { source: "QUDT — Quantities, Units, Dimensions and Types".into(), url: Some("https://www.qudt.org/doc/DOC_VOCAB-UNITS.html".into()), notes: Some("qudtUnitIri cross-references QUDT, itself a cross-reference hub (QUDT units carry qudt:ucumCode, qudt:uneceCommonCode, qudt:wikidataMatch). toBaseFactor/toBaseOffset correspond to qudt:conversionMultiplier / conversionOffset; kind=currency corresponds to qudt:CurrencyUnit, which also carries NO conversion multiplier — FX is external.".into()) },
        PriorArtDef { source: "Wikidata".into(), url: Some("https://www.wikidata.org/wiki/Q11570".into()), notes: Some("wikidataId (kilogram = Q11570) is a universal glue identifier — links to every Wikipedia language edition and many external databases. Free SPARQL endpoint plus dumps.".into()) },
        PriorArtDef { source: "ISO 4217 — Currency codes".into(), url: Some("https://www.iso.org/iso-4217-currency-codes.html".into()), notes: Some("iso4217 (alpha) plus iso4217Numeric and minorExponent for currency units. ISO 4217 IS the authoritative currency-code registry — notably, currency is the ONE unit family with a single authoritative code system; physical units have none.".into()) },
        PriorArtDef { source: "schema.org — unitCode".into(), url: Some("https://schema.org/unitCode".into()), notes: Some("Precedent that the minimum unit model is (value, unitCode), and that unitCode in practice means a UN/CEFACT Rec 20 code.".into()) },
        PriorArtDef { source: "NIST SP 811 / SP 330 — and why NIST is NOT a field".into(), url: Some("https://www.nist.gov/pml/special-publication-811".into()), notes: Some("Recorded deliberately. NIST publishes SI usage guidance (SP 811) and the US edition of the SI Brochure (SP 330) — prose only. NIST assigns no unit codes and maintains no unit registry; there is nothing to cross-reference, so no NIST field exists on this shape. Same for ISO 80000 — it defines units in prose and assigns no codes.".into()) },
    ],
    ..ShapeDef::default()
});
