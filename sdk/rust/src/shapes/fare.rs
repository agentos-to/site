// DO NOT EDIT — generated from platform/ontology/shapes/fare.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// The priced class-of-service unit for a transport journey — the BASE
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Fare {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub base_price: Option<f64>,
    pub booking_code: Option<String>,
    pub changeable: Option<bool>,
    pub class: Option<String>,
    pub components: Option<i64>,
    pub conditions: Option<serde_json::Value>,
    pub currency: Option<String>,
    pub fare_family: Option<String>,
    pub identifier: String,
    pub miles_earned: Option<i64>,
    pub passenger_type: Option<String>,
    pub points_earned: Option<i64>,
    pub product_type: Option<String>,
    pub refundable: Option<bool>,
    pub restrictions: Option<Vec<String>>,
}

pub static FARE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "fare".into(),
    plural: Some("fares".into()),
    description: Some("The priced class-of-service unit for a transport journey — the BASE".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("basePrice", FieldType::Number),
        FieldDef::optional("bookingCode", FieldType::String),
        FieldDef::optional("changeable", FieldType::Boolean),
        FieldDef::optional("class", FieldType::String),
        FieldDef::optional("components", FieldType::Integer),
        FieldDef::optional("conditions", FieldType::Json),
        FieldDef::optional("currency", FieldType::String),
        FieldDef::optional("fareFamily", FieldType::String),
        FieldDef::required("identifier", FieldType::String),
        FieldDef::optional("milesEarned", FieldType::Integer),
        FieldDef::optional("passengerType", FieldType::String),
        FieldDef::optional("pointsEarned", FieldType::Integer),
        FieldDef::optional("productType", FieldType::String),
        FieldDef::optional("refundable", FieldType::Boolean),
        FieldDef::optional("restrictions", FieldType::StringList),
    ],
    identity: vec!["at".into(), "identifier".into()],
    display: Some(DisplaySpec {
        subtitle: Some("fareFamily".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
