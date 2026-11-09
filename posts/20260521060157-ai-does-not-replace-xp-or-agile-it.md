Title: AI does not replace XP or Agile. It raises the cost of pretending.

URL Source: http://emmanuelvalverderamos.substack.com/p/ai-does-not-replace-xp-or-agile-it

Final URL: https://emmanuelvalverderamos.substack.com/p/ai-does-not-replace-xp-or-agile-it

Published Time: 2026-05-21T06:01:57+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!5mzI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6dd57499-c0bb-4764-9f50-9356fc17b9f2_1024x558.png)](https://substackcdn.com/image/fetch/$s_!5mzI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6dd57499-c0bb-4764-9f50-9356fc17b9f2_1024x558.png)

An airport installs new self-check-in kiosks.

The machines are fast. Passengers print boarding passes in seconds. The queue at the entrance almost disappears. Managers look at the dashboard and celebrate: more passengers processed per minute, fewer staff needed at the counter, less waiting at the first visible step.

Then the rest of the airport starts to bend. Security cannot absorb the new flow. Bags arrive at the wrong belt. Boarding gates fill too early. More passengers reach the gate before the aircraft is ready. Some miss flights because the bottleneck did not disappear. It moved.

From the passenger’s point of view, the airport did not become better. They do not care how quickly a boarding pass was printed if the plane leaves late, the bag is lost, or the connection is missed. The machine made one part of the system faster. It did not make the journey better.

Much of the current conversation about _Artificial Intelligence_ (_AI_) and software development confuses a faster station with a better journey.

Coding agents can produce code, tests, refactors, documentation, migrations, and pull requests faster than many teams were used to. That matters. It changes the economics of code production. It changes the shape of daily work. It changes what is cheap to try.

But it does not change what software is accountable for.

Users still care whether the product helps them, whether existing behaviour works after a release, whether the system is available when needed, whether incidents are resolved quickly, and whether each change increases or decreases their trust.

The business still cares whether software creates value, reduces risk, preserves optionality, improves time to market, and remains economically possible to own. The system still cares whether changes are coherent, tested, integrated, observable, recoverable, maintainable, and aligned with reality.

None of that disappears because the code came from a coding agent.

That is why the claim that _AI_ replaces _Extreme Programming_ (_XP_) or Agile is backwards. _AI_ does not make those disciplines less relevant. It makes the absence of those disciplines more expensive.

[![Image 2](https://substackcdn.com/image/fetch/$s_!Fnls!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98dfb6f9-0b40-4e08-bed0-c3ce65c82e23_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Fnls!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98dfb6f9-0b40-4e08-bed0-c3ce65c82e23_1024x559.png)

*   _AI_ coding agents can increase code production. They can also improve local efficiency by reducing the effort required to produce certain artefacts. But software development is judged by effectiveness: whether a team turns ideas into valuable, reliable, working software in users’ hands, while preserving the ability to change the system again tomorrow.

*   Code was not the final output before _AI_, and it is not the final output now. The output that matters is value.

*   If a team generates one hundred times more code but delivers value later, breaks existing functionality more often, increases review load, or takes longer to recover from incidents, the system did not improve. It became busier.

*   That distinction explains why the evidence around _AI_ looks mixed. A controlled GitHub Copilot study found that developers completed a bounded JavaScript task 55.8% faster with Copilot. METR’s 2025 randomized controlled trial found that experienced open-source developers working on familiar repositories took 19% longer when _AI_ tools were allowed. DORA 2025 frames _AI_ as an amplifier of organisational strengths and weaknesses, not as a substitute for the underlying system. Faros’ 2026 telemetry reports higher throughput signals alongside larger pull requests, more bugs per pull request, longer review time, more incidents per pull request, and more code churn.

*   Agile and _XP_ were not meant to be ceremonies. Agile points toward early and continuous delivery of valuable software, working software, collaboration, technical excellence, simplicity, and adaptation. _XP_ gives those ideas sharper engineering teeth through short cycles, automated tests, _Test-Driven Development_ (_TDD_), refactoring, incremental design, small releases, shared ownership, and frequent integration.

*   The better question is not: “Can _AI_ write the code?” It can.

*   The better question is: “What keeps generated change aligned with user value, system behaviour, design integrity, and operational reality once it enters a living system?” That question brings Agile and _XP_ back into focus.

1.   Code was never the outcome

2.   Productivity, efficiency, and effectiveness are not the same thing

3.   _AI_ made one station faster, not the whole system

4.   Output is not effectiveness

5.   The user does not care who wrote the code

6.   The story of a cheap change

7.   _AI_ does not replace Agile. It exposes fake Agile

8.   _AI_ does not replace _XP_. It exposes weak feedback

9.   _Test-Driven Development_ (_TDD_) as executable intent

10.   _Trunk-Based Development_ as integration discipline

11.   _Continuous Delivery_ as value flow

12.   Refactoring as economic control

13.   Small batches as protection against generated inventory

14.   Pairing, review, and shared judgment

15.   “Use _AI_” is not a strategy

16.   What teams should measure now

17.   Conclusions

18.   References

[![Image 3](https://substackcdn.com/image/fetch/$s_!-z89!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f754e42-001b-4e30-94b0-40e577767380_1024x558.png)](https://substackcdn.com/image/fetch/$s_!-z89!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f754e42-001b-4e30-94b0-40e577767380_1024x558.png)

A team can generate a thousand lines of code before lunch and still be no closer to improving a user’s life. It can close tickets, merge pull requests, update dashboards, and produce beautiful internal reports while the product becomes slower, less reliable, harder to change, and more confusing to operate.

This was true before _AI_. _AI_ has made the truth harder to ignore.

Software development has always suffered from a dangerous substitution: treating code as the output because code is visible, countable, reviewable, and easy to attach to individual activity. Code feels like progress because it is concrete. It appears in a repository. It moves through a pull request. It can be counted by tools that have no understanding of whether the change should exist.

But code is not value by itself.

Code is a liability until it earns its keep. It consumes attention. It needs to be understood, tested, secured, deployed, observed, documented, maintained, adapted, and eventually removed. It can create revenue, reduce cost, enable learning, improve user experience, and open future options. It can also increase basal cost, create cognitive drag, slow future change, expand the blast radius of incidents, and make the next valuable decision harder.

That is why cheap code is not the same as cheap software. Lowering the cost of creation does not remove the cost of ownership. It can increase the temptation to create more than the system can economically carry.

This is the core economic trap in _AI_-assisted development. The easiest part to accelerate is not always the part limiting the system’s ability to create value. The cost was not only writing the code. The cost was carrying it, changing it, trusting it, operating it, explaining it, and recovering when it behaved differently from what people expected.

A user does not experience code production. The user experiences the product.

They experience whether the flow helps them complete a task. They experience whether payment works. They experience whether yesterday’s feature still works after today’s release. They experience whether the system is available when they need it. They experience whether support can explain what happened. They experience whether the team recovers quickly when something fails.

A user does not care that a team generated one hundred times more code if the feature arrives later. They do not care that a coding agent produced a clever implementation if every release breaks something they depend on. They do not care that development looked cheaper if incidents now take thirteen hours to resolve.

From the user’s side of the glass, only the outcome counts.

[![Image 4](https://substackcdn.com/image/fetch/$s_!jhTy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F068cb451-c28c-4e0f-8889-c6696649f16e_1024x558.png)](https://substackcdn.com/image/fetch/$s_!jhTy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F068cb451-c28c-4e0f-8889-c6696649f16e_1024x558.png)

A lot of the _AI_ conversation becomes confused because it uses the word “productivity” as if it meant everything good.

It does not.

Productivity is about output per unit of input. In software, this might mean more code, more generated tests, more pull requests, more completed tickets, more documentation, or more artefacts per developer-hour.

Efficiency is about using fewer resources or less waste to produce that output. A developer may spend less time typing boilerplate. A team may spend less effort scaffolding repetitive code. A coding agent may reduce the human effort needed to produce a first draft.

Effectiveness is different. Effectiveness is about achieving the intended outcome. In software, that means delivering valuable, reliable, usable, maintainable software to users, while preserving the ability to change the system again tomorrow.

The trap is that _AI_ can improve productivity and efficiency locally while damaging effectiveness systemically.

A team can produce more code and still deliver value later. It can type less and still spend more time reviewing, correcting, integrating, debugging, and explaining. It can generate more pull requests and still increase lead time. It can create more tests and still miss the behaviour that matters. It can ship more often and still reduce user trust if each release becomes less reliable.

This is the distinction the industry keeps blurring.

More output is not automatically better software. Less effort is not automatically better economics. Faster local production is not automatically better value flow.

The real question is not whether _AI_ makes teams more productive at producing code. In many contexts, it can. The real question is whether that extra output improves delivery effectiveness, or merely increases the amount of work the system must verify, integrate, operate, and eventually pay for.

_AI_ can make teams more productive at producing code, and less effective at delivering value.

The wrong question is: “Can _AI_ write the code?”

Of course it can.

It can write plausible code. It can modify existing code. It can scaffold tests. It can propose refactorings. It can explain APIs. It can migrate syntax. It can generate examples. It can produce a full vertical slice faster than many teams could manually type the first draft a few years ago.

The important question is whether the resulting change deserves to enter the system. That means asking:

1.   Does it express the right product intent?

2.   Does it preserve existing behaviour?

3.   Does it fit the design?

4.   Does it reduce or increase the future cost of change?

5.   Does it make incidents easier or harder to diagnose?

6.   Does it create more knowledge in the team, or move knowledge into a prompt transcript nobody will read again?

7.   Does it make the system easier to evolve, or does it merely make the pull request look complete?  
_AI_ changes how fast change can be proposed. It does not automatically improve how safely change can be accepted.

A generated pull request is not value. It is a claim on future judgment. Someone, or some combination of people and tools, still has to decide whether the change is correct, valuable, coherent, reversible, observable, and worth carrying. The scarce resource is no longer typing. In many teams, the scarce resource is judgment.

And judgment is exactly where weak Agile and weak _XP_ collapse.

A team that already had unclear product strategy will use _AI_ to generate faster ambiguity. A team that already had poor test discipline will generate more code with weak behavioural protection. A team that already had slow review will feed the review queue faster. A team that already avoided refactoring will accumulate generated design damage faster. A team that already confused activity with progress will finally get activity at industrial scale.

That is not transformation. It is acceleration without steering.

[![Image 5](https://substackcdn.com/image/fetch/$s_!mWGG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1941cb02-12b0-4490-9615-905bc01c7588_1024x558.png)](https://substackcdn.com/image/fetch/$s_!mWGG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1941cb02-12b0-4490-9615-905bc01c7588_1024x558.png)

The serious _AI_ conversation is not whether coding agents can increase output. In many contexts, they can. A team can generate more code, draft more tests, produce more pull requests, and move faster through the visible act of implementation. That may be an increase in local productivity. It may even be an increase in local efficiency if less human effort is needed to produce the same kind of artefact.

But software development is not judged by output alone. It is judged by effectiveness: whether the team turns ideas into valuable, reliable, working software in users’ hands, while preserving the ability to change the system again tomorrow.

That distinction explains why the evidence looks mixed.

The GitHub Copilot study by Peng, Kalliamvakou, Cihon, and Demirer found that developers with Copilot completed a bounded JavaScript HTTP server task 55.8% faster than the control group. That is evidence of improved local task throughput in a constrained setting. It does not prove improved delivery effectiveness across a living software system.

METR’s 2025 randomized controlled trial looked at experienced open-source developers working on real issues in mature repositories they already knew. In that setting, developers expected _AI_ to help and later believed it had helped, but measured completion time was 19% slower when _AI_ was allowed. That result does not prove _AI_ slows all work. It shows that once context, existing design, review expectations, tests, documentation, and repository reality enter the picture, local generation speed is no longer the same thing as system effectiveness.

Faros’ 2026 telemetry points in the same direction. It reports higher throughput signals alongside larger pull requests, more bugs per pull request, longer review time, more incidents per pull request, and more churn. That should be treated as vendor telemetry, not universal causal proof. But it is exactly the kind of signal we should expect when output increases faster than the delivery system can absorb it.

DORA’s work sharpens the point: _AI_ is an amplifier of the system it enters. Strong systems can convert _AI_ assistance into better outcomes. Weak systems can convert _AI_ assistance into more noise, more queues, and more expensive rework.

The lesson is not “_AI_ is good” or “_AI_ is bad.” The lesson is that output, efficiency, and effectiveness are different things. _AI_ can improve the first two locally while damaging the third systemically.

A station can get faster while the journey gets worse. A developer can feel more productive while the delivery system becomes more fragile. A tool can improve local output while feeding the real constraint.

The airport prints boarding passes faster. The plane still leaves late.

A user does not experience your development process. They do not experience your prompts, your agents, your workflow graph, your automation scripts, your pull request template, or your internal output dashboard. They experience the product.

They experience whether the feature solves their problem. They experience whether yesterday’s behaviour still works today. They experience whether the system is available when they need it. They experience whether support can help them when something goes wrong. They experience whether they can trust the product after every release.

This is where much of the _AI_ conversation goes wrong. It treats code production as if it were the final output of software development. It is not. Code is inventory until it is safely integrated, delivered, operated, learned from, and converted into value.

Generating one hundred times more code is not impressive if the user receives value at the same speed. It is worse than unimpressive if the extra code increases defects, slows review, expands cognitive load, and makes incidents harder to resolve.

A team can look faster from the inside while becoming slower from the outside. Developers see more code generated. Managers see more pull requests. Dashboards show more activity. But the user sees broken flows, delayed features, unstable releases, and slower recovery when something fails.

That is not acceleration. It is local optimisation wearing a value costume.

A simple diagram helps here, as long as it does not try to place agentic programming inside _XP_. That would make the wrong thing central. The important distinction is not how much work enters the system, but whether the system can turn that work into value without losing trust.

![Image 6](https://substackcdn.com/image/fetch/$s_!FDzW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73c6ef15-f51e-4420-893a-845575294606_3636x588.png)

The real conversation is not where to place agentic workflows in a process diagram. The real conversation is whether the system can absorb generated change without damaging value, reliability, delivery, recovery, and trust.

[Illustrative example] Imagine a team working on a subscription product. A new discount rule is needed for enterprise customers who renew early. The rule sounds small. The agent receives a prompt with the ticket, the relevant files, and a short explanation from the developer. In a few minutes, it modifies the pricing service, updates a couple of tests, adds a new case to the invoice preview, and writes a clean pull request description.

Everything looks efficient.

The build is green. The diff is bigger than expected, but most of it looks reasonable. The reviewer is busy. The generated explanation sounds coherent. The tests cover the happy path. The pull request is approved because the team is under pressure and the change seems low risk.

That night, invoices are generated incorrectly for a subset of customers who have an old negotiated contract. The old exception was not in the prompt. It was not in the ticket. It was not in the tests. It lived in a corner of the domain that two people knew about, one comment vaguely hinted at, and the existing code handled through an unpleasant conditional nobody liked.

Support sees the problem first. Finance escalates. Engineering starts digging. The code was generated quickly, but the intent was not preserved durably. The reviewer did not reconstruct the domain rule. The tests did not express the old contract exception. The pull request was easy to produce and expensive to trust. The team spends hours finding the affected invoices, understanding the blast radius, patching the rule, and explaining what happened.

The code was cheap. The change was expensive.

This example is not an argument against using _AI_. A human could have made the same mistake. That is the point: the fundamentals did not change.

If the behaviour matters, it needs to be understood.

If the rule matters, it needs to be expressed.

If the risk matters, it needs to be controlled.

If trust matters, the system needs feedback loops strong enough to catch wrongness before users pay for it.

_AI_ can help produce the change. It cannot, by itself, decide what the change must not break.

[![Image 7](https://substackcdn.com/image/fetch/$s_!U1b1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70b8f839-bdb8-4089-86da-0006b7824a9c_1024x558.png)](https://substackcdn.com/image/fetch/$s_!U1b1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70b8f839-bdb8-4089-86da-0006b7824a9c_1024x558.png)

Agile was not supposed to mean stand-ups, Jira rituals, velocity theatre, roadmap theatre, or a sprint-shaped waterfall with better branding. The Agile Manifesto values individuals and interactions, working software, customer collaboration, and responding to change. Its principles put customer satisfaction through early and continuous delivery of valuable software first. They also emphasise frequent delivery of working software, daily collaboration between business people and developers, sustainable development, technical excellence, good design, simplicity, self-organising teams, and regular reflection.

That is not tool worship. It is a theory of software development under uncertainty.

_AI_ does not remove that uncertainty. It can reduce some friction in exploring possible implementations, but it does not know which customer problem matters most by itself. It does not decide what tradeoff is economically sound. It does not turn a list of disconnected tickets into strategy. It does not convert a vague roadmap into product judgment. It does not make value appear because the backlog moved faster.

In fact, _AI_ can make fake Agile look better for a while.

A team can generate more of almost everything:

1.   Stories

2.   Acceptance criteria

3.   Tasks

4.   Estimates

5.   Summaries

6.   Release notes

7.   Pull requests

8.   Diagrams

9.   Meeting notes  
The surface area of movement expands. The theatre becomes cheaper, faster, and more convincing.

But if the team does not have a clear diagnosis of the problem, a coherent product strategy, a staged path of learning, and a way to validate outcomes, _AI_ will only decorate confusion.

Bad Agile asks: “How many tickets did we close?” Real Agile asks: “Did valuable working software reach users sooner, with feedback that changes what we do next?”

Bad _AI_ adoption asks: “How much code did we generate?” Serious _AI_ adoption asks: “Did we improve the system’s ability to deliver valuable change safely?”

That distinction matters because “use _AI_” is not a strategy. It is an instruction. Strategy requires diagnosis, terrain, constraints, capabilities, tradeoffs, and coherent action. Without those things, _AI_ adoption becomes another way to confuse movement with progress.

The same applies to product work. A roadmap is not a strategy, and a timeline is not a roadmap. Strategy explains the challenge and the logic of response. A roadmap communicates staged movement. A timeline schedules specific actions. Collapse those distinctions and you get visible movement, hidden confusion, and false certainty. _AI_ makes that theatre cheaper to produce.

That is why _AI_ does not replace Agile. It raises the cost of pretending to be Agile.

A team that truly values working software over paperwork should ask whether _AI_ is helping get valuable, validated changes to users sooner. A team that truly values customer collaboration should ask whether _AI_ is improving contact with reality, or just producing plausible artefacts about reality. A team that truly values responding to change should ask whether _AI_ is preserving optionality, or just increasing the cost of future movement.

The Agile question is not: “Are we using the new tools?” The Agile question is: “Are we learning faster, delivering valuable software sooner, and adapting without losing technical and human sustainability?”

_XP_ is even more exposed to misunderstanding because many people reduce it to practices: pair programming, _Test-Driven Development_ (_TDD_), refactoring, continuous integration, small releases, stories, planning cycles. But in _Extreme Programming Explained_, Kent Beck and Cynthia Andres do not present _XP_ as a bag of ceremonies. They present it as a discipline for social change, technical excellence, feedback, communication, simplicity, courage, respect, and risk reduction.

That matters in the _AI_ era because _AI_ attacks the system at exactly the points _XP_ was designed to strengthen.

_AI_ increases the amount of proposed change. _XP_ asks for short cycles and fine-grained feedback. _AI_ can produce plausible code that misses intent. _XP_ asks for tests, customer involvement, and communication. _AI_ can make accidental complexity easier to create. _XP_ asks for simplicity, refactoring, and incremental design.

_AI_ can make large batches tempting because generation feels cheap. _XP_ asks for small steps, frequent integration, and frequent delivery. _AI_ can isolate people behind tools. _XP_ asks for collaboration, shared understanding, and collective responsibility. _AI_ can turn confidence into a hallucinated feeling of progress. _XP_ asks for concrete feedback from tests, integration, users, and running software.

This is why _XP_ was never a typing strategy. It was a feedback strategy.

The practices matter because they interact. Tests without refactoring can freeze bad design. Refactoring without tests can become unsafe editing. Continuous integration without small batches can become a slow gate at the end of a queue. Pairing without shared ownership can become isolated mentoring. Planning without real customer involvement can become backlog administration. _XP_ matters because it treats software development as a system of mutually reinforcing feedback loops, not a list of isolated rituals.

Beck and Andres’ principle of flow is especially relevant here. They warn that software has often delivered value in large chunks, and that when teams respond to stress by making chunks bigger, feedback gets worse and risk rises. Their direction is the opposite: deploy smaller increments of value more frequently.

_AI_ changes who, or what, can propose the next edit. It does not change the need to know whether the edit belongs.

[![Image 8](https://substackcdn.com/image/fetch/$s_!c2ks!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff92e4128-d535-47eb-b4b3-cb1182183e3c_1024x558.png)](https://substackcdn.com/image/fetch/$s_!c2ks!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff92e4128-d535-47eb-b4b3-cb1182183e3c_1024x558.png)

In a world where code generation is cheap, intent becomes expensive.

This is where _Test-Driven Development_ (_TDD_) becomes much more than a programmer habit. It becomes a way of making intent executable before production code starts to accumulate. A test is not only a check. At its best, it is a concrete example of behaviour the system should provide. It gives the team a small, objective target. It narrows the scope of generation. It gives reviewers something better than taste to discuss.

Without executable intent, _AI_ can satisfy the shape of the request while missing the reason behind it. A prompt can be ambiguous. A story can be too broad. A design note can hide assumptions. A generated implementation can look idiomatic while breaking an invariant that lived only in someone’s head. A reviewer can scan style and still miss behaviour.

The risk is not that _AI_ always writes bad code. The risk is that it often writes plausible code, and plausibility is expensive to review.

_TDD_ changes the conversation. Before asking an agent to implement, the team asks:

1.   What behaviour should be true?

2.   What example would fail today?

3.   What existing behaviour must remain unchanged?

4.   What edge case matters?

5.   What would give us confidence that the change is real?

6.   What would reveal that the generated code misunderstood the problem?  
That is not ceremony. That is steering.

In the _AI_ era, a failing test is a better prompt than a vague instruction. It says, in executable form, what reality should look like after the change. It also creates a limit. Once the test passes, the team can ask whether the implementation is simple, whether the design improved or degraded, whether the test expresses behaviour rather than structure, and whether another example is needed.

This is where _Test-Driven Development_ (_TDD_) protects against one of _AI_’s strongest temptations: excess. When the cost of writing code drops, the temptation to write “just in case” code rises. _TDD_ forces the next behaviour to earn its way into the system through a concrete example, a failing check, and a small step toward working software.

A team using _AI_ without executable intent may get faster code. A team using _AI_ with strong examples, _TDD_, and fast feedback may get safer learning.

Those are different outcomes.

[![Image 9](https://substackcdn.com/image/fetch/$s_!tkuh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35527b75-be9c-4241-a008-eac0b80c996b_1024x558.png)](https://substackcdn.com/image/fetch/$s_!tkuh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35527b75-be9c-4241-a008-eac0b80c996b_1024x558.png)

Generated change becomes dangerous when it stays away from the shared system for too long.

A coding agent can produce a large branch quickly. It can modify many files, create tests, change configuration, and rewrite behaviour before anyone else has integrated related work. The branch looks like progress because it contains a lot of movement. But until it returns to the shared line of development, it is still a private version of reality.

This is where _Trunk-Based Development_ matters.

_Trunk-Based Development_ keeps collaboration centred on a single shared branch, usually called trunk or main. The discipline is not merely naming a branch “main.” The discipline is integrating small changes frequently, avoiding long-lived development branches, and keeping the shared codebase releasable. Hammant describes it as collaboration on a single shared branch where commits are written back to trunk, long-lived development branches are resisted, and every commit should still produce a production-ready build.

Short-lived branches can support review and automated checking, but they must remain short-lived. They should not become warehouses for generated work. Hammant explicitly describes short-lived feature branches as suitable for review and automated build checking, but not for artifact creation or publication.

In an _AI_-assisted team, this becomes more important, not less. If agents increase the rate at which changes are proposed, long-lived branches become divergence machines. Every hour a generated change stays away from trunk is an hour in which assumptions can age, neighbouring changes can conflict, tests can stop representing the real system, and reviewers can lose context.

The problem is not that branches exist. The problem is that delayed integration hides the real cost of change.

_Trunk-Based Development_ forces generated work to meet shared reality quickly. It keeps feedback close to the act of change. It reduces the distance between “the agent produced something” and “the team knows whether this belongs in the system.”

A pull request is not integration. A CI server is not integration. A branch named main is not _Trunk-Based Development_. Integration happens when change joins the shared line of development quickly enough that divergence does not become its own hidden system.

A team that generates code quickly but integrates slowly has not improved delivery. It has increased the speed at which divergence is created.

[![Image 10](https://substackcdn.com/image/fetch/$s_!RaGt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b9743a1-2792-4ca9-92f2-d502cba921d9_1024x558.png)](https://substackcdn.com/image/fetch/$s_!RaGt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b9743a1-2792-4ca9-92f2-d502cba921d9_1024x558.png)

Integration is not the final outcome. Integrated code is still not value until it can be safely delivered, operated, and learned from.

_Continuous Delivery_ is the discipline of making the path from idea to realised business value shorter, safer, more repeatable, and more reliable. Its point is not deployment theatre. Its point is reducing the time and risk between deciding that a change matters and having that change available to users.

Humble and Farley frame cycle time as the time from deciding a change is needed to having it in production, and they describe the goal as making the path from idea to realised business value shorter and safer. They also make the economic point directly: software delivers no revenue until it is in the hands of users.

That distinction matters in the _AI_ era.

A coding agent can make implementation feel fast, but if releasing still takes days, weeks, or months, the user has not received value sooner. If the path to production is manual, fragile, stressful, or poorly understood, faster code production just creates more waiting work. If every release is risky, generated changes accumulate as inventory.

_Continuous Delivery_ asks a harder question: can every valuable change move through build, test, deployment, release, operation, and feedback with enough speed and confidence that the team can learn from reality?

That is effectiveness.

Not code generated. Not pull requests opened. Not tickets moved. Usable software, safely delivered, in the hands of users.

Humble and Farley’s framing is useful here because they do not treat delivery as mere speed. They connect delivery to feedback: any change should trigger feedback, feedback should arrive as soon as possible, and the delivery team should receive and act on it. Their feedback process includes build, unit tests, quality checks, acceptance tests, nonfunctional tests, exploratory testing, and customer demonstration where relevant.

In a world with _AI_ coding agents, _Continuous Delivery_ becomes the economic test of the whole system. It reveals whether faster production becomes earlier value, or whether it becomes a larger queue in front of release.

The point is not to generate more change. The point is to make valuable change safely releasable.

[![Image 11](https://substackcdn.com/image/fetch/$s_!Hw13!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17dcd5f7-5bdc-4b6c-9793-b4f0c10c46a8_1024x558.png)](https://substackcdn.com/image/fetch/$s_!Hw13!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17dcd5f7-5bdc-4b6c-9793-b4f0c10c46a8_1024x558.png)

Refactoring is often reduced to “cleaning code.” That reduction is dangerous. Martin Fowler defines refactoring as changing the internal structure of software to make it easier to understand and cheaper to modify without changing observable behaviour.

That definition gives us the economic point.

Refactoring is not aesthetic polishing. It is a way to manage the future cost of change. It protects understandability, modifiability, and design integrity. It helps keep the cost of the next valuable change from rising silently. It is how a team pays down accidental complexity before it compounds into delivery drag.

_AI_ makes this more important because generated code can add behaviour faster than it preserves conceptual integrity.

An agent can fit into local style while still weakening the model. It can duplicate logic rather than discovering the right abstraction. It can add conditionals where a better responsibility split is needed. It can satisfy the visible test while making the next change harder. It can produce code that is syntactically acceptable and semantically expensive.

The danger is not only bad code. The danger is adequate code in the wrong place.

This is where _XP_’s incremental design matters. Incremental design is not speculative architecture. It is the daily investment required to keep the design aligned with what the team now understands. That is the opposite of letting generated patches accumulate until the codebase becomes a landfill of local solutions.

_AI_-assisted development needs refactoring as economic hygiene. Not heroic rewrites. Not platform dreams disguised as cleanliness. Not future-proofing based on imagined requirements. It needs opportunistic refactoring, guided by the next change, protected by tests, limited by economic sense, and aimed at making imminent or likely future change cheaper.

If agents make it cheaper to add code, refactoring helps decide whether that code deserves to stay in the shape it first arrived.

[![Image 12](https://substackcdn.com/image/fetch/$s_!WOVw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe715d5e2-04d1-4706-9258-20db9f5f8c3e_1024x558.png)](https://substackcdn.com/image/fetch/$s_!WOVw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe715d5e2-04d1-4706-9258-20db9f5f8c3e_1024x558.png)

Cheap generation creates a psychological trap: because code is easier to produce, larger changes feel less costly.

They are not.

The cost of a batch is not only the time spent typing it. The cost of a batch includes review time, context reconstruction, test scope, integration risk, deployment risk, rollback difficulty, user impact, incident diagnosis, and the opportunity cost of delayed feedback.

Large batches hide mistakes. They increase cognitive load. They make review less precise. They delay learning. They expand blast radius. They make it harder to know which part of a change caused a problem. _AI_ does not remove those costs. It can make them easier to trigger.

This is why small batches are not an old Agile preference. They are a control mechanism.

A small change is easier to understand, test, review, integrate, release, roll back, learn from, delete, and explain to a user. It is also easier to connect to a business outcome.

When generation is cheap, teams need stronger batch discipline, not weaker discipline.

The temptation will be to ask the agent for the whole flow: schema change, backend endpoint, frontend screen, tests, documentation, migration, release notes, and maybe a refactor on the way. Sometimes that may be useful for exploration. But as delivery work, large generated batches can become review traps. The reviewer must reconstruct intent across too many files. The test suite may say green while important product assumptions remain untested. The pull request looks efficient because it contains a lot of work, but the system absorbs it slowly.

Small batches keep generated change accountable.

They force the team to ask: what is the smallest behaviour that teaches us something or creates value? What is the smallest safe release? What is the smallest reversible step? What is the smallest slice that lets users, tests, integration, and production give us feedback?

That is Agile in the real sense: learning through small, valuable, working increments.

[![Image 13](https://substackcdn.com/image/fetch/$s_!f_ZK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43c83831-31cd-4c23-8f5e-cf02d2e1286c_1024x559.png)](https://substackcdn.com/image/fetch/$s_!f_ZK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43c83831-31cd-4c23-8f5e-cf02d2e1286c_1024x559.png)

Some people hear “_AI_ coding agent” and assume pair programming becomes less relevant. That conclusion depends on misunderstanding pairing as two humans sharing a keyboard because typing was scarce.

Typing was not the point. Shared judgment was the point.

Pairing helps with attention, design discussion, naming, problem framing, risk perception, knowledge transfer, and immediate feedback. It helps make decisions visible while they are still cheap to change. It reduces the loneliness of difficult work. It spreads context. It catches misunderstandings early.

_AI_ does not replace that. It changes the shape of the collaboration.

Sometimes the useful pairing will be human-human, where two people use _AI_ as a tool while preserving shared intent. Sometimes it will be human-agent, where the human writes tests, constrains scope, asks for alternatives, and rejects plausible but wrong output. Sometimes it will be review-pairing, where two humans inspect a generated change because the risk is high, the domain is subtle, or the design tradeoff matters.

The key is not the seating arrangement. The key is whether the team protects shared understanding.

This is especially important because _AI_ can produce work that feels finished before the team has understood it. A generated implementation may compress the visible act of coding, but it can also move reasoning out of the team’s heads. The code appears. The explanation sounds plausible. The tests pass. The pull request looks complete.

Before treating generated work as finished, the team should be able to answer:

1.   Why is this design right?

2.   Which alternatives were rejected?

3.   Which assumptions did the agent make?

4.   What should we do if this change fails in production?  
If the answer is no, the team did not save time. It borrowed time from the future at uncertain interest.

Review has the same problem. Review is not a cleaning service for generated code. It is a scarce decision point in the system. If review becomes the place where all upstream ambiguity is dumped, senior engineers become the airport security queue. Every generated change reaches them faster, larger, and more polished on the surface, while the deeper work of intent validation becomes heavier.

Good teams will not solve this by asking reviewers to work harder. They will improve the quality of work before review: clearer intent, smaller batches, better tests, stronger local verification, simpler design, better prompts, and better rules for what agents are allowed to change without human attention.

That is not anti-_AI_. That is respect for the constraint.

[![Image 14](https://substackcdn.com/image/fetch/$s_!CzfY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38c6eaee-31b3-4ee2-bf70-4ede07a9baba_1024x558.png)](https://substackcdn.com/image/fetch/$s_!CzfY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38c6eaee-31b3-4ee2-bf70-4ede07a9baba_1024x558.png)

There is a familiar feeling around many _AI_ initiatives.

Lots of pilots. Lots of excitement. A growing story that this changes everything. But beneath the noise, the pattern often looks less like transformation and more like premature adoption:

1.   Use cases not clearly tied to business outcomes

2.   Teams experimenting without a clear direction

3.   Success metrics that are vague, missing, or too local

4.   Limited measurable impact on value, quality, delivery, or learning  
We have seen versions of this pattern before. Cloud promised speed and flexibility. Microservices promised scalability and independent evolution. Data platforms promised better decisions. None of those ideas were wrong. The problem was not the technology itself. The problem was adoption moving faster than understanding.

_AI_ can fall into the same trap.

The question is not: “Where can we apply _AI_?”

The better question is: “Where are we currently losing time, money, quality, or trust, and can _AI_ meaningfully improve that constraint?”

Without that shift, many _AI_ initiatives will remain interesting experiments rather than real transformation.

A strategy has a diagnosis, a guiding policy, and coherent action. It explains what is happening, what matters, where advantage may come from, what constraints shape the terrain, and which actions fit together. “Use _AI_” does none of that.

It is a command.

It may be a useful command in some contexts. It may create exploration. It may reduce friction. It may reveal opportunities. But by itself, it does not say where the system is constrained, what outcome should improve, how risks will be managed, what tradeoffs are acceptable, or what evidence would make the team change direction.

That is why _AI_ adoption often becomes another version of roadmap theatre. Leaders ask for visible movement. Teams produce artefacts. Dashboards show activity. Everyone can point to examples.

But the deeper questions remain unanswered:

1.   What user problem are we solving better because of _AI_?

2.   Which part of the delivery system is constrained?

3.   Are we reducing lead time, or increasing work in progress?

4.   Are we improving quality, or increasing review burden?

5.   Are we strengthening product judgment, or generating plausible stories faster?

6.   Are we lowering the cost of future change, or increasing basal cost?

7.   Are we improving recovery from incidents, or increasing operational fragility?  
Without those questions, _AI_ adoption becomes the corporate equivalent of printing boarding passes faster while passengers miss flights.

This is where Agile and _XP_ provide a useful discipline, not because they are fashionable, but because they point back to reality. Agile asks whether we are delivering valuable working software early and continuously. _XP_ asks whether we have the feedback loops, technical excellence, collaboration, tests, integration, and design discipline to change software safely. _Trunk-Based Development_ asks whether change is joining shared reality quickly. _Continuous Delivery_ asks whether integrated change can become user value safely and repeatedly. Software economics asks whether the investment creates value after cost, risk, delay, and future carrying cost are considered. _Theory of Constraints_ (_TOC_) asks whether we are improving the system constraint or flooding it. Product strategy asks whether our movement has a coherent logic.

_AI_ does not replace any of these questions.

It makes them harder to dodge.

A team that measures _AI_ success only through usage is not measuring success. It is measuring exposure.

Accepted suggestions, prompts sent, generated lines, _AI_-authored pull requests, and tool adoption may be useful operational signals, but they do not tell us whether software delivery improved. They say the team used the tool. They do not say the tool improved the system.

A better measurement set should connect _AI_ use to the outcomes software is actually accountable for.

For production and local efficiency, measure:

1.   Generated code volume

2.   Accepted suggestions

3.   Time spent prompting

4.   Time spent reviewing generated output

5.   Time spent correcting generated output

6.   Repetitive work removed  
These signals are useful, but they are not enough. They tell you whether the machine is producing more and whether local work feels cheaper. They do not tell you whether users receive value sooner.

For delivery effectiveness, measure:

1.   Lead time from idea to production

2.   Lead time from commit to production

3.   Deployment frequency

4.   Work in progress

5.   Batch size

6.   Pull request size

7.   Review waiting time

8.   Time in review

9.   Reopened work

10.   Rework rate  
These signals help reveal whether _AI_ is improving flow or increasing unfinished inventory.

For quality and safety, measure:

1.   Change failure rate

2.   Failed deployment recovery time

3.   Deployment rework rate

4.   Incidents per change

5.   Escaped defects

6.   Regression rate

7.   Flaky test rate

8.   Test execution time

9.   Security findings introduced by change

10.   Mutation testing signal where appropriate  
These signals help reveal whether generated change is becoming trustworthy software or merely passing through weak gates.

For trust and operability, measure:

1.   Mean time to detect incidents

2.   Mean time to restore service

3.   Rollback success

4.   Observability coverage for changed flows

5.   Support contacts linked to recent changes

6.   User-facing reliability

7.   Error budget consumption

8.   On-call load

9.   Cognitive load around incident diagnosis

10.   Alert fatige

11.   Time needed to explain a generated change after merge  
These signals help reveal whether the system remains understandable and recoverable when change accelerates.

For product value, measure:

1.   User outcome movement

2.   Adoption of delivered capabilities

3.   Drop-off in changed flows

4.   Customer-reported friction

5.   Revenue, retention, cost reduction, or risk reduction where relevant

6.   Time from release to learning

7.   Product bets validated or invalidated

8.   Strategic coherence of the roadmap  
These signals help reveal whether generated work is becoming valuable change, not merely internal motion.

For maintainability, measure:

1.   Files touched per change

2.   Change coupling

3.   Hotspots

4.   Complexity trends

5.   Duplication trends

6.   Code churn

7.   Ownership clarity

8.   Test readability

9.   Design coherence around core domain concepts

10.   Time needed for a new team member to understand a changed area  
These signals help reveal whether the codebase remains economically changeable after the generated work is merged.

The point is not to create a dashboard museum. The point is to stop pretending that faster code generation is enough evidence.

A team should be able to say: after adopting _AI_ in this workflow, our lead time improved without harming stability, our review queues stayed healthy, our test quality improved, our incidents did not increase, our recovery remained fast, our users received value earlier, and our codebase remained easier to change.

If the team cannot say something like that, it may still be getting value from _AI_. But it does not yet know the system-level price.

[![Image 15](https://substackcdn.com/image/fetch/$s_!jL3-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28bbe337-cc10-42a6-9cef-79acf545e972_1024x558.png)](https://substackcdn.com/image/fetch/$s_!jL3-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28bbe337-cc10-42a6-9cef-79acf545e972_1024x558.png)

_AI_ has changed software development. It has made code easier to produce. It has made examples easier to explore. It has made some tasks faster. It has made documentation, explanation, scaffolding, migration, and test generation more accessible. It has opened useful possibilities for teams willing to learn carefully.

But it has not changed what matters.

The user still does not care how much code was generated. The user cares whether the product works, helps, improves, and can be trusted. The business still does not care about generated volume by itself. It cares about value, cost, risk, time to market, recovery, optionality, and return. The system still does not care whether a human, an agent, or a workflow produced the change. It cares whether the change can be safely integrated into a living product and turned into value.

That is why _AI_ does not replace _XP_ or Agile. It raises the cost of pretending.

Fake Agile can produce more artefacts now. Weak _XP_ can produce more code now. Poor strategy can generate more movement now. Fragile systems can receive more changes now. But none of that means users receive better value sooner.

In a world where code is expensive to write, teams can hide behind scarcity. In a world where code is cheap to generate, teams are exposed. Their real constraints become visible: unclear intent, weak tests, delayed integration, large batches, poor design, overloaded review, fragile delivery, weak operability, and shallow product judgment.

Agile and _XP_ were always supposed to address those problems. Not as ceremonies. Not as nostalgia. Not as branding. As disciplines for staying connected to reality while changing software.

_Trunk-Based Development_ keeps generated change close to shared reality. _Continuous Delivery_ keeps integrated change connected to value. _Test-Driven Development_ (_TDD_) keeps implementation connected to intent. Refactoring keeps the future cost of change visible. Small batches keep risk small enough to reason about. Pairing and review keep judgment shared.

The teams that benefit most from _AI_ will not be the ones that generate the most code. They will be the ones that can convert generated change into valuable, reliable, maintainable software without losing trust. They will use _AI_, but they will not let _AI_ set the rhythm of the system. They will protect feedback. They will keep batches small. They will test behaviour. They will integrate frequently. They will refactor opportunistically. They will collaborate around intent. They will measure value, not theatre.

_AI_ has made it cheaper to propose change. It has not made it cheaper to be wrong.

The hard part was not typing before, and it is not typing now. The hard part is absorbing change without losing value, reliability, understanding, and trust.

*   Beck, Kent, and Andres, Cynthia. _Extreme Programming Explained: Embrace Change, Second Edition_. Addison-Wesley Professional, 2004

*   Beck, Kent, Beedle, Mike, van Bennekum, Arie, Cockburn, Alistair, Cunningham, Ward, Fowler, Martin, Grenning, James, Highsmith, Jim, Hunt, Andrew, Jeffries, Ron, Kern, Jon, Marick, Brian, Martin, Robert C., Mellor, Steve, Schwaber, Ken, Sutherland, Jeff, and Thomas, Dave. _Manifesto for Agile Software Development_.

[https://agilemanifesto.org/](https://agilemanifesto.org/)

*   Beck, Kent, Beedle, Mike, van Bennekum, Arie, Cockburn, Alistair, Cunningham, Ward, Fowler, Martin, Grenning, James, Highsmith, Jim, Hunt, Andrew, Jeffries, Ron, Kern, Jon, Marick, Brian, Martin, Robert C., Mellor, Steve, Schwaber, Ken, Sutherland, Jeff, and Thomas, Dave. _Principles behind the Agile Manifesto_. [https://agilemanifesto.org/principles.html](https://agilemanifesto.org/principles.html)

*   Becker, Joel, Rush, Nate, Barnes, Beth, and Rein, David. _Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity_. [https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

*   DORA. _State of AI-assisted Software Development 2025_. [https://dora.dev/dora-report-2025/](https://dora.dev/dora-report-2025/)

*   Faros AI. _AI Impact on Engineering Productivity: 2026 Report Data_. [https://www.faros.ai/research/ai-acceleration-whiplash](https://www.faros.ai/research/ai-acceleration-whiplash)

*   Faros AI. _The AI Engineering Report 2026: The AI Acceleration Whiplash, Ten Takeaways_. [https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways](https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways)

*   Fowler, Martin. _Continuous Integration_. [https://martinfowler.com/articles/continuousIntegration.html](https://martinfowler.com/articles/continuousIntegration.html)

*   Fowler, Martin. _Definition of Refactoring_. [https://martinfowler.com/bliki/DefinitionOfRefactoring.html](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)

*   Google Cloud. _Announcing the 2024 DORA report_. [https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report)

*   Hammant, Paul. _Trunk-Based Development And Branch By Abstraction_. Leanpub, 2020. [http://leanpub.com/trunk-based-development](http://leanpub.com/trunk-based-development)

*   Humble, Jez, and Farley, David. _Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation_. Addison-Wesley Professional, 2010

*   Peng, Sida, Kalliamvakou, Eirini, Cihon, Peter, and Demirer, Mert. _The Impact of AI on Developer Productivity: Evidence from GitHub Copilot_. [https://arxiv.org/abs/2302.06590](https://arxiv.org/abs/2302.06590)

*   Valverde Ramos, Emmanuel. _Faster code, slower system_. [https://emmanuelvalverderamos.substack.com/p/faster-code-slower-system](https://emmanuelvalverderamos.substack.com/p/faster-code-slower-system)

*   Valverde Ramos, Emmanuel. _Cheap code is not cheap Software_. [https://emmanuelvalverderamos.substack.com/p/cheap-code-is-not-cheap-software](https://emmanuelvalverderamos.substack.com/p/cheap-code-is-not-cheap-software)

*   Valverde Ramos, Emmanuel. _Use AI is not a strategy_. [https://emmanuelvalverderamos.substack.com/p/use-ai-is-not-a-strategy](https://emmanuelvalverderamos.substack.com/p/use-ai-is-not-a-strategy)

*   Valverde Ramos, Emmanuel. _Product strategy is not a roadmap, and a roadmap is not a timeline_. [https://emmanuelvalverderamos.substack.com/p/product-strategy-is-not-a-roadmap](https://emmanuelvalverderamos.substack.com/p/product-strategy-is-not-a-roadmap)
