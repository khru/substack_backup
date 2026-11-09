Title: Stop making strategy without a map

URL Source: http://emmanuelvalverderamos.substack.com/p/stop-making-strategy-without-a-map

Final URL: https://emmanuelvalverderamos.substack.com/p/stop-making-strategy-without-a-map

Published Time: 2026-07-14T06:00:15+00:00

Markdown Content:
Imagine asking for directions in a city you do not know and being told to move fast, stay aligned, and be innovative. None of that advice is useless. None of it tells you where to turn.

Strategy conversations often fail in the same way. The language sounds confident, but the landscape is missing. A team may have a roadmap, quarterly objectives, product bets, architecture diagrams, and budget commitments, yet still struggle to explain why one move makes sense now and another does not.

This is the problem Wardley Mapping tries to solve. It gives teams a way to make strategic context visible. Instead of debating from opinions, status, vendor pressure, or fashionable practices, the team can discuss users, needs, dependencies, maturity, constraints, and movement.

A Wardley map does not make the decision for you. It does something more practical: it improves the conversation before the decision is made.

*   Wardley Mapping is a way to visualize strategic context by starting with users and their needs.

*   A map shows the value chain required to satisfy those needs, from visible user-facing capabilities to hidden enabling components.

*   Each component is placed on an evolution axis: genesis, custom built, product, and commodity or utility.

*   The same management approach should not be used for every component. Novel work needs learning, custom work needs close collaboration, product-like work needs evaluation, and commodity work needs standardization.

*   Wardley Mapping helps with product strategy, platform strategy, build versus buy, legacy modernization, cloud migration, outsourcing, team boundaries, and prioritization.

*   The goal is not to create a perfect drawing. The goal is to expose assumptions, find mismatches, and make better strategic moves.

*   A useful first map can be created around one real decision, one user, one need, and one value chain.

*   The article includes a complete worked example for an e-commerce self-service returns portal.

1.   Why strategy needs a map

2.   What Wardley Mapping is

3.   The two whys: purpose and movement

4.   How a Wardley map works

5.   The four stages of evolution

6.   How to create your first map

7.   Complete worked example: self-service returns portal

8.   How to read map patterns

9.   Real uses at work

10.   Common mistakes

11.   How to run a 90-minute mapping session

12.   Conclusions

13.   References

[![Image 1](https://substackcdn.com/image/fetch/$s_!-eI-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab5d3d40-bd93-4890-902a-d1f12d923ba1_1024x558.png)](https://substackcdn.com/image/fetch/$s_!-eI-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab5d3d40-bd93-4890-902a-d1f12d923ba1_1024x558.png)

Most teams do not fail because they lack ambition. They fail because they lack position. They know what they want to achieve, but they cannot clearly explain where they are, what the landscape looks like, which constraints matter, and why this move is better than another.

This is why strategy documents can be dangerous. They often contain familiar words that make people feel safe: innovation, efficiency, alignment, customer-centricity, transformation, platform, ecosystem, Artificial Intelligence, cloud, modernization. These words may be useful, but they are not strategy by themselves. They do not show the user need, the dependencies, the maturity of each capability, the likely direction of change, or the cost of choosing one move over another.

A team can say, “We need a platform,” without showing which repeated needs the platform will serve. A company can say, “We need to modernize,” without identifying which part of the legacy system blocks valuable change. A product organization can say, “We need this feature,” without proving whether it addresses a real user need or merely satisfies a stakeholder request.

Wardley Mapping introduces discipline into this conversation. It asks the team to stop treating strategy as a polished story and start treating it as situated judgment. Before deciding what to do, the team must describe the landscape in which the decision lives.

That shift matters because software and product work are economic work. Every product decision, architecture decision, vendor decision, platform decision, and modernization decision spends money, time, attention, and organizational capacity. When the landscape is unclear, the investment is exposed to avoidable waste and risk.

[![Image 2](https://substackcdn.com/image/fetch/$s_!wf9H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2afd2a5-05aa-454a-ad41-ce3ee48aa111_1024x558.png)](https://substackcdn.com/image/fetch/$s_!wf9H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2afd2a5-05aa-454a-ad41-ce3ee48aa111_1024x558.png)

Wardley Mapping is a practice for visualizing a strategic landscape. It begins with users and their needs, then maps the chain of components required to satisfy those needs. Each component is positioned according to two dimensions: how visible it is to the user, and how evolved it is.

The vertical dimension is the value chain. Components near the top are more visible to the user. Components lower down are less visible, although they may still be essential. For example, a customer using an e-commerce returns portal cares about whether they can return an item easily, track the process, and receive a refund. They do not usually care whether the company hand-built its address validation service, hosting layer, or email delivery mechanism.

The horizontal dimension is evolution. Components move from uncertain and novel to more common, standardized, and expected. A new business capability may begin as exploration. Over time it may become custom built, then available as a product, and eventually treated as a commodity or utility.

This second dimension is what makes Wardley Mapping more than a dependency diagram. A dependency diagram may show that a returns portal needs payment integration, carrier integration, order history, and customer notifications. A Wardley map also asks whether those components are novel, custom, product-like, or commodity-like.

That question changes the strategy. If a component is commodity-like, handcrafting it may be wasteful. If a component is novel, treating it as predictable delivery may be naive. If a component is custom and strategically important, outsourcing it too early may move learning outside the organization. If a component is mature but critical, the right concern may be resilience, ownership, and operational quality rather than differentiation.

Wardley Mapping is not about making prettier diagrams. It is about making better decisions under uncertainty.

A useful distinction in Wardley Mapping is the difference between the why of purpose and the why of movement. The why of purpose explains what we are trying to achieve. The why of movement explains why this move makes sense from our current position.

Most organizations are more comfortable with purpose than movement. They can say they want better customer experience, faster delivery, lower cost, higher reliability, stronger product differentiation, or improved operational efficiency. Those goals may be valid, but they do not explain which move should happen next.

Consider a company that says, “We want to improve customer experience by making returns easier.” That is purpose. It matters, but it is not enough. The movement question is more specific: should the company build a custom returns portal, buy a returns management product, extend its commerce platform, improve customer support scripts, change return policy rules, or fix warehouse processing first?

Each of those moves may support the purpose. They are not equally good. Their value depends on the landscape: user needs, current capabilities, existing systems, operational constraints, component maturity, cost, risk, and timing.

This is where Wardley Mapping becomes useful. It helps the team connect purpose to movement. It does not stop at “we want better returns.” It asks what the customer needs, what capabilities satisfy that need, what those capabilities depend on, how evolved each dependency is, and which move improves the situation.

The practical consequence is simple. A strategy should not only explain what the organization wants. It should explain why this move is appropriate in this context.

A Wardley map has a simple structure. It starts with a user. The user has needs. Those needs require capabilities. Those capabilities depend on other components. The map places those components vertically by visibility and horizontally by evolution.

The first anchor is the user. This prevents the conversation from starting with internal preferences. A team may want to sell a product, reduce cost, reuse a platform, adopt a vendor, or remove a legacy system. Those may be legitimate business concerns, but the map begins with the person or group receiving value.

The second element is the user need. This should be expressed as an outcome, not as a solution. “A returns portal” is not a user need. “The customer needs to know whether an item can be returned, start the process easily, and understand when the refund will arrive” is closer to a need.

The third element is the value chain. Once the need is clear, the team identifies what must exist to satisfy it. In an e-commerce returns flow, visible capabilities might include eligibility checking, return request creation, label generation, tracking, refund status, and customer notifications. Underneath those visible capabilities sit less visible components such as order history, product catalog, return policy rules, carrier integration, warehouse status, payment refund integration, fraud checks, authentication, address validation, monitoring, and hosting.

The fourth element is evolution. Each component is placed from left to right according to how mature and industrialized it is. The team asks whether the component is novel and uncertain, custom to the organization, available as a product, or commodity-like.

The map is useful because it combines these ideas in one shared view. It shows what the user values, what the organization must provide, what sits underneath the visible experience, and which components should be treated differently because they are at different stages of evolution.

A first map will not be perfect. That is acceptable. The value is not in producing a final artifact. The value is in making assumptions visible enough for the team to challenge them.

[![Image 3](https://substackcdn.com/image/fetch/$s_!uK5R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09820bac-aee0-4e1e-88b7-3809f7b480ce_1024x558.png)](https://substackcdn.com/image/fetch/$s_!uK5R!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09820bac-aee0-4e1e-88b7-3809f7b480ce_1024x558.png)

The evolution axis is central to Wardley Mapping because it changes how work should be treated. The same delivery model, funding model, governance model, and team structure should not be applied to every component.

Genesis is the uncertain beginning. The component is novel, rare, unstable, and poorly understood. The team does not yet know exactly what shape it should take, whether users will value it, or which constraints will matter most.

Work in genesis needs learning. It should be approached through discovery, experiments, prototypes, fast feedback, and careful reduction of uncertainty. A fixed delivery promise can be dangerous here because the team may not yet understand what it is building.

In a returns example, a new predictive model for detecting return abuse in a highly specific market might be genesis if the organization has never tested it and does not know whether the signals are useful.

Custom built means the component is understood enough to build, but it remains specific to the context. It may change often, depend on local knowledge, or reflect business-specific rules.

Work in this stage needs close collaboration. It often requires product, engineering, operations, legal, support, and domain experts to work together because the component encodes how the business actually works.

In a returns portal, return policy rules may be custom built. They may depend on country, product category, customer segment, promotional conditions, delivery date, item condition, fraud risk, and commercial strategy.

A product-like component is more mature. Vendors exist. Patterns are known. Comparison is possible. The organization can evaluate options instead of inventing everything from scratch.

Work in this stage needs selection, integration, lifecycle management, and vendor understanding. The economic risk is excessive customization. A product can reduce cost and time, but only if the organization avoids bending it into a poor copy of its old process.

In a returns portal, carrier integration or customer notification tooling may be product-like. Many services already exist, and the team should be careful before building these capabilities from scratch.

Commodity or utility components are standardized, widespread, expected, and often invisible to the user. The user does not reward the company for handcrafting them, but failure may still be painful.

Work in this stage needs standardization, automation, operational discipline, cost awareness, and resilience. The goal is usually not differentiation. The goal is reliable, low-friction consumption.

In a returns portal, authentication, hosting, address validation, and basic logging are likely to be commodity-like or close to it. They may still require security and operational care, but they are rarely the strategic reason customers choose the company.

The important lesson is that evolution changes the economics of work. A component can begin as a source of differentiation and later become an expected utility. When that happens, the organization must change how it manages the component. Continuing to treat commodity work as bespoke craft consumes attention that could be used where learning or differentiation matter more.

[![Image 4](https://substackcdn.com/image/fetch/$s_!LdW3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fede011b4-7567-4b52-a30e-e3d26efe06eb_1024x558.png)](https://substackcdn.com/image/fetch/$s_!LdW3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fede011b4-7567-4b52-a30e-e3d26efe06eb_1024x558.png)

The easiest way to start is to map one real decision. Do not map the entire company. Do not start with an abstract transformation theme. Pick one product, one service, one user journey, one platform question, or one painful decision that people are already debating.

A good first question might be: should we build or buy this capability? Which part of this legacy system should we modernize first? Should we create a platform team for this area? Why is delivery slow in this workflow? Which parts of this service are differentiating and which are merely necessary?

Once the question is selected, identify the primary user. Be specific. “Customer” may be too broad. “Customer trying to return an item without contacting support” is better. “Developer deploying a service safely without waiting for another team” is better. “Finance analyst reconciling refunds at month end” is better.

After the user is clear, write the user need as an outcome. Avoid naming the solution too early. The user does not need “a dashboard” in the abstract. They may need to detect operational issues before customers complain. The user does not need “a portal” in the abstract. They may need to complete a return without uncertainty, delay, or avoidable support contact.

Next, build the value chain. Start with the visible capabilities that satisfy the need, then ask what each capability depends on. Continue downward until further decomposition stops being useful for the decision at hand. The goal is not to describe every technical detail. The goal is to reveal the components that influence the strategic choice.

Then place each component on the evolution axis. Ask whether it is novel, custom, product-like, or commodity-like. Be careful not to confuse how you currently treat the component with how evolved it is in the market. A company may handcraft something that is already available as a mature product. That does not make the component strategically custom. It may indicate waste, inertia, or historical accident.

Finally, discuss mismatches. Look for commodity components receiving custom investment, uncertain components being given fixed commitments, product-like components being over-customized, and strategically important knowledge being moved outside the organization too early.

At the end of this process, the team should be able to state what the map changes about the decision. If the map changes nothing, either the decision was already obvious or the map is too shallow.

[![Image 5](https://substackcdn.com/image/fetch/$s_!-T7E!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14ccd0b1-f85c-402c-b92d-42fb6852b8f6_1024x558.png)](https://substackcdn.com/image/fetch/$s_!-T7E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14ccd0b1-f85c-402c-b92d-42fb6852b8f6_1024x558.png)

Let us walk through a complete example. The situation is an e-commerce company that wants to reduce support volume and improve customer experience around product returns. Several people in the company are arguing about whether to build a custom self-service returns portal or buy a returns management product.

Question: should we build, buy, or delay a self-service returns portal for customers?

Answer: we should not decide at the level of “returns portal” because that phrase hides many components with different maturity, cost, risk, and user value. Some parts may be standard product capabilities. Some may be commodity infrastructure. Some may be business-specific and worth custom investment. We need to map the capability before choosing a build or buy answer.

This reframes the conversation. The team is no longer asking whether the whole thing should be built or bought. It is asking which parts of the capability deserve custom work, which should be consumed from the market, which should reuse existing internal capabilities, and which should be delayed.

Question: who is the primary user?

Answer: the primary user is the customer who wants to return a product without contacting support. Secondary users include support agents, warehouse teams, finance, operations, and fraud teams, but the first map should be anchored on the customer.

This matters because different users produce different maps. A customer-anchored map focuses on clarity, eligibility, instructions, tracking, and refund confidence. A warehouse-anchored map would focus more on intake processing, inspection, restocking, exception handling, and inventory accuracy. Both may be useful, but they are not the same map.

Question: what does the customer need?

Answer: the customer needs to know whether the item can be returned, start the return easily, receive clear instructions, track the return status, and understand when the refund or exchange will happen. The customer does not primarily need “a portal”. The portal is one possible solution to the need.

This distinction prevents solution bias. If the team starts with “build a portal”, it may miss simpler improvements such as clearer order pages, better notifications, improved return policy wording, or tighter support automation. Starting with the need keeps the map honest.

Question: what capabilities directly satisfy the customer need?

Answer: the visible capabilities are return eligibility result, return request flow, return instructions, return label generation, return tracking, refund or exchange status, and customer notifications.

These are visible because the customer interacts with them directly or experiences their output. If they fail, the customer notices immediately. A confusing eligibility message, missing label, unclear instruction, or delayed refund status will generate support contact and reduce trust.

Question: what does each visible capability depend on?

Answer: return eligibility depends on order history, product category, delivery date, return policy rules, item condition rules, customer history, and fraud checks. Label generation depends on carrier integration, address validation, country rules, shipping service selection, and packaging constraints. Refund or exchange status depends on payment provider integration, warehouse confirmation, finance rules, inventory status, and customer notifications.

This is where the idea starts becoming a map. The returns portal is not one thing. It is a visible customer experience sitting on top of policy, data, logistics, payments, warehouse operations, identity, communication, monitoring, and exception handling.

The team now estimates where each component sits on the evolution axis. These placements are not universal truths. They are working assumptions for this company and this decision.

[![Image 6](https://substackcdn.com/image/fetch/$s_!Q-6h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff78b25f3-e106-4912-aac0-0a5c32d43c5c_2295x2107.png)](https://substackcdn.com/image/fetch/$s_!Q-6h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff78b25f3-e106-4912-aac0-0a5c32d43c5c_2295x2107.png)

The table is useful, but it is not yet the map. The map needs a visual arrangement where visibility and evolution can be seen together. A textual approximation can help in the article, but a final published version should include a proper image or SVG.

```
Visibility

High
  Customer
|
| needs
v
  Return eligibility result   [Custom built]
  Return request flow [Product -> Custom built]
  Return instructions [Custom built]
  Return label generation [Product]
  Return tracking [Product]
  Refund or exchange status   [Product -> Custom built]

Medium
  Return policy rules [Custom built]
  Fraud and abuse checks  [Custom built]
  Customer notifications  [Product]
  Carrier integration [Product]
  Payment refund integration  [Product -> Commodity]
  Inventory and warehouse update  [Custom built]

Low
  Order history   [Product -> Custom built]
  Address validation  [Product -> Commodity]
  Authentication  [Commodity]
  Monitoring and audit log[Product -> Commodity]
  Hosting [Commodity -> Utility]

Evolution
Genesis | Custom built | Product | Commodity / Utility
```

This approximation shows the reasoning, but a true Wardley map would place each component spatially on two axes. The vertical position would show visibility to the customer, and the horizontal position would show evolution. Lines would show dependencies. Annotations could mark inertia, risk, movement, or disagreement.

Question: what does the map reveal?

Answer: the strategic investment is not generic hosting, authentication, address validation, basic carrier integration, or email infrastructure. Those components are mature enough that the company should usually reuse internal standards, buy products, or consume existing services. The more strategic areas are return policy rules, eligibility logic, fraud checks, warehouse integration, refund orchestration, and the customer-facing experience around uncertainty.

This immediately changes the build versus buy conversation. A full custom build would waste effort on mature components. A full product purchase might fail if the product cannot represent the company’s policy, warehouse process, fraud rules, and customer promise. The better answer is likely a mixed strategy.

Question: where is the main risk?

Answer: the main risk is not whether the company can display a form. The main risk is whether the eligibility decision is correct, whether refund timing matches the customer promise, whether warehouse operations can support the process, whether fraud controls are proportionate, and whether customers understand what is happening without contacting support.

This is a practical insight. If the team had started with user interface screens, it might have underestimated the operational and policy work underneath the visible portal. The map shows that a beautiful flow can still fail if the eligibility logic, warehouse events, refund rules, and notifications are unreliable.

Question: what should not be built from scratch?

Answer: the team should not build custom authentication, custom address validation, custom carrier integration, custom email infrastructure, or custom hosting unless there are strong constraints. Those components are not the differentiating parts of the landscape. Building them would increase cost and delay without improving the customer’s return experience in a meaningful way.

Question: what should the company learn before scaling?

Answer: the company should learn which return reasons are most common, which product categories create exceptions, where customers currently contact support, how often fraud checks are needed, how quickly the warehouse can process returns, and whether customers understand the return status messages. The first release should test these assumptions before the company commits to a broader platform.

The map suggests that the team should not start by building a complete custom returns platform. It also suggests that buying a product and forcing every business rule into it may create problems if the company’s return policy and warehouse operations are specific.

A better strategy is to reuse or buy mature components while custom-building the policy and orchestration parts that reflect the company’s actual business. The team should use existing authentication, hosting, monitoring, address validation, notification infrastructure, and carrier services where possible. It should invest custom effort in eligibility rules, fraud checks, warehouse integration, refund orchestration, exception handling, and the customer-facing flow.

The first release should be deliberately narrow. For example, it could support one country, refund-only returns, a limited set of product categories, and customers with standard completed orders. It should exclude international returns, exchanges, damaged items, marketplace sellers, high-value fraud-risk items, and complex exceptions until the team has learned enough from the first slice.

The strategic decision is no longer “build or buy the returns portal”. The decision becomes more precise: buy or reuse mature components, build the business-specific logic, release a narrow slice, learn from real usage, and expand only after the risky assumptions have been tested.

That is the value of the map. It turns an abstract strategic argument into a concrete set of choices.

Once a map exists, the team needs to interpret it. The goal is not to admire the drawing. The goal is to find patterns that change the decision.

[![Image 7](https://substackcdn.com/image/fetch/$s_!XmOm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2194451a-26c6-4298-8772-deeb0f0b8ed0_2340x1357.png)](https://substackcdn.com/image/fetch/$s_!XmOm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2194451a-26c6-4298-8772-deeb0f0b8ed0_2340x1357.png)

These patterns help move the article from beginner explanation to practical judgment. A reader should not only know what the axes mean. They should begin to understand what certain positions imply.

For example, custom work in commodity space does not automatically mean the team is wrong. There may be regulatory or operational constraints. But the map changes the burden of proof. If the market provides mature address validation, the team needs a strong reason to build and operate its own.

The same applies in the opposite direction. If a component is still uncertain, forcing it through a fixed delivery plan may create false confidence. In that case, the responsible move may be to reduce scope, run an experiment, and learn before scaling.

Wardley Mapping is useful because many organizational decisions are really questions about user needs, dependencies, maturity, and movement. The map gives different functions a shared surface for discussing those questions.

[![Image 8](https://substackcdn.com/image/fetch/$s_!_hT1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1addb7ac-09f7-4297-9ecc-bc34a1f5e7cd_1600x1280.png)](https://substackcdn.com/image/fetch/$s_!_hT1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1addb7ac-09f7-4297-9ecc-bc34a1f5e7cd_1600x1280.png)

Product teams can use Wardley Mapping to separate user needs from feature requests. A stakeholder may ask for a dashboard, export, workflow, or portal, but the map asks what the user actually needs and what capabilities are required to satisfy that need.

In the returns example, “build a portal” was too broad. The map revealed several separate capabilities: eligibility, instructions, tracking, refund status, notifications, policy, fraud checks, and warehouse integration. That decomposition helps the product team prioritize the first useful slice.

[![Image 9](https://substackcdn.com/image/fetch/$s_!Pnzn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6d0683a-7351-490a-9fca-c6d68d3a6b0e_1600x1280.png)](https://substackcdn.com/image/fetch/$s_!Pnzn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6d0683a-7351-490a-9fca-c6d68d3a6b0e_1600x1280.png)

Platform teams can use Wardley Mapping to avoid building platforms from internal enthusiasm alone. A platform should serve repeated user needs, usually for internal users such as developers, product teams, analysts, or operations teams.

The map helps identify which components are mature enough to standardize and which are still too unstable. Standardizing authentication, deployment templates, observability, or service ownership may improve flow. Standardizing a business workflow that is still changing may freeze learning too early.

[![Image 10](https://substackcdn.com/image/fetch/$s_!JQKE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0602a279-d147-48c8-bb6f-b4f98b484274_1600x1280.png)](https://substackcdn.com/image/fetch/$s_!JQKE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0602a279-d147-48c8-bb6f-b4f98b484274_1600x1280.png)

Wardley Mapping improves build versus buy decisions because it shows that most capabilities are not one thing. A returns portal includes commodity components, product components, custom business rules, operational integrations, and user-facing experience.

The decision is rarely “build everything” or “buy everything”. A better decision may be to buy mature components, build the business-specific differentiators, and delay uncertain parts until the team has learned enough.

[![Image 11](https://substackcdn.com/image/fetch/$s_!wF2m!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa81e577b-9da3-45e9-89ef-d2aa3ed2dd7c_1600x1280.png)](https://substackcdn.com/image/fetch/$s_!wF2m!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa81e577b-9da3-45e9-89ef-d2aa3ed2dd7c_1600x1280.png)

Modernization is often framed too broadly. A system is old, painful, or unpopular, so the organization decides to replace it. This can become expensive if the team does not know which parts of the system are actually blocking valuable change.

A Wardley map helps identify which components are still strategically important, which are commodity but trapped, which are risky, and which can be left alone for now. It also helps distinguish technical discomfort from economic urgency.

[![Image 12](https://substackcdn.com/image/fetch/$s_!FuQN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4a72725-3d71-475a-8b86-be45173c67eb_1600x1280.png)](https://substackcdn.com/image/fetch/$s_!FuQN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4a72725-3d71-475a-8b86-be45173c67eb_1600x1280.png)

Cloud migration should not be treated as a strategy by itself. It is usually a change in how underlying components are provided and operated. The map helps ask which components should move, why they should move, and what practices must change around them.

Moving infrastructure without changing ownership, deployment, observability, cost management, resilience, and operating model may produce a more expensive version of the old system. Mapping helps make those dependencies visible before the migration becomes a large commitment.

[![Image 13](https://substackcdn.com/image/fetch/$s_!op69!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65363300-5ccf-4520-881c-967f87d7ee8e_1600x1280.png)](https://substackcdn.com/image/fetch/$s_!op69!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65363300-5ccf-4520-881c-967f87d7ee8e_1600x1280.png)

Team boundaries should support the flow of change. A map helps discuss whether teams should align around user needs, product areas, platforms, capabilities, or shared services.

A component in genesis may need a small exploratory team. A custom business capability may need close collaboration between product, engineering, operations, and domain experts. A commodity capability may belong in a platform, shared service, or external provider. The map helps avoid applying one team model to every kind of work.

[![Image 14](https://substackcdn.com/image/fetch/$s_!nP7r!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bf42e69-101c-47d9-80f2-0f383fcf125d_1024x558.png)](https://substackcdn.com/image/fetch/$s_!nP7r!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bf42e69-101c-47d9-80f2-0f383fcf125d_1024x558.png)

The first common mistake is starting with technology instead of the user. If the conversation begins with Kubernetes, microservices, Artificial Intelligence, cloud, data mesh, or platform engineering, the team is already at risk of anchoring on a solution. Technology belongs on the map as a component, not as the starting point.

The second mistake is mapping the organization chart instead of the value chain. The fact that a team owns something does not explain whether it is visible to the user, strategically important, commodity-like, duplicated, risky, or evolving. Sometimes the map reveals that the current organization structure is part of the problem.

The third mistake is treating the map as objective truth. A Wardley map is a model. Its value comes from making assumptions visible, not from pretending the drawing is reality. The right phrase is not “the map says”. The better phrase is “our current understanding is”.

The fourth mistake is trying to make the perfect map. A useful map is good enough to improve the conversation. The first map should create challenge, reveal assumptions, and guide the next question. It does not need to describe every system, dependency, or exception.

The fifth mistake is confusing low visibility with low importance. Hosting, authentication, backups, observability, payment integrity, and audit logs may sit low on the map, but failure in these components can damage the entire user experience. Low visibility means the user does not usually value custom craftsmanship there. It does not mean the component can be neglected.

The sixth mistake is assuming commodity means outsource. A commodity component may still remain internal for regulatory, security, latency, resilience, cost, or control reasons. The point is not automatic outsourcing. The point is appropriate treatment: standardization, automation, operational discipline, and clear ownership.

The seventh mistake is assuming custom means strategic. Custom may mean valuable differentiation. It may also mean historical accident, unnecessary variation, local preference, or unresolved complexity. The map asks for evidence rather than accepting custom work as important by default.

The eighth mistake is drawing once and never updating the map. User needs change, components evolve, vendors mature, regulation appears, and inertia grows. A map should be revisited when the landscape changes or when the decision becomes important again.

[![Image 15](https://substackcdn.com/image/fetch/$s_!wp9x!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3c0d559-50a1-485a-8fb9-accf6ccf451e_1024x558.png)](https://substackcdn.com/image/fetch/$s_!wp9x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3c0d559-50a1-485a-8fb9-accf6ccf451e_1024x558.png)

A first mapping session does not need to be complicated. The goal is to create a useful first map around a real decision, not to teach the entire theory of Wardley Mapping.

Invite a small cross-functional group. For a product or software decision, that might include product, engineering, operations, support, security, architecture, and someone close to the customer or user. The group should be small enough to have a real conversation and diverse enough to challenge assumptions.

Start with a decision statement. For example: “Should we build or buy a self-service returns capability?” Write the statement where everyone can see it. Then ask the group to identify the primary user and the user need. Spend enough time here, because a weak user need will distort the rest of the map.

Next, identify visible capabilities. Ask what the user experiences directly. In the returns example, this included eligibility, request creation, instructions, tracking, refund status, and notifications. Then move downward into dependencies. Ask what each capability needs in order to work.

Once the value chain is visible, place each component on the evolution axis. Do not let the group hide disagreement. If one person thinks return policy rules are custom and another thinks they are product-like, mark the disagreement. Disagreement is useful because it shows where assumptions differ.

After placement, look for mismatches. Ask where the organization is handcrafting mature components, where it is forcing certainty onto uncertain work, where it is over-customizing products, and where hidden dependencies create visible risk.

End the session with decisions and open questions. The output should not be only a map. It should include what the map changed, what the team now believes, what remains uncertain, what should be tested, and what move should happen next.

A simple 90-minute agenda could look like this:

[![Image 16](https://substackcdn.com/image/fetch/$s_!DnpK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e741e06-f970-46dc-93b3-0666cf3b01b7_1382x616.png)](https://substackcdn.com/image/fetch/$s_!DnpK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e741e06-f970-46dc-93b3-0666cf3b01b7_1382x616.png)

The facilitator’s job is not to defend the map. The facilitator’s job is to keep the conversation anchored on user needs, dependency, evolution, and decision quality.

Wardley Mapping is useful because it changes the quality of strategic conversation. It helps teams move from broad intention to situated judgment. Instead of asking only what the organization wants, the team asks who the user is, what the user needs, what components are required, how evolved those components are, and what move fits the landscape.

The most important lesson is not that every team needs a beautiful map. The important lesson is that strategy needs position. Without position, teams copy practices, overbuild commodity capabilities, standardize unstable work, outsource learning, and call internal preferences strategic.

In software and product work, this has a direct economic consequence. Poor strategic visibility can waste money, time, attention, and delivery capacity. It can also increase risk by hiding critical dependencies under user-facing plans. A Wardley map helps expose those commitments before they become expensive.

The practical next step is small. Pick one decision your team is already debating. Choose one user and one need. Draw the value chain. Place each component on the evolution axis. Discuss where the map changes the decision. If nothing changes, the map may be too shallow or the decision may already be obvious. If something changes, you have found the value of the practice.

*   Wardley, Simon. _Wardley Maps_. [https://learnwardleymapping.com/book/](https://learnwardleymapping.com/book/)

*   Wardley, Simon. _On being lost_. [https://medium.com/wardleymaps/on-being-lost-2ef5f05eb1ec](https://medium.com/wardleymaps/on-being-lost-2ef5f05eb1ec)

*   Wardley, Simon. _Finding a path_. [https://medium.com/wardleymaps/finding-a-path-cdb1249078c0](https://medium.com/wardleymaps/finding-a-path-cdb1249078c0)

*   Wardley, Simon. _Exploring the map_. [https://medium.com/wardleymaps/exploring-the-map-ad0266fad59b](https://medium.com/wardleymaps/exploring-the-map-ad0266fad59b)

*   Wardley, Simon. _Doctrine_. [https://medium.com/wardleymaps/doctrine-8bb0015688e5](https://medium.com/wardleymaps/doctrine-8bb0015688e5)

*   Wardley, Simon. _The play and a decision to act_. [https://medium.com/wardleymaps/the-play-and-a-decision-to-act-8eb796b1dff1](https://medium.com/wardleymaps/the-play-and-a-decision-to-act-8eb796b1dff1)

*   Wardley, Simon. _Getting started yourself_. [https://medium.com/wardleymaps/getting-started-yourself-e1a359b785a2](https://medium.com/wardleymaps/getting-started-yourself-e1a359b785a2)

*   Wardley, Simon. _Finding a new purpose_. [https://medium.com/wardleymaps/finding-a-new-purpose-8c60c9484d3b](https://medium.com/wardleymaps/finding-a-new-purpose-8c60c9484d3b)

*   Wardley, Simon. _Keeping the wolves at bay_. [https://medium.com/wardleymaps/keeping-the-wolves-at-bay-93de21b6b2f8](https://medium.com/wardleymaps/keeping-the-wolves-at-bay-93de21b6b2f8)

*   Wardley, Simon. _Charting the future_. [https://medium.com/wardleymaps/anticipation-89692e9b0ced](https://medium.com/wardleymaps/anticipation-89692e9b0ced)

*   Wardley, Simon. _I wasn’t expecting that_. [https://medium.com/wardleymaps/i-wasnt-expecting-that-dcfe122a2234](https://medium.com/wardleymaps/i-wasnt-expecting-that-dcfe122a2234)

*   Wardley, Simon. _The scenario_. [https://medium.com/wardleymaps/the-scenario-8bc05feee81](https://medium.com/wardleymaps/the-scenario-8bc05feee81)

*   Wardley, Simon. _Something wicked this way comes_. [https://medium.com/wardleymaps/something-wicked-this-way-comes-b028d5c607bf](https://medium.com/wardleymaps/something-wicked-this-way-comes-b028d5c607bf)

*   Wardley, Simon. _On the practice of scenario planning_. [https://medium.com/wardleymaps/on-the-practice-of-scenario-planning-49eed8279e90](https://medium.com/wardleymaps/on-the-practice-of-scenario-planning-49eed8279e90)

*   Wardley, Simon. _Super Looper_. [https://medium.com/wardleymaps/round-round-get-around-i-loop-around-d88e865d4337](https://medium.com/wardleymaps/round-round-get-around-i-loop-around-d88e865d4337)

*   Wardley, Simon. _To infinity and beyond_. [https://medium.com/wardleymaps/to-infinity-and-beyond-c7a53ccd2a07](https://medium.com/wardleymaps/to-infinity-and-beyond-c7a53ccd2a07)

*   Wardley, Simon. _Better for Less_. [https://medium.com/wardleymaps/better-for-less-58fe8c0a3aaa](https://medium.com/wardleymaps/better-for-less-58fe8c0a3aaa)

*   Wardley, Simon. _On playing chess_. [https://medium.com/wardleymaps/on-playing-chess-2634b825dbac](https://medium.com/wardleymaps/on-playing-chess-2634b825dbac)

*   Sun Tzu. _The Art of War_.
