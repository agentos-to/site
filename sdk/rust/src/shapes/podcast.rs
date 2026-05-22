// DO NOT EDIT — generated from platform/ontology/shapes/podcast.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use agentos_graph::{
    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,
    ShapeDef, ShortcutDef,
};
use once_cell::sync::Lazy;
use serde::{Deserialize, Serialize};

/// A podcast series. Contains episodes. Not the audio itself — that's on the episode.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Podcast {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub feed_url: Option<String>,
}

pub static PODCAST: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "podcast".into(),
    plural: Some("podcasts".into()),
    description: Some("A podcast series. Contains episodes. Not the audio itself — that's on the episode.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("feedUrl", FieldType::Url),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("host".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
