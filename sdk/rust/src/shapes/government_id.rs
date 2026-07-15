// DO NOT EDIT — generated from platform/ontology/shapes/government_id.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A government-issued identity document — passport, driver license,
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct GovernmentId {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub birth_date: Option<String>,
    pub category: String,
    pub class: Option<String>,
    pub expiry_date: Option<String>,
    pub full_name: Option<String>,
    pub identifier: String,
    pub issue_date: Option<String>,
    pub issuing_country: String,
    pub issuing_state: Option<String>,
    pub national_id_last4: Option<String>,
    pub nationality: Option<String>,
    pub place_of_issue: Option<String>,
    pub sex: Option<String>,
    pub status: Option<String>,
}

pub static GOVERNMENT_ID: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "government_id".into(),
    plural: Some("government_ids".into()),
    description: Some("A government-issued identity document — passport, driver license,".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("birthDate", FieldType::Datetime),
        FieldDef::required("category", FieldType::String),
        FieldDef::optional("class", FieldType::String),
        FieldDef::optional("expiryDate", FieldType::Datetime),
        FieldDef::optional("fullName", FieldType::String),
        FieldDef::required("identifier", FieldType::String),
        FieldDef::optional("issueDate", FieldType::Datetime),
        FieldDef::required("issuingCountry", FieldType::String),
        FieldDef::optional("issuingState", FieldType::String),
        FieldDef::optional("nationalIdLast4", FieldType::String),
        FieldDef::optional("nationality", FieldType::String),
        FieldDef::optional("placeOfIssue", FieldType::String),
        FieldDef::optional("sex", FieldType::String),
        FieldDef::optional("status", FieldType::String),
    ],
    timed: Some("self".into()),
    identity: vec!["issuingCountry".into(), "category".into(), "identifier".into()],
    display: Some(DisplaySpec {
        subtitle: Some("category".into()),
        highlights: vec!["identifier".into(), "issuingCountry".into(), "expiryDate".into()],
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "ICAO Doc 9303 (Machine Readable Travel Documents)".into(), url: Some("https://www.icao.int/publications/pages/publication.aspx?docnum=9303".into()), notes: Some("The MRTD standard behind every e-passport MRZ. Our identifier = document number, issuingCountry = issuing state code, fullName / birthDate / sex / nationality / expiryDate map 1:1 onto the MRZ data groups. We store the parsed face values, never the chip's private keys or the full MRZ checksum secrets.".into()) },
        PriorArtDef { source: "schema.org/Permit".into(), url: Some("https://schema.org/Permit".into()), notes: Some("schema.org's closest peer — issuedBy, validFor, validIn, validUntil, permitAudience. Our issuingCountry / issuingState ≈ issuedBy authority; expiryDate ≈ validUntil. Permit is generic; we specialize into identity documents with an ICAO/AAMVA field set.".into()) },
        PriorArtDef { source: "AAMVA DL/ID Card Design Standard (PDF417 barcode)".into(), url: Some("https://www.aamva.org/topics/dl-id-card-design-standard".into()), notes: Some("North American driver-license barcode spec. Our identifier = customer/DL number, class = vehicle class + endorsements, issuingState = jurisdiction, fullName / birthDate / sex / issueDate / expiryDate map onto the AAMVA data elements (DAQ, DCA, DBB, DBA).".into()) },
    ],
    ..ShapeDef::default()
});
