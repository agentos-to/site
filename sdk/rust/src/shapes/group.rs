// DO NOT EDIT — generated from platform/ontology/shapes/group.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A group or community — online group, reading group, etc.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Group {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub category: Option<String>,
    pub member_count: Option<i64>,
}

pub static GROUP: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "group".into(),
    plural: Some("groups".into()),
    description: Some("A group or community — online group, reading group, etc.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("category", FieldType::String),
        FieldDef::optional("memberCount", FieldType::Integer),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("category".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/Group (via Organization/memberOf)".into(), url: Some("https://schema.org/Organization".into()), notes: Some("schema.org models groups as Organization. Our memberCount ≈ numberOfEmployees loosely; category ≈ naics/knowsAbout.".into()) },
        PriorArtDef { source: "FOAF Group".into(), url: Some("http://xmlns.com/foaf/spec/#term_Group".into()), notes: Some("Foundational social-graph vocabulary. foaf:member populates membership; category has no direct FOAF peer.".into()) },
    ],
    ..ShapeDef::default()
});
