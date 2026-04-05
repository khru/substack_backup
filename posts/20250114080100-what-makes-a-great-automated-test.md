---
title: "What makes a great automated test? The test desiderata"
requested_url: "https://emmanuelvalverderamos.substack.com/p/what-makes-a-great-automated-test"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/what-makes-a-great-automated-test"
substack_post_id: 152829672
retrieved_at: "2026-04-05T07:53:53.630Z"
---
# What makes a great automated test? The test desiderata

Creating great automated tests is essential for building confidence in your code and maintaining it long-term. This article explores the key principles of effective testing, focusing on foundational concepts that will support your journey in automated testing and Test-Driven Development (TDD).

---

## Managing expectations

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

## Introduction

Tests are not just tools to verify your application's behavior—they serve a deeper purpose. As the **first users** of your application, they provide crucial feedback about its **quality and testability**. Well-written tests guide development, reveal pain points and signal opportunities for improvement in your design.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## Tests as first-class citizens

Tests are often the earliest interaction points with our code. They set expectations for behavior and ensure predictable system evolution. Their role extends beyond verification:

- **Insight into testability**: Tests reveal how easy or difficult it is to interact with our system. A testable system typically has a modular, well-designed structure.
- **Quality indicators**: Tests highlight problematic areas in system design. If test setup requires extensive boilerplate or complex configurations, it signals underlying architectural issues.
- **Feedback mechanisms**: Tests tell us when our system becomes cumbersome, inefficient, or fragile. Growing difficulty in test maintenance often indicates accumulating design or technical debt.

### Non-automatable pain points

When parts of your tests, like setup, execution, or teardown, resist automation, they create workflow bottlenecks. Tests requiring manual intervention or complex configurations often reflect design choices that favor short-term gains over long-term maintainability.

## Listening to your tests

Tests aren't just scripts; they're conversational partners in development. When they fail or become hard to maintain, they send clear signals:

- **Test Fragility**: Frequent test failures may indicate brittle code or unstable dependencies.
- **Slow Feedback Loops**: Tests that take too long discourage iterative development and point to system inefficiencies.
- **Opaque Failures**: Unclear or non-specific failures often indicate poorly defined test cases or overly complex logic.

By heeding these signals, teams can address issues before they become major problems. This makes tests valuable not only for quality assurance but also for system design and continuous improvement.

## What makes a good automated test?

### Kent Beck’s Test Desiderata

Kent Beck outlined 12 key properties of tests, creating a framework for evaluating their effectiveness. These principles guide developers in writing maintainable and impactful tests:

[![Mindmap](https://substackcdn.com/image/fetch/$s_!9otf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcba5d5b-95b4-4617-b0f7-d70c25b89ada_2904x2244.jpeg)](https://substackcdn.com/image/fetch/$s_!9otf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcba5d5b-95b4-4617-b0f7-d70c25b89ada_2904x2244.jpeg)

- **Isolated**: Tests should return the same results regardless of the order in which they are run.
- **Composable**: I should be able to test different dimensions of variability separately and combine the results.
- **Deterministic**: If nothing changes, the test result shouldn’t change.
- **Fast**: Tests should run quickly.
- **Writable**: Tests should be cheap to write relative to the cost of the code being tested.
- **Readable**: Tests should be comprehensible for the reader, invoking the motivation for writing this particular test.
- **Behavioral**: Tests should be sensitive to changes in the behavior of the code under test. If the behavior changes, the test result should change.
- **Structure-Insensitive**: Tests should not change their result if the structure of the code changes.
- **Automated**: Tests should run without human intervention.
- **Specific**: If a test fails, the cause of the failure should be obvious.
- **Predictive**: If the tests all pass, then the code under test should be suitable for production.
- **Inspiring**: Passing the tests should inspire confidence.

Some test properties complement each other, for example, automation naturally leads to faster test execution.

Other properties can work against each other. When tests more accurately reflect production conditions, they often run more slowly.

Sometimes (and here's where it gets interesting), properties only appear to conflict. Through clever use of composability, you can achieve both speed *and* production-like behavior in your tests.

These properties create a delicate balance between practical utility and long-term maintainability, helping teams build test suites that deliver both immediate and lasting value.

Let's explore each of these qualities in detail to understand what makes a test truly effective, moving beyond theory into practical application.

Disclaimer: All the code examples come from Kent Beck and Kelly Sutton's videos explaining the Test Desiderata

### 1. Isolated - Tests should return the same results regardless of the order in which they are run.

Isolation means that tests must be independent and produce consistent results regardless of the order in which they run. When tests share state, for example, through global variables, one test can affect another's outcome, creating unpredictable results and hard-to-diagnose failures.

**About the code example:**

The example shows an `HourlyWageCalculator` application that computes employee wages based on weekly hours and hourly rates. The code uses a global variable `$number_of_calculations` to count calculations. Though seemingly innocuous, this shared state creates test dependencies, causing tests to fail when run in different orders, a clear violation of the isolation principle.

**Production code:**

```ruby
module MinimumWage
  $number_of_calculations = 0

  class HourlyWageCalculator
    class &lt;&lt; self
      def calculate(employee)
        $number_of_calculations += 1
        $number_of_calculations * employee.weekly_hours * employee.hourly_rate
      end
    end
  end
end

class Employee
  attr_reader :weekly_hours, :hourly_rate

  def initialize(weekly_hours:, hourly_rate:)
    @weekly_hours = weekly_hours
    @hourly_rate = hourly_rate
  end
end
```

**Test code:**

```ruby
require "minimum_wage/hourly_wage_calculator"

RSpec.describe MinimumWage::HourlyWageCalculator do
  describe ".calculate" do
    subject { described_class.calculate(employee) }

    context 'Kent' do
      let(:employee) do
        Employee.new(
          weekly_hours: 40,
          hourly_rate: 8
        )
      end

      it "calculates the total hourly wages" do
        expect(subject).to eq(320)
      end
    end

    context 'Kelly' do
      let(:employee) do
        Employee.new(
          weekly_hours: 40,
          hourly_rate: 7
        )
      end

      it "calculates the total hourly wages" do
        expect(subject).to eq(560)
      end
    end
  end
end
```

When running the tests in reverse order, the shared global variable alters the results, leading to test failures:

**Reordered test code:**

```ruby
require "minimum_wage/hourly_wage_calculator"

RSpec.describe MinimumWage::HourlyWageCalculator do
  describe ".calculate" do
    subject { described_class.calculate(employee) }

    context 'Kelly' do
      let(:employee) do
        Employee.new(
          weekly_hours: 40,
          hourly_rate: 7
        )
      end

      it "calculates the total hourly wages" do
        expect(subject).to eq(560)
      end
    end

    context 'Kent' do
      let(:employee) do
        Employee.new(
          weekly_hours: 40,
          hourly_rate: 8
        )
      end

      it "calculates the total hourly wages" do
        expect(subject).to eq(320)
      end
    end
  end
end
```

To maintain test isolation, avoid shared states and reset any global environment after each test run. Kent Beck's "*clean up after yourself*" principle is key: whenever you modify the global state, restore it to its original condition after the test completes. This practice ensures your tests remain isolated, can run in any order, and produce reliable results.

### 2. Composable - I should be able to test different dimensions of variability separately and combine the results

Composability in software systems means we can test individual components separately and combine them confidently. This approach dramatically reduces the number of tests needed. Instead of testing every possible combination directly, composable tests allow developers to focus on core building blocks and verify their interactions.

#### **Why composability matters**

Emily Bache's work on the Gilded Rose Kata demonstrates how composability efficiently manages complex business rules. Her "axes of variability" concept creates focused, targeted tests that work together to verify the entire system. This prevents developers from writing endless test cases for every possible combination.

For instance, in the context of the `HourlyWageCalculator`, composable tests would:

- Test that weekly hours are calculated correctly.
- Test that the hourly rate is handled properly.
- Combine these tests to ensure the final calculation is accurate.

**Production Code:**

```ruby
module MinimumWage
  class HourlyWageCalculator
    class &lt;&lt; self
      def calculate(employee)
        employee.weekly_hours * employee.hourly_rate
      end
    end
  end
end

class Employee
  attr_reader :weekly_hours, :hourly_rate

  def initialize(weekly_hours:, hourly_rate:)
    @weekly_hours = weekly_hours
    @hourly_rate = hourly_rate
  end
end
```

**Composable Tests:**

```ruby
require "minimum_wage/hourly_wage_calculator"

RSpec.describe MinimumWage do
  let(:employee) do
    Employee.new(
      weekly_hours: 40,
      hourly_rate: 8,
    )
  end

	# Given that the Employee works 40 hours at a rate of 8
  describe Employee do
    describe "#weekly_hours and #hourly_rate" do
      subject { employee }

      it { expect(subject.weekly_hours).to eq(40) }
      it { expect(subject.hourly_rate).to eq(8) }
    end
  end

	# For that Employee the salary would be $320
  describe MinimumWage::HourlyWageCalculator do
    describe ".calculate" do
      subject { described_class.calculate(employee) }

      it "calculates the correct rate based on weekly_hours and hourly_rate" do
        expect(subject).to eq(320)
      end
    end
  end
end
```

By testing `weekly_hours` and `hourly_rate` separately from their combined calculation, you prevent test cases from growing exponentially. This approach eliminates redundancy while following sound software design principles.

At its core, composable testing embodies a philosophy of modularity in both code and tests. When each test focuses on a single responsibility, developers can create more robust systems and avoid the complexity of bloated test suites.

### 3. Deterministic - If nothing changes, the test result shouldn’t change

Deterministic tests produce the same results every time they run when no changes are made to the system. Tests that sometimes pass and sometimes fail without code changes are called "flaky." These flaky tests undermine confidence in the test suite by creating uncertainty, when a test fails, developers can't tell if there's a real issue or if it's just test instability.

Consider a real example: a test designed to click an "Edit" button on a web page. The test failed unexpectedly when the test environment generated a random user named "Meredith," because the name contained "Edit" as a substring. The test clicked the wrong element, demonstrating how uncontrolled factors like random data can cause unreliable results.

To avoid these issues, deterministic tests should:

- Control external inputs by explicitly passing required parameters, such as dates, times, or random seeds.
- Eliminate dependencies on factors outside the test's control, such as system clocks or random number generators.

By maintaining consistent results, developers can trust their test suite to provide reliable feedback. As Kent Beck emphasizes, flaky tests erode trust, making determinism essential for a dependable testing process.

### 4. Fast - Tests should run quickly.

Fast tests are essential for maintaining developer flow and minimizing context switching. Kent Beck emphasizes that test speed isn't a luxury, it's a necessity for effective feedback loops. When tests run in under a second, developers can maintain focus, iterate quickly, and stay in a "flow" state. However, slower tests that take 10 seconds or more disrupt concentration, causing developers to switch to unrelated tasks. This context switching increases cognitive load and reduces productivity.

To illustrate this, let's examine a simple hourly wage calculator:

**Production Code:**

```ruby
module MinimumWage
  class HourlyWageCalculator
    class &lt;&lt; self
      def calculate(employee)
        employee.weekly_hours * employee.hourly_rate
      end
    end
  end
end

class Employee
  attr_reader :first_name, :last_name, :address, :weekly_hours, :hourly_rate

  def initialize(first_name:, last_name:, address:, weekly_hours:, hourly_rate:)
    @first_name = first_name
    @last_name = last_name
    @address = address
    @weekly_hours = weekly_hours
    @hourly_rate = hourly_rate
  end
end
```

**Test code:**

```ruby
require "minimum_wage/hourly_wage_calculator"

RSpec.describe MinimumWage::HourlyWageCalculator do
  describe ".calculate" do
    subject { described_class.calculate(employee) }

    let(:employee) do
      Employee.new(
        first_name: 'Kent',
        last_name: 'Beck',
        address: '1 Main St., Berkeley, CA, 94701',
        weekly_hours: 40,
        hourly_rate: 8
      )
    end

    it "calculates the total hourly wages" do
      expect(subject).to eq(320)
    end
  end
end
```

The test suite in this example executes quickly, offering instant feedback. However, adding a delay dramatically alters this experience. Let's see what happens when we introduce a`sleep`statement:

**Modified test code:**

```ruby
require "minimum_wage/hourly_wage_calculator"

RSpec.describe MinimumWage::HourlyWageCalculator do
  describe ".calculate" do
    subject { described_class.calculate(employee) }

    # We make it go slow
    before { sleep 10 }

    let(:employee) do
      Employee.new(
        first_name: 'Kent',
        last_name: 'Beck',
        address: '1 Main St., Berkeley, CA, 94701',
        weekly_hours: 40,
        hourly_rate: 8
      )
    end

    it "calculates the total hourly wages" do
      expect(subject).to eq(320)
    end
  end
end
```

A 10-second delay can disrupt developers' concentration, causing them to context-switch to other tasks like checking email. This interruption breaks their flow state, reducing efficiency and creating frustration.

#### Key takeaway

Fast tests are vital for maintaining developer momentum. Quick feedback keeps developers engaged and focused, while slow tests increase mental overhead and disrupt workflow. Making test speed a priority ensures your testing approach supports efficient development and creates a productive environment.

### 5. Writable - Tests should be cheap to write relative to the cost of the code being tested

Writable tests should balance the effort of creating them against their value. Kent Beck emphasizes that tests shouldn't be so burdensome to write that they outweigh their benefits. For example, spending hours writing a test for simple code with minimal failure impact may not be worthwhile.

When writing tests feels unnecessarily difficult, it often reveals problems in the system being tested. Tests provide valuable feedback about code design. Complex setup requirements or excessive boilerplate may signal that the code's interface needs improvement.

Let's illustrate this concept with an example using an hourly wage calculator and an employee class:

**Production Code:**

```ruby
module MinimumWage
  class HourlyWageCalculator
    class &lt;&lt; self
      def calculate(employee)
        employee.weekly_hours * employee.hourly_rate
      end
    end
  end
end

class Employee
  attr_reader :first_name, :last_name, :address, :weekly_hours, :hourly_rate

  def initialize(first_name:, last_name:, address:, weekly_hours:, hourly_rate:)
    @first_name = first_name
    @last_name = last_name
    @address = address
    @weekly_hours = weekly_hours
    @hourly_rate = hourly_rate
  end
end
```

**Test code:**

```ruby
require "minimum_wage/hourly_wage_calculator"

RSpec.describe MinimumWage::HourlyWageCalculator do
  describe ".calculate" do
    subject { described_class.calculate(employee) }

    let(:employee) do
      Employee.new(
        first_name: 'Kent',
        last_name: 'Beck',
        address: '1 Main St., Berkeley, CA, 94701',
        weekly_hours: 40,
        hourly_rate: 8
      )
    end

    it "calculates the total hourly wages" do
      expect(subject).to eq(320)
    end

    context 'when testing another employee' do
      let(:employee) do
        Employee.new(
          first_name: 'Kelly',
          last_name: 'Sutton',
          address: '1 Main St., San Francisco, CA, 94103',
          weekly_hours: 40,
          hourly_rate: 7
        )
      end

      it "calculates the total hourly wages" do
        expect(subject).to eq(280)
      end
    end
  end
end
```

This test has a clear issue: including`first_name`,`last_name`, and`address`attributes when they don't affect the wage calculation. This unnecessary data adds complexity and makes the test harder to write and maintain. A cleaner approach would focus solely on the attributes that matter:

**Refined test code:**

```ruby
RSpec.describe MinimumWage::HourlyWageCalculator do
  describe ".calculate" do
    subject { described_class.calculate(employee) }

    let(:employee) do
      Employee.new(
        weekly_hours: 40,
        hourly_rate: 8
      )
    end

    it "calculates the total hourly wages" do
      expect(subject).to eq(320)
    end

    context 'when testing another employee' do
      let(:employee) do
        Employee.new(
          weekly_hours: 40,
          hourly_rate: 7
        )
      end

      it "calculates the total hourly wages" do
        expect(subject).to eq(280)
      end
    end
  end
end
```

#### Key takeaway

Well-written tests should be easy to create and maintain. Focus on testing only the relevant attributes to minimize setup complexity and reduce cognitive load. When tests feel difficult to write, it often signals underlying design issues in your code. By addressing these problems, you not only make testing easier but also improve your codebase's overall quality.

### 6. Readable - Tests should be comprehensible for the reader, invoking the motivation for writing this particular test

When writing tests, remember that they'll be read far more often than they're written. Tests serve two key purposes: validating code for machines and documenting behavior for developers. A well-written test tells a clear, self-contained story about its purpose and reasoning. This clarity reduces the mental effort required from future readers, whether that's you returning to the code months later or another developer exploring the system.

Let's consider an example using the same minimum wage calculator:

**Production Code:**

```ruby
module MinimumWage
  class HourlyWageCalculator
    class &lt;&lt; self
      def calculate(hours, rate, zip_code = nil)
        if zip_code == '94103'
          calculate_sf(hours, rate)
        else
          hours * rate
        end
      end

      private

      def calculate_sf(hours, rate)
        hours * [rate, 15.0].max
      end
    end
  end
end
```

**Readable test code:**

```ruby
require "minimum_wage/hourly_wage_calculator"

RSpec.describe MinimumWage::HourlyWageCalculator do
  describe '.calculate' do
    subject { described_class.calculate(hours, rate, zip_code) }

    let(:hours) { 40 }
    let(:rate) { 8 }
    let(:zip_code) { nil }

    it "calculates the total hourly wages" do
      expect(subject).to eq(320)
    end

    context "zip_code is in San Francisco" do
      let(:zip_code) { '94103' }

      context "rate is below $15 per hour" do
        let(:rate) { 14 }

        it "uses $15 as the rate" do
          expect(subject).to eq(600)
        end
      end

      context "rate is above $15 per hour" do
        let(:rate) { 16 }

        it "uses the given rate" do
          expect(subject).to eq(640)
        end
      end
    end
  end
end
```

In this example, the relationship between `hours`, `rate`, and the expected outcome is crystal clear. The test communicates its purpose and behavior directly, letting readers understand the system immediately without having to navigate through layers of abstractions or shared setup.

Let's look at a less readable version, where we try to follow DRY (Don't Repeat Yourself) principles by moving `40` hours into a helper method:

**Less Readable test code:**

```ruby
require "minimum_wage/hourly_wage_calculator"

def default_hours
  40
end

RSpec.describe MinimumWage::HourlyWageCalculator do
  describe '.calculate' do
    subject { described_class.calculate(hours, rate, zip_code) }

    let(:hours) { default_hours }
    let(:rate) { 8 }
    let(:zip_code) { nil }

    it "calculates the total hourly wages" do
      expect(subject).to eq(320)
    end

    context "zip_code is in San Francisco" do
      let(:zip_code) { '94103' }

      context "rate is below $15 per hour" do
        let(:rate) { 14 }

        it "uses $15 as the rate" do
          expect(subject).to eq(600)
        end
      end

      context "rate is above $15 per hour" do
        let(:rate) { 16 }

        it "uses the given rate" do
          expect(subject).to eq(640)
        end
      end
    end
  end
end
```

While this refactoring reduces duplication, it actually makes the test harder to understand. Moving `40` into a separate method obscures the direct connection between inputs (`hours`, `rate`) and the expected output. Future readers must now hunt through multiple locations to understand the test's purpose, which increases their mental workload.

#### Key takeaway

Readable tests should prioritize clarity over abstraction. They should tell a clear story by presenting all necessary information upfront. When faced with the trade-off between reducing duplication and maintaining readability, tests should favor readability. Remember: tests are meant to serve as clear documentation of system behavior, not as puzzles for future developers to decode.

### 7. Behavioral - Tests should be sensitive to changes in the behavior of the code under test. If the behavior changes, the test result should change

Imagine you're working on a payroll system that calculates minimum wage rates across different regions. For most cases, the calculation is simple, multiply hours worked by the hourly rate. But what about cities like San Francisco that have their own minimum wage laws? Your tests must be precise enough to catch any changes in how these calculations work.

Consider a test suite that verifies San Francisco's minimum wage enforcement. When a worker's hourly rate falls below the $15 minimum wage, the system must adjust their pay upward. If their rate already exceeds $15, no adjustment is needed. This demonstrates behavioral sensitivity, the test catches functionality changes, such as when someone accidentally types $150 instead of $15 for the minimum wage. In such cases, the tests fail immediately, alerting us to the problem.

Here is an example of how this could look in Ruby code:

**Production Code:**

```ruby
module MinimumWage
  class HourlyWageCalculator
    class &lt;&lt; self
      def calculate(hours, rate, zip_code = nil)
        if zip_code == '94103'
          calculate_sf(hours, rate)
        else
          hours * rate
        end
      end

      private

      def calculate_sf(hours, rate)
        hours * [rate, 15.0].max
      end
    end
  end
end
```

**Test code:**

```ruby
require "minimum_wage/hourly_wage_calculator"

RSpec.describe MinimumWage::HourlyWageCalculator do
  describe '.calculate' do
    subject { described_class.calculate(hours, rate, zip_code) }

    let(:hours) { 40 }
    let(:rate) { 8 }
    let(:zip_code) { nil }

    it "calculates the total hourly wages" do
      expect(subject).to eq(320)
    end

    context "zip_code is in San Francisco" do
      let(:zip_code) { '94103' }

      context "rate is below $15 per hour" do
        let(:rate) { 14 }

        it "uses $15 as the rate" do
          expect(subject).to eq(600)
        end
      end

      context "rate is above $15 per hour" do
        let(:rate) { 16 }

        it "uses the given rate" do
          expect(subject).to eq(640)
        end
      end
    end
  end
end
```

**Behavioral sensitivity** means your test suite functions as a safety net. Rather than merely confirming that your system works now, it verifies that the code continues to behave as intended over time. When something breaks, these tests alert you immediately, before issues surface in production or through customer complaints.

Consider what happens when someone accidentally modifies the production code, introducing a bug in the minimum wage logic. For example:

**Modified production code:**

```ruby
module MinimumWage
  class HourlyWageCalculator
    class &lt;&lt; self
      def calculate(hours, rate, zip_code = nil)
        if zip_code == '94103'
          calculate_sf(hours, rate)
        else
          hours * rate
        end
      end

      private

      def calculate_sf(hours, rate)
        hours * [rate, 150].max # Bug introduced: rate bumped to 150 instead of 15
      end
    end
  end
end
```

When this change occurs, the tests fail immediately, indicating that the system's behavior has changed. This illustrates the value of behavioral sensitivity, tests should catch any unintended changes in system functionality, ensuring problems are detected and fixed before they reach production.

### 8. Structure-Insensitive - Tests should not change their result if the structure of the code changes

Let's explore this concept with an example. Consider a minimum wage calculator that determines wages based on various conditions, for instance, whether an employee works in San Francisco, where the minimum wage is $15 per hour. Here's how the initial production code looks:

**Production code:**

```ruby
module MinimumWage
  class HourlyWageCalculator
    class &lt;&lt; self
      def calculate(hours, rate, zip_code = nil)
        if zip_code == '94103'
          calculate_sf(hours, rate)
        else
          hours * rate
        end
      end

      private

      def calculate_sf(hours, rate)
        hours * [rate, 15.0].max
      end
    end
  end
end
```

Let's look at an example of a **structure-sensitive** test that incorrectly depends on the `calculate_sf` method:

**Test code:**

```ruby
require "minimum_wage/hourly_wage_calculator"

RSpec.describe MinimumWage::HourlyWageCalculator do
  describe '.calculate' do
    subject { described_class.calculate(hours, rate, zip_code) }

    let(:hours) { 40 }
    let(:rate) { 8 }
    let(:zip_code) { nil }

    it "calculates the total hourly wages" do
      expect(subject).to eq(320)
    end

    context "zip_code is in San Francisco" do
      let(:zip_code) { '94103' }

      # This is the test we are putting the focus on
      it "uses the .calculate_sf method" do
        expect(described_class).to receive(:calculate_sf).and_return(600)
        expect(subject).to eq(600)
      end
    end
  end

  describe '.calculate_sf' do
    subject { described_class.send(:calculate_sf, 40, 14) }

    it "uses a minimum wage of $15" do
      expect(subject).to eq(600)
    end
  end
end
```

Initially, these tests appear to work well. However, they rely too heavily on the existence of the `calculate_sf` method, making them fragile. If you refactor the production code by inlining `calculate_sf`, the tests will break, even though the system's behavior hasn't changed:

**Refactored production code:**

```ruby
module MinimumWage
  class HourlyWageCalculator
    class &lt;&lt; self
      def calculate(hours, rate, zip_code = nil)
        if zip_code == '94103'
          hours * [rate, 15.0].max
        else
          hours * rate
        end
      end
    end
  end
end
```

The tests break because they depend on the code's structure rather than its behavior. This highlights why tests should be **structure-insensitive**. Such tests focus on the system's outputs and behavior instead of its internal implementation, giving you the confidence to refactor code without breaking the test suite.

When tests are structure-sensitive, developers become frustrated and lose trust in their test suite. This erosion of trust often leads teams to abandon testing practices entirely. To prevent this, always ensure your tests validate behavior, not implementation details.

### 9. Automated - Tests should run without human intervention

Automation is essential for maintaining efficient and consistent testing. Traditional manual testing, where humans click through applications, observe results, and approve changes, may seem quick and cost-effective at first. However, it creates significant scalability challenges as systems grow.

Consider a simple UI change. While manual verification might take just minutes initially, the complexity increases exponentially as the system evolves. Each new feature or bug fix contributes to the "n-squared" problem, where adding elements to a system exponentially increases the number of interactions to test. This leads to repetitive, time-consuming testing cycles as each element must be tested against all existing ones.

Automated tests address these issues by:

- **Reducing repetition:** Once written, automated tests can be run repeatedly without extra effort, ensuring consistent verification.
- **Providing fast feedback:** Automated tests execute quickly, helping developers spot issues immediately after making changes, essential for continuous integration and delivery.
- **Improving reliability:** Automated tests eliminate human error and oversight that often occur during manual testing, particularly under pressure.

While automation requires upfront investment, both in writing tests and sometimes restructuring code for testability, the benefits are substantial. Clear interfaces and decoupled components make automation more effective. As Martin Fowler emphasizes in his article "Continuous Integration," automated tests form the foundation of CI/CD pipelines, enabling frequent code integration and reliable deployment.

In the end, automated tests save time, minimize errors, and build system confidence. By removing the need for constant human oversight, they free developers to focus on what matters most: building features.

### 10. Specific - If a test fails, the cause of the failure should be obvious

When tests are specific, developers can quickly identify the root cause of failures without extensive debugging. Let's explore this concept using a payroll system with a **minimum wage calculator**:

**Production code:**

```ruby
module MinimumWage
  class HourlyWageCalculator
    class &lt;&lt; self
      def calculate(employee)
        calculate_for(
          hours: employee.weekly_hours,
          rate: employee.hourly_rate
        )
      end

      def calculate_for(hours:, rate:)
        hours * rate
      end
    end
  end
end

class Employee
  attr_reader :weekly_hours, :hourly_rate

  def initialize(weekly_hours:, hourly_rate:)
    @weekly_hours = weekly_hours
    @hourly_rate = hourly_rate
  end
end
```

**Test code:**

```ruby
require "minimum_wage/hourly_wage_calculator"

RSpec.describe MinimumWage do
  describe ".calculate" do
    subject { described_class.calculate(employee) }

    let(:employee) do
      Employee.new(
        weekly_hours: 40,
        hourly_rate: 8
      )
    end

    it "calculates the correct rate based on weekly_hours and hourly_rate" do
      expect(subject).to eq(320)
    end
  end

  describe ".calculate_for" do
    subject { described_class.calculate_for(hours: 40, rate: 8) }

    it "calculates the correct rate based on weekly_hours and hourly_rate" do
      expect(subject).to eq(320)
    end
  end
end
```

### Specificity in Action

- If someone introduces an error in the `calculate_for` method by making an off-by-one mistake:

```ruby
def calculate_for(hours:, rate:)
  (hours + 1) * rate
end
```

- The failing `.calculate_for` test pinpoints the exact location of the problem.
	Test Output:

```plaintext
.calculate_for calculates the correct rate based on weekly_hours and hourly_rate
   Failure/Error: expect(subject).to eq(320)

     expected: 320
          got: 328
```

- If someone introduces an error in the higher-level `calculate` method:

```ruby
def calculate(employee)
  calculate_for(
    hours: employee.weekly_hours + 1,
    rate: employee.hourly_rate
  )
end
```

- The test for`.calculate`will also fail:

```plaintext
.calculate calculates the correct rate based on weekly_hours and hourly_rate
   Failure/Error: expect(subject).to eq(320)

     expected: 320
          got: 328
```

- In this case, **both tests** fail because the error in `calculate_for` propagates to `calculate`. The test output clearly indicates where to investigate.

In every scenario, these specific tests pinpoint the exact function causing the error. Without such granular tests, you'd face unclear failures that require extensive debugging.

### Why Specificity Matters

Specific tests:

- Highlight the **exact location** of an error, minimizing debugging time.
- Build **trust** in the test suite through clear, actionable feedback.
- Eliminate the ambiguity that comes with broad, system-wide tests.

By transforming failures into clear, actionable corrections, specific tests boost both developer confidence and coding efficiency.

### 11. Predictive - If the tests all pass, then the code under test should be suitable for production

Tests should act as an oracle, predicting how the system will behave in production. These tests bridge the gap between testing environments and real-world scenarios, ensuring that passing tests indicate production readiness.

However, achieving predictiveness is challenging. Real-world systems depend on factors beyond developer control, changing browser behaviors, network conditions, and third-party integrations. A system might pass all tests in a controlled environment yet fail in production due to unexpected edge cases, such as rare concurrency issues or dependency failures.

Kent Beck and Kelly Sutton note that while no test suite can predict every production issue, gaps between test results and production behavior guide improvements. By addressing these gaps, the test suite's predictiveness evolves. As Beck states, "your tests should be an oracle".

Predictive tests are essential because they:

- **Build trust:** Teams rely on predictive tests to signal whether changes are safe to deploy.
- **Enhance stability:** By identifying gaps in test coverage, teams can proactively address potential production failures.
- **Support decision-making:** A predictive test suite enables faster, data-driven decisions about deployments and feature rollouts.

Achieving predictiveness demands thoughtful design, robust coverage, and continuous refinement. While perfect predictiveness remains unattainable, pursuing it aligns testing practices with the ultimate goal: delivering reliable software.

### 12. Inspiring - Passing the tests should inspire confidence

The final property of a great test is its ability to inspire confidence. A well-designed test suite doesn't just validate correctness, it empowers developers to work with freedom and creativity. When tests provide reliable feedback, they reduce the fear of change, enabling teams to innovate without hesitation.

Kent Beck illustrates this through the transformative confidence teams gain when their tests become predictive and reliable. This shift not only empowers individual developers but also builds trust among teammates, customers, and stakeholders. Tests that inspire confidence lead to:

- **Empowered development:** Developers can refactor boldly and experiment freely, knowing their tests will catch issues before deployment.
- **Improved productivity:** Time previously spent worrying about potential failures shifts toward solving problems and creating value.
- **Better collaboration:** Shared trust in the test suite strengthens team dynamics and encourages collaborative problem-solving.

Inspiring tests go beyond mere correctness, they create a culture of safety and reliability where developers feel supported in taking risks and pushing boundaries. As Beck notes, "Nobody wants tests per se, but they sure do want this feeling of confidence." Tests that inspire form the foundation for sustainable and innovative software development.

## Introduction to FIRST Principles

The **FIRST principles**, developed by Tim Ottinger and Jeff Langr, offer a fundamental approach to effective unit testing. The acronym stands for **Fast, Isolated, Repeatable, Self-verifying, and Timely**, key characteristics that make tests both functional and supportive of sustainable development.

- **Fast**: Tests must run quickly to enable frequent execution. This speed lets developers catch errors immediately and iterate confidently. When tests are slow, developers tend to skip them.
- **Isolated**: Each test should examine one unit of behavior independently of external factors or other tests. This isolation makes failure diagnosis clear and eliminates dependency issues.
- **Repeatable**: Tests should yield consistent results regardless of timing or environment. This reliability builds trust in the test suite.
- **Self-verifying**: Tests must provide clear pass/fail outcomes without requiring manual review of logs or outputs. Any ambiguity undermines automation's value.
- **Timely**: Write tests alongside, or before the corresponding code, following test-driven development (TDD) practices. This timing helps shape better designs and validates code intent early.

Kent Beck's article "Desirable Unit Tests" builds on these ideas with his "Test Desiderata", 12 desirable properties for tests. He views testing as multi-dimensional, where different attributes matter more or less depending on context. Beck emphasizes isolation, predictiveness, and inspiration while warning against rigid adherence to any single testing approach. His attributes complements FIRST by encouraging thoughtful alignment between testing practices and broader software quality goals.

## Comparing FIRST Principles to Test Desiderata

While both frameworks value clarity, independence, and maintainability, they differ in their focus:

- **Test Desiderata** offers comprehensive set of attributes for evaluating test quality across all test types.
- **FIRST** concentrates on practical aspects of efficient unit test writing and maintenance.

**Aspect** **FIRST Principles** **Test Desiderata** **Scope** Focused on unit tests. Encompasses all types of tests, from unit to system-level tests. **Key Focus** Practical efficiency (speed, reliability). Comprehensive qualities, including inspiration and predictiveness. **Guidance** Clear, actionable for rapid feedback cycles. Encourages broader reflection on testing trade-offs. **Emphasis** Fast execution, independence, and immediate utility. Sustainability, composability, and system-wide quality indicators. **Inspiration** Encourages quick iterations but doesn't emphasize broader confidence. Inspires confidence and aligns testing practices with system goals.

## Addressing Test Smells

Test smells indicate problems in your test suite. Common issues include:

- **Fragile Tests:** Tests that break with minor changes, violating structure-insensitivity.
- **Noisy Tests:** Tests with unnecessary complexity that impairs readability and writing.
- **Slow Tests:** Tests that impede rapid feedback by taking too long to run.
- **False Positives/Negatives:** Tests that produce misleading results, compromising predictiveness.

Fixing these smells strengthens alignment with Test Desiderata principles and improves reliability.

## Conclusions

### FRIST Principles

FIRST provides an excellent foundation for unit tests, though its narrow focus limits its application to complex testing scenarios. Its emphasis on operational efficiency makes it particularly valuable for developers new to testing.

### Test Desiderata

The Test Desiderata has become my preferred list of attributes for evaluating and guiding testing. Here's why:

- **Guidance and Trade-offs**: Test Desiderata helps identify ideal test qualities and assess trade-offs systematically. While unit tests prioritize speed, integration tests might focus more on readability and composability.
- **Listening to Tests**: Test Desiderata teaches us to "listen" to our tests. When tests become difficult to write or maintain, they often signal underlying design issues. Early refactoring prevents these issues from becoming significant technical debt.
- **First-Class Citizens**: Tests deserve the same care as production code. This approach ensures long-term maintainability and utility.
- **Composability Challenges**: Composability proves the most challenging among the desiderata. Creating reusable, modular tests without overcomplication requires deep architectural understanding and experience.
- **Avoiding Premature Abstractions**: Test Desiderata promotes test refactoring while avoiding premature abstractions, keeping tests simple and purposeful.

By following these practices, I've built test suites that not only validate behavior but also improve design, enhance maintainability, and provide valuable feedback throughout development.

## References

- Beck, Kent. *Test Desiderata.* [https://testdesiderata.com/](https://testdesiderata.com/)
- Ottinger, Tim. Langr, Jeff. *Unit Tests Are FIRST: Fast, Isolated, Repeatable, Self-Verifying, and Timely.* [Medium Article](https://medium.com/pragmatic-programmers/unit-tests-are-first-fast-isolated-repeatable-self-verifying-and-timely-a83e8070698e).
- Beck, Kent. *Desirable Unit Tests.* [Tidy First Substack](https://tidyfirst.substack.com/p/desirable-unit-tests).
- Bache, Emily. *Why Developers LOVE The Gilded Rose Kata.* [YouTube Video](https://youtu.be/Mt4XpGxigT4?si=wiw-dsxMVCbGq3xy).
- Beck, Kent &amp; Sutton, Kelly. *Test Desiderata Series (Videos on YouTube):*
	- *Behavioral Sensitivity.* [Video Link](https://youtu.be/Mt4XpGxigT4?si=wiw-dsxMVCbGq3xy).
	- *Structure-Insensitive Tests.* [Video Link](https://youtu.be/bvRRbWbQwDU?si=-mjNfoVCr_S7ucd-).
	- *Readable Tests.* [Video Link](https://youtu.be/bDaFPACTjj8?si=_KUoqn7m2Di794n_).
	- *Tests Should be Easy to Write.* [Video Link](https://youtu.be/CAttTEUE9HM?si=iIy4R23Wo1FYWPfJ).
	- *Tests Should be Fast.* [Video Link](https://youtu.be/L0dZ7MmW6xc?si=kosqo6Vhsa11HvtD).
	- *Tests Should be Deterministic.* [Video Link](https://youtu.be/PwWyp-wpFiw?si=3CbrAHoc5Jj6wa1f).
	- *Tests Should Be Automated.* [Video Link](https://youtu.be/YQlmP08dj6g?si=QJQTOVdkJJNUkJ2-).
	- *Tests Should Be Isolated.* [Video Link](https://youtu.be/HApI2cspQus?si=zlRqHoumOJFfo80G).
	- *Tests Should Be Composable.* [Video Link](https://youtu.be/Wf3WXYaMt8E?si=xq6ZM68xby7gRHyM).
	- *Tests Should Be Specific.* [Video Link](https://youtu.be/8lTfrCtPPNE?si=rTYg5SXsInQow8s2).
	- *Tests Should Predict Production.* [Video Link](https://youtu.be/7o5qxxx7SmI?si=7Ty0FgHiXB1BmqZu).
	- *Tests Should be Inspiring.* [Video Link](https://youtu.be/2Q1O8XBVbZQ?si=0t7ZYTJgz_F5SS2v).
- Bache, Emily. *Best Tests for Gilded Rose Kata | Kent Beck’s Desiderata.* [YouTube Video](https://youtu.be/vMww6pV6P7s?si=f8tmJLBC4cBuKJXy).
