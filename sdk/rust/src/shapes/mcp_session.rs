// DO NOT EDIT — generated from platform/ontology/shapes/agentos/mcp_session.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An MCP session — a client connected, made some calls, disconnected.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct McpSession {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub client: String,
    pub ended_at: Option<String>,
    pub git_branch: String,
    pub message_count: Option<i64>,
    pub project_id: String,
    pub session_type: Option<String>,
    pub started_at: Option<String>,
    pub token_count: Option<i64>,
}

pub static MCP_SESSION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "mcp_session".into(),
    plural: Some("mcp_sessions".into()),
    description: Some("An MCP session — a client connected, made some calls, disconnected.".into()),
    icon: Some("terminal".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::required("client", FieldType::String),
        FieldDef::optional("endedAt", FieldType::Datetime),
        FieldDef::required("gitBranch", FieldType::String),
        FieldDef::optional("messageCount", FieldType::Integer),
        FieldDef::required("projectId", FieldType::String),
        FieldDef::optional("sessionType", FieldType::String),
        FieldDef::optional("startedAt", FieldType::Datetime),
        FieldDef::optional("tokenCount", FieldType::Integer),
    ],
    out: vec![
        EdgeDef { label: "in".into(), to: Some("list".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["client".into(), "projectId".into(), "gitBranch".into()],
    display: Some(DisplaySpec {
        subtitle: Some("client".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
