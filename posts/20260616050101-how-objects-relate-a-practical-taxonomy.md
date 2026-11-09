Title: How Objects Relate: A Practical Taxonomy for Object-Oriented Design

URL Source: http://emmanuelvalverderamos.substack.com/p/how-objects-relate-a-practical-taxonomy

Final URL: https://emmanuelvalverderamos.substack.com/p/how-objects-relate-a-practical-taxonomy

Published Time: 2026-06-16T05:01:01+00:00

Markdown Content:
**Most explanations mix runtime links, type hierarchies, and design patterns into one blurry list. This article untangles them, shows where each relationship belongs, and explains the differences with real code and UML diagrams.**

[![Image 1](https://substackcdn.com/image/fetch/$s_!vPlE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04c7ffa6-04a8-49cc-8c3e-26e895e0018d_1024x558.png)](https://substackcdn.com/image/fetch/$s_!vPlE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04c7ffa6-04a8-49cc-8c3e-26e895e0018d_1024x558.png)

If you learned object relationships as a flat list like this:

*   Association

*   Dependency

*   Aggregation

*   Composition

*   Inheritance

*   Implementation

you learned something useful, but also something incomplete.

Those terms do not all answer the same question.

A better mental model is layered:

1.   **Structural links between objects**  
Association, navigability, multiplicity, qualified association, association class, self-association, aggregation, composition

2.   **Type and contract relations**  
Generalization, subtyping, subclassing, interface realization, classification

3.   **Usage and collaboration relations**  
Dependency, visibility, delegation, collaborates-with

4.   **Recurring design structures**  
Strategy, Decorator, Proxy, Observer, Composite

That layered view fits the topic far better because some relationships describe **who is linked**, some describe **what kind of thing something is**, some describe **who needs whom to work**, and some are larger recurring arrangements built from the earlier ones.

[![Image 2](https://substackcdn.com/image/fetch/$s_!gQ5a!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fafd2571c-67b9-4999-8118-2af67cb38869_1402x1122.png)](https://substackcdn.com/image/fetch/$s_!gQ5a!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fafd2571c-67b9-4999-8118-2af67cb38869_1402x1122.png)

1.   Why the usual list never quite works

2.   The layered taxonomy

3.   A quick UML notation decoder

4.   Layer 1: structural links between objects

5.   Layer 2: type and contract relations

6.   Layer 3: usage and collaboration relations

7.   Layer 4: recurring design structures

8.   The confusion that wastes the most time: composition vs composition over inheritance

9.   A practical decision guide

10.   Conclusion

11.   References

Look at these three examples:

*   An `Order` contains `OrderLine` items

*   A `CheckoutService` delegates to a `PaymentGateway`

*   A `CardPayment` is a `PaymentMethod`

All three are “object relationships” in a very broad sense.

But they are not the same kind of relationship.

One is about whole-part structure.  
One is about collaboration.  
One is about specialization and substitutability.

That is the real source of the confusion.

When these all get taught as one flat list, the words become slippery. Developers can repeat the definitions, but they still hesitate when they look at real code because they are answering different questions with the same mental drawer. The modelling literature separates structural links, type relations, and collaboration concerns much more carefully than most classroom cheat sheets do.

So the unlock for this whole topic is simple:

> Not all object relationships are relationships of the same kind.

Once you accept that, the fog starts to lift.

Here is the map we will use.

![Image 3](https://substackcdn.com/image/fetch/$s_!gwwi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0489d0b0-7686-46f2-9538-2ea2736ab70a_2213x396.png)

Each layer answers a different question:

*   **Structural links** ask: who is related to whom?

*   **Type and contract relations** ask: what kind of thing is this, and what can stand in for what?

*   **Usage and collaboration relations** ask: who needs whom to get work done?

*   **Recurring design structures** ask: what larger arrangements show up again and again in good designs?

This is the most useful mental model in the whole article. It turns a memorization problem into a judgment problem.

Before going deeper, it helps to know what the main arrows and markers are trying to say.

*   **Association**: solid line. A stable structural relation.

*   **Dependency**: dashed arrow. Temporary use or reliance.

*   **Generalization / inheritance**: solid line with hollow triangle toward the more general type.

*   **Interface realization**: dashed line with hollow triangle toward the interface.

*   **Aggregation**: hollow diamond at the whole side.

*   **Composition**: filled diamond at the whole side.

*   **Multiplicity**: labels like `1`, `0..1`, `*`, `1..*`.

*   **Qualified association**: a key such as `[sku]` is shown at the association end.

*   **Association class**: the relationship itself is promoted to a class with its own data.

A compact picture helps:

[![Image 4](https://substackcdn.com/image/fetch/$s_!FfwV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d0305bf-1996-4bfc-aa50-17b783ddbfd5_1956x516.png)](https://substackcdn.com/image/fetch/$s_!FfwV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d0305bf-1996-4bfc-aa50-17b783ddbfd5_1956x516.png)

UML is not trying to decorate boxes with different arrows. It is trying to encode different kinds of meaning.

This is the most intuitive layer.

It answers the most natural question:

**Who is linked to whom?**

An **association** is a stable semantic link between objects.

In plain English:

One object knows about, refers to, or is related to another in a way that is part of the object model.

A simple example:

*   an `Order` is placed by a `Customer`

[![Image 5](https://substackcdn.com/image/fetch/$s_!WgGE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F464a4182-be92-4c27-ae1f-b44815ed1b47_222x516.png)](https://substackcdn.com/image/fetch/$s_!WgGE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F464a4182-be92-4c27-ae1f-b44815ed1b47_222x516.png)

Why this is association:

*   The link is part of the structure of `Order`

*   The relationship is stable enough to live in the model

*   You can ask an order who placed it

The important point is not “there is contact between two objects.” The important point is that the relationship belongs to the structure of the model. That is what makes this different from a temporary dependency.

Once you have an association, two more questions matter:

*   Can one side navigate to the other?

*   How many instances can participate?

These sound small, but they change the meaning of the model.

`Order` knows its `Customer`, but `Customer` does not expose orders directly.

Now `Customer` also tracks its orders.

This is not about ownership.

It is about **traversability**.

And multiplicity matters too:

*   One customer may place many orders

*   Each order usually has one customer

Association tells you that a link exists. Navigability tells you who can follow it. Multiplicity tells you how many related instances there may be. Keeping those separate makes diagrams and code much easier to read.

> Association tells you that a link exists. Navigability tells you who can follow it. Multiplicity tells you how many links there may be.

A class can be associated with itself.

That sounds advanced, but it is ordinary.

A simple example:

*   An employee mentors another employee

[![Image 6](https://substackcdn.com/image/fetch/$s_!DOGX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55e0cade-da08-4dd8-9f0c-9e332a68e22e_236x448.png)](https://substackcdn.com/image/fetch/$s_!DOGX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55e0cade-da08-4dd8-9f0c-9e332a68e22e_236x448.png)

This is still association.

It is not inheritance.

That matters because the same class appears on both ends, but the question is still “who relates to whom?”, not “what kind of thing is this?”.

A **qualified association** is a relationship accessed through a key.

In software terms, the easiest way to picture it is this:

one object has access to a larger related set, but reaches a specific related object by using a qualifier such as an identifier.

A clean example is a product catalog looking up product descriptions by SKU.

![Image 7](https://substackcdn.com/image/fetch/$s_!eAzA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F278e3f5c-2a4c-494b-b1b6-6a95751a81c6_367x516.png)

Why this matters:

*   It is not just “the catalog has many products”

*   The key is part of how the relationship is understood

*   It turns lookup into part of the model rather than leaving it as a hidden implementation detail

A useful side effect of qualification is that it often reduces multiplicity at the target end, because the key usually selects one object from a larger set.

Sometimes the relationship itself has meaningful data.

That is the moment a plain association stops being enough.

A classic example:

*   A student is enrolled in a course

*   But the **enrollment** has its own data: date, status, grade

[![Image 8](https://substackcdn.com/image/fetch/$s_!riIL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20ac863b-5ba2-48d0-ba75-a3ff6aa626cf_446x588.png)](https://substackcdn.com/image/fetch/$s_!riIL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20ac863b-5ba2-48d0-ba75-a3ff6aa626cf_446x588.png)

Why this is not just a many-to-many association:

*   The relationship now has its own information

*   The relationship becomes a concept worth naming

*   The model becomes clearer once the link is promoted to a first-class citizen

Many messy many-to-many models are really unnamed association classes. That is one of the most useful modelling upgrades developers learn once they stop treating associations as only lines between boxes.

> Many messy many-to-many designs are really unnamed association classes.

I want to be very explicit here.

I am keeping aggregation **brief and precise on purpose**.

Not because it does not exist.  
Not because you will never see it.  
But because it is one of the least useful distinctions in the standard list.

A practical definition is this:

**aggregation is a weak whole-part relation where the part can exist independently of the whole**

A small example:

*   A `Department` has `Professor` objects

*   A professor can exist without that department

[![Image 9](https://substackcdn.com/image/fetch/$s_!-WGv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3fd0736-a483-4d59-9e9a-c1ddfccab944_258x516.png)](https://substackcdn.com/image/fetch/$s_!-WGv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3fd0736-a483-4d59-9e9a-c1ddfccab944_258x516.png)

Why I am not giving aggregation more space:

*   It is intentionally weak

*   It often says little that plain association does not already say

*   It is much less actionable than composition in real modelling work

That is why aggregation deserves recognition, but not obsession. If association already says enough, use association. If lifecycle ownership matters, use composition.

> If association already says enough, use association. If lifecycle ownership matters, use composition.

**Composition** is the strong whole-part relation.

This one matters much more.

The practical test is simple:

*   The part belongs to one whole at a time

*   The part is not conceptually free-floating

*   The whole is responsible for the part’s lifecycle

A very good example is `Order` and `OrderLine`.

[![Image 10](https://substackcdn.com/image/fetch/$s_!L6TO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed8321ff-5954-418d-a995-9acbe85d881f_231x516.png)](https://substackcdn.com/image/fetch/$s_!L6TO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed8321ff-5954-418d-a995-9acbe85d881f_231x516.png)

Why this is composition:

*   An order line exists as part of an order

*   The order controls creation of its lines

*   Lifecycle ownership is the point of the relationship

Association says linked. Composition says owned as part of the whole. That is the real distinction worth remembering.

> Association says linked. Composition says owned as part of the whole.

[![Image 11](https://substackcdn.com/image/fetch/$s_!kMwr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F301ce12b-ae58-4415-82bf-015669c62e8d_802x559.png)](https://substackcdn.com/image/fetch/$s_!kMwr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F301ce12b-ae58-4415-82bf-015669c62e8d_802x559.png)

Now the question changes.

We are no longer asking:

**Who is linked to whom?**

We are asking:

*   What kind of thing is this?

*   What contract does it satisfy?

*   What may stand in for what?

That is where inheritance belongs.

A **generalization** says that one thing is a more specific kind of another.

A simple example:

[![Image 12](https://substackcdn.com/image/fetch/$s_!u1-v!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c8256c9-f278-4c3e-ab65-cc38a409d317_749x468.png)](https://substackcdn.com/image/fetch/$s_!u1-v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c8256c9-f278-4c3e-ab65-cc38a409d317_749x468.png)

Why this is different from association:

*   The question is not “**what is linked?**”

*   The question is “**what kind of thing is this?**”

*   `CardPayment`**is a**`PaymentMethod`

This layer is about taxonomy, substitutability, and contract, not about runtime links between objects.

This is one of the most important distinctions in the whole article.

They are related, but not identical.

*   **subtyping** is about contract and substitutability

*   **subclassing** is about inheriting implementation structure

You can have subtyping without shared implementation inheritance.

Both classes satisfy the same contract.

Neither inherits implementation from a base class.

That difference matters because many bad hierarchies come from confusing reuse with meaning.

A subtype promises. A subclass reuses. Sometimes one does both. They are still not the same idea. And when you confuse them, you start inheriting because code is nearby instead of inheriting because meaning and substitutability are truly there.

> A subtype promises. A subclass reuses. Sometimes one does both. They are still not the same idea.

When a class satisfies an interface contract, UML calls that **interface realization**.

That is a better phrase than the loose classroom word “implementation” because it tells you what matters most: the class is realizing a contract.

[![Image 13](https://substackcdn.com/image/fetch/$s_!ocfH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52088802-8047-4e6b-93fe-76fe3f2e6473_427x516.png)](https://substackcdn.com/image/fetch/$s_!ocfH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52088802-8047-4e6b-93fe-76fe3f2e6473_427x516.png)

Why this is different from inheritance:

*   No shared base implementation is required

*   The focus is contract conformance

*   It belongs to the type-and-contract layer, not the structural link layer

This becomes especially useful when you build systems around delegation, substitution, and dependency inversion instead of rigid hierarchies.

One of the easiest traps in object modelling is treating every domain distinction as a subclassing problem.

But classification is richer than that.

A customer might be:

*   Corporate

*   Priority

*   Suspended

*   Credit-approved

If you try to force all of those into one inheritance tree, you quickly create either nonsense or class explosion.

Real domains often contain several independent classification dimensions, and inheritance trees are frequently a poor fit for that. This becomes even clearer when you consider multiple classification and dynamic classification, both of which show that type can be more fluid and more multi-dimensional than mainstream inheritance trees suggest.

That matters because it teaches a deeper lesson:

sometimes the right answer is not “build a bigger hierarchy.”

Sometimes the right answer is “this distinction belongs to state, role, policy, or collaboration instead.”

Now the question changes again.

We are no longer asking who is linked or what kind of thing something is.

We are asking:

*   Who needs whom to do work?

*   How does one object gain access to another?

*   When is the relationship structural, and when is it just operational?

A **dependency** is a weaker relation than association.

A simple rule of thumb:

if one object only needs another object temporarily in order to do some work, you are usually looking at a dependency rather than a structural association.

[![Image 14](https://substackcdn.com/image/fetch/$s_!21B6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a94eec9-af6e-4563-a8e1-6821d526f9b8_257x516.png)](https://substackcdn.com/image/fetch/$s_!21B6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a94eec9-af6e-4563-a8e1-6821d526f9b8_257x516.png)

Why this is dependency:

*   The relation is operational

*   The pricer does not need to keep the policy as part of its identity

*   The other object is needed to perform an action, not define structure

Association tends to live in the object. Dependency tends to live in the action.

> Association tends to live in the object. Dependency tends to live in the action.

In code, collaboration does not happen by magic.

One object needs some path to another.

That is where **visibility** matters.

A practical set of forms is:

*   Attribute visibility

*   Parameter visibility

*   Local visibility

*   Global visibility

The object keeps the collaborator as state.

The collaborator is passed in only for the current call.

The collaborator is created or captured inside the method.

The collaborator is globally reachable.

This exists, but it is usually the least interesting and often the least desirable form in object design.

Why this matters:

visibility is not exactly a domain relationship.

It is the access path that makes collaboration possible in the design.

That is subtle, but very practical.

Delegation is one of the most important object relationships in day-to-day design.

One object receives a request, then hands responsibility to another object that is better suited to do the work.

[![Image 15](https://substackcdn.com/image/fetch/$s_!7f9w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a32c10e-18c0-44f2-a5aa-e6a7714f3f7f_1073x534.png)](https://substackcdn.com/image/fetch/$s_!7f9w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a32c10e-18c0-44f2-a5aa-e6a7714f3f7f_1073x534.png)

Why this matters:

*   Delegation is not inheritance

*   Delegation is not UML composition

*   Delegation is about behavioral handoff

It is often the quiet answer to problems that people first try to solve with inheritance. If a class really just needs another object to perform a behavior, delegation is usually clearer than pretending one object is a more specific kind of the other.

> Delegation is often the quiet answer to problems that people first try to solve with inheritance.

[![Image 16](https://substackcdn.com/image/fetch/$s_!zvFo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4a7e36d-2714-4b9b-9058-d47fc158c799_1024x559.png)](https://substackcdn.com/image/fetch/$s_!zvFo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4a7e36d-2714-4b9b-9058-d47fc158c799_1024x559.png)

This distinction is easy to miss, but very valuable.

Not every “uses” relation deserves the same conceptual weight.

Sometimes one object merely uses another as a tool.

Sometimes two objects genuinely collaborate to fulfill behavior.

That difference matters because it changes how central the relationship is to the design.

A logger may be merely used.

A checkout service and payment gateway collaborate.

A pricing service and discount policy collaborate.

That is a useful mental move even if you never draw it on a UML diagram. It pushes you to ask:

is this other object just nearby, or is it part of how this object fulfills its responsibility? Some object-oriented traditions treat `collaborates-with` as one of the few relations that says something intrinsic about an object’s role, which is one reason this distinction is so valuable in practice.

Now we reach the level where many taxonomies become messy.

Patterns.

Here is the clean way to place them:

**patterns are recurring arrangements built from simpler relations, not primitive peer categories beside association or inheritance**

That keeps the taxonomy from exploding.

It also keeps the article honest. When you say “Strategy,” “Decorator,” or “Observer,” you are usually naming a larger arrangement of contracts, links, delegation, and lifecycle decisions, not a new primitive relation.

**Problem:** vary behavior without changing the context.

**Builds on:** interface realization, dependency, delegation.

[![Image 17](https://substackcdn.com/image/fetch/$s_!HIdY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09539217-83a6-4897-b582-7977a298b795_504x916.png)](https://substackcdn.com/image/fetch/$s_!HIdY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09539217-83a6-4897-b582-7977a298b795_504x916.png)

What matters here is that the context does not hard-code one behavior. It depends on a contract and hands the work to whichever strategy it receives. That is why Strategy is one of the clearest examples of composition over inheritance in practice.

**Problem:** add responsibilities without changing the outward contract.

**Builds on:** interface realization, composition, delegation.

[![Image 18](https://substackcdn.com/image/fetch/$s_!gkzK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f05e5e1-986f-4333-95d7-a45e89b457e3_1168x768.png)](https://substackcdn.com/image/fetch/$s_!gkzK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f05e5e1-986f-4333-95d7-a45e89b457e3_1168x768.png)

The decorator keeps the same outward contract, stores a wrapped component through that contract, and delegates work to it while adding behavior around the call. Structurally it resembles Proxy, but the intent is different: Decorator enhances behavior. Proxy controls access.

**Problem:** control access to a real subject or stand in for it.

**Builds on:** interface realization, association, delegation.

[![Image 19](https://substackcdn.com/image/fetch/$s_!y3BP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9049c6d-5d9e-4366-bfb0-6361c6e41878_812x768.png)](https://substackcdn.com/image/fetch/$s_!y3BP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9049c6d-5d9e-4366-bfb0-6361c6e41878_812x768.png)

Proxy and Decorator can look structurally similar, but their intent is different. Proxy stands in for the real subject and controls access to it. Decorator adds responsibilities while preserving the same base interface.

**Problem:** propagate a change or event to many dependents.

**Builds on:** association or dependency, notification collaboration, one-to-many propagation.

[![Image 20](https://substackcdn.com/image/fetch/$s_!VbEX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe283b4fa-2e8c-4604-93e7-322acbe0dfab_422x648.png)](https://substackcdn.com/image/fetch/$s_!VbEX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe283b4fa-2e8c-4604-93e7-322acbe0dfab_422x648.png)

[![Image 21](https://substackcdn.com/image/fetch/$s_!-cXx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F896e86dd-c6e0-4949-a669-c9dbdb321990_1306x534.png)](https://substackcdn.com/image/fetch/$s_!-cXx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F896e86dd-c6e0-4949-a669-c9dbdb321990_1306x534.png)

Observer is easier to understand when you see both pieces:

*   The static structure: one subject, many observers

*   The dynamic flow: one event, many notifications

That is why a diagram helps here more than a paragraph alone.

**Problem:** treat one object and a whole tree of objects uniformly.

**Builds on:** interface realization, recursive association, and often composition.

A familiar example is packaging:

*   A box can contain products

*   A box can also contain smaller boxes

*   Both can be treated through the same interface when you calculate total price

[![Image 22](https://substackcdn.com/image/fetch/$s_!zUqr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe723b718-f2f9-4f1c-8264-ea86eb314061_1012x816.png)](https://substackcdn.com/image/fetch/$s_!zUqr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe723b718-f2f9-4f1c-8264-ea86eb314061_1012x816.png)

What matters here is the recursive structure:

*   Leaves and containers share one common interface

*   The container stores children through that same interface

*   The client can treat one object and a whole tree in the same way

This is also why Composite is easy to confuse with composition. Composite is a **pattern** that often uses composition. Composition is a **relationship** about ownership and lifecycle. They are related, but not the same thing.

> Patterns are not missing relationship types. They are recurring structures built from simpler ones.

These are not the same thing.

They answer different questions.

And a lot of confusion disappears once you separate them.

This is the relationship we covered earlier:

*   Strong whole-part

*   Lifecycle ownership

*   One whole responsible for its parts

Example:

*   `Order` composed of `OrderLine`

That is a structural modelling idea.

It tells you something about ownership, containment, and lifecycle.

This is not a UML relation.

It is a design guideline.

It means:

Prefer assembling behavior from collaborating objects instead of subclassing just to reuse behavior.

Here the service is not a whole made of parts in the UML sense.

Instead, the design is assembling behavior through collaboration.

Same word root. Different question.

> UML composition asks: who owns the part?  
> Composition over inheritance asks: how should behavior be assembled?

This is the part that usually gets skipped too quickly, and it is the part that gives the guideline its practical force.

Inheritance is not bad.

But it is very easy to reach for it too early because it feels tidy at first.

Two classes share some behavior.  
So you extract a base class.  
Now the duplication is gone and the hierarchy looks cleaner.

At that point, inheritance feels like a win.

The problems usually show up later.

A subclass cannot freely stop being what the parent says it is.  
It cannot quietly narrow the parent contract just because that would be convenient.  
If it overrides behavior, it is still expected to remain compatible with what callers already expect from the base type.

That is where the pressure starts.

[![Image 23](https://substackcdn.com/image/fetch/$s_!j2te!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4412d3e0-4046-4818-8457-5dc4f288f0ed_1408x768.png)](https://substackcdn.com/image/fetch/$s_!j2te!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4412d3e0-4046-4818-8457-5dc4f288f0ed_1408x768.png)

The subclass is no longer just reusing code.  
It is also carrying the meaning, assumptions, and constraints of the parent.

That creates a few common problems:

*   Subclasses become tightly coupled to superclasses

*   Internal details of the parent start leaking into child classes

*   Changes in the parent can ripple into several descendants

*   One inheritance tree is often forced to represent several variation dimensions at once

And that last point is where designs often become brittle.

Maybe one hierarchy started as a clean taxonomy.  
Later it also needs to express discount rules.  
Then output format.  
Then delivery policy.  
Then validation differences.

Now the hierarchy is doing too many jobs at once.

Composition helps because it keeps those decisions more local.

[![Image 24](https://substackcdn.com/image/fetch/$s_!Y4Qp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a5b3ce0-46d7-491c-a91d-a42ffdf5881f_1408x768.png)](https://substackcdn.com/image/fetch/$s_!Y4Qp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a5b3ce0-46d7-491c-a91d-a42ffdf5881f_1408x768.png)

A service can delegate pricing to a pricing policy.  
A formatter can wrap another formatter.  
A checkout flow can collaborate with a payment gateway.  
A class can satisfy a contract without inheriting implementation from a parent.

That usually gives you a flatter and more flexible design:

*   Behavior can vary independently

*   Responsibilities are easier to isolate

*   Changes stay more local

*   One variation does not automatically force a redesign of the whole hierarchy

*   Several dimensions of change do not immediately explode into subclass combinations

So the real takeaway **is not**:

“inheritance is wrong.”

It is:

**Use inheritance when you truly have a stable kind-of relationship and safe substitutability. Use composition when what you really need is flexible behavior assembly.** Composition over inheritance is recommended precisely because inheritance brings interface pressure, encapsulation leakage, tight coupling, and the risk of parallel hierarchy explosion when several variation dimensions are forced into one tree.

Another time I use inheritance is when I’m refactoring; s**ometimes it’s a useful intermediate step** that will eventually be removed once the refactoring is complete, but it’s a step I take to start refactoring what I want. Examples of this include when you have to use legacy code techniques such as “Subclass and Override Method”.

When you are not sure which relationship you are looking at, do not start by memorizing notation.

Start by asking the right question.

[![Image 25](https://substackcdn.com/image/fetch/$s_!z4FQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e3a6abe-2101-475b-b5f3-d14e3639602b_3162x5515.png)](https://substackcdn.com/image/fetch/$s_!z4FQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e3a6abe-2101-475b-b5f3-d14e3639602b_3162x5515.png)

The goal is not to turn judgment into a flowchart. The goal is to prevent category mistakes.

Most mistakes here happen because people pick a label before they decide which layer they are working in.

[![Image 26](https://substackcdn.com/image/fetch/$s_!kXv0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21af7328-9669-4b20-89f6-4690df1b90b0_3600x2655.png)](https://substackcdn.com/image/fetch/$s_!kXv0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21af7328-9669-4b20-89f6-4690df1b90b0_3600x2655.png)

Most confusion about object relationships is not caused by impossible definitions.

It is caused by flattening several different kinds of design decision into one list.

Once you separate the layers, the topic becomes much calmer:

structural links tell you who is related to whom

type and contract relations tell you what kind of thing something is and what it promises

usage and collaboration relations tell you who needs whom to get work done

recurring design structures tell you how simpler relations are repeatedly combined in good designs

That layered view does something important: it helps you choose the right question before you choose the label.

*   If you are describing a stable link, you are probably in the structural layer.

*   If you are describing kind-of meaning or contract conformance, you are in the type layer.

*   If you are describing temporary use or behavioral handoff, you are in the collaboration layer.

*   If you are describing a larger recurring arrangement such as Strategy, Decorator, Proxy, Observer, or Composite, you are no longer dealing with a primitive relation at all. You are looking at a design structure built from several simpler ones.

That is also why some distinctions deserve more weight than others.

Aggregation is worth recognizing, but rarely worth centering.  
Composition matters because ownership and lifecycle matter.  
Subtyping and subclassing must be kept separate because substitutability and implementation reuse are not the same decision.  
And composition over inheritance matters because it reminds us that flexible behavior is often assembled more safely through contracts, delegation, and collaboration than through deep hierarchies.

In the end, the problem was never the words themselves.

The problem was using one flat vocabulary for several different kinds of meaning.

Once you stop doing that, object relationships stop feeling slippery. The arrows become easier to read. The code becomes easier to model. And the design decisions behind both become easier to explain.

> The real skill is not memorizing the notation. The real skill is noticing which layer you are in.

This article is grounded mainly in these uploaded sources:

*   **David West,**_**Object Thinking**_  
Especially useful for the distinction between intrinsic and situational relationships, and for the importance of `is-a-kind-of` and `collaborates-with`.

*   **Martin Fowler,**_**Analysis Patterns**_  
Especially useful for association vs mapping, generalization, subtyping vs subclassing, multiple classification, and dynamic classification.

*   **Craig Larman,**_**Applying UML and Patterns**_  
Especially useful for qualified association, association class, visibility, aggregation, composition, and UML notation for interface realization.

*   **Alexander Shvets,**_**Dive Into Design Patterns**_  
Useful for the practical framing of object relations, the rationale behind favoring composition over inheritance, and the structural understanding of Decorator, Proxy, Strategy, Observer, and Composite.
