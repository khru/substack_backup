---
title: "Unit Testing: Basics"
subtitle: "Basic introduction to unit test"
requested_url: "https://emmanuelvalverderamos.substack.com/p/unit-testing-basics"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/unit-testing-basics"
substack_post_id: 153249906
retrieved_at: "2026-03-24T08:45:29.208Z"
---
# Unit Testing: Basics

### Basic introduction to unit test

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

## **Introduction**

Unit testing is a foundational practice in software development, ensuring that individual components of a system work as intended. By validating the smallest testable units of code, developers can identify and address issues early, build confidence in their implementations, and enable iterative improvements without fear of unintended consequences.

This article explores the origins, principles, and practices of unit testing, focusing on the distinctions between **solitary vs. sociable tests**, the characteristics of effective tests as outlined in the **Test Desiderata**, and the role of **pragmatism** in testing strategies. Through historical context, practical examples, and actionable insights, we aim to demystify unit testing and highlight its importance in crafting robust and sustainable software.

## **A Historical Perspective on Unit Testing**

### **The Roots of Unit Testing**

The theoretical roots of unit testing can be traced back to the structured programming era of the 1960s and 1970s when developers began breaking down software into smaller, testable components. The emphasis on modularity naturally lent itself to testing small, discrete units of functionality.

Unit testing became widely accessible with the release of **JUnit** by Kent Beck and Erich Gamma in 1997. Alongside Extreme Programming (XP) in the late '90s, developers began integrating unit tests as an essential practice in the Agile movement.

## **What is Unit Testing?**

### **Definition**

A **unit test** is an automated test that validates the behavior of the smallest testable unit of software, typically a single function or method, even a class. These tests are designed to:

- **Verify behavior**: Ensure that the code produces the expected results for given inputs.
- **Detect defects early**: Catch errors in logic or implementation at the earliest possible stage.
- **Enable refactoring**: Allow developers to improve or modify code with confidence.

### **Key Characteristics of Unit Tests**

The **Test Desiderata**, developed by Kent Beck, outlines the qualities of effective tests. For me, though, these are the key characteristics that a test should offer. The unit test for me should cover most of them.

### **Purpose**

Unit tests act as a developer's first line of defense by verifying that small pieces of code work correctly before integration into larger systems or the integration between several components of your application. These focused tests minimize downstream errors, leading to more stable and maintainable software.

## **Solitary vs. Sociable Unit Tests**

### Historical context

The terms were introduced by *Jay Fields* in his book **[Working Effectively with Unit Tests](https://leanpub.com/wewut)** in 2015.

[![](https://substackcdn.com/image/fetch/$s_!7PLf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ba82b10-aa81-469b-ab7c-29762ba967f5_312x457.jpeg)](https://substackcdn.com/image/fetch/$s_!7PLf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ba82b10-aa81-469b-ab7c-29762ba967f5_312x457.jpeg)

After that, Martin Fowler wrote an article about this topic **[UnitTest](https://martinfowler.com/bliki/UnitTest.html)**.

Consider the difference between testing a car engine in isolation versus testing it after installation with other car components. Unit tests, both solitary and sociable, help developers achieve precision and confidence across these different testing scenarios.

### **Definitions**

- **Solitary Unit Tests**: Focus on isolating the unit under test by mocking or stubbing external dependencies. These tests focus solely on the logic within the unit itself.
- **Sociable Unit Tests**: Validate the behavior of a unit in collaboration with its immediate dependencies, ensuring that interactions are functioning as expected.

### **Examples**

To illustrate the differences between solitary and sociable tests, let's examine two scenarios: a `PrintDate` utility and a `Product` class with a dependency.

### **Solitary Test**

A class that receives a logger and a date and outputs a timestamped message.

[![](https://substackcdn.com/image/fetch/$s_!cbuf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F733654ec-f04f-4f80-82e3-959b67e0c265_5384x3322.png)](https://substackcdn.com/image/fetch/$s_!cbuf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F733654ec-f04f-4f80-82e3-959b67e0c265_5384x3322.png)

**Implementation Code**

```typescript
interface Calendar {
  today(): string;
}
```

```typescript
interface Calendar {
  today(): string;
}
```

```typescript
interface Printer {
  printLine(line: string): void;
}
```

```typescript
class PrintDate {
  private calendar: Calendar;
  private printer: Printer;

  constructor(calendar: Calendar, printer: Printer) {
    this.calendar = calendar;
    this.printer = printer;
  }

  printCurrentDate(): void {
    const today = this.calendar.today();
    this.printer.printLine(today);
  }
}
```

**Test Code**

```typescript
describe('PrintDate (Solitary Tests)', () =&gt; {
  it('should print the current date returned by the calendar', () =&gt; {
    // Arrange
    const stubCalendar: Calendar = { today: jest.fn().mockReturnValue('2024-06-10') };
    const mockPrinter: Printer = { printLine: jest.fn() };
    const printDate = new PrintDate(stubCalendar, mockPrinter);

    // Act
    printDate.printCurrentDate();

    // Assert
    expect(mockPrinter.printLine).toHaveBeenCalledWith('2024-06-10');
  });
});
```

### **Sociable Test**

A controller that integrates with a service layer to fetch and display user data.

[![](https://substackcdn.com/image/fetch/$s_!nUim!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa37f1f4-f905-4877-89b7-c5e20a4527ff_6088x3322.png)](https://substackcdn.com/image/fetch/$s_!nUim!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa37f1f4-f905-4877-89b7-c5e20a4527ff_6088x3322.png)

**Implementation Code**

```typescript
class Price {
  private cost: number;
  private margin: number;

  constructor(cost: number, margin: number) {
    this.cost = cost;
    this.margin = margin;
  }

  calculate(): number {
    return this.cost + (this.cost * this.margin) / 100;
  }
}
```

```typescript
class Product {
  private name: string;
  private price: Price;

  constructor(name: string, cost: number, margin: number) {
    this.name = name;
    this.price = new Price(cost, margin);
  }

  productDetails(): { name: string; price: number } {
    return {
      name: this.name,
      price: this.price.calculate(),
    };
  }
}
```

**Test Code**

```typescript
describe('Product - Sociable Unit Tests', () =&gt; {
  it('calculates the price of the product correctly with a given margin', () =&gt; {
    // Arrange
    const product = new Product('Laptop', 1000, 20);

    // Act
    const result = product.productDetails();

    // Assert
    expect(result).toEqual({
      name: 'Laptop',
      price: 1200, // Cost: 1000 + 20% margin =&gt; 1200
    });
  });
});
```

### **Trade-offs**

- **Solitary tests** are faster and more reliable, but they risk over-mocking, which can lead to tests that don’t reflect real-world behavior. While sociable tests validate real interactions, they can fail intermittently due to changes in collaborators. To address this, ensure collaborators have clear, stable contracts, and minimize reliance on dynamic data sources.
- **Sociable tests** provide better coverage of interactions but may become flaky due to dependency changes, and also could be more prompt to not test the behavior but the code structure if the person lacks experience with creating tests.

[![](https://substackcdn.com/image/fetch/$s_!xUag!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34c69f1a-7f70-4148-97d3-0341a0de6c90_3576x800.png)](https://substackcdn.com/image/fetch/$s_!xUag!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34c69f1a-7f70-4148-97d3-0341a0de6c90_3576x800.png)

## Internal VS Peer

These terms were introduced in the book *Growing Object-Oriented Software, Guided by Tests*, where the difference between the concepts of *peer* and *internal* is explained.

The book provides the following insights to help understand these concepts:

> As we organize our system, we must decide what is inside and outside each object, so that the object provides a coherent abstraction with a clear API. Much of the point of an object, as we discussed above, is to encapsulate access to its internals through its API and to hide these details from the rest of the system. An object communicates with other objects in the system by sending and receiving messages, the objects that communicates directly are its peers.

> This decision matters because it affects how easy an object is to use, and so contributes to the internal quality of the system. If we expose too much of an object’s internals through its API, its clients will end up doing some of its work

- **Peers:** External collaborators that the system under test (**SUT**) depends on to perform its responsibilities. Peers represent meaningful **roles** in the system and **should be replaced with test doubles (mocks, stubs, spies) when necessary**.
- **Internals:** Components that exist **inside the boundary** of the **SUT** and are part of its internal structure. They should **not** be replaced with test doubles because doing so leads to **fragile, structure-sensitive tests**.

### **Why does this matter in unit testing?**

Misunderstanding this distinction often leads to:
✅ **Over-mocking:** Testing internal collaborators separately from the SUT increases test fragility and makes refactoring painful.
✅ **Testing implementation details instead of behavior:** Mocks should be used for **peer interactions** but **not** for **internals**.
✅ **False failures:** Small structural changes break tests unnecessarily when mocks are used for internal objects.

If you want to know more about this topic I suggest that you check the article [mockist tdd unit is not the class](https://codesai.com/posts/2025/03/mockist-tdd-unit-not-the-class)

## **Conclusion**

While unit tests offer many advantages, their most valuable benefit is providing quick, specific feedback through tests that are easy to write and read. As developers spend significant time reading code, these characteristics make unit tests both meaningful and worthwhile.

Understanding the distinction between the two types of unit tests is crucial, as it helps clarify common misconceptions. The examples above illustrate these differences clearly.

It's worth emphasizing that while both approaches have their trade-offs, neither is inherently superior—they serve different purposes. What matters is understanding when, how, and why to use each one, as they are distinct tools in our testing arsenal.

By understanding solitary and sociable tests, developers can create a well-rounded test suite that balances precision and collaboration. Start by identifying units that require isolation, and incrementally introduce sociable tests to validate critical integrations. In the end, effective unit testing will make your software robust, reliable, and maintainable.

### When do I use sociable test or solitary testing

**Sociable**:

- If our **SUT** uses collaborators that return **immutable values**.
- If our **SUT** uses collaborators that are **pure functions**.
- If our **SUT** is the **Aggregate Root**.
- If our **SUT** is **orchestrating** individual logics.
- If out **SUT** has “**internal collaborators**”
- …

**Solitary** (*careful with testing structure and not behavior*):

- Our test requires a collaborator to behave in a specific way.
- We need to avoid a side effect (e.g. mutate the state on other dependencies that are not my SUT)
- We want to stay within the boundaries of our application (e.g. calling a 3rd party system)
- If our test is breaking the [FIRST principles](https://agileinaflash.blogspot.com/2009/02/first.html).

I think this video from the conversation between Kent Beck, Martin Fowler and DHH, about if TDD is dead, is really interesting, [Martin Fowler mentions this](https://youtube.com/clip/Ugkx8xlSuwqy9FHGrHjBYlgvv7-KgBexgDb9?si=fj4z78zqpl5RVczc).

I think that the focus should never be on the size of the unit, but on the properties that the test should have.

## References

- **Beck, Kent**. *Test-Driven Development: By Example*. Addison-Wesley, 2002.
- **Beck, Kent**. *Extreme Programming Explained: Embrace Change*. Addison-Wesley, 2000.
- **Fowler, Martin**. *Refactoring: Improving the Design of Existing Code*. Addison-Wesley, 1999.
- **Meszaros, Gerard**. *xUnit Test Patterns: Refactoring Test Code*. Addison-Wesley, 2007.
- **Martin, Robert C.** *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall, 2008.
- **Feathers, Michael C.** *Working Effectively with Legacy Code*. Prentice Hall, 2004.
- **Beck, Kent**. *Test Desiderata* [https://testdesiderata.com](https://testdesiderata.com).
- **Marick, Brian**. *The Craft of Software Testing: Subsystems Testing Including Object-Based and Object-Oriented Testing*. Prentice Hall, 1995.
- **Fields, Jay**. *Working Effectively with Unit Tests* [https://leanpub.com/wewut](https://leanpub.com/wewut)
- Schuchert, Brett &amp; Ottinge, Tim*. F.I.R.S.T principles* [https://agileinaflash.blogspot.com/2009/02/first.html](https://agileinaflash.blogspot.com/2009/02/first.html)
- **Rivero, Manuel**. *The class is not the unit in the London school style of TDD* [https://codesai.com/posts/2025/03/mockist-tdd-unit-not-the-class](https://codesai.com/posts/2025/03/mockist-tdd-unit-not-the-class)
