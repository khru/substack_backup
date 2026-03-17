---
title: "Exploring Testing Strategies: Past, Present, and Future"
requested_url: "https://emmanuelvalverderamos.substack.com/p/exploring-testing-strategies-past"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/exploring-testing-strategies-past"
substack_post_id: 154266094
retrieved_at: "2026-03-17T08:45:46.609Z"
---
# Exploring Testing Strategies: Past, Present, and Future

## What Is a Testing Strategy?

A **Testing Strategy** is a **high-level, systematic plan** that defines how to ensure **software quality** throughout development. It serves as a **blueprint** for testing, outlining the **approach, scope, objectives, tools, processes, and techniques** teams use to validate functionality, performance, security, and usability for a **reliable and maintainable product**.

This strategy **aligns testing efforts** with business and technical goals, emphasizing **risk mitigation**, **early defect detection**, and **continuous feedback** to improve software quality.

A **testing strategy** is a **high-level plan** that defines:

- **What to test:** components, integrations, workflows, etc.
- **How to test:** tools, frameworks, automation, and manual checks.
- **Why to test:** specific goals, such as **confidence in releases**, and **error prevention**.

### Key Purpose:

- **Confidence:** Ensures the system works as expected under different conditions.
- **Maintainability:** Prevents regressions and supports **safe refactoring**.
- **Code resilience:** Keeps the test suite efficient as systems grow.

### Testing objectives

Defines **what needs to be tested** and **why**. Examples include:

- Ensuring **critical functionality** works as expected.
- Validating **system performance** under load.
- Verifying **security measures** to prevent vulnerabilities.
- Maintaining **regression coverage** during iterations.

### Scope and coverage

Specifies the **boundaries** of testing, what will be tested and **what won't**.

- **In-Scope:** Core features, APIs, third-party integrations.
- **Out-of-Scope:** Legacy systems or experimental features.

Coverage defines:

- **Functional testing** (features and workflows).
- **Non-functional testing** (performance, scalability, security).
- **Edge cases** and **error handling**.

### Testing Levels

Break testing into **granular stages**, each targeting different aspects of the software. Common levels include:

- **Unit Testing:** Verifies individual components or methods in isolation.
- **Integration Testing:** Ensures modules work together.
- **System Testing:** Tests the complete application in its environment.
- **Acceptance Testing:** Validates requirements based on business expectations.

### Testing Types

Specifies the **types of testing** needed, based on product complexity and risk:

- **Functional Testing:** Ensures features meet requirements.
- **Non-Functional Testing:** Evaluates performance, scalability, and usability.
- **Regression Testing:** Confirms existing features are unaffected by new changes.
- **Security Testing:** Identifies vulnerabilities to prevent attacks.
- **Exploratory Testing:** Uncovers unexpected behaviors through manual investigation.
- **Automated Testing:** Speeds up execution for repetitive tasks like regression tests.
- …

### Testing Tools and Frameworks

Outlines the **toolchain** used for test execution, automation, and reporting:

- **Unit Testing Tools:** JUnit, NUnit.
- **Integration Testing Tools:** Testcontainers, WireMock, Pact.
- **UI Testing Tools:** Selenium, Playwright, Cypress.
- **Performance Testing Tools:** JMeter, Gatling, Locust.
- **CI/CD Integration:** Jenkins, GitLab CI, GitHub Actions.

### Roles and Responsibilities

Defines who is accountable for **designing**, **implementing**, **executing**, and **maintaining tests**.

- **Developers:** Write unit and integration tests.
- **Test Automation Engineers (Optional):** Implement and maintain automation frameworks.
- **Ops/Infrastructure Engineers:** Set up test environments and CI/CD pipelines.

### Risk assessment and mitigation

Identifies **risks** and prioritizes testing based on their **impact and likelihood**. Examples include:

- **High-risk areas:** Payment processing, authentication, or data integrity.
- **Risk Mitigation Strategies:** Use contract tests and mocks for third-party dependencies.

**Note**: *A modern approach emphasizes that **developers own testing responsibilities**, integrating testing into development workflows.*

### Test environment setup (when needed)

Specifies the **infrastructure** needed for testing, including:

- **Development Environments** for tests.
- **Staging Environments** for integration and system tests.
- **Isolated Containers** for testing microservices.

### Sensible defaults for testing strategies

A **sensible default** is a **template or guideline** that teams can adopt, adapt, and evolve. Instead of starting from scratch, teams can rely on proven patterns and adjust based on **architecture** (e.g., monoliths vs. microservices) and **team workflows**.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## More common testing strategies

- Manual testing (Created around 1950)
- [The Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)(2009 - Mike Cohn and Martin Fowler)
- Testing Diamond
- [Testing Trophy](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)(2018 - Kent C. Dodds)
- [Testing Honeycomb](https://engineering.atspotify.com/2018/01/testing-of-microservices/)(2018 - Spotify)

## Manual Testing

### **Historical background**

#### Early software testing (1950s–1970s)

- Testing was **entirely manual**, performed by **programmers** or **end-users** during the **Waterfall development model**.
- Focused primarily on **functional verification** and **debugging programs** step-by-step.
- Testing strategies were **ad-hoc**, often unstructured, and documentation was **minimal**.

#### Structured testing (1980s–1990s)

- The rise of **structured programming** introduced the **V-Model** for testing, formalizing testing into **phases** (Unit, Integration, System, and Acceptance Testing).

[![](https://substackcdn.com/image/fetch/$s_!yhPP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24d61efb-59f6-45a3-8f84-06affde24700_1434x1236.png)](https://substackcdn.com/image/fetch/$s_!yhPP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24d61efb-59f6-45a3-8f84-06affde24700_1434x1236.png)

- Test cases became **documented artifacts**, and **test plans** outlined scope, requirements, and criteria.
- **Exploratory testing** emerged to address gaps in predefined test cases.

#### Modern Agile Era (2000s–Today)

- Agile development shifted the focus to **iterative testing cycles**, integrating manual testing into **sprints** for **early feedback**.
- Manual testing adapted to **exploratory** and **session-based testing** while automation began replacing **regression** and **repetitive tests**.
- Despite advancements in **CI/CD pipelines** and **test automation tools**, manual testing remains relevant for **UX testing**, **edge cases**, and **new feature validation**.

---

[![](https://substackcdn.com/image/fetch/$s_!Vw_V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff184821-a9c7-48d8-8b68-5a1fe8e48229_2141x2790.png)](https://substackcdn.com/image/fetch/$s_!Vw_V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff184821-a9c7-48d8-8b68-5a1fe8e48229_2141x2790.png)

The idea is simple: it starts with many manual tests and, over time, tries to convert them into acceptance or E2E tests, with some integration tests and fewer unit tests.

### The problem

- As the software evolves and grows, we need to create more tests. The team performing manual tests must also document and track each test so that they can repeat it when new functionality is added. They need to verify that existing behavior hasn't been broken (regression tests).
- Difficult to scale and maintain over time, as tests continuously grow.
- Having designed the code without considering its testability, introducing other types of tests later becomes complicated, resulting in tests that are harder to write, read, and maintain.
- Too much waste occurs when separating development from testing, as this increases both the feedback loop and the amount of rework needed.
- From my perspective, there's another factor that makes this strategy particularly fragile: when trying to invert the pyramid to increase automated tests, the complexity of existing tests makes them fragile and difficult to modify. This causes some tests to fail during code refactoring and new test addition, not because of code errors, but due to changes in its structure.

**Focus**

Manual testing focuses on **human-driven validation** of software behavior. It emphasizes **exploratory testing**, **usability validation**, and **edge cases** that are difficult to automate.

Key aspects include:

- **Exploratory Testing**: Embraces creativity and intuition to uncover unexpected issues.
- **User-Centric Approach**: Simulates real user interactions to validate workflows and usability.
- **Context-Driven Flexibility**: Adapts to changing requirements and emerging issues during development.

**Levels**

- **Exploratory Testing**
	- **Definition**: Testers systematically explore the application without scripts, using their **expertise** and **intuition** to find defects.
	- **Purpose**: Uncovers **unknown unknowns**, usability issues, and unexpected behaviors.
- **Ad-Hoc Testing**
	- **Definition**: Quick, unstructured testing where testers **check functionality** without following formal procedures.
	- **Purpose**: Provide rapid feedback before releases to identify **obvious issues**.
- **User Acceptance Testing (UAT)**
	- **Definition**: Validates that the application fulfills **business requirements** and **stakeholder needs**.
	- **Purpose**: Confirms the system meets functional requirements specified in the project.
- **Regression Testing**
	- **Definition**: Checks that **existing features** continue working after system changes.
	- **Purpose**: Ensures new code changes don't disrupt existing functionality.

**Application**

Manual testing proves most valuable in this specific context:

- **Non-functional Testing:** Examines **accessibility**, **localization**, and **compliance** requirements.

Tools Commonly Used:

- **Excel/Google Sheets:** This is used to document test cases and steps.
- **JIRA** or **TestRail:** This is used to track test execution and defect logging.
- **Postman:** This is for manual API testing before automation implementation.

**Critique**

- Advantages
	- Can’t think of a real one
- Disadvantages
	- **Time-Consuming:** Requires significant manual effort, especially for repetitive tasks, making it slower than automated approaches.
	- **Prone to Human Error:** Results may vary based on the tester’s experience and focus, potentially leading to missed defects.
	- **Limited Scalability:** Inefficient for large systems with multiple devices, platforms, and browsers.
	- **Poor CI/CD Support:** Does not integrate seamlessly into automated pipelines required for continuous testing in Agile and DevOps workflows.
	- **False Sense of Security:** Focuses on **happy paths**, often overlooking edge cases and non-deterministic failures that automated tests can simulate better.
	- **Difficult to change:** When you’ve been using it for some time is hard to revert it.

## Test Pyramid

### Historical context

The **Test Pyramid** is one of the most well-known testing strategies in software development. It was introduced by **Mike Cohn** in his 2009 book, *"Succeeding with Agile"*. While **Martin Fowler** later expanded on the concept in his blog post *"The Practical Test Pyramid"*, it is Mike Cohn who is credited with coining the term and formalizing its structure.

Before the **Test Pyramid**, testing strategies often leaned heavily on **manual testing** or **end-to-end tests**. These approaches posed challenges such as:

- **Slow Feedback Loops**: End-to-end tests required large setups, were **time-consuming**, and often slowed down development cycles.
- **Fragile Tests**: Tests that relied on external systems or full-stack validations frequently broke due to **environmental inconsistencies**.
- **High Maintenance Costs**: Maintaining end-to-end tests was **expensive** and required **specialized skills**, making the process impractical for agile teams focused on **continuous delivery**.

The **Agile Manifesto** (2001) and the rise of **Extreme Programming (XP)** emphasized **fast feedback**, **continuous integration**, and **automated testing** as core principles. This shift called for **structured testing strategies** to support iterative development.

---

[![](https://substackcdn.com/image/fetch/$s_!-F1T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb37cd4a-48c3-4e62-a69d-fbfd440cf46b_2406x1696.png)](https://substackcdn.com/image/fetch/$s_!-F1T!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb37cd4a-48c3-4e62-a69d-fbfd440cf46b_2406x1696.png)

**Focus:**

- Emphasizes a **layered approach** to testing, prioritizing **unit tests** at the base, **integration tests** in the middle, and a **small set of end-to-end tests** at the top.
- Focuses on **speed, reliability, and cost-effectiveness** by reducing dependence on **slow and fragile tests**.

> "The Test Pyramid visualizes how to create a balanced and maintainable test suite that prioritizes fast feedback loops." – Mike Cohn, Succeeding with Agile.

**Levels:**

- **Unit Tests:** They comply with the FIRST principles.
- **Integration Tests:** Verify interactions between components, services or systems.
- **End-to-End Tests:** Validate entire workflows across systems.

*My Honest Opinion: I believe that in the book, the author was referring to broader integration testing when discussing integration tests.*

**Application:**

- Ideal for **monolithic systems**.

**Critique:**

- **Advantages:**
	- **Fast feedback**: Unit tests provide immediate validation.
	- **Cost-effective**: Fewer dependencies reduce maintenance costs.
	- **Maintainability**: Clear separation between layers ensures scalable test suites.
	- Allows you to pivot to any other testing strategy.
- **Disadvantages:**
	- **Limited for distributed systems**: Focuses on monoliths and may lack coverage for **systems** that would require **contract testing**.
	- **False confidence**: Heavy reliance on **unit tests** can overlook **integration issues**, leading to deployment failures.
	- **Fragility at the top**: End-to-end tests are **brittle**, expensive, and slow to execute.

## Testing diamond

### Historical context

The **Testing Diamond** emerged as an alternative to the **Test Pyramid** in response to the evolving needs of modern software architectures, particularly **microservices** and **distributed systems**. While the **Test Pyramid** prioritized **unit tests** at the base and minimized **end-to-end tests**, the **Testing Diamond** emphasizes the importance of **integration tests** as the foundation, reflecting the complexity of modern systems that depend on multiple interacting services.

The **Testing Diamond** gained attention in the early 2010s as teams building **service-oriented architectures (SOA)** and **microservices** realized that focusing too heavily on **unit tests** left gaps in testing **interactions between components**. This gap often resulted in **false confidence**, where isolated components appeared to work correctly, but their integration failed.

---

[![](https://substackcdn.com/image/fetch/$s_!68cm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcf9d02a-f752-48f1-a7d8-e0ac5fce1d69_1928x1682.png)](https://substackcdn.com/image/fetch/$s_!68cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcf9d02a-f752-48f1-a7d8-e0ac5fce1d69_1928x1682.png)

**Focus:**

- Prioritizes **integration tests** as the most critical layer, followed by **unit tests** and **end-to-end tests**.
- Recognizes the **interconnected nature** of modern architectures and aims to validate **real-world interactions** between components and services.
- Balances **realistic testing** with **speed and cost-effectiveness**, focusing on **contract tests** and **component tests** to verify system interactions.

**Levels:**

- **Unit Tests:** They comply with the FIRST principles.
- **Integration Tests:** Validates **interactions between components** and services, often including **contract tests**.
- **End-to-End Tests:** Verifying functionality and user interactions.

*My Honest Opinion: This testing strategy introduced and utilized both narrow and broad integration testing approaches.*

**Application:**

- Best suited for **distributed systems**, **microservices**, **legacy systems**, and **API-first architectures**.
- Integrates seamlessly with **DevOps pipelines**, using **integration tests** to detect issues early in development.
- Enables effective **contract testing** to verify service compatibility.

**Critique:**

- **Advantages:**
	- **Better coverage for distributed systems**: Validates service integration effectively, reducing production failures.
	- **Focuses on contracts**: Verifies **API interactions** and service boundaries, minimizing risks in **service dependencies**.
	- **Balances speed and realism**: Provides quicker feedback than end-to-end tests while maintaining realistic interactions.
	- **Adaptable to modern architectures**: Aligns with **DevOps** practices and strengthens **CI/CD pipelines**.
	- Allows you to pivot to any other testing strategy.
- **Disadvantages:**
	- **Higher infrastructure costs**: Managing **containerized environments** and mock servers increases complexity.
	- **Slower than unit tests**: Additional setup and teardown time can impact feedback cycles.
	- **Over-reliance on integration tests**: May lead to neglecting **unit tests**, resulting in gaps in **code-level coverage**.
	- **Complexity in contract maintenance**: Frequent **API contract** updates create potential bottlenecks as services evolve.

## Testing trophy

### **Historical Context**

The **Testing Trophy** is a modern testing strategy popularized by **Kent C. Dodds** in 2018 through his blog post, *["The Testing Trophy and Testing Classifications"](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)*. He later expanded on this concept in his 2019 talk, *["Write Tests. Not Too Many. Mostly Integration"](https://youtu.be/Fha2bVoC8SE)*.

Dodds developed this strategy as a direct response to the limitations of the **Test Pyramid**. He argued that the pyramid's heavy emphasis on **unit tests** created **false confidence** by isolating logic instead of validating **real-world scenarios**.

Key influences that shaped the **Testing Trophy** include:

- **Guillermo Rauch's Tweet (2016):**
	- "Write tests. Not too many. Mostly integration." – *Guillermo Rauch*
	- This concise statement challenged the **Test Pyramid** approach and became the cornerstone of Dodds' strategy.
- **Modern Web Frameworks:** The emergence of **React**, **Angular**, and other **frontend-heavy frameworks** demanded testing strategies that prioritized **UI interactions** and **state transitions**, revealing the limitations of **unit-test-heavy approaches**.
- **Tooling Evolution:** New tools like **Jest**, **React Testing Library**, **Cypress**, and **Playwright** simplified **integration testing**, reducing the need for **mocks** while enabling more **realistic tests**.
- **Static Analysis Growth:** Advanced tools like **TypeScript** and **ESLint** reduced the need for **low-level validation tests**, encouraging developers to adopt **higher-level testing approaches**.

---

[![](https://substackcdn.com/image/fetch/$s_!fB1U!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69aef123-f448-4cad-aaec-b0eb74894d1a_1387x1782.png)](https://substackcdn.com/image/fetch/$s_!fB1U!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69aef123-f448-4cad-aaec-b0eb74894d1a_1387x1782.png)

**Focus:**

The **Testing Trophy** prioritizes **integration tests** as the foundation for confidence, complemented by **static analysis**, **unit tests**, and **end-to-end tests**.

Key principles include:

- **Confidence Over Isolation** – Focuses on **behavioral testing** instead of isolating components excessively.
- **Minimizing Mocks** – Reduces reliance on **test doubles** to avoid **fragile tests** disconnected from real behavior.
- **Cost and Efficiency** – Balances **fast execution** and **real-world reliability** without over-relying on costly tests.

> "Write tests. Not too many. Mostly integration." – Guillermo Rauch, 2016

*> "Focus on tests that minimize mocking and maximize confidence in user-facing behavior." – Kent C. Dodds, 2018*

**Levels:**

- **Static analysis:** Linting, type checks, and formatting tools.
- **Unit Tests:** Fast and isolated tests for individual methods.
- **Integration Tests (Main focus):** Critical focus, testing workflows, and APIs.
- **End-to-End Tests:** Final checks for UI and critical flows.

From my understanding, the author talks about narrow social tests, mainly.

> Integration tests are those which test multiple units integrating with one another. *– Kent C. Dodds*

**Application:**

The **Testing Trophy** suits **modern frontend applications**, **API-driven architectures**, and **microservices** requiring higher **integration reliability**.

**Use Cases:**

- **Frontend Development:** Focuses on **state transitions**, **UI rendering**, and **event flows** in frameworks like **React**.
- **API Testing:** Combines **integration tests** with **contract testing tools** like **Pact** and **WireMock**.
- **Microservices:** Prioritizes **contract tests** and **service-level validations** over **end-to-end tests**.

**Critique:**

- **Advantages:**
	- **Balanced Testing Layers:** Prioritizes **integration tests**, balancing **cost**, **speed**, and **real-world reliability**.
	- **Less Fragile Tests:** Reduces reliance on **mocks**, focusing on **behavioral testing** instead of isolated logic.
	- **Adaptable for Modern Systems:** Works well for **distributed systems**, **frontend-heavy applications**, and **APIs**.
	- Allows you to pivot to any other testing strategy.
- **Disadvantages:**
	- **Debugging Complexity:** **Integration test failures** are often **harder to debug** due to **dependencies**.
	- **Edge Case Coverage:** Reduces **unit testing**, which may lead to **missed edge cases** and **algorithm errors**.
	- **Contract Testing Gaps:** Lacks explicit focus on **contract testing**, which is crucial for **microservices**.
	- **Learning Curve:** Developers accustomed to **unit-test-first approaches** may struggle to **transition** to **integration-first strategies**.

## Honeycomb

### Historical context

The **Testing Honeycomb** emerged in response to challenges posed by **microservices architectures** that traditional strategies, like the **Test Pyramid**, couldn't adequately address. Microservices introduce **distributed dependencies**, where services must communicate over networks, handle failures gracefully, and evolve independently. This complexity highlighted the need for **focused integration tests** to validate service interactions while reducing reliance on **integrated tests**, which are often brittle and hard to maintain.

### The Evolution of Testing Strategies

- **Unit Tests Dominance (Test Pyramid Era)**: The **Test Pyramid** approach emphasized **unit tests** as the foundation for test coverage. These tests provided **fast**, **reliable** validation of isolated code behavior. However, in **distributed systems**, critical bugs emerged from **inter-service communication issues** that unit tests couldn't detect.
- **Integrated Tests Surge**: To validate **real-world behavior**, teams shifted toward **integrated tests** that examined services working together. Though this approach improved system behavior confidence, it introduced **fragility** through external dependencies, resulting in slower execution, **false positives**, and **environmental inconsistencies**.
- **Emergence of the Honeycomb Approach**: Spotify introduced the **Testing Honeycomb** to strike a balance between **integration tests** and **implementation detail tests**, while minimizing fragile **integrated tests**. This strategy recognizes that **interactions between services**, rather than individual components, present the main complexity—and adapts testing practices accordingly.

---

[![](https://substackcdn.com/image/fetch/$s_!JYA_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fb83c0f-638d-416f-a946-a0a9f9fa0a9c_1529x1675.png)](https://substackcdn.com/image/fetch/$s_!JYA_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7fb83c0f-638d-416f-a946-a0a9f9fa0a9c_1529x1675.png)

**Focus:**

- Designed for **microservices** and **distributed systems**. Prioritizes **integrated tests** to ensure services interact reliably.

**Levels:**

- **Integration Tests:** Verify the correctness of a service in isolation by focusing on explicit interaction points, such as APIs or messaging interfaces, often using in-memory databases or mock services to simulate dependencies.
- **Implementation Detail Tests:**
	- Validate **specific internal logic** within a service that is **not covered** by integration tests.
	- Often focuses on **business rules**, **algorithms**, or **utility methods** critical to the service.
- **Integrated Tests:** Test **multiple services** interacting with **real dependencies** (databases, APIs, etc.) as they would in production.

**Application:**

- **Microservices and APIs**:
	- Validates **service compatibility** without needing **live dependencies**.
	- Enables smooth testing during **parallel development** of services.
- **DevOps and CI/CD Pipelines**:
	- Delivers **fast feedback loops** by reducing reliance on slow integrated tests.
	- Integrates naturally into **automated deployment workflows**.
- **Legacy System Migrations**:
	- Enables teams to confidently **refactor internal logic** while maintaining **external contracts**.

**Critique:**

- **Advantages:**
	- **Focus on interactions:** targets testing at the key points of complexity in microservices.
	- **Faster feedback loops:** well-designed integration tests prevent development bottlenecks.
	- **Resilient and scalable:** adapts to evolving architectures without relying on end-to-end tests.
	- **Simplifies contract testing:** maintains **API compatibility** across service changes.
	- **Improved maintainability:** reduces brittle, high-maintenance test suites.
- **Disadvantages:**
	- **Internal coverage gaps:** limited implementation testing may miss critical **business logic** errors.
	- **Setup complexity:** integration tests often require sophisticated **mock services** or **test containers**.
	- **Knowledge overhead:** teams need expertise in specialized tools like **Pact**, **TestContainers**, or **WireMock**.
	- **Dependency drift:** mock responses can diverge from actual service behavior, requiring ongoing **contract synchronization**.
	- Bad feedback from failing test.
	- Rename the types of tests when they still do the same
		- Integrated = Broad integration test
		- Implementation details = Unit (sociable or Solitary)
	- High complexity in the testing environments.

---

## Key Takeaways

A **Testing Strategy** ensures clarity, consistency, and confidence in software testing efforts. By defining **what to test, how to test, and why to test**, it helps teams:

- Deliver **stable and reliable software**.
- Adapt quickly to **changing requirements**.
- Scale testing as systems grows in complexity.

## Conclusion

Testing strategies exist to create **confidence in software delivery**, ensuring teams focus not only on meeting requirements but also on **maintainability** and **future scalability**. A well-defined strategy aligns with **business goals** while enabling teams to evolve systems through **iterative testing** and **continuous feedback**.

Using **sensible defaults**, like prioritizing automated tests, incorporating risk assessments, and integrating testing into CI/CD pipelines, can make strategies **practical and adaptable** for modern software development.

I've noticed many people trying to create their structural diagrams, whether pyramids, diamonds, or other shapes, to represent their testing strategy. However, the original testing pyramid and its manual testing component were simply meant to illustrate test quantities and facilitate discussions about different test types and their cost.

[![Imagen](https://substackcdn.com/image/fetch/$s_!SKRS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2e640d5-59d7-473f-8a4a-02dcfaaf622c_951x558.png)](https://substackcdn.com/image/fetch/$s_!SKRS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2e640d5-59d7-473f-8a4a-02dcfaaf622c_951x558.png)

Representing testing strategies through geometric shapes often becomes unnecessarily complex and confusing. As a result, these shapes aren't effective tools for communicating our intended message, suggesting we should consider alternative visualization formats.

[![](https://substackcdn.com/image/fetch/$s_!Vk8P!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54fe4f69-cc77-4662-815f-22b599740fa3_17356x7645.png)](https://substackcdn.com/image/fetch/$s_!Vk8P!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54fe4f69-cc77-4662-815f-22b599740fa3_17356x7645.png)

*Disclaimer: This is an example and should not be taken as a definitive test plan.*

Through this definition of testing strategy and example, we can understand the importance of test types, their appropriate usage, and timing.

This image helps us establish sensible defaults and address a crucial yet often overlooked topic when discussing geometric testing models: "What are our test boundaries?" and "When should we use solitary versus sociable tests?" This structure facilitates meaningful discussions about essential testing concepts, moving beyond simple comparisons of which approach is superior or justifying one method over another.

Dave Farley shows a similar example in his video [Testing Strategy for DevOps: What to test and When](https://youtu.be/z-3aSVfoyBY?si=Lq2nyV2naAYTV5Lm).

This is how I usually achieve this, through 3 sessions:

- In the first one, we gathered the entire technical team, split them into small groups, and asked them to draw the current architecture from their perspective. After a while, we bring everyone together and have them discuss whether they agree or not. Usually, in well-oiled or cohesive teams, this tends to be quite quick. If that's not the case, we give them more time and open discussions about why some see it one way and others another way, trying to reach a middle ground where everyone feels comfortable. This helps make future communication more fluid and ensures we're all on the same page regarding terminology.
	- **Outcome**: get an architecture diagram and a common understanding of the architecture.
- In the second session, we gather the technical team again, separate them, and have them design what they believe are their current test boundaries. Once all teams finish, we come together, share our findings, evaluate which approach the team feels most comfortable and confident with, and then we begin discussing the current state of the code and what our priority should be for the current strategy, as well as starting to consider where we want to go. It's in this session where we create the image we saw earlier.
	- Outcome:
		- Have clear the boundaries of our test currently and the responsibility of each type of test.
		- Have a clear view of What, When, and Where we are going to test the things we need to test.

[![](https://substackcdn.com/image/fetch/$s_!pLWm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc16db32c-3718-4c28-99b7-d29b346ff828_9728x5036.jpeg)](https://substackcdn.com/image/fetch/$s_!pLWm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc16db32c-3718-4c28-99b7-d29b346ff828_9728x5036.jpeg)

*This is an example of how the boundaries should look like after the session*

- In the final session (only held if it makes sense), we discuss the north star of where we'd like to take our testing strategy, why, and how we're going to do it. From this session emerge the initiatives that will help us migrate the current strategy, taking into account alignment with both product strategy and technical strategy.
- Outcome: Migration plan and initiatives to move forward.

Testing strategies are not just procedural frameworks; they are the foundation for **confidence in software delivery**. Confidence means more than ensuring code correctness; it's about knowing that software will behave **predictably in production**, scale with **business growth**, and remain **maintainable** over time.

## Offtopic

If you look at the Diamon, the trophy, and the Honeycomb, you would see that if you remove the static analysis from the trophy, that from our definition of test, does not match, because a test exercises a behavior, the static analysis is not “exercising “ any behavior. They are the same, the only conversation is about what the tests are exercising.

---

## **7. References**

- **Mike Cohn (2009):** *Succeeding with Agile*.
- **Kent C. Dodds (2018):** *The Testing Trophy*.
- **Spotify Engineering (2021):** *Honeycomb Testing Strategy*.
- **Martin Fowler (2001):** *Continuous Integration*.
- **Kent Beck (2003):** *TDD by Example*.
- **Lisa Crispin &amp; Janet Gregory (2009):** *Agile Testing*.
- **Gerard Meszaros (2007):** *xUnit Test Patterns*.
- **Dodds, Kent C.**: *The Testing Trophy and Testing Classifications*. [kentcdodds.com](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications).
- **Dodds, Kent C.**: *Write Tests. Not Too Many. Mostly Integration.* [YouTube](https://youtu.be/Fha2bVoC8SE).
- **Fowler, Martin**: *The Practical Test Pyramid*. [martinfowler.com](https://martinfowler.com/articles/practical-test-pyramid.html).
- **Fowler, Martin**: *Test Shapes*. [martinfowler.com](https://martinfowler.com/articles/2021-test-shapes.html).
- **Bray, Tim**. *"Testing in 2021."* ([tbray.org](https://www.tbray.org/ongoing/When/202x/2021/05/15/Testing-in-2021)).
- **Farley, Dave**. *[Testing Strategy for DevOps: What to test and When](https://youtu.be/z-3aSVfoyBY?si=Lq2nyV2naAYTV5Lm)*.
- **Schaffer, A**. (2018). *Testing of Microservices*. [engineering.atspotify.com](https://engineering.atspotify.com/2018/01/testing-of-microservices/)

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
