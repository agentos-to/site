// DO NOT EDIT — generated from platform/ontology/shapes/flow.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A process / swim-lane — actors across ordered steps. The universal shape
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Flow {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub goal: Option<String>,
    pub status: Option<String>,
    pub trigger: Option<String>,
}

pub static FLOW: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "flow".into(),
    plural: Some("flows".into()),
    description: Some("A process / swim-lane — actors across ordered steps. The universal shape".into()),
    icon: Some("workflow".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("goal", FieldType::Text),
        FieldDef::optional("status", FieldType::String),
        FieldDef::optional("trigger", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "involves".into(), to: Some("node".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "has_step".into(), to: Some("step".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "serves".into(), to: Some("node".into()), from: None, card: Cardinality::Many },
        EdgeDef { label: "produces".into(), to: Some("node".into()), from: None, card: Cardinality::One },
    ],
    display: Some(DisplaySpec {
        subtitle: Some("goal".into()),
        highlights: vec!["trigger".into(), "status".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "BPMN 2.0 (OMG)".into(), url: Some("https://www.omg.org/spec/BPMN/2.0/".into()), notes: Some("Pools/lanes = actors; SequenceFlow imposes step order; the lane a step sits in assigns its actor.".into()) },
        PriorArtDef { source: "schema.org/HowTo".into(), url: Some("https://schema.org/HowTo".into()), notes: Some("HowTo = a flow; its steps are HowToStep items; HowTo.result ≈ goal.".into()) },
        PriorArtDef { source: "UML Activity Diagram (activity partitions)".into(), url: Some("https://www.uml-diagrams.org/activity-diagrams.html".into()), notes: Some("Activity partitions are the formal name for swim-lanes; actions are ordered by control flow.".into()) },
    ],
    ..ShapeDef::default()
});
