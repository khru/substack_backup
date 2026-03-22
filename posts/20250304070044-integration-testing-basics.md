---
title: "Integration Testing: Basics"
subtitle: "The basics"
requested_url: "https://emmanuelvalverderamos.substack.com/p/integration-testing-basics"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/integration-testing-basics"
substack_post_id: 153259735
retrieved_at: "2026-03-22T08:29:25.592Z"
---
# Integration Testing: Basics

### The basics

## **Introduction to Integration Test**

Integration testing plays a pivotal role in verifying the interaction between different components of a software system. Unlike unit tests, which validate isolated units of logic, integration tests confirm that various parts of a system can work together correctly. These tests help catch issues that arise when components interact, such as misconfigurations, interface mismatches, or database integration errors.

There are three primary types of integration tests:

- **Narrow Integration Tests** – Validate specific integrations within a component using test doubles like stubs, mocks, or any other test double.
- **Broad Integration Tests** – Verify interactions between multiple components, often relying on real infrastructure such as databases.
- **Contract Tests** – Ensure communication between systems adheres to predefined contracts, verifying expectations between clients and providers.

Each type serves a specific purpose and complements the overall testing strategy.

> Integration tests are designed to verify how components or systems work together, but achieving a balance in scope and speed is critical.

> - Martin Fowler

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

**
Production code**

```java
public class Temperature {
    private final double value;
    private final Unit unit;

    public Temperature(double value, Unit unit) {
        this.value = value;
        this.unit = unit;
    }

    public double getValue() {
        return value;
    }

    public Unit getUnit() {
        return unit;
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Temperature other)) return false;
        return Double.compare(value, other.value) == 0 &amp;&amp; unit == other.unit;
    }

    @Override
    public int hashCode() {
        return Objects.hash(value, unit);
    }
}
```

```java
public enum Unit {
    CELSIUS, FAHRENHEIT
}
```

```java
public interface TemperatureRepository {
    void save(Temperature temperature);
    List&lt;Temperature&gt; findAll();
}
```

```java
public class PostgresTemperatureRepository implements TemperatureRepository {

    private final Connection connection;

    public PostgresTemperatureRepository(Connection connection) {
        this.connection = connection;
    }

    @Override
    public void save(Temperature temperature) {
        try (PreparedStatement stmt = connection.prepareStatement(
                "INSERT INTO temperatures (value, unit) VALUES (?, ?)")) {
            stmt.setDouble(1, temperature.getValue());
            stmt.setString(2, temperature.getUnit().name());
            stmt.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public List&lt;Temperature&gt; findAll() {
        List&lt;Temperature&gt; result = new ArrayList&lt;&gt;();
        try (PreparedStatement stmt = connection.prepareStatement("SELECT value, unit FROM temperatures");
             ResultSet rs = stmt.executeQuery()) {
            while (rs.next()) {
                double value = rs.getDouble("value");
                Unit unit = Unit.valueOf(rs.getString("unit"));
                result.add(new Temperature(value, unit));
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return result;
    }
}
```

## **
Narrow Integration Tests**

[![](https://substackcdn.com/image/fetch/$s_!Ix2C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d0a23ce-a959-41bb-96c3-ee945df9e765_17732x6504.png)](https://substackcdn.com/image/fetch/$s_!Ix2C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d0a23ce-a959-41bb-96c3-ee945df9e765_17732x6504.png)

### **Definition**

Narrow integration tests verify the interaction between a component and its immediate dependencies while isolating external systems. These tests utilize **test doubles** such as stubs, mocks, or any other test double to simulate behavior, focusing on specific integrations within a constrained scope.

### **Example in Java Using Mockito**

We have a `TemperatureService` class that interacts with a `TemperatureRepository` to save and retrieve temperature data. In this narrow test, we isolate the repository by stubbing its behavior.

**Production code**

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

Test code:

Unit test, testing the contract and that the communication works as it should

```java
public class TemperatureServiceShould {

    private TemperatureRepository stubRepository;
    private TemperatureService service;

    @BeforeEach
    void setUp() {
        stubRepository = mock(TemperatureRepository.class); // Stub repository
        service = new TemperatureService(stubRepository);
    }

    @Test
    void record_and_retrieve_temperature_in_celsius() {
        // Arrange
        Temperature tempCelsius = new Temperature(25.0, Unit.CELSIUS);
        doNothing().when(stubRepository).save(tempCelsius);
        when(stubRepository.findAll()).thenReturn(List.of(tempCelsius));

        // Act
        service.recordTemperature(tempCelsius);
        List&lt;Temperature&gt; temperatures = service.getAllTemperatures();

        // Assert
        assertEquals(tempCelsius, temperatures.get(0));
    }
}
```

*This test is only an example, and will not bee testing any usefull behavior.*

Narrow integration test: covering the actions for the repository

```java
public class PostgresTemperatureRepositoryNarrowTest {

    private static final PostgreSQLContainer&lt;?&gt; postgres =
            new PostgreSQLContainer&lt;&gt;("postgres:15")
                    .withDatabaseName("testdb")
                    .withUsername("user")
                    .withPassword("pass");

    private Connection connection;
    private PostgresTemperatureRepository repository;

    @BeforeAll
    static void startContainer() {
        postgres.start();
    }

    @AfterAll
    static void stopContainer() {
        postgres.stop();
    }

    @BeforeEach
    void setUp() throws Exception {
        connection = DriverManager.getConnection(
                postgres.getJdbcUrl(),
                postgres.getUsername(),
                postgres.getPassword());

        try (Statement stmt = connection.createStatement()) {
            stmt.execute("CREATE TABLE IF NOT EXISTS temperatures (" +
                    "id SERIAL PRIMARY KEY," +
                    "value DOUBLE PRECISION NOT NULL," +
                    "unit VARCHAR(20) NOT NULL)");
            stmt.execute("DELETE FROM temperatures");
        }

        repository = new PostgresTemperatureRepository(connection);
    }

    @AfterEach
    void tearDown() throws Exception {
        connection.close();
    }

    @Test
    void return_empty_list_when_no_data_exists() {
        List&lt;Temperature&gt; temperatures = repository.findAll();
        assertTrue(temperatures.isEmpty());
    }

    @Test
    void save_temperature_persists_it_in_database() {
        Temperature temp = new Temperature(21.0, Unit.CELSIUS);

        repository.save(temp);

        List&lt;Temperature&gt; all = repository.findAll();
        assertEquals(1, all.size());
        assertEquals(temp, all.get(0));
    }

    @Test
    void find_all_returns_all_saved_temperatures() {
        Temperature t1 = new Temperature(20.0, Unit.CELSIUS);
        Temperature t2 = new Temperature(68.0, Unit.FAHRENHEIT);

        repository.save(t1);
        repository.save(t2);

        List&lt;Temperature&gt; all = repository.findAll();
        assertEquals(2, all.size());
        assertTrue(all.contains(t1));
        assertTrue(all.contains(t2));
    }
}
```

### **Trade-offs**

- **Advantages**: Fast, deterministic, and simple to execute.
- **Disadvantages**:
	- Test doubles might not match real behavior, leading to false positives.
	- "Narrow scope means real-world failures may still surface during broader integration testing" (*IntegrationTest*, [source](https://martinfowler.com/bliki/IntegrationTest.html)).

## **Broad Integration Tests**

### **Definition**

Broad integration tests validate the behavior of multiple components interacting with real infrastructure, such as databases or APIs. These tests aim to ensure that end-to-end flows within the system work as expected.

### **Example in Java using Testcontainers and PostgreSQL**

We use **Testcontainers** to spin up a real PostgreSQL database for testing the `TemperatureService` and `TemperatureRepository`.

Production code

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
}
```

Test code

```java
public class TemperatureServiceShould {

    static PostgreSQLContainer&lt;?&gt; postgres =
        new PostgreSQLContainer&lt;&gt;("postgres:16-alpine");
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
}
```

### **Trade-offs**

- **Advantages**: Real-world integration ensures higher confidence in system behavior.
- **Disadvantages**:
	- Slower execution.
	- Requires significant setup and teardown.
	- "Broad integration tests can expose faults, but pinpointing root causes may require deeper debugging" (*IntegrationTest*, [source](https://martinfowler.com/bliki/IntegrationTest.html)).

## **Contract Tests**

### **Definition**

Contract tests validate the communication between a client and a provider by ensuring that the agreed-upon contract is respected. This is particularly useful in microservices and API-driven systems.

### **Example in Java using WireMock**

Production code

```java
public class ExternalTemperatureClient {

    private final HttpClient httpClient;
    private final ObjectMapper objectMapper;
    private final String baseUrl;

    public ExternalTemperatureClient(String baseUrl) {
        this.baseUrl = baseUrl;
        this.httpClient = HttpClient.newHttpClient();
        this.objectMapper = new ObjectMapper();
    }

    public Temperature fetchTemperature() {
        try {
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(baseUrl + "/api/temperature"))
                    .GET()
                    .build();

            HttpResponse&lt;String&gt; response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

            if (response.statusCode() != 200) {
                throw new RuntimeException("Failed to fetch temperature. Status: " + response.statusCode());
            }

            return objectMapper.readValue(response.body(), Temperature.class);

        } catch (IOException | InterruptedException e) {
            Thread.currentThread().interrupt(); // Restore interrupted state
            throw new RuntimeException("Error while communicating with external service", e);
        }
    }
}
```

Test code

```java
public class ExternalTemperatureClientTest {

    static WireMockServer wireMockServer;
    private ExternalTemperatureClient client;

    @BeforeAll
    static void startWireMock() {
        wireMockServer = new WireMockServer();
        wireMockServer.start();
    }

    @AfterAll
    static void stopWireMock() {
        wireMockServer.stop();
    }

    @BeforeEach
    void setup() {
        int port = wireMockServer.port();
        client = new ExternalTemperatureClient("&lt;http://localhost&gt;:" + port);
    }

    @Test
    void should_fetch_temperature_in_celsius_successfully() {
        // Arrange: Stub the external service response
        stubFor(get(urlEqualTo("/api/temperature"))
            .willReturn(aResponse()
                .withHeader("Content-Type", "application/json")
                .withBody("{\\"degrees\\":25.0,\\"unit\\":\\"CELSIUS\\"}")
                .withStatus(200)
            ));

        // Act: Call the client to fetch the temperature
        Temperature temperature = client.fetchTemperature();

        // Assert: Verify that the response matches the contract
        assertEquals(25.0, temperature.degrees());
        assertEquals(Unit.CELSIUS, temperature.unit());
	}

	@Test
    void should_throw_exception_when_response_status_is_not_200() {
        // Arrange
        stubFor(get(urlEqualTo("/api/temperature"))
                .willReturn(aResponse().withStatus(500)));

        // Act &amp; Assert
        RuntimeException exception = assertThrows(RuntimeException.class, () -&gt; client.fetchTemperature());
        assertTrue(exception.getMessage().contains("Failed to fetch temperature"));
    }
}
```

If you are working as the provider and the other service is the consumer or if you want to ensure the contract between provider and consumer, you may want to use [PACT](https://docs.pact.io/), which is a tool that could help with this.

### **Trade-offs**

- **Advantages**: Prevents integration issues due to incompatible expectations.
- **Disadvantages**: Adds overhead when maintaining contracts.

> "Contract tests reduce uncertainty in distributed systems by validating explicit agreements"
> - Martin Fowler

## **Conclusion**

[![](https://substackcdn.com/image/fetch/$s_!4KaN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82d04bca-c2bb-4e78-ad3d-f5224d671703_12008x6216.png)](https://substackcdn.com/image/fetch/$s_!4KaN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82d04bca-c2bb-4e78-ad3d-f5224d671703_12008x6216.png)

Integration testing is essential to ensure that systems and components collaborate effectively.

- **Narrow integration tests**: Verify small, internal integrations using test doubles.
- **Broad integration tests**: Validate real-world interactions with infrastructure.
- **Contract tests**: Ensure that communication adheres to agreed contracts.

[![](https://substackcdn.com/image/fetch/$s_!O-N3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73ea728d-c0af-41d2-b9f6-c3dfdca58a33_690x136.png)](https://substackcdn.com/image/fetch/$s_!O-N3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73ea728d-c0af-41d2-b9f6-c3dfdca58a33_690x136.png)

Balancing all three approaches ensures software systems' confidence, reliability, and maintainability.

### **References**

- Fowler, Martin. *IntegrationTest*. [https://martinfowler.com/bliki/IntegrationTest.html](https://martinfowler.com/bliki/IntegrationTest.html)
- Fowler, Martin. *ContractTest*. [https://martinfowler.com/bliki/ContractTest.html](https://martinfowler.com/bliki/ContractTest.html)
- Fowler, Martin. *TestDouble*. [https://martinfowler.com/bliki/TestDouble.html](https://martinfowler.com/bliki/TestDouble.html)
- Google Testing Blog. *Just Say No to More End-to-End Tests*. [https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)
- [Optivem Journal.](https://journal.optivem.com/p/external-system-contract-tests)*[External System Contract Tests](https://journal.optivem.com/p/external-system-contract-tests)*[.](https://journal.optivem.com/p/external-system-contract-tests)
- WireMock Documentation. *Mocking External APIs*. [https://wiremock.org](https://wiremock.org)
- Testcontainers Documentation. *Testing with Containers*. [https://www.testcontainers.org](https://www.testcontainers.org)
- PACT [https://docs.pact.io/](https://docs.pact.io/)
