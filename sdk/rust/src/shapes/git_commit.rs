// DO NOT EDIT — generated from platform/ontology/shapes/git_commit.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A git commit — a single point in version control history.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct GitCommit {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub additions: Option<i64>,
    pub all_day: Option<bool>,
    pub committed_at: Option<String>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub deletions: Option<i64>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub files_changed: Option<i64>,
    pub ical_uid: Option<String>,
    pub message: Option<String>,
    pub properties: Option<serde_json::Value>,
    pub recurrence: Option<Vec<String>>,
    pub sha: Option<String>,
    pub short_hash: Option<String>,
    pub show_as: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub timezone: Option<String>,
    pub visibility: Option<String>,
}

pub static GIT_COMMIT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "git_commit".into(),
    plural: Some("git_commits".into()),
    description: Some("A git commit — a single point in version control history.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("additions", FieldType::Integer),
        FieldDef::optional("allDay", FieldType::Boolean),
        FieldDef::optional("committedAt", FieldType::Datetime),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("deletions", FieldType::Integer),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("filesChanged", FieldType::Integer),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("message", FieldType::Text),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("sha", FieldType::String),
        FieldDef::optional("shortHash", FieldType::String),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "authored_by".into(), to: Some("account".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "committed_by".into(), to: Some("account".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "in".into(), to: Some("repository".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "derived_from".into(), to: Some("git_commit".into()), from: None, card: Cardinality::One },
    ],
    also: vec!["event".into()],
    display: Some(DisplaySpec {
        subtitle: Some("author".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Git Internals — commit object".into(), url: Some("https://git-scm.com/book/en/v2/Git-Internals-Git-Objects".into()), notes: Some("Our sha/shortHash/message/parent match the commit object exactly. author/committer follow Git's distinct author-vs-committer model.".into()) },
        PriorArtDef { source: "Conventional Commits 1.0".into(), url: Some("https://www.conventionalcommits.org/en/v1.0.0/".into()), notes: Some("Practical structure for message field (type(scope): subject). Optional — we don't enforce but it's compatible.".into()) },
    ],
    ..ShapeDef::default()
});
