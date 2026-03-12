---
title: "Happy Path vs. Sad Paths (Personal opinion)"
requested_url: "https://emmanuelvalverderamos.substack.com/p/happy-path-vs-sad-paths-personal"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/happy-path-vs-sad-paths-personal"
substack_post_id: 174813547
retrieved_at: "2026-03-12T08:37:11.600Z"
---
# Happy Path vs. Sad Paths (Personal opinion)

[![](https://substackcdn.com/image/fetch/$s_!JRfz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25c014ce-5ae9-45ff-9e56-d2f5a78e0373_6500x4334.jpeg)](https://substackcdn.com/image/fetch/$s_!JRfz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25c014ce-5ae9-45ff-9e56-d2f5a78e0373_6500x4334.jpeg)

## How I choose where to start

I love doing TDD, and I try to move in baby steps. Before I write the first test, I ask a simple question: what is the smallest step that gives me real feedback?

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## A common case: an endpoint with infrastructure preconditions

Suppose we need an API endpoint that requires authentication. Only after the user is authenticated can we run the business logic.

I could begin with a full happy path test. The problem is that it forces me to design the route, the controller, authentication, validation, and domain logic at once. That is a lot for a first red phase.

A smaller and often better first step is a sad path driven by the precondition. For example, “if the user is not authenticated, they cannot create or view the resource.” The exact status code depends on product policy. It might be 401, 403, or 404 to avoid resource enumeration. The important part is to pick one and lock it in a test.

### Why this sad path works well

- It forces you to create the minimal skeleton: route, controller, and authentication middleware or filter.
- It gives fast feedback that the HTTP pipeline and basic security are alive.
- It reduces the scope for the next step. Once the precondition is in place, the happy path becomes simpler to implement.

### Suggested baby step sequence

- **An unauthenticated request**&nbsp;returns the agreed-upon status code.
- **An authenticated request with invalid input**&nbsp;returns a 400 or 422 error.
- **An authenticated request with valid input** returns 201 and the created resource.
- **Additional domain rules,** such as invariants, idempotency, and conflict handling.

Each step focuses on observable behavior and forces only the code needed to pass the test.

## Mini acceptance tests at the HTTP level

Framework agnostic pseudocode:

```
# 1. Sad path based on authentication precondition
When POST /orders with body {...} and no auth
Then response.status is 401  # or 403 or 404 by policy

# 2. Sad path based on validation
Given an authenticated user
When POST /orders with invalid body {}
Then response.status is 422

# 3. Happy path
Given an authenticated user
When POST /orders with valid body { “sku”: “ABC-123”, “qty”: 2 }
Then response.status is 201
And response.body contains orderId and totals
```

These three tests drive a clean incremental implementation and let you refactor safely between steps.

## When not to start with the sad path

This strategy shines when the sad case comes from **infrastructure preconditions** such as authentication, authorization, rate limiting, or request shape. If your uncertainties are in **domain behavior** or subtle business rules, it is usually more effective to start with the **domain happy path**. Make the primary rule visible first, then fold the edges with additional tests.

Practical rule:

- Clear platform or infrastructure preconditions present: start with a sad path that exercises them.
- Uncertain domain behavior or language to discover: start with the happy path, define invariants, then cover edge cases.

## A quick decision checklist

- Does your first test force you to build too much at once? If yes, find a smaller sad path.
- Where is the biggest uncertainty: infrastructure or domain? Attack that area first.
- Can you get executable feedback in minutes? If not, cut the scope of the first test.
- Are error contracts and status codes agreed? Capture them in the test to avoid ambiguity.

## Conclusion

There is no universal order. In TDD, I look for the smallest step that gives useful feedback. With infrastructure preconditions, starting from a sad path activates the right skeleton and clears the way for the happy path. If the risk is in the domain, I begin with the main flow and then close the gaps. The key is to pause before typing, choose the first test that reduces risk, and move in short cycles.
