// DO NOT EDIT — generated from platform/ontology/shapes/app.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An application — the one installable, launchable unit. System apps
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct App {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub account: Option<serde_json::Value>,
    pub color: Option<String>,
    pub composition: Option<serde_json::Value>,
    pub default_route: Option<String>,
    pub default_view: Option<String>,
    pub description: Option<String>,
    pub error: Option<String>,
    pub handles: Option<Vec<String>>,
    pub icon_role: Option<String>,
    pub is_system: Option<bool>,
    pub route: Option<String>,
    pub status: Option<String>,
}

pub static APP: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "app".into(),
    plural: Some("apps".into()),
    description: Some("An application — the one installable, launchable unit. System apps".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("account", FieldType::Json),
        FieldDef::optional("color", FieldType::String),
        FieldDef::optional("composition", FieldType::Json),
        FieldDef::optional("defaultRoute", FieldType::String),
        FieldDef::optional("defaultView", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("error", FieldType::Text),
        FieldDef::optional("handles", FieldType::StringList),
        FieldDef::optional("iconRole", FieldType::String),
        FieldDef::optional("isSystem", FieldType::Boolean),
        FieldDef::optional("route", FieldType::String),
        FieldDef::optional("status", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "online_at".into(), to: Some("website".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "privacy_at".into(), to: Some("webpage".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "terms_at".into(), to: Some("webpage".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("description".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "macOS .app bundle (Info.plist)".into(), url: Some("https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html".into()), notes: Some("CFBundleIdentifier ≈ id; CFBundleName ≈ name; CFBundleIconFile ≈ iconRole (we use a role rather than a file path so themes can override).".into()) },
        PriorArtDef { source: "freedesktop .desktop entry".into(), url: Some("https://specifications.freedesktop.org/desktop-entry-spec/latest/".into()), notes: Some("Name, Icon, Exec — the Linux/XDG peer. We model the launchable surface, not the executable (the engine knows how to spawn).".into()) },
        PriorArtDef { source: "Windows AppUserModelID".into(), url: Some("https://learn.microsoft.com/en-us/windows/win32/shell/appids".into()), notes: Some("Stable per-app identity decoupled from the executable on disk. Our `id` plays the same role — themes and bookmarks reference it, the binary is an implementation detail of seed_system_apps().".into()) },
        PriorArtDef { source: "Model Context Protocol (MCP) — Server".into(), url: Some("https://modelcontextprotocol.io/specification".into()), notes: Some("An installed app = an MCP-registerable provider. id ≈ MCP server name; status tracks connection lifecycle.".into()) },
        PriorArtDef { source: "OpenAPI 3.1 (Info + Servers)".into(), url: Some("https://spec.openapis.org/oas/v3.1.0".into()), notes: Some("Our description/online_at/privacy_at/terms_at ≈ OpenAPI info.description/info.termsOfService/contact.".into()) },
    ],
    ..ShapeDef::default()
});
