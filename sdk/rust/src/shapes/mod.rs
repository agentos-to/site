// DO NOT EDIT — generated from platform/ontology/shapes/*.yaml.
// Regen: `python3 platform/codegen/generate.py`.

#![allow(non_upper_case_globals)]

// Curated prelude for the generated shape files. Every shape file does
// `use super::sdk_prelude::*;` — one canonical import line, no per-file
// symbol list, no namespace leakage from mod.rs's own lookup machinery
// below (PreviewPolicy, Display, lookup_*, etc). Standard Rust idiom:
// `serde::prelude`, `clap::prelude`, `bevy::prelude::*` all work this way.
//
// Symbol set is derived from the ontology — only the types at least one
// shape references are re-exported, so an unused-import warning here is
// impossible by construction.
pub(crate) mod sdk_prelude {
    pub(crate) use agentos_graph::{
        DerivedBinding, DisplaySpec, FieldDef, FieldType, ShapeDef, ShortcutDef,
    };
    pub(crate) use once_cell::sync::Lazy;
    pub(crate) use serde::{Deserialize, Serialize};
}

pub mod account;
pub mod activity;
pub mod actor;
pub mod aircraft;
pub mod airline;
pub mod airport;
pub mod app;
pub mod birth;
pub mod book;
pub mod booking_offer;
pub mod bookmark;
pub mod branch;
pub mod brand;
pub mod calendar;
pub mod channel;
pub mod class;
pub mod community;
pub mod conversation;
pub mod conversion;
pub mod creative_work;
pub mod credential;
pub mod dimension;
pub mod dns_record;
pub mod document;
pub mod domain;
pub mod email;
pub mod episode;
pub mod event;
pub mod fare;
pub mod file;
pub mod financial_account;
pub mod flight;
pub mod font;
pub mod git_commit;
pub mod group;
pub mod health_biomarker;
pub mod health_condition;
pub mod health_immunization;
pub mod health_lab;
pub mod health_observation;
pub mod health_panel;
pub mod health_procedure;
pub mod health_reference_range;
pub mod icon;
pub mod image;
pub mod intellectual_property;
pub mod invitation;
pub mod launch;
pub mod leg;
pub mod list;
pub mod loaded_model;
pub mod mcp_session;
pub mod meeting;
pub mod membership;
pub mod message;
pub mod model;
pub mod note;
pub mod offer;
pub mod order;
pub mod organization;
pub mod pass;
pub mod payment_method;
pub mod person;
pub mod place;
pub mod playlist;
pub mod podcast;
pub mod post;
pub mod practice;
pub mod product;
pub mod project;
pub mod protocol;
pub mod qualification;
pub mod quantity_kind;
pub mod quote;
pub mod repository;
pub mod reservation;
pub mod result;
pub mod review;
pub mod role;
pub mod seatmap;
pub mod shelf;
pub mod skill;
pub mod software;
pub mod sound;
pub mod source;
pub mod spec;
pub mod tag;
pub mod task;
pub mod tax_line;
pub mod theme;
pub mod tool_call;
pub mod transaction;
pub mod transcript;
pub mod transition;
pub mod trip;
pub mod unit;
pub mod user;
pub mod video;
pub mod volume;
pub mod webpage;
pub mod website;

pub use account::{ACCOUNT, Account};
pub use activity::{ACTIVITY, Activity};
pub use actor::{ACTOR, Actor};
pub use aircraft::{AIRCRAFT, Aircraft};
pub use airline::{AIRLINE, Airline};
pub use airport::{AIRPORT, Airport};
pub use app::{APP, App};
pub use birth::{BIRTH, Birth};
pub use book::{BOOK, Book};
pub use booking_offer::{BOOKING_OFFER, BookingOffer};
pub use bookmark::{BOOKMARK, Bookmark};
pub use branch::{BRANCH, Branch};
pub use brand::{BRAND, Brand};
pub use calendar::{CALENDAR, Calendar};
pub use channel::{CHANNEL, Channel};
pub use class::{CLASS, Class};
pub use community::{COMMUNITY, Community};
pub use conversation::{CONVERSATION, Conversation};
pub use conversion::{CONVERSION, Conversion};
pub use creative_work::{CREATIVE_WORK, CreativeWork};
pub use credential::{CREDENTIAL, Credential};
pub use dimension::{DIMENSION, Dimension};
pub use dns_record::{DNS_RECORD, DnsRecord};
pub use document::{DOCUMENT, Document};
pub use domain::{DOMAIN, Domain};
pub use email::{EMAIL, Email};
pub use episode::{EPISODE, Episode};
pub use event::{EVENT, Event};
pub use fare::{FARE, Fare};
pub use file::{FILE, File};
pub use financial_account::{FINANCIAL_ACCOUNT, FinancialAccount};
pub use flight::{FLIGHT, Flight};
pub use font::{FONT, Font};
pub use git_commit::{GIT_COMMIT, GitCommit};
pub use group::{GROUP, Group};
pub use health_biomarker::{HEALTH_BIOMARKER, HealthBiomarker};
pub use health_condition::{HEALTH_CONDITION, HealthCondition};
pub use health_immunization::{HEALTH_IMMUNIZATION, HealthImmunization};
pub use health_lab::{HEALTH_LAB, HealthLab};
pub use health_observation::{HEALTH_OBSERVATION, HealthObservation};
pub use health_panel::{HEALTH_PANEL, HealthPanel};
pub use health_procedure::{HEALTH_PROCEDURE, HealthProcedure};
pub use health_reference_range::{HEALTH_REFERENCE_RANGE, HealthReferenceRange};
pub use icon::{ICON, Icon};
pub use image::{IMAGE, Image};
pub use intellectual_property::{INTELLECTUAL_PROPERTY, IntellectualProperty};
pub use invitation::{INVITATION, Invitation};
pub use launch::{LAUNCH, Launch};
pub use leg::{LEG, Leg};
pub use list::{LIST, List};
pub use loaded_model::{LOADED_MODEL, LoadedModel};
pub use mcp_session::{MCP_SESSION, McpSession};
pub use meeting::{MEETING, Meeting};
pub use membership::{MEMBERSHIP, Membership};
pub use message::{MESSAGE, Message};
pub use model::{MODEL, Model};
pub use note::{NOTE, Note};
pub use offer::{OFFER, Offer};
pub use order::{ORDER, Order};
pub use organization::{ORGANIZATION, Organization};
pub use pass::{PASS, Pass};
pub use payment_method::{PAYMENT_METHOD, PaymentMethod};
pub use person::{PERSON, Person};
pub use place::{PLACE, Place};
pub use playlist::{PLAYLIST, Playlist};
pub use podcast::{PODCAST, Podcast};
pub use post::{POST, Post};
pub use practice::{PRACTICE, Practice};
pub use product::{PRODUCT, Product};
pub use project::{PROJECT, Project};
pub use protocol::{PROTOCOL, Protocol};
pub use qualification::{QUALIFICATION, Qualification};
pub use quantity_kind::{QUANTITY_KIND, QuantityKind};
pub use quote::{QUOTE, Quote};
pub use repository::{REPOSITORY, Repository};
pub use reservation::{RESERVATION, Reservation};
pub use result::{RESULT, Result};
pub use review::{REVIEW, Review};
pub use role::{ROLE, Role};
pub use seatmap::{SEATMAP, Seatmap};
pub use shelf::{SHELF, Shelf};
pub use skill::{SKILL, Skill};
pub use software::{SOFTWARE, Software};
pub use sound::{SOUND, Sound};
pub use source::{SOURCE, Source};
pub use spec::{SPEC, Spec};
pub use tag::{TAG, Tag};
pub use task::{TASK, Task};
pub use tax_line::{TAX_LINE, TaxLine};
pub use theme::{THEME, Theme};
pub use tool_call::{TOOL_CALL, ToolCall};
pub use transaction::{TRANSACTION, Transaction};
pub use transcript::{TRANSCRIPT, Transcript};
pub use transition::{TRANSITION, Transition};
pub use trip::{TRIP, Trip};
pub use unit::{UNIT, Unit};
pub use user::{USER, User};
pub use video::{VIDEO, Video};
pub use volume::{VOLUME, Volume};
pub use webpage::{WEBPAGE, Webpage};
pub use website::{WEBSITE, Website};

// ===========================================================
// Display specs — `display:` block per shape
// ===========================================================

/// Per-field clip policy at preview/card density.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum PreviewPolicy {
    Clip,
    Full,
    MaxChars(usize),
}

/// The five closed roles every theme + renderer projects against.
#[derive(Debug, Clone)]
pub struct Display {
    pub title: Option<&'static str>,
    pub subtitle: Option<&'static str>,
    pub image: Option<&'static str>,
    pub highlights: &'static [&'static str],
    pub body: Option<&'static str>,
    pub preview: &'static [(&'static str, PreviewPolicy)],
    pub also: &'static [&'static str],
}

pub fn lookup_display(shape: &str) -> Option<&'static Display> {
    SHAPE_DISPLAY.iter().find(|(name, _)| *name == shape).map(|(_, d)| d)
}

pub static SHAPE_DISPLAY: &[(&'static str, Display)] = &[
    ("account", Display {
        title: None,
        subtitle: Some("identifier"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("activity", Display {
        title: None,
        subtitle: Some("action"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("actor", Display {
        title: None,
        subtitle: Some("actorType"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("aircraft", Display {
        title: None,
        subtitle: Some("model"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &["product"],
    }),
    ("airline", Display {
        title: None,
        subtitle: Some("iataCode"),
        image: Some("image"),
        highlights: &["headquarters"],
        body: None,
        preview: &[],
        also: &["organization", "actor"],
    }),
    ("airport", Display {
        title: None,
        subtitle: Some("iataCode"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("app", Display {
        title: None,
        subtitle: Some("name"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("birth", Display {
        title: None,
        subtitle: Some("location"),
        image: None,
        highlights: &["startDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("book", Display {
        title: None,
        subtitle: Some("written_by"),
        image: Some("image"),
        highlights: &["datePublished", "published_by"],
        body: Some("description"),
        preview: &[],
        also: &["creative_work", "product"],
    }),
    ("booking_offer", Display {
        title: None,
        subtitle: Some("totalAmount"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("bookmark", Display {
        title: None,
        subtitle: Some("name"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("branch", Display {
        title: None,
        subtitle: Some("commit"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("brand", Display {
        title: None,
        subtitle: Some("tagline"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("calendar", Display {
        title: None,
        subtitle: Some("source"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("channel", Display {
        title: None,
        subtitle: Some("subscriberCount"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("class", Display {
        title: None,
        subtitle: Some("activityType"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("community", Display {
        title: None,
        subtitle: Some("text"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("conversation", Display {
        title: None,
        subtitle: Some("text"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("conversion", Display {
        title: None,
        subtitle: Some("kind"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("creative_work", Display {
        title: None,
        subtitle: Some("written_by"),
        image: Some("image"),
        highlights: &["datePublished", "published_by"],
        body: Some("description"),
        preview: &[],
        also: &[],
    }),
    ("credential", Display {
        title: None,
        subtitle: Some("source"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("dimension", Display {
        title: None,
        subtitle: Some("label"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("dns_record", Display {
        title: None,
        subtitle: Some("recordType"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("document", Display {
        title: None,
        subtitle: Some("contentType"),
        image: None,
        highlights: &["datePublished", "author", "wordCount"],
        body: Some("abstract"),
        preview: &[],
        also: &["file"],
    }),
    ("domain", Display {
        title: None,
        subtitle: Some("registrar"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("email", Display {
        title: None,
        subtitle: Some("author"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &["message"],
    }),
    ("episode", Display {
        title: None,
        subtitle: Some("author"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("event", Display {
        title: None,
        subtitle: Some("startDate"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("fare", Display {
        title: None,
        subtitle: Some("fareFamily"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("file", Display {
        title: None,
        subtitle: Some("path"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("financial_account", Display {
        title: None,
        subtitle: Some("last4"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("flight", Display {
        title: None,
        subtitle: Some("airline"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["leg", "event"],
    }),
    ("font", Display {
        title: None,
        subtitle: Some("author"),
        image: Some("image"),
        highlights: &["datePublished", "published_by"],
        body: Some("description"),
        preview: &[],
        also: &["creative_work"],
    }),
    ("git_commit", Display {
        title: None,
        subtitle: Some("author"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("group", Display {
        title: None,
        subtitle: Some("category"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("health-biomarker", Display {
        title: None,
        subtitle: Some("category"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("health-condition", Display {
        title: None,
        subtitle: Some("clinicalStatus"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("health-immunization", Display {
        title: None,
        subtitle: Some("dateAdministered"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("health-lab", Display {
        title: None,
        subtitle: Some("labType"),
        image: Some("image"),
        highlights: &["headquarters"],
        body: None,
        preview: &[],
        also: &["organization", "actor"],
    }),
    ("health-observation", Display {
        title: None,
        subtitle: Some("startDate"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["result", "event"],
    }),
    ("health-panel", Display {
        title: None,
        subtitle: Some("startDate"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["list", "event"],
    }),
    ("health-procedure", Display {
        title: None,
        subtitle: Some("performedDate"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("health-reference-range", Display {
        title: None,
        subtitle: Some("refText"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("icon", Display {
        title: None,
        subtitle: Some("purpose"),
        image: Some("image"),
        highlights: &["datePublished", "published_by"],
        body: Some("description"),
        preview: &[],
        also: &["creative_work"],
    }),
    ("image", Display {
        title: None,
        subtitle: Some("format"),
        image: Some("image"),
        highlights: &["datePublished", "published_by"],
        body: Some("description"),
        preview: &[],
        also: &["creative_work", "file"],
    }),
    ("intellectual_property", Display {
        title: None,
        subtitle: Some("category"),
        image: None,
        highlights: &["identifier", "status", "granted_by"],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("invitation", Display {
        title: None,
        subtitle: Some("invitationType"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("launch", Display {
        title: None,
        subtitle: Some("rocketId"),
        image: None,
        highlights: &["startDate", "rocketId", "launchpadId"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("leg", Display {
        title: None,
        subtitle: Some("flightNumber"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("list", Display {
        title: None,
        subtitle: Some("name"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("loaded_model", Display {
        title: None,
        subtitle: Some("size"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("mcp_session", Display {
        title: None,
        subtitle: Some("client"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("meeting", Display {
        title: None,
        subtitle: Some("location"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("membership", Display {
        title: None,
        subtitle: Some("status"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("message", Display {
        title: None,
        subtitle: Some("from"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("model", Display {
        title: None,
        subtitle: Some("name"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("note", Display {
        title: None,
        subtitle: Some("noteType"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("offer", Display {
        title: None,
        subtitle: Some("price"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("order", Display {
        title: None,
        subtitle: Some("total"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("organization", Display {
        title: None,
        subtitle: Some("industry"),
        image: Some("image"),
        highlights: &["headquarters"],
        body: None,
        preview: &[],
        also: &["actor"],
    }),
    ("pass", Display {
        title: None,
        subtitle: Some("status"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("payment_method", Display {
        title: None,
        subtitle: Some("displayName"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("person", Display {
        title: None,
        subtitle: Some("about"),
        image: Some("image"),
        highlights: &["birthdate", "gender"],
        body: Some("notes"),
        preview: &[],
        also: &["actor"],
    }),
    ("place", Display {
        title: None,
        subtitle: Some("featureType"),
        image: Some("image"),
        highlights: &["city", "country", "rating"],
        body: Some("fullAddress"),
        preview: &[],
        also: &[],
    }),
    ("playlist", Display {
        title: None,
        subtitle: Some("text"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &["list"],
    }),
    ("podcast", Display {
        title: None,
        subtitle: Some("host"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("post", Display {
        title: None,
        subtitle: Some("author"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("practice", Display {
        title: None,
        subtitle: Some("parent"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("product", Display {
        title: None,
        subtitle: Some("brand"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("project", Display {
        title: None,
        subtitle: Some("state"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("protocol", Display {
        title: None,
        subtitle: Some("name"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("qualification", Display {
        title: None,
        subtitle: Some("category"),
        image: None,
        highlights: &["identifier", "validIn", "granted_by"],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("quantity-kind", Display {
        title: None,
        subtitle: Some("label"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("quote", Display {
        title: None,
        subtitle: Some("year"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("repository", Display {
        title: None,
        subtitle: Some("language"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("reservation", Display {
        title: None,
        subtitle: Some("reservationType"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("result", Display {
        title: None,
        subtitle: Some("url"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("review", Display {
        title: None,
        subtitle: Some("author"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &["post"],
    }),
    ("role", Display {
        title: None,
        subtitle: Some("name"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("seatmap", Display {
        title: Some("flightNumber"),
        subtitle: None,
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("shelf", Display {
        title: None,
        subtitle: Some("isExclusive"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &["list"],
    }),
    ("skill", Display {
        title: None,
        subtitle: Some("description"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("software", Display {
        title: None,
        subtitle: Some("applicationCategory"),
        image: None,
        highlights: &["version", "runtimePlatform"],
        body: None,
        preview: &[],
        also: &["product"],
    }),
    ("sound", Display {
        title: None,
        subtitle: Some("purpose"),
        image: Some("image"),
        highlights: &["datePublished", "published_by"],
        body: Some("description"),
        preview: &[],
        also: &["creative_work", "file"],
    }),
    ("source", Display {
        title: None,
        subtitle: Some("sourceId"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("spec", Display {
        title: None,
        subtitle: Some("state"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["task", "event", "file"],
    }),
    ("tag", Display {
        title: Some("name"),
        subtitle: Some("tagType"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("task", Display {
        title: None,
        subtitle: Some("state"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("tax_line", Display {
        title: None,
        subtitle: Some("description"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("theme", Display {
        title: None,
        subtitle: Some("family"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("tool_call", Display {
        title: None,
        subtitle: Some("name"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("transaction", Display {
        title: None,
        subtitle: Some("category"),
        image: None,
        highlights: &["amount", "postingDate", "currency"],
        body: Some("notes"),
        preview: &[],
        also: &["event"],
    }),
    ("transcript", Display {
        title: None,
        subtitle: Some("language"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("transition", Display {
        title: None,
        subtitle: Some("startDate"),
        image: None,
        highlights: &["startDate", "givenName", "familyName", "gender"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("trip", Display {
        title: None,
        subtitle: Some("tripType"),
        image: None,
        highlights: &["startDate", "endDate", "location"],
        body: None,
        preview: &[],
        also: &["event"],
    }),
    ("unit", Display {
        title: None,
        subtitle: Some("symbol"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("user", Display {
        title: None,
        subtitle: Some("name"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &["actor"],
    }),
    ("video", Display {
        title: None,
        subtitle: Some("author"),
        image: Some("image"),
        highlights: &["datePublished", "published_by"],
        body: Some("description"),
        preview: &[],
        also: &["creative_work", "file"],
    }),
    ("volume", Display {
        title: None,
        subtitle: Some("kind"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("webpage", Display {
        title: None,
        subtitle: Some("url"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
    ("website", Display {
        title: None,
        subtitle: Some("url"),
        image: None,
        highlights: &[],
        body: None,
        preview: &[],
        also: &[],
    }),
];

// ===========================================================
// Field order — YAML declaration order per shape
// ===========================================================

pub fn lookup_field_order(shape: &str) -> &'static [&'static str] {
    SHAPE_FIELD_ORDER.iter().find(|(name, _)| *name == shape).map(|(_, o)| *o).unwrap_or(&[])
}

pub static SHAPE_FIELD_ORDER: &[(&'static str, &'static [&'static str])] = &[
    ("account", &["identifier", "handle", "displayName", "display", "email", "phone", "bio", "accountType", "color", "isActive", "joinedDate", "lastActive", "lastProfileFetch", "userId", "issuer", "metadata"]),
    ("activity", &["action", "changedKeys", "toolName", "duration", "success", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("actor", &["actorType"]),
    ("aircraft", &["model", "variant", "seatCapacity", "rangeKm", "iataCode", "icaoCode", "category", "price", "priceAmount", "originalPrice", "originalPriceAmount", "currency", "categories", "availability", "images", "quantity", "weight", "weightValue", "weightUnit", "soldByWeight", "department", "aisle", "sku", "barcode", "nutritionScore", "novaGroup", "calories", "servingSize", "customizationGroups"]),
    ("airline", &["iataCode", "icaoCode", "callsign", "country", "alliance", "industry", "actorType"]),
    ("airport", &["iataCode", "icaoCode", "city", "country", "countryCode", "timezone", "elevationFt", "terminalCount"]),
    ("app", &["id", "name", "iconRole", "route", "defaultView", "isSystem", "handles"]),
    ("birth", &["givenName", "additionalName", "familyName", "honorificPrefix", "honorificSuffix", "legalName", "maidenName", "sortAs", "nameOrder", "phoneticGivenName", "phoneticFamilyName", "gender", "nickname", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("book", &["isbn", "isbn13", "pages", "genres", "series", "format", "language", "originalTitle", "places", "characters", "awardsWon", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "coverage", "tags", "category", "price", "priceAmount", "originalPrice", "originalPriceAmount", "currency", "categories", "availability", "images", "quantity", "weight", "weightValue", "weightUnit", "soldByWeight", "department", "aisle", "sku", "barcode", "nutritionScore", "novaGroup", "calories", "servingSize", "customizationGroups"]),
    ("booking_offer", &["cartId", "referenceNumber", "status", "preparedAt", "presentedAt", "approvedAt", "expiresAt", "currency", "baseAmount", "taxAmount", "feesAmount", "totalAmount", "itineraryHash", "signature", "signatureAlg", "signedBy", "checkoutUrl", "confirmEndpoint", "isRefundable", "isChangeable", "hasVoidWindow", "voidWindowEndsAt", "conditions", "blob", "review", "contactEmail", "contactPhone", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("bookmark", &["name"]),
    ("branch", &["commit", "upstream", "ahead", "behind", "isCurrent", "isRemote"]),
    ("brand", &["tagline", "country", "primaryColor", "textColor"]),
    ("calendar", &["calendarId", "color", "backgroundColor", "foregroundColor", "isPrimary", "isReadonly", "accessRole", "source", "timezone"]),
    ("channel", &["banner", "subscriberCount"]),
    ("class", &["activityType", "capacity", "spotsRemaining", "isFull", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("community", &["privacy", "memberCount", "subscriberCount", "allowCrypto"]),
    ("conversation", &["isGroup", "isArchived", "unreadCount", "messageCount", "accountEmail", "historyId", "source", "cwd", "gitBranch"]),
    ("conversion", &["kind", "factor", "rate", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("creative_work", &["name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "language", "coverage", "tags"]),
    ("credential", &["domain", "identifier", "itemType", "source", "obtainedAt", "lastVerified", "refreshable", "storeRowId"]),
    ("dimension", &["key", "label", "length", "mass", "time", "current", "temperature", "amount", "luminous", "dimensionless"]),
    ("dns_record", &["domain", "recordName", "recordType", "type", "ttl", "priority", "recordId", "values"]),
    ("document", &["contentType", "language", "wordCount", "abstract", "tableOfContents", "filename", "mimeType", "size", "path", "format", "encoding", "lineCount", "kind", "sha"]),
    ("domain", &["status", "registrar", "autoRenew", "nameservers"]),
    ("email", &["subject", "messageId", "inReplyTo", "isUnread", "isStarred", "isDraft", "isSent", "isTrash", "isSpam", "hasAttachments", "draftId", "conversationId", "accountEmail", "sizeEstimate", "references", "replyTo", "deliveredTo", "attachments", "toRaw", "ccRaw", "bccRaw", "unsubscribe", "unsubscribeOneClick", "manageSubscription", "listId", "isAutomated", "precedence", "mailer", "returnPath", "authResults", "bodyHtml", "isOutgoing"]),
    ("episode", &["durationMs", "episodeNumber", "seasonNumber"]),
    ("event", &["startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("fare", &["identifier", "bookingCode", "productType", "fareFamily", "class", "basePrice", "currency", "passengerType", "milesEarned", "pointsEarned", "components", "refundable", "changeable", "restrictions", "conditions"]),
    ("file", &["filename", "mimeType", "size", "path", "format", "encoding", "lineCount", "kind", "sha"]),
    ("financial_account", &["identifier", "accountId", "accountNumber", "routingNumber", "last4", "currency", "accountType", "balance", "available", "creditLimit", "minimumPayment", "cardType", "interestRate"]),
    ("flight", &["flightNumber", "durationMinutes", "cabinClass", "stops", "carbonEmissions", "sequence", "departureTime", "arrivalTime", "duration", "vehicleType", "layoverMinutes", "trace", "tracePointCount", "polyline", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("font", &["family", "genericFamily", "postscriptName", "weights", "styles", "formats", "scripts", "glyphCount", "designerUrl", "vendorUrl", "licenseInfoUrl", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "language", "coverage", "tags"]),
    ("git_commit", &["sha", "shortHash", "message", "additions", "deletions", "filesChanged", "committedAt", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("group", &["memberCount", "category"]),
    ("health-biomarker", &["measure", "category", "loincCode", "analyteType", "description"]),
    ("health-condition", &["clinicalStatus", "verificationStatus", "proximity", "bodySite", "severity", "snomedCode", "icd10Code", "clinicalArea", "mitigation", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("health-immunization", &["dateAdministered", "cvxCode", "manufacturer", "lotNumber", "doseNumber", "seriesDoses", "site", "route", "diseaseTarget", "notes", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("health-lab", &["cliaNumber", "npi", "ccn", "labType", "accreditation", "industry", "actorType"]),
    ("health-observation", &["value", "valueText", "refLow", "refHigh", "refText", "flag", "status", "notes", "indexedAt", "resultType", "externalUrl", "postId", "score", "similarity", "community", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("health-panel", &["panelCode", "fasting", "description", "id", "listId", "listType", "ordering_mode", "member_shape", "privacy", "isDefault", "isPublic", "itemCount", "default_view", "icon_size", "sort_by", "path", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("health-procedure", &["performedDate", "procedureType", "bodySite", "outcome", "status", "cptCode", "snomedCode", "findings", "followUp", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("health-reference-range", &["low", "high", "unit", "refText", "category", "provenance", "method", "ageLow", "ageHigh", "sex", "pregnancy", "gestationalAge", "fasting", "timeOfDay", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("icon", &["dimension", "format", "url", "component", "purpose", "style", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "language", "coverage", "tags"]),
    ("image", &["width", "height", "format", "altText", "appName", "windowId", "displayId", "displayIndex", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "language", "coverage", "tags", "filename", "mimeType", "size", "path", "encoding", "lineCount", "kind", "sha"]),
    ("intellectual_property", &["category", "mark", "identifier", "register", "status", "filingBasis", "niceClass", "validIn", "renewalPeriod", "verificationUrl"]),
    ("invitation", &["invitationType", "email", "role", "status", "token", "acceptedAt", "revokedAt", "message", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("launch", &["flightNumber", "rocketId", "launchpadId", "crewIds", "reusedBoosters", "landingOutcomes", "articleUrl", "webcastUrl", "wikipediaUrl", "patchImage", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("leg", &["sequence", "departureTime", "arrivalTime", "duration", "durationMinutes", "flightNumber", "cabinClass", "vehicleType", "layoverMinutes", "carbonEmissions", "trace", "tracePointCount", "polyline", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("list", &["id", "listId", "listType", "ordering_mode", "member_shape", "privacy", "isDefault", "isPublic", "itemCount", "default_view", "icon_size", "sort_by", "path"]),
    ("loaded_model", &["size", "quantization", "vramUsage", "sizeVram", "digest", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("mcp_session", &["client", "projectId", "gitBranch", "sessionType", "startedAt", "endedAt", "messageCount", "tokenCount"]),
    ("meeting", &["calendarLink", "isVirtual", "meetingUrl", "conferenceProvider", "phoneDialIn", "meetingType", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("membership", &["status", "tier", "autoRenew", "price", "currency", "billingType", "useCount", "guestPassQuantity", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("message", &["isOutgoing", "isStarred", "conversationId"]),
    ("model", &["contextLength", "contextWindow", "maxOutput", "pricingInput", "pricingOutput", "modality", "modelType", "quantization", "quantizationLevel", "size", "parameterSize", "format", "family", "digest"]),
    ("note", &["noteType", "isPinned"]),
    ("offer", &["price", "currency", "offerType", "availability", "bookingToken", "departureToken", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("order", &["orderId", "orderDate", "total", "totalAmount", "originalTotal", "originalTotalAmount", "savings", "currency", "status", "deliveryDate", "eta", "subtotal", "tipAmount", "deliveryFee", "taxes", "summary", "fareBreakdown", "deliveryInstructions", "interactionType", "orderUuid", "body", "head", "messages", "timeline", "itemStates", "latestArrival", "progress", "progressTotal", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("organization", &["industry", "actorType"]),
    ("pass", &["status", "quantity", "purchasedQuantity", "useCount", "isAllDayPass", "price", "currency", "ticketNumber", "nameOnTicket", "seatAssignment", "boardingGroup", "ticketClass", "gate", "terminal", "checkinStatus", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("payment_method", &["identifier", "type", "subtype", "brand", "displayName", "customDescription", "holderName", "last4", "binRange", "expMonth", "expYear", "expirationDate", "currency", "balance", "fingerprint", "isDefault", "isPrimary", "isExpired", "isSelected", "status", "providerTokens", "metadata"]),
    ("person", &["url", "notes", "about", "actorType"]),
    ("place", &["fullAddress", "placeFormatted", "streetNumber", "street", "neighborhood", "locality", "city", "district", "region", "postalCode", "country", "countryCode", "latitude", "longitude", "accuracy", "featureType", "categories", "phone", "website", "hours", "businessStatus", "rating", "reviewCount", "priceLevel", "timezone", "eta", "isOrderable", "closedMessage", "productCount", "mapboxId", "wikidataId", "googlePlaceId"]),
    ("playlist", &["id", "listId", "listType", "ordering_mode", "member_shape", "privacy", "isDefault", "isPublic", "itemCount", "default_view", "icon_size", "sort_by", "path"]),
    ("podcast", &["feedUrl"]),
    ("post", &["externalUrl", "postType", "score", "commentCount", "community"]),
    ("practice", &["description", "code", "codeSystem", "aliases"]),
    ("product", &["category", "price", "priceAmount", "originalPrice", "originalPriceAmount", "currency", "categories", "availability", "images", "quantity", "weight", "weightValue", "weightUnit", "soldByWeight", "department", "aisle", "sku", "barcode", "nutritionScore", "novaGroup", "calories", "servingSize", "customizationGroups"]),
    ("project", &["state", "color", "parentId"]),
    ("protocol", &["name", "homepage", "rfc", "wikidataId"]),
    ("qualification", &["category", "identifier", "status", "renewalPeriod", "level", "validIn", "verificationUrl"]),
    ("quantity-kind", &["key", "label"]),
    ("quote", &["context", "year"]),
    ("repository", &["stars", "forks", "language", "topics", "openIssues", "isArchived", "isPrivate", "defaultBranch", "license", "size"]),
    ("reservation", &["reservationType", "reservationId", "status", "bookingType", "bookingTime", "modifiedTime", "startTime", "endTime", "partySize", "totalAmount", "baseAmount", "taxAmount", "currency", "checkinUrl", "conditions", "voidWindowEndsAt", "availableActions", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("result", &["indexedAt", "resultType", "externalUrl", "postId", "score", "similarity", "community"]),
    ("review", &["rating", "ratingMax", "tags", "isVerified", "externalUrl", "postType", "score", "commentCount", "community"]),
    ("role", &["title", "department", "roleType", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("seatmap", &["flightNumber", "origin", "destination", "fareBasisCode", "classOfService", "aircraftCode", "totalSeats", "availableSeats", "cabins", "tiers", "hasExitRow", "hasFreeSeats", "hasPaidSeats", "basicEconomyLocked"]),
    ("shelf", &["isExclusive", "id", "listId", "listType", "ordering_mode", "member_shape", "privacy", "isDefault", "isPublic", "itemCount", "default_view", "icon_size", "sort_by", "path"]),
    ("skill", &["skillId", "description", "color", "status", "error"]),
    ("software", &["version", "applicationCategory", "runtimePlatform", "codename", "category", "price", "priceAmount", "originalPrice", "originalPriceAmount", "currency", "categories", "availability", "images", "quantity", "weight", "weightValue", "weightUnit", "soldByWeight", "department", "aisle", "sku", "barcode", "nutritionScore", "novaGroup", "calories", "servingSize", "customizationGroups"]),
    ("sound", &["durationMs", "channels", "sampleRate", "bitDepth", "purpose", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "language", "coverage", "tags", "filename", "mimeType", "size", "path", "format", "encoding", "lineCount", "kind", "sha"]),
    ("source", &["sourceId", "address", "scanner", "enabled", "description", "lastSynced"]),
    ("spec", &["problem", "successCriteria", "remoteId", "priority", "state", "labels", "targetDate", "target", "parentId", "projectId", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties", "filename", "mimeType", "size", "path", "format", "encoding", "lineCount", "kind", "sha"]),
    ("tag", &["color", "tagType", "annotated", "hash"]),
    ("task", &["remoteId", "priority", "state", "labels", "targetDate", "target", "parentId", "projectId", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("tax_line", &["code", "description", "amount", "currency", "kind", "nature", "country", "appliesToIndex", "refundable", "merchantImposed", "rate", "taxableAmount", "inclusive"]),
    ("theme", &["themeId", "family", "description", "style", "startMenu", "defaultBackgroundColor"]),
    ("tool_call", &["name", "input", "output", "isError", "durationMs"]),
    ("transaction", &["amount", "currency", "balance", "category", "postingDate", "pending", "recurring", "notes", "type", "details", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("transcript", &["language", "sourceType", "contentRole", "durationMs", "segmentCount", "segments"]),
    ("transition", &["givenName", "additionalName", "familyName", "honorificPrefix", "honorificSuffix", "legalName", "maidenName", "sortAs", "nameOrder", "phoneticGivenName", "phoneticFamilyName", "gender", "nickname", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("trip", &["tripType", "status", "departureTime", "arrivalTime", "duration", "durationMinutes", "distance", "vehicleType", "cabinClass", "fare", "fareAmount", "currency", "rating", "trackingUrl", "isSurge", "isScheduled", "stops", "bookingToken", "carbonEmissions", "isPool", "isReserve", "guest", "marketplace", "vehicle", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"]),
    ("unit", &["ucumCode", "symbol", "label", "kind", "siDigitalFrameworkUri", "unCefactCommonCode", "qudtUnitIri", "wikidataId", "toBaseFactor", "toBaseOffset", "iso4217", "iso4217Numeric", "minorExponent", "logBase"]),
    ("user", &["osUsername", "primaryUser", "actorType"]),
    ("video", &["durationMs", "resolution", "frameRate", "codec", "viewCount", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "language", "coverage", "tags", "filename", "mimeType", "size", "path", "format", "encoding", "lineCount", "kind", "sha"]),
    ("volume", &["kind", "address", "auto_mount"]),
    ("webpage", &["visitCount", "lastVisitUnix", "contentType", "error"]),
    ("website", &["status", "versionId", "anonymous", "claimToken", "claimUrl"]),
];

// ===========================================================
// Ancestors — transitive `also:` closure per shape
// ===========================================================

pub fn lookup_ancestors(shape: &str) -> &'static [&'static str] {
    SHAPE_ANCESTORS.iter().find(|(n, _)| *n == shape).map(|(_, a)| *a).unwrap_or(&[])
}

pub static SHAPE_ANCESTORS: &[(&'static str, &'static [&'static str])] = &[
    ("activity", &["event"]),
    ("aircraft", &["product"]),
    ("airline", &["organization", "actor"]),
    ("birth", &["event"]),
    ("book", &["creative_work", "product"]),
    ("booking_offer", &["event"]),
    ("class", &["event"]),
    ("conversion", &["event"]),
    ("document", &["file"]),
    ("email", &["message"]),
    ("flight", &["leg", "event"]),
    ("font", &["creative_work"]),
    ("git_commit", &["event"]),
    ("health-condition", &["event"]),
    ("health-immunization", &["event"]),
    ("health-lab", &["organization", "actor"]),
    ("health-observation", &["result", "event"]),
    ("health-panel", &["list", "event"]),
    ("health-procedure", &["event"]),
    ("health-reference-range", &["event"]),
    ("icon", &["creative_work"]),
    ("image", &["creative_work", "file"]),
    ("invitation", &["event"]),
    ("launch", &["event"]),
    ("leg", &["event"]),
    ("loaded_model", &["event"]),
    ("meeting", &["event"]),
    ("membership", &["event"]),
    ("offer", &["event"]),
    ("order", &["event"]),
    ("organization", &["actor"]),
    ("pass", &["event"]),
    ("person", &["actor"]),
    ("playlist", &["list"]),
    ("reservation", &["event"]),
    ("review", &["post"]),
    ("role", &["event"]),
    ("shelf", &["list"]),
    ("software", &["product"]),
    ("sound", &["creative_work", "file"]),
    ("spec", &["task", "event", "file"]),
    ("task", &["event"]),
    ("transaction", &["event"]),
    ("transition", &["event"]),
    ("trip", &["event"]),
    ("user", &["actor"]),
    ("video", &["creative_work", "file"]),
];

// ===========================================================
// Event types — shapes whose `also:` chain includes `event`
// ===========================================================

pub static EVENT_TYPES: &[&'static str] = &["activity", "birth", "booking_offer", "class", "conversion", "event", "flight", "git_commit", "health-condition", "health-immunization", "health-observation", "health-panel", "health-procedure", "health-reference-range", "invitation", "launch", "leg", "loaded_model", "meeting", "membership", "offer", "order", "pass", "reservation", "role", "spec", "task", "transaction", "transition", "trip"];

// ===========================================================
// Derived bindings — per-shape `derived:` block as JSON
// ===========================================================

pub static SHAPE_DERIVED_JSON: &str = r#"{"person": {"birthdate": {"find": "born_in", "is": "birth", "get": "startDate"}, "current_residence": {"find": "lived_at", "where_link": {"to": null}, "get": "name"}, "current_role": {"find": "worked_at", "where_link": {"to": null}, "get": "title"}, "givenName": {"latest": [{"find": "born_in", "is": "birth", "get": "givenName"}, {"find": "changed", "is": "transition", "get": "givenName"}]}, "additionalName": {"latest": [{"find": "born_in", "is": "birth", "get": "additionalName"}, {"find": "changed", "is": "transition", "get": "additionalName"}]}, "familyName": {"latest": [{"find": "born_in", "is": "birth", "get": "familyName"}, {"find": "changed", "is": "transition", "get": "familyName"}]}, "honorificPrefix": {"latest": [{"find": "born_in", "is": "birth", "get": "honorificPrefix"}, {"find": "changed", "is": "transition", "get": "honorificPrefix"}]}, "honorificSuffix": {"latest": [{"find": "born_in", "is": "birth", "get": "honorificSuffix"}, {"find": "changed", "is": "transition", "get": "honorificSuffix"}]}, "legalName": {"latest": [{"find": "born_in", "is": "birth", "get": "legalName"}, {"find": "changed", "is": "transition", "get": "legalName"}]}, "maidenName": {"latest": [{"find": "born_in", "is": "birth", "get": "maidenName"}, {"find": "changed", "is": "transition", "get": "maidenName"}]}, "sortAs": {"latest": [{"find": "born_in", "is": "birth", "get": "sortAs"}, {"find": "changed", "is": "transition", "get": "sortAs"}]}, "nameOrder": {"latest": [{"find": "born_in", "is": "birth", "get": "nameOrder"}, {"find": "changed", "is": "transition", "get": "nameOrder"}]}, "phoneticGivenName": {"latest": [{"find": "born_in", "is": "birth", "get": "phoneticGivenName"}, {"find": "changed", "is": "transition", "get": "phoneticGivenName"}]}, "phoneticFamilyName": {"latest": [{"find": "born_in", "is": "birth", "get": "phoneticFamilyName"}, {"find": "changed", "is": "transition", "get": "phoneticFamilyName"}]}, "gender": {"latest": [{"find": "born_in", "is": "birth", "get": "gender"}, {"find": "changed", "is": "transition", "get": "gender"}]}, "nickname": {"latest": [{"find": "born_in", "is": "birth", "get": "nickname"}, {"find": "changed", "is": "transition", "get": "nickname"}]}}}"#;

// ===========================================================
// Shortcuts — per-shape `shortcuts:` block as JSON
// ===========================================================

pub static SHAPE_SHORTCUTS_JSON: &str = r#"{"person": {"birthdate": {"writes": "born_in[is=birth].startDate"}, "givenName": {"writes": "born_in[is=birth].givenName"}, "additionalName": {"writes": "born_in[is=birth].additionalName"}, "familyName": {"writes": "born_in[is=birth].familyName"}, "honorificPrefix": {"writes": "born_in[is=birth].honorificPrefix"}, "honorificSuffix": {"writes": "born_in[is=birth].honorificSuffix"}, "legalName": {"writes": "born_in[is=birth].legalName"}, "maidenName": {"writes": "born_in[is=birth].maidenName"}, "sortAs": {"writes": "born_in[is=birth].sortAs"}, "nameOrder": {"writes": "born_in[is=birth].nameOrder"}, "phoneticGivenName": {"writes": "born_in[is=birth].phoneticGivenName"}, "phoneticFamilyName": {"writes": "born_in[is=birth].phoneticFamilyName"}, "gender": {"writes": "born_in[is=birth].gender"}, "nickname": {"writes": "born_in[is=birth].nickname"}}}"#;
