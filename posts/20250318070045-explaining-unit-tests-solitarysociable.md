---
title: "Explaining Unit Tests Solitary/Sociable and Integration Tests Narrow/Broad "
requested_url: "https://emmanuelvalverderamos.substack.com/p/explaining-unit-tests-solitarysociable"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/explaining-unit-tests-solitarysociable"
substack_post_id: 152612051
retrieved_at: "2026-03-13T08:35:09.353Z"
---
# Explaining Unit Tests Solitary/Sociable and Integration Tests Narrow/Broad

[![](https://substackcdn.com/image/fetch/$s_!enhx!,w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5bb0a6d-8b27-4895-9411-adf21115888e_444x250.gif)](https://substackcdn.com/image/fetch/$s_!enhx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5bb0a6d-8b27-4895-9411-adf21115888e_444x250.gif)

Testing terms like unit tests and integration tests and their nuances are often misused or overlap, creating confusion. By clearly defining and understanding their boundaries, we can better align on a testing strategy. This article clarifies these distinctions by focusing on the boundaries of the Subject Under Test (SUT) across different test types.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

# Unit tests: solitary vs. sociable

[![](https://substackcdn.com/image/fetch/$s_!giNn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a17ad17-cb27-4acf-9add-d707323d77e4_10060x8808.png)](https://substackcdn.com/image/fetch/$s_!giNn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a17ad17-cb27-4acf-9add-d707323d77e4_10060x8808.png)

**Unit tests** typically refer to isolated tests that check a specific function or method, focusing on one component at a time. But what exactly constitutes a "unit"? This is where nuance comes in. The **solitary** versus **sociable** approaches represent different philosophies about what makes a unit.

- **Solitary Unit Tests**: These tests use test doubles for all external interactions, completely isolating the unit. Think of it like testing one gear while replacing all other gears with test doubles. This approach keeps the focus purely on the target code, eliminating external noise. The goal is to validate the business logic of the SUT in isolation, ensuring its correctness without testing irrelevant aspects, and verifying only the contracts of its collaborators when needed (where contracts are the public APIs of dependencies). **Samman Coaching properties alignment**: According to **Emily Bache**, unit tests should have properties like isolation, repeatability, fast feedback, and clarity. **Solitary unit tests** align perfectly with these properties by isolating the unit under test from external dependencies, enabling faster and more deterministic feedback. This strict isolation reduces developers' cognitive load by focusing solely on the SUT's behavior, ensuring clarity. Solitary unit tests go beyond mere isolation—they foster disciplined habits that promote excellent software design. By requiring mocked and isolated dependencies, developers must focus on a unit's core functionality without distractions.

The fundamental distinction between solitary and sociable unit tests lies in the **boundary** **of the SUT**. Solitary unit tests maintain a strict boundary around the target logic, treating all else as external dependencies that must be mocked. Sociable unit tests, however, extend this boundary to include nearby, lightweight collaborators, offering a more realistic context while staying short of full integration testing.

[![](https://substackcdn.com/image/fetch/$s_!iYd5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3288c07a-8bdd-4226-bbcf-29786085f79e_8488x4008.png)](https://substackcdn.com/image/fetch/$s_!iYd5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3288c07a-8bdd-4226-bbcf-29786085f79e_8488x4008.png)

- **Sociable Unit Tests**: In contrast, sociable unit tests allow the unit to interact with its real, lighter collaborators. This might mean testing a repository interacting with an in-memory database. The aim is to keep the interactions realistic while focusing on the core functionality. Sociable tests can make it easier to understand how units work together without using test doubles for everything. The SUT in this context is tested along with its close collaborators to ensure that interactions are realistic.
**	Emily Bache's** article highlights that while sociable unit tests may lack the strict isolation property, they gain the advantage of realistic collaboration. This means these tests are better suited for verifying that integration points and shared logic work as expected, particularly in the context of ensuring that lightweight components interact correctly without full integration testing overhead.

[![](https://substackcdn.com/image/fetch/$s_!m8Sp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce9e4995-c313-4d67-a9e5-6f2652f8a5ce_6906x4008.png)](https://substackcdn.com/image/fetch/$s_!m8Sp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce9e4995-c313-4d67-a9e5-6f2652f8a5ce_6906x4008.png)

However, **sociable unit tests **often resemble integration tests, tests, because they involve real collaborators. as well as **solitary tests**, look a lot like **narrow integration tests** because they isolate the collaborators. Here’s where the ambiguity sets in. 🤯

### My personal view on this

[![](https://substackcdn.com/image/fetch/$s_!lMBu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e0022f3-9a5f-48ca-a459-509ae018e49a_12846x3191.png)](https://substackcdn.com/image/fetch/$s_!lMBu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e0022f3-9a5f-48ca-a459-509ae018e49a_12846x3191.png)

# Integration tests: narrow vs. broad

---

### Historical context

The term "integration test" has been around for a long time. Initially, it referred to tests that integrated systems, where you needed replicas of your production systems to perform these tests. This was more expensive but ensured proper integration and communication with external systems. As Martin Fowler notes in his article about integration testing, around 2010 he began to see a different type of integration test: the ones we'll present here as "narrow" integration tests. This is interesting; from my perspective, one of the precursors of this change might have been the book "Growing Object-Oriented Software, Guided by Tests," though this is just my perception. What is clear is that the definition of "integration test" can vary depending on who is conveying the message and when and where they learned the concept.

---

Integration tests are complex to understand because the term is **polysemic**—it carries multiple interpretations that often create confusion within teams. Let's examine each meaning:

[![](https://substackcdn.com/image/fetch/$s_!xo7_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb832fc3c-900c-4a62-9c52-4f839a98ee96_12008x6216.png)](https://substackcdn.com/image/fetch/$s_!xo7_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb832fc3c-900c-4a62-9c52-4f839a98ee96_12008x6216.png)

- **Narrow integration tests**: These tests focus on the interactions between a few closely related components, such as a controller and a repository. It's like checking whether a small set of gears mesh smoothly. **Valentina Jemuović** underscores the importance of narrow integration tests to verify both **presentation and infrastructure behavior** without involving the whole system. They often resemble **solitary unit tests** but are distinct in that they deliberately cross unit boundaries. In narrow integration tests, the boundary of the SUT expands just enough to validate collaboration between key components, but not so far as to require entire subsystems or infrastructure elements. Defining this precise boundary allows these tests to be effective without the brittleness and overhead often seen in broader integration tests. Narrow integration tests are also used to verify integrations between classes by doubling external dependencies (like file systems or databases), ensuring that contracts with external systems work correctly without actually calling those systems.
**	Martin Fowler** defines them like this:
- Exercise only that portion of the code in my service that talks to a separate service
- Uses test doubles of those services, either in process or remote
- Thus consists of many narrowly scoped tests, **often no larger in scope than a unit test** (and usually run with the same test framework that's used for unit tests)
- **Broad integration tests**: These validate larger interactions, subsystems, or even full systems. While valuable for ensuring components work together properly, they are **slower**, more **fragile**, and harder to debug. The SUT in broad integration tests typically encompasses a major subsystem or the entire application, involving testing between different systems such as external applications, databases, and other components. Building a comprehensive integration test suite requires careful thought and planning. It represents an investment in system maintainability and reliability that reduces defects and rework in the long run.
**	Martin Fowler** defines them like this:
	- Require live versions of all services, requiring substantial test environment and network access
	- Exercise code paths through all services, not just code responsible for interactions

> If your only integration tests are broad ones, you should consider exploring the narrow style, as it's likely to significantly improve your testing speed, ease of use, and resiliency. Since narrow integration tests are limited in scope, they often run very fast, so can run in early stages of a [DeploymentPipeline](https://martinfowler.com/bliki/DeploymentPipeline.html), providing faster feedback should they go red.
> - Martin Fowler

# Contract tests

Beyond unit and integration tests, contract tests play a crucial role in validating system behavior.

- **Contract Tests**: These specialized integration tests ensure that services agree on their interactions, particularly in **consumer-driven contracts**. Contract tests are essential when working with external services, as they allow services to evolve independently while maintaining integration correctness. The SUT in contract tests focuses on the communication layer or API contract between services.

# Solitary unit tests vs. narrow integration tests: a crucial distinction

> As if this terminological confusion isn't enough, things have worsened in the late 2010s with yet another usage of “integration test”. This comes from a divergence in the meaning of [Unit Test](https://martinfowler.com/bliki/UnitTest.html). Some people define unit test to be what I refer to as a solitary unit test, one where all program elements other than the one under test are replaced with test doubles. Given this narrow definition some writers defining “integration test” to mean sociable unit tests
> - Martin Fowler

The distinction between **solitary unit tests** and **narrow integration tests** is one of the most significant yet commonly misunderstood aspects of testing. Understanding this difference can profoundly impact how teams structure their testing strategy and maintain code quality.

- **Solitary Unit Tests**: These tests isolate individual units by using test doubles for all external dependencies. They focus on the smallest pieces of logic without interference from other components. Solitary unit tests are fast, reliable, and provide rapid feedback about specific logic. By ensuring no external behavior affects the outcome, they remain precise and easier to diagnose when they fail. The SUT is purely the unit itself, isolated from all dependencies, focusing solely on core business logic. **Samman Coaching Properties Alignment**: As noted by **Emily Bache**, solitary unit tests excel at providing fast feedback and isolation—crucial properties for detecting issues in the smallest units of code quickly and reliably.
- **Narrow Integration Tests**: These tests validate how a small number of related components interact. They cross unit boundaries to test real interactions between components, such as a controller working with a repository. While they use test doubles for external dependencies (like databases or file systems), they test real implementations of internal collaborators. This approach provides a more realistic assessment of system behavior while keeping tests manageable. The SUT encompasses both the primary unit and its key collaborators, ensuring they work together as intended.

This distinction is crucial because it defines the **scope and intent** of each test type. **Solitary unit tests** validate logic in **isolation**, while **narrow integration tests** verify **collaboration** between components. Misunderstanding these differences can lead to over-reliance on one type, potentially missing critical issues or creating brittle tests.

Notice how **narrow integration tests** can appear similar to **solitary unit tests**? Though both involve testing interactions, their **purpose** differs:

- **Unit Tests** aim to validate business logic.
- **Integration Tests** validate connections between components.

The key difference between solitary unit tests and narrow integration tests lies in the **System Under Test (SUT)** and its **size/scope**.

Here's a comparative table between **Solitary Unit Tests** and **Narrow Integration Tests**:

[![](https://substackcdn.com/image/fetch/$s_!J5bJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f66e772-1df2-467c-a792-c2371d4914da_5096x1056.png)](https://substackcdn.com/image/fetch/$s_!J5bJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f66e772-1df2-467c-a792-c2371d4914da_5096x1056.png)

When teams misunderstand these boundaries, they often rely too heavily on broad integration tests. These tests are slower to run, more difficult to debug, and provide less specific feedback. By clearly defining the SUT boundary, we can minimize our dependence on broad tests and create a more targeted, efficient testing strategy.

# The Polysemy and semantic diffusion

Terms like **unit test** and **integration test** have multiple meanings—they signify different things to different people. This phenomenon, called **semantic diffusion**, happens when definitions become blurred as people apply these terms across various contexts. For instance, one person might consider a "unit test" to be a **solitary** test using test doubles, while another sees it as testing with **real collaborators**.

This **[semantic diffusion](https://martinfowler.com/bliki/SemanticDiffusion.html)** leads to misunderstandings, inconsistent practices, and team frustration. Martin Fowler explores this challenge extensively, noting how proper alignment prevents chaos in testing strategy.

To combat semantic diffusion, teams should clearly define the boundaries of the SUT for each test type. This clear communication ensures everyone shares the same understanding and aligns their testing practices accordingly.

## Aligning on definitions: reducing cognitive load

Before implementing a testing strategy, teams must **align on key definitions**:

- **What constitutes a unit?** Is it a method, a class, or something broader?
- **What is integration?** Does it mean testing with real databases or just internal dependencies?
- **Which dependencies are real, and which are test doubles?**

Clear alignment on these points reduces **cognitive load** and improves clarity. Without shared definitions, test suites can devolve into a confusing mix of solitary, sociable, narrow, and broad tests lacking a clear purpose.

**Valentina Jemuović's** article exemplifies the kind of discussions teams should have, as she clearly explains her terminology and reasoning.

Her **New Test Pyramid** offers a refined approach emphasizing **contract tests**, **component tests**, and **narrow integration tests**—focusing on meaningful interactions to minimize fragility.

In her framework, **contract tests** verify communication between components, **component tests** validate internal system behaviors, and **narrow integration tests** check presentation and infrastructure logic while limiting integration scope. This approach reduces reliance on broad integration tests, minimizing the fragility of highly coupled components and slow, broad-scoped tests.

Valentina's methodology shows how contract tests ensure reliable service communication, while component tests focus on internal behavior verification. By concentrating on specific system parts, narrow integration tests reduce the brittleness of broad integration testing, resulting in fewer false positives and refactoring failures. This approach provides greater confidence in delivery through thorough component testing.

[Her article clearly defines each test type](https://journal.optivem.com/p/new-test-pyramid), facilitating better communication and establishing common ground. When agreement isn't possible, the recommended approach is to **[disagree and commit](https://en.wikipedia.org/wiki/Disagree_and_commit)**, with the option to revisit the discussion later.

# Conclusion: testing is about communication

> All this is why I’m wary with “integration test”. When I read it, I look for more context so I know which kind the author really means. If I talk about broad integration tests, I prefer to use “system test” or “end-to-end test”. I don’t have any better name for narrow integration tests, so I do use that (but with “narrow” to help signal to the reader the nature of these tests). I continue to use “unit test” for both kinds, using solitary/sociable when I need to make a distinction.
> - Martin Fowler

Testing isn't just a technical challenge, it's a communication challenge. Misaligned definitions of testing terms create chaotic test suites that are slow, fragile, or overly dependent on test doubles.

The solution? **Agree on definitions**, use appropriate tools, and remember that testing is as much about **team alignment** as code quality. Clear definitions reduce cognitive load and create a cohesive strategy that helps build robust software efficiently.

The clearest path to effective testing lies in understanding and communicating the boundaries we set for our Subject Under Test. Whether it's a solitary unit or any other type of test, knowing these boundaries ensures we apply the right type of test, leading to efficient, reliable, and maintainable software.

### Team agreements, sensible defaults, and test planning

Creating effective testing strategies requires establishing **team agreements** and a shared understanding of what terms like "unit test," "integration test," and "narrow integration" mean in your context. These definitions form the foundation for effective collaboration.

Once these definitions are clear, apply **sensible defaults**—pre-defined, simple approaches for common tasks. These defaults aren't necessarily "best practices" but starting points that reduce friction and simplify everyday tasks. They provide a common foundation, letting team members focus on more complex challenges.

However, a strong testing strategy alone isn't enough. You also need a well-defined **testing plan**. The plan outlines **how and when** to execute tests, ensuring the right balance of **unit**, **integration**, **contract**, **acceptance tests**, and **E2E** throughout development. This maximizes coverage without burdening your CI/CD pipeline, ensuring higher confidence and reliability in delivery.

By establishing **team agreements**, embracing **sensible defaults**, and creating a clear **testing plan**, your team can work predictably and cohesively. This alignment reduces cognitive load, helps individuals make confident decisions, and lets everyone focus on meaningful progress.

If you previously chose to disagree and commit, you can now revisit those decisions and their trade-offs to evaluate alternatives and necessary changes.

As **Martin Fowler** argues, effective testing isn't about seeking approval—it's about maintaining clean code that can be continuously improved, emphasizing professional diligence and accountability. This applies to all purposeful tests, whether they're **solitary unit tests**, **sociable unit tests**, **narrow integration tests**, or **broad integration tests**.

### Testing decisions are trade-offs, not silver bullets

In software development, there are no silver bullets or universal solutions. Every decision, especially around testing, comes with trade-offs. A common challenge in testing discussions is expecting a one-size-fits-all rule. This mindset isn't just unrealistic—it's counterproductive. The key lies in understanding and managing trade-offs.

When reaching an agreement, start with these considerations:

- **The Subject Under Test (SUT):** Clearly defining the SUT helps understand its boundaries and the behaviors to validate. This understanding guides test type selection, whether using solitary unit tests, sociable unit tests, narrow integration tests, or broad integration tests.
- **Testing strategy and planning:** A well-thought-out testing strategy helps identify the right balance between test types. What mix of unit, integration, and contract tests will best support the codebase? What are each test type's limits? This planning ensures the testing suite supports development without becoming a bottleneck.
- **Kent Beck's&nbsp;*****Test desiderata*****:**&nbsp;The&nbsp;*Test desiderata*&nbsp;defines good test qualities: isolation, readability, determinism, speed, and predictability, among others. As tests grow more complex, moving from unit to integration tests, some properties diminish. For instance, broad integration tests often sacrifice&nbsp;**feedback speed**&nbsp;and&nbsp;**specificity**&nbsp;compared to unit tests. Understanding these trade-offs helps structure tests to minimize downsides and maximize utility.

For example, a broad integration test might provide system-wide confidence but takes longer to debug and may not pinpoint specific issues. A unit test, however, can fail quickly and clearly, offering more actionable feedback.

Finally, testing is a **team alignment activity**, not just a technical one. Document and agree on testing strategy decisions collaboratively. Consider formalizing this conversation in an **RFC (Request for Comments)**, **ADR (Architectural Decision Record)**, or **Concern Document**. These formats ensure clarity and help new team members quickly align with team definitions, strategies, and expectations.

By grounding testing discussions in context, trade-offs, and team collaboration, we create strategies that are technically sound and aligned with how teams work. This approach builds clarity, efficiency, and confidence across the team and codebase.

## References

- [Bernhardt, Gary.](https://youtu.be/yTkzNHF6rMs?si=qizoQt-dQAy_-Mnj)*[Boundaries](https://youtu.be/yTkzNHF6rMs?si=qizoQt-dQAy_-Mnj)*[.](https://youtu.be/yTkzNHF6rMs?si=qizoQt-dQAy_-Mnj)
- Fowler, Martin. *Unit Test*. [https://martinfowler.com/bliki/UnitTest.html](https://martinfowler.com/bliki/UnitTest.html)
- Fowler, Martin. *Integration Test*. [https://martinfowler.com/bliki/IntegrationTest.html](https://martinfowler.com/bliki/IntegrationTest.html)
- Fowler, Martin. *Semantic Diffusion*. [https://martinfowler.com/bliki/SemanticDiffusion.html](https://martinfowler.com/bliki/SemanticDiffusion.html)
- Fowler, Martin. *Mocks Aren't Stubs*. [https://martinfowler.com/articles/mocksArentStubs.html](https://martinfowler.com/articles/mocksArentStubs.html)
- Fowler, Martin. *Test Pyramid*. [https://martinfowler.com/bliki/TestPyramid.html](https://martinfowler.com/bliki/TestPyramid.html)
- [Jemuović, Valentina.](https://journal.optivem.com/p/new-test-pyramid)*[New Test Pyramid](https://journal.optivem.com/p/new-test-pyramid)*[.](https://journal.optivem.com/p/new-test-pyramid)
- [Rainsberger, J.B.](https://youtu.be/7XI3H_rKmRU)*[Integrated Tests Are a Scam](https://youtu.be/7XI3H_rKmRU)*[.](https://youtu.be/7XI3H_rKmRU)
- Beck, Kent. *Test Desiderata*
	[https://testdesiderata.com/](https://testdesiderata.com/)
- Khorikov, Vladimir. *Unit Testing Principles, Practices, and Patterns*.
- Bache, Emily. "Styles of Unit Tests. [https://sammancoaching.org/learning_hours/test_design/styles_of_unit_tests.html](https://sammancoaching.org/learning_hours/test_design/styles_of_unit_tests.html)
- Disagree and commit. [https://en.wikipedia.org/wiki/Disagree_and_commit](https://en.wikipedia.org/wiki/Disagree_and_commit)
- Thirion, Yoan. *Some of the graphic references in the article*. [https://yoan-thirion.gitbook.io/knowledge-base/xtrem-reading/my-book-infographics](https://yoan-thirion.gitbook.io/knowledge-base/xtrem-reading/my-book-infographics)
