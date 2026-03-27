---
title: "Introduction to Domain Storytelling"
subtitle: "Turn domain knowledge into shared understanding, better software decisions, and living documentation."
requested_url: "https://emmanuelvalverderamos.substack.com/p/introduction-to-domain-storytelling"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/introduction-to-domain-storytelling"
substack_post_id: 184103934
retrieved_at: "2026-03-27T08:57:49.870Z"
---
# Introduction to Domain Storytelling

### Turn domain knowledge into shared understanding, better software decisions, and living documentation.

## What is domain sotorytelling?

[![](https://substackcdn.com/image/fetch/$s_!8weJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb87dda09-5fa6-4000-ad6b-fc1b0691bdcc_1257x688.png)](https://substackcdn.com/image/fetch/$s_!8weJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb87dda09-5fa6-4000-ad6b-fc1b0691bdcc_1257x688.png)

Domain Storytelling is a collaborative modeling technique that captures **how work actually happens in a business** by telling and visualizing **concrete stories** (scenarios). Instead of starting with abstract process diagrams or technical assumptions, you start with something humans are naturally good at: **narrating what people do, in what order, with which things, and why**.

A Domain Story is a **pictographic story**: actors (people, teams, or systems) perform activities (verbs) with work objects (things they handle), in a sequence that represents time. It is simple on purpose. That simplicity is not a limitation, it is the point.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

If EventStorming helps you discover the domain through a timeline of domain events, and Event Modeling helps you blueprint UI-to-event behavior, Domain Storytelling helps you first answer a more fundamental question:

> What is the real business flow, as people live it?

## What Domain Storytelling is and what it is not?

### What it is

Domain Storytelling is **scenario-based modeling** of business processes. You document typical examples of work, using a lightweight visual language that domain experts can immediately validate.

It is excellent for:

- Understanding a domain fast
- Building a shared language between business and engineering
- Surfacing assumptions, gaps, and “we do it differently depending on…” moments
- Producing simple documentation that stays readable months later

### What it is not

It is not:

- A complete “all-possible-paths” process specification
- A technical sequence diagram of HTTP calls and database writes
- BPMN with gateways and exhaustive branching

Instead, Domain Storytelling prefers:

- **One concrete story at a time**
- **One diagram per meaningful scenario**
- **Alternatives modeled as separate stories**, not mixed into a single flow

This choice protects clarity. You keep the model readable for business people, and you prevent early “design-by-abstraction” mistakes.

## The visual language: building blocks 🧩

A Domain Story is composed of a few primitives that map to natural language.

[![](https://substackcdn.com/image/fetch/$s_!IIXO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F881957a1-19a4-41e9-b27f-749cf21c39ae_1162x1204.png)](https://substackcdn.com/image/fetch/$s_!IIXO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F881957a1-19a4-41e9-b27f-749cf21c39ae_1162x1204.png)

### 👤 Actors (who)

An actor is a person, a group, or a software system that plays an active role in the story.

Good actor names are roles, not individuals:

- “Cashier”, not “Matthew”
- “Moviegoer”, not “Ana”
- “Booking System”, not “Service A”

### 📄 Work Objects (what)

Work objects are things actors work with or exchange:

- Tickets, prices, seating plans, orders, invoices, emails
- Physical items or information items

Work objects are labeled using the domain language. They often become **valuable vocabulary anchors** for later modeling (and even code).

### ➡️ Activities (what someone does)

Activities are verbs that connect actors to work objects (and sometimes other actors). They describe action in business terms:

- “suggests”, “marks”, “pays”, “hands over”

A strong rule-of-thumb:

- Actors and work objects are nouns
- Activities are verbs

### 🔢 Sequence numbers (time)

Sequence numbers express **temporal order**. Without them, you do not really have a story, you have a graph.

### 📝 Annotations (assumptions and clarifications)

Annotations capture:

- Assumptions (“moviegoer has no subscription”)
- Clarifications (“and mentions the language”)
- Minor variations worth noting without creating a separate story

### 🗂️ Groups (structure)

Groups cluster parts of the story that belong together:

- A phase (“Search”, “Payment”)
- A location (“At the box office”)
- A repeated or optional segment
- An organizational boundary

Groups help scale Domain Storytelling without changing the language.

## The grammar: how to “read” a Domain Story 📚

The core sentence structure is:

**Actor (subject) → Activity (verb) → Work Object (object), **Optionally extended with: **“with whom”** (another actor)

[![](https://substackcdn.com/image/fetch/$s_!kize!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93db791c-99ec-45c3-aa57-78433f0440c9_798x116.png)](https://substackcdn.com/image/fetch/$s_!kize!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93db791c-99ec-45c3-aa57-78433f0440c9_798x116.png)

That is why Domain Storytelling stays accessible: it mirrors how people describe work in conversation.

## A complete example Metropolis Cinema 🎬

We will build the story progressively, from the first sentence to the complete narrative.

### Story setup what the domain expert tells

A moviegoer arrives at the box office. They want to buy a ticket for a show. The cashier uses the seating plan to find and suggest seats. The moviegoer chooses a seat. The cashier marks it. Then payment happens and the ticket is handed over.

This would be the final result suggested on the book.

[![](https://substackcdn.com/image/fetch/$s_!-jZ6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f1917aa-987e-42e6-8da8-4d9f596aa7d9_893x1236.png)](https://substackcdn.com/image/fetch/$s_!-jZ6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f1917aa-987e-42e6-8da8-4d9f596aa7d9_893x1236.png)

I have re-think it again only with the small domain story that I mention on top and I came also with other way of represent it. And alternative to this big picture could be a smaller version, with slices of the behavior. For example.

The moviegoer ask if he can buy tickets for the movie he/she want’s to watch.

[![](https://substackcdn.com/image/fetch/$s_!4WeL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad886e13-90ba-4c89-820c-0016f6690379_1514x486.png)](https://substackcdn.com/image/fetch/$s_!4WeL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad886e13-90ba-4c89-820c-0016f6690379_1514x486.png)

When the moviegoer has decided if wants to buy the tickets, can buy the tickets.

[![](https://substackcdn.com/image/fetch/$s_!L0Tx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fc21cb8-ff55-4416-8e16-5a2fe41e1d82_1395x667.png)](https://substackcdn.com/image/fetch/$s_!L0Tx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fc21cb8-ff55-4416-8e16-5a2fe41e1d82_1395x667.png)

As you can see, this slice does not do all the storytelling at onece, but helps to understad the business.

At this stage, we have not modeled behavior yet. We only established:

- who participates
- a key assumption that shapes the scenario

This is already useful because it forces specificity.

Notice what happens here:

- We get a **shared, time-ordered story**.
- We learn domain language: show, seating plan, available seats.
- We capture an important nuance with a small annotation (“mentions the language”) instead of exploding the diagram with branching.

This is what “expert-level clarity” looks like in Domain Storytelling:

- The story reads naturally in order.
- The business flow is explicit.
- The assumptions are visible.
- The model stays understandable without technical knowledge.

## How to make Domain Stories useful 🧭

When stories become confusing, it is almost always a scope problem. These three scope dimensions keep you honest:

### Granularity (level of detail)

- High-level overview: good for alignment and onboarding
- Fine-grained: good for clarifying a specific workflow
- Too detailed: becomes UI-click tracking and loses business meaning

### Time frame

- **As-is**: how the business works today (often messy, manual, real)
- **To-be**: how it should work after change (software-enabled future)

A common workflow is to model as-is first to remove fantasy, then to-be to support change design.

### Domain purity

- **Pure**: no software mentioned, only business actions
- **Digitalized**: includes software systems as actors

This is a powerful technique: start pure to understand intent, then digitalize to discuss how software supports the work.

---

## How to use Domain Storytelling in day-to-day work 🧠✅

You do not need a “big workshop” to get value. A practical routine looks like this:

- **Pick a concrete scenario** (not a vague requirement)
- **Tell it in sentences** (“who does what with what, in what order”)
- **Draw and number each step**
- **Capture assumptions as annotations**
- **Stop when the story makes sense end-to-end**
- **List variations** (then model them as separate stories if they matter)

### What you can derive from Domain Stories

Even though Domain Storytelling is intentionally business-first, it feeds directly into engineering work:

- **Shared language**: terms become domain vocabulary
- **Candidate boundaries**: groups and handoffs hint at bounded contexts
- **Test scenarios**: each story is a strong acceptance test seed
- **Better event discovery**: later, in EventStorming, you will find events faster because the business narrative is already stable

## Common mistakes⚠️

### Mistake 1: mixing alternatives into one diagram

If you start saying “sometimes” every second sentence, you probably need another story.

**Fix:** model the default scenario first, list variations, then create separate stories for the few that matter.

### Mistake 2: modeling protocols instead of business actions

“User sends POST /checkout” is not a domain activity.

**Fix:** write what the actor intends in business language: “places order”, “confirms booking”, “marks seat”.

### Mistake 3: losing time (no sequence numbers)

Without sequence numbers, you cannot replay the story reliably.

**Fix:** number activities as you draw. Always.

### Mistake 4: turning the story into UI click-tracking

Domain Storytelling is about work, not cursor movement.

**Fix:** keep activities meaningful at business level. Use Event Modeling later when you want UI-to-event precision.

## Conclusions

Domain Storytelling is one of the best tools you can use to **understand the real business process** before you design software. It creates shared understanding quickly, and it does so in a format that is readable by almost anyone.

It shines especially as a **precursor to EventStorming or Event Modeling**, because it stabilizes the narrative of “what really happens” before you jump into events, commands, projections, or architecture. It does not mean Domain Stories capture every nuance, but they consistently surface the high-impact conversations and assumptions that matter most.

Beyond discovery, Domain Storytelling is also excellent documentation:

- It is simple enough for new team members to understand fast
- It makes onboarding easier because you can replay real scenarios
- It supports architecture work (including C4) by providing business context that explains why certain boundaries and decisions make sense
- It helps teams ask better questions earlier, when change is cheap

In short: **Domain Storytelling gives you a shared, story-shaped understanding of the domain.** Once you have that, every downstream modeling and design activity becomes faster, clearer, and less risky.

On the other hand, the question also you should ask your self is if you really need it or with UML also you could achive the same level of clarity, this could be an example of it.

[![](https://substackcdn.com/image/fetch/$s_!lOin!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74329866-d851-454e-82e8-db4d534f803f_2613x1804.png)](https://substackcdn.com/image/fetch/$s_!lOin!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74329866-d851-454e-82e8-db4d534f803f_2613x1804.png)

[Live editor](https://mermaid.live/edit#pako:eNp1U0GO0zAUvcqXd5VK1WaSppPFSFVGlE1QRVmhbtz0N7Ga2MHfbqdUlbgAQsOG5WyQuAJCnIYLMEfASWg1dGaiLGK__95_78fes1QtkUWM8L1FmeK14Jnm5VyCe7g1StpygfrfOjVKQzIBTnB_d_sNErURmKn_8Xjc4t9vf3_8dH_35RfEnHJxLKq4NiIVFZcGZtO29OvPPz8-wwy5ETKDquASaEcGnY-W9FoZBLXBuns3HkcwJrJlZYSSEZRHF5A7NamA7IJSLRr4WYVBB97Uocm0BcnkxdVVDbzFoiDY5iLNgXK1BZPjDrbO72OteNydTSPwOrV5neYtHo-dVL0_QUNAD2Ot3ICcXiN8VtwqIDU1fMNFwRcFNnR6snMyieCiA1OtKkW8eCBXIzObZS4cPZY6CWmR5QbUCurYCcp6XtTYc1YzyzN8cnq1Wb8D15gKcgzgcgmLQqVrl_JslnGuFLlIvOl9Fjjhet22a8FnflTQgZdC8gLwJs2dLzwLOqY1neZaaZHimYkp39EZ55XzTG2XmuUO5BqdA9ZlmRZLFhltsctK1CWvl2xf8-fM1ZY4Z5H7XOKK28LM2VweHM0d53dKlUemVjbLWbTiBbmVrZbcHK_WaVejXKKOlZWGRaOB14iwaM9uWHTh9zzP98LhYOiP_NFFEHTZzm2PeqHfd-8ocFjoeYcu-9C07fcug4EfeJdhP-j74bAfHv4ChbdAQw)

Sometimes, we may also reinvent the wheel, but also you need to know if this could be something you would like to use to understand your business.

## References

- Domain Storytelling website (overview, purposes). [Domain Storytelling](https://domainstorytelling.org/)
- Domain Storytelling Quick-Start Guide (pictographic language, Metropolis story, scope, scenario-based modeling). [Domain Storytelling](https://domainstorytelling.org/quick-start-guide)
- Egon.io user guide (tool rules, export formats like `.egn`). [Egon.io](https://egon.io/howto)
- Open Practice Library: Domain Storytelling practice (definition, why it is used, links to related methods). [Open Practice Library](https://openpracticelibrary.com/practice/domain-storytelling/)
- “The First Book About Domain Storytelling” (book landing page). [Domain Storytelling](https://domainstorytelling.org/book)
