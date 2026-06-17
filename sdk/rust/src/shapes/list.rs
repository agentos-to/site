// DO NOT EDIT — generated from platform/ontology/shapes/list.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A list — the universal ordered (or not) collection. Folders, menus,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct List {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub arrangement: Option<String>,
    #[serde(rename = "default_view")]
    pub default_view: Option<String>,
    #[serde(rename = "icon_size")]
    pub icon_size: Option<i64>,
    pub is_default: Option<bool>,
    pub is_public: Option<bool>,
    pub item_count: Option<i64>,
    pub list_id: Option<String>,
    pub list_type: Option<String>,
    #[serde(rename = "member_shape")]
    pub member_shape: Option<String>,
    #[serde(rename = "ordering_mode")]
    pub ordering_mode: Option<String>,
    pub path: Option<String>,
    pub privacy: Option<String>,
    #[serde(rename = "sort_by")]
    pub sort_by: Option<String>,
}

pub static LIST: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "list".into(),
    plural: Some("lists".into()),
    description: Some("A list — the universal ordered (or not) collection. Folders, menus,".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("arrangement", FieldType::String),
        FieldDef::optional("default_view", FieldType::String),
        FieldDef::optional("icon_size", FieldType::Integer),
        FieldDef::optional("isDefault", FieldType::Boolean),
        FieldDef::optional("isPublic", FieldType::Boolean),
        FieldDef::optional("itemCount", FieldType::Integer),
        FieldDef::optional("listId", FieldType::String),
        FieldDef::optional("listType", FieldType::String),
        FieldDef::optional("member_shape", FieldType::String),
        FieldDef::optional("ordering_mode", FieldType::String),
        FieldDef::optional("path", FieldType::String),
        FieldDef::optional("privacy", FieldType::String),
        FieldDef::optional("sort_by", FieldType::String),
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "schema.org/ItemList".into(), url: Some("https://schema.org/ItemList".into()), notes: Some("listType ≈ itemListOrder; contains ≈ itemListElement; isPublic ≈ publicAccess.".into()) },
        PriorArtDef { source: "ActivityStreams 2.0 Collection / OrderedCollection".into(), url: Some("https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection".into()), notes: Some("contains[] ≈ items; ordering_mode='linear' ≈ OrderedCollection, ordering_mode='unordered' ≈ Collection.".into()) },
        PriorArtDef { source: "WinFS Item / FolderMember".into(), url: Some("https://learn.microsoft.com/en-us/archive/msdn-magazine/2004/january/winfs-lets-users-search-and-manage-files-based-on-content".into()), notes: Some("WinFS unified Folder + Contact + Photo under a single Item base, with FolderMember as a holding link. Our list-with-contains is the same pattern: one shape, one link mechanism, view-time projections handle the \"I want it to look like an album\" case.".into()) },
        PriorArtDef { source: "Vannevar Bush — As We May Think (Memex trails)".into(), url: Some("https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/".into()), notes: Some("A Memex trail is a named, ordered list of associative jumps. A `list` with ordering_mode='linear' and contains-bookmarks IS Bush's trail. Foundational precedent for the everything-is-a-list thesis.".into()) },
        PriorArtDef { source: "POSIX / Single Unix Specification (directories)".into(), url: Some("https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html".into()), notes: Some("listType='folder' with optional `path` field mirrors a POSIX directory. The engine treats it as a list; the filesystem mirror is a projection, not a separate primitive.".into()) },
    ],
    ..ShapeDef::default()
});
