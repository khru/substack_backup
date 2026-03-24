---
title: "ACID, properly understood: transactions as the engine of correctness"
requested_url: "https://emmanuelvalverderamos.substack.com/p/acid-properly-understood-transactions"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/acid-properly-understood-transactions"
substack_post_id: 188432489
retrieved_at: "2026-03-24T08:45:08.838Z"
---
# ACID, properly understood: transactions as the engine of correctness

## History

Do you trust a system that only works when the world behaves.

Most engineers meet ACID as a slogan. “Our database is ACID compliant” shows up in slide decks as if it were a single on or off switch. That framing hides the real job ACID does.

ACID is not about a database being safe, but about preserving invariants while the world is actively trying to break them. Concurrency, partial failures, retries, node crashes, process pauses, disk quirks, and humans pushing deploy at 3 a.m. ACID is the promise set that lets you write rules and trust that those rules survive all of that.

If you start from zero and follow the thread, you end up in deep machinery: logs, locks, MVCC (Multi-Version Concurrency Control), serializability theory, recovery algorithms, distributed commit protocols, sagas, outbox patterns, and the boundary between what a database can guarantee and what only the application can guarantee.

Use that contrast, not a slogan, as the anchor for everything that follows.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## The problem

Imagine a bank transfer.

- debit account A
- credit account B
- record a ledger entry
- enforce “balance never goes negative”

Now add reality.

- two transfers run at the same time
- the process crashes after debiting A but before crediting B
- the client times out and retries
- the primary node fails right after replying “commit ok”
- a read replica is behind
- a second service consumes an event and writes to a search index

If you cannot state what happens in these cases, you do not have a system, you have vibes.

ACID is the difference between “I hope it works” and “I can explain exactly what must be true after any sequence of failures and retries.”

Write the failure cases down before you claim correctness.

## Constraints and tradeoffs

Correctness has a cost. Stronger guarantees usually reduce concurrency or add coordination. You accept that cost when the invariant is worth it, and you reduce it when the invariant can be relaxed.

ACID is not the only tool. It is the base tool. The rest of this article shows you where it is enough and where you must build on top of it.

Decide which invariants deserve the cost before you choose the guarantees.

### Quote anchor from the Quotes collection

> “If you can get today’s work done today, but you do it in such a way that you can’t possibly get tomorrow’s work done tomorrow, then you lose.”

> - Martin Fowler

ACID decisions follow this exact warning. If you optimize short-term throughput by weakening boundaries you cannot recover, tomorrow’s incidents become expensive and hard to explain.

## ACID as a product requirement

Choosing ACID or relaxing it is primarily a product decision constrained by customer expectations and business risk. It is only secondarily a database choice.

Technically this means you are choosing transaction boundaries and isolation levels. Product wise this protects trust, refunds, and contractual promises. Operationally this costs coordination, contention, and recovery complexity.

A banking transfer and a social media like counter are not the same product. The transfer demands strict invariants and auditability. The like counter can tolerate eventual correction and lower isolation if the user experience is designed for it.

The core question is not “is ACID supported.” The core question is “what does the customer expect to be true after failure, retry, or delay.”

State the customer expectation in plain language before you choose a guarantee.

## Introduction

[![](https://substackcdn.com/image/fetch/$s_!3AXU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ac99a3c-c0b2-4c9a-a174-64ae4b8281c1_8850x3373.png)](https://substackcdn.com/image/fetch/$s_!3AXU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ac99a3c-c0b2-4c9a-a174-64ae4b8281c1_8850x3373.png)

ACID stands for:

- Atomicity: all of a transaction happens, or none of it does.
- Consistency: every committed transaction preserves the rules of the system.
- Isolation: concurrent transactions do not step on each other in ways that violate those rules.
- Durability: once committed, the effects survive failures.

Those four words sound obvious. The trap is that each word hides formal definitions, implementation tricks, and tradeoffs. Worse, different systems reuse the same words to mean different things.

This article follows a strict order.

- What a transaction is and why it exists.
- Where ACID comes from historically.
- Each property, with failure modes and mechanisms.
- How ACID is used in real systems today, including microservices and event driven architectures.
- A practical playbook: when to insist on ACID, where to draw boundaries, and how to build correctness when global ACID is not available.

Use this order as your map, and do not skip steps.

## The aha moment

A transaction is a promise that your system keeps its rules even when the timeline is hostile.

If you cannot state what must be true after a crash or retry, you have no correctness story. ACID is the tool that turns that story into a contract.

Write the contract before you write the code.

## Before ACID: the transaction as the unit of correctness

A transaction is a sequence of reads and writes that the system treats as one logical operation, with two possible outcomes:

- commit: changes become visible as a unit
- rollback: changes are discarded as if they never happened

Visualize it as a state machine.

[![](https://substackcdn.com/image/fetch/$s_!BQbu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfeffd0a-91b7-491a-801b-a88bf9bd8d52_1309x348.png)](https://substackcdn.com/image/fetch/$s_!BQbu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfeffd0a-91b7-491a-801b-a88bf9bd8d52_1309x348.png)

Two concepts appear early and keep returning.

- Invariant: a rule that must always hold in committed state. Examples: balance never negative, inventory never negative, every order has exactly one customer.
- Schedule: the interleaving of operations from multiple transactions. Most weird bugs are really bad schedules.

Carry these two terms forward. You will use them in every letter of ACID.

## Historical context: where ACID comes from

### Records, ledgers, and shared truth under concurrency

It is tempting to tell a clean origin story where databases come from banks. The reality is more interesting.

Banks helped forge the transactional mindset because the core workflow is a ledger. If you debit one place, you must credit another, and you must be able to prove what happened after a crash or a dispute. That made correctness non negotiable and failures immediately expensive and visible.

But banking was not alone. Early pressures came from industries that needed real-time updates, high concurrency, and strong recovery.

- aerospace and manufacturing
- airlines and reservations
- utilities and telecom
- finance and trading

The point is not “who invented it first.” The point is why transactions became inevitable. The world wanted interactive, multi-user, always-on record keeping where mistakes were catastrophic.

### From file processing to DBMS

Early systems stored state in application-owned files. That model broke fast.

- each application reinvented integrity rules
- concurrency control was fragile and inconsistent
- recovery after crashes was often manual and error prone

Once systems became interactive, the question changed.

If the machine dies at the worst possible moment, can you recover to a state that is still correct.

That question demands an abstraction that can draw a hard line in history. Transactions do exactly that. Commit is a durable boundary. Rollback is a controlled return to a known good state.

### The rise of OLTP

By the 1960s and 1970s, online transaction processing became the dominant pattern. Lots of short requests, each requiring a clean all-or-nothing outcome.

Two historical anchor points are worth remembering.

- Airline reservation systems were a forcing function. SABRE is often cited because it operationalized large-scale, real-time shared inventory updates.
- Transaction processing monitors became a layer that made OLTP feasible. IBM CICS is a classic example.

A retrospective on Jim Gray’s work notes that he defined and developed the fundamental concepts and techniques that underlie online transaction processing systems.

This is the intellectual pre history of what later gets condensed into ACID.

### IMS and CICS: transaction platforms, not just databases

Early “database systems” were often inseparable from transaction execution and recovery machinery.

- IBM IMS illustrates the pre-relational world: hierarchical storage, strong operational tooling, and transaction-style execution.
- CICS explains why “transaction” became first-class even outside relational databases.

Transaction processing was forged in industries where shared mutable state and failure recovery were unavoidable, and banking became one of the clearest, highest-stakes homes for the model.

### The relational model and algebra

By the late 1960s, database models existed, but they were navigational. The application had to know paths through the data structure. That coupled code to layout and access patterns.

In 1970, Edgar Codd published the relational model. The important point is not “tables are nice.” It is this.

The relational model separated what data means from how it is stored, and it did so with mathematics.

Relational algebra matters because it made two things possible.

- A clean, composable language of operations over relations.
- A foundation for query optimization: rewrite expressions while preserving meaning, then choose efficient physical strategies.

A compact mental model looks like this.

[![](https://substackcdn.com/image/fetch/$s_!hhze!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa76d8087-30b9-445b-ace9-32963b881454_552x1628.png)](https://substackcdn.com/image/fetch/$s_!hhze!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa76d8087-30b9-445b-ace9-32963b881454_552x1628.png)

Relational algebra in the simplest story:

- Selection filters rows by a predicate.
- Projection chooses columns.
- Join combines rows from two relations based on matching keys.

[![](https://substackcdn.com/image/fetch/$s_!R2DX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2aae41d2-b23b-4980-a7b8-07b34c58052d_1821x140.png)](https://substackcdn.com/image/fetch/$s_!R2DX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2aae41d2-b23b-4980-a7b8-07b34c58052d_1821x140.png)

Relational algebra belongs in an ACID history because it changed what people expected from a database. Once you have declarative queries and formal semantics, it becomes reasonable to demand principled concurrency control, integrity constraints, and crash recovery as properties of the data system, not ad hoc application behavior.

### The acronym ACID

[![](https://substackcdn.com/image/fetch/$s_!aznf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e68e178-3553-4d30-bb27-23276205f0e8_11652x1326.png)](https://substackcdn.com/image/fetch/$s_!aznf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e68e178-3553-4d30-bb27-23276205f0e8_11652x1326.png)

The acronym came later. In 1983, Theo Harder and Andreas Reuter coined ACID in a survey on transaction-oriented recovery. The ideas behind it were already in the air, but the acronym made the promise set memorable and discussable.

One note that still causes confusion. The “C” is the least self contained letter because it depends on what invariants you actually care about. That is why consistency is often the most abused word in the acronym.

Treat the history as proof that correctness is an economic choice, not a fashion.

## Atomicity: commit or clean abort

Atomicity is often explained as “either everything happens or nothing happens.” In practice, that is shorthand for two stronger requirements.

- Abortability: if a transaction fails, every partial effect is undone.
- Atomic visibility: other transactions never see a half finished result.

### What atomicity protects you from

- process crash in the middle of a multi step update
- constraint violation halfway through a batch of writes
- deadlock victim rollback
- client retry after timeout while the server continues

Atomicity is why a transfer does not leak money when you crash at the wrong time.

### Why customers care

If a checkout charges a card but does not create an order, the customer sees a charge without a product. That destroys trust, creates refund cost, and triggers support load.

Atomicity makes the user experience reliable. Either the order exists or it does not. There is no partial success screen that the customer has to decode.

### A real world rollback: ATM cash you forgot to take

Imagine you withdraw cash at an ATM and forget to take the banknotes. Many ATMs use cash retract. If you do not take the cash within a short window, the machine pulls it back in. The goal is that you are not left debited for money you never received.

In transaction terms, the operation did not complete successfully, so the system performs the equivalent of a rollback.

### How atomicity is implemented on one node

Most systems combine:

- write-ahead logging (WAL), record intended changes in an append-only log before data pages
- undo information, enough to roll back uncommitted writes
- a commit record, a single point in the log that means “this transaction is committed”

Conceptually:

[![](https://substackcdn.com/image/fetch/$s_!pT6q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f49f1dc-29f6-4eff-a582-b2069a2f6175_946x1276.png)](https://substackcdn.com/image/fetch/$s_!pT6q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f49f1dc-29f6-4eff-a582-b2069a2f6175_946x1276.png)

The separation is the key. You can commit quickly by forcing the log, and apply changes to data pages later.

### Atomicity across multiple systems

The moment a transaction spans multiple independent systems, atomicity becomes a coordination problem. Either everyone commits or everyone aborts.

That is the atomic commit problem, and it leads to protocols like two phase commit.

A useful sentence to keep in mind: ensuring that multiple systems either all succeed or all fail is the atomic commit problem.

If your operation crosses systems, choose a commit protocol or redesign the workflow so the invariant does not depend on a global transaction.

## Consistency: the most overloaded letter

Consistency is where most discussions go off the rails. There are at least three different “consistencies” people mix.

- ACID consistency: every committed transaction preserves the system invariants.
- Replication consistency: how replicas converge and what reads can see.
- CAP consistency: typically linearizability, or behaves like a single up to date copy.

In ACID, consistency is about invariants, not replication.

### What the database can enforce

A database can help enforce invariants through:

- schema constraints, such as NOT NULL, CHECK, FOREIGN KEY, UNIQUE
- triggers
- transactional semantics for read modify write

But the database cannot invent your business rules. If your invariant is “an order cannot ship before payment is authorized,” that is not a schema constraint by default. That is application logic and process.

### The correct way to think about C

The application defines invariants. The transaction mechanism preserves them under concurrency and failure.

This framing matters because it tells you what to test and what to review.

- invariants live in code and schema
- transactions are the enforcement boundary
- “ACID compliant” without explicit invariants is meaningless

### Why customers care

Consistency is a product promise. If your terms say “you can never overspend your balance,” then that rule is part of the customer contract. If it fails, you have compliance risk, audit risk, and trust loss.

Technically this means you must encode the invariant and guard it with transactions. Product wise this protects contractual promises. Operationally this costs stronger constraints and stricter concurrency control.

List your invariants explicitly, then encode them where the transaction can enforce them.

## Isolation: concurrency without chaos

Isolation is the hardest letter because it is simultaneously:

- a formal property, serializability
- an engineering problem, locks vs MVCC vs optimistic validation
- a product surface, isolation levels
- a performance tradeoff, contention vs throughput

### Why isolation exists

If two transactions run at the same time, their operations interleave. Without isolation, you can observe partial results and violate invariants even if each transaction is correct in isolation.

Concurrency is the path to scale, but it is also the path to unintended interleavings. That is why isolation exists.

### Classic anomalies you should know

For those at home, an anomaly is a wrong business outcome caused by a valid looking interleaving of concurrent transactions. If you see the word dirty, read it as uncommitted. A dirty value is a value written by a transaction that could still roll back and disappear.

- dirty write: T1 overwrites data that T2 wrote but has not committed yet
- dirty read: T1 reads data that T2 wrote but has not committed yet
- lost update: two transactions read the same value and one update erases the other
- read skew: a transaction reads an inconsistent snapshot across related rows
- write skew: two transactions make decisions on the same snapshot and both commit, violating an invariant
- phantom: a predicate query returns a different row set inside the same transaction

Real world example, flash sale with one last unit:

- checkout A reads stock = 1
- checkout B reads stock = 1
- both transactions decrement and commit
- both orders are confirmed even though only one unit existed

That is a lost update anomaly. You did not just lose a number. You created an oversell incident that support and finance must unwind.

[![](https://substackcdn.com/image/fetch/$s_!M1kO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7aebb4d2-e1f5-4d8c-93d0-676448e54bf7_1770x1016.png)](https://substackcdn.com/image/fetch/$s_!M1kO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7aebb4d2-e1f5-4d8c-93d0-676448e54bf7_1770x1016.png)

### The gold standard: serializable isolation

Serializable means the outcome is equivalent to some serial order of transactions.

That is a clean definition because it exactly matches how you reason about invariants. It is as if transactions ran one at a time.

### Why systems offer weaker isolation levels

Serializable isolation can be expensive under high contention or long running transactions. So many databases expose weaker levels. The ANSI SQL definitions are based on a limited set of phenomena, and there is a well known critique showing those phenomena do not fully characterize real behavior, especially with multiversion schemes.

### How isolation is implemented

There are three major families. You should be able to map any database you use onto one of these.

#### 1) Two phase locking

- transactions take locks
- once a transaction releases a lock, it cannot acquire new ones
- serializability comes from lock discipline

Pros:

- simple model, strong guarantee

Cons:

- blocking, deadlocks, poor tail latency under contention

#### 2) MVCC and snapshot isolation

MVCC means Multi-Version Concurrency Control. Instead of mutating one in-place row version, the database keeps version history so readers can see a stable snapshot while writers create newer versions.

A simplified picture:

[![](https://substackcdn.com/image/fetch/$s_!9U-q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1bd7a6ad-17ea-4606-aeb2-42d86ac9f869_867x596.png)](https://substackcdn.com/image/fetch/$s_!9U-q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1bd7a6ad-17ea-4606-aeb2-42d86ac9f869_867x596.png)

Snapshot isolation feels good because:

- reads do not block writes and writes do not block reads
- many anomalies disappear

But snapshot isolation is not automatically serializable. The canonical footgun is write skew.

#### 3) Serializable snapshot isolation and optimistic validation

SSI means Serializable Snapshot Isolation. It keeps much of snapshot-style performance while detecting dangerous structures that would lead to non-serializable outcomes, aborting one transaction when needed.

This is a practical “best of both worlds” approach when implemented well, but it comes with its own tuning and abort behavior.

### Isolation in practice: the only question that matters

When you choose an isolation level, do not ask “is it fast.”

Ask:

Which anomalies can still happen, and can they violate my invariants.

If yes, either:

- raise isolation
- rewrite the transaction to lock or materialize the right decision points
- move the invariant into a single row or a single authority
- redesign the workflow, saga, reservation, escrow

Isolation is not a checkbox. It is a contract you sign with your future self.

### Why customers care

Isolation prevents double booking, overselling, and phantom charges. These are not just bugs. They are broken promises that damage trust and increase support load.

Technically this means you choose an isolation level that prevents anomalies that break your invariants. Product wise this protects fairness and availability. Operationally this costs contention and sometimes aborts.

Choose isolation by the anomalies you can tolerate, not by the default setting.

## Durability: surviving crashes is a system problem

Durability means once a transaction commits, its effects persist even if the process or machine crashes.

Durability is usually implemented with:

- WAL forced to stable storage at commit
- checkpoints to bound recovery time
- careful ordering rules, log first then data pages
- recovery algorithms that replay history to a consistent point

Durability gets subtle when you include:

- disk write caches
- filesystems and fsync semantics
- replication and failover

### Durability with replication

If you commit on a primary and replicate asynchronously, a failover can lose committed transactions from the old primary. In that setup, durability is conditional. It depends on whether the commit made it to the new authority.

If you need durability that survives node loss, you typically need synchronous replication of the commit decision, not just local fsync.

### Why customers care

Durability is the promise behind every success screen. If you show “payment complete” and then lose the record, you created a dispute and a reputational hit.

Technically this means log force, careful ordering, and replication guarantees. Product wise this protects trust and dispute resolution. Operationally this costs latency and storage.

Decide which success screens must survive node loss, then choose the replication mode to match.

## What problems ACID solves today

Even in modern systems, you still run into the same classes of failure.

ACID solves:

- invariant preservation under concurrency
- crash safety
- retry safety
- operational sanity

What ACID does not solve by itself:

- correctness across multiple independent systems without a commit protocol
- distributed consensus problems
- CAP consistency under partitions
- semantic correctness if your invariant is wrong

Use this list to decide where ACID ends and where other patterns begin.

## How ACID is used now

### Then: monolith plus relational database

The classic architecture was straightforward:

- one database
- one transaction boundary per business operation
- strong guarantees inside that boundary

In that world, ACID is the center of gravity. You build invariants into schema and transactional code.

### Now: distributed systems and boundaries

Modern systems often look like this:

- many services
- each service has its own data store
- communication is over the network
- events are involved

In that world:

- you can still have strong ACID inside a service database
- global ACID across services is possible, but often operationally painful
- correctness becomes a composition problem

Some distributed databases do provide strong transactional semantics across partitions using tightly integrated protocols and time or ordering mechanisms. This works best when the whole system is designed as one database, not as heterogeneous components glued together.

Draw explicit transaction boundaries for each service before you argue about global guarantees.

## A real example: checkout flow, monolith vs microservices

Let’s use a concrete workflow.

- create order
- reserve inventory
- authorize payment
- confirm order
- emit events for shipping, email, analytics

### The monolith version

In a monolith with one relational database, you can do:

- transaction starts
- insert order row
- decrement inventory
- insert payment authorization record
- commit

If any step fails, rollback restores invariants.

### The microservices version

Now split into services:

- Order service with its own DB
- Inventory service with its own DB
- Payment service with its own DB
- Message broker for events

The naive approach is dual writes.

- write to DB
- publish event

Dual writes break in exactly the way you fear. One write succeeds and the other fails.

A clean visual:

[![](https://substackcdn.com/image/fetch/$s_!RCV_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fdf9c8c-baac-48ac-a6c5-1b10d3e99412_1385x386.png)](https://substackcdn.com/image/fetch/$s_!RCV_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fdf9c8c-baac-48ac-a6c5-1b10d3e99412_1385x386.png)

If the Order service writes to its DB and crashes before publishing, downstream services never see the order. If it publishes and crashes before committing, downstream sees a phantom order.

### The practical solution: transactional outbox and idempotent consumers

The outbox pattern makes the database transaction the source of truth for what happened, and turns event publication into a reliable step.

Minimal model:

- In one DB transaction, update internal state and append an outbox row.
- A separate publisher reads outbox rows and publishes to the broker.
- Consumers are idempotent because delivery is typically at least once.

[![](https://substackcdn.com/image/fetch/$s_!QOCK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F871b8970-463c-4df0-a623-f45ea0f04f71_641x1030.png)](https://substackcdn.com/image/fetch/$s_!QOCK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F871b8970-463c-4df0-a623-f45ea0f04f71_641x1030.png)

Both the internal table updates and the outbox updates must be bundled into a single transaction.

This does not give you global ACID. It gives you local ACID plus reliable propagation, which is how most event driven systems stay sane at scale.

### Coordinating the workflow: saga

A saga is a sequence of local transactions with compensating actions if a later step fails.

For checkout:

- T1: create order as pending
- T2: reserve items
- T3: authorize payment
- T4: mark confirmed
- if T3 fails, release inventory and cancel order

Orchestration view:

[![](https://substackcdn.com/image/fetch/$s_!-yta!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f081417-31a6-4252-8da3-c4aacfabe658_1327x1388.png)](https://substackcdn.com/image/fetch/$s_!-yta!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f081417-31a6-4252-8da3-c4aacfabe658_1327x1388.png)

This is life beyond distributed transactions in practice. Correctness is achieved through explicit workflow state, compensation, and careful idempotence.

Choose the workflow pattern that matches your failure budget and recovery plan.

## Distributed transactions: when they work, why they are unpopular

Two phase commit exists to give atomicity across multiple participants.

The key problem is blocking. If participants vote yes and the coordinator crashes, they can be stuck in doubt, holding locks and blocking progress until the coordinator recovers.

A mental model of two phase commit:

[![](https://substackcdn.com/image/fetch/$s_!6e5_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cf2f727-9207-4369-bb58-999bf7e60e44_1315x1074.png)](https://substackcdn.com/image/fetch/$s_!6e5_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cf2f727-9207-4369-bb58-999bf7e60e44_1315x1074.png)

Distributed transactions can still be the right choice when:

- participants are part of one tightly integrated system
- latency is acceptable
- operational risk is acceptable
- you cannot tolerate intermediate states that sagas introduce

Across heterogeneous systems, they are often avoided because the failure modes are ugly and the overhead is real.

If you choose 2PC, do it with eyes open and a recovery playbook.

## When not to pay for ACID

There are product contexts where weaker guarantees are acceptable, but only if the product design makes that explicit.

Examples where weaker guarantees can be acceptable:

- social media like counters, where eventual correction is acceptable
- analytics pipelines, where results can be delayed or corrected later
- recommendation systems, where stale data is tolerable

These are only acceptable if you also design for them:

- the UI communicates eventuality or revision
- compensation paths exist for incorrect outcomes
- business metrics tolerate temporary drift

If you relax ACID without these assumptions, you are not trading cost for risk, you are trading trust for surprises.

Make the product assumption explicit before you relax the guarantee.

## Product driven examples

Two examples show how product pressure changes the technical design.

### Banking transfer vs social media like counter

A banking transfer is a contract. The invariant is strict: money cannot disappear or duplicate. That demands strong atomicity, durable commits, and high isolation for balance updates.

A social media like counter is a feedback loop. The invariant is soft: it should be roughly correct and eventually consistent. That can be implemented with weaker isolation and asynchronous correction.

### Inventory reservation vs analytics pipeline

Inventory reservation is a promise to a paying customer. It requires isolation to avoid overselling and atomicity to avoid partial checkout states.

An analytics pipeline can tolerate delay and reprocessing. It can use eventual consistency, compensation, and idempotent writes rather than global transactions.

Match each workflow to the weakest guarantee your users can tolerate, not to the strongest guarantee your database can offer.

## Conclusions

- ACID is not one feature. It is four promises with different mechanisms and costs.
- The C is about invariants. If you do not define invariants, ACID is marketing.
- Isolation is the battleground.
	- know which anomalies your system allows
	- decide if those anomalies can violate your invariants

- Local ACID is easy and massively valuable. Global ACID is possible, but expensive.
- In distributed systems, correctness usually comes from composition.
	- local transactions
	- reliable event publication
	- idempotent consumers
	- sagas for cross service workflows
- If someone claims “we guarantee exactly once” across arbitrary side effects, ask where the atomic commit boundary is.
	- if they cannot point to it, they are hand waving

If you internalize that, you stop debating buzzwords and start designing invariants with explicit enforcement boundaries. That is what being good at ACID actually means.

Apply these points to your next design review and force the invariants into the open.

## Decision framework

Use this checklist to translate product requirements into technical choices.

- What are the explicit invariants, and which ones are contractual promises.
- What is the user visible failure if an invariant breaks.
- What is the acceptable recovery time and acceptable data loss.
- Which operations require atomicity across multiple steps.
- Which anomalies can your product tolerate, and which violate trust.
- What isolation level is required for those invariants.
- Where must durability be synchronous, and where is it acceptable to be conditional.
- Where are transaction boundaries inside a service.
- Where do you need sagas instead of distributed transactions.
- Where do you need outbox and idempotent consumers.
- What is the operational cost of each choice.
- What SLAs and support workflows depend on these guarantees.

Use this with product, engineering, and operations before you commit to a data model.

## References

- Harder, Theo; Reuter, Andreas. *Principles of Transaction Oriented Database Recovery*. [https://www.researchgate.net/publication/200030219_Principles_of_Transaction-Oriented_Database_Recovery](https://www.researchgate.net/publication/200030219_Principles_of_Transaction-Oriented_Database_Recovery)
- Chamberlin, Donald D.; Astrahan, Morton M.; et al. *A History and Evaluation of System R*. [https://www.cs.cmu.edu/~natassa/courses/15-721/papers/p632-chamberlin.pdf](https://www.cs.cmu.edu/~natassa/courses/15-721/papers/p632-chamberlin.pdf)
- Gray, Jim; Reuter, Andreas. *Transaction Processing: Concepts and Techniques*. [https://archive.org/details/transactionproce0000gray](https://archive.org/details/transactionproce0000gray)
- Lindsay, Bruce G. *Jim Gray at IBM: The Transaction Processing Revolution*.
- https://sigmodrecord.org/?download_id=4373&amp;smd_process_download=1
- International Business Machines Corporation. *Information Management System*. [https://www.ibm.com/history/information-management-system](https://www.ibm.com/history/information-management-system)
- International Business Machines Corporation. *History of IMS: Beginnings at NASA*. [https://www.ibm.com/docs/en/zos-basic-skills?topic=now-history-ims-beginnings-nasa](https://www.ibm.com/docs/en/zos-basic-skills?topic=now-history-ims-beginnings-nasa)
- International Business Machines Corporation. *Sabre*. [https://www.ibm.com/history/sabre](https://www.ibm.com/history/sabre)
- Sabre Corporation. *The Sabre Story*. [https://www.sabre.com/files/Sabre-History-rev2017.pdf](https://www.sabre.com/files/Sabre-History-rev2017.pdf)
- Codd, Edgar F. *A Relational Model of Data for Large Shared Data Banks*. [https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf)
- Codd, Edgar F. *A Data Base Sublanguage Founded on the Relational Calculus*. [https://www.gorbachev.am/files/library/dbms/Codd%20-%20Alpha.pdf](https://www.gorbachev.am/files/library/dbms/Codd%20-%20Alpha.pdf)
- Date, C. J. *E. F. Codd and Relational Theory: A Detailed Review*. [https://forum.thethirdmanifesto.com/wp-content/uploads/asgarosforum/985420/about-EFCRT.pdf](https://forum.thethirdmanifesto.com/wp-content/uploads/asgarosforum/985420/about-EFCRT.pdf)
- Berenson, Hal; Bernstein, Philip; Gray, Jim; Melton, Jim; O’Neil, Elizabeth; O’Neil, Patrick. *A Critique of ANSI SQL Isolation Levels*. [https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-95-51.pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-95-51.pdf)
- Mohan, C.; Levine, Frank. *ARIES: A Transaction Recovery Method Supporting Fine Granularity Locking and Partial Rollbacks Using Write Ahead Logging*. [https://web.stanford.edu/class/cs345d-01/rl/aries.pdf](https://web.stanford.edu/class/cs345d-01/rl/aries.pdf)
- Garcia Molina, Hector; Salem, Kenneth. *Sagas*. [https://www.cs.princeton.edu/techreports/1987/070.pdf](https://www.cs.princeton.edu/techreports/1987/070.pdf)
- Helland, Pat. *Life Beyond Distributed Transactions: An Apostate’s Opinion*. [https://www.ics.uci.edu/~cs223/papers/cidr07p15.pdf](https://www.ics.uci.edu/~cs223/papers/cidr07p15.pdf)
- Gilbert, Seth; Lynch, Nancy. *Brewer’s Conjecture and the Feasibility of Consistent, Available, Partition Tolerant Web Services*. [https://www.cs.princeton.edu/courses/archive/spr22/cos418/papers/cap.pdf](https://www.cs.princeton.edu/courses/archive/spr22/cos418/papers/cap.pdf)
- Pritchett, Dan. *Base: An Acid Alternative*. [https://queue.acm.org/detail.cfm?id=1394128](https://queue.acm.org/detail.cfm?id=1394128)
- Corbett, James C.; Dean, Jeffrey; Epstein, Michael; et al. *Spanner: Google’s Globally Distributed Database*. [https://research.google.com/archive/spanner-osdi2012.pdf](https://research.google.com/archive/spanner-osdi2012.pdf)
- Thomson, Alexander; Diamond, Thaddeus; Weng, Shu Chun; Ren, Kun; Shao, Philip; Abadi, Daniel J. *Calvin: Fast Distributed Transactions for Partitioned Database Systems*. [https://cs.yale.edu/homes/thomson/publications/calvin-sigmod12.pdf](https://cs.yale.edu/homes/thomson/publications/calvin-sigmod12.pdf)
- Cahill, Michael J.; Rohm, Uwe; Fekete, Alan. *Serializable Isolation for Snapshot Databases*. [https://people.eecs.berkeley.edu/~kubitron/courses/cs262a-F13/handouts/papers/p729-cahill.pdf](https://people.eecs.berkeley.edu/~kubitron/courses/cs262a-F13/handouts/papers/p729-cahill.pdf)
- Kleppmann, Martin. *Designing Data Intensive Applications*. [https://martin.kleppmann.com/2017/03/27/designing-data-intensive-applications.html](https://martin.kleppmann.com/2017/03/27/designing-data-intensive-applications.html)
- Bellemare, Adam. *Building Event Driven Microservices: Leveraging Organizational Data at Scale*. [https://www.oreilly.com/library/view/building-event-driven-microservices/9781492057888/](https://www.oreilly.com/library/view/building-event-driven-microservices/9781492057888/)
- Saudi Central Bank. *Time Out Cash Retract on ATMs*. [https://rulebook.sama.gov.sa/en/time-out-cash-retract-atms](https://rulebook.sama.gov.sa/en/time-out-cash-retract-atms)
- Euronet. *Issues Withdrawing Cash*. [https://www.euronetatms.com/issues-withdrawing-cash/](https://www.euronetatms.com/issues-withdrawing-cash/)
- Revolut Bank UAB. *My Cash Withdrawal Was Reverted*. [https://help.revolut.com/en-ES/business/help/making-paymentsbusiness/atm-withdrawals/why-has-my-cash-withdrawal-been-reverted/](https://help.revolut.com/en-ES/business/help/making-paymentsbusiness/atm-withdrawals/why-has-my-cash-withdrawal-been-reverted/)
- Wikipedia. *ACID*. [https://en.wikipedia.org/wiki/ACID](https://en.wikipedia.org/wiki/ACID)
