// DO NOT EDIT — generated from platform/ontology/shapes/settings.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An AgentOS settings node — the user's portable configuration store,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Settings {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
}

pub static SETTINGS: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "settings".into(),
    plural: Some("settings".into()),
    description: Some("An AgentOS settings node — the user's portable configuration store,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "macOS ~/Library/Application Support + Preferences".into(), url: Some("https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html".into()), notes: Some("Direct precedent. macOS keeps per-user, per-app configuration in the user's home Library — portable with the home directory, one subdirectory per app. Our parent settings node mirrors Preferences (the OS defaults domain); each `--configures-->` app node mirrors one Application Support/<App> directory. We diverge by living in the graph (queryable, cascade-resolved) rather than plist files on disk.".into()) },
        PriorArtDef { source: "XDG Base Directory ($XDG_CONFIG_HOME)".into(), url: Some("https://specifications.freedesktop.org/basedir-spec/latest/".into()), notes: Some("The Linux convention: user config under ~/.config/<app>, machine state kept separate. Same person-vs-machine seam we draw between this home settings store and the System-resident seat.".into()) },
    ],
    prefs_schemas: serde_json::from_str("{\"ui\": [{\"key\": \"themeId\", \"kind\": \"select\", \"label\": \"Theme\", \"description\": \"Desktop theme \\u2014 window chrome, fonts, sounds.\", \"group\": \"Theme\", \"optionsShape\": \"theme\", \"optionsVolume\": \"system\", \"optionsValue\": \"themeId\", \"optionsLabel\": \"name\", \"optionsNone\": \"Base\"}, {\"key\": \"fontSize\", \"kind\": \"number\", \"label\": \"Font Size\", \"description\": \"Base UI font size in pixels.\", \"group\": \"Fonts\", \"tab\": \"Fonts\", \"min\": 8, \"max\": 20, \"step\": 1, \"default\": 12}, {\"key\": \"background.color\", \"kind\": \"color\", \"label\": \"Background Color\", \"description\": \"Solid background tone for this view.\", \"group\": \"Background\", \"tab\": \"Background\", \"default\": \"#3A6EA5\"}, {\"key\": \"background.position\", \"kind\": \"select\", \"label\": \"Position\", \"description\": \"How the wallpaper fills the surface.\", \"group\": \"Background\", \"tab\": \"Background\", \"default\": \"fill\", \"options\": [{\"value\": \"fill\", \"label\": \"Fill\"}, {\"value\": \"fit\", \"label\": \"Fit\"}, {\"value\": \"stretch\", \"label\": \"Stretch\"}, {\"value\": \"center\", \"label\": \"Center\"}, {\"value\": \"tile\", \"label\": \"Tile\"}]}, {\"key\": \"icons.iconSize\", \"kind\": \"number\", \"label\": \"Icon Size\", \"description\": \"Icon side length in pixels.\", \"group\": \"Icons\", \"tab\": \"Icons\", \"min\": 24, \"max\": 96, \"step\": 4, \"default\": 32}, {\"key\": \"icons.iconSpacing\", \"kind\": \"number\", \"label\": \"Icon Spacing\", \"description\": \"Pixels between icon cells.\", \"group\": \"Icons\", \"tab\": \"Icons\", \"min\": 4, \"max\": 48, \"step\": 2, \"default\": 8}, {\"key\": \"icons.showIcons\", \"kind\": \"boolean\", \"label\": \"Show Icons\", \"description\": \"Render icons on this view.\", \"group\": \"Icons\", \"tab\": \"Icons\", \"default\": true}, {\"key\": \"icons.startingCorner\", \"kind\": \"select\", \"label\": \"Starting Corner\", \"description\": \"Where the first icon lands.\", \"group\": \"Icons\", \"tab\": \"Icons\", \"default\": \"top-left\", \"options\": [{\"value\": \"top-left\", \"label\": \"Top Left\"}, {\"value\": \"top-right\", \"label\": \"Top Right\"}, {\"value\": \"bottom-left\", \"label\": \"Bottom Left\"}, {\"value\": \"bottom-right\", \"label\": \"Bottom Right\"}]}, {\"key\": \"icons.flowDirection\", \"kind\": \"select\", \"label\": \"Flow Direction\", \"description\": \"Whether icons fill columns or rows first.\", \"group\": \"Icons\", \"tab\": \"Icons\", \"default\": \"vertical-first\", \"options\": [{\"value\": \"vertical-first\", \"label\": \"Vertical First\"}, {\"value\": \"horizontal-first\", \"label\": \"Horizontal First\"}]}], \"system\": [{\"key\": \"defaultBrowser\", \"kind\": \"select\", \"label\": \"Default Browser\", \"description\": \"The browser the engine drives for sessions, page saves, and login windows.\", \"group\": \"Browser\", \"optionsShape\": \"browser\", \"optionsVolume\": \"system\", \"optionsValue\": \"id\", \"optionsLabel\": \"name\", \"optionsNone\": \"Automatic\"}]}").ok(),
    ..ShapeDef::default()
});
