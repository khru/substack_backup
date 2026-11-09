Title: The Productivity mirage

URL Source: http://emmanuelvalverderamos.substack.com/p/the-productivity-mirage

Final URL: https://emmanuelvalverderamos.substack.com/p/the-productivity-mirage

Published Time: 2026-06-11T05:01:19+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!DDQm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7571051f-cf21-4d9b-bab2-7e51c7739ac9_1024x558.png)](https://substackcdn.com/image/fetch/$s_!DDQm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7571051f-cf21-4d9b-bab2-7e51c7739ac9_1024x558.png)

Imagine a restaurant that buys a miraculous new oven.

Before the oven, the kitchen could prepare ten dishes per hour. After the oven, it can prepare thirteen, twenty, maybe one hundred. The kitchen manager is thrilled. The board is shown a clean chart: dishes produced per hour went up. Someone writes a confident internal memo saying the restaurant has become dramatically more productive.

Then you walk into the dining room and the story changes. Some tables are empty. Some dishes were never ordered. Some plates arrive faster than waiters can serve them. Some food looks perfect but has to be sent back after the first bite. The fridge is filling with leftovers. The menu is longer, but customers are not happier. Revenue has not improved. Waste has increased.

The kitchen became faster. The restaurant did not become more productive.

That is the mistake many organizations are about to make with _Large Language Models_ (_LLMs_) and software development. They will look at the subsystem where output is easiest to count, the development team, and confuse local acceleration with organizational productivity.

But an organization is not a code generator. A product is not a pull request factory. A business is not a backlog-burning machine. An organization becomes more productive when it turns investment into useful outcomes with acceptable cost, risk, quality, flow, maintainability, and learning. If _LLM_-based AI helps a team generate more software that nobody uses, nobody wants, nobody deletes, and everyone has to maintain, the organization has not become more productive. It has become better at manufacturing liabilities.

**Every time I say AI on this article I’m talking about LLM and agents, and also MCP, because all of this elements ARE NOT AI. But everybody call this AI**

_LLM_-based AI may increase coding activity and some upstream throughput metrics. That does not prove organizational productivity. Productivity is not measured by how much software enters the system. It is measured by how much investment returns as useful, adopted, maintainable value.

Efficiency, effectiveness, and productivity are not the same thing. A development team can become more efficient at producing features while the organization becomes less effective at creating value. If productivity is defined as “more features,” then more features will look like success. But the organization does not exist to maximize feature count. It exists to generate return from investment.

The development team is a subsystem. Optimizing that subsystem can overload discovery, prioritization, review, testing, deployment, operations, support, maintenance, and customer adoption. If the organization cannot show better outcomes, better flow, better quality, lower risk, lower cost of ownership, or higher _Return on Investment_ (_ROI_), it should not claim that AI made it more productive.

A feature is an investment only when there is a plausible path to return. If it does not create value, reduce risk, increase learning, improve flow, or create useful optionality, it is not an investment. It is cost.

1.   Productivity, efficiency, and effectiveness are not the same thing

2.   The productivity claim is using the wrong boundary

3.   Software is an investment before it is value

4.   Output, outcome, and the ladder of evidence

5.   More output can create more economic burden

6.   Flow decides whether local speed becomes system throughput

7.   Systems thinking: the structure produces the behavior

8.   What the evidence actually says

9.   The AI-assisted feature equation

10.   What organizations should measure instead

11.   Conclusions

12.   References

[![Image 2](https://substackcdn.com/image/fetch/$s_!PX7w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb28ae4c2-0902-4c4b-a241-3c7e631e91cb_1024x558.png)](https://substackcdn.com/image/fetch/$s_!PX7w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb28ae4c2-0902-4c4b-a241-3c7e631e91cb_1024x558.png)

Before discussing whether _Large Language Models_ (_LLMs_) make organizations more productive, we need to slow down and ask a more basic question: productive at what?

Efficiency is about the relationship between resources consumed and output produced. If a team creates the same output with less time, less effort, or less cost, it has become more efficient at that activity. A code assistant may improve efficiency in some parts of development if it helps produce drafts, tests, migrations, documentation, or repetitive changes with less effort.

Effectiveness is different. Effectiveness asks whether the thing we produced achieved the intended purpose. A team can be efficient at building features and still ineffective at improving the product. A feature delivered quickly but ignored by users is not an effective business outcome. It is merely an efficiently produced cost.

Productivity is the most dangerous word because it depends on what we decide to count. A basic productivity ratio compares output with input, but the ratio becomes misleading when we choose the wrong output. If productivity means “features delivered per month,” then producing more features makes a team look more productive. That definition may be useful inside a narrow development dashboard, but it is not enough for an organization.

The organization does not exist to maximize feature count. It exists to turn investment into valuable return. That return may appear as revenue, adoption, retention, lower support load, lower operational cost, reduced risk, faster learning, or stronger strategic positioning. More features only matter if they contribute to that return.

[![Image 3](https://substackcdn.com/image/fetch/$s_!B_By!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff26696ec-87dc-4597-a2d8-bd4ae4d92b6c_1792x700.png)](https://substackcdn.com/image/fetch/$s_!B_By!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff26696ec-87dc-4597-a2d8-bd4ae4d92b6c_1792x700.png)

This is why productivity is misleading when we do not name the goal. If we evaluate productivity as “more functionality shipped,” we can always make the number go up. We can generate more code, open more pull requests, merge more changes, and release more product surface area. But if those features do not increase adoption, traction, learning, cost reduction, or _ROI_, the organization has not become more productive. It has become more efficient at creating cost.

Productivity is not neutral. It always hides a theory of value.

So the real question is not whether _LLMs_ help us produce more software. The real question is whether they help the organization produce more valuable outcomes per unit of investment. If we do not make that distinction, we are not measuring productivity. We are measuring movement and hoping it means progress.

[![Image 4](https://substackcdn.com/image/fetch/$s_!pQBH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41893280-73de-4c34-80cd-d1a8c4369a4d_1024x558.png)](https://substackcdn.com/image/fetch/$s_!pQBH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41893280-73de-4c34-80cd-d1a8c4369a4d_1024x558.png)

The claim usually sounds practical.

*   “We are more productive because developers complete more tickets.”

*   “We are more productive because pull requests are created faster.”

*   “We are more productive because AI helps us ship more features.”

*   “We are more productive because our engineers write more code with fewer people.”

Those claims may describe local activity, but they do not prove organizational productivity. They measure what happens inside one part of the system. They do not prove that the whole system is turning investment into value.

The development team is a subsystem. A very important one, but still a subsystem. It receives signals from product strategy, discovery, customer research, sales pressure, incidents, compliance needs, executive urgency, architecture constraints, and operational reality. It produces software changes that must travel through review, testing, deployment, release, adoption, support, learning, maintenance, and sometimes deletion.

A simplified value stream looks like this:

```
Idea
-> Discovery
-> Prioritization
-> Design
-> Development
-> Review
-> Testing
-> Deployment
-> Release
-> Adoption
-> Support
-> Learning
-> Evolution or deletion
-> Economic return
```

Development matters, but it is not the whole journey. In many organizations, development is not even the constraint. The constraint may be unclear strategy, slow decision-making, too much _Work in Progress_ (_WIP_), weak product discovery, overloaded review, brittle tests, manual regression, release fear, poor observability, high support load, or inability to delete.

If the constraint is not code generation, making code generation faster will not necessarily increase organizational throughput. It may simply create more inventory before the real bottleneck.

![Image 5](https://substackcdn.com/image/fetch/$s_!dD6S!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17840b2-157e-4899-b828-4aba57121ed8_5730x684.png)

That inventory might look like pull requests waiting for review. It might look like half-finished tickets. It might look like features shipped but not adopted. It might look like code paths that nobody understands six months later. It might look like support burden, incident risk, cloud cost, test maintenance, documentation drift, or product surface area that users must navigate.

Software inventory is dangerous because it does not always look like inventory. It does not sit on a shelf with dust on it. It hides inside the codebase, the product interface, the test suite, the deployment pipeline, the support queue, and the minds of the people who must remember why it exists.

So the first question is not whether developers can move faster with _LLMs_. Sometimes they can. The first question is whether faster movement inside the development subsystem improves the larger economic system.

[![Image 6](https://substackcdn.com/image/fetch/$s_!WJYV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb2921c9-7a18-4bba-8f87-ef17c273797d_1024x559.png)](https://substackcdn.com/image/fetch/$s_!WJYV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb2921c9-7a18-4bba-8f87-ef17c273797d_1024x559.png)

A feature is not “work completed.” A feature is capital placed at risk in the hope of future benefit.

Before a feature is adopted, it is not value. It is a bet. It consumes time, money, attention, opportunity, and risk capacity before reality tells us whether it was worth building. That distinction changes the entire conversation.

The uploaded software-economics chapter frames software as a way to turn money, time, attention, and judgment into capability, then capability into value, and value into return. It also makes a simple but often ignored point: closed tickets and lines of code do not imply profit.

That means a company should not ask only, “What can AI help us build faster?” It should also ask what evidence suggests the feature should exist, what customer behavior would prove that it matters, what the cost of being wrong is, what better alternative is being delayed, how quickly the organization will know whether the idea worked, how easily the feature can be removed, and what it will cost while it exists.

Those questions are not philosophical decoration. They are software economics.

An investment needs return. In software, return may appear as revenue, retention, conversion, reduced operational cost, lower support burden, faster learning, reduced risk, stronger strategic positioning, or increased ability to change. _ROI_ is not only about “money came back immediately.” It is about whether the value created justifies the investment made, when that return arrives, how likely it is, what was blocked while waiting, and how much freedom remains after the commitment.

A feature that creates no return is not a weak investment. It is cost.

This is where _LLM_-based AI changes the shape of the problem. If AI reduces the apparent cost of producing software, it becomes easier to create more bets. That can be useful when the organization is disciplined about discovery, small slices, fast feedback, adoption measurement, and deletion. It becomes dangerous when the organization already confuses output with value.

Cheaper production does not create demand. It only lowers the friction required to place more bets.

[![Image 7](https://substackcdn.com/image/fetch/$s_!5_OJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f418d42-5a23-48bc-af69-5a9fc038ede3_1024x558.png)](https://substackcdn.com/image/fetch/$s_!5_OJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f418d42-5a23-48bc-af69-5a9fc038ede3_1024x558.png)

A lot of AI productivity arguments collapse because they use the wrong word at the wrong level.

Output is what the system produces: prompts, generated code, accepted suggestions, commits, pull requests, tickets, features, releases.

Outcome is the useful change caused by that output: customer adoption, revenue growth, retention improvement, lower support load, reduced operational cost, faster learning, lower risk, or a better ability to change direction.

Throughput is the rate at which valuable work flows through the whole system. More coding activity is not necessarily more throughput if work piles up in review, testing, deployment, customer adoption, or maintenance.

[![Image 8](https://substackcdn.com/image/fetch/$s_!P-ex!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfcbb283-6de2-4e69-ad5b-bf93665db480_670x1804.png)](https://substackcdn.com/image/fetch/$s_!P-ex!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfcbb283-6de2-4e69-ad5b-bf93665db480_670x1804.png)

The higher we climb, the harder the productivity claim becomes. Generated code is easy to count. Accepted suggestions are easy to count. Pull requests are easy to count. Adoption is harder. Retention is harder. Economic return is harder. Deletion discipline is harder.

That is why organizations often stop measuring too early.

They measure activity and call it productivity. They measure output and call it value. They measure local speed and call it business improvement.

A healthier measurement ladder would separate the layers:

*   **Activity metrics**: prompts, generated code, accepted suggestions, commit

*   **Engineering throughput metrics**: pull requests, merged changes, cycle time, lead time, deployments

*   **Product and business metrics**: adoption, retention, conversion, revenue, cost reduction, support reduction

*   **Economic metrics**: ROI, opportunity cost, cost of delay, cost of carry, maintenance cost, risk, liquidity, optionality

The mistake is not measuring activity. Activity can be useful diagnostic data. The mistake is stopping there. A pulse tells you a body is alive, but it does not tell you whether it is healthy, learning, recovering, or winning a marathon.

The same is true for software organizations.

[![Image 9](https://substackcdn.com/image/fetch/$s_!gdAp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27cb32d8-17e4-42a2-8362-208efb3a7261_1024x558.png)](https://substackcdn.com/image/fetch/$s_!gdAp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27cb32d8-17e4-42a2-8362-208efb3a7261_1024x558.png)

More software is not only more capability. More software is also more surface area.

Every feature that remains in a product has ongoing cost. It must be understood, tested, secured, supported, documented, migrated, monitored, and considered during future changes. The uploaded software-economics chapter says more software is also more burden, and that a feature must justify both its initial cost and its continuing cost of existence. It also defines risk as the probability and consequence of being wrong, which is essential when the wrong feature can become a long-lived cost.

This ongoing burden is close to what Eduardo Ferro calls the basal cost of software: the cost generated by software simply existing. A feature nobody uses may still increase onboarding friction, support effort, test complexity, deployment risk, security surface, and cognitive load. It may not create visible revenue, but it keeps sending invoices to the organization. Thoughtworks’ discussion of the concept summarizes it as the cost of features beyond initial development, including maintenance and onboarding until the feature is dead. ([Basal cost of software by Edu Ferro](https://www.eferro.net/2021/02/basal-cost-of-software.html))

That is why deletion is not housekeeping. Deletion is an economic practice.

If an organization proudly says, “AI helped us ship 100 features instead of 10,” the first question should be: “How many did customers adopt?” The second should be: “How many created measurable value?” The third should be: “How many did you remove when they did not?”

If the answer to the third question is zero, the organization may not have improved productivity. It may have expanded its cost base.

There are three economic terms that make this clearer.

Opportunity cost is the value of the best alternative you gave up. When a team builds low-value features, the cost is not only the effort spent on those features. It is also the onboarding problem not fixed, the incident rate not reduced, the product complexity not simplified, the customer research not done, the old feature not deleted, and the bottleneck not addressed.

Cost of carry is the cost of holding unfinished or unvalidated work. In software, work in progress consumes attention, coordination, context, review capacity, decision capacity, and risk capacity. Branches, tickets, pull requests, unreleased features, partial migrations, and ambiguous decisions all carry cost while they wait.

Cost of delay is the economic loss caused by receiving value later than we could have. If _LLMs_ help teams start more work but review, testing, release, or adoption becomes slower, the organization can celebrate local acceleration while increasing economic delay.

This is the trap. AI can make it easier to produce more software, but if that software does not become useful value, the organization has not created more productivity. It has created more cost, faster.

[![Image 10](https://substackcdn.com/image/fetch/$s_!PeJD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1e3a51b-2a8a-4747-8aad-6b4d01ebf953_1024x559.png)](https://substackcdn.com/image/fetch/$s_!PeJD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1e3a51b-2a8a-4747-8aad-6b4d01ebf953_1024x559.png)

Lean thinking is allergic to the confusion between activity and value.

A busy system is not necessarily a flowing system. A fully utilized system is often a clogged system. A team that starts many things can look committed while becoming slow, brittle, and unable to respond.

The uploaded software-economics chapter puts this plainly: organizations often assume that the healthiest system is the one where everyone is busy, but a system optimized for utilization can become congested, overloaded, and slow. Activity rises while delivery suffers. It also frames liquidity as the ability to redirect effort, attention, knowledge, and investment toward the most valuable next move.

This matters because _LLM_-based AI can increase the amount of work entering the delivery system. More generated code. More branches. More pull requests. More suggested changes. More features asking to exist. If the rest of the value stream cannot absorb that work, queues grow.

A queue is not a harmless waiting room. It is a place where investment is trapped.

Pull requests waiting for review are trapped investment. Features waiting for release are trapped investment. Product decisions waiting for evidence are trapped investment. Code deployed behind flags but never evaluated is trapped investment. Every queue delays learning, delays return, and increases the chance that the work becomes stale before it becomes valuable.

This is where _Theory of Constraints_ (_TOC_) gives us a clean rule: improving a non-constraint does not improve the whole system. If review is the constraint, generating more code creates a review queue. If product discovery is the constraint, generating more features creates more wrong things faster. If deployment is the constraint, merging more code increases unreleased inventory. If customer adoption is the constraint, shipping more features increases product noise.

![Image 11](https://substackcdn.com/image/fetch/$s_!MN76!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F406d0a9f-3f59-4c9a-adc7-53bccf476d08_3536x188.png)

A highway does not improve because more cars enter it. It improves when more people reach their destination safely and predictably.

Software works the same way. Starting more work is not productivity. Finishing more valuable work with less waste is closer. Learning sooner is closer. Reducing the cost of change is closer. Creating customer behavior that justifies the investment is closer.

A development system can be full of motion and still void of progress.

[![Image 12](https://substackcdn.com/image/fetch/$s_!YSRk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf0bf644-bd8d-45c8-8ee0-cad027a1ab3f_1024x558.png)](https://substackcdn.com/image/fetch/$s_!YSRk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf0bf644-bd8d-45c8-8ee0-cad027a1ab3f_1024x558.png)

Systems thinking helps us avoid the illusion that a single tool can transform an organization by itself.

Donella Meadows explains systems through elements, interrelations, and purpose. The visible parts matter, but behavior comes from how those parts are connected and what the system is organized to produce. Her Slinky example is useful because it shows that the same external action can produce different behavior depending on the internal structure of the system.

That is exactly what happens when _LLMs_ enter software organizations.

AI does not enter an empty room. It enters incentives, queues, review habits, release mechanisms, product pressure, quality thresholds, budget models, team topology, architecture, customer feedback loops, and leadership beliefs. If the organization rewards output over outcomes, AI will not fix that. It will help the organization produce more of what it already rewards.

If teams are praised for shipping more features, AI will help ship more features. If teams are praised for closing tickets, AI will help close tickets. If teams are praised for visible busyness, AI will create more visible busyness. If nobody is accountable for adoption, deletion, cost of carry, or _ROI_, AI will not magically create that accountability.

This is why the problem is not only technical. It is structural.

A company may say its purpose is customer value, but if its budget process, planning rituals, promotion criteria, roadmap reviews, and executive dashboards reward output, then output is the real operating goal. Meadows’ systems lens is uncomfortable because it asks us to infer purpose from behavior, not from slogans.

![Image 13](https://substackcdn.com/image/fetch/$s_!1IKo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F738414b6-a73e-48d9-a274-e409ab526843_4867x258.png)

This loop is not a prediction that every organization will suffer in the same way. It is a warning about a plausible structure. When the system rewards output, more generated code can increase review pressure. More review pressure can create queues. Queues can create pressure to move faster. Pressure can produce shallower review. Shallow review can increase defects and rework. Rework consumes capacity, and lower capacity creates more pressure to produce.

That is why the AI productivity debate should not start with “Which tool should we buy?” It should start with “What does our system currently reward?”

If the answer is output, AI may make the system worse while making the dashboard look better.

[![Image 14](https://substackcdn.com/image/fetch/$s_!5b0L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23375bc8-711a-4fc7-880d-ea5353b7bb5c_1024x558.png)](https://substackcdn.com/image/fetch/$s_!5b0L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23375bc8-711a-4fc7-880d-ea5353b7bb5c_1024x558.png)

The evidence around AI-assisted software development is still developing, and it does not support a simple slogan. It does not support “AI makes organizations productive.” It also does not support “AI is useless.” The more careful reading is this: local coding activity can increase, but the effect weakens as we move toward production, usage, quality, and economic return.

The _SPACE_ framework matters because it was created to avoid the mistake of reducing developer productivity to one activity metric. It defines developer productivity across satisfaction and well-being, performance, activity, communication and collaboration, and efficiency and flow. It also names “productivity is all about developer activity” as a myth and warns that activity metrics should not be used in isolation. ([queue.acm.org](https://queue.acm.org/detail.cfm?id=3454124))

DORA is useful because it studies software delivery performance and organizational capabilities. Its 2025 AI-assisted software development report does not say that buying AI tools is enough. It says AI acts as an amplifier, magnifying an organization’s existing strengths and weaknesses, and that the greatest returns come from focusing on the underlying organizational system rather than the tools alone. ([dora.dev](https://dora.dev/dora-report-2025/))

Faros gives us a sharper operational warning because its 2026 report analyzes engineering telemetry from 22,000 developers and 4,000 teams. That matters because telemetry lets us look beyond how productive people feel and inspect downstream signals such as review time, code quality, incidents, churn, and lead time. Faros reports increased task completion and code-related work, but also reports that bugs per developer rose 54 percent, the incidents-to-pull-request ratio more than tripled, median review time increased 5x, and 31 percent more pull requests merged without review.

The throughput section of the Faros report is especially important. It reports task throughput per developer up 33.7 percent, epics completed per developer up 66.2 percent, pull-request merge rate up 16.2 percent, and code-related tasks up 210 percent. But deployment frequency is the exception: deployments per week fell in the measured subset, while code churn increased 861 percent. Faros itself warns that throughput measures what was shipped, not what survived.

The NBER working paper _Writing Code vs. Shipping Code_ studies productivity effects across generations of AI coding tools. The public NBER page identifies it as a 2026 working paper by Mert Demirer, Leon Musolff, and Liyuan Yang, and the public PDF preview says the effect builds gradually, consistent with the lag between writing code and shipping a release. ([NBER](https://www.nber.org/papers/w35275))

That evidence is valuable because it separates writing code from shipping code. It also suggests that even release-like output is not the end of the story. The chart that motivated this article makes the next step visible: more app releases do not automatically imply more significant usage, more reviews, or more traction.

Pendo’s 2019 feature adoption report adds the product-side warning. It analyzed anonymized product usage data and found that 80 percent of features in the average software product were rarely or never used. The PDF also reports that 12 percent of features generated 80 percent of average daily usage volume. This is vendor research, so it should not be treated as a universal law. Still, it is a useful warning: many organizations already build more functionality than users meaningfully adopt. ([Pendo.io](https://www.pendo.io/resources/the-2019-feature-adoption-report/))

Token pricing makes the cost side more visible. GitHub announced that Copilot plans transition to usage-based billing on June 1, 2026, with usage calculated from token consumption, including input, output, and cached tokens. GitHub’s documentation also explains that Copilot interactions consume input tokens, output tokens, and cached tokens, with the total converted into AI credits. OpenAI’s pricing documentation says tokens are billed at the chosen model’s input and output rates, and Anthropic’s pricing documentation describes cache write and cache read token pricing. ([The GitHub Blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/))

The responsible conclusion is not that AI reduces productivity. That would be too blunt.

The responsible conclusion is sharper: some datasets show local acceleration in coding activity and upstream delivery metrics, but organizational productivity remains unproven unless the organization can show better outcomes, better flow, better quality, lower risk, lower cost of ownership, or higher _ROI_.

[![Image 15](https://substackcdn.com/image/fetch/$s_!4C9r!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c3f24a5-cc65-445e-97b4-23899f68b6dd_1024x559.png)](https://substackcdn.com/image/fetch/$s_!4C9r!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c3f24a5-cc65-445e-97b4-23899f68b6dd_1024x559.png)

A feature is an investment equation before it is a product announcement.

A useful thinking model is not “feature cost equals build cost.” Build cost is only one line in the equation. The economic result of a feature depends on the benefit it may produce, the cost of creating it, the cost of carrying it, and the risks attached to being wrong.

A better model is this:

```
Expected economic result of a feature =
expected benefit
- opportunity cost
- discovery cost
- build cost
- review cost
- testing cost
- deployment cost
- operational cost
- maintenance cost
- basal cost
- cost of carry
- product adoption risk
- technical risk
- operational risk
- rework risk
```

The product adoption risk deserves to be explicit. It is the risk that users do not want, adopt, understand, or value the feature. That risk is not secondary. In product software, it is often the central risk. A feature is not valuable because it exists. It becomes valuable when users, customers, or the organization absorb it in a way that creates return.

With _LLM_-based AI, the equation does not disappear. It changes shape:

```
Expected economic result of an AI-assisted feature =
expected benefit
- opportunity cost
- discovery cost
- prompting and orchestration cost
- token cost
- build cost
- review cost
- testing cost
- deployment cost
- operational cost
- maintenance cost
- basal cost
- cost of carry
- product adoption risk
- technical risk
- operational risk
- rework risk
```

Some costs may go down. It is plausible that _LLMs_ reduce the cost of scaffolding, exploration, code generation, migration drafts, repetitive changes, test data generation, documentation drafts, and some forms of technical discovery. That should be measured, not assumed.

[![Image 16](https://substackcdn.com/image/fetch/$s_!NTmN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabf36fcb-caa9-4eec-96cc-6859a8c352d4_1024x558.png)](https://substackcdn.com/image/fetch/$s_!NTmN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabf36fcb-caa9-4eec-96cc-6859a8c352d4_1024x558.png)

Some costs may go up. Prompting and orchestration can become real work. Token usage can become a visible operating cost. Review may become harder if generated changes are larger. Testing may need to become stronger if confidence falls. Rework may increase if accepted code is not production-ready. Maintenance may increase if the organization ships more surface area. Basal cost increases when more features remain alive without creating enough value.

![Image 17](https://substackcdn.com/image/fetch/$s_!6sgh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35d8a25a-3528-43ce-af38-13dc9a18031c_6148x812.png)

The economic question is not whether AI made one line cheaper. The economic question is whether the total system became cheaper, safer, faster to learn from, and more capable of producing return.

If the savings in build cost are eaten by higher review cost, higher rework, higher token spend, higher maintenance, higher basal cost, and the same or worse adoption risk, the organization has not improved the outcome. It has only moved cost from one column to another.

The dangerous move is to look only at reduced build cost and declare victory.

That is like saying a mortgage is cheap because the first payment was small.

[![Image 18](https://substackcdn.com/image/fetch/$s_!uQte!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda61b536-dc4a-4bf0-b5e0-46ecf558c4d8_1024x559.png)](https://substackcdn.com/image/fetch/$s_!uQte!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda61b536-dc4a-4bf0-b5e0-46ecf558c4d8_1024x559.png)

A productive organization does not merely produce more. It converts more of its investment into useful outcomes with less waste, lower risk, and better optionality.

That requires a different measurement conversation.

First, measure adoption. Are users adopting the shipped changes? Are customers reaching value sooner? Are feature usage, retention, conversion, revenue, or operational efficiency improving? Are we measuring actual behavior, or only internal activity?

Second, measure flow across the whole value stream. Is valuable work moving faster from idea to validated outcome? Is lead time improving from concept to production, not only from coding start to pull request? Are review queues, QA queues, release queues, and decision queues shrinking?

Third, measure investment quality. Are bets smaller? Is opportunity cost lower? Are we learning earlier? Are we avoiding large batches of speculative functionality? Are we killing weak ideas before they become expensive software?

Fourth, measure quality and safety. Are bugs, incidents, rework, rollback frequency, change failure rate, and support load improving? Or are we raising output while lowering the quality threshold?

Fifth, measure maintenance burden. Is the codebase becoming easier to understand, change, test, and operate? Are we reducing basal cost, or adding permanent complexity?

Sixth, measure deletion discipline. Are unused features removed? Do we know which features are rarely used? Can we safely delete code, flags, screens, options, endpoints, reports, and workflows that no longer justify their existence?

Seventh, measure liquidity. Can the organization redirect effort quickly when evidence changes? Can it pause work, split work, abandon weak bets, and reinvest in stronger ones?

Eighth, measure human system health. Are developers, reviewers, product people, support teams, and operators less overloaded? Or has AI shifted pressure from writing code to reviewing, coordinating, cleaning, and firefighting?

These questions are less glamorous than “How much faster can we code?” They are also more economically honest.

A company can claim AI improved organizational productivity only when it can show that more value flows through the whole system, not merely that more output exits the development subsystem.

[![Image 19](https://substackcdn.com/image/fetch/$s_!9J2R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6157a6b-c6c8-488c-80ed-95e3f316e6d2_1024x559.png)](https://substackcdn.com/image/fetch/$s_!9J2R!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6157a6b-c6c8-488c-80ed-95e3f316e6d2_1024x559.png)

_LLM_-based AI changes software development, but it does not repeal software economics.

It can help developers explore faster, draft faster, generate faster, automate repetitive changes, summarize unfamiliar code, and create useful leverage in the right context. None of that should be dismissed. The argument is not that AI is useless. The argument is that “more code” is not the same as “more organizational productivity.”

Productivity is not a property of the development team alone. It is a property of the whole system that turns investment into outcomes. If one subsystem accelerates while the rest of the system becomes overloaded, the organization has not necessarily improved. It may have created a faster path to waste.

A company that ships 100 features nobody wants is not more productive than a company that ships 10 features customers actually use. It is not more innovative because its backlog burns faster. It is not more efficient because its developers accept more generated code. It is not more competitive because its product surface area expands.

The serious productivity question is harder. Did we create more useful value? Did we learn sooner? Did we reduce the cost of change? Did we improve flow across the whole value stream? Did we reduce risk? Did we remove what did not work? Did the investment return more than it consumed?

If the answer is no, then AI did not make the organization more productive. It made one subsystem louder.

And this is where the conversation should stop being polite.

**Spending more money to generate more code and calling it productivity does not make you more productive. It makes you a worse steward of capital.**

If you can generate 30 percent more features but cannot show more adoption, more traction, more revenue, more learning, more cost reduction, or better _Return on Investment_ (_ROI_), those features are not proof of productivity. They are a larger cost base.

You are not celebrating productivity. You are celebrating the ability to spend more while producing less economic value.

If you can create more features than before and still fail to increase _ROI_, the conclusion is not that the software industry has changed beyond recognition. The conclusion is simpler and harsher: you never understood the economics of software in the first place.

That says more about you as a business operator, and more about your organization, than it says about the future of software.

The future advantage will not belong to organizations that generate the most software. It will belong to organizations that can decide what should exist, validate it quickly, ship it safely, measure whether it matters, and delete it when it does not.

In an age where producing software becomes easier, judgment becomes the scarce resource.

*   Anthropic. _Claude API Pricing_. [https://platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing)

*   Anthropic. _Prompt Caching_. [https://platform.claude.com/docs/en/build-with-claude/prompt-caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

*   Demirer, Mert, Musolff, Leon, Yang, Liyuan. _Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools_. [https://www.nber.org/papers/w35275](https://www.nber.org/papers/w35275)

*   DORA. _State of AI-assisted Software Development 2025_. [https://dora.dev/dora-report-2025/](https://dora.dev/dora-report-2025/)

*   Faros AI. _AI Engineering Report 2026: The Acceleration Whiplash_. [https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways](https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways)

*   Ferro Aldama, Eduardo. _Basal Cost of Software_. [https://www.eferro.net/2021/02/basal-cost-of-software.html](https://www.eferro.net/2021/02/basal-cost-of-software.html)

*   Forsgren, Nicole, Storey, Margaret-Anne, Maddila, Chandra, Zimmermann, Thomas, Houck, Brian, Butler, Jenna. _The SPACE of Developer Productivity_. [https://queue.acm.org/detail.cfm?id=3454124](https://queue.acm.org/detail.cfm?id=3454124)

*   GitHub. _GitHub Copilot Is Moving to Usage-based Billing_. [https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

*   GitHub Docs. _Usage-based Billing for Organizations and Enterprises_. [https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises)

*   Meadows, Donella H. _Thinking in Systems: A Primer_. [https://www.chelseagreen.com/product/thinking-in-systems/](https://www.chelseagreen.com/product/thinking-in-systems/)

*   OpenAI. _API Pricing_. [https://developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing)

*   Pendo. _The 2019 Feature Adoption Report_. [https://www.pendo.io/resources/the-2019-feature-adoption-report/](https://www.pendo.io/resources/the-2019-feature-adoption-report/)

*   Poppendieck, Mary, Poppendieck, Tom. _Implementing Lean Software Development: From Concept to Cash_. [https://www.pearson.com/en-us/subject-catalog/p/implementing-lean-software-development-from-concept-to-cash/P200000003154](https://www.pearson.com/en-us/subject-catalog/p/implementing-lean-software-development-from-concept-to-cash/P200000003154)
