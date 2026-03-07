---
title: "The Hero / Rockstar / “10× Developer”"
requested_url: "https://emmanuelvalverderamos.substack.com/p/the-hero-rockstar-10-developer"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/the-hero-rockstar-10-developer"
substack_post_id: 168233948
retrieved_at: "2026-03-07T08:25:40.285Z"
---
# The Hero / Rockstar / “10× Developer”

[![](https://substackcdn.com/image/fetch/$s_!GmX7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96eac6dd-9300-41bb-bd53-f66b3b052fab_6000x4000.jpeg)](https://substackcdn.com/image/fetch/$s_!GmX7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96eac6dd-9300-41bb-bd53-f66b3b052fab_6000x4000.jpeg)

People smells, like code smells, warn that the social and technical system is under stress. A single teammate can show several patterns at once. Improvement happens only when the individual accepts the problem. Coaching and structure help, but a team cannot fix someone who will not engage; waiting multiplies the harm.

### Context, motivation, and close cousins

Hero culture appears where deadlines loom, legacy systems resist refactoring, and rewards favour dramatic saves over steady prevention. Leaders may equate visible effort with value, and customers often applaud last-minute “miracles”.

How does it differ from related patterns?

- **Cowboy Coder** rejects standards from the start, while the hero follows them until crisis strikes.
- **Knowledge Kidnapper** withholds information to gain leverage, while the hero hoards it unintentionally because everything flows through one person.
- **Martyr** seeks admiration for sacrifice, while the hero seeks victory and status.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### Core behaviours

- Centralizes critical knowledge, scripts, and configurations.
- Works solo on sensitive paths, claiming it is faster.
- Delays reviews because “nobody else sees the whole picture”.
- Answers most design questions, discouraging others from learning.

### Early warning signs

- Pull-request queues stall when the hero is away.
- Incident post-mortems repeatedly name the same fixer.
- Chat threads include “Ask Alex; only Alex knows”.
- The bus factor for a key subsystem drops to one.

### Impact over time

- **Short term**: incidents resolve quickly, and the team feels relieved.
- **Medium term**: delivery slows whenever the hero context-switches; onboarding stretches; silos form.
- **Long term**: burnout risk for the hero, attrition for others, systemic fragility, and rising defect rates.

### Software-economics impact and risks

- Delay cost: features queue for hero bandwidth.
- Maintenance cost: undocumented hot fixes become expensive debt.
- Opportunity cost: new initiatives wait behind the hero backlog.
- Explicit risks: single point of failure, unreviewed production changes, and security gaps.

Team Topologies notes that when cognitive load is ignored, teams become bottlenecks that suffer delays, quality issues, and demotivation.

### Systemic impact

Hero worship skews structures and culture. Expertise equals power, discouraging knowledge sharing and lowering psychological safety. Performance reviews value firefighting over prevention, so automation and documentation stall.

### Variants

- Gatekeeper Hero – controls every merge into main.
- Fire-fighter Hero – thrives on incident adrenaline.
- Martyr-Hero – complains about workload yet refuses delegation.

### Biases that feed the pattern

- Self-enhancement bias – overestimating one’s indispensability.
- Outcome bias – celebrating dramatic rescues while ignoring missing safeguards.
- Reward substitution – incentives favour visibility and crisis wins over sustainable health.

### Root causes

Perverse incentives, weak succession planning, legacy complexity, cultures that equate hours with commitment, and leadership fear of an initial dip while knowledge spreads.

### Detection metrics

- The bus factor is below three on critical repositories.
- More than twenty percent of production incidents were resolved by one individual.
- Pull-request lead time doubles when the hero is unavailable.
- Vacation usage is under half of the entitlement.

### Extended example

Two sprints before launch, the payments service collapses nightly. Alex patches it in minutes, pushes to main, and saves the milestone. Everyone applauds. Two weeks later, Alex attends a conference; deployments halt because nobody can decipher the deployment scripts. Operations clones production data to debug, breaching GDPR, and marketing delays a campaign, burning one hundred fifty thousand euros in advertising. The chief technology officer realises the service level agreement depends on a single engineer. A competitor offers Alex a thirty percent raise, and Alex leaves. Velocity drops forty percent for four months while the team reverse-engineers patches, customer churn reaches twelve percent, morale sinks, and the board questions leadership. The heroic save has become a seven-figure liability.

### Mitigation paths

Individual actions

- Pair or mob regularly, placing the hero in the navigator seat to spread expertise.
- Write lightweight runbooks and checklists after each fix.
- Follow **[Never the Expert](https://emmanuelvalverderamos.substack.com/p/never-the-expert-breaking-knowledge)**: if you are the recognised expert, you should not perform tasks in your specialty. Instead, coach two teammates who take the driver's seat until they can deliver without you. Expertise becomes a teaching duty, not a bottleneck.

Team actions

- Rotate on-call, reviews, and key ceremonies.
- Adopt collective ownership. “The whole team owns all code. Anybody can change any part they need to.”
- Map critical knowledge areas and flag subsystems with a low bus factor.

Organisational actions

- Reward prevention, mentoring, and documentation, not firefighting.
- Require at least two maintainers for every critical component before release.
- Allocate learning time, for example, one afternoon per sprint for knowledge-sharing talks.
- Invest in continuous integration, continuous delivery, and automated tests so releases do not rely on heroic effort.

### Preventive practices

Pair programming, collective ownership, limited cognitive load for stream-aligned teams, continuous integration, and mandatory peer reviews reduce hero dependency.

### TL;DR

Hero culture creates a velocity illusion: fast rescues today and chronic bottlenecks tomorrow. Real costs appear as delay, maintenance, turnover, and risk. Spread knowledge, align incentives with sustainable teamwork, automate routine work, and build a resilient, replaceable team.

### References

- Greene, Robert. *Mastery*.
- Hunt, Andrew; Thomas, David. *The Pragmatic Programmer: Your Journey to Mastery*.
- Skelton, Matthew; Pais, Manuel. *Team Topologies*.
- Wake, William C. *Extreme Programming Explored*.
- Hanselman, Scott. *The Myth of the Rockstar Programmer*. https://www.hanselman.com/blog/the-myth-of-the-rockstar-programmer
