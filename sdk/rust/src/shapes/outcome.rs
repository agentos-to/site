// DO NOT EDIT — generated from platform/ontology/shapes/outcome.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A tracked target-state — the change being sought, with a status and
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Outcome {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub archived: Option<bool>,
    pub baseline: Option<String>,
    pub current: Option<String>,
    pub metric: Option<String>,
    pub priority: Option<i64>,
    pub statement: Option<String>,
    pub status: Option<String>,
    pub target: Option<String>,
}

pub static OUTCOME: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "outcome".into(),
    plural: Some("outcomes".into()),
    description: Some("A tracked target-state — the change being sought, with a status and".into()),
    icon: Some("target".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("archived", FieldType::Boolean),
        FieldDef::optional("baseline", FieldType::String),
        FieldDef::optional("current", FieldType::String),
        FieldDef::optional("metric", FieldType::String),
        FieldDef::optional("priority", FieldType::Integer),
        FieldDef::optional("statement", FieldType::Text),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("target", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "depends_on".into(), to: Some("outcome".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "upholds".into(), to: Some("principle".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "serves".into(), to: Some("node".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "owns".into(), to: Some("node".into()), from: None, card: Cardinality::Many },
    ],
    display: Some(DisplaySpec {
        subtitle: Some("status".into()),
        body: Some("statement".into()),
        highlights: vec!["status".into(), "priority".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
