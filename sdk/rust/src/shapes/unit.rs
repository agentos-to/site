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
    out: vec![
        EdgeDef { label: "measures".into(), to: Some("dimension".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "quantifies".into(), to: Some("quantity-kind".into()), from: None, card: Cardinality::Many },
    ],
    identity_any: vec!["ucumCode".into(), "siDigitalFrameworkUri".into(), "iso4217".into()],
    display: Some(DisplaySpec {
        subtitle: Some("symbol".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
