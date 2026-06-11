// DO NOT EDIT — generated from platform/ontology/shapes/quantity-kind.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A quantity kind — WHAT is being measured, semantically. "Mass
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct QuantityKind {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub key: String,
    pub label: Option<String>,
}

pub static QUANTITY_KIND: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "quantity-kind".into(),
    plural: Some("quantity-kinds".into()),
    description: Some("A quantity kind — WHAT is being measured, semantically. \"Mass".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::required("key", FieldType::String),
        FieldDef::optional("label", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "measures".into(), to: Some("dimension".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "specialization_of".into(), to: Some("quantity-kind".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["key".into()],
    display: Some(DisplaySpec {
        subtitle: Some("label".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
