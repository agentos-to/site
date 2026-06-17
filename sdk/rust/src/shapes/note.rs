// DO NOT EDIT — generated from platform/ontology/shapes/note.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// Private text content, primarily for the author. Journal entries, PKM notes,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Note {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub is_pinned: Option<bool>,
    pub note_type: Option<String>,
}

pub static NOTE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "note".into(),
    plural: Some("notes".into()),
    description: Some("Private text content, primarily for the author. Journal entries, PKM notes,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("isPinned", FieldType::Boolean),
        FieldDef::optional("noteType", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("noteType".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Zettelkasten / Luhmann slip-box".into(), url: Some("https://zettelkasten.de/overview/".into()), notes: Some("Our noteType (fleeting/literature/permanent) is the canonical Zettelkasten triad; references[] ≈ Luhmann's permanent links.".into()) },
        PriorArtDef { source: "W3C Web Annotation Data Model".into(), url: Some("https://www.w3.org/TR/annotation-model/".into()), notes: Some("Our extractedFrom = target; createdBy = creator. Notes are annotations without a structured position selector.".into()) },
        PriorArtDef { source: "Obsidian / Roam / Logseq PKM conventions".into(), url: Some("https://obsidian.md/".into()), notes: Some("Practical PKM lineage. isPinned/noteType mirror the \"pinned/daily/permanent\" UX of modern note apps.".into()) },
    ],
    ..ShapeDef::default()
});
