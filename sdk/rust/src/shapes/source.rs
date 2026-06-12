// DO NOT EDIT — generated from platform/ontology/shapes/agentos/source.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A content source — where apps, themes, shapes, and wallpapers live.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Source {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub address: String,
    pub description: Option<String>,
    pub enabled: Option<bool>,
    pub last_synced: Option<String>,
    pub scanner: Option<String>,
    pub source_id: Option<String>,
}

pub static SOURCE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "source".into(),
    plural: Some("sources".into()),
    description: Some("A content source — where apps, themes, shapes, and wallpapers live.".into()),
    icon: Some("📦".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::required("address", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
        FieldDef::optional("enabled", FieldType::Boolean),
        FieldDef::optional("lastSynced", FieldType::Datetime),
        FieldDef::optional("scanner", FieldType::String),
        FieldDef::optional("sourceId", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "in".into(), to: Some("list".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["address".into()],
    display: Some(DisplaySpec {
        subtitle: Some("sourceId".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Homebrew Taps".into(), url: Some("https://docs.brew.sh/Taps".into()), notes: Some("Direct precedent. Our sourceId/address match tap name/URL; our platform=agentos parallels tap formulae discovery.".into()) },
        PriorArtDef { source: "Cydia / Sileo (APT repos for iOS)".into(), url: Some("https://wiki.theapebox.com/index.php/Package_Management".into()), notes: Some("Namespaced third-party source model. Our sourceId prefix is the Cydia repo-namespace pattern.".into()) },
        PriorArtDef { source: "Debian APT sources.list".into(), url: Some("https://wiki.debian.org/SourcesList".into()), notes: Some("Canonical third-party source mechanism. Our enabled flag parallels APT source enable/disable; lastSynced ≈ apt-get update timestamp.".into()) },
    ],
    ..ShapeDef::default()
});
