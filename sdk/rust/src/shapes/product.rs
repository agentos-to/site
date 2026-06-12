// DO NOT EDIT — generated from platform/ontology/shapes/product.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A purchasable item OR an identifiable product released into the world.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Product {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub aisle: Option<String>,
    pub availability: Option<String>,
    pub barcode: Option<String>,
    pub calories: Option<f64>,
    pub categories: Option<Vec<String>>,
    pub category: Option<String>,
    pub currency: Option<String>,
    pub customization_groups: Option<serde_json::Value>,
    pub department: Option<String>,
    pub images: Option<serde_json::Value>,
    pub nova_group: Option<i64>,
    pub nutrition_score: Option<String>,
    pub original_price: Option<String>,
    pub original_price_amount: Option<f64>,
    pub price: Option<String>,
    pub price_amount: Option<f64>,
    pub quantity: Option<i64>,
    pub serving_size: Option<String>,
    pub sku: Option<String>,
    pub sold_by_weight: Option<bool>,
    pub weight: Option<String>,
    pub weight_unit: Option<String>,
    pub weight_value: Option<f64>,
}

pub static PRODUCT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "product".into(),
    plural: Some("products".into()),
    description: Some("A purchasable item OR an identifiable product released into the world.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("aisle", FieldType::String),
        FieldDef::optional("availability", FieldType::String),
        FieldDef::optional("barcode", FieldType::String),
        FieldDef::optional("calories", FieldType::Number),
        FieldDef::optional("categories", FieldType::StringList),
        FieldDef::optional("category", FieldType::String),
        FieldDef::optional("currency", FieldType::String),
        FieldDef::optional("customizationGroups", FieldType::Json),
        FieldDef::optional("department", FieldType::String),
        FieldDef::optional("images", FieldType::Json),
        FieldDef::optional("novaGroup", FieldType::Integer),
        FieldDef::optional("nutritionScore", FieldType::String),
        FieldDef::optional("originalPrice", FieldType::String),
        FieldDef::optional("originalPriceAmount", FieldType::Number),
        FieldDef::optional("price", FieldType::String),
        FieldDef::optional("priceAmount", FieldType::Number),
        FieldDef::optional("quantity", FieldType::Integer),
        FieldDef::optional("servingSize", FieldType::String),
        FieldDef::optional("sku", FieldType::String),
        FieldDef::optional("soldByWeight", FieldType::Boolean),
        FieldDef::optional("weight", FieldType::String),
        FieldDef::optional("weightUnit", FieldType::String),
        FieldDef::optional("weightValue", FieldType::Number),
    ],
    out: vec![
        EdgeDef { label: "branded_as".into(), to: Some("brand".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "manufactured_by".into(), to: Some("organization".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "created_by".into(), to: Some("actor".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "inspired_by".into(), to: Some("product".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "tagged_with".into(), to: Some("tag".into()), from: None, card: Cardinality::Many },
    ],
    identity_any: vec!["url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("brand".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/Product + Offer".into(), url: Some("https://schema.org/Product".into()), notes: Some("Product on schema.org, price/priceAmount/currency/availability on nested Offer. Our sku/barcode map to sku/gtin13/gtin12; brand/manufacturer match directly. schema.org has `releaseDate` on Product (mirrors our `released`) but no formalized end-of-life property.".into()) },
        PriorArtDef { source: "Wikidata P2669 (discontinued date)".into(), url: Some("https://www.wikidata.org/wiki/Property:P2669".into()), notes: Some("Wikidata's canonical \"discontinued date\" property — broadly used across Wikidata's product entities (software, hardware, vehicles, consumer goods) with consistent semantics (\"date when a product ceased to be manufactured, supported, or available\"). Our `discontinued` field aligns directly. Wikidata P577 (publication date) similarly aligns with our `released`.".into()) },
        PriorArtDef { source: "schema.org/CreativeWork (creator, isBasedOn)".into(), url: Some("https://schema.org/CreativeWork".into()), notes: Some("Our `creator: actor[]` mirrors schema.org/creator (Person|Organization). Our `inspiredBy: product[]` maps to schema.org/isBasedOn (CreativeWork derivation/credit link); we keep the more readable name and broaden the target to any product so non-CreativeWork lineages (one aircraft type inspired by another, one OS inspired by another) work the same way.".into()) },
        PriorArtDef { source: "GS1 GTIN (UPC/EAN)".into(), url: Some("https://www.gs1.org/standards/id-keys/gtin".into()), notes: Some("Canonical barcode standard. Our barcode field is a GTIN-8/12/13/14; GS1 also underlies schema.org's gtin* properties.".into()) },
        PriorArtDef { source: "Open Food Facts API".into(), url: Some("https://openfoodfacts.github.io/openfoodfacts-server/api/".into()), notes: Some("Best practical source for food attributes. Our nutritionScore/novaGroup/calories/servingSize mirror nutriscore_grade/nova_group/nutriments.energy-kcal/serving_size.".into()) },
    ],
    ..ShapeDef::default()
});
