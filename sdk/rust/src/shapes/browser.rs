// DO NOT EDIT — generated from platform/ontology/shapes/browser.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A web browser installed on this machine — a Chromium-family (or, later,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Browser {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub app_name: Option<String>,
    pub installed: Option<bool>,
    pub macos_default: Option<bool>,
}

pub static BROWSER: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "browser".into(),
    plural: Some("browsers".into()),
    description: Some("A web browser installed on this machine — a Chromium-family (or, later,".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("appName", FieldType::String),
        FieldDef::optional("installed", FieldType::Boolean),
        FieldDef::optional("macosDefault", FieldType::Boolean),
    ],
    identity: vec!["id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("appName".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "xdg-settings / LaunchServices default handler".into(), url: Some("https://specifications.freedesktop.org/mime-apps-spec/latest/".into()), notes: Some("Both macOS (LaunchServices' https handler) and Linux (xdg-settings get default-web-browser) model \"the default browser\" as an OS registry over detected installs. Same split here: detection owns existence, a user preference owns the pick.".into()) },
    ],
    ..ShapeDef::default()
});
