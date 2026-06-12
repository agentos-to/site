// DO NOT EDIT — generated from platform/ontology/shapes/protocol.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A protocol or technical spec — git, bitcoin, ssh, smtp, oauth, etc.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Protocol {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub homepage: Option<String>,
    pub rfc: Option<String>,
    pub wikidata_id: Option<String>,
}

pub static PROTOCOL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "protocol".into(),
    plural: Some("protocols".into()),
    description: Some("A protocol or technical spec — git, bitcoin, ssh, smtp, oauth, etc.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("homepage", FieldType::Url),
        FieldDef::optional("rfc", FieldType::String),
        FieldDef::optional("wikidataId", FieldType::String),
    ],
    identity: vec!["name".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/CreativeWork".into(), url: Some("https://schema.org/CreativeWork".into()), notes: Some("Closest match in schema.org — protocols are creative works in the broadest sense. We narrow to protocols and technical specifications used as identity namespaces.".into()) },
        PriorArtDef { source: "Wikidata (Communication protocol, Q15836568)".into(), url: Some("https://www.wikidata.org/wiki/Q15836568".into()), notes: Some("wikidataId enables cross-reference for dedupe across other knowledge graphs. Most well-known protocols have Q-IDs.".into()) },
        PriorArtDef { source: "IANA Protocol Registry".into(), url: Some("https://www.iana.org/protocols".into()), notes: Some("Authoritative registry for many protocols. Our `name` aligns with IANA protocol slugs where applicable.".into()) },
    ],
    ..ShapeDef::default()
});
