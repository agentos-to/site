// DO NOT EDIT — generated from platform/ontology/shapes/dimension.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A physical dimension — the abstract nature of a quantity, expressed as
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Dimension {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub amount: Option<i64>,
    pub current: Option<i64>,
    pub dimensionless: Option<bool>,
    pub key: String,
    pub label: Option<String>,
    pub length: Option<i64>,
    pub luminous: Option<i64>,
    pub mass: Option<i64>,
    pub temperature: Option<i64>,
    pub time: Option<i64>,
}

pub static DIMENSION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "dimension".into(),
    plural: Some("dimensions".into()),
    description: Some("A physical dimension — the abstract nature of a quantity, expressed as".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("amount", FieldType::Integer),
        FieldDef::optional("current", FieldType::Integer),
        FieldDef::optional("dimensionless", FieldType::Boolean),
        FieldDef::required("key", FieldType::String),
        FieldDef::optional("label", FieldType::String),
        FieldDef::optional("length", FieldType::Integer),
        FieldDef::optional("luminous", FieldType::Integer),
        FieldDef::optional("mass", FieldType::Integer),
        FieldDef::optional("temperature", FieldType::Integer),
        FieldDef::optional("time", FieldType::Integer),
    ],
    out: vec![
        EdgeDef { label: "has_base_unit".into(), to: Some("unit".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["key".into()],
    display: Some(DisplaySpec {
        subtitle: Some("label".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "BIPM — SI Brochure, 9th edition (2019)".into(), url: Some("https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf".into()), notes: Some("Defines the 7 base quantities (length, mass, time, electric current, thermodynamic temperature, amount of substance, luminous intensity) and their dimensions L, M, T, I, Θ, N, J. The seven exponent fields here are exactly those base dimensions.".into()) },
        PriorArtDef { source: "ISO 80000-1 — Quantities and units, Part 1: General".into(), url: Some("https://www.iso.org/standard/76921.html".into()), notes: Some("The ISQ (International System of Quantities) — the rigorous definition of a quantity dimension as a product of base-quantity powers. This shape is a direct encoding of an ISQ dimension.".into()) },
        PriorArtDef { source: "QUDT — QuantityKindDimensionVector".into(), url: Some("https://www.qudt.org/doc/DOC_SCHEMA-QUDT.html".into()), notes: Some("QUDT encodes the same 7 exponents as separate properties (qudt:dimensionExponentForMass etc.) plus a compact vector IRI. Our `key` mirrors that compact form; the seven integer fields mirror the per-dimension properties.".into()) },
    ],
    ..ShapeDef::default()
});
