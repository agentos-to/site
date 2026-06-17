// DO NOT EDIT — generated from platform/ontology/shapes/video.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A video file — the media artifact, not the social context around it.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Video {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub codec: Option<String>,
    pub copyright_year: Option<i64>,
    pub coverage: Option<String>,
    pub date_created: Option<String>,
    pub description: Option<String>,
    pub duration_ms: Option<i64>,
    pub encoding: Option<String>,
    pub filename: Option<String>,
    pub format: Option<String>,
    pub frame_rate: Option<f64>,
    pub kind: Option<String>,
    pub language: Option<String>,
    pub license: Option<String>,
    pub line_count: Option<i64>,
    pub mime_type: Option<String>,
    pub path: Option<String>,
    pub resolution: Option<String>,
    pub sha: Option<String>,
    pub size: Option<i64>,
    pub tags: Option<Vec<String>>,
    pub view_count: Option<i64>,
}

pub static VIDEO: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "video".into(),
    plural: Some("videos".into()),
    description: Some("A video file — the media artifact, not the social context around it.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("codec", FieldType::String),
        FieldDef::optional("copyrightYear", FieldType::Integer),
        FieldDef::optional("coverage", FieldType::String),
        FieldDef::optional("dateCreated", FieldType::Date),
        FieldDef::optional("description", FieldType::String),
        FieldDef::optional("durationMs", FieldType::Integer),
        FieldDef::optional("encoding", FieldType::String),
        FieldDef::optional("filename", FieldType::String),
        FieldDef::optional("format", FieldType::String),
        FieldDef::optional("frameRate", FieldType::Number),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("language", FieldType::String),
        FieldDef::optional("license", FieldType::String),
        FieldDef::optional("lineCount", FieldType::Integer),
        FieldDef::optional("mimeType", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("resolution", FieldType::String),
        FieldDef::optional("sha", FieldType::String),
        FieldDef::optional("size", FieldType::Integer),
        FieldDef::optional("tags", FieldType::StringList),
        FieldDef::optional("viewCount", FieldType::Integer),
    ],
    also: vec!["creative_work".into(), "file".into()],
    identity_any: vec!["sha".into(), "url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("author".into()),
        image: Some("image".into()),
        body: Some("description".into()),
        highlights: vec!["datePublished".into(), "published_by".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/VideoObject".into(), url: Some("https://schema.org/VideoObject".into()), notes: Some("Our durationMs ≈ duration (ISO 8601 period); resolution ≈ videoFrameSize; frameRate has no direct property; codec ≈ encodingFormat.".into()) },
        PriorArtDef { source: "IANA Media Types (video/*)".into(), url: Some("https://www.iana.org/assignments/media-types/media-types.xhtml#video".into()), notes: Some("Our codec values map to registered video/* media types (mp4, webm, ogg).".into()) },
        PriorArtDef { source: "MPEG / ITU video codec specs".into(), url: Some("https://www.itu.int/rec/T-REC-H.264".into()), notes: Some("Canonical codec definitions. Our codec values are MPEG/ITU codec short names (h264, vp9, av1).".into()) },
    ],
    ..ShapeDef::default()
});
