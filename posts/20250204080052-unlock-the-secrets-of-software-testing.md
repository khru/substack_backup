---
title: "Unlock the Secrets of Software Testing: State-Based, Output-Based, and Communication-Based verifications"
requested_url: "https://emmanuelvalverderamos.substack.com/p/unlock-the-secrets-of-software-testing"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/unlock-the-secrets-of-software-testing"
substack_post_id: 152656084
retrieved_at: "2026-03-20T08:35:57.084Z"
---
# Unlock the Secrets of Software Testing: State-Based, Output-Based, and Communication-Based verifications

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

### Introduction to testing types of verifications

In software testing, it's crucial to understand different verification styles to ensure code quality, robustness, and maintainability. This section focuses on three distinct styles of assertions: **State-Based**, **Output-Based**, and **Communication-Based**. These approaches are based on concepts from Vladimir Khorikov's book *Unit Testing Principles, Practices, and Patterns*, and are further explored in Emily Bache's article on test design styles. Each style offers a unique way to test your system, varying based on system behavior, dependency interactions, and verification requirements.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### The SUT and its behavior

The fundamental connection between these test types: **State-Based**, **Output-Based**, and **Communication-Based**—centers on the System Under Test ([SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test)) and its behavior. The appropriate testing approach depends on what's being tested (whether a class, component, or microservice) and what needs verification (state changes, outputs, or interactions).

This framework simplifies test categorization by focusing on how the [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test) behaves in different scenarios. From unit tests checking object states to integration tests verifying module communication, or contract tests confirming service interactions—each test ensures the [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test) behaves as intended.

In conclusion, effective testing goes beyond mere categorization or naming conventions. What matters most is the type of verification performed, the expected behavior of the [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test), and the long-term costs of test maintenance.

### State-Based verification

[![](https://substackcdn.com/image/fetch/$s_!_3cm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd671612-c4c3-4bd2-8772-f6cb2dba2343_9780x4288.png)](https://substackcdn.com/image/fetch/$s_!_3cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd671612-c4c3-4bd2-8772-f6cb2dba2343_9780x4288.png)

**State-based tests** verify the final state of a system after an operation is completed. These tests check whether the state of the system under test ([SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test)) or its collaborators has changed as expected after acting. The state can refer to the [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test) itself, its dependencies, or external dependencies like databases or file systems.

- **Usage**: This testing style is ideal for validating system state changes after specific interactions.
- **Example**: Consider a payment processing class. After calling the payment method, a state-based test would verify that the customer's balance has decreased by the correct amount.

```java
@Test
void add_given_product_to_the_order() {
  // Arrange
  Product product = new Product("Free Guy");
  Order sut = new Order();

  // Act
  sut.add(product);

  // Assert
  assertThat(sut.products())
      .hasSize(1)
      .containsExactly(product);
}
```

State-based tests excel at verifying persistent changes, especially when code has side effects that need tracking, such as database writes or object state modifications.

### Output-Based verification

[![](https://substackcdn.com/image/fetch/$s_!ZVv7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F098f29ec-dc3f-4838-bf12-7305c6530a11_9920x4489.png)](https://substackcdn.com/image/fetch/$s_!ZVv7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F098f29ec-dc3f-4838-bf12-7305c6530a11_9920x4489.png)

**Output-based tests** focus on providing input to the system under test ([SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test)) and verifying its output. These tests work with pure functions—those that produce no side effects and return only a value to the caller.

- **Usage**: These tests are ideal for functional units where the output depends solely on the input.
- **Example**: Consider a function that adds two numbers. An output-based test would feed different number pairs into the function and verify that each sum matches the expected result.

```java
@Test
void discount_of_two_products_should_be_two_percent() {
  // Arrange
  Product product1 = new Product("Kaamelott");
  Product product2 = new Product("Free Guy");

  // Act
  double discount = PriceEngine.calculateDiscount(product1, product2);

  // Assert
  assertThat(discount).isEqualTo(0.02);
}
```

Since output-based tests treat the system as a black box, they are effective at testing business rules and pure logic in a clean, straightforward manner.

### Communication-Based verification

[![](https://substackcdn.com/image/fetch/$s_!SCVD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda7ef076-ac15-41eb-b70c-12d2a49bd77a_9920x3736.png)](https://substackcdn.com/image/fetch/$s_!SCVD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda7ef076-ac15-41eb-b70c-12d2a49bd77a_9920x3736.png)

**Communication-based tests** verify how a system interacts with its collaborators by checking that the system under test makes the correct method calls to its dependencies. These dependencies are typically replaced with test doubles—mocks, stubs, or spies.

- **Usage**: Communication-based tests focus on verifying interactions rather than final states or outputs. They shine when testing systems with complex dependencies or when an operation's correctness depends on specific calls to collaborators.
- **Example**: Consider a class that sends emails for new user registrations. Rather than testing if an email was actually sent (which would require an external service), you would use a mock email sender to verify that it received the correct parameters.

```java
@Test
void greet_a_user_should_send_an_email_to_it() {
  // Arrange
  String email = "john.doe@email.com";
  EmailGateway emailGatewaySpy = mock(EmailGateway.class);
  Controller sut = new Controller(emailGatewaySpy);

  // Act
  sut.greetUser(email);

  // Assert
  verify(emailGatewaySpy, times(1)).sendGreetingsEmail(email);
}
```

Communication-based tests are particularly useful for validating how the [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test) works, ensuring that methods interact correctly with their dependencies. These tests can serve as a bridge between unit tests and integration tests when verifying communication flows.

## Summary

These three testing approaches offer distinct perspectives for verifying software correctness.

- **State-based tests** verify state changes after an action, making them perfect for scenarios involving persistent side effects.
- **Output-based tests** excel at pure logic verification, ensuring functions produce consistent, predictable results from given inputs.
- **Communication-based tests** examine how objects interact, ensuring different system components collaborate effectively.

Each approach has its strengths and limitations. Choosing the right one depends on your system's specific behavior. Used together, they create a robust strategy for maintaining software quality, reliability, and adaptability to change.

Thanks for reading Crafting software! This post is public so feel free to share it.

[Share](https://emmanuelvalverderamos.substack.com/p/unlock-the-secrets-of-software-testing?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## References

- Fowler, Martin. *Mocks Aren't Stubs*. [https://martinfowler.com/articles/mocksArentStubs.html](https://martinfowler.com/articles/mocksArentStubs.html)
- Khorikov, Vladimir. *Unit Testing Principles, Practices, and Patterns*.
- Bache, Emily. "Styles of Unit Tests. [https://sammancoaching.org/learning_hours/test_design/styles_of_unit_tests.html](https://sammancoaching.org/learning_hours/test_design/styles_of_unit_tests.html)
- Thirion, Yoan. *Some of the graphic references in the article*. [https://yoan-thirion.gitbook.io/knowledge-base/xtrem-reading/my-book-infographics](https://yoan-thirion.gitbook.io/knowledge-base/xtrem-reading/my-book-infographics)

[Start Survey](https://emmanuelvalverderamos.substack.com/survey/1553661?token=)
