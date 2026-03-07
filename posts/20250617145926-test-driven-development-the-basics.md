---
title: "Test-Driven Development the basics"
requested_url: "https://emmanuelvalverderamos.substack.com/p/test-driven-development-the-basics"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/test-driven-development-the-basics"
substack_post_id: 162677485
retrieved_at: "2026-03-07T08:25:44.291Z"
---
# Test-Driven Development the basics

### 🧠 Summary Insight

**> TDD is not just a technique, it is a philosophy of software development rooted in discipline, feedback, and evolutionary design.**
> Done well, it produces not only well-tested code, but also *better structured, easier to change, and more human-friendly software systems*.

## Table of Contents

- What is Test-Driven Development and why should you care?
- ❌ What TDD is *Not* - unlearning the misconceptions first
- The TDD methodology and its canonical flow 🔄📐
- 🔁 Feedback loops: designing with decisions in mind
- The test list 📝
- Failing for the right reason ❌🎯
- Fake it until you make it 🤖
- What about *triangulation*? 🎯
- Obvious implementation 💡
- Refactor: the designer's playground 🧼🧱
- 🎯 Practical Application: The FizzBuzz Kata

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## What is Test-Driven Development and why should you care?

In the fast, evolving and uncertain landscape of modern software development, every line of code we write represents more than just logic and structure, it’s a long-term decision with real consequences. Test-Driven Development, or TDD, is not simply a method for writing tests. It is a disciplined design practice, a mindset, and more importantly, a strategic approach to managing complexity, enhancing adaptability, and protecting intent over time.

At its essence, TDD is a technique for writing software through short, iterative feedback loops. It invites us to write a failing test first (🔴 Red), make it pass with the simplest implementation (🟢 Green), and then improve the design while keeping the test green (🔵 Refactor). This cycle is famously described through **Kent Beck’s three laws of TDD**:

> “You are not allowed to write any production code unless it is to make a failing test pass. You are not allowed to write any more of a test than is sufficient to fail, and failing to compile is considered failing. You are not allowed to write any more production code than is sufficient to pass the currently failing test.”

- Kent Beck, *Test-Driven Development: By Example*

These constraints are not arbitrary. They are boundaries designed to protect us from ourselves, from speculative design, overengineering, and early coupling. By forcing us to move in small, safe, deliberate steps, these laws help us build systems that are better structured, easier to change, and more resilient to uncertainty.

As **Sandro Mancuso** argues in *The Software Craftsman* 🛠️:

> “Without discipline, technical practices, and responsibility, Agile becomes just a chaotic set of rituals.”

TDD, when practiced well, is an act of responsibility. It elevates how we write code and how we think about design, intent, and professional behavior. It is not a testing tool, it’s a thinking framework. It is how we externalize design decisions into code, creating **living documentation** that grows with the product and protects its intent over time.

From an economic perspective, **Luis Artola** in *Software Economics* frames software development as the act of managing irreversible decisions under uncertainty. TDD supports this idea by giving us **rapid feedback** and protecting our ability to adapt without excessive cost:

> “The true cost in software does not come from the work done, but from the future options it limits.”

- Luis Artola, *Software Economics*

Every small test clarifies intent, reduces ambiguity, and exposes inconsistencies early, when they are still cheap to fix. In economic terms, TDD helps us preserve the flexibility to change, which is our most valuable asset in a dynamic market.

But beyond design and economics, the strongest argument for TDD may be **human**. Codebases do not collapse in a single moment, they erode slowly, one rushed decision at a time. TDD counters this decay, not with grand refactors, but with daily maintenance. As **Martin Fowler** explains in *Refactoring*:

> “If you don't actively manage your design, it will decay. To keep your software healthy, you have to invest continuously in keeping it clean and coherent.”

Practiced regularly, TDD becomes more than a workflow, it becomes a **habit of thinking**. At first, it may feel slower and more constrained. But over time, it becomes empowering. Developers gain clarity. Feedback accelerates learning. Risk becomes visible and manageable. And progress becomes sustainable.

> “The act of writing a test first makes you think twice about the design. That’s a good thing.”

- Steve Freeman &amp; Nat Pryce, *Growing Object-Oriented Software, Guided by Tests*

In the next section, we will explore the **TDD cycle** in detail: what it looks like in action, why each phase matters, and how it helps us reason about behavior, design, and confidence, one test at a time.

---

## ❌ What TDD is *Not* - unlearning the misconceptions first

Before we go deeper, let’s pause and clear the slate. If we’re going to learn something well, we first need to let go of what we *think* we know.

Test-Driven Development is not what many people believe it is. And that confusion is costly, in time, quality, and trust.

Here are the most common myths and misconceptions 👇

---

### 🚫 TDD is not “writing tests before code”

Let’s be very specific here.

Writing a test before you write your production code is a *necessary condition* for TDD, but it is **not sufficient**.

TDD is not about testing. It’s not about being “test-first.” It’s about using tests to **drive the design** of the code through **incremental feedback loops**.

As Kent Beck explains in *TDD by Example*:

> “The trick is to get to green as quickly as possible, not to write the test first.”

The test is a **thought experiment**, not a verification script. You write the test to **discover** what the code should do, not to confirm what you’ve already implemented.

TDD isn’t test-first. It’s **design-first, with tests as the vehicle**.

---

### 🚫 TDD is not about exhaustive testing

This is another trap. TDD does not aim for 100% coverage, or some abstract measure of testing completeness. It’s not about writing every possible test for every possible path.

TDD is about **writing just enough test to guide the next slice of design**.

As you move, you verify only what you **need to verify**. You keep the loop tight. You test what **matters**, not what might matter in some imagined future.

TDD gives you **confidence in the behavior you care about right now**, and the design to safely evolve that behavior later.

In other words:

> “You don’t write tests to prove you’re right. You write tests to be free to change your mind.”

- *inspired by Kent Beck*

---

### 🚫 TDD is not about tools or frameworks

There is no special IDE, no required mocking library, no magic test runner that makes something TDD.

TDD is a **discipline**, not a setup.

The core materials are simple:

- A way to write tests
- A way to run them fast
- A willingness to let the tests shape your thinking

As Sandro Mancuso argues in *The Software Craftsman*:

> “TDD is not about tools. It’s about commitment to quality, responsibility, and design.”

Frameworks can help. But they can also get in the way.

The best tool you can bring to TDD is your **attention**.

---

### 🚫 TDD is not QA

This one is critical.

TDD is not a quality assurance strategy. It is a **development strategy**, a **thinking process**, for designing code with clarity and intent.

It does not replace exploratory testing, boundary testing, stress testing, or user validation.

You use TDD to **design with confidence**. You use QA to **validate what you missed**.

They complement each other. One does not replace the other.

---

### 🚫 TDD is not “just for backend code”

Another misconception is that TDD only works when you’re writing pure functions or backend logic.

Not true.

TDD works anywhere you want to **discover behavior safely and incrementally**. That includes:

- UI components (with thoughtful design and inversion)
- APIs and contract tests
- Infrastructure as code
- System configuration
- Even machine learning pipelines or data transformations

The key is designing **for testability**, not just to test, but to **decouple your design** and enable feedback.

> “If it’s hard to test, that’s a signal, not a blocker.”

- *Inspired by The Programmer’s Brain* &amp; *Growing OO Software*

---

### 🚫 TDD is not for “perfect” developers

TDD is not a purity contest. It’s not about never breaking the rules or always getting it right.

It’s about building software through a process of **safe, structured trial and error**.

You don’t need to be perfect. You just need to be **deliberate**.

---

## ✅ So… What *is* TDD then?

TDD is:

- A **thinking discipline** that structures your design decisions
- A way to keep software **flexible and safe to change**
- A mechanism for **delaying decisions** until you have more evidence
- A daily habit that builds **trust**, in your code, your teammates, and yourself

In the words of Luis Artola:

> “Software is a tool for deferring decisions until the last responsible moment. TDD is how we protect that delay.”

And in the words of Kent Beck:

> “The real value of TDD is that it makes you *think*, about behavior, design, and intent.”

If you're doing TDD and you don't feel like you're thinking more deeply about your code, your interfaces, and your responsibilities, you're probably not doing TDD yet.

That’s okay. This is a journey. Let’s walk it with eyes wide open.

[![](https://substackcdn.com/image/fetch/$s_!V6Z_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1c5264b-8581-4ce6-ba09-d2c0588885a5_1488x787.png)](https://substackcdn.com/image/fetch/$s_!V6Z_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1c5264b-8581-4ce6-ba09-d2c0588885a5_1488x787.png)

---

## The TDD methodology and its canonical flow 🔄📐

Test-Driven Development is often reduced to the slogan “red-green-refactor,” but behind this seemingly simple loop lies a rich discipline with deep implications for **software design, system evolution, and developer thinking**. The TDD cycle is a **design method**, a **learning process**, and a **feedback engine**.

Let’s unpack the full meaning of this cycle, guided by the canonical process and enriched by experience, theory, and core literature. We'll revisit this flow repeatedly as we apply it to real, world katas, but here we establish its conceptual foundation.

[![](https://substackcdn.com/image/fetch/$s_!NsDO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff74899b1-0e3f-49a9-a994-0935baa8dc1a_1830x1104.png)](https://substackcdn.com/image/fetch/$s_!NsDO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff74899b1-0e3f-49a9-a994-0935baa8dc1a_1830x1104.png)

### The flow: red → green → refactor

TDD works through a **tight loop** of three actions:

[![](https://substackcdn.com/image/fetch/$s_!nRBv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91ac391d-aa18-40d2-8509-402b5f74a660_821x532.png)](https://substackcdn.com/image/fetch/$s_!nRBv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91ac391d-aa18-40d2-8509-402b5f74a660_821x532.png)

- **Red** 🔴 Write a small test that expresses a new behavior. The test must fail - and fail for the *right reason*. This step makes our **assumption visible** and forces us to confront what we don’t know.

- **Green** 🟢 Write the minimal amount of production code to make the test pass. No more. No less. This is the phase of **exploration** and **constrained delivery**. We use it to understand the *simplest mechanism* that satisfies the test.

- **Refactor** 🔵 With the test passing, we can now clean up both the test and the production code. We simplify, remove duplication, clarify intention. Tests give us the **safety net** to change design without fear.

> “TDD isn’t about testing. It’s about design. The tests are just a way to drive it.”

- Kent Beck, *Test-Driven Development: By Example*

This loop happens fast. We move in **baby steps**. Each cycle is a moment of **learning**, where we confirm or update our mental model of the system.

> “Programmers are not typists. Our job is to think, and to learn.”

- Felienne Hermans, *The Programmer’s Brain*

### The Three Laws of TDD

The **three laws of TDD** to encourage strict discipline:

- **You may not write production code unless you have a failing test.**
- **You may not write more of a test than is necessary to fail.**
- **You may not write more production code than is necessary to pass the test.**

These constraints **force learning and simplicity**. They guide us away from overdesign and speculation and toward just-in-time clarity.

> “Each test is a decision. With each passing test, we commit to a shape, a path, in our design.”

- Freeman &amp; Pryce, *Growing Object-Oriented Software, Guided by Tests*

When practiced with discipline, this creates a **living system** that grows around real needs and real constraints, not imagined futures.

---

## 🔁 Feedback loops: designing with decisions in mind

> “TDD is not a ritual. It’s a way to make better decisions under uncertainty, by shrinking the gap between intent and outcome.”

In modern software systems, **uncertainty is not a bug**, it’s the environment. Requirements shift. Codebases age. People rotate. Markets change. In this ever-evolving landscape, our job is not to **control** the system but to create processes that make it **adaptive**. TDD is one of the strongest tools we have for doing exactly that.

At its core, **Test-Driven Development is a feedback system**. Each Red → Green → Refactor cycle gives us a tight, observable loop between what we believe should happen and what actually does. This matters. Because, as Kent Beck points out in *Tidy First?*, every design choice we make is also a **learning moment**, and learning only works if you can see the outcome of your choices clearly and quickly.

> “Structure and behavior are different things. And you can only improve structure if behavior is already protected.”

- Kent Beck, *Tidy First?*

In economic terms, Luis Artola frames software development as the ongoing negotiation of **irreversible decisions**. The value of TDD is that it **de-risks decision-making** by shortening the feedback loop: we don’t have to commit to big designs upfront. Instead, we can test one idea, observe the outcome, and adapt.

This aligns with Donella Meadows’ system thinking: the most powerful interventions in complex systems are often **feedback loops**. The faster and clearer the feedback, the safer the evolution. In TDD, every test is a micro-feedback unit. It tells us immediately when we’ve broken something, misunderstood a requirement, or created unnecessary complexity.

### ⚙️ How Feedback Loops in TDD Work

[![](https://substackcdn.com/image/fetch/$s_!MV0n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45e0f04d-5865-456f-b2bf-34ecd30ac150_1486x356.png)](https://substackcdn.com/image/fetch/$s_!MV0n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45e0f04d-5865-456f-b2bf-34ecd30ac150_1486x356.png)

With each cycle, we tighten the **gap between intent and outcome**, shrinking the cost of failure while increasing the precision of feedback. We don’t just write better code, we become better **system thinkers**.

> “Every clean green test is a conversation with the future. It tells you what the system should do and gives you the safety to change it.”

- Inspired by *Growing Object-Oriented Software, Guided by Tests*

TDD isn’t just craftsmanship, it’s **strategic clarity**. It's how we build systems that respond, adapt, and grow with confidence, even as everything else changes.

### The test list 📝

Before diving into a cycle, we often begin with a **test list**, a written queue of behaviors we expect to support. These are not commitments. They are **intentions**, a rough backlog of cases we might explore.

Example:

```
- should return "1" when given 1
- should return "2" when given 2
- should return "Fizz" when given 3
- should return "Fizz" when given 6
- should return "Fizz" when given 9
- should return "Buzz" when given 5
- should return "Buzz" when given 10
- should return "Buzz" when given 20
- should return "FizzBuzz" when given 15
- should return "FizzBuzz" when given 30
- should return "FizzBuzz" when given 45
```

As we write and refactor, the list changes. We **remove** what’s done, **add** what’s discovered, and **reorder** based on what’s next. The list is a tool to focus our thoughts, not a specification document.

> “Test lists are a scaffolding for thought. They help you plan your exploration, not predict your future.”

- Kent Beck, *TDD by Example*

---

### Failing for the right reason ❌🎯

In the **Red phase**, we must ensure that the test fails for the reason we expect: the **assertion** we wrote is not yet true.

If the failure comes from a compiler error, a misnamed method, or a setup mistake, we haven’t reached the real red yet. We're still correcting **syntax or setup**, not testing behavior.

This practice trains **hypothesis-driven development**: we form a belief, encode it as a test, and then check whether it holds.

---

### Fake it until you make it 🤖

When we reach the **green phase** of the TDD cycle, after having written a test that fails for the right reason, we now ask: *“What’s the simplest thing I can do to make this test pass?”*

Often, the answer is not the “final” solution.

Instead, we **fake it**.

```
fun fizzBuzz(n: Int): String {
    return "1"
}
```

Yes, it’s hard-coded. Yes, it looks ridiculous. But it’s **intentional**. This style of implementation is known as **Fake it until you make it**.

#### Why fake it?

- **We avoid overthinking.** Rather than trying to predict all future requirements, we focus on **this test**. That’s enough.

- **We limit the scope.** Our implementation is laser-focused on passing a single test case. We’re not writing code we don’t need yet.

- **We allow the design to emerge.** With more examples, patterns will **emerge from necessity**, not imagination.

- **We learn by feedback.** With every passing test, we gain a piece of knowledge about the shape our solution should take.

---

### What about *triangulation*? 🎯

[![](https://substackcdn.com/image/fetch/$s_!9SqY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76943985-e8c5-4f24-b1fa-0e55714335cd_7920x4320.png)](https://substackcdn.com/image/fetch/$s_!9SqY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76943985-e8c5-4f24-b1fa-0e55714335cd_7920x4320.png)

Once we have faked our way through **two similar tests**, we still don't abstract.

But when we write a **third** test that reveals the **same pattern**, we’ve reached the point where generalizing starts to make sense.

This is the **Rule of Three**, or **Triangulation**.

> “Don’t abstract until you’ve repeated something three times.”

- Kent Beck, *Test-Driven Development: By Example*

Let’s illustrate this in the context of the *FizzBuzz* kata.

---

#### Triangulation in practice: numbers that are not Fizz or Buzz

We start by writing a test for input 1:

```
@Test fun `returns 1 for input 1`() {
    assertEquals("1", fizzBuzz(1))
}
```

We fake it:

```
fun fizzBuzz(n: Int): String {
    return "1"
}
```

Next test, for input 2:

```
@Test fun `returns 2 for input 2`() {
    assertEquals("2", fizzBuzz(2))
}
```

We fake it again:

```
fun fizzBuzz(number: Int): String {
    if (number == 2) {
        return "2"
    }

    return "1"
}
```

Now the third case: 4

```
@Test fun `returns 4 for input 4`() {
    assertEquals("4", fizzBuzz(4))
}
```

We fake it once more:

```
fun fizzBuzz(number: Int): String {
    if (number == 2) {
        return "2"
    }

    if (number == 4) {
        return "4"
    }

    return "1"
}
```

At this point, we pause. What are we seeing?

Each test expects the number to be returned as a string, unless the number is a multiple of 3 or 5. But we haven’t seen those yet. For now, **this logic repeats** with no variation.

We’ve seen the same behavior **three times**. Now, and **only now**, we can consider **refactoring**:

```
fun fizzBuzz(number: Int): String {
    return number.toString()
}
```

This is a classic triangulation moment.

🟢 We’ve **proven** through test repetition that this behavior is not an exception, it’s a pattern.

🧠 And importantly, we’ve avoided generalizing prematurely. Had we written this `toString()` logic after only one or two tests, we would have assumed too much, and risked **locking ourselves into the wrong abstraction**.

---

### Why does this matter?

Because many developers **rush abstraction**.

They see a pattern, assume it will hold, and jump to a generalized solution. But that assumption often proves wrong, and then you’re stuck unraveling it later.

> "Duplication is far cheaper than the wrong abstraction."

- Sandi Metz, *Practical Object-Oriented Design in Ruby*

🧼 The cost of small duplication is trivial compared to the cost of bad design choices. 🚨 And **tests give us the evidence** we need to **build our system empirically**, not speculatively.

---

### Takeaways

- **Fake it until you make it** allows you to start from certainty, not guesswork.
- **Triangulation** delays abstraction until the pattern has been proven through at least 3 examples.
- This process **reduces cognitive load**, improves flexibility, and strengthens the link between tests and design.

🔁 It is not laziness. It is **disciplined restraint**.

### Obvious implementation 💡

In TDD, after writing a failing test and watching it fail for the right reason, our next step is to write **just enough production code to make the test pass**. One strategy for this is the **obvious implementation**, writing the simplest general solution when it's so clearly correct that writing a fake return value would be contrived or slower.

Kent Beck uses this approach in *Test-Driven Development by Example*, particularly in the chapter where he’s working through the multiplication logic for a Dollar class. For instance, when testing Dollar(5) * 2 == Dollar(10), he might write a hardcoded return initially, but then once he sees that multiplication logic will repeat with other values like 3 or 4, he jumps to the real formula:

```
fun times(multiplier: Int): Dollar {
    return Dollar(amount * multiplier)
}
```

This leap is possible **only because**:

- The correct implementation is **trivial** and **obvious**.
- The abstraction is backed by **multiple test cases** (a form of triangulation).
- The programmer **fully understands the domain behavior** (money multiplication is straightforward).

> "I could write just enough code to pass the test, but the correct implementation is obvious. So I’ll go ahead and do it."

- *Kent Beck*, *Test-Driven Development by Example*

However, problems arise when developers **assume** they know the right abstraction too early, particularly in more complex or less well-understood domains. This leads to **premature abstraction**, the enemy of evolutionary design.

As Sandi Metz reminds us:

> "Duplication is far cheaper than the wrong abstraction."

And this is why Kent Beck introduces the **fake-it** and **triangulation** strategies, not as crutches, but as **design constraints** that help us avoid generalizing prematurely.

#### How to decide between Fake-it and Obvious implementation?

Ask yourself:

- Have I already seen at least **two other examples** of this behavior?
- Is the implementation **absolutely trivial**?
- Am I introducing **zero design decisions**?

If the answer is **yes**, go ahead. Otherwise, prefer fake-it or write another small test to guide you there.

#### Trust your discomfort

Discomfort is a key signal in TDD. If you're unsure whether your implementation is obvious or speculative, **lean toward safety**. Add another test. Use fake-it. Observe more.

As Kent Beck writes:

> "Don't rush to abstraction. Let it come to you."

This patient mindset is what transforms TDD from a testing technique into a **design discipline**.

---

### Refactor: the designer's playground 🧼🧱

Once our test goes green, we enter the phase of **refactor**. In Test-Driven Development, this is not an optional polish or an afterthought, it is an essential act of design. Here, we make the code not just work, but **work well**: clean, expressive, modular, and understandable.

To refactor is to improve the **structure of code without changing its behavior**. As Kent Beck emphasizes in *Tidy First?*, structure and behavior are two sides of a codebase. The behavior defines what the system does. The structure defines how we, as humans, can understand, extend, and reason about that behavior. Refactoring protects the future. It ensures that the system remains adaptable, understandable, and safe to evolve.

Martin Fowler famously formalized refactoring as a catalog of small, behavior, preserving transformations. But Kent Beck adds a crucial nuance: before we even perform classic refactorings like extracting methods or renaming variables, we might need to **tidy**. Tidying, as Beck defines it, is a pre-refactor, a micromovement that gently improves the code’s shape in safe, local steps. Examples include deleting dead code, adding guard clauses, normalizing naming patterns, or moving declarations closer to their usage. These actions are not tracked on Jira. They are not designed in advance. But they build momentum. Tidying makes the next change easier.

> "You tidy to make the next change easier. You refactor to improve the system's structure. Both are design. Both matter."

- Kent Beck, *Tidy First?*

Unlike a traditional design phase, **refactoring is not planned**. We don’t say, “we’ll spend two weeks cleaning the code.” That mindset almost always fails. Instead, we adopt a **continuous design rhythm**. As we build behavior incrementally, we also improve structure incrementally. One change at a time. One step at a time. Always with the safety net of passing tests. This alternation, behavior, then structure, is what Kent Beck calls **empirical software design**. Design evolves, like sculpture, through small, observable changes, not grand rewrites.

In the refactor phase, we often do things like:

- Remove duplication
- Extract or inline functions
- Improve names to make intention clearer
- Simplify conditional logic
- Reshape data structures
- Make dependencies explicit

We may also **refactor the tests**. Tests are first-class citizens in our design system. As Beck reminds us, tests are the first client of our code. If our test is hard to write or read, that is a design smell. During refactor, we might rename the test for clarity, extract helpers to remove duplication, or consolidate repetitive cases into **parameterized tests**, a technique especially useful when we apply the **Rule of Three** to discover generality from repeated specific examples.

#### Tidy vs Refactor: a useful distinction

Tidying and refactoring are often conflated, but their difference is subtle and important:

- **Tidying** is local, frictionless, and safe. You do it when you see it. You don’t need permission. You change names, move things around, or simplify expressions to make the next step clearer.
- **Refactoring**, while also safe by design, may involve more structural change. It may require thought, sequencing, and collaboration. It is where we **reshape the code’s design**, often in preparation for, or immediately after, a behavior change.

> “Big design changes feel impossible? Take smaller steps. Still too big? Take even smaller ones.”

- Kent Beck, *Tidy First?*

Tidyings are small acts of respect. They are how we make the code kinder to the next reader, often ourselves. They are also how we **train our design senses**: by seeing patterns, clarifying intentions, and leaving the code better than we found it.

#### The green safety net

Refactor lives under the protection of green tests. The feedback loop is immediate. If the test turns red, we know we’ve broken something, and we can fix it fast. This safety unlocks creativity. It allows us to take risks with structure, to try new designs, to make the code truly reflect its purpose.

Refactoring is not something we do when we have time. It is something we build into our flow. It is an act of responsibility and an expression of professionalism. In the words of *The Software Craftsman*:

> “Technical debt is not technical, it is cultural.”

- Sandro Mancuso, *The Software Craftsman*

We refactor to honor the craft. To invest in future velocity. To leave a system better, safer, clearer. Every refactor is a gift to the team, a small act of stewardship for the long life of the code.

**> "If it hurts, do it more often, and bring the pain forward."**

- *Martin Fowler, Refactoring: Improving the Design of Existing Code*

---

## 🎯 Practical Application: The FizzBuzz Kata

FizzBuzz is a perfect starting kata for practicing TDD. It’s simple, well-known, and has just enough branching logic to illustrate essential TDD techniques like:

- Test List
- Red-Green-Refactor cycle
- Fake it until you make it
- Triangulation
- Parameterization
- And careful abstraction

We’ll walk through it step by step, using **Kotlin** as our language, while making the TDD thinking process fully explicit. Our goal is not just to solve the kata, but to **understand how we arrive at each step through discipline, observation, and feedback**.

---

## 📝 The Test List

> A test list is not a plan. It’s a conversation with the future.

Before writing any tests, we take a moment to think: What behaviors do we expect to see?

This gives us a **Test List**: a scratchpad of the expected outcomes, not ordered by complexity or priority but by intent.

```
- should return "1" when given 1
- should return "2" when given 2
- should return "Fizz" when given 3
- should return "Fizz" when given 6
- should return "Fizz" when given 9
- should return "Buzz" when given 5
- should return "Buzz" when given 10
- should return "Buzz" when given 20
- should return "FizzBuzz" when given 15
- should return "FizzBuzz" when given 30
- should return "FizzBuzz" when given 45
```

We will **triangulate** each behavior family (plain numbers, Fizz, Buzz, FizzBuzz) and **only generalize once patterns emerge**. This protects us from premature abstraction.

Let’s begin 🔧

---

## 🔴 First Red: The First Test

### ❓ Which test should we write first?

Following the **Fake it until you make it** philosophy, we want to start **as simply as possible**, with a case that doesn’t force us to deal with Fizz or Buzz yet.

Let’s pick:

```
@Test
fun `should return 1 when given 1`() {
    assertEquals("1", fizzBuzz(1))
}
```

### 🔎 Compilation Error: Fails to Compile (First Red)

At this point, we don’t even have a function named fizzBuzz. So this is a good **first failure**. TDD teaches us that **"failing to compile is failing."** That’s okay, it means we’ve taken our first real step in the cycle.

✅ Fix compilation only:

```
fun fizzBuzz(n: Int): String {
    TODO("Not yet implemented")
}
```

But now, the test fails at runtime with:

```
kotlin.NotImplementedError: An operation is not implemented
```

That’s still not the right failure.

We want to fail **on the assertion**, not on the structure.

```
fun fizzBuzz(number: Int): String {
    return ""
}
```

Now we run the test and see:

```
Expected :1
Actual   :
```

🎉 Success! Not because the test passes, but because it **fails for the right reason**.

> “We write the failing test not to see red, but to verify our hypothesis.”

- Kent Beck, *Test-Driven Development by Example*

At this moment, our hypothesis is: ❝For input 1, the output should be "1".❞

We now know the test is **asserting behavior**, not structure or noise.

### 🟢 Green: Fake it and begin triangulating

In the **first red** phase, we wrote:

```
@Test
fun `should return "1" when given 1`() {
    assertEquals("1", fizzBuzz(1))
}
```

We made it pass with the simplest possible code:

```
fun fizzBuzz(number: Int): String {
    return "1"
}
```

---

### 🔴 Red: Given a 2 should return 2

```
@Test
fun `should return "2" when given 2`() {
    assertEquals("2", fizzBuzz(2))
}
```

It fails with:

```
Expected :2
Actual   :1
```

This is a **failure for the correct reason**: our current implementation always returns "1", but we want it to return the actual number as a string. However, we’re still in **fake-it mode**, so we don’t jump to the general solution yet.

---

### 🟢 Green: Given a 2 should return 2

We extend our when block to fake "2" as well:

```
fun fizzBuzz(number: Int): String {
    return when (number) {
        1 -&gt; "1"
        else -&gt; "2"
    }
}
```

Both tests pass ✅. But we’re still **hardcoding** values - intentionally delaying generalization to avoid premature abstraction.

---

### 🔴 Red: Given 4 should return 4

```
@Test
fun `should return "4" when given 4`() {
    assertEquals("4", fizzBuzz(4))
}
```

Fails with:

```
Expected :4
Actual   :2
```

---

### 🟢 Green: Given 4 should return 4

Still faking our way through one case at a time. We update the function:

```
fun fizzBuzz(number: Int): String {
    return when (number) {
        1 -&gt; "1"
        2 -&gt; "2"
        else -&gt; "4"
    }
}
```

🎯 All three tests pass - we’re still duplicating intentionally. At this stage, we now have **three examples** of the same kind of behavior. This repetition signals an opportunity to generalize.

---

### 🔵 Refactor: Triangulation and safe generalization

Now that we’ve seen the same behavior repeat three times, returning the input as a string, we’re ready to refactor confidently. This is **triangulation**: using multiple data points to justify an abstraction.

> “Triangulation helps us resist the urge to generalize prematurely. Duplication is not a failure, it’s data.”

- Inspired by *Kent Beck*

We refactor the function to:

```
fun fizzBuzz(number: Int): String {
    return number.toString()
}
```

This is a safe, grounded improvement. We no longer need to fake each value, we’ve **emerged** the correct abstraction through disciplined steps.

🧼 We also take this moment to clean our tests, maybe by organizing them or updating their names if needed. That’s the full value of the **refactor phase**: we strengthen both production and test code without fear, because our green tests keep us safe.

We now have multiple tests that verify the same type of behavior: when the number is not divisible by 3 or 5, we just return the number as a string. This is pure duplication in **intention**, so we can consolidate these into a **parameterized test**.

This isn’t just about reducing lines of code, it's about **clarity** and **intention**. By grouping these examples under a shared test, we make the **business rule** behind them more visible.

---

### 🔵 Refactor the tests: group non-FizzBuzz numbers

Here’s the refactored version using JUnit 5’s `@ParameterizedTest` with `@ValueSource`:

```
@ParameterizedTest(name = "should return \"{0}\" when number is not divisible by 3 or 5")
@ValueSource(ints = [1, 2, 4])
fun `should return number as string when not divisible by 3 or 5`(number: Int) {
    assertEquals(number.toString(), fizzBuzz(number))
}
```

---

### ✅ Why this matters

- The **name** of the test now expresses the rule: "return the number as a string when it’s not Fizz or Buzz".
- It **communicates business behavior**, not just mechanics.
- If a new such case arises (e.g., 7), we can simply **add to the input list**, not duplicate test logic.
- It makes reading and maintaining the test easier, and more resilient to change.

---

💡 **Design Insight**: This test now acts as a **specification**, it communicates an explicit contract with the system. That’s part of what makes TDD powerful when done with care: tests become living documentation of the business behavior.

### 🔴 Red: Add the first “Fizz” test (number divisible by 3)

We introduce a new test:

```
@Test
fun `should return Fizz when number is divisible by 3`() {
    assertEquals("Fizz", fizzBuzz(3))
}
```

Fails with:

```
expected: "Fizz"
but was: "3"
```

✅ Good. The test fails for the **right reason**: the output didn’t match our assertion. This confirms our hypothesis is testable and that we’re in the **red** phase properly.

---

### 🟢 Green: Fake it until you make it 🤖

To pass the test **safely**, we add a specific case for the number 3 - faking the implementation:

```
fun fizzBuzz(number: Int): String {
    return when (number) {
        3 -&gt; "Fizz"
        else -&gt; number.toString()
    }
}
```

This is a textbook example of **Fake it until you make it**: We hardcode the result just for 3, even though we *know* what the general rule is. We're deliberately delaying generalization. Why?

> Because one case is not a pattern. It's an exception.

🟢 The test now passes. Great.

### 🔵 Refactor: 🧼 Not yet - we need to triangulate first

We don’t have enough repetition yet to extract the "Fizz" behavior. Refactoring now would mean guessing the rule prematurely - which would violate the discipline of **triangulation**.

Let’s update our test list and prep for the next step.

#### 📋 Updated test list

```
✔ should return "1" when given 1
✔ should return "2" when given 2
✔ should return "4" when given 4
✔ should return "Fizz" when given 3
🔜 should return "Fizz" when given 6
🔜 should return "Fizz" when given 9
- should return "Buzz" when given 5
- should return "Buzz" when given 10
- should return "Buzz" when given 20
- should return "FizzBuzz" when given 15
- should return "FizzBuzz" when given 30
- should return "FizzBuzz" when given 45
```

---

### 🔴 Red: Given a 6 should return Fizz

We want to begin triangulating. That means we now add a second example that should also result in "Fizz", to build evidence of a pattern.

```
@Test
fun `should return Fizz when number is divisible by 3 - example 6`() {
    assertEquals("Fizz", fizzBuzz(6))
}
```

Fails with:

```
expected: "Fizz"
but was: "6"
```

✅ Excellent, it fails for the **right reason**. The function returns "6" instead of "Fizz". This confirms we are on the correct track, and still within the Red phase boundaries.

---

### 🟢 Green: Given a 6 should return Fizz

Let’s not generalize yet. Instead, we continue **faking** it safely by adding the special case for 6.

```
fun fizzBuzz(number: Int): String {
    return when (number) {
        3 -&gt; "Fizz"
        6 -&gt; "Fizz"
        else -&gt; number.toString()
    }
}
```

Now the test for 6 passes ✅ We’re still keeping things simple and only handling exactly what is needed.

---

### 🔵 Refactor 🧼 (Still too early to generalize!)

This is only the **second occurrence**. Still not enough evidence. Let’s hold off refactoring and triangulate further.

> “Don’t generalize before you’ve been burned by the repetition.” – Kent Beck, *Test-Driven Development: By Example*

We still have one more case in our 📋 test list to prepare for triangulation.

---

### 📋 Updated test list

```
✔ should return "1" when given 1
✔ should return "2" when given 2
✔ should return "4" when given 4
✔ should return "Fizz" when given 3
✔ should return "Fizz" when given 6
🔜 should return "Fizz" when given 9
...
```

Perfect 👣 Let’s move into the third "Fizz" case (9), where we’ll complete the triangulation and earn the right to generalize 💡

---

### 🔴 Red: Given a 9 should return Fizz

This is the **final step in our triangulation**. After this, we should be able to extract the pattern that defines "Fizz".

```
@Test
fun `should return Fizz when number is divisible by 3 - example 9`() {
    assertEquals("Fizz", fizzBuzz(9))
}
```

Fails with:

```
expected: "Fizz"
but was: "9"
```

Perfect! 🛑 We’re still failing for the correct reason, the test is checking our hypothesis and finds it untrue. That’s what we want in the **Red** phase.

---

### 🟢 Green: Given a 9 should return Fizz

We now have:

- 3 -&gt; "Fizz"
- 6 -&gt; "Fizz"
- 9 -&gt; "Fizz"

⚠️ If we were to add a third fake for 9, our code would look like this:

```
fun fizzBuzz(number: Int): String {
    return when (number) {
        3 -&gt; "Fizz"
        6 -&gt; "Fizz"
        9 -&gt; "Fizz"
        else -&gt; number.toString()
    }
}
```

While that would still be correct and valid, we now have **enough duplication** to **triangulate** 🧠

---

### 🔵 Refactor 🧼: Apply the triangulation

We now ask: what pattern do 3, 6, and 9 share?

They are all **divisible by 3**.

Let’s implement that abstraction:

```
fun fizzBuzz(number: Int): String {
    if (number % 3 == 0) {
        return "Fizz"
    }

    return number.toString()
}
```

### ✅ All previous tests still pass!

Let’s double check:

- "Fizz" for 3 → ✅
- "Fizz" for 6 → ✅
- "Fizz" for 9 → ✅
- "1", "2", "4" return themselves → ✅

Lets parametrize the test

```
@ParameterizedTest()
@ValueSource(ints = [3, 6, 9])
fun `should return Fizz as string when not divisible by 3`(number: Int) {
    assertEquals("Fizz", fizzBuzz(number))
}
```

---

#### 💡 What did we learn?

We just saw the **Rule of Three** in action:

> “Once is coincidence, twice is suspicious, three times is a pattern.”

Triangulation helped us **avoid premature abstraction**, while steadily growing confidence in the design.

This form of **emergent behavior discovery** is at the heart of TDD. Our code now reflects a deeper business rule: *“Return 'Fizz' for numbers divisible by 3.”*

---

#### 📋 Updated test list

```
✔ should return "1" when given 1
✔ should return "2" when given 2
✔ should return "4" when given 4
✔ should return "Fizz" when given 3
✔ should return "Fizz" when given 6
✔ should return "Fizz" when given 9
🔜 should return "Buzz" when given 5
🔜 should return "Buzz" when given 10
🔜 should return "Buzz" when given 20
- should return "FizzBuzz" when given 15
- should return "FizzBuzz" when given 30
- should return "FizzBuzz" when given 45
```

---

### 🔴 Red: Given a 5 should return Buzz

Our hypothesis: if a number is divisible by 5, it should return "Buzz".

Let’s encode this as a test:

```
@Test
fun `should return Buzz when number is divisible by 5 - example 5`() {
    assertEquals("Buzz", fizzBuzz(5))
}
```

Fails with:

```
expected: "Buzz"
but was: "5"
```

✅ This is a **clean Red**: we’re failing for the right reason, our implementation is not yet handling divisibility by 5. This confirms our test expresses real behavior and our hypothesis is meaningful.

---

### 🟢 Green: Given a 5 should return Buzz

Just like with Fizz, we **don’t generalize yet**. We fake it with a hardcoded check:

```
fun fizzBuzz(number: Int): String {
    if (number % 3 == 0) {
        return "Fizz"
    }

    if (number == 5) {
        return "Buzz"
    }

    return number.toString()
}
```

🟢 Test passes!

Yes, it’s hardcoded, but that’s **intentional**. We’re isolating behavior before we attempt generalization.

---

### 🔵 Refactor 🧼: Not yet - one case is not a pattern

We’ve only seen "Buzz" once. Let’s follow our rule of thumb: **don’t generalize before the third example**.

---

#### 📋 Updated test list

```
✔ should return "1" when given 1
✔ should return "2" when given 2
✔ should return "4" when given 4
✔ should return "Fizz" when given 3
✔ should return "Fizz" when given 6
✔ should return "Fizz" when given 9
✔ should return "Buzz" when given 5
🔜 should return "Buzz" when given 10
🔜 should return "Buzz" when given 20
- should return "FizzBuzz" when given 15
- should return "FizzBuzz" when given 30
- should return "FizzBuzz" when given 45
```

### 🔴 Red: Given 10 should return Buzz

We're now encoding a second example of "Buzz" behavior:

```
@Test
fun `should return Buzz when number is divisible by 5 - example 10`() {
    val result = fizzBuzz(10)
    assertEquals("Buzz", result)
}
```

Fails with:

```
expected: "Buzz"
but was: "10"
```

✅ Perfect, we are still failing for the **correct reason**. This test is telling us that our current logic does not handle 10 properly. That’s a clear signal: we’re still within the **Red** phase boundaries and ready to move.

---

### 🟢 Green: Given 10 should return Buzz

No generalization yet. We’re still in **Fake it until you make it** mode, so we treat this as a special case:

```
fun fizzBuzz(number: Int): String {
    if (number % 3 == 0) {
        return "Fizz"
    }

    if (number == 5) {
        return "Buzz"
    }

    if (number == 10) {
        return "Buzz"
    }

    return number.toString()
}
```

🟢 Both tests for 5 and 10 now pass ✅

Yes, this is duplicated behavior, **on purpose**. Our discipline tells us to wait until we see three cases before making a design decision.

---

### 🔵 Refactor 🧼: Not yet - triangulation needs one more step

We're holding off abstraction until we hit the **third example**. This approach ensures our abstractions are **grounded in evidence**, not guesses.

#### 📋 Updated test list

```
✔ should return "1" when given 1
✔ should return "2" when given 2
✔ should return "4" when given 4
✔ should return "Fizz" when given 3
✔ should return "Fizz" when given 6
✔ should return "Fizz" when given 9
✔ should return "Buzz" when given 5
✔ should return "Buzz" when given 10
🔜 should return "Buzz" when given 20
- should return "FizzBuzz" when given 15
- should return "FizzBuzz" when given 30
- should return "FizzBuzz" when given 45
```

Perfect 💡 Let’s close the loop on the "Buzz" behavior with our third example: 20. This will give us the evidence we need to safely generalize through **triangulation**.

---

### 🔴 Red: Given a 20 should return 20

```
@Test
fun `should return Buzz when number is divisible by 5 - example 20`() {
    assertEquals("Buzz", fizzBuzz(20))
}
```

Fails with:

```
expected: "Buzz"
but was: "20"
```

✅ Excellent. We’re failing for the **right reason** again, we’re now very close to unlocking a refactor.

---

### 🟢 Green: Given a 20 should return 20

We **could**:

```
fun fizzBuzz(number: Int): String {
    if (number % 3 == 0) {
        return "Fizz"
    }

    if (number == 5) {
        return "Buzz"
    }

    if (number == 10) {
        return "Buzz"
    }

    if (number == 20) {
        return "Buzz"
    }

    return number.toString()
}
```

But this is the **third** case, and that means we now have license to generalize through **triangulation** 🔍

---

### 🔵 Refactor 🧼: Time to abstract the "Buzz" rule

We’ve seen "Buzz" returned for 5, 10, and 20. What do they have in common?

👉 All are divisible by **5**

We can safely extract the business rule now:

```
fun fizzBuzz(number: Int): String {
    if (number % 3 == 0) {
        return "Fizz"
    }

    if (number % 5 == 0) {
        return "Buzz"
    }

    return number.toString()
}
```

🧪 All previous tests still pass ✅

- Fizz for 3, 6, 9 → ✅
- Buzz for 5, 10, 20 → ✅
- 1, 2, 4 → ✅

Beautiful. This is **disciplined design** in motion: we abstracted only after evidence made the rule *safe and necessary*.

Lets parametrize the test

```
@ParameterizedTest()
@ValueSource(ints = [5, 10, 20])
fun `should return Buzz as string when not divisible by 5`(number: Int) {
    assertEquals("Buzz", fizzBuzz(number))
}
```

### 📋 Updated test list

```
✔ should return "1" when given 1
✔ should return "2" when given 2
✔ should return "4" when given 4
✔ should return "Fizz" when given 3
✔ should return "Fizz" when given 6
✔ should return "Fizz" when given 9
✔ should return "Buzz" when given 5
✔ should return "Buzz" when given 10
✔ should return "Buzz" when given 20
🔜 should return "FizzBuzz" when given 15
🔜 should return "FizzBuzz" when given 30
🔜 should return "FizzBuzz" when given 45
```

---

### 🔴 Red: Given a 15 should return FizzBuzz

```
@Test
fun `should return FizzBuzz when number is divisible by 3 and 5`() {
    assertEquals("FizzBuzz", fizzBuzz(15))
}
```

Fails with:

```
expected: "FizzBuzz"
but was: "Fizz"
```

✅ Great! We fail for the **correct reason**. Our current implementation correctly returns "Fizz" for 15, because it's divisible by 3, but it does **not yet** account for divisibility by **both** 3 and 5.

This test clearly identifies **a missing behavior**, giving us the green light to evolve the design.

---

### 🟢 Green: Given a 15 should return FizzBuzz

Let’s begin conservatively and fake this case:

```
fun fizzBuzz(number: Int): String {
    if (number == 15) return "FizzBuzz"

    if (number % 3 == 0) return "Fizz"

    if (number % 5 == 0) return "Buzz"

    return number.toString()
}
```

✅ The test now passes!

We’re **faking** only for 15 to isolate the behavior. We resist the urge to generalize too soon. Why? Because:

> “One case is an exception. Two is suspicious. Three is a pattern.”

- *Kent Beck, TDD by Example*

We need **more examples** to justify a proper rule. So let’s triangulate.

#### 📋 Updated test list

```
✔ should return "1" when given 1
✔ should return "2" when given 2
✔ should return "4" when given 4
✔ should return "Fizz" when given 3
✔ should return "Fizz" when given 6
✔ should return "Fizz" when given 9
✔ should return "Buzz" when given 5
✔ should return "Buzz" when given 10
✔ should return "Buzz" when given 20
✔ should return "FizzBuzz" when given 15
🔜 should return "FizzBuzz" when given 30
🔜 should return "FizzBuzz" when given 45
```

### 🔴 Red: Given a 30 should return FizzBuzz

```
@Test
fun `should return FizzBuzz when number is divisible by 3 and 5 - example 30`() {
    assertEquals("FizzBuzz", fizzBuzz(30))
}
```

Fails with:

```
expected: "FizzBuzz"
but was: "Fizz"
```

✅ Again, the test fails for the **right reason**.

Our current implementation:

```
if (number == 15) return "FizzBuzz"
if (number % 3 == 0) return "Fizz"
if (number % 5 == 0) return "Buzz"
```

…returns "Fizz" for 30 because it matches % 3 == 0, and the "FizzBuzz" condition only exists for 15. This confirms the test is targeting a real gap in our implementation.

---

### 🟢 Green: Given a 30 should return FizzBuzz

We’re still in fake-it territory, not enough evidence yet to extract a general rule. So we explicitly add the case for 30:

```
fun fizzBuzz(number: Int): String {
	if (number == 15) {
		 return "FizzBuzz"
	}

	if (number == 30) {
		 return "FizzBuzz"
	}

    if (number % 3 == 0) return "Fizz"
    if (number % 5 == 0) return "Buzz"

    return number.toString()
}
```

✅ Both tests for 15 and 30 now pass.

We’re repeating ourselves intentionally, **waiting until we see three cases** before abstracting.

### 📋 Updated test list

```
✔ should return "1" when given 1
✔ should return "2" when given 2
✔ should return "4" when given 4
✔ should return "Fizz" when given 3
✔ should return "Fizz" when given 6
✔ should return "Fizz" when given 9
✔ should return "Buzz" when given 5
✔ should return "Buzz" when given 10
✔ should return "Buzz" when given 20
✔ should return "FizzBuzz" when given 15
✔ should return "FizzBuzz" when given 30
🔜 should return "FizzBuzz" when given 45
```

### 🔴 Red: Given a 45 should return FizzBuzz

```
@Test
fun `should return FizzBuzz when number is divisible by 3 and 5 - example 45`() {
    assertEquals("FizzBuzz", fizzBuzz(45))
}
```

Fails with:

```
expected: FizzBuzz
but was: 45
```

✅ Great! The test fails **for the right reason**, our function is returning "45" instead of "FizzBuzz". This confirms that we’re still safely in the **Red** phase.

---

### 🟢 Green: Given a 45 should return FizzBuzz

Not anymore!

We've already **triangulated** with:

- 15 → "FizzBuzz"
- 30 → "FizzBuzz"
- 45 → (currently failing but expected "FizzBuzz")

We’ve seen the same behavior enough times to **generalize**.

And in fact, in our previous step, we already did 💡 The current implementation is:

```
fun fizzBuzz(number: Int): String {
	if (number == 15) {
		 return "FizzBuzz"
	}

	if (number == 30) {
		 return "FizzBuzz"
	}

	if (number == 45) {
		 return "FizzBuzz"
	}

    if (number % 3 == 0) return "Fizz"
    if (number % 5 == 0) return "Buzz"

    return number.toString()
}
```

### 🔵 Refactor: final refactor

First small refactor

```
fun fizzBuzz(number: Int): String {
    var result = ""

    if (number % 3 == 0) result += "Fizz"
    if (number % 5 == 0) result += "Buzz"

    return if (result.isNotEmpty()) result else number.toString()
}
```

Improve the function

```
fun fizzBuzz(number: Int): String {
    val result = buildString {
        if (number % 3 == 0) append("Fizz")
        if (number % 5 == 0) append("Buzz")
    }
    return result.ifEmpty { n.toString() }
}
```

Extract modules to more expressive functions

```
fun fizzBuzz(number: Int): String {
    val result = buildString {
        if (isMultipleOfThree(number)) append("Fizz")
        if (isMultipleOfFive(number)) append("Buzz")
    }
    return result.ifEmpty { number.toString() }
}

private fun isMultipleOfThree(number: Int): Boolean = number % 3 == 0

private fun isMultipleOfFive(number: Int): Boolean = number % 5 == 0
```

With this, the test now **passes** ✅, without needing any change to production code!

That’s the **power of triangulation** and **disciplined abstraction**: once the pattern is sound, you don’t need to touch the implementation anymore, the **design holds** 🧱

---

### 🧼 Refactor: nothing to change!

Our function is now:

- Readable
- Maintainable
- Extendable

No duplication, no condition tangle, no guesswork. We’ve *let the tests lead us* to a stable, minimal, and expressive design.

---

## 📋 Final Test List Review ✅

```
✔ should return "1" when given 1
✔ should return "2" when given 2
✔ should return "4" when given 4
✔ should return "Fizz" when given 3
✔ should return "Fizz" when given 6
✔ should return "Fizz" when given 9
✔ should return "Buzz" when given 5
✔ should return "Buzz" when given 10
✔ should return "Buzz" when given 20
✔ should return "FizzBuzz" when given 15
✔ should return "FizzBuzz" when given 30
✔ should return "FizzBuzz" when given 45
```

---

### 🌱 What did we gain?

- Discipline: we followed Red → Green → Refactor without skipping steps
- Design clarity: duplication and behavior guided our generalizations
- Safety: tests protected our code from regressions
- Insight: each test became an example, a specification, and a learning point

TDD isn’t about testing. It’s about **growing reliable, adaptive software through feedback and design**.

Here are **clear, objective conclusions** based on your detailed and comprehensive article on Test-Driven Development (TDD):

---

## ✅ Conclusions on TDD

### TDD is a design process, not a testing activity

Test-Driven Development is not about validating correctness after implementation. It is a disciplined approach to **explore, clarify, and shape design decisions before writing production code**, using tests as a thinking tool.

### The Red–Green–Refactor loop is a feedback-driven engine for learning

Each cycle reveals assumptions, validates expectations, and gives immediate insight into structure and behavior. TDD supports **incremental discovery**, making design safer, clearer, and less speculative.

### TDD protects against uncertainty and design erosion

In a world where requirements shift and knowledge evolves, TDD provides a structure for **de-risking irreversible decisions**. It helps teams move confidently, adapting systems with minimal friction and maximum clarity.

### Code emerges from intention, not mechanics

In TDD, a test encodes intention before implementation. It answers the question: “What should this system do?” The resulting code is not just functional—it is **intentional and explainable**. Tests become **living documentation** of purpose and behavior.

### Fake-it and triangulation are tools for safe discovery

Faking responses and delaying abstraction aren’t shortcuts—they are **strategies to avoid premature design**. TDD encourages developers to wait for real patterns to emerge before generalizing. This leads to stronger, more stable structures.

### Refactoring is part of the flow, not a phase

Clean code is not something you do “later.” TDD embeds **continuous structural improvement** in the development loop. Because behavior is protected by tests, developers can reshape the code confidently and frequently.

### Design emerges from usage, not imagination

Rather than guessing future needs, TDD lets design grow out of real, testable behaviors. Abstractions arise from **repeated examples**, not assumptions. This mindset results in more coherent, decoupled systems.

### Tests are executable design conversations

A well-written test does more than check output—it **explains behavior, preserves decisions, and signals intent**. Tests communicate context, clarify purpose, and provide safety for change. They are a shared language between developers and the future.

### TDD fosters thoughtfulness, not perfectionism

TDD is not about getting it “right” from the start. It is about **moving deliberately**, with clarity and purpose. The method encourages small steps, fast feedback, and steady learning. It builds software—and developers—with resilience.

### The real value of TDD is the judgment it cultivates

More than green bars or coverage metrics, the outcome of TDD is **better decision-making**. It trains developers to be mindful of intent, structure, and evolution. Over time, it strengthens both systems and the people who build them.

## 📚 References

- **Kent Beck**, *Test-Driven Development: By Example*
- **Sandro Mancuso**, *The Software Craftsman*
- **Luis Artola**, *Software Economics*
- **Martin Fowler**, *Refactoring: Improving the Design of Existing Code*
- **Kent Beck**, *Tidy First?*
- **Steve Freeman &amp; Nat Pryce**, *Growing Object-Oriented Software, Guided by Tests*
- **Felienne Hermans**, *The Programmer’s Brain*
- **Donella Meadows**, *Thinking in Systems*
- **Sandi Metz**, *Practical Object-Oriented Design in Ruby*
