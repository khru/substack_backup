Title: Event Sourcing, CQRS, And CQRS Plus Event Sourcing

URL Source: http://emmanuelvalverderamos.substack.com/p/event-sourcing-cqrs-and-cqrs-plus

Final URL: https://emmanuelvalverderamos.substack.com/p/event-sourcing-cqrs-and-cqrs-plus

Published Time: 2026-04-28T06:00:26+00:00

Markdown Content:
Do you want your system to remember what happened, or do you want it to answer questions fast?

A CRUD system stores the latest state. It overwrites the past. That is cheap and simple until you need an audit trail, a dispute timeline, a causal explanation, or you need to rebuild a read model for a new product feature. At that moment, overwriting stops being a storage choice and becomes a business exposure.

Event Sourcing and CQRS solve different problems. They overlap. They combine well. But they are not the same. Treating them as the same is a reliable way to ship a system that is complex, slow, and still not trustworthy.

This article starts at zero and goes deep. You will learn:

*   What each architecture is actually optimizing.

*   What code you write differently in each one.

*   Where the complexity really lives.

*   How to avoid primitive obsession, magic strings, and switch statements.

*   How to separate Domain Events from Integration Events without lying to yourself.

*   How to design for replay, idempotency, and schema evolution without building a fragile monster.

You will also get diagrams that are readable and name things in domain language.

This guide intentionally focuses on architecture mechanics and distribution tradeoffs. Broker deep dives, pub-sub semantics, and streaming-first design are better handled in dedicated follow-up articles.

> So you might end up defining architecture as things that people perceive as hard to change.
> 
> 
> - Martin Fowler

Use that as the framing constraint for every choice in this article. Event streams, read models, projection pipelines, and integration contracts are architectural because they are costly to change after production adoption.

*   **CQRS (Command Query Responsibility Segregation):**Separate write-side command handling from read-side query handling so each model can be optimized for its job.

*   **State:**The current values of an entity or aggregate. Example: Order status is Paid, outstanding balance is 0.

*   **Command:**A request to change state. It expresses intent. It can be rejected. Example: PlaceOrder, CapturePayment.

*   **Query:**A request to read data. It must not change state. Example: GetOrderSummary.

*   **Domain Event**  
An immutable fact that happened inside your domain boundary. It is written after a decision is made. Example: OrderPlaced, PaymentCaptured.

*   **Integration Event:**A message published for other systems. It is a contract with the outside world. It may mirror a Domain Event, but it often needs different shape, different stability rules, and different naming.

*   **Invariant:**A rule that must always hold inside a consistency boundary. Example: “You cannot capture payment twice for the same order.”

*   **Aggregate:**A consistency boundary. You load it, enforce invariants, and produce Domain Events. If you cannot enforce a rule without reading another aggregate, your boundary is wrong.

*   **Projection:**A read model built by consuming events and translating them into query-friendly tables or documents.

*   **Materialized View:**A stored, precomputed view built from another source, usually a log or a write database. It trades storage and compute for fast reads.

*   **DTO (Data Transfer Object):**A read-optimized shape returned to callers. It is usually not your domain model.

*   **Idempotency:**Processing the same message more than once does not change the final result beyond the first application. This is mandatory in event driven systems.

*   **Optimistic Concurrency:**You write only if the expected version matches the stored version. If it does not, you retry by reloading and re-deciding.

*   **Upcaster:**A component that translates older event versions into the current canonical event shape during replay.

Actionable conclusion: if your team uses these words inconsistently, stop. Fix vocabulary first. Architecture discussions without shared meaning are just noise.

> Domain events are applied inside a single domain model and are usually synchronous.
> 
> 
> - Scott Millett and Nick Tune, _Patterns, Principles, and Practices of Domain-Driven Design_

![Image 1](https://substackcdn.com/image/fetch/$s_!JDGC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1757ef9c-b216-4033-a08e-8ed517ddb83d_2835x258.png)

Your write path and your read path want different shapes.

The write path wants:

*   A model that enforces invariants.

*   Transactions or version checks.

*   Clear ownership of data and rules.

The read path wants:

*   Data shaped for screens, dashboards, search, exports.

*   Fast queries with minimal joins.

*   Multiple query shapes that evolve with product needs.

The first serious mistake is assuming one model can serve both perfectly. You can do that for small systems. For long-lived systems, it becomes a tax: every new screen fights your write model, and every new invariant fights your read needs.

Event Sourcing attacks the “truth and history” problem. CQRS attacks the “shape mismatch” problem. Combining them attacks both, but with real operational burden.

Actionable conclusion: decide which business pain you are solving first. Then choose the cheapest architecture that solves it.

![Image 2](https://substackcdn.com/image/fetch/$s_!XbqH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54e25a4d-c1de-4ddc-ae77-aacccd551c61_2952x188.png)

Pure Event Sourcing means you store Domain Events as your source of truth. You do not persist current state as the primary record. Current state is derived by replaying events into an in-memory state representation.

Pure Event Sourcing solves “I need to know what happened” as a first-class requirement.

If you store only current state, you lose intermediate steps. In regulated domains, that can be unacceptable. In non-regulated domains, it still matters when you need explainability, fraud detection, and reversible operations.

It also solves a recovery problem. If a bug writes bad state and overwrites correct state, recovery is hard. If you have an append-only history, recovery is often a rebuild with corrected code.

It also solves an evolution problem. If you want a new read model, the event stream can be used to rebuild it without migrating your write database into a new shape.

Pure Event Sourcing is expensive for reads unless you are willing to replay events for each query or accept narrow query requirements.

It is also expensive for schema evolution. Events are durable contracts. You cannot casually rename fields or reinterpret meaning.

It is also expensive for operational discipline. If you do not plan for snapshots, replays, and event versioning, your system will degrade over time.

[![Image 3](https://substackcdn.com/image/fetch/$s_!KnVN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4015c2e3-bba4-40e1-acd6-07f9469df604_1648x1578.png)](https://substackcdn.com/image/fetch/$s_!KnVN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4015c2e3-bba4-40e1-acd6-07f9469df604_1648x1578.png)

Event Sourcing is not “store events and hope”. You still need a strong domain model. In practice you implement:

*   Value Objects to remove primitive obsession.

*   An Aggregate that exposes commands as intention-revealing methods.

*   Domain Events as immutable objects.

*   An Event Store port.

*   Concurrency control using expected version.

The aggregate is where business language lives. The event store is infrastructure.

This is not style. It is correctness. Money with raw numbers is how you leak invariants into random parts of your codebase.

In Event Sourcing, two commands can race. You must prevent both from appending based on the same version.

You do this by appending with expectedRevision. If it does not match, you reload and re-decide. That pushes you toward deterministic domain logic and clean command handling.

[![Image 4](https://substackcdn.com/image/fetch/$s_!CR2y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6227bcf-37b6-4daf-a1ee-55a3afe11b13_1777x1206.png)](https://substackcdn.com/image/fetch/$s_!CR2y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6227bcf-37b6-4daf-a1ee-55a3afe11b13_1777x1206.png)

It fits when history is the product.

*   Financial transactions.

*   Entitlements and permissions.

*   Business workflows with disputes.

*   Audit-heavy domains.

It also fits when you know you will want to add new read models and analytics later without rewriting the write side.

It hurts when your product is query-heavy and you need many read shapes with low latency. You can still do it, but you will build projections, which moves you toward CQRS anyway.

It also hurts when your team cannot commit to event schema governance. Without that, you get brittle replays and broken consumers.

Actionable conclusion: Pure Event Sourcing is a strong choice only when immutable history is a first-class business requirement, not a technical curiosity.

Replaying thousands of events for every command is expensive. Snapshots store derived aggregate state every N events so you replay only the tail.

Snapshots are not the source of truth. They are a cache. You must be able to drop them and rebuild them from events.

[![Image 5](https://substackcdn.com/image/fetch/$s_!dTS5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F197fdd83-14e4-446f-806d-2022c80c70cb_1811x882.png)](https://substackcdn.com/image/fetch/$s_!dTS5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F197fdd83-14e4-446f-806d-2022c80c70cb_1811x882.png)

Actionable conclusion: If you adopt Event Sourcing, design snapshot strategy early. Do not bolt it on after performance collapses.

[![Image 6](https://substackcdn.com/image/fetch/$s_!xglp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2523e7a3-bd13-42f0-960e-c0556bb0685a_3967x4781.png)](https://substackcdn.com/image/fetch/$s_!xglp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2523e7a3-bd13-42f0-960e-c0556bb0685a_3967x4781.png)

[![Image 7](https://substackcdn.com/image/fetch/$s_!OjZS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc37dff57-4a74-4291-85ee-3472d66bc594_7126x4586.png)](https://substackcdn.com/image/fetch/$s_!OjZS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc37dff57-4a74-4291-85ee-3472d66bc594_7126x4586.png)

Pure CQRS means you separate the command side from the query side. The write database stores current state. The read database stores query-optimized views.

This is not about using two databases. It is about using two models.

CQRS solves the shape mismatch problem: the structure you need to enforce invariants is rarely the structure you need to serve queries.

A write model wants normalized data and clear transactional boundaries. A read model wants denormalized data shaped for screens.

CQRS lets you evolve read models quickly without corrupting domain logic. That often makes teams faster, not slower.

CQRS adds synchronization complexity. Your read model must be updated when your write model changes.

CQRS also forces you to decide consistency semantics. If read updates are asynchronous, users may not see their write immediately.

CQRS also adds duplication. That is intentional. You trade storage and complexity for speed and flexibility.

[![Image 8](https://substackcdn.com/image/fetch/$s_!tBzC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87d0df63-c1c7-4b42-9401-d8cf1f359c53_4421x1536.png)](https://substackcdn.com/image/fetch/$s_!tBzC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87d0df63-c1c7-4b42-9401-d8cf1f359c53_4421x1536.png)

Notice what is happening here: this is CQRS without Event Sourcing, but it still uses event-driven synchronization. That is common. It is also where many systems fail.

If you update your write database and publish a message in separate steps, failures create split-brain outcomes:

*   DB write succeeds, publish fails.

*   Publish succeeds, DB write fails.

That is not a corner case. It is normal under retries, timeouts, and partial outages.

The Transactional Outbox pattern solves this by writing the outbound message into the same transaction as the business update, then relaying it.

You still see a string in order.orderPlaced.v1. That is not avoidable because integration messages need a stable identifier. The difference is that it is wrapped, validated, and treated as part of a contract. It is not a random magic string floating around your system.

It fits when:

*   Read load is heavy or unpredictable.

*   You need multiple read shapes.

*   You want to evolve read models quickly.

*   Your write model can remain relatively stable.

It also fits as a stepping stone. Many teams adopt CQRS first, then adopt Event Sourcing only for parts of the domain where history becomes critical.

It is wrong when you do not have a clear read problem.  
If your reads are simple and your write model is not under strain, CQRS adds complexity without payoff.

It is also wrong when your product requires strong, trustworthy history inside the system itself. You can add audit logs, but that is not the same as a domain-level immutable history.

Actionable conclusion: Use CQRS when your read needs are genuinely different from your write needs and you can justify the synchronization tax.

This model uses Event Sourcing on the write side and CQRS projections on the read side.

You store Domain Events in an event store. You publish Integration Events outward. You build projections for fast queries.

This is where you get powerful capabilities:

*   Full history.

*   Multiple read models.

*   Rebuildable views.

*   Clear separation between decision-making and data-serving.

This is also where teams ship broken systems when they ignore operational reality.

[![Image 9](https://substackcdn.com/image/fetch/$s_!D0hQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12e046ff-cfd9-4a15-84b6-0279696ec4b5_4462x1536.png)](https://substackcdn.com/image/fetch/$s_!D0hQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12e046ff-cfd9-4a15-84b6-0279696ec4b5_4462x1536.png)

Domain Events express business facts inside your boundary. They can be rich, typed, and internal.

Integration Events are contracts for other systems. They must be stable, versioned, and designed with consumer needs and privacy constraints.

A clean approach is:

*   Domain Event is produced by the aggregate.

*   A translator maps Domain Events to Integration Events.

*   Integration Events are published through an outbox or transactional mechanism.

*   Projections consume events to build read models.

This prevents “outside consumers” from dictating your domain model and prevents your domain model from leaking internal structure.

[![Image 10](https://substackcdn.com/image/fetch/$s_!KXxq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45e8034f-ebb1-4cd8-b695-8e893c9e5ee8_552x1276.png)](https://substackcdn.com/image/fetch/$s_!KXxq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45e8034f-ebb1-4cd8-b695-8e893c9e5ee8_552x1276.png)

Actionable conclusion: Domain Events are about truth inside your boundary. Integration Events are about collaboration outside your boundary. Separate them or you will build coupled systems disguised as decoupled.

In the combined model, your read side is not a database. It is a pipeline:

*   Consume events.

*   Deduplicate.

*   Apply updates.

*   Store checkpoints.

*   Monitor lag.

*   Support rebuilds.

If your projection code cannot handle duplicate delivery, partial failures, and replays, your system is not correct.

[![Image 11](https://substackcdn.com/image/fetch/$s_!47iL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba52eb90-93be-433a-bf0e-e213130436f3_2212x882.png)](https://substackcdn.com/image/fetch/$s_!47iL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba52eb90-93be-433a-bf0e-e213130436f3_2212x882.png)

Actionable conclusion: treat projector idempotency as a correctness invariant, not an implementation detail.

This example is intentionally richer than a bank account. It models an order that can be placed, paid, and shipped. It also cleanly separates Domain Events from Integration Events.

This is the key difference versus state persistence: your aggregate does not “save itself”. It produces events. Persistence is separate.

This is the exact smell you referenced: instead of projecting with a switch over event types, you use double dispatch through accept.

Actionable conclusion: in CQRS plus Event Sourcing, polymorphism belongs in Domain Events and projection visitors, while deserialization is handled by a registry, not a switch.

Integration Events should be:

*   Explicitly versioned.

*   Narrow.

*   Stable.

*   Designed with consumer needs.

*   Free of internal domain structure.

A practical pattern is to publish Integration Events from an Outbox even in an Event Sourced system. That gives you reliable delivery semantics without pretending that “publishing never fails”.

[![Image 12](https://substackcdn.com/image/fetch/$s_!Wkvq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99d222a1-0166-422b-b8d1-6b453a853143_2342x822.png)](https://substackcdn.com/image/fetch/$s_!Wkvq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99d222a1-0166-422b-b8d1-6b453a853143_2342x822.png)

Actionable conclusion: reliability belongs in persistence. Publishing is I/O. Treat it like I/O.

Event Sourcing forces invariants into the aggregate because decisions happen by replaying history and producing events.

CQRS without Event Sourcing can enforce invariants with transactions and constraints, but teams often drift into anemic “update row” logic if they are not disciplined.

CQRS plus Event Sourcing makes the invariant boundary explicit: the aggregate stream is the unit of consistency.

Actionable conclusion: if invariants are central and non-negotiable, an aggregate-first model helps you keep them correct.

State-based systems often answer: “What is the value now?”  
Event-sourced systems also answer: “Why is it this way?” because the timeline is present.

CQRS systems can make debugging harder if you do not correlate write-side transactions with read-side projections and outbox messages. You must build observability into the pipeline.

Actionable conclusion: if you adopt CQRS, invest in end-to-end correlation ids, event ids, and projection lag metrics.

State-based systems evolve via schema migrations. That can be painful for big, long-lived databases.

Event-sourced systems evolve via:

*   New events for new facts.

*   New projections for new read shapes.

*   Upcasters or multi-version handling for old events.

In practice, this can make “run old and new side by side” easier than “migrate everything in place”. But only if you planned for it.

Actionable conclusion: if you expect frequent changes in read needs, projections are a powerful lever. If you expect frequent changes in event meaning, you need governance and discipline.

CQRS and event-driven approaches often increase moving parts:

*   Brokers.

*   Relays.

*   Projectors.

*   Checkpoints.

*   Replay tooling.

*   Schema registries.

*   Consumer lag monitoring.

If you cannot operate these, the architecture is wrong for your team right now.

Actionable conclusion: pick the architecture you can run reliably, not the architecture you can diagram.

![Image 13](https://substackcdn.com/image/fetch/$s_!5JCN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15163198-ff0b-479b-9b9d-0492452abdb8_2054x348.png)

If you skip this, replay becomes fragile. Older events are still facts. They need a deterministic path into the current model.

[![Image 14](https://substackcdn.com/image/fetch/$s_!qUx2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7b560cf-e230-4158-b342-e4d1759b5be6_1763x444.png)](https://substackcdn.com/image/fetch/$s_!qUx2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7b560cf-e230-4158-b342-e4d1759b5be6_1763x444.png)

Catch-up subscriptions are usually simpler for internal projections. Persistent subscriptions and broker fan-out can scale distribution, but require stricter operational discipline on ordering and consumer lag.

[![Image 15](https://substackcdn.com/image/fetch/$s_!ZIpX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F624c4dab-0a82-4519-a268-23ca24692632_1258x437.png)](https://substackcdn.com/image/fetch/$s_!ZIpX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F624c4dab-0a82-4519-a268-23ca24692632_1258x437.png)

A decision process that is hard to game

Write them as business constraints:

*   “We must explain every balance change.”

*   “We must rebuild analytics for the last 2 years.”

*   “Reads must be under 50 ms p95 for order history.”

*   “We must support multiple read models for different teams.”

If your list includes “explain every change”, Event Sourcing is immediately on the table.

Are reads:

*   Few and simple, mostly “current state”?

*   Many and shaped for multiple screens?

*   Heavy search and filtering?

If reads are many and shape-specific, CQRS is on the table even without Event Sourcing.

If your product requires “read-your-write immediately” on most screens, asynchronous projections might create UX friction.

If you can tolerate eventual consistency for most screens, projections are a huge win.

If you cannot run an event pipeline with idempotent consumers, checkpoints, replays, and schema governance, then CQRS plus Event Sourcing is a future move, not a current one.

[![Image 16](https://substackcdn.com/image/fetch/$s_!Wm4m!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59c0bb8e-fa62-4ee9-8432-ef763b9fb65b_1569x1404.png)](https://substackcdn.com/image/fetch/$s_!Wm4m!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59c0bb8e-fa62-4ee9-8432-ef763b9fb65b_1569x1404.png)

You do not need to jump directly to the hardest thing

1.   Start with a strong domain model inside your current persistence approach.  
Kill primitive obsession. Use Value Objects. Make invariants explicit.

2.   Introduce CQRS only for the read models that hurt.  
Do not split everything. Split the pain.

3.   Add Outbox if you publish messages from your write database.  
Without it, reliability is fake.

4.   Adopt Event Sourcing for one aggregate where history is obviously valuable.  
Prove replay and snapshot strategy in a limited scope.

5.   Add projections and build replay tooling as a product feature.  
If you cannot rebuild, you do not own your system.

Actionable conclusion: incremental adoption protects you from ideology and lets you buy complexity only when it pays rent.

You are going to implement the same banking capabilities three times:

*   Open an account

*   Deposit cash

*   Withdraw cash

*   Query the current balance

All three implementations share the same domain language and the same Value Objects. What changes is persistence, read strategy, and the shape of the application layer.

** Note all this factory methods `of` could use an object or a specific type, but for the example I thought it was good enough.

[![Image 17](https://substackcdn.com/image/fetch/$s_!Ynrm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e29a3be-6599-4b51-9e4b-2ced48fda917_681x1020.png)](https://substackcdn.com/image/fetch/$s_!Ynrm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e29a3be-6599-4b51-9e4b-2ced48fda917_681x1020.png)

No switch statements. Each event knows how to apply itself to state and how to route itself to a visitor when you need one.

No generic errors like CannotShipBeforePaid. The banking rules are explicit.

[![Image 18](https://substackcdn.com/image/fetch/$s_!kVnz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7419797e-3f7d-4776-8290-1ffce9d4cb2c_2150x978.png)](https://substackcdn.com/image/fetch/$s_!kVnz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7419797e-3f7d-4776-8290-1ffce9d4cb2c_2150x978.png)

[![Image 19](https://substackcdn.com/image/fetch/$s_!_e9k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F800a6803-d804-483a-9f45-fd50fc920fb2_1416x882.png)](https://substackcdn.com/image/fetch/$s_!_e9k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F800a6803-d804-483a-9f45-fd50fc920fb2_1416x882.png)

Key characteristic: reads are computed from history. Fast reads are not the goal here.

[![Image 20](https://substackcdn.com/image/fetch/$s_!tFMX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32998fb8-a66f-415b-b0d4-2a154aa47de1_1187x1388.png)](https://substackcdn.com/image/fetch/$s_!tFMX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32998fb8-a66f-415b-b0d4-2a154aa47de1_1187x1388.png)

These are not Domain Events. They exist to update read models and inform other systems. They are versioned and enumerated.

[![Image 21](https://substackcdn.com/image/fetch/$s_!C55_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7b53f06-1862-4529-abfe-e18ffd0d3b7e_2348x978.png)](https://substackcdn.com/image/fetch/$s_!C55_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7b53f06-1862-4529-abfe-e18ffd0d3b7e_2348x978.png)

[![Image 22](https://substackcdn.com/image/fetch/$s_!OK6K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa87b689f-fa55-46e6-8b8b-dfd78261af96_1590x630.png)](https://substackcdn.com/image/fetch/$s_!OK6K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa87b689f-fa55-46e6-8b8b-dfd78261af96_1590x630.png)

No switch statements.

Key characteristic: reads are fast because they hit a view. History is not preserved unless you add a separate audit mechanism.

[![Image 23](https://substackcdn.com/image/fetch/$s_!xsDy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fe30e4a-79ea-4268-bf3e-1be072a48cb8_1502x1644.png)](https://substackcdn.com/image/fetch/$s_!xsDy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fe30e4a-79ea-4268-bf3e-1be072a48cb8_1502x1644.png)

This is where you keep Domain Events rich and internal, and keep Integration Events stable and consumer oriented.

No switch statements. Use Visitor.

The translator above is intentionally incomplete because balance derivation should come from the aggregate state or a dedicated calculator, not from ad hoc deltas. A concrete implementation below fixes that by using the aggregate’s balance after applying events.

This shows the combined pipeline:

*   load stream

*   rehydrate aggregate

*   decide

*   append domain events with expected revision

*   translate to integration events

*   write integration events to outbox

[![Image 24](https://substackcdn.com/image/fetch/$s_!CBt8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde56cfae-b695-443d-ba3e-3c9c20c5dc36_2376x978.png)](https://substackcdn.com/image/fetch/$s_!CBt8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde56cfae-b695-443d-ba3e-3c9c20c5dc36_2376x978.png)

[![Image 25](https://substackcdn.com/image/fetch/$s_!WMRY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb17b23a3-4629-40dc-9861-d061273f9709_1567x630.png)](https://substackcdn.com/image/fetch/$s_!WMRY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb17b23a3-4629-40dc-9861-d061273f9709_1567x630.png)

[![Image 26](https://substackcdn.com/image/fetch/$s_!4TBa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80ae56dd-6bb7-4ab7-8317-7dc1272112ad_1425x556.png)](https://substackcdn.com/image/fetch/$s_!4TBa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80ae56dd-6bb7-4ab7-8317-7dc1272112ad_1425x556.png)

If you want idempotency here, add a ProjectionCheckpoint store keyed by (projectorId, accountId) or by a global position. The key idea is the same: the projector must be safe under duplicate delivery.

*   Pure Event Sourcing: append Domain Events, derive state by replay

*   Pure CQRS: write current state, push integration events via outbox

*   CQRS plus Event Sourcing: append Domain Events, project into read models, publish integration events

*   Pure Event Sourcing: replay events on read

*   Pure CQRS: read from materialized views

*   CQRS plus Event Sourcing: read from materialized views

*   Pure Event Sourcing: optimistic concurrency on stream revision

*   Pure CQRS: database transaction plus outbox transaction

*   CQRS plus Event Sourcing: optimistic concurrency plus outbox transaction

Do not let diagrams teach the wrong rule. The biggest mistakes in practice are:

*   Mixing domains across diagrams (banking vs user profile) which breaks reader trust.

*   Implying that Event Sourcing always means full replay for every read, which is only one option.

*   Treating the Event Bus as mandatory in CQRS plus Event Sourcing, when it is often “subscription to the event store” or “outbox to broker,” depending on the stack.

The diagrams below keep one domain language, preserve architectural boundaries, and make implementation decisions explicit.

This diagram is valuable because it shows the core mechanic: rehydrate aggregate from the event stream, decide, append a new Domain Event. It also makes the read trade-off explicit.

[![Image 27](https://substackcdn.com/image/fetch/$s_!ExvN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6f81214-13f3-4d70-8e9c-fbe8b92d8dea_2913x1714.png)](https://substackcdn.com/image/fetch/$s_!ExvN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6f81214-13f3-4d70-8e9c-fbe8b92d8dea_2913x1714.png)

Actionable conclusion: keep this diagram because it teaches the real write path and prevents replay misconceptions.

*   It teaches the real write path of Event Sourcing.

*   It makes snapshots a performance tactic, not a different architecture.

*   It avoids teaching “Event Sourcing always equals full replay” as a universal rule.

If your article already explains snapshots later, keeping the snapshot box here is still helpful. It prevents the reader from concluding that replay cost is inevitable.

This is valuable when it shows two things clearly: the write model enforces invariants on the write store, and the read model is updated through a reliable synchronization mechanism.

If you show “Write DB triggers synchronizer,” you risk implying a brittle coupling. For an article, it is better to show a stable, production-friendly pattern like Outbox.

[![Image 28](https://substackcdn.com/image/fetch/$s_!Kd2u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4c1dc6f-63e9-4b29-875a-d4ef81e3fcc4_6662x1926.png)](https://substackcdn.com/image/fetch/$s_!Kd2u!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4c1dc6f-63e9-4b29-875a-d4ef81e3fcc4_6662x1926.png)

Actionable conclusion: keep this diagram because it separates write and read concerns while preserving reliable synchronization.

*   It teaches CQRS as “different models for write vs read,” not “microservices.”

*   It shows the minimum reliability mechanism you need when reads depend on async sync.

*   It stays in banking language all the way through.

This is valuable when it shows the split correctly:

*   Write side persists Domain Events.

*   Read side consumes events and builds projections.

*   The integration boundary is explicit: a Domain Event is not automatically an Integration Event.

[![Image 29](https://substackcdn.com/image/fetch/$s_!UsHH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdeebeb7-5814-4729-907c-557c436812ee_7051x2912.png)](https://substackcdn.com/image/fetch/$s_!UsHH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcdeebeb7-5814-4729-907c-557c436812ee_7051x2912.png)

Actionable conclusion: keep this diagram because it makes boundary translation and projection correctness explicit.

*   It makes “Domain Event vs Integration Event” visible in the system, not just in prose.

*   It shows the operational reality: projection idempotency and checkpointing.

*   It shows the Event Bus as “broker distribution,” not a magical component.

If you have room, these two are high ROI because they explain failure modes with one picture.

[![Image 30](https://substackcdn.com/image/fetch/$s_!MNuM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb99c13a7-ba42-43f4-ae65-402f2ba908bc_1905x1014.png)](https://substackcdn.com/image/fetch/$s_!MNuM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb99c13a7-ba42-43f4-ae65-402f2ba908bc_1905x1014.png)

[![Image 31](https://substackcdn.com/image/fetch/$s_!cjzG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F539d3588-257e-40b1-b20a-b314107b1f19_1515x920.png)](https://substackcdn.com/image/fetch/$s_!cjzG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F539d3588-257e-40b1-b20a-b314107b1f19_1515x920.png)

If your article explicitly teaches when eventual consistency is acceptable, this diagram makes the concept concrete.

This version shows the balance each handler believes is true, the balance that actually becomes true, and the domain level result after retry.

[![Image 32](https://substackcdn.com/image/fetch/$s_!q1N5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e7bccf8-920a-4cf6-af22-c022d490dfda_3248x2820.png)](https://substackcdn.com/image/fetch/$s_!q1N5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e7bccf8-920a-4cf6-af22-c022d490dfda_3248x2820.png)

Why this diagram pays off:

*   It shows that concurrency control is not “an infrastructure error.” It is how you stop two valid commands from producing an invalid final state.

*   It shows that the eventual user facing error is often a domain error (InsufficientFunds) after retry, not ConcurrencyConflict.

You can explain the same architecture with different event distribution mechanics. Each one is real. Each one has different operational properties.

This is the cleanest mental model: the event store is the log, projections are consumers with checkpoints. Catch-up subscriptions are a common fit for read models because they preserve ordering and rely on explicit checkpoints.

[![Image 33](https://substackcdn.com/image/fetch/$s_!6ZsS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54aca99f-6917-44ee-a415-ca8425ddd61e_5355x2094.png)](https://substackcdn.com/image/fetch/$s_!6ZsS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54aca99f-6917-44ee-a415-ca8425ddd61e_5355x2094.png)

When this is a good choice:

*   You want the event store to be the single distribution mechanism for internal projections.

*   You value deterministic ordering and replay as first class needs.

Checkpoint strategy is the first non-negotiable detail. Store one checkpoint per projection consumer, not one global checkpoint for the whole service. The checkpoint should include at least the consumer name, stream or subscription identifier, last processed position, and update timestamp. Persist checkpoint updates in the same transaction where you persist the projection row update. If those two writes are separated, your projector can acknowledge progress without actually updating the read model. That is silent data loss.

Replay strategy is the second non-negotiable detail. Rebuild means resetting projection state, resetting checkpoint to the initial position, and replaying the stream in order. If you also use inbox deduplication, clear the inbox state for that consumer before replay. If you keep old dedupe markers, replay skips historical events and the rebuilt view is incomplete. Run rebuild as an explicit operation with progress metrics and back-pressure controls, not as an ad hoc script.

Actionable conclusion: if a team cannot explain checkpoint transaction boundaries and replay reset rules in five minutes, the projection pipeline is not production ready.

This is the “reliable publish” model: write and publish are made consistent by persisting outgoing messages as part of the same local transaction, then relaying them to a broker.

This variant is especially common when other services must consume integration events, not just internal projections.

[![Image 34](https://substackcdn.com/image/fetch/$s_!3zyh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d0e94e9-7d4f-48e1-8219-99cebbb6ae30_5733x1940.png)](https://substackcdn.com/image/fetch/$s_!3zyh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d0e94e9-7d4f-48e1-8219-99cebbb6ae30_5733x1940.png)

When this is a good choice:

*   You want a broker as the integration backbone.

*   You want independent consumers to scale without hitting the event store.

*   You want to decouple read model updates from the event store technology.

The key thing to be honest about:

*   If your event store and outbox are in different datastores, you cannot make them atomic without distributed transactions. Many teams implement the outbox as part of the same persistence boundary, or derive integration events by subscribing to the event store and then publishing.

This is the “publish right after commit” style. It is common in codebases, but you need to frame it correctly: it is simple, but can suffer from dual write inconsistencies unless you add outbox or similar guarantees.

[![Image 35](https://substackcdn.com/image/fetch/$s_!Ly1F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ba4d95d-db12-4644-af51-8ed432ac2e0e_4269x1554.png)](https://substackcdn.com/image/fetch/$s_!Ly1F!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ba4d95d-db12-4644-af51-8ed432ac2e0e_4269x1554.png)

When this is a good choice:

*   You have one runtime and one deployment unit, and you can treat publishing as part of the same reliability boundary.

*   You can tolerate or mitigate publish failures with retries and idempotent handling.

The critical caveat is failure after commit. If the event store append succeeds and publish fails, your read models and downstream consumers miss the change. Retries inside the same request are not enough because process crashes and node restarts happen. You need a recoverable publish path. The usual answer is transactional outbox. A secondary answer is a durable pending-publish log with an autonomous relay loop and idempotent publisher semantics.

Actionable conclusion: direct bus publish is acceptable only when you can prove recovery for post-commit publish failures. If you cannot prove that, move to outbox.

The Inbox pattern is not a different architecture. It is a safety layer for consumers. It is how you survive at-least-once delivery and retries without corrupting your read model.

You can present it as a small diagram you reuse everywhere you show message consumption.

[![Image 36](https://substackcdn.com/image/fetch/$s_!xaM9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80acac6e-a7aa-44f2-9237-1856dde2266b_2094x1178.png)](https://substackcdn.com/image/fetch/$s_!xaM9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80acac6e-a7aa-44f2-9237-1856dde2266b_2094x1178.png)

This aligns with the idempotent consumer guidance: duplicates are normal, so you design for them.

A more complete example:

[![Image 37](https://substackcdn.com/image/fetch/$s_!a2jY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee58127f-cfda-462d-981e-75bcdf93ac42_3638x1972.png)](https://substackcdn.com/image/fetch/$s_!a2jY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee58127f-cfda-462d-981e-75bcdf93ac42_3638x1972.png)

When to use Inbox, Outbox or both

[![Image 38](https://substackcdn.com/image/fetch/$s_!ikTH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfcd5502-34f7-4472-9e8e-9a5f2b7f50a3_1645x2144.png)](https://substackcdn.com/image/fetch/$s_!ikTH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfcd5502-34f7-4472-9e8e-9a5f2b7f50a3_1645x2144.png)

How could it look like:

[![Image 39](https://substackcdn.com/image/fetch/$s_!eSA3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf0f9f99-e5a6-4daf-a1f2-8d26cc7a5a6e_3693x2078.png)](https://substackcdn.com/image/fetch/$s_!eSA3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf0f9f99-e5a6-4daf-a1f2-8d26cc7a5a6e_3693x2078.png)

[![Image 40](https://substackcdn.com/image/fetch/$s_!y7xB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffabdf089-dc0d-46f2-8f97-ca5052dadd08_9588x4308.png)](https://substackcdn.com/image/fetch/$s_!y7xB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffabdf089-dc0d-46f2-8f97-ca5052dadd08_9588x4308.png)

*   Bellemare, Adam. _Building Event-Driven Microservices: Leveraging Organizational Data at Scale_.

*   Dilger, Martin. _Understanding Eventsourcing: Planning and Implementing Scalable Systems with Event Modeling and Event Sourcing_.

*   Fowler, Martin. _What Do You Mean by Event-Driven?_. [https://martinfowler.com/articles/201701-event-driven.html](https://martinfowler.com/articles/201701-event-driven.html)

*   Fowler, Martin. _CQRS_. [https://martinfowler.com/bliki/CQRS.html](https://martinfowler.com/bliki/CQRS.html)

*   Millett, Scott; Tune, Nick. _Patterns, Principles, and Practices of Domain-Driven Design_.

*   Richardson, Chris. _Microservices Patterns_.

*   Richardson, Chris. _Pattern: Transactional Outbox_. [https://microservices.io/patterns/data/transactional-outbox.html](https://microservices.io/patterns/data/transactional-outbox.html)

*   Confluent, Team. _Exactly-once Semantics is Possible: Here’s How Apache Kafka Does it_. [https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/](https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/)

*   Microsoft, Learn. _CQRS Pattern_. [https://learn.microsoft.com/azure/architecture/patterns/cqrs](https://learn.microsoft.com/azure/architecture/patterns/cqrs)

*   Microsoft, Learn. _Event Sourcing Pattern_. [https://learn.microsoft.com/azure/architecture/patterns/event-sourcing](https://learn.microsoft.com/azure/architecture/patterns/event-sourcing)

*   Microsoft, Learn. _Materialized View Pattern_. [https://learn.microsoft.com/azure/architecture/patterns/materialized-view](https://learn.microsoft.com/azure/architecture/patterns/materialized-view)

*   Refactoring.guru, Team. _Switch Statements Code Smell_. [https://refactoring.guru/smells/switch-statements](https://refactoring.guru/smells/switch-statements)

*   Refactoring.guru, Team. _Visitor Pattern_. [https://refactoring.guru/design-patterns/visitor](https://refactoring.guru/design-patterns/visitor)
