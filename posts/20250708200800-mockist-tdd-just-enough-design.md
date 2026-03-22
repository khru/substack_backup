---
title: "Mockist TDD: Just enough design"
requested_url: "https://emmanuelvalverderamos.substack.com/p/mockist-tdd-just-enough-design"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/mockist-tdd-just-enough-design"
substack_post_id: 164630204
retrieved_at: "2026-03-22T08:29:17.228Z"
---
# Mockist TDD: Just enough design

In software development, we often swing between two extremes. On one side, we overdesign up front, trying to predict the future. On the other hand, we skip design entirely, jumping straight into code and hoping it will "emerge." The problem is, both approaches fail in practice.

**Just Enough Design** is the balance. It’s not about guessing everything. It’s not about flying blind either. It’s about designing the minimum needed to move forward with clarity and confidence.

Let’s look at what that means in a real case: building a robot-cleaning system for office spaces.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## It starts with identifying Actors, Roles, and Actions

[![](https://substackcdn.com/image/fetch/$s_!5uus!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41318dde-4904-46ed-bafd-4eb14dc05abc_939x668.png)](https://substackcdn.com/image/fetch/$s_!5uus!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41318dde-4904-46ed-bafd-4eb14dc05abc_939x668.png)

Before writing a single line of code, we started by visualizing how people and systems actually interact. We used **Domain Storytelling**, a technique that captures key roles, actions, and sequences using icons and arrows. No tech jargon, no code, just stories.

It helped answer essential questions:

- Who triggers the process?
- What are they trying to achieve?
- What steps happen, and in what order?

In our case, we learned that:

- The main actor is a *Cleaner*.
- The goal is to clean a specific workspace area.

This shared story aligned everyone, domain experts, developers, and designers around the same goal. It gave us a foundation to start designing intentionally.

## From Actors, Roles, and Actions to how the system will communicate and the responsabilities each part will have

To understand the problem we want to solve, we need to think carefully about how to build the system. With just enough design planning, we can identify the actors and map out how they should communicate with each other, allowing us to create something like this.

With the process mapped out, we moved on to **UML diagrams**, not as documentation, but as a tool to think clearly.

We focused on **sequence diagrams** to visualize behavior and dependencies:

- Who calls what?
- What messages are exchanged?
- Where are the system boundaries?

[![](https://substackcdn.com/image/fetch/$s_!CYV3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F393102e8-0ea5-4400-9c58-4809485d549b_4741x2262.png)](https://substackcdn.com/image/fetch/$s_!CYV3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F393102e8-0ea5-4400-9c58-4809485d549b_4741x2262.png)

This is where you think about the basics: the actors, their interactions, the messages passed between them, and what kind of relationships they will have.

[![](https://substackcdn.com/image/fetch/$s_!jsI7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa937c318-23ad-45d3-bcca-36c259c4eb31_4741x2262.png)](https://substackcdn.com/image/fetch/$s_!jsI7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa937c318-23ad-45d3-bcca-36c259c4eb31_4741x2262.png)

These diagrams will force you to think about the system you're trying to build. They don't take much time and can be modified at any point. The goal is to understand what you need and guide your design process.

Another solution for this case could be CRC cards instead of UML.

[![](https://substackcdn.com/image/fetch/$s_!a6yA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1934355e-8c10-47d7-bd3b-7b1b6854eab7_1380x860.png)](https://substackcdn.com/image/fetch/$s_!a6yA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1934355e-8c10-47d7-bd3b-7b1b6854eab7_1380x860.png)

[![](https://substackcdn.com/image/fetch/$s_!WOZX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff7c9c45-95d8-4212-b404-8e4d3056afab_7402x3216.png)](https://substackcdn.com/image/fetch/$s_!WOZX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff7c9c45-95d8-4212-b404-8e4d3056afab_7402x3216.png)

# Key tactics that made this possible

We didn’t rely on luck or intuition. We used a clear set of **deliberate tactics** to apply **Just Enough Design**:

✔ **Domain Storytelling/Event Storming**: to understand what is happening, and identify actors and roles
✔ **UML Sequence diagrams**: To identify communications in the system and contracts
✔ **CRC Cards or UML class diagrams**: To identify responsibilities and communications in the system

This toolkit gave us just enough structure to know what we expect, how our system will interact with each other to achieve the task at hand.

# Final thoughts

**Just Enough Design** is not about designing less. It’s about designing *intentionally*. You don’t need architecture diagrams on every wall, but you do need shared understanding, clean interfaces to know how the system will communicate, and clear responsibilities.

> “Extremes are bad. We are going from BDUF (Big Design Up Front) to no design at all.”

> - Sandro Mancuso

## Why “Just Enough” Keeps Shifting

Software’s superpower is its low cost of change. We can ship, learn, and pivot faster than any physical discipline, but that agility punishes guesswork done too far in advance. A sketch drawn in month 1 may be irrelevant by month 6.

So the practical question is **not** “design up front or nothing?” but:

**> How much design do we need *****today***** to move forward with confidence while keeping the door open for tomorrow’s surprises?**

That amount changes as knowledge grows. On day 1, it might be minutes; in month 12, it could be a few hours spread across refactors, whiteboard sessions, and architecture spikes.

### Refactoring shapes the Real Design

Up-front sketches set the initial angle, but **most of the final design emerges through continual refactoring**, closing the gap between what the code says today and what we learned yesterday. And this happens every TDD cycle.

### Balancing the debate on extremes

> “Extremes are bad. We are going from BDUF (Big Design Up Front) to no design at all.”
> Sandro Mancuso

Sandro warns about pendulum swings; Javi reminds us that radical moves can ignite progress. Both views can coexist:

- **Breakthroughs** often start with extremes (think test-first in the early 2000s).
- **Sustainable delivery** needs an adaptable middle path: just enough design every day, refreshed continually.

 Share this comment on the post, I fully agree with this opinion in. That’s why I’ve updated the post.

[![](https://substackcdn.com/image/fetch/$s_!k9Qp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feeb6bbaa-5c17-467b-b202-e06e5f8d081c_688x269.png)](https://substackcdn.com/image/fetch/$s_!k9Qp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feeb6bbaa-5c17-467b-b202-e06e5f8d081c_688x269.png)

[![](https://substackcdn.com/image/fetch/$s_!LAw2!,w_56,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f614ac4-f17a-4cf4-bc01-eedb89699530_96x96.jpeg)](https://javil.substack.com/p/how-much-upfront-design-is-enough-379f51345572?utm_source=substack&amp;utm_campaign=post_embed&amp;utm_medium=web)
