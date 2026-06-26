// DO NOT EDIT — generated from platform/ontology/shapes/agentos/theme.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An OS theme — a self-contained runtime pack.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Theme {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub default_background_color: Option<String>,
    pub description: Option<String>,
    pub theme_id: String,
}

pub static THEME: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "theme".into(),
    plural: Some("themes".into()),
    description: Some("An OS theme — a self-contained runtime pack.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("defaultBackgroundColor", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::required("themeId", FieldType::String),
    ],
    identity: vec!["themeId".into()],
    prior_art: vec![
        PriorArtDef { source: "System theme APIs (macOS NSAppearance, Windows WinUI)".into(), url: Some("https://developer.apple.com/documentation/appkit/nsappearance".into()), notes: Some("OS-level theme abstraction — a named appearance the whole shell reads (aqua, darkAqua). Ours is a runtime pack stacked over the default floor.".into()) },
    ],
    ..ShapeDef::default()
});
