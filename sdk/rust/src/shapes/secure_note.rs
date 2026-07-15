// DO NOT EDIT — generated from platform/ontology/shapes/secure_note.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A secret free-text note — the "Secure Note" a password manager stores
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct SecureNote {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub category: Option<String>,
    pub is_pinned: Option<bool>,
    pub secret_ref: Option<String>,
}

pub static SECURE_NOTE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "secure_note".into(),
    plural: Some("secure_notes".into()),
    description: Some("A secret free-text note — the \"Secure Note\" a password manager stores".into()),
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
        FieldDef::optional("isPinned", FieldType::Boolean),
        FieldDef::optional("secretRef", FieldType::String),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("category".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "1Password \"Secure Note\" item category".into(), url: Some("https://support.1password.com/item-categories/".into()), notes: Some("The direct source. 1P's Secure Note is title + one big concealed notes field + tags. We keep the title (name) and tags on the graph and route the concealed body into secrets (secretRef), exactly matching 1P's field concealment.".into()) },
        PriorArtDef { source: "AgentOS `note` shape".into(), url: None, notes: Some("Deliberately NOT reused. `note.content` is graph plaintext for full-text PKM; a secure note's body must be encrypted-sidebanded. Distinct storage contract => distinct shape, no `also: [note]`.".into()) },
        PriorArtDef { source: "Bitwarden \"Secure Note\" type".into(), url: Some("https://bitwarden.com/help/managing-items/".into()), notes: Some("Same primitive — a named item whose notes field is encrypted at rest. Confirms the title-on-metadata / body-as-secret split.".into()) },
    ],
    ..ShapeDef::default()
});
