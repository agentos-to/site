// DO NOT EDIT — generated from platform/ontology/shapes/tax_line.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A single tax, fee, or surcharge line item on a priced commerce
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct TaxLine {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub amount: Option<f64>,
    pub applies_to_index: Option<i64>,
    pub code: Option<String>,
    pub country: Option<String>,
    pub currency: Option<String>,
    pub description: Option<String>,
    pub inclusive: Option<bool>,
    pub kind: Option<String>,
    pub merchant_imposed: Option<bool>,
    pub nature: Option<String>,
    pub rate: Option<f64>,
    pub refundable: Option<bool>,
    pub taxable_amount: Option<f64>,
}

pub static TAX_LINE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "tax_line".into(),
    plural: Some("tax_lines".into()),
    description: Some("A single tax, fee, or surcharge line item on a priced commerce".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("amount", FieldType::Number),
        FieldDef::optional("appliesToIndex", FieldType::Integer),
        FieldDef::optional("code", FieldType::String),
        FieldDef::optional("country", FieldType::String),
        FieldDef::optional("currency", FieldType::String),
        FieldDef::optional("description", FieldType::String),
        FieldDef::optional("inclusive", FieldType::Boolean),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("merchantImposed", FieldType::Boolean),
        FieldDef::optional("nature", FieldType::String),
        FieldDef::optional("rate", FieldType::Number),
        FieldDef::optional("refundable", FieldType::Boolean),
        FieldDef::optional("taxableAmount", FieldType::Number),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("description".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
