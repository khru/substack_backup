---
title: "How to write a test?"
subtitle: "The 4 phases of a test and the 3 steps in a test"
requested_url: "https://emmanuelvalverderamos.substack.com/p/how-to-write-a-test"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/how-to-write-a-test"
substack_post_id: 152960047
retrieved_at: "2026-03-05T08:36:07.655Z"
---
# How to write a test?

### The 4 phases of a test and the 3 steps in a test

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

## Introdución

This article provides an introductory guide to writing tests. We'll explore the 4 phases of a test and the 3 test components, examining how they work together. To get the most from this guide, you should be familiar with the concept of Subject Under Test. Having experience with a testing framework will also help you grasp these concepts better.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## Las 4 fases de un test

[![](https://substackcdn.com/image/fetch/$s_!9EMR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2079dc6-fc11-41de-9783-7a92a89572de_2760x3118.png)](https://substackcdn.com/image/fetch/$s_!9EMR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2079dc6-fc11-41de-9783-7a92a89572de_2760x3118.png)

### **Setup**

This phase prepares all necessary conditions for the test. Here, you create objects, set initial states, configure dependencies, and get the test environment ready.

- **Examples**:
- Instantiate a class.
- Create test doubles (e.g., stubs, spies).
- Prepare input data that the [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test)will need.

Testing frameworks provide two key setup concepts to make your tests more readable: `BeforeEach` and `BeforeAll`. With `BeforeEach`, any functionality defined in that method runs before each test. With `BeforeAll`, the defined functionality runs once before the first test begins and doesn't run again until the next test suite execution.

### Exercise

This phase executes the behavior being tested. You interact with the system under test ([SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test)) by calling the method or function you want to validate.

- **Examples**:
- Call the [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test) with the setup information and capture the output based on what you want to verify.

### Verify

In this phase, you check if the output or behavior of the system under test matches what you expect. This is where you use assertions to verify correctness.

- Use assertions to confirm that the returned value matches the expected output.
- Verify interactions with test doubles when indirect outputs are involved.

This phase relates directly to verification types, which will be covered in another post.

### **Teardown**

This phase restores the test environment to its original state by cleaning up resources. This prevents tests from interfering with each other when they share state or resources.

- **Examples**:
- Close database connections or any other external dependency.
- Reset test doubles or mock servers
- Clear temporary files or reset static variables.

Most testing frameworks provide similar functionality for teardown as they do for setup. Methods like `AfterEach` and `AfterAll` work like their setup counterparts but execute after tests are complete.

## The 3 parts of a test - Arrange, Act, Assert or Given, When, Then

> Arrange-Act-Assert is a simple concept, and probably only adds marginal value. But it costs nothing to practice, and it gets us that much closer to being a community willing to agree on some standards. What I also like about memorable acronyms like AAA is that they provide a consistent way to communicate simple ideas, which often don't have concise and consistent names.

> - [Tim Ottinger](http://agileotter.blogspot.com/) &amp; [Jeff Langr](http://langrsoft.com/)

The **Arrange-Act-Assert (AAA)** pattern is a widely used method for writing clear, systematic unit tests. It divides each test into three distinct phases:

- **Arrange:** Set up the initial test conditions by creating objects, configuring dependencies, and preparing the test environment. This establishes the context for testing the desired behavior.
- **Act:** Execute the functionality you want to test by calling methods or functions of the System Under Test ([SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test)) using the prepared data.
- **Assert:** Verify the results by comparing the actual output with expected outcomes to confirm the [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test) behaves correctly.

This pattern makes tests easier to understand and maintain by separating responsibilities. Each test focuses on a specific behavior, which improves precision and effectiveness.

The AAA pattern mirrors the **Given-When-Then** approach used in Behavior-Driven Development (BDD), where:

- **Given:** Sets up the initial context or preconditions.
- **When:** Describes the action or event being executed.
- **Then:** Specifies the expected outcome or postcondition.

Both approaches create tests that are easy to read and understand for developers, which is for me one of the most important points, because like the [test desiderata](https://emmanuelvalverderamos.substack.com/p/what-makes-a-great-automated-test) mentions readability is one of the important attributes that a good test should have.

These 3 parts of a test have a direct and important relationship with the first three phases of the test phases we discussed earlier. The Arrange part corresponds to the Setup phase, where we prepare our test environment. The Act part aligns with the Exercise phase, where we execute the behavior we want to test. Finally, the Assert part matches the Verify phase, where we confirm our expectations. This structured approach helps create clear, maintainable tests that are easy to understand and modify. If we examine this relationship in more detail, it would look something like this.

[![](https://substackcdn.com/image/fetch/$s_!j7cq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F750819d1-6c58-4996-bf19-534f027c85e6_15564x5422.png)](https://substackcdn.com/image/fetch/$s_!j7cq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F750819d1-6c58-4996-bf19-534f027c85e6_15564x5422.png)

Let’s see a small example

```java
public class TemperatureConverterShould {

  @Test
  void converts_the_temperature_given_in_celsius_to_fahrenheit() {
    // Arrange
    TemperatureConverter converter = new TemperatureConverter();
    double inCelsius = 25.0;

    // Act
    double inFahrenheit = converter.celsiusToFahrenheit(inCelsius);

    // Assert
    assertEquals(77.0, inFahrenheit, 0.001); // Allowing a small delta for floating-point precision
  }
}
```

## Test focus on the Behavior

To create a good test is really important to identify the behavior you are trying to test, and identify the best way of testing it.

## Conclusions

Understanding the phases of a test is crucial—it reveals how tests work behind the scenes and provides valuable insights into your current testing phase and requirements during development.

Similarly, using the Arrange-Act-Assert or Given-When-Then patterns helps separate responsibilities in tests and guides our thinking about assertions. This is why many TDD practitioners start with assertions: they shape how the test will be structured and what needs to be verified.

Focus always on the behaviour to test, and identify the best way to do it.

## References

- Ottinger, Tim. Langr, Jeff. Agile in a Flash - Arrange-Act-Assert. https://agileinaflash.blogspot.com/2009/03/arrange-act-assert.html
- [Bache, Emily. 3 Parts of a TEST | Guided Learning Hour](https://youtu.be/8KB5aF6QXe8).
- Bache, Emily. 3 Parts of a TEST [https://sammancoaching.org/learning_hours/test_design/three_parts_of_a_test.html](https://sammancoaching.org/learning_hours/test_design/three_parts_of_a_test.html)
- Meszaros, Gerard. Four-Phase Test. [http://xunitpatterns.com/Four%20Phase%20Test.html#:~:text=How%20It%20Works,result%20verification%20and%20fixture%20teardown.](http://xunitpatterns.com/Four%20Phase%20Test.html#:~:text=How%20It%20Works,result%20verification%20and%20fixture%20teardown.)
