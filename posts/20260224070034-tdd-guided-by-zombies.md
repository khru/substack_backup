---
title: "TDD Guided by ZOMBIES"
subtitle: "How to find where to start"
requested_url: "https://emmanuelvalverderamos.substack.com/p/tdd-guided-by-zombies"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/tdd-guided-by-zombies"
substack_post_id: 187498754
retrieved_at: "2026-03-09T08:38:58.117Z"
---
# TDD Guided by ZOMBIES

### How to find where to start

## Introduction

[![](https://substackcdn.com/image/fetch/$s_!0KSx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea0e81fe-b4ff-4ce7-88b5-c70f5f25a84f_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!0KSx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea0e81fe-b4ff-4ce7-88b5-c70f5f25a84f_2816x1536.png)

Test Driven Development is usually taught as a loop: write a failing test, make it pass, refactor. In real work, the hardest part is often earlier than the refactor step. It is staring at a blank editor and asking, “What test should I write next?” James Grenning’s “TDD Guided by ZOMBIES” is a mnemonic and a lightweight decision process that tackles exactly that moment. In his original write up, Grenning describes leaning on ZOMBIES to choose “a logical next step,” to keep tight cause and effect, and to make progress when a problem feels stuck. He also frames it as a way to cultivate “procrastination skills” in a positive sense: intentionally delaying the tricky parts until you have a foundation of working behavior and tests that will keep you honest.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## From ZOM to ZOMBIES: a small idea that grew teeth

[![](https://substackcdn.com/image/fetch/$s_!igTS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F636610a4-f17f-45cd-a777-544040d81cc4_2003x902.png)](https://substackcdn.com/image/fetch/$s_!igTS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F636610a4-f17f-45cd-a777-544040d81cc4_2003x902.png)

ZOMBIES did not appear out of nowhere. Grenning explains that in his book *Test Driven Development for Embedded C* he talked about a simple pattern he called 0, 1, N, and that his friend Tim Ottinger gave it the more memorable name ZOM. Grenning even quotes the core intuition: “There are only three numbers important in computing: Zero, One and Many.” The point is not math, it is test selection. Zero and One are special cases that tend to reveal different design pressures, while Many is the first real generalization where shortcuts start to break. ZOMBIES keeps that ZOM spine and adds reminders about boundaries, interfaces, exceptions, and staying simple, because those are exactly the areas developers skip when they rush toward the “interesting” algorithm.

## Not a strict checklist: ZOMBIES is two dimensional on purpose

[![](https://substackcdn.com/image/fetch/$s_!K16r!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1810df42-b7db-4215-ad56-61aabb7d3674_1620x1536.png)](https://substackcdn.com/image/fetch/$s_!K16r!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1810df42-b7db-4215-ad56-61aabb7d3674_1620x1536.png)

A common misunderstanding is treating ZOMBIES as a rigid sequence you must follow letter by letter. Grenning is explicit that it is “not your usual sequential acronym” and that it is only partially sequential because it has “two dimensions.” One axis is ZOM (from simple to generalized), and the other axis is BIE (boundary behaviors, interface definition, exceptional behavior), with S pushing you toward simple scenarios and simple solutions that connect both axes. This matters because you do not “finish” interfaces and boundaries at the end. You notice them from the first tests, and you keep noticing them as the behavior expands. ZOMBIES is less like a recipe and more like a map that keeps you from getting lost.

### B: Boundary behaviors

[![](https://substackcdn.com/image/fetch/$s_!iev9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3bb3251-3b41-4bd8-a378-c18ebb908414_1885x1148.png)](https://substackcdn.com/image/fetch/$s_!iev9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3bb3251-3b41-4bd8-a378-c18ebb908414_1885x1148.png)

A boundary is any edge where behavior changes. The classic ones are empty versus not empty, full versus not full, minimum versus maximum, and off by one transitions. Boundaries are dangerous because a lot of code is “almost right” at the edges. A loop works for many items but fails at zero. A pop works for one element but fails when you pop the last one and forget to restore the empty state. A capacity check works until you hit exactly the limit.

In the Stack kata, boundaries show up constantly:

- **Empty boundary**: `Pop` on an empty stack should throw underflow. `Peek` on empty should throw underflow.
- **Transition boundary**: after pushing the first item, `IsEmpty` flips from true to false. After popping the last item, it flips back.
- **Capacity boundary**: pushing when `Size == capacity` should throw overflow.
- **Index boundary**: “top element” is always at `Count - 1`. That is a boundary expression by itself, because if you get it wrong, you crash or return the wrong element.

The reason Grenning tells people not to start with boundaries is not because they are unimportant. It is because boundaries are where complexity concentrates. If you start with the scariest boundary case, you tend to write either a huge test that mixes multiple concerns or a bunch of defensive production code before you even know the happy path. ZOMBIES nudges you to earn boundaries after you have at least one working slice of behavior, so the boundary test has a clear meaning and a clear failure mode.

A practical way to think about boundaries in your scenario list is: once the happy path works for One and Many, do a quick sweep and ask “where does the behavior flip?” Those flips are almost always worth a test because they define the contract of your component.

### I: Interface definition (tests as design, not only verification)

[![](https://substackcdn.com/image/fetch/$s_!4JIt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b0e1596-a22b-41e1-8b9b-6651b6149ded_1586x1220.png)](https://substackcdn.com/image/fetch/$s_!4JIt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b0e1596-a22b-41e1-8b9b-6651b6149ded_1586x1220.png)

In ZOMBIES, “interface” is not just about writing an interface type in your language. It is about the shape of the API your caller experiences: method names, parameters, return values, how errors are signaled, what is mutable, what is immutable, and what is even possible to express.

This matters because tests are written from the caller’s point of view. Every test forces you to answer questions like:

- How do you create the thing? Constructor, factory, builder?
- How do you ask for state? Properties or methods?
- What does `Pop` return? What does `Peek` return?
- What happens on misuse? Exception, result type, null, default value?
- How do you express capacity? Do you even need it yet?

In the stack walkthrough, interface design happens earlier than it looks. The very first Zero test forces “there is a Stack class and it exposes IsEmpty and Size.” The One tests force “there is a Push method.” The boundary tests force “there is a Pop and Peek and they signal underflow in a specific way.” Later, overflow forces “capacity exists as an input to construction.” Even later, if you decide to introduce a `Capacity` value type or a factory like `Stacks.Create`, that is interface evolution driven by the pressure you experienced, not speculation.

This is why ZOMBIES is so effective for design. It prevents you from inventing a perfect API in your head and then trying to make tests fit it. Instead, the tests pull an API out of the problem one slice at a time, and the API ends up closer to how people actually want to use the code.

A useful rule during refactor is: if your tests read like a story a caller would tell, your interface is probably improving. If your tests read like “I am fighting the API,” your interface is probably wrong.

### E: Exercise exceptional behavior (misuse and failure modes, on stable ground)

[![](https://substackcdn.com/image/fetch/$s_!96-Y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa95a9fc7-61db-490f-b549-fbfb57563edb_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!96-Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa95a9fc7-61db-490f-b549-fbfb57563edb_2816x1536.png)

Exceptional behavior is everything outside the happy path: misuse, invalid input, invalid state, and failure modes that must be defined for the component to be trustworthy. In many codebases, this is where production defects live because teams under test pressure stop once the happy path passes.

In the Stack kata, the “E” is mostly:

- `Pop`on empty throws underflow
- `Peek`on empty throws underflow
- `Push`on full throws overflow
- Creating with invalid capacity throws invalid capacity

The interesting part is not that you test exceptions. The interesting part is when you choose to test them. ZOMBIES puts exceptional behavior later because if you start with errors, you often end up building defensive behavior around something you have not defined yet. Once the happy path and the core transitions are solid, exceptional tests become clearer. You know what “normal” means, so you can express “not normal” precisely.

There is also a design benefit here that is easy to miss: exceptional behavior decisions shape your API. An exception type becomes part of the contract. A message becomes part of the contract if you assert it. If you want to avoid repeating magic strings, it is a good pattern for the exception to own its message. That keeps tests readable and avoids scattering the same literal across the suite.

One more subtle point: exceptional behavior tests are often where you discover you need parallel change. Adding capacity is an exceptional requirement because it changes construction. You can introduce it safely by expanding the API, migrating tests, and then contracting the old path away. That keeps the suite green and keeps the change understandable.

### How BIE fits into the scenario list without turning it into a checklist

If you want a lightweight way to apply BIE while keeping ZOM as your main driver, do this:

- Start with a ZOM slice you can complete quickly
- While you write those tests, jot down any boundary you notice but do not chase it immediately
- Let the tests shape the interface naturally, and refactor it only when you have evidence
- Once the happy path is stable, return to the list and add the exceptional cases explicitly

That keeps your momentum while still ensuring you do not “accidentally forget” the parts that make software reliable in the real world.

## What each letter really pushes you to do in practice

In Grenning’s framing, Zero is about the simplest post conditions right after creation, like “it is empty” and “it is not full.” One is the first meaningful transition, usually a boundary crossing, like going from empty to not empty. Many is where you stop faking it and start generalizing: multiple items, richer scenarios, and behavior that forces you away from hardcoded values. Boundary behaviors are the edges where defects hide: full, empty, wrap around, off by one limits, and state transitions. Interface definition is the reminder that tests are also a design tool: each test you write is forcing a call site, a name, parameters, return values, and error signaling. Exercise exceptional behavior is about abuse cases and failure modes, but importantly, it comes after you have stable happy paths so you can interpret failures clearly. Simple scenarios and simple solutions is the discipline that keeps all of this from turning into a giant test that tries to prove everything at once. Grenning stresses that keeping things simple is hard, but it is the habit that makes the whole method sustainable.

## The circular buffer example: ZOMBIES as a step by step path, not theory

Grenning’s article is anchored in a concrete example: test driving a `CircularBuffer` (FIFO) module in C. He starts by making a test list “in no particular order” including wrap around, overflow, underflow, empty, full, and the FIFO happy path, and then points out the trap: engineers feel pulled toward the hardest parts first, like wrap around and overflow. His advice is the opposite: start with easy behavior, build a foundation, and only then take on the more involved scenarios “one at a time.” That is ZOMBIES in action, and it is also the reason the mnemonic works for people under pressure: it gives you permission to defer complexity without losing control of the outcome.

With Zero, he writes tests like “is empty after creation” and “is not full after creation,” and those tests immediately force interface decisions such as `Create`, `Destroy`, `IsEmpty`, and `IsFull`. With One, he moves to `Put` and the empty to not empty transition, then extends the boundary again with “put then get returns to empty,” and “get equals put for one item.” At this stage, Grenning intentionally uses incomplete implementations, including hardcoded return values, because the goal is to move toward the solution with the smallest possible change and let the next tests force the next bit of behavior. He describes the discomfort this creates for new practitioners, but the lesson is clear: if a fake implementation passes, that is information that your tests have not yet demanded the real behavior.

When he reaches Many, the first FIFO test forces proper ordering across multiple values, and only then does he start introducing capacity into the interface, driven by tests like “report capacity” and “capacity is adjustable.” This is where ZOMBIES shows its design benefit: it keeps the interface evolving in response to real usage pressure, not speculation. Boundaries then become unavoidable: filling to capacity, wrapping, and verifying that “full” and “empty” remain correct through transitions. Finally, he explicitly calls out the E in ZOMBIES with tests such as “put to full fails” and “get from empty returns default value,” and he also lists additional abuse scenarios that might warrant tests, like creating with zero or negative length, passing null pointers, or running out of heap, while noting that responses to these are application specific and outside the article’s scope.

## Why the “S” matters: staying simple is what keeps feedback fast

[![](https://substackcdn.com/image/fetch/$s_!eJzi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69fb9104-8cdc-4e7e-9dee-1e8bd3c1f0c6_2240x1536.png)](https://substackcdn.com/image/fetch/$s_!eJzi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69fb9104-8cdc-4e7e-9dee-1e8bd3c1f0c6_2240x1536.png)

ZOMBIES is not just about ordering test cases. It is also about keeping feedback loops tight. Grenning repeats a simple idea that many teams forget mid sprint: “It’s easier to keep code working than to fix it after you break it.” In the circular buffer, he uses this principle to justify one change at a time, even when he knows more changes are coming. He also acknowledges reality: sometimes tests stop being simple, and you either split them or accept some complexity. He labels a couple of his later checks as “belt and suspender tests,” not because they are worthless, but because by that point the design is stable enough that those tests are about protecting integrity through exceptional interactions, not discovering new behavior.

One of the strongest moments in the article is when an “exceptional” scenario turns into a design refactor prompted by concurrency. Grenning introduces a curve ball: imagine `Put` runs in an interrupt and `Get` runs in a task. A shared counter becomes a race condition that can corrupt state, and he uses the existing tests as a safety net to refactor toward an algorithm where each operation updates its own index consistently. The important takeaway is not the specific concurrency fix, it is the workflow: once you have grown behavior with small steps, you can make significant internal changes with confidence because the behavior is pinned down by tests.

## How the community explains it: slicing work, not just testing code

The appeal of ZOMBIES is that it generalizes beyond Grenning’s embedded C examples. Samman Coaching teaches it explicitly as a way to keep TDD cycles “short and fairly regular,” describing ZOMBIES as an acronym invented by Grenning to help slice problems into workable pieces, and emphasizing the same structure: think in Zero, One, Many, and for each consider boundaries, interfaces, and exceptions while keeping scenarios and solutions simple. This framing is useful because it shifts the mindset from “writing tests” to “managing incremental discovery.”

## A practical way to apply ZOMBIES on your next feature

[![](https://substackcdn.com/image/fetch/$s_!Az8a!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F117386d5-00de-4402-9cc9-f5a9edf566d2_9641x4422.png)](https://substackcdn.com/image/fetch/$s_!Az8a!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F117386d5-00de-4402-9cc9-f5a9edf566d2_9641x4422.png)

If you want to use ZOMBIES tomorrow, do not start by trying to memorize the letters. Start by writing a short test list in plain language, just like Grenning does for the circular buffer, and then pick the smallest Zero you can that still forces a real interface decision. From there, move to the One that represents the first meaningful transition, and only then push toward Many where the behavior can no longer be faked cheaply. As you do this, keep asking the BIE questions continuously: what boundary did I just cross, what interface did this test force me to expose, what exceptional behavior should I note for later? The key is “note for later” rather than “solve now.” Grenning’s whole point about skillful procrastination is that you can park scary cases on the list without letting them hijack your design before you even have a working baseline.

## The kata and the goal

Codurance’s Stack kata asks you to build a stack with core behaviors like `Push`, `Pop`, `Peek`, `Size`, and `IsEmpty`, plus boundary behavior like underflow and overflow, plus invalid capacity. We are not aiming for thread safety. What we do want is to avoid inconsistent internal state and impossible states by design. The most practical way to do that is to avoid duplicated sources of truth, keep invariants obvious, and introduce types or abstractions only when a test forces the need.

## The ZOMBIES test list

We will update it as we learn. This list starts unordered. That is deliberate. The point is to remove blank page fear and have a place to park thoughts.

```
# Scenario list

Zero
- [ ] given_a_new_stack_when_asking_if_it_is_empty_then_the_result_should_be_true
- [ ] given_a_new_stack_when_asking_the_size_then_the_result_should_be_zero

One
- [ ] given_an_empty_stack_when_pushing_one_item_then_it_should_not_be_empty
- [ ] given_an_empty_stack_when_pushing_one_item_then_the_size_should_be_one

Many
- [ ] given_a_stack_when_pushing_two_items_then_the_size_should_be_two
- [ ] given_a_stack_when_pushing_three_items_then_the_size_should_be_three

Boundaries and exceptions
- [ ] given_an_empty_stack_when_popping_then_it_should_throw_underflow
- [ ] given_an_empty_stack_when_peeking_then_it_should_throw_underflow
- [ ] given_a_full_stack_when_pushing_then_it_should_throw_overflow
- [ ] given_a_negative_capacity_when_creating_a_stack_then_it_should_throw_invalid_capacity

LIFO
- [ ] given_a_stack_with_one_item_when_popping_then_the_result_should_be_the_pushed_item
- [ ] given_a_stack_with_two_items_when_popping_twice_then_the_second_result_should_be_the_first_pushed_item

Peek semantics
- [ ] given_a_stack_with_one_item_when_peeking_then_the_result_should_be_the_pushed_item
- [ ] given_a_stack_with_one_item_when_peeking_then_the_size_should_remain_one
```

## Parallel Change (expand, migrate, contract) in plain words

Parallel Change is how you introduce a backwards-incompatible API or model change without breaking everything at once. You split the change into three phases:

- Expand: add the new path while keeping the old path working
- Migrate: gradually move callers to the new path, keeping the suite green
- Contract: delete the old path once nothing uses it

In this kata, capacity is a perfect example. If we add capacity as a mandatory constructor parameter too early, we pollute Zero and One. If we add it later in a big bang, we change all tests and production at once and create a fragile moment. Parallel Change lets us introduce capacity exactly when needed, while keeping earlier tests stable, and then later make capacity explicit everywhere and remove the temporary compatibility path.

## The walk: each iteration shows Red, Green, Refactor, and the refactored code is carried forward

### Iteration 1 (Zero): a new stack is empty

#### 🔴 Red: first test (fails to compile)

```csharp
using NUnit.Framework;

namespace StackKata.Tests;

public class StackShould
{
    [Test]
    public void given_a_new_stack_when_asking_if_it_is_empty_then_the_result_should_be_true()
    {
        var stack = new Stack&lt;string&gt;();

        Assert.That(stack.IsEmpty, Is.True);
    }
}
```

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    public void IsEmpty()
    {
        throw new System.NotImplementedException();
    }
}
```

#### 🟢 Green: minimum production code

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    public bool IsEmpty()
    {
        return true;
    }
}
```

#### 🔵 Refactor: none

Checklist update

✅given_a_new_stack_when_asking_if_it_is_empty_then_the_result_should_be_true

### Iteration 2 (Zero): size starts at 0

#### 🔴 Red

```csharp
[Test]
public void given_a_new_stack_when_asking_the_size_then_the_result_should_be_zero()
{
    var stack = new Stack&lt;string&gt;();

    Assert.That(stack.Size, Is.EqualTo(0));
}
```

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    public bool IsEmpty()
    {
        return true;
    }

    public void Size()
    {
        throw new System.NotImplementedException();
    }
}
```

#### 🟢 Green

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    public bool IsEmpty()
    {
        return true;
    }

    public int Size()
    {
        return 0;
    }
}
```

#### 🔵 Refactor: none

Checklist update

✅ given_a_new_stack_when_asking_the_size_then_the_result_should_be_zero

### Iteration 3 (One): after one push, it is not empty

#### 🔴 Red

```csharp
[Test]
public void given_an_empty_stack_when_pushing_one_item_then_it_should_not_be_empty()
{
    var stack = new Stack&lt;string&gt;();

    stack.Push("A");

    Assert.That(stack.IsEmpty, Is.False);
}
```

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    public bool IsEmpty()
    {
        return true;
    }

    public int Size()
    {
        return 0;
    }

    public void Push(T item)
    {
        throw new System.NotImplementedException();
    }
}
```

#### 🟢 Green: fake it until you make it

Smallest change is to introduce the minimum state to satisfy “not empty”.

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    private bool hasAny;

    public bool IsEmpty()
    {
        return !hasAny;
    }

    public int Size()
    {
        return 0;
    }

    public void Push(T item)
    {
        hasAny = true;
    }
}
```

#### 🔵 Refactor: none

Checklist update

✅ given_an_empty_stack_when_pushing_one_item_then_it_should_not_be_empty

### Iteration 4 (One): after one push, size is 1

#### 🔴 Red

```csharp
[Test]
public void given_an_empty_stack_when_pushing_one_item_then_the_size_should_be_one()
{
    var stack = new Stack&lt;string&gt;();

    stack.Push("A");

    Assert.That(stack.Size, Is.EqualTo(1));
}
```

#### 🟢 Green: still fake, still minimal

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    private bool hasAny;

    public bool IsEmpty()
    {
        return !hasAny;
    }

    public int Size()
    {
        return hasAny ? 1 : 0;
    }

    public void Push(T item)
    {
        hasAny = true;
    }
}
```

#### 🔵 Refactor: Update test

```csharp
using NUnit.Framework;

namespace StackKata.Tests;

public class StackShould
{
    private Stack&lt;string&gt; stack;

    [SetUp]
    public void Setup()
    {
        stack = new Stack&lt;string&gt;();
    }

    [Test]
    public void given_a_new_stack_when_asking_if_it_is_empty_then_the_result_should_be_true()
    {
        Assert.That(stack.IsEmpty, Is.True);
    }

    [Test]
    public void given_a_new_stack_when_asking_the_size_then_the_result_should_be_zero()
    {
        Assert.That(stack.Size, Is.EqualTo(0));
    }

    [Test]
    public void given_an_empty_stack_when_pushing_one_item_then_it_should_not_be_empty()
    {
        stack.Push("A");

        Assert.That(stack.IsEmpty, Is.False);
    }

    [Test]
    public void given_an_empty_stack_when_pushing_one_item_then_the_size_should_be_one()
    {
        stack.Push("A");

        Assert.That(stack.Size, Is.EqualTo(1));
    }
}
```

Checklist update

✅ given_an_empty_stack_when_pushing_one_item_then_the_size_should_be_one

### Iteration 5 (Many): triangulation point 2, size is 2

#### 🔴 Red

```csharp
[Test]
public void given_a_stack_when_pushing_two_items_then_the_size_should_be_two()
{
    stack.Push("A");
    stack.Push("B");

    Assert.That(stack.Size, Is.EqualTo(2));
}
```

#### 🟢 Green: fake with special casing, on purpose

We replace the boolean with a count, but we still do not generalize yet. We want the next test to force it.

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    private int totalElements;

    public bool IsEmpty()
    {
        return totalElements == 0;
    }

    public int Size()
    {
        return totalElements;
    }

    public void Push(T item)
    {
        if  (totalElements == 0)
        {
            totalElements = 1;
        }
        else
        {
            totalElements = 2;
        }
    }
}
```

#### 🔵 Refactor: none

Checklist update

✅ given_a_stack_when_pushing_two_items_then_the_size_should_be_two

### Iteration 6 (Many): triangulation point 3, size is 3, then refactor to the real rule

#### 🔴 Red

```csharp
[Test]
public void given_a_stack_when_pushing_three_items_then_the_size_should_be_three()
{
    stack.Push("A");
    stack.Push("B");
    stack.Push("C");

    Assert.That(stack.Size, Is.EqualTo(3));
}
```

#### 🟢 Green: extend fake one last time

```csharp
public void Push(T item)
{
    if  (totalElements == 0)
    {
        totalElements = 1;
        return;
    }

    if (totalElements == 1)
    {
        totalElements = 2;
        return;
    }

    totalElements = 3;
}
```

#### 🔵 Refactor: triangulation earned, generalize to increment

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    private int totalElements = 0;
    private const int EmptyStack = 0;

    public bool IsEmpty()
    {
        return totalElements == EmptyStack;
    }

    public int Size()
    {
        return totalElements;
    }

    public void Push(T item)
    {
        totalElements++;
    }
}
```

Checklist update

✅ given_a_stack_when_pushing_three_items_then_the_size_should_be_three

At this point we still have not stored any items. That is correct. Our tests demanded only size and emptiness.

### Iteration 7 (Boundary): popping an empty stack throws underflow

#### 🔴 Red

```csharp
[Test]
public void given_an_empty_stack_when_popping_then_it_should_throw_underflow()
{
    Assert.That(
        () =&gt; stack.Pop(),
        Throws.TypeOf&lt;StackUnderflow&gt;().And.Message.EqualTo(StackUnderflow.MessageText)
    );
}
```

```csharp
namespace StackKata;

public sealed class StackUnderflow : Exception
{
    public static string MessageText =&gt; "Stack underflow";

    public StackUnderflow() : base(MessageText)
    {
    }
}
```

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    private int totalElements = 0;
    private const int EmptyStack = 0;

    public bool IsEmpty()
    {
        return totalElements == EmptyStack;
    }

    public int Size()
    {
        return totalElements;
    }

    public void Push(T item)
    {
        totalElements++;
    }

    public T Pop()
    {
        throw new System.NotImplementedException();
    }
}
```

#### 🟢 Green: introduce the exception and the minimal pop

Update `Stack&lt;T&gt;` (minimum change is “always throw”, because the only demanded behavior is “pop on empty throws”):

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    private int totalElements = 0;
    private const int EmptyStack = 0;

    public bool IsEmpty()
    {
        return totalElements == EmptyStack;
    }

    public int Size()
    {
        return totalElements;
    }

    public void Push(T item)
    {
        totalElements++;
    }

    public T Pop()
    {
        throw new StackUnderflow();
    }
}
```

#### 🔵 Refactor: none

Checklist update

✅ given_an_empty_stack_when_popping_then_it_should_throw_underflow

### Iteration 8 (One): pop returns the pushed item, storage is born

#### 🔴 Red

```csharp
[Test]
public void given_a_stack_with_one_item_when_popping_then_the_result_should_be_the_pushed_item()
{
    stack.Push("A");

    Assert.That(stack.Pop(), Is.EqualTo("A"));
}
```

#### 🟢 Green: fake with the smallest data representation

We do not need a list yet. One item can be represented by a single field.

Green code (minimal change, still naive)

```csharp
namespace StackKata;

public class Stack&lt;T&gt;
{
    private int totalElements = 0;
    private const int EmptyStack = 0;
    private T topItem = default;

    public bool IsEmpty()
    {
        return totalElements == EmptyStack;
    }

    public int Size()
    {
        return totalElements;
    }

    public void Push(T item)
    {
        totalElements++;
        topItem = item;
    }

    public T Pop()
    {
        if (totalElements == EmptyStack) throw new StackUnderflow();

        totalElements--;
        return topItem;
    }
}
```

#### 🔵 Refactor: none

Checklist update

✅given_a_stack_with_one_item_when_popping_then_the_result_should_be_the_pushed_item

### Iteration 9 (Many): pop twice forces real LIFO storage

#### 🔴 Red

```csharp
[Test]
public void given_a_stack_with_two_items_when_popping_twice_then_the_second_result_should_be_the_first_pushed_item()
{
    stack.Push("A");
    stack.Push("B");
    stack.Pop();

    Assert.That(stack.Pop(), Is.EqualTo("A"));
}
```

#### 🟢 Green: replace fake storage with a real structure, and remove duplicated state

This test creates pressure: we can no longer pretend a single `topItem` is enough. The simplest correct representation is a list. While we do that, we also eliminate inconsistent states by removing the separate `count` field. `Size` and `IsEmpty` now derive from a single source of truth.

```csharp
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        items.Add(item);
    }

    public T Pop()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();

        var topIndex = items.Count - 1;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }
}
```

#### 🔵 Refactor: tidy the naming pressure, keep the “top” concept explicit

We already replaced a magic number by `TopOffset`. That is enough for now. The key is that the refactored code above is the state we carry into the next iteration.

```csharp
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;
    private const int TopOffset = 1;

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        items.Add(item);
    }

    public T Pop()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();

        var topIndex = items.Count - TopOffset;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }
}
```

Checklist update

✅given_a_stack_with_two_items_when_popping_twice_then_the_second_result_should_be_the_first_pushed_item

Refactor note: this step also reduced the chance of inconsistent internal state. We stopped tracking “count” separately. That is exactly the kind of “avoid impossible states” improvement that does not require thread safety.

---

### Iteration 10 (Boundary): peek underflow

#### 🔴 Red

```plaintext
[Test]
public void given_an_empty_stack_when_peeking_then_it_should_throw_underflow()
{
    Assert.That(
        () =&gt; stack.Peek(),
        Throws.TypeOf&lt;StackUnderflow&gt;().And.Message.EqualTo(StackUnderflow.MessageText)
    );
}
```

```csharp
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;
    private const int TopOffset = 1;

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        items.Add(item);
    }

    public T Pop()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();

        var topIndex = items.Count - TopOffset;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }

    public T Peek()
    {
        throw new System.NotImplementedException();
    }
}
```

#### 🟢 Green

```csharp
using System;
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;
    private const int TopOffset = 1;

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        items.Add(item);
    }

    public T Pop()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();

        var topIndex = items.Count - TopOffset;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }

    public T Peek()
    {
        throw new StackUnderflow();
    }
}
```

#### 🔵 Refactor: none

Checklist update

✅ given_an_empty_stack_when_peeking_then_it_should_throw_underflow

### Iteration 11 (One): peek returns the top item

#### 🔴 Red: peek returns the pushed item

```plaintext
[Test]
public void given_a_stack_with_one_item_when_peeking_then_the_result_should_be_the_pushed_item()
{
    stack.Push("A");

    Assert.That(stack.Peek(), Is.EqualTo("A"));
}
```

#### 🟢 Green

```csharp
using System;
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;
    private const int TopOffset = 1;

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        items.Add(item);
    }

    public T Pop()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();

        var topIndex = items.Count - TopOffset;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }

    public T Peek()
    {
        return Pop();
    }
}
```

**Caution**: this implementation now can fail because of the pop

#### 🔵 Refactor

Update the test list

✅given_a_stack_with_one_item_when_peeking_then_the_result_should_be_the_pushed_item

### Iteration 12 (One): peek should not change the size

#### 🔴 Red: peek does not mutate size

```plaintext
[Test]
public void given_a_stack_with_one_item_when_peeking_then_the_size_should_remain_one()
{
    stack.Push("A");
    stack.Peek();

    Assert.That(stack.Size, Is.EqualTo(1));
}
```

#### 🟢 Green

```csharp
using System;
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;
    private const int TopOffset = 1;

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        items.Add(item);
    }

    public T Pop()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();

        var topIndex = items.Count - TopOffset;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }

    public T Peek()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();
        return items[^TopOffset];
    }
}
```

#### 🔵 Refactor: update the test list and tidy test data

This is a good moment to tidy the tests. We introduce constants in the test class to avoid repeated literals. This does not change behavior, it reduces noise.

Refactor code (test file snippet, carried forward into next iterations)

```csharp
using NUnit.Framework;

namespace StackKata.Tests;

public class StackShould
{
    private const string ItemA = "A";
    private const string ItemB = "B";
    private const string ItemC = "C";
    private Stack&lt;string&gt; stack;

    [SetUp]
    public void Setup()
    {
        stack = new Stack&lt;string&gt;();
    }

    [Test]
    public void given_a_new_stack_when_asking_if_it_is_empty_then_the_result_should_be_true()
    {
        Assert.That(stack.IsEmpty, Is.True);
    }

    [Test]
    public void given_a_new_stack_when_asking_the_size_then_the_result_should_be_zero()
    {
        Assert.That(stack.Size, Is.EqualTo(0));
    }

    [Test]
    public void given_an_empty_stack_when_pushing_one_item_then_it_should_not_be_empty()
    {
        stack.Push(ItemA);

        Assert.That(stack.IsEmpty, Is.False);
    }

    [Test]
    public void given_an_empty_stack_when_pushing_one_item_then_the_size_should_be_one()
    {
        stack.Push(ItemA);

        Assert.That(stack.Size, Is.EqualTo(1));
    }

    [Test]
    public void given_a_stack_when_pushing_two_items_then_the_size_should_be_two()
    {
        stack.Push(ItemA);
        stack.Push(ItemB);

        Assert.That(stack.Size, Is.EqualTo(2));
    }

    [Test]
    public void given_a_stack_when_pushing_three_items_then_the_size_should_be_three()
    {
        stack.Push(ItemA);
        stack.Push(ItemB);
        stack.Push(ItemC);

        Assert.That(stack.Size, Is.EqualTo(3));
    }

    [Test]
    public void given_an_empty_stack_when_popping_then_it_should_throw_underflow()
    {
        Assert.That(
            () =&gt; stack.Pop(),
            Throws.TypeOf&lt;StackUnderflow&gt;().And.Message.EqualTo(StackUnderflow.MessageText)
        );
    }

    [Test]
    public void given_a_stack_with_one_item_when_popping_then_the_result_should_be_the_pushed_item()
    {
        stack.Push(ItemA);

        Assert.That(stack.Pop(), Is.EqualTo(ItemA));
    }

    [Test]
    public void given_a_stack_with_two_items_when_popping_twice_then_the_second_result_should_be_the_first_pushed_item()
    {
        stack.Push(ItemA);
        stack.Push(ItemB);
        stack.Pop();

        Assert.That(stack.Pop(), Is.EqualTo(ItemA));
    }

    [Test]
    public void given_an_empty_stack_when_peeking_then_it_should_throw_underflow()
    {
        Assert.That(
            () =&gt; stack.Peek(),
            Throws.TypeOf&lt;StackUnderflow&gt;().And.Message.EqualTo(StackUnderflow.MessageText)
        );
    }

    [Test]
    public void given_a_stack_with_one_item_when_peeking_then_the_result_should_be_the_pushed_item()
    {
        stack.Push(ItemA);

        Assert.That(stack.Peek(), Is.EqualTo(ItemA));
    }

    [Test]
    public void given_a_stack_with_one_item_when_peeking_then_the_size_should_remain_one()
    {
        stack.Push(ItemA);
        stack.Peek();

        Assert.That(stack.Size, Is.EqualTo(1));
    }
}
```

And we replace occurrences of `"A"` with `ItemA`, and so on.

Remove duplicated code for ensuring that the stack is not empty.

```csharp
using System;
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;
    private const int TopOffset = 1;

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        items.Add(item);
    }

    public T Pop()
    {
        EnsureNotEmpty();
        var topIndex = items.Count - TopOffset;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }

    public T Peek()
    {
        EnsureNotEmpty();
        return items[^TopOffset];
    }

    private void EnsureNotEmpty()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();
    }
}
```

Checklist update

✅ given_a_stack_with_one_item_when_peeking_then_the_size_should_remain_one

## Capacity appears only when needed, introduced via Parallel Change

Up to now, capacity was not part of our world. That was intentional. Now we need overflow and invalid capacity, so we bring it in. We will do it using Parallel Change so earlier tests remain clean, and we avoid a big-bang break.

### Iteration 12 (Exceptions): invalid capacity is rejected

#### 🔴 Red

```csharp
[Test]
public void given_a_negative_capacity_when_creating_a_stack_then_it_should_throw_invalid_capacity()
{
    Assert.That(
        () =&gt; new Stack&lt;string&gt;(capacity: -1),
        Throws.TypeOf&lt;InvalidCapacity&gt;().And.Message.EqualTo(InvalidCapacity.MessageText)
    );
}
```

New exception:

```csharp
using System;

namespace StackKata;

public sealed class InvalidCapacity : Exception
{
    public static string MessageText =&gt; "Capacity must be zero or greater";

    public InvalidCapacity() : base(MessageText)
    {
    }
}
```

Now we do the Expand phase in `Stack&lt;T&gt;`: we add a new constructor that accepts capacity, and we keep the parameterless constructor working by delegating to a named constant. This keeps earlier tests unchanged, and it exercises the new path via the new failing test.

```csharp
using System;
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;
    private const int TopOffset = 1;

    private const int UnboundedCapacity = int.MaxValue;
    private readonly int capacity;

    public Stack() : this(UnboundedCapacity)
    {
    }

    public Stack(int capacity)
    {
        this.capacity = capacity;
    }

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        items.Add(item);
    }

    public T Pop()
    {
        EnsureNotEmpty();
        var topIndex = items.Count - TopOffset;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }

    public T Peek()
    {
        EnsureNotEmpty();
        return items[^TopOffset];
    }

    private void EnsureNotEmpty()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();
    }
}
```

Now the test fail not because they do not compile but because of the feature we want to add.

#### 🟢 Green: expand the API, do not break existing tests

```csharp
using System;
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;
    private const int TopOffset = 1;

    private const int MinimumCapacity = 0;
    private const int UnboundedCapacity = int.MaxValue;
    private readonly int capacity;

    public Stack() : this(UnboundedCapacity)
    {
    }

    public Stack(int capacity)
    {
        if (capacity &lt; MinimumCapacity) throw new InvalidCapacity();
        this.capacity = capacity;
    }

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        items.Add(item);
    }

    public T Pop()
    {
        EnsureNotEmpty();
        var topIndex = items.Count - TopOffset;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }

    public T Peek()
    {
        EnsureNotEmpty();
        return items[^TopOffset];
    }

    private void EnsureNotEmpty()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();
    }
}
```

#### 🔵 Refactor: do nothing else yet

We are deliberately allowing the temporary compatibility constructor because this is Expand. We will remove it later in Contract.

Checklist update

✅given_a_negative_capacity_when_creating_a_stack_then_it_should_throw_invalid_capacity

### Iteration 13 (Boundary): overflow when pushing to a full stack

I’ve decided that the capacity will be and integer for outside, because it can be an internal collaborator of the library, but as a developer for a Publish API, I could also decided that this could be part of the contract of the API of muy stack library.

#### 🔴 Red

```csharp
[Test]
public void given_a_full_stack_when_pushing_then_it_should_throw_overflow()
{
    var stack = new Stack&lt;string&gt;(capacity: 1);

    stack.Push(ItemA);

    Assert.That(
        () =&gt; stack.Push(ItemB),
        Throws.TypeOf&lt;StackOverflow&gt;().And.Message.EqualTo(StackOverflow.MessageText)
    );
}
```

```csharp
using System;

namespace StackKata;

public sealed class StackOverflow : Exception
{
    public static string MessageText =&gt; "Stack overflow";

    public StackOverflow() : base(MessageText)
    {
    }
}
```

#### 🟢 Green

```csharp
using System;
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;
    private const int TopOffset = 1;

    private const int MinimumCapacity = 0;
    private const int UnboundedCapacity = int.MaxValue;
    private readonly int capacity;

    public Stack() : this(UnboundedCapacity)
    {
    }

    public Stack(int capacity)
    {
        if (capacity &lt; MinimumCapacity) throw new InvalidCapacity();
        this.capacity = capacity;
    }

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        if (items.Count == capacity) throw new StackOverflow();
        items.Add(item);
    }

    public T Pop()
    {
        EnsureNotEmpty();
        var topIndex = items.Count - TopOffset;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }

    public T Peek()
    {
        EnsureNotEmpty();
        return items[^TopOffset];
    }

    private void EnsureNotEmpty()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();
    }
}
```

Minimal production change is a guard inside `Push`.

#### 🔵 Refactor:

Checklist update

✅ given_a_full_stack_when_pushing_then_it_should_throw_overflow

## Parallel Change continuation: migrate tests, then contract the old API away

At this point we are carrying a parameterless constructor only to keep earlier tests unchanged. That is temporary. Now we do the Migrate phase: we update earlier tests to use explicit capacity. Then we do Contract: delete `Stack()`.

## Refactor checkpoint: migrate tests to explicit capacity (carried forward)

This is test refactoring only. Behavior does not change. We just stop pretending capacity does not exist now that it is part of the kata.

Example migration (before)

```csharp
[SetUp]
public void Setup()
{
    stack = new Stack&lt;string&gt;();
}
```

After migration (carried forward)

```csharp
[SetUp]
public void Setup()
{
    stack = new Stack&lt;string&gt;(capacity: 10);
}
```

We pick capacities that are comfortably above what each test needs so overflow does not appear accidentally.

## Contract: remove the parameterless constructor (production refactor)

Refactor code (before contract)

```csharp
public Stack() : this(UnboundedCapacity)
{
}
```

After contract (carried forward)

```csharp
// removed
```

Carried-forward `Stack&lt;T&gt;` now starts only with `Stack(int capacity)`. `UnboundedCapacity` becomes unused and is removed as part of the tidy.

Carried-forward `Stack&lt;T&gt;` after contract

```csharp
using System;
using System.Collections.Generic;

namespace StackKata;

public class Stack&lt;T&gt;
{
    private readonly List&lt;T&gt; items = new();
    private const int EmptyStack = 0;
    private const int TopOffset = 1;

    private const int MinimumCapacity = 0;
    private readonly int capacity;

    public Stack(int capacity)
    {
        if (capacity &lt; MinimumCapacity) throw new InvalidCapacity();
        this.capacity = capacity;
    }

    public bool IsEmpty()
    {
        return items.Count == EmptyStack;
    }

    public int Size()
    {
        return items.Count;
    }

    public void Push(T item)
    {
        if (items.Count == capacity) throw new StackOverflow();
        items.Add(item);
    }

    public T Pop()
    {
        EnsureNotEmpty();
        var topIndex = items.Count - TopOffset;
        var topItem = items[topIndex];
        items.RemoveAt(topIndex);
        return topItem;
    }

    public T Peek()
    {
        EnsureNotEmpty();
        return items[^TopOffset];
    }

    private void EnsureNotEmpty()
    {
        if (items.Count == EmptyStack) throw new StackUnderflow();
    }
}
```

This is a clean finish to the capacity introduction: capacity was not in Zero, it appeared when needed, and it became explicit everywhere without a big-bang break.

### Next steps

Now I could build and interface of the Publish API of my library, and use it working on the “interfaces“ point of the ZOMBIES, but I think for the example this should be enough.

## Conclusions

One important clarification before we wrap up: the point of this article is not my particular solution to the Stack kata. The stack implementation is just a convenient vehicle. What matters is the thinking process that ZOMBIES encourages: how you create an initial scenario list, how you choose the next smallest test without getting lost, how you deliberately postpone hard cases without forgetting them, and how you keep revisiting and reshaping that list as you learn. If you finish with a different internal design than mine but you can explain why each test exists and how each step earned the next one, then the article has done its job.

ZOMBIES is a genuinely useful technique for the moment TDD feels most uncomfortable: when you know you should write a failing test first, but you do not know what “the next test” should be. The mnemonic reduces that decision fatigue. It gives you a default direction that is usually safe: start with the least you can prove, move through the first meaningful transition, and only generalize once you have enough evidence. Under stress, that is not a small benefit. It is often the difference between “I’m stuck” and “I can take one more step.”

That said, ZOMBIES is not a universal truth and it should not be treated like a recipe. It is a tool, not a rule. It helps you choose tests in a sensible order, but it does not guarantee that the order is always optimal for every context, team, or codebase. The right mindset is “this belongs in my toolkit,” not “this is the way.” With experience, you learn when to lean on it and when to deviate because your context demands a different slice.

This is especially important for experienced practitioners who have worked across different environments. A common pattern in front end testing is starting with a “render the component” test because it feels like a Zero: prove it exists, prove it renders. That instinct is understandable. But in many real codebases, those tests end up covered by more meaningful interaction tests, integration checks, or contract tests. In that situation, the render test often adds maintenance cost and noise without increasing confidence. The discipline is not “always do the first Z.” The discipline is “choose the next test that teaches you something new.”

That leads to a principle that can feel counterintuitive but matters a lot for healthy test suites: you should not be afraid to delete tests. Tests are not sacred. They are an engineering asset, and assets need pruning. If a test does not protect behavior you care about, or if it duplicates coverage in a way that does not reduce risk, it is a candidate for removal. The key is intent and context. Deleting tests blindly is reckless. Deleting tests deliberately, because you understand what they cover and what other tests already guarantee, is maturity. A test suite should feel like a sharp safety net, not a museum.

A second lesson from this walk is how much the scenario list matters. The list is not bureaucracy, and it is not something you write once and forget. It is your external memory. It lets you practice Grenning’s “skillful procrastination”: you can write down wrap around, overflow, underflow, invalid input, and all the scary things, and then you can still start with something boring like “it is empty.” You are not ignoring complexity. You are sequencing it. The list evolves as you learn. You cross items off, you split items when a test turns out to be doing too much, and you add items when you discover missing cases. That living list is one of the highest leverage habits in the whole workflow.

A third lesson is the separation between Green and Refactor. Green is not the time to design the perfect model. Green is the time to do the smallest change that makes the failing test pass. That often means hardcoded values, naive implementations, or an intentionally awkward special case. That is not sloppiness, it is information gathering. It tells you what the tests have actually demanded so far. Refactor is where you earn cleanliness: you remove duplication, you introduce guard clauses, you collapse special cases into general rules once triangulation has forced the pattern, and you apply design principles only when you have safety. That discipline is what keeps TDD from turning into “slow programming.”

Parallel change is a practical complement to this discipline. When the design needs to evolve in a way that would otherwise cause a big bang break, expand, migrate, contract keeps your feedback loop intact. In this kata, capacity is a perfect example: if you force capacity into the constructor from day one, you pollute the earliest ZOM steps. If you change the constructor in one go later, you risk breaking everything at once. Parallel change gives you a controlled path where the suite stays meaningful at every point and where each commit has a clear intention.

Finally, the best outcome of ZOMBIES is not “more tests.” It is better cause and effect. You end up with tests that have one reason to fail, production code that has fewer impossible states, and a design that is shaped by real usage rather than speculation. If you use the technique with that goal in mind, you get something more valuable than a green build: you get a development rhythm that stays calm under pressure.

In short, ZOMBIES is a very interesting heuristic that can help many people decide how to start and how to proceed in small steps. It is not always the right tool, and it is not something you must apply blindly. Use it when it helps you slice the work and avoid getting stuck. Deviate when your context makes other tests more valuable. Keep the loop tight, keep refactor sacred, keep your scenario list alive, and do not be afraid to prune tests when they stop paying rent.

## References

- James Grenning, “TDD Guided by ZOMBIES.” ([James Grenning’s Blog](https://blog.wingman-sw.com/tdd-guided-by-zombies))
- Samman Coaching, “Slicing a task using ZOMBIES.” ([Samman Technical Coaching](https://sammancoaching.org/learning_hours/small_steps/zombies.html))
- Martin Fowler, “Parallel Change.” ([martinfowler.com](https://martinfowler.com/bliki/ParallelChange.html))
