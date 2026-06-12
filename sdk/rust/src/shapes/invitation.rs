// DO NOT EDIT — generated from platform/ontology/shapes/invitation.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An invitation to join something — an organization, a workspace, a team, a
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Invitation {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub accepted_at: Option<String>,
    pub all_day: Option<bool>,
    pub current_url: Option<String>,
    pub date_updated: Option<String>,
    pub distinct_id: Option<String>,
    pub email: Option<String>,
    pub end_date: Option<String>,
    pub ical_uid: Option<String>,
    pub invitation_type: Option<String>,
    pub message: Option<String>,
    pub properties: Option<serde_json::Value>,
    pub recurrence: Option<Vec<String>>,
    pub revoked_at: Option<String>,
    pub role: Option<String>,
    pub show_as: Option<String>,
    pub source_title: Option<String>,
    pub source_url: Option<String>,
    pub start_date: Option<String>,
    pub status: Option<String>,
    pub timezone: Option<String>,
    pub token: Option<String>,
    pub visibility: Option<String>,
}

pub static INVITATION: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "invitation".into(),
    plural: Some("invitations".into()),
    description: Some("An invitation to join something — an organization, a workspace, a team, a".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("acceptedAt", FieldType::Datetime),
        FieldDef::optional("allDay", FieldType::Boolean),
        FieldDef::optional("currentUrl", FieldType::String),
        FieldDef::optional("dateUpdated", FieldType::Datetime),
        FieldDef::optional("distinctId", FieldType::String),
        FieldDef::optional("email", FieldType::String),
        FieldDef::optional("endDate", FieldType::Datetime),
        FieldDef::optional("icalUid", FieldType::String),
        FieldDef::optional("invitationType", FieldType::String),
        FieldDef::optional("message", FieldType::Text),
        FieldDef::optional("properties", FieldType::Json),
        FieldDef::optional("recurrence", FieldType::StringList),
        FieldDef::optional("revokedAt", FieldType::Datetime),
        FieldDef::optional("role", FieldType::String),
        FieldDef::optional("showAs", FieldType::String),
        FieldDef::optional("sourceTitle", FieldType::String),
        FieldDef::optional("sourceUrl", FieldType::Url),
        FieldDef::optional("startDate", FieldType::Datetime),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("timezone", FieldType::String),
        FieldDef::optional("token", FieldType::String),
        FieldDef::optional("visibility", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "extended_by".into(), to: Some("account".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "extended_to".into(), to: Some("account".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "within_org".into(), to: Some("organization".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "at_namespace".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
    ],
    also: vec!["event".into()],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("invitationType".into()),
        highlights: vec!["startDate".into(), "endDate".into(), "location".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "ActivityStreams 2.0 Invite activity".into(), url: Some("https://www.w3.org/TR/activitystreams-vocabulary/#dfn-invite".into()), notes: Some("AS2 Invite is the canonical fediverse verb. Our inviter = actor; invitee = target; status tracks Accept/Reject/TentativeAccept responses.".into()) },
        PriorArtDef { source: "iCalendar ATTENDEE + PARTSTAT (RFC 5545)".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc5545".into()), notes: Some("Calendar-style invitations. Our status maps to PARTSTAT (NEEDS-ACTION/ACCEPTED/DECLINED/DELEGATED).".into()) },
        PriorArtDef { source: "SCIM 2.0 (RFC 7644) — user provisioning".into(), url: Some("https://datatracker.ietf.org/doc/html/rfc7644".into()), notes: Some("Enterprise invitation/provisioning. Our email/role/organization align with SCIM User resource's email + entitlements + group membership.".into()) },
    ],
    ..ShapeDef::default()
});
