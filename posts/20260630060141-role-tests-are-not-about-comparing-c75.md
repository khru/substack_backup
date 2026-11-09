Title: Role tests are not about comparing implementations 2

URL Source: http://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75

Final URL: https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75

Published Time: 2026-06-30T06:01:41+00:00

Markdown Content:
This article is a continuation or extension of the article

Following these two points of clarification:

*   Role testing is not contract testing: In the previous article, Javi López mentioned to me that he does not view role testing as contract testing.

*   My friend Adrían Muñoz Gamez gave me feedback that in the previous article Tests should fail for only one reason, for the sake of simplicity, I wrote a test that called `save` and then `findById`, which is not a good or consistent test, since it should fail for only one reason, and that test had two reasons to fail.

Therefore, to clarify these questions and delve deeper into the topic, I have written this article.

[![Image 1](https://substackcdn.com/image/fetch/$s_!7PZL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a63d7a4-2bc0-4acd-857c-a59d62545e3e_1024x559.png)](https://substackcdn.com/image/fetch/$s_!7PZL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a63d7a4-2bc0-4acd-857c-a59d62545e3e_1024x559.png)

Interfaces often give us confidence earlier than they should.

At first, everything looks fine. The interface is clean. One implementation passes its tests. Another is convenient for local development. A third might be useful in tests or in a different runtime context. The compiler is satisfied, the test suite is green, and the boundary appears well designed.

None of those facts proves that every implementation means the same thing by `save` and `findById`.

Consider these two implementations:

`CustomerRows` is a small table gateway used to keep the example focused on repository behaviour rather than database driver calls. Its shape appears later.

Both implement the same method:

A basic test that saves one customer and finds it later can pass for both. But save the same customer id twice and their meanings separate.

The in-memory implementation replaces the previous value. Assuming `id` is a primary key, the PostgreSQL implementation shown above rejects the second insert. One interprets `save` as an upsert. The other interprets it as an insert.

The interface did not prevent the disagreement:

The same structural interface can therefore hide incompatible observable behaviour:

It defines which messages clients can send. It does not define enough of the behaviour clients can rely on.

That is the problem role tests help us examine.

A role test is a reusable suite of behavioural examples for a role. It does not primarily ask whether the in-memory repository behaves like PostgreSQL, or whether a new implementation reproduces every observable detail of an old one.

A role contract asks:

> What must every implementation make true so that clients can safely depend on this role?

Each implementation is checked against the same behavioural specification.

The contract boundary is:

> A role test does not compare implementations with one another. It checks each implementation against the client-visible behavioural contract of the role.

This makes role tests useful in several situations:

*   Keeping an in-memory fake aligned with a production adapter

*   Checking several production adapters that claim the same role

*   Introducing a new Strategy implementation

*   Replacing a library, database adapter, algorithm, or external dependency during a refactor

*   Running an old and a new implementation side by side while clients migrate

There is also an important limit. Passing a finite test suite does not prove complete substitutability. It provides executable evidence for the behaviours represented by those examples. Untested concurrency, durability, performance, security, and failure properties do not become guaranteed merely because the suite is green.

Role tests are therefore both a testing technique and a design technique. They protect known behaviour, expose semantic disagreements, keep test doubles honest, and force vague abstractions to become more precise.

[![Image 2](https://substackcdn.com/image/fetch/$s_!xt9e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9469d067-e73a-4286-86e1-7872a40f2426_1024x559.png)](https://substackcdn.com/image/fetch/$s_!xt9e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9469d067-e73a-4286-86e1-7872a40f2426_1024x559.png)

*   **An interface defines shape, while a role test defines expected behaviour.** A signature can say `save(customer)`, but it cannot fully say what must be true after saving

*   **Role tests do not primarily compare implementations.** They run the same behavioural specification against each implementation

*   **In object-oriented literature, role tests are a form of contract or polymorphic testing.** The name emphasizes that one behavioural contract is reused against every implementation of a role

*   **The role is the reference, not the fake, the database, or the legacy implementation.** When implementations disagree, the team must clarify the contract

*   **Roles are often discovered from the client side.** A client’s needs reveal the messages and responsibilities required from a collaborator

*   **Role tests are valuable during refactors.** An old dependency and its replacement can both be adapted to the same role and checked with the same suite before clients migrate

*   **Role tests keep fakes aligned with real adapters.** A lightweight in-memory implementation should satisfy the same client-visible promises, even though it does not reproduce infrastructure details

*   **Strategy implementations can also have role tests.** The shared suite protects properties common to every valid strategy, or the complete behaviour when a new strategy is intended as a drop-in replacement

*   **Passing the suite is evidence, not a formal proof.** The suite protects only the part of the contract it encodes

*   **Implementation-specific tests still matter.** SQL, filesystem, HTTP, security, performance, and operational concerns need their own tests

*   [The problem with interfaces](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7the-problem-with-interfaces)

*   [What a role test is](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7what-a-role-test-is)

*   [Are role tests contract tests?](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7are-role-tests-contract-tests)

*   [What a role test is not](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7what-a-role-test-is-not)

*   [Roles are discovered from the client side](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7roles-are-discovered-from-the-client-side)

*   [A small example in Kotlin](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7a-small-example-in-kotlin)

*   [The first testing smell: using one role method to arrange another](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7the-first-testing-smell-using-one-role-method-to-arrange-another)

*   [A precise role-test fixture](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7a-precise-role-test-fixture)

*   [Testing two implementations with the same role test](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7testing-two-implementations-with-the-same-role-test)

*   [The missing save contract](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7the-missing-save-contract)

*   [Keeping test doubles aligned with real adapters](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7keeping-test-doubles-aligned-with-real-adapters)

*   [Using role tests to replace a dependency safely](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7using-role-tests-to-replace-a-dependency-safely)

*   [Replacing an OpenAPI-generated client without breaking local clients](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7replacing-an-openapi-generated-client-without-breaking-local-clients)

*   [A Strategy example during a refactor](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7a-strategy-example-during-a-refactor)

*   [Role tests, characterization tests, and differential tests](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7role-tests-characterization-tests-and-differential-tests)

*   [What should go into a role test?](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7what-should-go-into-a-role-test)

*   [What should not go into a role test?](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7what-should-not-go-into-a-role-test)

*   [Role tests and object-oriented design](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7role-tests-and-object-oriented-design)

*   [Common mistakes](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7common-mistakes)

*   [When role tests are worth the cost](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7when-role-tests-are-worth-the-cost)

*   [Conclusion](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7conclusion)

*   [References](https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing-c75?open=false#%C2%A7references)

[![Image 3](https://substackcdn.com/image/fetch/$s_!41CT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ea311c6-9ef7-4ad9-8464-5e0f578b4676_1024x559.png)](https://substackcdn.com/image/fetch/$s_!41CT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ea311c6-9ef7-4ad9-8464-5e0f578b4676_1024x559.png)

Interfaces are useful because they let us name a role without committing every client to one concrete implementation.

They appear around persistence, clocks, payment gateways, event publishers, file systems, external APIs, pricing policies, routing algorithms, feature flags, and other boundaries where substitution matters.

But an interface is incomplete.

It defines what can be called, not everything those calls are expected to mean.

Take the repository again:

The type signature answers some questions:

*   Which messages can a client send?

*   Which arguments are required?

*   Which result type is returned?

*   Which implementations can be supplied where `CustomerRepository` is expected?

It leaves other questions unanswered:

*   What should be true after a customer is saved?

*   Which customer fields must be preserved?

*   What happens when no customer has the requested id?

*   Should customers with different ids remain independent?

*   What happens when the same id is saved twice?

*   Which failures can clients observe?

*   Is saved data immediately visible to a later lookup?

*   Does the role promise durable storage, or only retrieval during the life of the object?

*   Is the implementation expected to be safe under concurrent access?

A repository contract does not need to answer every possible question. It must state the behaviours clients are allowed to rely on instead of relying on a familiar method name.

The word `save` feels meaningful because developers bring conventions to it. One reads it as insert. Another reads it as upsert. Another expects optimistic concurrency. Another assumes the call returns only after durable persistence.

The compiler cannot resolve those interpretations. It verifies structural compatibility, not the full meaning of the abstraction.

A behavioural contract can include:

*   Preconditions: what must be true before a call

*   Postconditions: what the implementation guarantees after a call

*   Invariants: what remains true across operations

*   Failure semantics: which failures clients may observe and how they are represented

*   History properties: how sequences of calls affect later observations

Barbara Liskov and Jeannette Wing’s work on behavioural subtyping makes the underlying point precise: syntactic compatibility is not sufficient. An implementation must preserve the properties that clients are entitled to assume from the abstraction’s specification.

A repository contract might contain this property:

```
Given a valid customer,
when the client saves it,
then a later lookup by the same id returns that customer.
```

It might also contain:

```
Given no saved customer with an id,
when the client looks up that id,
then the repository reports that the customer is missing.
```

If clients rely on replacement semantics, it might additionally contain:

```
Given a previously saved customer,
when the client saves another customer with the same id,
then a later lookup returns the most recently saved customer.
```

These statements describe relationships between calls. The interface alone cannot express them.

The first shift is:

> An interface is not the whole contract. It is the typed surface through which the contract is exercised.

The role test gives part of that contract an executable form.

[![Image 4](https://substackcdn.com/image/fetch/$s_!ZuSY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59551594-d44b-4995-9a5d-097c98a04719_1024x559.png)](https://substackcdn.com/image/fetch/$s_!ZuSY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59551594-d44b-4995-9a5d-097c98a04719_1024x559.png)

A role test is a reusable suite of behavioural examples that states what every valid implementation of a role must make true for its clients.

In responsibility-driven design, a role is a coherent set of related responsibilities within a collaboration. An object can play one or more roles. A responsibility is an obligation to perform work, make a decision, or know information. A collaboration is an interaction between objects or roles.

`CustomerRepository` can be understood as a role with responsibilities such as:

*   Remember a customer presented by a client

*   Find a remembered customer by identity

*   Represent absence using the agreed domain language

The role can be played by several objects:

*   `InMemoryCustomerRepository`

*   `PostgresCustomerRepository`

*   `FileCustomerRepository`

*   `RemoteCustomerRepository`

The role is not any one of those classes. It is the set of responsibilities they claim to fulfil for their clients.

A role test says:

> Any implementation that claims to be a `CustomerRepository` should satisfy these examples.

Conceptually:

The role test normally contains:

1.   Shared examples that describe the role

2.   A factory or fixture hook supplied by each concrete implementation test

This makes the suite executable documentation. A future reader can inspect it to understand what the abstraction means in this codebase, not only which methods it exposes.

That matters because weak abstractions rarely announce themselves with invalid method signatures. They appear when:

*   Different implementations interpret the same method differently

*   A fake becomes more permissive than production

*   A replacement dependency preserves API shape but changes behaviour

*   Clients begin to rely on behaviour that was never made explicit

*   A shared interface is hiding several incompatible roles

A role test gives those behaviours a home.

[![Image 5](https://substackcdn.com/image/fetch/$s_!uSrq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cd6678f-4fe7-419b-a5b5-0c83a8e48feb_1024x559.png)](https://substackcdn.com/image/fetch/$s_!uSrq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cd6678f-4fe7-419b-a5b5-0c83a8e48feb_1024x559.png)

In the broad object-oriented sense, a role test is a form of contract test.

The older contract idea comes from Bertrand Meyer’s _Design by Contract_ (DbC). In that model, a call is an agreement between a client and a supplier. The client must satisfy the preconditions for using the operation. The supplier must guarantee the promised postconditions and preserve the relevant invariants.

Role tests do not require a DbC language or runtime assertion mechanism. They borrow the same discipline: make the client-supplier promise explicit enough that it can be checked.

For a repository role, the agreement might say:

*   Precondition: the customer has a valid identity.

*   Postcondition: a later lookup by that identity returns the saved customer.

*   Invariant: different customer identities remain independent.

The role test turns those promises into examples that every implementation must satisfy.

Manuel Rivero calls them “role or contract tests.” His definition starts from the contract clients establish with a role and then tests every adapter to check that it respects that contract. He prefers the name _role test_ because _contract test_ has become overloaded.

Jason Gorman describes the same reusable-suite pattern as “polymorphic/contract testing”: test methods live in a base suite, while concrete test subclasses provide different implementations. Rivero also relates role tests to the contract tests in J. B. Rainsberger’s collaboration-and-contract testing model.

That vocabulary connects several older ideas. _Mock Roles, not Objects_ explains how client tests discover outgoing interfaces from the services a collaboration needs. Liskov and Wing’s behavioural subtyping work explains why substitutability requires preserving specified properties, not merely matching method signatures. Fowler’s writing on contract tests uses the same broad contract language for a different risk: compatibility between independently changing services. The overlap is useful, but the testing target is different.

The resulting definition is:

> A role test is an object-oriented contract test expressed as a reusable behavioural suite and applied to every implementation that claims the same role.

The distinctive move is to execute one contract against two or more alternatives that must be substitutable.

The word _interfaces_ can mislead here.

The sources describe testing different implementations or adapters of a role, not testing a contract against several unrelated interfaces. Usually there is one role interface:

and several implementations:

In a dynamic language, there may be no formal interface construct at all. The role can be a duck type documented by shared examples. This is one reason “two or more interfaces” cannot be the general definition.

When two external dependencies expose different interfaces, adapters translate both into one stable role interface. The role suite runs against the adapters:

```
Legacy API -> Legacy adapter -> CustomerRepository contract
New API    -> New adapter    -> CustomerRepository contract
```

A second implementation is not logically required to write the suite. The suite can document a role before another implementation exists. Its substitutability value becomes visible when a fake, replacement, alternative strategy, or second adapter is added.

The terminology becomes confusing because _contract testing_ also has a narrower and now widespread meaning in distributed systems. Martin Fowler uses the term for tests that check whether an external service continues to satisfy the behaviour expected by a client. Consumer-driven contract-testing literature develops that idea further around consumers, providers, published interactions, and independent deployment.

The two usages protect different risks:

Object-oriented role or contract test Distributed contract test Protects substitutability between implementations Protects compatibility between independently changing participants Runs one behavioural suite against every implementation Verifies requests, responses, messages, schemas, and interaction semantics Common examples are fake versus real repository or old versus new strategy Common examples are mobile client versus HTTP API or event consumer versus producer The contract is usually owned inside one design The contract crosses a deployment, team, or service boundary

An HTTP-backed repository may need both. Its role suite checks that the adapter presents the expected `CustomerRepository` semantics to local clients. Its distributed contract tests check that the remote provider still accepts and returns the agreed protocol.

Here, _role test_ names the object-oriented, polymorphic use: one behavioural suite, one role, every implementation that claims it. Distributed contract testing remains a separate compatibility concern at service or deployment boundaries.

[![Image 6](https://substackcdn.com/image/fetch/$s_!_nSw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ae651f5-4e89-4d25-b64e-97e3c0c9a3cb_1024x559.png)](https://substackcdn.com/image/fetch/$s_!_nSw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ae651f5-4e89-4d25-b64e-97e3c0c9a3cb_1024x559.png)

It is tempting to describe role testing as “testing two implementations of the same interface against each other.”

That wording is understandable but imprecise.

If we frame the technique that way, one implementation can accidentally become the reference and the other becomes a copy.

The flow should not be:

`PostgreSQL behaviour -> copy into the in-memory fake`
It should be:

`client needs -> role contract -> shared examples -> implementations`
The wrong oracle is:

`InMemoryCustomerRepository behaves like PostgresCustomerRepository.`
The role oracle is:

```
InMemoryCustomerRepository satisfies CustomerRepositoryRoleShould.
PostgresCustomerRepository satisfies CustomerRepositoryRoleShould.
```

The role is the reference, not one implementation.

If the implementations disagree, the answer is not automatically “make the fake match PostgreSQL” or “make PostgreSQL match the fake.”

Possible explanations include:

*   The fake is wrong

*   The production adapter is wrong

*   The old implementation contains accidental behaviour

*   The role test is missing a client-visible rule

*   The abstraction promises something one implementation cannot provide

*   Two different roles are hiding behind one interface

Differential testing runs the same inputs through two implementations and compares their outputs.

That can be valuable when replacing a legacy algorithm, database query, parser, or library. It can reveal disagreements over a large input set.

But it uses one implementation, or agreement between implementations, as an oracle. If the old implementation contains a bug, differential testing can encourage the new implementation to reproduce it.

A role test uses an intentional behavioural specification as the oracle.

Test reuse is useful. If several implementations must satisfy the same examples, copying those tests would create maintenance risk.

The deeper value is semantic:

*   The team states the shared behaviour once

*   Every implementation is held to the same meaning

*   A disagreement becomes a design decision

*   A new implementation tests the abstraction itself

A finite suite protects the examples and properties it encodes.

It does not automatically establish:

*   Every possible input

*   Every operation sequence

*   Thread safety

*   Durability

*   Performance

*   Security

*   Availability

*   Untested failures

Passing the suite is evidence that an implementation satisfies the represented portion of the contract. It is not a formal proof that every client-visible property is preserved.

A PostgreSQL repository still needs tests for migrations, constraints, transactions, mapping, and database integration. A filesystem adapter may need tests for paths, permissions, atomic writes, and serialization. An HTTP adapter may need tests for authentication, timeouts, status-code translation, and retry behaviour.

Those tests protect implementation-specific responsibilities.

The role test protects shared behaviour.

A reusable role suite can use:

*   A Kotlin or Java test interface

*   An abstract test class

*   Parameterized tests

*   Dynamic tests

*   RSpec shared examples

*   Composition through functions or fixtures

The mechanism is secondary. The reusable behavioural specification is the technique.

[![Image 7](https://substackcdn.com/image/fetch/$s_!CDu_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F274d53bb-935e-491c-9d96-27a2df6a8dc9_1024x559.png)](https://substackcdn.com/image/fetch/$s_!CDu_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F274d53bb-935e-491c-9d96-27a2df6a8dc9_1024x559.png)

A role does not usually appear because we invented an interface in isolation.

It often appears because a client needs help.

A use case needs somewhere to save a customer. A workflow needs a way to publish an event. A policy needs a source of time. A checkout process needs a pricing strategy. A migration needs an abstraction around a library that is being replaced.

In each case, the client is not asking for a concrete class. It is asking for a collaborator that can play a useful role in a larger behaviour.

Imagine we are developing `RegisterCustomer`:

At first, the test does not need a database. It needs to express that successful registration asks something to remember the customer.

The recording repository is a client-test double. It records the outgoing collaboration that this client needs and refuses unrelated messages:

The messages sent by the client begin to reveal a required role.

Later, another client needs lookup. Another needs replacement semantics. Another needs to distinguish missing data from infrastructure failure. The role becomes more precise as real client needs appear.

The discovery path moves from a client’s behaviour to a role and then to the implementations that must satisfy it:

Role tests fit naturally with _Test-Driven Development_ (TDD) and need-driven design.

The paper _Mock Roles, not Objects_ explains how tests for a client can discover outgoing interfaces based on services the client requires. The interface is pulled into existence by demand rather than pushed outward from all the features a provider happens to offer.

Two testing activities follow:

1.   Client tests protect how the client collaborates with the role

2.   Role tests protect whether concrete implementations honour that role

The client test does not prove that PostgreSQL works. The PostgreSQL role test does not prove that `RegisterCustomer` sends the correct message. Together they protect both sides of the collaboration.

Client needs change how interfaces are designed.

A good role interface is not a list of everything an implementation can do. It is a description of what a client needs from a collaborator.

Consider a provider-oriented interface:

Those operations may exist in one infrastructure component, but they do not form one coherent client role.

Application clients may need:

Operational tooling may need:

Narrow roles are easier to understand, substitute, adapt, and role-test.

[![Image 8](https://substackcdn.com/image/fetch/$s_!NdNZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe034c9e8-bdc2-42c2-8c38-a97cb0bbfae2_1024x559.png)](https://substackcdn.com/image/fetch/$s_!NdNZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe034c9e8-bdc2-42c2-8c38-a97cb0bbfae2_1024x559.png)

The repository example is familiar, but role tests are not mainly about repositories.

Role tests also apply to clocks, payment gateways, event publishers, file adapters, HTTP clients, caches, notification senders, search adapters, and Strategy implementations.

Start with a small domain:

Now decide how lookup absence appears in the role’s language.

A nullable result would be concise:

An explicit result makes the contract easier to see:

The repository becomes:

The result type already communicates one decision: absence is a normal lookup outcome represented as `Missing`, not `null` or an exception.

It still does not define the relationship between calls. The role suite will do that.

JUnit Jupiter allows test methods to be declared in interfaces. A concrete test class can implement the interface, supply a factory method, and inherit the shared examples.

The snippets below are complete for the design point they teach. Database, service, or sandbox harnesses are shown only where their shape affects the role-test contract.

The tests use Arrange, Act, Assert because it makes each expectation explicit. This structure is not part of role testing itself. It is simply a readable way to express each behavioural example.

The suite observes the repository only through its public role. It says nothing about maps, SQL, transactions, files, HTTP requests, JSON, or connection pools.

That is intentional.

The factory name also states a fixture precondition:

Every implementation-specific test must provide a clean repository. Without isolation, shared examples can leak state into one another and stop being reliable specifications.

The naming convention is deliberate. `CustomerRepositoryRoleShould` makes the role the subject of the specification:

```
CustomerRepositoryRoleShould find saved customer by id.
CustomerRepositoryRoleShould return missing when customer does not exist.
CustomerRepositoryRoleShould keep saved customers separated by id.
```

The individual method names remain short while the complete test name communicates the behavioural subject.

[![Image 9](https://substackcdn.com/image/fetch/$s_!mqvP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa437fb22-f5b1-4397-bd58-3f40a17d0136_1024x559.png)](https://substackcdn.com/image/fetch/$s_!mqvP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa437fb22-f5b1-4397-bd58-3f40a17d0136_1024x559.png)

The first suite is good enough to introduce the idea, but it also hides a testing smell.

The example named `find saved customer by id` uses `save` to create the precondition and `findById` to make the observation. If it fails, the failure might be in saving, lookup, mapping, equality, fixture isolation, or the relationship between two calls.

Some role examples genuinely need a sequence of role messages. If the contract is about a conversation, the test should show the conversation. The problem is accidental sequencing caused by weak fixture support.

A useful rule is:

> If a test is about lookup, do not use `save` to create the precondition. If a test is about saving, do not use `findById` to observe the result.

The test should fail for the behaviour it is trying to specify.

For lookup behaviour, the repository should already contain the customer. For saving behaviour, the test should observe stored state without going back through lookup.

That does not mean exposing implementation details to production code. It means giving the test suite implementation-specific fixture hooks that can prepare and inspect state outside the role method currently under test.

A sharper role suite separates the production role from test infrastructure:

Now the shared examples can say exactly which behaviour they exercise:

The lookup example arranges state through `givenStored` and exercises only `findById`. The save example exercises only `save` and observes state through `storedCustomerById`.

The fixture is not part of the production role. The in-memory fixture can write directly to the backing map. The PostgreSQL fixture can prepare and inspect rows through the table gateway. The shared suite stays focused on client-visible behaviour, while each concrete fixture owns the mechanics needed to make the examples precise.

That precision matters because role tests often become design evidence. A noisy test that can fail for five reasons is a weak witness. A role test should make the missing or broken contract visible.

The change in test shape is small but important.

Before, a lookup example arranged state through the role method `save`:

After, the same lookup example uses fixture infrastructure for the precondition and reserves the role call for the behaviour under test:

The same separation works in the other direction. A save example should not need `findById` to observe the result:

[![Image 10](https://substackcdn.com/image/fetch/$s_!Hsyd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb35a43ea-929e-4192-8c28-c5d2763826e6_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Hsyd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb35a43ea-929e-4192-8c28-c5d2763826e6_1024x559.png)

The in-memory implementation is small:

Its concrete test declares that it must satisfy the role:

Now add a PostgreSQL implementation:

`PostgresCustomerLookupMapper` is deliberately not injected into the repository.

It is an internal implementation detail of the PostgreSQL adapter, not a peer of the `CustomerRepository` role. Extracting a collaborator does not automatically mean promoting it to the constructor boundary.

The role test protects the shared behaviour of `CustomerRepository`.

The mapper supports one implementation. As shown here, it is private and exercised through the repository. If it grows enough to deserve direct tests, that would be a reason to revisit its visibility and responsibilities, not a reason to place it in the shared role.

The PostgreSQL test uses the same suite:

The concrete database harness is intentionally represented by `TestDatabase.freshCustomerRows()`. In a real test suite it must provide:

*   A migrated schema

*   An empty customers table

*   Isolation between tests

*   The same database dialect used by the production adapter

Possible implementations include a rolled-back transaction, table truncation, a fresh schema, a database sandbox, or a disposable container.

The minimal table needed by these examples is:

`PostgresCustomerRepositoryFixture` deliberately uses the table gateway directly. It prepares and inspects state at the adapter boundary without calling the role method currently under test.

That gives each role example a sharper failure signal:

```
givenStored(...) -> repository.findById(...)
repository.save(...) -> storedCustomerById(...)
```

If the lookup test fails, the failure points at lookup behaviour. If the save test fails, the failure points at save behaviour.

The shared suite should not know which isolation strategy is used. Fixture construction belongs to the concrete adapter test.

Both implementations now satisfy the same known behaviours.

The in-memory adapter can use a map. PostgreSQL can use a table gateway and an internal mapper. The suite does not care because those are implementation decisions, not role-level promises.

The behavioural specification is written once and run against every implementation that claims the abstraction.

[![Image 11](https://substackcdn.com/image/fetch/$s_!tvZ6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F548c007d-b045-4604-a2e8-d1d789dfac28_1024x559.png)](https://substackcdn.com/image/fetch/$s_!tvZ6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F548c007d-b045-4604-a2e8-d1d789dfac28_1024x559.png)

The current role suite still has a weakness.

It does not define what happens when the same customer id is saved twice.

That omission allows the in-memory and PostgreSQL implementations to pass while disagreeing about `save`.

Suppose a client renames a customer by saving a new representation with the same identity. Replacement semantics then become part of the role.

Add one example:

This is the same before-and-after lesson applied to a new contract decision. The old shape would have been noisier:

That test checks an important history property, but it can still fail through lookup. The fixture-based version keeps the observed behaviour focused on what `save` must do when the identity already exists.

The in-memory implementation passes. The PostgreSQL implementation fails because the second insert violates the unique key.

The failed test reveals a missing contract decision.

Possible responses include:

1.   Define `save` as an upsert and change PostgreSQL

2.   Define duplicate identity as an error and change the in-memory fake

3.   Rename `save` to `add` if creation is the real responsibility

4.   Separate `add` and `replace`

5.   Introduce optimistic concurrency if silent replacement would lose changes

6.   Admit that the implementations do not satisfy the same role

The role test should not invent the answer merely to make implementations equal. The decision comes from client needs and domain rules.

If last-write-wins replacement is the intended contract, PostgreSQL can implement an upsert:

The production adapter now satisfies the chosen role.

This does not make the fake the source of truth. The client requirement and the resulting specification are the source of truth. The fake happened to implement the selected behaviour first.

The example also demonstrates the limit of role testing:

> A shared suite is only as complete as the client-visible behaviours it expresses.

Green tests meant that both implementations satisfied the initial examples. They did not mean that every semantic question had already been answered.

[![Image 12](https://substackcdn.com/image/fetch/$s_!AYG6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F244ab47b-bbca-4f42-9bca-8cb8ecd4ad8f_1024x559.png)](https://substackcdn.com/image/fetch/$s_!AYG6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F244ab47b-bbca-4f42-9bca-8cb8ecd4ad8f_1024x559.png)

An in-memory repository is a fake: a working but simplified implementation of a dependency.

Fakes are useful because they are fast, deterministic, and easy to construct:

Those strengths also make them dangerous. A fake can become a fantasy object that behaves conveniently in tests but cannot be substituted by production.

Common divergences include:

*   A map overwrites duplicate keys while SQL rejects them

*   A fake accepts values rejected by database constraints

*   A fake returns the exact stored instance while production reconstructs data

*   A fake ignores serialization and representation loss

*   A fake offers immediate consistency while a remote store is eventually consistent

*   A fake never fails

*   A fake is not thread-safe while production use is concurrent

*   A fake claims persistence but loses everything when the process ends

A role suite reduces drift for the behaviours included in the contract.

The fake should not be judged by this rule:

> Make the fake reproduce PostgreSQL.

The role contract asks for this:

> Make the fake and PostgreSQL honour the same promises made by `CustomerRepository`.

Everything outside those promises may differ.

That separation prevents two opposite mistakes.

The first is an unrealistically weak fake:

Client tests using this fake can pass even though saved data can never be found.

The second mistake is recreating the infrastructure inside the fake. If the in-memory repository implements SQL locking, database transactions, network retries, connection pools, and persistence formats, it is no longer lightweight.

Role tests identify the middle ground:

*   Reproduce the shared semantics

*   Omit implementation-specific mechanics

*   Test the real adapter separately

The resulting test strategy has different suites protecting different risks:

Fakes are a common use case, but not the whole technique. A filesystem repository and a PostgreSQL repository can both be production adapters. A sandbox payment gateway and a live gateway may both be production-like environments. Kafka and another broker may coexist during migration.

The relevant fact is that each implementation claims the same role.

[![Image 13](https://substackcdn.com/image/fetch/$s_!qJYU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F974739ba-ca80-4ec6-afbf-0d333f9e1e1a_1024x559.png)](https://substackcdn.com/image/fetch/$s_!qJYU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F974739ba-ca80-4ec6-afbf-0d333f9e1e1a_1024x559.png)

Role tests become especially useful when a dependency must be replaced.

Imagine a system coupled to a legacy customer library:

The team wants to migrate to a new service:

The APIs differ. Directly changing every client would mix several concerns:

*   Understanding what clients actually need

*   Translating between data models

*   Implementing the new integration

*   Updating every use site

*   Deciding which legacy behaviours must be preserved

A safer refactor introduces a stable role:

The old dependency receives an adapter:

The new dependency receives another adapter:

Both adapters run the same role suite:

The following fixtures show the contract shape. Each real project supplies the backing test environment.

`LegacyCustomerRepositoryFixture` and `ServiceCustomerRepositoryFixture` follow the same pattern as the PostgreSQL fixture: they expose the adapter through `repository`, prepare state through the real dependency’s test environment, and inspect state without calling the role method currently under test.

These fixture names represent production-compatible test environments: an isolated instance of the legacy store and a sandbox, emulator, disposable service, or controlled integration environment for the replacement.

Using another hand-written fake underneath each adapter may make the suite faster, but it would not prove that the adapter translates the real dependency correctly. If a provider cannot run in the role suite, retain provider-specific integration or distributed contract tests beside it.

A gradual migration can then proceed in small steps:

1.   Identify the behaviour clients need from the old dependency

2.   Introduce a role interface around those needs

3.   Adapt the old dependency to the role

4.   Write the shared role suite

5.   Make the old adapter satisfy the suite

6.   Implement the new adapter

7.   Make the new adapter satisfy the same suite

8.   Switch clients incrementally

9.   Remove the old dependency when no clients remain

This is closely related to Branch by Abstraction. Martin Fowler describes that technique as introducing an abstraction so an old and a new supplier can coexist while clients migrate gradually.

Role tests strengthen the technique by making the abstraction’s expected behaviour executable.

The role suite does not compare the two external APIs. It checks that both adapters present the same `CustomerRepository` behaviour to local clients.

Role testing does not usually verify a contract against two unrelated interfaces. It verifies one role contract against the implementations or adapters that claim that role.

If the old and new dependencies expose different APIs, adapters translate both into the stable role.

During migration, the system may also run both implementations against production-like traffic and compare selected observations. That is useful, but it is differential testing or shadow traffic, not the role test itself.

The techniques complement one another:

*   The role suite states what must remain true

*   Characterization tests reveal what the old dependency currently does

*   Differential tests find disagreements between old and new implementations

*   Integration tests prove that each real dependency is wired correctly

*   Feature flags or controlled routing migrate clients gradually

Role tests are valuable because they prevent “the old dependency did it” from becoming the only definition of correctness.

[![Image 14](https://substackcdn.com/image/fetch/$s_!5_Bt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffac2230c-b7a4-46ed-9fe9-59cdab54ad7a_1024x559.png)](https://substackcdn.com/image/fetch/$s_!5_Bt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffac2230c-b7a4-46ed-9fe9-59cdab54ad7a_1024x559.png)

Generated clients are useful. An _OpenAPI Specification_ (OAS) document describes provider-facing details: paths, operations, schemas, parameters, responses, and protocol errors.

The risk appears when application code starts speaking generated-client language directly.

Imagine checkout code coupled to a generated shipping client:

The generator is not the problem. The transport contract has become the local application role.

Checkout needs a smaller role:

The shared role suite protects local behaviour, not OpenAPI protocol details:

The old adapter can wrap the generated client:

The replacement can be a handwritten adapter:

Both adapters run the same `ShippingQuotesRoleShould` suite.

*   The OAS contract describes the provider API

*   The role test describes the local application role

*   The generated client and the handwritten adapter are implementation choices behind that role

The role suite does not replace provider contract tests, schema checks, authentication tests, retry tests, timeout tests, or real integration tests. It protects the meaning promised to application code while provider protocol concerns stay at the provider boundary.

[![Image 15](https://substackcdn.com/image/fetch/$s_!3fUM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe91c64b5-0516-44e8-942e-40734a5bb7c7_1024x559.png)](https://substackcdn.com/image/fetch/$s_!3fUM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe91c64b5-0516-44e8-942e-40734a5bb7c7_1024x559.png)

The Strategy pattern defines a family of algorithms behind a common interface so a client can select or replace the algorithm without owning its implementation details.

That makes Strategy a natural place for role tests, but it introduces an important distinction.

Sometimes strategies are intentionally different:

`RoadRouteStrategy and WalkingRouteStrategy`
They receive the same origin and destination but should produce different routes. A shared role suite can protect common properties, such as returning a connected route with the requested endpoints. It should not require equal routes.

In other cases, a new Strategy is intended as a behavioural replacement for an old one. Then the role suite can protect the complete business behaviour that must survive the refactor.

Consider a checkout that delegates pricing:

The example uses a deliberately small, single-currency `Money` value so that the pricing rules remain visible:

Production money handling may require several currencies, explicit rounding rules, overflow protection, and auditability. The pricing role below only needs enough money behaviour to make the strategy rules visible.

The current strategy contains legacy conditionals:

The team wants to replace it with a rule-based design:

The role suite expresses the rules clients rely on:

Both strategies claim the role:

The static structure is simple: `Checkout` depends on the role, while the role suite verifies both strategy implementations independently.

Now the team can refactor the internal design without changing what `Checkout` is allowed to assume.

The suite protects business meaning:

*   Regular customers pay the subtotal

*   Preferred customers receive the agreed discount

*   A zero subtotal remains zero

It does not protect implementation details:

*   `if` statements

*   Rule ordering internals not visible to clients

*   The number of rule objects

*   Whether percentages are calculated through one method or another

The suite protects business meaning without turning the old implementation into the oracle.

If the legacy strategy contains an accidental bug for one unusual order, the team must decide whether that behaviour is contractual. A characterization or differential test may expose the disagreement. The role suite contains the decision about what should survive.

> Strategies are interchangeable only relative to the properties promised by their shared role.

If `RoadRouteStrategy` and `WalkingRouteStrategy` intentionally optimize different outcomes, their role test should express common route validity, not equal paths. If `RuleBasedPriceCalculationStrategy` is a drop-in replacement for the legacy pricing strategy, its suite can express the complete pricing rules that clients require.

[![Image 16](https://substackcdn.com/image/fetch/$s_!3sdD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F920b2670-a42c-4631-af5d-e5221e7657ca_1024x559.png)](https://substackcdn.com/image/fetch/$s_!3sdD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F920b2670-a42c-4631-af5d-e5221e7657ca_1024x559.png)

During a replacement, teams often need three related activities. They should not collapse into one another.

![Image 17](https://substackcdn.com/image/fetch/$s_!3PLT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39c040c8-a26c-495d-94b7-555ab62662df_688x188.png)

Observed legacy behaviour can inform the role contract. It should not become the role contract automatically.

Michael Feathers describes characterization tests as tests that document actual current behaviour so code can be changed more deterministically.

When a team does not yet understand a legacy implementation, a characterization test records what happens today:

Before the refactor, the test creates a concrete observation:

The legacy implementation currently gives preferred customers a ten percent discount.

It does not yet say:

Every valid pricing strategy must give preferred customers a ten percent discount.

That second statement requires a decision. The team may confirm that the behaviour is an intentional business rule, discover that it is an accidental bug, or decide that the rule should change.

Characterization tests are useful but dangerous as a source of truth. They capture what exists, including accidental behaviour.

Differential tests run the same examples through old and new implementations:

Differential tests reveal disagreement across many generated or recorded inputs.

They are less useful for deciding which result is correct.

Role tests encode the behaviour clients are allowed to require. If the team decides that the preferred-customer discount is contractual, the observation moves into the shared role suite:

The expected value is the same as in the characterization test, but the oracle is different.

The characterization-test oracle:

The legacy strategy does this today.

The role-test oracle:

Every strategy that claims this role must do this.

Characterization tests can feed a role test, but they should not become the role test automatically.

During a dependency replacement, a strong workflow can use all three:

1.   Characterize the legacy implementation

2.   Identify which observed behaviours are intentional

3.   Place intentional shared behaviour in the role suite

4.   Run the role suite against old and new adapters

5.   Use differential testing on a wider dataset to find unexpected disagreements

6.   Decide each disagreement using domain rules and client needs

The workflow avoids two failure modes:

*   Blindly copying every legacy behaviour

*   Rewriting the dependency without understanding what clients rely on

[![Image 18](https://substackcdn.com/image/fetch/$s_!YFlh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a51e535-653c-4cb2-80c4-0928ebb832b1_1024x559.png)](https://substackcdn.com/image/fetch/$s_!YFlh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a51e535-653c-4cb2-80c4-0928ebb832b1_1024x559.png)

A shared-suite behaviour must be promised by every valid implementation.

A practical filter is:

> Could a client written only against this role reasonably depend on this behaviour?

For `CustomerRepository`, that may include:

*   A saved customer can be found by id

*   An unknown id produces `Missing`

*   Customers with different ids remain independent

*   Relevant customer data survives persistence and reconstruction

*   Saving the same id has defined semantics

*   Invalid input is handled consistently, if input validation belongs to the role

*   Failures use a stable domain language, if clients are expected to react to them

For `PriceCalculationStrategy`, it may include:

*   Business rules that every drop-in pricing implementation must preserve

*   Boundary behaviour such as preserving a zero subtotal

*   Boundary behaviour around zero or discount limits

Role tests often describe operation sequences rather than isolated methods:

```
save customer
find customer
```

```
save original
save replacement
find identity
```

```
calculate regular order
calculate preferred order
preserve a zero subtotal
```

The term behavioural contract matters because the suite describes interactions, not only isolated method returns.

Use preconditions, postconditions, invariants, failures, and history as prompts:

*   Does one implementation reject an input the role accepts?

*   Does it return an outcome the role does not permit?

*   Does it throw an exception clients cannot handle?

*   Can it break an invariant?

*   Can a sequence of calls create an observation forbidden by the role?

Do not add every conceivable case. Add behaviours clients are allowed to rely on and risks likely to cause semantic drift.

The suite should grow when the role becomes better understood.

[![Image 19](https://substackcdn.com/image/fetch/$s_!TOj3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93e072eb-613c-4dcc-84df-04ed7cce55aa_1024x559.png)](https://substackcdn.com/image/fetch/$s_!TOj3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93e072eb-613c-4dcc-84df-04ed7cce55aa_1024x559.png)

A role test should not become a dump of every behaviour of every implementation.

These do not belong in a generic `CustomerRepositoryRoleShould`:

*   Creating the customers table

*   Using a specific SQL index

*   Opening exactly one database connection

*   Retrying a PostgreSQL deadlock three times

*   Calling `PostgresCustomerLookupMapper`

*   Serializing customers as JSON

*   Storing files under a particular directory

*   Using a mutable map internally

*   Calling an HTTP endpoint with a specific library

Some of these behaviours need tests. They belong to the concrete adapter.

The same separation applies to Strategy:

*   The role suite can protect pricing outcomes

*   It should not require `RuleBasedPriceCalculationStrategy` to evaluate rules through a particular collection operation

*   It should not require the legacy strategy to contain an `if`

The shared suite should also avoid accidental behaviour.

Suppose PostgreSQL returns rows in insertion order for a query without `ORDER BY`. If no client is promised that order, do not add it to the role suite merely because it happened in one test run.

Every shared assertion increases the contract surface. Once clients depend on it, changing it becomes more expensive.

The suite should capture intentional guarantees, not everything implementations happen to share.

There is another warning sign: implementation-specific branching inside the suite.

If every assertion changes according to the implementation, the suite no longer describes one role. It describes a family of incompatible behaviours.

The right response may be:

*   Narrow the shared contract

*   Split the interface

*   Introduce separate roles

*   Accept that one implementation is not substitutable

[![Image 20](https://substackcdn.com/image/fetch/$s_!YG0o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F353661c1-7f29-4da1-918d-4e201e19dba7_1024x559.png)](https://substackcdn.com/image/fetch/$s_!YG0o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F353661c1-7f29-4da1-918d-4e201e19dba7_1024x559.png)

Role tests are not only a testing technique. They create design pressure.

They force a question that class-oriented designs can avoid:

> What role is this object playing for its clients?

That question is stronger than:

> What class is this?

A class is a code construct. A role is a responsibility in a collaboration.

Role tests fit naturally with object-oriented design. Objects collaborate through messages and make promises to their neighbours. A role test captures part of those promises.

Role tests can reveal weak abstractions:

*   If the interface is hard to role-test, the role may be unclear

*   If each implementation needs exceptions to the shared suite, the interface may hide several concepts

*   If the suite needs implementation internals, the abstraction may be leaking

*   If the suite becomes enormous, the role may own too many responsibilities

*   If a fake cannot satisfy production semantics, the fake may be misleading

*   If production cannot satisfy the role promised to clients, the abstraction may be unrealistic

The `PostgresCustomerLookupMapper` example illustrates a smaller boundary decision.

The mapper improves one adapter’s internal design. It is not part of the shared repository role. Clients should not know it exists, so the role suite ignores it.

The Strategy example illustrates another boundary.

`Checkout` knows only `PriceCalculationStrategy`. It should not know whether pricing is implemented through conditionals, a rule collection, a decision table, or an external engine. The role test protects the result that `Checkout` can rely on.

Role tests also support evolvability.

When a new adapter or strategy is introduced, the suite provides immediate feedback about whether the existing abstraction is strong enough. When a dependency is replaced, the suite separates client promises from supplier details. When a test fake is used, the suite reduces the risk that tests execute against an easier but semantically false world.

Role tests do not magically produce good design. They make vague contracts harder to ignore.

[![Image 21](https://substackcdn.com/image/fetch/$s_!b7de!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e31665f-1425-41c0-9010-981000df5c8a_1024x559.png)](https://substackcdn.com/image/fetch/$s_!b7de!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e31665f-1425-41c0-9010-981000df5c8a_1024x559.png)

The production adapter is not automatically the truth. The fake is not automatically the truth. The legacy dependency is not automatically the truth.

The intentional role specification is the reference.

Characterization and differential tests can reveal legacy behaviour. They do not decide which behaviour deserves to become contractual.

Passing examples is evidence for represented behaviour, not exhaustive proof.

State the boundary of the suite honestly.

Tests such as “store the customer in a map,” “execute this SQL,” or “evaluate exactly three pricing rules” may be valid implementation tests. They are not role tests.

Persistence, search, exporting, reporting, and notification rarely form one coherent repository role.

Test friction can be design feedback.

If the suite expects replacement from one repository and duplicate rejection from another, it is not protecting one role.

Role tests are useful when a meaningful role and substitution pressure already exist. They are not a reason to create interfaces everywhere.

A PostgreSQL adapter can pass its role suite and still fail because of migrations, permissions, configuration, connection pools, or deployment.

An HTTP adapter can pass and still fail against the real provider.

Role tests are object-oriented contract tests for substitutability. Distributed contract tests use the same broad language for compatibility across an independently changing boundary. State which meaning is intended instead of treating either vocabulary as universal.

A fake that ignores calls, always succeeds, or stores less information than the role promises can make client tests misleading.

A fake should reproduce shared semantics, not database engines, networks, or operational failure systems.

Alternative strategies can intentionally produce different outputs.

The shared suite should protect the common role. Equal output is required only when one strategy is intended as a behavioural replacement for another.

Each implementation fixture must create a clean and known state. Shared tests are unreliable if state leaks between examples.

A test interface, abstract class, or shared-example feature is only the delivery mechanism.

Most mistakes come from choosing the wrong oracle, widening the role beyond client needs, or confusing shared semantics with implementation mechanics.

[![Image 22](https://substackcdn.com/image/fetch/$s_!4giz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4773a70-936e-4513-8a12-c32af767475d_1024x559.png)](https://substackcdn.com/image/fetch/$s_!4giz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4773a70-936e-4513-8a12-c32af767475d_1024x559.png)

Role tests add work:

*   A shared suite must be named and maintained

*   Every implementation needs an isolated fixture

*   The team must decide which behaviours are genuinely shared

*   Real adapters can make the suite slower

They are especially valuable when:

*   A fake is used heavily in client tests

*   Several implementations already exist

*   A new Strategy is intended as a drop-in replacement

*   A database, library, framework, or external service is being replaced

*   Old and new adapters must coexist during migration

*   Different deployments choose different adapters

*   Semantic drift would be expensive

*   The abstraction is important enough to deserve explicit behavioural documentation

They may add little value when:

*   There is one implementation and no realistic substitution pressure

*   The interface exists only because a framework requires it

*   The abstraction has almost no meaningful behaviour

*   The implementations intentionally promise different semantics

*   The role suite would repeat behaviour already protected more clearly through a stable public boundary

Sometimes the difficulty of writing a role test is evidence that the interface itself is not carrying enough design value.

Removing, narrowing, or splitting the interface may be better than surrounding it with more test architecture.

[![Image 23](https://substackcdn.com/image/fetch/$s_!wkci!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F266da9d4-bcf5-44fc-a059-b3d8812ec7e1_1024x559.png)](https://substackcdn.com/image/fetch/$s_!wkci!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F266da9d4-bcf5-44fc-a059-b3d8812ec7e1_1024x559.png)

A role test is a small idea with a large design consequence.

It says that an abstraction means something.

An interface tells the compiler which messages an object accepts. It does not fully describe what clients may assume after sending those messages.

That is how an in-memory repository and a PostgreSQL repository can both implement:

while disagreeing about duplicate identity.

A role test turns the client-visible promises of that abstraction into shared executable examples.

It does not ask the fake to copy PostgreSQL. It does not ask the new dependency to reproduce every legacy accident. It does not require alternative strategies to produce identical results when their purposes differ.

In the object-oriented terminology documented by Rivero and Gorman, this is contract testing applied polymorphically: one contract suite is executed against every implementation that claims the role. The name _role test_ makes the intended meaning explicit and avoids confusing it with consumer-provider contract testing across distributed boundaries.

It asks each implementation:

> Do you satisfy the behaviour promised by this role?

That question helps in daily design:

*   A fake and a real adapter remain aligned on shared semantics

*   Several production adapters can be checked against one role

*   A new Strategy can preserve required business rules

*   An old and a new dependency can coexist behind one abstraction during a gradual refactor

*   Disagreements reveal missing contract decisions

The technique has limits. A passing suite covers only the properties it expresses. Implementation-specific, integration, distributed-contract, performance, security, and operational tests remain necessary.

But the shared suite gives the team something an interface alone cannot provide: an executable statement of meaning.

The interface gives the collaboration a vocabulary.

The role test gives that vocabulary behavioural meaning.

*   Aniche, Maurício. _Effective Software Testing: A Developer’s Guide_. [https://www.manning.com/books/effective-software-testing](https://www.manning.com/books/effective-software-testing)

*   Cruz, Marie; Glover, Lewis; Mittal, Madhura; Prescott, Lewis. _Contract Testing in Action_. [https://www.manning.com/books/contract-testing-in-action](https://www.manning.com/books/contract-testing-in-action)

*   Feathers, Michael C. _Working Effectively with Legacy Code_. [https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000000231](https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000000231)

*   Fowler, Martin. _Branch by Abstraction_. [https://martinfowler.com/bliki/BranchByAbstraction.html](https://martinfowler.com/bliki/BranchByAbstraction.html)

*   Fowler, Martin. _Contract Test_. [https://martinfowler.com/bliki/ContractTest.html](https://martinfowler.com/bliki/ContractTest.html)

*   Fowler, Martin. _Mocks Aren’t Stubs_. [https://martinfowler.com/articles/mocksArentStubs.html](https://martinfowler.com/articles/mocksArentStubs.html)

*   Freeman, Steve; Mackinnon, Tim; Pryce, Nat; Walnes, Joe. _Mock Roles, not Objects_. [https://jmock.org/oopsla2004.pdf](https://jmock.org/oopsla2004.pdf)

*   Freeman, Steve; Pryce, Nat. _Growing Object-Oriented Software, Guided by Tests_.

[https://www.growing-object-oriented-software.com/](https://www.growing-object-oriented-software.com/)

*   Gamma, Erich; Helm, Richard; Johnson, Ralph; Vlissides, John. _Design Patterns: Elements of Reusable Object-Oriented Software_. [https://www.pearson.com/en-us/subject-catalog/p/design-patterns-elements-of-reusable-object-oriented-software/P200000009480](https://www.pearson.com/en-us/subject-catalog/p/design-patterns-elements-of-reusable-object-oriented-software/P200000009480)

*   Gorman, Jason. _ContractTesting: Simple example of polymorphic/contract testing in JUnit_. [https://github.com/jasongorman/ContractTesting](https://github.com/jasongorman/ContractTesting)

*   JUnit Team. _Test Interfaces and Default Methods_. [https://docs.junit.org/6.1.0/writing-tests/test-interfaces-and-default-methods.html](https://docs.junit.org/6.1.0/writing-tests/test-interfaces-and-default-methods.html)

*   Liskov, Barbara; Wing, Jeannette. _A Behavioral Notion of Subtyping_. [https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf)

*   Meszaros, Gerard. _xUnit Test Patterns: Refactoring Test Code_.

[http://xunitpatterns.com/](http://xunitpatterns.com/)

*   Meyer, Bertrand. _Building Bug-Free O-O Software: An Introduction to Design by Contract_. [https://www.eiffel.com/values/design-by-contract/introduction/](https://www.eiffel.com/values/design-by-contract/introduction/)

*   OpenAPI Initiative. _OpenAPI Specification_. [https://spec.openapis.org/oas/latest.html](https://spec.openapis.org/oas/latest.html)

*   Rainsberger, J. B. _Integrated Tests Are a Scam_.

[Video 3](https://vimeo.com/80533536)

*   Rivero, Manuel. _Example of role tests in Java with JUnit_. [https://codesai.com/posts/2022/08/role-tests-junit](https://codesai.com/posts/2022/08/role-tests-junit)

*   Rivero, Manuel. _Role tests for implementation of interfaces discovered through TDD_. [https://codesai.com/posts/2022/04/role-tests](https://codesai.com/posts/2022/04/role-tests)

*   Sato, Danilo. _Parallel Change_. [https://martinfowler.com/bliki/ParallelChange.html](https://martinfowler.com/bliki/ParallelChange.html)

*   Wirfs-Brock, Rebecca; McKean, Alan. _Object Design: Roles, Responsibilities, and Collaborations_. [https://www.informit.com/store/object-design-roles-responsibilities-and-collaborations-9780201379433](https://www.informit.com/store/object-design-roles-responsibilities-and-collaborations-9780201379433)

*   Wirfs-Brock, Rebecca; Wilkerson, Brian; Wiener, Lauren. _Designing Object-Oriented Software_. [https://dl.acm.org/doi/book/10.5555/573097](https://dl.acm.org/doi/book/10.5555/573097)
