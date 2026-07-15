// DO NOT EDIT — generated from platform/ontology/shapes/software_license.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A purchased entitlement to use a software product — the license record
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct SoftwareLicense {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub expiry_date: Option<String>,
    pub license_key_last4: Option<String>,
    pub licensed_to: String,
    pub order_number: Option<String>,
    pub product_name: String,
    pub purchase_date: Option<String>,
    pub seats: Option<i64>,
    pub secret_ref: Option<String>,
    pub version: Option<String>,
}

pub static SOFTWARE_LICENSE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "software_license".into(),
    plural: Some("software_licenses".into()),
    description: Some("A purchased entitlement to use a software product — the license record".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("expiryDate", FieldType::Datetime),
        FieldDef::optional("licenseKeyLast4", FieldType::String),
        FieldDef::required("licensedTo", FieldType::String),
        FieldDef::optional("orderNumber", FieldType::String),
        FieldDef::required("productName", FieldType::String),
        FieldDef::optional("purchaseDate", FieldType::Datetime),
        FieldDef::optional("seats", FieldType::Integer),
        FieldDef::optional("secretRef", FieldType::String),
        FieldDef::optional("version", FieldType::String),
    ],
    timed: Some("self".into()),
    identity: vec!["productName".into(), "licensedTo".into()],
    display: Some(DisplaySpec {
        subtitle: Some("productName".into()),
        highlights: vec!["version".into(), "seats".into(), "expiryDate".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "1Password \"Software License\" item category".into(), url: Some("https://support.1password.com/item-categories/".into()), notes: Some("The direct source. 1P's Software License item holds product version, licensed to, license key, order number, order date, seats. We keep every field EXCEPT the key value — the key is a `password`/secret field in 1P and stays a secret here too (licenseKeyLast4 + secretRef only).".into()) },
        PriorArtDef { source: "schema.org/SoftwareApplication + Offer/Order".into(), url: Some("https://schema.org/SoftwareApplication".into()), notes: Some("The licensed product is a schema.org SoftwareApplication (our `software` relation); the license itself is closer to an Order / Offer acceptance — orderNumber ≈ Order.orderNumber, purchaseDate ≈ orderDate. No single schema.org type covers a seat-based key, so we model it explicitly.".into()) },
        PriorArtDef { source: "SPDX license identifiers".into(), url: Some("https://spdx.org/licenses/".into()), notes: Some("For OSS the \"license\" is a well-known SPDX id (MIT, GPL-3.0) with no key or seat count — that lives on the `software` product, not here. This shape is for PURCHASED per-seat commercial keys, which SPDX does not model.".into()) },
    ],
    ..ShapeDef::default()
});
