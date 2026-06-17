// DO NOT EDIT — generated from platform/ontology/shapes/issue.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// The demand atom of the product board — a problem, request, or observation.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Issue {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub comment_count: Option<i64>,
    pub community: Option<String>,
    pub declined: Option<bool>,
    pub external_url: Option<String>,
    pub post_type: Option<String>,
    pub score: Option<i64>,
}

pub static ISSUE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "issue".into(),
    plural: Some("issues".into()),
    description: Some("The demand atom of the product board — a problem, request, or observation.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("commentCount", FieldType::Integer),
        FieldDef::optional("community", FieldType::String),
        FieldDef::optional("declined", FieldType::Boolean),
        FieldDef::optional("externalUrl", FieldType::Url),
        FieldDef::optional("postType", FieldType::String),
        FieldDef::optional("score", FieldType::Integer),
    ],
    also: vec!["post".into()],
    derived: vec![
        DerivedBinding { key: "downvotes".into(), spec: serde_json::from_str("{\"count\": \"for\", \"where\": {\"direction\": \"down\"}}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "status".into(), spec: serde_json::from_str("{\"reverse\": \"addresses\", \"get\": \"status\", \"prefer\": [\"achieved\", \"active\", \"at-risk\", \"proposed\"], \"map\": {\"achieved\": \"addressed\", \"active\": \"in-progress\", \"at-risk\": \"in-progress\", \"proposed\": \"planned\"}, \"default\": \"open\", \"authored\": {\"field\": \"declined\", \"equals\": true, \"then\": \"declined\"}}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "upvotes".into(), spec: serde_json::from_str("{\"count\": \"for\", \"where\": {\"direction\": \"up\"}}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "weight".into(), spec: serde_json::from_str("{\"tally\": \"for\", \"by\": \"direction\", \"map\": {\"up\": 1, \"down\": -1}}").unwrap_or(serde_json::Value::Null) },
    ],
    display: Some(DisplaySpec {
        subtitle: Some("status".into()),
        highlights: vec!["status".into(), "weight".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Linear issue + Customer Requests".into(), url: Some("https://linear.app/docs/customer-requests".into()), notes: Some("An issue aggregates a request count rather than storing a status the team hand-maintains. Our weight ≈ the request count; status is derived from the addressing outcome's stage, never typed on the issue.".into()) },
        PriorArtDef { source: "Teresa Torres — Opportunity Solution Tree".into(), url: Some("https://www.producttalk.org/2016/08/opportunity-solution-tree/".into()), notes: Some("An opportunity (problem) is the citizen; solutions hang off it. Our issue is the opportunity; outcome `addresses` issue is the spine that makes a solution earn its existence.".into()) },
        PriorArtDef { source: "Canny / Featurebase post".into(), url: Some("https://canny.io/".into()), notes: Some("The shipped atom is a demand item with a vote tally and a status lifecycle, grouped by status into a roadmap. issue (also post) + vote is that atom; the roadmap is this list grouped by derived status.".into()) },
    ],
    ..ShapeDef::default()
});
