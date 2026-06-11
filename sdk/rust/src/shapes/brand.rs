// DO NOT EDIT — generated from platform/ontology/shapes/brand.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A consumer brand — a named, visual, commercial identity. Often (but not
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Brand {
    pub name: String,
    pub text: Option<String>,
    pub url: String,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub country: Option<String>,
    pub primary_color: Option<String>,
    pub tagline: Option<String>,
    pub text_color: Option<String>,
}

pub static BRAND: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "brand".into(),
    plural: Some("brands".into()),
    description: Some("A consumer brand — a named, visual, commercial identity. Often (but not".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::required("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("country", FieldType::String),
        FieldDef::optional("primaryColor", FieldType::String),
        FieldDef::optional("tagline", FieldType::String),
        FieldDef::optional("textColor", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "owned_by".into(), to: Some("organization".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "online_at".into(), to: Some("website".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "depicted_by".into(), to: Some("image".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("tagline".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
