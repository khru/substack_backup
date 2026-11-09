Title: Role tests are not about comparing implementations

URL Source: http://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing

Final URL: https://emmanuelvalverderamos.substack.com/p/role-tests-are-not-about-comparing

Published Time: 2026-06-23T05:00:35+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!JAKb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d5c08d2-bec5-40ee-90e6-af7618c46e60_1024x559.png)](https://substackcdn.com/image/fetch/$s_!JAKb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d5c08d2-bec5-40ee-90e6-af7618c46e60_1024x559.png)

Interfaces often give us confidence earlier than they should.

At first, everything looks fine. The interface is clean, one implementation passes its tests, another implementation is easy to use in local development, and a third one might be useful in tests or in a different runtime context. The compiler is satisfied, the tests are green, and the boundary looks clean. The problem is that none of those things prove that every implementation means the same thing by `save` and `findById`.

That is the problem role tests help us examine.

An interface can tell us what can be called, but it cannot fully tell us what those calls are supposed to mean.

This interface tells us that a customer can be saved and later searched by id. Or, more carefully, it gives us a method named `save` and a method named `findById`. The rest of the meaning lives outside the type signature.

The interface does not answer all the behavioural questions clients eventually care about. What should happen when a customer does not exist? What does saving mean? Should two customers with different ids remain independent? And if several implementations exist, what makes them valid substitutes for the same clients?

A role test gives us a place to answer those questions.

The important nuance is that a role test is not mainly a way to compare two implementations with each other. It is a way to define the expected behaviour of a role, and then ask every implementation of that role to prove that it behaves correctly.

We are not asking whether implementation A behaves like implementation B. We are asking whether implementation A satisfies the role, and whether implementation B satisfies the same role.

When multiple implementations pass the same reusable behavioural tests, we gain confidence that they honour the same contract. Not only the same method names, but the same meaning.

[![Image 2](https://substackcdn.com/image/fetch/$s_!facS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35fb2774-a9da-40fc-a478-e6a581ffb4e4_1672x941.png)](https://substackcdn.com/image/fetch/$s_!facS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35fb2774-a9da-40fc-a478-e6a581ffb4e4_1672x941.png)

*   **An interface defines shape, but a role test defines expected behaviour.**  
A method signature can say `save(customer)`, but it cannot fully say what must be true after saving. Role tests make that meaning executable.

*   **Role tests do not primarily compare implementations against each other.**  
They compare each implementation against the same behavioural contract. If several implementations pass the same role test, they are compatible with the same role.

*   **Roles are often discovered from the client side.**  
A client object needs help, sends messages to a collaborator, and those messages start revealing a role. The interface may be written later, but the role begins to appear from use.

*   **A role test can be implemented in different ways.**  
In this article, I use a Kotlin interface with default test methods. That is only one mechanism. The important idea is the reusable behavioural suite, not the specific reuse technique.

*   **They are useful for any interface with multiple meaningful implementations.**  
A fake and a production adapter are a common example, but not the only one. Role tests apply whenever several implementations claim to satisfy the same behavioural contract.

*   **A role test should describe externally visible behaviour, not implementation details.**  
The test should not care whether the repository uses a map, a database, a file, or an HTTP service. It should care about what the role promises to its clients.

*   **The main design benefit is semantic pressure.**  
Role tests force us to say what an abstraction means. That makes weak interfaces, vague responsibilities, and misleading implementations easier to detect.

1.   The problem with interfaces

2.   What a role test is

3.   What a role test is not

4.   Roles are discovered from the client side

5.   A small example in Kotlin

6.   Testing two implementations with the same role test

7.   Why this matters for every implementation of an interface

8.   What should go into a role test?

9.   What should not go into a role test?

10.   Role tests and object-oriented design

11.   Common mistakes

12.   Conclusion

13.   References

Interfaces are useful because they let us name a role without committing every client to one concrete implementation. That is one of the reasons they are so common around persistence, clocks, payment gateways, event publishers, file systems, external APIs, and other boundaries where substitution matters.

But an interface is also incomplete.

It defines what can be called, not everything those calls are expected to mean.

Take this example again:

The shape is clear, but the behaviour is still partly implicit. We can infer that `save` stores a customer and that `findById` retrieves one, but the interface does not explicitly define all the behavioural rules around those operations.

What should happen after saving a customer? What happens if two customers are saved? What happens if the same customer is saved twice? Which parts of the customer must be preserved? Are failures represented as exceptions, sealed results, nullable results, or something else?

Some of those answers may feel obvious because we understand the word “repository”. But that is exactly the problem: a lot of design knowledge hides inside naming conventions, team habits, framework expectations, and assumptions that are never made executable.

The compiler can check that an implementation has the right methods. It cannot check that those methods mean what the clients think they mean.

A role test can help.

The interface gives the role a shape. The role test gives the role a behavioural meaning.

The first shift is this:

> An interface is not the whole contract. It is only part of the contract.

The real contract also includes behaviour.

[![Image 3](https://substackcdn.com/image/fetch/$s_!1_aM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc9d0f54-1020-41b4-ac5b-6306ba0f394e_1024x559.png)](https://substackcdn.com/image/fetch/$s_!1_aM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc9d0f54-1020-41b4-ac5b-6306ba0f394e_1024x559.png)

A role test is a reusable test suite that defines the expected behaviour of a role. In many object-oriented designs, that role is represented by an interface.

More precisely:

> A role test is a reusable behavioural test suite that states what every valid implementation of an interface must make true for its clients.

In responsibility-driven design terms, a role is not just a type name. A role is a set of related responsibilities within a collaboration. That is why role tests fit the concept so well: they do not test “a class”; they test whether an implementation fulfils the responsibilities expected from that role.

For example:

The role test says something stronger than the interface alone can say:

> Any valid `CustomerRepository` should behave like this.

That is different from saying:

> This particular implementation should behave like this.

The distinction matters because the same test suite can be applied to multiple implementations.

For example:

*   `InMemoryCustomerRepository`

*   `SqlCustomerRepository`

*   `FileCustomerRepository`

*   `HttpCustomerRepository`

All of them may implement `CustomerRepository`. If they do, and if they are meant to be valid substitutes for the same clients, they should pass the same role test.

That makes the role test a form of executable documentation. It tells future readers what the interface means in this codebase, not only what methods it exposes.

This is valuable because weak abstractions rarely announce themselves with invalid method signatures. Most of the time, they look fine at the type level. The weakness appears later, when different implementations interpret the same interface differently, when test doubles become too permissive, or when clients rely on behaviours that were never made explicit.

A role test gives those behaviours a home.

There is a related term here: contract test.

That term is useful, but it is also overloaded. In some contexts, contract testing refers to service contracts between distributed systems. In others, it refers to tests that verify an implementation against a shared abstraction. The phrase “role test” is useful because it keeps the focus on the object-oriented idea: a collaborator plays a role, and that role has behavioural expectations.

The role test is the executable specification of those expectations.

[![Image 4](https://substackcdn.com/image/fetch/$s_!ieWQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a2494f5-4488-4a72-a3d3-61cba2ff9c1b_902x1420.png)](https://substackcdn.com/image/fetch/$s_!ieWQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a2494f5-4488-4a72-a3d3-61cba2ff9c1b_902x1420.png)

[![Image 5](https://substackcdn.com/image/fetch/$s_!gYXE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0f7d141-b8e5-44cd-b88e-ef87e85e7228_2202x906.png)](https://substackcdn.com/image/fetch/$s_!gYXE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0f7d141-b8e5-44cd-b88e-ef87e85e7228_2202x906.png)

A role test is not a direct implementation comparison.

It is tempting to describe it as “testing two implementations of the same interface against each other.” That description is close enough to be understandable, but it is not precise enough to be useful as a design idea.

If we frame role tests that way, one implementation can accidentally become the reference implementation, and the other one becomes a copy. Sometimes that is useful, but it is not the core of the idea.

A better framing is this:

> We define the expected behaviour of the role once, then run that same behaviour against every implementation.

So instead of saying:

> `InMemoryCustomerRepository` behaves like `SqlCustomerRepository`.

We want to say:

> `InMemoryCustomerRepository` satisfies `CustomerRepositoryRoleShould`.  
> `SqlCustomerRepository` satisfies `CustomerRepositoryRoleShould`.

The role is the reference. Not one implementation.

That changes the design conversation. If the SQL implementation and the in-memory implementation disagree, the answer is not automatically “make the in-memory implementation match SQL.” Maybe the in-memory version is wrong. Maybe the SQL implementation exposes accidental behaviour. Maybe the interface is hiding two different roles. Maybe the role test is missing an important rule.

The role test is not there to crown one implementation as truth. It is there to make the shared behavioural contract explicit.

It is also not mainly a trick to reduce duplicated tests.

Reducing duplication is a useful consequence. If two implementations need to satisfy the same behaviour, reusing the same tests is obviously better than copying test cases. But that is not the deepest reason role tests matter.

The deeper reason is that they force the team to state the behaviour of the role once, clearly, and then hold every implementation to that shared meaning.

[![Image 6](https://substackcdn.com/image/fetch/$s_!nim0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65d9ac66-52c7-4f95-b749-e47ed85b1820_1024x559.png)](https://substackcdn.com/image/fetch/$s_!nim0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65d9ac66-52c7-4f95-b749-e47ed85b1820_1024x559.png)

A role does not usually appear because we sat down and invented an interface in isolation.

Very often, it appears because a client object needs help.

A service needs somewhere to save a customer. A use case needs a way to publish an event. A policy needs a source of time. A workflow needs something that can charge a payment. In each case, the client is not asking for a concrete class first. It is asking for a collaborator that can play a useful role in a larger behaviour.

![Image 7](https://substackcdn.com/image/fetch/$s_!0Ypj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bbfe92e-c360-49ba-9246-333f27e574b3_4122x236.png)

That is why role tests fit naturally with test-driven design.

Imagine we are testing `RegisterCustomer`.

At first, the test does not need a database. It only needs to express that, once the customer is registered, something must remember that customer. That need may first appear as a test double. Later, it becomes a `CustomerRepository` interface. Later still, the role test captures what all repositories must honour.

At that moment, the test is not only describing a method call. It is starting to discover a role.

The interface may be written later, but the role starts appearing from use.

This is why the word “client” matters. A role is not defined only by the object that implements it. It is also shaped by the clients that depend on it. The contract exists between both sides: the client should only rely on the role’s advertised responsibilities, and the implementation should satisfy them.

This is a useful way to think about mock objects too. The important idea is not that we are mocking a class that already exists. The important idea is that the client’s interactions reveal what kind of collaborator it needs. The messages sent to a test double can help us discover a role, and a role test can later protect that role across implementations.

That changes how we think about interfaces.

A good interface is not just a list of operations an implementation happens to provide. It is a description of what clients need from a collaborator.

That is exactly the situation behind our small `CustomerRepository` example. We should not read the repository interface as something invented from the database outward. We should read it as something discovered from the needs of a client that wants to register, update, or retrieve customers.

This also connects role tests with substitutability. If several adapters claim to satisfy the same role, clients should not be affected by which adapter they receive. Each adapter may work differently inside, but all of them must honour the same behavioural contract.

That is the design pressure role tests create.

They are not only checking implementation compatibility. They are checking whether the role discovered from client needs remains stable across the objects that claim to fulfil it.

[![Image 8](https://substackcdn.com/image/fetch/$s_!NaLI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47c41c3c-637e-4edc-a5ef-f5a1d605962b_1731x1448.png)](https://substackcdn.com/image/fetch/$s_!NaLI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47c41c3c-637e-4edc-a5ef-f5a1d605962b_1731x1448.png)

[![Image 9](https://substackcdn.com/image/fetch/$s_!8NTQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b7f8f14-2964-4a63-9394-f1de6fe57548_1223x1232.png)](https://substackcdn.com/image/fetch/$s_!8NTQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b7f8f14-2964-4a63-9394-f1de6fe57548_1223x1232.png)

We will use a repository because the example is familiar, not because role tests are mainly about repositories.

The same idea applies to clocks, payment gateways, event publishers, file adapters, HTTP clients, caches, notification senders, search adapters, or any other interface with meaningful substitution pressure.

Let us use a small domain.

Now we need to decide how the role represents the result of a lookup.

[![Image 10](https://substackcdn.com/image/fetch/$s_!uHOL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8273aca1-96c0-44f4-b083-784b99f44bd8_1024x559.png)](https://substackcdn.com/image/fetch/$s_!uHOL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8273aca1-96c0-44f4-b083-784b99f44bd8_1024x559.png)

In Kotlin, I prefer making absence explicit with a sealed result rather than returning `null` or introducing a `MissingCustomer` null object. A `null` return can be simple, but it hides meaning. A null object can be useful in some domains, but it can also create an object that looks like a customer while representing the absence of one. A sealed result makes the contract explicit: a lookup either found a customer or it did not.

The repository interface becomes:

Now the absence case is part of the role’s language. The role does not say “maybe there is a customer, maybe there is `null`.” It says “a lookup has two possible outcomes: found or missing.”

That is not a detail. It is part of the behavioural contract clients are allowed to rely on.

Now we write the role test. In this example, I will express it as a Kotlin interface with default test methods.

That is not a requirement of role testing. It is only a convenient way to write this kind of reusable behavioural suite in Kotlin with JUnit 5.

The important idea is not that the role test is an interface, an abstract class, or a specific framework feature. The important idea is that the same behavioural test suite can be executed against every implementation of the role.

Using an interface keeps the example aligned with the idea we are testing: `CustomerRepositoryRoleShould` describes the behaviour any `CustomerRepository` implementation must satisfy.

In the example, each test follows Arrange, Act, Assert. That is not a separate concept in role testing. It is simply the test structure I will use to keep each behavioural expectation readable. Role tests work best when they are boring and explicit: set up the implementation, exercise the role, and assert the externally visible behaviour.

This test does not say anything about maps, SQL, transactions, files, HTTP calls, JSON, or connection pools. It only describes behaviour that should be true from the outside.

That is the point.

A role test protects behaviour, not implementation.

The naming convention is also intentional. The `Should` suffix belongs to the test interface, not to each individual test method.

That gives us a specification such as `CustomerRepositoryRoleShould`, where each method completes the behavioural idea:

> `CustomerRepositoryRoleShould` find saved customer by id.  
> `CustomerRepositoryRoleShould` return missing when customer does not exist.  
> `CustomerRepositoryRoleShould` keep saved customers separated by id.

This keeps the individual test names short while preserving the idea that the role itself is the subject of the specification.

[![Image 11](https://substackcdn.com/image/fetch/$s_!uzo_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb1f2c6d-446d-48e2-bfac-c8d0130eb068_2211x1096.png)](https://substackcdn.com/image/fetch/$s_!uzo_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb1f2c6d-446d-48e2-bfac-c8d0130eb068_2211x1096.png)

Now we can create an in-memory implementation.

Its test class is small because the behavioural tests already live in `CustomerRepositoryRoleShould`.

Now imagine we also have a SQL implementation.

The SQL repository should not need to expose every detail of how a `ResultSet` becomes a domain result. Its responsibility is to execute the SQL query and use its internal machinery to translate the result into the repository’s domain language.

That mapping responsibility can be separated without making it part of the repository’s public boundary.

Notice that `SqlCustomerLookupMapper` is not injected into the repository. That is intentional.

It is an internal implementation detail of the SQL adapter, not a peer of the `CustomerRepository` role. Extracting a collaborator does not automatically mean promoting it to the constructor boundary.

This matters for the article because it shows the same design principle at a smaller level.

`CustomerRepository` is the role shared by multiple implementations. `SqlCustomerLookupMapper` is not part of that role. As shown here, the mapper is private and exercised through the SQL repository behaviour. If it grows enough to deserve direct tests, that would be a signal to revisit its visibility and design.

That distinction is important.

The role test protects the shared behaviour of `CustomerRepository`.

The lookup mapper supports one concrete implementation.

The SQL test reuses the same role test.

The concrete test class is also responsible for test isolation. The shared role test defines behaviour, but each implementation-specific test class must create a clean, known state for that implementation.

For an in-memory implementation, creating a new instance may be enough. For a database-backed implementation, the concrete test class must clean, migrate, recreate, or otherwise isolate the database state before each test. Without that isolation, one test can leak state into another, and the role test stops being a reliable specification.

Now both implementations must satisfy the same behavioural contract.

[![Image 12](https://substackcdn.com/image/fetch/$s_!NXiA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffdb6c2d8-55d1-4997-97e9-92119c319f42_1024x559.png)](https://substackcdn.com/image/fetch/$s_!NXiA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffdb6c2d8-55d1-4997-97e9-92119c319f42_1024x559.png)

The in-memory implementation can use a map. The SQL implementation can use a database and an internal lookup mapper. The role test does not care because those are implementation decisions, not role-level promises.

The same would be true if the second implementation were file-based, HTTP-based, cache-backed, or provided by another storage engine. The example uses an in-memory repository and a SQL repository because they are easy to understand, not because role tests are only about fakes or repositories.

This is where role tests become practical. They let us write the behavioural specification once, then reuse it against every implementation that claims to satisfy the same abstraction.

The important part is not that we used a Kotlin test interface. The same idea could be implemented with an abstract test class, parametrized tests, composition, or another mechanism supported by the testing framework.

The mechanism is secondary.

The reusable behavioural contract is the point.

[![Image 13](https://substackcdn.com/image/fetch/$s_!Dv-I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1215d269-7258-45d0-848d-9dc7ce2ec0df_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Dv-I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1215d269-7258-45d0-848d-9dc7ce2ec0df_1024x559.png)

[![Image 14](https://substackcdn.com/image/fetch/$s_!cvHp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2cbea108-22dd-4946-ad63-1e34c3350bfc_1024x559.png)](https://substackcdn.com/image/fetch/$s_!cvHp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2cbea108-22dd-4946-ad63-1e34c3350bfc_1024x559.png)

Fakes are a useful example, but they are not the whole story.

Role tests are useful whenever several implementations claim to satisfy the same interface.

For example, a `CustomerRepository` may have several implementations:

*   `InMemoryCustomerRepository`

*   `SqlCustomerRepository`

*   `FileCustomerRepository`

*   `HttpCustomerRepository`

Only one of those implementations may be a test double. Some may be production adapters. Some may exist because the system is migrating from one storage mechanism to another. Some may exist because different deployments use different infrastructure. Some may exist because the same product supports different integration modes.

The point is not whether one implementation is “real” and another is “fake”.

The point is that all of them claim to play the same role.

If they do, they should honour the same behavioural contract.

A fake repository that passes the same role test as the SQL repository is a common and useful example because it prevents the fake from becoming a fantasy object that only works in tests. But the same reasoning applies to any pair or group of implementations.

A filesystem-backed repository and a SQL-backed repository may also need to satisfy the same role. A sandbox payment gateway and a production payment gateway may also need to satisfy the same role. A system clock and a fixed clock may also need to satisfy the same role, at least for the subset of behaviour that belongs to the clock abstraction. A message publisher backed by Kafka and another backed by an in-memory bus may also need to satisfy the same role.

In all these cases, the role test is not about fakes. It is about substitutability.

[![Image 15](https://substackcdn.com/image/fetch/$s_!bag2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0da44b22-1908-434d-88d9-f283570c2824_1024x559.png)](https://substackcdn.com/image/fetch/$s_!bag2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0da44b22-1908-434d-88d9-f283570c2824_1024x559.png)

If a client depends on `CustomerRepository`, the client should not need to know whether the implementation is backed by memory, SQL, a file, or an external service. Each implementation may work differently inside, but all valid implementations must preserve the behaviour promised by the role.

That is what the role test protects.

It does not remove the need for implementation-specific tests. A SQL repository still needs tests around migrations, mapping, transactions, constraints, or integration with the database. A filesystem repository may need tests around paths, permissions, and serialization. An HTTP adapter may need tests around status codes, retries, and network failures.

Those tests matter, but they are not role tests.

The role test protects the shared behaviour.

The implementation-specific tests protect the implementation-specific responsibilities.

This distinction is important because otherwise the idea can be read as if role testing were mainly a way to keep fakes honest. That is one valuable use case, but it is only an example of the larger idea.

Role testing applies whenever an interface represents a role and more than one implementation claims to fulfil it.

A role test should include behaviours that all valid implementations must share.

A useful way to decide whether something belongs in a role test is to ask two questions:

*   Under what conditions is this responsibility valid?

*   What should be true after the responsibility has been used?

For `CustomerRepository`, “when a customer is saved” is the condition we set up, and “the same customer can later be found by id” is the aftereffect we expect. That is the kind of behaviour a role test should capture.

The role test does not discover the contract by itself. It makes explicit the part of the contract that the team has decided clients are allowed to rely on.

For a repository, that may include rules such as:

*   A saved customer can be found by id.

*   An unknown customer produces a missing lookup result.

*   Two customers with different ids remain independent.

*   Saving a customer preserves the relevant customer data.

*   Saving the same id twice has a defined behaviour, if clients rely on that.

*   Invalid input is rejected consistently, if that belongs to the role.

The most important phrase is “if that belongs to the role.”

Not every difference between implementations is a contract violation. Some differences are implementation details.

A SQL repository may use transactions while an in-memory repository does not. A database-backed adapter may care about migrations, indexes, isolation levels, or connection handling. Those details matter, but they do not automatically belong in the role test.

The example role test above does not define all possible repository behaviours. For instance, it does not define what happens when the same customer id is saved twice. That is deliberate. A role test should grow only when clients need that behaviour to be part of the contract.

If clients rely on saving the same id twice replacing the previous customer, that belongs in the role test. If clients rely on duplicate saves failing, that belongs in the role test. If clients do not rely on either behaviour, we should be careful not to smuggle in one implementation’s accidental behaviour as if it were part of the role.

The role test should stay at the level of meaning. It should answer one question:

> What must every valid implementation make true for its clients?

Not this one:

> How does this implementation work internally?

There is another important distinction here: the role test should not collect everything implementations happen to share. It should capture only the behaviours clients are allowed to rely on.

For a repository, role tests often focus on persistence semantics. For a clock, they may focus on time behaviour. For a payment gateway, they may focus on how payment requests are represented and how failures are reported. For a message publisher, they may focus on what is published and when.

The stronger the role, the easier it is to test. The weaker the role, the more the test exposes confusion.

That confusion can be useful. Sometimes the difficulty of writing a role test is feedback that the interface does not yet mean anything precise.

![Image 16](https://substackcdn.com/image/fetch/$s_!J05A!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ed8b228-85c3-4579-b1b2-8aed26bd57a5_4816x652.png)

A role test should not become a dump of every behaviour of every implementation.

That is a common mistake.

The role test is not the place for SQL-specific behaviour, cache-specific behaviour, file-system-specific behaviour, or performance assumptions unless those concerns are part of the role being promised.

For example, these do not belong in a generic `CustomerRepositoryRoleShould`:

*   Creating the customers table

*   Using a specific SQL index

*   Retrying deadlocks

*   Serializing customer as JSON

*   Storing customer names in lowercase

*   Verifying that the SQL lookup mapper calls `resultSet.next()`

Some of those behaviours may need tests. But they are not role tests for `CustomerRepository`. They are implementation tests for a specific adapter or one of its internal collaborators.

This separation matters because a role test protects shared meaning, while an implementation test protects implementation-specific responsibilities.

Mixing them creates noise. It also makes the reusable test suite less reusable.

The role test should be as abstract as the role, and no more concrete than necessary.

That also means role tests are not always worth adding. If there is no meaningful substitution pressure, a role test may add more ceremony than value. A single implementation behind an interface that nobody substitutes, nobody discovers from client needs, and nobody expects to vary may not need a role test. In that case, the better question might be whether the interface itself is carrying enough design value.

[![Image 17](https://substackcdn.com/image/fetch/$s_!MH4V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95c8a2ec-87c7-46ba-b962-42ddfd323497_1110x2300.png)](https://substackcdn.com/image/fetch/$s_!MH4V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95c8a2ec-87c7-46ba-b962-42ddfd323497_1110x2300.png)

Role tests are not only a testing technique. They also push on design.

They force a question that object-oriented design often avoids:

> What role is this object playing?

That question is stronger than:

> What class is this?

A class is a piece of code. A role is a responsibility in a collaboration.

This is why role tests fit naturally with object-oriented design. Objects are not just containers of state. They participate in behaviour, collaborate with other objects, send messages, and make promises to their clients.

A role test captures one of those promises.

This is also why role tests can reveal weak abstractions. If an interface is hard to role-test, maybe the role is not clear. If every implementation needs exceptions to the shared tests, maybe the interface is hiding several different concepts. If the role test has to know too many implementation details, maybe the abstraction is leaking. If one implementation passes but another cannot, maybe one of them is not respecting the real constraints of the role, or maybe the role itself is poorly defined.

The `SqlCustomerLookupMapper` example also shows something useful about design boundaries. Extracting a collaborator does not automatically make it part of the shared role. A mapper may improve the SQL adapter’s internal design, but clients of `CustomerRepository` should not know it exists. The role test should therefore ignore it.

The point is not that role tests magically produce good design. They do not. The point is that they create useful pressure.

They make vague contracts harder to ignore.

They also remind us that object-oriented design is not mainly about drawing class boxes. It is about the roles objects play in collaboration. When we test a role, we are not only testing an API surface. We are testing a promise made to clients.

That promise is what allows substitution to remain safe.

![Image 18](https://substackcdn.com/image/fetch/$s_!LnUj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89724ef9-9d3c-46a9-9c21-2cfe4b631212_3652x748.png)

The SQL implementation is not automatically the truth. The in-memory implementation is not automatically the truth either. The same applies to any other implementation: file-based, HTTP-based, cache-backed, sandbox, production, or fake.

The role is the truth.

If two implementations disagree, the answer is not automatically “make one match the other.” Sometimes one implementation exposed accidental behaviour that should not belong to the role. Sometimes another implementation is too permissive. Sometimes the interface is wrong. Sometimes there are two roles hiding behind one interface.

The role test should help clarify the contract, not blindly copy one implementation.

[![Image 19](https://substackcdn.com/image/fetch/$s_!O2KM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cd2810b-ed64-4fa6-88d9-e43680c9d8f6_1024x559.png)](https://substackcdn.com/image/fetch/$s_!O2KM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cd2810b-ed64-4fa6-88d9-e43680c9d8f6_1024x559.png)

This happens when the test starts asking how the implementation works instead of what the role promises.

For example, tests such as “store customer in internal map”, “call insert statement”, “open database connection”, or “use this lookup mapper” may be valid implementation tests, but they are not role tests.

A role test should stay outside the object and observe behaviour.

[![Image 20](https://substackcdn.com/image/fetch/$s_!m-YP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04aa59b0-65e8-4685-b3ee-b4c8f5d3b5e1_1024x559.png)](https://substackcdn.com/image/fetch/$s_!m-YP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04aa59b0-65e8-4685-b3ee-b4c8f5d3b5e1_1024x559.png)

If the role test becomes huge, the role may be too broad.

For example:

This is no longer just persistence. It mixes querying, exporting, and notification-like behaviour. A role test for this interface will probably feel awkward because the interface itself is awkward.

[![Image 21](https://substackcdn.com/image/fetch/$s_!uto6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faaf20eac-4146-49f2-b243-32a5604a8251_1024x559.png)](https://substackcdn.com/image/fetch/$s_!uto6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faaf20eac-4146-49f2-b243-32a5604a8251_1024x559.png)

Test friction can be design feedback.

Role tests do not replace integration tests.

A role test asks whether an implementation satisfies the behaviour expected from a role. An integration test asks whether real parts work together in a real or realistic environment.

A SQL repository can pass its role test and still fail in production because of configuration, migrations, permissions, connection pooling, infrastructure, or deployment mistakes. An HTTP adapter can pass the shared role test and still fail because of authentication, timeouts, status-code handling, or incompatible API changes.

Role tests are valuable, but they are not a complete testing strategy.

Role tests are useful when there is a meaningful role. They are not a reason to create interfaces everywhere.

If there is only one implementation and no meaningful substitution pressure, an interface may add ceremony without value.

The sequence should not be this:

> I want a role test, therefore I need an interface.

It should be this:

> There is a role with multiple implementations or important substitution pressure, therefore a role test may help.

Otherwise, role tests become another form of test architecture theatre.

Because many examples use abstract test classes, test interfaces, or parametrized tests, it is easy to confuse the idea with the mechanism.

That confusion leads to statements such as:

> A role test is an abstract test class.

Or:

> A role test is a test interface.

Neither statement is quite right.

A role test can be implemented with an abstract class, a test interface, parametrized tests, composition, or another mechanism. The role test is the reusable behavioural contract. The mechanism is only the way we share and execute that contract.

This distinction matters because different teams and frameworks may prefer different mechanisms. The mechanism should serve the idea, not define it.

[![Image 22](https://substackcdn.com/image/fetch/$s_!VQaP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcefb0dad-d48c-4402-9912-6f69c8350acd_4068x1276.png)](https://substackcdn.com/image/fetch/$s_!VQaP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcefb0dad-d48c-4402-9912-6f69c8350acd_4068x1276.png)

A role test is a small idea with a large design consequence.

It says that an abstraction means something. Not only that it has methods, not only that the compiler accepts it, and not only that different implementations have the same shape.

An interface gives us shape. A role test gives us behaviour.

When multiple implementations pass the same role test, we gain confidence that they are not merely compatible with the compiler. They are compatible with the role they claim to play.

This matters whenever implementations can drift: a SQL repository and a filesystem repository, a production adapter and a fake, a real gateway and a sandbox gateway, a Kafka publisher and an in-memory publisher, a system clock and a fixed clock.

In all of those cases, the danger is not only that one implementation has a bug. The deeper danger is that the role itself becomes vague.

Role tests help prevent that vagueness from hiding behind clean method signatures. They make the contract executable. They give every implementation a standard to satisfy. They give adapters a shared behavioural baseline. And they give design conversations a sharper question:

> What does this role actually promise?

That is the question worth keeping.

Because object-oriented design is not only about classes. It is about responsibilities, collaborations, and roles that mean something.

A role test is one way of making that meaning visible.

*   Rebecca Wirfs-Brock, Brian Wilkerson, and Lauren Wiener, _Designing Object-Oriented Software_

*   Rebecca Wirfs-Brock and Alan McKean, _Object Design: Roles, Responsibilities, and Collaborations_

*   Steve Freeman and Nat Pryce, _Growing Object-Oriented Software, Guided by Tests_

[https://www.growing-object-oriented-software.com/](https://www.growing-object-oriented-software.com/)

*   Steve Freeman, Nat Pryce, Tim Mackinnon, and Joe Walnes, _Mock Roles, not Objects_  
[https://jmock.org/oopsla2004.pdf](https://jmock.org/oopsla2004.pdf)

*   Manuel Rivero, _Role tests for implementation of interfaces discovered through TDD_  
[https://codesai.com/posts/2022/04/role-tests](https://codesai.com/posts/2022/04/role-tests)

*   Manuel Rivero, _Example of role tests in Java with JUnit_  
[https://codesai.com/posts/2022/08/role-tests-junit](https://codesai.com/posts/2022/08/role-tests-junit)

*   jMock, _Articles and Papers_  
[https://jmock.org/articles.html](https://jmock.org/articles.html)
