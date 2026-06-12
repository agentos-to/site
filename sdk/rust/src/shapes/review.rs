// DO NOT EDIT — generated from platform/ontology/shapes/review.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A user review of a product. Reviews are also posts, so they carry engagement metrics.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Review {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub comment_count: Option<i64>,
    pub community: Option<String>,
    pub external_url: Option<String>,
    pub is_verified: Option<bool>,
    pub post_type: Option<String>,
    pub rating: Option<f64>,
    pub rating_max: Option<f64>,
    pub score: Option<i64>,
    pub tags: Option<Vec<String>>,
}

pub static REVIEW: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "review".into(),
    plural: Some("reviews".into()),
    description: Some("A user review of a product. Reviews are also posts, so they carry engagement metrics.".into()),
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
        FieldDef::optional("externalUrl", FieldType::Url),
        FieldDef::optional("isVerified", FieldType::Boolean),
        FieldDef::optional("postType", FieldType::String),
        FieldDef::optional("rating", FieldType::Number),
        FieldDef::optional("ratingMax", FieldType::Number),
        FieldDef::optional("score", FieldType::Integer),
        FieldDef::optional("tags", FieldType::StringList),
    ],
    out: vec![
        EdgeDef { label: "reviews".into(), to: Some("product".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "posted_by".into(), to: Some("account".into()), from: None, card: Cardinality::One },
    ],
    also: vec!["post".into()],
    display: Some(DisplaySpec {
        subtitle: Some("author".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/Review".into(), url: Some("https://schema.org/Review".into()), notes: Some("Our rating ≈ reviewRating.ratingValue; ratingMax ≈ bestRating; reviews = itemReviewed; isVerified has no direct property (extension).".into()) },
        PriorArtDef { source: "schema.org/AggregateRating".into(), url: Some("https://schema.org/AggregateRating".into()), notes: Some("For product review aggregates. Our rating/ratingMax map to ratingValue/bestRating; reviewCount is inherited when computed.".into()) },
    ],
    ..ShapeDef::default()
});
