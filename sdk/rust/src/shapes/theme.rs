// DO NOT EDIT — generated from platform/ontology/shapes/agentos/theme.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An OS theme — a named knob-vector over its family's structure.
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
    pub family: Option<String>,
    pub start_menu: Option<String>,
    pub style: Option<String>,
    pub theme_id: String,
}

pub static THEME: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "theme".into(),
    plural: Some("themes".into()),
    description: Some("An OS theme — a named knob-vector over its family's structure.".into()),
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
        FieldDef::optional("family", FieldType::String),
        FieldDef::optional("startMenu", FieldType::String),
        FieldDef::optional("style", FieldType::String),
        FieldDef::required("themeId", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "represents".into(), to: Some("product".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["themeId".into()],
    display: Some(DisplaySpec {
        subtitle: Some("family".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "System theme APIs (macOS NSAppearance, Windows WinUI)".into(), url: Some("https://developer.apple.com/documentation/appkit/nsappearance".into()), notes: Some("OS-level theme abstraction. Our `family` parallels NSAppearance.Name (aqua, darkAqua) and Windows theme families.".into()) },
    ],
    ..ShapeDef::default()
});
