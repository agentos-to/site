// DO NOT EDIT — generated from platform/ontology/shapes/principle.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A guiding bright-line — a value or rule used to judge edge cases. Universal:
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Principle {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub domain: Option<String>,
    pub rationale: Option<String>,
    pub statement: Option<String>,
    pub status: Option<String>,
}

pub static PRINCIPLE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "principle".into(),
    plural: Some("principles".into()),
    description: Some("A guiding bright-line — a value or rule used to judge edge cases. Universal:".into()),
    icon: Some("scale".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("domain", FieldType::String),
        FieldDef::optional("rationale", FieldType::Text),
        FieldDef::optional("statement", FieldType::Text),
        FieldDef::optional("status", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "held_by".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "supersedes".into(), to: Some("principle".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "conflicts_with".into(), to: Some("principle".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "governs".into(), to: Some("node".into()), from: None, card: Cardinality::One },
    ],
    display: Some(DisplaySpec {
        subtitle: Some("domain".into()),
        body: Some("rationale".into()),
        highlights: vec!["statement".into(), "status".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "principles.design".into(), url: Some("https://principles.design/".into()), notes: Some("1600+ principles modeled as name + statement + elaboration, grouped into named collections → name / statement / rationale.".into()) },
        PriorArtDef { source: "MADR (Markdown ADR) — decision drivers".into(), url: Some("https://adr.github.io/madr/".into()), notes: Some("Decision drivers are principles applied to a choice; the status enum (proposed/accepted/deprecated/superseded) → status + supersedes.".into()) },
        PriorArtDef { source: "GOV.UK Design Principles".into(), url: Some("https://www.gov.uk/guidance/government-design-principles".into()), notes: Some("Canonical 10-principle collection — each principle is an imperative statement + worked examples.".into()) },
    ],
    ..ShapeDef::default()
});
