// DO NOT EDIT — generated from platform/ontology/shapes/episode.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

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
    prior_art: vec![
        PriorArtDef { source: "Apple Podcasts RSS Extensions (itunes:episode)".into(), url: Some("https://help.apple.com/itc/podcasts_connect/#/itcb54353390".into()), notes: Some("De-facto podcast metadata standard. Our episodeNumber/seasonNumber/ durationMs = itunes:episode/itunes:season/itunes:duration.".into()) },
        PriorArtDef { source: "schema.org/PodcastEpisode".into(), url: Some("https://schema.org/PodcastEpisode".into()), notes: Some("Our series ≈ partOfSeries (PodcastSeries); transcribe ≈ transcript; guest ≈ actor.".into()) },
        PriorArtDef { source: "Podcast Namespace (podcast:*)".into(), url: Some("https://podcastindex.org/namespace/1.0".into()), notes: Some("Modern open extension to RSS. Covers our guest, season, episode, and transcript relations via podcast:person, podcast:season, etc.".into()) },
    ],
    ..ShapeDef::default()
});
