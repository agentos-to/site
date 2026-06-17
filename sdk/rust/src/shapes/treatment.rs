// DO NOT EDIT — generated from platform/ontology/shapes/treatment.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A named therapeutic approach — a modality. CBT, DBT, EMDR, IFS, CPT,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Treatment {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub abbreviation: Option<String>,
    pub aliases: Option<Vec<String>>,
    pub description: Option<String>,
}

pub static TREATMENT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "treatment".into(),
    plural: Some("treatments".into()),
    description: Some("A named therapeutic approach — a modality. CBT, DBT, EMDR, IFS, CPT,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("abbreviation", FieldType::String),
        FieldDef::optional("aliases", FieldType::StringList),
        FieldDef::optional("description", FieldType::Text),
    ],
    identity_any: vec!["name".into(), "abbreviation".into()],
    display: Some(DisplaySpec {
        subtitle: Some("abbreviation".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Psychology Today — \"Types of Therapy\"".into(), url: Some("https://www.psychologytoday.com/us/types-of-therapy".into()), notes: Some("The canonical directory of ~80 modalities with name + abbreviation + description — the facet a therapist lists and a client filters by. The source for treating modality as a first-class named thing.".into()) },
        PriorArtDef { source: "APA Division 12 — Research-Supported Psychological Treatments".into(), url: Some("https://div12.org/treatments/".into()), notes: Some("Maps treatments to the disorders/concerns they have evidence for — i.e. the `treats --> concern` edge, with a research-strength rating. Confirms the indication is the defining relationship of a modality.".into()) },
        PriorArtDef { source: "SAMHSA Evidence-Based Practices Resource Center".into(), url: Some("https://www.samhsa.gov/resource-search/ebp".into()), notes: Some("Federal catalogue of evidence-based behavioral-health interventions, each indexed by the conditions it addresses — reinforces modality-as- entity indexed by indication rather than by delivering organization.".into()) },
    ],
    ..ShapeDef::default()
});
