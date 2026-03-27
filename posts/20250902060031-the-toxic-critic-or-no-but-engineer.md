---
title: "The Toxic Critic or “No-but” Engineer"
requested_url: "https://emmanuelvalverderamos.substack.com/p/the-toxic-critic-or-no-but-engineer"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/the-toxic-critic-or-no-but-engineer"
substack_post_id: 168235821
retrieved_at: "2026-03-27T08:57:55.701Z"
---
# The Toxic Critic or “No-but” Engineer

[![](https://substackcdn.com/image/fetch/$s_!OG0k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2dea687e-9bc1-4a0c-88a9-6ebf64b03e0b_5184x3456.jpeg)](https://substackcdn.com/image/fetch/$s_!OG0k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2dea687e-9bc1-4a0c-88a9-6ebf64b03e0b_5184x3456.jpeg)

People smells alert us to hidden stress in a team just as code smells warn of design issues. A single teammate can combine several patterns at once. Improvement starts only when the individual acknowledges the problem. Coaching and structure help, yet a team cannot change someone who refuses to engage; delay multiplies the harm.

### Context, motivation, and close cousins

A Toxic Critic thrives when high standards are valued but psychological safety is low. Teams that confuse bluntness with honesty encourage sharp put-downs disguised as feedback.

Close cousins and the differences:

- Micromanager dictates solutions; the Toxic Critic blocks ideas without offering alternatives.
- Seagull Manager criticises from above and vanishes; the Toxic Critic stays in the trenches and keeps saying “No, but ...”.
- Knowledge Kidnapper withholds information; the Toxic Critic discourages sharing altogether.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### Core behaviours

- Shoots down proposals with phrases such as “that will never work” or “we tried that and failed”, without evidence or suggestions.
- Leaves snide comments on pull requests focusing on style over substance.
- Publicly mocks mistakes instead of guiding improvements.
- Dominates discussions, interrupting others and dismissing new voices.
- Rarely documents decisions, claiming the obvious should not require writing.

### Early warning signs

- Brainstorming sessions end early because people stop suggesting ideas.
- Pull request authors request specific reviewers to avoid negative comments.
- Team chat channels contain sarcastic emojis or gifs after someone shares work.
- Engineers phrase ideas as questions to avoid direct dismissal.

### Impact over time

- **Short term**: a few bugs may be caught quickly due to constant scrutiny.
- **Medium term**: psychological safety drops, idea flow slows, and team members self-censor.
- **Long term**: creative problem solving dies, turnover rises, and technical debt grows because improvements never pass the “No-but” filter.

### Software economics and risks

- Delay cost: discussions loop while the Critic seeks perfect solutions.
- Maintenance cost: outdated patterns remain because change faces constant opposition.
- Opportunity cost: new features stall; innovation moves to competitors.
- Explicit risks: loss of talent, reduced diversity of thought, and hidden design flaws that survive untested.

### Systemic impact

A single Toxic Critic can tilt culture toward blame and defensiveness. Experienced engineers pull back from mentoring, and juniors stop asking questions. The team enters a negative spiral where silence feels safer than contribution.

### Variants

- Gate S-keeper: applies arbitrary style guidelines to block merges.
- Sniper: fires biting critiques in group channels, never one-on-one.
- Nostalgia Guard: dismisses anything not built “the old reliable way”.

### Biases that feed the pattern

- Negativity bias: giving more weight to flaws than possibilities.
- Confirmation bias: seeking evidence that new ideas will fail.
- Illusion of superiority: believing personal standards are objectively correct.

*The Hidden Leadership Biases That Sabotage Teams* notes that unchecked negativity bias erodes motivation and teamwork.

### Root causes

Feedback culture that prizes clever put-downs, lacks coaching skills, unclear decision criteria, and leaders who reward correctness over collaboration.

### Detection metrics

- Pull requests with more than three review cycles rise above the team average.
- Fewer than 20 percent of planning session participants speak twice or more.
- Engagement survey item “I feel safe sharing new ideas” scores below sixty percent.
- Voluntary turnover spikes within two quarters of repeated negative incidents.

### Extended example

In a media-streaming company, Priya is known for spotting performance issues but also for harsh reviews. Pair programming, trunk-based development, and automated tests are mandated, yet Priya leaves curt comments such as “sloppy” or “read the spec” without detail. Junior developers stop suggesting test refactors, fearing ridicule. During a major scaling project, the database team ignores a fresh sharding proposal because Priya said “too risky” months earlier. The existing design fails during a Black Friday sale, causing three hours of outage and a one hundred and twenty thousand euro revenue hit. Post-mortem analysis shows the dismissed proposal would have reduced query load by forty percent. Two engineers resigned within a month, citing hostile feedback.

### Mitigation paths

Individual actions

- Practice Ask-Offer-Ask: start with clarifying questions, offer constructive feedback, and ask how you can help.
- Pair with peers you often critique, focusing on coaching language.
- Keep a personal “positivity ledger”, writing at least one positive observation per review.

Team actions

- Establish a feedback code of conduct that separates behaviour critique from personal attack.
- Use structured review checklists that focus on behaviour and acceptance criteria over style.
- Rotate facilitation in retrospectives so quieter voices lead sessions.

Organisational actions

- Train leaders in non-violent communication and coaching techniques from *Coaching for Performance*.
- Tie performance evaluations to collaboration metrics such as review helpfulness, not just defect counts found.
- Provide anonymous upward feedback channels and act on repeated patterns quickly.

### Preventive practices

Pair programming, psychological safety check-ins, explicit team norms for respectful critique, and rotating code review partners limit the space for toxic commentary. Continuous integration tools enforce style rules automatically so reviews focus on behaviour and value.

### TL;DR

The Toxic Critic blocks ideas with negativity and no alternatives, draining psychological safety and slowing delivery. Costs rise through delay, missed opportunities, and attrition. Replace harsh critique with constructive feedback, share ownership of quality, and foster a culture where every voice can improve the code.

### References

- Brown, Andrew Richard. *Taming Your Dragon: Addressing Your Technical Debt*.
- Hunt, Andrew; Thomas, David. *The Pragmatic Programmer: Your Journey to Mastery*.
- Skelton, Matthew; Pais, Manuel. *Team Topologies*.
- Whitmore, John. *Coaching for Performance*.
- Sinek, Simon. *Leaders Eat Last*.
- Beck, Kent. *Extreme Programming Explained: Embrace Change*.
