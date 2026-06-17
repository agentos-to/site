// DO NOT EDIT — generated from platform/ontology/shapes/podcast.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

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
    prior_art: vec![
        PriorArtDef { source: "RSS 2.0 (feed + channel)".into(), url: Some("https://www.rssboard.org/rss-specification".into()), notes: Some("Our feedUrl is a canonical RSS feed URL; episodes relation ≈ channel's item elements.".into()) },
        PriorArtDef { source: "Apple Podcasts RSS extensions (itunes:*)".into(), url: Some("https://help.apple.com/itc/podcasts_connect/#/itcb54353390".into()), notes: Some("De-facto standard. Our host[] ≈ itunes:author; our series-episode hierarchy aligns with itunes:episode/itunes:season.".into()) },
        PriorArtDef { source: "Podcast Namespace (podcast:*)".into(), url: Some("https://podcastindex.org/namespace/1.0".into()), notes: Some("Modern open extension. podcast:person covers guests/hosts; podcast:transcript covers our transcribe relation.".into()) },
    ],
    ..ShapeDef::default()
});
