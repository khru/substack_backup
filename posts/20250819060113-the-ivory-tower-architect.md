---
title: "The Ivory Tower Architect"
requested_url: "https://emmanuelvalverderamos.substack.com/p/the-ivory-tower-architect"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/the-ivory-tower-architect"
substack_post_id: 168235318
retrieved_at: "2026-03-14T08:29:45.673Z"
---
# The Ivory Tower Architect

[![](https://substackcdn.com/image/fetch/$s_!lTO8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0311300f-db9c-4203-8c51-352ff263166a_6240x4160.jpeg)](https://substackcdn.com/image/fetch/$s_!lTO8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0311300f-db9c-4203-8c51-352ff263166a_6240x4160.jpeg)

People smells, just like code smells, warn that the social and technical system is under strain. One teammate may exhibit several patterns at the same time. Improvement comes only when the individual accepts the problem. Coaching and structure help, but a team cannot reform someone who refuses to change, and delay multiplies the harm.

### Context, motivation, and close cousins

The Ivory Tower Architect appears where design and implementation are split, feedback loops are weak, and promotion paths reward polished diagrams more than working software.

- Micromanager dictates every commit; the Ivory Tower Architect dictates abstractions, leaving others to fill the gaps.
- Knowledge Kidnapper hoards implementation detail; the Architect hoards design intent.
- Gold Plater adds unnecessary complexity while coding; the Architect adds it during planning.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### Core behaviours

- Produces large reference diagrams with little or no code validation.
- Mandates frameworks “for future-proofing” without evidence of need.
- Avoids pull-request conversations, calling coding “detail work.”
- Updates design documents rather than product backlogs when issues surface.
- Treats questions about the design as resistance instead of feedback.

### Early warning signs

- Discussions begin with “How do we fit this into the diagram?” rather than “What problem are we solving?”
- Pull requests reference architectural rules that nobody can link to user value.
- Documentation grows faster than test coverage.
- Engineers privately mention an “architecture tax” before any release.

### Impact over time

**Short term:** the high-level picture feels reassuring.
**Medium term:** integration pain rises as reality collides with the picture.
**Long term:** delivery slows, diagrams drift from running code, and refactors consume whole quarters.

### Software-economics impact and risks

- Delay cost: Every change must align with the blueprint.
- Maintenance cost: unused layers increase cognitive load.
- Opportunity cost: experiments stall because the architecture is locked.
- Explicit risks: platform coupling, morale loss, framework abandonment.

### Systemic impact

A wall forms between designers and builders. Psychological safety drops because challenging the diagram feels risky. Continuous improvement stalls; energy shifts to navigating doctrine instead of serving users.

### Variants

- Spec Dropper: hands over a thick document, then vanishes.
- Framework Hoarder: mandates proprietary stacks regardless of context.
- Diagram Chaser: redraws boxes each quarter and announces a new “north star.”

### Biases that feed the pattern

- Authority bias: assuming senior architects must be correct.
- Sunk-cost fallacy: clinging to a plan because many hours went into drawing it.
- Confirmation bias: ignoring evidence that contradicts the blueprint.

### Root causes

Promotion criteria tied to presentation skills, missing feedback loops between code and design, and cultures that prize “future-proof” abstractions over incremental learning.

### Detection metrics

- Architect contributes fewer than five percent of commits in the primary code repository.
- Cross-layer change lead time exceeds seven days.
- The percentage of unused classes or services rises release after each release.
- Team survey shows low confidence in explaining why chosen patterns matter.

### Extended example

A banking platform hires Ravi as chief architect. Pair programming, trunk-based development, and automated tests exist in other teams, but Ravi prefers formal design reviews. He mandates a twelve-layer onion, an event bus, and a niche framework. Six months later only two business capabilities are live, performance is poor because each request serialises data four times, and no integration tests run across layers. Developers hack direct database calls to meet quarter-end targets, violating the diagram. Auditors flag the inconsistent patterns and delay regulatory approval, costing two hundred thousand euros in interest on the late launch. Ravi responds by refining the diagram instead of addressing the backlog.

### Mitigation paths

**Individual actions**

- Apply [Never the Expert](https://emmanuelvalverderamos.substack.com/p/never-the-expert-breaking-knowledge): code a small spike in the riskiest area with a peer, then hand ownership to them.
- Capture decisions in one-page architecture decision records.
- Spend one day each sprint pairing with implementers to validate assumptions.

**Team actions**

- Hold regular architecture coffees where any engineer can question decisions.
- Keep diagrams lightweight and version-controlled alongside the code.
- Track cross-layer cycle time and discuss it in retrospectives.

**Organisational actions**

- Recognise architects for lead-time reduction, not diagram complexity.
- Fund short exploratory spikes and discard prototypes that do not prove value.
- Use evolutionary-architecture fitness functions to catch drift early.

### Preventive practices

Incremental design, pair programming, architecture decision records, trunk-based development, and continuous integration keep design and implementation in sync and stop an Ivory Tower from forming.

### TL;DR

An Ivory Tower Architect supplies elegant diagrams that drift from running code, slowing delivery and raising risk. Keep architecture hands-on, share ownership, and integrate feedback. Reward outcomes, not drawings.

### References

- Brooks, Frederick P. *The Mythical Man-Month*.
- Cockburn, Alistair; Garrido de Paz, Juan Manuel. *Hexagonal Architecture Explained: How the Ports and Adapters Architecture Simplifies Your Life, and How to Implement It*.
- Hunt, Andrew; Thomas, David. *The Pragmatic Programmer: Your Journey to Mastery*.
- Skelton, Matthew; Pais, Manuel. *Team Topologies*.
- Wake, William C. *Extreme Programming Explored*.
- Brown, Andrew Richard. *Taming Your Dragon: Addressing Your Technical Debt*.
