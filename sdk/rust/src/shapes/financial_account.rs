// DO NOT EDIT — generated from platform/ontology/shapes/financial_account.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A financial account — bank checking/savings, brokerage, crypto wallet, etc.
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct FinancialAccount {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub account_id: Option<String>,
    pub account_number: Option<String>,
    pub account_type: Option<String>,
    pub available: Option<f64>,
    pub balance: Option<f64>,
    pub card_type: Option<String>,
    pub credit_limit: Option<f64>,
    pub currency: Option<String>,
    pub identifier: String,
    pub interest_rate: Option<f64>,
    pub last4: Option<String>,
    pub minimum_payment: Option<f64>,
    pub routing_number: Option<String>,
}

pub static FINANCIAL_ACCOUNT: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "financial_account".into(),
    plural: Some("financial_accounts".into()),
    description: Some("A financial account — bank checking/savings, brokerage, crypto wallet, etc.".into()),
    fields: vec![
        FieldDef::optional("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("accountId", FieldType::String),
        FieldDef::optional("accountNumber", FieldType::String),
        FieldDef::optional("accountType", FieldType::String),
        FieldDef::optional("available", FieldType::Number),
        FieldDef::optional("balance", FieldType::Number),
        FieldDef::optional("cardType", FieldType::String),
        FieldDef::optional("creditLimit", FieldType::Number),
        FieldDef::optional("currency", FieldType::String),
        FieldDef::required("identifier", FieldType::String),
        FieldDef::optional("interestRate", FieldType::Number),
        FieldDef::optional("last4", FieldType::String),
        FieldDef::optional("minimumPayment", FieldType::Number),
        FieldDef::optional("routingNumber", FieldType::String),
    ],
    out: vec![
        EdgeDef { label: "at_namespace".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "accessed_via".into(), to: Some("account".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "owned_by".into(), to: Some("person".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["at".into(), "identifier".into()],
    display: Some(DisplaySpec {
        subtitle: Some("last4".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "OFX (Open Financial Exchange)".into(), url: Some("https://financialdataexchange.org/ofx".into()), notes: Some("Bank-feed canonical. Our accountNumber / routingNumber / balance / available map to OFX BANKACCTFROM / LEDGERBAL / AVAILBAL.".into()) },
        PriorArtDef { source: "ISO 20022 Financial Messaging".into(), url: Some("https://www.iso20022.org/".into()), notes: Some("Modern bank-messaging standard. Our last4 / cardType / creditLimit / interestRate align with ISO 20022 Card / Account components.".into()) },
        PriorArtDef { source: "schema.org/BankAccount".into(), url: Some("https://schema.org/BankAccount".into()), notes: Some("Our accountNumber ≈ accountId; balance / available are accountMinimumInflow / accountOverdraftLimit loosely; cardType fits schema.org/CreditCard.".into()) },
        PriorArtDef { source: "1Password Bank Account item".into(), url: Some("https://1password.com/".into()), notes: Some("1P's Bank Account category holds institution + account number + routing + type — same shape. Their Crypto Wallet and Credit Card are separate categories; we treat them as different `accountType` values on the same shape for now, splitting only if the field diversity forces it.".into()) },
    ],
    ..ShapeDef::default()
});
