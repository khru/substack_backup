Title: Cheap Code is not cheap Software the SaaSmagedon

URL Source: http://emmanuelvalverderamos.substack.com/p/cheap-code-is-not-cheap-software

Final URL: https://emmanuelvalverderamos.substack.com/p/cheap-code-is-not-cheap-software

Published Time: 2026-05-07T05:01:36+00:00

Markdown Content:
Imagine a team creates a tiny serverless function. Just one Lambda. It receives a request, performs a small operation, and returns a response. The implementation is simple, the deployment is quick, and the infrastructure looks almost free. Nobody is worried because the unit cost is ridiculous.

A few weeks later, someone connects it to a retrying client. A partner starts calling it more often than expected. A bug creates a loop. The function starts writing logs at debug level. An integration fails and retries every few seconds. Then the team realises the function also talks to a paid API, writes to storage, emits traces, triggers alerts, and sits behind a workflow that nobody fully owns.

The code was cheap, the first deployment was cheap, and the first thousand calls were cheap. Then usage, retries, logs, observability, storage, API calls, incidents, ownership, and debugging turned the “tiny function” into a real economic object. The cost did not disappear because the unit cost was small. The cost appeared when the system started living.

That is exactly what is happening with many conversations about LLM-assisted software development. A few days ago I heard an argument about software architecture and AI-assisted development that sounded attractive if you only look at software through the narrow lens of code production.

The argument was roughly this: before LLMs, companies often bought SaaS products because building internally was too expensive. If a problem was already solved in the market, paying for an off-the-shelf solution usually made economic sense. But now that LLMs have made code generation much cheaper, the denominator has changed. The same internal solution that previously made no sense may now have a better return, because the cost of building it has fallen.

At first sight, this sounds sharp. It sounds economic. It sounds modern. It sounds like the kind of thing companies want to hear right now. But it hides a dangerous simplification.

Software economics is not the economics of typing code. It is the economics of turning money, time, attention, judgment, coordination, knowledge, maintenance, risk, and future change into capability, value, and return.

And once you look at the full system, the conclusion becomes much less exciting. LLMs may reduce part of the cost of producing code. They do not remove the cost of owning software. Worse than that, they introduce a new kind of cost surface: variable, provider-controlled, token-metered, behaviour-sensitive, constantly changing, and often impossible to price accurately before the bill arrives.

The mistake is not saying that LLMs make some development cheaper. They do. The mistake is pretending that cheaper code means cheaper software.

It does not.

*   The build-versus-buy decision has changed, but not in the simple way many people are selling.

*   LLMs may reduce part of the cost of producing code, but code production is only one part of the investment.

*   Internal software carries permanent economic weight: maintenance, operations, security, observability, knowledge, ownership, dependencies, support, upgrades, incidents, training, governance, and future change.

*   Replacing SaaS with internal tools does not remove cost. It changes the kind of cost the company now owns.

*   A company with 70 developers, 150 internal artefacts, and 50 SaaS products does not become cheaper by blindly converting SaaS into internal systems. It may simply increase its carrying cost, bus factor risk, cognitive load, operational burden, and opportunity cost.

*   The average number of artefacts per developer is a weak comfort metric. The real problem is uneven ownership, local concentration of knowledge, operational responsibility, and the number of systems each team must understand well enough to change safely.

*   The mistake in the “AI makes make cheaper than buy” argument is that it lowers one visible denominator and ignores several hidden ones.

*   That denominator is not only bigger than people admit. It is also unstable.

*   Token pricing, model choice, context size, output volume, tool use, agentic retries, billing rules, tokenizer changes, reasoning modes, cache behaviour, and provider decisions can change the economics after the decision has already been made.

*   Companies also inherit the cost of keeping people updated on LLM tools, workflows, risks, pricing models, benchmark changes, and new capabilities.

*   This training cost is not optional. If a company expects employees to use a tool professionally, the company must pay the cost of learning that tool professionally.

*   The AI-assisted workflow itself has maintenance cost. When the tools change, the company has to test, adapt, retrain, rewrite guidance, and rediscover whether the old efficiency still exists.

*   “It works for me” is not enough. In 2026, “working with LLMs works for me” is becoming the new “it works on my machine.”

*   Optimising for fewer tokens can create cognitive debt: the invoice may shrink while the future cost of understanding the code grows.

*   The real question is not “can we build this now?” The real question is “should we own this forever, under a cost structure we do not fully control?”

*   Cheap code can still become expensive software.

The argument has a clean economic shape.

Before LLMs, building internally was expensive. You needed developers, time, discovery, implementation, testing, integration, maintenance, infrastructure, and all the usual coordination around software work.

So when a company faced a non-core problem, the usual build-versus-buy conversation often favoured buying.

Examples are everywhere:

*   Feature flags

*   CRM

*   Analytics

*   Customer support

*   Billing

*   Identity

*   Observability

*   Internal workflow tooling

*   Operational dashboards

*   Experimentation platforms

If the market already offered a good enough solution, buying could be economically rational. Not because SaaS was free. It was not. But because internal development carried a large upfront cost and a long tail of ownership.

Now LLMs enter the picture.

Code becomes easier to generate. Scaffolding becomes faster. Integrations become cheaper to draft. A small team can produce something plausible in weeks. The first version feels closer than it used to feel.

So the argument says: if the cost of internal development drops, then the return of building internally improves.

In simplified form:

**Expected return = value of the solved problem / cost of building the solution**

If the denominator falls, the ratio improves.

That is true as far as it goes.

The problem is that it does not go very far.

Because the denominator is not “cost of producing the first version of the code.”

The denominator is the total cost of owning the capability.

That is a very different number.

[![Image 1](https://substackcdn.com/image/fetch/$s_!RNtA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b4a59bd-9600-45d6-accd-0dd2fb0df258_1024x558.png)](https://substackcdn.com/image/fetch/$s_!RNtA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b4a59bd-9600-45d6-accd-0dd2fb0df258_1024x558.png)

This is the category error.

A piece of software is not finished when the code exists. It is not finished when the pull request is merged. It is not finished when the first demo works. It is not finished when the model produces a plausible implementation. It is not finished when the team says, “we can build this in six weeks.”

That is only the moment where the company begins to own the consequences.

The first version is not the investment. The whole lifecycle is the investment.

That lifecycle includes:

*   Understanding the problem well enough to avoid building the wrong thing

*   Designing the solution well enough to make it changeable

*   Testing the behaviour well enough to trust it

*   Deploying it safely

*   Monitoring it

*   Securing it

*   Supporting it

*   Upgrading dependencies

*   Handling incidents

*   Explaining it to new people

*   Integrating it with other systems

*   Migrating it when assumptions change

*   Removing it when it no longer pays for itself

This is where the sales version of the argument becomes too thin.

It talks as if LLMs lowered “the cost of software.”

They did not.

They lowered parts of the cost of producing certain kinds of code under certain conditions.

That is useful. That is real. That can matter.

But it is not the same as lowering the full cost of software ownership.

[![Image 2](https://substackcdn.com/image/fetch/$s_!PE3f!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0252836-8a22-4a57-a311-00315de0e965_1024x559.png)](https://substackcdn.com/image/fetch/$s_!PE3f!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0252836-8a22-4a57-a311-00315de0e965_1024x559.png)

Buying SaaS is not magic.

SaaS has costs:

*   Licences

*   Vendor lock-in

*   Integration friction

*   Procurement overhead

*   Security review

*   Data governance

*   Migration risk

*   Contract negotiation

*   Feature limitations

*   Pricing changes

*   Operational dependency on a third party

There are absolutely cases where building internally makes sense:

*   If the capability is core to the business

*   If the SaaS solution does not fit the problem

*   If the workflow creates strategic advantage

*   If the integration cost is worse than ownership cost

*   If the data or compliance constraints make external dependency too risky

*   If the company has enough repeated volume to amortise the investment

*   If the internal solution can create a genuine advantage that the market cannot provide

That is not the argument I am rejecting.

The weak argument is different.

The weak argument says that because generating code is cheaper, companies should reopen many make decisions that previously lost against buy.

Sometimes, yes.

Often, no.

Because when you replace a SaaS product with an internal system, you do not eliminate the cost. You move the cost inside the company.

You move it into:

*   Engineering capacity

*   Operational responsibility

*   Future maintenance

*   Incident response

*   Architectural coupling

*   Onboarding

*   Knowledge concentration

*   Every future change that now has one more thing to consider

The invoice may disappear, but the cost does not. It changes shape.

[![Image 3](https://substackcdn.com/image/fetch/$s_!u5-1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9876833-84e6-4700-980a-45d9942c01e2_1024x559.png)](https://substackcdn.com/image/fetch/$s_!u5-1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9876833-84e6-4700-980a-45d9942c01e2_1024x559.png)

Imagine a company with 70 developers and 150 internal artefacts.

By artefact I mean any meaningful system, service, application, library, job, workflow, integration, platform component, data pipeline, internal tool, automation, or operational asset that somebody must understand, change, operate, or keep alive.

At first, the average looks manageable:

150 artefacts / 70 developers = 2.14 artefacts per developer

That number is comforting because it creates the illusion of an even distribution. But organisations do not work like spreadsheets. Knowledge is uneven. Ownership is uneven. Risk is uneven.

Some teams own five critical things. Some teams own one peripheral service. Some developers understand the old billing integration. Some understand the deployment pipeline. Some understand the customer allocation engine. Some understand a legacy process nobody wants to touch. Some artefacts have clear owners. Some are orphaned. Some are officially owned by a team that no longer has anyone who understands them deeply.

So the average is not wrong. It is just weak.

Now add 50 SaaS products around the company’s software and business operations:

*   Feature flags

*   CRM

*   Analytics

*   Customer support

*   Observability

*   Experimentation

*   Billing

*   Identity

*   Data tooling

*   Marketing automation

*   Incident management

*   Documentation

*   Security scanning

*   Workflow automation

*   Internal communication

*   Search

*   Monitoring

*   Scheduling

*   Translation

*   Reporting

Those SaaS products are not “free complexity.” They still need configuration, integration, governance, training, security review, ownership, cost control, and operational understanding.

The organisation now has 200 relevant artefacts around the system of work:

200 artefacts / 70 developers = 2.85 artefacts per developer

At the average level, the difference looks small: 2.14 to 2.85. That does not sound dramatic enough to change a strategic decision.

But the average is hiding the real problem.

The important topic is that this is not only a risk of possible lack of knowledge but also a capacity issue.

The question is not whether the global average increased by 0.71 artefacts per developer. The question is where the extra ownership lands, which teams absorb it, which people become bottlenecks, which systems become orphaned, and which future changes become harder because there is now more local knowledge to preserve.

The real questions are more concrete:

*   Who is the owner of this extra internal tools?

*   Does one product team now own a custom feature flag system?

*   Does one engineer become the only person who understands the allocation logic?

*   Does a team that already owns customer-facing systems now also own internal replacements for vendor products?

*   Does the organisation increase the number of things that can fail without increasing the number of people who can safely fix them?

That is where the economic damage lives.

Not in the average.

In the concentration.

[![Image 4](https://substackcdn.com/image/fetch/$s_!ut9B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67478779-c79c-4c03-9b23-50b9531ecb82_1024x559.png)](https://substackcdn.com/image/fetch/$s_!ut9B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67478779-c79c-4c03-9b23-50b9531ecb82_1024x559.png)

People often talk about bus factor as an engineering concern.

It is also an economic concern.

If only one person understands a system, the company has a liquidity problem. The knowledge is not liquid. The work is not easily transferable. The option to move fast is weaker than it looks. The cost of change rises. The cost of delay rises. The cost of interruption rises. The risk of being wrong rises.

A company may think it has built a cheap internal alternative. But if that alternative is understood by two people, supported by one team, undocumented in the parts that matter, and tightly connected to several business workflows, then the company has not bought freedom.

It has bought fragility.

And fragility has a carrying cost.

This is one of the most important economic points in software.

The cost of software is not only the cost of creating it. It is the cost of keeping it understandable enough to remain useful.

When understanding decays, liquidity decays. And when liquidity decays, every future decision becomes more expensive.

The symptoms are familiar:

*   Small changes stop being small

*   Incidents take longer to diagnose

*   New developers take longer to onboard

*   Dependencies become scarier

*   Refactoring becomes politically harder

*   Teams delay changes because nobody is sure what will break

That is not a technical inconvenience. That is capital trapped in cognitive mud.

[![Image 5](https://substackcdn.com/image/fetch/$s_!zIpL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F119b7f7f-16bc-4b6f-a909-29e879f0720d_1024x559.png)](https://substackcdn.com/image/fetch/$s_!zIpL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F119b7f7f-16bc-4b6f-a909-29e879f0720d_1024x559.png)

There is another cost the cheap-code argument usually ignores.

Keeping the lights on.

Every internal system requires some amount of operational care. Even a small system needs a place to run, a way to deploy, a way to observe, a way to secure, a way to recover, and a way to evolve.

That means:

*   Cloud services

*   Infrastructure configuration

*   Logs

*   Metrics

*   Traces

*   Alerts

*   Dashboards

*   Access control

*   Secrets management

*   Backup and recovery

*   Dependency updates

*   Vulnerability remediation

*   Runtime upgrades

*   Incident response

*   Capacity planning

*   Data retention

*   Compliance review

None of this disappears because the first version was generated faster.

In fact, LLM-assisted development can make this worse if teams produce more internal systems than they have the operational maturity to carry.

The bottleneck moves.

It used to be: can we build it?

Now it becomes: can we own everything we are suddenly able to build?

That is a better question.

It is also a much less fashionable one.

Maintenance is often treated as an unfortunate afterthought.

It should not be.

Maintenance is the normal state of useful software.

If a system matters, it will change. If it integrates with other systems, it will break assumptions. If it handles real users, it will receive edge cases. If it touches business workflows, it will accumulate exceptions. If it runs in production, it will require care. If it becomes successful, more people will depend on it. If more people depend on it, the cost of being wrong increases.

That is why the build-versus-buy decision cannot be reduced to first-version cost.

An internal tool does not only compete with the SaaS product on initial implementation cost. It competes on:

*   Total cost of ownership

*   Speed of adaptation

*   Reliability

*   Security

*   Compliance

*   User experience

*   Integration quality

*   Support burden

*   Strategic differentiation

*   Opportunity cost

*   Risk

*   Reversibility

*   Future optionality

If you only compare licence cost against development cost, you are not doing economics.

You are doing procurement with missing columns.

Let’s return to the simplified formula.

**Expected return = value of the solved problem / cost of building the solution**

This is the part that sounds persuasive.

If LLMs reduce the cost of building, the denominator goes down, so the expected return goes up.

But the correct denominator is not that narrow.

A more honest version would look like this:

**Expected return = expected value of the capability / total cost of ownership**

And **total cost of ownership includes**:

*   Discovery cost

*   Build cost

*   Integration cost

*   Review cost

*   Test cost

*   Deployment cost

*   Infrastructure cost

*   Observability cost

*   Security cost

*   Maintenance cost

*   Dependency cost

*   Support cost

*   Incident cost

*   Training cost

*   Onboarding cost

*   Migration cost

*   Decommissioning cost

*   Opportunity cost

*   Coordination cost

*   Cognitive cost

That last one matters more than most spreadsheets admit.

**Cognitive cost is the cost of making the system understandable enough that people can work with it safely.**

Every additional artefact increases the surface area of knowledge. Every extra internal system increases the number of relationships people must reason about. Every replacement for a SaaS product adds more local context the company must preserve. Every new workflow creates more explanation debt. Every undocumented decision makes future work slower.

This is where “AI made it cheap to build” becomes incomplete.

**Even if AI reduces build cost by 50 percent, 70 percent, or more, the company still has to pay for the rest of the lifecycle.**

And in many systems, the rest of the lifecycle is the larger economic problem.

[![Image 6](https://substackcdn.com/image/fetch/$s_!oLov!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffcbaaf4a-9b59-4d04-98f3-f84de2204d64_1024x559.png)](https://substackcdn.com/image/fetch/$s_!oLov!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffcbaaf4a-9b59-4d04-98f3-f84de2204d64_1024x559.png)

There is another hidden problem in the cheap-code argument.

It treats the cost of AI-assisted development as if it were stable.

It is not.

That is a serious economic mistake.

Saying “AI makes internal development cheaper” without knowing what the token cost will be over the life of the system is like building a business case on the assumption that a currency exchange rate will never move.

It may look stable on the day you make the decision. It may look acceptable in the first invoice. It may look harmless during a prototype. It may look manageable while a small team is experimenting.

That does not mean it will remain stable after the company has built workflows, habits, tooling, architecture, and delivery expectations around it.

This matters because AI-assisted development is not priced like traditional developer time. It is priced through a moving surface:

*   Input tokens

*   Output tokens

*   Cached tokens

*   Tool-use tokens

*   Model choice

*   Context size

*   Thinking effort

*   Agentic loops

*   Retry behaviour

*   Generated diffs

*   Review cycles

*   Subscription limits

*   Provider policy

*   Billing model changes

*   Tokenizer changes

That is not a small detail. It is the economic substrate of the decision.

If a company decides to reimplement a SaaS product internally because “AI made development cheaper,” it is implicitly making a bet on a cost structure it does not fully control.

The vendor of the SaaS product had one visible price model.

The new internal AI-assisted system may have another price model hidden behind prompts, tokens, model routing, output length, context windows, retries, tool calls, and provider changes.

That is not only cost.

That is uncertainty.

And uncertainty is risk.

This is the part that many AI arguments quietly avoid.

If the economic case depends on LLM-assisted development being cheap, predictable, and available, then the company has created a dependency on a cost structure it does not own.

The provider can change:

*   The billing model

*   Token accounting

*   Model availability

*   Limits

*   Default behaviour

*   The tokenizer

*   The price of better models

*   The availability of the model the workflow was built around

*   The number of tokens consumed by the same task, even if the company does not change a single line of its own process

This is not hypothetical as a class of risk.

Modern AI coding tools are already moving from simple subscription-like mental models toward more usage-sensitive billing. Some providers account for input, output, cached tokens, model choice, and tool use. Some model upgrades can change tokenisation, meaning the same text can map to a different number of tokens.

That does not mean these tools are bad.

It means they are economically dynamic.

And economically dynamic dependencies must be treated differently from stable internal assumptions.

If the business case for replacing SaaS with internal software only works when token costs, model behaviour, and agent loops remain favourable, then the business case is weaker than it looks.

Because the company does not control the machine that changed the economics.

It is renting part of the economics from a provider.

[![Image 7](https://substackcdn.com/image/fetch/$s_!PXsv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faeeb729d-a2a1-4901-9a01-573abc037cfa_1024x559.png)](https://substackcdn.com/image/fetch/$s_!PXsv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faeeb729d-a2a1-4901-9a01-573abc037cfa_1024x559.png)

The token model creates a strange economic pressure.

If output tokens cost more than input tokens, then verbose generated code is not just annoying. It is billable waste.

The company pays when:

*   The model produces too much code

*   The model produces unnecessary abstractions

*   The model generates five files where two would do

*   The model rewrites half the codebase to make a small change

*   The model needs several retries to produce a usable result

*   The model generates tests, scaffolding, explanations, migrations, and diffs that must later be reviewed

At first, someone will say the obvious thing: then guide the model better.

That is true, but it does not remove the cost. It changes where the cost appears.

*   Good guidance consumes input tokens.

*   Good architecture requires explanation.

*   Good design requires constraints.

*   Good tests require examples.

*   Good refactoring requires context.

*   Good review requires back-and-forth.

*   Good agentic development requires iteration.

So there is no free path.

If you give the model weak guidance, you may get too much code, worse design, more rework, and more cognitive load.

If you give the model strong guidance, you spend more tokens shaping the work, constraining the output, explaining the architecture, and forcing better responsibility boundaries.

And if you optimise too aggressively for fewer output tokens, you risk producing code that is denser, less explicit, harder to read, harder to review, and more expensive for humans to understand later.

That is the trap.

Token optimisation can become cognitive debt creation.

The organisation saves money in the invoice and pays it back in understanding.

This is where the argument becomes more subtle.

Good software design is not only about reducing the number of lines.

It is about creating a structure that humans can understand, change, test, and reason about.

Sometimes that means:

*   Smaller components

*   Clearer names

*   More explicit responsibilities

*   Separating behaviours that could technically live together

*   Writing tests that explain behaviour

*   Avoiding clever density because density makes the system harder to inspect

But many AI pricing models create a pressure against explicitness.

Not always directly. Not always consciously. But economically.

More explanation means more tokens. More context means more tokens. More generated tests mean more tokens. More careful refactoring means more tokens. More alternatives explored means more tokens. More iteration means more tokens.

So a team trying to control AI cost may begin to optimise the wrong thing:

*   Shorter prompts

*   Shorter outputs

*   Less explanation

*   Less structure

*   Less exploration

*   Less diagnostic back-and-forth

*   Less design conversation

*   Less review context

That can make the bill look better.

But it can make the software worse.

A cheaper generated result may become more expensive to understand. A shorter answer may hide more assumptions. A denser implementation may increase review effort. A compressed design may increase future change cost. A shallow prompt may create hidden rework. A reduced test suite may move cost into debugging.

This is why token cost is not only a finance issue.

It can become a design pressure.

And if that pressure is not made explicit, teams may unknowingly trade invoice cost for cognitive debt.

The bill goes down. The system gets harder to carry.

That is not a win.

It is a cost transfer.

When people discuss risk in LLM-assisted development, they usually talk about hallucination.

That matters.

But it is not the only risk.

There is also product risk from the AI provider itself.

A coding agent is not just a compiler, an editor, or a library. It is a remote, evolving system whose behaviour, limits, pricing, model routing, context management, reasoning modes, and token accounting can change outside your company’s release process.

That creates a new class of operational uncertainty.

The workflow may change because:

*   The model becomes more expensive for the same workload

*   A new tokenizer changes token counts

*   A new model produces longer outputs

*   A reasoning mode behaves differently than expected

*   A subscription plan introduces stricter limits

*   A provider changes what is included and what is metered

*   An agent requires more retries to reach the same result

*   The workflow becomes slower, more expensive, or less predictable without the company changing its own code

This is not the same risk profile as programming something yourself from zero.

When developers write code directly, the company carries many risks: defects, poor design, maintenance cost, bus factor, weak testing, opportunity cost, and knowledge concentration.

But it does not have the same kind of dependency on a third-party model changing how many billable units are consumed by the same task, or silently shifting the behavioural assumptions of the coding assistant that made the internal build look economically attractive.

That risk is different.

It is not just another old software risk with a new name.

It is an additional AI-specific risk surface that did not exist in the same form when the company programmed the system directly from zero.

And that matters.

Because if the economic case depends on AI making development cheap, the company also has to price the risk that the AI layer itself becomes less cheap, less predictable, or less useful than expected.

[![Image 8](https://substackcdn.com/image/fetch/$s_!GNl1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52f5c094-0b06-43bf-bc4d-6b62eb2a3697_1024x559.png)](https://substackcdn.com/image/fetch/$s_!GNl1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52f5c094-0b06-43bf-bc4d-6b62eb2a3697_1024x559.png)

There is another cost that almost never appears in the cheap-code argument.

The cost of staying current.

This cost is often treated as if it were ridiculous, secondary, or too small to matter.

It is not.

If a company decides that LLMs and coding agents are now part of how software is built, then the company has also accepted a training responsibility.

Not as a nice-to-have. Not as a hobby for curious developers. Not as something people should somehow absorb in their spare time. Not as “engineers should keep up because this is the industry now.”

If a company expects people to use a tool professionally, then the company must pay the cost of learning that tool professionally.

That means:

*   Time

*   Training

*   Experimentation

*   Internal guidance

*   Updated practices

*   Shared examples

*   Security rules

*   Review standards

*   Prompt patterns

*   Agent usage policies

*   Failure catalogues

*   Benchmarking attempts

*   Time away from direct product work

This is not a small side cost.

Because these tools do not stand still.

They change constantly:

*   New models appear

*   Old models are deprecated

*   Tokenizers change

*   Pricing changes

*   Context windows change

*   Default behaviours change

*   Reasoning modes change

*   Agent capabilities change

*   Tool integrations change

*   Memory behaviour changes

*   Sandboxing rules change

*   IDE integrations change

*   CLI workflows change

*   Cloud agents change

*   Permissions change

*   Review flows change

Every meaningful change creates a new question: does our old way of working still make sense?

That question has a cost.

The team has to:

*   Test

*   Compare

*   Adapt

*   Document

*   Retrain

*   Update internal practices

*   Change prompts

*   Change guardrails

*   Change review expectations

*   Change what it allows the agent to do

*   Change how much autonomy is acceptable

*   Change how it measures whether the tool is still helping

This is workflow maintenance.

And it is not free.

The company is not only maintaining software anymore.

It is maintaining the method by which software is produced.

That is a much bigger statement than most AI adoption plans admit.

A software system has maintenance cost.

An AI-assisted way of working has maintenance cost too.

That second cost is newer, so many companies pretend it is smaller.

It may not be.

When a team builds with LLMs and coding agents, the team does not only need to maintain the resulting software. It also needs to maintain the workflow that produced that software.

That includes:

*   Which models are allowed

*   Which tools are approved

*   Which prompts or instructions are recommended

*   Which tasks can be delegated to agents

*   Which tasks require human design first

*   Which parts of the codebase agents can edit

*   Which tests must run before accepting changes

*   Which security constraints must never be bypassed

*   Which review rules apply to generated code

*   Which outputs are considered unacceptable

*   Which workflows are still worth using after a tool update

This is not a one-time setup.

It decays.

The workflow may need to change when:

*   The tool changes

*   Pricing changes

*   The tokenizer changes

*   The model becomes more verbose

*   The agent becomes more autonomous

*   The provider changes limits

*   Review standards change

*   Security expectations change

*   The codebase changes enough that old prompts stop working

And every time the workflow changes, the company pays again.

It pays in:

*   Learning

*   Experimentation

*   Mistakes

*   Review fatigue

*   Lost focus

*   Meetings

*   Internal documentation

*   Rework

*   Opportunity cost

This is the irony.

The tool sold as a way to reduce software cost can create a new internal product that the company must continuously manage: the AI development workflow itself.

And if the company does not manage it, the workflow still changes.

It just changes accidentally.

[![Image 9](https://substackcdn.com/image/fetch/$s_!QV8t!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d4c1e31-0456-48ab-b7f2-69d101c6635b_1024x559.png)](https://substackcdn.com/image/fetch/$s_!QV8t!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d4c1e31-0456-48ab-b7f2-69d101c6635b_1024x559.png)

The uncomfortable part is that companies are often adopting these tools without a reliable way to compare the old workflow with the new one.

A vendor benchmark may tell you that a model performs better on a coding benchmark. A release note may tell you that a new feature exists. A demo may show a beautiful path through a clean problem. A leaderboard may suggest that one model is stronger than another.

But none of that tells you whether your organisation’s real workflow improved.

It does not tell you if your LLM development configuration preformes better or worse base when the model change or even when the vendor changes elements like the tokenizer. So there is not way of knowing if a minor update on the tool will break your development workflow.

It also does not tell you whether:

*   Your engineers understand the code better

*   Review quality improved

*   Maintainability improved

*   The system became easier to change

*   The team created less cognitive debt

*   The same work now requires fewer retries

*   The agent’s output fits your architecture

*   The team is still effective after the tool changes

That benchmark does not come for free.

The company has to build it or accept that it is operating partly by faith.

And this is where one of the most repeated arguments in AI-assisted development becomes weak.

“It works for me.”

Good.

That may be true.

It may work in your context:

*   With your codebase

*   With your prompts

*   With your habits

*   With your tolerance for rework

*   With your ability to review the output

*   With your architecture in your head

*   With your preferred model

*   With your current pricing plan

*   With your current token limits

*   With your current agent behaviour

*   With your current IDE integration

*   With your current workflow

That is not nothing.

But it is not enough.

In 2026, “**working with LLMs works for me**” is becoming the new “**it works on my machine.**”

It may be true locally.

It may even be useful locally.

But if it is not reproducible, if it is not measurable, if it cannot survive a model change, if it collapses when the provider changes something internally, if the same workflow behaves differently after a silent behavioural shift, then the argument is being held together with toothpicks.

The problem is not that it works for you.

The problem is pretending that “it works for me” is a business case.

A serious organisation cannot build an economic argument on personal comfort with a moving toolchain.

It needs:

*   A baseline

*   Comparison

*   Reproducibility

*   Failure modes

*   Cost visibility

*   A way to know when the tool has stopped helping

Otherwise, every success story becomes local folklore.

And local folklore is not strategy.

If the company does not build its own benchmark, every update becomes a small act of hope.

Maybe the new model is better for our work. Maybe the new agent flow saves time. Maybe the new default behaviour is acceptable. Maybe the new reasoning mode is good enough. Maybe the new token consumption is still worth it. Maybe the new workflow is still more efficient than the old one.

That is not an economic argument. It is unmanaged uncertainty, and unmanaged uncertainty should not be sold as productivity.

“It works for me” is fine as a personal report.

It is not enough as an investment thesis.

There is also an opportunity cost in adopting the AI-assisted way of working.

Before the company gets the supposed efficiency, it has to spend capacity learning how to get it.

People have to learn the tool. Teams have to change habits. Senior engineers have to review strange outputs. Internal standards have to be updated. Security concerns have to be handled. Architectural boundaries have to be explained to the agent. Prompts and workflows have to be refined. Bad patterns have to be corrected. Useful patterns have to be shared. The organisation has to discover where the tool helps and where it creates drag.

None of this is free.

And none of it guarantees return.

The company is making an investment under uncertainty.

It does not know in advance whether:

*   The tool will work well for its codebase

*   Developers will become faster in the work that matters

*   Review time will increase

*   Generated code will increase cognitive load

*   The tool will fit the architecture

*   Future updates will preserve the workflow that made the investment look attractive

So the adoption cost must be priced like any other investment.

Expected return is not automatic. Risk is not zero. Opportunity cost is not imaginary.

If the team spends weeks adapting to a new AI workflow, those weeks are not available for product work, reliability work, architecture improvement, customer problems, or reducing existing debt.

The question is not whether learning AI tools is useful.

Often it is.

The question is whether the company is honestly pricing the cost of making that learning operational.

Most are not.

This is one of the most dangerous parts of the whole situation.

A SaaS invoice is annoying because it is visible.

You can see the subscription. You can negotiate the contract. You can compare plans. You can evaluate seats. You can model renewal. You can ask whether usage justifies cost.

The AI-assisted internal alternative may feel cheaper because the cost is distributed.

Some of it appears as:

*   Tool subscriptions

*   API usage

*   Agentic loops

*   Retries

*   Review time

*   Generated code nobody asked for

*   Maintenance

*   Cognitive load

*   Operational ownership

*   Debugging strange model behaviour

*   Staying current with tool changes

*   Retraining people after a new release

*   Future work, when the people who built the first version are no longer around

This is why replacing SaaS with internal AI-assisted software can create a visibility problem.

The old cost was explicit. The new cost is fragmented.

The old cost appeared in procurement. The new cost appears across engineering, platform, security, architecture, support, cloud, cognitive load, training, governance, and provider usage.

The old cost was annoying because someone could point to it.

The new cost may be more dangerous because it is easier to miss.

A hidden cost is not cheaper.

It is just harder to manage.

[![Image 10](https://substackcdn.com/image/fetch/$s_!lj0o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a11817d-e8f4-4a1b-8252-08f2db5c6e87_1024x559.png)](https://substackcdn.com/image/fetch/$s_!lj0o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a11817d-e8f4-4a1b-8252-08f2db5c6e87_1024x559.png)

Software has a basal cost.

A feature charges rent simply by existing.

It may not receive active development. It may not be in a current roadmap. It may not have incidents every week. It may not appear in the list of strategic initiatives.

But it still exists.

And because it exists, people must account for it.

They must:

*   Avoid breaking it

*   Understand whether it is still used

*   Decide whether it participates in migrations

*   Include it in security thinking

*   Preserve compatibility

*   Explain it to new people

*   Test around it

*   Remember its edge cases

*   Carry it in the mental model of the product

That is basal cost.

And internal replacements for SaaS products add basal cost.

This is why the build-versus-buy question is not only about whether an internal solution is cheaper to create.

It is about whether the company deserves to add another permanent object to its economic surface area.

Some systems earn that right.

Many do not.

Opportunity cost is the part executives often underprice because it does not appear as an invoice.

But it is everywhere.

If your engineers are rebuilding a feature flag platform, they are not improving the product experience. If they are building a CRM replacement, they are not reducing customer churn. If they are maintaining an internal analytics tool, they are not improving the monetisation journey. If they are operating a custom allocation engine, they are not working on the constraint that actually limits growth. If they are debugging internal tooling, they are not reducing the cost of customer support. If they are spending weeks rediscovering how to work with the latest model release, they are not improving the product either.

This does not mean internal platforms are always bad.

Some internal capabilities are worth building because they unlock speed, safety, learning, or strategic differentiation.

But the decision must be explicit.

The question is not:

Can three people build this in six weeks with AI?

The question is:

Is this the best use of six weeks of those three people, plus all future ownership cost, plus the cost of maintaining the AI-assisted workflow that made the estimate attractive?

That is the opportunity cost question.

And it is the question the cheap-code argument tries to avoid.

Because once you ask it, “we can build it now” stops sounding like a strategy.

It becomes only one input.

There is an important distinction here.

The example of assigning customer orders to the nearest warehouse, or optimising order allocation across fulfilment centres, is not the same as rebuilding a generic SaaS product.

That kind of capability may be close to the economic engine of the business.

If allocation affects delivery time, fulfilment cost, stock availability, customer experience, margin, and operational efficiency, then it may be worth building internally.

Why?

Because the problem may be specific. The decision quality may matter. The context may be hard to buy. The data may be proprietary. The feedback loop may be local. The value may be large enough to justify ownership. The capability may become a strategic advantage.

That is a strong build candidate.

But that does not prove the general argument.

It proves the opposite.

It proves that build versus buy should be judged by economic context, not by excitement about cheaper code.

Internal order allocation may deserve ownership because it is close to the business model.

But that does not mean the same argument applies to:

*   A custom feature flag platform

*   A custom CRM

*   A custom observability stack

*   A custom billing engine, unless billing itself is part of the strategic differentiation

*   A custom support tool, unless support workflow is a core advantage

The mistake is using a strong core example to justify weak peripheral decisions.

That is how companies drift into accidental platform companies.

They do not decide to become one.

They just say “we can build this now” too many times.

[![Image 11](https://substackcdn.com/image/fetch/$s_!R292!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb2d43d-e9e9-4650-9b6c-332a04f1c463_1024x559.png)](https://substackcdn.com/image/fetch/$s_!R292!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb2d43d-e9e9-4650-9b6c-332a04f1c463_1024x559.png)

The word core is abused constantly.

A problem is not core because:

*   It is technically interesting

*   The team can build a better internal version

*   The vendor annoys us

*   The current SaaS is expensive

*   The architecture would be elegant

*   AI makes the implementation feel possible

Core means that the capability is materially tied to how the business creates, captures, protects, or compounds value.

That is a stricter test.

A capability may be core if improving it changes margin, conversion, retention, risk, learning speed, operational leverage, differentiation, or strategic optionality in a meaningful way.

A capability may not be core if it is simply necessary to operate.

Payroll is necessary. That does not mean most companies should build payroll software.

Authentication is necessary. That does not mean most companies should build identity platforms from scratch.

Feature flags are useful. That does not mean most companies should build their own feature flag system.

Observability is essential. That does not mean most companies should become observability vendors internally.

Necessary is not the same as strategic. Useful is not the same as core. Annoying is not the same as worth owning.

There is a better economic question than “can we build it?”

Can we amortise it?

If we invest in an internal system, the investment must pay back over repeated use.

A rough way to think about it is:

**Time to amortise = investment cost / net benefit per period**

But investment cost must include the full ownership cost, not only initial development.

And net benefit must be real.

Not:

*   “We saved licence money” while quietly spending more engineering time

*   “We have more control” while increasing operational fragility

*   “We can customise everything” while creating a maintenance swamp

*   “We can move faster” while adding one more system every team must understand

*   “AI made it cheaper” while the cost now depends on tokens, context, retries, output volume, and provider behaviour

*   “Developers are more productive” while the company ignores training, adaptation, workflow maintenance, benchmarking, and review cost

A good internal platform can amortise beautifully.

It can:

*   Build once

*   Be used many times

*   Reduce repeated effort

*   Standardise safe paths

*   Improve delivery

*   Reduce cognitive load

*   Make teams faster by removing accidental complexity

That is real.

But a bad internal platform does the opposite.

It is built once, maintained forever, used reluctantly, explained constantly, worked around frequently, upgraded painfully, migrated eventually, and retired never.

That is not an investment.

That is a mortgage disguised as empowerment.

[![Image 12](https://substackcdn.com/image/fetch/$s_!N1yN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd223bb7c-b0b3-4b1f-a7fc-6a1e0be0630e_1024x558.png)](https://substackcdn.com/image/fetch/$s_!N1yN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd223bb7c-b0b3-4b1f-a7fc-6a1e0be0630e_1024x558.png)

This is the part that feels counterintuitive.

A tool can lower the cost of an activity and still make the overall system worse.

How?

By increasing the volume of low-quality decisions.

If AI makes it easier to create internal software, more internal software will be created. Some of it will be useful. Some of it will be strategically important. Some of it will be experimental and disposable. Good.

But some of it will become permanent by accident.

A small script becomes an internal tool. An internal tool becomes a workflow. A workflow becomes a dependency. A dependency becomes a production concern. A production concern becomes a system nobody can remove. A system nobody can remove becomes part of the company’s carrying cost.

This is how cheap creation becomes expensive ownership.

The danger is not only that AI writes bad code.

The danger is that AI makes it easier to create more software than the organisation can responsibly understand, operate, and retire.

The constraint was never only code production.

The constraint is organisational digestion.

*   How much software can this company safely absorb?

*   How many systems can it operate?

*   How many behaviours can it test?

*   How many integrations can it reason about?

*   How many incidents can it handle?

*   How many dependencies can it upgrade?

*   How many internal platforms can it govern?

*   How many local exceptions can it remember?

*   How many AI-generated artefacts can it review?

*   How many provider-cost assumptions can it monitor?

*   How many workflow changes can it absorb without losing the efficiency it claims to have gained?

That is the real capacity question.

AI does not remove it.

It makes it more urgent.

There is a childish way of framing buy decisions as weakness.

The childish version says:

*   Real builders build

*   Strong engineering organisations create their own tools

*   SaaS is for companies that lack capability

*   Buying is dependency

*   Building is freedom

That is romantic nonsense.

Buying can be a disciplined decision.

It can mean the company understands where not to spend scarce attention. It can mean engineering capacity is being protected for higher-return work. It can mean the business refuses to turn every operational annoyance into an internal product. It can mean the organisation values liquidity. It can mean the company has enough humility to avoid becoming an accidental vendor for itself.

A good buy decision says:

This problem is real, but solving it internally does not create enough advantage to justify the ownership cost.

That is not weakness.

That is strategy.

The opposite can also be true.

A good build decision says:

This capability is close enough to our value creation, specific enough to our context, and valuable enough over time that ownership is justified.

That is also strategy.

The mature organisation can say both.

It knows what to own. It knows what not to own. It knows that control is not free. It knows that dependency is not always bad. It knows that internal capability must earn its place. It knows that AI can change the build case without automatically winning it.

The immature organisation treats “we can build it” as if it answered the question.

It does not.

There is another uncomfortable layer.

The cheap-code argument is attractive because it lets management avoid a harder conversation.

If the only problem is that software was expensive to produce, then AI looks like a simple managerial gift:

*   More output

*   Less cost

*   More internal options

*   Less vendor dependence

*   Higher apparent return

But if the real problem is total ownership, then management has to do harder work.

It must:

*   Decide what is core

*   Price opportunity cost

*   Understand maintenance capacity

*   Make ownership explicit

*   Fund the boring parts

*   Kill internal systems that do not pay back

*   Avoid turning every local pain into a permanent asset

*   Ask whether teams are already overloaded

*   Distinguish visible savings from real economic improvement

*   Understand whether the AI cost structure is stable enough to support the business case

*   Decide what happens if the provider changes the economics later

*   Train people properly instead of dumping tool uncertainty onto individual developers

*   Maintain the workflow, not only buy the subscription

That is less exciting.

It also requires more judgment.

And this is where many companies fail.

They talk about AI as if the main bottleneck was engineering typing speed.

But many software organisations are not slow because developers type too slowly.

They are slow because:

*   Decision-making is weak

*   Priorities conflict

*   Architecture is tangled

*   Teams are overloaded

*   Product discovery is shallow

*   Ownership is unclear

*   Old systems carry too much cognitive debt

*   Every change touches too many things

*   “Do nothing” has been accumulating cost for years

AI does not automatically fix any of that.

In weak systems, it can simply produce more material for the weakness to consume.

The decision should not be:

Can AI help us build this cheaper?

The decision should be:

Should we own this capability?

That question can be broken down.

Does it materially affect value creation, margin, retention, learning speed, risk reduction, differentiation, or strategic optionality?

If not, buying deserves serious consideration.

Good enough does not mean perfect.

It means the SaaS solution solves the problem well enough that internal ownership would not create enough additional return.

Many teams exaggerate uniqueness.

Every company has special cases.  
Not every special case justifies a custom system.

Will the internal solution pay back repeatedly over time?

Or is this just an expensive way to avoid a vendor invoice?

Not who will build it.

*   Who will own it when the original builders move on?

*   Who will respond to incidents?

*   Who will update dependencies?

*   Who will answer support questions?

*   Who will remove it when it stops paying back?

This is where averages become dangerous. The company does not need to know only how many artefacts exist per developer. It needs to know where ownership, knowledge, and operational responsibility are concentrated.

What does the company stop doing because this is now being built, operated, and maintained?

Can the company change course easily?

Or does this decision create migration cost, data lock-in, workflow lock-in, and organisational dependency?

Risk is not only probability.

Risk is probability multiplied by impact.

Impact includes sunk implementation cost, rollback cost, migration cost, disruption cost, delay introduced, and opportunity cost.

If being wrong is expensive, cheap initial development is not enough.

LLMs may reduce implementation effort.

But do they reduce:

*   Discovery cost

*   Maintenance cost

*   Support cost

*   Operational cost

*   Cognitive load

*   Risk

*   The cost of future change

If the answer is no, then the denominator has not fallen as much as the argument claims.

What happens if:

*   Token pricing changes

*   A tokenizer changes

*   The model produces longer outputs

*   The agent needs more retries

*   A plan moves from subscription-like pricing to usage-based billing

*   The default reasoning mode changes

*   The provider changes limits

*   The same workflow consumes more billable units next quarter

If the business case collapses under those questions, the decision was not economically robust.

It was optimistic.

If the company expects teams to use LLMs and agents, who pays the time required to learn them?

*   Who creates the internal guidance?

*   Who updates it?

*   Who verifies that old practices still work?

*   Who decides which features are safe to adopt?

*   Who teaches developers how to use the tools without producing more cognitive debt?

*   Who pays for the experimentation required to find out whether the tool is actually improving the work?

If the answer is “developers will figure it out,” the company is not doing economics.

It is externalising cost onto its own people.

How will it know whether the new AI workflow is better than the old one?

*   Not in a vendor demo.

*   Not in a generic benchmark.

*   Not in a leaderboard.

*   Not in a conference talk.

*   Not because one senior developer says “it works for me.”

In its codebase.

*   With its architecture.

*   With its tests.

*   With its review standards.

*   With its risk profile.

*   With its people.

*   With its product constraints.

If the company cannot answer that, then it does not know whether the investment works.

It only knows that the tools are fashionable.

The problem with the argument is not that it is completely false.

That would be easier.

The problem is that it is locally true and globally incomplete.

Yes, AI can make some internal development cheaper. Yes, some make decisions that previously looked irrational may now deserve reconsideration. Yes, some small teams can build useful systems faster than before. Yes, some core business capabilities may become more economically viable to own. Yes, the build-versus-buy frontier may move.

But that is not the same as saying that buying SaaS is now less necessary in general.

That leap is where the argument breaks.

It mistakes a movement in one cost component for a transformation of the whole economic equation.

It sees:

*   Cheaper creation, and ignores more expensive ownership

*   Local productivity, and ignores systemic carrying cost

*   The first six weeks, and ignores the next six years

*   Generated code, and ignores training, workflow maintenance, tool volatility, benchmarking, rework, review fatigue, and organisational adaptation

And now there is an additional problem.

It treats AI-assisted development cost as if it were stable, while the pricing unit itself is variable.

That is the deeper failure.

The cheap-code argument does not only underestimate cost.

It assumes cost stability in a market whose pricing unit, workflow surface, and tool behaviour are explicitly unstable.

That is not rigorous.

It is wishful accounting.

“We can build it now” sounds empowering.

It may even be true.

But as a decision rule, it is dangerous.

Because:

*   Possibility is not strategy

*   Feasibility is not value

*   Cheapness is not return

*   Internal control is not freedom

*   More code is not more capability

*   More capability is not more advantage

*   More systems are not more leverage

A company should be very careful when the main argument for building something is that building became easier.

That is the same logic that produces overengineering.

Only now it wears AI clothing.

Before, teams built abstractions because they could imagine future variation. Now, teams may build internal products because AI makes the first version feel cheap.

The psychology is similar.

The future cost is underpriced. The current excitement is overvalued. The organisation confuses capability with obligation.

And then, months later, everyone wonders why the team is slower despite having more tools.

The answer is usually simple.

They added more things to carry.

The better position is not anti-AI.

That would be lazy.

The better position is economically disciplined AI.

Use LLMs to:

*   Explore build options

*   Prototype

*   Test feasibility

*   Generate throwaway experiments

*   Compare vendor APIs

*   Model integration approaches

*   Create internal tools where ownership is justified

*   Reduce boilerplate

*   Accelerate learning

*   Support engineering judgment

But do not let them erase the ownership question.

A good AI-assisted make decision should produce more than code.

It should produce a better economic case.

It should clarify:

*   What problem is being solved

*   Why this problem matters

*   Whether the capability is core

*   What value is expected

*   What cost is avoided

*   What cost is introduced

*   What risks are reduced

*   What risks are added

*   What ownership model exists

*   What happens if the team is wrong

*   How the investment will be amortised

*   When the system should be retired

*   What token-cost assumptions support the case

*   What provider changes would break the case

*   What level of model behaviour is required

*   What level of agentic retry is acceptable

*   What happens if the cost per useful change increases

*   What training is needed

*   What workflow maintenance is expected

*   What benchmark will prove that the new way of working is actually better

That is the discipline.

AI should make the build case easier to test.

It should not make the build case easier to avoid.

The build-versus-buy decision has changed.

But not because “code is cheap now.”

It has changed because the cost structure of software work is being redistributed.

Some implementation work is cheaper. Some experimentation is faster. Some prototypes are easier. Some internal capabilities are more plausible. Some old buy decisions should be reopened.

But the deepest economics have not disappeared.

Software still has:

*   Carrying cost

*   Ownership

*   Cognitive load

*   Operational responsibility

*   Maintenance

*   Opportunity cost

*   Risk

*   The burden of earning its place

And AI adds another layer.

The cost of creating software may now depend on:

*   Tokens

*   Output length

*   Context size

*   Tool use

*   Model choice

*   Billing policy

*   Tokenizer behaviour

*   Reasoning modes

*   Cache behaviour

*   Provider decisions

It also depends on the company’s ability to train people, maintain the AI workflow, adapt to tool changes, and benchmark whether the new way of working is still better than the old one.

That is not a rounding error.

That is part of the economic model.

So the serious question is not whether AI lets us build more.

Of course it does.

The serious question is whether the organisation can economically absorb what it is now able to create, especially when part of the cost structure is controlled by someone else and part of the workflow keeps changing under its feet.

Because cheap code can still become expensive software.

And expensive software is not expensive because someone typed it slowly. It is expensive because the company must understand it, change it, operate it, secure it, support it, train people around it, maintain the workflow that produced it, and live with the consequences.

Now it may also be expensive because the tool that made it look cheap changed the bill.

The strongest version of the AI argument is worth taking seriously.

LLMs can reduce parts of software creation cost. That matters. It can change some investment decisions. It can make some internal solutions viable where they were previously too expensive. It can help teams prototype faster, explore alternatives earlier, and build certain capabilities with less initial effort.

But that is not the whole economic picture.

The weak version of the argument treats software as if its main cost were code generation. It is not. The main cost is often ownership.

That ownership includes maintenance, operations, security, observability, support, knowledge distribution, onboarding, dependency management, incident response, future change, training, workflow maintenance, and the opportunity cost of every hour spent carrying something the business did not need to own.

I’d like to give an example to help you understand the economic terms properly.

Let’s say we want to run manual tests, and we decide to automate those manual tests using LLMs. However, these won’t be fully automated tests; instead, the LLM will generate a report on the test it has performed, and a human will review it.

Option 1: Manual test done by a human

**Cost of an automated test = Creation cost + Maintenance cost**

Option 2: The manual test automated by LLMs (but still manual)

**Cost of a manual test with LLM = Cost of creating the prompt + Cost of tokens (depending on the day) + Review of the report**

Since this is a loop where, if the review is incorrect, you need to run the test again or change the prompt, you’re paying for each use. This might seem cheaper if you thought it were a one-time cost, but that is NOT the case.

Obviously, this example is flawed because it represents a misuse of LLMs, meaning the human is misusing the tool. However, the example I just provided is merely to illustrate the economic realities behind it and how misusing LLMs would end up costing you more than having a human do the job poorly. Because let’s not forget that humans, in the automated testing scenario, can also make mistakes, but the risk and cost of fixing the first scenario are much lower that a bad use of LLMs.

This is why the example of a core allocation system is not enough to justify a general movement away from SaaS. Some capabilities are worth building because they sit close to the business model. Others are merely necessary infrastructure, and necessary infrastructure does not automatically deserve internal ownership.

The economic test is stricter.

*   Can the company amortise the investment?

*   Does the capability create strategic advantage?

*   Is the market solution insufficient in a way that matters?

*   Will internal ownership reduce or increase long-term drag?

*   Who will own it after the first version?

*   What becomes slower because this now exists?

*   What is the cost of being wrong?

*   What happens if the AI cost structure changes?

*   What happens if the tokenizer changes?

*   What happens if the model consumes more tokens for the same work?

*   What happens if the provider changes limits, plans, reasoning defaults, or billing units?

*   Who pays the training cost?

*   Who maintains the AI workflow?

*   How does the company know that the new workflow is better than the old one?

*   Is the argument reproducible, or is it just another “it works on my machine”?

Those questions matter more now, not less.

AI has made it easier to create software.

That means software organisations need better economic judgment, not weaker judgment.

Because when creation gets cheaper, the temptation to create too much gets stronger.

And when the unit of creation is priced through a provider-controlled token system, the temptation becomes even more dangerous.

The cost was never just writing the code. The cost was carrying it. And now, part of the cost is also trusting that the machine that made it cheaper today will not make it more expensive tomorrow.

That is why the claim that AI makes internal development broadly more attractive than SaaS is not a serious economic conclusion by itself.

It is a partial observation pretending to be a strategy.

*   Artola, Luis. _Software economics_. [https://leanpub.com/software-economics](https://leanpub.com/software-economics)

*   Boehm, Barry W. _Software Engineering Economics_. Prentice-Hall, 1981.

*   Brooks, Frederick P. _The Mythical Man-Month: Essays on Software Engineering_. Addison-Wesley, 1975.

*   Ferro, Edu. _Basal Cost of software_. [https://www.eferro.net/2021/02/basal-cost-of-software.html](https://www.eferro.net/2021/02/basal-cost-of-software.html)

*   Rumelt, Richard P. _Good Strategy/Bad Strategy: The Difference and Why It Matters_. Profile Books, 2011.

*   Cagan, Marty. _INSPIRED: How to Create Tech Products Customers Love_. Wiley, 2018.

*   Fowler, Martin. _Refactoring: Improving the Design of Existing Code_. Addison-Wesley, 2018.

*   Fowler, Martin. _Refactoring_. [https://martinfowler.com/books/refactoring.html](https://martinfowler.com/books/refactoring.html)

*   Fowler, Martin. _Mind the platform execution gap_. [https://martinfowler.com/articles/platform-prerequisites.html](https://martinfowler.com/articles/platform-prerequisites.html)

*   Parnas, David Lorge. _On the Criteria To Be Used in Decomposing Systems into Modules_. [https://www.cs.umd.edu/class/spring2003/cmsc838p/Design/criteria.pdf](https://www.cs.umd.edu/class/spring2003/cmsc838p/Design/criteria.pdf)

*   GitHub. _GitHub Copilot is moving to usage-based billing_. [https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

*   GitHub Docs. _Usage-based billing for individuals_. [https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals](https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals)

*   Anthropic. _Pricing_. [https://platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing)

*   Anthropic. _Migration guide_. [https://platform.claude.com/docs/en/about-claude/models/migration-guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)

*   Anthropic. _What’s new in Claude Opus 4.7_. [https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7)

*   Anthropic. _An update on recent Claude Code quality reports_. [https://www.anthropic.com/engineering/april-23-postmortem](https://www.anthropic.com/engineering/april-23-postmortem)

*   Anthropic. _Introducing advanced tool use on the Claude Developer Platform_. [https://www.anthropic.com/engineering/advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use)

*   Anthropic. _Claude Code changelog_. [https://docs.anthropic.com/en/docs/claude-code/changelog](https://docs.anthropic.com/en/docs/claude-code/changelog)

*   OpenAI. _Codex changelog_. [https://developers.openai.com/codex/changelog](https://developers.openai.com/codex/changelog)

*   DORA. _State of AI-assisted Software Development 2025_. [https://dora.dev/dora-report-2025/](https://dora.dev/dora-report-2025/)

*   DORA. _DORA Research Program_. [https://dora.dev/research/](https://dora.dev/research/)

*   Buenosvinos, Carlos. _Software architecture and AI-assisted development_.

[Video 3](https://www.youtube.com/watch?v=J0PCKkFSZD4)
