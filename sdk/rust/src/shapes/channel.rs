// DO NOT EDIT — generated from platform/ontology/shapes/channel.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A content channel — typically a YouTube channel. Videos are uploaded to channels.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Channel {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub banner: Option<String>,
    pub subscriber_count: Option<i64>,
}

pub static CHANNEL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "channel".into(),
    plural: Some("channels".into()),
    description: Some("A content channel — typically a YouTube channel. Videos are uploaded to channels.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("banner", FieldType::Url),
        FieldDef::optional("subscriberCount", FieldType::Integer),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("subscriberCount".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "ActivityStreams 2.0 Collection".into(), url: Some("https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection".into()), notes: Some("A channel is a platform-specific Collection of media items. Our banner is channel branding; AS2 doesn't model that directly.".into()) },
        PriorArtDef { source: "YouTube Data API — Channel resource".into(), url: Some("https://developers.google.com/youtube/v3/docs/channels".into()), notes: Some("Practical source. Our channel id/banner map to YouTube's channelId and brandingSettings.image.bannerExternalUrl.".into()) },
        PriorArtDef { source: "RSS 2.0 <channel>".into(), url: Some("https://www.rssboard.org/rss-specification".into()), notes: Some("Original \"channel\" concept — a grouped feed with title, image, and items. Our channel is the same pattern for video.".into()) },
    ],
    ..ShapeDef::default()
});
