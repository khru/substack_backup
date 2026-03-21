---
title: "The Knowledge Kidnapper or Silo Builder"
requested_url: "https://emmanuelvalverderamos.substack.com/p/the-knowledge-kidnapper-or-silo-builder"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/the-knowledge-kidnapper-or-silo-builder"
substack_post_id: 168235092
retrieved_at: "2026-03-21T08:27:33.582Z"
---
# The Knowledge Kidnapper or Silo Builder

[![](https://substackcdn.com/image/fetch/$s_!hNFq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc246da23-5188-46ae-8358-68bbd1043342_5184x3456.jpeg)](https://substackcdn.com/image/fetch/$s_!hNFq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc246da23-5188-46ae-8358-68bbd1043342_5184x3456.jpeg)

##

People smells, like code smells, reveal strain in the social and technical system. One person may show several patterns at once. Improvement happens only when the individual acknowledges the issue. Coaching and structure help, but a team cannot reform someone who refuses to change, and delay magnifies the harm.

### Context, motivation, and close cousins

This pattern appears where legacy systems are opaque, documentation is scarce, and individual expertise is rewarded more than collaboration. The organisation often idolises specialists and measures value by the difficulty of replacement.

Close cousins and the differences:

- Hero focuses on crisis rescue, while the Knowledge Kidnapper maintains quiet control day by day.
- Cowboy Coder hides knowledge by ignoring process, while the Kidnapper hides it deliberately to stay indispensable.
- Micromanager hoards decisions, while the Kidnapper hoards technical know-how.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### Core behaviours

- Keeps deployment scripts and runbook details in personal folders.
- Answers questions vaguely or withholds key context.
- Blocks pairing sessions or refuses knowledge transfer meetings.
- Maintains private branches or tooling that only they can run.
- Documents high-level flow but omits critical parameters and edge cases.

### Early warning signs

- New hires cannot complete onboarding without the Kidnapper.
- Service alerts route directly to one individual.
- Code comments say, "Ask Pat before touching this".
- Knowledge sharing meetings get postponed repeatedly.

### Impact over time

- **Short term**: deliveries stay on track because the Kidnapper fixes issues quickly.
- **Medium term**: velocity dips when other developers must wait for explanations.
- **Long term**: the bus factor drops to one, burnout risk rises, and the team stalls when the Kidnapper is absent.

### Software economics impact and risks

- Delay cost: tasks block waiting for answers.
- Maintenance cost: undocumented decisions require reverse engineering.
- Opportunity cost: product ideas wait until the Kidnapper has time.
- Explicit risks: single point of failure, knowledge loss upon resignation, and inability to rotate on call.

Team Topologies warns that bottlenecks caused by hidden knowledge create systemic fragility that limits scale.

### Systemic impact

Psychological safety erodes because people fear breaking unknown rules. Career growth stalls for others, and resentment grows. Leadership spends effort retaining one person instead of building a resilient team.

### Variants

- Legacy Guardian keeps old code and resists refactoring suggestions.
- Tool Wizard owns custom pipelines that nobody else can run.
- Domain Gatekeeper owns business logic specifications and refuses to share access.

### Biases that feed the pattern

- Scarcity bias: belief that knowledge is power only when scarce.
- Status quo bias: fear that sharing will change personal influence.
- Fundamental attribution error: assuming others will misuse information.

### Root causes

Reward systems that praise unique expertise, lack of onboarding budgets, absence of pair programming culture, and leaders equating irreplaceability with value.

### Detection metrics

- Bus factor of one on critical repositories.
- Support tickets are resolved by the same individual over fifty percent of the time.
- Less than ten percent of the key documentation is edited by multiple authors.
- Vacation overlap charts show gaps in coverage.

### Extended example

A logistics company relies on a routing engine written five years ago by Nora. No pair programming, trunk-based development, or tests exist for this module. To deploy, Nora calls a private script that sets obscure environment flags. When a new developer proposes improvements, Nora says she will handle them later. One Friday, Nora becomes ill and cannot respond to incidents. Orders fail to route and delivery windows slip, costing eighty thousand euros in penalties. Emergency contractors spend two weeks reverse engineering the code and discover hard-coded secrets. Management realises the real expense was not Nora's absence but years of unchecked knowledge hoarding.

### Mitigation paths

Individual actions

- Follow [Never the Expert](https://emmanuelvalverderamos.substack.com/p/never-the-expert-breaking-knowledge): stop coding in your private area and mentor two teammates until they can deploy without you.
- Record short walkthrough videos after each release.
- Schedule pair programming on the most hidden parts of the system.

Team actions

- Rotate on call and code ownership every sprint.
- Add documentation updates to the Definition of Done.
- Use architectural decision records to log why and how key choices are made.

Organisational actions

- Include knowledge sharing in performance reviews and promotions.
- Budget half a day each sprint for learning sessions and internal talks.
- Provide automation for onboarding environments so that no single person controls access.

### Preventive practices

Pair or ensemble programming, collective ownership, trunk-based development, automated tests, and a culture that values transparency over individual heroics all reduce the appeal and possibility of knowledge kidnapping.

### TL;DR

The Knowledge Kidnapper creates artificial scarcity that slows delivery and increases risk. Short-term control becomes long-term liability. Spread knowledge, align incentives with transparency, and build tooling that makes sharing the default path.

### References

- Hunt, Andrew; Thomas, David. *The Pragmatic Programmer: Your Journey to Mastery*.
- Skelton, Matthew; Pais, Manuel. *Team Topologies*.
- Wake, William C. *Extreme Programming Explored*.
- Meadows, Donella. *Thinking in Systems*.
- Lencioni, Patrick. *The Five Dysfunctions of a Team*.
