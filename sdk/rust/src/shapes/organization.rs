// DO NOT EDIT — generated from platform/ontology/shapes/organization.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A company, nonprofit, or other organization. Organizations are actors — they
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Organization {
    pub name: String,
    pub text: Option<String>,
    pub url: String,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub actor_type: Option<String>,
    pub industry: Option<String>,
}

pub static ORGANIZATION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "organization".into(),
    plural: Some("organizations".into()),
    description: Some("A company, nonprofit, or other organization. Organizations are actors — they".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::required("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("actorType", FieldType::String),
        FieldDef::optional("industry", FieldType::String),
    ],
    also: vec!["actor".into()],
    identity: vec!["url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("industry".into()),
        image: Some("image".into()),
        highlights: vec!["headquarters".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
