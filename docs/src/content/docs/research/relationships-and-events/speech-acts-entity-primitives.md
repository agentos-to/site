---
title: Speech Act Theory Maps to Entity Primitives
description: Research into whether linguistic categories of utterances map to knowledge graph primitives.
---

Research into whether linguistic categories of utterances map to knowledge graph primitives. Finding: **Searle's 5 illocutionary act categories map almost perfectly to AgentOS's illocutionary primitives, validating the architecture from a completely independent theoretical framework.**

---

## 1. Sentence Types in Grammar (4 Types)

English grammar classifies sentences by their function:

| Type | Function | Punctuation | Example |
|------|----------|-------------|---------|
| **Declarative** | Makes a statement / claims truth | Period | "The meeting is at 3pm." |
| **Interrogative** | Asks a question / seeks information | Question mark | "When is the meeting?" |
| **Imperative** | Gives a command / requests action | Period or exclamation | "Schedule the meeting." |
| **Exclamatory** | Expresses strong feeling | Exclamation mark | "What a great meeting!" |

These are surface-level categories. Speech act theory goes deeper.

---

## 2. Speech Act Theory (Austin & Searle)

### Austin's Three Levels

J.L. Austin (1962, *How to Do Things with Words*) discovered that every utterance operates at three simultaneous levels:

| Level | What it is | Example: "I'll be there at 3pm" |
|-------|-----------|--------------------------------|
| **Locutionary** | The literal content (what you *say*) | The words and their meaning |
| **Illocutionary** | The act performed (what you're *doing*) | Making a promise / commitment |
| **Perlocutionary** | The effect achieved (what *happens*) | The listener now expects you |

The **illocutionary** level is the key one — it classifies what the utterance DOES in the world, not just what it says.

### Searle's 5 Categories of Illocutionary Acts

John Searle (1976) classified all possible illocutionary acts into 5 exhaustive categories based on their "direction of fit" between words and the world:

| Category | Direction of Fit | What it does | Definition |
|----------|-----------------|-------------|------------|
| **Assertive** | Word → World | Claims something is true | Speaker asserts a proposition about how the world IS. The words must match reality. |
| **Directive** | World → Word | Requests/demands action or information | Speaker tries to get the hearer to do something. Reality must change to match the words. |
| **Commissive** | World → Word | Commits to a future action | Speaker commits themselves to a course of action. Reality must change (the speaker will act). |
| **Declarative** | Both directions | Creates reality by utterance | The act of saying it MAKES it so. "I now pronounce you married." "You're fired." |
| **Expressive** | Neither | Expresses psychological state | Speaker expresses feelings about a state of affairs. No truth conditions. |

The **direction of fit** is the deep insight:
- **Assertives**: words must match reality (descriptive)
- **Directives & Commissives**: reality must match words (prescriptive)
- **Declarations**: saying it makes it so (performative — both directions at once)
- **Expressives**: neither — feelings just ARE

---

## 3. The Mapping to AgentOS Primitives

The mapping between Searle's categories and AgentOS's entity primitives is remarkably clean:

| Searle Category | Direction of Fit | AgentOS Primitive | How it maps |
|----------------|-----------------|-------------------|-------------|
| **Assertive** | Word → World | **story** | Claims about reality: "This happened," "This is true" |
| **Directive** (action) | World → Word | **outcome** (task) | Demands reality change: "Do this," "Make this happen" |
| **Directive** (info-seeking) | World → Word | **question** | Demands information: "What is X?", "When did Y?" |
| **Commissive** | World → Word | **outcome** | Commits to future state: "I will do X," "We aim for Y" |
| **Declarative** | Both | **right** | Creates reality by utterance: "You're fired," "This license grants..." |
| **Expressive** | Neither | ??? | Feelings and reactions — possibly annotations, not first-class entities |

### Key Insight: Two Orthogonal Axes

The existing ontological primitives (work, actor, event, list) and the illocutionary primitives (story, outcome, question, right) form two orthogonal axes:

| Axis | What it captures | Primitives | Nature |
|------|-----------------|-----------|--------|
| **Ontological** | The nouns — things that EXIST | work, actor, event, list | What IS in the world |
| **Illocutionary** | The verbs — what people DO | story, outcome, question, right | What people DO about the world |

This gives a principled answer to "why these primitives and not others?" — because they span both axes of human knowledge: **what exists** and **what we do about it.**

### The Expressive Gap

Searle's 5th category (expressives) doesn't clearly map to an entity primitive. Expressives include:
- "Thank you" (gratitude)
- "I'm sorry" (apology)
- "Congratulations" (celebration)
- Emoji reactions, likes, upvotes

These might be best modeled as **annotations on other entities** (reactions to posts, acknowledgments of events) rather than first-class primitives. A "like" is an expressive act ON a work, not an independent entity.

---

## 4. Validation from Linguistics

The fact that a knowledge graph architecture independently arrived at categories that map to a 70-year-old linguistic framework is strong validation:

1. **Story = Assertive**: Both are about claiming truth. A story asserts "this happened." An assertive speech act claims "this is the case."

2. **Outcome/Task = Directive + Commissive**: Both are about changing reality. A task directs "do this." A goal commits "we will achieve this." Both have the same direction of fit — reality must change to match the words.

3. **Question = Directive (info-seeking)**: Searle classified questions as a subtype of directives — they direct the hearer to provide information. This validates question as its own primitive (a directive that seeks information rather than action).

4. **Right = Declarative**: Both create reality by utterance. A license declares "you may do X." A marriage certificate declares "you are married." The act of declaring IS the creation.

5. **Work, Actor, Event, List**: These have NO counterpart in speech act theory — correctly so. They describe what EXISTS (ontology), not what people DO (illocution). The two axes are genuinely orthogonal.

---

## 5. The Direction of Fit as a Design Principle

The "direction of fit" gives a clean test for classifying new entity types:

| Direction | Test | If yes, it's... |
|-----------|------|-----------------|
| Word → World | "Does this claim something about reality?" | Story / assertive |
| World → Word | "Does this demand reality change?" | Outcome / directive+commissive |
| Both | "Does saying this make it so?" | Right / declarative |
| Neither | "Does this express a feeling?" | Annotation / expressive |
| N/A | "Does this just exist?" | Ontological primitive |

---

## Significance for Entity Architecture

This research led to the "5+5" (later 5+4, then evolved further) primitive architecture:

**Ontological primitives** (what EXISTS):
- work — things people create
- actor — things that can do things  
- event — things that happen at a time
- list — organizational grouping
- record — structured data entries

**Illocutionary primitives** (what people DO):
- story — claims about reality (assertive)
- outcome — desired states of the world (directive + commissive)
- question — frames seeking resolution (directive, info-seeking)
- right — reality created by declaration (declarative)

The expressives gap was resolved by treating reactions/expressions as relationship data (annotations) rather than entities.
