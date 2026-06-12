// DO NOT EDIT — generated from platform/ontology/shapes/project.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A project that groups tasks. Tasks belong to projects.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Project {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub color: Option<String>,
    pub parent_id: Option<String>,
    pub state: Option<String>,
}

pub static PROJECT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "project".into(),
    plural: Some("projects".into()),
    description: Some("A project that groups tasks. Tasks belong to projects.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("color", FieldType::String),
        FieldDef::optional("parentId", FieldType::String),
        FieldDef::optional("state", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "at_namespace".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("state".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Linear API — Project".into(), url: Some("https://developers.linear.app/docs/graphql/working-with-the-graphql-api".into()), notes: Some("Our state/color come directly from Linear's Project model.".into()) },
        PriorArtDef { source: "GitHub Projects (v2)".into(), url: Some("https://docs.github.com/en/graphql/reference/objects#projectv2".into()), notes: Some("Canonical open-source project-board model. state ≈ ProjectV2SingleSelectFieldOption; color is per-field metadata.".into()) },
        PriorArtDef { source: "schema.org/Project".into(), url: Some("https://schema.org/Project".into()), notes: Some("Generic project-as-effort type. Thinner than the practical APIs; mainly useful for outbound JSON-LD.".into()) },
    ],
    ..ShapeDef::default()
});
