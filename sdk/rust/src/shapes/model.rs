// DO NOT EDIT — generated from platform/ontology/shapes/model.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// An AI model — LLM, embedding model, or other ML model.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct Model {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub context_length: Option<i64>,
    pub context_window: Option<i64>,
    pub digest: Option<String>,
    pub family: Option<String>,
    pub format: Option<String>,
    pub max_output: Option<i64>,
    pub modality: Option<Vec<String>>,
    pub model_type: Option<String>,
    pub parameter_size: Option<String>,
    pub pricing_input: Option<f64>,
    pub pricing_output: Option<f64>,
    pub quantization: Option<String>,
    pub quantization_level: Option<String>,
    pub size: Option<String>,
}

pub static MODEL: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "model".into(),
    plural: Some("models".into()),
    description: Some("An AI model — LLM, embedding model, or other ML model.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("contextLength", FieldType::Integer),
        FieldDef::optional("contextWindow", FieldType::Integer),
        FieldDef::optional("digest", FieldType::String),
        FieldDef::optional("family", FieldType::String),
        FieldDef::optional("format", FieldType::String),
        FieldDef::optional("maxOutput", FieldType::Integer),
        FieldDef::optional("modality", FieldType::StringList),
        FieldDef::optional("modelType", FieldType::String),
        FieldDef::optional("parameterSize", FieldType::String),
        FieldDef::optional("pricingInput", FieldType::Number),
        FieldDef::optional("pricingOutput", FieldType::Number),
        FieldDef::optional("quantization", FieldType::String),
        FieldDef::optional("quantizationLevel", FieldType::String),
        FieldDef::optional("size", FieldType::String),
    ],
    arrival_vals: vec!["pricingInput".into(), "pricingOutput".into()],
    identity: vec!["at".into(), "name".into()],
    display: Some(DisplaySpec {
        subtitle: Some("name".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "Hugging Face Model Cards".into(), url: Some("https://huggingface.co/docs/hub/en/model-cards".into()), notes: Some("Our provider/contextLength/modality/family/quantization/ parameterSize align with HF model-card metadata conventions.".into()) },
        PriorArtDef { source: "Ollama /api/show + Modelfile".into(), url: Some("https://github.com/ollama/ollama/blob/main/docs/modelfile.md".into()), notes: Some("Our quantization/quantizationLevel/format/digest/parameterSize come directly from Ollama's show-model response.".into()) },
        PriorArtDef { source: "OpenRouter Models API".into(), url: Some("https://openrouter.ai/docs/models".into()), notes: Some("Our contextLength/contextWindow/maxOutput/pricingInput/ pricingOutput mirror OpenRouter's model spec.".into()) },
    ],
    ..ShapeDef::default()
});
