Title: Transactional Outbox Pattern, from Zero to Production

URL Source: http://emmanuelvalverderamos.substack.com/p/transactional-outbox-pattern-from

Final URL: https://emmanuelvalverderamos.substack.com/p/transactional-outbox-pattern-from

Published Time: 2026-04-21T06:01:15+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!O7M-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b0454f9-372e-4ad7-b151-eab2465844e7_1024x1536.png)](https://substackcdn.com/image/fetch/$s_!O7M-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b0454f9-372e-4ad7-b151-eab2465844e7_1024x1536.png)

Do you want speed and reliability at the same time, or are you willing to pay later.

Event driven systems let you ship fast, but they also split a fact into two actions, and that split is where failures hide.

Think of it as sending a package and the receipt in two envelopes. You gain freedom, but you can lose trust if one arrives without the other.

The failure is simple. You commit a row in PostgreSQL and then publish an event, and one of those steps fails.

You get two lies, and both are expensive.

*   DB updated but no event.

*   Event published but DB rolled back.

Do not call this eventual consistency and move on. It is missing facts, and missing facts create cleanup work.

Distributed transactions try to solve this, but they bring costs you can feel.

> If you want to make sure that several different systems either commit or abort together, two-phase commit can help.
> 
> 
> - Martin Kleppmann, Designing Data-Intensive Applications, p. 456

That line is true, but it is not free. Two-phase commit adds coordination, locks, and a failure mode that hurts throughput and operations.

Messaging systems also rarely guarantee exactly-once end to end.

> A message broker should ideally deliver each message only once, but guaranteeing exactly-once messaging is usually too costly.
> 
> 
> - Chris Richardson, Microservices Patterns, p. 125

So the constraint is clear. We want local atomicity, reliable publishing, and eventual consistency that we can actually manage.

Here is the atomic truth table in one glance.

![Image 2](https://substackcdn.com/image/fetch/$s_!H1X9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb1766ea-ae5e-482d-a0c7-aa434ed48964_1242x219.png)

Use the table as a diagnostic, not as decoration.

Outbox removes the two inconsistent outcomes by making DB commit and outbox insert one atomic step.

Delivery semantics are not words, they are behaviors you must design for.

*   At most once: you may lose messages, but you never see duplicates.

*   At least once: you do not lose messages, but you may see duplicates.

*   Effectively once: you see duplicates but your processing makes them harmless.

Write the integration event to an outbox table in the same local transaction as the business data, then publish it later. Not publish inside the transaction, but persist then relay.

> Both the internal table updates and the outbox updates must be bundled into a single transaction.
> 
> 
> - Adam Bellemare, Building Event-Driven Microservices, p. 82

That is the entire pattern. Everything else is just disciplined plumbing to keep the promise.

We will build a minimal ecommerce flow with .NET 10, PostgreSQL, Dapper, and FluentMigrator. No Entity Framework, and no hidden magic.

OrderService writes orders and outbox messages. NotificationService consumes events and uses an inbox to deduplicate. That is the minimal end to end path.

We will use hexagonal architecture so the core logic depends on ports, not on infrastructure. That is not style, it is control.

Before the code, define what you are sending, because the message type sets your guarantees.

*   Command: do this, one handler, can fail validation.

*   Event: this happened, immutable, many consumers.

*   Query: give me information, no state change.

Outbox is for events, not commands. Misuse it and you create invisible coupling.

Here is the outbox row lifecycle in plain steps.

*   Created inside the business transaction.

*   Claimed by a relay with a lock and deadline.

*   Published to the broker or stream.

*   Marked published or marked failed with error details.

If you do not track this lifecycle, you will not understand your own lag.

Here is the flow you are about to build.

[![Image 3](https://substackcdn.com/image/fetch/$s_!6slX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0f7f96e-3f94-4f89-9c84-9fee963d85bf_2733x1266.png)](https://substackcdn.com/image/fetch/$s_!6slX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0f7f96e-3f94-4f89-9c84-9fee963d85bf_2733x1266.png)

[![Image 4](https://substackcdn.com/image/fetch/$s_!FRk0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79062d8a-f9ff-4de3-bdc4-421494b531f0_5551x2128.png)](https://substackcdn.com/image/fetch/$s_!FRk0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79062d8a-f9ff-4de3-bdc4-421494b531f0_5551x2128.png)

The only cross system step is outside the database transaction, which is where retries are safe.

Here is the code shape using ports and adapters so you can see the boundaries.

[![Image 5](https://substackcdn.com/image/fetch/$s_!KYdv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fceb2a941-b0a6-4733-9bd0-6fb8eb4501b8_2042x2060.png)](https://substackcdn.com/image/fetch/$s_!KYdv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fceb2a941-b0a6-4733-9bd0-6fb8eb4501b8_2042x2060.png)

Ports protect the core from infrastructure churn and keep change affordable.

This example is long on purpose. The pattern is simple, but production is not.

You need IDs and money with meaning, not naked primitives. This prevents silent bugs.

Checkpoint: if a value can be invalid, encode the rule now, not later.

Keep domain events inside the model, not glued on later. That keeps intent close to behavior.

Checkpoint: a domain event is about the domain, not about transport.

Integration events are public contracts. Keep them explicit and versioned.

Checkpoint: if a consumer needs it, it belongs here, not in your internal model.

This is the seam where you protect your model from the outside world.

Checkpoint: keep domain events stable and evolve integration events with versioned message types.

Event names are contracts, not labels. Use past tense and describe facts, not commands.

Use a stable, explicit message type that carries versioning, for example order.placed.v1 or payment.authorized.v1.

Avoid leaking internal structure into the name. If your name depends on a table or a class, it will change when your code changes.

When you need a breaking change, create a new versioned type, publish both for a while, then retire the old one once all consumers have moved.

Checkpoint: message names should make sense to a consumer who does not know your code.

This is the unit that actually gets persisted and later published.

Checkpoint: the outbox payload is a public contract, so treat it like one.

Ports make the application layer independent of infrastructure. That is how you keep change cheap.

Checkpoint: no port should leak infrastructure types into the domain.

The outbox table is the atomic boundary you can trust.

Checkpoint: the lock fields exist to allow safe parallel relays.

The inbox table prevents duplicate side effects on the consumer.

Checkpoint: inbox is a write barrier, not a cache.

This is the heart of the pattern. One transaction, two writes.

Checkpoint: kill the process after commit and before publish. The outbox row is still there.

Repositories take an explicit transaction so nothing leaks across boundaries.

Checkpoint: if the order write fails, the outbox insert fails with it.

Claiming prevents duplicate publishes when multiple relay instances run.

Checkpoint: locking is cheap compared to duplicate side effects.

Here is the claiming flow at a glance.

[![Image 6](https://substackcdn.com/image/fetch/$s_!kWPo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd93e1de-6c38-4fd9-b106-196633c822f1_1238x726.png)](https://substackcdn.com/image/fetch/$s_!kWPo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd93e1de-6c38-4fd9-b106-196633c822f1_1238x726.png)

Claiming is what makes horizontal scaling safe without global coordination.

The relay is a background worker that retries safely. It is boring on purpose.

Checkpoint: retries are safe because the outbox row is still the source of truth.

You need a retry policy that degrades gently, not a loop that burns your database.

Exponential backoff is the default because it reduces pressure while failures persist.

In this code, backoff doubles up to a max, which is simple and predictable.

If you need more control, consider jittered backoff, circuit breakers, and a dead letter table after N attempts.

Remember the tradeoff. Faster retries reduce lag but raise load and operational pressure.

RabbitMQ is a broker. Messages leave the queue after acknowledgment.

Checkpoint: the broker is not your transaction, the outbox is.

Kafka is a log. Retention and replay are first class.

Checkpoint: idempotent producer reduces duplicates but does not remove the need for inbox.

Inbox is the consumer side gate. It makes duplicates harmless.

Checkpoint: duplicates become a no-op, not a fire drill.

The use case handles idempotency and side effects in one local transaction.

Checkpoint: if the consumer crashes before commit, it will retry safely.

Here is the inbox flow in one picture.

[![Image 7](https://substackcdn.com/image/fetch/$s_!H-Q1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa528d186-77fe-4006-9af8-8987ca6a3e2f_1155x1178.png)](https://substackcdn.com/image/fetch/$s_!H-Q1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa528d186-77fe-4006-9af8-8987ca6a3e2f_1155x1178.png)

Inbox is your duplicate firewall, and it keeps recovery cheap.

Ack only after the DB transaction commits. That is the order of truth.

Checkpoint: ack is your statement of durability, so do it last.

Commit offsets only after the transaction commits. Do not lie to your log.

Checkpoint: if you do not commit, Kafka will replay, and inbox will protect you.

Ordering is only guaranteed per aggregate or per partition, not across the whole system.

If you care about order, choose a key like orderId for Kafka partitions and design RabbitMQ consumers to avoid parallel reordering.

Replay is not an outbox feature, it is a broker or storage feature.

Kafka makes replay explicit by letting you reset offsets and reprocess from a point in time. RabbitMQ does not, so replay usually means storing events elsewhere or requeueing from a dead letter store.

If you plan to replay, design your consumers so reprocessing is safe, and be clear about what can be replayed and what cannot.

Concrete payloads make versioning real, not theoretical.

If you need to add a field, do it in a backward compatible way and keep the old type running in parallel.

For example, order.placed.v2 can add discountCode without breaking order.placed.v1, then you phase out v1 after consumers switch.

Inbox makes duplicates safe, but only if your side effects are idempotent at the boundary.

For example, sending two emails or charging a card twice is not idempotent, so those actions need their own guards or external idempotency keys.

The transport is a configuration choice, not a code fork. That keeps options open.

Checkpoint: you can switch brokers without touching core logic.

Use docker compose to run PostgreSQL, RabbitMQ, Kafka, and both services together. That makes the system testable as a whole.

Checkpoint: a pattern is only real when you can run it end to end.

Polling is simple and predictable. CDC is faster but heavier. Decide based on throughput and operational capacity.

Outbox prevents missing events. Inbox prevents duplicate side effects. Use both when correctness matters.

RabbitMQ distributes work to competing consumers. Kafka records facts for replay. Choose based on which behavior protects value in your context.

If events are low criticality and you can tolerate loss without recovery, outbox may be more machinery than you need.

If your data store does not support local transactions or you do not have a durable write, outbox cannot deliver its promise.

Outbox rows cannot grow forever.

Keep published rows for a short retention window so you can debug and replay locally, then archive or purge on a schedule.

A practical default is to keep 7 to 30 days of published rows and move older ones to cold storage or delete them.

Do not delete unpublished rows without a manual review and a clear incident record.

Use this to verify your safety guarantees, not just your happy path.

*   Crash after DB commit, before publish. Expect outbox row to remain and publish later.

*   Crash after publish, before mark published. Expect duplicate delivery and inbox to absorb it.

*   Broker down. Expect outbox backlog to grow and relay to retry with backoff.

*   Database down. Expect relay to stop and resume without loss.

*   Consumer crash before ack or offset commit. Expect replay and idempotent handling.

*   Lock timeout. Expect another relay to claim and publish safely.

Measure what you cannot see in logs.

*   Outbox lag: age of oldest unpublished message.

*   Outbox size: count of unpublished messages.

*   Publish error rate and last_error distribution.

*   Inbox duplicate rate.

*   Consumer lag for Kafka.

*   Queue depth for RabbitMQ.

*   Dead letter count and age.

Start with alerts on outbox lag and dead letter growth. Those are the earliest signs of drift.

Versioning is not optional when multiple services consume your events.

*   Keep message types explicit and versioned.

*   Add fields in a backward compatible way first.

*   Publish both versions during migration.

*   Remove old versions only after all consumers confirm the switch.

If you skip this, you will break consumers silently and call it a data bug.

Retries must have a limit, and failures need a place to land.

![Image 8](https://substackcdn.com/image/fetch/$s_!hH4R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feeae95c8-3819-47ce-bac7-38ef89f07255_3255x452.png)

Dead letter is not an exception. It is part of your reliability model.

Keep this short and run it after any change that touches outbox, relay, or consumer logic.

*   Place an order and ensure one outbox row is created and later marked published.

*   Stop the broker, create orders, then restart and confirm backlog drains.

*   Kill the relay during publish and confirm duplicates are absorbed by the inbox.

*   Crash the consumer before commit and confirm replay does not create duplicates.

*   Simulate schema change and confirm old consumers still process v1 correctly.

Events are shared memory across services, so be deliberate about content.

*   Do not emit PII unless it is essential.

*   Do not include internal database IDs that reveal structure.

*   Prefer business identifiers that are stable and shareable.

*   Publishing inside the business transaction. Look for broker calls inside your unit of work.

*   Acknowledging before commit. Watch for ack or offset commit before DB commit.

*   No inbox or idempotency key. Duplicates will create side effects.

*   Outbox without claiming. Multiple relays will race and double publish.

*   Message types without versions. You will block future changes.

*   No lag metrics. Incidents will surprise you instead of warning you.

[![Image 9](https://substackcdn.com/image/fetch/$s_!_uVg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ceda407-19cb-48ef-a4a8-c7ea5774ef28_4374x3622.png)](https://substackcdn.com/image/fetch/$s_!_uVg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ceda407-19cb-48ef-a4a8-c7ea5774ef28_4374x3622.png)

[![Image 10](https://substackcdn.com/image/fetch/$s_!civV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ffd33a9-c6b4-47cc-829d-48931eb208db_5170x4239.png)](https://substackcdn.com/image/fetch/$s_!civV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ffd33a9-c6b4-47cc-829d-48931eb208db_5170x4239.png)

Transactional outbox moves failure from your business transaction to a controlled relay. That is a clear tradeoff you can price.

Outbox handles missing events, inbox handles duplicate effects. Repeat that until it becomes a habit, because habits protect reliability.

The limit is real. You still need idempotent consumers, schema versioning, and observability for lag and retries.

Resist premature CDC, measure your publish lag, compare broker behaviors, and decide with data, not hope.

If it fits your context, the systemic impact is fewer hidden inconsistencies and fewer late stage surprises.

If it fits your context, team health improves because on call incidents become boring and predictable.

*   Richardson, Chris. _Microservices Patterns_.

*   Bellemare, Adam. _Building Event-Driven Microservices_.

*   Kleppmann, Martin. _Designing Data-Intensive Applications_.
