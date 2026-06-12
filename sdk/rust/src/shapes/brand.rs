// DO NOT EDIT — generated from platform/ontology/shapes/brand.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A consumer brand — a named, visual, commercial identity. Often (but not
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Brand {
    pub name: String,
    pub text: Option<String>,
    pub url: String,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub country: Option<String>,
    pub primary_color: Option<String>,
    pub tagline: Option<String>,
    pub text_color: Option<String>,
}

pub static BRAND: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "brand".into(),
    plural: Some("brands".into()),
    description: Some("A consumer brand — a named, visual, commercial identity. Often (but not".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::required("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("country", FieldType::String),
        FieldDef::optional("primaryColor", FieldType::String),
        FieldDef::optional("tagline", FieldType::String),
        FieldDef::optional("textColor", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "owned_by".into(), to: Some("organization".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "online_at".into(), to: Some("website".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "depicted_by".into(), to: Some("image".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["url".into()],
    display: Some(DisplaySpec {
        subtitle: Some("tagline".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/Brand".into(), url: Some("https://schema.org/Brand".into()), notes: Some("Our tagline ≈ slogan; founded = foundingDate; ownedBy ≈ parentOrganization (on the owning Organization); logo = logo. schema.org doesn't model color on Brand; that's a Wikidata extension.".into()) },
        PriorArtDef { source: "Wikidata (Brand, Q431289)".into(), url: Some("https://www.wikidata.org/wiki/Q431289".into()), notes: Some("Cross-reference identity for dedupe. country maps to P17 (country); founded to P571 (inception); ownedBy to P127 (owned by); primaryColor ≈ P465 \"hex color code\" (Wikidata stores without the \"#\" prefix — we include it to match CSS and our app-frontmatter convention).".into()) },
        PriorArtDef { source: "Apple PassKit pkpass".into(), url: Some("https://developer.apple.com/documentation/walletpasses".into()), notes: Some("Wallet passes carry backgroundColor / foregroundColor / labelColor — three-color palette aligned with our primaryColor / textColor. We ship two here (pairing primary with its paired text color) and defer the third until a renderer needs it. An itinerary PDF can derive a \"label\" color from a lighter tint of textColor at render time if needed, rather than fixing it at the data layer.".into()) },
        PriorArtDef { source: "Material Design 3 — dynamic color roles".into(), url: Some("https://m3.material.io/styles/color/roles".into()), notes: Some("Material's palette has paired slots (`primary` / `onPrimary`; `secondary` / `onSecondary`; `surface` / `onSurface`). Our primaryColor/textColor follows the primary/onPrimary pairing. Secondary tiers are deferred until renderers actually need them.".into()) },
    ],
    ..ShapeDef::default()
});
