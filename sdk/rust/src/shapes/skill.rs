// DO NOT EDIT — generated from platform/ontology/shapes/agentos/skill.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A connected service/integration in agentOS. Each skill provides tools
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Skill {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub color: Option<String>,
    pub description: Option<String>,
    pub error: Option<String>,
    pub skill_id: Option<String>,
    pub status: Option<String>,
}

pub static SKILL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "skill".into(),
    plural: Some("skills".into()),
    description: Some("A connected service/integration in agentOS. Each skill provides tools".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("color", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("error", FieldType::Text),
        FieldDef::optional("skillId", FieldType::String),
        FieldDef::optional("status", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("description".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
