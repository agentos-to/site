// DO NOT EDIT — generated from platform/ontology/shapes/payment_method.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A saved payment instrument — credit/debit card, PayPal/Venmo account,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct PaymentMethod {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub balance: Option<f64>,
    pub bin_range: Option<String>,
    pub brand: Option<String>,
    pub currency: Option<String>,
    pub custom_description: Option<String>,
    pub display_name: Option<String>,
    pub exp_month: Option<i64>,
    pub exp_year: Option<i64>,
    pub expiration_date: Option<String>,
    pub fingerprint: Option<String>,
    pub holder_name: Option<String>,
    pub identifier: String,
    pub is_default: Option<bool>,
    pub is_expired: Option<bool>,
    pub is_primary: Option<bool>,
    pub is_selected: Option<bool>,
    pub last4: Option<String>,
    pub metadata: Option<serde_json::Value>,
    pub provider_tokens: Option<serde_json::Value>,
    pub status: Option<String>,
    pub subtype: Option<String>,
    pub type_: Option<String>,
}

pub static PAYMENT_METHOD: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "payment_method".into(),
    plural: Some("payment_methods".into()),
    description: Some("A saved payment instrument — credit/debit card, PayPal/Venmo account,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("balance", FieldType::Number),
        FieldDef::optional("binRange", FieldType::String),
        FieldDef::optional("brand", FieldType::String),
        FieldDef::optional("currency", FieldType::String),
        FieldDef::optional("customDescription", FieldType::String),
        FieldDef::optional("displayName", FieldType::String),
        FieldDef::optional("expMonth", FieldType::Integer),
        FieldDef::optional("expYear", FieldType::Integer),
        FieldDef::optional("expirationDate", FieldType::String),
        FieldDef::optional("fingerprint", FieldType::String),
        FieldDef::optional("holderName", FieldType::String),
        FieldDef::required("identifier", FieldType::String),
        FieldDef::optional("isDefault", FieldType::Boolean),
        FieldDef::optional("isExpired", FieldType::Boolean),
        FieldDef::optional("isPrimary", FieldType::Boolean),
        FieldDef::optional("isSelected", FieldType::Boolean),
        FieldDef::optional("last4", FieldType::String),
        FieldDef::optional("metadata", FieldType::Json),
        FieldDef::optional("providerTokens", FieldType::Json),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("subtype", FieldType::String),
        FieldDef::optional("type", FieldType::String),
    ],
    identity: vec!["at".into(), "identifier".into()],
    display: Some(DisplaySpec {
        subtitle: Some("displayName".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
