// DO NOT EDIT — generated from platform/ontology/shapes/tax_line.yaml.
// Regen: `python3 platform/codegen/generate.py`.

use super::sdk_prelude::*;

/// A single tax, fee, or surcharge line item on a priced commerce
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", default)]
pub struct TaxLine {
    pub name: String,
    pub text: Option<String>,
    pub url: Option<String>,
    pub image: Option<String>,
    pub author: Option<String>,
    pub date_published: Option<String>,
    pub content: Option<String>,
    pub amount: Option<f64>,
    pub applies_to_index: Option<i64>,
    pub code: Option<String>,
    pub country: Option<String>,
    pub currency: Option<String>,
    pub description: Option<String>,
    pub inclusive: Option<bool>,
    pub kind: Option<String>,
    pub merchant_imposed: Option<bool>,
    pub nature: Option<String>,
    pub rate: Option<f64>,
    pub refundable: Option<bool>,
    pub taxable_amount: Option<f64>,
}

pub static TAX_LINE: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {
    name: "tax_line".into(),
    plural: Some("tax_lines".into()),
    description: Some("A single tax, fee, or surcharge line item on a priced commerce".into()),
    fields: vec![
        FieldDef::required("id", FieldType::String),
        FieldDef::required("name", FieldType::String),
        FieldDef::optional("text", FieldType::String),
        FieldDef::optional("url", FieldType::String),
        FieldDef::optional("image", FieldType::String),
        FieldDef::optional("author", FieldType::String),
        FieldDef::optional("datePublished", FieldType::String),
        FieldDef::optional("content", FieldType::String),
        FieldDef::optional("amount", FieldType::Number),
        FieldDef::optional("appliesToIndex", FieldType::Integer),
        FieldDef::optional("code", FieldType::String),
        FieldDef::optional("country", FieldType::String),
        FieldDef::optional("currency", FieldType::String),
        FieldDef::optional("description", FieldType::String),
        FieldDef::optional("inclusive", FieldType::Boolean),
        FieldDef::optional("kind", FieldType::String),
        FieldDef::optional("merchantImposed", FieldType::Boolean),
        FieldDef::optional("nature", FieldType::String),
        FieldDef::optional("rate", FieldType::Number),
        FieldDef::optional("refundable", FieldType::Boolean),
        FieldDef::optional("taxableAmount", FieldType::Number),
    ],
    out: vec![
        EdgeDef { label: "at_namespace".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "applies_to".into(), to: Some("fare".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "derived_from".into(), to: Some("offer".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "under".into(), to: Some("reservation".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "for".into(), to: Some("leg".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "imposed_by".into(), to: Some("actor".into()), from: None, card: Cardinality::One },
        EdgeDef { label: "held_at".into(), to: Some("place".into()), from: None, card: Cardinality::One },
    ],
    identity: vec!["at".into(), "id".into()],
    display: Some(DisplaySpec {
        subtitle: Some("description".into()),
        ..DisplaySpec::default()
    }),
    prior_art: vec![
        PriorArtDef { source: "IATA List of Ticket and Airport Taxes and Fees (ILTATF)".into(), url: Some("https://www.iata.org/en/publications/store/list-of-ticket-and-airport-taxes-and-fees/".into()), notes: Some("Canonical 1500+ entry registry of 2-char airline tax codes, grouped AT (airport), PC (passenger charge), ST (stamp), TT (ticket), MT (misc). Our `code` = ILTATF code when applicable; `nature` corresponds to ILTATF's grouping.".into()) },
        PriorArtDef { source: "IATA NDC Tax / TaxBreakdown element".into(), url: Some("https://developer.iata.org/en/ndc/".into()), notes: Some("NDC's Price structure carries Taxes/Tax with TaxCode, CollectionPoint, CountryCode, Nature, Amount, Description. Our code/country/nature/amount/description map 1:1. NDC's Nature enum (security, fuel, facility, tax) informs our values.".into()) },
        PriorArtDef { source: "schema.org/UnitPriceSpecification + PriceComponentTypeEnumeration".into(), url: Some("https://schema.org/UnitPriceSpecification".into()), notes: Some("Generic commerce. priceComponentType (\"Tax\"), valueAddedTaxIncluded (our `inclusive`), priceCurrency. Lightweight; we add code, country, `imposedBy` to cover the authority-chain gap.".into()) },
        PriorArtDef { source: "UBL 2.1 / Peppol BIS Billing 3.0 — TaxSubtotal / TaxCategory".into(), url: Some("https://docs.peppol.eu/poacc/billing/3.0/".into()), notes: Some("European eInvoicing. TaxSubtotal carries TaxableAmount, TaxAmount, Percent, TaxCategory/TaxScheme (VAT/GST). Our taxableAmount/amount/rate/nature align directly.".into()) },
        PriorArtDef { source: "Stripe Invoice tax_amounts[]".into(), url: Some("https://docs.stripe.com/api/invoices/object".into()), notes: Some("Stripe's line-item tax_amounts[] carries amount, inclusive, tax_rate, taxability_reason, taxable_amount. Our inclusive/ rate/taxableAmount match; jurisdiction/jurisdiction_level inspired the country + `imposedBy` split.".into()) },
        PriorArtDef { source: "Shopify Order tax_lines[]".into(), url: Some("https://shopify.dev/docs/api/admin-rest/latest/resources/order".into()), notes: Some("Minimal commerce model: price, rate, title, channel_liable. Our amount/rate/description map 1:1. Shopify allows multiple tax_lines per line item with same title + different rates — same pattern we need (US Transportation Tax recurring per segment). We disambiguate via appliesToIndex.".into()) },
        PriorArtDef { source: "Avalara / TaxJar tax breakdown".into(), url: Some("https://developer.avalara.com/".into()), notes: Some("Commerce tax engines. Jurisdiction hierarchy (country / state / county / city / special) and combined tax rate. Informs the `imposedBy: actor` relation for layered jurisdictions (hotel occupancy + tourism + state sales tax, each their own line).".into()) },
    ],
    ..ShapeDef::default()
});
