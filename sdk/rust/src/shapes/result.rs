// DO NOT EDIT — generated from platform/ontology/shapes/result.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A search result — a pointer to something found. Not the thing itself.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Result {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub community: Option<String>,
    pub external_url: Option<String>,
    pub favicon: Option<String>,
    pub indexed_at: Option<String>,
    pub post_id: Option<String>,
    pub result_type: Option<String>,
    pub score: Option<i64>,
    pub similarity: Option<f64>,
}

pub static RESULT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "result".into(),
    plural: Some("results".into()),
    description: Some("A search result — a pointer to something found. Not the thing itself.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("community", FieldType::String),
        FieldDef::optional("externalUrl", FieldType::Url),
        FieldDef::optional("favicon", FieldType::Url),
        FieldDef::optional("indexedAt", FieldType::Datetime),
        FieldDef::optional("postId", FieldType::String),
        FieldDef::optional("resultType", FieldType::String),
        FieldDef::optional("score", FieldType::Integer),
        FieldDef::optional("similarity", FieldType::Number),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("url".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "OpenSearch Description Document".into(), url: Some("https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md".into()), notes: Some("Result-pointer model: each hit has a URL + metadata. Our resultType ≈ Url template's type attribute.".into()) },
        PriorArtDef { source: "Web Search API conventions (Brave/Bing)".into(), url: Some("https://api.search.brave.com/app/documentation/web-search/get-started".into()), notes: Some("Practical source. Our indexedAt/resultType align with common fields across Brave, Bing, and Exa web APIs.".into()) },
    ],
    ..ShapeDef::default()
});
