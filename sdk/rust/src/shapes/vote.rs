// DO NOT EDIT — generated from platform/ontology/shapes/vote.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A dated, directional endorsement of an issue. Each cast is its OWN node,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Vote {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub direction: Option<String>,
    pub instance: Option<String>,
    pub note: Option<String>,
}

pub static VOTE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "vote".into(),
    plural: Some("votes".into()),
    description: Some("A dated, directional endorsement of an issue. Each cast is its OWN node,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("direction", FieldType::String),
        FieldDef::optional("instance", FieldType::String),
        FieldDef::optional("note", FieldType::Text),
    ],
    out: vec![
        EdgeDef { label: "for".into(), to: Some("issue".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "cast_by".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
    ],
    display: Some(DisplaySpec {
        subtitle: Some("direction".into()),
        body: Some("note".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Canny / Featurebase vote object".into(), url: Some("https://developers.canny.io/api-reference".into()), notes: Some("A vote is an object (voter + post + created date), not a counter — so duplicates merge and votes roll up. Our `for`/`cast_by`/`date` mirror Canny's post/voter/created; score is derived from the set, never stored.".into()) },
        PriorArtDef { source: "ActivityStreams 2.0 Like".into(), url: Some("https://www.w3.org/TR/activitystreams-vocabulary/#dfn-like".into()), notes: Some("A Like is an Activity with actor + object — our cast_by ≈ actor, for ≈ object. We add `direction` (up/down) and `note`/`instance` for evidence-bearing agent recurrence, which AS2 Like lacks.".into()) },
    ],
    ..ShapeDef::default()
});
