// DO NOT EDIT — generated from platform/ontology/shapes/bookmark.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A pointer into the graph — the universal shortcut. A bookmark is a
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Bookmark {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub address: Option<String>,
    pub handle: Option<String>,
}

pub static BOOKMARK: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "bookmark".into(),
    plural: Some("bookmarks".into()),
    description: Some("A pointer into the graph — the universal shortcut. A bookmark is a".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("address", FieldType::String),
        FieldDef::optional("handle", FieldType::String),
    ],
    identity: vec!["points_to".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Browser bookmarks (Mosaic / Netscape Navigator hotlist)".into(), url: Some("https://en.wikipedia.org/wiki/Bookmark_(digital)".into()), notes: Some("Direct precedent. A bookmark is a name + a target; the target is the contract; the surface doesn't care what's behind it. We replace HTTP URLs with graph node references; everything else maps 1:1.".into()) },
        PriorArtDef { source: "macOS alias / Windows .lnk file".into(), url: Some("https://en.wikipedia.org/wiki/Alias_(Mac_OS)".into()), notes: Some("OS-level shortcut primitive. Same shape: name + target. Per- instance position is handled by the parent folder/desktop in both — for us that lives on the contains-link.".into()) },
        PriorArtDef { source: "Finder sidebar / Windows Explorer Quick Access".into(), url: Some("https://support.apple.com/guide/mac-help/customize-the-finder-sidebar-mchlp3014/mac".into()), notes: Some("OS file managers use a bookmark sidebar as their universal navigation primitive (My Computer, Documents, Network). We treat every shape the same way — bookmark to any graph node, no FS bias.".into()) },
    ],
    ..ShapeDef::default()
});
