// DO NOT EDIT — generated from platform/ontology/shapes/milestone.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A point-in-time checkpoint — a significant, zero-duration moment in a
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Milestone {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub all_day: Option<bool>,
    pub criterion: Option<String>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub end_date: Option<String>,
    pub ical_uid: Option<String>,
    pub properties: Option<serde_json::Value>,
    pub reached_at: Option<String>,
    pub recurrence: Option<Vec<String>>,
    pub show_as: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub timezone: Option<String>,
    pub visibility: Option<String>,
}

pub static MILESTONE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "milestone".into(),
    plural: Some("milestones".into()),
    description: Some("A point-in-time checkpoint — a significant, zero-duration moment in a".into()),
    icon: Some("flag".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("allDay", FieldType::Boolean),
        FieldDef::optional("criterion", FieldType::Text),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("reachedAt", FieldType::Datetime),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "part_of".into(), to: Some("node".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "blocked_by".into(), to: Some("milestone".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "completes".into(), to: Some("node".into()), from: None, card: Cardinality::Many },
    ],
    also: vec!["event".into()],
    display: Some(DisplaySpec {
        subtitle: Some("status".into()),
        body: Some("criterion".into()),
        highlights: vec!["status".into(), "reachedAt".into()],
        ..DisplaySpec::default()
    }),
    ..ShapeDef::default()
});
