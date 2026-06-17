// DO NOT EDIT — generated from platform/ontology/shapes/user.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An AgentOS user — the **seat** at this machine. Pure OS bookkeeping:
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct User {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub actor_type: Option<String>,
    pub os_username: Option<String>,
    pub primary_user: Option<bool>,
}

pub static USER: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "user".into(),
    plural: Some("users".into()),
    description: Some("An AgentOS user — the **seat** at this machine. Pure OS bookkeeping:".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("actorType", FieldType::String),
        FieldDef::optional("osUsername", FieldType::String),
        FieldDef::optional("primaryUser", FieldType::Boolean),
    ],
    out: vec![
        EdgeDef { label: "identified_as".into(), to: Some("person".into()), from: None, card: Cardinality::One },
    ],
    also: vec!["actor".into()],
    identity_any: vec!["osUsername".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "POSIX getpwuid (passwd database)".into(), url: Some("https://pubs.opengroup.org/onlinepubs/9699919799/functions/getpwuid.html".into()), notes: Some("The OS-level \"user\" — uid + login name + home dir. Our `osUsername` mirrors `pw_name`; identity-by-OS-account follows the same pattern. We diverge by separating the OS seat (`user`) from the human (`person`); POSIX conflates them.".into()) },
        PriorArtDef { source: "schema.org/Audience".into(), url: Some("https://schema.org/Audience".into()), notes: Some("Loose fit. schema.org has no \"OS user\" concept — user accounts are product-specific. We model it explicitly because AgentOS is the product, and the seat is the machine's record of the human.".into()) },
    ],
    ..ShapeDef::default()
});
