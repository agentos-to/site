// DO NOT EDIT — generated from platform/ontology/shapes/image.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An image file. Photos, screenshots, diagrams, artwork.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Image {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub alt_text: Option<String>,
    pub app_name: Option<String>,
    pub copyright_year: Option<i64>,
    pub coverage: Option<String>,
    pub date_created: Option<String>,
    pub description: Option<String>,
    pub display_id: Option<i64>,
    pub display_index: Option<i64>,
    pub encoding: Option<String>,
    pub filename: Option<String>,
    pub format: Option<String>,
    pub height: Option<i64>,
    pub kind: Option<String>,
    pub language: Option<String>,
    pub license: Option<String>,
    pub line_count: Option<i64>,
    pub mime_type: Option<String>,
    pub path: Option<String>,
    pub sha: Option<String>,
    pub size: Option<i64>,
    pub tags: Option<Vec<String>>,
    pub width: Option<i64>,
    pub window_id: Option<i64>,
}

pub static IMAGE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "image".into(),
    plural: Some("images".into()),
    description: Some("An image file. Photos, screenshots, diagrams, artwork.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("altText", FieldType::String),
        FieldDef::optional("appName", FieldType::String),
        FieldDef::optional("copyrightYear", FieldType::Integer),
        FieldDef::optional("coverage", FieldType::String),
        FieldDef::optional("dateCreated", FieldType::Date),
        FieldDef::optional("description", FieldType::String),
        FieldDef::optional("displayId", FieldType::Integer),
        FieldDef::optional("displayIndex", FieldType::Integer),
        FieldDef::optional("encoding", FieldType::String),
        FieldDef::optional("filename", FieldType::String),
        FieldDef::optional("format", FieldType::String),
        FieldDef::optional("height", FieldType::Integer),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("language", FieldType::String),
        FieldDef::optional("license", FieldType::String),
        FieldDef::optional("lineCount", FieldType::Integer),
        FieldDef::optional("mimeType", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("sha", FieldType::String),
        FieldDef::optional("size", FieldType::Integer),
        FieldDef::optional("tags", FieldType::StringList),
        FieldDef::optional("width", FieldType::Integer),
        FieldDef::optional("windowId", FieldType::Integer),
    ],
    also: vec!["creative_work".into(), "file".into()],
    identity_any: vec!["sha".into(), "url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("format".into()),
        image: Some("image".into()),
        body: Some("description".into()),
        highlights: vec!["datePublished".into(), "published_by".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/ImageObject".into(), url: Some("https://schema.org/ImageObject".into()), notes: Some("Our width/height = width/height; format ≈ encodingFormat; altText = caption/accessibilityCaption.".into()) },
        PriorArtDef { source: "IANA Media Types (image/*)".into(), url: Some("https://www.iana.org/assignments/media-types/media-types.xhtml#image".into()), notes: Some("Our format values (PNG, JPEG, WebP, SVG) align with registered image/* media types.".into()) },
        PriorArtDef { source: "Exif 2.3 (JEITA CP-3451)".into(), url: Some("https://www.cipa.jp/std/documents/e/DC-008-Translation-2019-E.pdf".into()), notes: Some("Source of most image metadata fields. width/height come from Exif PixelXDimension/PixelYDimension.".into()) },
    ],
    ..ShapeDef::default()
});
