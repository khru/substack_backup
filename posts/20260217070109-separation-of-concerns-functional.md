---
title: "Separation of concerns, functional thinking, and the discipline of simplicity"
requested_url: "https://emmanuelvalverderamos.substack.com/p/separation-of-concerns-functional"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/separation-of-concerns-functional"
substack_post_id: 185633927
retrieved_at: "2026-03-08T08:26:05.236Z"
---
# Separation of concerns, functional thinking, and the discipline of simplicity

## Table of contents

- Introduction
- Separation of concerns
	- What it is and why it matters
	- Where it comes from
	- Why it keeps showing up under different names
	- Layers of concern, from lines to architecture
- Functional programming as a separation engine
	- Actions
	- Calculations
	- Data
	- Data structures
	- Separation of state and immutability
	- The rule of contagion
	- Explicit and implicit inputs and outputs
- Relating separation of concerns with actions, calculations, data, and data structures
	- A practical separation strategy
	- Hierarchy of dependencies and hierarchy of preferences
- A complete refactor exercise in JavaScript
	- The starting point: “everything mixed” spaghetti code
	- Step 1: name things so humans can read them
	- Step 2: make implicit inputs and outputs explicit
	- Step 3: split actions from calculations
	- Step 4: separate state, prefer immutability
	- Step 5: effects as data, functional core and imperative shell
	- Step 6: the effect runner, and why it is a great place to improve design
	- Step 7: inversion of control, dependency inversion, ports and adapters, and the configurator
	- Final code: from spaghetti to separations
- Architecture: onion, clean architecture, and why the same rule keeps winning
- Simplicity as a discipline
- Code smells encountered in the refactor
- References

## 1. Introduction

From my personal point of view, separation of concerns feels like one of the most important software design principles and potentially one of the least understood and used. In this article, I try to relate two concepts that make complete sense to me: some of the foundations of functional programming, specifically actions, calculations, and data, with separation of concerns. I wrote this article not only to show that relationship, but also to show how it connects to other important ideas like clean architecture and onion architecture.

Even in the exercise included here, when I started writing it I began working with examples using ports and adapters, and during the refactors I ended up building a configurator. That happened simply by following separation of concerns and applying refactors and tidyings when they were necessary. From my point of view, this is directly related to many architectures we use, such as functional core and imperative shell.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## 2. Separation of concerns

### 2.1 What it is and why it matters

Separation of concerns is the practice of designing software so that different “reasons to change” do not tangle into the same place. It is not about creating more files or smaller functions for the sake of it. It is about creating boundaries that make change cheaper, safer, and more predictable.

When concerns are mixed, three things tend to happen:

- Understanding becomes expensive. You must hold unrelated facts in your head at the same time.
- Changing becomes risky. A change to one concern accidentally breaks another.
- Testing becomes harder. You cannot test a rule without also touching infrastructure.

Separation of concerns is fundamentally a cognitive tool. It gives you permission to focus on one dimension at a time.

### 2.2 Where it comes from

The phrase “separation of concerns” is strongly associated with Edsger W. Dijkstra. In his 1974 paper “On the role of scientific thought”, he frames it as a technique for ordering your thoughts effectively: you study one aspect in isolation for the sake of its own consistency, while still knowing other aspects exist.

Around the same era, David Parnas wrote “On the criteria to be used in decomposing systems into modules” (1972). His argument is not “split by steps in the flowchart”, but “split by design decisions likely to change”, and design modules to hide those decisions. That is separation of concerns expressed as “separate by volatility”.

Those two perspectives fit perfectly together:

- Dijkstra: separate to think clearly.
- Parnas: separate to change safely.

Fran Iglesias’ article is a very practical bridge between these ideas and day to day code. It emphasizes separation as a technique that can be applied at different scales, and it illustrates the “input, processing, output” lens as an approachable entry point.

### 2.3 Why it keeps showing up under different names

A lot of software design principles are just separation of concerns wearing different clothes.

- Modularity and information hiding: separating decisions likely to change.
- Cohesion and coupling: grouping what belongs together, loosening what should not be tied.
- Ports and adapters: separating the application core from delivery and infrastructure.
- Onion and clean architecture: enforcing a dependency direction that protects the core.
- Functional core and imperative shell: separating calculations from actions.

These are not unrelated ideas. They are different angles on the same fundamental goal: keep volatile, messy reality away from stable logic.

### 2.4 Separation of concerns and SRP

Robert C. Martin’s Single responsibility principle (SRP) is usually summarized as “a module should have one reason to change”. In his own writing, he explicitly connects SRP to Parnas and to separation of concerns, and he offers an alternative wording: “gather together the things that change for the same reasons; separate those things that change for different reasons”.

Now, the spicy part.

It is my opinion that SRP often reads like a rebranding of older ideas rather than a fundamentally new invention. The reason I hold that opinion is simple: Dijkstra and Parnas clearly discuss the core concept decades earlier, and SRP maps closely onto that same conceptual territory. At the same time, I cannot prove plagiarism as fact, and I do not think the available evidence is strong enough to claim that as more than my interpretation. What I can say with confidence is that SRP sits on top of a long lineage of modularity and separation thinking, and Martin himself points at that lineage.

So, if you are looking for something actionable:

- The valuable idea is not the name.
- The valuable idea is: separate by reasons to change, and protect your thinking by not mixing concerns.

### 2.5 Layers of concern, from lines to architecture

Separation of concerns can be applied in layers:

- Within a line: avoid doing three conceptual operations in one expression.
- Within a function: avoid mixing computation, state change, IO, and orchestration.
- Within a module: keep business rules away from delivery and infrastructure.
- Within a system: enforce dependency direction so changes do not cascade inward.

A simple mental model that scales surprisingly well is: input, processing, output.

Here is that model as a diagram:

[![](https://substackcdn.com/image/fetch/$s_!rtVT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe065c93b-b44c-40c3-a2eb-31cfff1737d6_1226x258.png)](https://substackcdn.com/image/fetch/$s_!rtVT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe065c93b-b44c-40c3-a2eb-31cfff1737d6_1226x258.png)

And the key move is to stop treating “processing” as a place where anything is allowed. Processing should be mostly calculations.

A tiny example helps.

#### Example: sum of CLI arguments

A “do everything at once” version in JavaScript:

```
// sum-cli.js
const numbers = process.argv.slice(2).map(Number);
const total = numbers.reduce((accumulator, value) =&gt; accumulator + value, 0);
console.log(total);
```

Even here we can spot concerns:

- Getting input (reading CLI args)
- Parsing (string to number)
- Computing (sum)
- Output (printing)

Separating them does not make the program “more enterprise”. It makes the responsibilities legible:

```
// sum-cli.js
function readCommandLineArguments(argv) {
  const argumentValues = argv.slice(2);
  return argumentValues;
}

function parseNumbers(stringValues) {
  return stringValues.map((stringValue) =&gt; Number(stringValue));
}

function sumNumbers(numbers) {
  const startingSum = 0;
  return numbers.reduce((accumulator, value) =&gt; accumulator + value, startingSum);
}

function writeOutput(text) {
  console.log(text);
}

const argumentValues = readCommandLineArguments(process.argv);
const numbers = parseNumbers(argumentValues);
const total = sumNumbers(numbers);
writeOutput(String(total));
```

This is separation of concerns at the smallest scale. The same thinking scales to architectures.

## 3. Functional programming as a separation engine

[![](https://substackcdn.com/image/fetch/$s_!8EMN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c892e5a-3f5a-4d2b-aeee-7090f84228b9_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!8EMN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c892e5a-3f5a-4d2b-aeee-7090f84228b9_2816x1536.png)

When people say “functional programming makes code easier to reason about”, the strongest practical reason is that it pushes you to separate actions from calculations, and to treat data as something you transform rather than something you mutate in place.

A very useful lens, heavily popularized by Grokking Simplicity, is to divide code into:

- Actions
- Calculations
- Data
- Data structures

### 3.1 Actions

[![](https://substackcdn.com/image/fetch/$s_!XMtz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56b2a382-cf1d-48e9-aa74-31ceaafff8fa_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!XMtz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F56b2a382-cf1d-48e9-aa74-31ceaafff8fa_2816x1536.png)

An action is anything that can change the world, or be changed by the world. The tell is simple: if running it twice can produce different results, or cause different outcomes, it is an action.

Typical actions in everyday JavaScript include:

- Reading and writing the DOM
- Calling an HTTP API
- Reading and writing to `localStorage`
- Logging
- Sending analytics events
- Reading the current time
- Generating randomness
- Mutating shared state

#### Actions are often tied to a time barrier

[![](https://substackcdn.com/image/fetch/$s_!P0JG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d34b92c-86c3-4f66-8be5-4d6d6ba422d3_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!P0JG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d34b92c-86c3-4f66-8be5-4d6d6ba422d3_2816x1536.png)

This is the part that people underestimate.

Some actions are not just “impure”. They are **time bound**. Once you cross a time barrier, the action cannot be replayed safely, or it changes meaning:

- “Send order confirmation email” today is not the same as sending it next week.
- “Charge customer card” now vs later may fail due to token expiry, balance changes, fraud checks, or policy windows.
- “Reserve inventory” depends on what was reserved by someone else a millisecond earlier.
- “Read current price” depends on when you read it, and you might not be allowed to assume it stays valid.
- Even “write to localStorage” can be time bound if you are racing other tabs or windows.

This creates **temporal coupling**: the correctness of the program depends on ordering and timing.

That is why functional design pushes a consistent strategy:

- Keep actions small.
- Do fewer actions when possible.
- Push actions to the edges.
- Turn “what should happen” into data, then interpret it at the edge.
- Make time explicit: read the clock once at the boundary, then pass the timestamp as data into calculations.

#### Practical techniques that make actions safer

Actions are inevitable, so the goal is not to eliminate them. The goal is to contain them and make them robust:

- **Idempotency**: design actions so repeating them does not cause double effects.
- **Ordering**: make the order explicit, especially when multiple actions must happen in sequence.
- **Retries and backoff**: recover from transient failure without duplicating outcomes.
- **Exactly once expectations**: if you need “exactly once”, do not hand wave. Use idempotency keys, deduplication, and persistence strategies.
- **Dependency inversion**: keep actions behind ports so the core does not know how they happen.

The simplest mental model I use is: actions are the boundary where the world leaks in. Treat them like the perimeter of a fortress. Everything behind that wall should be calm

### 3.2 Calculations

[![](https://substackcdn.com/image/fetch/$s_!Vcqq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff911f600-ccfb-435c-bdd4-45644bc2c76f_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!Vcqq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff911f600-ccfb-435c-bdd4-45644bc2c76f_2816x1536.png)

Calculations are computations from input to output. They always give the same output when you give them the same input. They do not depend on time, ordering, repetition, or external state.

In practice, calculations are where I want most of the meaning to live:

- Pricing rules
- Tax rules
- Validation
- Eligibility decisions
- Building view models
- Building effect plans
- Mapping from raw data shapes into domain shapes

#### Why I prefer calculations

Not because they are “pure”, but because they remove entire categories of worry:

- I do not need to care what else is running at the same time.
- I do not need to care what ran in the past.
- I do not need to care how many times it was called.
- I can test them without scaffolding the world.

That is a separation of concerns win: calculations isolate the “policy” concerns from the “mechanism” concerns.

#### What calculations cannot do

Calculations cannot guarantee that something actually happened. They can only describe what should happen or compute what a result should be.

That is not a weakness. It is the point.

A good design often looks like this:

- Calculations build a plan as data.
- Actions execute that plan at the boundary.

This is where “functional core and imperative shell” stops being a diagram and becomes a daily workflow.

### 3.3 Data

[![](https://substackcdn.com/image/fetch/$s_!72yI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32e09269-9449-4c4d-8c52-dd1562af4e01_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!72yI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32e09269-9449-4c4d-8c52-dd1562af4e01_2816x1536.png)

Data is the values your program uses. It includes:

- Inputs, outputs
- Intermediate representations
- Configuration
- Commands (when you represent “what to do” as values)

One of the biggest functional tricks is turning “effects” into data.

### 3.4 Data structures

Data structures are how you shape and organize data so that transformations are predictable and meaningful. In practice, for most application code, this means:

- Prefer plain objects and arrays that represent domain concepts clearly.
- Avoid mixing unrelated data in the same shape.
- Choose structures that reflect invariants.

Structure encodes meaning. When you choose a structure, you are making a statement about the problem:

- A list implies order matters.
- A set implies uniqueness matters.
- A map implies lookup by key matters.
- A nested object implies ownership and grouping.

Good data structures reduce the need for “clever logic” because the invariants are visible in the shape.

### 3.5 Separation of state and immutability

[![](https://substackcdn.com/image/fetch/$s_!PKox!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3224b52-4ba2-4b0b-be36-ce71bb883cd2_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!PKox!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3224b52-4ba2-4b0b-be36-ce71bb883cd2_2816x1536.png)

A common source of complexity is state that changes in place. Mutation hides history and makes it harder to reason locally.

Immutability is not a religion. It is a separation technique:

- Calculations produce new values rather than modifying existing ones.
- Actions are the parts that persist or display those new values.

In real systems, most change pressure concentrates at the edges:

- UI changes often
- Integration points change often
- Storage technology changes often
- Business rules also change, but you want them to change in isolation

If you can make the core logic operate on immutable data, the volatility stays near the boundaries.

### 3.6 The rule of contagion

[![](https://substackcdn.com/image/fetch/$s_!1gBQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92ef2abb-fce6-4973-b430-c9f4691385a7_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!1gBQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92ef2abb-fce6-4973-b430-c9f4691385a7_2816x1536.png)

Here is a rule that shows up in practice again and again: actions are “infectious”. If a function performs an action, everything that calls it becomes harder to test and reason about, and tends to become action shaped too. Side effects spread.

That propagation pressure is what I call the rule of contagion (also called the propagation rule): once you mix actions into a place, actions tend to spread outward through dependencies until you push them back to the edges.

A diagram version:

[![](https://substackcdn.com/image/fetch/$s_!HXp0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa86fffd4-6126-492e-ad8c-970292427ea4_1226x1022.png)](https://substackcdn.com/image/fetch/$s_!HXp0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa86fffd4-6126-492e-ad8c-970292427ea4_1226x1022.png)

The core stays calm. The shell deals with reality.

### 3.7 Explicit and implicit inputs and outputs

[![](https://substackcdn.com/image/fetch/$s_!r2BA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1588c301-d23c-4f9e-a6c6-f11362a08397_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!r2BA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1588c301-d23c-4f9e-a6c6-f11362a08397_2816x1536.png)

A huge amount of accidental complexity comes from implicit inputs and outputs.

- **Implicit inpu**t: reading a global variable, environment, singleton, localStorage, time.
- **Implicit output**: mutating global state, writing to localStorage, sending analytics, updating UI.

When inputs and outputs are implicit, you do not see dependencies in the function signature. That makes refactoring dangerous because the true dependency graph is hidden.

A very practical takeaway is: make functions smaller and make more calculations, because calculations are the easiest place to concentrate clarity.

## 4. Relating separation of concerns with actions, calculations, data, and data structures

At this point the connection should feel almost obvious:

- Separation of concerns is the general principle.
- Actions, calculations, data, and data structures are a concrete classification system that tells you what to separate.

### 4.1 A practical separation strategy

When I refactor toward separation, I follow a sequence like this:

- List concerns without changing code. What responsibilities are mixed here?
- Identify actions first. Actions are the most contagious and the hardest to test.
- Extract calculations next. Turn “business rules” into pure functions.
- Make inputs and outputs explicit. Pass dependencies in, return results out.
- Separate state updates. Prefer returning a new state over mutating.
- Represent effects as data. Have the core describe effects, and the shell execute them.
- Enforce dependency direction. Core must not import infrastructure.

This is both a refactor strategy and an architecture strategy.

### 4.2 Hierarchy of dependencies and hierarchy of preferences

Hierarchy of dependencies is about where dependencies are allowed to point.

In onion, hexagonal, and clean architecture families, the dependency rule is basically: dependencies point inward. The core should not depend on outer details like databases or frameworks.

Hierarchy of preferences is a related practical guideline: prefer to place volatile things in outer layers, and prefer to keep stable logic in inner layers.

[![](https://substackcdn.com/image/fetch/$s_!8ePS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F448389f0-8441-445a-886f-ee012769fbe8_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!8ePS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F448389f0-8441-445a-886f-ee012769fbe8_2816x1536.png)

My preference stack looks like this:

- Prefer calculations over actions.
- Prefer explicit inputs over implicit inputs.
- Prefer explicit outputs over implicit outputs.
- Prefer immutable state updates over mutation.
- Prefer representing decisions as data over hardwired conditionals.
- Prefer dependency injection (or explicit wiring) over hidden globals.

This preference hierarchy is not dogma. It is simply the set of choices that tends to make code easier to change.

## 5. A refactor exercise in JavaScript

This exercise is inspired by the kind of scenario used in Grokking Simplicity (for example, the MegaMart style examples). I am not reproducing the book verbatim. Instead, I am building a fully self contained version that demonstrates the same moves: isolate actions, extract calculations, make state explicit, and end with a functional core and imperative shell.

### 5.1 The starting point: “everything mixed” spaghetti code

Here is the starting point, intentionally messy. This is the sort of code that appears naturally when you are trying to ship.

```
// shopping-cart.js
const freeShippingThresholdInDollars = 20;
const taxRate = 0.1;

function addToCartAndUpdateEverything(productId, quantity) {
  const storedCartJson = localStorage.getItem("cart");
  const cart = storedCartJson ? JSON.parse(storedCartJson) : [];

  const product = window.catalog.find((item) =&gt; item.id === productId);

  cart.push({
    productId: product.id,
    name: product.name,
    price: product.price,
    quantity: quantity,
  });

  let subtotal = 0;
  for (const line of cart) {
    subtotal = subtotal + line.price * line.quantity;
  }

  let shipping = 0;
  if (subtotal &lt; freeShippingThresholdInDollars) {
    shipping = 5;
  }

  const tax = subtotal * taxRate;
  const total = subtotal + shipping + tax;

  document.querySelector("#subtotal").textContent = subtotal.toFixed(2);
  document.querySelector("#shipping").textContent = shipping.toFixed(2);
  document.querySelector("#tax").textContent = tax.toFixed(2);
  document.querySelector("#total").textContent = total.toFixed(2);

  localStorage.setItem("cart", JSON.stringify(cart));
  window.analytics.track("add_to_cart", { productId, quantity, total });
}
```

#### What concerns are mixed?

- Reading from localStorage (action)
- Parsing JSON (calculation)
- Looking up product in global catalog (action and implicit input)
- Updating cart state (state change)
- Computing totals (calculation)
- Rendering UI (action)
- Persisting cart (action)
- Tracking analytics (action)

### 5.2 Step 1: name things so humans can read them

This is pure tidying. No behavior change.

Goals:

- Remove abbreviations.
- Replace magic numbers with named constants.
- Make units obvious.
- Avoid floating point for money.

I switch to cents to avoid rounding surprises, and I use constants that describe intent.

```
const centsPerDollar = 100;

const freeShippingThresholdInCents = 20 * centsPerDollar;
const standardShippingCostInCents = 5 * centsPerDollar;

const taxRateAsPercent = 10;
const percentBase = 100;

function calculateTaxInCents(subtotalInCents) {
  return Math.round((subtotalInCents * taxRateAsPercent) / percentBase);
}
```

### 5.3 Step 2: make implicit inputs and outputs explicit

The original function reads from globals and writes to globals. That hides dependencies.

Here is the thinking: before splitting logic, I want to see what the function needs to do its job.

I introduce a parameter object style configuration and explicit dependencies:

```
function addToCartAndUpdateEverything({
  productId,
  quantity,
  catalog,
  loadCart,
  saveCart,
  renderTotals,
  trackEvent,
}) {
  const cart = loadCart();
  const product = catalog.find((item) =&gt; item.id === productId);

  // Still messy, but dependencies are now visible.
}
```

This is already separation of concerns in a quiet form: dependencies are now part of the interface.

This also avoids the long parameter list smell because the call site can use named keys.

### 5.4 Step 3: split actions from calculations

Now I explicitly identify actions:

- loadCart, saveCart
- renderTotals
- trackEvent
- catalog access (depending on how it is provided)

I want a pure calculation that takes data and returns data.

First, I separate “add line item” from everything else:

```
function addLineItem(cartLines, product, quantity) {
  return [
    ...cartLines,
    {
      productId: product.id,
      name: product.name,
      unitPriceInCents: product.priceInCents,
      quantity,
    },
  ];
}
```

Then I extract calculations for totals:

```
function calculateSubtotalInCents(cartLines) {
  const startingSubtotalInCents = 0;
  return cartLines.reduce((subtotalInCents, line) =&gt; {
    return subtotalInCents + line.unitPriceInCents * line.quantity;
  }, startingSubtotalInCents);
}

function calculateShippingInCents(subtotalInCents) {
  const qualifiesForFreeShipping = subtotalInCents &gt;= freeShippingThresholdInCents;
  return qualifiesForFreeShipping ? 0 : standardShippingCostInCents;
}

function calculateTotals(cartLines) {
  const subtotalInCents = calculateSubtotalInCents(cartLines);
  const shippingInCents = calculateShippingInCents(subtotalInCents);
  const taxInCents = calculateTaxInCents(subtotalInCents);
  const totalInCents = subtotalInCents + shippingInCents + taxInCents;

  return { subtotalInCents, shippingInCents, taxInCents, totalInCents };
}
```

At this point, most of the complexity is now in calculations, which are easy to test.

### 5.5 Step 4: separate state, prefer immutability

Instead of mutating the cart, every update returns a new cart.

This aligns with the “separation of state” idea: state updates become calculations.

Now our orchestration function can look like:

```
function addToCartAndUpdateEverything({
  productId,
  quantity,
  catalog,
  loadCart,
  saveCart,
  renderTotals,
  trackEvent,
}) {
  const cartLines = loadCart();
  const product = catalog.find((item) =&gt; item.id === productId);

  const nextCartLines = addLineItem(cartLines, product, quantity);
  const totals = calculateTotals(nextCartLines);

  renderTotals(totals);
  saveCart(nextCartLines);
  trackEvent("add_to_cart", { productId, quantity, totalInCents: totals.totalInCents });

  return nextCartLines;
}
```

This is better, but it still mixes actions (render, save, track) with orchestration.

### 5.6 Step 5: effects as data, functional core and imperative shell

Now we have a more readable code, and here is where separation of concerns start to “push“ us towards architectural design.

Instead of doing actions, the core returns a list of effects to be performed.

#### Functional core

```
const effectTypeRenderCartTotals = "render_cart_totals";
const effectTypePersistCart = "persist_cart";
const effectTypeTrackAnalyticsEvent = "track_analytics_event";

function addToCartCore({ cartLines, product, quantity }) {
  const nextCartLines = addLineItem(cartLines, product, quantity);
  const totals = calculateTotals(nextCartLines);

  const effects = [
    { type: effectTypeRenderCartTotals, totals },
    { type: effectTypePersistCart, cartLines: nextCartLines },
    {
      type: effectTypeTrackAnalyticsEvent,
      eventName: "add_to_cart",
      payload: { productId: product.id, quantity, totalInCents: totals.totalInCents },
    },
  ];

  return { nextCartLines, effects };
}
```

This is calculation. Even the “effects” are just data structures.

#### Imperative shell

Now we need something that executes those effects. This is where a function like `runEffects` comes from. It does not exist in the original spaghetti code because we only need it after we adopt this architecture.

```
function runEffects({ effects, dependencies }) {
  for (const effect of effects) {
    if (effect.type === effectTypeRenderCartTotals) {
      dependencies.renderTotals(effect.totals);
    }

    if (effect.type === effectTypePersistCart) {
      dependencies.saveCart(effect.cartLines);
    }

    if (effect.type === effectTypeTrackAnalyticsEvent) {
      dependencies.trackEvent(effect.eventName, effect.payload);
    }
  }
}
```

The functional core stays calm. The imperative shell deals with reality.

### 5.7 Step 6: the effect runner, and why it is a great place to improve design

The first `runEffects` is intentionally simple. In production, it often grows into a change hotspot.

It is also a great place to improve design because it concentrates your action boundary:

- If you make the interpreter better, you make the boundary cleaner.
- If you inject dependencies properly here, you reduce global coupling everywhere.

### 5.8 Step 7: inversion of control, dependency inversion, ports and adapters, and the configurator

The goal is not to “be object oriented”. The goal is to stop growing a conditional switchboard and to make change local.

#### Option A: table driven dispatch (simple IoC in JavaScript)

This replaces conditionals with a dictionary of handlers. It is inversion of control because the runner no longer decides behavior. The mapping does.

```
function createEffectHandlers(dependencies) {
  return {
    [effectTypeRenderCartTotals]: (effect) =&gt; dependencies.renderTotals(effect.totals),
    [effectTypePersistCart]: (effect) =&gt; dependencies.saveCart(effect.cartLines),
    [effectTypeTrackAnalyticsEvent]: (effect) =&gt;
      dependencies.trackEvent(effect.eventName, effect.payload),
  };
}

function runEffects({ effects, effectHandlers }) {
  for (const effect of effects) {
    const handler = effectHandlers[effect.type];
    if (!handler) {
      throw new Error(`No handler registered for effect type: ${effect.type}`);
    }
    handler(effect);
  }
}
```

#### Option B: command pattern style objects

If you want polymorphism, you can represent effects as command objects with an `execute` method. This removes the type check entirely.

```
function createRenderCartTotalsCommand(totals) {
  return {
    execute: (dependencies) =&gt; dependencies.renderTotals(totals),
  };
}

function createPersistCartCommand(cartLines) {
  return {
    execute: (dependencies) =&gt; dependencies.saveCart(cartLines),
  };
}

function createTrackEventCommand(eventName, payload) {
  return {
    execute: (dependencies) =&gt; dependencies.trackEvent(eventName, payload),
  };
}

function runCommands({ commands, dependencies }) {
  for (const command of commands) {
    command.execute(dependencies);
  }
}
```

Which option is “better” depends on the needs of your system. The important part is that the effect boundary remains clean: calculations create intent, actions interpret intent.

#### Ports and adapters, and the configurator

If you squint, we have already built ports and adapters:

- Ports: `renderTotals`, `saveCart`, `trackEvent`, `loadCart`
- Adapters: DOM rendering implementation, localStorage implementation, analytics implementation

What is missing is a clear place where wiring happens. That wiring is the configurator, also commonly called the composition root.

Here is a simple configurator:

```
function createShoppingCartApplication({ catalog, documentRef, localStorageRef, analyticsRef }) {
  function loadCart() {
    const cartJson = localStorageRef.getItem("cart");
    return cartJson ? JSON.parse(cartJson) : [];
  }

  function saveCart(cartLines) {
    localStorageRef.setItem("cart", JSON.stringify(cartLines));
  }

  function renderTotals(totals) {
    documentRef.querySelector("#subtotal").textContent = formatMoney(totals.subtotalInCents);
    documentRef.querySelector("#shipping").textContent = formatMoney(totals.shippingInCents);
    documentRef.querySelector("#tax").textContent = formatMoney(totals.taxInCents);
    documentRef.querySelector("#total").textContent = formatMoney(totals.totalInCents);
  }

  function trackEvent(eventName, payload) {
    analyticsRef.track(eventName, payload);
  }

  const dependencies = { renderTotals, saveCart, trackEvent };
  const effectHandlers = createEffectHandlers(dependencies);

  function addToCart({ productId, quantity }) {
    const cartLines = loadCart();
    const product = catalog.find((item) =&gt; item.id === productId);

    const { nextCartLines, effects } = addToCartCore({ cartLines, product, quantity });
    runEffects({ effects, effectHandlers });

    return nextCartLines;
  }

  return { addToCart };
}

function formatMoney(amountInCents) {
  const dollars = amountInCents / 100;
  return dollars.toFixed(2);
}
```

Notice what happened:

- The core never imports DOM, localStorage, analytics.
- The configurator owns real world dependencies.
- Dependency direction is clear.
- Testing the core is trivial. Testing the shell is focused.

### 5.9 Final code: from spaghetti to separations

[![](https://substackcdn.com/image/fetch/$s_!wScA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdadbc2b3-6b5c-4866-9dc5-5de9c8452589_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!wScA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdadbc2b3-6b5c-4866-9dc5-5de9c8452589_2816x1536.png)

The end result is not “more code”. It is more structure. And structure is what gives you properties:

- Testability: core logic is pure.
- Reusability: calculations can be used anywhere.
- Reliability: fewer hidden dependencies.
- Change isolation: UI changes do not threaten business rules.
- Potential resilience: failures in adapters can be handled at the shell without corrupting the core.

## 6. Architecture: onion, clean architecture, and why the same rule keeps winning

Onion architecture emphasizes separation of concerns across the whole system and pushes infrastructure outward. Hexagonal architecture frames the same idea as ports and adapters: the application is inside, external agents are outside, and communication happens through ports. Clean architecture generalizes the dependency rule: source code dependencies must point inward toward the core.

This is why functional core and imperative shell is not “a different idea”. It is the same boundary rule applied with functional language: keep calculations at the center, and push actions to the shell.

But **the important thing to remember at this point that the root for all this “architectures“ is the same the Separation of Concerns principle** and now we are only using a way of understanding functions to separate the concers.

A diagrammatic way to connect them:

[![](https://substackcdn.com/image/fetch/$s_!3vza!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F241cdda0-dfa4-4c50-8e71-94ccef03567d_1226x970.png)](https://substackcdn.com/image/fetch/$s_!3vza!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F241cdda0-dfa4-4c50-8e71-94ccef03567d_1226x970.png)

The rule is not “never touch the outside”. The rule is: make the outside call inward, not the other way around.

## 7. Simplicity as a discipline

Simplicity is not something you get by accident. It is something you practice.

The discipline is:

- Keep changes small.
- Keep the system working.
- Improve structure so behavior changes become easier.
- Use names, constants, and small extractions as tools for thinking.

In the refactor above, the first moves were not “architecture”. They were tidyings:

- naming
- constants
- making units explicit
- extracting calculations

That is simplicity as a discipline: doing the small, boring things that make the next step safe.

## 8. Conclusions

In my conclusions, I would say that this is one of the most relevant software principles and that without any doubt it is where many people should start.

Separation of concerns is not a slogan. It is a working tool:

- It organizes thinking.
- It organizes change.
- It shapes architectures (ports and adapters, onion, clean architecture, Imerative shell and functional core).
- It becomes practical in everyday refactoring when you separate actions from calculations and treat effects as data.

If you internalize these ideas, you get more than clean code. You get code that stays alive.

[![](https://substackcdn.com/image/fetch/$s_!R5nn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12684a4f-e539-45e6-b04a-32d2f8da8e84_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!R5nn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12684a4f-e539-45e6-b04a-32d2f8da8e84_2816x1536.png)

And remember my idea is not to push functional programming, or any of the other topics I’ve mention, I just want that people learn to see the importance of SoC and give them the tools to know how to do it.

---

Thanks for reading Crafting software! This post is public so feel free to share it.

[Share](https://emmanuelvalverderamos.substack.com/p/separation-of-concerns-functional?utm_source=substack&utm_medium=email&utm_content=share&action=share)

---

## References

### Core concepts and history

- Edsger W. Dijkstra. *On the role of scientific thought (EWD447)* (1974). [https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html)
- David L. Parnas. *On the criteria to be used in decomposing systems into modules* (Communications of the ACM, 1972). [https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf](https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf)
- Fran Iglesias Gómez. *Separation of concerns*. [https://franiglesias.github.io/separation-of-concerns/](https://franiglesias.github.io/separation-of-concerns/)
- Robert C. Martin. *The single responsibility principle* (The Clean Code Blog, 2014). [https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)

### Functional thinking

- Eric Normand. *Grokking Simplicity: Taming complex software with functional thinking*. Manning Publications. [https://www.manning.com/books/grokking-simplicity](https://www.manning.com/books/grokking-simplicity)

### Refactoring and tidyings

- Kent Beck. *Tidy First?* [https://www.oreilly.com/library/view/tidy-first/9781098151232/](https://www.oreilly.com/library/view/tidy-first/9781098151232/)
- Martin Fowler. *Refactoring: Improving the design of existing code* (2nd ed.). [https://refactoring.com/catalog/](https://refactoring.com/catalog/)

### Architecture

- Alistair Cockburn. *Hexagonal architecture* (Ports and adapters). [https://alistair.cockburn.us/hexagonal-architecture](https://alistair.cockburn.us/hexagonal-architecture)
- Jeffrey Palermo. *The Onion Architecture: part 1*. [https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/)
- Gary Bernhardt. *Functional core, imperative shell*. [https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)
- Gary Bernhardt. *Boundaries*. [https://www.destroyallsoftware.com/talks/boundaries](https://www.destroyallsoftware.com/talks/boundaries)

### Smells and refactorings

- Refactoring.Guru. *Long method*. [https://refactoring.guru/smells/long-method](https://refactoring.guru/smells/long-method)
- Refactoring.Guru. *Primitive obsession*. [https://refactoring.guru/smells/primitive-obsession](https://refactoring.guru/smells/primitive-obsession)
- Refactoring.Guru. *Divergent change*. [https://refactoring.guru/smells/divergent-change](https://refactoring.guru/smells/divergent-change)
- Refactoring.Guru. *Long parameter list*. [https://refactoring.guru/smells/long-parameter-list](https://refactoring.guru/smells/long-parameter-list)
- Refactoring.Guru. *Shotgun surgery*. [https://refactoring.guru/smells/shotgun-surgery](https://refactoring.guru/smells/shotgun-surgery)
- Refactoring.Guru. *Replace conditional with polymorphism*. [https://refactoring.guru/replace-conditional-with-polymorphism](https://refactoring.guru/replace-conditional-with-polymorphism)
