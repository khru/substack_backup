---
title: "Acceptance Testing: More Than Tests, Executable Specifications"
requested_url: "https://emmanuelvalverderamos.substack.com/p/acceptance-testing-more-than-tests"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/acceptance-testing-more-than-tests"
substack_post_id: 160772733
retrieved_at: "2026-03-10T08:36:08.304Z"
---
# Acceptance Testing: More Than Tests, Executable Specifications

### Introduction: When Do You Know Your Software Is Ready?

> “All unit tests were passing... but the user couldn’t even register.”

This isn’t a rare story. You might have a flawless technical test suite, great code coverage, and well-isolated unit tests, and yet still fail to deliver *actual* value.

Why?
Because correctness at the *code level* is not the same as *business correctness*. A system can be technically sound and still not meet the expectations of the people who use it.

> “The biggest cause of failed software is not bugs. It’s misaligned expectations.”
> — *Paraphrased from Gojko Adzic, Specification by Example*

At its core, testing isn’t just a technical safety net. It’s a communication strategy. Tests should act as **unambiguous conversations between stakeholders and the system**. That’s why *acceptance tests* are essential.

**Acceptance testing is not about testing after the fact.**
It’s about clearly defining what the system should do *before* implementation, using language and examples that both business and developers understand.

These tests are:

- **Executable specifications** that validate *observable* system behaviors.
- Written in a **shared language** that everyone on the team: devs, designers, product owners, can understand.
- A bridge between **intention and implementation**.

> “Acceptance tests are not tests. They are unambiguous, automated conversations between people and software.”
> - *Gojko Adzic*

Too often, developers rely on low-level tests, verifying function outputs, mocking dependencies, asserting method calls. But these rarely validate that the system actually works from a user’s point of view.

> “You can have 100% code coverage and still deploy broken software.”
> - *Dave Farley*

That’s why we need acceptance tests: to confirm that the system behaves as expected *in the ways that actually matter*, to the business, to the user, to the product.

This is not optional: quality is a developer’s responsibility.


Testing *is* software design. It’s part of our job to build the right thing, not just build it right.

In this article, we’ll explore:

- What acceptance tests really are (and are not)
- How they differ from unit and integration tests
- How to structure them clearly and maintainably
- Common mistakes to avoid
- And how they can transform your design, communication, and delivery confidence

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### What Are Acceptance Tests, Really?

Acceptance tests are **automated, high-level examples that describe what the system should do from the perspective of a user or stakeholder**. Their goal is to validate that a **business requirement or functionality is fulfilled** in a way that’s observable and valuable to the end user.

> “An acceptance test doesn’t ask *how* something is implemented. It verifies that *what matters* to the business is actually happening.”
> - *Adapted from Gojko Adzic, Specification by Example*

They serve as **Executable Specifications**, meaning they don’t just describe behavior, they verify it in a reproducible, automated way. If you remove the automation, you still have a living specification. If you remove the clarity of intent, you're left with just brittle automation.

#### ✅ Key Characteristics:

- Written in the **language of the domain**, not in technical terms.
- Focus on **observable outcomes**, not internal logic or structures.
- Describe **what is expected**, not how it should be achieved.
- Can be **read by humans** and **executed by machines**.

#### 💡 Important Clarification:

**> Acceptance tests are not QA’s responsibility.**

They are the responsibility of the **development team**, because they define and verify **functional completeness**. Developers are responsible for **ensuring software quality** through tests that reflect what users care about, not just that “the code runs.”

> “Quality is not something we test for after development. It’s something we build into the system from the beginning.”
> - *Dave Farley*

### 🔄 Relationship to Functionality

A **functionality** is a unit of value. It might be described as a **user story**, a **feature**, or a **capability** of the system. Acceptance tests are the way we **validate that a functionality is done**, that it behaves correctly under expected conditions and edge cases.

> ✅ *A functionality is not “done” until its acceptance criteria are expressed as automated acceptance tests that pass.*

These tests should live close to the team, integrated in the delivery pipeline, and be treated as **first-class citizens**, at the same level as unit or integration tests.

### 🧭 Acceptance Test Scope and Boundaries

Acceptance tests **do not verify internal implementations**. They only validate behaviors that are meaningful to the user or stakeholder.

- ✅ Expected business behavior
- ✅ Functional acceptance criteria
- ✅ Interaction across modules or systems (at a behavioral level)
- ❌ Low-level validations
- ❌ Visual alignment (belongs to visual regression/UI snapshot tests)
- ❌ Data structure shape (unless it's part of a contract)

> "If the user wouldn’t notice it’s broken, it shouldn’t be in your acceptance test."

### Foundational Properties of Good Acceptance Tests

Acceptance tests are not generic assertions about code, they are focused validations of functional behavior, seen through the lens of the user. While they may take many forms depending on architecture (API-first, UI-driven, CLI, etc.), good acceptance tests tend to share a set of common properties that guide their effectiveness and intent.

These aren’t strict requirements, but heuristics, qualities we strive for to maximize confidence and clarity.

- 🧠 Behavior-oriented The test describes what the system does, not how it’s built. It's focused on verifying outcomes that matter to the user, not internal wiring.
> 	"You’re not testing your code. You’re testing your promises." — Dan North
- 🗣️ Expressed in ubiquitous language The scenario speaks the language of the domain: product, developers, business, all should recognize the terms used. Whether written in code or Gherkin, it should reflect shared understanding.
- 🎯 Scoped to one functionality An acceptance test should target a single user-facing functionality (or acceptance criterion). For instance, a test validating “edit a feature toggle” should not break due to issues in flag creation, those are validated elsewhere.
> 	“A test should fail for exactly one reason. Otherwise, your confidence is diluted, and your feedback is misleading.”
- 🧪 Fails meaningfully When a test fails, it should clearly indicate a broken behavior from the user’s perspective. It shouldn't fail due to incidental setup, infrastructure issues, or side concerns unrelated to the business rule being validated.
- 🪟 Try to be interface-conscious (not agnostic) While acceptance tests often exercise the system via its public interfaces (HTTP, CLI, UI), this isn’t always required. Sometimes it’s valid to interact with the system more directly (e.g., database insertions during setup), especially if the interface isn’t the subject of the behavior being tested.

	The interface only matters when it's part of the business value.
	Use the interface to express the intent of the functionality, not to define or constrain it unnecessarily.

	For example: If we want to test the edition of a feature flag through the API, it’s perfectly acceptable to create that feature directly in the database first. We’re not validating creation here, just edition. Avoid coupling multiple behaviors in the same test unless that's the behavior being described.

✅ Use the interface that reflects the behavior being specified. ❌ Don’t bind to UI or network calls unless they’re the focus.

### Acceptance Test Styles

Acceptance tests can vary in how they express behavior. The key tradeoff is between **readability**, **reusability**, and **coupling to implementation**. Let’s explore three common styles.

#### a. Without DSL (raw/technical style)

This is often the first step for many teams: writing tests directly against the HTTP layer or using raw browser drivers or test clients. Here’s a real-world example using Laravel’s testing API in PHP:

```php
#[Test]
public function should_return_an_empty_list_of_features(): void
{
    $this-&gt;json(
        method: Request::METHOD_GET,
        uri: '/feature-flags'
    );

    $this-&gt;assertResponseStatus(Response::HTTP_OK);
    self::assertCount(0, $this-&gt;response-&gt;json('data'));
}
```

- ✅ Fast to write, no abstraction needed.
- ✅ Makes HTTP intent clear.
- ❌ Still low-level: not using domain language ("empty list of features" is implicit).
- ❌ Harder to reuse and maintain at scale.

> ✨ *Note:* This is already a valid acceptance test, it checks observable behavior from the user’s perspective. However, it’s coupled to the technical API and lacks domain storytelling.

---

### b. Internal DSL (fluent, domain-oriented)

```php
interface BookStoreClient {
    public function searchForBook(string $title): void;
    public function selectBook(string $author): void;
    public function addToCart(): void;
    public function checkout(string $item): void;
    public function assertPurchase(string $item): void;
}
```

```php
class AmazonClient implements BookStoreClient
{
    public function __construct(
        private readonly string $baseUrl,
        private readonly ClientInterface $httpClient,
        private readonly RequestFactoryInterface $requestFactory,
        private readonly StreamFactoryInterface $streamFactory
    ) {}

    public function searchForBook(string $title): void
    {
        $uri = "{$this-&gt;baseUrl}/search?title=" . urlencode($title);
        $request = $this-&gt;requestFactory-&gt;createRequest('GET', $uri);
        $this-&gt;httpClient-&gt;sendRequest($request);
    }

    public function selectBook(string $author): void
    {
        $this-&gt;post("/select?author=" . urlencode($author));
    }

    public function addToCart(): void
    {
        $this-&gt;post('/cart/add');
    }

    public function checkout(string $item): void
    {
        $this-&gt;post('/checkout?item=' . urlencode($item));
    }

    public function assertPurchase(string $item): void
    {
        $request = $this-&gt;requestFactory
                        -&gt;createRequest('GET', "{$this-&gt;baseUrl}/purchases");
        $response = $this-&gt;httpClient-&gt;sendRequest($request);
        $body = (string) $response-&gt;getBody();

        if (strpos($body, $item) === false) {
            throw new \RuntimeException("Expected item not found: $item");
        }
    }

    private function post(string $path): void
    {
        $request = $this-&gt;requestFactory
                        -&gt;createRequest('POST', "{$this-&gt;baseUrl}{$path}");
        $request = $request-&gt;withBody($this-&gt;streamFactory-&gt;createStream(''));
        $this-&gt;httpClient-&gt;sendRequest($request);
    }
}
```

```php
class ShoppingDSL
{
    public function __construct(
        private readonly BookStoreClient $client
    ) {}

    public function searchForBook(string $title): void
    {
        $this-&gt;client-&gt;searchForBook($title);
    }

    public function selectBook(string $author): void
    {
        $this-&gt;client-&gt;selectBook($author);
    }

    public function addSelectedItemToShoppingBasket(): void
    {
        $this-&gt;client-&gt;addToCart();
    }

    public function checkOut(string $item): void
    {
        $this-&gt;client-&gt;checkout($item);
    }

    public function assertItemPurchased(string $item): void
    {
        $this-&gt;client-&gt;assertPurchase($item);
    }
}
```

```php
class EcommerceShouldTest extends TestCase
{
    private ShoppingDSL $shopping;

    protected function setUp(): void
    {
        $baseUrl = $_ENV['AMAZON_BASE_URL'];
        $psr17 = new Psr17Factory();
        $client = new AmazonClient(
            $baseUrl,
            new CurlClient(),
            $psr17,
            $psr17
        );

        $this-&gt;shopping = new ShoppingDSL($client);
    }

    public function test_should_buy_book_with_credit_card(): void
    {
        $this-&gt;shopping-&gt;searchForBook("Continuous Delivery");
        $this-&gt;shopping-&gt;selectBook("David Farley");
        $this-&gt;shopping-&gt;addSelectedItemToShoppingBasket();
        $this-&gt;shopping-&gt;checkOut("Continuous Delivery");

        $this-&gt;shopping-&gt;assertItemPurchased("Continuous Delivery");
    }
}
```

- ✅ Highly readable.
- ✅ Reusable.
- ✅ Expresses business-level intent clearly.
- ⚠️ Requires intentional design.

#### c. External DSL (Gherkin style)

```rust
Feature: Manage feature flags
  Scenario: Activate a feature flag
    Given a feature flag named "dark_mode"
    When I activate the feature flag "dark_mode"
    Then the feature flag "dark_mode" should be active
```

```php
&lt;?php

class FeatureContext implements Context
{
    private array $featureFlags = [];

    /**
     * @Given a feature flag named :name
     */
    public function aFeatureFlagNamed(string $name)
    {
        $this-&gt;featureFlags[$name] = false; // Initially inactive
    }

    /**
     * @When I activate the feature flag :name
     */
    public function iActivateTheFeatureFlag(string $name)
    {
        $this-&gt;featureFlags[$name] = true;
    }

    /**
     * @Then the feature flag :name should be active
     */
    public function theFeatureFlagShouldBeActive(string $name)
    {
        Assert::assertTrue($this-&gt;featureFlags[$name], "Feature flag '$name' is not active.");
    }
}
```

- ✅ Extremely readable.
- ✅ Useful for shared understanding with non-dev stakeholders.
- ✅ Doubles as living documentation.
- ⚠️ Needs glue code (step definitions).
- ❌ Can get rigid or verbose if overused or poorly maintained.
- ⚠️ Still requires devs to maintain automation behind the steps.

### ⚖️ Important Note: No Style Is "Better", Only Different

None of the acceptance testing styles we’ve covered (raw/technical, internal DSL, external DSL) is inherently superior to the others.
Each has its own **context**, **goals**, and **trade-offs**.

- Some are easier to write, but harder to read.
- Others are more expressive, but require more upfront design.
- Some are ideal for developer-only teams, others support cross-functional collaboration.

> What matters is **clarity of behavior**, not the syntax.
> What matters is **alignment**, not the testing framework.

Choose the style that best serves your team’s communication, architecture, and delivery needs.

The right test is the one that helps you build the **right thing** — and helps everyone understand it.

Each style of acceptance testing (raw, internal DSL, external DSL) comes with its own strengths and trade-offs:

- 🛠️ **Raw tests** are easy to start, but tightly coupled to implementation
- 🧠 **Internal DSLs** provide clarity and reuse, but require thoughtful design
- 📝 **External DSLs (like Gherkin)** support collaboration, but add overhead and risk of misuse

Choose based on what maximizes clarity, reliability, and team alignment — not based on trends or tooling preference.

### Dave Farley’s Layered Architecture

- **Test Case** – the story validating a behavior.
- **DSL Layer** – domain-specific language, readable by humans.
- **Protocol Driver** – connects to the tech layer (API, UI, etc.).
- **System Under Test (SUT)** – the real or simulated system.

[![](https://substackcdn.com/image/fetch/$s_!6ld0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4428aeb8-b6d1-422e-8d4d-2d2ba456f3d7_14304x10240.png)](https://substackcdn.com/image/fetch/$s_!6ld0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4428aeb8-b6d1-422e-8d4d-2d2ba456f3d7_14304x10240.png)

[![](https://substackcdn.com/image/fetch/$s_!v0ud!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F050f084d-5148-4c78-a02b-f3a2df605f06_900x714.jpeg)](https://substackcdn.com/image/fetch/$s_!v0ud!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F050f084d-5148-4c78-a02b-f3a2df605f06_900x714.jpeg)

🧠 This separation **decouples business intent from implementation details**.

### **🧨 **Common Mistakes in Acceptance Testing

Even when teams embrace acceptance testing, several anti-patterns creep in that dilute its effectiveness and increase maintenance cost.

#### 🚫 Testing the UI instead of validating behavior

Developers often confuse acceptance tests with UI tests. Clicking buttons and asserting on DOM elements may validate the interface, not the actual behavior.

> “An acceptance test should fail only if the business behavior is broken, not because a button’s class name changed.”

#### 🚫 Fragile tests coupled to structure (HTML, JSON, DB schema)

Tests that rely on internal implementation details, like CSS selectors, database state, or deeply nested API structures, break easily with refactors. These are brittle and don’t represent real acceptance criteria.

#### 🚫 Overly long or unfocused scenarios

Some tests try to validate entire flows (e.g., registration + login + checkout + confirmation) in one scenario. This increases the risk of false negatives and creates noise.

> Every acceptance test should validate one *single* functionality or criterion.

#### 🚫 Leaky abstraction in DSL usage

When steps or DSL are too close to technical operations (e.g., click("#submit")), they fail to communicate *intent*. They become implementation-specific scripts instead of executable documentation.

#### 🚫 Using them as regression guards for unrelated features

Acceptance tests are not meant to protect low-level implementation details. If one feature breaks due to another, this suggests **coupling** in the product, not an issue with the test.

### **🌟 **Real Benefits of Acceptance Testing

Done right, acceptance tests don’t just catch bugs, they enable confident, aligned delivery. Here's what they unlock:

#### ✅ Shared understanding across disciplines

Acceptance tests embody the *definition of done* in an executable format. They reduce ambiguity between developers, product owners, and stakeholders.

> “It’s not done until the acceptance test passes.”

#### ✅ Executable business documentation

These tests don’t just check correctness, they *tell the story* of your product in domain language. They replace outdated confluence pages with living specs that evolve with the codebase.

#### ✅ Early feedback and fast validation

Because they focus on business expectations, acceptance tests fail early and meaningfully. This helps catch misalignments before a feature is even finished.

#### ✅ Improved design via outside-in thinking

Writing acceptance tests first (à la ATDD or BDD) encourages building systems that serve actual business needs, rather than technical assumptions.

> Behavior drives structure, not the other way around.

#### ✅ Trustworthy safety net for refactors

When written at the right level of abstraction, acceptance tests ensure that the *essence* of a feature still works, even if the underlying code is completely restructured.

#### ✅ Developer-owned quality culture

These are not QA tests. They are a contract between the **development team and the business**. The responsibility lies with devs to ensure functionality behaves as expected, and stays that way.

## ✅ Conclusion: Confidence Through Clarity

*> “Acceptance tests are not tests. They are unambiguous, automated conversations between people and software.”*
> - **Gojko Adzic**

Acceptance testing isn’t about checking boxes or adding automation for the sake of it. It’s about building a **shared understanding of what your system is supposed to do**, and verifying that it actually does it.

A good acceptance test answers a fundamental question:
**“If this test passes, can I confidently say this functionality works as expected for the user?”**

🔁 Reminder: An acceptance test should always validate exactly one functionality or one acceptance criterion.

If it doesn't, it's likely asserting an implementation detail rather than testing meaningful behavior.

It’s that simple and that powerful.

### 🧭 Acceptance tests are...

- ✅ A **communication tool** between business and developers
- ✅ A **design aid** that clarifies what to build before writing code
- ✅ A **safety net** that guarantees critical behaviors remain intact
- ✅ A **living specification** that evolves alongside your product

And they are **owned by the development team**. Quality is not a separate phase, nor the responsibility of another department. It is a discipline that starts with **defining behavior** and **making it executable**.

> “Testing is not a phase. It is part of your design process.”
> - **Dave Farley**

## 📚 References

- Adzic, Gojko. *Specification by Example*.
- Smart, John Ferguson. *BDD in Action*.
- Wynne, Matt. Hellesøy, Aslak. Rose, Seb. *The Cucumber Book*.
- Farley, Dave. *Continuous Delivery*.
- Crispin, Lisa. Gregory, Janet. *Agile Testing*.
- Meszaros, Gerard. *xUnit Test Patterns*.
- Beck, Kent. *Test-Driven Development: By Example*.
- Fowler, Martin. *UnitTest*. [https://martinfowler.com/bliki/UnitTest.html](https://martinfowler.com/bliki/UnitTest.html)
- Fowler, Martin. *IntegrationTest*. [https://martinfowler.com/bliki/IntegrationTest.html](https://martinfowler.com/bliki/IntegrationTest.html)
- Fowler, Martin. *SemanticDiffusion*. [https://martinfowler.com/bliki/SemanticDiffusion.html](https://martinfowler.com/bliki/SemanticDiffusion.html)
- Dodds, Kent C. *The Testing Trophy*. [https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)
- Rauch, Guillermo. *Write tests. Not too many. Mostly integration.*
- Farley, Dave. *[How to Write Acceptance Tests](https://youtu.be/JDD5EEJgpHU)*.

- Bache, Emily. *Styles of Unit Tests*. [https://sammancoaching.org/learning_hours/test_design/styles_of_unit_tests.html](https://sammancoaching.org/learning_hours/test_design/styles_of_unit_tests.html)
- Jemuović, Valentina. *New Test Pyramid*.
