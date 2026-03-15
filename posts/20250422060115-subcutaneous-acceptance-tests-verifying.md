---
title: "Subcutaneous Acceptance Tests: Verifying Behavior Just Below the Surface"
requested_url: "https://emmanuelvalverderamos.substack.com/p/subcutaneous-acceptance-tests-verifying"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/subcutaneous-acceptance-tests-verifying"
substack_post_id: 161290283
retrieved_at: "2026-03-15T08:31:37.606Z"
---
# Subcutaneous Acceptance Tests: Verifying Behavior Just Below the Surface

### What Happens After 200 OK?

> “Your API returns 201 Created when registering a user… but did the user receive the welcome email?”

A correct HTTP response doesn’t always mean the system behaved correctly. In many cases, the user-facing **value** comes from side effects — not just response bodies.

Let’s say you run a REST API. When someone registers, the backend must send a personalized welcome email. You can’t observe that behavior through the HTTP response. A black-box test wouldn't catch that failure. Yet verifying it is essential.

That’s where **subcutaneous acceptance tests** shine.

They let us validate user-facing **behaviors** from just under the surface of the system — not too deep (like a unit test), not too external (like an end-to-end test), but **right at the boundary of behavior**.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### What Is a Subcutaneous Acceptance Test?

A subcutaneous acceptance test:

- Verifies a **user-level behavior** or acceptance criterion.
- **Bypasses the transport layer** (e.g., HTTP), but not the business logic.
- **Injects controlled dependencies** (e.g., a mock email sender).
- Focuses on **side effects**, not just output responses.
- Avoids relying on infrastructure like databases, SMTP servers, or external systems.

> “It’s still an acceptance test — it just dives slightly under the skin to get clearer feedback.”

### Use Case: Send a Welcome Email After User Registration

#### ✅ Functional Requirement:

> “When a user registers, the system must send a personalized welcome email.”

We don’t want to spin up the full application stack. We just want to verify that **after registration**, the email is sent with the expected content.

### The Final Implementation

This example uses:

- A User domain object
- A RegisterUserUseCase
- An EmailSender interface
- A subcutaneous test that verifies behavior using **Mockito**

#### Domain Model

```java
public class User {
    private final String email;
    private final String username;

    public User(String email, String username) {
        this.email = email;
        this.username = username;
    }

    public String email() { return email; }
    public String username() { return username; }
}
```

#### Email DTO

```java
public record EmailMessage(String to, String subject, String body) {}
```

#### EmailSender Interface

```java
public interface EmailSender {
    void send(EmailMessage message);
}
```

#### UserRepository Interface

```java
public interface UserRepository {
    void save(User user);
}
```

#### RegisterUserController

```java
public class RegisterUserController {

    private final EmailSender emailSender;

    public RegisterUserController(EmailSender emailSender) {
        this.emailSender = emailSender;
    }

    public int registerUser(String email, String username) {
        UserRepository userRepository = user -&gt; {}; // No-op for simplicity
        RegisterUserUseCase useCase = new RegisterUserUseCase(userRepository, emailSender);
        useCase.register(new User(email, username));
        return 200;
    }
}
```

### Subcutaneous Acceptance Test

Here’s how we verify that the **business behavior** actually happened:

```java
import org.junit.jupiter.api.Test;
import org.mockito.ArgumentCaptor;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

public class RegisterUserSubcutaneousTest {

    @Test
    void should_send_personalized_welcome_email_after_user_registration() {
        EmailSender emailSender = mock(EmailSender.class);
        RegisterUserController controller = new RegisterUserController(emailSender);

        int response = controller.registerUser("emma@example.com", "emma");

        assertEquals(200, response);

        ArgumentCaptor&lt;EmailMessage&gt; captor = ArgumentCaptor.forClass(EmailMessage.class);
        verify(emailSender).send(captor.capture());

        EmailMessage message = captor.getValue();
        assertAll(
            () -&gt; assertEquals("emma@example.com", message.to()),
            () -&gt; assertEquals("Welcome emma!", message.subject()),
            () -&gt; assertEquals("Thanks for signing up, emma.", message.body())
        );
    }
}
```

✅ The test validates **one acceptance criterion**: the email was sent, with the right data.

### Why Not a Black Box Test?

With a black-box API test, you'd miss what really matters, the **email behavior**.

- HTTP response codes don’t reflect all business logic
- Subcutaneous tests avoid awkward side effects, like calling a 3º party system that you do not control.
- They’re faster and more precise at validating **side effects**

### When to Use Subcutaneous Tests

Use them when:

- Behavior cannot be verified via the public interface
- You want fast feedback and clear behavioral assertions
- You want to verify **what the system does**, not just what it returns

Avoid when:

- You must test UI or end-to-end performance
- Side effects **are the interface** (e.g., webhook endpoints)

### Benefits Recap

✅ Clean feedback on user-level behavior
✅ Avoids unnecessary infrastructure setup
✅ Easy to write and execute
✅ Great fit for hexagonal and Clean Architecture
✅ Ideal for **communication-based** testing

### Visual Overview

[![](https://substackcdn.com/image/fetch/$s_!SSKc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d12377c-9fe9-453d-b50f-760c68c2ab24_3840x1229.png)](https://substackcdn.com/image/fetch/$s_!SSKc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d12377c-9fe9-453d-b50f-760c68c2ab24_3840x1229.png)

We stay close to real behavior, but control dependencies for **precise verification**.

### Conclusion: Clarity, Behavior, Confidence

> “A subcutaneous acceptance test checks if your system kept its promise — not just if it returned the right code.”

Don’t settle for superficial test coverage. If your software makes promises (like “users will get a welcome email”), you should test that promise — clearly, directly, and effectively.

Subcutaneous acceptance tests help you do just that.
No overkill. No overreach. Just **behavioral confidence**, done right.

## References

- Fowler, Martin. *SubcutaneousTest*. [https://martinfowler.com/bliki/SubcutaneousTest.html](https://martinfowler.com/bliki/SubcutaneousTest.html)
- Farley, Dave. *[How to Write Acceptance Tests](https://youtu.be/JDD5EEJgpHU)*.

- Adzic, Gojko. *Specification by Example*.
- Beck, Kent. *Test-Driven Development: By Example*.
- Freeman, Steve. Pryce, Nat. *Growing Object-Oriented Software, Guided by Tests*.
- Meszaros, Gerard. *xUnit Test Patterns*.
- Crispin, Lisa. Gregory, Janet. *Agile Testing*.
- North, Dan. *Introducing BDD*. [https://dannorth.net/introducing-bdd/](https://dannorth.net/introducing-bdd/)
- Smart, John Ferguson. *BDD in Action*.
