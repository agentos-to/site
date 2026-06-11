// DO NOT EDIT — generated from platform/ontology/shapes/user.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An AgentOS user — the seat at this machine. Carries the user's
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct User {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub actor_type: Option<String>,
    pub os_username: Option<String>,
    pub primary_user: Option<bool>,
}

pub static USER: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "user".into(),
    plural: Some("users".into()),
    description: Some("An AgentOS user — the seat at this machine. Carries the user's".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("actorType", FieldType::String),
        FieldDef::optional("osUsername", FieldType::String),
        FieldDef::optional("primaryUser", FieldType::Boolean),
    ],
    out: vec![
        EdgeDef { label: "identified_as".into(), to: Some("person".into()), from: None, card: Cardinality::One },
    ],
    also: vec!["actor".into()],
    identity_any: vec!["osUsername".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    prefs_schemas: serde_json::from_str("{\"ui\": [{\"key\": \"themeId\", \"kind\": \"select\", \"label\": \"Theme\", \"description\": \"Desktop theme \\u2014 window chrome, fonts, sounds.\", \"group\": \"Theme\", \"optionsShape\": \"theme\", \"optionsValue\": \"themeId\", \"optionsLabel\": \"name\"}, {\"key\": \"fontSize\", \"kind\": \"number\", \"label\": \"Font Size\", \"description\": \"Base UI font size in pixels.\", \"group\": \"Fonts\", \"tab\": \"Fonts\", \"min\": 8, \"max\": 20, \"step\": 1, \"default\": 12}, {\"key\": \"background.color\", \"kind\": \"color\", \"label\": \"Background Color\", \"description\": \"Solid background tone for this view.\", \"group\": \"Background\", \"tab\": \"Background\", \"default\": \"#3A6EA5\"}, {\"key\": \"background.position\", \"kind\": \"select\", \"label\": \"Position\", \"description\": \"How the wallpaper fills the surface.\", \"group\": \"Background\", \"tab\": \"Background\", \"default\": \"fill\", \"options\": [{\"value\": \"fill\", \"label\": \"Fill\"}, {\"value\": \"fit\", \"label\": \"Fit\"}, {\"value\": \"stretch\", \"label\": \"Stretch\"}, {\"value\": \"center\", \"label\": \"Center\"}, {\"value\": \"tile\", \"label\": \"Tile\"}]}, {\"key\": \"icons.iconSize\", \"kind\": \"number\", \"label\": \"Icon Size\", \"description\": \"Icon side length in pixels.\", \"group\": \"Icons\", \"tab\": \"Icons\", \"min\": 24, \"max\": 96, \"step\": 4, \"default\": 32}, {\"key\": \"icons.iconSpacing\", \"kind\": \"number\", \"label\": \"Icon Spacing\", \"description\": \"Pixels between icon cells.\", \"group\": \"Icons\", \"tab\": \"Icons\", \"min\": 4, \"max\": 48, \"step\": 2, \"default\": 8}, {\"key\": \"icons.showIcons\", \"kind\": \"boolean\", \"label\": \"Show Icons\", \"description\": \"Render icons on this view.\", \"group\": \"Icons\", \"tab\": \"Icons\", \"default\": true}, {\"key\": \"icons.startingCorner\", \"kind\": \"select\", \"label\": \"Starting Corner\", \"description\": \"Where the first icon lands.\", \"group\": \"Icons\", \"tab\": \"Icons\", \"default\": \"top-left\", \"options\": [{\"value\": \"top-left\", \"label\": \"Top Left\"}, {\"value\": \"top-right\", \"label\": \"Top Right\"}, {\"value\": \"bottom-left\", \"label\": \"Bottom Left\"}, {\"value\": \"bottom-right\", \"label\": \"Bottom Right\"}]}, {\"key\": \"icons.flowDirection\", \"kind\": \"select\", \"label\": \"Flow Direction\", \"description\": \"Whether icons fill columns or rows first.\", \"group\": \"Icons\", \"tab\": \"Icons\", \"default\": \"vertical-first\", \"options\": [{\"value\": \"vertical-first\", \"label\": \"Vertical First\"}, {\"value\": \"horizontal-first\", \"label\": \"Horizontal First\"}]}]}").ok(),
    ..ShapeDef::default()
});
