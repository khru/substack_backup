Title: Agents are not a new abstraction layer. They are a new place to hide the bill

URL Source: http://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction

Final URL: https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction

Published Time: 2026-06-29T13:00:46+00:00

Markdown Content:
This article is a direct response to Sebastian Bergmann’s article _Beyond Best Practices_, published on phpunit.expert.

Sebastian Bergmann is the creator of PHPUnit, and his article makes a serious argument: LLM-based coding agents are not replacing compilers, but extending the historical progression of software abstraction. In that framing, we moved from machine code to assembly, then to higher-level languages, frameworks, libraries, and now agentic systems. The claim is that agents let us focus on what software should do and why, while the implementation details move into automation.

[![Image 1](https://substackcdn.com/image/fetch/$s_!MtPu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc14dd96a-a2ef-4f81-8d60-52fd05310ebd_1237x1794.png)](https://substackcdn.com/image/fetch/$s_!MtPu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc14dd96a-a2ef-4f81-8d60-52fd05310ebd_1237x1794.png)

I respect the seriousness of the argument. I also think this specific abstraction claim is wrong.

Not because agents are useless.

Not because automation is bad.

Not because tests, documentation, code review, static analysis, and architectural constraints are unimportant. They are essential.

The problem is more basic: comparing LLM agentic development with abstraction only works if we weaken the meaning of abstraction until it becomes almost indistinguishable from hiding, delegation, or automation.

That is the mistake this article rejects.

A real abstraction lets us ignore selected details because the model underneath has stable semantics, reliable boundaries, and a contract strong enough to reason with. If the thing forces me to know its hidden behavior, model quirks, prompt sensitivity, tool limitations, and failure patterns in order to use it safely, then it has not raised the level of abstraction in the engineering sense. It has moved the cost somewhere else.

At best, that is a leaky abstraction.

At worst, it is not an abstraction at all.

It is just another tool with a nicer story.

Imagine taking your car to a workshop because the engine makes a strange noise. The mechanic disappears behind a curtain, returns with a confident smile, and tells you the car is fixed.

Then he hands you a flashlight, a torque wrench, a diagnostic scanner, and a warning:

“Before driving, please check every bolt, every cable, every fluid level, and every safety-critical part. Sometimes I improvise.”

That is not an abstraction over car repair.

That is delegation without trust.

The work may still be useful. The first pass may save time. The mechanic may have found something you missed. But if the final responsibility, the verification burden, the diagnosis of mistakes, and the cost of rework all remain yours, the curtain did not become an abstraction layer. It became a place where risk disappears for a moment before it returns wearing a cleaner shirt.

This is where much of the current conversation around _Large Language Model_ (LLM) agentic development goes wrong. We are told that agents are the next layer in the long history of software abstraction. Assembly gave way to C. C gave way to higher-level languages. Operating systems hid hardware. Cloud platforms hid machines. Kubernetes hid servers behind desired state. Now, supposedly, agents will hide programming itself behind intent.

That story sounds elegant. It is also dangerously lazy.

LLM agentic development is not automatically a new abstraction layer. It can be a useful tool. It can be a powerful accelerator in some contexts. It can help explore, scaffold, transform, summarize, and automate slices of work. But calling it a new abstraction layer without asking what contract it provides, what semantics it preserves, what failures it bounds, what costs it moves, and what evidence supports it is bullshit.

The problem is not that teams are experimenting with LLM agents. The problem is that many are trying to convince themselves that moving uncertainty behind a prompt, a model, an agent runner, and a tool-calling loop is the same thing as raising the level of abstraction.

It is not.

LLM agentic development is better understood as probabilistic orchestration with delegated execution and delayed verification than as a software abstraction layer.

A real abstraction gives us a usable model, stable boundaries, preserved semantics, and a way to reduce the number of details we must track for a given purpose. It does not make reality disappear. It decides which details are irrelevant at a particular level and gives us a contract strong enough to work safely without constantly opening the box.

Current LLM agents do not provide that kind of contract for software development as a whole. They can plan, call tools, edit files, run commands, inspect failures, and produce plausible outputs. Their behavior still depends on model versions, prompts, context selection, tool availability, memory, permissions, infrastructure, and human supervision.

That does not make them useless. It makes them something different.

They are useful when the task is bounded, the feedback loop is fast, the cost of error is acceptable, and verification is independent. They become dangerous when organizations treat their fluency as correctness, their speed as delivery, or their autonomy as abstraction.

Usefulness is not the same as abstraction.

Speed is not the same as delivery.

Fluency is not the same as correctness.

The honest claim is this: LLM agents can reduce some local work while adding new verification, review, security, governance, and maintenance work elsewhere. Whether that is worth it depends on context, measurement, and the cost of keeping the system trustworthy.

The dishonest claim is this: agentic development is simply the next abstraction layer, so skepticism is just nostalgia.

*   [A curtain is not an abstraction](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7a-curtain-is-not-an-abstraction)

*   [What abstraction actually means](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7what-abstraction-actually-means)

*   [Abstraction in software is a contract, not a vibe](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7abstraction-in-software-is-a-contract-not-a-vibe)

*   [Abstraction is not hiding, automation, delegation, orchestration, or compression](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7abstraction-is-not-hiding-automation-delegation-orchestration-or-compression)

*   [If I must know the model’s quirks, what exactly was abstracted?](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7if-i-must-know-the-models-quirks-what-exactly-was-abstracted)

*   [Why the old abstraction ladder is seductive](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7why-the-old-abstraction-ladder-is-seductive)

*   [What LLM agentic development actually is](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7what-llm-agentic-development-actually-is)

*   [The claim I am rejecting](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7the-claim-i-am-rejecting)

*   [The missing contract](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7the-missing-contract)

*   [Non-determinism is not a footnote](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7non-determinism-is-not-a-footnote)

*   [Hallucination is not a leaky abstraction](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7hallucination-is-not-a-leaky-abstraction)

*   [The infrastructure matters more than the slogan](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7the-infrastructure-matters-more-than-the-slogan)

*   [The hidden detail is not the problem; hidden responsibility is](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7the-hidden-detail-is-not-the-problem-hidden-responsibility-is)

*   [We already learned this lesson with frameworks](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7we-already-learned-this-lesson-with-frameworks)

*   [The evidence is mixed, and that matters](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7the-evidence-is-mixed-and-that-matters)

*   [What to measure before believing the story](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7what-to-measure-before-believing-the-story)

*   [Where LLM agents are genuinely useful](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7where-llm-agents-are-genuinely-useful)

*   [Where the abstraction claim collapses](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7where-the-abstraction-claim-collapses)

*   [A test for calling something an abstraction layer](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7a-test-for-calling-something-an-abstraction-layer)

*   [A better mental model](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7a-better-mental-model)

*   [The sharp line](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7the-sharp-line)

*   [Conclusion](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7conclusion)

*   [References](https://emmanuelvalverderamos.substack.com/p/agents-are-not-a-new-abstraction?open=false#%C2%A7references)

[![Image 2](https://substackcdn.com/image/fetch/$s_!hSCI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fadf8b8-1899-4ed3-9e51-d301d930ee30_1024x559.png)](https://substackcdn.com/image/fetch/$s_!hSCI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fadf8b8-1899-4ed3-9e51-d301d930ee30_1024x559.png)

A curtain hides. An abstraction explains by choosing what not to show.

That distinction matters. A curtain can cover a messy kitchen. It can also cover a fire. Hiding detail is only useful when the hidden detail is either irrelevant to the current task or controlled by a reliable boundary.

A car steering wheel is an abstraction because, for normal driving, you do not need to understand every mechanical detail between the wheel and the tyres. The abstraction has properties. Turning left has a stable meaning. Resistance in the wheel gives meaningful feedback. The driver has a usable model, and that model is reliable enough for the purpose.

A restaurant menu is also an abstraction. You order “mushroom risotto,” not “ninety grams of arborio rice, stock added gradually, stirred until starch release gives a creamy texture.” But the menu only works because there is a kitchen, a recipe, a supply chain, a cook, and a shared cultural expectation of what “risotto” means.

If the kitchen sometimes returns soup, sometimes rice pudding, and sometimes a philosophical essay about mushrooms, the menu is no longer a useful abstraction. It is a gamble with typography.

Software abstraction works the same way. It is not a decorative layer of words. It is a model with boundaries, responsibilities, and consequences.

When someone says “LLM agents are just another abstraction layer,” the first question should be simple:

What exactly can I stop knowing, stop checking, or stop controlling because this layer exists?

If the honest answer is “nothing important,” then we are not discussing abstraction. We are discussing a tool that still requires supervision.

That tool may still be valuable. A supervised tool can be valuable. A powerful assistant can be valuable. A fast generator can be valuable. But value is not the same as abstraction.

A curtain hides the mess. An abstraction changes how we can safely think.

[![Image 3](https://substackcdn.com/image/fetch/$s_!docH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a6968d7-2482-4af2-91bf-88201bd9199b_1024x559.png)](https://substackcdn.com/image/fetch/$s_!docH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a6968d7-2482-4af2-91bf-88201bd9199b_1024x559.png)

Abstraction is the act of representing something by deliberately leaving out details that are not relevant to a particular purpose while preserving the properties that are relevant.

That last part carries the weight: preserving the properties that are relevant.

A map is an abstraction of territory. A subway map may distort distance, geography, and scale, but it preserves connectivity. That is why it works. It would be a poor map for hiking and a useful map for changing trains. Its value depends on purpose.

A calendar is an abstraction of time. It ignores weather, mood, energy, uncertainty, and human exhaustion, but it preserves dates, durations, recurrence, and sequence. It is useful for planning a meeting. It is not enough to understand whether a team has cognitive capacity to absorb another project.

An invoice is an abstraction of economic exchange. It does not include every conversation, every trade-off, every frustration, or every late-night decision. It preserves parties, amounts, dates, obligations, and payment state. That is why it can move through accounting systems.

Good abstractions are not vague. They are selective. They have a point of view.

A useful abstraction does not merely hide detail. It changes the flow of knowledge. It removes knowledge the caller should not need, while preserving the knowledge the caller must have to act safely. If it exposes irrelevant detail, it creates noise. If it hides essential detail, it creates risk.

In computing, abstraction is not a luxury. It is how we survive scale. We cannot reason about every transistor, scheduler decision, cache line, system call, network packet, object, database page, dependency, and user behavior at the same time. We build models that allow us to think at a chosen level.

Procedures, types, modules, protocols, relational tables, objects, queues, containers, virtual machines, and cloud resources are all ways of drawing a boundary around complexity.

But every useful boundary also makes a promise.

It says: “For this purpose, you can think about me like this.”

The moment that promise is weak, unstable, or unverifiable, the abstraction begins to rot.

[![Image 4](https://substackcdn.com/image/fetch/$s_!k2_g!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4de7c62-df0d-4003-856c-0a513a25f066_1024x559.png)](https://substackcdn.com/image/fetch/$s_!k2_g!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4de7c62-df0d-4003-856c-0a513a25f066_1024x559.png)

A software abstraction is not just a nicer interface. It is a contract between the user of the abstraction and the thing being abstracted.

That contract may be formal, like a type signature, protocol specification, schema, or database constraint. It may be semi-formal, like an architectural boundary, module interface, or documented behavior. It may be cultural, like a team convention backed by tests, review discipline, and shared ownership.

But it must exist.

Without a contract, the abstraction becomes a rumor.

A useful software abstraction usually gives us several things:

1.   A stable interface

2.   Preserved semantics

3.   Hidden implementation details

4.   Explicit failure modes

5.   Composability

6.   Observability at the boundary

7.   Accountability  
This is why David Parnas matters here. His work on modular decomposition was not about placing code into separate files. It was about using information hiding as a design criterion. A good module hides a design decision likely to change, so the rest of the system does not become coupled to that decision.

That is abstraction with teeth.

Barbara Liskov’s work on data abstraction points in the same direction. Data abstraction helps organize programs so they can be modified and maintained. Again, the important move is not “hide something somewhere.” The important move is to define behavior through an abstraction that users can rely on while implementations remain replaceable.

A stack is a simple example. The user of a stack should not need to know whether it is backed by an array, a linked structure, contiguous memory, a persistent data structure, or something else. But the user does need stable semantics for push, pop, empty state, and errors.

If `pop` sometimes returns the last item, sometimes invents an item, and sometimes rewrites the caller’s source code, we would not celebrate it as a bold new abstraction.

We would call it broken.

[![Image 5](https://substackcdn.com/image/fetch/$s_!8f5O!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1745931-c57d-425f-985c-309e62cd8bc7_1024x559.png)](https://substackcdn.com/image/fetch/$s_!8f5O!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1745931-c57d-425f-985c-309e62cd8bc7_1024x559.png)

The agentic development conversation often collapses several different ideas into one glamorous word: abstraction.

That collapse is the source of much of the confusion.

Hiding is only part of abstraction. Hiding becomes useful when the hidden detail is irrelevant at the current level or controlled by a reliable contract.

A black box is not automatically an abstraction. A black box can also be a liability.

When an agent hides planning, context selection, tool execution, and code generation behind a chat interface, it has hidden activity. It has not necessarily created a safe model for reasoning.

The question is not “did it hide detail?”

The question is “did it preserve the right meaning while hiding the right detail?”

Automation performs work. Abstraction changes the model we reason with.

A script that formats files is automation. It may save time, but it does not necessarily change the conceptual model of the system. A compiler is both automation and abstraction. It automates translation and gives programmers a higher-level language with stable semantics.

An LLM agent may automate parts of software work. It may generate boilerplate, run tests, search documentation, produce migration drafts, or propose refactorings. That can be useful. But automating fragments of work does not automatically create a new abstraction layer over software development.

Automation asks: “Can the machine perform this task?”

Abstraction asks: “Can I safely reason at another level?”

Those are different questions.

Delegation gives work to another actor. Abstraction lets us ignore selected implementation details because the boundary is reliable enough.

A junior developer can implement a task. That does not make the junior developer an abstraction layer over software engineering. A contractor can write code. A consultant can propose architecture. A team can outsource a subsystem. Delegation moves work, but it does not erase responsibility.

LLM agents often create delegation without ownership. The human delegates a task, receives an output, and remains responsible for correctness, maintainability, security, and integration.

That is not abstraction.

That is supervised delegation.

Orchestration coordinates steps, tools, services, and feedback loops.

An agentic system may inspect files, call tools, run tests, edit code, evaluate failures, and try again. That is orchestration. It may be powerful. It may be impressive. It may produce useful results.

But orchestration is not automatically abstraction.

A chaotic process can be orchestrated. A fragile deployment pipeline can be orchestrated. A sequence of unreliable actions can be orchestrated. Coordination does not imply a stable conceptual model.

Agentic development is often better described as probabilistic orchestration with delegated execution and delayed verification than as abstraction.

That description is less glamorous, but more accurate.

LLMs are good at compression in the human sense. They can summarize code, explain logs, condense documentation, and turn large context into fluent language.

That can help. A summary can orient a developer. A generated explanation can reduce the cost of entering a codebase. A condensed plan can make a task feel manageable.

But compression can lose meaning.

A summary is not a contract. A fluent explanation is not evidence. A confident plan is not correctness. A compressed version of a codebase may omit the very detail that matters.

In software, the dangerous detail is often not loud. It is quiet. It lives in edge cases, production incidents, implicit invariants, old migrations, strange customer behavior, and comments nobody trusts but nobody deletes.

A model that compresses context can help us navigate complexity. It does not automatically abstract it.

[![Image 6](https://substackcdn.com/image/fetch/$s_!-QFz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa65d01e5-b992-448d-a6e3-db4632656eb4_1024x559.png)](https://substackcdn.com/image/fetch/$s_!-QFz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa65d01e5-b992-448d-a6e3-db4632656eb4_1024x559.png)

A simple example is enough.

Suppose I ask a model to generate a Mermaid diagram with labels that need line breaks. One model may correctly use `<br>` because Mermaid expects HTML-style line breaks in many label contexts. Another, weaker or differently trained model may use `\n`, because it confuses a textual newline escape with Mermaid’s rendering rules.

The result is not just a cosmetic issue. The moment I need to know which model handles Mermaid line breaks correctly, which one confuses `<br>` with `\n`, and how to defend myself against that difference, I am no longer reasoning at a clean higher level.

I am reasoning about the implementation behavior of the supposed abstraction.

That is exactly the kind of thing software engineers normally call a leaky abstraction. The leak is not that something went wrong once. The leak is that safe use requires knowledge of what was supposedly hidden.

And this gets worse when teams want to treat models as interchangeable.

The industry loves saying “use the model that fits the task,” as if swapping one LLM for another were like swapping one implementation behind a stable interface. But that is often not true. Different models have different failure modes, different instruction-following behavior, different context sensitivity, different tool-use reliability, different formatting quirks, different hallucination profiles, and different behavior under pressure.

If replacing the model changes the behavior of the system in ways the caller must understand, then the model boundary is not acting like a reliable abstraction.

It is acting like a dependency.

And dependencies need management.

[![Image 7](https://substackcdn.com/image/fetch/$s_!QqoD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fc532c7-296f-4b6f-9fc0-d19dc91515c0_1024x559.png)](https://substackcdn.com/image/fetch/$s_!QqoD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fc532c7-296f-4b6f-9fc0-d19dc91515c0_1024x559.png)

The industry loves a ladder.

Machine code. Assembly. C. Managed runtimes. Frameworks. Cloud. Serverless. Agents.

The ladder feels obvious because software history really does contain successful abstraction jumps. High-level languages removed much of the need to think in registers. Operating systems gave programs a model of files, processes, memory, and devices. Databases let us ask for sets of data without hand-writing storage traversal. Cloud platforms let teams provision capabilities through APIs instead of buying hardware.

So the story writes itself: LLM agents are the next rung. We will stop writing code and start expressing intent. We will stop managing implementation and start managing outcomes. Programming will move from syntax to goals.

There is a grain of truth there. Programming has always moved between levels of description. We do build more powerful notations. We do create better tools. We do automate old manual work. We do convert repeated expert activity into reusable mechanisms.

But the old abstraction story leaves out the price of admission.

C did not become useful because it was more English-like than assembly. It became useful because compilers, linkers, runtimes, conventions, debuggers, operating systems, and hardware targets formed a technical ecosystem with stable enough semantics.

_Structured Query Language_ (SQL) did not become useful because it magically removed data complexity. It became useful because relational theory, database engines, query optimizers, transactions, indexes, constraints, and execution plans created a practical contract. The abstraction leaks, especially through performance, but the model is not arbitrary.

Kubernetes did not become useful because YAML is beautiful. It is not. It became useful because desired state, controllers, reconciliation loops, scheduling, health checks, service discovery, and declarative APIs created a model teams could operate, debug, and automate. The abstraction leaks often, but it has a shape.

The history of abstraction is not the history of hiding more.

It is the history of inventing stronger models.

That is the part the agentic development hype usually skips.

[![Image 8](https://substackcdn.com/image/fetch/$s_!4gsK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc92d3e4-ed66-4755-9384-93da5da15b72_1024x559.png)](https://substackcdn.com/image/fetch/$s_!4gsK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc92d3e4-ed66-4755-9384-93da5da15b72_1024x559.png)

LLM agentic development is a socio-technical loop where an LLM is given instructions, context, tools, permissions, and feedback so it can perform multi-step software work.

In the simplest case, the model suggests code. In a more agentic case, the system can inspect files, plan changes, call tools, run commands, execute tests, search documentation, edit code, and iterate.

Some systems follow predefined workflows. Others let the model dynamically choose its own process and tool usage. Anthropic’s guidance makes this distinction explicit: workflows are systems where LLMs and tools are orchestrated through predefined code paths, while agents direct their own processes and tool use while working toward a goal.

That distinction matters.

A workflow is code-driven orchestration with LLM calls inside it. An agent gives the LLM more control over process and action selection. The more control the model gets, the more the system depends on the model’s judgment, the quality of context, the safety of tools, the permission model, and the strength of verification.

A simplified agentic development loop looks like this:

This is not one layer. It is a loop made of several moving parts:

1.   The base model

2.   The prompt

3.   The context window

4.   The retrieval mechanism

5.   The repository state

6.   The tools exposed to the agent

7.   The permissions granted to those tools

8.   The execution environment

9.   The tests and checks available

10.   The human reviewer

11.   The organization’s quality bar

12.   The future maintainer

When the loop works, it can feel magical. A feature appears. A test is generated. A migration is drafted. A bug is explored. A refactor is attempted. A library is explained. A tedious transformation is done in minutes.

But “it feels magical” is not an abstraction criterion.

A slot machine also hides complexity. That does not make it a financial planning abstraction.

[![Image 9](https://substackcdn.com/image/fetch/$s_!LD0s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F674d117b-f4ed-45cf-935d-1da858e80c66_1024x559.png)](https://substackcdn.com/image/fetch/$s_!LD0s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F674d117b-f4ed-45cf-935d-1da858e80c66_1024x559.png)

I am not rejecting the use of LLM agents.

I am rejecting this claim:

“LLM agentic development is just another abstraction layer over software development.”

That claim is too vague to be useful and too comforting to be harmless.

It suggests that the main historical pattern is “we stop caring about lower-level details.” That is false. The real pattern is more demanding: we build a model that lets us ignore some details because other details have been stabilized, specified, automated, tested, and bounded.

The abstraction claim also smuggles in a managerial fantasy. If agents are an abstraction layer over development, then maybe teams can buy the layer and reduce the need for deep engineering knowledge. Maybe the organization can route around slow humans. Maybe review becomes optional. Maybe design becomes prompting. Maybe tests are generated after the fact. Maybe senior engineers become supervisors of synthetic output rather than stewards of system integrity.

That fantasy is not new.

It is the old dream of automatic programming with a fresh coat of venture capital paint.

Frederick Brooks warned that there is no single technology or management technique that removes the essential difficulties of software. His point is still brutal: much of software’s difficulty is not typing code. It is understanding the problem, preserving conceptual integrity, managing change, conforming to other systems, and reasoning about a structure with too many interacting states.

LLM agents may reduce some accidental difficulty. They may help with ceremony, scaffolding, translation, boilerplate, exploration, and local edits.

But if they do not reduce the essential difficulty of understanding what should be built, why it should behave that way, how it interacts with the rest of the system, and how it will be safely changed later, they are not an abstraction over software development.

They are a new interface to a still-hard problem.

[![Image 10](https://substackcdn.com/image/fetch/$s_!DUS_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1966345-f6f7-4b28-b789-5f4707b60654_1024x559.png)](https://substackcdn.com/image/fetch/$s_!DUS_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1966345-f6f7-4b28-b789-5f4707b60654_1024x559.png)

A real abstraction answers the question:

What can I rely on?

With LLM agentic development, the answer is often uncomfortable.

Can I rely on the same prompt producing the same result tomorrow? Not fully.

Can I rely on the model understanding the domain rule the same way a team understands it after months of production incidents? No.

Can I rely on generated tests proving the generated code is correct? No.

Can I rely on a green test suite if the agent changed the tests, the implementation, and the assumptions together? No.

Can I rely on the agent preserving architectural boundaries unless they are explicitly encoded and checked? No.

Can I rely on the generated patch being maintainable by someone who did not watch the whole conversation? No.

Can I rely on the tool staying stable while the model, editor, plugin, context mechanism, pricing, rate limits, and agent framework evolve? No.

That does not mean the tool is useless. It means the abstraction claim is premature.

A useful abstraction reduces the number of details I must actively manage. A weak agentic setup often increases the number of details I must audit:

1.   Was the prompt precise enough?

2.   Did the model use the right files?

3.   Did retrieval miss a critical convention?

4.   Did the agent change behavior outside the intended scope?

5.   Did it introduce duplication?

6.   Did it bypass an architectural boundary?

7.   Did it generate tests that merely approve its own mistake?

8.   Did it rely on a deprecated API?

9.   Did it add a dependency we do not want?

10.   Did it solve the visible symptom while damaging the domain model?

11.   Did it produce code that compiles but cannot be owned?

12.   Did it make the next change harder?  
If I must ask all of that every time, I am not standing on a new abstraction layer.

I am supervising a probabilistic contributor with access to my attention, my tools, and sometimes my codebase.

[![Image 11](https://substackcdn.com/image/fetch/$s_!HlPh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76b6845d-1523-45dd-91f6-c88e9561e62b_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!HlPh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76b6845d-1523-45dd-91f6-c88e9561e62b_1024x1024.png)

Non-determinism is not a philosophical objection. It is an engineering property.

LLM APIs increasingly expose controls for reproducibility, such as seeds or system fingerprints, but those controls are not the same thing as a language specification, a type contract, or a deterministic compiler pipeline. They can improve repeatability in bounded settings. They do not turn an open-ended agent run into a stable abstraction over software development.

A compiler can have bugs. A database optimizer can choose a surprising plan. A distributed system can fail in strange ways. Mature abstractions are not perfect. But they are built around mechanisms that make behavior inspectable, reproducible, specified, constrained, or at least debuggable.

LLM agentic systems sit in a different place.

A prompt is not a specification in the same sense as a type contract, protocol, schema, or executable test. A model response is not a proof. A generated plan is not reliable execution. A successful run is not evidence that the next run will behave the same way.

That instability changes the economics of work.

When a tool is deterministic enough, we automate around it. When it is not, we supervise around it. Those are not the same motion.

Automation scales by moving human attention away from routine execution. Supervision consumes human attention to keep uncertain execution within acceptable bounds.

LLM agentic development often claims the first while quietly demanding the second.

That is the bill.

[![Image 12](https://substackcdn.com/image/fetch/$s_!ENto!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6395015-ff71-4f5c-8178-dcc19b62907a_1024x559.png)](https://substackcdn.com/image/fetch/$s_!ENto!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6395015-ff71-4f5c-8178-dcc19b62907a_1024x559.png)

All non-trivial abstractions leak. That observation is useful, but it should not be abused.

When _Transmission Control Protocol_ (TCP) abstracts over unreliable _Internet Protocol_ (IP), the network can still leak through. You still need timeouts. You still need retries. You still need to understand latency, congestion, and partial failure when systems matter.

But TCP’s abstraction is not “sometimes I invent packets that sound right.”

It has a protocol.

LLM hallucination is different. A model can produce fluent, plausible, confident output that is factually unsupported, semantically wrong, or subtly inconsistent with the codebase. In software, that is not just a content problem. It is a trust-boundary problem.

Generated code can look right while violating a domain invariant. Generated tests can look professional while asserting the wrong behavior. Generated documentation can sound helpful while preserving a false mental model. Generated architecture advice can be stylistically convincing while ignoring constraints that exist only in production scars, team agreements, or old migration notes.

That is not an abstraction leak in the normal sense.

That is a system presenting unverified synthesis as if it were knowledge.

The danger is not that LLMs fail. All tools fail. The danger is that they fail in a way that is rhetorically smooth.

A compiler error is ugly, but honest.

A hallucinated explanation is beautiful, but dangerous.

[![Image 13](https://substackcdn.com/image/fetch/$s_!w9zP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25111afc-f94c-4df6-9c12-9f2bd7704db9_1024x559.png)](https://substackcdn.com/image/fetch/$s_!w9zP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25111afc-f94c-4df6-9c12-9f2bd7704db9_1024x559.png)

People talk about agents as if the model were the product.

It is not.

An agentic development system is an infrastructure stack. It includes the model, the tool runner, the editor integration, the file system permissions, the sandbox, the memory system, the repository search, the dependency manager, the shell, the browser, the test runner, the policy layer, the audit trail, the logs, and the human operating model.

Change any of those and the system changes.

This is why the claim “the agent abstracts development” is so weak. The behavior depends heavily on the surrounding infrastructure.

A model with poor repository context is not the same as a model with precise retrieval. A model with unrestricted shell access is not the same as a model running in a sandbox. A model that can edit tests and code together is not the same as one that must satisfy externally owned tests. A model that can access production credentials is not the same as one that cannot.

The agent is not the abstraction.

At best, the abstraction is the controlled system around the agent: task boundaries, permissions, checks, traces, feedback, and ownership.

And most teams do not have that abstraction.

They have an editor plugin, a chat window, a half-written prompt, a few conventions, a fragile _Continuous Integration_ (CI) pipeline, a senior engineer reviewing too much code, and a manager counting output.

That is not a new layer of software engineering.

That is a new shape of operational risk.

[![Image 14](https://substackcdn.com/image/fetch/$s_!AJF4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1be99e04-6daa-4619-be41-f4f69023e912_1024x559.png)](https://substackcdn.com/image/fetch/$s_!AJF4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1be99e04-6daa-4619-be41-f4f69023e912_1024x559.png)

The key mistake in the abstraction story is not that agents hide detail. All abstractions hide detail. The mistake is that agents often hide the work while leaving the responsibility untouched.

That is the difference.

A compiler hides register allocation, instruction selection, and many machine-level details. But it also gives the developer a language specification, error model, build process, and repeatable artifact.

A database hides storage layout, query execution, and indexing machinery. But it also gives transactions, isolation levels, constraints, query plans, and operational signals.

An agent hides context selection, inference, planning, tool choice, and intermediate reasoning. But in many setups, it does not give the team a stable semantic model, a bounded failure model, or an independent correctness contract.

The hidden detail is not what makes the agent risky.

The hidden responsibility is.

[![Image 15](https://substackcdn.com/image/fetch/$s_!tsBw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9259d56-bb4a-41ed-956f-00c0d4cd91a1_1024x559.png)](https://substackcdn.com/image/fetch/$s_!tsBw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9259d56-bb4a-41ed-956f-00c0d4cd91a1_1024x559.png)

This problem is not new.

Imagine building a business-critical system on top of a framework. The framework promises productivity. It gives structure, conventions, routing, persistence helpers, dependency injection, validation, security primitives, testing utilities, and a happy path.

That can be useful.

But now imagine that every few weeks the framework changes its public interfaces, shifts its conventions, deprecates common paths, changes configuration semantics, and forces your business code to move because the framework moved underneath it.

Would you call that a successful abstraction?

Probably not.

You would call it coupling.

You would ask why your business model is so exposed to framework churn. You would introduce boundaries. You would isolate framework-specific code. You would protect the domain from external volatility. You would stop pretending that convenience is the same as independence.

This is one of the reasons developers have spent years learning not to couple their core business logic directly to frameworks. We create ports. We isolate adapters. We distinguish domain decisions from infrastructure decisions. We accept that frameworks are useful, but we also know that framework convenience can become framework gravity.

Agentic development has the same problem.

If your development process depends on the quirks of a specific model, a specific agent runner, a specific prompt format, a specific tool-calling protocol, a specific editor integration, a specific context-selection strategy, and a specific vendor’s execution environment, then you have not escaped implementation detail.

You have acquired a new implementation detail.

Calling that an abstraction layer does not make the coupling disappear.

It only makes the coupling harder to see.

[![Image 16](https://substackcdn.com/image/fetch/$s_!64fQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F154aee2e-34d4-4f0b-9804-592064b702f3_1024x559.png)](https://substackcdn.com/image/fetch/$s_!64fQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F154aee2e-34d4-4f0b-9804-592064b702f3_1024x559.png)

The evidence around LLM coding tools is not a clean victory lap. It is context-dependent, and the context matters more than the demo.

There are controlled studies where coding assistants improve completion time on bounded programming tasks. One well-known GitHub Copilot study found that developers using Copilot completed a JavaScript _Hypertext Transfer Protocol_ (HTTP) server task 55.8 percent faster than the control group.

That is real evidence. But it is evidence about a specific task shape, not proof that agentic development abstracts software engineering.

There are also studies that complicate the story.

METR studied 16 experienced open-source developers across 246 tasks in mature repositories they knew well. Participants expected AI to reduce completion time. After the study, they also believed it had helped. The measured result was different: the AI-assisted condition took 19 percent longer in that setting.

That does not prove AI coding tools are useless. It proves the serious point: perceived productivity, local output, and actual system-level throughput are not the same thing.

DORA and FAROS are looking through different windows.

DORA captures perception, capabilities, and organizational self-reporting. FAROS captures telemetry from engineering systems. One tells us how teams experience AI adoption and what capabilities they believe matter. The other looks at downstream signals such as review time, bugs, incidents, churn, and production strain.

The disagreement is useful because the article is precisely about that gap.

A team can feel faster while the system becomes harder to review. A developer can feel more productive while the codebase becomes harder to maintain. A dashboard can show more completed tasks while production absorbs more defects.

That gap is where the bill hides.

FAROS should not be treated as the final word. It is vendor telemetry from one platform, and observational telemetry cannot settle causality by itself. But it is still useful because it measures the part of the system that self-reported productivity often misses: review queues, churn, incidents, bugs, and production strain.

That makes it relevant to this article.

The question is not only whether AI helps developers produce more. It often does. The sharper question is whether the rest of the engineering system can absorb that output without turning acceleration into rework.

That is where the numbers become uncomfortable.

FAROS’s 2026 AI Engineering Report analyzes roughly two years of telemetry from 22,000 developers and 4,000 teams. The throughput numbers are real: task completion is up 34 percent, epics completed per developer are up 66 percent, and code-related tasks are up 210 percent. If all you count is output, the story looks great.

Then the bill arrives.

In the same report, bugs per developer are up 54 percent, the incidents-to-pull-request ratio is up 242.7 percent, median review time is up roughly five times, and pull requests merged without review are up 31.3 percent. Average pull request size is up 51.3 percent and average files edited per pull request are up 59.7 percent. For the subset of organizations instrumenting deployment frequency and lead time, deployment frequency is down and lead time is up sharply.

FAROS calls this “Acceleration Whiplash.” That phrase earns its place. It names the thing this article is arguing: the acceleration is real, but the system receiving the output was not designed to absorb it. More code is not the same as more trustworthy software. More completed tasks are not the same as less risk. More merged pull requests are not the same as delivery.

The important part is not that FAROS is the final word. The important part is that its failure pattern matches the mechanism: output rises locally, verification cost rises downstream, and the organization mistakes motion for progress until the review queue, incident queue, and maintenance queue start sending invoices.

Benchmarks such as SWE-bench Verified are also useful. SWE-bench Verified evaluates models and agents on real-world software issues from open-source repositories, and it gives the industry a better shared measurement surface than demos. But benchmark success is not the same as long-term product ownership.

Research on whether “solved” SWE-bench issues are really solved correctly adds another warning. A patch can satisfy the benchmark harness and still miss developer intent, introduce an overfitted fix, or rely on behavior that would be rejected by maintainers.

A generated patch can pass available tests and still fail to match developer intent. A solved issue can still create future maintenance cost. A benchmark can measure issue resolution, but it does not fully measure conceptual integrity, domain understanding, architectural fit, operability, support load, or the cost paid by the next developer.

This is exactly the kind of evidence we should expect if LLM tools reduce some local production cost while increasing verification and maintenance cost elsewhere.

The empirical picture does not support a simple slogan like “agents make developers obsolete” or “agents are useless.” Both are lazy.

The more accurate reading is harder:

LLM agents can be valuable in certain task classes, but the total outcome depends on task type, codebase familiarity, context quality, verification strength, review cost, security exposure, and long-term maintenance burden.

That is not marketing.

That is engineering.

[![Image 17](https://substackcdn.com/image/fetch/$s_!8-vd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0980ac6-2194-4585-9742-66424062fd77_1024x559.png)](https://substackcdn.com/image/fetch/$s_!8-vd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0980ac6-2194-4585-9742-66424062fd77_1024x559.png)

If an organization wants to claim that agents are raising the level of abstraction, it should be able to show where the cost went.

Not vibes. Not developer sentiment. Not a demo where a feature appears in three minutes. Not a dashboard that counts accepted suggestions and calls it productivity.

Real delivery evidence.

This is where DORA and _Accelerate_ still matter. Deployment frequency, lead time for changes, change failure rate, and time to restore service are not perfect metrics, but they ask the right kind of question: did the system get better at delivering change safely? They do not confuse typing speed with delivery.

For agentic development, the measurement surface has to get wider:

1.   Pull request size by human-authored, AI-assisted, and agent-authored work

2.   Review time by task class and risk level

3.   Human review comments separated from agent review comments

4.   Unreviewed merge rate

5.   Reopened ticket rate

6.   Bugs per pull request

7.   Incidents per pull request

8.   Lead time from commit to production

9.   Work restarts after review or testing

10.   Code churn by provenance, especially recently generated code deleted soon after merge

11.   Test changes made together with implementation changes

12.   Architectural boundary violations caught after the fact  
These metrics are not a morality test. They are how a team finds the bill.

If agent usage rises and pull request size rises, review time rises, incidents per pull request rise, and unreviewed merges rise, the organization did not buy an abstraction layer. It bought a faster way to manufacture review debt.

If agent usage rises while lead time improves, change failure rate stays controlled, review remains bounded, generated changes stay small, and human review comments feed back into better agent rules, then the organization may be building something real.

The difference is not enthusiasm.

It is whether the organization can see where the work moved.

[![Image 18](https://substackcdn.com/image/fetch/$s_!Lzqf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b93a4e9-fa52-4f88-a222-5b729210ba81_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Lzqf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b93a4e9-fa52-4f88-a222-5b729210ba81_1024x559.png)

A serious critique should not pretend there is no value.

There is value.

LLM agents can be useful when the cost of being slightly wrong is low, the feedback loop is fast, and the verification mechanism is independent of the generated output.

They are especially useful for exploration. An agent can summarize files, trace call paths, locate likely extension points, and generate hypotheses. The output should be treated as a guide, not as truth.

They are useful for first drafts. Boilerplate, adapters, migrations, test skeletons, documentation drafts, release-note drafts, and repetitive transformations can be accelerated when review is cheap and responsibility remains clear.

They are useful for mechanical change. Renames, API migrations, formatting changes, and broad but simple edits can fit the agentic loop when automated checks are strong and the scope is controlled.

They are useful for generating alternatives. Agents can propose multiple designs, compare trade-offs, and surface options a developer can evaluate.

They are useful for disposable prototypes. When learning is the goal and production quality is not yet required, agentic speed can be an advantage.

They are useful for test discovery. Agents can suggest missing cases, edge conditions, and characterization scenarios. They should not be trusted to define correctness alone.

They are useful for translation between representations. They can help move from notes to documentation, from examples to scaffolding, from API descriptions to client snippets, from logs to incident summaries, and from design conversations to decision records.

In these cases, the agent is not a mature abstraction over development.

It is a power tool. Power tools are useful. Power tools also remove fingers when treated as magic.

[![Image 19](https://substackcdn.com/image/fetch/$s_!W7VL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a61d51-2563-43d1-8e86-f09c0de4ff7d_1024x559.png)](https://substackcdn.com/image/fetch/$s_!W7VL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a61d51-2563-43d1-8e86-f09c0de4ff7d_1024x559.png)

The abstraction claim collapses when the work requires deep semantic ownership.

It collapses in domain-heavy systems where correctness lives in business rules that are not fully written down. It collapses in legacy codebases where the important knowledge is buried in production behavior, old incidents, implicit team conventions, and accidental dependencies.

It collapses in distributed systems where the difficulty is not the syntax of the change but the interaction between time, failure, retries, state, observability, and rollback.

It collapses in security-sensitive work where excessive agency, prompt injection, insecure output handling, plugin design, and overreliance are not academic risks. They are system design concerns.

It collapses in product development when the hard part is deciding what not to build. Agents can generate code faster than organizations can validate value. More code with more uncertainty is not progress. It is inventory.

It collapses in refactoring when the goal is not to move text around, but to preserve behavior while improving design. A refactoring is only a refactoring if behavior is preserved. A plausible diff is not enough.

It collapses in _Test-Driven Development_ (TDD) when the agent writes the tests and the implementation from the same vague instruction, because the test may only encode the model’s misunderstanding. The discipline of TDD is not “tests exist.” It is using tests to create feedback, clarify design, and protect behavior through small steps.

It collapses in architecture when the generated solution optimizes local elegance while damaging global coherence. An agent can write a nice class that should not exist. It can introduce an abstraction that solves today’s prompt and becomes tomorrow’s tax.

The pattern is consistent.

Where independent verification is strong, agents can help.

Where verification depends on human judgment, domain knowledge, and architectural taste, the cost comes back.

[![Image 20](https://substackcdn.com/image/fetch/$s_!0_jE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3261ecff-540e-43b7-9b5e-3d6a5934e52a_1024x559.png)](https://substackcdn.com/image/fetch/$s_!0_jE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3261ecff-540e-43b7-9b5e-3d6a5934e52a_1024x559.png)

A technology should not be called an abstraction layer just because it hides complexity.

It should pass a harder test.

1.   What can I safely stop thinking about?

2.   Which details are hidden, and why are they safe to hide?

3.   What semantics are preserved?

4.   What contract does the layer provide?

5.   What failure modes are explicit?

6.   How do I observe and debug the boundary?

7.   Can I replace the implementation without changing the caller’s mental model?

8.   Does it reduce cognitive load, or does it move the burden to review?

9.   Does it make errors easier to detect, or more fluent and harder to notice?

10.   Who owns correctness when the layer fails?  
Most current agentic development setups fail this test for software development as a whole.

They may pass it for narrow, well-bounded workflows.

That distinction matters.

An agent that formats files under strict rules, inside a sandbox, with deterministic checks, and no authority to change behavior may be part of a useful automation layer.

An agent that generates a production change from a vague issue, edits code and tests together, invents missing context, and relies on a tired senior developer to catch the difference between plausible and correct is not an abstraction layer.

It is an attention loan.

And like all loans, someone pays interest.

[![Image 21](https://substackcdn.com/image/fetch/$s_!V992!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F140c1481-933d-4e5f-b399-4f0c0f1c7b57_1024x559.png)](https://substackcdn.com/image/fetch/$s_!V992!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F140c1481-933d-4e5f-b399-4f0c0f1c7b57_1024x559.png)

The better mental model is not “agent as abstraction layer.”

The better mental model is “agent as unreliable collaborator inside a controlled delivery system.”

That framing is less glamorous and more useful. It forces the right questions.

What tasks are safe to delegate? What checks are independent? What permissions are necessary? What should require human approval? What context must be supplied? What should be forbidden? What evidence tells us the tool improved total flow rather than local output? What happens when the model changes? What happens when a generated patch passes tests but damages maintainability? What happens when the agent is confidently wrong?

A controlled delivery system looks more like this:

Notice where the abstraction might live.

It is not in the LLM response. It is in the policy, checks, boundaries, traceability, and ownership model around the agent.

This is where mature engineering can create real value. A team might define task classes where agentic execution is acceptable. It might require external tests before implementation. It might block changes outside allowed directories. It might run architectural fitness functions. It might record prompts, tool calls, diffs, and approvals. It might measure rework, review time, defect escape, cycle time, maintainability, and support burden.

Then, maybe, the organization has built something that behaves like an abstraction for a narrow class of work.

But that is not the same as saying “agents abstract development.”

It says:

“We built a constrained system where agents can perform specific work under explicit boundaries.”

That is a much smaller claim.

It is also a much more serious one.

There is a sharp line between these two statements:

1.   “LLM agents help me move faster in some tasks.”

2.   “LLM agents are a new abstraction layer over software development.”  
The first statement can be true.

The second statement needs evidence and a contract.

The first can be local, personal, and contextual. The second is architectural. The first can be measured through task time, review time, defects, and subjective effort. The second must explain what complexity is hidden, what semantics are preserved, what failures are bounded, and what responsibilities have genuinely moved.

Most agentic development discourse jumps from the first to the second because the second sounds more historic. It gives the moment a destiny. It lets teams feel like they are climbing the same ladder that took us from assembly to high-level languages.

But history is not a ladder.

It is also a graveyard of tools that promised to remove thinking and instead created different thinking.

The mature move is not to reject the tool.

The mature move is to refuse the myth.

LLM agentic development is not worthless. It is not trivial. It is not a toy. It can be genuinely useful, and in some contexts it can change the economics of software work.

But useful does not mean abstract.

A real abstraction gives us a model strong enough to think with. It reduces relevant cognitive load. It preserves semantics. It defines boundaries. It exposes failure in ways we can manage. It lets us ignore selected details because the system has earned that trust.

Current LLM agents have not earned that status for software development as a whole. Today, they are better understood as probabilistic execution loops that can generate, transform, and explore under supervision. Their value depends on task selection, context quality, independent verification, security boundaries, and the cost of review and maintenance.

The bullshit is not using LLM agents.

The bullshit is pretending that the unpaid verification work disappeared because we moved it behind a prompt.

If a team wants to use agents well, it should stop asking whether agents are the future and start asking harder questions.

What work are we delegating? What risk are we accepting? What checks are independent? What knowledge are we losing? What rework are we creating? What would prove that this improved the system rather than just increasing output?

That is the difference between engineering and self-deception.

Agents may help us move faster. They may help us explore, draft, transform, and automate. But speed is not abstraction. Fluency is not correctness. Delegation is not a contract.

A real abstraction lets us reason safely at another level.

Current agentic development does not do that for software development as a whole. It can be part of a controlled engineering system, but it is not itself the layer that makes the hard parts disappear.

The unpaid work did not vanish.

It moved into review, verification, security, governance, and maintenance.

Calling that an abstraction layer is not technical clarity.

It is self-deception with better branding.

An abstraction layer is not a curtain.

It is a contract.

*   Abelson, Harold; Sussman, Gerald Jay. _Structure and Interpretation of Computer Programs_. [https://web.mit.edu/6.001/6.037/sicp.pdf](https://web.mit.edu/6.001/6.037/sicp.pdf)

*   Anthropic. _Building effective agents_. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)

*   Anthropic. _Building effective AI agents_. [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

*   Autio, Chloe; Schwartz, Reva; Dunietz, Jesse; Jain, Shomik; Stanley, Martin; Tabassi, Elham; Hall, Patrick; Roberts, Kamie. _Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile_. [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

*   Becker, Joel; Rush, Nate; Barnes, Beth; Rein, David. _Measuring the impact of early-2025 AI on experienced open-source developer productivity_. [https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

*   Becker, Joel; Rush, Nate; Barnes, Elizabeth; Rein, David. _Measuring the impact of early-2025 AI on experienced open-source developer productivity_. [https://arxiv.org/abs/2507.09089](https://arxiv.org/abs/2507.09089)

*   Bergmann, Sebastian. _Beyond Best Practices_. [https://phpunit.expert/articles/beyond-best-practices.html](https://phpunit.expert/articles/beyond-best-practices.html)

*   Bender, Emily M.; Gebru, Timnit; McMillan-Major, Angelina; Shmitchell, Shmargaret. _On the dangers of stochastic parrots: Can language models be too big_. [https://dl.acm.org/doi/10.1145/3442188.3445922](https://dl.acm.org/doi/10.1145/3442188.3445922)

*   Bommasani, Rishi; Hudson, Drew A.; Adeli, Ehsan; Altman, Russ; Arora, Simran; von Arx, Sydney; Bernstein, Michael S.; Bohg, Jeannette; Bosselut, Antoine; Brunskill, Emma; et al. _On the opportunities and risks of foundation models_. [https://arxiv.org/abs/2108.07258](https://arxiv.org/abs/2108.07258)

*   Brooks, Frederick P. _No Silver Bullet: Essence and accidents of software engineering_. [https://www.cs.unc.edu/techreports/86-020.pdf](https://www.cs.unc.edu/techreports/86-020.pdf)

*   Dijkstra, Edsger W. _The humble programmer_. [https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html](https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html)

*   DORA. _DORA metrics: The four keys_. [https://dora.dev/guides/dora-metrics-four-keys/](https://dora.dev/guides/dora-metrics-four-keys/)

*   DORA. _State of AI-assisted software development 2025_. [https://dora.dev/dora-report-2025/](https://dora.dev/dora-report-2025/)

*   Faros AI. _AI Engineering Report 2026: The Acceleration Whiplash_. [https://pages.faros.ai/hubfs/AI_Engineering_Report_2026_The_Acceleration_Whiplash_Faros.pdf](https://pages.faros.ai/hubfs/AI_Engineering_Report_2026_The_Acceleration_Whiplash_Faros.pdf)

*   Forsgren, Nicole; Humble, Jez; Kim, Gene. _Accelerate: The science of lean software and DevOps_. [https://itrevolution.com/product/accelerate/](https://itrevolution.com/product/accelerate/)

*   Huang, Lei; Yu, Weijiang; Ma, Weitao; Zhong, Weihong; Feng, Zhangyin; Wang, Haotian; Chen, Qianglong; Peng, Weihua; Feng, Xiaocheng; Qin, Bing; Liu, Ting. _A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions_. [https://arxiv.org/abs/2311.05232](https://arxiv.org/abs/2311.05232)

*   Khononov, Vlad. _Balancing coupling in software design_. [https://www.oreilly.com/library/view/balancing-coupling-in/9780137353514/](https://www.oreilly.com/library/view/balancing-coupling-in/9780137353514/)

*   Liskov, Barbara. _Data abstraction and hierarchy_. [https://www.cs.tufts.edu/~nr/cs257/archive/barbara-liskov/data-abstraction-and-hierarchy.pdf](https://www.cs.tufts.edu/~nr/cs257/archive/barbara-liskov/data-abstraction-and-hierarchy.pdf)

*   Liu, Jiawei; et al. _Large Language Model-based agents for software engineering: A survey_. [https://arxiv.org/abs/2409.02977](https://arxiv.org/abs/2409.02977)

*   Microsoft. _Reproducible output with Azure OpenAI Service_. [https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/reproducible-output](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/reproducible-output)

*   OpenAI. _Advanced usage: Reproducible outputs_. [https://developers.openai.com/api/docs/guides/advanced-usage](https://developers.openai.com/api/docs/guides/advanced-usage)

*   OpenAI. _Agents SDK_. [https://platform.openai.com/docs/guides/agents-sdk](https://platform.openai.com/docs/guides/agents-sdk)

*   OpenAI. _Responses API tools_. [https://platform.openai.com/docs/guides/tools](https://platform.openai.com/docs/guides/tools)

*   OWASP Foundation. _OWASP Top 10 for LLM applications_. [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

*   Parnas, David L. _On the criteria to be used in decomposing systems into modules_. [https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf](https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf)

*   Peng, Sida; Kalliamvakou, Eirini; Cihon, Peter; Demirer, Mert. _The impact of AI on developer productivity: Evidence from GitHub Copilot_. [https://arxiv.org/abs/2302.06590](https://arxiv.org/abs/2302.06590)

*   Schick, Timo; Dwivedi-Yu, Jane; Dessi, Roberto; Raileanu, Roberta; Lomeli, Maria; Zettlemoyer, Luke; Cancedda, Nicola; Scialom, Thomas. _Toolformer: Language models can teach themselves to use tools_. [https://arxiv.org/abs/2302.04761](https://arxiv.org/abs/2302.04761)

*   Spolsky, Joel. _The law of leaky abstractions_. [https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

*   SWE-bench. _SWE-bench Verified_. [https://www.swebench.com/verified.html](https://www.swebench.com/verified.html)

*   Wang, Lei; Ma, Chen; Feng, Xueyang; Zhang, Zeyu; Yang, Hao; Zhang, Jingsen; Chen, Zhiyuan; Tang, Jiakai; Chen, Xu; Lin, Yankai; Zhao, Wayne Xin; Wei, Zhewei; Wen, Ji-Rong. _A survey on Large Language Model based autonomous agents_. [https://arxiv.org/abs/2308.11432](https://arxiv.org/abs/2308.11432)

*   Wang, You; Pradel, Michael; Liu, Zhongxin. _Are “solved issues” in SWE-bench really solved correctly: An empirical study_. [https://arxiv.org/abs/2503.15223](https://arxiv.org/abs/2503.15223)

*   Wing, Jeannette M. _Computational thinking_. [https://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf](https://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf)

*   Wing, Jeannette M. _Computational thinking and thinking about computing_. [https://people.cs.vt.edu/~kafura/CS6604/Papers/Wing-CT-Thinking-About-Computing.pdf](https://people.cs.vt.edu/~kafura/CS6604/Papers/Wing-CT-Thinking-About-Computing.pdf)

*   Wright, Hyrum. _Hyrum’s Law_. https://www.hyrumslaw.com/
