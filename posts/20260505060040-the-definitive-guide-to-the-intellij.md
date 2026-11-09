Title: The definitive guide to the IntelliJ IDEA HTTP Client

URL Source: http://emmanuelvalverderamos.substack.com/p/the-definitive-guide-to-the-intellij

Final URL: https://emmanuelvalverderamos.substack.com/p/the-definitive-guide-to-the-intellij

Published Time: 2026-05-05T06:00:40+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!az5h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5e4961a-22cc-45c7-a2b7-2d6f196d0e87_1500x604.png)](https://substackcdn.com/image/fetch/$s_!az5h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5e4961a-22cc-45c7-a2b7-2d6f196d0e87_1500x604.png)

The IntelliJ IDEA HTTP Client lets you create, read, run, and test HTTP requests directly inside the IDE. Instead of treating API calls as throwaway experiments, it lets you keep them as part of your project in plain text files that can be reviewed, versioned, reused, and executed by the whole team.

That changes the role of request files. A good `.http` or `.rest` file is not just a quick manual check. It can become:

*   executable documentation

*   a developer onboarding tool

*   a smoke test suite

*   a collection of operational checks

*   a debugging aid

*   a lightweight integration test layer

*   a bridge between local development and CI

This guide is written as a full learning path. It starts with the basic request syntax, then builds toward variables, secrets, authentication, tests, scripts, event driven systems, health checks, and terminal execution with `ijhttp`.

The goal is simple: after reading this guide, you should be able to design and maintain a clean, reliable, team friendly HTTP Client setup for a real project.

Before diving into syntax, it helps to understand how the IntelliJ HTTP Client is best used.

Think of it as a text based request runner with four layers:

1.   **Request files**  
These are your `.http` or `.rest` files. They contain one or more requests.

2.   **Environment files**  
These are JSON files that provide reusable values such as hosts, ports, usernames, and tokens.

3.   **Scripts and tests**  
These are JavaScript snippets attached to requests, either inline or in external files. They let you prepare data, capture values from responses, and assert expectations.

4.   **Execution surfaces**  
You can run requests from the IDE, from run configurations, from imported request files, or from the `ijhttp` CLI.

If you structure those four layers well, your request files stop being random snippets and start acting like a coherent test and documentation system.

A clean IntelliJ HTTP Client setup usually revolves around these file types:

*   `.http` or `.rest` for requests

*   `http-client.env.json` for shared non secret environment values

*   `http-client.private.env.json` for secrets and machine specific sensitive values

*   `.js` files for reusable test and helper code

*   optional payload files such as `.json`, `.xml`, or `.graphql`

*   optional shell or PowerShell scripts for running `ijhttp`

*   optional container files such as `compose.yaml` or `Dockerfile` if you want to run `ijhttp` without installing it locally

A recommended project layout is:

```
http/
  onboarding.http
  users.http
  auth.http
  health.http
  events.http
  graphql.http
  websocket.http
  grpc.http
  data/
    create-user.json
    update-user.json
  scripts/
    common-tests.js
    auth.js
    signature.js
  http-client.env.json
  http-client.private.env.json
  .gitignore
  compose.yaml
  run-http.sh
  run-http.ps1
```

This layout keeps the request suite readable and discoverable. New team members can start in `onboarding.http` and then move into more specialized files.

You can create either a scratch HTTP request file or a physical file in your project.

A scratch file is useful for quick experiments. A physical file is better for documentation, shared examples, team workflows, and version control.

For most real projects, prefer physical files.

A minimal file might look like this:

`GET https://httpbin.org/get`
Run it from the gutter icon next to the request.

That is the smallest useful unit: one request, one file, one execution.

The request format is intentionally simple:

```
Method Request-URI HTTP-Version
Header-Name: Header-Value

Request body
```

A more complete example:

```
GET https://api.example.com/users/42 HTTP/1.1
Accept: application/json
X-Correlation-Id: 123e4567-e89b-12d3-a456-426614174000
```

The important rules are:

*   the method comes first

*   the URL comes next

*   the HTTP version is optional

*   headers go below the request line

*   the body starts after one blank line

*   multiple requests in one file are separated with `###`

*   comments start with `#` or `//`

Example with two requests:

```
# Fetch all users
GET https://api.example.com/users
Accept: application/json

###
# Fetch one user
GET https://api.example.com/users/42
Accept: application/json
```

As files grow, names matter. IntelliJ lets you name requests so they are easier to find in search, run configurations, and the Services tool window.

Use names aggressively in shared files.

```
### @name getAllUsers
GET https://api.example.com/users
Accept: application/json

### @name getUserById
GET https://api.example.com/users/42
Accept: application/json
```

In practice, request names become the table of contents for a large `.http` file.

The HTTP Client can send the usual HTTP methods. For onboarding, it is useful to show each of them with a realistic example.

Use `GET` to retrieve data.

```
### @name getUsers
GET https://api.example.com/users?page=1&pageSize=20
Accept: application/json
```

Use `POST` to create resources or trigger actions.

```
### @name createUser
POST https://api.example.com/users
Content-Type: application/json
Accept: application/json

{
  "email": "alice@example.com",
  "displayName": "Alice"
}
```

Use `PUT` when replacing the full representation of a resource.

```
### @name replaceUser
PUT https://api.example.com/users/42
Content-Type: application/json
Accept: application/json

{
  "id": 42,
  "email": "alice@example.com",
  "displayName": "Alice Doe",
  "status": "active"
}
```

Use `PATCH` for partial updates.

```
### @name patchUserStatus
PATCH https://api.example.com/users/42
Content-Type: application/json
Accept: application/json

{
  "status": "disabled"
}
```

Use `DELETE` to remove a resource.

```
### @name deleteUser
DELETE https://api.example.com/users/42
Accept: application/json
```

Use `HEAD` when you need headers without the response body.

```
### @name headUsers
HEAD https://api.example.com/users
Accept: application/json
```

Use `OPTIONS` to discover supported methods or CORS related metadata.

```
### @name optionsUsers
OPTIONS https://api.example.com/users
Accept: */*
```

Use `TRACE` only if your server and security posture allow it.

```
### @name traceGateway
TRACE https://gateway.example.com/ping
Accept: */*
```

`CONNECT` is much less common in application level testing, but the syntax is still just a request line and optional headers.

```
### @name connectProxy
CONNECT proxy.example.com:443 HTTP/1.1
Host: proxy.example.com:443
```

If your platform uses custom verbs, IntelliJ can recognize them after you add them to the IDE settings.

A practical rule is this: use standard methods unless your platform has a strong reason not to.

A lot of broken request files are not broken because of syntax. They are broken because the author did not make the request intent explicit.

Good request files usually specify:

*   `Accept`

*   `Content-Type` when a body exists

*   auth headers when required

*   correlation or tracing headers if your platform uses them

Example:

```
### @name getOrders
GET https://api.example.com/orders?status=pending&region=eu
Accept: application/json
X-Correlation-Id: req-20260302-001
X-Tenant-Id: acme
```

This kind of explicitness is especially useful in onboarding because it teaches the reader what the platform expects.

The HTTP Client supports bodies written inline or read from files.

```
### @name createOrder
POST https://api.example.com/orders
Content-Type: application/json
Accept: application/json

{
  "customerId": "CUST-100",
  "items": [
    { "sku": "BOOK-001", "quantity": 2 },
    { "sku": "PEN-002", "quantity": 3 }
  ]
}
```

This is better when the body is large or reused.

```
### @name createUserFromFile
POST https://api.example.com/users
Content-Type: application/json
Accept: application/json
< ./data/create-user.json
```

File based bodies keep the request readable and make payload review easier in pull requests.

```
### @name tokenRequest
POST https://auth.example.com/oauth/token
Content-Type: application/x-www-form-urlencoded
Accept: application/json

grant_type=client_credentials&scope=orders.read
```

Use this when uploading files or mixed form fields.

```
### @name uploadDocument
POST https://api.example.com/documents
Content-Type: multipart/form-data; boundary=boundary

--boundary
Content-Disposition: form-data; name="metadata"
Content-Type: application/json

{
  "documentType": "invoice",
  "customerId": "CUST-100"
}
--boundary
Content-Disposition: form-data; name="file"; filename="invoice.pdf"
Content-Type: application/pdf

< ./data/invoice.pdf
--boundary--
```

One of the strengths of the HTTP Client is that a single file can hold a coherent workflow.

This is not just convenient. It is important for teaching and maintenance.

A file should ideally group requests that belong to one concern:

*   `users.http` for user lifecycle

*   `auth.http` for authentication flows

*   `health.http` for operational checks

*   `orders.http` for the order domain

*   `events.http` for event related edge workflows

Example:

```
### @name listUsers
GET https://api.example.com/users
Accept: application/json

###
### @name getUser
GET https://api.example.com/users/42
Accept: application/json

###
### @name createUser
POST https://api.example.com/users
Content-Type: application/json
Accept: application/json

{
  "email": "bob@example.com",
  "displayName": "Bob"
}
```

This gives the file a narrative, not just a list of unrelated calls.

There are several ways to execute requests in IntelliJ:

*   run one request from the gutter

*   run all requests in a file sequentially

*   create run configurations

*   navigate and run from the Structure tool window

*   import requests from another `.http` file and run them

This is especially useful when request B depends on request A.

For example:

1.   log in

2.   capture token

3.   create resource

4.   fetch resource

5.   verify result

If you run all requests in the file, IntelliJ executes them in order.

Large teams often need composition. Instead of putting every request in one giant file, keep them modular and import where needed.

Run all requests from another file:

`run ./users.http`
This is useful for smoke suites and onboarding bundles.

A practical pattern is:

*   domain files for day to day work

*   one top level `onboarding.http` or `smoke.http`

*   that top level file imports and runs smaller files

Variables are what turn a request file from a one off script into a reusable asset.

You can use variables in URLs, headers, query parameters, and bodies:

```
GET https://{{host}}/users/{{userId}}
Accept: application/json
Authorization: Bearer {{token}}
```

IntelliJ supports several variable types.

These are local to the current `.http` file.

```
@host = api.example.com
@userId = 42

### @name getUserInPlace
GET https://{{host}}/users/{{userId}}
Accept: application/json
```

Use these for small shared constants inside one file.

These live in environment files and are available to request files.

`http-client.env.json`

```
{
  "local": {
    "scheme": "http",
    "host": "localhost:8080",
    "basePath": "/api",
    "tenantId": "acme-local"
  },
  "staging": {
    "scheme": "https",
    "host": "staging-api.example.com",
    "basePath": "/api",
    "tenantId": "acme-staging"
  }
}
```

Use them like this:

```
### @name getUsersFromEnvironment
GET {{scheme}}://{{host}}{{basePath}}/users
Accept: application/json
X-Tenant-Id: {{tenantId}}
```

Use these for secrets, certificates, passwords, and tokens.

`http-client.private.env.json`

```
{
  "local": {
    "username": "dev-user",
    "password": "dev-password",
    "clientSecret": "local-secret",
    "apiToken": "replace-me"
  },
  "staging": {
    "username": "stage-user",
    "password": "stage-password",
    "clientSecret": "stage-secret",
    "apiToken": "replace-me"
  }
}
```

Example request:

```
### @name getProtectedResource
GET {{scheme}}://{{host}}{{basePath}}/secure/profile
Accept: application/json
Authorization: Bearer {{apiToken}}
```

For team use, the shared rule should be:

*   public file for non sensitive shared values

*   private file for secrets

*   add the private file to `.gitignore`

Example `.gitignore`:

`http-client.private.env.json`
These are defined in a pre request script and exist only for the request that follows.

```
< {% request.variables.set("generatedUserId", "user-" + $random.uuid) %}

### @name createGeneratedUser
POST https://{{host}}{{basePath}}/users
Content-Type: application/json
Accept: application/json

{
  "id": "{{generatedUserId}}",
  "email": "generated@example.com"
}
```

Use this when a value should exist only for a single call.

Global variables are stored in `client.global` and can be reused in later requests during the same IntelliJ session.

This is extremely useful in chained workflows such as login then call protected endpoint.

From a practical project perspective:

*   use in place variables for file local readability

*   use public environment files for shared non secret settings

*   use private environment files for secrets

*   use per request variables for computed one off values

*   use global variables for values captured from earlier responses in multi step flows

Try not to put secrets directly in `.http` files. If you do, the file stops being safely shareable.

The HTTP Client provides dynamic variables such as:

*   UUIDs

*   timestamps

*   random numbers

*   random names and other faker style values

*   system environment variables

Examples:

```
### @name createRandomUser
POST https://{{host}}{{basePath}}/users
Content-Type: application/json
Accept: application/json

{
  "id": "{{$uuid}}",
  "email": "{{$random.email}}",
  "createdAt": "{{$isoTimestamp}}"
}
```

System environment variable example:

```
### @name currentUserFromOsEnv
GET http://localhost:63345/{{$env.USER}}
```

Dynamic variables are excellent for smoke tests and exploratory work, but use them carefully in assertions. Highly random input can make debugging harder.

One of the most powerful features in IntelliJ is the ability to iterate over collections stored in variables. When a variable contains an array, the HTTP Client can send one request for each element.

This is how you parameterize one request so it runs many times without duplicating the request block.

```
< {% request.variables.set("userIds", [101, 102, 103, 104]) %}

### @name getUserByCollection
GET https://{{host}}{{basePath}}/users/{{userIds}}
Accept: application/json
```

That single request definition sends four consecutive requests.

```
< {% request.variables.set("users", [
  { "id": 1, "email": "alice@example.com", "role": "admin" },
  { "id": 2, "email": "bob@example.com", "role": "reader" },
  { "id": 3, "email": "carol@example.com", "role": "writer" }
]) %}

### @name createUsersFromCollection
POST https://{{host}}{{basePath}}/users
Content-Type: application/json
Accept: application/json

{
  "id": {{$.users..id}},
  "email": "{{$.users..email}}",
  "role": "{{$.users..role}}"
}
```

```
< {% request.variables.set("accounts", [
  { "id": 10, "expectedStatus": "active" },
  { "id": 11, "expectedStatus": "disabled" }
]) %}

### @name verifyAccounts
GET https://{{host}}{{basePath}}/accounts/{{$.accounts..id}}
Accept: application/json

> {%
const current = request.variables.get("accounts")[request.iteration()];
client.test(`Account ${current.id} has expected status`, () => {
  client.assert(response.status === 200, "Expected HTTP 200");
  client.assert(jsonPath(response.body, "$.status") === current.expectedStatus, "Unexpected account status");
});
%}
```

```
< {% request.variables.set("books", [
  { "title": "Ulysses", "year": 1922 },
  { "title": "Dune", "year": 1965 }
]) %}

### @name createBooks
POST https://{{host}}{{basePath}}/books
Content-Type: application/json
Accept: application/json

{
  "title": "{{$.books..title}}",
  "year": "{{$.books..year}}"
}

> {%
const title = request.templateValue(0);
const year = request.templateValue(1);
client.log(`Processed ${title} (${year})`);
%}
```

This feature is one of the best reasons to keep request suites in IntelliJ rather than scattering repeated examples across many files.

Scripts are where the HTTP Client becomes much more than a manual request runner.

There are two script hooks:

*   pre request scripts, prefixed with `<`

*   response handler scripts, prefixed with `>`

```
< {% request.variables.set("traceId", $random.uuid) %}

### @name getUsersWithTrace
GET https://{{host}}{{basePath}}/users
Accept: application/json
X-Trace-Id: {{traceId}}
```

```
### @name healthCheck
GET https://{{host}}{{basePath}}/health
Accept: application/json

> {%
client.test("Health endpoint returns 200", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
});
%}
```

`http/scripts/common-tests.js`

```
export function assertJson(response) {
  client.assert(
    response.headers.valueOf("Content-Type").includes("application/json"),
    "Expected JSON response"
  );
}

export function assertStatus(response, status) {
  client.assert(response.status === status, `Expected HTTP ${status}`);
}
```

Use it in a response handler:

```
### @name getUsersWithCommonTests
GET https://{{host}}{{basePath}}/users
Accept: application/json

> {%
import { assertJson, assertStatus } from "./scripts/common-tests.js";

client.test("Users endpoint is healthy", () => {
  assertStatus(response, 200);
  assertJson(response);
});
%}
```

The ability to reuse script modules is critical in medium and large projects. Without it, request files become full of duplicated assertions.

A very common pattern is:

1.   send request A

2.   extract something from the response

3.   store it

4.   use it in request B

Example:

```
### @name login
POST https://{{host}}{{basePath}}/auth/login
Content-Type: application/json
Accept: application/json

{
  "username": "{{username}}",
  "password": "{{password}}"
}

> {%
client.global.set("accessToken", jsonPath(response.body, "$.accessToken"));
client.test("Login succeeded", () => {
  client.assert(response.status === 200, "Expected login to return 200");
  client.assert(!!client.global.get("accessToken"), "No access token captured");
});
%}

###
### @name getCurrentUser
GET https://{{host}}{{basePath}}/me
Accept: application/json
Authorization: Bearer {{accessToken}}

> {%
client.test("Current user endpoint returns 200", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
});
%}
```

This pattern is foundational for real world suites. It lets your request files express workflows, not just isolated calls.

The HTTP Client is not a full replacement for your unit test framework, but it is excellent for request level and workflow level checks.

Use `client.test()` to name a test and `client.assert()` for conditions.

```
### @name getStatus
GET https://{{host}}{{basePath}}/status
Accept: application/json

> {%
client.test("Status endpoint returns 200", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
});
%}
```

```
### @name getUsersHeaders
GET https://{{host}}{{basePath}}/users
Accept: application/json

> {%
client.test("Response is JSON", () => {
  client.assert(
    response.headers.valueOf("Content-Type").includes("application/json"),
    "Expected application/json"
  );
});
%}
```

```
### @name getCurrentUserProfile
GET https://{{host}}{{basePath}}/me
Accept: application/json
Authorization: Bearer {{accessToken}}

> {%
client.test("Profile contains id and email", () => {
  client.assert(!!jsonPath(response.body, "$.id"), "Expected id");
  client.assert(!!jsonPath(response.body, "$.email"), "Expected email");
});
%}
```

These are important for onboarding because they teach the expected failure model of the system.

```
### @name getUserNotFound
GET https://{{host}}{{basePath}}/users/999999
Accept: application/json

> {%
client.test("Unknown user returns 404", () => {
  client.assert(response.status === 404, "Expected HTTP 404");
});
%}
```

```
### @name createUserValidationError
POST https://{{host}}{{basePath}}/users
Content-Type: application/json
Accept: application/json

{
  "email": "not-an-email"
}

> {%
client.test("Invalid payload returns 400", () => {
  client.assert(response.status === 400, "Expected HTTP 400");
});
%}
```

A good suite contains both happy path and error path checks.

Authentication is one of the most common reasons request suites become messy. The fix is to organize auth examples by complexity.

```
### @name basicAuthExample
GET https://{{host}}{{basePath}}/basic-secure
Authorization: Basic {{username}} {{password}}
Accept: application/json
```

```
### @name digestAuthExample
GET https://{{host}}{{basePath}}/digest-secure
Authorization: Digest {{username}} {{password}}
Accept: application/json
```

```
### @name bearerAuthExample
GET https://{{host}}{{basePath}}/secure/resource
Accept: application/json
Authorization: Bearer {{apiToken}}
```

```
### @name loginAndCaptureToken
POST https://{{host}}{{basePath}}/auth/login
Content-Type: application/json
Accept: application/json

{
  "username": "{{username}}",
  "password": "{{password}}"
}

> {%
client.global.set("bearerToken", jsonPath(response.body, "$.token"));
client.test("Token captured", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
  client.assert(!!client.global.get("bearerToken"), "Missing token");
});
%}

###
### @name useCapturedToken
GET https://{{host}}{{basePath}}/secure/resource
Accept: application/json
Authorization: Bearer {{bearerToken}}
```

This is usually the best starting point when your API has a custom login endpoint.

IntelliJ also supports OAuth 2.0 as a first class feature. Instead of manually calling the token endpoint, you can define auth configuration in `http-client.env.json` and then use `{{$auth.token("...")}}` in requests.

Example environment fragment:

```
{
  "staging": {
    "Security": {
      "Auth": {
        "orders-api": {
          "Type": "OAuth2",
          "Grant Type": "Client Credentials",
          "Token URL": "https://auth.example.com/oauth/token",
          "Client ID": "orders-client",
          "Client Secret": "{{clientSecret}}",
          "Scope": "orders.read orders.write"
        }
      }
    }
  }
}
```

Example request:

```
### @name listOrdersOAuth2
GET https://{{host}}{{basePath}}/orders
Accept: application/json
Authorization: Bearer {{$auth.token("orders-api")}}
```

This is cleaner than hand rolling OAuth flows when the provider fits IntelliJ’s supported configuration model.

If your server needs an ID token instead of an access token, IntelliJ also supports `{{$auth.idToken("...")}}`.

A definitive guide would be incomplete without security discipline.

The core rules are:

*   do not hardcode passwords, tokens, client secrets, or certificates in `.http` files

*   keep secrets in `http-client.private.env.json`

*   add the private file to `.gitignore`

*   use `@no-log` on requests that should not be written to request history

*   use `@no-cookie-jar` when you do not want cookies persisted

*   do not commit response files that may contain secrets

Example:

```
# @no-log
### @name loginWithoutHistory
POST https://{{host}}{{basePath}}/auth/login
Content-Type: application/json
Accept: application/json

{
  "username": "{{username}}",
  "password": "{{password}}"
}
```

And if cookie persistence is undesirable:

```
# @no-cookie-jar
### @name sessionInitWithoutCookieJar
GET https://{{host}}{{basePath}}/session/start
Accept: application/json
```

Some APIs require client side certificates.

IntelliJ supports client certificate configuration through the private environment file.

Example:

```
{
  "staging": {
    "SSLConfiguration": {
      "clientCertificate": "certs/client.crt",
      "clientCertificateKey": "certs/client.key",
      "hasCertificatePassphrase": true
    }
  }
}
```

You can also describe certificate objects with explicit formats:

```
{
  "staging": {
    "SSLConfiguration": {
      "clientCertificate": {
        "path": "certs/client.crt",
        "format": "PEM"
      },
      "clientCertificateKey": {
        "path": "certs/client.key",
        "format": "DER"
      }
    }
  }
}
```

For trusted development scenarios with self signed certificates, IntelliJ also allows host certificate verification to be disabled in the private environment file:

```
{
  "local-ssl": {
    "SSLConfiguration": {
      "verifyHostCertificate": false
    }
  }
}
```

Use that only for local or carefully controlled development environments.

Some systems do not use bearer tokens. They use signed requests.

The HTTP Client supports cryptographic helpers in pre request scripts, which lets you compute signatures before sending the request.

Example HMAC signature:

```
< {%
const signature = crypto.hmac.sha256()
  .withTextSecret(request.environment.get("secret"))
  .updateWithText(request.body.tryGetSubstituted())
  .digest()
  .toHex();

request.variables.set("signature", signature);
%}

### @name signedRequest
POST https://{{host}}{{basePath}}/signed-endpoint
Content-Type: application/json
X-Signature: {{signature}}

{
  "eventId": "{{$uuid}}",
  "occurredAt": "{{$isoTimestamp}}"
}
```

This is particularly useful for internal webhooks, event ingress endpoints, and legacy systems that authenticate payload integrity.

The HTTP Client automatically stores received cookies in its cookie jar and reuses them for matching requests. That is convenient, but it also means you should understand when state is being carried forward.

Similarly, IntelliJ stores recently executed requests in request history. This is very useful for debugging and comparing responses, but for sensitive requests you should disable logging with `@no-log`.

If you need to inspect redirect behavior itself rather than follow it, use `@no-redirect`.

Example:

```
# @no-redirect
### @name inspectRedirect
GET https://{{host}}{{basePath}}/redirect
Accept: */*
```

Request files are not only for business APIs. They are also excellent for operational checks.

This matters because many teams need a simple, documented way to answer questions like:

*   Is the service up?

*   Is it ready to receive traffic?

*   Are dependencies available?

*   Is startup complete?

```
### @name health
GET https://{{host}}/health
Accept: application/json

> {%
client.test("Health endpoint returns 200", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
});
%}
```

```
### @name live
GET https://{{host}}/health/live
Accept: application/json

> {%
client.test("Liveness returns 200", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
});
%}
```

```
### @name ready
GET https://{{host}}/health/ready
Accept: application/json

> {%
client.test("Readiness returns 200", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
});
%}
```

```
### @name startup
GET https://{{host}}/health/startup
Accept: application/json

> {%
client.test("Startup returns 200 once boot completes", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
});
%}
```

```
### @name detailedHealth
GET https://{{host}}/health
Accept: application/json

> {%
client.test("Detailed health shows UP", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
  client.assert(jsonPath(response.body, "$.status") === "UP", "Expected overall status UP");
});
%}
```

If your application is deployed on Kubernetes, the same operational concepts should usually appear in your request files because they are part of how the system behaves in production.

Example manifest fragment:

```
livenessProbe:
  httpGet:
    path: /health/live
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /health/ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5

startupProbe:
  httpGet:
    path: /health/startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
```

A good onboarding guide links these concepts together:

*   the application exposes health endpoints

*   Kubernetes probes them

*   the request files document and test them

*   developers can reproduce the checks locally

A common mistake is to think HTTP request files only matter for REST APIs.

That is too narrow.

They are extremely useful in systems that are event driven, as long as the system exposes any compatible edge surface such as:

*   HTTP endpoints

*   webhooks

*   GraphQL

*   WebSocket

*   gRPC

*   health and admin endpoints

*   auth endpoints

*   replay or reprocessing endpoints

Imagine this flow:

1.   an order service receives a command and emits `OrderPlaced`

2.   a payment service consumes `OrderPlaced`

3.   the payment service emits `PaymentAuthorized` or `PaymentRejected`

4.   a shipping service reacts to `PaymentAuthorized`

The core event propagation may happen through a broker, not through REST. But the surrounding developer workflows still benefit from HTTP Client files:

*   obtain a token

*   create seed state

*   call a command endpoint

*   query read models

*   inspect health endpoints

*   register or test a webhook

*   open a WebSocket stream

*   call a gRPC command

*   verify final state after asynchronous processing

So the right mental model is not “these files are for REST”. The better model is “these files are for compatible interfaces around your system”.

Here is a practical example.

The application exposes an HTTP command endpoint that starts a process. Internally it publishes an event and later reaches a final state.

```
### @name placeOrder
POST https://{{host}}{{basePath}}/orders
Content-Type: application/json
Accept: application/json
Authorization: Bearer {{accessToken}}

{
  "customerId": "CUST-100",
  "items": [
    { "sku": "BOOK-001", "quantity": 1 }
  ]
}

> {%
client.global.set("orderId", jsonPath(response.body, "$.orderId"));
client.test("Order accepted", () => {
  client.assert(response.status === 202 || response.status === 201, "Expected HTTP 201 or 202");
  client.assert(!!client.global.get("orderId"), "No orderId captured");
});
%}
```

```
### @name getOrderProjection
GET https://{{host}}{{basePath}}/orders/{{orderId}}
Accept: application/json
Authorization: Bearer {{accessToken}}

> {%
client.test("Order projection is reachable", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
});
%}
```

```
### @name verifyPaymentResult
GET https://{{host}}{{basePath}}/orders/{{orderId}}/payment-status
Accept: application/json
Authorization: Bearer {{accessToken}}

> {%
client.test("Payment reached a terminal state", () => {
  const status = jsonPath(response.body, "$.status");
  client.assert(["AUTHORIZED", "REJECTED"].includes(status), "Expected terminal payment status");
});
%}
```

This is exactly where request files shine in event driven platforms. They give developers a repeatable way to drive the system at the edge and verify outcomes.

The HTTP Client supports GraphQL requests.

A GraphQL request starts with the `GRAPHQL` keyword.

```
### @name listTodosGraphQL
GRAPHQL https://{{host}}/graphql

query {
  toDos {
    title
    completed
    author {
      username
    }
  }
}
```

```
### @name countryByGraphQLVariables
GRAPHQL https://{{host}}/graphql

query ($name: String!, $capital: String!) {
  country(name: $name, capital: $capital) {
    name
    capital
  }
}

{
  "name": "France",
  "capital": "Paris"
}
```

You can also use HTTP Client environment variables inside the GraphQL variables block.

The HTTP Client also supports WebSocket requests, which is very relevant for event streams, notifications, and subscription style workflows.

Example:

```
### @name notificationsSocket
WEBSOCKET wss://{{host}}/ws/notifications
Content-Type: application/json

{
  "type": "subscribe",
  "channel": "orders"
}
===
wait-for-server
{
  "type": "ack"
}
```

This makes the HTTP Client useful even when the system is not centered on REST.

The HTTP Client can also issue gRPC requests.

Example:

```
### @name sayHelloGrpc
GRPC grpcs://{{host}}/hello.HelloService/SayHello
Content-Type: application/json

{
  "name": "Alice"
}
```

You can send gRPC metadata as headers:

```
### @name sayHelloGrpcWithMetadata
GRPC grpcs://{{host}}/hello.HelloService/SayHello
X-Request-Id: req-001
Authorization: Bearer {{apiToken}}
Content-Type: application/json

{
  "name": "Alice"
}
```

This is especially useful in service to service platforms where business traffic is gRPC but developers still need readable, runnable request artifacts.

A strong onboarding file should be the first thing a developer opens.

Its job is not to be exhaustive. Its job is to teach the shape of the system.

A good onboarding file often contains, in order:

1.   how to select an environment

2.   how to authenticate

3.   how to check service health

4.   how to create one representative resource

5.   how to fetch that resource

6.   how to run one negative test

7.   how to run the full file

Example skeleton:

```
### @name health
GET {{scheme}}://{{host}}/health
Accept: application/json

###
### @name login
POST {{scheme}}://{{host}}{{basePath}}/auth/login
Content-Type: application/json
Accept: application/json

{
  "username": "{{username}}",
  "password": "{{password}}"
}

> {%
client.global.set("accessToken", jsonPath(response.body, "$.accessToken"));
%}

###
### @name createExampleUser
POST {{scheme}}://{{host}}{{basePath}}/users
Content-Type: application/json
Accept: application/json
Authorization: Bearer {{accessToken}}

{
  "email": "onboarding@example.com",
  "displayName": "Onboarding User"
}

> {%
client.global.set("createdUserId", jsonPath(response.body, "$.id"));
%}

###
### @name readExampleUser
GET {{scheme}}://{{host}}{{basePath}}/users/{{createdUserId}}
Accept: application/json
Authorization: Bearer {{accessToken}}
```

This gives new team members a clear first path.

One of the strongest operational features of the ecosystem is `ijhttp`, the HTTP Client CLI.

It lets you run request files from the terminal and in CI.

Important limitation: at the time of writing, the CLI does not support OAuth 2.0 authorization or SSL configuration. Plan around that when choosing between IDE execution and CLI execution.

You can install `ijhttp` via ZIP, Homebrew on macOS, or use the official Docker image.

For many teams, Docker is the easiest option because it avoids local installation.

```
docker run --rm -it \
  -v "$PWD:/workdir" \
  -w /workdir \
  jetbrains/intellij-http-client \
  --version
```

```
docker run --rm -it \
  -v "$PWD:/workdir" \
  -w /workdir \
  jetbrains/intellij-http-client \
  --env-file http/http-client.env.json \
  --private-env-file http/http-client.private.env.json \
  --env local \
  http/onboarding.http
```

```
services:
  ijhttp:
    image: jetbrains/intellij-http-client
    working_dir: /workdir
    volumes:
      - ./:/workdir
    entrypoint: ["ijhttp"]
```

Run it like this:

```
docker compose run --rm ijhttp \
  --env-file http/http-client.env.json \
  --private-env-file http/http-client.private.env.json \
  --env local \
  http/onboarding.http
```

This is a very practical team pattern because it gives everyone the same execution environment.

If you want a project local wrapper image:

```
FROM jetbrains/intellij-http-client
WORKDIR /workdir
ENTRYPOINT ["ijhttp"]
```

Build it:

`docker build -t project-ijhttp .`
Run it:

```
docker run --rm -it \
  -v "$PWD:/workdir" \
  -w /workdir \
  project-ijhttp \
  --env-file http/http-client.env.json \
  --private-env-file http/http-client.private.env.json \
  --env local \
  http/onboarding.http
```

A helper script lowers friction a lot.

`http/run-http.sh`

```
#!/usr/bin/env bash
set -euo pipefail

REQUEST_FILE="${1:-http/onboarding.http}"
ENV_NAME="${2:-local}"

docker run --rm -i \
  -v "$PWD:/workdir" \
  -w /workdir \
  jetbrains/intellij-http-client \
  --env-file http/http-client.env.json \
  --private-env-file http/http-client.private.env.json \
  --env "$ENV_NAME" \
  "$REQUEST_FILE"
```

Usage:

```
bash http/run-http.sh http/onboarding.http local
bash http/run-http.sh http/health.http staging
```

`http/run-http.ps1`

```
param(
    [string]$RequestFile = "http/onboarding.http",
    [string]$Environment = "local"
)

docker run --rm -i `
  -v "${PWD}:/workdir" `
  -w /workdir `
  jetbrains/intellij-http-client `
  --env-file http/http-client.env.json `
  --private-env-file http/http-client.private.env.json `
  --env $Environment `
  $RequestFile
```

Usage:

```
.\http\run-http.ps1 -RequestFile http\onboarding.http -Environment local
.\http\run-http.ps1 -RequestFile http\health.http -Environment staging
```

These scripts are simple, but they make request execution much easier for people who do not want to remember Docker commands.

When using `ijhttp`, these options matter most:

*   `--env-file` for public environment values

*   `--private-env-file` for private values

*   `--env` for environment selection

*   `-V` for inline public variable overrides

*   `-P` for inline private variable overrides

*   `-L HEADERS` or `-L VERBOSE` for more detailed logging

Examples:

`ijhttp --env-file http/http-client.env.json --env local http/onboarding.http``ijhttp --private-env-file http/http-client.private.env.json --env local http/auth.http``ijhttp -V host=localhost:8080 -V tenantId=acme http/health.http``ijhttp -P password=super-secret -P username=dev-user http/auth.http``ijhttp -L VERBOSE http/health.http`
A definitive guide should include at least one realistic all in one example.

`http/onboarding.http`

```
### @name health
GET {{scheme}}://{{host}}/health
Accept: application/json

> {%
client.test("Health is reachable", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
});
%}

###
### @name login
# @no-log
POST {{scheme}}://{{host}}{{basePath}}/auth/login
Content-Type: application/json
Accept: application/json

{
  "username": "{{username}}",
  "password": "{{password}}"
}

> {%
client.global.set("accessToken", jsonPath(response.body, "$.accessToken"));
client.test("Login succeeded", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
  client.assert(!!client.global.get("accessToken"), "Expected accessToken");
});
%}

###
### @name createUser
POST {{scheme}}://{{host}}{{basePath}}/users
Content-Type: application/json
Accept: application/json
Authorization: Bearer {{accessToken}}

{
  "email": "guide-user-{{$uuid}}@example.com",
  "displayName": "Guide User"
}

> {%
client.global.set("createdUserId", jsonPath(response.body, "$.id"));
client.test("User created", () => {
  client.assert(response.status === 201 || response.status === 200, "Expected HTTP 200 or 201");
  client.assert(!!client.global.get("createdUserId"), "Expected created user id");
});
%}

###
### @name getCreatedUser
GET {{scheme}}://{{host}}{{basePath}}/users/{{createdUserId}}
Accept: application/json
Authorization: Bearer {{accessToken}}

> {%
client.test("Created user can be fetched", () => {
  client.assert(response.status === 200, "Expected HTTP 200");
  client.assert(!!jsonPath(response.body, "$.id"), "Expected id");
  client.assert(!!jsonPath(response.body, "$.email"), "Expected email");
});
%}

###
### @name deleteCreatedUser
DELETE {{scheme}}://{{host}}{{basePath}}/users/{{createdUserId}}
Accept: application/json
Authorization: Bearer {{accessToken}}

> {%
client.test("Created user can be deleted", () => {
  client.assert(response.status === 204 || response.status === 200, "Expected HTTP 204 or 200");
});
%}
```

This one file teaches a new developer:

*   how to select an environment

*   how login works

*   how tokens are captured

*   how to create data

*   how to read data

*   how to clean up

*   how assertions are written

That is exactly what onboarding material should do.

Fix: split by domain and use one top level onboarding or smoke file.

Fix: move them to `http-client.private.env.json`.

Fix: use `### @name` consistently.

Fix: add validation, auth, and not found examples.

Fix: extract reusable assertions into JavaScript helper files.

Fix: parameterize scheme, host, base paths, credentials, and identifiers.

Fix: include health, readiness, liveness, and startup endpoints.

Fix: document the compatible interfaces around the event driven system, not just REST resources.

If you want request files to stay maintainable, define a few team rules.

Recommended standards:

*   one concern per file

*   request names are mandatory

*   every protected workflow starts with an auth example

*   every domain file contains at least one negative test

*   secrets never live in `.http` files

*   onboarding file must be runnable end to end

*   health file must exist for every service

*   common assertions go in reusable script files

*   large payloads should live in data files

*   terminal execution should work through Docker wrappers or helper scripts

These rules sound simple, but they prevent most long term drift.

This tool is especially strong when you want:

*   executable API documentation

*   developer onboarding

*   exploratory testing

*   smoke and regression checks at request level

*   reproducible health checks

*   reusable authentication workflows

*   simple CI execution through `ijhttp`

*   lightweight validation around HTTP, GraphQL, WebSocket, and gRPC edges

It is not meant to replace unit tests, property based testing, or full end to end test frameworks. It sits in a different and very useful layer.

If you only remember five things from this guide, remember these:

1.   Keep request files in version control and treat them as real project assets.

2.   Separate public environment values from secrets.

3.   Name requests and group them by concern.

4.   Use scripts and assertions to turn examples into repeatable checks.

5.   Include operational and event driven edge workflows, not just CRUD examples.

That combination is what turns the IntelliJ HTTP Client from a convenience feature into a serious engineering tool.

JetBrains. HTTP Client.  
[https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html](https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html)

JetBrains. Exploring the HTTP request syntax.  
[https://www.jetbrains.com/help/idea/exploring-http-syntax.html](https://www.jetbrains.com/help/idea/exploring-http-syntax.html)

JetBrains. HTTP Client variables.  
[https://www.jetbrains.com/help/idea/http-client-variables.html](https://www.jetbrains.com/help/idea/http-client-variables.html)

JetBrains. OAuth 2.0 authorization.  
[https://www.jetbrains.com/help/idea/oauth-2-0-authorization.html](https://www.jetbrains.com/help/idea/oauth-2-0-authorization.html)

JetBrains. HTTP Client CLI.  
[https://www.jetbrains.com/help/idea/http-client-cli.html](https://www.jetbrains.com/help/idea/http-client-cli.html)

JetBrains. Manage HTTP requests directly in the IDE.  
[https://www.jetbrains.com/pages/intellij-idea-http-client/](https://www.jetbrains.com/pages/intellij-idea-http-client/)

Kubernetes. Liveness, Readiness, and Startup Probes.  
[https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)

Kubernetes. Configure Liveness, Readiness and Startup Probes.  
[https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
