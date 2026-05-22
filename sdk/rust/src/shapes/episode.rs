// DO NOT EDIT — generated from platform/ontology/shapes/episode.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A single episode of a podcast or show. Transcribable.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Episode {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub duration_ms: Option<i64>,
    pub episode_number: Option<i64>,
    pub season_number: Option<i64>,
}

pub static EPISODE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "episode".into(),
    plural: Some("episodes".into()),
    description: Some("A single episode of a podcast or show. Transcribable.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("durationMs", FieldType::Integer),
        FieldDef::optional("episodeNumber", FieldType::Integer),
        FieldDef::optional("seasonNumber", FieldType::Integer),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("author".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
