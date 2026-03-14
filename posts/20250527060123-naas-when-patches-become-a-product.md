---
title: "❌ ÑaaS: when patches become a product"
subtitle: "The cultural, economic, and technical cost of selling software illusions"
requested_url: "https://emmanuelvalverderamos.substack.com/p/naas-when-patches-become-a-product"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/naas-when-patches-become-a-product"
substack_post_id: 162686688
retrieved_at: "2026-03-14T08:29:53.436Z"
---
# ❌ ÑaaS: when patches become a product

### The cultural, economic, and technical cost of selling software illusions

### Introduction

[![](https://substackcdn.com/image/fetch/$s_!I2Uw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8fe4610-57ee-4e76-9a7a-d11486636dae_4822x6461.png)](https://substackcdn.com/image/fetch/$s_!I2Uw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8fe4610-57ee-4e76-9a7a-d11486636dae_4822x6461.png)

Not all software is built to last. Some of it isn’t even built to work. In the grey zone between delivery and deception lives a growing industry practice: packaging quick fixes and broken design as if it were meaningful progress. This is **ÑaaS** - *Ñapa as a Service*.

Born out of satire, ÑaaS is disturbingly real. It refers to a delivery model where the *ñapa*, a cheap workaround, hack, or patch, becomes the default way of working. Wrapped in Jira tickets, sprint demos, and superficial agility, these patches masquerade as value while silently corrupting the system.

But this isn’t just a question of poor craftsmanship. It’s a matter of **software economics**: how irreversible decisions, cost asymmetry, and long-term value are ignored in favor of short-term optics.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### What is a ñapa?

In Spanish slang, a *ñapa* is an improvised fix, a poorly planned, badly executed patch that pretends to solve a problem. In code, it looks like this:

- Stacking conditionals to “just make it work”
- Avoiding tests because “we’ll clean it up later”
- Saying “yes” to change without assessing consequences

> “In computing, it is said to be the poorly paid and worse executed job, which consists of constructing a simulation of what the customer expects to see, with the minimum effort, and totally removed from what a healthy mind would consider appropriate.”

*> - ÑaaS, Calidad y software*

A ñapa is not a mistake. It’s a *strategy*, a way to pretend progress has been made, when in fact, fragility has been added.

ÑaaS emerges when this strategy is normalized, scaled, and sold.

---

### The economics of technical bankruptcy

**Luis Artola**, in *Software Economics*, reframes software as a game of managing **irreversible decisions under uncertainty**. The cost of a decision is not just in what it does, it’s in what it prevents us from doing later.

> “The real cost in software does not come from the work done, but from the future options it limits.”

ÑaaS is the embodiment of poor economic judgment. By favoring speed over structure, it:

- Limits reversibility
- Creates invisible coupling
- Pushes cost downstream
- Reduces future design freedom

A patch may “work” today, but it becomes tomorrow’s constraint. That’s not technical debt. That’s **technical bankruptcy**, a place where you can’t change without breaking everything.

[![](https://substackcdn.com/image/fetch/$s_!M_DD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d947212-2fdd-4cdd-94f5-83c825f6a094_500x560.jpeg)](https://substackcdn.com/image/fetch/$s_!M_DD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d947212-2fdd-4cdd-94f5-83c825f6a094_500x560.jpeg)

---

### Why fast is slow (and dirty is expensive)

Every time a team chooses a shortcut instead of a solution, it trades short-term comfort for long-term suffering. Ñapas may feel fast:

- You deliver something visible
- The ticket is closed
- The stakeholder is quiet, for now

But like all fake economies, the bill comes later:

- QA explodes with edge cases
- Onboarding takes weeks because nothing makes sense
- Fixes ripple into regressions
- Refactors get harder and riskier

> 💣 “Every shortcut taken without impact analysis is a delayed explosion.”

*> - TDD by example, adapted*

ÑaaS creates waste disguised as velocity. It’s not delivering value. It’s delivering *problems with a receipt*.

---

### When cruft becomes cultural debt

At some point, poor design stops being a problem, and starts being the norm.

ÑaaS evolves into a culture where:

- Developers fake solutions because “that’s how it’s done here”
- No one questions broken architecture, only deadlines
- Juniors inherit a mess and believe this is what “agile” looks like
- Leaders chase optics, not outcomes

This is how **cultural debt** forms: when dysfunction becomes invisible because everyone’s busy looking busy.

---

### 📉 Complexity, entropy, and the illusion of liquidity

The **economic framing** around software **liquidity**.

Instead of only tracking how much debt (or bad code) exists, the team proposes measuring how *free* a team is to respond to change. This is a subtle but important shift:

> “Debt isn't just the code. It's the reduction in our ability to act.”

A highly indebted codebase may still deliver-but it does so by sacrificing the future. Over time, the **interest payments**, increased friction, slower delivery, cognitive overload, **consume all available capacity**.

In economic terms:

- **Code entropy** = cost of maintaining structure as change increases
- **Liquidity** = how easily we can adapt, validate, or evolve features
- **Technical drag** = cumulative effect of poor abstractions and friction

---

### How ÑaaS violates software economics

Let’s break down the economic crimes of ÑaaS:

[![](https://substackcdn.com/image/fetch/$s_!yFFt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39f9c304-af48-429f-bb5d-84a350bd74fc_1193x521.png)](https://substackcdn.com/image/fetch/$s_!yFFt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39f9c304-af48-429f-bb5d-84a350bd74fc_1193x521.png)

ÑaaS is not just bad engineering. It’s **economically irrational**.

---

### From fake delivery to sustainable change

The opposite of ÑaaS isn’t “slowness”, it’s **clarity**. Teams that want to build real value:

- Assess the impact before implementing
- Allow architecture to emerge from real constraints
- Build feedback loops that expose risk early
- Resist abstracting until repetition proves it necessary (triangulation)
- Invest in refactoring, not post-mortems

Being slow now is often the fastest way to be fast later.

---

## 📜 **Manifesto against ÑaaS**

- We are building better software by choosing clarity, discipline, and intent over shortcuts, illusions, and chaos. Through this commitment, we’ve come to value:
- Sustainable design **over** quick delivery that rots under pressure.
- Impact awareness **more than** blindly reacting to changing demands.
- Structural integrity **more than** superficial fixes that “just pass for now.”
- Technical courage **over** silent compliance with bad decisions.
- Early feedback **more than** late-stage firefighting.
- Intentional simplicity **over** rushed abstraction or clever hacks.
- Collective responsibility **more than** isolated heroics or blame deflection. Transparent trade-offs **over** hiding risk behind “small changes.”
- Refactoring as investment **more than** deferring cleanup until it’s too late.

That is, while we see value in the items on the right, we value those on the left more.

In addition to this:

## 📜 **Manifesto for software crafting**

As aspiring Software Craftsperson we are raising the bar of professional software development by practicing it and helping others learn the craft. Through this work we have come to value:

Not only working software, but also **well-crafted software**

Not only responding to change, but also **steadily adding value**

Not only individuals and interactions, but also **a community of professionals**

Not only customer collaboration, but also **productive partnerships**

That is, in pursuit of the items on the left we have found the items on the right to be indispensable.

[https://manifesto.softwarecraftsmanship.org/](https://manifesto.softwarecraftsmanship.org/)

---

### Conclusion: the cost of pretending

ÑaaS is a clever joke. But like all satire, it points to a painful truth: that teams are often forced to deliver lies in code form, because truth is politically inconvenient.

You can’t build systems that last by piling on patches that don’t. And you can’t fix cultural rot with more process.

What we need is not more speed. It’s more courage.

So let’s stop calling hacks solutions. Let’s stop pretending output is progress. Let’s build with intent, clarity, and responsibility.

Let’s end ÑaaS, before it becomes the standard.

### 🧨 Final quote: The real face of ÑaaS

> “Hacer basura y luego hablar de deuda técnica es tener mucho morro.” *(“Shipping trash and then calling it technical debt is just plain shameless.”)*

> - *Luis Artola, Software Economics*

---

### 📚 References

- Artola, Luis. *Software Economics*. 2021.
- Ocaña, José Manuel. *ÑaaS – Ñapa as a Service*. Blog post, *Calidad y Software*, July 10, 2015. [https://calidadysoftware.wordpress.com/2015/07/10/naas-napa-as-a-service](https://calidadysoftware.wordpress.com/2015/07/10/naas-napa-as-a-service)
- Ensemble Podcasting. *[Episode on Programal](https://open.spotify.com/episode/61kh9BTCLEImt4uI5BhrRF?si=zhLaiksDQTGfrhskTFxg1Q)*
- Cunningham, Ward. *[Ward Explains Technical Debt](https://youtu.be/pqeJFYwnkjE)*[, 2009](https://youtu.be/pqeJFYwnkjE).
