// DO NOT EDIT — generated from platform/ontology/shapes/airport.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An airport. Created from flight search results and linked to flights.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Airport {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub city: Option<String>,
    pub country: Option<String>,
    pub country_code: Option<String>,
    pub elevation_ft: Option<i64>,
    pub iata_code: String,
    pub icao_code: Option<String>,
    pub terminal_count: Option<i64>,
    pub timezone: Option<String>,
}

pub static AIRPORT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "airport".into(),
    plural: Some("airports".into()),
    description: Some("An airport. Created from flight search results and linked to flights.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("city", FieldType::String),
        FieldDef::optional("country", FieldType::String),
        FieldDef::optional("countryCode", FieldType::String),
        FieldDef::optional("elevationFt", FieldType::Integer),
        FieldDef::required("iataCode", FieldType::String),
        FieldDef::optional("icaoCode", FieldType::String),
        FieldDef::optional("terminalCount", FieldType::Integer),
        FieldDef::optional("timezone", FieldType::String),
    ],
    identity: vec!["iataCode".into()],
    display: Some(DisplaySpec {
        subtitle: Some("iataCode".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "IATA/ICAO Airport Codes".into(), url: Some("https://www.iata.org/en/publications/directories/code-search/".into()), notes: Some("iataCode is 3-letter (LAX, JFK); icaoCode is 4-letter (KLAX, KJFK). Canonical identifiers for global airport routing.".into()) },
        PriorArtDef { source: "schema.org/Airport".into(), url: Some("https://schema.org/Airport".into()), notes: Some("Our iataCode/icaoCode = iataCode/icaoCode; city/country = address fields; elevationFt ≈ elevation. Direct alignment.".into()) },
        PriorArtDef { source: "OurAirports open dataset".into(), url: Some("https://ourairports.com/data/".into()), notes: Some("Practical open dataset covering terminalCount, elevation, and country codes (ISO 3166-1) aligning with our countryCode field.".into()) },
    ],
    ..ShapeDef::default()
});
