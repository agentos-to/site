// DO NOT EDIT — generated from platform/ontology/shapes/agentos/service.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A service — a named interface the engine brokers between strangers.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Service {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub description: Option<String>,
}

pub static SERVICE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "service".into(),
    plural: Some("services".into()),
    description: Some("A service — a named interface the engine brokers between strangers.".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
    ],
    identity: vec!["id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("description".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Debian alternatives system (update-alternatives)".into(), url: Some("https://wiki.debian.org/DebianAlternatives".into()), notes: Some("A generic name (editor) resolves to one of several registered providers via a per-name symlink the admin can repoint. Our service id ≈ the generic name; defaults_to ≈ the symlink.".into()) },
        PriorArtDef { source: "Windows XP — Set Program Access and Defaults".into(), url: Some("https://learn.microsoft.com/en-us/windows/win32/shell/default-programs".into()), notes: Some("The OS-level \"which program answers this kind of request\" surface. Our defaults_to link is that choice as graph state.".into()) },
        PriorArtDef { source: "Android Intents (action + default app)".into(), url: Some("https://developer.android.com/guide/components/intents-filters".into()), notes: Some("Apps declare which actions they answer; the user picks a default per action. provided_by ≈ intent-filter; defaults_to ≈ the user's \"always\" choice.".into()) },
    ],
    ..ShapeDef::default()
});
