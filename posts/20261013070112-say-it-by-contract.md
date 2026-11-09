Title: Say it by contract

URL Source: http://emmanuelvalverderamos.substack.com/p/say-it-by-contract

Final URL: https://emmanuelvalverderamos.substack.com/p/say-it-by-contract

Published Time: 2026-10-13T07:01:12+00:00

Markdown Content:
You would not board a flight with a ticket that says “probably Madrid, probably tomorrow, probably your seat.” You would not sign a mortgage where the bank’s obligations live in a hallway conversation. You would not accept a job offer where the salary depends on how payroll interprets your name next month.

Yet software is full of agreements like that. A function receives a value that is supposed to be a valid identifier. A method receives a number that is supposed to be positive. A module exposes an operation that only works when the object is in a certain state, but the public interface does not say so. The code compiles, the tests pass, the deployment goes out, and production breaks. The team calls it an edge case.

Many times, it was not an edge case. It was a hidden clause.

_Design by Contract_ (DbC), introduced by Bertrand Meyer through Eiffel and his wider method of object-oriented software construction, gives us a discipline for making those clauses explicit. A software element should say what it expects, what it promises, and what must remain true while it works. Meyer frames those ideas through assertions: preconditions, postconditions, and invariants. The deeper lesson is not syntax. It is responsibility.

This article is language-agnostic. The examples use Kotlin only because Kotlin gives us concise tools for domain-specific types, sealed outcomes, exhaustive `when` expressions, and explicit argument or state checks. The same thinking applies in Java, C#, TypeScript, PHP, Python, Rust, Swift, Go, Scala, and many other languages.

A contract is not a guard clause with better manners. A contract is the public shape of responsibility.

_Design by Contract_ (DbC) is a way of designing software collaboration through explicit obligations, benefits, and semantic promises.

A contract answers three questions:

*   **Precondition:** what must be true before an operation is called?

*   **Postcondition:** what must be true after an operation completes successfully?

*   **Invariant:** what must remain true for an object, module, aggregate, or abstraction across its observable lifetime?

Meyer’s method treats contracts as part of a broader reliability discipline. They connect classes, abstract data types, inheritance, assertions, exception handling, documentation, and testing. They are not just runtime checks.

Modern languages express contract thinking through types, constructors, factories, assertions, result types, sealed unions, encapsulation, contract tests, boundary parsers, and behavioral interface rules. The mechanism changes. The responsibility does not.

The most useful distinction is this:

*   Invalid external input is normal and should be translated at the boundary.

*   Expected business rejection is part of the domain conversation.

*   Broken internal assumptions are contract violations.

If every unhappy path becomes an exception, the contract is not precise enough.

1.   [Hidden clauses are still clauses](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7hidden-clauses-are-still-clauses)

2.   [Meyer’s bigger idea](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7meyers-bigger-idea)

3.   [Correctness needs a specification](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7correctness-needs-a-specification)

4.   [Assertions put the what beside the how](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7assertions-put-the-what-beside-the-how)

5.   [A class is a small language](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7a-class-is-a-small-language)

6.   [Preconditions, postconditions, and invariants](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7preconditions-postconditions-and-invariants)

7.   [Every obligation is also a benefit](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7every-obligation-is-also-a-benefit)

8.   [More reliability by checking less](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7more-reliability-by-checking-less)

9.   [Invariants protect abstractions across time](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7invariants-protect-abstractions-across-time)

10.   [Contracts inside algorithms](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7contracts-inside-algorithms)

11.   [Demanding contracts and tolerant contracts](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7demanding-contracts-and-tolerant-contracts)

12.   [Command-query separation](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7command-query-separation)

13.   [Boundary validation is not domain contracting](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7boundary-validation-is-not-domain-contracting)

14.   [Exceptions, failures, and broken contracts](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7exceptions-failures-and-broken-contracts)

15.   [Subtyping is subcontracting](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7subtyping-is-subcontracting)

16.   [The Ariane lesson](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7the-ariane-lesson)

17.   [Translating contracts into modern languages](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7translating-contracts-into-modern-languages)

18.   [Case study: a Kotlin reservation model](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7case-study-a-kotlin-reservation-model)

19.   [Tests as contract witnesses](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7tests-as-contract-witnesses)

20.   [Kotlin contracts are not Meyer contracts](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7kotlin-contracts-are-not-meyer-contracts)

21.   [When contracts hurt](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7when-contracts-hurt)

22.   [Practical checklist](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7practical-checklist)

23.   [Conclusion](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7conclusion)

24.   [References](https://emmanuelvalverderamos.substack.com/p/say-it-by-contract?open=false#%C2%A7references)

[![Image 1](https://substackcdn.com/image/fetch/$s_!v6DL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17b5e4d-6663-4e5d-8d9b-bca8a4e2fcb1_1024x559.png)](https://substackcdn.com/image/fetch/$s_!v6DL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17b5e4d-6663-4e5d-8d9b-bca8a4e2fcb1_1024x559.png)

A method named `reserveSeats` receives an identifier and a number.

That signature looks harmless. It hides a room full of questions.

*   What makes a flight identifier valid?

*   Can `seats` be zero?

*   Can `seats` be negative?

*   Is there a maximum number of seats per reservation?

*   What happens when the flight does not exist?

*   What happens when the flight exists but has no capacity?

*   Does the operation mutate state?

*   Does it return a reservation?

*   What must be true after it succeeds?

*   What must remain true even when it rejects the request?

Those facts often live in different places: tests, old tickets, controller validations, database constraints, issue comments, monitoring alerts, and the memory of the developer who first wrote the feature. The operation has rules, but the rules are not part of the operation’s visible agreement.

That is the hidden clause problem. A hidden contract is still a contract. It is just a contract the code cannot help you enforce, explain, or test directly.

_Design by Contract_ is not mainly about adding more checks. It is about moving the agreement from rumor to code.

[![Image 2](https://substackcdn.com/image/fetch/$s_!Lhxr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08c88338-ce53-4705-9196-610f367e8716_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Lhxr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08c88338-ce53-4705-9196-610f367e8716_1024x559.png)

A shallow explanation of _DbC_ starts with syntax. It says: use `require`, `ensure`, and invariants.

That is not wrong, but it is too small. Meyer’s argument is larger than a syntax feature. In _Object-Oriented Software Construction_, object technology is presented through connected ideas: class as structure and type, contract as reliability discipline, abstract data type as semantic foundation, and inheritance as classification and reuse.

The map matters because it prevents a weak interpretation of _DbC_.

*   A class gives software a shape.

*   A contract gives that shape obligations.

*   An abstract data type gives those obligations meaning.

*   Inheritance must preserve that meaning when behavior is reused or specialized.

This is the article’s compass.

Without that compass, _DbC_ becomes “validation with fancy names.” With it, contracts become part of how we design, specify, document, test, reuse, and evolve software.

Meyer also separates the method from the notation. Eiffel made contracts executable and visible in a direct way, but the idea is not trapped inside Eiffel. A Kotlin value object, a Rust newtype, a TypeScript parser, a C# record, a Java sealed hierarchy, a PHP readonly object, or a Python dataclass can all carry pieces of contract thinking when used deliberately.

The question is not, “Does my language have Eiffel syntax?” The question is, “Who owes what to whom, and can the reader see it?”

Software correctness is not a feeling.

A program is not correct because it compiles. It is not correct because it has tests. It is not correct because the team likes the design. It is correct relative to a specification.

This idea predates _DbC_. C. A. R. Hoare’s work on axiomatic programming gave us a way to reason about programs through assertions before and after execution. A simplified form is commonly written like this:

{P} A {Q}

Read it as: if operation `A` starts in a state where `P` is true, then after `A` completes successfully, `Q` should be true.

In that framing:

*   `P` is the precondition.

*   `Q` is the postcondition.

*   The operation is judged by the relationship between them.

Meyer adapts this style of reasoning into object-oriented design. The everyday lesson is not that every codebase must become a formal proof system. The lesson is that an operation without a specification can only be judged by accident.

A method name tells us what the author hoped the operation would mean. A contract tells us what the operation is allowed to mean.

A program normally tells us how something is done.

It assigns values, calls functions, sends messages, persists data, transforms input into output, and changes state. The implementation is the how.

A contract adds the what. It says what must be true before the work starts, what must be true after it finishes, and what must remain true around the operation. Assertions place part of the specification next to the implementation.

That placement is practical. If the specification only lives in a requirements document, it can drift away from the code. If it only lives in tests, it may cover examples without exposing the full agreement. If it only lives in someone’s memory, it disappears when that person leaves. If it lives in the software text, readers can see the operation and its obligations together.

Assertions serve several jobs:

*   They guide implementation.

*   They document behavior close to the code.

*   They support testing and debugging by making violations visible.

*   They make exception handling more precise because the system can distinguish broken assumptions from normal outcomes.

*   They make reuse safer because operating conditions travel with the reusable element.

The word assertion can sound like a runtime mechanism. The deeper idea is methodological. A runtime assertion may be enabled or disabled. The contract remains part of the design.

[![Image 3](https://substackcdn.com/image/fetch/$s_!YLbX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37d5ac1d-97e7-429c-a812-7984475aac74_1024x559.png)](https://substackcdn.com/image/fetch/$s_!YLbX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37d5ac1d-97e7-429c-a812-7984475aac74_1024x559.png)

Imagine a stack with these operations:

```
put
remove
item
empty
count
```

The list is not enough.

Without semantics, `put` could insert at the top, insert at the bottom, ignore the value, duplicate it, or remove something else first. `remove` could remove the newest item, the oldest item, or a random item. `item` could return the top item, the bottom item, or the last inspected item.

Names suggest meaning. They do not prove it.

This is where Meyer’s connection between abstract data types and assertions becomes essential. An abstract data type is not just a name and a list of functions. It includes semantic properties: axioms, preconditions, and relationships between operations.

For a stack, a meaningful contract might say:

*   A new stack is empty.

*   After putting an item on a stack that can accept it, `item` returns that item.

*   After putting an item, `count` increases by one.

*   `remove` is only valid when the stack is not empty, unless the operation deliberately models empty removal as a normal outcome.

*   Representation details are private.

Two stack implementations may differ completely. One may use an array and an index. Another may use linked nodes. The client should not care. The client cares that the observable behavior satisfies the same contract.

A class is a small language for a concept. The contract is its grammar.

[![Image 4](https://substackcdn.com/image/fetch/$s_!Cy0t!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0cd088ad-6cf3-4351-874d-135148019e38_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Cy0t!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0cd088ad-6cf3-4351-874d-135148019e38_1024x559.png)

The three core contract elements are simple, but they become powerful when responsibility is assigned carefully.

A **precondition** states what must be true before an operation is called. It binds the client. If the precondition is violated, the call is invalid.

A **postcondition** states what must be true after an operation completes successfully. It binds the supplier. If the postcondition is violated, the supplier failed.

An **invariant** states what must remain true for the object, module, aggregate, or abstraction across its observable states. It binds the implementation. If the invariant is violated after creation or after an exported operation, the supplier has exposed an inconsistent abstraction.

The relationship is easier to see as a responsibility flow.

For a flight reservation model:

*   A seat request must represent a valid reservation size.

*   Available seats must never be negative.

*   If a reservation is accepted, availability decreases by exactly the requested number of seats.

*   If there are not enough seats, the request is rejected as a domain outcome.

The last point matters. “Not enough seats” is not automatically a broken contract. In a real reservation system, capacity can change between reading availability and requesting seats. A customer asking for seats on a full flight has not necessarily misused the program. The business simply says no.

A precise contract distinguishes three things:

*   Invalid call.

*   Valid call with rejected business outcome.

*   Supplier failure.

Design improves when those three things stop sharing the same bucket.

Meyer’s contract metaphor works because obligations and benefits are symmetrical.

The client’s obligation is the supplier’s benefit. If the client satisfies the precondition, the supplier can write simpler code because it may assume the condition holds. The supplier’s obligation is the client’s benefit. If the supplier satisfies the postcondition, the client can rely on the promised result without inspecting private details.

That symmetry changes code.

Without a contract, every collaborator becomes suspicious. Every layer checks everything. Every method half-trusts its inputs. Every call is surrounded by nervous code.

With a contract, we can trust the right things.

Not everything. The right things.

A contract is like a bridge with a weight limit. The limit is not there to annoy the driver. It is there so the bridge can be trusted. Once the driver respects the limit, the bridge must do its job. Once the bridge promises to carry the load, the driver does not need to inspect the steel beams before crossing.

Software has the same deal. Once the boundary has turned an external number into a valid seat request, the domain does not need to wonder whether the request is zero. The type, constructor, parser, or validation layer has already made that impossible. Once an availability object exists, the rest of the model does not need to wonder whether it represents negative seats. The invariant should have rejected that state before the object became observable.

A good contract does not add noise. It removes questions.

The phrase “checking less” sounds dangerous until we define it.

It does not mean “trust everything.” It means “do not check the same responsibility everywhere.”

A common defensive style says:

*   Validate at the controller.

*   Validate again in the service.

*   Validate again in the domain object.

*   Validate again in the repository.

*   Validate again in the mapper.

*   Add one more check because you never know.

This looks safe at first. Later, one layer changes a rule and another layer does not. The controller allows ten seats, the domain allows nine, the _Application Programming Interface_ (API) documentation says eight, and the database constraint says something else. The checks were supposed to increase safety. They created drift.

_DbC_ asks a sharper question: who owns this condition?

There are several possible answers:

*   The **boundary** owns hostile input translation.

*   The **caller** owns the preconditions of valid internal calls.

*   The **supplier** owns postconditions.

*   The **object or module** owns invariants.

*   The **application** owns workflow decisions.

*   The **infrastructure** owns external failure handling.

The code becomes simpler when those answers are explicit. Defensive programming often treats every collaborator as suspicious. Contract thinking assigns responsibility so collaborators can trust the right agreement at the right boundary.

A precondition or postcondition belongs to a particular operation. An invariant belongs to the abstraction as a whole.

Creation must establish the invariant. Exported operations must preserve it when called in a state satisfying their preconditions and the invariant. If inheritance is involved, inherited invariants also constrain descendants. This is one reason contracts and inheritance cannot be separated cleanly.

This matters because invariants are often misunderstood. An invariant does not necessarily mean every private instruction must preserve the object at every micro-step. A mutable object may temporarily move through an intermediate state while an operation is executing. The discipline is that the object must not expose that broken state through its public boundary. It must be whole when creation finishes, and it must be whole again when exported operations return.

Modern systems stretch this idea beyond classes.

*   An aggregate has invariants.

*   A module has invariants.

*   A database transaction may protect invariants.

*   A distributed workflow may try to preserve invariants through messages, compensations, and eventual consistency.

*   A type can make some invalid states impossible, although not every business invariant fits inside a type system.

The invariant is the abstraction’s spine. If outside code can bend it, the contract is weaker than it looks.

Most practical explanations of _DbC_ stop at preconditions, postconditions, and class invariants. Meyer’s treatment goes deeper. Assertions also help inside algorithms.

A **loop invariant** states what remains true before and after every loop iteration. A **loop variant** is a value that moves in a direction that proves the loop is making progress toward termination.

These ideas matter when correctness depends on non-trivial iteration:

*   Binary search.

*   Parsers.

*   Schedulers.

*   Pricing algorithms.

*   Reconciliation jobs.

*   Migration scripts.

*   Allocation algorithms.

*   Financial calculations.

*   Data structure operations.

Consider binary search in plain language. Before each iteration, the target, if it exists, must still be inside the current search interval. Every step must shrink that interval. The invariant protects the meaning of the interval. The variant, often the interval size, argues that the loop cannot continue forever if the algorithm is correct.

If the interval does not shrink, the algorithm may loop forever. If the invariant is broken, the algorithm may skip the target.

Modern teams do not need to write formal proofs for every loop. They should recognize when a loop carries business-critical meaning. In those places, naming the invariant can prevent subtle bugs.

For simple loops, tests may be enough. For complex loops, the invariant is the flashlight.

A strict contract is not always the best contract. Two styles are useful.

The operation says: “You may only call me when this condition holds.”

For example:

`reserveSeats may only be called when enough seats are available.`
If the caller violates that condition, the caller is wrong. This style works well when the condition truly belongs to the caller, especially inside a trusted domain model or between internal collaborators.

The operation says: “You may call me with a valid request. I will return one of the known outcomes.”

For example:

`reserveSeats may return Accepted or Rejected.NotEnoughSeats.`
This style works well when the condition is part of the normal business conversation. In a reservation system, capacity can change between checking availability and asking for seats. A customer request may be valid even when the business refuses it.

Modern languages give us better tools than raw error codes:

*   Sealed results.

*   Discriminated unions.

*   Result objects.

*   Sum types.

*   Error values with typed payloads.

*   Domain events.

*   Explicit rejection types.

The contract becomes:

*   This request is well-formed.

*   The supplier will attempt the business operation.

*   The result will be one of the known outcomes.

*   Each outcome has its own promise.

That is not weaker than throwing exceptions. It is more precise.

Contracts are easier to understand when commands and queries do not pretend to be the same thing.

A **command** asks the system to do something. It may change state.

A **query** asks the system for information. It should not change the abstract state observable by clients.

Meyer’s command-query separation principle prohibits abstract side effects in functions. A concrete internal change may be acceptable if it does not change what clients can observe through public queries. A query may update a cache, lazily compute a value, or reorganize internal storage. If none of that changes the abstract answer to visible queries, the abstraction remains the same.

A query that changes the answer to another visible query breaks the mental model. Asking a question should not change the answer.

This matters because postconditions should usually be observable. A postcondition such as:

`After reserving 2 seats from 3 available seats, available seats is 1.`
should not require looking into private fields. The client should observe it through a public query, returned state, event, or result.

This also improves tests. A behavior-focused test asks, “What can the client observe after the operation?” It does not ask, “Which private collection did the object mutate?”

The test is a witness, not a spy.

The outside world does not speak your domain language.

HTTP gives you strings and numbers. JSON does not know what a reservation is. A message broker may deliver stale payloads. A database row from an old version may not satisfy today’s model. A third-party API may lie without malice.

The boundary is not a trusted client. The boundary is weather.

The boundary must parse, validate, and translate before the domain receives anything meaningful.

Many systems lose clarity by treating malformed external input, missing application data, expected domain rejection, infrastructure failure, and broken internal state as the same thing.

They are not the same thing.

[![Image 5](https://substackcdn.com/image/fetch/$s_!ccqy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb18beccd-6fb6-4e31-b4f2-62cd30635c3c_922x460.png)](https://substackcdn.com/image/fetch/$s_!ccqy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb18beccd-6fb6-4e31-b4f2-62cd30635c3c_922x460.png)

A contract-aware design keeps those categories separate. The tool can vary: exceptions, result types, railway-oriented programming, typed errors, validation libraries, algebraic data types, or plain objects. The distinction should not vary.

Exceptions are where contract thinking often becomes blurry.

A broken contract and an expected outcome are not the same thing.

Meyer’s framing helps: a routine fails when it cannot fulfill its contract. An exception is the abnormal event that disrupts normal execution. Exception handling is not a license to turn ordinary business alternatives into jumps through the call stack.

If a caller passes an invalid value to an internal operation whose precondition clearly rejects that value, an exception or assertion failure may be appropriate. The program was used incorrectly.

If a supplier finishes an operation and its postcondition is false, an exception or assertion failure may be appropriate. The supplier failed to keep its promise.

If an object exposes a state that violates its invariant, an exception or assertion failure may be appropriate. The abstraction is no longer trustworthy.

If a customer tries to reserve seats and there are not enough seats, that may be a normal business outcome. The caller did not necessarily misuse the program. The business said no.

The useful categories are:

*   **Precondition violation:** invalid call.

*   **Postcondition violation:** supplier defect.

*   **Invariant violation:** inconsistent abstraction.

*   **Expected rejection:** valid business refusal.

*   **Operational failure:** dependency, network, persistence, or platform problem.

Recovery also has a contract. If an operation handles an abnormal situation, it must either restore a meaningful state and retry, or report failure in a way that the caller can understand. Half-recovery is often worse than no recovery because it leaves the abstraction pretending to be alive while its invariant is already broken.

Contracts become sharper when polymorphism enters the room.

If an implementation is used through an interface, it is a subcontractor. It must not make life harder for clients of the interface.

In contract terms:

*   A subtype must not require more than the supertype promised.

*   A subtype must not deliver less than the supertype promised.

*   A subtype must preserve inherited invariants.

*   A subtype must not surprise clients that only know the abstraction.

This aligns with Liskov and Wing’s behavioral subtyping: properties expected of supertype objects should still hold for subtype objects.

A bad language-neutral example:

```
interface DiscountPolicy
    discountFor(customer)

implementation LoyaltyDiscountPolicy
    discountFor(customer)
        require customer is loyal
        return 10 percent
```

The interface says, “I can calculate a discount for a customer.” The implementation says, “Actually, only loyal customers.”

That strengthens the precondition. A caller using the interface cannot know this. The implementation has betrayed the interface.

There are two better designs. One option makes the operation total over all customers:

```
discountFor(customer)
    if customer is loyal
        return 10 percent
    otherwise
        return 0 percent
```

Another option narrows the input type so the contract becomes visible:

```
discountFor(loyalCustomer)
    return 10 percent
```

These designs say different things. The first says, “This policy can answer for every customer.” The second says, “This policy only applies after loyalty has already been established.”

The mistake is the middle ground: a broad interface with a narrow implementation.

This applies beyond classical inheritance. It applies to interface implementations, abstract classes, TypeScript structural types, protocols, traits, typeclasses, adapters, plugin systems, and public APIs.

The review question is simple: an this implementation be used wherever the abstraction is expected without surprising the caller?

If not, the contract is lying.

Ariane 5 Flight 501 is often used as a software cautionary tale because it is dramatic: on June 4, 1996, the launcher failed roughly 40 seconds after the flight sequence began. The inquiry board traced the technical chain to the inertial reference system software. A conversion from a 64-bit floating-point value to a 16-bit signed integer raised an operand error because the value was too large. Both redundant inertial reference systems used the same software and failed for the same reason.

The simple story is “an overflow crashed a rocket.”

The contract story is more useful.

The relevant software came from Ariane 4. The assumption behind the unprotected conversion was valid for Ariane 4’s trajectory but not for Ariane 5’s. The inquiry board noted that the Ariane 5 trajectory data had not been included in the relevant inertial reference system requirements and specification. Jézéquel and Meyer’s “Design by Contract: The lessons of Ariane” makes the software reuse lesson explicit: the reusable module carried an operating condition, but that condition was not attached to the reusable element where reuse needed it.

That does not mean contracts magically prevent disasters. It means reusable software without visible operating conditions is dangerous.

The deeper lesson is not “check every conversion forever.” Engineering always has cost, performance, and complexity trade-offs. The deeper lesson is that a decision not to check something is only defensible when the reason travels with the software element that depends on it.

Invisible assumptions are not free. They accumulate interest.

The method is language-agnostic. The implementation is not.

Eiffel has native contract syntax. Many modern languages do not. Some have strong type systems, sum types, and exhaustive pattern matching. Some rely more on runtime checks. Some provide annotations, macros, libraries, or conventions. Some make illegal states difficult to represent. Some make runtime validation unavoidable.

The contract thinking remains transferable.

[![Image 6](https://substackcdn.com/image/fetch/$s_!l3rs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb35dfb5d-1df6-4145-a72d-7d99979d768c_915x564.png)](https://substackcdn.com/image/fetch/$s_!l3rs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb35dfb5d-1df6-4145-a72d-7d99979d768c_915x564.png)

Translations differ by language:

*   In **Kotlin**, data classes, `require`, `check`, sealed interfaces, exhaustive `when`, and private constructors are useful.

*   In **C#**, records, value objects, nullable reference types, guard clauses, contracts by convention, and result types are common.

*   In **Java**, records, sealed classes, constructor or factory validation, and explicit result objects can express many ideas.

*   In **TypeScript**, compile-time types must be paired with runtime parsing at boundaries because type information does not protect runtime input.

*   In **PHP**, readonly value objects, named constructors, exceptions, and explicit result objects are practical tools.

*   In **Rust**, newtypes, `Result`, enums, ownership, and pattern matching support strong contract expression.

*   In **Python**, dataclasses, type hints, validators, runtime assertions, and clear module boundaries can help, but runtime checks remain important.

*   In **Go**, small interfaces, explicit errors, constructor functions, and package-level encapsulation often carry the agreement.

The point is not to force every language into Eiffel’s shape. The point is to preserve the question: who owes what to whom, and how does the code make that visible?

Now let’s make the idea concrete.

The business rule is small enough to fit in one paragraph: a customer can request seats for a flight. The request must contain a valid number of seats. If enough seats are available, the reservation is accepted and availability decreases by exactly that number. If there are not enough seats, the reservation is rejected and availability remains unchanged.

That gives us:

*   A valid seat request before entering the domain model.

*   Non-negative availability as an invariant.

*   A postcondition for accepted reservations.

*   An expected domain rejection for insufficient capacity.

*   A result type that documents all business outcomes.

`RequestedSeats` makes invalid request sizes impossible inside the domain. `AvailableSeats` protects the non-negative invariant. `FlightId.fromExternal` belongs at the boundary because external text may fail to become a valid identifier.

Kotlin documents `require` as a way to validate input arguments and `check` as a way to validate object or variable state. That distinction maps well to contract thinking: `require` fits caller obligations, while `check` fits supplier state, postconditions, and invariant checks.

This design is immutable. Meyer’s Eiffel examples often use commands that mutate objects and express postconditions through old values and queries. This Kotlin version translates the same contract idea into an immutable state transition: an accepted reservation returns a new `FlightAvailability`.

The contract is visible:

*   `RequestedSeats` rejects invalid request sizes.

*   `AvailableSeats` rejects impossible availability.

*   `reserve` returns either `Accepted` or `NotEnoughSeats`.

*   `Accepted` includes the reservation and updated availability.

*   `NotEnoughSeats` includes current availability, making the rejection state observable.

*   The non-negative availability invariant is owned by `AvailableSeats`, so `FlightAvailability` can compose an already-valid concept.

Notice what is not happening: `NotEnoughSeats` is not an exception. It is a domain decision.

That distinction is the contract.

The outside world gives us strings and numbers. The domain should receive concepts.

The handler separates categories:

*   `InvalidFlightId` is boundary input rejection.

*   `InvalidSeatCount` is boundary input rejection.

*   `FlightNotFound` is an application result.

*   `NotEnoughSeats` is a domain decision.

*   An invariant violation would be a programming defect.

The example is about the contract, not Kotlin. In another language, the shapes would change. The responsibility split should survive.

Tests are not the contract itself. Tests are witnesses.

A contract states the agreement. A good test demonstrates that visible behavior respects that agreement in a meaningful scenario. It should not inspect private fields. It should not mock internal structure. It should not care whether the implementation uses a list, an array, an event, or a private helper.

It should ask what the client can observe. The test code below keeps that witness role visible.

Each test has one reason to fail. The parser tests witness the valid lower boundary, the invalid upper boundary, and invalid construction separately. The reservation tests witness the postcondition about availability, the returned reservation, and the rejected domain outcome without inspecting private representation.

There is no test for private representation because private representation is not part of the client contract. If a test knows too much about the inside, it becomes another hidden clause. It tells the implementation, “I know how you work inside, and I will punish you if you change.”

That is not a witness. That is a hostage note.

Kotlin has a package named `kotlin.contracts`.

The name can mislead.

Kotlin contracts let functions describe certain effects to the compiler, such as returning normally, implying a condition, or calling a lambda in place. The API for declaring custom function contracts remains experimental and requires opt-in.

This can help the compiler reason about nullability after the function returns.

It is useful. It is not Meyer’s _Design by Contract_.

It does not express a domain postcondition such as “an accepted reservation decreases availability by requested seats.” It does not model business rejection. It does not preserve aggregate invariants. It does not decide who owns a condition.

Use Kotlin contracts when they help the compiler understand a small function. Use _Design by Contract_ to design collaboration.

They share a word. They do not share the same scope.

Contracts are powerful because they reduce ambiguity. They hurt when they increase it.

They hurt when the same check appears in every layer without responsibility being clarified. They hurt when expected business outcomes become exceptions. They hurt when a class exposes technical errors instead of domain decisions. They hurt when assertions repeat implementation details instead of stating observable promises. They hurt when a subtype quietly changes what its interface appeared to allow.

They also hurt when they are used as blame. A contract is not a way to say, “You called me wrong, so I do not care.” It is a way to make correct collaboration easier than incorrect collaboration.

Runtime monitoring needs judgment. Some contracts should be checked in development. Some should be checked during tests. Some critical invariants may deserve production monitoring. Some contracts are better expressed through types, construction rules, parsers, or result models. Some postconditions are better witnessed by tests and documentation than checked after every assignment.

There is no useful rule that says “check everything at runtime.” There is no useful rule that says “trust everything because the contract says so.”

The right question is: where does this contract give the most safety for the least confusion?

Use this checklist when reviewing code through a contract lens.

Ask:

*   What must be true before this operation is called?

*   Is that condition a caller obligation, a boundary parsing concern, or an expected business case?

*   What does the operation promise after success?

*   Is the promise visible through returned values, public queries, state transition, or events?

*   What remains true no matter which successful path is taken?

*   Are postconditions expressed through observable behavior rather than private representation?

Ask:

*   Can this abstraction represent an invalid value?

*   Is a primitive hiding a domain concept?

*   Should construction reject invalid values?

*   Should external parsing return a typed rejection, nullable result, or validation result instead of throwing?

*   Does the abstraction expose mutable internals?

*   Can another object break its invariant?

*   Is the invariant established at creation?

*   Is the invariant preserved after exported operations?

Ask:

*   Where does untrusted input become domain data?

*   Are malformed input, missing data, business rejection, and infrastructure failure modeled separately?

*   Does the domain receive concepts or raw transport data?

*   Are external identifiers parsed at the edge?

*   Does the boundary avoid swallowing broad failures?

Ask:

*   Can every implementation accept what the abstraction appears to accept?

*   Does any implementation strengthen the precondition?

*   Does any implementation weaken the postcondition?

*   Does any implementation violate inherited invariants?

*   Should the input type be narrower?

*   Should the result type be richer?

*   Do contract tests verify the behavior expected from all implementations?

Ask:

*   Does the test verify behavior?

*   Does it fail for one clear reason?

*   Does it assert only what matters for that behavior?

*   Does it avoid private state?

*   Does it witness a precondition, postcondition, invariant, or explicit outcome?

The goal is not more ceremony. The goal is fewer hidden clauses.

A lot of software fails because the agreement was never written where the code could see it.

The caller brought the wrong value. The supplier returned less than it promised. The object exposed an impossible state. The subtype changed the deal. The boundary passed weather into the domain and hoped the domain would stay dry.

_Design by Contract_ gives us a sharper language for these failures.

A precondition says: “Bring this.”

A postcondition says: “I will deliver that.”

An invariant says: “I will remain whole.”

Meyer’s deeper lesson is that contracts are not an isolated technique. They connect the class, the abstract data type, the reliability discipline, and inheritance. They bring semantics back into the software text. They make documentation more precise. They make tests more meaningful. They make exception handling less vague. They make reuse safer because operating conditions travel with the module.

The idea is not tied to Eiffel, Kotlin, Java, C#, TypeScript, PHP, Python, Rust, or any other single language. Each language gives different tools. The discipline is the same: make obligations explicit, make promises observable, protect invariants, and keep expected outcomes separate from broken assumptions.

The point is not to write more checks. The point is to remove guesswork.

Do not ask objects to read your mind. Do not ask tests to police private machinery. Do not ask callers to discover hidden clauses in production. Do not ask reusable code to carry assumptions in silence.

Say the agreement out loud. Then make the code keep it.

*   Apt, Krzysztof R., Olderog, Ernst-Rüdiger. _Fifty years of Hoare’s logic_. [https://link.springer.com/article/10.1007/s00165-019-00501-3](https://link.springer.com/article/10.1007/s00165-019-00501-3)

*   Estler, H.-Christian, Furia, Carlo A., Nordio, Martin, Piccioni, Marco, Meyer, Bertrand. _Contracts in practice_. [https://arxiv.org/abs/1211.4775](https://arxiv.org/abs/1211.4775)

*   Ferreira, David R., Mendes, Alexandra, Ferreira, João F. _Contract usage and evolution in Android mobile applications_. [https://arxiv.org/abs/2401.14244](https://arxiv.org/abs/2401.14244)

*   JetBrains. _Exception and error handling_. [https://kotlinlang.org/docs/exceptions.html](https://kotlinlang.org/docs/exceptions.html)

*   JetBrains. _ExperimentalContracts_. [https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-experimental-contracts/](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/-experimental-contracts/)

*   JetBrains. _Inline value classes_. [https://kotlinlang.org/docs/inline-classes.html](https://kotlinlang.org/docs/inline-classes.html)

*   JetBrains. _kotlin.contracts_. [https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/)

*   JetBrains. _Sealed classes and interfaces_. [https://kotlinlang.org/docs/sealed-classes.html](https://kotlinlang.org/docs/sealed-classes.html)

*   JetBrains. _UUIDs_. [https://kotlinlang.org/docs/uuids.html](https://kotlinlang.org/docs/uuids.html)

*   JetBrains. _What’s new in Kotlin 2.3.0_. [https://kotlinlang.org/docs/whatsnew23.html](https://kotlinlang.org/docs/whatsnew23.html)

*   JetBrains. _What’s new in Kotlin 2.4.0_. [https://kotlinlang.org/docs/whatsnew24.html](https://kotlinlang.org/docs/whatsnew24.html)

*   Jézéquel, Jean-Marc, Meyer, Bertrand. _Design by Contract: The lessons of Ariane_. [https://se.inf.ethz.ch/~meyer/publications/computer/ariane.pdf](https://se.inf.ethz.ch/~meyer/publications/computer/ariane.pdf)

*   Lions, J. L. _ARIANE 5 Flight 501 failure: Report by the inquiry board_. [https://www-users.cse.umn.edu/~arnold/disasters/ariane5rep.html](https://www-users.cse.umn.edu/~arnold/disasters/ariane5rep.html)

*   Liskov, Barbara H., Wing, Jeannette M. _A behavioral notion of subtyping_. [https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf)

*   Meyer, Bertrand. _Applying “Design by Contract”_. [https://se.inf.ethz.ch/~meyer/publications/computer/contract.pdf](https://se.inf.ethz.ch/~meyer/publications/computer/contract.pdf)

*   Meyer, Bertrand. _Class invariants: Concepts, problems, solutions_. [https://arxiv.org/abs/1608.07637](https://arxiv.org/abs/1608.07637)

*   Meyer, Bertrand. _Design by Contract_. [https://se.inf.ethz.ch/~meyer/publications/old/dbc_chapter.pdf](https://se.inf.ethz.ch/~meyer/publications/old/dbc_chapter.pdf)

*   Meyer, Bertrand. _Object-Oriented Software Construction, second edition_. [https://bertrandmeyer.com/wp-content/upLoads/OOSC2.pdf](https://bertrandmeyer.com/wp-content/upLoads/OOSC2.pdf)
