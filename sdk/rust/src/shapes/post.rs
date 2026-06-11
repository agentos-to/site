// DO NOT EDIT — generated from platform/ontology/shapes/post.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A piece of published content — a Reddit submission, HN story, YouTube upload,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Post {
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
    pub post_type: Option<String>,
    pub score: Option<i64>,
}

pub static POST: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "post".into(),
    plural: Some("posts".into()),
    description: Some("A piece of published content — a Reddit submission, HN story, YouTube upload,".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
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
        FieldDef::optional("postType", FieldType::String),
        FieldDef::optional("score", FieldType::Integer),
    ],
    out: vec![
        EdgeDef { label: "at_namespace".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "posted_by".into(), to: Some("account".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "published_in".into(), to: Some("community".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "replies_to".into(), to: Some("post".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "replies".into(), to: Some("post".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "contains".into(), to: Some("video".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "shows".into(), to: Some("image".into()), from: None, card: Cardinality::Many },
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("author".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
