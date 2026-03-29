---
title: "The Martyr or Over-Committer"
requested_url: "https://emmanuelvalverderamos.substack.com/p/the-martyr-or-over-committer"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/the-martyr-or-over-committer"
substack_post_id: 168235568
retrieved_at: "2026-03-29T07:50:36.003Z"
---
# The Martyr or Over-Committer

[![](https://substackcdn.com/image/fetch/$s_!pLgZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67eb858a-97d4-45b1-974f-e5a445a4bed6_6016x4016.jpeg)](https://substackcdn.com/image/fetch/$s_!pLgZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67eb858a-97d4-45b1-974f-e5a445a4bed6_6016x4016.jpeg)

People smells, like code smells, signal hidden stress in a team. A single person can show several patterns at once. Change happens only when the individual recognises the issue. Coaching and structure help, but a team cannot rescue someone who refuses to adjust; waiting multiplies the harm.

### Context, motivation, and close cousins

The Martyr appears in cultures that praise visible effort, endless availability, and “going the extra mile.” Leaders reward hours worked rather than outcomes, and peers unconsciously reinforce the pattern by applauding heroic overtime.

*Close cousins*

- **Hero** seeks glory through crisis saves; the Martyr seeks validation through sacrifice.
- **Micromanager** controls details; the Martyr absorbs tasks to spare the team from pain.
- **Burnout Champion** (a future pattern) shares the same root causes but crashes before work is done.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### Core behaviours

- Volunteers for every urgent task and refuses to delegate.
- Works late nights or weekends and shares screenshots of time stamps as proof of dedication.
- Rejects help with phrases like “It’s faster if I do it.”
- Shows visible exhaustion yet insists “the release depends on me.”
- Accepts stretch goals without negotiating scope, then scrambles to deliver.

### Early warning signs

- Sprint commitments consistently exceed team capacity because the Martyr promises extra work.
- Pull requests arrive at irregular hours; build failures pile up until the Martyr is online.
- Vacation requests are postponed “until after the next milestone.”
- Retrospective notes read, “We will just push harder next time.”

### Impact over time

- **Short term:** deadlines appear safe because someone absorbs overflow.
- **Medium term:** velocity plummets when the Martyr context-switches; knowledge sharing stalls; quality drops.
- **Long term:** burnout strikes, turnover rises, and the remaining team inherits unfinished work and hidden debt.

### Software economics and risks

- **Delay cost:** when the Martyr finally crashes, blocked tasks surface at once.
- **Maintenance cost:** rushed fixes and skipped reviews inflate technical debt.
- **Opportunity cost:** innovation pauses while the team fire-fights defects created under time pressure.
- **Explicit risks:** missed deadlines, production incidents, loss of key personnel.

In *Team Topologies* Skelton and Pais warn that hidden work and unbalanced load create fragile delivery systems that cannot scale.

### Systemic impact

Sacrifice becomes the norm; healthy work boundaries erode. Colleagues feel guilty taking time off, and new hires adopt the same unhealthy habits. Psychological safety declines because admitting limits looks like weakness.

### Variants

- **Victim-Martyr:** complains about overload but refuses help.
- **Crunch Champion:** glorifies long hours and expects others to mirror them.
- **Stealth Martyr:** hides overtime to appear effortlessly productive, masking unsustainable habits.

### Biases that feed the pattern

- **Self-serving bias:** equating hours with value.
- **Sunk-cost fallacy:** staying late because time already invested must pay off.
- **Reward substitution:** leadership praises visible effort, not sustainable delivery.

### Root causes

Hero culture, unclear workload boundaries, lack of capacity planning, performance reviews tied to perceived dedication rather than results, and leadership silence around burnout.

### Detection metrics

- The individual’s average weekly hours exceed the team median by 20 percent or more.
- The vacation balance accrued is greater than one employment year.
- The ratio of tasks completed solo vs paired exceeds three to one.
- Spike in defects traced to late-night or last-minute commits.

### Extended example

At a SaaS provider, Jordan owns customer reporting. Pair programming, trunk-based development, and tests exist, but Jordan bypasses them during crunch. Each sprint, Jordan takes extra tickets, merges unreviewed code at night, and promises fixes “over the weekend.” The team delivers on schedule until a critical outage occurs during Jordan’s first holiday in eight months. Reports fail for seventy-two hours, breaching service agreements and costing ninety-five thousand euros in credits. Emergency patches reveal duplicated queries and race conditions introduced during late-night merges. Jordan returns exhausted and guilty, accepts more tasks to “make up the loss,” and resigns four weeks later. Recruitment and onboarding cost a further fifty-five thousand euros, while remaining engineers spend six sprints stabilising the module.

### Mitigation paths

**Individual actions**

- Practice [Never the Expert](https://emmanuelvalverderamos.substack.com/p/never-the-expert-breaking-knowledge): if you hold exclusive knowledge, coach two teammates and stop coding the module until they can deliver without you.
- Use a personal work-in-progress limit: no more than two active tasks at once.
- Schedule regular breaks and protect vacation time.

**Team actions**

- Adopt capacity-based sprint planning; limit carry-over work.
- Pair or mob on high-risk tasks so that effort and context spread naturally.
- Surface load metrics in retrospectives and adjust commitments.

**Organisational actions**

- Align performance reviews with sustainable throughput, not overtime.
- Provide burnout awareness training based on lessons from *Leaders Eat Last.*
- Monitor workload dashboards for outliers and intervene early.

### Preventive practices

Work-in-progress limits, collective ownership, pair programming, continuous integration, and explicit sprint goals keep scope realistic. Psychological-safety checks and regular feedback loops encourage teammates to signal when they are at capacity.

### TL;DR

The Martyr trades self-sacrifice for perceived progress, but hidden over time becomes hidden debt. Delay, maintenance cost, and attrition follow. Balance workload, share context, and reward sustainable pace to keep teams healthy and resilient.

### References

- Brown, Andrew Richard. *Taming Your Dragon: Addressing Your Technical Debt.*
- Hunt, Andrew; Thomas, David. *The Pragmatic Programmer: Your Journey to Mastery.*
- Skelton, Matthew; Pais, Manuel. *Team Topologies.*
- Sinek, Simon. *Leaders Eat Last.*
- Wake, William C. *Extreme Programming Explored.*
