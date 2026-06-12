// DO NOT EDIT — generated from platform/ontology/shapes/webpage.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A web page. Base type for search result. Also used for browser history
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Webpage {
    pub name: String,
    pub text: Option<String>,
    pub url: String,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub content_type: Option<String>,
    pub error: Option<String>,
    pub favicon: Option<String>,
    pub last_visit_unix: Option<i64>,
    pub visit_count: Option<i64>,
}

pub static WEBPAGE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "webpage".into(),
    plural: Some("webpages".into()),
    description: Some("A web page. Base type for search result. Also used for browser history".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::required("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("contentType", FieldType::String),
        FieldDef::optional("error", FieldType::String),
        FieldDef::optional("favicon", FieldType::Url),
        FieldDef::optional("lastVisitUnix", FieldType::Integer),
        FieldDef::optional("visitCount", FieldType::Integer),
    ],
    identity: vec!["url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("url".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/WebPage".into(), url: Some("https://schema.org/WebPage".into()), notes: Some("Our URL-as-identity matches schema.org's @id/url convention; contentType ≈ encodingFormat.".into()) },
        PriorArtDef { source: "HTTP semantics (RFC 9110)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc9110".into()), notes: Some("Our contentType is the Content-Type response header; error ≈ non-2xx status text.".into()) },
        PriorArtDef { source: "Chrome history / WebExtensions History API".into(), url: Some("https://developer.chrome.com/docs/extensions/reference/api/history".into()), notes: Some("Practical source. Our visitCount/lastVisitUnix lift from the history API's VisitItem structure.".into()) },
    ],
    ..ShapeDef::default()
});
