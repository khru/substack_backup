---
title: "In depth view to Peers, Internals collaborators"
requested_url: "https://emmanuelvalverderamos.substack.com/p/in-depth-view-to-peers-internals"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/in-depth-view-to-peers-internals"
substack_post_id: 164573136
retrieved_at: "2026-03-15T08:31:19.797Z"
---
# In depth view to Peers, Internals collaborators

## Introduction

[![Growing Object-Oriented Software, Guided by Tests (The Addison-Wesley  Signature Series) : Freeman, Steve, Pryce, Nat: Amazon.de: Books](https://substackcdn.com/image/fetch/$s_!-HwH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a0d68c7-ce2c-4b7f-b8a0-e109a3d7889e_1938x2560.jpeg)](https://substackcdn.com/image/fetch/$s_!-HwH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a0d68c7-ce2c-4b7f-b8a0-e109a3d7889e_1938x2560.jpeg)

Test-Driven Development (TDD) isn’t just about writing tests first. In *Growing Object-Oriented Software, Guided by Tests* (GOOS), Steve Freeman and Nat Pryce present a way to grow software incrementally with tests that **drive the design**. Their approach is grounded in object-oriented design, focusing not only on correctness but on creating **collaborative, decoupled systems** that are easy to understand, maintain, and evolve.

A central idea in GOOS is: We use test doubles only for the peers of the object under test, never for its internals.

**> “We grow the system from the outside in, starting with the behaviour we want and discovering the design as we go.”**

Understanding what constitutes a "peer" vs an "internal" is critical if you want to write meaningful tests and create systems that are resilient to change. This article delves into these ideas in depth, providing examples, direct quotes from the book, and practical techniques to apply in your code.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## What Is a Peer?

A **peer** is an **external collaborator** that your object uses to fulfill part of its responsibilities. You communicate with peers via a **public interface**, and you can substitute them with test doubles to validate the interaction.

Peers are:

- Independent objects.
- Connected by clear contracts.
- Often injected via a constructor or an interface.

### Real-world Peer Examples

- A `PaymentGateway` that charges customers.
- A `Repository` that stores entities.
- A `Clock` that provides the current time.
- A `Mailer` that sends notifications.

---

## What Is an Internal?

An **internal** is an object or function that exists **only to help fulfill the behavior** of the object under test. Internals do not participate in cross-object collaboration and **should never be replaced with a test double**.

Freeman and Pryce emphasize: Mocking an internal implementation detail... couples the test to the structure of the class, rather than its externally visible behavior.

Internals are:

- Implementation details.
- Often private or encapsulated.
- Replaceable through refactoring.

---

## The Rule: Mock Peers, Not Internals

Only replace collaborators with test doubles when those collaborators are peers.

When you mock an internal:

- You couple the test with implementation details.
- You block refactoring.
- You lose confidence in test reliability.

When you mock a peer:

- You test real **interactions** between units.
- You focus on **collaboration**, not internal steps.

---

## Worked Example: Order Processing System

### The Domain

```
data class Order(val productId: String, val quantity: Int, val userId: String)
```

### The Peers

```
interface Inventory {
    fun isAvailable(productId: String, quantity: Int): Boolean
    fun reserve(productId: String, quantity: Int)
}

interface PaymentGateway {
    fun charge(userId: String, amount: Double)
}

interface OrderRepository {
    fun save(order: Order)
}
```

### The Internal

```
private class PriceCalculator {
    fun totalFor(productId: String, qty: Int): Double = when (productId) {
        "book"   -&gt; 10.0  * qty
        "laptop" -&gt; 800.0 * qty
        else     -&gt; throw IllegalArgumentException("Unknown product $productId")
    }
}
```

### The Subject Under Test

```
class OrderProcessor(
    private val inventory: Inventory,
    private val paymentGateway: PaymentGateway,
    private val orderRepository: OrderRepository,
    private val priceCalculator: PriceCalculator
) {
    fun process(order: Order): Boolean {
        if (!inventory.isAvailable(order.productId, order.quantity)) return false
        val total = priceCalculator.calculate(order.productId, order.quantity)
        inventory.reserve(order.productId, order.quantity)
        paymentGateway.charge(order.userId, total)
        orderRepository.save(order)
        return true
    }
}
```

## Final Summary

Use test doubles when needed and design your code, understanding the types of classes you need to create and their corresponding responsibilities.

Related post.


Thanks to [Manuel Rivero](https://www.linkedin.com/in/manuel-rivero-54411271/) and also [Codesai](https://codesai.com/) for writing about this topic.

- *Rivero, Manuel*. **Heuristics to determine unit boundaries: object peer stereotypes, detecting effects and FIRS-ness. **[https://codesai.com/posts/2025/07/heuristics-to-determine-unit-boundaries](https://codesai.com/posts/2025/07/heuristics-to-determine-unit-boundaries).
- *Rivero, Manuel*. **"Isolated" test means something very different to different people!. **[https://codesai.com/posts/2025/06/isolated-test-something-different-to-different-people](https://codesai.com/posts/2025/06/isolated-test-something-different-to-different-people)
- *Rivero, Manuel*. **The class is not the unit in the London school style of TDD. **[https://codesai.com/posts/2025/03/mockist-tdd-unit-not-the-class](https://codesai.com/posts/2025/03/mockist-tdd-unit-not-the-class)
- *Rivero, Manuel*. **Breaking out to improve cohesion (peer detection techniques) **[https://codesai.com/posts/2025/11/breaking-out-to-improve-cohesion](https://codesai.com/posts/2025/11/breaking-out-to-improve-cohesion)
