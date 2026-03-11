---
title: "The Gold-Plater or Over-Engineer"
requested_url: "https://emmanuelvalverderamos.substack.com/p/the-gold-plater-or-over-engineer"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/the-gold-plater-or-over-engineer"
substack_post_id: 168236019
retrieved_at: "2026-03-11T08:35:27.727Z"
---
# The Gold-Plater or Over-Engineer

[![](https://substackcdn.com/image/fetch/$s_!7SMZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c9d3866-9bb0-4989-895d-5375b5604c3a_2667x1830.jpeg)](https://substackcdn.com/image/fetch/$s_!7SMZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c9d3866-9bb0-4989-895d-5375b5604c3a_2667x1830.jpeg)

People smells, like code smells, flag hidden stress in a team. A single teammate can combine several patterns. Change begins only when the individual admits the issue. Coaching and structure help, but a team cannot reform someone who refuses to adapt; delay multiplies the harm.

### Context, motivation, and close cousins

The Gold-Plater appears when engineers value elegance or novelty over user value. Organisations that celebrate technical “cleverness” and set vague success criteria encourage extra layers for “future proofing”.

Close cousins and how they differ

- Hero seeks a crisis to solve, while the Gold-Plater creates complexity before a crisis exists.
- Cowboy ignores standards, whereas the Gold-Plater adds standards on standards.
- NIH Zealot rejects external tools; the Gold-Plater overloads internal code with patterns regardless of context.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### Core behaviours

- Introduces microservices, CQRS, or event sourcing for simple CRUD features.
- Refactors working code into elaborate abstractions without a failing test as trigger.
- Suggests new frameworks each quarter, arguing “we will need it soon”.
- Writes factory builders, base classes, and generic layers no user story demands.
- Optimises performance in paths that are not on any profiling report.

### Early warning signs

- Pull requests double in size with “scaffolding for future extensions”.
- Sprint review demos show infrastructure work while user stories slip.
- Stand-up comments include “I future-proofed it” more often than “I delivered value”.
- Test coverage drops because helpers become harder to wire.

### Impact over time

- **Short term**: The team feels intellectually stimulated by shiny architecture.
- **Medium term**: cognitive load rises; onboarding slows; bugs appear in seldom-used layers.
- **Long term**: velocity drops, maintenance cost soars, and refactoring becomes risky because dependencies multiply.

### Software economics and risks

- Delay cost: extra abstractions push delivery dates.
- Maintenance cost: Every new layer must be updated during changes.
- Opportunity cost: features lag while engineers polish internals.
- Explicit risks: Over-engineered systems fail to meet evolving business needs.

Martin Fowler reminds us in “YAGNI” that building for hypothetical futures often wastes time and hides defects.

### Systemic impact

Over-engineering shifts the conversation from outcomes to technology fashion. Product managers lose trust, and engineers who value simplicity become disengaged. Technical debt accrues in the form of “architecture debt” that nobody wants to simplify.

### Variants

- Framework-Crafter: starts an internal platform instead of using a library.
- Pattern-Collector: applies every GoF pattern in one module.
- Premature-Optimizer: micro-optimizes code paths without benchmarks.

### Biases that feed the pattern

- Overconfidence bias: believing one can predict future requirements.
- Novelty bias: overvaluing the new and underestimating maintenance.
- Survivorship bias: citing success stories of complex systems while ignoring simpler wins.

### Root causes

Reward systems that prize innovation over impact, lack of lightweight architecture review, unclear acceptance criteria for “done”, and leadership admiration for technical grandstanding.

### Detection metrics

- The ratio of engineering hours spent on infrastructure vs user stories exceeds fifty percent.
- The number of unused interfaces or layers grows release after release.
- Lead time for small changes increases despite team maturity.
- Post-mortems cite hidden complexity as the root cause more than twice per quarter.

### Extended example

A health-tech start-up sells an appointment booking tool. Lara, a senior engineer, insists on splitting the simple monolith into ten microservices “before traffic grows”. Pair programming, trunk-based development, and tests exist, but Lara pauses them to scaffold a Kubernetes cluster. The first deployment takes three weeks and budgets triple. Developers spend entire sprints wiring service meshes. Meanwhile, a competitor ships a usable dashboard and captures market share. Eight months later, investors question why the codebase has ninety pods but only half the planned features. The company hires consultants to merge several services back into one, costing one hundred and ten thousand euros.

### Mitigation paths

Individual actions

- Practice [Never the Expert](https://emmanuelvalverderamos.substack.com/p/never-the-expert-breaking-knowledge) by pairing on real user stories before suggesting abstractions.
- Use the “two-story rule”: do not generalise code until a second feature needs it.
- Run production profiling before any performance rewrite.

Team actions

- Define a “YAGNI gate” in pull-request templates: the author states the current user story that requires each abstraction.
- Keep a lightweight architecture council with rotating membership to review large proposals.
- Measure cycle time; if it rises after an engineering investment, hold a learning review.

Organisational actions

- Tie performance reviews to delivered customer value, not framework count.
- Allocate explicit spike budgets and cancel spikes that fail to prove benefit.
- Provide mentoring on evolutionary architecture so teams learn to grow designs incrementally.

### Preventive practices

Test-driven development, incremental design, domain-driven discovery workshops, and regular retrospectives about cognitive load help teams resist gold-plating. Continuous delivery pipelines expose the cost of extra layers quickly, steering decisions toward simplicity.

### TL;DR

The Gold-Plater adds shiny complexity to solve tomorrow’s problems today, slowing delivery and inflating cost. Apply YAGNI, share design responsibility, and reward value delivered to keep engineering lean and adaptable.

### References

- Beck, Kent. *Extreme Programming Explained: Embrace Change*.
- Hunt, Andrew; Thomas, David. *The Pragmatic Programmer: Your Journey to Mastery*.
- Skelton, Matthew; Pais, Manuel. *Team Topologies*.
