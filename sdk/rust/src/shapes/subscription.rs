// DO NOT EDIT — generated from platform/ontology/shapes/agentos/subscription.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A standing subscription — a durable intent to stream live entities, re-armed on every engine boot.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Subscription {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub app: String,
    pub op: String,
    pub service: Option<String>,
    pub target: Option<String>,
}

pub static SUBSCRIPTION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "subscription".into(),
    plural: Some("subscriptions".into()),
    description: Some("A standing subscription — a durable intent to stream live entities, re-armed on every engine boot.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::required("app", FieldType::String),
        FieldDef::required("op", FieldType::String),
        FieldDef::optional("service", FieldType::String),
        FieldDef::optional("target", FieldType::String),
    ],
    identity: vec!["app".into(), "op".into()],
    display: Some(DisplaySpec {
        subtitle: Some("target".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "W3C WebSub subscriptions".into(), url: Some("https://www.w3.org/TR/websub/".into()), notes: Some("A subscription is a stored intent (topic + callback) the hub re-delivers against — content never lives on the subscription. Our app/op ≈ topic/callback.".into()) },
        PriorArtDef { source: "MQTT persistent sessions".into(), url: Some("https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html".into()), notes: Some("Subscriptions survive connection loss and re-attach on reconnect. Our engine-boot re-arm parallels session resumption.".into()) },
        PriorArtDef { source: "systemd unit enablement (systemctl enable)".into(), url: Some("https://www.freedesktop.org/software/systemd/man/systemctl.html".into()), notes: Some("Enablement is a durable on-disk fact distinct from the running process; boot re-creates the runtime state from it. Our node ≈ the wants/ symlink, the live CDP hook ≈ the running unit.".into()) },
    ],
    ..ShapeDef::default()
});
