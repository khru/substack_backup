---
title: "AI can write code. That was never the bottleneck."
subtitle: "The real constraints in software development are product decisions, business trade-offs, organizational structure. Accelerating code production does not remove them. It exposes them."
requested_url: "https://emmanuelvalverderamos.substack.com/p/the-real-bottleneck-was-never-code"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/the-real-bottleneck-was-never-code"
substack_post_id: 190302623
retrieved_at: "2026-03-25T08:43:31.318Z"
---
# AI can write code. That was never the bottleneck.

### The real constraints in software development are product decisions, business trade-offs, organizational structure. Accelerating code production does not remove them. It exposes them.

AI can generate code faster than ever.

But most software organizations were never limited by code production in the first place.

The real constraints lie in decisions, architecture, how teams are structured, the business streams, autonomous teams and so on...

## The pager goes off

[![](https://substackcdn.com/image/fetch/$s_!2Lrh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4af82fcc-7cfc-46f1-9633-92aa91a929e8_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!2Lrh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4af82fcc-7cfc-46f1-9633-92aa91a929e8_2816x1536.png)

At 2:17 AM the pager goes off.

Production latency is climbing. Error rates are rising. A downstream dependency is failing intermittently and the system is beginning to cascade.

Someone joins the incident call. Someone opens the service code. Someone starts scrolling.

The code compiles.
The tests pass.
The service deployed successfully a few days ago.

But something is wrong.

Thirty minutes later the call is still quiet except for the sound of keyboards and Slack notifications. Engineers read through functions, trace dependencies, and try to reconstruct the assumptions behind pieces of logic that technically work but whose reasoning is unclear.

The problem is not just that the code is complex.

The problem is that nobody fully understands it.

Eventually the incident is resolved. A conditional path is patched, a configuration is rolled back, the system stabilizes.

But the deeper issue remains.

The code was not obviously bad.

It was opaque.

And that distinction matters more than most people realize.

The scenario I describe in the introduction to this article may seem a bit far-fetched to some people; you might even think I’m making it up, but the reality is that even Anthripic itself says the same thing.

> AI use impairs conceptual understanding, code reading, and debugging abilities, without delivering significant efficiency gains on average

> - [Judy Hanwen Shen](https://arxiv.org/search/cs?searchtype=author&amp;query=Shen,+J+H), [Alex Tamkin](https://arxiv.org/search/cs?searchtype=author&amp;query=Tamkin,+A) (study from Anthripic)

[![](https://substackcdn.com/image/fetch/$s_!xUeu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11661f7d-f164-446a-be2a-937cd3f43420_1542x887.png)](https://substackcdn.com/image/fetch/$s_!xUeu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11661f7d-f164-446a-be2a-937cd3f43420_1542x887.png)

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

# The assumption behind the AI boom

There is a strange assumption at the center of the current AI boom.

It assumes software development has historically been slow because writing code is difficult.

It assumes software development has historically been slow because writing code is difficult. It assumes productivity has been constrained mainly by producing artifacts such as code, tickets, or documentation. And it assumes that if those artifacts can be produced faster, the system as a whole will move faster too.

That assumption is often wrong.

In many real product organizations, software production was never the primary bottleneck.

The hard part was deciding what deserved to exist.

Why it mattered.
Which trade-offs were acceptable.
How systems should evolve.
How teams should be structured to support that evolution.

[![](https://substackcdn.com/image/fetch/$s_!KSDT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf5a06af-6a0b-442a-959d-695722d61653_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!KSDT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf5a06af-6a0b-442a-959d-695722d61653_2816x1536.png)

AI tools are extraordinary at accelerating production.

But production was rarely the real constraint.

AI increases code throughput.

**Software organizations are limited by decision throughput.**

That is the paradox at the center of the current AI moment.

Research from the **2025 DORA report on AI-assisted software development** reflects this tension. The report shows widespread AI adoption among developers while also observing that AI can increase delivery throughput while simultaneously increasing delivery instability. In other words, productivity improvements do not automatically translate into healthier systems.

AI is real.

The question is whether we are accelerating the part of the system that actually limits progress.

# How technological revolutions actually settle

Technologies that genuinely reshape work usually follow a familiar trajectory.

First they appear as novelty.
Then advantage.
Then habit.
Eventually expectation.

Version control changed collaboration. Continuous integration changed delivery. Cloud infrastructure changed deployment. Containers changed environments.

None of these technologies remained permanently revolutionary.

They became infrastructure.

The same pattern appears outside software.

Cars reshaped cities. Email transformed communication. GPS changed navigation. Office software became basic professional literacy.

At some point technologies that truly matter stop feeling revolutionary.

They simply become normal.

The current AI conversation often looks different. Instead of gradually becoming infrastructure, AI still exists inside a constant narrative of disruption. The discussion focuses on capability. It rarely examines constraints.

But software history shows a different pattern. Progress usually comes from raising the level of abstraction.

Assembly replaced machine code.
High level languages replaced assembly.
Frameworks replaced boilerplate infrastructure.

Each step reduced some kinds of work while making other responsibilities more important.

AI may simply be the next abstraction layer.

If that is the case, engineering does not disappear.

The center of gravity moves upward.

# The real bottlenecks in software organizations

[![](https://substackcdn.com/image/fetch/$s_!nxzd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facd124b8-0144-47d8-9a22-04ba8f9f79ec_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!nxzd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facd124b8-0144-47d8-9a22-04ba8f9f79ec_2816x1536.png)

Inside real product organizations, constraints rarely look like “we cannot write code fast enough”.

They usually appear somewhere else.

Tweet by the creator of [OpenCode](https://opencode.ai/)

### Product decisions

Many organizations struggle not because they cannot build software but because they are unsure what should be built.

Understanding real user problems is difficult. Prioritization under uncertainty is difficult. Discovery is difficult.

Building the wrong thing faster does not improve the system.

It simply produces waste faster.

### Business decisions

Software exists inside economic constraints.

Companies must decide how to increase return on investment without damaging reliability, degrading the user experience, or undermining long term product quality.

These are decision problems.

Not programming problems.

### Organizational structure

A large portion of friction in software development comes from organizational design.

Teams are declared autonomous but depend on each other to move forward. Ownership boundaries are unclear. Communication overhead grows as systems grow.

This is where Conway’s Law becomes important.

In *How Do Committees Invent?*, Melvin Conway observed that organizations design systems that mirror their communication structures.

If the organization is fragmented, the architecture tends to become fragmented as well.

Generating code faster does not solve this.

## The decision latency bottleneck

Software development rarely slows down because engineers cannot type fast enough.

It slows down because decisions move slowly through organizations.

Product teams must decide what problem is worth solving.
Operations must decide whether changes are safe.
Leadership must decide which trade-offs are acceptable.

Each of these decisions introduces latency.

Code can be written in minutes.

But the decision that justifies the code can take weeks.

And the validation that proves the decision was correct can take months.

AI changes the cost of producing code.

It does not change the cost of making good decisions.

In fact, it may increase the importance of them.

Because when implementation becomes cheap, the consequences of bad decisions become more expensive.

# AI accelerates output, but output was rarely the constraint

[![](https://substackcdn.com/image/fetch/$s_!sNKu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa15ea491-7f16-47b7-bdd7-f665bdd5a1ca_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!sNKu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa15ea491-7f16-47b7-bdd7-f665bdd5a1ca_2816x1536.png)

To understand where AI fits, it helps to distinguish three concepts.

Output is what teams produce. Outcome is what changes because of that work. Throughput is how quickly work flows through the system.

AI dramatically increases output.

But output is not value.

A feature can ship and deliver no value. A redesign can confuse users. A system can increase complexity without improving anything meaningful.

The DORA research describes AI primarily as an **amplifier**.

It magnifies the strengths of well organized teams and the weaknesses of poorly organized ones.

AI does not automatically improve organizations.

It accelerates whatever system already exists.

## When AI leaves the benchmark and enters production

Much of the excitement around AI coding is based on benchmark results.

But benchmarks rarely capture what real software work looks like.

Real work is long lived.
It evolves over time.
It interacts with existing systems.
And it must survive incidents.

The Remote Labor Index tries to measure this difference by evaluating AI systems on real freelance jobs rather than synthetic benchmarks.

The result is sobering.

While AI systems perform extremely well on many coding benchmarks, their success rate on real paid remote work remains dramatically lower. Completing an entire project at professional quality is far more difficult than generating a plausible code snippet.

A second study, SWE-CI, evaluates something even closer to real software development: long term codebase evolution.

Instead of testing whether a model can produce a correct patch once, it evaluates whether the model can maintain system integrity across extended sequences of changes.

The study builds tasks from real repositories spanning hundreds of days and dozens of commits.

The challenge is not writing code.

The challenge is avoiding regressions while evolving a system.

Production experience points in the same direction.

A Financial Times report described an internal Amazon briefing that discussed a trend of incidents involving high blast radius changes and GenAI assisted code modifications where safeguards and best practices were still emerging.

The hard part is not generating a change.

The hard part is containing its consequences.

# AI makes good engineering more important, not less

Generating code has always been the cheapest part of building software.

The expensive parts are understanding systems, making sound design decisions, maintaining clarity, and keeping complexity under control.

AI dramatically increases the volume of code produced.

It does not automatically improve the quality of the decisions behind that code.

If engineering discipline is weak, AI produces larger volumes of poorly structured systems.

If engineering discipline is strong, AI can accelerate implementation without destroying clarity.

When the cost of producing code falls, the cost of making the wrong decision rises.

Let’s put an example that we all can understand:

If at school I have to write an essay, Would I ask the IA about what should I write the essay? the answer is clear NO, I would look for the topic, I would tell it what I want and maybe some sources I want to research, and when the results come I would have to check that it has not hallucinated, change the structure, read the essay, but for that I need to know:

- What I want
- How I wanted
- Why I wanted like this.

More examples here: [https://www.linkedin.com/posts/ian-cooper-2b059b_coding-is-dead-long-live-programming-https-share-7438131759264870400-SY2Q](https://www.linkedin.com/posts/ian-cooper-2b059b_coding-is-dead-long-live-programming-https-share-7438131759264870400-SY2Q)

# Engineering is not typing

[![](https://substackcdn.com/image/fetch/$s_!LAw2!,w_56,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f614ac4-f17a-4cf4-bc01-eedb89699530_96x96.jpeg)](https://javil.substack.com/p/whats-the-important-part-of-being?utm_source=substack&amp;utm_campaign=post_embed&amp;utm_medium=web)

The popular narrative around AI often treats programming as if it were mainly typing code. It is not.

Another way to understand this shift is to look at the difference between execution and responsibility.

Many engineers have worked in environments where the job is defined mostly as ticket execution. A task appears in the backlog, the implementation is delivered, the tests pass, and the ticket is closed. The focus is on completing work quickly and keeping the queue moving.

In those situations the developer’s main concern is the work immediately in front of them. The impact of each change on the larger system is often outside the scope of the task. Decisions are small, local, and rarely require deep reflection about long-term consequences.

AI tools fit naturally into this model because they are very good at accelerating execution. They help produce implementations faster. They help close tickets faster. They help move work through the system.

But the profession of software development has never been defined only by execution.

The difficult part of engineering lies in decisions whose consequences are hard to reverse.

Decisions about system boundaries.
Decisions about data models.
Decisions about dependencies.
Decisions about how complexity is introduced or controlled.

These decisions shape the behavior of the system long after the ticket that introduced them has been closed.

And this is where the center of gravity of the profession increasingly sits.

AI may accelerate the production of implementations, **but it does not eliminate the need to understand which decisions matter**, when they matter, and what their long-term consequences will be.

If anything, **accelerating implementation makes these decisions more important**.

**Because when the cost of producing code falls, the cost of making the wrong decision rises.**

Engineering involves architecture, trade-offs, debugging, reliability, and long-term maintainability.

A design pattern can be implemented syntactically while being misunderstood conceptually.

The code looks correct.

The design intent is missing.

Now imagine generating large volumes of code with AI in an environment where developers cannot evaluate the design quality of what they receive.

The risk is not always incorrect code.

The risk is code that works but is poorly understood.

# The cognitive bottleneck

Research summarized in **The Programmer’s Brain** by Felienne Hermans shows that developers spend a large portion of their time reading code rather than writing it.

Programming difficulty often arises from three factors:

lack of knowledge lack of information limits in cognitive processing

Software engineering is therefore fundamentally cognitive work.

It requires building mental models of complex systems.

AI accelerates generation.

It does not eliminate the need for understanding.

# The review and incident problem

AI systems can generate code quickly.

Human review capacity does not scale at the same rate.

Someone still needs to read the code, understand its implications, and decide whether it is safe to deploy.

This becomes most visible during incidents.

When systems fail, engineers must reason about behavior under pressure.

If the system is poorly understood, debugging becomes archaeology.

The system runs.

But the organization’s understanding of the system erodes.

There is a second risk here beyond review overhead.

Automation can reduce contact with the kind of work that used to build understanding.

One of the core insights in Lisanne Bainbridge’s “Ironies of Automation” is that the human remains responsible for the hardest moments even as automation absorbs more of the routine ones.

That matters in software because the skills needed at 2:17 AM during an incident are not built by approving outputs passively. They are built by wrestling with systems, debugging real failures, and forming mental models through repeated exposure. If a team generates more and understands less, then the hardest moment arrives exactly when its operational intuition is weakest.

# The operational opacity problem

This leads to a subtle but important risk.

The problem is not always incorrect code.

The problem is **opaque code**.

Opaque systems work most of the time.

But when something breaks, nobody has a clear mental model of how the pieces interact.

Over time complexity grows faster than understanding.

The system works.

But the organization loses the ability to explain why.

# The paradox of the content economy

There is also an irony in the AI conversation.

A large portion of AI-related content repackages existing material into summaries, explainers, and commentary.

Retrieving information and summarizing announcements are tasks AI systems perform well.

Which means the people predicting the replacement of engineers are often working in a layer of the economy that is itself highly exposed to automation.

The creators who remain valuable will be those who provide context, experience, and judgment.

Exactly the same qualities that remain valuable in engineering.

# The conference effect and the content layer

The public narrative around AI is not shaped only by engineers building production systems.

It is also shaped by a large ecosystem of commentators, influencers, and conference programming incentives.

Conference agendas, technical media, and online discourse often emphasize AI topics heavily. Organizers rarely publish acceptance statistics for talks, so the trend is difficult to measure precisely. But the composition of many conference programs suggests that AI framing has become a strong signal of relevance.

Topics such as principles of software design and engineering practices increasingly need to be framed through an AI lens in order to attract attention.

Ironically, these are exactly the areas that determine whether AI generated output becomes useful or harmful.

But not just that, the fundamentals of software design and engineering practices should also have their space on this types of content and events.

# Saturation and backlash

The current AI wave is also producing a cultural reaction.

Part of the backlash against AI is not fear of technology. It is fatigue with misapplied technology.

Global surveys show that public trust in AI systems remains limited even as adoption increases.

Users also react negatively when AI features appear in products without clearly improving the experience.

When AI is inserted everywhere regardless of context, people stop experiencing it as innovation. They start experiencing it as clutter or imposition.

That reaction does not mean AI is useless.

It means usefulness still matters.

# Conclusion

At the beginning of this article, an engineer stared at code during a production incident.

The system was running.

But nobody fully understood it.

That moment captures the real tension in the AI moment.

We are accelerating production.

But production was rarely the real bottleneck.

The real constraints lie elsewhere.

Several conclusions follow.

First, the real constraints in software organizations are usually:

- Product decisions.
- Business trade-offs.
- Organizational structure.
- Engineering judgment.
- System understanding.

Second, AI increases output capacity, but output was rarely the scarce resource in software development, and remember output is NOT outcome.

Third, Conway’s Law reminds us that systems reflect organizational structure. Many bottlenecks are structural before they are technical.

Fourth, AI does not reduce the importance of engineering discipline. It increases the cost of weak architecture, weak design, and weak decision making.

Fifth, the current AI narrative is amplified by media and incentive structures that reward prediction more than operational insight.

Sixth, the growing backlash against AI is often a reaction to saturation and weak product fit rather than rejection of the technology itself.

AI will change how software is built.

But the important question is not whether AI can generate more code.

The important question is whether we are improving the systems that decide what that code should be.

Because if we are not, we are simply producing complexity faster.

And the next time the pager goes off at 2:17 AM, we may discover that we built a system nobody truly understands.

AI can accelerate implementation.
It cannot replace experience.

**And experience is exactly what you gain by dealing with the consequences of real systems.**

**AI is very good at helping engineers finish work. It is much less helpful when the real challenge is deciding which work should exist in the first place.**

**If you think this article wasn't necessary, I thought so too, but after reading things like this:**

- [Don't reciew the AI changes](https://www.linkedin.com/posts/fabian-wesner_are-code-reviews-still-needed-the-idea-share-7437838894013923331-AN1u)
- [All you need is good tests](https://www.linkedin.com/feed/update/urn:li:activity:7437838897088471040/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287437857452374519808%2Curn%3Ali%3Aactivity%3A7437838897088471040%29)

Last but not least, I think is important that we start thinking about how this will impact our ability to learn what we are doing and do a better work, example of this are reacent studies from companies like anthropic. Where they say this:

> Research shows AI helps people do [parts](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566) of their job faster. In an observational [study](https://www.anthropic.com/research/estimating-productivity-gains) of [Claude.ai](http://claude.ai/redirect/website.v1.6c59e1cc-e9fd-42a2-b881-d16825636aed) data, we found AI can speed up some tasks by 80%. But does this increased productivity come with trade-offs? Other research shows that when people use AI assistance, they become [less engaged with their work](https://www.nature.com/articles/s41598-025-98385-2) and [reduce](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf) the effort they put into doing it—in other words, they offload their thinking to AI.

> …

> On average, participants in the AI group finished about two minutes faster, although the difference was not statistically significant. There was, however, a significant difference in test scores: the AI group averaged 50% on the quiz, compared to 67% in the hand-coding group—or the equivalent of nearly two letter grades (Cohen's *d*=0.738, *p*=0.01). The largest gap in scores between the two groups was on debugging questions, suggesting that the ability to understand when code is incorrect and why it fails may be a particular area of concern if AI impedes coding development.

> …

> Our results **suggest that incorporating AI aggressively into the workplace, particularly with respect to software engineering, comes with trade-offs.** The findings highlight that not all AI-reliance is the same: the way we interact with AI while trying to be efficient affects how much we learn. Given time constraints and organizational pressures, junior developers or other professionals may rely on AI to complete tasks as fast as possible at the cost of skill development—and notably the ability to debug issues when something goes wrong.

> Though preliminary, t**hese results suggest important considerations as companies transition to a greater ratio of AI-written to human-written code**. **Productivity benefits may come at the cost of skills necessary to validate AI-written code if junior engineers’ skill development has been stunted by using AI in the first place**. Managers should think intentionally about how to deploy AI tools at scale, and consider systems or intentional design choices that ensure engineers continue to learn as they work—and are thus able to exercise meaningful oversight over the systems they build.

Source: *[How AI assistance impacts the formation of coding skill](https://www.anthropic.com/research/AI-assistance-coding-skills)*

A video de resume this articule and also express in a different way the same that I talk on this article

The question that comes to mind after writing this article, rereading it many times, and updating it (more than seven times so far)

**What is the real, root problem that AI is meant to solve? And how is it solving it?**

This reminds me of Facebook. Before Facebook, nobody felt the need to “connect”, we were already connected. A need was simply created that we DIDN’T have to solve a problem we DIDN’T have. My question is: is anyone capable of answering the fundamental questions. **What problem did we have that this technology solves, and how is it doing so?** So far, I only see promises that it will do many things and that it will be something that changes the world. And it is changing it, but not because it’s contributing anything to us, but because we’re using it for things without even considering the consequences.

Let’s take an example that every developer will understand: imagine you’re given a problem to solve, and instead of thinking about the problem and coming up with a solution, you simply take an untested solution and apply it without considering what implications it might have. The next day, it will be like the beginning of this article: In the worst-case scenario and even in the best-case scenario, you’ll realize you’re building something that doesn’t solve the problem or might not solve it.

I often say that the difference between someone with little or no experience and someone with experience is that, before writing code, the latter stops to think about what they’re doing.

By distinguishing between the problem space and the solution space and understanding the trade-offs involved in the decisions we make—sadly, in the case of AI, due to social pressure, the hype generated, and all the smoke and mirrors— I get the feeling that we’re entering a state of urgency and/or fear that’s causing us to make decisions that may not be the best for us, simply because others are making us feel that way. With this article, I’d like to call on everyone to, before rushing headlong into a solution, at least consider what implications using it will have and whether or not it’s even sustainable.

Speaking of sustainability, I’ll give another example that developers will understand: when you’re going to use a library or a framework for a professional application, you don’t just grab the framework that just came out; you check if it solves your problem, if it’s stable, if it has documentation, if it’s been tested, and if other companies are using it—you do much more thorough research. With AI, you’re not even waiting for that—you’re using the beta version, and you and your company are the beta testers. I know it sounds sad, but it’s true.

Other interesting points of view for the AI are this:[Marcus on AILLMs + Coding Agents = Security NightmareLast October, I wrote an essay called “When it comes to security, LLMs are like Swiss cheese — and that’s going to cause huge problems” warning that “The more people use LLMs, the more trouble we are going to be in”. Until last week, when I went to Black Hat Las Vegas, I had no earthly idea how serious the problems were. There, I got to know Nathan Hami…Read more7 months ago · 422 likes · 72 comments · Gary Marcus and Nathan Hamiel](https://garymarcus.substack.com/p/llms-coding-agents-security-nightmare?utm_source=substack&amp;utm_campaign=post_embed&amp;utm_medium=web)

# References

- Conway, M. (1968). *How Do Committees Invent?* [https://www.melconway.com/Home/pdf/committees.pdf](https://www.melconway.com/Home/pdf/committees.pdf)
- Harvey, N., Storer, K., DeBellis, D., et al. (2025). *State of AI-Assisted Software Development*. [https://dora.dev/research/2025/dora-report/](https://dora.dev/research/2025/dora-report/)
- Hermans, F. (2021). *The Programmer’s Brain*. Manning.
- Gillespie, N., Lockey, S., Ward, T., Macdade, A., Hassed, G. (2025). *Trust, Attitudes and Use of Artificial Intelligence: A Global Study*. [https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf](https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf)
- Emilio Carrión. *[El código que nadie entiende ya está en producción](https://www.linkedin.com/pulse/el-c%C3%B3digo-que-nadie-entiende-ya-est%C3%A1-en-producci%C3%B3n-emilio-carri%C3%B3n-swxle/?trackingId=qyZXsWaEQn%2BvCBZvb9VY6A%3D%3D)*
- Emilio Carrión. *[La IA no va a eliminar al ingeniero de software. Va a eliminar al que solo escribía código.](https://www.linkedin.com/pulse/la-ia-va-eliminar-al-ingeniero-de-software-que-solo-escrib%25C3%25ADa-carri%25C3%25B3n-kcele/)*
- Forsgren, N., Humble, J., Kim, G. (2018).** ***Accelerate: The Science of Lean Software and DevOps*
- DeMarco, T., Lister, T. (1999). Peopleware: *Productive Projects and Teams*
- Chen, J., Xu, X., Wei, H., Chen, C., Zhao, B. (2026) *SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration. [https://arxiv.org/abs/2603.03823](https://arxiv.org/abs/2603.03823)*
- Anthropic. *How AI assistance impacts the formation of coding skill* [https://www.anthropic.com/research/AI-assistance-coding-skills](https://www.anthropic.com/research/AI-assistance-coding-skills)
- [Judy Hanwen Shen](https://arxiv.org/search/cs?searchtype=author&amp;query=Shen,+J+H), [Alex Tamkin](https://arxiv.org/search/cs?searchtype=author&amp;query=Tamkin,+A). *How AI Impacts Skill Formation*. [https://arxiv.org/abs/2601.20245](https://arxiv.org/abs/2601.20245)
