---
title: "Event-Driven Architecture introduction"
requested_url: "https://emmanuelvalverderamos.substack.com/p/event-driven-architecture-from-zero"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/event-driven-architecture-from-zero"
substack_post_id: 188437395
retrieved_at: "2026-04-18T07:57:14.104Z"
---
# Event-Driven Architecture introduction

## Context

Do you want teams to move without waiting on each other.

Event-driven architecture grew as a response to brittle synchronous chains. You replace tight calls with durable facts so each service can move at its own pace.

This is not “async everywhere”. It is “facts first, reactions later”. Decide which fact is worth broadcasting.

Think of it like publishing a city traffic report instead of calling every driver. Pick the report you want to trust.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### The problem

Coordination becomes a tax when many services and owners must change together.

A synchronous chain fails in the middle and forces humans to stitch it back together. Do you want your recovery plan to live in people or in code. Move the recovery into code.

When you switch to events, you trade direct control for new failure modes: missing events, duplicates, and replayed history. Plan for those failures, do not deny them.

### Constraints and tradeoffs

Messaging systems rarely give you exactly-once delivery end to end, and you must design for that.

> A message broker should ideally deliver each message only once, but guaranteeing exactly-once messaging is usually too costly.

> - Chris Richardson, Microservices Patterns, p. 125

If you want atomicity across systems, two-phase commit exists, but it is heavy and couples infrastructure.

> If you want to make sure that several different systems either commit or abort together, two-phase commit can help.

> - Martin Kleppmann, Designing Data-Intensive Applications, p. 456

So the tradeoff is clear. You accept at-least-once delivery and build idempotent handling so outcomes remain stable. Decide the guarantee you will own.

### Quote anchor from the Quotes collection

> Attempting to maximize utilization is a self-defeating process. Optimal utilization can be achieved only by concentrating on flow.

> - Mary Poppendieck

Event-driven systems work when flow is explicit and recoverable. Queue depth, lag, retries, and replay paths are flow constraints, not implementation details.

## The solution

### The core idea in one line

Treat events as facts that already happened and let services react, not as commands disguised as events.

### The introduction to the example

We use a small Order flow to make reliability decisions explicit before infrastructure complexity enters the conversation.

OrderService creates a domain event, maps it to an integration event, and publishes to an at-least-once event bus. NotificationService consumes it and uses an inbox to ignore duplicates. A simple event log lets us replay. Keep it simple, then scale it.

Here is the flow at a glance.

[![](https://substackcdn.com/image/fetch/$s_!ZcuM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faae27a30-65b4-40e9-ad43-69f5e246ef59_2392x386.png)](https://substackcdn.com/image/fetch/$s_!ZcuM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faae27a30-65b4-40e9-ad43-69f5e246ef59_2392x386.png)

Here is the same flow in time.

[![](https://substackcdn.com/image/fetch/$s_!XLAY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3280c1f5-3a08-4a44-b3fa-fca4600a0727_2812x822.png)](https://substackcdn.com/image/fetch/$s_!XLAY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3280c1f5-3a08-4a44-b3fa-fca4600a0727_2812x822.png)

### The example

This path is deliberate. Each step removes one failure mode without pretending the problem is solved forever. Follow the steps in order.

#### Step 1: Separate commands, events, and queries

A command is a request to do something. An event is a record of something that happened. A query is a request for information. Not a command, but a fact.

If it can fail validation, it is a command. If it represents history, it is an event. Name them accordingly.

Checkpoint: if you cannot tell which is which, your system will drift. Label each message type now.

#### Step 2: Choose the event pattern you actually mean

Do you mean event notification, event-carried state transfer, event sourcing, or CQRS. They are not the same. For those at home:

- event notification means a small signal, “something changed”
- event-carried state transfer means sending enough state so consumers can update locally
- event sourcing means events are the write-side source of truth
- CQRS (Command Query Responsibility Segregation) means separate write and read models

Martin Fowler points out that people use the word “event” to mean different patterns, which creates confusion.

> “The biggest outcome of the summit was recognizing that when people talk about “events”, they actually mean some quite different things.”

> - Martin Fowler

Event notification is a doorbell. Event-carried state transfer is the full receipt. Decide which doorbell you are building.

> “Event notification is nice because it implies a low level of coupling, and is pretty simple to set up.”

> - Martin Fowler

Write the chosen pattern at the top of the design and stick to it.

#### Step 3: Use the right pattern name

Observer is in-process. Pub-Sub is distributed. CQS is a rule about separating commands and queries.

If you call everything Pub-Sub, you hide failure modes and mislead your team. Name the pattern before you design the reliability.

Checkpoint: if it does not cross a boundary, it is Observer, not Pub-Sub.

#### Step 4: Name the boundary and the owner of the fact

An event is only a fact if it has an owner. If two services can emit the same fact, it is not a fact, it is a rumor.

Pick one owner for each event type and make that responsibility explicit. Write it down.

Checkpoint: if you cannot name the owner, you are not ready to publish.

#### Step 5: Create a domain event first

Domain events describe what happened inside a bounded context. Integration events describe what you share outside.

In the sample, the domain event is small and owned by `OrderService`.

```csharp
public sealed record OrderPlaced(

    OrderId OrderId,

    CustomerId CustomerId,

    Money Total,

    DateTime OccurredUtc

);
```

Keep the domain event focused on your model, not on downstream needs. Protect the boundary.

#### Step 6: Map to an integration event with a name and version

Integration events are contracts. They must be explicit and stable.

We map the domain event to an integration event and assign a versioned message type.

```csharp
public sealed record OrderPlacedIntegrationEvent(

    MessageId MessageId,

    OrderId OrderId,

    CustomerId CustomerId,

    Money Total,

    DateTime OccurredUtc

) : IntegrationEvent(MessageId, OccurredUtc)

{

    public override string MessageType =&gt; “order.placed.v1”;

}
```

The workflow makes the boundary explicit.

```csharp

public async Task PlaceOrderAsync(CustomerId customerId, Money total, CancellationToken ct)

{

    var domainEvent = _orderService.PlaceOrder(customerId, total);

    var integrationEvent = _mapper.ToIntegrationEvent(domainEvent);

    await _publisher.PublishAsync(integrationEvent, ct);

}
```

If the name reads like a command, you are leaking control into a fact. Fix the name.

#### Step 7: Include the minimum contract fields

At minimum you need a message id, a type, and the occurrence time.

Without a message id you cannot deduplicate. Without a type you cannot route. Without time you cannot reason about ordering.

Checkpoint: if any of these are missing, stop and add them.

#### Step 8: Accept at-least-once delivery as the default

Most brokers give you at-least-once in failure scenarios. Exactly-once across systems is expensive.

Design as if duplicates are normal. That is the discipline that keeps you safe.

#### Step 9: Make handlers idempotent with an inbox

If a duplicate arrives, the handler must do nothing, not do it twice.

> If the application logic that processes messages is idempotent, then duplicate messages are harmless.

> - Chris Richardson, Microservices Patterns, p. 126

The inbox is the fence.

```csharp
if (!_inbox.TryMarkProcessed(integrationEvent.MessageId))

{

    _logger.LogInformation(

        “Duplicate ignored for message id {MessageId}.”,

        integrationEvent.MessageId.Value);

    return Task.CompletedTask;

}
```

If you cannot afford a duplicate side effect, you cannot skip this step.

#### Step 10: Publish reliably with an outbox

When you must keep a fact, write it inside the same database transaction as your business change.

> An outbox table contains notable changes made to the internal data of a data store, with each significant update stored as its own row.

> - Adam Bellemare, Building Event-Driven Microservices, p. 82

Decide whether you need an outbox now or can defer it with a clear plan.

#### Step 11: Decide how replay will work

Replays are normal in streaming systems and during recovery. If replay breaks state, you have not built a resilient system.

In the sample, the event log replays all events so we can test idempotency. Use it to prove your safety.

#### Step 12: Choose your ordering strategy

Ordering is only guaranteed within a partition, not across the whole system. For those at home, a partition is one ordered slice of the broker log. You get stable order inside that slice, not across all slices.

If ordering matters, partition by the aggregate id, like OrderId, so related events stay together. If it does not matter, avoid pretending it does.

#### Step 13: Pick the broker model that matches your recovery plan

RabbitMQ is strong at work distribution. Kafka is strong at durable replay.

Not a preference, but a recovery model. Choose the model that matches your reality.

#### Step 14: Version contracts deliberately

Version your message types and evolve them in parallel.

Run v1 and v2 together until consumers move. Do not break clients by surprise.

Checkpoint: if you cannot support two versions at once, your evolution plan is weak.

#### Step 15: Build a retry and backoff policy

Retries without backoff turn glitches into outages. Use exponential backoff with jitter and a hard cap.

When a message keeps failing, move it to a dead letter store and alert. The goal is visibility, not endless retries.

Decide your backoff and dead letter policy before production.

#### Step 16: Model the business before you wire it

If you do not know your event flow, you will build the wrong system.

Run a EventStorming session to surface the real business events before you lock in the architecture.

#### Step 17: Slice the flow with Event Modeling

Event Modeling turns the flow into command, event, read model slices. It forces precision.

If you cannot show the slice, you do not know the system. Draw it.

#### Step 18: Use CQRS when read and write needs diverge

CQRS (Command Query Responsibility Segregation) is a separation of models, not a requirement of EDA. Use it when read needs and write needs are truly different.

If you do not have that divergence, keep one model and move on.

#### Step 19: Measure the system, not just the code

At minimum, track outbox lag, publish error rate, inbox duplicate rate, and consumer lag.

If you do not measure these, you only see the system when it breaks. Decide what you will alert on.

#### Step 20: Run the sample end to end

Run the sample and watch duplicates get ignored and replays stay harmless. This is how you validate the guarantees, not just the diagram.

## Conclusions

[![](https://substackcdn.com/image/fetch/$s_!8MMY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93f49047-bdf8-43bf-9db7-2fb6715a5805_6207x3875.png)](https://substackcdn.com/image/fetch/$s_!8MMY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93f49047-bdf8-43bf-9db7-2fb6715a5805_6207x3875.png)

Event-driven architecture is a commitment to facts and reactions, not a shortcut to “async everything”.

The system becomes resilient only when you accept at-least-once delivery and design for idempotent handling. That is the real discipline, not the tooling.

Your biggest risk is confusing patterns. Event notification, state transfer, event sourcing, and CQRS are different choices. If you mix them without knowledge, you will pay for it. Decide which you mean.

If it fits your context, the systemic impact is fewer hidden dependencies and clearer ownership boundaries. That makes recovery mechanical instead of heroic.

If it fits your context, team health improves because on call incidents become predictable, not dramatic. Choose the practices that keep people calm.

This article is the fundamentals anchor. Broker operating models, pub-sub versus streaming semantics, and architecture impact are expanded in dedicated follow-up articles.

## References

- Richardson, Chris. *Microservices Patterns*.
- Bellemare, Adam. *Building Event-Driven Microservices*.
- Kleppmann, Martin. *Designing Data-Intensive Applications*.
- Brandolini, Alberto. *Introducing EventStorming*.
- Dilger, Martin. *Understanding Eventsourcing: Planning and Implementing Scalable Systems with Event Modeling and Event Sourcing*.
- Fowler, Martin. *What do you mean by “Event-Driven”?*. [https://martinfowler.com/articles/201701-event-driven.html](https://martinfowler.com/articles/201701-event-driven.html)
