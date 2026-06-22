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
    pub additional_name: Option<String>,
    pub birth_date: Option<String>,
    pub death_date: Option<String>,
    pub family_name: Option<String>,
    pub gender: Option<String>,
    pub given_name: Option<String>,
    pub honorific_prefix: Option<String>,
    pub honorific_suffix: Option<String>,
    pub identities: Option<serde_json::Value>,
    pub legal_name: Option<String>,
    pub maiden_name: Option<String>,
    pub name_order: Option<String>,
    pub nickname: Option<String>,
    pub notes: Option<String>,
    pub phonetic_family_name: Option<String>,
    pub phonetic_given_name: Option<String>,
    pub sort_as: Option<String>,
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
        FieldDef::optional("additionalName", FieldType::String),
        FieldDef::optional("birthDate", FieldType::Datetime),
        FieldDef::optional("deathDate", FieldType::Datetime),
        FieldDef::optional("familyName", FieldType::String),
        FieldDef::optional("gender", FieldType::String),
        FieldDef::optional("givenName", FieldType::String),
        FieldDef::optional("honorificPrefix", FieldType::String),
        FieldDef::optional("honorificSuffix", FieldType::String),
        FieldDef { name: "identities".into(), ty: FieldType::Json, description: Some("One human, every way to reach or recognize them — an array of identity claims: [{platform, id, handle?, instance?, account?}]. Emit one entry per identity you know: source address-books ({platform:\"google\", id:<resourceName>, account:<book email>}, {platform:\"icloud\", id:<vCard UID>}), join keys ({platform:\"email\", id:<address>}, {platform:\"phone\", id:<number>}), and social ({platform:\"x\", id:<numeric id>, handle:\"conorh\"}). `id` is the STABLE MATCH KEY — a canonical, sync-surviving identifier (DID / UUID / numeric id / actor URI / Google resourceName / vCard UID, or a normalized email / E.164 phone). Emit it already canonical: phone → E.164 (+15125551234), email → lowercased (Gmail also strips dots and +tags). `handle` is the mutable human-facing name (@user) — display + URL only, NEVER matched alone (handles get recycled). `instance` scopes a federated handle (Mastodon homeserver, Matrix). `account` (address-book sources only) names which book. URL / icon / label / category all DERIVE from the `platform` registry node — never store them per entry. You do NOT dedup: just upsert what a book returned. On write the engine OR-matches each `(platform, id)` claim, MERGES into the existing person on any collision (unioning both sets, losing no source), and returns a receipt naming the matched signal (\"merged into X — matched phone +1…\"). Name never matches; handle-only entries (no `id`) are never indexed, so they never trigger a merge. Merges are conservative and will become reversible via `split`.".into()), required: false },
        FieldDef::optional("legalName", FieldType::String),
        FieldDef::optional("maidenName", FieldType::String),
        FieldDef::optional("nameOrder", FieldType::String),
        FieldDef::optional("nickname", FieldType::String),
        FieldDef::optional("notes", FieldType::Text),
        FieldDef::optional("phoneticFamilyName", FieldType::String),
        FieldDef::optional("phoneticGivenName", FieldType::String),
        FieldDef::optional("sortAs", FieldType::String),
    ],
    also: vec!["actor".into()],
    timed: Some("self".into()),
    derived: vec![
        DerivedBinding { key: "current_residence".into(), spec: serde_json::from_str("{\"find\": \"lived_at\", \"where_link\": {\"to\": null}, \"get\": \"name\"}").unwrap_or(serde_json::Value::Null) },
        DerivedBinding { key: "current_role".into(), spec: serde_json::from_str("{\"find\": \"worked_at\", \"where_link\": {\"to\": null}, \"get\": \"title\"}").unwrap_or(serde_json::Value::Null) },
    ],
    display: Some(DisplaySpec {
        subtitle: Some("about".into()),
        image: Some("image".into()),
        body: Some("notes".into()),
        highlights: vec!["birthDate".into(), "gender".into()],
        ..DisplaySpec::default()
    }),
    groups: vec![
        FieldGroupDef { name: "Name".into(), fields: vec!["givenName".into(), "additionalName".into(), "familyName".into(), "nickname".into(), "legalName".into(), "maidenName".into()] },
        FieldGroupDef { name: "Personal".into(), fields: vec!["birthDate".into(), "gender".into(), "current_residence".into(), "current_role".into()] },
        FieldGroupDef { name: "About".into(), fields: vec!["about".into(), "notes".into(), "url".into()] },
    ],
    prior_art: vec![
        PriorArtDef { source: "schema.org/Person".into(), url: Some("https://schema.org/Person".into()), notes: Some("givenName / familyName / additionalName / honorificPrefix / honorificSuffix / birthDate map 1:1 onto plain fields. schema.org keeps these flat on Person; so do we — they are intrinsic to the one human. We diverge by modeling `identities[]` as a first-class uniform set rather than scattered sameAs URLs.".into()) },
        PriorArtDef { source: "vCard 4.0 (RFC 6350) §6.2.2 N property + §5.9 SORT-AS".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc6350#section-6.2.2".into()), notes: Some("The N property is `family;given;additional;prefixes;suffixes`, each comma-multi-valued. Round-trips exactly through the structured name fields; SORT-AS → `sortAs`.".into()) },
        PriorArtDef { source: "W3C i18n — Personal names around the world".into(), url: Some("https://www.w3.org/International/questions/qa-personal-names".into()), notes: Some("Canonical reference for why \"first/last\" is a Western bias. CJK names put family first; Spanish uses two surnames; Icelandic uses patronymics. `nameOrder` captures the rendering rule; structured fields stay neutral.".into()) },
        PriorArtDef { source: "FOAF (Friend of a Friend)".into(), url: Some("http://xmlns.com/foaf/spec/".into()), notes: Some("Original social-graph vocabulary. Largely superseded by schema.org but still a reference for account-centric modeling.".into()) },
    ],
    ..ShapeDef::default()
});
