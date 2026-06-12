// DO NOT EDIT — generated from platform/ontology/shapes/actor.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// Base type for anything that can be attributed as "who did this" in the graph.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Actor {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub actor_type: Option<String>,
}

pub static ACTOR: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "actor".into(),
    plural: Some("actors".into()),
    description: Some("Base type for anything that can be attributed as \"who did this\" in the graph.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("actorType", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("actorType".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "FOAF Agent".into(), url: Some("http://xmlns.com/foaf/spec/#term_Agent".into()), notes: Some("FOAF Agent is the base class for Person, Organization, and Group. Our actorType mirrors FOAF's agent taxonomy.".into()) },
        PriorArtDef { source: "ActivityStreams 2.0 Actor".into(), url: Some("https://www.w3.org/TR/activitystreams-vocabulary/#actor-types".into()), notes: Some("AS2 defines Actor types (Person, Organization, Group, Service, Application). Our agent ≈ Service/Application.".into()) },
    ],
    ..ShapeDef::default()
});
