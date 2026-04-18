---
title: Simplification Passes & Accreted Cruft — Cross-Domain Briefing
description: Seven lenses for reasoning about a codebase refactor by analogy — how rockets, cheese, dead laws, and famous rewrites all describe systems that accrete and rare deliberate passes that cut back.
---

## 1. SpaceX Raptor 1 → 2 → 3: deletion as a design discipline

The Raptor engine is the canonical modern example of simplification-as-engineering. The
progression is aggressive, numeric, and public.

**Raptor 1 (sea level):** 185 tonnes-force thrust, 2,080 kg engine mass, 3,630 kg including
vehicle-side hardware, ~330s Isp. Musk called the early units "the Christmas tree" — one
prototype literally had a snowman painted on it because engineers joked it looked like
holiday decoration. It was festooned with development sensors, exposed plumbing,
flanged joints, and a full engine-shroud heat shield on the booster.

**Raptor 2 (sea level):** 230 tonnes-force thrust (+24%), 1,630 kg mass (-22%), 347s Isp
([SpaceX stats via X](https://x.com/SpaceX/status/1819795288116330594)). Valve plates replaced
individual valves, most development sensors were deleted, plumbing was integrated or removed.
The throat was widened, sacrificing ~1% Isp for a large thrust gain. Raptor 2 "looks borderline
incomplete compared to the original" ([Everyday Astronaut](https://everydayastronaut.com/spacex-raptor-engine-comparison/)).

**Raptor 3 (announced April 2024):** 21% more thrust than R2, 7% lighter, and — the headline
change — **no engine heat shield at all**. Secondary flow paths and regenerative cooling were
pulled *inside* the engine body; the chamber jacket and pumps became the heat shield. Bolted
joints, flange connections, and the booster-side fire-suppression system were eliminated,
saving ~1 tonne per engine ([Metal AM](https://www.metal-am.com/spacex-debuts-raptor-3-engine-further-enhanced-with-metal-additive-manufacturing/)).
Musk: "Raptor 3 is truly sublime engineering. So much so that even experienced veterans of
the space industry thought it was impossible" ([X](https://x.com/elonmusk/status/1858939734271422921)).

**Forcing functions.** The simplification wasn't aesthetic — it was driven by hard physics:
cost per ton to orbit (every kg of engine mass is a kg less payload), rapid reusability
(fewer joints = fewer inspection points), and manufacturability (additive printing can't
easily produce a bolted assembly, so "print as one piece" forces integration). Musk's
5-step algorithm formalizes this: (1) make the requirements less dumb, (2) **delete the
part or process**, (3) simplify/optimize, (4) accelerate cycle time, (5) automate — in that
order. "Possibly the most common error of a smart engineer is to optimize a thing that
should not exist" ([Jeff Winter](https://www.jeffwinterinsights.com/insights/elon-musks-five-step-design-process)).
The mantra "the best part is no part, the best process is no process — it weighs nothing,
costs nothing, can't go wrong" is the compressed form.

---

## 2. Government cheese: a policy that outlived its purpose and spawned its own industry

In 1977, under Carter, the **Food and Agriculture Act of 1977** raised the federal purchase
price for dairy and committed USDA to buy "as much cheese at that price as farmers were
willing to sell" ([NPR Planet Money](https://www.npr.org/2021/05/21/999144678/big-government-cheese-classic)).
Roughly $2B over four years flowed to producers. Farmers did the rational thing and produced
vastly more milk than anyone could drink.

By 1981, the government owned **over 500 million pounds of cheese**, stored in hundreds of
warehouses across 35 states — about two pounds per American citizen, and 1-in-4 pounds of US
cheddar ([HISTORY.com](https://www.history.com/articles/government-cheese-dairy-farmers-reagan)).
Reagan released 30M pounds through the Temporary Emergency Food Assistance Program in
December 1981 — the block-of-orange-cheese TEFAP distribution that coined "government cheese"
as shorthand for commodity welfare.

**The workaround-industry.** Rather than unwind the price supports, Congress created
**Dairy Management Inc. (DMI)** in the 1990s via a "checkoff" tax on dairy producers —
a semi-public USDA marketing arm funded by the very surplus it exists to burn down.
DMI's job is to push cheese *into* American food. Concrete wins:

- **Domino's Smart Slice** (launched Jan 2011, [Domino's IR](https://ir.dominos.com/news-releases/news-release-details/dominos-pizza-launches-dominos-smart-slice-school-lunch-pizza)):
  DMI helped Domino's formulate a reduced-fat mozzarella and placed it in 21,000 schools,
  moving an extra 3M pounds of cheese. DMI paid Domino's $5.8M in 2019 alone
  ([Farm Action](https://farmaction.us/2023/10/26/dairy-farmers-shouldnt-be-forced-to-fund-dominos-marketing/)).
- **Taco Bell Grilled Cheese Burrito**: developed by DMI's on-site food science team and uses
  **11× the cheese of a regular Taco Bell taco** ([Dairy Foods](https://www.dairyfoods.com/articles/96756-dairy-checkoff-program-to-drive-an-additional-millions-of-pounds-of-cheese-use)).
- **Pizza Hut Asia-Pacific**: +136% US cheese volume since the 2016 DMI partnership
  ([Dairy Checkoff](https://www.dairycheckoff.com/news/checkoff-news/checkoffs-pizza-strategy-success-indonesia-japan)).

The US private cheese stockpile hit **~1.4 billion pounds** in 2018 ([Pacific Standard](https://psmag.com/economics/what-will-the-us-government-do-with-1-4-billion-pounds-of-cheese/));
the government-owned portion is smaller today but the structural surplus has never been
resolved. The canonical pattern: a 1977 emergency subsidy became a permanent production
incentive, which spawned a marketing bureaucracy whose entire purpose is consuming the
output of the original workaround. Nobody's job description is "delete the price support."

---

## 3. Antiquated UK laws: why bad rules don't get repealed

Most "weird old law" lists mix real statutes with myths. The real ones are instructive:

- **Dying in Parliament — MYTH.** Derived from a confused belief that dying in a royal
  palace entitles you to a state funeral. The Law Commission's Statute Law Repeals team has
  confirmed no such statute; at least four deaths have occurred in Westminster without
  legal consequence ([Milners](https://www.milnerslaw.co.uk/is-it-illegal-to-die-in-parliament-6-weird-laws-in-england-and-wales/)).
- **Carrying a plank on a London pavement — REAL.** Section 54 of the **Metropolitan Police
  Act 1839** still forbids carrying "any cask, tub, hoop, wheel, ladder, plank, pole" on a
  footway except while loading/unloading. 187 years old. Still technically enforceable.
- **Handling salmon in suspicious circumstances — REAL and modern.** Section 32 of the
  **Salmon Act 1986** ([Wikipedia](https://en.wikipedia.org/wiki/Salmon_Act_1986)) criminalizes
  receiving or handling salmon one could reasonably believe was illegally fished. It's an
  anti-poaching provision with a comedy-ready summary.

**The mechanism by which bad laws don't get repealed.** Per the UK Law Commission
([lawcom.gov.uk](https://lawcom.gov.uk/repeals/)): "There is no special procedure for
passing an Act that repeals legislation: the process is exactly the same as for any other
Act of Parliament." Repeal competes for the same scarce parliamentary floor time as new
legislation — and there's no constituency that *wants* an old irrelevant law repealed.
The Law Commission only proposes repeals that are uncontroversial and clearly spent. As
a result, the UK has passed **21 Statute Law (Repeals) Acts** since 1965, each a bulk
cleanup of hundreds of dead statutes ([Wikipedia](https://en.wikipedia.org/wiki/Statute_Law_(Repeals)_Act))
— the parliamentary equivalent of a dependency-pruning commit. They exist precisely
because normal repeal is uneconomic.

The software analogue is sharp: dead code survives because deleting it is never anyone's
sprint goal and carries downside risk ("what if something depends on it?") without
upside reward.

---

## 4. Desuetude: the system's immune response to accreted rules

**Desuetude** is the doctrine that a statute, by long non-enforcement and notorious public
disregard, becomes effectively void. It's the legal system's pressure-release valve for
laws nobody wants but nobody will repeal. Critically, only **West Virginia** formally
recognizes desuetude as a US legal doctrine ([Wikipedia](https://en.wikipedia.org/wiki/Desuetude)) —
everywhere else, the release valve operates informally, through prosecutorial discretion
and selective non-enforcement.

**Canonical examples:**

- **Blue laws** (Sunday closing laws). Most states still have them on the books; almost none
  enforce them; the Stanford paper by Ira P. Robbins frames them as a case study in
  desuetude's slow erosion ([Stanford Law](https://law.stanford.edu/wp-content/uploads/2022/10/Robbins-10282022-online-version.pdf)).
- **Jaywalking.** Technically illegal in most US cities; enforced almost exclusively as a
  pretext. "If you were arrested for jaywalking, there's a pretty good chance you were
  irritating the officer in some other way he couldn't legally nail you on."
- **Federal cannabis prohibition.** A live example of desuetude *in progress* — a Schedule I
  federal classification coexisting with legal adult-use markets in 24 states, held together
  by annual non-enforcement riders (Rohrabacher-Farr) and DOJ discretion ([NYU Law Review](https://nyulawreview.org/wp-content/uploads/2018/08/NYULawReview-90-1-Markano.pdf)).

**Why "immune response" is the right metaphor.** Desuetude isn't principled — it's a
patch. It lets the system tolerate inconsistency between its formal rules and its actual
behavior. The cost: unpredictability (the rule can snap back any time a prosecutor wants
it to), selective enforcement against disfavored groups, and the rot of public trust that
comes from "everyone knows it's illegal but nobody's actually charged."

Software analogue: the feature flag left permanently in the "off" position, the deprecated
endpoint that's never removed because "something might still hit it," the linter rule that
gets `# noqa`'d at every call site. Each one is a small act of desuetude — the rule exists
but doesn't bind. Over time the gap between declared behavior and actual behavior becomes
a reliability hazard.

---

## 5. Software rewrites: named triggers and what got kept

Six case studies where a team stopped patching and started over. The pattern across all
six: a specific numeric wall (latency, build time, incident rate) made incremental cleanup
economically impossible.

**Twitter: Ruby on Rails → Scala/JVM (2008–2012).** Trigger: the **Fail Whale**. By 2010
tweet-rate had climbed into hundreds of millions/day and Ruby's long-running-process and
memory characteristics couldn't keep up. Twitter rewrote the message queue and tweet storage
engine in Scala, kept the Rails front-end initially but moved rendering to browser JS.
Payoff: the 2012 US election saw **327,452 tweets/minute** with no Fail Whale ([VentureBeat](http://venturebeat.com/2012/11/07/twitter-election-dev-post-mortem/)).
Kept: the product semantics and most user-facing code paths. Threw away: the Ruby backend
entirely.

**Shopify: Rails monolith → modular monolith (2016+).** Trigger: 2.8M lines of Ruby, 500k
commits, and "changing one piece of code would cause unintended side effects on seemingly
unrelated code" ([Shopify Engineering](https://shopify.engineering/shopify-monolith)).
They explicitly cited Martin Fowler's **design stamina hypothesis** as the decision
moment: once feature delivery slows to a crawl, pay down the architecture. They rejected
microservices and built the **Packwerk** tool for enforcing module boundaries inside Rails.
Kept: one deploy unit. Threw away: technical-axis organization (re-sliced by business
domain: billing, orders, checkout).

**Facebook: PHP → HHVM → Hack (2008+).** The *anti-rewrite*. Facebook explicitly rejected
the instinctive "let's rewrite in Java" response and instead rewrote the **layer below** —
transpiler, then JIT, then a gradually-typed PHP dialect (Hack). Marton Trencseni frames
this as "avoiding the Second-system effect" ([Bytepawn](https://bytepawn.com/hack-hhvm-second-system-effect.html)).
Kept: every line of existing PHP. Threw away: the Zend runtime and PHP's type-weakness.
The lesson: sometimes the cut isn't at the application layer.

**Stripe: Ruby → Sorbet-typed Ruby (2017+).** Trigger: ~3/4 of Stripe engineers working
in one large Ruby codebase, and the realization that growth in that codebase was
"one of the most critical tasks to maintaining product velocity" ([lethain.com](https://lethain.com/stripe-sorbet/)).
Built in 8 months, rolled out over 7 more. Kept: Ruby itself and all runtime behavior.
Threw away: untyped code as the default (files now default to `typed: strict`). A gradual
migration that worked *because* it was gradual.

**Discord: Go → Rust for Read States (2020).** Trigger: Go's garbage collector triggering
every 2 minutes regardless of actual garbage, walking the entire live heap, causing latency
spikes on a service hit on every connect/message/read ([Discord blog](https://discord.com/blog/why-discord-is-switching-from-go-to-rust)).
Kept: the service boundary and API. Threw away: GC as a memory-management strategy.
Response times dropped from milliseconds to microseconds. Quote worth noting: "even with
basic optimization, Rust outperformed a highly-tuned Go service."

**Figma: not Electron — C++/WASM from day one.** Evan Wallace's counter-example: Figma
never "ditched Electron" because it was never an Electron app at its core. The canvas and
document representation are **C++ compiled to WebAssembly**; only the chrome around the
canvas is TypeScript ([madebyevan.com](https://madebyevan.com/figma/), [Figma blog](https://www.figma.com/blog/webassembly-cut-figmas-load-time-by-3x/)).
WASM cut load time 3×, parsing is ~20× faster than asm.js. The decision moment was
architectural, not a rewrite — but the principle is the same: the domain (60fps canvas
rendering of complex vector graphics) was incompatible with the default platform, so
they went down a layer.

**The common shape.** Every one of these has a measurable trigger (latency, LOC, GC pause,
build time), keeps the product-facing contract stable, and cuts at a specific architectural
seam. None was a "let's rewrite everything" — each was a surgical excision.

---

## 6. Chesterton's Fence vs Lindy: when to cut, when to preserve

**Chesterton's Fence** (G.K. Chesterton, *The Thing*, 1929): "Don't ever take a fence down
until you know the reason it was put up." **Lindy effect** (Mandelbrot/Taleb): the expected
remaining life of a non-perishable thing is proportional to its current age. Both argue
for *preservation*.

Both can fail the same way: the fence may still be standing because nobody has had the
courage, the authority, or the budgeted parliamentary time to tear it down. Lindy describes
survival, not correctness. "Old" and "load-bearing" are not synonyms.

**How the greats reconcile this:**

- **Rich Hickey, "Simple Made Easy"**: the key distinction is *simple* (un-complected,
  literally un-braided) vs *easy* (close to hand, familiar). Most legacy code is "easy" to
  the people who wrote it and "complex" to everyone else. Hickey's complect/compose
  distinction cuts through Chesterton: you don't need to know why the braid was woven to
  see that untwisting it is valuable ([talk transcript](https://github.com/matthiasn/talk-transcripts/blob/master/Hickey_Rich/SimpleMadeEasy.md)).
  Hickey: "Having state in your program is never simple … it complects value and time."
- **Niklaus Wirth, "A Plea for Lean Software" (1995)**: software's girth outpaces its
  functionality because hardware makes it possible. His Project Oberon OS was 200KB
  including editor and compiler. Core principle: "a system that is not understood in its
  entirety by a single individual should probably not be built" ([PDF](https://cr.yp.to/bib/1995/wirth.pdf)).
  Wirth's answer to Chesterton: if *no one* understands why the fence is there, that's the
  fence's problem, not yours.
- **John Carmack**: "all the various code quality metrics correlated at least as strongly
  with code size as error rate — code size alone gives essentially the same error-predicting
  ability" ([sevangelatos.com](http://www.sevangelatos.com/john-carmack-on-static-code-analysis/)).
  Carmack's practical resolution: inline short one-use code to make control flow explicit;
  split thousand-line functions to make them followable. Optimize for "the limits of the
  human mind (his own in low-effort mode)." The fence stays if a tired engineer at 2am can
  still see why; it goes if it's only defensible after 30 minutes of archaeology.
- **Fred Brooks, "No Silver Bullet"**: essential vs accidental complexity. Chesterton's
  fence may guard essential complexity (keep it) or accidental (cut it). The engineer's
  job is distinguishing which.

**The working synthesis.** Chesterton is a *burden of proof* rule, not a preservation rule.
You must *understand* before you cut — but once you understand, cutting is often the right
move. The junior engineer deletes without understanding; the senior engineer understands
then deletes; the bad senior engineer understands and refuses to delete out of misplaced
respect for the past.

---

## 7. Effective vs efficient: productive adversarial tension

The pattern: pair every system with a counter-system whose job is to keep it honest.
Payments acceptance vs fraud. Sales vs compliance. Dev velocity vs reliability. Each pair
would, alone, optimize itself into a failure mode (100% acceptance = fraud-bled bankruptcy;
100% compliance = no revenue). The pairing forces a productive equilibrium.

**Google SRE error budgets** are the sharpest codification. Per the SRE book
([sre.google/sre-book/embracing-risk](https://sre.google/sre-book/embracing-risk/)):

> "Product development performance is largely evaluated on product velocity, while SRE
> performance is evaluated based upon reliability of a service, which implies an incentive
> to push back against a high rate of change."

The error budget converts this from a political argument into a number. If your SLO is
99.9%, you have 0.1% *budget* to burn on risky launches. When the budget is full, push
hard. When it's near zero, the **dev team self-polices** — they don't want to blow the
budget and stall their own launches. "SRE isn't in the game of second-guessing what the
dev team is doing. So there's no need for an adversarial relationship or information
hiding." The tension becomes a shared denominator.

**Team Topologies** (Skelton & Pais, 2019) generalizes this. Stream-aligned teams ship
features end-to-end; enabling teams are specialists who *guide* stream-aligned teams without
owning their work; platform teams provide self-service substrate; complicated-subsystem
teams own gnarly specialist domains. The key move: **define team interfaces explicitly**,
because "not all communication and collaboration is good" ([Jacob Kaplan-Moss review](https://jacobian.org/2021/jul/5/book-review-team-topologies/)).
The explicit interface is what converts potential adversarial friction into a bounded,
contract-based negotiation.

**Conway's Law** is the reason this matters: "organizations produce systems that mirror
their communication structure" ([Martin Fowler](https://martinfowler.com/bliki/ConwaysLaw.html)).
If the sales/compliance tension is *inside one team*, you get mushy half-compliant
half-selling code. If it's *across two teams with a contract*, you get two clean systems
that negotiate at a defined seam. Tension at the seam, not inside the module.

**Why this is productive, not deadlock.** Three ingredients:
1. **A shared denominator** (error budget, fraud rate, customer complaints) — both sides
   care about the *same* number.
2. **Information symmetry** — both sides see the same dashboards.
3. **A defined interface** — not "please be more careful," but "here's the SLO, here's what
   happens when we blow it."

Without those, adversarial tension becomes political. With them, it's a control loop.

The architectural takeaway for a refactor: if your codebase has no counter-pressure against
accretion, accretion wins by default. Every "delete the part" needs an institutional
sponsor whose job is specifically to argue for deletion — a Raptor-3 team inside the
organization, with its own budget and its own shared denominator (lines of code deleted,
build time reduced, part count removed). Without it, the Christmas tree always wins.

---

## Sources

- [Raptor Engine — Starship Wiki](https://starship-spacex.fandom.com/wiki/Raptor_Engine)
- [Raptor 1 vs 2 — Everyday Astronaut](https://everydayastronaut.com/spacex-raptor-engine-comparison/)
- [SpaceX debuts Raptor 3 — Metal AM](https://www.metal-am.com/spacex-debuts-raptor-3-engine-further-enhanced-with-metal-additive-manufacturing/)
- [SpaceX Raptor 3 performance stats — X](https://x.com/SpaceX/status/1819795288116330594)
- [Musk on Raptor 3 — X](https://x.com/elonmusk/status/1858939734271422921)
- [Musk's 5-step process — Jeff Winter](https://www.jeffwinterinsights.com/insights/elon-musks-five-step-design-process)
- [Government Cheese — NPR Planet Money](https://www.npr.org/2021/05/21/999144678/big-government-cheese-classic)
- [How the US Ended Up With Warehouses of Cheese — HISTORY](https://www.history.com/articles/government-cheese-dairy-farmers-reagan)
- [1.4B pounds of cheese — Pacific Standard](https://psmag.com/economics/what-will-the-us-government-do-with-1-4-billion-pounds-of-cheese/)
- [Domino's Smart Slice launch — Domino's IR](https://ir.dominos.com/news-releases/news-release-details/dominos-pizza-launches-dominos-smart-slice-school-lunch-pizza)
- [Dairy Farmers Shouldn't Fund Domino's — Farm Action](https://farmaction.us/2023/10/26/dairy-farmers-shouldnt-be-forced-to-fund-dominos-marketing/)
- [DMI drives 12M+ pounds — Dairy Foods](https://www.dairyfoods.com/articles/96756-dairy-checkoff-program-to-drive-an-additional-millions-of-pounds-of-cheese-use)
- [Salmon Act 1986 — Wikipedia](https://en.wikipedia.org/wiki/Salmon_Act_1986)
- [Is it illegal to die in Parliament — Milners](https://www.milnerslaw.co.uk/is-it-illegal-to-die-in-parliament-6-weird-laws-in-england-and-wales/)
- [UK Law Commission Repeals](https://lawcom.gov.uk/repeals/)
- [Statute Law (Repeals) Act — Wikipedia](https://en.wikipedia.org/wiki/Statute_Law_(Repeals)_Act)
- [Desuetude — Wikipedia](https://en.wikipedia.org/wiki/Desuetude)
- [Obsolescence of Blue Laws — Stanford Law](https://law.stanford.edu/wp-content/uploads/2022/10/Robbins-10282022-online-version.pdf)
- [Cannabis & Federal-State Policy Gap — NYU Law Review](https://nyulawreview.org/wp-content/uploads/2018/08/NYULawReview-90-1-Markano.pdf)
- [Why Discord is switching from Go to Rust](https://discord.com/blog/why-discord-is-switching-from-go-to-rust)
- [Twitter fail whale killed by Scala migration — VentureBeat](http://venturebeat.com/2012/11/07/twitter-election-dev-post-mortem/)
- [Twitter's shift from Ruby to Java — InfoQ](https://www.infoq.com/news/2012/11/twitter-ruby-to-java/)
- [Under Deconstruction: Shopify's Monolith](https://shopify.engineering/shopify-monolith)
- [Deconstructing the Monolith — Shopify](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity)
- [Hack, HHVM and the Second-system effect — Bytepawn](https://bytepawn.com/hack-hhvm-second-system-effect.html)
- [Why did Stripe build Sorbet — lethain.com](https://lethain.com/stripe-sorbet/)
- [Gradual typing of Ruby at scale — Sorbet docs](https://sorbet.org/docs/talks/strange-loop-2018)
- [Figma — Made by Evan](https://madebyevan.com/figma/)
- [WebAssembly cut Figma's load time — Figma Blog](https://www.figma.com/blog/webassembly-cut-figmas-load-time-by-3x/)
- [Simple Made Easy transcript — Rich Hickey](https://github.com/matthiasn/talk-transcripts/blob/master/Hickey_Rich/SimpleMadeEasy.md)
- [A Plea for Lean Software — Niklaus Wirth, 1995](https://cr.yp.to/bib/1995/wirth.pdf)
- [Carmack on static code analysis](http://www.sevangelatos.com/john-carmack-on-static-code-analysis/)
- [Chesterton's Fence — Mind Collection](https://themindcollection.com/chestertons-fence/)
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/)
- [Team Topologies review — Jacob Kaplan-Moss](https://jacobian.org/2021/jul/5/book-review-team-topologies/)
- [Conway's Law — Martin Fowler](https://martinfowler.com/bliki/ConwaysLaw.html)
