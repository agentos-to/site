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
    ..ShapeDef::default()
});
