// DO NOT EDIT — generated from platform/ontology/shapes/cursor.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A mouse-pointer image — the arrow, the I-beam, the hand, the resize
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Cursor {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub copyright_year: Option<i64>,
    pub coverage: Option<String>,
    pub date_created: Option<String>,
    pub description: Option<String>,
    pub dimension: Option<i64>,
    pub encoding: Option<String>,
    pub filename: Option<String>,
    pub format: Option<String>,
    pub hotspot_x: Option<i64>,
    pub hotspot_y: Option<i64>,
    pub kind: Option<String>,
    pub language: Option<String>,
    pub license: Option<String>,
    pub line_count: Option<i64>,
    pub mime_type: Option<String>,
    pub path: Option<String>,
    pub purpose: Option<String>,
    pub sha: Option<String>,
    pub size: Option<i64>,
    pub tags: Option<Vec<String>>,
}

pub static CURSOR: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "cursor".into(),
    plural: Some("cursors".into()),
    description: Some("A mouse-pointer image — the arrow, the I-beam, the hand, the resize".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("copyrightYear", FieldType::Integer),
        FieldDef::optional("coverage", FieldType::String),
        FieldDef::optional("dateCreated", FieldType::Date),
        FieldDef::optional("description", FieldType::String),
        FieldDef::optional("dimension", FieldType::Integer),
        FieldDef::optional("encoding", FieldType::String),
        FieldDef::optional("filename", FieldType::String),
        FieldDef::optional("format", FieldType::String),
        FieldDef::optional("hotspotX", FieldType::Integer),
        FieldDef::optional("hotspotY", FieldType::Integer),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("language", FieldType::String),
        FieldDef::optional("license", FieldType::String),
        FieldDef::optional("lineCount", FieldType::Integer),
        FieldDef::optional("mimeType", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("purpose", FieldType::String),
        FieldDef::optional("sha", FieldType::String),
        FieldDef::optional("size", FieldType::Integer),
        FieldDef::optional("tags", FieldType::StringList),
    ],
    also: vec!["creative_work".into(), "file".into()],
    identity_any: vec!["sha".into(), "url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("purpose".into()),
        image: Some("image".into()),
        body: Some("description".into()),
        highlights: vec!["datePublished".into(), "published_by".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "CSS UI `cursor` property".into(), url: Some("https://www.w3.org/TR/css-ui-4/#cursor".into()), notes: Some("The render contract: `cursor: url(<url>) <hotspotX> <hotspotY>, <keyword>`. Our hotspotX/hotspotY ARE the `<x> <y>` the spec needs for image cursors; purpose maps to the trailing keyword.".into()) },
        PriorArtDef { source: "Windows .cur / .ani cursor format".into(), url: Some("https://learn.microsoft.com/en-us/windows/win32/menurc/about-cursors".into()), notes: Some("Source format of the bundled XP scheme — the .cur header carries the hotspot in its image-directory entry (bytes 4–7), which we read and record as hotspotX/hotspotY when downscaling to PNG. `.ani` (animated) is excluded — browsers don't support it in CSS cursor.".into()) },
        PriorArtDef { source: "schema.org/ImageObject".into(), url: Some("https://schema.org/ImageObject".into()), notes: Some("A cursor is an image artifact; most metadata (author, license, datePublished) comes from creative_work via `also`, dimension ≈ width/height.".into()) },
    ],
    ..ShapeDef::default()
});
