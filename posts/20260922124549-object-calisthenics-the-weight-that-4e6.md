Title: Object Calisthenics: the weight that teaches objects to think

URL Source: http://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6

Final URL: https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6

Published Time: 2026-09-22T12:45:49+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!eBJq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f79502b-3480-4f56-b3b0-241e48472cf3_1024x559.png)](https://substackcdn.com/image/fetch/$s_!eBJq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f79502b-3480-4f56-b3b0-241e48472cf3_1024x559.png)

A movement can look correct until weight is added. A squat without weight may hide the knee that falls inward. A plank may look stable until the body starts shaking after twenty seconds. A runner can move quickly for years while compensating with the wrong muscles. Then a coach changes one thing: slower tempo, stricter posture, less momentum, more control. Suddenly the body tells the truth.

Code does the same.

A method with three nested decisions looks fine while the feature is small. A string that represents a country code feels practical until validation appears in five places. A list of order lines looks harmless until filtering, pricing, formatting, and shipment rules start orbiting around it. A getter feels innocent until half the system uses it to make decisions that the object itself should understand.

Object Calisthenics adds weight to code. Not production weight, but training weight.

Jeff Bay introduced Object Calisthenics in _The ThoughtWorks Anthology_ as an exercise made of nine strict rules. The exercise is simple: write a small object-oriented program under constraints that are stricter than normal, then observe what the code forces you to change. Once the exercise has done its work, the rules are relaxed into guidelines.

That framing matters because Object Calisthenics is easy to ruin. Treat it as a universal checklist and it becomes dogma. Treat it as a style guide and it becomes shallow. Treat it as a static-analysis score and it becomes theatre. Its value is not obedience. Its value is perception.

Object Calisthenics trains the eye to see responsibility:

1.   Where is behavior misplaced?

2.   Where does data leak?

3.   Where is a primitive hiding a domain concept?

4.   Where is a collection doing work without a name?

5.   Where does one object know too much about another?

6.   Where have objects become procedural records wearing class syntax?

The nine rules are not the design.

They are the weights that reveal the design.

[![Image 2](https://substackcdn.com/image/fetch/$s_!-i-G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2300f3af-7e5b-4e48-a913-69d3b990a8d5_1448x1086.png)](https://substackcdn.com/image/fetch/$s_!-i-G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2300f3af-7e5b-4e48-a913-69d3b990a8d5_1448x1086.png)

Object Calisthenics is a strict object-oriented design exercise introduced by Jeff Bay. It asks developers to write a small project using nine constraints:

1.   One level of indentation per method

2.   No `else`

3.   Wrap primitives and strings

4.   First-class collections

5.   One dot per line

6.   No abbreviations

7.   Small entities

8.   No more than two instance variables

9.   No getters, setters, or public properties

The rules are best understood as design detectors. They reveal mixed abstraction levels, branch-heavy logic, primitive obsession, leaked collection behavior, knowledge leakage, weak naming, poor cohesion, data clumps, and behavior that has been stolen from the object that owns the data.

The deeper goal is responsibility placement. Good object-oriented design is not about having many classes. It is about giving concepts, decisions, invariants, and collaborations the right home.

This article uses one running example. The first version is intentionally poor because we need to see the smell. The corrected version is tested and follows the exercise much more strictly. The tests are not decoration. They show how the design is used, how the collaboration changes, and which behavior stays stable while the structure moves.

Use Object Calisthenics in katas, refactoring practice, domain-heavy code, teaching, pair programming, and design workshops. Apply it carefully around DTOs, read models, serialization objects, ORM mappings, framework adapters, generated code, and performance-sensitive low-level code.

The rule is not the lesson. The discomfort is the lesson.

1.   [The running example: an order that may or may not ship](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7the-running-example-an-order-that-may-or-may-not-ship)

2.   [Baseline production code: the movement before adding weight](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7baseline-production-code-the-movement-before-adding-weight)

3.   [Baseline tests: protecting behavior and exposing collaboration](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7baseline-tests-protecting-behavior-and-exposing-collaboration)

4.   [What the baseline tests already reveal](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7what-the-baseline-tests-already-reveal)

5.   [What Object Calisthenics is](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7what-object-calisthenics-is)

6.   [Rules are not principles](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7rules-are-not-principles)

7.   [Object-oriented syntax is not object thinking](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7object-oriented-syntax-is-not-object-thinking)

8.   [The real target: responsibility placement](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7the-real-target-responsibility-placement)

9.   [The nine rules as design detectors](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7the-nine-rules-as-design-detectors)

10.   [From smell to corrected design](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7from-smell-to-corrected-design)

11.   [What the tests reveal about the interface](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7what-the-tests-reveal-about-the-interface)

12.   [Change 1: from](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-1-from-string-status-to-orderstatus)`String status`[to](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-1-from-string-status-to-orderstatus)`OrderStatus`

13.   [Change 2: from](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-2-from-string-countrycode-to-countrycode)`String countryCode`[to](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-2-from-string-countrycode-to-countrycode)`CountryCode`

14.   [Change 3: from](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-3-from-int-weightingrams-to-weight)`int weightInGrams`[to](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-3-from-int-weightingrams-to-weight)`Weight`

15.   [Change 4: from](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-4-from-orderitembefore-to-orderline)`OrderItemBefore`[to](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-4-from-orderitembefore-to-orderline)`OrderLine`

16.   [Change 5: from](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-5-from-listorderitembefore-to-orderlines)`List<OrderItemBefore>`[to](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-5-from-listorderitembefore-to-orderlines)`OrderLines`

17.   [Change 6: from](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-6-from-supportedcountries-to-shippingpolicy)`SUPPORTED_COUNTRIES`[to](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-6-from-supportedcountries-to-shippingpolicy)`ShippingPolicy`

18.   [Change 7: from external service decision to](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7change-7-from-external-service-decision-to-order)`Order`

19.   [The public API before and after](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7the-public-api-before-and-after)

20.   [The second requirement: digital items can ship without weight](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7the-second-requirement-digital-items-can-ship-without-weight)

21.   [Factory and builder: a separate construction concern](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7factory-and-builder-a-separate-construction-concern)

22.   [The resulting production model](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7the-resulting-production-model)

23.   [The resulting JUnit 5 tests](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7the-resulting-junit-5-tests)

24.   [The collaboration changes with the design](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7the-collaboration-changes-with-the-design)

25.   [A map of the design pressure](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7a-map-of-the-design-pressure)

26.   [When the rules fight each other](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7when-the-rules-fight-each-other)

27.   [Fake compliance](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7fake-compliance)

28.   [When Object Calisthenics helps](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7when-object-calisthenics-helps)

29.   [When Object Calisthenics hurts](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7when-object-calisthenics-hurts)

30.   [Practicing safely with tests and baby steps](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7practicing-safely-with-tests-and-baby-steps)

31.   [Conclusions](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7conclusions)

32.   [References](https://emmanuelvalverderamos.substack.com/p/object-calisthenics-the-weight-that-4e6?open=false#%C2%A7references)The running example: an order that may or may not ship

[![Image 3](https://substackcdn.com/image/fetch/$s_!12BM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbe29ad8-e014-4b8d-adf8-cb30762838cd_1024x559.png)](https://substackcdn.com/image/fetch/$s_!12BM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbe29ad8-e014-4b8d-adf8-cb30762838cd_1024x559.png)

We will use one example throughout the article. The domain is simple: deciding whether an order can be shipped.

Initial business rule:

1.   The order must be paid

2.   The shipping country must be supported

3.   The order must have at least one item

4.   Every item must have a positive weight

The supported countries are Spain, Germany, and France. In the code, we will use `ES` as the default positive example, then cover `DE` and `FR` explicitly through tests.

The first version is deliberately ordinary. It is the kind of code that can survive for a while without attracting attention. That is exactly why it is useful for learning. The movement looks fine before weight arrives.

[![Image 4](https://substackcdn.com/image/fetch/$s_!FJlk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78ed051f-8a3e-4119-aa4f-d2b597688543_1024x559.png)](https://substackcdn.com/image/fetch/$s_!FJlk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78ed051f-8a3e-4119-aa4f-d2b597688543_1024x559.png)

The following code intentionally violates Object Calisthenics. That is the point. It is the smell we are going to study.

This code is easy to defend. It is short, direct, and readable enough. It has no clever abstraction. It has one public decision method. A team under pressure could ship it and move on.

That is the trap. The method knows too much:

1.   It knows that a paid order is represented by the string `"PAID"`

2.   It knows that supported destinations are represented by country-code strings

3.   It knows that an order has a shipping address

4.   It knows that a shipping address has a country code

5.   It knows that an order has items

6.   It knows that items are stored in a collection

7.   It knows that an item with non-positive weight cannot be shipped

This is a lot of knowledge for one method. If the business adds suspended orders, digital items, hazardous goods, warehouse restrictions, partial shipments, or carrier-specific rules, this method will invite more branches. The posture is already there. The extra weight has not arrived yet.

The structure explains the smell better than the method alone:

The arrows are the problem. The service does not collaborate with an order as a responsible object. It interrogates a small object graph and assembles the decision elsewhere.

Object Calisthenics helps us see the posture before it becomes injury.

[![Image 5](https://substackcdn.com/image/fetch/$s_!LfUz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa67626a2-b76f-4fd7-bee7-0e6759c330f3_1024x559.png)](https://substackcdn.com/image/fetch/$s_!LfUz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa67626a2-b76f-4fd7-bee7-0e6759c330f3_1024x559.png)

Before changing the design, we need tests. Without tests, refactoring becomes guessing.

These first tests are characterization tests. They capture what the current code does. They are not trying to bless the design. They protect behavior while we move the structure.

The tests use JUnit 5. Repeated equivalent business cases are expressed as parameterized tests. Each test has one reason to fail. When a test covers several inputs, those inputs represent the same behavior.

These tests do two jobs.

The first job is obvious: they protect behavior. If we change the internal structure and one of these cases breaks, we know we changed more than design.

The second job is more interesting: they reveal the collaboration style. The setup passes raw strings for status and country. It passes an integer for weight. It builds an order, an address, and items, then asks a service to interrogate them. The test is not only checking behavior. It is showing how the design feels from the outside.

Good tests do that. They reveal the shape of collaboration.

[![Image 6](https://substackcdn.com/image/fetch/$s_!bDZy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61ac991f-9455-4c7c-bb62-3af3ec6b027c_1024x559.png)](https://substackcdn.com/image/fetch/$s_!bDZy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61ac991f-9455-4c7c-bb62-3af3ec6b027c_1024x559.png)

The baseline test says this:

That looks convenient, but it hides three decisions:

1.   What is a valid order status?

2.   What is a valid country code?

3.   Can a weight be negative, zero, or missing?

The test is already showing primitive obsession before the production code is inspected. A raw `"PAID"` is not just text. A raw `"ES"` is not just text. A raw `100` is not just a number. These values carry domain meaning, but the model has no place to protect that meaning yet.

The baseline also shows externalized behavior:

That call may look normal, but it tells us something about responsibility placement. The shipping decision lives outside the order. The service must ask the order for data, walk through its address, inspect its item collection, and evaluate each item weight. The order is present, but it does not own the question.

The extra one-item and multiple-item cases matter because they expose collection behavior as behavior, not just storage. An empty list, one valid line, many valid lines, and many lines with one invalid line are different pressures on the design. The baseline service handles all of them by reaching into the collection itself. That is the smell.

This is why tests are not only a safety net. They are design feedback.

[![Image 7](https://substackcdn.com/image/fetch/$s_!K8iP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc295cc53-9fd8-45d5-a821-42793cceda75_1024x559.png)](https://substackcdn.com/image/fetch/$s_!K8iP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc295cc53-9fd8-45d5-a821-42793cceda75_1024x559.png)

Object Calisthenics comes from Jeff Bay’s chapter in _The ThoughtWorks Anthology_. Bay’s proposal was not a new object-oriented theory. It was an exercise. Take a small project, around one thousand lines of code, and apply nine strict rules. The rules are intentionally harder than everyday production standards because the goal is to change how the developer sees object-oriented design.

It is not a framework, an architecture, or a production standard. It is a deliberately artificial constraint exercise. The code is the training ground, and the rules are temporary resistance used to expose design decisions that ordinary coding often hides.

That is why the word “calisthenics” matters. Physical calisthenics uses the body’s own weight to develop strength, control, harmony, and precision. Object Calisthenics uses the code’s own structure to develop design perception. The program becomes the body. The rules become the training load. Refactoring becomes the movement.

Bay’s own framing contains the nuance people often lose later. The rules are rigid during the exercise, then they become guidelines. They can contradict one another. They can lead to poor results when applied mechanically. This is not a small footnote. It is the key to the whole practice.

A strict exercise can teach better judgment, but a strict exercise should not replace judgment. The real value is not that a class ends under fifty lines or that a method has one indentation level. The real value is that, while trying to satisfy those constraints, the developer has to ask questions that ordinary code lets them avoid:

*   Why is this method so deep?

*   Why does this branch know the type of the thing it is handling?

*   Why is this `String` carrying business meaning?

*   Why does this service know the inside of an order, its address, its lines, its weights, and its shipping rules?

*   Why does this object expose data instead of behavior?

Object Calisthenics makes the easy answer unavailable for a while. That is the training.

[![Image 8](https://substackcdn.com/image/fetch/$s_!Hw75!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c24841b-a093-40dd-9a03-2b48fdb79e9b_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Hw75!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c24841b-a093-40dd-9a03-2b48fdb79e9b_1024x559.png)

One common mistake is to call the nine Object Calisthenics rules “principles.” They are not principles. They are strict heuristics inside a training exercise.

A principle is a stable design guideline that helps us decide between alternatives across contexts. Ideas such as encapsulation, abstraction, polymorphism, information hiding, cohesion, and coupling can be treated as design concepts, design forces, criteria, or design qualities depending on the source and the context.

Software literature does not classify these ideas consistently. Some sources group them under design principles, while others treat information hiding as a modularization criterion and cohesion and coupling as qualities of modularity. That difference in terminology does not change how the nine rules expose responsibility problems.

The vocabulary used here is:

*   A rule is a strict constraint used during the exercise.

*   A heuristic is a practical detector that helps us notice a design problem.

*   A design concept is a reusable idea that helps us think about software structure.

*   A design force is a pressure that pushes the code toward or away from a particular shape.

*   A refactoring is a behavior-preserving change to internal structure.

*   A pattern is a named design response to recurring forces.

Those distinctions protect us from dogma. Object Calisthenics does not say that every branch is bad, every getter is evil, every class must have two fields, or every string deserves a wrapper. It says that, for a short and focused exercise, we remove the usual escape routes so that hidden design problems become visible.

The rule is the flashlight. The design force is what the flashlight helps us see.

[![Image 9](https://substackcdn.com/image/fetch/$s_!pdQ3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F317f0b68-79e9-4efc-9771-2d685e7146ed_1024x559.png)](https://substackcdn.com/image/fetch/$s_!pdQ3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F317f0b68-79e9-4efc-9771-2d685e7146ed_1024x559.png)

A codebase can have classes, interfaces, constructors, methods, and inheritance while still being procedural in its heart.

This is common. A team moves from procedural code into an object-oriented language. Data is placed into classes. Functions become services. Conditionals move into managers. Getters and setters appear everywhere. The shape of the code changes, but the thinking stays the same: data lives in one place, decisions live somewhere else, and objects are mostly containers.

That style can work for simple systems, especially at boundaries. A data transfer object (DTO) is often just a data carrier. A read model may exist only to serve a screen. A persistence record may reflect database shape. There is no need to pretend those objects are rich domain models.

The problem appears when the same style invades domain behavior. An order becomes a set of fields. A shipping service asks for the order status, the address, the country, the item list, and the item weights. Then it decides whether the order can ship. The object called `Order` exists, but the responsibility called “decide whether this order can ship” lives outside it.

Object-oriented syntax is present. Object thinking is not.

Object thinking asks different questions:

*   Which object should know this?

*   Which object should decide this?

*   Which object should protect this invariant?

*   Which object should collaborate with whom?

*   Which concept is still unnamed?

*   Which behavior is living too far from the data it uses?

*   Which caller knows structure it should not know?

Object Calisthenics is valuable because each rule attacks one of the ways procedural thinking hides inside object-oriented syntax.

[![Image 10](https://substackcdn.com/image/fetch/$s_!4hVK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec3545bf-7d12-4cae-9f7e-be8ff2f01277_1024x559.png)](https://substackcdn.com/image/fetch/$s_!4hVK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec3545bf-7d12-4cae-9f7e-be8ff2f01277_1024x559.png)

Responsibility-driven design gives Object Calisthenics its deeper spine. Objects are not just small data structures. They play roles in a community. A role carries responsibilities. A responsibility is fulfilled through collaboration.

This also matches the older modularity lesson behind information hiding: a boundary is useful when it assigns responsibility and controls what knowledge crosses it. If a boundary does not reduce cognitive load, protect a decision, or make change safer, it is not doing much design work. It is mostly moving code around.

The language also comes straight out of _Responsibility-Driven Design_ (RDD). Wirfs-Brock and McKean ask designers to think in terms of candidate objects, roles, collaborators, and object neighborhoods. That is why the first-class collection rule matters more than it first appears. A collection object is not a wrapper around `List`. It is a neighbor in a small community of objects. It owns group behavior so the rest of the neighborhood does not have to know how the group is represented.

That language changes how we read the nine rules:

[![Image 11](https://substackcdn.com/image/fetch/$s_!G3Tb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b4779fe-0919-49e7-a50f-72cf2d8b9437_1658x854.png)](https://substackcdn.com/image/fetch/$s_!G3Tb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b4779fe-0919-49e7-a50f-72cf2d8b9437_1658x854.png)

Object Calisthenics is deliberate practice for responsibility placement. The goal is not prettier code, smaller code, or simply more classes. The goal is to give responsibilities better homes.

A design improves when decisions, data, invariants, and language move closer to the concept that owns them. Sometimes that concept is an entity. Sometimes it is a value object. Sometimes it is a collection. Sometimes it is a policy. Sometimes it is a domain service. Sometimes the right answer is to leave the behavior in an application service because it coordinates several things and does not naturally belong to one of them.

The corrected shipping design can be read as a small object neighborhood:

The diagram is intentionally not a database model. It shows responsibilities and collaborations, not tables. The important question is not “where is the list?” The important question is “which object should answer the group-level question?”

The exercise does not answer that for us. It gives us pressure, then asks us to think.

[![Image 12](https://substackcdn.com/image/fetch/$s_!ZQm_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fd85527-4381-4e75-b2b4-e44d5c9e1344_1024x559.png)](https://substackcdn.com/image/fetch/$s_!ZQm_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fd85527-4381-4e75-b2b4-e44d5c9e1344_1024x559.png)

The rules look simple when listed. Their real value appears when we map each rule to the design pressure it exposes.

[![Image 13](https://substackcdn.com/image/fetch/$s_!cq5-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef9ca617-8538-4367-af98-e29c6095d4df_1982x1358.png)](https://substackcdn.com/image/fetch/$s_!cq5-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef9ca617-8538-4367-af98-e29c6095d4df_1982x1358.png)

Notice the pattern. The rule is narrow, but the pressure is broad. The rule says “one dot per line.” The design question says, “Why does this object know the path through another object’s internals?” The rule says “wrap primitives.” The design question says, “What domain concept is currently being carried by an unprotected scalar value?”

The smell names are useful, but they are not verdicts. A smell is a symptom that asks for investigation. Object Calisthenics makes those symptoms harder to ignore by removing the easiest escape routes for a while.

The rule gives the hand something concrete to do. The design question gives the mind something worth understanding.

The rule asks a method to stay at one visible level of control flow. A loop containing a conditional containing another conditional forces the reader to move between the general purpose of the method and the details of one branch. That movement is the smell. The indentation is only its most visible symptom.

Why use it? It helps separate levels of abstraction. A method that coordinates an order should say that it checks readiness and lines. A different method or object should explain how a physical line decides whether its weight is valid. In the baseline service, nested `if` statements mix payment, destination, collection, and item-level details in one decision.

How do we apply it? Extract a cohesive calculation, move a rule to the object that owns it, or introduce a collaborator. The result might read like `return status.allowsShipping() && policy.accepts(destination) && lines.canBeShipped();`, with each concept responsible for its own detail.

The trade-off is method fragmentation. Extracting every two lines can make the code harder to follow and can create names that merely repeat the implementation. Use the rule when a method is making the reader change abstraction level, not as a demand that every block disappear.

The no-`else` rule makes the main path visible. Invalid or exceptional cases leave the method early, so the successful path is not buried inside a final branch. In the shipping example, an unpaid order can return `false` immediately, followed by the destination and line checks.

Why use it? Nested alternatives often grow around a central method until the method becomes a map of every possible variation. Guard clauses reduce that nesting. If the alternatives represent different kinds of object, the pressure may point toward polymorphism, as it does with physical and digital order lines.

How do we apply it? Start with the simplest guard clause:

The rule does not mean that every `else` is a defect. Some algorithms describe two equally important alternatives, and an `else` can be clearer than a series of returns. Removing it mechanically can produce awkward code or premature class hierarchies. The useful question is whether the branch clarifies a decision or hides a responsibility.

A primitive becomes suspicious when it carries rules that the type system cannot express. `"PAID"` is a string syntactically, but it is an order status semantically. `"ES"` is text syntactically, but it is a country code with normalization and format rules. `100` is a number syntactically, but it is a weight measured in grams.

Why use wrappers? A value object gives the meaning a home. `CountryCode` can normalize and validate its value. `Weight` can reject negative measurements and answer whether the weight is positive. `OrderStatus` can decide whether its state allows shipping. The service no longer repeats these rules or knows their representation.

How do we know when to wrap a value? Look for validation, units, formatting, comparison, repeated conversions, or behavior attached to the same primitive. Start with the smallest object that protects a real invariant. Do not create `StringValue` merely to satisfy a rule.

The trade-off is ceremony. A wrapper adds a type, a constructor, equality, and sometimes serialization work. For a local counter or a framework field, that cost may be unjustified. The rule pays for itself when the value crosses boundaries, appears in several decisions, or can be invalid in more than one way.

A collection stops being an implementation detail when the group has a business rule. `List<OrderLine>` is storage. `OrderLines` can answer whether the order has lines and whether every line can be shipped. `Set<CountryCode>` is storage. `SupportedCountries` can answer whether a destination is included.

Why use a collection object? Without one, loops and filters spread across services. Each caller decides what an empty collection means, which elements are valid, and whether the group is mutable. A first-class collection gives those decisions a single home and gives the group a name that can enter the domain language.

How do we apply it? Move a meaningful operation into the collection, such as `allLinesCanBeShipped`, `contains`, `totalWeight`, or `hasLines`. Keep the underlying collection private and copy incoming values when the object should be stable:

The trade-off is wrapper proliferation. A collection with no behavior becomes a renamed list and adds indirection without protecting anything. Create the object when the group has a rule, a vocabulary, or an invariant that callers would otherwise repeat.

The one-dot rule is a warning against navigating through another object’s structure. `order.getShippingAddress().getCountryCode()` tells the caller that an order contains an address and that the address exposes a country code. The caller has learned two internal relationships to make one decision.

Why use it? It limits knowledge between collaborators. A caller can ask `shippingPolicy.accepts(destination)` without knowing how a destination stores its country code. If the internal representation changes, fewer clients need to change with it.

How do we apply it? Replace structural navigation with a domain question, move the decision to the object that has the required knowledge, or introduce a collaborator that represents the relationship. In this example, `ShippingDestination.isIncludedIn(supportedCountries)` is more meaningful than exposing the country code to the service.

The trade-off is over-wrapping. A fluent API such as `query.where(...).orderBy(...).limit(...)` may be clear and intentional, even though it contains several dots. The rule is not a punctuation contest. It is a way to find knowledge leakage and train-wreck calls, then decide whether the collaboration is appropriate.

Names are part of the design. `addr`, `svc`, `cfg`, and `wgt` save a few characters while making the reader decode the vocabulary from context. In a small method that cost may seem trivial. Across a system, compressed names make boundaries and responsibilities harder to discover.

Why use the rule? Object Calisthenics treats naming as a design probe. Writing `shippingDestination` instead of `dest` may reveal that the code has several kinds of destination. Writing `orderLines` instead of `items` may reveal that the collection has order-specific behavior. A longer name can expose a missing concept.

How do we apply it? Use the clearest name that distinguishes the role: `shippingPolicy`, `countryCode`, `physicalOrderLine`, and `supportedCountries`. Keep established technical abbreviations such as `HTTP`, `URL`, and `JUnit` when they are the shared vocabulary of the domain or platform.

The trade-off is verbosity. Names can become unwieldy when they repeat context or describe implementation instead of intent. The rule is useful when the abbreviation hides a role. It is not a ban on every short name or a demand to spell out universally understood terms.

The word “entity” in this rule refers to a program entity such as a class or method, not specifically to a Domain-Driven Design entity. The rule asks whether the entity has a coherent responsibility and whether its size makes that responsibility difficult to understand.

Why use it? Large classes accumulate unrelated reasons to change. In the baseline service, shipping status, country coverage, collection traversal, and item weight all change for different business reasons. Their co-location makes the class look convenient while increasing the chance that one change disturbs another.

How do we apply it? Look for groups of methods that use different state, branches that describe different concepts, and names that belong to several vocabularies. Extract `Weight`, `OrderLines`, and `ShippingPolicy` when each object can explain a rule in its own language. Smallness should follow cohesion, not a line-count scoreboard.

The trade-off is fragmentation. A class split into ten files can be harder to understand than a coherent class of one hundred lines. Small entities help when each new boundary gives a responsibility a clear home. They hurt when the boundaries exist only to satisfy a metric.

This is the most artificial rule, and that is why it can be useful during practice. It forces us to ask whether a class is holding several concepts at once. Three fields are not automatically a design failure. The limit is a pressure applied to the design, not a theorem about object shape.

Why use it? A group of fields often points to a value object, a parameter object, or a collaborator. In the example, separating `OrderStatus` and `ShippingDestination` into `ShippingReadiness` gives those facts a shared purpose: deciding whether the order is eligible for shipping under a policy.

How do we apply it? Group fields that change together or participate in the same decision. Move behavior with the fields it needs. Then inspect the result. If the new class has a name, a coherent invariant, and useful behavior, the pressure found a real concept.

The trade-off is artificial indirection. A class can end up containing one field and a forwarding method only because the limit demanded it. That is a warning to stop. The rule has completed its job when it reveals a design question; it has not earned the right to dictate the final structure.

This rule attacks objects that expose state and leave every decision to their callers. A getter is not automatically bad. The smell appears when a caller extracts several values, makes a decision, and leaves the object as a passive record.

Why use it? Behavior placed beside the data it protects can keep invariants intact. Instead of asking an order for its status, destination, lines, and weights, then deciding in a service, the caller asks `order.canBeShippedWith(policy)`. The order and its collaborators retain control of their rules.

How do we apply it? Replace data requests that exist only to support a decision with intention-revealing operations. Replace setters with constructors or state-changing commands that preserve valid states. Keep queries when they are honest parts of the public contract, especially at read boundaries.

The trade-off is awkward integration with data transfer objects, query models, serializers, and object-relational mapping (ORM) frameworks. Those objects often exist to carry data and may need accessors. Apply the rule strongly to domain behavior, then relax it at boundaries where data exposure is the object’s actual job.

Notice the pattern. The rule is narrow, but the pressure is broad. The rule says “one dot per line.” The design question says, “Why does this object know the path through another object’s internals?” The rule says “wrap primitives.” The design question says, “What domain concept is currently being carried by an unprotected scalar value?”

The rule gives the hand something concrete to do. The design question gives the mind something worth understanding.

The article should not jump from bad code to polished code without showing what changed. The useful learning path is smell, rule, corrected object, test change, design effect.

[![Image 14](https://substackcdn.com/image/fetch/$s_!KFXV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5dc35369-1058-4431-a54b-42647dbe95a2_3497x1151.png)](https://substackcdn.com/image/fetch/$s_!KFXV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5dc35369-1058-4431-a54b-42647dbe95a2_3497x1151.png)

This table is the spine of the refactoring. The corrected design is not a random set of small classes. Each class exists because a specific smell revealed a missing responsibility.

That is the difference between extraction and design. Extracting code can make a method shorter. Moving responsibility can make the system easier to reason about. Object Calisthenics is valuable when it pushes the second, not merely the first.

The test does more than protect a business rule. It is also a client of the design. Read it as a small usability test for the object model:

The assertion is clear. It asks a meaningful domain question: can this order be shipped? The setup is more revealing. The test has to know that payment is represented by `OrderStatus.PAID`, that a country is represented by a string accepted by `CountryCode`, that a physical line needs a `Weight`, and that a policy must be assembled before the order can answer.

That knowledge is not automatically wrong. A test is allowed to construct its subject. The question is whether the construction exposes the right concepts or forces the test to understand implementation details.

The snippet gives us four design signals:

1.   `OrderStatus.PAID` is a named domain concept. It is easier to understand and safer to change than the raw string `"PAID"`.

2.   The string `"ES"` is still a boundary primitive in the test helper. The domain converts it into `CountryCode`, so the validation rule has one home.

3.   `new PhysicalOrderLine(new Weight(100))` makes the physical-line rule visible. A digital line can later implement the same role without inventing a meaningless weight.

4.   `policy()` hides repeated construction. If the policy construction remains noisy, a named factory or builder may improve the test vocabulary. That decision belongs to the construction section, not to the shipping assertion.

The test therefore helps us see the object model from the outside. A public API that reads like the business question is a good sign. A setup that requires a long tour through internal structure is a design smell worth investigating. The test does not prove that the model is good, but it makes the collaboration visible.

The examples that follow use small test-first steps and preserve the behavior after each refactoring. The subject here is the design pressure revealed by those steps, not the testing method itself.

[![Image 15](https://substackcdn.com/image/fetch/$s_!uQPP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39222cf5-61ac-4a92-9eab-947f3aadbcfc_1024x559.png)](https://substackcdn.com/image/fetch/$s_!uQPP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39222cf5-61ac-4a92-9eab-947f3aadbcfc_1024x559.png)

The baseline code represents status as a string:

This is primitive obsession. The service must know the exact representation of a paid order. If someone writes `"paid"`, `"Paid"`, or `"PAYED"`, the compiler cannot help. The string carries business meaning, but the model does not protect it.

The corrected design uses an enum because the known statuses are a closed set:

The baseline test checks status indirectly through the service:

The corrected test checks the status concept directly:

The behavior did not change. The location of the behavior changed. The rule for paid orders now lives in `OrderStatus`, where the status language lives.

[![Image 16](https://substackcdn.com/image/fetch/$s_!EN0b!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F397ab58a-d601-424d-8aa6-7b7cbd2cac85_1024x559.png)](https://substackcdn.com/image/fetch/$s_!EN0b!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F397ab58a-d601-424d-8aa6-7b7cbd2cac85_1024x559.png)

The baseline code passes country codes as strings:

That looks harmless until validation appears:

*   Is `"es"` allowed?

*   Is `"ESP"` allowed?

*   Is `null` allowed?

*   Should country codes be normalized?

If the answer lives everywhere, the codebase will eventually disagree with itself.

The corrected design introduces a value object:

`equals` must keep the `Object` parameter because this is the method defined by Java’s equality contract. Changing the signature to `equals(CountryCode)` would create an overload, not an override. Calls made through `Object`, collections, or generic code would not use that overload reliably. Java 21 pattern matching lets the method keep the correct signature without the separate cast.

The corrected tests check the value object directly. Each test has one reason to fail.

We are no longer testing country-code behavior indirectly through shipping. We test the concept where the concept lives. The shipping tests can then rely on valid country codes instead of rechecking validation every time.

[![Image 17](https://substackcdn.com/image/fetch/$s_!UtTP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0f340b9-d22c-4d50-91ea-8002f5e496c6_1024x559.png)](https://substackcdn.com/image/fetch/$s_!UtTP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0f340b9-d22c-4d50-91ea-8002f5e496c6_1024x559.png)

The baseline code exposes weight as an integer:

The service knows the unit, the representation, and the shipping rule. This is too much knowledge in one place.

The corrected design introduces `Weight`:

The corrected tests move measurement behavior into `Weight`:

This change is subtle. `Weight` knows whether it is positive. It does not know whether an order line can be shipped. That distinction matters later when digital items enter the model. A good value object protects measurement meaning, but it should not steal behavior from another concept.

[![Image 18](https://substackcdn.com/image/fetch/$s_!X6Vt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa50190aa-7d84-40a2-884e-a4e6fd1ccfb5_1024x559.png)](https://substackcdn.com/image/fetch/$s_!X6Vt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa50190aa-7d84-40a2-884e-a4e6fd1ccfb5_1024x559.png)

The baseline code has one kind of item:

The service asks the item for its weight and decides whether the item can ship. That is Tell, Don’t Ask in the wrong direction. The service asks for data, then makes the item-level decision itself.

The corrected design introduces a role:

The corrected tests ask each kind of line a domain question. There is no test that mixes physical and digital line assertions together. Each test has one reason to fail.

This is where the design begins to absorb variation. A physical line and a digital line answer the same question differently. The caller no longer needs a branch that says, “If physical, check weight; if digital, allow shipping.” The variation moved to the objects that vary.

[![Image 19](https://substackcdn.com/image/fetch/$s_!9dUP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F265d8f54-873f-4802-b8d4-f42a1bca1b1f_1024x559.png)](https://substackcdn.com/image/fetch/$s_!9dUP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F265d8f54-873f-4802-b8d4-f42a1bca1b1f_1024x559.png)

The baseline service owns collection behavior:

The service checks whether the collection is empty. It loops through the collection. It evaluates each element. The list is not passive anymore. It has behavior, but the behavior has no home.

The corrected design introduces a first-class collection:

The corrected tests ask the collection object the collection-level business question.

This is a meaningful test change. We are not testing private iteration. We are testing the collection-level business question: can this group of order lines be shipped?

[![Image 20](https://substackcdn.com/image/fetch/$s_!gGXz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4779521-1c3b-4baa-9b1d-eb0a36bdc8c5_1024x559.png)](https://substackcdn.com/image/fetch/$s_!gGXz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4779521-1c3b-4baa-9b1d-eb0a36bdc8c5_1024x559.png)

The baseline code hides shipping policy inside a service constant:

A constant starts small, but it invites growth. Carrier-specific countries, warehouse coverage, customs restrictions, shipping zones, or regional rollout rules will all compete for space inside the same service.

The corrected design gives the policy a name:

The baseline tests cover the supported countries in the service because the service owns the constant:

The corrected tests cover the same behavior in `ShippingPolicy` because the policy now owns the decision:

The `policySupportingSpainGermanyAndFrance()` helper is better than repeating the same object graph in every test, but object construction is a separate design concern from the shipping decision itself:

This is not automatically bad. A test should keep essential behavior visible. However, when several tests need the same valid policy, the cluster of constructors becomes fixture noise. The test is asking for a policy, but the reader has to parse the construction recipe before seeing the behavior.

This is where a creational pattern can help. Factory Method separates creation from use. Builder is useful when construction has several meaningful configuration steps. Both are creational patterns, but they solve different pressures. They should be discussed and tested as construction tools, not introduced as another Object Calisthenics rule.

The tests do not assert that a factory or builder calls a particular constructor. They assert that the resulting policy still accepts the destinations it is meant to accept. If creation breaks, the product-level behavior fails.

The factory gives a canonical policy a domain name. The builder makes a variable policy readable when the list of supported destinations is part of the scenario.

The factory is a good fit for the canonical Spain, Germany, and France policy because that configuration has a name. The builder is a good fit for a policy assembled from scenario-specific countries. Neither should be added merely to eliminate every `new` expression.

The tests can now use the factory for the default case and the builder for a custom case. The assertion still names the behavior. We test the creation APIs through the policy they create, which avoids coupling the test to private fields or constructor calls.

The factory and builder can be shared with production code when their construction rules are part of the domain. A test-only fixture factory is also valid when it creates named, stable examples. Do not turn every test helper into a builder. If the helper hides the only important input, inline it. If it expresses a recurring domain scenario, keep it.

This change also addresses the one-dot rule. The original service navigated from order to address to country code. The corrected model asks a policy whether it accepts a destination. The caller no longer walks through internal structure to make a decision.

[![Image 21](https://substackcdn.com/image/fetch/$s_!uxHI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc681857-29f4-4e63-80b5-4130ee54ee7b_1024x559.png)](https://substackcdn.com/image/fetch/$s_!uxHI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc681857-29f4-4e63-80b5-4130ee54ee7b_1024x559.png)

The baseline API asks a service:

The service owns the decision, so it must know everything. It knows status representation, destination representation, collection shape, item shape, and weight rule. That is the central smell.

The corrected API asks the order:

The corrected domain code is:

The corrected tests ask the order a domain question. Each negative test changes one reason at a time while keeping the rest of the setup valid.

The helper accepts a raw `String countryCode` only at the test boundary to keep examples readable. The domain model does not receive a raw country string. The helper immediately converts it into `CountryCode`.

This is a useful distinction. Object Calisthenics is not asking us to make every test painful. It is asking us to stop letting unprotected primitives travel through the domain.

[![Image 22](https://substackcdn.com/image/fetch/$s_!89f9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff262712b-15d9-4cb2-88e1-36fa7217ed5b_1024x559.png)](https://substackcdn.com/image/fetch/$s_!89f9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff262712b-15d9-4cb2-88e1-36fa7217ed5b_1024x559.png)

The business expectations remain stable for the original rule set:

[![Image 23](https://substackcdn.com/image/fetch/$s_!N58m!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70a83974-1ff0-48d5-9764-360ac7349f4f_3528x1311.png)](https://substackcdn.com/image/fetch/$s_!N58m!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70a83974-1ff0-48d5-9764-360ac7349f4f_3528x1311.png)

That last row is important. The behavior does change in one deliberate way. In the baseline, a negative weight can be constructed and is rejected later by `ShippingServiceBefore`. In the corrected model, negative weight is rejected at construction by `Weight`. The system fails earlier, closer to the invalid value.

The structure of the tests changes because the design changes:

![Image 24](https://substackcdn.com/image/fetch/$s_!qk45!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff556ef1e-50a4-40db-8c60-2c290569cb47_3511x782.png)

The old API accepts raw data and centralizes the decision in a service. The new API builds domain concepts and asks the order a domain question.

The syntax changed, but the important change is the collaboration model.

The class structure now makes the ownership change visible:

The diagram is larger than the baseline, but the knowledge is less centralized. `Order` asks `ShippingReadiness` and `OrderLines` questions. `OrderLines` asks each line. Physical and digital lines vary behind the same role. `CountryCode` and `Weight` keep invalid values from leaking into the rest of the design.

[![Image 25](https://substackcdn.com/image/fetch/$s_!Q_Ck!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39717fd0-07e0-461c-b7ab-071eca79642f_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Q_Ck!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39717fd0-07e0-461c-b7ab-071eca79642f_1024x559.png)

The first business rule said every item must have positive weight. That seems fine until the business adds a new rule:

Digital items can be shipped without weight.

This requirement is important because it tests the design. If we had placed shipping behavior inside `Weight`, we would have a problem. Weight can know whether it is positive. It should not know whether an item can be shipped. A digital item may not have weight at all. A physical item needs positive weight. A hazardous item may need additional checks. A subscription item may need no shipping.

The corrected design places the variation in `OrderLine`.

The tests are complete and separated by reason:

This is where Object Calisthenics becomes more than wrapping primitives. It asks us to put behavior in the right place, not merely in the nearest small class.

When the next product type arrives, its shipping behavior can be added beside the existing line types instead of inside a central order policy.

[![Image 26](https://substackcdn.com/image/fetch/$s_!SaA3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56f5ead2-edb4-4603-b90a-d8ca21b68ffb_1024x559.png)](https://substackcdn.com/image/fetch/$s_!SaA3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56f5ead2-edb4-4603-b90a-d8ca21b68ffb_1024x559.png)

The resulting model keeps status, destination, weight, line behavior, collection behavior, and shipping policy in named concepts.

This is where Object Calisthenics becomes more than wrapping primitives. It asks us to put behavior in the right place, not merely in the nearest small class.

When the next product type arrives, its shipping behavior can be added beside the existing line types instead of inside a central order policy.

[![Image 27](https://substackcdn.com/image/fetch/$s_!Uw6C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa712c254-7239-4a53-b3f5-6db701065372_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Uw6C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa712c254-7239-4a53-b3f5-6db701065372_1024x559.png)

The following tests are complete. They avoid multiple unrelated assertions in one test.

The tests teach the API of the design. The baseline tests ask a service to inspect an object. The corrected tests ask concepts to answer meaningful questions.

That is the shift from procedural object syntax to object thinking.

The refactoring is not successful because it creates more files. It is successful only if the direction of knowledge changes. The baseline service reaches through the order, while the corrected order collaborates with concepts that own status, destination, policy, lines, and line-level shipping behavior.

The arrows are collaborations, not ownership claims. The diagram deliberately omits constructors and persistence details. Its purpose is to show which object is asked a domain question and which object is forced to know the internal path to the answer.

[![Image 28](https://substackcdn.com/image/fetch/$s_!frkq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25e2ba08-9001-4b6d-a2a7-c0dae261ed36_1024x559.png)](https://substackcdn.com/image/fetch/$s_!frkq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25e2ba08-9001-4b6d-a2a7-c0dae261ed36_1024x559.png)

The nine rules are easier to understand as a system of pressures than as a list of commandments.

The rules are not separate tricks. They are coordinated discomfort.

[![Image 29](https://substackcdn.com/image/fetch/$s_!AuSe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F455cc412-9da4-4548-bcb6-03c872c1cdac_1024x559.png)](https://substackcdn.com/image/fetch/$s_!AuSe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F455cc412-9da4-4548-bcb6-03c872c1cdac_1024x559.png)

Bay warned that the rules can contradict one another or lead to poor results when applied mechanically. That warning should not be softened. It should be central.

Consider the `Order` example. Moving behavior into objects reduced getter usage and knowledge leakage. Wrapping values improved domain language. First-class collections gave line behavior a home. But satisfying the two-instance-variable rule pushed us toward `ShippingReadiness`.

That may be good. It may also be artificial. The rule created a design question. It did not answer it.

The same tension appears elsewhere:

*   If we remove every `else`, we may create polymorphism too early.

*   If we wrap every primitive, we may create dozens of empty objects with no behavior.

*   If we reduce every class to two fields, we may introduce wrapper objects that exist only because the rule demanded them.

*   If we remove every getter, we may make presentation code awkward or hide useful queries behind confusing commands.

*   If we enforce one dot per line mechanically, we may reject fluent APIs that are clear and intentional.

A training constraint can overfit the training environment. In the gym, strict tempo teaches control. In a game, moving with that same artificial tempo may be absurd. The point of the drill is to change perception, not to freeze movement forever.

Object Calisthenics works best when we treat rule conflict as a learning event.

Ask:

*   What pressure is this rule exposing?

*   Is that pressure meaningful in this part of the system?

*   Does the refactoring introduce a real concept?

*   Does the new object own behavior, invariants, or language?

*   Is the design easier to change after the move?

*   Are we reducing coupling, or only hiding it?

*   Are we increasing cohesion, or only splitting files?

When two rules fight, the winner should be design clarity, not rule compliance.

[![Image 30](https://substackcdn.com/image/fetch/$s_!pwGt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe24c1c0-c161-4154-b04f-5c0345f12893_1024x559.png)](https://substackcdn.com/image/fetch/$s_!pwGt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe24c1c0-c161-4154-b04f-5c0345f12893_1024x559.png)

Object Calisthenics is easy to fake. The code can satisfy the visible rule while missing the design lesson.

[![Image 31](https://substackcdn.com/image/fetch/$s_!mrF1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F059aca47-9f35-4cb9-9e07-5b0fc256eecc_3518x1407.png)](https://substackcdn.com/image/fetch/$s_!mrF1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F059aca47-9f35-4cb9-9e07-5b0fc256eecc_3518x1407.png)

The most dangerous form of fake compliance is theatre. Primitive-wrapper theatre. Polymorphism theatre. Encapsulation theatre. Dot-count theatre. The code looks more object-oriented, but the responsibility placement is not better.

A useful test is this: would the new object make sense to a domain expert, a maintainer, or a future developer reading the code six months from now?

If the answer is no, the object may be a gym scar rather than a stronger muscle.

[![Image 32](https://substackcdn.com/image/fetch/$s_!obSs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64c239a4-804d-4b40-bf54-c5ed6b66f6dd_1024x559.png)](https://substackcdn.com/image/fetch/$s_!obSs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64c239a4-804d-4b40-bf54-c5ed6b66f6dd_1024x559.png)

Object Calisthenics helps when a team is trying to learn object-oriented design through practice rather than slogans.

It is useful in katas because a kata is a safe place to exaggerate. The team can write code naturally first, then repeat the exercise under the nine constraints and compare the designs. The comparison is often more valuable than the final code.

It is useful in pair programming and mob programming because constraints make design feedback concrete. Instead of saying “this feels wrong,” someone can say, “The one-dot rule hurts here. What knowledge is leaking?” That language keeps the conversation focused on the code, not on the person who wrote it.

It is useful in refactoring workshops because the rules give people a place to start. A large method can be intimidating. “Use one level of indentation” is a manageable first move. After the method is flatter, the deeper responsibility questions become easier to see.

It is useful in domain-heavy code because domain concepts often hide behind primitives, strings, maps, and lists. The exercise pushes those concepts into named objects with behavior and invariants.

It is useful when procedural habits have invaded object-oriented syntax. Classes that expose data, services that make every decision, and domain objects with no agency are exactly the kind of code this exercise exposes.

It is also useful for teaching because it turns abstract design ideas into embodied experience. Encapsulation stops being a definition in a book. It becomes the discomfort of trying to remove a getter. Cohesion stops being a vague virtue. It becomes the discomfort of trying to keep an entity small. Coupling stops being a diagram. It becomes the discomfort of a dot chain that knows too much.

[![Image 33](https://substackcdn.com/image/fetch/$s_!bSWp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ecb355e-4753-421b-b82e-0436e4feac96_1024x559.png)](https://substackcdn.com/image/fetch/$s_!bSWp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ecb355e-4753-421b-b82e-0436e4feac96_1024x559.png)

Object Calisthenics hurts when a team treats it as production law.

It is weak around boundary objects. DTOs, API payloads, persistence records, read models, and serialization objects often exist to carry data across a boundary. Their job is not always to model rich behavior. Forcing every boundary object into the same style as domain logic can create ceremony without benefit.

It is weak around generated code. Generated clients, database models, or protocol classes are shaped by tools and external contracts. Human design pressure is not the main force there.

It is weak around some framework adapters. An ORM may require certain constructors or properties. A web framework may expect request models. A serializer may require accessible fields. A strict rule can fight the tool instead of improving the design.

It can hurt performance-sensitive low-level code. Extra objects, indirection, allocation, and dispatch may matter in some contexts. Most business systems are not dominated by that concern, but when the concern is real, it should be respected.

It can also hurt simple scripts. A small one-off migration may not need a rich object model. The cost of abstraction can exceed the value.

A practical boundary looks like this:

[![Image 34](https://substackcdn.com/image/fetch/$s_!KW69!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66b1e54d-8bc3-45e5-baa0-ca850a0812f6_3515x1292.png)](https://substackcdn.com/image/fetch/$s_!KW69!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66b1e54d-8bc3-45e5-baa0-ca850a0812f6_3515x1292.png)

The same code shape can mean different things in different layers. A public property in a DTO may be boring and correct. A public property in a domain object may be a design leak.

Context is not an excuse to avoid thinking. Context is what thinking is for.

[![Image 35](https://substackcdn.com/image/fetch/$s_!M1Ks!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fb4d200-00b8-4792-9c3d-f159f42899ad_1024x559.png)](https://substackcdn.com/image/fetch/$s_!M1Ks!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fb4d200-00b8-4792-9c3d-f159f42899ad_1024x559.png)

Object Calisthenics often leads to refactoring, and refactoring should be protected by feedback.

Fowler defines refactoring as changing internal structure without changing observable behavior. That matters because Object Calisthenics can tempt us into large rewrites. Moving behavior, introducing value objects, wrapping collections, and replacing conditionals with polymorphism are all structural changes. Without tests, we are guessing.

If the code already exists, start with characterization tests. Capture the current behavior before trying to improve the design. This is especially important when the code has hidden edge cases, legacy behavior, or business rules nobody fully remembers.

If you are adding new behavior, _Test-Driven Development_ (_TDD_) can help the design grow in smaller steps. The connection fits Object Calisthenics well because both practices reward short feedback loops.

A safe sequence looks like this:

1.   Pick a small piece of code.

2.   Write tests around the current behavior or the next behavior.

3.   Apply one rule or one group of related rules.

4.   Make the smallest behavior-preserving refactoring.

5.   Run the tests.

6.   Commit.

7.   Repeat.

For the shipping example, a safe path could be:

1.   Characterize `ShippingServiceBefore.canShip`.

2.   Introduce `OrderStatus` and move the paid rule.

3.   Introduce `CountryCode` and `ShippingDestination`.

4.   Introduce `Weight` without putting item shipping policy inside weight.

5.   Introduce `OrderLine` variants for physical and digital lines.

6.   Introduce `OrderLines` as a first-class collection.

7.   Introduce `SupportedCountries` and `ShippingPolicy`.

8.   Move the shipping decision into `Order`.

9.   Revisit field count and cohesion.

10.   Stop when the design is clearer.

The last step is not a compromise. It is professionalism. Stop when the design is clearer, not when the scoreboard says the rules are satisfied.

[![Image 36](https://substackcdn.com/image/fetch/$s_!Ip7N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10764acb-a443-4c06-b2c0-6a381e0ddad3_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Ip7N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10764acb-a443-4c06-b2c0-6a381e0ddad3_1024x559.png)

A team can learn Object Calisthenics without turning it into a coding standard.

Use a small exercise. The theatrical statement example from refactoring literature works well. A shopping cart works. A shipping decision works. A booking system works. The domain should be small enough to understand in minutes and rich enough to contain decisions, values, collections, and formatting.

Run the exercise in rounds:

1.   Write the code naturally.

2.   Write characterization tests.

3.   Apply the rules to move responsibilities into better homes.

4.   Compare the designs after each meaningful movement.

5.   Add a small requirement change.

6.   Observe whether the design absorbs the change or asks for another central branch.

7.   Discuss where the rules helped and where they became noisy.

The important thing is not strict obedience in production. The important thing is shared language.

Useful questions:

*   Which rule revealed the most useful pressure?

*   Which rule created the most noise?

*   Which new object had real behavior?

*   Which new object was only ceremony?

*   Which branch represented true variation?

*   Which getter exposed stolen behavior?

*   Which rule would we apply to our production domain code?

*   Which rule would we relax at boundaries?

*   Which code became easier to test?

*   Which code became harder to understand?

Do not end the workshop with “from now on, all code follows Object Calisthenics.” That turns learning into bureaucracy. End with a shared language of design pressure.

The outcome is a shared vocabulary for precise design conversations: this primitive is hiding a concept, this service is stealing behavior, this dot chain leaks knowledge, or this class is large because it has more than one role.

[![Image 37](https://substackcdn.com/image/fetch/$s_!BmvP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6997dc0e-727f-467f-b541-670dde691a65_1024x559.png)](https://substackcdn.com/image/fetch/$s_!BmvP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6997dc0e-727f-467f-b541-670dde691a65_1024x559.png)

Object Calisthenics teaches through discomfort:

*   The indentation rule makes mixed abstraction uncomfortable.

*   The no-`else` rule makes branch-heavy decisions uncomfortable.

*   The primitive rule makes unnamed values uncomfortable.

*   The collection rule makes scattered group behavior uncomfortable.

*   The dot rule makes leaked knowledge uncomfortable.

*   The naming rule makes vague language uncomfortable.

*   The size rule makes weak cohesion uncomfortable.

*   The field-count rule makes data clumps uncomfortable.

*   The accessor rule makes stolen behavior uncomfortable.

That discomfort is not a failure. It is the point. A good exercise does not flatter us. It reveals the compensation pattern.

The first time we try the rules, the code may feel worse before it feels better. That is normal. A body learning a new movement shakes because it can no longer rely on its old shortcuts. Code does the same. The easy branch, the naked string, the public getter, the central service, the long method, and the exposed collection were all shortcuts. Some were harmless. Some were expensive. The exercise helps us tell the difference.

The final skill is not following Object Calisthenics. The final skill is seeing design pressure early.

[![Image 38](https://substackcdn.com/image/fetch/$s_!_8pi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f34f775-8e18-43eb-9b19-11aad9748762_1024x559.png)](https://substackcdn.com/image/fetch/$s_!_8pi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f34f775-8e18-43eb-9b19-11aad9748762_1024x559.png)

Object Calisthenics is often presented as nine rules for better code. That framing is too small.

It is better understood as deliberate practice for object thinking. Its nine rules add artificial weight to ordinary code so that poor responsibility placement becomes visible. They expose procedural habits that survive inside object-oriented syntax. They reveal where behavior is too far from data, where concepts are unnamed, where collections are treated as passive containers, where callers know too much, and where objects have become bags of state.

The rules are strict during practice because practice needs resistance. They should become guidelines afterward because production needs judgment. Bay’s own framing allows that nuance, and the best use of Object Calisthenics depends on keeping it.

A mature developer does not ask, “Does this code obey all nine rules?”

A mature developer asks better questions:

*   What responsibility is misplaced here?

*   Which concept is hiding behind this primitive?

*   Which collection has behavior but no name?

*   Which branch is really a domain variation?

*   Which object is being interrogated instead of trusted?

*   Which name is too compressed to carry meaning?

*   Which class is large because the concept is rich, and which class is large because the design is confused?

*   Which getter is useful information sharing, and which getter is a door through which behavior escaped?

The exercise will not design the system for us. It will not remove the need for trade-offs. It will not make context disappear. It will not turn every production object into a tiny perfect model.

It does something more useful.

It teaches us where to look. Once we can see the pressure, we can choose the next move with intent.

*   Iglesias, Fran. _Solo un nivel de indentación_. [https://franiglesias.github.io/calisthenics-1/](https://franiglesias.github.io/calisthenics-1/)

*   Iglesias, Fran. _No usar la palabra clave ELSE_. [https://franiglesias.github.io/calisthenics-2/](https://franiglesias.github.io/calisthenics-2/)

*   Iglesias, Fran. _Object Calisthenics: Empaquetar primitivas en objetos_. [https://franiglesias.github.io/calisthenics-3/](https://franiglesias.github.io/calisthenics-3/)

*   Iglesias, Fran. _Object Calisthenics: Colecciones de primera clase_. [https://franiglesias.github.io/calisthenics-4/](https://franiglesias.github.io/calisthenics-4/)

*   Iglesias, Fran. _Object Calisthenics: Un punto por línea_. [https://franiglesias.github.io/calisthenics-5/](https://franiglesias.github.io/calisthenics-5/)

*   Iglesias, Fran. _Object Calisthenics: No usar abreviaturas_. [https://franiglesias.github.io/calisthenics-6/](https://franiglesias.github.io/calisthenics-6/)

*   Iglesias, Fran. _Object Calisthenics: Mantener todas las entidades pequeñas_. [https://franiglesias.github.io/calisthenics-7/](https://franiglesias.github.io/calisthenics-7/)

*   Iglesias, Fran. _Object Calisthenics: No más de dos variables de instancia por clase_. [https://franiglesias.github.io/calisthenics-8/](https://franiglesias.github.io/calisthenics-8/)

*   Iglesias, Fran. _Object Calisthenics: No usar getters, setters o propiedades públicas_. [https://franiglesias.github.io/calisthenics-9/](https://franiglesias.github.io/calisthenics-9/)

*   Iglesias, Fran. _Object Calisthenics: Comentarios finales_. [https://franiglesias.github.io/calisthenics-10/](https://franiglesias.github.io/calisthenics-10/)

*   Kofler, Peter. _Compliance with Object Calisthenics_. [https://blog.code-cop.org/2018/01/compliance-with-object-calisthenics.html](https://blog.code-cop.org/2018/01/compliance-with-object-calisthenics.html)

*   Lieberherr, Karl. _Law of Demeter: Principle of Least Knowledge_. [https://www.khoury.northeastern.edu/home/lieber/LoD.html](https://www.khoury.northeastern.edu/home/lieber/LoD.html)

*   Parnas, David Lorge. _On the Criteria To Be Used in Decomposing Systems into Modules_. [https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf](https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf)

*   Snyder, Alan. _Encapsulation and Inheritance in Object-Oriented Programming Languages_. [https://www.cs.tufts.edu/comp/150CBD/readings/snyder86encapsulation.pdf](https://www.cs.tufts.edu/comp/150CBD/readings/snyder86encapsulation.pdf)

*   Stakater. _Object Calisthenics_. [https://developerhandbook.stakater.com/architecture/object-calisthenics.html](https://developerhandbook.stakater.com/architecture/object-calisthenics.html)

*   Wirfs-Brock, Rebecca, McKean, Alan. _Object Design: Roles, Responsibilities, and Collaborations_. [https://www.oreilly.com/library/view/object-design-roles/0201379430/](https://www.oreilly.com/library/view/object-design-roles/0201379430/)

*   Bay, Jeff. _Object Calisthenics, in The ThoughtWorks Anthology_. [https://media.pragprog.com/titles/twa/toc.pdf](https://media.pragprog.com/titles/twa/toc.pdf)

*   Bay, Jeff. _Object Calisthenics: 9 Steps to Better Software Design Today_. [https://www.bennadel.com/resources/uploads/2012/objectcalisthenics.pdf](https://www.bennadel.com/resources/uploads/2012/objectcalisthenics.pdf)

*   Bourque, Pierre, Fairley, Richard E. _Guide to the Software Engineering Body of Knowledge_. [https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4](https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4)

*   Evans, Eric. _Domain-Driven Design Reference_. [https://www.domainlanguage.com/ddd/reference/](https://www.domainlanguage.com/ddd/reference/)

*   Fowler, Martin. _Evans Classification_. [https://martinfowler.com/bliki/EvansClassification.html](https://martinfowler.com/bliki/EvansClassification.html)

*   Fowler, Martin. _Refactoring_. [https://refactoring.com/](https://refactoring.com/)

*   Fowler, Martin. _Tell Dont Ask_. [https://martinfowler.com/bliki/TellDontAsk.html](https://martinfowler.com/bliki/TellDontAsk.html)

*   Fowler, Martin. _Object Mother_. [https://martinfowler.com/bliki/ObjectMother.html](https://martinfowler.com/bliki/ObjectMother.html)

*   Freeman, Steve, Pryce, Nat. _Growing Object-Oriented Software, Guided by Tests_. [https://www.oreilly.com/library/view/growing-object-oriented-software/9780321574442/](https://www.oreilly.com/library/view/growing-object-oriented-software/9780321574442/)

*   Gamma, Erich, Helm, Richard, Johnson, Ralph, Vlissides, John. _Design Patterns: Elements of Reusable Object-Oriented Software_. [https://www.pearson.com/en-us/subject-catalog/p/design-patterns-elements-of-reusable-object-oriented-software/P200000009480/9780201633610](https://www.pearson.com/en-us/subject-catalog/p/design-patterns-elements-of-reusable-object-oriented-software/P200000009480/9780201633610)
