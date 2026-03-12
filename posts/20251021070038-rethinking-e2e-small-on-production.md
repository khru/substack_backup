---
title: "Rethinking E2E: small, on-production smoke checks for critical flows"
requested_url: "https://emmanuelvalverderamos.substack.com/p/rethinking-e2e-small-on-production"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/rethinking-e2e-small-on-production"
substack_post_id: 171904113
retrieved_at: "2026-03-12T08:37:10.422Z"
---
# Rethinking E2E: small, on-production smoke checks for critical flows

[![Roll Safe Think About It Meme Generator - Imgflip](https://substackcdn.com/image/fetch/$s_!tb3M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3430cf83-f6ad-46f7-b797-1347499703da_702x395.jpeg)](https://substackcdn.com/image/fetch/$s_!tb3M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3430cf83-f6ad-46f7-b797-1347499703da_702x395.jpeg)

A few weeks ago, during one of our usual virtual coffees with **[Matheus Marabesi](https://www.linkedin.com/in/marabesi/)**, **[Javier López](https://javil.substack.com/)**, and **[Isidro López](https://www.linkedin.com/in/islomar/)**, two comments made me reframe what I call an E2E test.

I have a bias. I have spent years practicing TDD, so I care a lot about short feedback cycles and the confidence that comes from adding only lines that are already covered.

Javi said something that stuck with me: E2E tests are often expensive and provide weak feedback. If what we need is confidence, other options give a stronger signal at a lower cost, for example, contract tests when we consume an API.

Isidro added a different angle that clicked immediately: E2E, in his mind, is more like smoke tests. They cover important flows and help us detect problems quickly.

Those two ideas crystallized my own definition.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## My working definition

**E2E is on production smoke checks of a few critical user journeys, running on a separate, non-blocking cadence, and wired to alerts.** The purpose is not exhaustive verification. The purpose is the rapid detection of something essential for users that is currently broken in production.

This is different from running a large suite against a production-like environment. It is small, focused, operational, and optimized for signal.

## Why does this framing help

- **Cost and signal.** Large, pre-release E2E suites tend to be slow, brittle, and costly to keep healthy. If the goal is confidence, most of it should come from faster layers that push on design while keeping feedback tight: unit tests with a behavioral focus, component or narrow-integration tests, acceptance tests below the UI, and contract tests where services collaborate. As Martin Fowler puts it, “Frequency reduces difficulty.” The tests you run often shape the design and reduce risk over time.

These smoke checks watch the important stuff: the flows that define the business.

## What on-production smoke checks look like

- **Scope:** a small number of critical flows, for example, sign-in, search to detail to checkout, booking confirmation, or top-up.
- **Cadence:** a separate, non-blocking pipeline. Run every few minutes or hourly, and also after a deployment.
- **Data strategy:** dedicated test users and idempotent paths. Use sandbox payments, zero-value SKUs, auto-cancel orders, or immediate rollbacks.
- **Observability:** each run emits structured logs and metrics, including correlation IDs. Failures page the owning team with context.
- **Stability tactics:** prefer stable seams such as public routes and contract-backed APIs. Avoid fragile selectors. Cap runtime per flow. Clean up on success and on failure.
- **Governance:** Treat these checks as operational monitors. Updating them follows the same discipline as updating a dashboard or an alert.

### Example: e-commerce checkout

Every 20 minutes:

- Log in as a smoke user.
- Add a known smoke SKU to the cart.
- Check out through a test payment path that creates a real order and auto-cancels or refunds immediately.
- Verify the expected status transitions, for example, `PLACED` → `PAID` → `CANCELLED` for the smoke SKU.
- In case the test fails, trigger an alert of an incident (P1, P2, P3).

If this fails, a real user is probably stuck. Treat it as a production incident.

## How does this fit with the rest of the strategy?

Think of a supporting structure that balances speed and realism. I am summarizing how I split responsibility, without ranking layers against each other, and without downplaying UI tests.

- **Unit tests with a behavioral focus.** Fast, isolated, and refactor-friendly. They shape, design, and give immediate feedback.
- **Component or narrow-integration tests.** They exercise small but meaningful collaborations, still at a good speed.
- **Contract tests.** They keep boundaries honest and make breaking changes visible early.
- **Acceptance or subcutaneous tests below the UI.** They assert business behavior without the flakiness of full end-to-end environments.
- **On-production E2E smoke checks.** A thin, high-value layer that confirms reality in production for the journeys that matter most.

## Common traps to avoid

- Turning smoke checks into a full regression suite.
- Encoding internal details that change often, for example, brittle selectors.
- Allowing long cinematic flows that attempt to cover everything. Split flows or move specific checks to faster layers.
- Alerting on every single failure. Use consecutive-failure rules and include enough context to triage quickly.

## Metrics that actually help

- **Time to detect** and **time to resolve** when a critical flow breaks.
- **False positive rate** for the smoke checks.
- **Coverage of critical journeys** rather than code coverage.
- **Mean runtime per flow**, kept short to stay actionable.
- **An explicit SLO for the smoke pipeline**, for example, is a target for failed runs without confirmed incidents.

## A practical recipe

- Pick three essential flows that users perform every day and that are important for your business.
- Make them idempotent and reliable to clean up.
- Add structured logging and trace correlation.
- Run the checks regularly on a non-blocking schedule.
- Alert on consecutive failures and include a short runbook.
- Triage these alerts as you would any other production signal.

## Where I landed

I still want tight loops and strong design pressure in the fast layers. That is where most quality is created. I also want a small, loud siren in production that tells me whether real users can complete the essential journeys. That is what I now call E2E in practice: on-production smoke checks for the few flows that define the business.

---

## Acknowledgements

This reframing of E2E testing grew out of conversations with three people I admire. Thank you, **[Matheus Marabesi](https://www.linkedin.com/in/marabesi/)**, **[Javier López Fernández](https://www.linkedin.com/in/javierlopezfernandez/)**, and **[Isidro López](https://www.linkedin.com/in/islomar/)**.

## Bibliography

**Previous articles that inform this view**

- What makes a great automated test [https://emmanuelvalverderamos.substack.com/p/what-makes-a-great-automated-test](https://emmanuelvalverderamos.substack.com/p/what-makes-a-great-automated-test)
- What to test, the subject under test [https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test](https://emmanuelvalverderamos.substack.com/p/what-to-test-the-subject-under-test)
- How to write a test [https://emmanuelvalverderamos.substack.com/p/how-to-write-a-test](https://emmanuelvalverderamos.substack.com/p/how-to-write-a-test)
- Unlock the secrets of software testing [https://emmanuelvalverderamos.substack.com/p/unlock-the-secrets-of-software-testing](https://emmanuelvalverderamos.substack.com/p/unlock-the-secrets-of-software-testing)
- Test doubles [https://emmanuelvalverderamos.substack.com/p/test-doubles](https://emmanuelvalverderamos.substack.com/p/test-doubles)
- Deep dive into the relationship between [https://emmanuelvalverderamos.substack.com/p/deep-dive-into-the-relationship-between](https://emmanuelvalverderamos.substack.com/p/deep-dive-into-the-relationship-between)
- Unit testing basics [https://emmanuelvalverderamos.substack.com/p/unit-testing-basics](https://emmanuelvalverderamos.substack.com/p/unit-testing-basics)
- Integration testing basics [https://emmanuelvalverderamos.substack.com/p/integration-testing-basics](https://emmanuelvalverderamos.substack.com/p/integration-testing-basics)
- Explaining unit tests, solitary and sociable [https://emmanuelvalverderamos.substack.com/p/explaining-unit-tests-solitarysociable](https://emmanuelvalverderamos.substack.com/p/explaining-unit-tests-solitarysociable)
- Collaborative work over just working [https://emmanuelvalverderamos.substack.com/p/collaborative-work-over-just-working](https://emmanuelvalverderamos.substack.com/p/collaborative-work-over-just-working)
- Acceptance testing, more than tests [https://emmanuelvalverderamos.substack.com/p/acceptance-testing-more-than-tests](https://emmanuelvalverderamos.substack.com/p/acceptance-testing-more-than-tests)
- Subcutaneous acceptance tests, verifying behavior below the UI [https://emmanuelvalverderamos.substack.com/p/subcutaneous-acceptance-tests-verifying](https://emmanuelvalverderamos.substack.com/p/subcutaneous-acceptance-tests-verifying)
- Exploring testing strategies, past and present [https://emmanuelvalverderamos.substack.com/p/exploring-testing-strategies-past](https://emmanuelvalverderamos.substack.com/p/exploring-testing-strategies-past)
- Test Driven Development, the basics [https://emmanuelvalverderamos.substack.com/p/test-driven-development-the-basics](https://emmanuelvalverderamos.substack.com/p/test-driven-development-the-basics)
- Mockist TDD, just enough design [https://emmanuelvalverderamos.substack.com/p/mockist-tdd-just-enough-design](https://emmanuelvalverderamos.substack.com/p/mockist-tdd-just-enough-design)

**Related articles**

- Codesai, Mockist TDD, the unit is not the class [https://codesai.com/posts/2025/03/mockist-tdd-unit-not-the-class](https://codesai.com/posts/2025/03/mockist-tdd-unit-not-the-class)
- Codesai, Isolated tests mean different things to different people [https://codesai.com/posts/2025/06/isolated-test-something-different-to-different-people](https://codesai.com/posts/2025/06/isolated-test-something-different-to-different-people)
- Codesai, Heuristics to determine unit boundaries [https://codesai.com/posts/2025/07/heuristics-to-determine-unit-boundaries](https://codesai.com/posts/2025/07/heuristics-to-determine-unit-boundaries)

**Supporting ideas and quotes**

- Martin Fowler, Frequency Reduces Difficulty [https://martinfowler.com/bliki/FrequencyReducesDifficulty.html](https://martinfowler.com/bliki/FrequencyReducesDifficulty.html)
