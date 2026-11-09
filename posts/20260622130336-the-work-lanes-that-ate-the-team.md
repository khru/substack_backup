Title: The work lanes that ate the team

URL Source: http://emmanuelvalverderamos.substack.com/p/the-work-lanes-that-ate-the-team

Final URL: https://emmanuelvalverderamos.substack.com/p/the-work-lanes-that-ate-the-team

Published Time: 2026-06-22T13:03:36+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!FlxN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67a82d68-d209-4dc4-bd0b-5a0d8938eb9a_1024x559.png)](https://substackcdn.com/image/fetch/$s_!FlxN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67a82d68-d209-4dc4-bd0b-5a0d8938eb9a_1024x559.png)

Imagine a small restaurant with one kitchen. There is one group of cooks, one oven, one set of knives, one queue of orders, and one dining room full of people waiting. At first, the work is obvious: cook good food and serve it while it is still warm.

Then someone tries to make the kitchen more predictable. Forty percent of the kitchen is for new dishes. Twenty percent is for complaints. Fifteen percent is for cleaning. Fifteen percent is for menu improvements. Ten percent is for sharpening knives, repairing tools and keeping the kitchen healthy.

The spreadsheet looks mature because every category has space. Nobody can say their concern was ignored. The manager can point at the plan and say, “We have reserved capacity for everything.”

Then reality enters through the back door. A pan catches fire during the “new dishes” allocation. A knife becomes blunt during the “complaints” allocation. A customer sends food back during the “cleaning” allocation. The oven starts failing during the “menu improvement” allocation.

Nobody in the dining room cares which percentage bucket the problem belongs to. They care whether the restaurant can serve good food.

Software teams are not kitchens, but the mistake is similar. We split work into artificial lanes and manage the lanes as if they were independent sources of value: product development, support, bugs, UX feedback, technical initiatives, reliability, security, operations and documentation.

The names are useful. The separation is the trap.

There is only one business. There is one product investment. There is one value stream. The rest is demand classification.

[![Image 2](https://substackcdn.com/image/fetch/$s_!OJDO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff61843a8-cb8d-40c7-81dd-e4b8c33681d9_1672x941.png)](https://substackcdn.com/image/fetch/$s_!OJDO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff61843a8-cb8d-40c7-81dd-e4b8c33681d9_1672x941.png)

Many companies create “work lanes” and reserve fixed percentages of team capacity for each one: product work, support, bugs, UX feedback, technical initiatives, security, reliability and operations. This feels organised, but it often hides the real problem: the team has more demand than capacity and too much _Work in Progress_ (WIP).

The flaw is not that support, bugs, UX feedback or technical work are unimportant. They are real. The flaw is treating them as separate internal businesses competing for fixed slices of the same team.

A product team has one economic mission: protect and improve the product’s ability to create value. Product work creates or extends user value. Support restores blocked value. Bugs remove negative value. UX feedback improves learning. Technical work protects delivery capacity, reduces risk or lowers the cost of change. Reliability protects continuity of value. Security reduces exposure to loss.

All of them belong to the same economic system.

When these categories become fixed percentages, the team starts serving the allocation model instead of the user. Flow gets worse, context switching grows, forecasts become fragile, and every delay becomes a debate about which lane consumed too much capacity.

A better model is one value stream with visible demand types, explicit decision policies, limited WIP, pull-based intake, clear expedite rules, enough slack for reality, and prioritisation based on value, risk, learning, cost of delay, cost of change and recovery needs.

Do not split the business into fictional internal lanes. Make the trade-offs visible and decide what protects or improves value next.

1.   What companies call work lanes

2.   The demand is real, the separation is imaginary

3.   There is only one business

4.   The wrong model: many lanes, one overloaded team

5.   The alternative in one picture

6.   Output, outcome and throughput

7.   The resource utilization trap

8.   The 50/50 person is not 50/50

9.   WIP, queues and Little’s Law

10.   The _Theory of Constraints_ problem

11.   Why this becomes anti-agile

12.   What fixed percentages hide

13.   What should happen to support, bugs and technical work

14.   Explicit policies instead of capacity slices

15.   A worked example: one value stream in practice

16.   What to measure instead

17.   The practical replacement

18.   Conclusions

19.   References

[![Image 3](https://substackcdn.com/image/fetch/$s_!06gC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1906b24d-8001-46fb-8a36-72879730f7e0_1024x559.png)](https://substackcdn.com/image/fetch/$s_!06gC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1906b24d-8001-46fb-8a36-72879730f7e0_1024x559.png)

The idea usually begins with a reasonable fear. The team is drowning in mixed demand. Product wants features. Support wants incidents handled. UX wants feedback applied. Engineering wants time to remove painful technical constraints. Operations wants reliability work. Security wants remediation. Stakeholders want dates.

Everyone has a valid concern, and nobody wants their concern to disappear under someone else’s urgency. So the organisation creates percentages.

Maybe the team gets 60 percent for product features, 20 percent for support, 10 percent for technical initiatives, and 10 percent for UX feedback. Or 50, 30, 20. Or one day per iteration for bugs. Or every Friday for technical debt.

The shape changes, but the logic is the same: divide capacity so every category has protected space.

This feels fair because every stakeholder receives a slice. It feels responsible because it says, “We know support matters.” It feels mature because it converts messy human tension into numbers. The spreadsheet becomes a peace treaty, but a peace treaty is not the same as flow.

The percentages do not do the hard work that the organisation quietly expects from them. They do not reduce demand, increase team capacity, remove dependencies, shrink work, make incidents arrive on schedule, make customer feedback wait politely for the UX lane, or make technical risk respect the calendar.

The model gives the organisation a feeling of control while the system underneath keeps behaving like a queue. That is the first trap: the categories are real, but the lines are fictional.

[![Image 4](https://substackcdn.com/image/fetch/$s_!o0Jo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02334d74-4b3a-4a40-ba62-cfec7af68325_1024x559.png)](https://substackcdn.com/image/fetch/$s_!o0Jo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02334d74-4b3a-4a40-ba62-cfec7af68325_1024x559.png)

Support is real. Bugs are real. UX feedback is real. Technical work is real. Reliability work is real. Security work is real. Product development is real. The fiction begins when we pretend these are separate lines of business.

A product team has one attention system, one cognitive budget, one delivery capability, one set of constraints and one flow of work. When the same people must serve five lanes, those lanes are not five parallel roads. They are five entrances into the same narrow bridge.

That distinction matters because otherwise the argument becomes too easy to misread. This article is not saying “ignore support”, “bugs do not matter”, “technical work is fake”, “UX feedback is a distraction”, “security and reliability can wait forever”, or “only feature work has value”.

The argument is sharper than that. These things should not be managed as independent missions competing for fixed percentages of the same team. They should be understood as different classes of demand entering one value stream.

A value stream is the path from a need, risk, problem or learning opportunity to delivered, restored or protected value. That value may appear as a new capability, a repaired production behaviour, reduced support pain, lower operational risk, faster learning, lower cost of change, or better user experience.

Naming demand is useful. Allocating the team into fixed percentages by demand type is the trap. Labels help us see the system. Percentages often make us serve the label instead of the user.

[![Image 5](https://substackcdn.com/image/fetch/$s_!zP7q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F169f8ea0-cb0f-4d5f-b966-2ac1129886cb_1024x559.png)](https://substackcdn.com/image/fetch/$s_!zP7q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F169f8ea0-cb0f-4d5f-b966-2ac1129886cb_1024x559.png)

This is where the usual conversation goes wrong. Many organisations still speak as if there were several businesses inside the company. “Business” wants features. “Product” wants outcomes. “Technology” wants technical health. “Support” wants issues solved. “UX” wants feedback addressed. “Security” wants risks removed.

This language feels harmless, but it quietly divides the company into tribes. Then every tribe asks for its lane.

But there is only one business.

Technology is not a supplier to the business. Technology is part of the business. Product is not a customer of engineering. Product and engineering are different responsibilities inside the same investment system. Support is not outside product. Support is product reality speaking back through pain. UX feedback is not a decorative stream. It is learning from the user’s contact with the product. Technical work is not a private engineering hobby. It protects future delivery capacity, risk, liquidity and cost of change.

A company does not succeed because one internal lane received its allocation. It succeeds when the product creates enough value to justify the money, time, attention and judgement invested in it.

So the central question is not, “How much percentage does each lane deserve?” The better question is, “What work best protects or improves user value now?”

That question is harder because it does not allow every stakeholder to hide behind a percentage. It forces the real trade-off into the open. Sometimes the answer is a feature that creates new value. Sometimes it is a production incident that must be resolved. Sometimes it is a confusing onboarding step that damages activation. Sometimes it is a refactor that lowers the cost of the next change. Sometimes it is a deletion that removes carrying cost. Sometimes it is a deployment improvement that reduces release risk. Sometimes it is a security fix that reduces exposure. Sometimes it is a discovery activity that prevents building the wrong thing.

The work type is not the point. The economic effect is the point.

[![Image 6](https://substackcdn.com/image/fetch/$s_!gK6g!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faab5576e-0547-4f5b-832d-04fe9dbdfce3_1024x559.png)](https://substackcdn.com/image/fetch/$s_!gK6g!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faab5576e-0547-4f5b-832d-04fe9dbdfce3_1024x559.png)

The fixed-lane model often looks like this:

[![Image 7](https://substackcdn.com/image/fetch/$s_!GzHh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7888a2ef-8e26-4582-ab16-b0ccc5340c23_2955x764.png)](https://substackcdn.com/image/fetch/$s_!GzHh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7888a2ef-8e26-4582-ab16-b0ccc5340c23_2955x764.png)

This model has a hidden contradiction. It says the team has several protected lines of work, but it does not give the team several independent capacities. The same people still need to think, coordinate, design, test, review, deploy, learn, monitor and support.

If the team had four independent kitchens, perhaps four percentages would make sense. But the team has one kitchen.

Every new lane creates a promise. Every promise creates pressure to start work. Every started item creates WIP. Every WIP item carries context, coordination and unfinished decisions. The team becomes busier, but value moves more slowly.

The board looks active, but the delivery system becomes heavy.

The alternative is not chaos. It is one visible value stream with different demand types, explicit policies, limited WIP and pull-based intake.

This model does not deny that work is different. It denies that different work types should become separate internal businesses.

The important move is not the diagram itself. The important move is changing the management question.

The old model asks, “Which lane owns capacity?” The better model asks, “Which demand should enter the constrained delivery system next, and why?”

That change turns the conversation from allocation politics into economic judgement.

[![Image 8](https://substackcdn.com/image/fetch/$s_!ZYMD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac2bedb5-0686-4123-8a6b-f3ff617d1547_1024x559.png)](https://substackcdn.com/image/fetch/$s_!ZYMD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac2bedb5-0686-4123-8a6b-f3ff617d1547_1024x559.png)

Work lanes usually optimise output accounting. They ask whether each category received activity, whether each internal group was represented in the iteration, and whether the promised capacity distribution was respected.

Those questions may sound responsible, but they are not enough. They mostly measure whether a category was fed.

A product organisation needs a better distinction:

*   **Output** is what the team ships

*   **Outcome** is what changes because of the work

*   **Throughput** is the rate at which the system finishes work over time  
Fixed lanes blur these ideas. They turn output per category into a proxy for value. If the team delivered five support tickets, two technical tasks and three feature stories, the spreadsheet looks balanced. But that does not tell us whether users are better served, whether support pain went down, whether the next change became cheaper, whether a risk was actually reduced, or whether the delivery system is healthier.

A lane can receive its percentage and still create little value. A team can be active in every category and still produce poor outcomes. A team can increase output and still reduce throughput by fragmenting its attention.

This is why lane accounting is seductive. It gives the organisation visible evidence of activity. But activity is not value. Motion is not progress. A full board is not a healthy system.

The business does not benefit because a lane was busy. It benefits when outcomes improve and the delivery system remains healthy enough to keep learning. Without output, nothing reaches users. Without throughput, delivery becomes sluggish and learning slows down. Without outcome, software may be shipped, but value remains unproven.

Work lanes become dangerous when they reward output by category, obscure throughput across the system and barely examine outcome.

[![Image 9](https://substackcdn.com/image/fetch/$s_!TA81!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c62e9fe-5774-4499-98a9-362ea7b54e0b_1024x559.png)](https://substackcdn.com/image/fetch/$s_!TA81!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c62e9fe-5774-4499-98a9-362ea7b54e0b_1024x559.png)

Fixed percentages are also a form of the resource utilization trap. They make the organisation feel responsible because every slice of capacity has a job. Nobody is idle. Nothing appears wasted. Every lane has a plan. Every person is attached to something. The calendar looks full.

But a fully allocated team is not necessarily a productive team. A fully occupied road is not an efficient road. It is a traffic jam.

The problem is not utilization itself. Capacity matters. Waste matters. People should not be left unsupported, bored or disconnected from meaningful work. The problem begins when utilization becomes the primary target and flow becomes secondary.

When the system is optimised to keep everyone busy, a predictable chain appears:

1.   Work gets pushed in faster than it can move out

2.   More work starts

3.   Less work finishes

4.   Coordination grows

5.   Waiting grows

6.   Re-planning grows

7.   Status reporting grows

8.   Context switching grows

9.   The team becomes a machine for converting effort into delay  
That loop looks like this:

[![Image 10](https://substackcdn.com/image/fetch/$s_!uY28!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc3a760e-e3bb-4714-a82b-9e49a52def6f_717x1948.png)](https://substackcdn.com/image/fetch/$s_!uY28!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc3a760e-e3bb-4714-a82b-9e49a52def6f_717x1948.png)

This is why some slack is not waste. In knowledge work, slack is often the space that allows flow, learning, helping, incident response, refactoring, mentoring, recovery and better decisions.

The absence of slack does not prove discipline. It may prove the system has no room to breathe.

The human version of the same mistake is the person split between two teams. On paper, the person is 50 percent in Team A and 50 percent in Team B. It looks efficient. Both teams get help. The person is shared. Capacity is maximised.

In reality, Team A keeps moving while the person is with Team B. Decisions are made. Code changes. Product context evolves. Small conversations happen. Assumptions accumulate. When the person returns to Team A, they are not simply “back”. They must rebuild the mental model they missed.

Then the same thing happens in Team B.

[![Image 11](https://substackcdn.com/image/fetch/$s_!-jwh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83247624-55cc-40f5-88ce-319a2556024b_1818x1134.png)](https://substackcdn.com/image/fetch/$s_!-jwh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83247624-55cc-40f5-88ce-319a2556024b_1818x1134.png)

The person is not doing half of each team’s work. They are also paying the re-entry cost for both teams. Some of that cost is visible in meetings. Much of it is invisible: rereading discussions, asking questions that were answered yesterday, hesitating before changing code, holding two product narratives in memory, feeling guilty in both places, and missing the small context that never reaches formal documentation.

The 150 percent figure is a useful metaphor, not a universal measurement. The exact cost depends on the work, the teams, the domain and the interruption pattern. But the direction is real: splitting attention does not split cleanly. Cognitive work has setup cost, re-entry cost and coordination cost.

The same thing happens when one team is split across several work lanes. The team is supposedly 60 percent product, 20 percent support, 10 percent technical work and 10 percent UX. But each lane carries its own context, stakeholders, urgency, vocabulary, artefacts and unfinished stories.

A spreadsheet can divide capacity. It cannot divide attention without loss.

There is a simple reason these systems become painful: queues grow when demand exceeds effective capacity.

In software, queues are often invisible. They can appear as a half-finished feature, a bug waiting for someone to reload context, a support issue waiting for product clarification, a technical decision waiting for architecture review, a pull request waiting for review, a release waiting for approval, a stakeholder waiting for an answer, a test suite waiting for someone to understand why it is flaky, or a dependency waiting for another team.

When a team has too much WIP, every item spends more time waiting. People may still be busy, but value is not moving.

Little’s Law gives us a simple relationship:

**Average lead time = Average WIP / Average throughput**

This is not a magic formula for prediction. It is a useful way to think about flow. If WIP grows and throughput does not grow with it, lead time gets worse.

That is exactly what fixed work lanes often do. Product wants visible progress. Support wants visible progress. UX wants visible progress. Technical initiatives want visible progress. Security wants visible progress. Reliability wants visible progress. So everything starts.

Then everything waits.

The organisation sees slow delivery and asks for more planning. More planning consumes more attention. More attention spent on planning reduces the attention available for finishing. The system becomes slower and more managed at the same time.

This is the deeper failure: the team is not short of categories. It is short of flow.

[![Image 12](https://substackcdn.com/image/fetch/$s_!xMiT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f22109e-b385-4304-a3bd-7110ccd1f708_1024x559.png)](https://substackcdn.com/image/fetch/$s_!xMiT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f22109e-b385-4304-a3bd-7110ccd1f708_1024x559.png)

_Theory of Constraints_ (TOC) gives another way to see the same issue. A system’s throughput is limited by its constraint. If the constraint is overloaded, optimising everything else does not improve the system. It can make the system worse by producing more work than the constraint can handle.

Fixed lanes often create local optimisation. Product optimises its lane. Support optimises its lane. UX optimises its lane. Technology optimises its lane. Security optimises its lane. Every lane can make a reasonable local argument, but the whole system slows down because the same team is the constraint.

The problem is not that any stakeholder is wrong. The problem is that the system is being managed as if every demand type had its own independent capacity.

[![Image 13](https://substackcdn.com/image/fetch/$s_!3iYF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71325d8c-7e89-4fcd-b9a9-9cb304e4bdb9_2290x992.png)](https://substackcdn.com/image/fetch/$s_!3iYF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71325d8c-7e89-4fcd-b9a9-9cb304e4bdb9_2290x992.png)

In TOC terms, the sensible response is to subordinate the system to the constraint. If the team’s attention is the constraint, do not feed it five parallel lanes and call that balance. Protect the constraint. Reduce unnecessary WIP. Make priorities explicit. Remove interruptions where possible. Improve the constraint if needed. Do not allow every non-constraint stakeholder to push work into the system just because their lane has a percentage.

That is not discipline. That is congestion with a budget.

[![Image 14](https://substackcdn.com/image/fetch/$s_!VkfC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9399882f-3f99-4ba3-b51c-27056fc45885_1024x559.png)](https://substackcdn.com/image/fetch/$s_!VkfC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9399882f-3f99-4ba3-b51c-27056fc45885_1024x559.png)

A fixed allocation model may look Agile from a distance. It may live inside iterations. It may use a board. It may have refinement, planning, stand-ups and retrospectives. It may call the work “stories”. It may even happen inside a team that sincerely believes it is working in an adaptive way.

But Agile is not the presence of ceremonies. Agile is a way of organising work around value, feedback, collaboration, technical excellence, simplicity and adaptation.

Fixed work-lane percentages become anti-agile when they replace adaptation with allocation. The problem is not that a team classifies demand. The problem is that the team follows a pre-negotiated capacity split instead of responding to the next most valuable, risky or time-sensitive piece of work.

That conflict appears in several ways:

*   It conflicts with customer value because it asks whether a lane received capacity before asking whether the next piece of work is the most valuable thing to do

*   It conflicts with responding to change because it freezes a capacity split before reality has finished speaking

*   It conflicts with sustainable pace because every surprise must either break the allocation, break the plan or break the people

*   It conflicts with technical excellence when technical work is treated as a side allowance rather than part of the team’s ability to respond

*   It conflicts with simplicity because it institutionalises more categories, more negotiation, more partial commitments and more coordination

*   It conflicts with self-organisation because the team is not truly deciding how best to achieve the goal. It is operating inside a capacity budget carved by internal categories  
If an iteration contains four unrelated mini-roadmaps because each lane needs its percentage, the team may be busy, but it is not focused. An iteration is not a drawer for unrelated obligations. It should have a direction, and a product team should have a mission.

That mission is not “satisfy every internal bucket”. It is “protect and improve the product’s ability to create value”.

[![Image 15](https://substackcdn.com/image/fetch/$s_!ZY34!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa31be63c-13bd-4f38-9272-deb97b02a509_1024x559.png)](https://substackcdn.com/image/fetch/$s_!ZY34!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa31be63c-13bd-4f38-9272-deb97b02a509_1024x559.png)

Fixed percentages feel transparent, but they often hide the most important information.

They hide **overload**. If every lane has capacity assigned, the system can look planned even when total demand is far beyond what the team can absorb.

They hide **opportunity cost**. A technical initiative started too early can block a support problem that is damaging trust. A feature started because the product lane needed movement can block a reliability fix that would reduce incidents. A UX item started because the UX lane has allocation can block a smaller product experiment that would teach more.

They hide **cost of delay**. Some work loses value when delayed. Some risks become more expensive with time. Some support issues compound through repeated contacts. Some technical constraints grow more expensive because every new change pays the tax.

They hide **cost of carry**. Every unfinished item must be remembered, discussed, updated, re-estimated, re-explained and eventually reloaded into someone’s head.

They hide **basal cost**. Every feature that exists must be supported, understood, monitored, adapted, tested and carried through future change. More software is not only more capability. It is also more surface area.

They hide **the real constraint**. Instead of asking, “What is limiting our ability to deliver value?” the organisation asks, “Did each lane get its share?”

That is a weaker question, and weaker questions produce weaker decisions.

[![Image 16](https://substackcdn.com/image/fetch/$s_!H-DO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4644617f-a219-4132-9b49-0f4421c673de_1024x559.png)](https://substackcdn.com/image/fetch/$s_!H-DO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4644617f-a219-4132-9b49-0f4421c673de_1024x559.png)

One value stream does not mean feature-only work. That would be a serious mistake.

Support matters because users are already paying the cost of a product failure, misunderstanding or operational gap. Bugs matter because they damage trust and produce rework. UX feedback matters because it improves the product’s contact with reality. Technical work matters because software has a carrying cost. Reliability matters because value that cannot survive production is not really delivered. Security matters because a product that creates avoidable exposure is not protecting the investment.

The correct move is not to remove these work types. The correct move is to stop treating them as separate businesses.

Here is a better classification:

Demand type What it really means Economic purpose Product feature A new or changed capability Create or extend user value Support A user or customer needs help Restore blocked or degraded value Bug Reality violates expected behaviour Remove negative value and protect trust UX feedback Users reveal friction or confusion Improve learning and reduce product friction Technical work The system is too costly, risky or slow to change Protect delivery capacity and reduce cost of change Reliability Production value is fragile Protect continuity of value Security The product has exposure to loss Reduce risk and protect the investment Documentation and knowledge work The system is hard to understand or operate Reduce cognitive load and coordination cost

This table does not create lanes. It creates language.

The difference is important. A lane says, “This category owns 20 percent.” A language says, “This kind of demand has this economic effect. Now let us decide whether it matters most.”

Production support deserves special care here. A product in production is not in a temporary exception state. It is alive. It will need support, learning, change, refinement and sometimes retirement. A team should measure the impact of production support on its development capacity, rotate exposure wisely when it helps learning, and turn repeated support themes into product improvement. Hiding production work in a percentage bucket misses the deeper lesson: support is one of the places where the product tells the truth.

[![Image 17](https://substackcdn.com/image/fetch/$s_!_r3C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc013c2f0-b916-4670-9c13-d0f3c969ee8f_1024x559.png)](https://substackcdn.com/image/fetch/$s_!_r3C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc013c2f0-b916-4670-9c13-d0f3c969ee8f_1024x559.png)

One value stream needs decision policies. Without them, “one stream” can become a polite name for whoever shouts loudest.

Explicit policies answer the question that fixed percentages try to avoid: what should happen when demand collides?

A practical starting point could look like this:

Policy area Example policy Expedite Only user-blocking incidents, revenue-impacting issues, severe production risk or urgent compliance exposure can bypass normal order Support Repeated support themes must create product learning, not only ticket closure Bugs Prioritise by severity, reach, frequency, trust damage and recovery cost UX feedback Do not convert every comment into work. Look for repeated friction, high-impact journeys and evidence of outcome risk Technical work Prioritise when it reduces cost of change for imminent work, removes a recurring bottleneck or reduces meaningful operational risk Reliability Prioritise when failure impact, recovery time or operational toil threatens value continuity Security Integrate security into daily work where possible. Avoid treating it only as a downstream gate WIP Do not start new work while active work exceeds the agreed limit Slack Preserve capacity for incidents, helping, improvement and unexpected learning Abandonment Stop work when evidence shows the expected economic effect no longer justifies the cost

These policies should not be carved in stone. They should be sparse, visible, understandable and changeable by the people who use them. Their purpose is not to remove judgement. Their purpose is to make judgement explicit enough to improve.

A WIP limit works in the same way. It is not magic by itself. It matters when it exposes overload, forces conversations, encourages collaboration and helps the team stop starting so it can start finishing.

[![Image 18](https://substackcdn.com/image/fetch/$s_!rBZV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F218516b8-f620-4269-8638-405550b95358_1024x559.png)](https://substackcdn.com/image/fetch/$s_!rBZV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F218516b8-f620-4269-8638-405550b95358_1024x559.png)

Imagine a team entering an iteration with four candidates competing for attention.

The first candidate is an activation feature. Product believes it may help trial users reach first value faster. The second is a repeated support issue: customers are opening tickets because invoice exports sometimes fail when a rare tax configuration is present. The third is UX feedback showing confusion in onboarding, but the evidence is still anecdotal. The fourth is a refactor in the billing module that engineering says will reduce risk before changing pricing rules next month.

Under the lane model, each item fights for its percentage. Product argues that the feature belongs to the product lane. Support argues that the invoice issue belongs to the support lane. UX argues that feedback must be represented. Engineering argues that the technical initiative lane exists precisely for the refactor.

The discussion becomes a negotiation between buckets.

Under the value-stream model, the team asks a different question: which work best protects or improves value now?

Candidate Demand type Economic effect Decision Invoice export issue Support and bug Restores trust, reduces repeated support load, protects a revenue-adjacent workflow Do first Billing refactor Technical work Reduces cost and risk of the next pricing change Pair with the invoice fix where the touched area overlaps Activation feature Product feature Plausible value, but not urgent enough to start as a large batch Slice smaller and prepare the smallest valuable experiment Onboarding UX feedback Learning Signals possible friction, but evidence is still weak Convert into discovery work before implementation

Notice what happened. The team did not ignore Product. It did not ignore Support. It did not ignore UX. It did not ignore Technology. It refused to treat them as separate businesses.

The invoice issue goes first because users are already experiencing harm, support demand is repeating, and the affected workflow is important. The billing refactor is not accepted as a vague technical improvement. It is connected to imminent work and to the area already being touched, which improves its economic case. The activation feature is not rejected, but it is sliced because the team does not want to create a large batch while the system is already carrying urgent demand. The UX feedback is respected as learning, but not blindly converted into implementation.

This is what one value stream makes possible: not fewer conversations, but better conversations.

A useful decision map could look like this:

[![Image 19](https://substackcdn.com/image/fetch/$s_!ucIr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2046f438-4433-4a3d-94a5-adf78febf0d0_1000x1000.png)](https://substackcdn.com/image/fetch/$s_!ucIr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2046f438-4433-4a3d-94a5-adf78febf0d0_1000x1000.png)

This diagram is intentionally not a Venn diagram. A Venn diagram can be useful to show overlap, but here it risks reinforcing the wrong mental model: Product, Support, UX and Technology as separate circles that occasionally intersect. The article’s thesis is stronger with flow and decision diagrams because the point is not overlap. The point is movement through one constrained system.

[![Image 20](https://substackcdn.com/image/fetch/$s_!YZ0i!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4758613-d1ca-47f0-8e46-e21d5a6180a6_1024x559.png)](https://substackcdn.com/image/fetch/$s_!YZ0i!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4758613-d1ca-47f0-8e46-e21d5a6180a6_1024x559.png)

If fixed work-lane percentages are weak measures, what should we look at?

Measure flow, outcomes, quality, risk and learning. Useful signals include lead time from request to value delivered, cycle time from start to finish, throughput of completed valuable items, WIP by state and demand type, age of active work, percentage of unplanned work over time, escaped defects, repeated support themes, operational toil, user-impacting incidents, time from customer feedback to product learning, cost of delay for major waiting items, amount of work abandoned after learning, team health, focus and cognitive load.

For software delivery specifically, the current DORA metrics are useful because they place throughput and instability in tension. The five metrics are:

*   Change lead time

*   Deployment frequency

*   Failed deployment recovery time

*   Change fail rate

*   Deployment rework rate  
These metrics matter because they discourage the false choice between speed and stability. A team that moves fast but creates instability is not protecting value. A team that is stable only because it rarely changes is not necessarily healthy either.

The same warning applies to any measurement system: do not isolate metrics into silos. If Product owns outcome, Engineering owns throughput, Operations owns recovery and Support owns tickets, the organisation has recreated work lanes through measurement. Shared ownership matters because the product is one system.

These measures are not perfect. They can be gamed if used badly. But they point closer to the real system than “percentage of capacity reserved per lane”.

The best use of measurement is not control. It is learning. A team does not need a dashboard to be watched harder. It needs visibility to make better decisions.

[![Image 21](https://substackcdn.com/image/fetch/$s_!Cpqx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1d0907f-01fb-423f-a35d-09ec2584c338_1024x559.png)](https://substackcdn.com/image/fetch/$s_!Cpqx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1d0907f-01fb-423f-a35d-09ec2584c338_1024x559.png)

A team that wants to move away from work lanes can start with a small operating model.

First, collect all demand in one visible place. Do not hide support, bugs, UX feedback or technical work in separate tools where the team cannot see the whole system.

Second, classify demand by type, but do not allocate fixed percentages. The label exists to understand the nature of the demand, not to create a mini-budget.

Third, define explicit policies. Decide what qualifies as expedite work, how support themes become product learning, when technical work is justified, and how security and reliability work enter the stream.

Fourth, limit WIP. Make the limit uncomfortable enough to force conversations. A WIP limit that never changes behaviour is decoration.

Fifth, use pull. Start work when the system has capacity, not because a lane needs activity.

Sixth, preserve slack. If every person and every day are already allocated, the team has no room for incidents, helping, improvement, learning or recovery.

Seventh, review outcomes and flow together. Ask both: did the work help, and did the system remain healthy enough to keep learning?

Eighth, improve the system. If support keeps eating capacity, do not merely reserve more support capacity. Ask why support demand is so high. If technical work keeps interrupting features, ask which technical constraints are causing repeated delay. If UX feedback keeps arriving late, ask why discovery and delivery are disconnected.

The point is not to make the board prettier. The point is to make reality harder to ignore.

[![Image 22](https://substackcdn.com/image/fetch/$s_!4BvL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef196166-4e1f-449d-8775-12464a0596fd_1672x941.png)](https://substackcdn.com/image/fetch/$s_!4BvL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef196166-4e1f-449d-8775-12464a0596fd_1672x941.png)

“Work lanes” are usually born from a good intention: protect important work from being forgotten. But when they become fixed capacity percentages, they often create the opposite effect. They hide overload, increase WIP, intensify context switching, weaken forecasts and turn product decisions into allocation disputes.

A team does not need four fictional missions. It needs one clear mission: protect and improve the user’s ability to get value from the product. That mission includes features, support, bugs, UX feedback, technical work, reliability, security, refactoring, discovery, documentation and deletion.

The demand types are real. The separate businesses are imaginary.

The question is not which lane deserves capacity. The question is which work best serves the product’s economic reality now.

A good product team should not be split into percentages like a budget spreadsheet. It should be treated as a learning and delivery system with finite attention, visible demand, limited WIP, explicit policies, enough slack to absorb reality and a shared language for economic trade-offs.

There is only one business, one product investment and one value stream. Everything else is a way of understanding what kind of demand is asking to enter.

The work was never really divided. Only the language was.

*   Agile Alliance. _Manifesto for Agile Software Development_. [https://agilemanifesto.org/](https://agilemanifesto.org/)

*   Agile Alliance. _Principles behind the Agile Manifesto_. [https://agilemanifesto.org/principles.html](https://agilemanifesto.org/principles.html)

*   Artola, Luis. _Software Economics_. [https://leanpub.com/software-economics](https://leanpub.com/software-economics)

*   Beck, Kent. _Extreme Programming Explained: Embrace Change_. [https://www.pearson.com/en-us/subject-catalog/p/extreme-programming-explained-embrace-change/P200000003514](https://www.pearson.com/en-us/subject-catalog/p/extreme-programming-explained-embrace-change/P200000003514)

*   Ferro Aldama, Eduardo. _Menos software, más impacto_. [https://menos-software.eferro.net](https://menos-software.eferro.net/)

*   Forsgren, Nicole; Humble, Jez; Kim, Gene. _Accelerate: The Science of Lean Software and DevOps_. [https://itrevolution.com/product/accelerate/](https://itrevolution.com/product/accelerate/)

*   Goldratt, Eliyahu M. _The Goal: A Process of Ongoing Improvement_. [https://northriverpress.com/the-goal/](https://northriverpress.com/the-goal/)

*   Google Cloud DORA. _DORA’s Software Delivery Performance Metrics_. [https://dora.dev/guides/dora-metrics/](https://dora.dev/guides/dora-metrics/)

*   Kanban University. _The Official Guide to The Kanban Method_. [https://kanban.university/kanban-guide/](https://kanban.university/kanban-guide/)

*   Little, John D. C. _A Proof for the Queuing Formula: L = λW_. [https://pubsonline.informs.org/doi/10.1287/opre.9.3.383](https://pubsonline.informs.org/doi/10.1287/opre.9.3.383)

*   Nygard, Michael T. _Release It! Second Edition_. [https://pragprog.com/titles/mnee2/release-it-second-edition/](https://pragprog.com/titles/mnee2/release-it-second-edition/)

*   Reinertsen, Donald G. _The Principles of Product Development Flow_. [https://lpd2.com/wp-content/uploads/2013/06/ReinertsenFLOWChap1.pdf](https://lpd2.com/wp-content/uploads/2013/06/ReinertsenFLOWChap1.pdf)

*   Schwaber, Ken; Sutherland, Jeff. _The Scrum Guide_. [https://scrumguides.org/scrum-guide.html](https://scrumguides.org/scrum-guide.html)

*   Shore, James. _The Art of Agile Development, 2nd Edition_. [https://www.oreilly.com/library/view/the-art-of/9781492080688/](https://www.oreilly.com/library/view/the-art-of/9781492080688/)

*   Theory of Constraints Institute. _Five Focusing Steps, a Process of On-Going Improvement_. [https://www.tocinstitute.org/five-focusing-steps.html](https://www.tocinstitute.org/five-focusing-steps.html)

*   Valverde Ramos, Emmanuel. _Output, Outcome, and Throughput: What Product Teams are really measuring when they say they deliver value_. [https://emmanuelvalverderamos.substack.com/p/output-outcome-and-throughput-what](https://emmanuelvalverderamos.substack.com/p/output-outcome-and-throughput-what)

*   Valverde Ramos, Emmanuel. _The Resource Utilization Trap: Why Keeping Everyone Busy Can Destroy Real Productivity_. [https://emmanuelvalverderamos.substack.com/p/the-resource-utilization-trap-why](https://emmanuelvalverderamos.substack.com/p/the-resource-utilization-trap-why)
