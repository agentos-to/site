// DO NOT EDIT — generated from platform/ontology/shapes/person.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A real human. People are actors — they can own accounts, hold roles,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Person {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub about: Option<String>,
    pub actor_type: Option<String>,
    pub notes: Option<String>,
}

pub static PERSON: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "person".into(),
    plural: Some("people".into()),
    description: Some("A real human. People are actors — they can own accounts, hold roles,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("about", FieldType::Text),
        FieldDef::optional("actorType", FieldType::String),
        FieldDef::optional("notes", FieldType::Text),
    ],
    also: vec!["actor".into()],
    identity_any: vec!["url".into()],
    derived: vec![
        DerivedBinding { key: "additionalName".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"additionalName\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"additionalName\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "birthdate".into(), spec: serde_json::from_str("{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"startDate\"}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "current_residence".into(), spec: serde_json::from_str("{\"find\": \"lived_at\", \"where_link\": {\"to\": null}, \"get\": \"name\"}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "current_role".into(), spec: serde_json::from_str("{\"find\": \"worked_at\", \"where_link\": {\"to\": null}, \"get\": \"title\"}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "familyName".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"familyName\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"familyName\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "gender".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"gender\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"gender\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "givenName".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"givenName\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"givenName\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "honorificPrefix".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"honorificPrefix\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"honorificPrefix\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "honorificSuffix".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"honorificSuffix\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"honorificSuffix\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "legalName".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"legalName\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"legalName\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "maidenName".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"maidenName\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"maidenName\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "nameOrder".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"nameOrder\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"nameOrder\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "nickname".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"nickname\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"nickname\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "phoneticFamilyName".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"phoneticFamilyName\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"phoneticFamilyName\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "phoneticGivenName".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"phoneticGivenName\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"phoneticGivenName\"}]}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "sortAs".into(), spec: serde_json::from_str("{\"latest\": [{\"find\": \"born_in\", \"is\": \"birth\", \"get\": \"sortAs\"}, {\"find\": \"changed\", \"is\": \"transition\", \"get\": \"sortAs\"}]}").unwrap_or(serde_json::Value::Null) },
    ],
    shortcuts: vec![
        ShortcutDef { key: "additionalName".into(), writes: "born_in[is=birth].additionalName".into() },
        ShortcutDef { key: "birthdate".into(), writes: "born_in[is=birth].startDate".into() },
        ShortcutDef { key: "familyName".into(), writes: "born_in[is=birth].familyName".into() },
        ShortcutDef { key: "gender".into(), writes: "born_in[is=birth].gender".into() },
        ShortcutDef { key: "givenName".into(), writes: "born_in[is=birth].givenName".into() },
        ShortcutDef { key: "honorificPrefix".into(), writes: "born_in[is=birth].honorificPrefix".into() },
        ShortcutDef { key: "honorificSuffix".into(), writes: "born_in[is=birth].honorificSuffix".into() },
        ShortcutDef { key: "legalName".into(), writes: "born_in[is=birth].legalName".into() },
        ShortcutDef { key: "maidenName".into(), writes: "born_in[is=birth].maidenName".into() },
        ShortcutDef { key: "nameOrder".into(), writes: "born_in[is=birth].nameOrder".into() },
        ShortcutDef { key: "nickname".into(), writes: "born_in[is=birth].nickname".into() },
        ShortcutDef { key: "phoneticFamilyName".into(), writes: "born_in[is=birth].phoneticFamilyName".into() },
        ShortcutDef { key: "phoneticGivenName".into(), writes: "born_in[is=birth].phoneticGivenName".into() },
        ShortcutDef { key: "sortAs".into(), writes: "born_in[is=birth].sortAs".into() },
    ],
    display: Some(DisplaySpec {
        subtitle: Some("about".into()),
        image: Some("image".into()),
        body: Some("notes".into()),
        highlights: vec!["birthdate".into(), "gender".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
