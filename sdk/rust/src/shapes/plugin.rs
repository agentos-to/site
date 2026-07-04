// DO NOT EDIT — generated from platform/ontology/shapes/plugin.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A plugin — a contract bundle that plugs the OS into an external
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Plugin {
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
    pub description: Option<String>,
    pub error: Option<String>,
    pub handles: Option<Vec<String>>,
    pub icon_role: Option<String>,
    pub status: Option<String>,
}

pub static PLUGIN: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "plugin".into(),
    plural: Some("plugins".into()),
    description: Some("A plugin — a contract bundle that plugs the OS into an external".into()),
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
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("error", FieldType::Text),
        FieldDef::optional("handles", FieldType::StringList),
        FieldDef::optional("iconRole", FieldType::String),
        FieldDef::optional("status", FieldType::String),
    ],
    identity: vec!["id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("description".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Model Context Protocol (MCP) — Server".into(), url: Some("https://modelcontextprotocol.io/specification".into()), notes: Some("A plugin = an MCP-registerable provider. id ≈ MCP server name; status tracks connection lifecycle. The engine is the host that brokers between callers and plugins.".into()) },
        PriorArtDef { source: "OpenAPI 3.1 (Info + Servers)".into(), url: Some("https://spec.openapis.org/oas/v3.1.0".into()), notes: Some("A plugin's readme frontmatter ≈ OpenAPI info — description, website, privacy/terms; each connection ≈ a Server + security scheme.".into()) },
        PriorArtDef { source: "VS Code / Obsidian plugin (contributes)".into(), url: Some("https://code.visualstudio.com/api/references/contribution-points".into()), notes: Some("A plugin declares what it contributes (tools, services, connections) via decorators; the host discovers and wires it — the plugin never reaches into the host or another plugin.".into()) },
    ],
    ..ShapeDef::default()
});
