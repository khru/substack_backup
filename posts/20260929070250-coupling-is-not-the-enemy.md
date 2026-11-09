Title: Coupling is not the enemy

URL Source: http://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy

Final URL: https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy

Published Time: 2026-09-29T07:02:50+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!NfUy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb73e3cc7-edab-4ab3-8ac6-3f37739b024d_1024x559.png)](https://substackcdn.com/image/fetch/$s_!NfUy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb73e3cc7-edab-4ab3-8ac6-3f37739b024d_1024x559.png)

_The real problem is putting the wrong knowledge at the wrong distance._

Imagine a workshop that has been used for years.

Not a showroom. A real workshop. The kind where shelves bend under the weight of old tools, half-used materials, spare parts, labels that once made sense, and boxes that everybody is afraid to open because nobody remembers what is inside. Nothing is broken in an obvious way. The hammer still works. The drill still works. The screws are somewhere. The problem is that every repair starts with a search.

The wrench is in the drawer with electrical tape. The spare blade is next to the paint brushes. The screws for the cabinet are in three different boxes because three different people “organized” them at different moments. The measuring tape is exactly where it should be, unless the last job involved the balcony, in which case it is probably in a bucket.

The workshop is not painful because it has many tools. It is painful because the layout no longer remembers the work.

Software becomes painful in the same way.

A system does not decay because one part talks to another part. It decays when the things that change together are far apart, when unrelated things live together, when the same concept has five names, when a business rule is duplicated across distant places, when an _Application Programming Interface_ (API) exposes internal details, when a test fails because a private collaboration changed, and when a small product change becomes a guided tour through the entire codebase.

In everyday design work, we often describe that pain with three words: cohesion, coherence, and coupling.

They are usually taught as separate ideas. Cohesion is good. Coupling is bad. Coherence is the fuzzy word people use when a system “feels wrong” but nobody has named the problem yet.

That framing is too weak.

These three ideas are not separate vocabulary games. They are three views of the same design problem: the cost of change.

Cohesion asks what belongs together.

Coupling asks what knowledge makes change propagate.

Coherence asks whether the whole system still makes sense. I am using coherence here as a practical design lens, not as a formal metric from the classic coupling and cohesion literature.

Good design is not the pursuit of zero coupling. A system with no coupling is not a system. It is a pile of parts.

Good design is the arrangement of knowledge around change. It puts related knowledge close enough to change safely, keeps unrelated knowledge apart, and reduces what distant parts need to know about each other.

The goal is not purity.

The goal is to make the next meaningful change less expensive, less risky, and easier to understand.

[![Image 2: X avatar for @KentBeck](https://substackcdn.com/image/fetch/$s_!z82v!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1457857343568244742%2FFVQ4hpRx.jpg) Kent Beck 🌻@KentBeck Coupling vs cohesion. Coupling: • Can be hard to find • Can be really hard &/| expensive to eliminate. Cohesive sub-elements are: • Usually easy to find • Cheap to achieve, & • Help you find de-coupling. 2:25 PM · Oct 31, 2020 7 Replies · 96 Reposts · 429 Likes](https://x.com/KentBeck/status/1322545224220991488)
Coupling is not the enemy.

Unmanaged coupling is the enemy. Hidden coupling is the enemy. Strong coupling across long distance and high volatility is the enemy.

Cohesion tells us whether the things inside a boundary belong together. Coupling tells us what knowledge makes change propagate across boundaries. Coherence tells us whether names, meanings, boundaries, behaviours, tests, and operational signals still feel like one understandable design.

In this article, a module is any boundary we can reason about as a unit: a function, class, package, service, public contract, or team-owned capability. The important part is not the technical shape. The important part is what knowledge the boundary exposes, what knowledge it hides, and what responsibility it protects.

The useful question is not “is this coupled?”. The useful question is: what knowledge is shared, how far apart are the elements, how often does that knowledge change, and does this relationship create cohesion or complexity?

There are three practical signals behind that question: shared lifecycle, shared knowledge, and flow of knowledge. Shared lifecycle tells us what has to be built, tested, deployed, or owned together. Shared knowledge tells us what one part must know about another. Flow of knowledge tells us which side exports meaning and which side must absorb it.

The practical moves are simple, but not easy:

1.   Move closer when strongly related things live too far apart

2.   Split apart when unrelated things live too close together

3.   Reduce shared knowledge when distance is necessary but the relationship is too strong  
Metrics and formulas can help, but they do not decide design. They are signals. The judgement comes from understanding change, expected volatility, and the economic trade-off between paying the cost of coupling and paying the cost of changing the structure.

*   [The mistake: treating coupling as the villain](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#the-mistake-treating-coupling-as-the-villain)

*   [What is a module?](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#what-is-a-module)

*   [Cohesion: what belongs together](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#cohesion-what-belongs-together)

*   [Coupling: what changes together](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#coupling-what-changes-together)

*   [Coherence: when the whole system still makes sense](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#coherence-when-the-whole-system-still-makes-sense)

*   [The vocabulary we inherited](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#the-vocabulary-we-inherited)

*   [The taxonomy map](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#the-taxonomy-map)

*   [Connascence: what exactly are the parts agreeing on?](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#connascence-what-exactly-are-the-parts-agreeing-on)

*   [Strength, distance, and volatility](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#strength-distance-and-volatility)

*   [Formulas are lenses, not verdicts](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#formulas-are-lenses-not-verdicts)

*   [The three design moves](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#the-three-design-moves)

*   [Practical examples](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#practical-examples)

*   [Software economics: design as the cost of future change](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#software-economics-design-as-the-cost-of-future-change)

*   [Conclusion](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#conclusion)

*   [References](https://emmanuelvalverderamos.substack.com/p/coupling-is-not-the-enemy#references)

[![Image 3](https://substackcdn.com/image/fetch/$s_!AUsO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04a98437-95e2-473d-946d-4907222138c6_1024x558.png)](https://substackcdn.com/image/fetch/$s_!AUsO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04a98437-95e2-473d-946d-4907222138c6_1024x558.png)

A lot of design conversations start with a sentence that sounds useful, but is not useful yet:

“This is coupled.”

Coupled how?

Coupled through a method call? A shared database table? A duplicated pricing rule? A status code? A message schema? A framework lifecycle? A deployment order? A timeout? A test fixture? A customer identifier that must mean the same thing across five services?

And coupled with respect to what change?

That last question matters. Two parts can be coupled with respect to one change and independent with respect to another. A frontend and backend may be coupled with respect to the shape of a response, but not with respect to the backend’s internal persistence model. A test may be coupled to observable behaviour, which is useful, or to the order of private method calls, which is often fragile. A payment area and an order area may be coupled because the business process genuinely requires coordination. That does not automatically make the design bad.

The phrase “coupling is bad” hides the work we need to do. It turns design into a moral judgement. The code is coupled, therefore guilty. The cure is decoupling, therefore virtuous.

But real systems are not improved by moral vocabulary. They are improved by better placement of knowledge.

A bridge is a kind of coupling. A knot is also a kind of coupling. The difference is not that one connects and the other does not. The difference is whether the connection carries the right load, in the right place, with the right amount of movement.

Software design is full of bridges that become knots.

The mistake is not that parts depend on each other. The mistake is that we stop asking what kind of dependency it is, what knowledge it shares, how far the knowledge travels, how often it changes, and whether that relationship makes the system easier or harder to change.

[![Image 4](https://substackcdn.com/image/fetch/$s_!2L-H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9636dba4-c31b-4747-814f-28361d7d8186_1024x559.png)](https://substackcdn.com/image/fetch/$s_!2L-H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9636dba4-c31b-4747-814f-28361d7d8186_1024x559.png)

Before going further, we need to define _module_, because the word is easy to misunderstand.

In this article, a module is not necessarily a package, class, service, folder, library, namespace, deployment unit, or microservice. Any of those can be a module, but none of them automatically is one in the design sense.

A component is any part of a system. A module is a component with a useful boundary. The difference matters. Splitting a system into many components does not automatically make it modular. A microservice that exposes its internal model, shares tables, leaks status codes, and requires coordinated deployments may be a component, but it is not behaving like a good module.

A module is a knowledge boundary around a responsibility.

It exposes some knowledge so the rest of the system can use it, and hides other knowledge so the rest of the system does not need to understand how it works. That boundary can exist at many scales: a function, a class, a package, a service, a public contract, or a team-owned capability. The scale changes, but the design question stays the same: what does this boundary expose, what does it hide, and what kind of change is supposed to remain inside it?

This is close to Ousterhout’s framing in _A Philosophy of Software Design_: a module has an interface and an implementation, and the interface is the knowledge other modules must carry in order to use it. The best modules do not merely split code into smaller pieces. They hide meaningful complexity behind a smaller, clearer interface. That distinction matters for cohesion and coupling because every public detail becomes knowledge the rest of the system may have to preserve.

A useful module has three parts:

1.   **Function:** what it offers to the rest of the system

2.   **Logic:** how it works internally

3.   **Context:** the assumptions under which it is valid to use

For example, `RefundEligibilityPolicy` exposes a decision: whether a refund can be created. Its internal logic may check delivery date, payment capture, final-sale status, and fraud review. Its context may assume that the `Order` and `Payment` belong to the same customer and tenant, and that the policy is being evaluated by the owner of the refund workflow. If consumers need to know all of that logic to use the module, the boundary is weak. If consumers can ask for the decision without reconstructing the rule, the boundary is doing useful work.

This is why cohesion and coupling depend on modules. Cohesion asks whether the elements inside a module belong together. Coupling asks what knowledge crosses from one module to another. A poor module exposes too much, hides too little, or groups responsibilities that change for different reasons. A good module protects a coherent responsibility and gives the rest of the system a small, clear way to use it.

[![Image 5](https://substackcdn.com/image/fetch/$s_!kEqe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bc21941-c3a3-4121-ac4f-9708d7db6dce_1024x559.png)](https://substackcdn.com/image/fetch/$s_!kEqe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bc21941-c3a3-4121-ac4f-9708d7db6dce_1024x559.png)

Cohesion asks whether the elements inside a boundary belong together.

Now that we have defined a module as a knowledge boundary around a responsibility, cohesion becomes more concrete: given this boundary, do the things inside it belong together?

That boundary can be a function, class, module, package, service, repository, team-owned area, or operational unit. The scale changes, but the question remains: do these things form a meaningful whole, or are they merely sharing space?

A cohesive module feels like a drawer arranged around a job. When you open it, you understand why those tools are together.

A non-cohesive module feels like a junk drawer. Useful things may be inside, but their proximity is accidental.

This is why names like `Utils`, `Helpers`, `Common`, `Shared`, `Base`, and `Manager` so often become dangerous. The names do not tell us what belongs there. They tell us that somebody needed a place to put something.

Consider this module:

Everything mentions `Customer`, so the module may look cohesive at first. But the reasons to change are different. Name formatting changes because of display rules. Refund eligibility changes because of support, finance, or legal policy. Loyalty discount changes because of retention strategy. Anonymization changes because of privacy and compliance.

The functions share a data structure.

They do not share a responsibility.

The problem is easier to see if we stop looking at the noun and start looking at the reasons to change.

The diagram is not saying that `Customer` is useless. It is saying that one noun can hide several responsibilities.

That is a crucial distinction. Cohesion is not “these things use the same noun”. Cohesion is “these things belong to the same concept, protect the same responsibility, and tend to change for the same reason”.

A better structure might be:

As a directory-like view, the split is even more obvious.

The improvement is not smaller files. Smaller files can still be nonsense.

The improvement is that the boundaries now explain the work. Each module has a clearer reason to exist, and a future change has a better place to go.

Cohesion lowers search cost. When a change arrives, you know where to look. When a rule breaks, you know where it should have been protected. When a concept evolves, you can see its shape.

Low cohesion makes every change begin with a question nobody enjoys asking:

“Where did we put that?”

Coupling is often described as dependency, but dependency is only the visible part.

From the module perspective, coupling is about what knowledge crosses a boundary and what future changes that crossing may force.

A more useful definition is this: two elements are coupled with respect to a change when changing one requires changing the other. This does not mean every dependency is harmful. It means the cost of a dependency depends on the kind of knowledge being shared, the distance between the elements, and the changes we expect.

That definition changes how we look at code.

A method call is a dependency, but it may not be a painful coupling if the called method has a stable contract.

A duplicated rule may be a painful coupling even if there is no method call, no import, and no direct static relationship.

Two files may live in different repositories and still be coupled because the same business change always touches both.

Imagine a refund policy duplicated across a frontend, backend, and support dashboard:

There is no direct call between these snippets. Static dependency analysis may not connect them.

But a product change will.

If the refund window changes from thirty days to forty-five days, all three places are now part of the same change. If final-sale policy changes, more places may need to move. If fraud review becomes part of refund eligibility, the gap between the three implementations becomes a production risk.

Here is the shape of the problem.

This is why imports are not enough. The coupling is not in the call graph. It is in the business rule.

This is functional coupling at a distance. I do not mean “functional coupling” as a canonical metric here. I mean that the same business function, refund eligibility, is effectively shared across distant elements.

The problem is not duplication in the abstract. The problem is duplicated volatile business knowledge across distant places. The rule is strong. The distance is high. The volatility is likely real. That combination creates cost.

Coupling tells us how change can travel. Change history tells us how it has actually travelled.

Sometimes we reduce coupling by separating things.

Sometimes we reduce coupling by hiding knowledge behind a contract.

Sometimes we do the opposite and move things closer together because pretending they are independent is the lie causing the pain.

That is the first important reversal:

Low coupling is not always the right move. Sometimes the right move is higher cohesion.

[![Image 6](https://substackcdn.com/image/fetch/$s_!VvW_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5675f572-f8f6-42ef-8e9a-a41d9fa7e0fd_1024x558.png)](https://substackcdn.com/image/fetch/$s_!VvW_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5675f572-f8f6-42ef-8e9a-a41d9fa7e0fd_1024x558.png)

Cohesion is local. Coherence is global.

A system is coherent when its names, meanings, behaviours, boundaries, tests, errors, operational signals, and design decisions feel like they belong to the same world.

Not the same layer. Not the same style everywhere. The same world.

This is not a replacement for cohesion or coupling. It is the reader’s experience of whether the design can be understood as one system.

Coherence does not mean uniformity. A domain model should not look like an infrastructure adapter. A long-running workflow should not look like a pure function. A stable commodity integration should not receive the same design attention as volatile core policy. Difference is not the enemy. Unexplained difference is.

A coherent system has an internal grammar. If you learn one part, you gain clues for understanding another. Names carry consistent meaning. Similar problems are solved in similar ways. Boundaries follow an understandable logic. Tests express a recognizable strategy.

Operational signals help people reason about production without becoming archaeologists.

An incoherent system can have clean modules and still be exhausting.

Naming incoherence:

*   The same person is called `User` in identity

*   The same person is called `Customer` in billing

*   The same person is called `Account` in support

*   The same person is called `Member` in marketing  
This may be correct if those are genuinely different concepts. But if they are accidental synonyms, every change begins with translation.

Semantic incoherence is worse:

*   `ACTIVE` means “can log in” in one service

*   `ACTIVE` means “has paid subscription” in another

*   `ACTIVE` means “not deleted” in a third  
The code can compile while the meaning falls apart.

Behavioural incoherence creates friction for every consumer:

*   One endpoint returns `404` when something is missing

*   Another returns `200` with an error body

*   Another returns `undefined`

*   Another throws a generic exception  
Testing incoherence makes the feedback loop noisy:

*   One module tests behaviour through public APIs

*   Another tests private methods

*   Another mocks every collaborator

*   Another needs a full environment to test simple logic  
Operational incoherence makes production harder to understand:

*   Every service uses different log fields

*   Every service uses different metric labels

*   Every service uses different error names

*   Every service uses different correlation identifiers

*   Every service uses different alert severity rules  
Coherence is the system-level version of understandability. It is what lets people predict where a rule might live, what a name might mean, how a failure might appear, and how a change might move.

Without coherence, each local decision may be defensible, while the whole system becomes tiring to inhabit.

Coherence is what lets local decisions add up to a system instead of a collection of private dialects.

The point is not sameness. The point is that the next reader can predict the shape of the system before opening every drawer.

[![Image 7](https://substackcdn.com/image/fetch/$s_!2T_5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e0aaea9-2adb-4ac1-87bf-a3215942cd80_1024x558.png)](https://substackcdn.com/image/fetch/$s_!2T_5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e0aaea9-2adb-4ac1-87bf-a3215942cd80_1024x558.png)

The old vocabulary still matters because it gives us names for recurring design shapes. But the vocabulary should be used diagnostically, not religiously.

These terms only become useful after we ask what boundary we are evaluating. A function, class, package, service, event contract, or team-owned capability can all be treated as modules for design reasoning, but the conclusion may change with the scale. A class may be cohesive while the package around it is incoherent. A service may be internally tidy while its public contract leaks too much knowledge.

The classic cohesion ladder moves from weak reasons for grouping code to stronger ones.

Coincidental cohesion means things are together by accident. A `CommonUtils` module full of unrelated helpers is the usual example.

Logical cohesion means things are grouped by category. A `NotificationService` that handles email, text messages, push notifications, Slack, and postal letters may be logically grouped, but each channel may change for different reasons.

Temporal cohesion means things happen at the same time. Startup code often has temporal cohesion.

Procedural cohesion means things follow a sequence. A checkout process may coordinate validation, stock reservation, payment, and confirmation.

Communicational cohesion means things work on the same data. This is stronger, but not always enough, as the `Customer` example showed.

Sequential cohesion means the output of one step becomes the input to the next. Parsers, import pipelines, and validation chains often have this shape.

Functional cohesion means everything contributes to one clearly defined purpose.

Informational cohesion means behaviour lives with the abstraction and data it protects, such as an `Order` object that owns its state transitions and invariants.

That ladder is useful, but it is incomplete without change.

A module can look cohesive by category and still change for many unrelated reasons. A module can look messy by strict rules and still be cohesive because it protects one difficult concept.

The classic coupling ladder is also useful.

Content coupling happens when one module depends on another module’s internals. For example, a test reads private fields through reflection, or a service writes directly into another service’s private tables.

Common coupling happens through shared mutable state. Global variables, mutable singletons, shared session state, and shared database rows are common examples.

External coupling happens when modules depend on the same external format, protocol, schema, or device. File formats, message schemas, database schemas, cloud conventions, and third-party API contracts all create this kind of coupling.

Control coupling happens when one module tells another how to behave. Boolean flags and mode parameters often reveal this:

Stamp coupling happens when a module passes a whole structure while the receiver only needs part of it.

If the function only needs an email address and customer status, passing the entire `Customer` exposes more knowledge than necessary.

Data coupling happens when modules communicate using only the data required for the interaction.

This is still coupling, but it is smaller and clearer.

The point of the vocabulary is not to recite the ladder.

The point is to ask better questions. What kind of knowledge crosses this boundary? Is that knowledge necessary? Is the boundary close or far? Is the knowledge stable or volatile?

This is how I prefer to use the old vocabulary in practice.

The taxonomy gives names. The questions create judgement.

Connascence is a useful microscope for coupling. The term comes from Meilir Page-Jones and has been refined in later design writing. It asks: what must two parts agree on in order to work together?

They may need to agree on a name:

*   `customerId`

*   `OrderDelivered`

*   `GET /orders/{orderId}`  
They may need to agree on a type or representation:

*   `customerId` uses a universally unique identifier

*   `amount` is `Money`

*   `createdAt` is an `Instant`  
They may need to agree on meaning:

*   `"D"` means delivered

*   `"C"` means captured

*   `-1` means unlimited

*   `true` means notify the customer  
This is where magic strings, magic numbers, and ambiguous booleans become design problems. The value is small. The hidden meaning is large.

They may need to agree on an algorithm:

*   The same pricing formula

*   The same checksum

*   The same signature verification

*   The same discount calculation  
They may need to agree on position:

The order of arguments becomes part of the contract.

They may need to agree on execution order:

1.   Open connection

2.   Begin transaction

3.   Execute statement

4.   Commit transaction

5.   Close connection  
They may need to agree on timing:

*   The token must be used before expiry

*   The callback must arrive within thirty seconds

*   The lock must be renewed before timeout  
They may need to agree on value:

*   The order total must equal the sum of order lines

*   Reserved stock plus available stock must remain consistent

*   Debit and credit entries must balance  
They may need to agree on identity:

*   The same aggregate

*   The same session

*   The same database row version

*   The same lock owner  
Connascence matters because not all shared knowledge is equal.

Sharing a field name is one thing. Sharing a business invariant across distant services is another. Sharing execution order in one function is one thing. Sharing timing assumptions across a distributed system is another.

The usual design heuristic is to keep stronger forms of connascence local, make weaker forms explicit in contracts, and avoid strong connascence across distance unless the business relationship truly requires it.

The ladder below is not a perfect ordering for every context, but it is a useful reading aid. As the shared knowledge becomes stronger, distance becomes more expensive.

The stronger the agreement, the more suspicious it becomes when the agreement crosses a distant boundary.

The microscope helps us see what the word “coupled” was hiding.

[![Image 8](https://substackcdn.com/image/fetch/$s_!9wZl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cc7a641-8b8f-4452-8f2e-53d6bbccbcec_1024x558.png)](https://substackcdn.com/image/fetch/$s_!9wZl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cc7a641-8b8f-4452-8f2e-53d6bbccbcec_1024x558.png)

Now we can assemble the model.

Coupling has strength.

Some relationships share only a name. Others share meaning, algorithms, timing, values, identity, or internals.

In Khononov’s model, strength is mostly about shared knowledge. The more one part needs to know about another part’s contract, model, business function, or implementation details, the stronger the integration becomes. A consumer that only knows a stable contract is in a different situation from a consumer that knows the provider’s internal tables, status codes, lifecycle, and business rules.

Coupling has distance.

Two related lines inside one function are close. Two services owned by different teams and deployed independently are far apart. Distance can be code distance, module distance, repository distance, service distance, team distance, deployment distance, or vendor distance.

Distance is not only a folder path. It also includes lifecycle distance. If two elements must be implemented, tested, released, operated, or owned together, they are closer than the architecture diagram suggests. If they can evolve independently, they are farther apart, even if an import exists.

Coupling has volatility.

Some knowledge barely changes. Some knowledge changes every week. Refund policy, pricing, promotions, onboarding, eligibility, compliance, and product experiments are often volatile. Stable infrastructure conventions may change rarely.

The combination matters more than any dimension alone.

There is one more detail that matters for practical design: knowledge flows in the opposite direction of dependency. If `Distribution` calls `Customer Relationship Management`, the dependency points from `Distribution` to `Customer Relationship Management`, but the knowledge that matters flows from the provider’s contract into the consumer’s code.

That distinction is easy to miss. We often draw dependency arrows and think we have explained the design. But the real cost sits in the knowledge that crosses the boundary. The more knowledge crosses, the more reasons the consumer has to change when the provider changes.

Khononov separates that pressure into a small set of questions.

This is why “low coupling” is not a complete design goal. A system needs coupling to achieve its purpose. The goal is to make the essential coupling explicit, local when it is strong, distant when it is weak, and stable enough for the volatility of the knowledge being shared.

In the simplified boolean version:

```
High strength + low distance =
    Cohesion

Low strength + high distance =
    Loose coupling

High strength + high distance =
    Global complexity

Low strength + low distance =
    Local complexity
```

The same model works better visually as a quadrant.

High strength and low distance is often healthy. Related things live close enough to be understood and changed together.

Low strength and high distance is also often healthy. Distant things share little knowledge, so they can evolve independently.

High strength and high distance is painful. Related things live far apart, so every change requires coordination, memory, compatibility, and careful testing.

Low strength and low distance is noisy. Unrelated things live together, so the reader pays a navigation tax.

This is the heart of the article:

> Good design is not low coupling everywhere. Good design is balanced coupling around expected change.

The practical decision can be summarized like this:

This diagram prevents a common refactoring mistake: separating things because they are coupled, without asking whether the coupling is telling us that they belong together.

Formulas can help us reason, but they do not understand the domain.

They do not know the next product change. They do not know whether a messy function is stable and harmless or volatile and dangerous. They do not know whether an abstraction protects policy or only decorates code.

Use formulas as lenses, not verdicts.

This is also where metric-driven refactoring is useful. A metric does not tell you what design should be. It helps you decide where to look first, compare two possible structures, and justify whether a refactoring is worth the cost. Fran Iglesias makes this point well: refactoring is not an aesthetic ritual; it is a way to control the future cost of software change. That fits the argument here, with one important constraint: a metric should select a conversation, not end it.

Heuristics such as code smells, object calisthenics, indentation depth, long parameter lists, feature envy, and primitive obsession can be treated as cheap signals. Metrics such as cyclomatic complexity, cognitive complexity, class coupling, class cohesion, change history, and ownership concentration can make those signals more explicit. But the design move still has to come from reading the code: move closer, split apart, reduce shared knowledge, or leave it alone.

Before looking at individual formulas, it helps to know what kind of question each family of metrics can answer.

The mistake is using a metric from one family to answer a question from another. A class cohesion metric will not tell you whether an event schema is too semantic. A package dependency metric will not tell you whether two files always change together.

The same caution applies to popular advice about loose coupling and high cohesion. Dependency injection can reduce concrete implementation coupling, but it still creates contract coupling. Messaging can reduce synchronous availability coupling, but it can increase schema, semantic, ordering, idempotency, and observability coupling. Docker and Terraform can reduce some environment and vendor friction, but they introduce their own configuration, pipeline, and operational contracts. Those tools can be good moves. They are not magic erasers.

_Afferent coupling_ counts how many external modules depend on the module being measured.

```
Afferent coupling =
    Number of external modules depending on this module
```

_Efferent coupling_ counts how many external modules the measured module depends on.

```
Efferent coupling =
    Number of external modules this module depends on
```

_Instability_ compares outgoing dependencies with total dependencies.

```
Instability =
    Efferent coupling
    / (Afferent coupling + Efferent coupling)
```

A value close to zero means many modules depend on this module, while this module depends on few external modules. A value close to one means this module depends on many external modules, while few modules depend on it.

_Abstractness_ compares abstract types with total types.

```
Abstractness =
    Number of abstract types / Total number of types
```

_Distance from main sequence_ combines abstractness and instability.

```
Distance from main sequence =
    Absolute value of (Abstractness + Instability - 1)
```

The useful question is not “is this number good?”.

The useful question is: does the package’s stability match its role?

A highly depended-on concrete package may be painful to change. A highly abstract package that nobody depends on may be unused speculation.

_Coupling between objects_ counts distinct classes connected to a measured class.

```
Coupling between objects =
    Number of distinct classes connected to the measured class
```

_Response for a class_ estimates the size of the response set: the methods that may execute in response to a message sent to an object of that class. In practice, tools vary in how deeply they follow calls, so compare values within the same tool rather than across tools.

```
Response for a class =
    Size of the response set for the class
```

The original _Lack of cohesion in methods_ formulation compares method pairs that share instance variables with method pairs that do not.

```
Lack of cohesion in methods =
    Maximum of:
        Number of method pairs that do not share fields
        - Number of method pairs that share fields,
        0
```

A graph-based version treats methods as nodes.

```
Graph-based lack of cohesion in methods =
    Number of connected components in the method graph
```

Where:

```
Method Graph =
    Methods are nodes.
    Two methods are connected if they share a field or call each other.
```

_Tight class cohesion_ measures direct method connectivity through shared instance variables.

```
Tight class cohesion =
    Number of directly connected method pairs
    / Number of possible method pairs
```

_Loose class cohesion_ measures direct or indirect method connectivity. Some sources count direct connections inside the indirect set, while others report them separately. When using the metric, state the variant.

```
Loose class cohesion =
    Number of directly or indirectly connected method pairs
    / Number of possible method pairs
```

These metrics are useful, but limited.

A stateless service may have no fields. A behaviour-rich object may delegate internally. A use case may legitimately coordinate several ports. A data class can have great field sharing and poor domain design.

The metric is a prompt for reading, not a replacement for reading.

The strength, distance, and volatility model gives us formulas for thinking. The formulas below are best read as qualitative or ordinal models. They are not a promise that the real cost of a change can be measured with exact arithmetic.

```
Maintenance effort =
    Strength * distance * volatility
```

This does not mean we can calculate exact maintenance cost with three numbers. It means the painful case appears when a relationship is strong, far away, and volatile.

```
Boolean modularity =
    Strength exclusive or distance
```

This means modularity appears when strength and distance are aligned in opposite ways: either strong things are close, or distant things are weakly related.

```
Boolean complexity =
    Not (strength exclusive or distance)
```

This means complexity appears when strong things are far apart or unrelated things are close together.

```
Boolean balanced coupling =
    (Strength exclusive or distance) or not volatility
```

This matters because not every imperfect design needs immediate repair. If the relationship is not volatile, the cost may be tolerable. Software design is not a beauty contest. It is an economic activity.

In a numeric scale, the same idea should be used to compare options, not to claim precision. A score can help a team discuss whether reducing strength, reducing distance, or accepting low volatility is the most economical move.

Some formulas are useful as working heuristics, but they are not canonical metrics.

They should be treated as conversation aids.

For change history:

```
Working heuristic, not a canonical metric:

Change similarity between element one and element two =
    Number of changes touching both elements
    / (Number of changes touching element one
       + Number of changes touching element two
       - Number of changes touching both elements)
```

For directional change coupling:

```
Working heuristic, not a canonical metric:

Change coupling confidence from element one to element two =
    Number of changes touching both elements
    / Number of changes touching element one
```

For team ownership:

```
Working heuristic, not a canonical metric:

Team cohesion signal =
    Changes made by the primary owning team
    / Total changes in the boundary
```

These signals are not truth. They help us notice where to look.

[![Image 9](https://substackcdn.com/image/fetch/$s_!OUOc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd43b09e8-1250-4d6c-97e6-7ac0f1220a7f_1024x558.png)](https://substackcdn.com/image/fetch/$s_!OUOc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd43b09e8-1250-4d6c-97e6-7ac0f1220a7f_1024x558.png)

Once we understand cohesion, coherence, coupling, strength, distance, and volatility, the practical moves become clearer.

There are many refactorings, patterns, heuristics, and architectural styles. Most of them serve a small set of design moves.

Refactoring has a narrower meaning than “changing the design”. In Fowler’s sense, a refactoring is a change to the internal structure of software that preserves observable behaviour while making the code easier to understand or cheaper to modify.

That definition matters because it keeps design work honest. If behaviour changes, we are not refactoring anymore. We are changing the product. If the structure changes without lowering the cost of understanding or future change, we are only rearranging code.

Tidying is a smaller word for a smaller move. In this article, a tidy is a behaviour-preserving structural improvement made near the work at hand: naming a hidden concept, moving a rule closer to its owner, splitting an accidental bucket, reducing a leaky parameter list, or making a test protect behaviour instead of private collaboration. A tidy should reduce local cognitive load, change amplification, or hidden knowledge without turning into a redesign.

That distinction is useful because not every tidy is a named refactoring, and not every refactoring is worth doing right now. A tidy earns its place when it makes the next behaviour change cheaper, safer, or easier to understand. Otherwise it is decoration.

In this article, refactoring is mostly opportunistic: it appears while preparing a behaviour change, while understanding code, while reviewing code, or while removing local friction. The important nuance is that opportunistic does not mean casual. It means small, behaviour-preserving, protected by tests, and motivated by nearby evidence.

At code scale, many design moves have familiar refactoring names: `Move Function`, `Extract Function`, `Extract Class`, `Introduce Parameter Object`, `Replace Primitive with Object`, `Hide Delegate`, `Remove Middle Man`, `Split Phase`, and `Change Function Declaration`. The names are useful, but they are not the point. The point is to move knowledge, redraw a boundary, or reduce what another part of the system needs to know.

The playbook is small enough to remember.

This matters because many design arguments are arguments about the wrong move. Someone wants to split when the system is asking to move closer. Someone wants an abstraction when the system is asking for a better boundary.

Move closer when strongly related things live too far apart.

This is the high strength and high distance case. The system pretends things are independent, but every meaningful change proves they are not.

Typical symptoms:

1.   The same business rule is duplicated across frontend, backend, dashboard, and batch jobs

2.   The same files change together repeatedly

3.   A small feature requires coordinated changes across many repositories

4.   Tests need to assemble half the system to check one policy

5.   A domain invariant is scattered across layers

6.   Configuration that belongs to one policy lives in a global bucket  
The move is not always “put everything in one class”. That would be a new problem with a different name.

Moving closer can mean moving a rule into a domain object, creating a policy module, grouping files by capability, bringing tests closer to behaviour, or putting ownership under one team.

The question is: what knowledge is already changing together, and where should it live?

Split apart when unrelated things live too close together.

This is the low strength and low distance case. The system puts things together, but they do not belong together.

Typical symptoms:

1.   A common module changes for unrelated reasons

2.   A service owns several workflows that do not share policy

3.   A utility class becomes a dumping ground

4.   A package name is too vague to reject new responsibilities

5.   Different teams keep editing different parts of the same module

6.   Tests for one behaviour require fixtures from unrelated behaviours  
The move is not “make more files”.

The move is to create boundaries that match reasons to change.

Reduce shared knowledge when distance is necessary.

Some things cannot or should not live close together. Public APIs, mobile clients, third-party integrations, separately deployed services, other teams, and external vendors create real distance. In those cases, the goal is not to erase distance. The goal is to reduce the strength of the relationship.

Typical symptoms:

1.   An API exposes internal models

2.   Consumers depend on provider status codes

3.   Events publish serialized aggregates instead of stable business facts

4.   Services read or write each other’s tables

5.   Application policy depends on vendor clients

6.   Tests depend on private collaboration details  
The move is to make the relationship smaller, clearer, and more stable. Use explicit contracts. Hide internal models. Publish stable events. Expose decisions instead of leaking the rule. Put vendor details behind an adapter when the policy should not know the vendor. Be careful: every new contract is also a maintenance responsibility. Reducing shared knowledge is not the same as adding indirection everywhere.

This is where many technical practices help, but they remain secondary. A value object helps when a primitive hides meaning. A port helps when policy depends on infrastructure. A named constant helps when a value has hidden meaning. A Special Case or Null Object helps when absence has valid neutral behaviour. A pattern is only useful when it changes the cost of future change.

The concepts become real when we see the bad context first.

Fowler’s code smells are useful here when treated as symptoms, not verdicts. `Divergent Change` often points to unrelated responsibilities living inside one boundary. `Shotgun Surgery` often points to one responsibility scattered across distance. `Feature Envy` often suggests behaviour is living away from the data or policy it uses most. `Primitive Obsession` and `Data Clumps` often point to unnamed knowledge. `Message Chains` and `Insider Trading` often point to leaked boundary knowledge. `Middle Man` and `Speculative Generality` warn that reducing coupling can also create waste.

A design move should answer five questions:

*   What coupling did we reduce?

*   What cohesion did we increase?

*   What coherence did we improve?

*   What cost of future change did we lower?

*   What new cost did we introduce?  
If a design move cannot answer those questions, it may be decoration.

For the examples below, keep this review loop in mind.

A product team changes the refund policy:

> Refunds are now allowed for forty-five days instead of thirty days, except for final-sale products and orders with unresolved fraud review.

At first, this sounds like a small change.

Then the team finds the rule in three places.

This is not just duplication.

It is functional coupling at a distance. The frontend, backend, and support dashboard are coupled with respect to refund policy changes.

There is also connascence of meaning. `"DELIVERED"` must mean the same thing across contexts. The number `30` carries policy. The absence of fraud review in some places is not visible from the code itself. The frontend and support dashboard know pieces of a business decision they probably should not own.

The current design spreads one decision across three places.

A better design moves the actual decision closer to the place that owns refund policy:

Then the frontend and support dashboard can consume the decision:

After the move, distant consumers no longer reconstruct the policy. They ask for a decision.

The point is not “logic always belongs in the backend”.

The point is that volatile business policy should not be reconstructed in distant consumers.

There is still a design question here: the policy may belong in the backend, in a domain module shared by several server-side capabilities, or in a dedicated service if refund eligibility is owned independently. The important move is not the physical location. It is that one owner speaks for the decision.

What improved?

*   **Cohesion:** Refund policy is concentrated

*   **Coupling:** Consumers no longer duplicate the decision logic

*   **Coherence:** The system has one language for refund eligibility

*   **Economics:** The next refund policy change should touch fewer places  
What did we pay?

*   The frontend may now need to handle loading states

*   The frontend may now need server-provided availability

*   The frontend may now need to handle cases where availability cannot be calculated yet  
That trade-off may be worth it because duplicated refund policy is more expensive than asking the owner of the policy.

The trade is not free, but it is explicit.

A rule says:

> An order cannot be confirmed without at least one order line.

But the rule appears in several places:

*   Frontend validation

*   Controller validation

*   Application service

*   Database constraint

*   End-to-end test setup  
Some duplication may be intentional. The frontend can provide fast feedback. The database can provide a final safety net.

But if the domain itself does not protect the invariant, the system has a hole in its centre.

A better move is to put the invariant near the concept it protects:

The frontend may still validate for usability. The database may still constrain for safety. But the core meaning now lives with `Order`.

That layered duplication is not automatically bad. It becomes bad when the outer checks become the authoritative rule and the domain object becomes only a bag of data.

The improved shape is not “only one check exists”. The improved shape is “one boundary owns the meaning”.

The lifecycle version makes the invariant more concrete. The order can move from draft to confirmed only through a valid transition.

What improved?

*   **Cohesion:** The order invariant lives near the order state

*   **Coupling:** Other layers no longer need to be the primary owners of the rule

*   **Coherence:** The domain model now says what an order is allowed to do

*   **Economics:** Future changes to order confirmation rules have a clearer home  
The trade-off is that the domain model now has behaviour and must be tested as behaviour, not treated as a passive data structure. That is not a cost to avoid. It is the cost of giving the concept a real boundary.

A package called `shared-common` contains this:

*   `MoneyFormatter`

*   `JwtParser`

*   `RefundPolicy`

*   `DateFormatter`

*   `TenantResolver`

*   `EmailTemplateNames`  
The package is shared, but “shared” is not a design reason. It is a distribution fact.

The module changes because of billing, identity, refunds, time handling, tenancy, and notifications. A change in one area risks rebuilding, retesting, versioning, or reviewing code that has nothing to do with it.

This is accidental cohesion wearing a respectable name.

A better structure might be:

As a tree, the new structure stops pretending that one shared bucket is a design boundary.

The point is not that every utility must move. Some utilities are stable, generic, and harmless. The point is that a shared package should not become a landfill of unrelated reasons to change.

After the split, the structure starts to describe ownership and change.

What improved?

*   **Cohesion:** Each module has a clearer responsibility

*   **Coupling:** Unrelated consumers no longer depend on the same shared bucket

*   **Coherence:** The package structure communicates business and technical ownership better

*   **Economics:** Changes can be reviewed, tested, and released with less accidental blast radius  
What did we pay?

*   There may be more packages or folders

*   Some imports may move

*   The team must decide where new shared code belongs instead of throwing it into common  
That cost is acceptable if the shared package had become a coordination trap.

A codebase is organized like this:

*   `controllers`

*   `services`

*   `repositories`

*   `validators`

*   `mappers`  
This may look clean. The technical roles are separated.

But a refund change touches all of them:

*   `RefundController`

*   `RefundService`

*   `RefundRepository`

*   `RefundValidator`

*   `RefundMapper`

*   `RefundTests`  
If every refund change forces the reader to travel across technical folders, the structure may be separating technical concerns while scattering a business concern.

A capability-oriented structure may be better:

The same structure as a tree makes the design intention visible: the refund capability owns the refund change.

This is not a universal rule. Technical grouping can work well in small systems, stable systems, or teams with strong conventions.

The question is empirical: what kinds of changes dominate?

The alternative is not “no technical structure”. It is technical structure inside a business capability.

If most changes are vertical business changes, capability grouping may improve cohesion. If most changes are horizontal technical changes, technical grouping may be enough. Many systems need a hybrid: capabilities at the top level, technical roles inside each capability, and shared infrastructure kept deliberately small.

This is how _Separation of Concerns_ should be understood here. It is not “make more layers”. It is separating knowledge that changes for different reasons while keeping together knowledge that changes for the same reason.

An order service exposes this response:

The frontend uses `status`, `paymentStatus`, `refundBlocked`, and `finalSale` to decide whether to show a refund button. The support dashboard uses `warehouseStatus` and `internalRiskScore`. Another service uses `status === "D"` to infer delivery.

The problem is not _JavaScript Object Notation_ (JSON).

The problem is leaked knowledge.

Consumers now know internal status codes, internal risk information, warehouse state, payment state, and refund policy hints. The provider has less freedom to change its model because consumers have built decisions on top of it.

This is model coupling. It also contains connascence of meaning: `"D"` means delivered, `"C"` means captured, `refundBlocked` means refund should not be offered, and `finalSale` participates in policy.

The coupling is not only the response shape. It is the internal decision model leaking into consumer code.

A better contract exposes information shaped by consumer need:

For support:

What improved?

*   **Cohesion:** Internal order state remains inside the order boundary

*   **Coupling:** Consumers no longer depend on internal status codes and policy details

*   **Coherence:** Each contract speaks the language of its use case

*   **Economics:** The provider can evolve internal representation with less consumer impact  
What did we pay?

*   The provider now needs to design and maintain explicit contracts

*   Different consumers may need different read models

*   There may be more mapping code  
That cost is often worth paying when consumers are distant and independent.

The boundary is the deciding factor. Inside a small module, a direct object may be perfectly fine. Across service, team, mobile, or third-party boundaries, leaking internals becomes much more expensive.

Events are often sold as decoupling.

Sometimes they are. Sometimes they only move the coupling into a message broker.

Bad event:

This event is not a stable business fact. It is a serialized internal object. Consumers must understand internal status codes, internal risk scoring, and lifecycle details. It also makes versioning harder because every internal field starts to look public once consumers rely on it.

The message broker removes the direct call, but it does not remove shared meaning.

An EventStorming lens helps here because it starts from business facts, not from database-shaped messages. The question is not “what changed inside the object?” The question is “what happened in the business that another part of the system may need to react to?”

This does not mean every system needs EventStorming. It means that, when events are unclear, modelling commands, aggregates, business facts, read models, policies, and hotspots can reveal which knowledge should be public and which knowledge is only internal state.

A better event says what happened:

This does not remove all coupling. Consumers still depend on the event name, schema, and meaning.

But the relationship is smaller and more coherent. The event is now closer to a business fact and less like a database row in motion.

This is also why event-driven architecture is not automatically decoupled architecture. It can reduce temporal coupling while preserving or increasing semantic coupling.

What improved?

*   **Cohesion:** Internal order state remains inside the owner

*   **Coupling:** Consumers depend on a stable fact, not a full internal model

*   **Coherence:** The event language matches something meaningful in the domain

*   **Economics:** Internal model changes are less likely to break consumers  
What did we pay?

*   Consumers that need different information may require additional events or read models

*   The producer must be clearer about event semantics and versioning  
Again, this is not free. It is a trade.

A refund use case talks directly to a vendor client:

This code may be fine in a small script.

But in an application where refund policy matters and payment providers can change, the business flow now knows too much about Stripe. Vendor language has entered application policy.

A smaller relationship is possible:

The use case depends on the port:

The adapter knows Stripe:

This is where Dependency Inversion and Ports and Adapters help.

But they help because they reduce shared knowledge between policy and infrastructure. They are not magic. Creating interfaces everywhere would not improve the design. It would only add ceremony.

The key distinction is simple:

*   Dependency Injection is a wiring technique

*   Dependency Inversion is a design principle about dependency direction

*   Ports and Adapters is an architectural style that keeps external tools at the edge  
Use them when the dependency direction matters.

Do not introduce a port just because a class talks to another class. Introduce a port when the policy should be protected from a volatile detail, an external system, or an infrastructure decision.

The structure is a boundary decision, not an interface ceremony.

A function receives this:

This example should stay bad long enough for the reader to see the smell.

The problem is not that primitives exist. The problem is that domain meaning is hidden inside primitives.

`amount` and `currency` travel together because they form a concept. That may justify a `Money` type.

This is still simplified. Real money handling needs explicit rounding rules, currency behaviour, and probably a decimal type rather than JavaScript’s `number`. The example is only about making hidden domain meaning visible.

The class structure is small, but the design move is important: meaning moves out of loose primitives and into named concepts.

`status === "P"` is connascence of meaning. A named status improves coherence:

`notifyCustomer: boolean` is control coupling. A first improvement may simply name the option:

That is not a full design transformation. It is a small tidy. It makes the call site less cryptic.

If notification behaviour becomes important, it may deserve a named policy or a separate use case. But that should come from change pressure, not from a rule that says booleans are always forbidden.

The lesson is not “wrap every primitive”. The lesson is:

> When meaning is hidden, name it. When a repeated group of values forms a concept, model it. When a flag exposes a behavioural decision, ask who should own that decision.

In Fowler’s catalog, this sits near `Replace Primitive with Object`, `Introduce Parameter Object`, and `Change Function Declaration`. But the important part is not the refactoring name. The important part is that hidden meaning has become explicit.

Tests can protect behaviour, or they can freeze implementation.

This is an over simplification in practice this is not so black or white.

Before:

This test repeats magic values. It knows vendor-level calls. It checks implementation details. It does not clearly express refund policy.

A behaviour-focused test might look like this:

This test is not better because it has more objects.

It is better only if it protects behaviour while reducing accidental coupling to vendor details.

This matters for _Test-Driven Development_ (TDD). Tests are not only safety nets. They are design feedback. A test that is hard to write may be telling you that the behaviour is in the wrong place, the boundary is unclear, or the dependency is too concrete. A test that fails on harmless refactoring may be coupled to implementation rather than behaviour.

This is also why refactoring and test design belong in the same conversation. Refactoring needs tests that protect observable behaviour. If tests lock down private collaboration, they make useful structural change expensive. If tests protect the behaviour that matters, they make small refactorings safer.

There is a caveat: not every mock is harmful, and not every in-memory fake is honest. The design question is whether the test double represents a real peer at a boundary or whether it freezes an internal collaboration that should be free to change.

Static dependencies tell us what the code says today.

Version history tells us what has been moving together.

Imagine this commit history:

*   Commit 1:

    *   `frontend-refund-validation.ts`

    *   `backend-refund-policy.ts`

*   Commit 2:

    *   `backend-refund-policy.ts`

    *   `support-refund-panel.ts`

*   Commit 3:

    *   `frontend-refund-validation.ts`

    *   `backend-refund-policy.ts`

    *   `refund-policy-tests.ts`

*   Commit 4:

    *   `backend-refund-policy.ts`

    *   `refund-email-template.ts`  
The frontend and backend files may not import each other.

But history says they are coupled.

```
Change coupling confidence from frontend refund validation to backend refund policy =
    Number of changes touching both files
    / Number of changes touching frontend refund validation
```

If frontend refund validation changes with backend refund policy eighty percent of the time, the structure may be lying. The system says “these are separate”, but the change history says “these move together”.

This does not automatically mean they should be merged. It means the relationship deserves attention. Maybe the rule should move closer to the backend. Maybe the frontend should consume a refund availability contract. Maybe the tests should be reorganized. Maybe the product behaviour genuinely requires coordinated change.

Git does not give the answer. It gives evidence. Treat that evidence carefully: commits can be too large, generated files can distort the signal, formatting commits should usually be ignored, and file renames need special handling.

[![Image 10: X avatar for @KentBeck](https://substackcdn.com/image/fetch/$s_!z82v!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1457857343568244742%2FFVQ4hpRx.jpg) Kent Beck 🌻@KentBeck for each desired change, make the change easy (warning: this may be hard), then make the easy change 11:07 PM · Sep 25, 2012 21 Replies · 1.02K Reposts · 1.93K Likes](https://x.com/KentBeck/status/250733358307500032)
Design is often discussed as if it were morality.

Clean is good. Coupled is bad. Abstract is mature. Duplication is shameful. Microservices are modern. Monoliths are old.

This language makes design conversations worse.

Software design is an economic activity. It changes the cost, risk, reversibility, and timing of future changes.

Cohesion lowers search cost. You know where to look.

Coherence lowers interpretation cost. You understand what you find.

Balanced coupling lowers propagation cost. A change does not wake the whole system without a good reason.

Poor cohesion increases navigation cost. Poor coherence increases translation cost. Strong distant volatile coupling increases coordination cost. Hidden meaning increases cognitive cost. Fragile tests increase refactoring cost. Shared internals reduce option value.

Ousterhout gives a compatible economic lens: complexity is whatever makes a system hard to understand and modify. Its visible symptoms are change amplification, cognitive load, and unknown unknowns. Those symptoms map directly onto the model in this article. Strong distant volatile coupling creates change amplification. Leaky interfaces and ambiguous primitives increase cognitive load. Incoherent names, hidden business rules, and accidental shared buckets create unknown unknowns.

His advice to separate what matters from what does not matter is another way to state the design goal here. Make important knowledge visible in the boundary that owns it. Hide knowledge that consumers should not need. Minimize the number of places where a decision matters.

That is why “tidy first” should not mean “clean everything”.

It should mean: make the structural move that lowers the cost of the change you are about to make. Then stop.

Beck has expressed the same rhythm more sharply: “For each desired change, make the change easy.” The practical sequence is not to admire structure first and change behaviour later. It is to make the next desired change easier, then make that change.

He also points to a useful asymmetry between coupling and cohesion. Coupling can be difficult to find and expensive to remove, while cohesive sub-elements are often easier and cheaper to discover. In practice, creating a cohesive sub-element often gives you the next clue about where the real decoupling opportunity lives.

That is why his line that “coupling and cohesion are the laws of physics of software design” lands so well. They are not a preference for small files, pure objects, microservices, monoliths, functions, or classes. They are the forces underneath all of those local choices.

Beck’s useful distinction is between behaviour changes and structure changes. A behaviour change alters what the system does for users. A structure change alters the arrangement of the code without changing observable behaviour. Tidying first is not a moral command to improve the codebase. It is a question about timing: would a small structural change make the next behaviour change cheaper, safer, or easier to understand?

The word “small” matters. Moving a helper, naming a concept, grouping coupled code, or extracting a narrow policy can be reversible. Extracting a service, splitting a database, or introducing a public contract can become expensive to undo once other code depends on the decision. The economic question changes with reversibility.

This is where discounted cash flows and optionality enter the design conversation. Sometimes a coupled solution is economically reasonable because it gets value to users sooner and the coupling may never become expensive. Sometimes decoupling is worth paying for now because it creates options: safer sequencing, easier rollout, independent replacement, or fewer coordinated changes later. The point is not to calculate a fake precise number. The point is to make the trade visible.

Sometimes that move is extracting a value object. Sometimes it is naming a magic value. Sometimes it is moving a rule closer to the concept it protects. Sometimes it is splitting a module. Sometimes it is introducing a port. Sometimes it is deleting code. Sometimes it is doing nothing because the code is stable, isolated, and not worth touching now.

The question is not “does this follow a principle?”.

The question is:

> What future change becomes cheaper because of this design move?

If the answer is unclear, the design move may be speculative.

Coupling is not the enemy.

The enemy is not knowing what kind of coupling we have. The enemy is hiding business meaning inside strings, numbers, booleans, and internal models. The enemy is separating things that always change together. The enemy is grouping things that have nothing to do with each other. The enemy is letting every team invent a different language for the same concept. The enemy is pretending a system is modular because it has many parts, even when every small change still travels everywhere.

A module is not a folder, class, package, or service by default. A module is a knowledge boundary around a responsibility.

Coherence asks whether the whole system still makes sense.

Cohesion asks what belongs together.

Coupling asks what knowledge makes change propagate.

Shared lifecycle asks what must move together.

Shared knowledge asks what meaning crosses a boundary.

Flow of knowledge asks which side exports assumptions and which side must live with them.

Change history asks what has actually moved together.

Those questions are more useful than most design slogans. They help us move away from purity and toward judgement.

When strongly related things live far apart, move them closer.

When unrelated things live together, split them apart.

When distance is necessary, reduce shared knowledge.

When the relationship is stable, explicit, close, and cheap, leave it alone.

When a small structural change makes the next behaviour change cheaper, tidy first.

When the structural change is large, hard to reverse, or mostly speculative, slow down and look for evidence.

The workshop does not become useful because every tool is isolated in its own locked box. It becomes useful because the layout remembers the work. The common tools are easy to reach. The dangerous tools are protected. The specialized tools are near the jobs that need them. The labels mean something. The space teaches the next person how to move.

Software design is not the pursuit of purity.

It is the arrangement of change.

*   Bay, Jeff. _Object Calisthenics, in The ThoughtWorks Anthology_. [https://www.oreilly.com/library/view/the-thoughtworks-anthology/9781934356142/](https://www.oreilly.com/library/view/the-thoughtworks-anthology/9781934356142/)

*   Beck, Kent. _Tidy First? A Personal Exercise in Empirical Software Design_. [https://www.oreilly.com/library/view/tidy-first/9781098151232/](https://www.oreilly.com/library/view/tidy-first/9781098151232/)

*   Beck, Kent. _For each desired change, make the change easy_.

[![Image 11: X avatar for @KentBeck](https://substackcdn.com/image/fetch/$s_!z82v!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1457857343568244742%2FFVQ4hpRx.jpg) Kent Beck 🌻@KentBeck for each desired change, make the change easy (warning: this may be hard), then make the easy change 11:07 PM · Sep 25, 2012 21 Replies · 1.02K Reposts · 1.93K Likes](https://x.com/KentBeck/status/250733358307500032)
*   Beck, Kent. _Coupling vs cohesion_.

[![Image 12: X avatar for @KentBeck](https://substackcdn.com/image/fetch/$s_!z82v!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1457857343568244742%2FFVQ4hpRx.jpg) Kent Beck 🌻@KentBeck Coupling vs cohesion. Coupling: • Can be hard to find • Can be really hard &/| expensive to eliminate. Cohesive sub-elements are: • Usually easy to find • Cheap to achieve, & • Help you find de-coupling. 2:25 PM · Oct 31, 2020 7 Replies · 96 Reposts · 429 Likes](https://x.com/KentBeck/status/1322545224220991488)
*   Bieman, James M., and Kang, Byung-Kyoo. _Cohesion and Reuse in an Object-Oriented System_. [https://www.cs.colostate.edu/~bieman/Pubs/aowsm95.pdf](https://www.cs.colostate.edu/~bieman/Pubs/aowsm95.pdf)

*   Booch, Grady. _Object-Oriented Analysis and Design with Applications_. [https://www.informit.com/store/object-oriented-analysis-and-design-with-applications-9780201895513](https://www.informit.com/store/object-oriented-analysis-and-design-with-applications-9780201895513)

*   Chidamber, Shyam R., and Kemerer, Chris F. _A Metrics Suite for Object Oriented Design_. [https://www.eso.org/~tcsmgr/oowg-forum/TechMeetings/Articles/OOMetrics.pdf](https://www.eso.org/~tcsmgr/oowg-forum/TechMeetings/Articles/OOMetrics.pdf)

*   Cockburn, Alistair. _Hexagonal Architecture_. [https://alistair.cockburn.us/hexagonal-architecture](https://alistair.cockburn.us/hexagonal-architecture)

*   Connascence.io. _Connascence_. [https://connascence.io/](https://connascence.io/)

*   Dijkstra, Edsger W. _On the role of scientific thought_. [https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html)

*   Fowler, Martin. _Refactoring: Improving the Design of Existing Code_. [https://martinfowler.com/books/refactoring.html](https://martinfowler.com/books/refactoring.html)

*   Fowler, Martin. _Special Case_. [https://martinfowler.com/eaaCatalog/specialCase.html](https://martinfowler.com/eaaCatalog/specialCase.html)

*   Iglesias, Fran. _Refactoring dirigido por métricas_. [https://franiglesias.github.io/metric-driven-refactoring/](https://franiglesias.github.io/metric-driven-refactoring/)

*   Khononov, Vlad. _Balancing Coupling in Software Design: Universal Design Principles for Architecting Modular Software Systems_. [https://www.informit.com/store/balancing-coupling-in-software-design-universal-design-9780137353484](https://www.informit.com/store/balancing-coupling-in-software-design-universal-design-9780137353484)

*   Lattix. _Metrics_. [https://docs.lattix.com/lattix/userGuide/Metrics.html](https://docs.lattix.com/lattix/userGuide/Metrics.html)

*   Liskov, Barbara H., and Wing, Jeannette M. _A Behavioral Notion of Subtyping_. [https://www.cs.cmu.edu/afs/cs/project/venari/www/subtype-toplas.html](https://www.cs.cmu.edu/afs/cs/project/venari/www/subtype-toplas.html)

*   Martin, Robert C. _OO Design Quality Metrics: An Analysis of Dependencies_. [https://linux.ime.usp.br/~joaomm/mac499/arquivos/referencias/oodmetrics.pdf](https://linux.ime.usp.br/~joaomm/mac499/arquivos/referencias/oodmetrics.pdf)

*   Ousterhout, John K. _A Philosophy of Software Design_. [https://web.stanford.edu/~ouster/cgi-bin/book.php](https://web.stanford.edu/~ouster/cgi-bin/book.php)

*   Parnas, David L. _On the Criteria To Be Used in Decomposing Systems into Modules_. [https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf](https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf)

*   Sharma, Tushar, and Spinellis, Diomidis. _Do We Need Improved Code Quality Metrics?_. [https://arxiv.org/abs/2012.12324](https://arxiv.org/abs/2012.12324)

*   Valverde Ramos, Emmanuel. _Introduction to Event Storming_. [https://emmanuelvalverderamos.substack.com/p/introduction-to-event-storming](https://emmanuelvalverderamos.substack.com/p/introduction-to-event-storming)

*   Zimmermann, Thomas, Weissgerber, Peter, Diehl, Stephan, and Zeller, Andreas. _Mining Version Histories to Guide Software Changes_. [https://www.st.cs.uni-saarland.de/papers/msr2004/msr2004.pdf](https://www.st.cs.uni-saarland.de/papers/msr2004/msr2004.pdf)
