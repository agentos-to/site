// DO NOT EDIT — generated from platform/ontology/shapes/repository.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A source code repository.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Repository {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub default_branch: Option<String>,
    pub forks: Option<i64>,
    pub is_archived: Option<bool>,
    pub is_private: Option<bool>,
    pub language: Option<String>,
    pub license: Option<String>,
    pub open_issues: Option<i64>,
    pub size: Option<i64>,
    pub stars: Option<i64>,
    pub topics: Option<Vec<String>>,
}

pub static REPOSITORY: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "repository".into(),
    plural: Some("repositories".into()),
    description: Some("A source code repository.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("defaultBranch", FieldType::String),
        FieldDef::optional("forks", FieldType::Integer),
        FieldDef::optional("isArchived", FieldType::Boolean),
        FieldDef::optional("isPrivate", FieldType::Boolean),
        FieldDef::optional("language", FieldType::String),
        FieldDef::optional("license", FieldType::String),
        FieldDef::optional("openIssues", FieldType::Integer),
        FieldDef::optional("size", FieldType::Integer),
        FieldDef::optional("stars", FieldType::Integer),
        FieldDef::optional("topics", FieldType::StringList),
    ],
    out: vec![
        EdgeDef { label: "forked_from".into(), to: Some("repository".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "owned_by".into(), to: Some("account".into()), from: None, card: Cardinality::One },
    ],
    identity_any: vec!["path".into(), "url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("language".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
