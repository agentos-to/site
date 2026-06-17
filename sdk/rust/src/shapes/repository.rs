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
    identity_any: vec!["path".into(), "url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("language".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Git internals + Git refs".into(), url: Some("https://git-scm.com/book/en/v2/Git-Internals-Git-References".into()), notes: Some("Our defaultBranch is a Git ref (refs/heads/main); forkedFrom is explicit in our model vs. implicit in Git (recorded only by forges).".into()) },
        PriorArtDef { source: "GitHub REST API — Repository".into(), url: Some("https://docs.github.com/en/rest/repos/repos".into()), notes: Some("Direct source. Our stars/forks/openIssues/topics/defaultBranch/ license/size/isArchived/isPrivate all come from the GitHub Repository resource.".into()) },
        PriorArtDef { source: "SPDX License List".into(), url: Some("https://spdx.org/licenses/".into()), notes: Some("Our license values are SPDX identifiers (MIT, Apache-2.0, GPL-3.0-or-later).".into()) },
    ],
    ..ShapeDef::default()
});
