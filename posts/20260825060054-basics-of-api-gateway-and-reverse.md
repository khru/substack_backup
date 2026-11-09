Title: Basics of API Gateway and Reverse Proxy

URL Source: http://emmanuelvalverderamos.substack.com/p/basics-of-api-gateway-and-reverse

Final URL: https://emmanuelvalverderamos.substack.com/p/basics-of-api-gateway-and-reverse

Published Time: 2026-08-25T06:00:54+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!8A9y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F909ac6c7-6cf1-4663-81c4-e2de78c628fe_1024x559.png)](https://substackcdn.com/image/fetch/$s_!8A9y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F909ac6c7-6cf1-4663-81c4-e2de78c628fe_1024x559.png)

Imagine a restaurant.

At the entrance there is a door. It opens, closes, keeps the rain out, and lets people enter without walking through the kitchen. A good door matters. If it jams, the restaurant has a problem. If it leaks, the restaurant has a problem. If it is too narrow, the restaurant has a problem.

But the door does not decide who has a reservation. It does not check allergies. It does not translate the menu. It does not tell the kitchen that table seven needs the tasting menu without shellfish. It does not know whether a customer is a regular, a delivery driver, a food critic, or someone trying to enter through the staff entrance.

That is the concierge’s job.

A reverse proxy is often the door. An _application programming interface_ (API) gateway is closer to the concierge. The confusion starts because both stand near the entrance, both receive requests before the real service does, and both can forward traffic somewhere else. Under the hood, many API gateways use reverse proxy mechanics. They accept traffic, match routes, apply rules, and forward valid requests to backend services.

The important difference is not the path the request travels.

The important difference is the promise being managed.

A reverse proxy mainly asks:

> Where should this request go, and how should traffic be handled safely?

An API gateway asks something broader:

> Who is calling this API, what are they allowed to do, under which rules, through which public contract, and how will we observe and evolve that contract over time?

That difference sounds small until the system grows. Then it becomes the difference between a clean entrance and a very expensive front door pretending to be a concierge.

A reverse proxy and an API gateway are not clean alternatives at the same level of abstraction. A reverse proxy is a network-facing intermediary that receives a request from a client and forwards it to a backend service. It commonly handles traffic concerns such as routing, load balancing, _transport layer security_ (TLS) termination, header forwarding, buffering, caching, and timeouts. NGINX’s reverse proxy documentation describes this in concrete terms: passing requests to proxied servers, modifying request headers, and configuring buffering for proxied responses. ([docs.nginx.com](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/))

An API gateway often includes reverse proxy behavior, but it adds API concerns. It can authenticate callers, apply rate limits, enforce quotas, transform requests or responses, route versions, collect telemetry, and make API policy explicit. AWS describes Amazon API Gateway as a service for creating, publishing, maintaining, monitoring, and securing APIs. Azure describes its API Management gateway as the runtime component responsible for proxying API requests, applying policies, and collecting telemetry. Google Cloud describes API Gateway as a way to provide secure access through a well-defined REST API that remains consistent across backend implementations. ([Documentación de AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html))

Use a reverse proxy when the main problem is traffic forwarding, safe exposure, load balancing, TLS termination, or simple routing. Use an API gateway when the API has become a consumer-facing contract that needs identity, access rules, quotas, versioning, analytics, governance, and operational ownership.

The trap is buying an API gateway when all you need is a door, or stretching a reverse proxy until it becomes a hand-built, undocumented, half-governed API platform.

1.   Before comparing, let’s name the pieces

2.   The simplest request flow

3.   What a reverse proxy adds

4.   NGINX as a reverse proxy

5.   What an API gateway adds

6.   Kong as an API gateway

7.   Same request, different responsibility

8.   The real distinction: traffic vs API policy

9.   Do not put business logic at the edge

10.   A small note about _backends for frontends_ (BFF)

11.   How to decide

12.   The economic story

13.   Common traps

14.   Conclusions

15.   References

Before comparing a reverse proxy with an API gateway, we need a small vocabulary. Otherwise, the article becomes a parade of familiar-sounding words that hide more than they explain.

A **client** is the thing making a request. It can be a browser, a mobile app, another backend service, a partner system, a script, or a public API consumer. The client wants something from your system.

A **backend service** is the application that actually handles the request. In a simple system, it may be one application. In a larger system, it may be one service among many: orders, payments, catalog, users, invoices, notifications, or anything else.

An **API** is the visible way another system talks to yours. It includes paths, methods, request bodies, response bodies, headers, status codes, authentication expectations, error formats, and behavior. An API is not just a URL. It is a promise.

A **route** is a rule that says where a request should go. For example, requests starting with `/orders` may go to the checkout service, while requests starting with `/users` may go to the users service.

A **policy** is a rule applied around the request. Authentication is a policy. Rate limiting is a policy. Quotas are policies. Request transformation can be a policy. Some policies protect the system. Some protect the consumer. Some protect the contract.

A **consumer** is the person, application, team, partner, or external system using your API. A reverse proxy can forward traffic without knowing much about consumers. An API gateway often needs to know who the consumer is because different consumers may have different permissions, limits, versions, or contracts.

An **API contract** is the promise your API makes to its consumers. It says, explicitly or implicitly: if you call this path, with this method, this data, and this authentication, you can expect this kind of response and behavior. Breaking that promise has a cost.

With those terms in place, the comparison becomes much easier.

A reverse proxy mostly cares about **moving requests safely**.

An API gateway cares about **managing API promises around those requests**.

Start with the simplest possible picture.

[![Image 2](https://substackcdn.com/image/fetch/$s_!nXI0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe06c4b06-b339-4c3e-999a-47378f058c3f_904x534.png)](https://substackcdn.com/image/fetch/$s_!nXI0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe06c4b06-b339-4c3e-999a-47378f058c3f_904x534.png)

The client calls the backend service directly. That is easy to understand, and for a local development environment it may be perfectly fine. But exposing a backend directly to the outside world often creates problems.

The backend may not be the right place to terminate TLS. It may not be the right place to handle every public hostname. It may not be the right place to distribute traffic across multiple instances. It may not be safe to expose its internal address. It may not be wise to let every client know the shape of the internal system.

So teams often add a component in front.

That is where the reverse proxy enters.

A reverse proxy receives the request first and forwards it to the backend service. The client talks to the reverse proxy as if it were the service. The reverse proxy then talks to the real backend.

[![Image 3](https://substackcdn.com/image/fetch/$s_!hdmm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eba67cb-0808-438f-9352-d636997bbd48_1308x726.png)](https://substackcdn.com/image/fetch/$s_!hdmm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eba67cb-0808-438f-9352-d636997bbd48_1308x726.png)

The reverse proxy can hide internal backend addresses, terminate TLS, route requests by path or hostname, forward useful headers, distribute requests across several backend instances, buffer responses, and apply timeouts. NGINX’s official documentation describes reverse proxying through exactly this kind of request forwarding, header modification, and response buffering. ([docs.nginx.com](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/))

In the restaurant metaphor, the reverse proxy is the door and the corridor. It lets people enter through the right place and sends them to the right room. That is useful. That is necessary. That can be enough.

But it is not the same as checking reservations, applying house rules, identifying guests, or managing promises made to regular customers.

That is the point where an API gateway may become necessary.

[![Image 4](https://substackcdn.com/image/fetch/$s_!l-yu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67472a2e-dd22-4b72-96b1-8929f3db6394_1024x559.png)](https://substackcdn.com/image/fetch/$s_!l-yu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67472a2e-dd22-4b72-96b1-8929f3db6394_1024x559.png)

Let’s keep the first code example deliberately small.

Imagine this backend service:

`checkout-api:3000`
It exposes this endpoint:

`GET /orders/{orderId}`
A minimal NGINX reverse proxy configuration could look like this:

This says:

`When a request arrives at api.example.com/orders/, forward it to checkout-api:3000/orders/.`
That is the essence of a reverse proxy. It receives the public request and forwards it to the backend.

A more realistic configuration often adds TLS, upstreams, request headers, request IDs, and timeouts:

This is still mostly traffic handling. The backend is hidden. TLS terminates at the edge. Traffic can be distributed across instances. Headers can preserve useful request information. Timeouts can prevent a slow backend from holding connections forever. NGINX documents both the core reverse proxy behavior and proxy module details such as response buffering. ([docs.nginx.com](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/))

But notice what is absent.

There is no API consumer. There is no subscription. There is no API key. There is no quota per client. There is no versioned public contract. There is no policy saying that the mobile app can call this endpoint 100 times per minute while a partner platform can call it 1,000 times per minute.

The reverse proxy is doing its job well.

Its job is traffic.

The door opens. The guest enters. The kitchen receives the order.

One practical warning matters here: path handling is part of the contract. If `/orders/123` is meant to reach the backend as `/orders/123`, test that behavior explicitly. Reverse proxy configuration can break contracts quietly when paths, slashes, or rewrites change.

[![Image 5](https://substackcdn.com/image/fetch/$s_!jLBZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F933d6e1d-2461-4c41-98af-bc70b427f8ff_1024x559.png)](https://substackcdn.com/image/fetch/$s_!jLBZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F933d6e1d-2461-4c41-98af-bc70b427f8ff_1024x559.png)

An API gateway still forwards requests. That is why it can look like a reverse proxy from far away.

But an API gateway adds a new layer of responsibility: API policy.

It can ask questions like:

1.   Who is calling?

2.   Are they authenticated?

3.   Are they allowed to call this API?

4.   Which version are they using?

5.   How many requests can they make?

6.   Should this request be transformed before reaching the backend?

7.   How do we observe usage by consumer, route, version, or product?

8.   Can we change the backend without changing the public API?  
Those questions are not just traffic questions. They are API management questions.

That is why major API gateway products describe themselves in broader terms than simple forwarding. AWS API Gateway is described as a service for creating, publishing, maintaining, monitoring, and securing APIs. Azure API Management describes policies that can address scenarios such as authentication, rate limiting, caching, and request or response transformation. Google Cloud API Gateway emphasizes a well-defined REST API that stays consistent regardless of backend implementation. ([Documentación de AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html))

This is the shift:

A reverse proxy mainly knows where the backend is.

An API gateway also knows something about the API consumer and the API promise.

In the restaurant metaphor, the gateway is not just opening the door. It is checking the reservation, applying the rules of the house, noticing whether the customer has a tasting menu, and recording what happened so the restaurant can operate reliably.

The concierge is now working.

[![Image 6](https://substackcdn.com/image/fetch/$s_!0Smb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02a70890-e395-406c-873e-4c0f2a77e622_1024x559.png)](https://substackcdn.com/image/fetch/$s_!0Smb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02a70890-e395-406c-873e-4c0f2a77e622_1024x559.png)

Before showing the gateway configuration, we need a tiny bit of Kong vocabulary.

A **Service** is the backend Kong will call. In our example, that backend is `checkout-api`.

A **Route** is the public path Kong listens to. In our example, that public path will be `/api/v1/orders`.

A **Consumer** is an API caller known to Kong. It can represent an app, a partner, a team, or another system.

A **Plugin** adds behavior to the request flow. A plugin can authenticate, rate limit, transform, log, or apply another kind of gateway policy. Kong’s documentation describes routes as a way to configure proxy behavior and plugins such as Key Auth, Rate Limiting, and Request Transformer as mechanisms for adding authentication, limits, and request changes. ([Kong Docs](https://developer.konghq.com/gateway/entities/route/))

First, here is Kong doing mostly routing:

This says:

`Expose /api/v1/orders publicly and forward matching requests to checkout-api:3000/orders.`
So far, this is still close to reverse proxy behavior. There is a public route and a backend service.

Now add gateway policy:

Now the configuration says much more:

```
Expose checkout orders as a versioned public API.
Require an API key.
Identify the consumer.
Apply a request limit.
Add gateway-level headers.
Forward valid requests to the backend.
```

That is the difference.

The client no longer calls:

`GET /orders/123`
It calls:

```
GET /api/v1/orders/123
apikey: ${MOBILE_APP_API_KEY}
```

The backend may still handle the same business request, but the public boundary is now richer. It has identity, policy, versioning, and operational visibility.

Two practical notes matter. First, the API keys above are placeholders. Real secrets should come from a deployment environment or secret manager, not from committed configuration. Second, `policy: local` is fine for a teaching example, but in a multi-node gateway deployment local counters can give each gateway node its own limit, which may not represent the product-level quota you think you are enforcing. Kong’s rate limiting documentation explains that the plugin limits requests over time windows and identifies clients by consumer when authentication is configured. ([Kong Docs](https://developer.konghq.com/plugins/rate-limiting/))

The point is not that this exact Kong file is a universal production recipe.

The point is that the API gateway is no longer only forwarding traffic. It is managing rules around API consumption.

[![Image 7](https://substackcdn.com/image/fetch/$s_!6giq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9a6a13e-b208-46bd-ae16-f6d2d1d55fee_1024x558.png)](https://substackcdn.com/image/fetch/$s_!6giq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9a6a13e-b208-46bd-ae16-f6d2d1d55fee_1024x558.png)

Now compare the two flows.

[![Image 8](https://substackcdn.com/image/fetch/$s_!26EM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffaa5bfe-6082-4545-a3b1-b2f650e5fd3f_1792x1578.png)](https://substackcdn.com/image/fetch/$s_!26EM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffaa5bfe-6082-4545-a3b1-b2f650e5fd3f_1792x1578.png)

Both components forward traffic. Both can sit at the edge. Both can make a backend available through a public URL.

But only one is clearly managing the API as a governed contract.

The reverse proxy answers:

`Where should this request go?`
The API gateway also answers:

```
Who is calling?
Are they allowed?
Which public API contract are they using?
Which rules apply before the backend receives the request?
How do we observe and evolve this API over time?
```

That is why the comparison is easy to misunderstand. The difference is not that one forwards and the other does not. The difference is what else the component owns.

A reverse proxy is mainly a traffic boundary.

An API gateway is an API operating boundary.

[![Image 9](https://substackcdn.com/image/fetch/$s_!M8S-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5f50d05-119b-40c1-94d9-c12e2d61daef_1024x559.png)](https://substackcdn.com/image/fetch/$s_!M8S-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5f50d05-119b-40c1-94d9-c12e2d61daef_1024x559.png)

Now we can introduce the architectural language without losing the reader.

A reverse proxy is usually a **traffic boundary**. It protects the backend from direct exposure and manages how requests move through the network.

An API gateway is usually an **API policy boundary**. It protects the backend too, but it also protects the public API contract, the consumer relationship, and the organization’s ability to evolve the API without scattering rules everywhere.

[![Image 10](https://substackcdn.com/image/fetch/$s_!aSPd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4874cfe-c072-4625-99c9-6a7675ca44d1_1613x1148.png)](https://substackcdn.com/image/fetch/$s_!aSPd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4874cfe-c072-4625-99c9-6a7675ca44d1_1613x1148.png)

This is where _Separation of Concerns_ stops being a slogan. It becomes a map of where each decision belongs.

The reverse proxy should not become the API product model. The API gateway should not become the place where every product rule is hidden. The backend application should not depend on whether the request arrived through NGINX, Kong, AWS API Gateway, Azure API Management, or a local test.

In ports and adapters language, the API is an inbound port into the system. The gateway is an adapter and policy layer in front of that port, not the domain itself. It may authenticate, throttle, route, validate coarse request shape, and translate protocol concerns, but it should not become the place where business decisions live.

That is the practical reading of the _dependency inversion principle_ (DIP) here. High-level application and business rules should not depend on low-level delivery mechanisms. The gateway may know how to reach the application, but the application should not be designed around the gateway.

The gateway may check whether the caller is allowed through the door.

The kitchen still decides how to cook.

[![Image 11](https://substackcdn.com/image/fetch/$s_!IfI9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebba33-dfb2-4d70-bc8c-db354b538708_1024x425.png)](https://substackcdn.com/image/fetch/$s_!IfI9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebba33-dfb2-4d70-bc8c-db354b538708_1024x425.png)

The gateway can reject an unauthenticated request. It can throttle abusive traffic. It can route `/api/v1/orders` to the checkout service. It can add correlation headers. It can enforce coarse API policy.

But it should not decide whether an order can be canceled.

It should not decide whether a refund is allowed.

It should not decide whether a customer deserves a discount.

Those are business rules. They belong behind the application boundary, where they can be named, tested, refactored, and protected by the model.

A bad design hides business behavior in edge rules:

```
If header X-Plan is premium
and path starts with /orders
and region is EU
and query flag refund=true
then route to special-refund-service.
```

That may look fast in the short term, but it creates invisible coupling. Business policy becomes distributed across headers, gateway rules, paths, and service exceptions. The team eventually needs to understand production behavior by reading YAML, dashboard settings, and half-remembered deployment conventions.

A cleaner design keeps edge policy at the edge and business policy in the application:

This code is not about NGINX or Kong. That is the point.

The gateway may authenticate the caller. The application decides whether the refund is allowed. The use case receives its policy from the outside, which is inversion of control in practice. The use case depends on an interface, not on a gateway rule, an HTTP header, or a database query. That keeps the business decision testable without the edge infrastructure.

The example is intentionally small. A real application may use stronger identifiers, explicit value objects, richer errors, and better domain language to avoid primitive obsession, data clumps, magic strings, and magic numbers. The important lesson is simpler: do not compensate for weak application modeling by hiding product logic in gateway configuration.

The gateway is a boundary, not a domain model.

The concierge should not rewrite the recipe.

There is one neighboring pattern worth mentioning because it prevents a common gateway mistake.

A _backends for frontends_ (BFF) service is a backend tailored to a specific frontend experience. Sam Newman describes the pattern as creating a backend service specifically designed for the needs of a particular frontend, and Microsoft’s architecture guidance frames it as a way to decouple backend services from frontend implementations so different client interfaces can have tailored experiences. ([samnewman.io](https://samnewman.io/patterns/architectural/bff/))

That matters because teams sometimes turn the API gateway into a universal orchestration layer for every frontend. The mobile app needs one payload. The web app needs another. The admin console needs a different flow. Slowly, the gateway becomes full of experience-specific behavior.

That is usually a smell.

The API gateway is a good place for cross-cutting API policy: authentication, quotas, routing, coarse validation, versioning, and telemetry. A BFF is often a better place for frontend-specific orchestration: shaping responses for mobile, combining calls for a web page, handling partial degradation for one user experience, or adapting backend workflows to a specific client.

Keep the distinction small and practical:

```
API gateway: rules for consuming the API.
BFF: support for a specific user experience.
Application: business workflow and behavior.
```

The moment one layer starts doing every job, the architecture becomes harder to reason about.

[![Image 12](https://substackcdn.com/image/fetch/$s_!7lhg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76cca29d-1049-423f-8ff5-c2650d658701_1024x559.png)](https://substackcdn.com/image/fetch/$s_!7lhg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76cca29d-1049-423f-8ff5-c2650d658701_1024x559.png)

The practical decision is not about brand names. It is about pressure.

Use a reverse proxy when the pressure is mostly operational:

1.   You need one public entry point for one or more backend services

2.   You need TLS termination, path routing, load balancing, compression, caching, or simple header forwarding

3.   Your consumers are internal, trusted, or few

4.   API versioning and developer onboarding are not yet difficult problems

5.   You can keep policy simple without creating configuration archaeology  
Use an API gateway when the pressure is mostly API governance:

6.   You expose APIs to multiple teams, applications, customers, partners, or external developers

7.   You need consistent authentication, authorization, quotas, rate limiting, request validation, or response shaping

8.   You need usage analytics by consumer, application, product, or API version

9.   You need API contracts that can evolve independently from backend implementation

10.   You need developer discovery, documentation, subscription keys, access requests, or lifecycle management

11.   You need API policy as a repeatable platform capability, not as scattered service code  
The decision tree is simple:

[![Image 13](https://substackcdn.com/image/fetch/$s_!YZ7d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F507e4020-f49b-4bd9-9362-14b8c7d45e78_1530x2345.png)](https://substackcdn.com/image/fetch/$s_!YZ7d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F507e4020-f49b-4bd9-9362-14b8c7d45e78_1530x2345.png)

A useful test is this:

**If removing the component mainly breaks routing, it was acting as a reverse proxy. If removing it breaks your API operating model, it was acting as an API gateway.**

[![Image 14](https://substackcdn.com/image/fetch/$s_!H5cN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff875bf4c-11a6-4095-8558-2915686ba69d_1024x559.png)](https://substackcdn.com/image/fetch/$s_!H5cN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff875bf4c-11a6-4095-8558-2915686ba69d_1024x559.png)

The wrong gateway decision is rarely just a technical mistake. It is an economic mistake.

Imagine the system starts with one web app and one backend. The team needs HTTPS, a public hostname, and safe forwarding to the backend. A reverse proxy is enough. Adding a full API gateway here may be premature platforming. It adds configuration, runtime cost, pricing questions, operational ownership, and another failure point before the system has the pressure to justify it.

Then the system grows.

A mobile app appears. The same backend still works, but now the team starts caring about payload size, version compatibility, and different release rhythms. Maybe a reverse proxy is still enough. Maybe a small BFF becomes useful. The answer depends on the actual pressure.

Then partners appear. Now the system needs to know who is calling. Partner A has a higher quota than partner B. One partner uses version one of the API. Another needs a migration window. Support wants to know which consumer is seeing errors. Product wants usage analytics. Security wants consistent authentication. Engineering wants to change backend implementation without breaking the public API.

At that point, the cost of not having an API gateway, or some equivalent API management mechanism, starts to rise.

The cost model is not mysterious:

1.   **Duplicated policy cost:** every service reimplements authentication, throttling, error shaping, and logging differently

2.   **Consumer breakage cost:** clients depend on unstable paths, payloads, headers, or versioning conventions

3.   **Configuration cost:** the gateway itself becomes a system that must be reviewed, tested, deployed, and observed

4.   **Runtime cost:** every extra hop adds latency, capacity planning, and failure modes

5.   **Vendor coupling cost:** managed gateways can shape deployment, observability, pricing, and portability

6.   **Future change cost:** weak boundaries make every API change more expensive than it needed to be  
Good architecture is not maximum abstraction. Good architecture is preserving future movement at a cost the system can afford.

A reverse proxy buys operational liquidity. It lets services move behind a stable entry point.

An API gateway buys API liquidity. It lets consumers keep a stable contract while backend implementation, policy, and operational rules evolve behind the boundary.

That distinction matters because every boundary has a carrying cost. A boundary can protect change, but it can also become inventory. A gateway that nobody governs becomes policy debt. A reverse proxy full of exceptions becomes routing debt. A BFF that accumulates business rules becomes product logic debt.

The question is not which component is fashionable.

The question is which cost you are choosing.

The first trap is buying too much platform too early. If the system has one client, one backend, no external consumers, no complex API policy, and no lifecycle pressure, a full API gateway may be more machinery than value. You do not need a concierge to operate a vending machine.

The second trap is stretching a reverse proxy too far. A reverse proxy can start clean and become a junk drawer. First one rewrite rule. Then one special header. Then a temporary authentication exception. Then a rate limit for one customer. Then a version-specific route. Then a script nobody wants to touch. The proxy did not fail. The boundary changed, and the team did not rename the problem.

The third trap is hiding business rules at the edge. Gateways are tempting places for quick decisions because configuration feels cheaper than code. But when business behavior is spread across paths, headers, plugins, and dashboard settings, the system becomes harder to understand and test.

The fourth trap is treating paths and headers as harmless strings. `/api/v1/orders`, `X-API-Version`, `apikey`, quota numbers, plan names, scopes, and tenant identifiers are contract decisions. They deserve tests, review, documentation, and ownership. Kong’s route documentation makes path behavior explicit through options such as `strip_path` and `path_handling`, which is a useful reminder that routing details can change the backend request in ways the consumer never sees. ([Kong Docs](https://developer.konghq.com/gateway/entities/route/))

The fifth trap is confusing “can” with “should.” Many tools can route, authenticate, transform, observe, and orchestrate. That does not mean every responsibility belongs in the same place. The clean architecture question is not “which box can technically do this?” The clean architecture question is “which boundary should own this decision?”

[![Image 15](https://substackcdn.com/image/fetch/$s_!frky!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04b5b7ba-ced0-43e6-bf9f-0b2b930b10c2_1024x559.png)](https://substackcdn.com/image/fetch/$s_!frky!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04b5b7ba-ced0-43e6-bf9f-0b2b930b10c2_1024x559.png)

The strongest answer to “reverse proxy vs API gateway” is this:

**You are probably comparing a mechanism with a responsibility.**

A reverse proxy is the mechanism many systems use to receive, route, and protect traffic before it reaches backend services. It is excellent when the problem is operational edge control: TLS termination, routing, load balancing, upstream isolation, buffering, caching, and simple traffic rules.

An API gateway may use the same kind of proxying underneath, but it exists for a broader reason. It manages the exposed API boundary. It centralizes policies that would otherwise be duplicated across services. It supports authentication, authorization, rate limits, quotas, versioning, analytics, consumer identity, developer experience, and contract stability.

The mistake is not choosing one or the other. The mistake is choosing by label.

Some teams buy an API gateway when they only need a door. They pay for a platform but use it as a forwarding rule. Other teams keep stretching a reverse proxy until it becomes an accidental API gateway with no owner, no contract model, no governance, and no clear operating discipline.

A better question is:

**What boundary are we trying to create?**

If the boundary is mostly about traffic, use a reverse proxy.

If the boundary is about APIs as contracts consumed by other people, teams, systems, customers, or partners, use an API gateway.

If the boundary is about tailoring backend behavior for a specific user experience, consider a BFF behind the gateway.

And if the real problem is a messy API, start there. No gateway can make a confused contract simple. It can only move the confusion to a more expensive place.

The tragedy of bad API architecture is not that teams pick the wrong box. It is that they let the wrong box make the wrong decisions.

The door matters.

The concierge matters.

The kitchen still needs to know how to cook.

*   NGINX. _NGINX Reverse Proxy_. [https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)

*   NGINX. _Module ngx\_http\_proxy\_module_. [https://nginx.org/en/docs/http/ngx_http_proxy_module.html](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)

*   Kong. _Routes_. [https://developer.konghq.com/gateway/entities/route/](https://developer.konghq.com/gateway/entities/route/)

*   Kong. _DB-less mode_. [https://developer.konghq.com/gateway/db-less-mode/](https://developer.konghq.com/gateway/db-less-mode/)

*   Kong. _Key Auth plugin_. [https://developer.konghq.com/plugins/key-auth/](https://developer.konghq.com/plugins/key-auth/)

*   Kong. _Rate Limiting plugin_. [https://developer.konghq.com/plugins/rate-limiting/](https://developer.konghq.com/plugins/rate-limiting/)

*   Kong. _Request Transformer plugin_. [https://developer.konghq.com/plugins/request-transformer/](https://developer.konghq.com/plugins/request-transformer/)

*   Amazon Web Services. _Amazon API Gateway documentation_. [https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

*   Amazon Web Services. _Amazon API Gateway_. [https://aws.amazon.com/api-gateway/](https://aws.amazon.com/api-gateway/)

*   Microsoft. _API gateway in Azure API Management_. [https://learn.microsoft.com/en-us/azure/api-management/api-management-gateways-overview](https://learn.microsoft.com/en-us/azure/api-management/api-management-gateways-overview)

*   Microsoft. _Policies in Azure API Management_. [https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-policies](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-policies)

*   Google Cloud. _API Gateway documentation_. [https://docs.cloud.google.com/api-gateway/docs](https://docs.cloud.google.com/api-gateway/docs)

*   Google Cloud. _About API Gateway_. [https://docs.cloud.google.com/api-gateway/docs/about-api-gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway)

*   Newman, Sam. _Backends for Frontends_. [https://samnewman.io/patterns/architectural/bff/](https://samnewman.io/patterns/architectural/bff/)

*   Microsoft. _Backends for Frontends pattern_. [https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends](https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends)
