// DO NOT EDIT — generated from platform/ontology/shapes/font.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A typeface — the family-level work. One node per font family
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Font {
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
    pub designer_url: Option<String>,
    pub family: Option<String>,
    pub formats: Option<Vec<String>>,
    pub generic_family: Option<String>,
    pub glyph_count: Option<i64>,
    pub language: Option<String>,
    pub license: Option<String>,
    pub license_info_url: Option<String>,
    pub postscript_name: Option<String>,
    pub scripts: Option<Vec<String>>,
    pub styles: Option<Vec<String>>,
    pub tags: Option<Vec<String>>,
    pub vendor_url: Option<String>,
    pub weights: Option<Vec<i64>>,
}

pub static FONT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "font".into(),
    plural: Some("fonts".into()),
    description: Some("A typeface — the family-level work. One node per font family".into()),
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
        FieldDef::optional("designerUrl", FieldType::String),
        FieldDef::optional("family", FieldType::String),
        FieldDef::optional("formats", FieldType::StringList),
        FieldDef::optional("genericFamily", FieldType::String),
        FieldDef::optional("glyphCount", FieldType::Integer),
        FieldDef::optional("language", FieldType::String),
        FieldDef::optional("license", FieldType::String),
        FieldDef::optional("licenseInfoUrl", FieldType::String),
        FieldDef::optional("postscriptName", FieldType::String),
        FieldDef::optional("scripts", FieldType::StringList),
        FieldDef::optional("styles", FieldType::StringList),
        FieldDef::optional("tags", FieldType::StringList),
        FieldDef::optional("vendorUrl", FieldType::String),
        FieldDef::optional("weights", FieldType::IntegerList),
    ],
    also: vec!["creative_work".into()],
    identity_any: vec!["family".into(), "postscriptName".into()],
    display: Some(DisplaySpec {
        subtitle: Some("author".into()),
        image: Some("image".into()),
        body: Some("description".into()),
        highlights: vec!["datePublished".into(), "published_by".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/Typeface".into(), url: Some("https://schema.org/Typeface".into()), notes: Some("Schema.org added Typeface in 2024. Sparse compared to OpenType (fontFamily, format only) — we lean on the OpenType `name` table for most fields.".into()) },
        PriorArtDef { source: "OpenType `name` table (ISO/IEC 14496-22)".into(), url: Some("https://learn.microsoft.com/en-us/typography/opentype/spec/name".into()), notes: Some("nameID 1=family; 6=postscriptName; 8=manufacturer (publisher in our model, via creative_work); 9=designer (author via creative_work); 13=licenseDescription (license via creative_work); 14=licenseInfoUrl; 11=vendorUrl; 12=designerUrl. Our font shape is a graph-native projection of this table; .woff2 metadata can round-trip losslessly.".into()) },
        PriorArtDef { source: "Google Fonts metadata".into(), url: Some("https://fonts.google.com/specimen/Roboto".into()), notes: Some("Treats fonts as \"families\" with weights / styles arrays. Same model we adopt. Google Fonts also tracks subsets (Latin / Cyrillic / Greek) — equivalent to our scripts field.".into()) },
        PriorArtDef { source: "ISO 15924 (script codes)".into(), url: Some("https://www.unicode.org/iso15924/iso15924-codes.html".into()), notes: Some("Our scripts field uses ISO 15924 four-letter codes (Latn / Cyrl / Grek / Arab / Hans / Hant / Jpan / Kore / etc.). Canonical identification of writing systems.".into()) },
    ],
    ..ShapeDef::default()
});
