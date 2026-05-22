// DO NOT EDIT — generated from platform/ontology/shapes/airline.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A commercial airline. Created from flight search results.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Airline {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub actor_type: Option<String>,
    pub alliance: Option<String>,
    pub callsign: Option<String>,
    pub country: Option<String>,
    pub iata_code: String,
    pub icao_code: Option<String>,
    pub industry: Option<String>,
}

pub static AIRLINE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "airline".into(),
    plural: Some("airlines".into()),
    description: Some("A commercial airline. Created from flight search results.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("actorType", FieldType::String),
        FieldDef::optional("alliance", FieldType::String),
        FieldDef::optional("callsign", FieldType::String),
        FieldDef::optional("country", FieldType::String),
        FieldDef::required("iataCode", FieldType::String),
        FieldDef::optional("icaoCode", FieldType::String),
        FieldDef::optional("industry", FieldType::String),
    ],
    also: vec!["organization".into()],
    identity: vec!["iataCode".into()],
    display: Some(DisplaySpec {
        subtitle: Some("iataCode".into()),
        image: Some("image".into()),
        highlights: vec!["headquarters".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
