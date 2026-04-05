---
title: "What to test? The Subject Under Test (SUT)"
requested_url: "https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test"
substack_post_id: 152835799
retrieved_at: "2026-04-05T07:53:52.990Z"
---
# What to test? The Subject Under Test (SUT)

## Managing Expectations

### Who is this article for?

This article is designed for:

- Beginners exploring the world of automated testing.
- Individuals starting with Test-Driven Development (TDD) want to understand what makes a good test.

### What this article won't cover

While this article provides a strong foundation, it won't cover:

- TDD processes.
- Strategies like the Test Pyramid.
- Types of tests (e.g., unit vs. integration).
- Test doubles such as mocks, stubs, or spies.

Instead, we'll focus on the characteristics that define a great automated test.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## What’s a Subject Under Test? (SUT)

The SUT (Subject Under Test) is the primary focus of a test. It's the piece of software—whether a class, module, or entire system—that you examine to verify its behavior. Think of it as the protagonist of your testing story.

> "The system under test". It is short for "whatever thing we are testing" and is always defined from the perspective of the test. When we are writing unit tests, the system under test (SUT) is whatever class (a.k.a. CUT), object (a.k.a. OUT), or method(s) (a.k.a. MUT) we are testing. When we are writing customer tests, the SUT is probably the entire application (a.k.a. AUT) or at least a major subsystem of it. The parts of the application that we are not verifying in this particular test may still be involved as a depended-on component (DOC).

> - Gerard Meszaros

[![](https://substackcdn.com/image/fetch/$s_!sn5L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcadb1e6-5109-46b8-9166-811a67795360_10984x1096.png)](https://substackcdn.com/image/fetch/$s_!sn5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcadb1e6-5109-46b8-9166-811a67795360_10984x1096.png)

## Example from the Customer's Point of View - Customer Test

> A test that verifies the behavior of a slice of the visible functionality of the overall system. The system under test (SUT) may be the entire system or a fully-functional top-to-bottom slice (or "module") of the system. A customer test should be independent of the design decisions made while building the SUT. That is, we should require the same set of customer tests regardless of how we choose to build the SUT. (But how the customer tests interact with the SUT may be affected by high-level software architecture decisions.)

> - Gerard Meszaros

Let's consider a practical example: imagine we work at an e-commerce company and need to create a view for adding a credit card. We can approach this from different perspectives. One key requirement is that when a user enters a credit card number, the system must validate it and ensure it meets our banking providers' format requirements.

In this case, the subject under test would be our input field, and we'll create tests to verify this validation behavior.

[![](https://substackcdn.com/image/fetch/$s_!vgNc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85a2a1fa-682c-416f-a5eb-3328c2b3d40a_10624x8704.png)](https://substackcdn.com/image/fetch/$s_!vgNc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85a2a1fa-682c-416f-a5eb-3328c2b3d40a_10624x8704.png)

Now let's verify that the form correctly transmits information to the payment management service for card registration. When a user clicks the submit button, we need to ensure the external service receives properly formatted data.

[![](https://substackcdn.com/image/fetch/$s_!8BqO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63b1a4f2-4eaa-4ac8-b82c-11964fad3272_10624x8704.png)](https://substackcdn.com/image/fetch/$s_!8BqO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63b1a4f2-4eaa-4ac8-b82c-11964fad3272_10624x8704.png)

For this scenario, the form itself becomes our subject under test. Here are the key behaviors we need to verify:

- Display validation messages when fields contain errors
- Send properly formatted data to the external payment system
- Redirect users after successful card addition
- Show error messages if card registration fails

## What would the SUT look like in the backend?

Let's explore how a subject under test operates in our card registration system's backend. This example will demonstrate how to apply our testing principles in a practical scenario.

To visualize this better, let's examine the class structure that represents our card registration system's architecture:

[![](https://substackcdn.com/image/fetch/$s_!9jfs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F709b9654-152f-49de-ad66-76a6f6a5fe2e_5344x6752.png)](https://substackcdn.com/image/fetch/$s_!9jfs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F709b9654-152f-49de-ad66-76a6f6a5fe2e_5344x6752.png)

Before we explore the implementation details, let's discuss an essential concept: Depended-On Components (DOCs). Understanding DOCs is crucial for mastering testing strategies for the SUT.

## What are DOCs (Depended-On Components)?

DOCs are the components that the SUT interacts with to perform its function. These include databases, APIs, external services, or other classes. While they're not the focus of your test, they play a vital supporting role.

Let's examine a concrete example where our subject under test is the `AddPaymentCartUseCase`. This class is a critical component in our payment processing system. Though we could test it in several ways, we'll focus on one specific strategy to illustrate our key points.

For effective testing, we'll implement a test double that simulates the Stripe service's calls. This approach serves multiple purposes: it creates deterministic tests with consistent results, ensures quick test execution without external dependencies, and aligns with the Test desiderata principles.

Through this approach, we can verify these critical aspects of our system's behavior:

- Perform thorough input validation on all payment card details, detecting errors early and responding appropriately when information doesn't meet specified criteria.
- Carefully examine the interactions with the Stripe service through our test double, ensuring proper formatting and transmission of all necessary information.
- Implement comprehensive error handling for various HTTP scenarios, including timeout conditions, network failures, and unexpected response codes.

[![](https://substackcdn.com/image/fetch/$s_!vw0F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e2093ba-92c3-4dcc-b19f-ac1cb5f6caf4_11574x6912.png)](https://substackcdn.com/image/fetch/$s_!vw0F!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e2093ba-92c3-4dcc-b19f-ac1cb5f6caf4_11574x6912.png)

Alternatively, we can test the `AddPaymentCartUseCase` by isolating it from the PaymentService using a test double. While this approach tests similar behaviors, it creates a different test boundary that focuses specifically on the use case's interactions.

[![](https://substackcdn.com/image/fetch/$s_!5yrM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9521ddc-21b3-4c5b-8341-fb4a108d2147_11574x7040.png)](https://substackcdn.com/image/fetch/$s_!5yrM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9521ddc-21b3-4c5b-8341-fb4a108d2147_11574x7040.png)

## Creating the SUT in testing

The process of creating the SUT involves setting up the system or component you want to test in a controlled manner. This includes initializing it with the required state, injecting dependencies (either real or test doubles), and configuring any needed context.

> The SUT is often defined by how well we can draw clear boundaries around what we want to verify, which directly impacts the effectiveness of our test strategy.

*> - Martin Fowler*

## Conclusions

Understanding the subject under test is essential for effective testing and selecting the most suitable testing approach. Your choice should be guided by the level of confidence each method provides and how well different testing strategies fit your needs. As shown in our examples, the same subject under test can be evaluated using different boundaries—whether testing the use case in isolation or examining its interactions with collaborating services.

### Key Takeaways:

- **SUT and DOCs**: Identify your system's boundaries and dependencies to create focused, meaningful tests.
- **Customer tests**: Design tests that validate user-facing behavior without depending on implementation details.
- **Strategic boundaries**: Test the same SUT at different boundary levels to gain deeper insights into system reliability and make informed testing decisions.

## References

- Meszaros, Gerard. *Subject under test (SUT)*. [xUnit Patterns](http://xunitpatterns.com/SUT.html).
- Meszaros, Gerard. *Customer test*. [xUnit Patterns](http://xunitpatterns.com/customer%20test.html).
- Meszaros, Gerard. *Depended-on component (DOC)*. [xUnit Patterns](http://xunitpatterns.com/DOC.html).
- Garzas, Javier. *¿Qué estoy probando y cuáles son mis dependencias en testing?*. [Javier Garzas](https://www.javiergarzas.com/2015/09/que-estoy-probando-y-cuales-son-mis-dependencias-en-testing.html?utm_source=chatgpt.com).
- Meszaros, Gerard. *xUnit Test Patterns: Refactoring Test Code*.
