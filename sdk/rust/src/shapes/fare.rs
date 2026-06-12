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
    out: vec![
        EdgeDef { label: "at_namespace".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "priced_for".into(), to: Some("trip".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "routed_through".into(), to: Some("leg".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "derived_from".into(), to: Some("offer".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "under".into(), to: Some("reservation".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "itemizes".into(), to: Some("tax_line".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "earns_into".into(), to: Some("membership".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["at".into(), "identifier".into()],
    display: Some(DisplaySpec {
        subtitle: Some("fareFamily".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "IATA Fare Basis Code / ATPCO filings".into(), url: Some("https://en.wikipedia.org/wiki/Fare_basis_code".into()), notes: Some("Airline canonical. First char = RBD/booking class (our `bookingCode`); remainder = airline-proprietary pointer into ATPCO-filed fare rules (our `identifier` as opaque string, `conditions` for the rule blob). Codes are 3-8 chars; we don't parse beyond the first char.".into()) },
        PriorArtDef { source: "IATA NDC FareDetail / FareComponent".into(), url: Some("https://developer.iata.org/en/ndc/".into()), notes: Some("NDC's FareDetail.FareComponent carries FareBasis.FareBasisCode, FareBasis.RBD, Price.BaseAmount, FareRules.Penalty, and CabinType.CabinTypeCode. Our identifier/bookingCode/basePrice/ class/refundable map directly.".into()) },
        PriorArtDef { source: "Duffel Offer Slice / fare_basis_code".into(), url: Some("https://duffel.com/docs/api/v2/offers".into()), notes: Some("Duffel surfaces fare_basis_code on each slice's segments along with cabin_class, cabin_class_marketing_name (our fareFamily), and passenger-level base_amount. Our basePrice = base_amount; class = cabin_class; fareFamily = cabin_class_marketing_name.".into()) },
        PriorArtDef { source: "Amtrak / Rail Europe fare types".into(), url: Some("https://www.amtrak.com/routes/fares".into()), notes: Some("Non-airline generalization. Amtrak fares are Saver / Value / Flexible / Premium / Business / First / Acela First / Acela First Refundable — their tier codes fit `identifier`; their names fit `fareFamily`; their rules fit `refundable`/ `changeable`/`restrictions`.".into()) },
        PriorArtDef { source: "GTFS fare_products.txt (transit)".into(), url: Some("https://gtfs.org/documentation/schedule/reference/#fare_productstxt".into()), notes: Some("Open transit standard for fare products. Their fare_product_id = our identifier; fare_product_name = fareFamily; amount = basePrice; currency_code = currency. rider_category matches passengerType (adult/child/senior/student).".into()) },
        PriorArtDef { source: "schema.org/Offer price + FlightReservation".into(), url: Some("https://schema.org/FlightReservation".into()), notes: Some("schema.org's Offer.price + Offer.priceCurrency align with our basePrice + currency. schema.org has no fare-basis concept; NDC and GTFS fill that gap.".into()) },
    ],
    ..ShapeDef::default()
});
