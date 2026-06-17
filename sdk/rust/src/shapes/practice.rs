// DO NOT EDIT — generated from platform/ontology/shapes/practice.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A field of practice or study — a discipline a person practices, or the
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Practice {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub aliases: Option<Vec<String>>,
    pub code: Option<String>,
    pub code_system: Option<String>,
    pub description: Option<String>,
}

pub static PRACTICE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "practice".into(),
    plural: Some("practices".into()),
    description: Some("A field of practice or study — a discipline a person practices, or the".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("aliases", FieldType::StringList),
        FieldDef::optional("code", FieldType::String),
        FieldDef::optional("codeSystem", FieldType::String),
        FieldDef::optional("description", FieldType::Text),
    ],
    display: Some(DisplaySpec {
        subtitle: Some("parent".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "NUCC Health Care Provider Taxonomy".into(), url: Some("https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40".into()), notes: Some("US medical-specialty code set — 3 levels (Grouping / Classification / Specialization), 10-char alphanumeric codes. The source for codeSystem=NUCC and for the parent-link hierarchy.".into()) },
        PriorArtDef { source: "Standard Occupational Classification (SOC) / O*NET-SOC".into(), url: Some("https://www.bls.gov/soc/".into()), notes: Some("US occupational taxonomy spanning every profession — 4 levels (Major / Minor / Broad / Detailed). codeSystem=SOC.".into()) },
        PriorArtDef { source: "ISCED Fields of Education and Training 2013 (ISCED-F)".into(), url: Some("https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/international-standard-classification-education-fields-education-and".into()), notes: Some("UNESCO field-of-study taxonomy — 3 levels (Broad / Narrow / Detailed). The field-of-study side, for a qualification's `field`.".into()) },
        PriorArtDef { source: "schema.org CategoryCode / occupationalCategory".into(), url: Some("https://schema.org/occupationalCategory".into()), notes: Some("schema.org has no dedicated discipline type — only the pluggable CategoryCode (codeValue + inCodeSet). Confirms code + codeSystem as a loose optional pair, not a hard taxonomy dependency.".into()) },
    ],
    ..ShapeDef::default()
});
