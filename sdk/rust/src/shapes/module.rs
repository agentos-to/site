// DO NOT EDIT — generated from platform/ontology/shapes/module.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A self-contained unit of a larger whole — a software module, a course
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Module {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub path: Option<String>,
    pub planned: Option<bool>,
    pub role: Option<String>,
    pub status: Option<String>,
    pub version: Option<String>,
}

pub static MODULE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "module".into(),
    plural: Some("modules".into()),
    description: Some("A self-contained unit of a larger whole — a software module, a course".into()),
    icon: Some("package".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("planned", FieldType::Boolean),
        FieldDef::optional("role", FieldType::Text),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("version", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "part_of".into(), to: Some("node".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "has_part".into(), to: Some("module".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "depends_on".into(), to: Some("module".into()), from: None, card: Cardinality::Many },
    ],
    display: Some(DisplaySpec {
        subtitle: Some("role".into()),
        highlights: vec!["status".into(), "path".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
