// DO NOT EDIT — generated from platform/ontology/shapes/tool_call.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A single tool invocation made by an agent during a message.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct ToolCall {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub duration_ms: Option<i64>,
    pub input: Option<String>,
    pub is_error: Option<bool>,
    pub output: Option<String>,
}

pub static TOOL_CALL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "tool_call".into(),
    plural: Some("tool_calls".into()),
    description: Some("A single tool invocation made by an agent during a message.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("durationMs", FieldType::Integer),
        FieldDef::optional("input", FieldType::Text),
        FieldDef::optional("isError", FieldType::Boolean),
        FieldDef::optional("output", FieldType::Text),
    ],
    identity: vec!["platform".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
