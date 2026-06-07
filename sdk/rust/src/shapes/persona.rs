// DO NOT EDIT — generated from platform/ontology/shapes/persona.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An archetype of an audience segment — a named, hypothetical user that
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Persona {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub goals: Option<Vec<String>>,
    pub headline: Option<String>,
    pub pain_points: Option<Vec<String>>,
    pub quote: Option<String>,
    pub reaches_for: Option<String>,
    pub who: Option<String>,
}

pub static PERSONA: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "persona".into(),
    plural: Some("personas".into()),
    description: Some("An archetype of an audience segment — a named, hypothetical user that".into()),
    icon: Some("user-round-search".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("goals", FieldType::StringList),
        FieldDef::optional("headline", FieldType::String),
        FieldDef::optional("painPoints", FieldType::StringList),
        FieldDef::optional("quote", FieldType::Text),
        FieldDef::optional("reachesFor", FieldType::Text),
        FieldDef::optional("who", FieldType::Text),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("headline".into()),
        body: Some("who".into()),
        highlights: vec!["reachesFor".into(), "quote".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
