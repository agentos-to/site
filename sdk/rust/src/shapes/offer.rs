// DO NOT EDIT — generated from platform/ontology/shapes/offer.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A purchasable offer — typically a flight itinerary with a price.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Offer {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub all_day: Option<bool>,
    pub availability: Option<String>,
    pub booking_token: Option<String>,
    pub currency: Option<String>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub departure_token: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub ical_uid: Option<String>,
    pub offer_type: Option<String>,
    pub price: Option<f64>,
    pub properties: Option<serde_json::Value>,
    pub recurrence: Option<Vec<String>>,
    pub show_as: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub timezone: Option<String>,
    pub visibility: Option<String>,
}

pub static OFFER: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "offer".into(),
    plural: Some("offers".into()),
    description: Some("A purchasable offer — typically a flight itinerary with a price.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("allDay", FieldType::Boolean),
        FieldDef::optional("availability", FieldType::String),
        FieldDef::optional("bookingToken", FieldType::String),
        FieldDef::optional("currency", FieldType::String),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("departureToken", FieldType::String),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("offerType", FieldType::String),
        FieldDef::optional("price", FieldType::Number),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "offered_for".into(), to: Some("product".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "offered_by".into(), to: Some("organization".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "covers_trip".into(), to: Some("trip".into()), from: None, card: Cardinality::Many },
    ],
    also: vec!["event".into()],
    identity: vec!["id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("price".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
