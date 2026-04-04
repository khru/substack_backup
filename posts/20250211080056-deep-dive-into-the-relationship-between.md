---
title: "Deep dive into the relationship between the verification of a test and the SUT"
requested_url: "https://emmanuelvalverderamos.substack.com/p/deep-dive-into-the-relationship-between"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/deep-dive-into-the-relationship-between"
substack_post_id: 152957003
retrieved_at: "2026-04-04T07:46:58.359Z"
---
# Deep dive into the relationship between the verification of a test and the SUT

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
- Test doubles such as mocks, stubs, or spies. (we will mention them but is not covered here)

Instead, we'll focus on the characteristics that define a great automated test.

## Introduction

In previous articles, we have discussed the concept of Subject Under Test ([SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test)) and introduced the basic concepts of test verifications. However, we haven't explored their relationship in detail. This article will delve deeper into the connections between these concepts.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## What does a test evaluate in the Subject Under Test?

When we think carefully about the Subject Under Test, we've talked about it as "the piece of software" we want to test. However, our tests aim to evaluate this piece by examining or exercising the expected behavior of this "code piece" or [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test), as well expressed in the test desiderata.

[![](https://substackcdn.com/image/fetch/$s_!GvKM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fafa01c-54bb-431a-8ea5-f864f8532acd_10984x1096.png)](https://substackcdn.com/image/fetch/$s_!GvKM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fafa01c-54bb-431a-8ea5-f864f8532acd_10984x1096.png)

## What types of behaviors might we encounter?

There are different types of behaviors. I will focus on these:

- Given a direct input, we always get the same direct output
- Given an indirect input, we get a direct output
- Given a direct input, we mutate the state and get an output
- Given a direct input, the behavior generates an exception
- Given a direct input, we connect to an external dependency and get an output

## Given a direct input, we always get the same direct output

[![](https://substackcdn.com/image/fetch/$s_!zuVS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8ef1826-7b6e-4d6b-ae9f-746fc7c27329_8936x3304.png)](https://substackcdn.com/image/fetch/$s_!zuVS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8ef1826-7b6e-4d6b-ae9f-746fc7c27329_8936x3304.png)

This is a good example of a test that will use an **Output-Based verification**

Test code

```java
public class TemperatureConverterShould {

  @Test
  void converts_the_temperature_given_in_celsius_to_fahrenheit() {
    // Arrange
    TemperatureConverter converter = new TemperatureConverter();
    double inCelsius = 25.0;

    // Act
    double inFahrenheit = converter.celsiusToFahrenheit(inCelsius);

    // Assert
    assertEquals(77.0, inFahrenheit, 0.001); // Allowing a small delta for floating-point precision
  }
}
```

Production code

```java
public class TemperatureConverter {

  public double celsiusToFahrenheit(double inCelsius) {
    return (inCelsius * 9 / 5) + 32;
  }
}
```

## Given an indirect input, we get a direct output

This would be a small variation of the previous example because sometimes tests do not only have direct inputs (from the arguments), but sometimes they could get the input from an inmutable state associated with the behavior, we could say that that inmutable state is an additional input to your behavior.

[![](https://substackcdn.com/image/fetch/$s_!xqnG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b5b2441-fdb4-4561-a9e7-ebe3f808fa02_8936x3464.png)](https://substackcdn.com/image/fetch/$s_!xqnG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b5b2441-fdb4-4561-a9e7-ebe3f808fa02_8936x3464.png)

It would be an example of a test that will use an **Output-Based verification**

Test code

```java
public class TemperatureShould {

  @Test
  void converts_the_temperature_given_in_celsius_to_fahrenheit() {
    // Arrange
    Temperature inCelsius = new Temperature(25.0, Unit.CELSIUS);

    // Act
    Temperature inFahrenheit = inCelsius.toFahrenheit();

    // Assert
    assertEquals(new Temperature(77.0, Unit.FAHRENHEIT), inFahrenheit);
  }
}
```

Production code

```java
public record Temperature(double degrees, Unit unit) {

  public Temperature toFahrenheit() {
    return switch (unit) {
      case CELSIUS -&gt; new Temperature((degrees * 9 / 5) + 32, Unit.FAHRENHEIT);
      case FAHRENHEIT -&gt; new Temperature(degrees, Unit.FAHRENHEIT);
    };
  }
}
```

```java
public enum Unit {
  CELSIUS, FAHRENHEIT
}
```

## Given a direct input, we mutate the state and get an output

As we also can read from a state to use the information as input we could also write (mutate) the state, meaning that we could not only get information from a state but also change the state with our behavior, and that would be a **state-based** verification.

[![](https://substackcdn.com/image/fetch/$s_!AydP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd402af5-e036-40f3-ad05-b3f2eef80535_8936x3464.png)](https://substackcdn.com/image/fetch/$s_!AydP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd402af5-e036-40f3-ad05-b3f2eef80535_8936x3464.png)

Test code

```java
public class TemperatureShould {

  @Test
  void converts_the_temperature_given_in_celsius_to_fahrenheit() {
    // Arrange
    Temperature temperature = new Temperature(25.0, Unit.CELSIUS);

    // Act
    temperature.convertToFahrenheit();

    // Assert
    assertEquals(Unit.FAHRENHEIT, temperature.unit());
    assertEquals(77.0, temperature.degrees());
  }
}
```

Production code

```java
public class Temperature {
  private double degrees;
  private Unit unit;

  public Temperature(double degrees, Unit unit) {
    this.degrees = degrees;
    this.unit = unit;
  }

  public double degrees() {
    return degrees;
  }

  public Unit unit() {
    return unit;
  }

  public void convertToFahrenheit() {
    if (unit == Unit.CELSIUS) {
      degrees = (degrees * 9 / 5) + 32;
      unit = Unit.FAHRENHEIT;
    }
  }
}
```

```java
public enum Unit {
  CELSIUS, FAHRENHEIT;
}
```

## Given a direct input, the behavior generates an exception

The exceptions could also be another type of output from our behavior, and to test we could use an **output-base verification.**

[![](https://substackcdn.com/image/fetch/$s_!Xj0h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2ebc611-f479-4d25-87e5-330b30506485_8936x3844.png)](https://substackcdn.com/image/fetch/$s_!Xj0h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2ebc611-f479-4d25-87e5-330b30506485_8936x3844.png)

An example of how we could test this would be:

Test code

```java
public class TemperatureShould {

  @Test
  void does_not_convert_the_temperature_given_in_fahrenheit_to_fahrenheit() {
    // Arrange
    Temperature inFahrenheit = new Temperature(25.0, Unit.FAHRENHEIT);

    // Act &amp; Assert
    assertThrows(RuntimeException.class, inFahrenheit::toFahrenheit);
  }
}
```

Production code

```java
public class Temperature {
  private final double degrees;
  private final Unit unit;

  public Temperature(double degrees, Unit unit) {
    this.degrees = degrees;
    this.unit = unit;
  }

  public double degrees() {
    return degrees;
  }

  public Unit unit() {
    return unit;
  }

  public Temperature toFahrenheit() {
    return switch (unit) {
      case CELSIUS -&gt; new Temperature((degrees * 9 / 5) + 32, Unit.FAHRENHEIT);
      case FAHRENHEIT -&gt; throw new RuntimeException("The temperature is already in Fahrenheit.");
    };
  }
}
```

```java
public enum Unit {
  CELSIUS, FAHRENHEIT;
}
```

## Given a direct input, we connect to an external dependency and get an output

We can also get inputs or outputs through I/O operations (database, file system, external API calls). When working with external systems like databases, we need to set up the initial state and establish the connection in our test.

[![](https://substackcdn.com/image/fetch/$s_!Pj6Y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08b28cea-123a-4211-8c8e-a78a693a18f0_8936x3844.png)](https://substackcdn.com/image/fetch/$s_!Pj6Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08b28cea-123a-4211-8c8e-a78a693a18f0_8936x3844.png)

I'll base this example on the official [Testcontainers documentation](https://testcontainers.com/guides/getting-started-with-testcontainers-for-java/). While keeping the example's complexity minimal, note that this code is meant to demonstrate the concept rather than serve as a best practice.

This test would be an example of **output-based verification**.

Test code

```java
public class TemperatureServiceShould {

  static PostgreSQLContainer&lt;?&gt; postgres = new PostgreSQLContainer&lt;&gt;("postgres:16-alpine");
  private TemperatureService service;

  @BeforeAll
  static void startContainer() {
    postgres.start();
  }

  @AfterAll
  static void stopContainer() {
    postgres.stop();
  }

  @BeforeEach
  void setUp() {
    DBConnectionProvider connectionProvider = new DBConnectionProvider(
      postgres.getJdbcUrl(),
      postgres.getUsername(),
      postgres.getPassword()
    );
    TemperatureRepository repository = new TemperatureRepository(connectionProvider);
    service = new TemperatureService(repository);
  }

  @Test
  void record_and_retrieve_temperature_in_celsius() {
    // Arrange
    Temperature tempCelsius = new Temperature(25.0, Unit.CELSIUS);

    // Act
    service.recordTemperature(tempCelsius);
    List&lt;Temperature&gt; temperatures = service.getAllTemperatures();

    // Assert
    assertEquals(tempCelsius, temperatures.get(0));
  }

  @Test
  void record_and_retrieve_temperature_in_fahrenheit() {
    // Arrange
    Temperature tempFahrenheit = new Temperature(77.0, Unit.FAHRENHEIT);

    // Act
    service.recordTemperature(tempFahrenheit);
    List&lt;Temperature&gt; temperatures = service.getAllTemperatures();

    // Assert
    assertEquals(tempFahrenheit, temperatures.get(0));
  }
}
```

The production code

```java
public class TemperatureRepository {
    private final DBConnectionProvider connectionProvider;

    public TemperatureRepository(DBConnectionProvider connectionProvider) {
        this.connectionProvider = connectionProvider;
        createTemperatureTableIfNotExists();
    }

    public void save(Temperature temperature) {
        try (Connection conn = connectionProvider.getConnection()) {
            PreparedStatement pstmt = conn.prepareStatement(
                "INSERT INTO temperatures(value, unit) VALUES (?, ?)"
            );
            pstmt.setDouble(1, temperature.degrees());
            pstmt.setString(2, temperature.unit().name());
            pstmt.execute();
        } catch (SQLException e) {
            throw new RuntimeException("Failed to save temperature", e);
        }
    }

    public List&lt;Temperature&gt; findAll() {
        List&lt;Temperature&gt; temperatures = new ArrayList&lt;&gt;();
        try (Connection conn = connectionProvider.getConnection()) {
            PreparedStatement pstmt = conn.prepareStatement("SELECT value, unit FROM temperatures");
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                double value = rs.getDouble("value");
                Unit unit = Unit.valueOf(rs.getString("unit"));
                temperatures.add(new Temperature(value, unit));
            }
        } catch (SQLException e) {
            throw new RuntimeException("Failed to fetch temperatures", e);
        }
        return temperatures;
    }

    private void createTemperatureTableIfNotExists() {
        try (Connection conn = connectionProvider.getConnection()) {
            PreparedStatement pstmt = conn.prepareStatement(
                """
                CREATE TABLE IF NOT EXISTS temperatures (
                    value DOUBLE NOT NULL,
                    unit VARCHAR NOT NULL
                )
                """
            );
            pstmt.execute();
        } catch (SQLException e) {
            throw new RuntimeException("Failed to create table", e);
        }
    }
}
```

```java
public class TemperatureService {
  private final TemperatureRepository repository;

  public TemperatureService(TemperatureRepository repository) {
    this.repository = repository;
  }

  public void recordTemperature(Temperature temperature) {
    repository.save(temperature);
  }

  public List&lt;Temperature&gt; getAllTemperatures() {
    return repository.findAll();
  }
}
```

```java
public record Temperature(double degrees, Unit unit) {}
```

```java
public enum Unit {
  CELSIUS, FAHRENHEIT
}
```

Looking at just the test code, we can see it's more complex than our previous examples. We now need to consider additional factors like having Docker installed and adding latency to our test.

The benefit of this test is that covers more and integrates with an external system, giving you more security. But could we test this [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test) without this dependency?

[![](https://substackcdn.com/image/fetch/$s_!nA1-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e42463e-f8a4-45dd-910c-4e51df0b33b0_8936x3844.png)](https://substackcdn.com/image/fetch/$s_!nA1-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e42463e-f8a4-45dd-910c-4e51df0b33b0_8936x3844.png)

To do that we need to understand the concept of test doubles, which one to use, when, and what behavior we expect it to replace.

[![](https://substackcdn.com/image/fetch/$s_!QR_S!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27a2925b-2edc-4b7a-bc88-87e8601f2f2a_18342x6429.png)](https://substackcdn.com/image/fetch/$s_!QR_S!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27a2925b-2edc-4b7a-bc88-87e8601f2f2a_18342x6429.png)

Test code

```java
public class TemperatureServiceShould {

    private TemperatureRepository stubRepository;
    private TemperatureService service;

    @BeforeEach
    void setUp() {
        // Stub the repository
        stubRepository = mock(TemperatureRepository.class);
        service = new TemperatureService(stubRepository);
    }

    @Test
    void record_and_retrieve_temperature_in_celsius() {
        // Arrange
        Temperature tempCelsius = new Temperature(25.0, Unit.CELSIUS);

        // Stub the behavior of the repository
        doNothing().when(stubRepository).save(tempCelsius);
        when(stubRepository.findAll()).thenReturn(List.of(tempCelsius));

        // Act
        service.recordTemperature(tempCelsius);
        List&lt;Temperature&gt; temperatures = service.getAllTemperatures();

        // Assert
        assertEquals(tempCelsius, temperatures.get(0));
    }

    @Test
    void record_and_retrieve_temperature_in_fahrenheit() {
        // Arrange
        Temperature tempFahrenheit = new Temperature(77.0, Unit.FAHRENHEIT);

        // Stub the behavior of the repository
        doNothing().when(stubRepository).save(tempFahrenheit);
        when(stubRepository.findAll()).thenReturn(List.of(tempFahrenheit));

        // Act
        service.recordTemperature(tempFahrenheit);
        List&lt;Temperature&gt; temperatures = service.getAllTemperatures();

        // Assert
        assertEquals(tempFahrenheit, temperatures.get(0));
    }
}
```

---

**Disclaimer**: *This is only an example, this test is not a good test, because is not testing any behavior because the test would be testing as the SUT the TeperatureService, but the Service does not have any behavior.*

---

While this approach doesn't test the database connection and related components, we can separate our testing strategy. We can test the service and repository as independent subjects under test, which gives us flexibility in how we implement our testing approach.

## The behavior you test is often related to a different behavior

As shown in the latest example, when building something larger than a simple function or class, we often need multiple classes to work together. Regardless of how these classes relate to each other, you'll need to understand their relationships and plan how to test them effectively. These decisions form your testing boundaries, which tie into your broader testing strategy and plan. The key is identifying which verification methods to use and when to use them. You'll also need to consider how connected behaviors should be tested, including how and why these connections exist in the first place.

[![](https://substackcdn.com/image/fetch/$s_!Ag5Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b2997ba-6719-497b-a7ad-609657c79ccb_26216x9352.png)](https://substackcdn.com/image/fetch/$s_!Ag5Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b2997ba-6719-497b-a7ad-609657c79ccb_26216x9352.png)

## Conclusions

- **Testing behavior as the core objective:** The fundamental purpose of testing is to validate how the subject under test behaves. This focus, highlighted in the **Test Desiderata**, ensures that tests stay meaningful, align with expected outcomes, and adapt well to implementation changes. By focusing on behavior, tests become more robust and reliable.
- **Understanding behavior and verification types** A test validates the behavior of the Subject Under Test ([SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test)). Understanding different verification types—**output-based**, **state-based**, and **exception-based**—helps align tests with expected outcomes. Each behavior needs a specific approach, and mastering these distinctions creates better, more maintainable tests.
- **The Role of Test Doubles in Isolating dependencies test doubles **help isolate the [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test) from external or awkward dependencies. Whether using **stubs**, **spies**, or **mocks**, choosing the right test double for each behavior is crucial. This improves reliability and clarifies the behavior's testing boundaries, not only that The test doubles have the resposibility of replacing a behavior from the production code.
- **Relationships between behaviors** System behaviors rarely exist in isolation. Complex systems feature interconnected behaviors that influence each other. Understanding these relationships is essential for effective testing across boundaries.
- **Establishing testing boundaries** Testing boundaries define a test's scope. By isolating the [SUT](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test) and focusing on direct behaviors while considering component interactions, you create scalable, maintainable tests. These boundaries guide the use of test doubles and shape your testing strategy. **It is also important to remark that NOT all dependencies should be isolated, only awkward dependencies**.
- **Building a comprehensive testing strategy** Understanding behaviors, verifications, and test doubles forms the foundation of a solid testing strategy. These concepts help us approach higher-level testing concepts like **test strategy** and **test plans**, enabling systematic testing of interconnected systems.
- **Understanding behavior interactions:** Testing involves both verifying individual behaviors and examining their interactions. This dual focus highlights the importance of clear testing scope, purpose, and appropriate testing tools.
- **Testing in real-world systems:** Real applications require testing both individual behaviors and their relationships. This needs a strategic approach that balances detailed unit tests with broader and/or narrow integration tests. These decisions should reflect what brings the most value to the team and product.

## References

- Khorikov, Vladimir. *Unit Testing Principles, Practices, and Patterns*.
- Zalas, Jakub. *Your tests are mocking you*. [YouTube](https://youtu.be/kdvN6owjXLw?si=0-G7tt7apUB5UIDP)
