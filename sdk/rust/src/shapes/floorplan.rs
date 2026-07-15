// DO NOT EDIT — generated from platform/ontology/shapes/floorplan.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A renderable floor / venue map — walls, furniture, and hit targets for
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Floorplan {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub indicator_size: Option<f64>,
    pub layout_svg: Option<String>,
    pub mobile_rotation_degrees: Option<f64>,
    pub resources: Option<serde_json::Value>,
    pub source_url: Option<String>,
    pub timezone: Option<String>,
    pub venue_name: Option<String>,
    pub view_box: Option<String>,
}

pub static FLOORPLAN: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "floorplan".into(),
    plural: Some("floorplans".into()),
    description: Some("A renderable floor / venue map — walls, furniture, and hit targets for".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("indicatorSize", FieldType::Number),
        FieldDef::optional("layoutSvg", FieldType::String),
        FieldDef::optional("mobileRotationDegrees", FieldType::Number),
        FieldDef::optional("resources", FieldType::Json),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("venueName", FieldType::String),
        FieldDef::optional("viewBox", FieldType::String),
    ],
    identity: vec!["id".into()],
    display: Some(DisplaySpec {
        title: Some("name".into()),
        subtitle: Some("venueName".into()),
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
