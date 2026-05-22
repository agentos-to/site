// DO NOT EDIT — generated from platform/ontology/shapes/volume.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A mounted Volume — a `.db` memex file the engine has attached to the
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
    pub kind: Option<String>,
}

pub static VOLUME: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "volume".into(),
    plural: Some("volumes".into()),
    description: Some("A mounted Volume — a `.db` memex file the engine has attached to the".into()),
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
        FieldDef::optional("kind", FieldType::String),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("kind".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
