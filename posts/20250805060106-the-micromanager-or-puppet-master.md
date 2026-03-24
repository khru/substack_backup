---
title: "The Micromanager or Puppet Master"
requested_url: "https://emmanuelvalverderamos.substack.com/p/the-micromanager-or-puppet-master"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/the-micromanager-or-puppet-master"
substack_post_id: 168234821
retrieved_at: "2026-03-24T08:45:19.220Z"
---
# The Micromanager or Puppet Master

[![](https://substackcdn.com/image/fetch/$s_!U_3p!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F558523e6-e344-4799-a9b9-11a2a2abbf0b_5184x3456.jpeg)](https://substackcdn.com/image/fetch/$s_!U_3p!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F558523e6-e344-4799-a9b9-11a2a2abbf0b_5184x3456.jpeg)

People smells, like code smells, show that the social and technical system is under stress. A single teammate can mix several patterns. Improvement happens only when the person accepts the problem. Coaching and structure help, but a team cannot reform someone who refuses to change. Waiting multiplies the damage.

### Context, motivation, and close cousins

Micromanagement thrives when delivery pressure is high and trust is low. Leaders who grew up in command and control cultures or who were promoted for individual output often fear losing visibility. They respond by directing every detail.

Close cousins and the differences:

- Hero: centralises knowledge to rescue crises, whereas the Micromanager dictates tasks to avoid surprises.
- Knowledge Kidnapper: hoards information; the Micromanager hoards decisions.
- Seagull Manager: swoops in with criticism, then vanishes; the Micromanager stays present and controlling.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### Core behaviours

- Reviews code for style nits instead of behaviour.
- Assigns work in micro tasks and demands hourly status updates.
- Rewrites pull requests at night without consulting the author.
- Decides road-map priorities unilaterally, bypassing product owners.
- Stands over shoulders during pairing sessions, steering each keystroke.

### Early warning signs

- Stand-ups drift into daily stand-before-the-throne meetings.
- Calendar fills with check-ins titled “quick sync” that last an hour.
- Developers ask peers for permission to commit trivial changes.
- Slack channels show questions like “Is it safe to merge or do we wait for Sam?”

### Impact over time

- **Short term**: decisions are fast because one person makes them.
- **Medium term**: autonomy drops, innovation slows, and staff engagement scores fall.
- **Long term**: turnover rises, hiring pipeline shrinks due to reputation, and delivery speed collapses when the Micromanager becomes a bottleneck.

### Software-economics impact and risks

- Delay cost: every decision queues for a single approver.
- Maintenance cost: the code reflects one mind, limiting collective ownership.
- Opportunity cost: experiments die because the approval overhead is too high.
- Explicit risks: low bus factor on decisions, burnout, and hidden single points of failure.

> "The greatest gift you can give your team is control of their own work."
> – Lopp, *The Art of Leadership*

### Systemic impact

Micromanagement erodes psychological safety. People stop raising risks and hide unfinished work to avoid scrutiny. Continuous improvement stalls because experiments need permission. The culture shifts from outcome orientation to task completion.

### Variants

- Shadow Coder: silently rewrites code after hours.
- Over Scheduler: fills every day with status meetings.
- Check-list Captain: measures success by task count, not impact.

### Biases that feed the pattern

- Illusion of control: belief that more oversight equals better outcomes.
- Authority bias: the assumption that a higher rank implies better decisions.
- Outcome bias: judging work by visible busyness instead of value delivered.

### Root causes

Reward systems that value visible workload, past success as an individual contributor, lack of training in delegation, and cultures that punish failure rather than learn from it.

### Detection metrics

- Lead time from coding complete to merge approval exceeds two days.
- More than eighty percent of pull requests have revisions made solely by the manager.
- Forty percent or more of working hours are spent in progress meetings.
- Annualised turnover in the team is higher than the organisational average.

### Extended example

In a retail platform team, Marta is promoted from senior developer to engineering manager. Pair programming, trunk-based development, and automated tests exist on paper but not in practice. Fearful of missing commitments, Marta demands that every pull request reference a Jira ticket and that no line ships without her review. She rejects changes that use unfamiliar patterns, rewriting them overnight. Developers stop proposing refactors because they are replaced anyway. Velocity slips ten percent each sprint as reviews pile up. After two quarters, three engineers leave. Replacements cost sixty thousand euros in recruitment. A post-mortem reveals that seventy percent of Marta’s time is spent editing code, leaving no room for coaching or removing blockers. Leadership realises the team has become slower than before Marta’s promotion.

### Mitigation paths

**Individual actions**

- Use the [Never the Expert](https://emmanuelvalverderamos.substack.com/p/never-the-expert-breaking-knowledge) rule: if you are the gatekeeper for reviews, step back and let two peers approve changes while you coach.
- Switch code reviews to behaviour focus: ask What does this code do instead of Why did you format it this way.
- Practice intent-based leadership from *Turn the Ship Around!* by asking teams to state intent rather than seek permission.

**Team actions**

- Introduce pair or ensemble programming sessions with rotating driver roles.
- Establish a Definition of Done that includes shared ownership and removes the need for a single-person sign-off.
- Measure pull request throughput and discuss it in retrospectives.

**Organisational actions**

- Align performance reviews with coaching, delegation, and team outcomes.
- Provide leadership training on situational awareness and trust, as described in *Engineering Management for the Rest of Us*.
- Limit meeting sizes and mandate at least one maker day without status meetings each week.

### Preventive practices

Small, cross-functional teams with clear product goals, regular retrospectives, trunk-based development with automated tests, and leadership that rewards learning over control create an environment where micromanagement cannot thrive.

### TL;DR

Micromanagement feels safe but trades control for speed and creativity. It raises delay costs, increases turnover, and turns the manager into a bottleneck. Delegate decisions, share ownership, and focus on outcomes, not activity, to build a resilient and innovative team.

### References

- Drasner, Sarah. *Engineering Management for the Rest of Us*.
- Lopp, Michael. *The Art of Leadership*.
- Marquet, L. David. *Turn the Ship Around!*.
- Skelton, Matthew; Pais, Manuel. *Team Topologies*.
- Willink, Jocko. *Leadership Strategy and Tactics*.
- Lencioni, Patrick. *The Five Dysfunctions of a Team*.
