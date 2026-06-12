// DO NOT EDIT — generated from platform/ontology/shapes/transcript.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A text transcript of audio/video content. Linked from meetings and videos.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Transcript {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub content_role: Option<String>,
    pub duration_ms: Option<i64>,
    pub language: Option<String>,
    pub segment_count: Option<i64>,
    pub segments: Option<serde_json::Value>,
    pub source_type: Option<String>,
}

pub static TRANSCRIPT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "transcript".into(),
    plural: Some("transcripts".into()),
    description: Some("A text transcript of audio/video content. Linked from meetings and videos.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("contentRole", FieldType::String),
        FieldDef::optional("durationMs", FieldType::Integer),
        FieldDef::optional("language", FieldType::String),
        FieldDef::optional("segmentCount", FieldType::Integer),
        FieldDef::optional("segments", FieldType::Json),
        FieldDef::optional("sourceType", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("language".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "WebVTT (W3C)".into(), url: Some("https://www.w3.org/TR/webvtt1/".into()), notes: Some("Our segments are WebVTT cues (start/end/text). language follows WebVTT's LANGUAGE header.".into()) },
        PriorArtDef { source: "SRT SubRip Subtitles".into(), url: Some("https://matroska.org/technical/subtitles.html#srt-subtitles".into()), notes: Some("Practical alternative cue format. Same segment shape.".into()) },
        PriorArtDef { source: "Whisper JSON output".into(), url: Some("https://github.com/openai/whisper".into()), notes: Some("Practical source — many transcript apps return Whisper-shaped JSON (segments with start/end/text). Direct match.".into()) },
    ],
    ..ShapeDef::default()
});
