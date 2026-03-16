---
title: "🚦 When Platform and Security Become Bottlenecks: A Call for Enabling Culture"
requested_url: "https://emmanuelvalverderamos.substack.com/p/when-platform-and-security-become"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/when-platform-and-security-become"
substack_post_id: 159934750
retrieved_at: "2026-03-16T08:06:14.352Z"
---
# 🚦 When Platform and Security Become Bottlenecks: A Call for Enabling Culture

Disclaimer: this article discusses what poorly implemented DevOps culture looks like, or how some teams—despite changing their name—continue to operate the same way they always have. This does **not** reflect companies or teams that have a healthy and well-established DevOps culture.

In technology-driven organizations, software delivery is critical for reaching customers and generating revenue. Platform, Security, and Integration teams should ideally **act as enabling teams**: empowering others by identifying challenges, reducing cognitive load, and providing practical tools, patterns, and practices that accelerate value delivery.

🔍 **What is an enabling team?**
According to *Team Topologies*, an enabling team is a team of specialists who help a stream-aligned team (or multiple teams) overcome obstacles. They **do not own long-term delivery responsibility**. Instead, they **act as coaches, mentors, and enablers**, transferring knowledge, improving practices, and helping teams build autonomy in areas like testing, observability, security, and infrastructure. Their success is defined by how well they help other teams succeed.

*> If an enabling team does its job well, the team that it is helping should no longer need the help from the enabling team after a few weeks or months.* – *Team Topologies*

However, these enabling teams frequently become unintended bottlenecks. ⚠️ **They impose rigid solutions, set inflexible requirements without context, or fail to make necessary decisions altogether**, **creating confusion and frustration**. This dysfunction reflects the "ivory tower" anti-pattern in architecture: isolated decision-makers without accountability or feedback loops.

This situation can also resemble what Alfredo Artiles describes as an escalation trap, drawing from Donella Meadows' systems thinking. This occurs when teams, such as Development and Platform (or misnamed "DevOps" teams), continuously push against each other in a competitive rather than collaborative manner. Each team's reactive actions intensify pressure on the other, creating a destructive spiral that ultimately harms both teams and organizational health.

[![](https://substackcdn.com/image/fetch/$s_!RyBr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e7fcbf6-a955-44fd-bf04-874d544396ae_470x650.jpeg)](https://substackcdn.com/image/fetch/$s_!RyBr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e7fcbf6-a955-44fd-bf04-874d544396ae_470x650.jpeg)

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## 🤝 Enablement vs. Control

In a healthy DevOps culture, enabling teams aim to reduce friction. As stated in *The DevOps Handbook*, “QA, IT Operations, and InfraSec are always working on ways to reduce friction for the team, creating the work systems that enable developers to be more productive and get better outcomes.” 📚

Yet, when platform or security teams only prescribe "what must be done," without empathy, collaboration, or accountability for outcomes, they increase friction. Product teams pay the price through delays, broken workflows, and decreased morale. 😓

## 📉 The Consequences of Disconnection

Luis Artola, in *Software Economics*, emphasizes that “software development is primarily a human activity,” making communication and alignment critical. Decisions lacking collaboration and empathy drastically raise costs and risks downstream.

Disconnected enabling teams cause:

- 🚨 **Loss of trust** among delivery teams.
- ⏳ **Delayed feedback cycles**, finding problems too late.
- 🔒 **Compliance over curiosity**, stifling innovation.
- 🛠️ **Technical debt** disguised as "security" or "standards."

These issues are measurable—seen through longer lead times, increased rework, and team disengagement. 📊

A system experiencing such bottlenecks would feel:

- 🐢 **Slow and heavy** due to delayed decisions and blocked flows.
- ⚠️ **Anxious and insecure** from uncertainty and disconnected mandates.
- 😣 **Frustrated and demotivated** because imposed requirements lack contextual empathy.
- 🔗❌ **Fragmented and isolated** as collaboration deteriorates.
- 😩 **Stressed and overloaded** when teams carry responsibilities without adequate support.
- 🌵 **Rigid and fragile** from inflexible processes, reducing adaptability.

## 🔄 Shift Left, But with Empathy

The "Shift Left" approach highlights addressing issues early in the development process. But pushing security or integration responsibilities onto teams without adequate support is abandonment, not empowerment. ❌

As *The DevOps Handbook* notes, “Instead of security and compliance activities only being performed at the end of the project, controls are integrated into every stage of daily work... resulting in better quality, security, and compliance outcomes.” 🔐

However, real empowerment doesn’t stop at shifting responsibility—it requires **support, trust, and capability-building**. As described in Lean Software Development and modern platform thinking, **enabling teams** should **partner** with product teams, **not prescribe** to them. Empowerment means equipping teams to take ownership—from discovery to delivery and operation—within a value stream they can fully influence.

If a team is expected to "own security" or "own performance," it must be equipped and supported to truly do so—with observability, training, architectural autonomy, and clarity of purpose. Otherwise, we’re just **shifting blame left, not capability**.

🎯 A healthy enabling team **amplifies flow**, accelerates learning, and disappears when no longer needed. Their impact isn’t in owning deliverables—but in unlocking the potential of other teams to own theirs.

In empowered teams, *"You build it, you run it"* isn't just a slogan—it’s an architectural and cultural commitment. This means platform and security teams must focus on **removing friction**, not adding checkpoints.

**A healthy "Shift Left" includes:**

- 🛠️ Building self-service tools that reduce dependency and waiting.
- 🧭 Co-designing guardrails and patterns with the teams that use them.
- 🤝 Rotating roles and creating joint support or champion programs to close empathy gaps.
- 🧪 Encouraging technical experiments and feedback-driven evolution.

If a team is expected to "own security" or "own performance," it must be equipped and supported to **truly do so**—with observability, training, architectural autonomy, and clarity of purpose. Otherwise, we’re just shifting blame left, not capability.

## 📈 Software Economics: Risk and Return

In economics, risk is defined as the mismatch between expected and actual outcomes. When enabling teams mandate processes disconnected from delivery teams' needs or customer goals, systemic risk increases. 📉

Luis Artola clearly states: “The risk of a software investment is directly related to how far the design is from the actual needs of the users.” 🎯 This principle applies equally to internal platforms and security frameworks. Poorly aligned investments yield negative ROI, wasted effort, and lost market opportunities.

## 🌟 The DevOps Culture: From Control to Genuine Collaboration

DevOps extends beyond automation; it involves cultural shifts toward transparency, ownership, and learning. High-performing teams integrate QA, security, and operations into development, measuring success by outcomes, not control.

Genuine collaboration, inspired by Patrick Lencioni’s principles, involves humility, hunger for contribution, and emotional intelligence. 💬 Enabling teams must:

- 🔍 Embed closely with product teams to grasp their context and workflows.
- 🛠️ Provide practical tools rather than rigid rules.
- ⚙️ Automate for consistency and ease of use, not merely enforcement.
- 📋 Clearly define roles and responsibilities to prevent confusion and indecision.
- 🙌 Treat internal teams as valued customers, adapting based on their feedback.
- 🔗 Embrace shared accountability for delivery outcomes.

As outlined in *The DevOps Handbook* and *Team Topologies*, enabling teams should operate as product teams themselves—**discovering real needs, delivering incrementally**, and validating effectiveness through feedback loops. 🚀

✅ When enabling teams behave like **coaches instead of controllers**, they foster trust, capability, and autonomy. When they act like **owners of decisions with no skin in the outcome**, they erode collaboration and increase systemic risk.

## ⚡ Agility and Enablement Vs Rigid processes

Agility isn't just about speed—it's about responsiveness, adaptability, and collaborative flow. If platform and security teams are becoming bottlenecks, the organization isn't genuinely agile. True agility involves:

🔄 Rapid feedback loops enabling quick learning and adjustments.
🤝 Cross-functional collaboration, fostering empathy and collective intelligence.
🚦 Empowering decision-making, rather than hierarchical approvals.
🌱 Continuous improvement as a mindset rather than an afterthought.

These aren’t just agile buzzwords—they are core enablers of what John Cutler calls **Product Teams**: teams that don’t merely execute, but **discover, solve, and deliver meaningful impact**.

To achieve this, platform and security teams must:

- 🎧 Listen to internal users as customers.
- 💡 Optimize for *flow* instead of *enforcement*.
- 🔍 Help product teams learn faster, deploy safer, and own more.

Without this, agility becomes theater: teams go through the motions of “DevOps” or “Agile” but are still bound by slow, centralized decisions and unclear ownership.

## ✅ Practical Steps for Cultivating an Enabling Culture

To move towards genuine collaboration and away from command-and-control bottlenecks, consider these actionable steps:

- 🎯 **Set Clear Shared Objectives**: Ensure goals are aligned across teams to foster collective ownership.
- 👥 **Cross-team Embedding**: Regularly embed platform and security team members within product teams to build empathy and context.
- 🔄 **Establish Feedback Loops**: Create automated and manual feedback mechanisms to continually adapt and refine solutions.
- 🛠️ **Promote Self-Service**: Offer robust self-service platforms that empower teams to safely innovate independently.
- 📖 **Document with Clarity and Context**: Maintain clear, context-rich documentation that explains "**why**," not just "what" and "how."
- 📊 **Measure Impact Transparently**: Regularly review and share metrics that reflect collaboration, efficiency, and overall satisfaction.
- 📚 **Train for Product Thinking: **Not all engineers come with a product mindset. Enabling teams can **accelerate this shift by mentoring**, offering training, and helping teams connect delivery with user impact.
- 🏗️ **Build Capabilities, Not Just Policies: **Enabling teams succeed when they **build capacity within others**, not when they centralize knowledge. Instead of saying “do X for security,” they **enable teams to understand X, apply it pragmatically, and adapt it as needed.**

The simplest way to start is by evaluating the “**as is**” and the “**status quo**”, and understanding how things are and why they are that way. Once you’re able to grasp that, talk to your colleagues from other teams—understand their pain points, learn what hurts them the most, and propose alternative solutions. Build the work together, understanding that what you’re trying to solve isn’t what *you* think is important, but what is important to your stakeholders. For teams like Platform, Infrastructure, Systems, Security, DevSecOps, QA, etc., the stakeholders is also the development team.

Once you understand this, build the “**to be**” with them creating a roadmap, based on the needs of your stakeholders. If you don’t, you’re likely telling others how they should work—and that can cause a lot of problems, as we’ve already mentioned.

# 🔐 **Manifesto for DevSecOps**

We are uncovering better ways of **delivering secure, resilient, and valuable systems**
by doing it and helping others do it.
Through this work, we have come to value:

- **Individuals, interactions, and shared responsibility **over rigid processes, tools, or silos
- **Secure, working systems that deliver real value **over excessive documentation or theoretical perfection
- **Customer, developer, and security collaboration **over contract negotiation and control gates
- **Pragmatic resilience and adaptability **over rigid plans or checkbox-driven compliance

That is, while there is value in the items on the right, **we value the items on the left more.**

Ultimately, **platform and security teams are most successful not when they enforce the most standards—but when they enable the most autonomy without sacrificing quality**.

A great enabling team knows when to **step in to guide**, and when to **step away to let others grow**. Their role isn’t to build more control—it’s to build more trust, competence, and shared ownership.

## 🔑 **Principles Behind the DevSecOps Manifesto**

We follow these principles:

- **Our highest priority is to deliver continuous, secure value** through systems that are safe, observable, and purpose-driven.
- **Security is a shared, embedded responsibility**, not a blocker. It must **balance risk, speed, and business impact**.
- **Working systems are only valuable if they’re secure, usable, and aligned with real customer needs**—not abstract checklists.
- **Infrastructure, policies, and controls are code**—they evolve, are tested, and are improved like any product feature.
- **We welcome changing requirements**—including threats, compliance needs, or customer priorities—as part of our reality.
- **We deliver secure, valuable systems frequently**, with fast feedback cycles to allow for learning and course correction.
- **Business, development, security, and operations collaborate continuously**, treating each other as peers, not gatekeepers.
- **We build around motivated and trusted people**, giving them tools, context, and autonomy to make good decisions—technically *and* strategically.
- **Face-to-face conversation (or high-bandwidth remote communication)** is the most effective way to solve complex, multi-disciplinary problems.
- **Secure and resilient value delivery** is our core measure of progress—not just output, but sustainable outcomes.
- **We work at a sustainable pace**, enabling delivery teams to balance innovation, incident response, and long-term improvement.
- **We pursue technical excellence, good design, and secure defaults**—but never in a vacuum. Everything must tie back to value and risk.
- **Simplicity is essential**—not just in design, but also in processes and controls. Complexity is a liability.
- **The best solutions emerge from empowered, cross-functional teams** who are close to the problem and the user.
- **We continuously reflect, adapt, and learn**—optimizing not just security posture or delivery speed, but how well we serve real-world needs.
- **We are pragmatists**. We embrace trade-offs, optimize for impact, and understand that **perfect security with zero delivery is failure**.

## 🎯 Closing Thoughts: A Question of Value

Every enabling team must honestly ask:

**Are we genuinely making it easier for our teams to succeed—or are we unintentionally obstructing them?** ❓

Building platforms, establishing security standards, and developing integration pipelines are necessary. But if these efforts do not enable faster, safer, and more confident software delivery, they become obstacles. 🚧 The cost of such misalignment isn’t just internal—it impacts customers, market position, and long-term sustainability. 🌱.

Ultimately, platform and security teams are successful not when they enforce the most standards—but when they enable **the most autonomy** without sacrificing quality and extra work for the rest of the teams.

---

**📚 References:**

- Kim, Gene., Humble, Jez., Debois, Patrick., Willis, John. *The DevOps Handbook*.
- Artiles, Alfredo. *El «equipo DevOps» y la trampa de la escalada*.
- Ferro, Edu. *Lean Software Delivery: Empowering the Team*
- Artola, Luis. *Software Economics*.
- Lencioni, Patrick. *The Ideal Team Player*.
- Allspaw, John. *The High-Velocity Edge*.
- Cunningham, Ward. *The WyCash Portfolio Management System*.
- Goldratt, Eliyahu M. *The Goal*.
- Meadows, Donella H. *Thinking in Systems*.
