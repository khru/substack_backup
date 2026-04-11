---
title: "Streaming vs Pub Sub and the Architectural Impact on Event Driven Systems"
requested_url: "https://emmanuelvalverderamos.substack.com/p/streaming-vs-pub-sub-and-the-architectural"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/streaming-vs-pub-sub-and-the-architectural"
substack_post_id: 188436598
retrieved_at: "2026-04-11T07:47:16.589Z"
---
# Streaming vs Pub Sub and the Architectural Impact on Event Driven Systems

## Context

This article is the second step after **A Developer’s Guide to Message Brokers**. The first article explains broker basics and delivery mechanics. This one focuses on architecture decisions when you choose between pub sub and streaming models.

Do you need events only to notify work, or do you need events as durable system history.

Teams often use the words pub sub and streaming as if they were interchangeable. They are related, but they optimize different things. Pub/sub emphasizes decoupled notification and reaction. Streaming emphasizes durable ordered logs and continuous stateful processing.

Confusing them leads to architecture mistakes:

- choosing a queue model when replay is mandatory
- choosing a log model when work distribution simplicity is the priority
- underestimating retention, partitioning, and state management costs

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### The problem

If you treat streaming as “pub sub but bigger,” you miss the design shift:

- in pub sub, the event is usually a delivery unit
- in streaming, the event log is usually a system asset

That difference affects recovery, data ownership, and long-term product capabilities.

### Constraints and tradeoffs

Neither model is universally better. Each one pays different costs.

Pub sub costs:

- routing and queue operations
- duplicate handling in consumers
- dead-letter and retry governance

Streaming costs:

- partition strategy and key discipline
- offset lifecycle and replay governance
- stateful processing complexity

If your architecture decision ignores these costs, your operating model will fail before your code does.

### Quote anchor

> “A stream of liberated events must materialize back into an exact replica of the source table, and this property is used extensively for event-driven microservices (as covered in Chapter 7).”

> - Adam Bellemare, Microservices Leveraging Organizational Data at Scale, p. 73

## Fast definitions

Pub sub:

- producer publishes an event
- broker routes to subscribers
- consumers react to delivery

Streaming:

- producers append records to a durable ordered log
- consumers advance offsets through that log
- consumers can replay history and build state incrementally

For those at home:

- an offset is the numeric position of a record inside a partition
- a partition is one ordered slice of the log

Real-world example: in a retail system, pub sub can notify Shipping that an order was paid, while streaming can retain every payment event for six months so Finance can rebuild daily settlement views after a bug fix.

The architectural distinction is not syntax. It is whether event history itself is first-class.

[![](https://substackcdn.com/image/fetch/$s_!rV6c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ee93d2e-3651-43b2-8ce9-6d3882cd2b8c_1217x972.png)](https://substackcdn.com/image/fetch/$s_!rV6c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ee93d2e-3651-43b2-8ce9-6d3882cd2b8c_1217x972.png)

## Where pub sub and streaming overlap

Both models can deliver event-driven decoupling and asynchronous processing.

Common ground:

- producers and consumers are decoupled by contracts
- transport failures still require retry and idempotency discipline
- schema evolution still requires versioning

This overlap is why teams mix terms. The overlap is real. The optimization target is still different.

## The core differences that change architecture

### 1) Time model

Pub sub usually focuses on current delivery. Streaming explicitly keeps event history for future reads and reprocessing.

Architecture impact:

- pub sub systems prioritize delivery success and dead-letter resolution
- streaming systems also prioritize retention policy, replay speed, and historical correctness

### 2) Consumer state model

Pub sub consumers often handle each message independently. Streaming consumers often maintain evolving state from ordered records.

Architecture impact:

- streaming pushes you toward deterministic processors, checkpoint strategy, and state store design
- pub sub can stay simpler when you only need reactive side effects

### 3) Recovery model

Pub sub recovery typically means redrive of failed messages. Streaming recovery often means replay from offsets and rebuilding materialized views. A materialized view is a stored read model rebuilt from source events or source tables to optimize queries.

Architecture impact:

- streaming supports broader reconstruction workflows
- pub sub supports focused operational recovery, often faster for task workloads

### 4) Ordering semantics

Pub sub ordering is often limited and delivery-dependent. Streaming typically offers partition ordering with explicit consumer offsets.

Architecture impact:

- in streaming, partition key design becomes a core domain decision
- in pub sub, routing keys and consumer concurrency limits dominate

### 5) Product capability surface

Streaming enables historical analytics and retrospective model creation more naturally. Pub sub is excellent for near real-time reaction flows.

Architecture impact:

- choose streaming when future recomputation is a business requirement
- choose pub sub when immediate reaction and low operational overhead are primary

## Impact on event-driven architecture decisions

### Bounded context boundaries

With pub sub, many teams publish integration events for immediate downstream action. With streaming, teams may also design around shared domain timelines used to derive many projections over time.

### Data ownership and projection strategy

In streaming systems, materialized views and projection pipelines become first-class architecture components. You need explicit ownership for projection code, offsets, and rebuild playbooks.

### Operational governance

Pub sub governance emphasizes queue behavior. Streaming governance emphasizes log lifecycle and replay safety.

Minimum governance questions:

- Who owns retention policy and why.
- What replay windows are acceptable for each consumer.
- How to validate projection correctness after replay.
- How to prevent stale consumers from applying conflicting updates.

### Cost model

Streaming is often more expensive in infrastructure and cognitive load. Pub sub is often cheaper initially but can limit historical reconstruction if retention is short.

Treat this as portfolio design. You can use both models in one architecture with explicit boundaries.

## A practical selection approach

Use this decision path:

- Start from recovery and audit requirements.
- If you only need decoupled reaction, start with pub sub.
- If you need durable replay and long-lived derived state, adopt streaming.
- If your domain has both needs, split by event category and consumer intent.

[![](https://substackcdn.com/image/fetch/$s_!cNzP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5215e1b3-e48c-489c-b87a-6055edc126ea_1500x2060.png)](https://substackcdn.com/image/fetch/$s_!cNzP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5215e1b3-e48c-489c-b87a-6055edc126ea_1500x2060.png)

## Common failure modes

- Calling a queue “streaming” without retention or replay discipline.
- Calling a log “pub sub” and ignoring partition key design.
- Mixing command intent into event contracts.
- Shipping non-idempotent consumers under at-least-once delivery.
- Treating broker choice as infrastructure preference instead of architecture choice.

Each one turns event architecture into operational debt.

## Conclusions

Pub/sub and streaming are not rivals. They are different coordination and recovery models.

Pub sub is usually the better default for decoupled reaction flows. Streaming is usually the better default for history-centric systems that need replay, stateful processing, and long-term projection evolution.

The right question is not “which technology is better.” The right question is “which failure and recovery model does this business flow need.”

Answer that first, and architecture decisions become clearer, cheaper, and more defensible.

## References

- Bellemare, Adam. *Building Event-Driven Microservices*.
- Fowler, Martin. *What do you mean by “Event-Driven”?*. [https://martinfowler.com/articles/201701-event-driven.html](https://martinfowler.com/articles/201701-event-driven.html)
- Kleppmann, Martin. *Designing Data-Intensive Applications*.
- Richardson, Chris. *Microservices Patterns*.
