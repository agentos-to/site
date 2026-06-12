// DO NOT EDIT — generated from platform/ontology/shapes/shape.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A shape definition - the ontology node that describes a node type.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Shape {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub also: Option<Vec<String>>,
    pub derived: Option<serde_json::Value>,
    pub description: Option<String>,
    pub display: Option<serde_json::Value>,
    pub fields: Option<serde_json::Value>,
    pub groups: Option<serde_json::Value>,
    pub icon: Option<String>,
    pub identity: Option<Vec<String>>,
    #[serde(rename = "identity_any")]
    pub identity_any: Option<Vec<String>>,
    pub in_: Option<serde_json::Value>,
    pub out: Option<serde_json::Value>,
    pub plural: Option<String>,
    pub prefs_schemas: Option<serde_json::Value>,
    #[serde(rename = "prior_art")]
    pub prior_art: Option<serde_json::Value>,
    pub shortcuts: Option<serde_json::Value>,
}

pub static SHAPE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "shape".into(),
    plural: Some("shapes".into()),
    description: Some("A shape definition - the ontology node that describes a node type.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("also", FieldType::StringList),
        FieldDef::optional("derived", FieldType::Json),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("display", FieldType::Json),
        FieldDef::optional("fields", FieldType::Json),
        FieldDef::optional("groups", FieldType::Json),
        FieldDef::optional("icon", FieldType::String),
        FieldDef::optional("identity", FieldType::StringList),
        FieldDef::optional("identity_any", FieldType::StringList),
        FieldDef::optional("in", FieldType::Json),
        FieldDef::optional("out", FieldType::Json),
        FieldDef::optional("plural", FieldType::String),
        FieldDef::optional("prefsSchemas", FieldType::Json),
        FieldDef::optional("prior_art", FieldType::Json),
        FieldDef::optional("shortcuts", FieldType::Json),
    ],
    identity: vec!["name".into()],
    display: Some(DisplaySpec {
        subtitle: Some("description".into()),
        body: Some("description".into()),
        highlights: vec!["plural".into()],
        ..DisplaySpec::default()
    }),
    groups: vec![
        FieldGroupDef { name: "Schema".into(), fields: vec!["fields".into(), "out".into(), "in".into()] },
        FieldGroupDef { name: "Display".into(), fields: vec!["display".into(), "groups".into()] },
        FieldGroupDef { name: "Identity".into(), fields: vec!["identity".into(), "identity_any".into(), "also".into()] },
        FieldGroupDef { name: "Automation".into(), fields: vec!["derived".into(), "shortcuts".into()] },
        FieldGroupDef { name: "Sources".into(), fields: vec!["prior_art".into()] },
        FieldGroupDef { name: "Preferences".into(), fields: vec!["prefsSchemas".into()] },
    ],
    prior_art: vec![
        PriorArtDef { source: "JSON Schema".into(), url: Some("https://json-schema.org/".into()), notes: Some("Prior art for describing fields and JSON-shaped validation contracts. AgentOS keeps shape identity and graph relations first-class instead of flattening everything into one document schema.".into()) },
        PriorArtDef { source: "W3C SHACL".into(), url: Some("https://www.w3.org/TR/shacl/".into()), notes: Some("Prior art for RDF graph shape constraints. AgentOS uses the same idea - graph data has shapes - but stores the shape definition as an inspectable node in the local graph.".into()) },
        PriorArtDef { source: "RDF Schema".into(), url: Some("https://www.w3.org/TR/rdf-schema/".into()), notes: Some("Prior art for classes/properties as graph vocabulary. AgentOS shape nodes are the local, executable version of that vocabulary.".into()) },
    ],
    ..ShapeDef::default()
});
