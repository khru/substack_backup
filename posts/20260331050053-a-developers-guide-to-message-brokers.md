---
title: "A Developer's Guide to Message Brokers"
requested_url: "https://emmanuelvalverderamos.substack.com/p/a-developers-guide-to-message-brokers"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/a-developers-guide-to-message-brokers"
substack_post_id: 188435973
retrieved_at: "2026-04-04T07:46:13.391Z"
---
# A Developer's Guide to Message Brokers

## Context

Do you want services to coordinate by calling each other, or by reacting to shared facts.

Most teams start with synchronous APIs because they are easy to explain. One service calls another, waits, and moves on. That model works while the number of services is small and ownership boundaries are stable. It fails when many teams need to change independently and still keep business flows reliable.

Pub sub appears as a response to that coordination tax. Instead of chaining calls, a producer publishes a fact and consumers react on their own timeline. A broker sits in the middle and handles routing, buffering, and delivery mechanics.

This is not “async everywhere.” It is explicit decoupling around event contracts.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### The problem

Without a brokered pub sub model, you usually pay in one of three ways:

- direct dependency chains where one outage cascades across services
- duplicated integration code in each service pair
- hidden ownership conflicts where multiple services emit competing versions of the same fact

The symptom is always similar: reliability depends on call order and human coordination, not on explicit contracts.

### Constraints and tradeoffs

A message broker improves decoupling, but it does not remove distributed systems constraints.

- Delivery is often at least once, so duplicates are normal.
- Ordering is usually scoped, not global.
- Consumers can lag and still be healthy, which changes how you define “up.”
- Operational burden moves from endpoint uptime to queue health, lag, retry policy, and dead-letter handling.

A broker is not a magic reliability box. It is a reliability substrate that still requires good architecture choices.

### Quote anchor

> “A message broker should ideally deliver each message only once, but guaranteeing exactly-once messaging is usually too costly.”

> - Chris Richardson

## What Pub/Sub is and what it is not

Pub sub (publish/subscribe) means producers publish events without knowing which consumers will react. Consumers subscribe to event types and process independently.

What it is:

- contract driven communication through event types
- temporal decoupling between producer and consumer
- one to many fan-out without direct service coupling

What it is not:

- a guarantee of exactly once effects
- a replacement for domain modeling
- an excuse to publish unowned or ambiguous events

Real-world example: order.placed.v1 is published once, then Billing reserves payment, Notifications sends the confirmation email, and Analytics updates revenue dashboards. Order Service does not call any of those services directly.

If you cannot name the owner of an event type, you are not publishing facts. You are publishing rumors.

[![](https://substackcdn.com/image/fetch/$s_!qDK5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13a538fa-310f-40c4-b385-dd274bd444ac_1236x556.png)](https://substackcdn.com/image/fetch/$s_!qDK5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13a538fa-310f-40c4-b385-dd274bd444ac_1236x556.png)

## Broker responsibilities that affect architecture

A broker is not only transport. It changes system behavior in ways that shape design decisions.

### 1) Routing and fan out

The broker decides who gets what message. Topic or exchange design becomes part of architecture, not infrastructure detail.

### 2) Buffering and backpressure

When consumers slow down, messages accumulate. That queue depth is a system signal. Lag means messages waiting in the broker that a consumer has not processed yet. You need policies for lag, retention, and throttling.

### 3) Retry and dead-letter behavior

Delivery failures can be retried or sent to a dead-letter queue (DLQ). Your retry policy defines business outcomes under failure. Blind retries can amplify incidents.

### 4) Delivery semantics

At-most-once, at-least-once, and effectively-once outcomes require different consumer design.

### 5) Contract lifecycle pressure

Once multiple teams consume an event, schema changes become governance work. Versioning strategy is mandatory.

## Delivery semantics and consumer design

Pub sub with a broker usually converges to this rule:

- assume duplicates
- make consumers idempotent
- preserve enough metadata to detect replay and recover safely

[![](https://substackcdn.com/image/fetch/$s_!2Z9S!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd48cdf15-9e4c-4492-90f7-d12d85b4e565_2266x1422.png)](https://substackcdn.com/image/fetch/$s_!2Z9S!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd48cdf15-9e4c-4492-90f7-d12d85b4e565_2266x1422.png)

If your consumer cannot answer “have I processed this message id already,” you do not have reliable pub sub behavior.

## Event contract design

A broker only moves bytes. Meaning lives in contracts.

A stable event contract needs at minimum:

- `messageId`for dedupe
- `eventType`with explicit version
- `occurredAt`to reason about timelines
- domain identifiers used by consumers for partitioning and correlation

Naming is architecture.

- Good: `order.placed.v1`
- Bad: `processOrderNow`

The first is a fact. The second is a remote command disguised as an event.

## Architecture impact in real systems

Pub sub with brokers changes architecture at four levels.

### Team boundaries

Teams can evolve consumers independently as long as contracts stay stable. This reduces release coupling and coordination overhead.

### Data ownership

The publisher owns event truth. Consumers own their local projections. Shared read databases become less necessary.

### Reliability model

Recovery shifts from synchronous retry chains to replay, redrive, and idempotent reprocessing. This is healthier for resilience but heavier operationally.

### Observability model

You need end-to-end tracing across asynchronous hops, plus broker metrics:

- queue depth or topic lag
- consumer lag per group
- retry count and dead-letter rate
- publish failure rate

If you only monitor API latency, you will miss the real failure modes.

## RabbitMQ style pub/sub versus log brokers

Queue-centric and log-centric brokers can both support pub sub, but they push different default behaviors.

Queue-centric posture (for example RabbitMQ):

- optimized for work distribution and ack flow
- operational focus on queue health and routing behavior
- strong fit when each message is mainly work to be done

Log-centric posture (for example Kafka in pub-sub usage):

- optimized for retained history and offset-based consumption
- operational focus on lag, partitioning, and replay
- strong fit when event history is a product asset

Your architecture choice should follow recovery needs, not tool familiarity.

## When pub sub with a broker is the wrong move

Do not force pub sub when you actually need:

- strict request-response interactions with immediate user feedback
- strongly consistent multi-step workflows with one transactional boundary
- very small systems where operational overhead outweighs decoupling value

Use the simplest mechanism that satisfies invariants and operational constraints.

## Decision framework

Before adopting brokered pub sub, answer this checklist:

- Which business facts are worth publishing.
- Which team owns each event type.
- What delivery guarantee you expect from transport.
- What idempotency boundary each consumer enforces.
- How you version contracts without breaking consumers.
- What replay strategy you need for incidents and backfills.
- Which metrics and alerts indicate early drift.

If these answers are vague, do not scale event traffic yet.

## Conclusions

Pub sub with a broker is not about adding asynchronous technology. It is about changing the coordination model of your system.

Done well, it reduces coupling and improves resilience. Done badly, it creates invisible failures and contract chaos.

The practical standard is simple: clear event ownership, explicit delivery assumptions, idempotent consumers, and observable broker behavior.

That baseline is the difference between event driven architecture as discipline and event driven architecture as noise.

## References

- Bellemare, Adam. *Building Event-Driven Microservices*.
- Fowler, Martin. *What do you mean by “Event-Driven”?*. [https://martinfowler.com/articles/201701-event-driven.html](https://martinfowler.com/articles/201701-event-driven.html)
- Kleppmann, Martin. *Designing Data-Intensive Applications*.
- Richardson, Chris. *Microservices Patterns*.
