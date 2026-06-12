// DO NOT EDIT — generated from platform/ontology/shapes/auth_challenge.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A platform demands something only a human (usually) can do — scan a QR
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct AuthChallenge {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub artifact: Option<String>,
    pub continue_with: Option<String>,
    pub expires_at: Option<String>,
    pub instructions: Option<String>,
    pub kind: Option<String>,
    pub payload: Option<String>,
    pub retrieval: Option<serde_json::Value>,
}

pub static AUTH_CHALLENGE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "auth_challenge".into(),
    plural: Some("auth_challenges".into()),
    description: Some("A platform demands something only a human (usually) can do — scan a QR".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("artifact", FieldType::Text),
        FieldDef::optional("continueWith", FieldType::String),
        FieldDef::optional("expiresAt", FieldType::Datetime),
        FieldDef::optional("instructions", FieldType::Text),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("payload", FieldType::String),
        FieldDef::optional("retrieval", FieldType::Json),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("instructions".into()),
        body: Some("artifact".into()),
        mono: Some("artifact".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "OAuth 2.0 Device Authorization Grant (RFC 8628)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc8628".into()), notes: Some("The device flow returns the human-must-act moment as data, not as an error: user_code + verification_uri + expires_in, with the client polling the token endpoint until the human acts. Same anatomy here — payload/artifact ≈ user_code/verification_uri, expiresAt ≈ expires_in, continueWith ≈ the polling step.".into()) },
        PriorArtDef { source: "whatsapp-web.js + qrcode-terminal".into(), url: Some("https://github.com/pedroslopez/whatsapp-web.js".into()), notes: Some("The proven precedent for QR-as-text: the linked-device QR payload is re-rendered as Unicode block characters in a terminal and scanned straight off the screen. `artifact` generalizes that to every text surface.".into()) },
    ],
    ..ShapeDef::default()
});
