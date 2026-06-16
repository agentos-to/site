// DO NOT EDIT — generated from platform/ontology/shapes/volume.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A mounted Volume — any named source of typed nodes the engine has
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Volume {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub address: Option<String>,
    #[serde(rename = "auto_mount")]
    pub auto_mount: Option<bool>,
    #[serde(rename = "default_view")]
    pub default_view: Option<String>,
    pub ejectable: Option<bool>,
    pub free_bytes: Option<i64>,
    pub icon: Option<String>,
    pub kind: Option<String>,
    pub provider: Option<String>,
    pub read_only: Option<bool>,
    pub removable: Option<bool>,
    pub scope: Option<String>,
    pub source: Option<String>,
    pub total_bytes: Option<i64>,
    #[serde(rename = "volume_id")]
    pub volume_id: Option<String>,
}

pub static VOLUME: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "volume".into(),
    plural: Some("volumes".into()),
    description: Some("A mounted Volume — any named source of typed nodes the engine has".into()),
    icon: Some("drive".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("address", FieldType::String),
        FieldDef::optional("auto_mount", FieldType::Boolean),
        FieldDef::optional("default_view", FieldType::String),
        FieldDef::optional("ejectable", FieldType::Boolean),
        FieldDef::optional("freeBytes", FieldType::Integer),
        FieldDef::optional("icon", FieldType::String),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("provider", FieldType::String),
        FieldDef::optional("readOnly", FieldType::Boolean),
        FieldDef::optional("removable", FieldType::Boolean),
        FieldDef::optional("scope", FieldType::String),
        FieldDef::optional("source", FieldType::String),
        FieldDef::optional("totalBytes", FieldType::Integer),
        FieldDef::optional("volume_id", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("kind".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "HDT (Header, Dictionary, Triples)".into(), url: Some("https://www.rdfhdt.org/what-is-hdt/".into()), notes: Some("RDF binary file format; one file = one queryable graph. The Header describes the dataset in its own vocabulary — same shapes-ride-along move as our embedded ontology.".into()) },
        PriorArtDef { source: "Stardog Virtual Graphs".into(), url: Some("https://docs.stardog.com/virtual-graphs/".into()), notes: Some("Register an external source under a URI; query as a named graph. Our volume shape is the registration row; mount/unmount is the verb pair.".into()) },
        PriorArtDef { source: "macOS Disk Utility / DMG".into(), url: Some("https://support.apple.com/guide/disk-utility/welcome/mac".into()), notes: Some("The UX mental model. A volume is an attached, browseable disk; the Finder shows it in the sidebar; eject detaches it without destroying the underlying file.".into()) },
    ],
    ..ShapeDef::default()
});
