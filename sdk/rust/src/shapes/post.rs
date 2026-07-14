// DO NOT EDIT — generated from platform/ontology/shapes/post.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A piece of published content — a Reddit submission, HN story, YouTube upload,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Post {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub comment_count: Option<i64>,
    pub community: Option<String>,
    pub expires_at: Option<String>,
    pub external_url: Option<String>,
    pub is_outgoing: Option<bool>,
    pub post_type: Option<String>,
    pub score: Option<i64>,
}

pub static POST: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "post".into(),
    plural: Some("posts".into()),
    description: Some("A piece of published content — a Reddit submission, HN story, YouTube upload,".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("commentCount", FieldType::Integer),
        FieldDef::optional("community", FieldType::String),
        FieldDef::optional("expiresAt", FieldType::Datetime),
        FieldDef::optional("externalUrl", FieldType::Url),
        FieldDef::optional("isOutgoing", FieldType::Boolean),
        FieldDef::optional("postType", FieldType::String),
        FieldDef::optional("score", FieldType::Integer),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("author".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "ActivityStreams 2.0 (Note/Article + Create)".into(), url: Some("https://www.w3.org/TR/activitystreams-vocabulary/".into()), notes: Some("Fediverse post model. Our postedBy ≈ actor/attributedTo; publish(community) ≈ audience/to; repliesTo/replies ≈ inReplyTo/replies; media/attachment ≈ attachment.".into()) },
        PriorArtDef { source: "OpenGraph protocol".into(), url: Some("https://ogp.me/".into()), notes: Some("How posts surface when linked. Our externalUrl + media[] correspond to og:url and og:image/og:video; postType loosely parallels og:type (article, video).".into()) },
        PriorArtDef { source: "ATProto app.bsky.feed.post".into(), url: Some("https://atproto.com/lexicons/app-bsky-feed".into()), notes: Some("Modern practical lexicon. Our repliesTo ≈ reply.parent; media ≈ embed.images; externalUrl ≈ embed.external.".into()) },
    ],
    ..ShapeDef::default()
});
