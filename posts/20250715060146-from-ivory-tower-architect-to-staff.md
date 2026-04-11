---
title: "From “Ivory Tower Architect” to Staff & Principal Engineer"
subtitle: "How a useful role became a distorted job title and what’s replacing it"
requested_url: "https://emmanuelvalverderamos.substack.com/p/from-ivory-tower-architect-to-staff"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/from-ivory-tower-architect-to-staff"
substack_post_id: 168232113
retrieved_at: "2026-04-11T07:47:43.593Z"
---
# From “Ivory Tower Architect” to Staff & Principal Engineer

### How a useful role became a distorted job title and what’s replacing it

[![](https://substackcdn.com/image/fetch/$s_!ifUE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67411a03-1bae-49cb-98e0-3d7f3524bf1b_4272x2848.jpeg)](https://substackcdn.com/image/fetch/$s_!ifUE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67411a03-1bae-49cb-98e0-3d7f3524bf1b_4272x2848.jpeg)

### Introduction: Defining the architect's role

> “The primary role of an architect is to ride the elevator between the penthouse and the engine-room, stopping wherever the work needs help.”

> — Gregor Hohpe [martinfowler.com](https://martinfowler.com/articles/architect-elevator.html?utm_source=chatgpt.com)

That image resonates because many teams still receive diagrams from on high that never meet the code. Yet when **Frederick P. Brooks** coined the term "*system architect”* in 1975, he was naming a **responsibility**, not a position: preserve a product’s **conceptual integrity**, the design choices that are hardest and costliest to change. **Grady Booch** later refined the idea:

> “All architecture is design but not all design is architecture. Architecture represents the significant design decisions that shape a system, where significant is measured by cost of change.” [Wikiquote](https://en.wikiquote.org/wiki/Grady_Booch?utm_source=chatgpt.com)

From the outset, then, the “*architect”* was a hat any engineer might wear when those decisions surfaced.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### Origins of the term

*How three decades turned a rotating hat into a headline on job ads.*

[![](https://substackcdn.com/image/fetch/$s_!GGag!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f6862f2-b187-4e2f-bfea-2cd6c4cd13ea_3339x680.png)](https://substackcdn.com/image/fetch/$s_!GGag!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f6862f2-b187-4e2f-bfea-2cd6c4cd13ea_3339x680.png)

In **1975,** Frederick P. Brooks published *The Mythical Man-Month*. The book introduced the idea of **conceptual integrity**, the principle that a system needs a single coherent vision. By presenting this as a responsibility rather than a management layer, Brooks set the stage for treating architecture as a cross-cutting concern owned by the whole team, not a top-down hierarchy.

In **1992,** David E. Perry and Alexander L. Wolf released “Foundations for the Study of Software Architecture,” the first formal academic framework for thinking about architecture. The paper assumed teams would *assign* an architect role when necessary, reinforcing the view that architectural work is a deliberate, shared practice.

Between **1991 and 1996,** Grady Booch published *Object-Oriented Analysis and Design* and later *Object Solutions*. Booch tied architectural effort directly to the **cost of change**, arguing that the most expensive decisions deserve the most architectural attention. His writing kept ownership of those decisions within the development team and encouraged architects to remain hands-on with code.

Finally, in **1999,** Ivar Jacobson, Grady Booch, and James Rumbaugh introduced *the Unified Software Development Process*. By embedding an **architecture-centric, iterative** approach and insisting that every iteration produce an executable baseline, they popularised architecture as an ongoing, team-wide activity rather than a one-off deliverable handed down from above.

*Takeaway:* *Software architect* hardened only in the mid-1990s, and still meant *shared responsibility* rather than a permanent seat.

### Semantic diffusion: role → job title → ivory tower

**Martin Fowler** calls the blurring of once-precise terms **semantic diffusion** [martinfowler.com](https://martinfowler.com/bliki/SemanticDiffusion.html?utm_source=chatgpt.com). Three forces accelerated it here:

- **Career-ladder pressure**: companies needed senior titles; the *Architect* became a promotion badge.
- **Recruiter shorthand**: job ads equated “Architect” with “10 years’ experience,” ignoring practice.
- **Broken feedback loops**: permanent architects drifted from code, dictating standards. InfoQ now lists the *Ivory-Tower Architect* as an anti-pattern [InfoQ](https://www.infoq.com/news/2023/01/ivory-tower-architects/?utm_source=chatgpt.com).

**Kent Beck** saw the drift early. In *Extreme Programming Explained,* he recalls suggesting stress-first coding to an architect who replied, “I spend all my time writing specifications and then explaining them to developers.” [Goodreads](https://www.goodreads.com/author/quotes/25211.Kent_Beck?page=2&amp;utm_source=chatgpt.com)
Exactly the behaviour XP meant to abolish.

*Myth vs Fact*

- **Myth:** “Architects don’t code.”
- **Fact:** Modern senior-IC (IC = Individual Contributors) ladders *require* periodic coding to stay credible.

### Modern successors: staff, tech lead, and principal engineers

[![](https://substackcdn.com/image/fetch/$s_!9gw9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1f60095-9ac8-4158-95b5-1268ba46dd5a_816x256.png)](https://substackcdn.com/image/fetch/$s_!9gw9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1f60095-9ac8-4158-95b5-1268ba46dd5a_816x256.png)

Fowler describes these senior ICs as living **“on the architect elevator,”** connecting boardroom strategy to ground-floor code [martinfowler.com](https://martinfowler.com/articles/architect-elevator.html?utm_source=chatgpt.com).

### Shared architectural ownership and shift-left

Teams reinforce shared ownership through **shift-left**, moving quality, security, **and architecture** as early as possible, so feedback arrives when change is cheap. Larry Smith coined “shift-left testing” in 2001 to capture that idea.

- **Collective design reviews** (Fowler’s “fitness functions”) catch drift before it ossifies, [martinfowler.com](https://martinfowler.com/articles/branching-patterns.html?utm_source=chatgpt.com).
- **Executable architecture baselines** from the Unified Process keep diagrams honest against running code.
- **Hands-on Staff, Tech Lead, and Principal ICs** code in the risky seams, realising Beck’s *emergent design* ideal.

Shift-left strengthens cohesion, coherence, and coordination **without** creating a single point of failure, precisely the opposite of the ivory-tower model.

### Conclusion

[![No hay descripción alternativa para esta imagen](https://substackcdn.com/image/fetch/$s_!wSH-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5f1b8b4-f826-4c37-a62e-a9787098d5aa_1024x1024.jpeg)](https://substackcdn.com/image/fetch/$s_!wSH-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5f1b8b4-f826-4c37-a62e-a9787098d5aa_1024x1024.jpeg)

[Architect rol evolution](https://www.linkedin.com/posts/lucamezzalira_architecture-architects-distributedsystems-activity-7354091225693495296-DlY8?utm_source=share&amp;utm_medium=member_desktop&amp;rcm=ACoAAB5jkFMBPbyiDHq7f5BzW_sEAWGbq9DPAh8)

In **2025,** the term “software architect” still appears on EU job boards, but semantic diffusion has stretched it thin. Before you post or accept that title, ask:

*Will this person ride the elevator, tighten feedback loops, and code at the risky seams, or will they vanish into the penthouse?*

If the answer is the latter, you don’t need an architect; you need **shared ownership, clear expectations, and shift-left feedback loops**. Roles evolve; responsibilities endure.

In 2025, unfortunately, there are still many companies where the role of Software Architect or Solution Architect remains that of the "ivory tower" architect. Sadly, I believe this is not only due to semantic diffusion, but also because of the way some companies and sectors operate, as well as the mindset of many individuals who have held the role for a while and believe their job is simply to tell others what to do.

Despite this article and many others pointing out that the role is evolving, this evolution is happening slowly and at a sluggish pace, in stark contrast to the latest front-end framework or whatever new trend emerges in AI.

I believe change is hard, but what surprises me is how change often seems harder for the things that don’t matter to us too much than for the things we simply enjoy or like.

---

### References

- Brooks, F. P., *The Mythical Man-Month*, 1975, [Wikipedia](https://en.wikipedia.org/wiki/The_Mythical_Man-Month?utm_source=chatgpt.com)
- Booch, G., quote in *Handbook of Software Architecture* [Wikiquote](https://en.wikiquote.org/wiki/Grady_Booch?utm_source=chatgpt.com)
- Perry, D. E. &amp; Wolf, A. L., “Foundations for the Study of Software Architecture”, 1992
- Jacobson, I.; Booch, G.; Rumbaugh, J., *The Unified Software Development Process*, 1999
- Fowler, M., “Semantic Diffusion”, 2006 [martinfowler.com](https://martinfowler.com/bliki/SemanticDiffusion.html?utm_source=chatgpt.com)
- Hohpe, G., “The Architect Elevator”, 2017 [martinfowler.com](https://martinfowler.com/articles/architect-elevator.html?utm_source=chatgpt.com)
- InfoQ, “Avoid Being an ‘Ivory-Tower’ Architect”, 2023 [InfoQ](https://www.infoq.com/news/2023/01/ivory-tower-architects/?utm_source=chatgpt.com)
- StaffEng.com, “Staff Archetypes”, 2020 [staffeng.com](https://staffeng.com/faq/?utm_source=chatgpt.com)
- LeadDev, “Being a Tech Lead Doesn’t Mean Having All the Answers”, 2023 [LeadDev](https://leaddev.com/leadership/being-tech-lead-doesnt-mean-having-all-answers?utm_source=chatgpt.com)
- Scriptworks, “Shift-Left Testing”, 2021 [scriptworks.io](https://www.scriptworks.io/blog/shift-left-testing/?utm_source=chatgpt.com)
- StaffEng.com, “What Do Staff Engineers Actually Do?”, 2021 [staffeng.com](https://staffeng.com/guides/what-do-staff-engineers-actually-do/?utm_source=chatgpt.com)
- Fowler, M., “Continuous Integration” (fitness-function discussion), 2024 [martinfowler.com](https://martinfowler.com/articles/branching-patterns.html?utm_source=chatgpt.com)
- Mezzalira, Luca. [https://www.linkedin.com/posts/lucamezzalira_architecture-architects-distributedsystems-activity-7354091225693495296-DlY8](https://www.linkedin.com/posts/lucamezzalira_architecture-architects-distributedsystems-activity-7354091225693495296-DlY8)
