---
title: "Outside-in: techniques Pivote and Drill-down"
requested_url: "https://emmanuelvalverderamos.substack.com/p/outside-in-technics-pivote-and-drill"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/outside-in-technics-pivote-and-drill"
substack_post_id: 168238656
retrieved_at: "2026-03-10T08:35:47.814Z"
---
# Outside-in: techniques Pivote and Drill-down

## Recommended readings before starting to read this article.


Let's imagine we're working on an API. We've started with the controller and moved to the next level: a use case that will need multiple dependencies. For this example, we'll call these external dependencies that will perform different tasks "services". If we want to use Outside-in, there are two ways to work downward: the concept of pivoting and the concept of drill-down.

> ⚠️ The test start from outside, from the controller, but the examples make sence at the use case level, I’m also not trying to encourage to use services after the use cases is just an example.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### Pivote

Sometimes our SUT needs multiple dependencies, but obviously, we won't implement each one of them. The common approach is to design the public API of our dependencies or collaborator classes without implementing them, pivoting between these dependencies or collaborators while we design them.

[![](https://substackcdn.com/image/fetch/$s_!f5Ud!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf169521-a249-4a3a-886b-c00eb88ecfbc_9018x3547.png)](https://substackcdn.com/image/fetch/$s_!f5Ud!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf169521-a249-4a3a-886b-c00eb88ecfbc_9018x3547.png)

**How it plays out:** you sketch the contracts of collaborator A and collaborator B, then you bounce between them as your test points out the next gap. You keep tests focused on the behavior of the use case while collaborators are represented by test doubles.

**Strengths:** This is the most common Outside-in path because it helps you discover collaborators gradually and design the communication between classes in small steps. It keeps you close to your use case’s behavior and helps you evolve the public APIs of the collaborators as you learn.

**Weak spot to watch:** if you are not yet comfortable [distinguishing peers](https://emmanuelvalverderamos.substack.com/p/in-depth-view-to-peers-internals) from internals, you can slide into [solitary tests](https://emmanuelvalverderamos.substack.com/p/explaining-unit-tests-solitarysociable?utm_source=publication-search), because you replace everything with doubles. Sometimes those collaborators do not need doubles, because they are internals, [not peers](https://emmanuelvalverderamos.substack.com/p/in-depth-view-to-peers-internals).

**Refactor move: materialization.** During the refactor phase, when a collaborator is internal and simple, consider swapping the double for the real implementation. I call this materialization: you replace the test double in your test with the real class implementation. Good candidates are collaborators who have no unusual or costly dependencies, for example, no database or remote API calls, and who do not violate FIRST. This reduces indirection, removes unnecessary test doubles, and keeps the design honest.

### Drill-down

Sometimes we'll want to design an entire dependency to reduce uncertainty or meet other needs. In these cases, we'll first design the public API of our collaborator class or dependency, make our test pass, and then immediately begin doing TDD downward by moving the test subject down and gradually implementing that entire branch. Since words alone can be complex to understand, I've created some images to help illustrate this concept.

[![](https://substackcdn.com/image/fetch/$s_!umKE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64a1c686-dd78-4d89-ad46-441964c87446_9415x3539.png)](https://substackcdn.com/image/fetch/$s_!umKE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64a1c686-dd78-4d89-ad46-441964c87446_9415x3539.png)

**Trade-off:** this path is less common. Because you have not yet identified all collaborators, you might need to adjust several of them during refactor, and sometimes even while red, if the initial contract you sketched turns out to be implausible. The benefit is clarity. When you are unsure about a collaborator’s contract, drilling down forces you to work through a realistic implementation and discover what that contract should be.

**Strengths**

- **Risk reduction**: drilling down validates the interface bet early, before you couple more tests to a design that may not hold.
- **YAGNI friendly**: by implementing a thin vertical slice, you avoid speculative doubles and scaffolding you might not need.
- **Faster value**: you get closer to a passing end-to-end check with an integrated slice, which can help you deliver a small increment sooner.
- **Clearer boundaries**: real behavior exposes invariants, data shapes, and failure modes, which improves naming and helps you decide whether a collaborator is a peer that deserves a double or an internal you can materialize.

**Weaknesses**

- **Possible rework**: as other collaborators emerge, your first contract might need changes. That can ripple through tests.
- **Focus shift**: going deeper can slow breadth discovery at the current layer, and you may switch contexts more often.
- **Premature detail**: you might over-invest in internals that later change.
- **Feedback drag**: if you build deep stacks of tests, cycles can slow unless you keep the vertical slice very thin.

## How this maps to breadth-first and depth-first

Your Pivot and Drill-down line up with Lasse Koskela’s “**breadth-first**” and “**depth-first**” test-driving lenses.

- Breadth-first, in Koskela’s words, means **“writing tests against the public interface … making them pass by faking the internals”**.
- Depth-first means **“traverse functionality depth-first and implement the details first for one small vertical slice”**.

Koskela presents these choices in Chapter 2, section 2.3, as two ways to proceed when a higher-level test exposes lower-level complexity, and he shows how you can either fake details for a while or go implement them now.

He returns to this in Chapter 4 when discussing test-selection strategies: **details first vs big picture first**, and **exploring the uncertain vs sticking with the familiar**. These frames connect directly to risk and learning, which is the heart of your argument about drill-down reducing risk and being YAGNI friendly.

### When to choose which

- **High risk or novelty:** prefer Drill-down. You reduce uncertainty sooner and validate the interface before coupling more tests to it.
- **Low uncertainty and you want flow:** prefer Pivot. You keep momentum by shaping collaborator APIs at the current layer, then fill in details later.

## Beyond Outside-in: choosing the next test

You can apply the same lenses when picking the next test in any context, not only Outside-in. You can continue on the same axis of change until you finish it (**depth-first**), or you can explore a new axis to learn a bit more about the problem and come back later to finish the earlier one (**breadth-first**). Koskela encourages working from a test list and using these heuristics to select the next step.

## Conclusions

There is no single right moment to pivot or to drill down. What matters is understanding the trade-offs and choosing the technique that fits your context. If the contracts are fuzzy, drill down to learn. If the behavior is clear and you need breadth, pivot to discover collaborators and shape their APIs. During refactor, materialize internal and simple collaborators, keep doubles for peers and costly boundaries, and let your tests describe behavior rather than structure.

This post draws on hands-on experience. For the breadth-first and depth-first mapping, see the references below.

## References

This post is based on my own experience and this books.

- Lasse Koskela, *Test-Driven: Practical TDD and Acceptance TDD for Java Developers*, Manning, 2007. Chapter 2, section 2.3 “Breadth-first, depth-first”, and Chapter 4, section 4.1.1 “Test-selection strategies”.
- Steve Freeman and Nat Pryce, *Growing Object-Oriented Software, Guided by Tests*, Addison-Wesley, 2010. (For Outside-in and peer discovery techniques mentioned at the top.)

### Acknowledgement

Thanks to [Ángel Siendones Sillero](https://www.linkedin.com/in/angel-siendones-sillero/) and my colleagues from the [Ensemble Podcasting](https://open.spotify.com/show/0sa3ACEoxLMy5NH7sisXVD?si=a90024e6810743de), for creating the term “**Materialization**“ for the concept of replacing test doubles for the real implementations.

I’ve updated the content thanks to Manuel Riveros’ comments:

[https://emmanuelvalverderamos.substack.com/p/outside-in-technics-pivote-and-drill/comment/161423263](https://emmanuelvalverderamos.substack.com/p/outside-in-technics-pivote-and-drill/comment/161423263)
