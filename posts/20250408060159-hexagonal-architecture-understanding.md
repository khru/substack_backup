---
title: "🛑 Hexagonal Architecture: Understanding Ports & Adapters"
requested_url: "https://emmanuelvalverderamos.substack.com/p/hexagonal-architecture-understanding"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/hexagonal-architecture-understanding"
substack_post_id: 160764100
retrieved_at: "2026-03-14T08:30:00.438Z"
---
# 🛑 Hexagonal Architecture: Understanding Ports & Adapters

## Definition and Context

> “Hexagonal Architecture has served well as a hook [...] However, the correct name is **Ports &amp; Adapters**.”

> - Alistair Cockburn​

> “The main problem with the term 'Hexagonal Architecture' is that it leads people to just draw hexagons all over the place [...] without implementing Ports &amp; Adapters.”

> - Alistair Cockburn​

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### 🧱 What is Software Architecture?

Software architecture is not your tech stack. It's not diagrams or folder trees. It’s the **shared mental model** that guides critical decisions about a system.

As Martin Fowler puts it:

> “It’s the shared understanding held by the expert developers.”
> - [What is Software Architecture](https://youtu.be/BVMngYKJ4hk)

> “Architecture is about the important stuff… whatever that is.”
> - Ralph Johnson, quoted in *Fundamentals of Software Architecture*

> “If you ask what the architecture is, and people show you a folder structure, you have a problem.”
> - Greg Young

> “Software architecture is more like city planning than building construction.”
> - Martin Fowler

It’s the “important stuff”, things that if done wrong, are hard to fix later.

---

### 🧩 What is Hexagonal Architecture?

Ports &amp; Adapters (Hexagonal Architecture) proposes two main zones: Inside (application logic) and Outside (everything else). Only the application (inside) owns the definitions of communication: ports.

[![](https://substackcdn.com/image/fetch/$s_!m6aJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2ee38b9-fea9-4a65-975e-d5a1180bf73d_1888x843.png)](https://substackcdn.com/image/fetch/$s_!m6aJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2ee38b9-fea9-4a65-975e-d5a1180bf73d_1888x843.png)

**Hexagonal Architecture**, also called **Ports and Adapters**, was introduced by Alistair Cockburn to solve a common problem:

> ❓ *How do we isolate the domain logic from external technologies like frameworks, databases, or UIs?*

The answer? **Invert the dependencies**. The application is at the center, exposing **ports** (interfaces), with external systems interacting via **adapters**.

This allows:

- Plugging in different UIs (CLI, Web, API)
- Swapping databases or services
- Writing meaningful tests, without touching business logic

> "Create your application to work without either a UI or a database so you can run automated regression-tests [...] and link applications together without any user involvement."
> - Alistair Cockburn​

⚠️ Hexagonal Architecture is not about folders, hexagons, or rigid layering.

### **What is a Port?**

A *port* is an interface. It defines a contract between the application and the outside world.

- **Driving Port**: what the app exposes to be *called* (e.g. UI, CLI, tests).
- **Driven Port**: what the app *calls* to obtain resources (e.g. database, services).

### **What is an Adapter?**

An *adapter* implements a port. It’s the glue between the app and external tech.

- For driving ports: adapters **call** the app (e.g. UI adapter).
- For driven ports: adapters are **called by** the app (e.g. DB adapter).

## Benefits

[![](https://substackcdn.com/image/fetch/$s_!4Qln!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a143711-2557-4f9f-a628-c69ec8ecf9da_1877x965.png)](https://substackcdn.com/image/fetch/$s_!4Qln!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a143711-2557-4f9f-a628-c69ec8ecf9da_1877x965.png)

> “The application is blissfully ignorant of the nature of the input device.”
> - Alistair Cockburn

One of the most powerful benefits is the deep decoupling from technology. The application doesn't care if tomorrow we replace the database, the web framework, or the storage mechanism.

Also, testability skyrockets. You can test the core business logic without involving infrastructure, by replacing adapters with simple fakes or stubs during tests.

From Cockburn’s own visual explanation:

[![](https://substackcdn.com/image/fetch/$s_!sTFB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe55b951e-fa43-48c2-b2d1-dc9806b75178_1882x919.png)](https://substackcdn.com/image/fetch/$s_!sTFB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe55b951e-fa43-48c2-b2d1-dc9806b75178_1882x919.png)

✅ **You can**:

- Swap out real adapters for test boubles in tests
- Change databases, UI, or protocols without rewriting your app
- Prevent tech-specific leakage into domain logic

📌 Diagram summary:

[![](https://substackcdn.com/image/fetch/$s_!0Wxh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ef3771b-adea-47d4-92c2-948b46fbd16f_2083x2238.png)](https://substackcdn.com/image/fetch/$s_!0Wxh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ef3771b-adea-47d4-92c2-948b46fbd16f_2083x2238.png)

## Costs

[![](https://substackcdn.com/image/fetch/$s_!StkL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2529f898-d623-4471-9ed5-3d2d266f449f_1846x857.png)](https://substackcdn.com/image/fetch/$s_!StkL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2529f898-d623-4471-9ed5-3d2d266f449f_1846x857.png)

🚧 As Cockburn outlines clearly, there are trade-offs:

- Extra interfaces to declare (especially in Java/C# or any other typed lang.)
- Configurators to write
- Slight complexity in setup
- Needs practice and discipline

> Ports &amp; Adapters introduces one more level of indirection on the driven side [...] might introduce additional mappers [...] learning this architecture is hard.”
> - Alistair Cockburn

🧠 But these costs are **cheap insurance** for long-lived or mission-critical systems.

Besides the initial design effort, the real cost lies in the discipline required to keep respecting the architecture over time. It's easy to accidentally let business logic leak into adapters or configuration code if we aren't constantly vigilant.

## Practical Example: Tax Rate Calculator

Let’s explore the **TaxCalculator** use case. It's simple, clear, and powerful.

### Components:

- **Interactor**: `TaxCalculator`
- **Driven port**: `ForGettingTaxRates`
- **Driving port**: `ForCalculatingTaxes`
- **Adapter**: `FixedRateRepository`
- **Configurator**: `Main.java`

**Inside:** `TaxCalculator` implements the business rules.
**Outside:** `FixedTaxRateRepository` is a basic adapter that supplies data to the application via a port.

### Java Code

```java
interface ForCalculatingTaxes {
    double taxOn(double amount);
}
```

```java

interface ForGettingTaxRates {
    double taxRate(double amount);
}
```

- `ForCalculatingTaxes`: defines what the system provides (calculating taxes).
- `ForGettingTaxRates`: defines what the system requires (obtaining tax rates).

```java
class TaxCalculator implements ForCalculatingTaxes {
    private ForGettingTaxRates taxRateRepository;

    public TaxCalculator(ForGettingTaxRates taxRateRepository) {
        this.taxRateRepository = taxRateRepository;
    }

    public double taxOn(double amount) {
        return amount * taxRateRepository.taxRate(amount);
    }
}
```

`TaxCalculator`: Implements the business logic. It uses a secondary adapter (tax rates repository) through the `ForGettingTaxRates` port.

```java
class FixedTaxRateRepository implements ForGettingTaxRates {
    public double taxRate(double amount) {
        return 0.15;
    }
}
```

- `FixedTaxRateRepository`: A simple, fixed implementation of the
- `ForGettingTaxRates`port.

```java
class Main {
    public static void main(String[] args) {
        ForGettingTaxRates taxRateRepository = new FixedTaxRateRepository();
        ForCalculatingTaxes myCalculator = new TaxCalculator(taxRateRepository);

        System.out.println(myCalculator.taxOn(100));
    }
}
```

- Here, the adapters are configured, and the system is invoked using the ports.
- This is the typical entry point for a Java application (`main` method), acting as a configurator.

## What is an Interactor?

[![](https://substackcdn.com/image/fetch/$s_!6jxK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2aa7e3e-0eb7-4170-ad9a-9494c4b8f624_1872x889.png)](https://substackcdn.com/image/fetch/$s_!6jxK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2aa7e3e-0eb7-4170-ad9a-9494c4b8f624_1872x889.png)

The **Interactor** (app logic) sits in the middle. It talks through **ports** (interfaces). External things plug in through **adapters**.

Key Principle: **The application owns its interfaces**.

From the diagram:

[![](https://substackcdn.com/image/fetch/$s_!bxIh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4f0b11f-4c65-40f9-9028-f88aa667767b_4741x786.png)](https://substackcdn.com/image/fetch/$s_!bxIh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4f0b11f-4c65-40f9-9028-f88aa667767b_4741x786.png)

The interactor:

- Implements the business rules
- Talks only to **ports**
- Doesn’t know what adapter it talks to

## 🚀 Production vs Testing 🧪

One of the major benefits of using Hexagonal Architecture (Ports &amp; Adapters) is that it simplifies switching between different runtime contexts, particularly between **production** and **testing**, without having to modify your core application logic.

> “With clearly defined ports, you can run automated tests with mocks, and swap adapters without modifying the application.”
> - Alistair Cockburn​

The key idea behind this flexibility lies in leveraging clearly defined ports and adapters. The application remains completely unaware of the concrete implementations it interacts with, enabling you to swap adapters seamlessly.

Let's explore this clearly with practical examples:

#### 🧪 Testing

[![](https://substackcdn.com/image/fetch/$s_!GKmH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8404fd70-22d4-4c6f-92e5-c04f966d83db_1886x828.png)](https://substackcdn.com/image/fetch/$s_!GKmH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8404fd70-22d4-4c6f-92e5-c04f966d83db_1886x828.png)

When writing tests, you want predictable, controlled environments that isolate the business logic from external systems. This is where the use of fake or stub adapters comes in handy.

Consider the following example:

To showcase the flexibility and testability of Hexagonal Architecture, let's clearly separate **production code** from **testing code**.

We'll have:

- **Production Code**
	- `ForGettingTaxRates`(Driven Port interface)
	- `TaxCalculator`(Core business logic)
- **Testing Code**
	- `TaxCalculatorTest`(JUnit test class using a stub/fake implementation)

Production code:

```java
public interface ForGettingTaxRates {
    double taxRate(double amount);
}
```

```java
public class TaxCalculator {

    private final ForGettingTaxRates taxRateRepository;

    public TaxCalculator(ForGettingTaxRates taxRateRepository) {
        this.taxRateRepository = taxRateRepository;
    }

    public double taxOn(double amount) {
        return amount * taxRateRepository.taxRate(amount);
    }
}
```

Testing code:

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TaxCalculatorTest {

    // Fake implementation (stub) for testing
    static class FakeTaxRateRepository implements ForGettingTaxRates {
        @Override
        public double taxRate(double amount) {
            return 0.10;  // predictable fixed rate (10%)
        }
    }

    @Test
    void calculatesTaxCorrectly() {
        // Arrange
        ForGettingTaxRates fakeRepository = new FakeTaxRateRepository();
        TaxCalculator calculator = new TaxCalculator(fakeRepository);

        double amount = 100.0;
        double expectedTax = 10.0; // 10% of 100

        // Act
        double calculatedTax = calculator.taxOn(amount);

        // Assert
        assertEquals(expectedTax, calculatedTax, 0.0001);
    }
}
```

### 🔍 Detailed Explanation of the Test Case

- **Arrange**:
	- We create a **fake adapter** (`FakeTaxRateRepository`) that returns a fixed tax rate. This ensures our test remains **predictable and isolated** from any external resource.
- **Act**:
	- We use this fake adapter with our core business logic (`TaxCalculator`) to perform the calculation.
- **Assert**:
	- We verify the calculated tax amount matches our expected result using JUnit assertions (`assertEquals`)

### 🎯 Benefits of this Approach:

- **Isolation from External Systems**:
	- Tests don't rely on files, databases, or APIs.
- **Predictable and Fast**:
	- Tests run quickly and reliably, always returning consistent results.
- **Easy to Maintain and Refactor**:
	- Changes to external implementations (databases, files, APIs) do **not** affect these unit tests.
- **Clear Separation of Concerns**:
	- Production and test code are entirely independent. Production code remains untouched by testing details.

### 🚀 Production

```java
// Driven port defined by the app
public interface ForGettingTaxRates {
    double taxRate(double amount);
}
```

```java
// Real adapter reading rates from a file
public class FileTaxRateRepository implements ForGettingTaxRates {
    private final String filename;

    public FileTaxRateRepository(String filename) {
        this.filename = filename;
    }

    @Override
    public double taxRate(double amount) {
        // Actual file reading logic goes here...
        // (e.g., parsing rates.txt and returning real rate)
        return 0.21; // Simplified real scenario
    }
}
```

```java
// Production configuration (main method)
public class Main {
    public static void main(String[] args) {
        ForGettingTaxRates fileRepo = new FileTaxRateRepository("rates.txt");
        TaxCalculator calculator = new TaxCalculator(fileRepo);

        double tax = calculator.taxOn(100);
        System.out.println("Calculated Tax: " + tax); // Outputs real calculated tax
    }
}
```

### Benefits for Production:

- **Realistic:** Connects to actual resources, delivering the behavior your users expect.
- **Flexible:** Simple to swap adapters without code changes in core logic, for example, from files to databases or web services.
- **Maintainable:** If the external resource changes (file to database), only the adapter implementation changes, leaving the core untouched.

### 💡 Key insight: No changes in core logic

An essential advantage of Hexagonal Architecture becomes clear here:

- **No change is required in your core application logic (**`TaxCalculator`**) between testing and production environments.**
- The only difference is which adapter you inject into your application. This simplifies deployment, reduces risk, and accelerates your development and testing processes significantly.

Consider again clearly:

```java
// The application logic remains untouched:
class TaxCalculator {
    private final ForGettingTaxRates taxRateRepository;

    public TaxCalculator(ForGettingTaxRates taxRateRepository) {
        this.taxRateRepository = taxRateRepository;
    }

    public double taxOn(double amount) {
        return amount * taxRateRepository.taxRate(amount);
    }
}
```

Whether you use a fake adapter (testing):

```java
ForGettingTaxRates fake = amount -&gt; 1.1;
TaxCalculator calculator = new TaxCalculator(fake);
```

Or a real adapter (production):

```java
ForGettingTaxRates fileRepo = new FileTaxRateRepository("rates.txt");
TaxCalculator calculator = new TaxCalculator(fileRepo);
```

Your core logic (`TaxCalculator`) remains stable and unmodified.

---

## Driving vs Driven Ports

[![](https://substackcdn.com/image/fetch/$s_!KSqh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01ca3d15-b0b0-4b1e-ace3-87f10178275c_1887x892.png)](https://substackcdn.com/image/fetch/$s_!KSqh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01ca3d15-b0b0-4b1e-ace3-87f10178275c_1887x892.png)

Here's a clear, detailed, and practical explanation of the difference between **Driving** and **Driven** Ports in Hexagonal Architecture, along with practical examples, ownership clarification, and implementation details:

In Hexagonal Architecture (Ports and Adapters), the concept of "ports" is fundamental. Ports represent the clear boundaries between your business logic (the core application) and external entities (such as databases, user interfaces, or external services). These boundaries fall into two distinct types:

- **Driving Ports**
- **Driven Ports**

Let's clearly distinguish them:

[![](https://substackcdn.com/image/fetch/$s_!o_gm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F586f091a-4bf6-4fb0-ab8b-01a3f1ba3aec_1990x1728.png)](https://substackcdn.com/image/fetch/$s_!o_gm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F586f091a-4bf6-4fb0-ab8b-01a3f1ba3aec_1990x1728.png)

Hexagonal Architecture doesn't officially use “**primary**” and “**secondary**” ports, but the mapping is common:

- **Primary Port ≈ Driving Port**
- **Secondary Port ≈ Driven Port**

The naming may vary, but the **direction and ownership** stay the same.

### 🚗 Driving Ports (Primary Ports)

**Direction**: External → App (incoming calls)

**Definition**:
A driving port exposes functionalities that your application provides. These ports allow external actors (like command-line interfaces, web APIs, mobile apps, or test suites) to invoke actions within your application.

**Ownership**:
The **application itself** defines and owns the driving ports. This means the core application is responsible for clearly specifying interfaces that external entities must use to interact with it.

#### Practical Example:

```java
// Driving Port defined by the application
public interface ForCalculatingTaxes {
    double taxOn(double amount);
}

// Application implements the Driving Port
public class TaxCalculator implements ForCalculatingTaxes {
    private final ForGettingTaxRates taxRateRepository;

    public TaxCalculator(ForGettingTaxRates taxRateRepository) {
        this.taxRateRepository = taxRateRepository;
    }

    @Override
    public double taxOn(double amount) {
        return amount * taxRateRepository.taxRate(amount);
    }
}
```

In this example:

- **ForCalculatingTaxes** is a driving port: the application defines it, and external entities use it to interact with the application.
- The application itself (via `TaxCalculator`) provides the implementation, making this functionality accessible externally (from a CLI, REST API, or unit test).

### ⚙️ Driven Ports (Secondary Ports)

**Direction**: App → External (outgoing calls)

**Definition**:
A driven port defines functionalities that your application requires from external systems. It represents external services the application needs (like databases, external APIs, messaging queues, etc.) to fulfill its responsibilities.

**Ownership**:
The **application itself** also owns the driven ports. The application specifies clearly defined interfaces describing exactly what external services it expects.

#### Practical Example:

```java
// Driven Port defined by the application
public interface ForGettingTaxRates {
    double taxRate(double amount);
}

// Adapter implementing Driven Port (External service or system)
public class FixedTaxRateRepository implements ForGettingTaxRates {
    @Override
    public double taxRate(double amount) {
        return 0.15; // Example implementation
    }
}
```

In this example:

- `ForGettingTaxRates`is a driven port: the application defines exactly what it needs (e.g., tax rates from external repositories), but doesn't implement it directly.
- The external adapter (e.g., `FixedTaxRateRepository`) provides an implementation of this interface, fulfilling the requirement described by the driven port.

### 🎯 Ownership Clarified

A key point to remember is that the **application owns and defines both types of ports** (Driving and Driven):

- **Driving Ports** are interfaces the application provides **for external actors**.
- **Driven Ports** are interfaces the application **requires external actors to fulfill**.

[![](https://substackcdn.com/image/fetch/$s_!hlJL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9adc3b69-78e3-495e-81d8-e98f48a2532a_1868x845.png)](https://substackcdn.com/image/fetch/$s_!hlJL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9adc3b69-78e3-495e-81d8-e98f48a2532a_1868x845.png)

This ownership principle helps maintain control and flexibility within the application's boundaries.

In Hexagonal Architecture, execution flows from the application outward (e.g., the app calls the database). However, **compile-time dependencies flow the opposite way**: adapters depend on the app, never the app on the adapters.

This inversion protects the core from external technology changes.

### 📐 Visualizing Driving vs Driven Ports

Here's a simplified diagram illustrating the directions and ownership clearly:

[![](https://substackcdn.com/image/fetch/$s_!ywFj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6fd68a9-c429-4580-a3f6-c9174b97bd42_4741x813.png)](https://substackcdn.com/image/fetch/$s_!ywFj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6fd68a9-c429-4580-a3f6-c9174b97bd42_4741x813.png)

- **Driving Port**: external → application (calls into the app)
- **Driven Port**: application → external (calls out from the app)

[![](https://substackcdn.com/image/fetch/$s_!7ujg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0451b444-9011-4924-8061-d8900a0052d4_1889x876.png)](https://substackcdn.com/image/fetch/$s_!7ujg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0451b444-9011-4924-8061-d8900a0052d4_1889x876.png)

## 🚩 Common Pitfalls &amp; Tips

- **Avoid Leaky Abstractions:**
	Keep ports focused purely on business logic interactions. Ports should never expose specific technology details (e.g., SQL syntax, web framework annotations).
- **Ownership discipline:**
	Always ensure your application explicitly defines both driving and driven ports. External libraries or frameworks should never dictate your business logic or interfaces.
- **Single Responsibility:**
	Each port should clearly represent one cohesive responsibility or intention. Avoid large, overly generic ports.

## 🧠 When and How to Apply Ports Effectively

- Clearly identify and define driving ports to expose your application functionalities (e.g., "calculate tax," "register user," "submit order").
- Clearly identify driven ports to describe external functionalities you depend upon (e.g., "get tax rates," "store user information," "send notification").
- Implement adapters separately, cleanly mapping these ports to external services or UI layers.

## Recommended Folder Structure (Cockburn-style)

[![](https://substackcdn.com/image/fetch/$s_!Zz9H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad70edb2-c438-4a4e-a1ac-2a02a66b5956_1872x896.png)](https://substackcdn.com/image/fetch/$s_!Zz9H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad70edb2-c438-4a4e-a1ac-2a02a66b5956_1872x896.png)

This is just a recomendation from the author, does not mean we have to use it.

```
TaxCalculatorApp
├── DrivenPorts
│   ├── ForPaying.java
│   ├── ForObtainingRates.java
│   └── ForStoringTickets.java
├── DrivingPorts
│   ├── ForCheckingCars.java
│   ├── ForConfiguringApp.java
│   └── ForParkingCars.java
└── TaxCalculator
```

```
DrivenAdapters
├── bluezone-adapter-forpaying-spy
├── bluezone-adapter-forobtainingrates-stub
└── bluezone-adapter-forstoringtickets-fake

DrivingAdapters
├── bluezone-driver-forcheckingcars-test
├── bluezone-adapter-forparkingcars-webui
└── bluezone-driver-forparkingcars-test
```

## Configurator Design

Here's a more detailed and practical explanation of **Configurator Design** in Hexagonal Architecture, clearly elaborating on both approaches, **Dependency Injection** and **Dependency Lookup (Service Locator)**, including practical examples, diagrams, and advice on when to use each one:

# Configurator Design in Hexagonal Architecture

[![](https://substackcdn.com/image/fetch/$s_!t6AK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a19917-337f-488b-95eb-e914406a43f4_1883x855.png)](https://substackcdn.com/image/fetch/$s_!t6AK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a19917-337f-488b-95eb-e914406a43f4_1883x855.png)

In Hexagonal Architecture, the **Configurator** is the component or mechanism responsible for wiring your application components together. It's the place where you connect your ports (interfaces) with your adapters (concrete implementations). The configurator itself **should not contain business logic**, but should purely manage dependencies.

Alistair Cockburn emphasizes clearly separating configuration from core business logic. Let's deeply explore two popular approaches to achieve this:

## ✅ Approach 1: Dependency Injection

**Dependency Injection (DI)** is about explicitly passing dependencies into your objects, typically through constructors or setter methods. The class receiving the dependency doesn't know where the implementation comes from; it simply accepts whatever fulfills the defined port (interface).

Here's a clear Java example using Dependency Injection with a constructor:

### Example: Tax Calculator (Dependency Injection)

[![](https://substackcdn.com/image/fetch/$s_!lw9W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe454f98e-4d08-4d91-a3f3-77dd1f529969_1877x883.png)](https://substackcdn.com/image/fetch/$s_!lw9W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe454f98e-4d08-4d91-a3f3-77dd1f529969_1877x883.png)

```java
interface ForGettingTaxRates {
    double taxRate(double amount);
}
```

```java
class FileTaxRateRepository implements ForGettingTaxRates {
    private final String filename;

    public FileTaxRateRepository(String filename) {
        this.filename = filename;
    }

    public double taxRate(double amount) {
        // Reads tax rate from a file (implementation detail)
        return 0.20; // Simplified example
    }
}
```

```java
class TaxCalculator {
    private final ForGettingTaxRates taxRateRepository;

    public TaxCalculator(ForGettingTaxRates taxRateRepository) {
        this.taxRateRepository = taxRateRepository;
    }

    public double taxOn(double amount) {
        return amount * taxRateRepository.taxRate(amount);
    }
}
```

```java
// Configurator (often located in your app entry-point)
public class Main {
    public static void main(String[] args) {
        // Injecting dependencies explicitly
        TaxCalculator calc = new TaxCalculator(
            new FileTaxRateRepository("rates.txt")
        );

        System.out.println(calc.taxOn(100));
    }
}
```

### Benefits of Dependency Injection:

- **Explicit and Clear:** Clearly defines dependencies, making the code easier to understand.
- **Testability:** Simple to test, because you can easily substitute mocks or stubs.
- **Flexibility:** Easy to swap implementations without changing core logic.

### When to use:

- When dependencies are relatively static or known at compile-time.
- Ideal for applications that need simplicity and clarity.

## ✅ Approach 2: Dependency Lookup (Service Locator)

**Dependency Lookup (also known as Service Locator)** is when your object actively queries another object (usually called a broker, locator, or factory) to obtain the correct dependency at runtime.

Here's a practical Java example demonstrating Dependency Lookup with a "broker" or "locator":

### Example: Tax Calculator (Dependency Lookup)

[![](https://substackcdn.com/image/fetch/$s_!RPqS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e8d9f7e-e958-45ed-90d8-03b8531dc920_1878x900.png)](https://substackcdn.com/image/fetch/$s_!RPqS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e8d9f7e-e958-45ed-90d8-03b8531dc920_1878x900.png)

In the following example I will talk about how it could be if production would need different tax rates per country, but it could be the same for production or test.

```java
interface ForGettingTaxRates {
    double taxRate(double amount);
}
```

```java
class USTaxRateRepository implements ForGettingTaxRates {
    public double taxRate(double amount) {
        return 0.07; // US-specific rate example
    }
}
```

```java
class EUTaxRateRepository implements ForGettingTaxRates {
    public double taxRate(double amount) {
        return 0.20; // EU-specific rate example
    }
}
```

```java
// this could be a factory but is just an example
class TaxRateRepositoryBroker {
    public ForGettingTaxRates repositoryFor(String country) {
        // Selects appropriate repository at runtime
        if ("US".equals(country)) {
            return new USTaxRateRepository();
        } else if ("EU".equals(country)) {
            return new EUTaxRateRepository();
        }
        throw new IllegalArgumentException("Unsupported country");
    }
}
```

```java
class TaxCalculator {
    private final ForGettingTaxRates taxRateRepository;

    public TaxCalculator(ForGettingTaxRates taxRateRepository) {
        this.taxRateRepository = taxRateRepository;
    }

    public double taxOn(double amount) {
        return amount * taxRateRepository.taxRate(amount);
    }
}
```

```java
// Configurator (application entry-point)
public class Main {
    public static void main(String[] args) {
        TaxRateRepositoryBroker broker = new TaxRateRepositoryBroker();
        TaxCalculator calc = new TaxCalculator(broker.repositoryFor("US"));

        System.out.println(calc.taxOn(100));
    }
}
```

### Benefits of Dependency Lookup:

- **Dynamic Configuration:** Dependencies can be determined at runtime, allowing greater flexibility for cases with multiple implementations.
- **Decoupling:** The calling object doesn’t need to know the specific implementation or creation details.

### Potential downsides:

- Slightly increases complexity due to the broker/locator logic.
- Makes dependencies less explicit and potentially harder to track without good discipline or documentation.

### When to use:

- When multiple dependencies exist and the exact dependency can only be determined at runtime.
- Ideal for highly dynamic systems or applications with configurable plugins or extensions.

## 🧠 Advice on Choosing the Best Approach

Use **Dependency Injection** when:

- You have stable or well-known dependencies.
- You want explicitness and simplicity.
- You want maximum testability with minimal setup.

Use **Dependency Lookup** when:

- Dependencies are determined at runtime, or vary significantly (e.g., by user preferences, geography, dynamic conditions).
- You need flexibility for complex, plugin-driven, or highly dynamic systems.

## ⚠️ Important Advice: Keep Business Logic Out of Your Configurator

Regardless of which method you choose, always keep your configurator clean and purely dedicated to configuring dependencies. Your configurator should **never contain business logic**. If you notice logic creeping into your configurator, it’s a clear indication you need to refactor and rethink your design.

**Your configurator’s single responsibility:** wire and instantiate your objects clearly and simply.

## 🖥️ Configurator Visualization

```
Configurator (Dependency Injection)
├── TaxCalculator(new FileTaxRateRepository("rates.txt"))

Configurator (Dependency Lookup)
├── TaxRateRepositoryBroker
│   ├── repositoryFor("US")
│   └── repositoryFor("EU")
└── TaxCalculator(broker.repositoryFor("US"))
```

By clearly understanding and choosing the appropriate configurator approach, you'll ensure your Hexagonal Architecture implementation remains clean, maintainable, and flexible in the long run.

🧠 Use the approach that best fits your context. Just don’t let logic leak into the configurator.

## What Hexagonal Architecture is NOT

When discussing Hexagonal Architecture (Ports &amp; Adapters), it’s crucial to clarify not only what it is but also explicitly what it **is not**, to avoid common misconceptions that lead to incorrect or overly complex implementations.

### ❌ Not a folder structure

Hexagonal Architecture should never be confused with just a folder structure. Although Alistair Cockburn recommends certain physical folder structures to maintain visual order and reduce cognitive load, the essence of this architecture is not about how you physically organize your files.

As Greg Young famously said:

> “If you ask what the architecture is, and people show you a folder structure, you have a problem.”

Hexagonal Architecture is primarily a clear logical separation between your business logic and external technical details. Folders help you organize your project, but should never be considered synonymous with your architecture.

**Example**: This code structure is Hexagonal Architecture

```java
interface ForCalculatingTaxes {
    double taxOn(double amount);
}
```

```java
interface ForGettingTaxRates {
    double taxRate(double amount);
}
```

```java
class TaxCalculator implements ForCalculatingTaxes {
    private final ForGettingTaxRates taxRateRepository;

    public TaxCalculator(ForGettingTaxRates taxRateRepository) {
        this.taxRateRepository = taxRateRepository;
    }

    public double taxOn(double amount) {
        return amount * taxRateRepository.taxRate(amount);
    }
}
```

```java
class FixedTaxRateRepository implements ForGettingTaxRates {
    public double taxRate(double amount) {
        return 0.15;
    }
}
```

```java
class Main {
    public static void main(String[] args) {
        ForGettingTaxRates taxRateRepository = new FixedTaxRateRepository();
        ForCalculatingTaxes myCalculator = new TaxCalculator(taxRateRepository);

        System.out.println(myCalculator.taxOn(100));
    }
}
```

```
src
├── FixedTaxRateRepository.java
├── ForCalculatingTaxes.java
├── ForGettingTaxRates.java
├── Main.java
├── TaxCalculation.java
└── TaxCalculator.java
```

### ❌ Not a layered architecture

[![](https://substackcdn.com/image/fetch/$s_!PDwk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F950ff0a9-3875-406d-a20c-686b091919b0_1028x574.png)](https://substackcdn.com/image/fetch/$s_!PDwk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F950ff0a9-3875-406d-a20c-686b091919b0_1028x574.png)

Another common misunderstanding is equating Hexagonal Architecture with traditional layered architectures (presentation, business logic, data access). While both approaches involve separation of concerns, Hexagonal Architecture doesn’t impose strict hierarchical layering or rigid single-direction dependencies (top-down).

[![](https://substackcdn.com/image/fetch/$s_!t86H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92943b9d-5dc3-493f-90d5-500ef4272d45_996x612.png)](https://substackcdn.com/image/fetch/$s_!t86H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92943b9d-5dc3-493f-90d5-500ef4272d45_996x612.png)

Instead, Hexagonal Architecture defines clear ports around the core business logic, accessible through external adapters from any direction, creating flexibility compared to the traditional, more rigid layered model. Martin Fowler illustrates this by comparing software architecture to city planning, dynamic and adaptable rather than rigid and fixed.

### ❌ Not only for microservices

Hexagonal Architecture isn't reserved exclusively for microservices. It’s equally useful and applicable to monolithic projects, modular applications, or any architectural style.

Its strength lies in the flexibility it provides by completely isolating your business logic from external technical details, rather than in the size or architectural style of the system.

### ❌ Not Clean Architecture or Onion Architecture

Though Hexagonal Architecture shares key concepts, such as inversion of control (IoC), with Clean Architecture and Onion Architecture, they are not identical.

Clean Architecture and Onion Architecture propose internal concentric layers (domain, application, infrastructure) with strict rules about dependencies between layers. Hexagonal Architecture, by contrast, is simpler and more direct: it defines ports around the core business logic, interacting through external adapters.

Its conceptual simplicity is precisely one of the greatest strengths of Hexagonal Architecture compared to more complex architectural models.

### ✅ It’s about isolating business logic from technical details

The true and profound essence of Hexagonal Architecture lies in clearly isolating essential business logic from external technical details (databases, user interfaces, external APIs, frameworks).

This isolation enables changing technical implementations without affecting the core of your system, significantly improving automated testing capabilities and long-term software flexibility and stability.

### ✅ Applicable to any project size and complexity

A major advantage of Hexagonal Architecture is that it can be applied regardless of project size or complexity. Literally, it does not require extensive additional infrastructure to implement effectively.

For instance, even a simple tax calculator can easily implement this architecture.

This example clearly demonstrates how you can easily get started in any kind of project, large or small and immediately reap benefits in terms of testability, flexibility, and clear separation of concerns.

### ✅ Implications for Testability

Another intrinsic positive implication of this architecture is greatly enhanced testability. By clearly isolating business logic, it facilitates using test doubles such as mocks, stubs, and fakes, allowing effective and efficient testing of the system’s core logic without dependency on external systems.

## Implications for Testability

Testing becomes **simpler** and **cleaner**:

- Replace any adapter with a test doubles
- Run integration tests with production adapters
- Never modify your app logic

📈 Result: fast feedback, stable domain logic, and fewer bugs.

## 📌 My Final Reflection

I'm honestly a bit tired of seeing countless courses, LinkedIn posts, and conference talks claiming to teach or demonstrate **Hexagonal Architecture (Ports and Adapters)**, but instead discussing concepts closer to **Onion Architecture**, **Clean Architecture**, or other related architectures, even mixing them up with **Domain-Driven Design (DDD)**.

Let's imagine this scenario:
If I showed you an empty glass and asked, "What is this?" and you answered, "It's a passenger airplane," we'd clearly have a problem. A glass has an objective definition; it isn't something we can arbitrarily redefine. This highlights the issue known as **Semantic Diffusion**, as described by Martin Fowler ([Semantic Diffusion](https://martinfowler.com/bliki/SemanticDiffusion.html)):

*> Semantic diffusion occurs when a term, originally well-defined by a group or individual, becomes diluted as it's shared widely, eventually risking losing its meaning altogether.*

This metaphor applies perfectly to what's happening with Hexagonal Architecture. People take a clearly defined architecture and unintentionally reshape its meaning, creating confusion and misunderstandings within our community.

### 🚩 Two Key Points I Want to Clarify:

#### 1️⃣ Folder Structure ≠ Architecture

A folder structure certainly brings us practical benefits, like reducing cognitive load, keeping related files together, and encouraging changes to be isolated to minimal places, supporting the Separation of concerns (principle). However, these advantages reflect our personal convenience and maintainability concerns, not architectural significance.

Architecture is fundamentally about defining and protecting what's crucial for the business or application, it's about the **logical** separation of concerns, not merely **physical** file organization. A famous Uncle Bob talk highlighted that folders often indicate the frameworks we use, but not the essence of what our application actually does. He was absolutely right, yet many misinterpretation arises from this point.

#### 2️⃣ Hexagonal Architecture ≠ Clean Architecture ≠ Onion Architecture

[![](https://substackcdn.com/image/fetch/$s_!wF3s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f4a1a1b-c28e-4e46-8922-c700d15358ea_1045x859.png)](https://substackcdn.com/image/fetch/$s_!wF3s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f4a1a1b-c28e-4e46-8922-c700d15358ea_1045x859.png)

[![](https://substackcdn.com/image/fetch/$s_!VWwu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98db46ec-0fa1-4116-a735-8ed73c7b6404_1634x515.png)](https://substackcdn.com/image/fetch/$s_!VWwu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98db46ec-0fa1-4116-a735-8ed73c7b6404_1634x515.png)

While Hexagonal, Clean, and Onion Architectures share common principles like **Inversion of Control (IoC)** and clear boundaries, they aren't the same. Each architecture was born with different motivations, solving distinct problems.

Hexagonal Architecture stands out because of its **simplicity and practicality**. It's genuinely straightforward, doesn't demand complex setups, and can easily fit into virtually any project, even the simplest ones. All you need to implement Hexagonal Architecture effectively are clearly defined ports and adapters, illustrated beautifully by the tax calculator example provided earlier in this article.

### 🎯 Final Thoughts on Semantic Diffusion

Semantic diffusion isn't new; terms like "Agile," "Web 2.0," and even "DevOps" have undergone similar distortions, often becoming buzzwords or losing their original clarity. Fowler mentions:

*> Semantic diffusion is essentially a game of telephone, where successive groups unknowingly distort a term’s original meaning, eventually diluting its value.*

As software professionals, it's our responsibility to keep concepts precise and coherent, not dogmatically, but respectfully. Let's strive to clearly articulate terms, regularly referencing the original definitions and principles. When introducing or teaching architectures, being explicit and respectful about their original context and intention helps preserve clarity and usefulness.

In the end, Hexagonal Architecture is just one powerful tool among many. It's simple, flexible, practical, and universally applicable without being overly restrictive or complex. Let's ensure its true meaning remains intact and clearly understood, avoiding confusion, misuse, or unnecessary complication.

## References &amp; Bibliography

- Alistair Cockburn - *Hexagonal Architecture Book*
- GitHub Examples:
	- [SmallerWebHexagon](https://github.com/totheralistair/SmallerWebHexagon)
	- [BlueZone Project](https://github.com/HexArchBook/bluezone_pro)
- Martin Fowler
	- [What is Software Architecture](https://youtu.be/BVMngYKJ4hk)
	- [Agile Architecture Keynote](https://youtu.be/ev2qvR9UFPs)
- Ralph Johnson via *Fundamentals of Software Architecture*
