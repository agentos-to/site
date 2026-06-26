// DO NOT EDIT — generated from platform/ontology/shapes/network.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A local network — a LAN identified by its gateway. "Home" and "Whole Foods
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Network {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub bssid: Option<String>,
    pub gateway_ip: Option<String>,
    pub gateway_mac: String,
    pub last_seen: Option<String>,
    pub ssid: Option<String>,
    pub subnet: Option<String>,
}

pub static NETWORK: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "network".into(),
    plural: Some("networks".into()),
    description: Some("A local network — a LAN identified by its gateway. \"Home\" and \"Whole Foods".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("bssid", FieldType::String),
        FieldDef::optional("gatewayIp", FieldType::String),
        FieldDef::required("gatewayMac", FieldType::String),
        FieldDef::optional("lastSeen", FieldType::Datetime),
        FieldDef::optional("ssid", FieldType::String),
        FieldDef::optional("subnet", FieldType::String),
    ],
    identity: vec!["gatewayMac".into()],
    display: Some(DisplaySpec {
        subtitle: Some("ssid".into()),
        highlights: vec!["ssid".into(), "subnet".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "IEEE 802 BSSID / SSID".into(), url: Some("https://standards.ieee.org/".into()), notes: Some("SSID is the human network name (not unique); BSSID is a specific AP's radio MAC. We identify the LAN by its gateway (router) MAC, the most stable per-network handle a client can observe without credentials.".into()) },
    ],
    ..ShapeDef::default()
});
