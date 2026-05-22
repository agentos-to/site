// DO NOT EDIT — generated from platform/ontology/shapes/seatmap.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A seat map for a specific flight + cabin, returned by an airline skill.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Seatmap {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub aircraft_code: Option<String>,
    pub available_seats: Option<i64>,
    pub basic_economy_locked: Option<bool>,
    pub cabins: Option<serde_json::Value>,
    pub class_of_service: Option<String>,
    pub destination: Option<String>,
    pub fare_basis_code: Option<String>,
    pub flight_number: Option<String>,
    pub has_exit_row: Option<bool>,
    pub has_free_seats: Option<bool>,
    pub has_paid_seats: Option<bool>,
    pub origin: Option<String>,
    pub tiers: Option<serde_json::Value>,
    pub total_seats: Option<i64>,
}

pub static SEATMAP: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "seatmap".into(),
    plural: Some("seatmaps".into()),
    description: Some("A seat map for a specific flight + cabin, returned by an airline skill.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("aircraftCode", FieldType::String),
        FieldDef::optional("availableSeats", FieldType::Integer),
        FieldDef::optional("basicEconomyLocked", FieldType::Boolean),
        FieldDef::optional("cabins", FieldType::Json),
        FieldDef::optional("classOfService", FieldType::String),
        FieldDef::optional("destination", FieldType::String),
        FieldDef::optional("fareBasisCode", FieldType::String),
        FieldDef::optional("flightNumber", FieldType::String),
        FieldDef::optional("hasExitRow", FieldType::Boolean),
        FieldDef::optional("hasFreeSeats", FieldType::Boolean),
        FieldDef::optional("hasPaidSeats", FieldType::Boolean),
        FieldDef::optional("origin", FieldType::String),
        FieldDef::optional("tiers", FieldType::Json),
        FieldDef::optional("totalSeats", FieldType::Integer),
    ],
    identity: vec!["id".into()],
    display: Some(DisplaySpec {
        title: Some("flightNumber".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
