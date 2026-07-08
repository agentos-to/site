// DO NOT EDIT — generated from platform/ontology/shapes/playlist.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A video playlist. Playlists are lists that contain videos instead of products.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Playlist {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub account: Option<String>,
    pub arrangement: Option<String>,
    #[serde(rename = "default_view")]
    pub default_view: Option<String>,
    #[serde(rename = "icon_size")]
    pub icon_size: Option<i64>,
    pub is_default: Option<bool>,
    pub is_public: Option<bool>,
    pub item_count: Option<i64>,
    pub list_id: Option<String>,
    pub list_type: Option<String>,
    #[serde(rename = "member_shape")]
    pub member_shape: Option<String>,
    pub mirror_key: Option<String>,
    #[serde(rename = "ordering_mode")]
    pub ordering_mode: Option<String>,
    pub path: Option<String>,
    pub privacy: Option<String>,
    pub provider: Option<String>,
    pub service: Option<String>,
    #[serde(rename = "sort_by")]
    pub sort_by: Option<String>,
    pub surface: Option<serde_json::Value>,
    pub tool: Option<String>,
}

pub static PLAYLIST: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "playlist".into(),
    plural: Some("playlists".into()),
    description: Some("A video playlist. Playlists are lists that contain videos instead of products.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("account", FieldType::String),
        FieldDef::optional("arrangement", FieldType::String),
        FieldDef::optional("default_view", FieldType::String),
        FieldDef::optional("icon_size", FieldType::Integer),
        FieldDef::optional("isDefault", FieldType::Boolean),
        FieldDef::optional("isPublic", FieldType::Boolean),
        FieldDef::optional("itemCount", FieldType::Integer),
        FieldDef::optional("listId", FieldType::String),
        FieldDef::optional("listType", FieldType::String),
        FieldDef::optional("member_shape", FieldType::String),
        FieldDef::optional("mirrorKey", FieldType::String),
        FieldDef::optional("ordering_mode", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("privacy", FieldType::String),
        FieldDef::optional("provider", FieldType::String),
        FieldDef::optional("service", FieldType::String),
        FieldDef::optional("sort_by", FieldType::String),
        FieldDef::optional("surface", FieldType::Json),
        FieldDef::optional("tool", FieldType::String),
    ],
    also: vec!["list".into()],
    display: Some(DisplaySpec {
        subtitle: Some("text".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/MusicPlaylist / ItemList".into(), url: Some("https://schema.org/MusicPlaylist".into()), notes: Some("Our contains(video[]) ≈ track/itemListElement. We generalize beyond music to any ordered media list.".into()) },
        PriorArtDef { source: "YouTube Data API — Playlist".into(), url: Some("https://developers.google.com/youtube/v3/docs/playlists".into()), notes: Some("Practical source. Playlist = ordered Video collection — inherits list identity semantics.".into()) },
    ],
    ..ShapeDef::default()
});
