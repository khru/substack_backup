---
title: "Discovering Peers with GOOS Techniques"
subtitle: "Breaking Out, Budding Off, and Bundling Up"
requested_url: "https://emmanuelvalverderamos.substack.com/p/discovering-peers-with-goos-techniques"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/discovering-peers-with-goos-techniques"
substack_post_id: 168237147
retrieved_at: "2026-03-05T08:35:44.627Z"
---
# Discovering Peers with GOOS Techniques

### Breaking Out, Budding Off, and Bundling Up

GOOS outlines three practical techniques to help identify and extract peers from your objects during the design process: **Breaking Out**, **Budding Off**, and **Bundling Up**.

[![Growing Object-Oriented Software, Guided by Tests (The Addison-Wesley  Signature Series) : Freeman, Steve, Pryce, Nat: Amazon.de: Books](https://substackcdn.com/image/fetch/$s_!M2vI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61edf1c7-38ea-4db4-bd36-4123bab52ad9_1938x2560.jpeg)](https://substackcdn.com/image/fetch/$s_!M2vI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61edf1c7-38ea-4db4-bd36-4123bab52ad9_1938x2560.jpeg)

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

[![](https://substackcdn.com/image/fetch/$s_!9qwX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10936fc9-8fc1-48ab-a7cb-c340396a1e23_1024x559.png)](https://substackcdn.com/image/fetch/$s_!9qwX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10936fc9-8fc1-48ab-a7cb-c340396a1e23_1024x559.png)

### 1. Breaking Out

[![](https://substackcdn.com/image/fetch/$s_!VC3q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F474f81a3-b444-4824-89d3-169026c20c4a_1024x559.png)](https://substackcdn.com/image/fetch/$s_!VC3q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F474f81a3-b444-4824-89d3-169026c20c4a_1024x559.png)

> “When we find that the code in an object is becoming complex … we can break out coherent units of behavior into helper types.”

**Goal**: Extract a distinct responsibility from a class that is doing too much. This helps clarify roles and reduces internal complexity.

Freeman and Pryce describe this as a method for improving the separation of concerns:

> "We factor out responsibilities into their own classes to help keep our objects focused and testable."

>  - Freeman &amp; Pryce, GOOS, Chapter 16

### Before (Tightly Coupled Logic)

```
class ReportService {
    fun generate(): ByteArray {
        val data = collectData()
        return renderToPdf(data)
    }
}
```

### After (Extracted Peer)

```
interface PdfRenderer {
    fun render(data: ReportData): ByteArray
}

class ReportService(private val renderer: PdfRenderer) {
    fun generate(): ByteArray {
        val data = collectData()
        return renderer.render(data)
    }
}
```

If you want to read about this topic in depth, check out **[Breaking out to improve cohesion (peer detection techniques)](https://codesai.com/posts/2025/11/breaking-out-to-improve-cohesion)**

---

### 2. Budding Off

[![](https://substackcdn.com/image/fetch/$s_!Bfwb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F659cd622-2b7a-4230-91f8-b4bd7753b4e1_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Bfwb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F659cd622-2b7a-4230-91f8-b4bd7753b4e1_1024x559.png)

**Goal**: Convert a hidden or hardcoded dependency into an explicit, replaceable peer.

Freeman and Pryce's definition:

> “*When we want to mark a new domain concept in the code, we often introduce a placeholder type that wraps a single field, or maybe has no fields at all. As the code grows, we fill in more detail in the new type by adding fields and methods. With each type that we add, we’re raising the level of abstraction of the code.*”

> - Freeman &amp; Pryce, GOOS, page 59

This technique is highly effective when isolating time, randomness, or external systems.

### Before Budding Off

```
class TokenService {
    fun generate(): String =
        "${UUID.randomUUID()}:${LocalDateTime.now()}"
}
```

### After Budding Off

```
// After
interface Clock {
    fun now(): LocalDateTime
}

class SystemClock : Clock {
    override fun now(): LocalDateTime = LocalDateTime.now()
}

class TokenService(private val clock: Clock) {
    fun generate(): String =
        "${UUID.randomUUID()}:${clock.now()}"
}
```

### 3. Bundling Up

[![](https://substackcdn.com/image/fetch/$s_!jQsM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a6dc36e-2c19-4e8d-881f-dd46139dec92_1024x559.png)](https://substackcdn.com/image/fetch/$s_!jQsM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a6dc36e-2c19-4e8d-881f-dd46139dec92_1024x559.png)

**Goal**: Consolidate several related internals into a higher-level peer abstraction.

The definition:

*> When we notice that a group of values are always used together, we take that as a suggestion that there’s a missing construct. A first step might be to create a new type with fixed public fields—just giving the group a name highlights the missing concept. Later we can migrate behavior to the new*

> - Freeman &amp; Pryce, GOOS, page 59

This supports encapsulation and makes intent clearer.

### Before Bundling-up

```
fun checkout(subtotal: Double, tax: Double, shipping: Double, discount: Double): Double =
    subtotal + tax + shipping - discount
```

### After Bundling

```
data class PriceBreakdown(
    val subtotal: Double,
    val tax: Double,
    val shipping: Double,
    val discount: Double
) {
    val total: Double
        get() = subtotal + tax + shipping - discount
}

fun checkout(prices: PriceBreakdown): Double = prices.total

```

---

## Final Summary

By respecting the line between peers and internals, and applying the techniques of **Breaking Out**, **Budding Off**, and **Bundling Up**, you create tests that are robust, resilient to change, and deeply aligned with the architecture of your software.
