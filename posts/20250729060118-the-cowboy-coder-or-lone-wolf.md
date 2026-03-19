---
title: "The Cowboy Coder or Lone Wolf"
requested_url: "https://emmanuelvalverderamos.substack.com/p/the-cowboy-coder-or-lone-wolf"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/the-cowboy-coder-or-lone-wolf"
substack_post_id: 168234553
retrieved_at: "2026-03-19T08:37:35.356Z"
---
# The Cowboy Coder or Lone Wolf

[![](https://substackcdn.com/image/fetch/$s_!z7BD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73d13d1f-ed5d-47c0-83e4-6c22451da592_6000x3236.jpeg)](https://substackcdn.com/image/fetch/$s_!z7BD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73d13d1f-ed5d-47c0-83e4-6c22451da592_6000x3236.jpeg)

###

People smells, like code smells, signal stress in the social and technical system. A single teammate can display more than one pattern. Change happens only when the person recognises the problem. Although coaching and structure help, a team cannot reform someone who will not engage, and waiting magnifies the harm.

### Context, motivation, and close cousins

Cowboy coding thrives in early-stage start-ups, rapid prototypes, and teams with weak technical leadership. Work is informal, deadlines fare luid, and processes are optional. An individual who enjoys direct control and instant feedback drifts into Lone Wolf habits.

Close cousins and the differences:

- Hero: follows the rules until a crisis, then bends them. The Cowboy ignores the rules from day one.
- Knowledge Kidnapper: keeps information for leverage. The Cowboy keeps it because documentation feels slower than coding.
- Martyr: seeks recognition for sacrifice. The Cowboy seeks freedom from oversight.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### Core behaviours

- Commits large changes directly to main without review.
- Works on private branches for weeks, then delivers a surprise merge.
- Skips tests and documentation because they “slow progress”.
- Refuses pair or mob sessions, claiming they “break flow”.
- Disregards shared conventions, renaming files and folders to personal taste.

### Early warning signs

- Sudden bursts of hundreds of changed lines appear in version control.
- Pull-request titles read “big refactor, easier to review by reading the code”.
- The team cannot run the product locally without asking one person.
- Stand-ups include “I did some magic yesterday, trust me”.

### Impact over time

- **Short term**: The Cowboy delivers visible features quickly.
- **Medium term**: integration pain grows, merge conflicts rise, and other developers slow down to understand surprise changes.
- **Long term**: the code drifts from agreed standards, defect counts climb, and the Cowboy becomes the only person able to patch production at speed.

### Software-economics impact and risks

- Delay cost: integration conflicts push release dates.
- Maintenance cost: undocumented shortcuts turn into expensive refactors.
- Opportunity cost: parallel work stalls while the team deciphers Lone Wolf changes.
- Explicit risks: bus factor of one on critical modules and unreviewed production code.

Team Topologies notes that ignoring cognitive load leads to delivery bottlenecks, delays, quality issues, and demotivation.

### Systemic impact

A Cowboy lowers psychological safety because teammates fear breaking hidden assumptions. Energy shifts from collaboration to damage control. Continuous improvement stalls since conventions and automation no longer fit the code. Leadership spends more time firefighting than planning.

### Variants

- Speed Cowboy: values raw feature velocity, ignores tests.
- Rewrite Cowboy: re-implements large areas without review.
- Stealth Cowboy: commits code while others sleep to avoid comments.

### Biases that feed the pattern

- Overconfidence bias: belief that personal code quality is always higher than team input.
- Present bias: valuing rapid delivery now over future maintenance pain.
- Ownership bias: treating part of the code as private territory.

### Root causes

Shallow review culture, missing continuous integration, lack of shared standards, reward systems that praise individual throughput, and leaders who mistake frequent commits for progress.

### Detection metrics

- The average pull-request size exceeds five hundred lines.
- Branch lifetime before merge surpasses five days in a trunk-based environment.
- Failing build rate rises after Cowboy merges.
- Fewer than half of the files show recent contributions from more than one author.

### Extended example

In a fintech start-up, Dana owns the risk-scoring service. The team has no pair programming, no trunk-based development, and no automated tests. Sprint after sprint, she pushes directly to main, arguing that review is overhead. When tests fail, she deletes the test folder to “unblock the pipeline”. Two months later, a security audit uncovers hard-coded credentials and an open port nobody knew about. Fixing the issues halts feature work for three weeks and costs forty thousand euros in emergency contractor fees. Investors learn that one developer controls the logic that approves loans and funding pauses until the team proves they have peer review, trunk-based development, and a working test suite.

### Mitigation paths

**Individual actions**

- Apply Never the Expert: if you built a component alone, stop coding in it and coach two teammates until they can ship changes without you.
- Pair or mob twice a week on critical areas.
- Write a one-page architecture note before large refactors.

**Team actions**

- Enforce branch policies requiring at least one reviewer and green tests.
- Limit pull-request size, for example, four hundred changed lines.
- Schedule regular codebase walkthroughs so knowledge spreads.

**Organisational actions**

- Tie performance reviews to collaboration metrics such as review participation and shared ownership.
- Provide continuous integration with fast feedback, making it easier to run tests than to skip them.
- Invest in coding standards and automated linters to guard the baseline.

### Preventive practices

Trunk-based development with small, frequent merges, ensemble programming, a Definition of Done that includes tests and documentation, a clear review culture, and retrospectives that surface Lone Wolf risks.

### TL;DR

Cowboy coding feels fast but trades short-term speed for long-term drag and risk. It raises integration costs, widens knowledge gaps, and leaves the team one step from failure. Enforce peer review, spread ownership, and reward collaboration over solo heroics.

### References

- Hunt, Andrew; Thomas, David. *The Pragmatic Programmer: Your Journey to Mastery*.
- Skelton, Matthew; Pais, Manuel. *Team Topologies*.
- Wake, William C. *Extreme Programming Explored*.
- Medium. Noor, Didiet. “The Myth of Lone Wolf Ten Times Developer.”
- https://medium.com/@lynxluna/the-myth-of-lone-wolf-10-developer-7916e94b5cd2
- Medium. Janis, CallMe. “How Cowboy Coding Has a Cost.” https://medium.com/@CallMeJanis/how-cowboy-coding-has-a-cost-148f0ae616c5
- ProFocus Technology. “The Danger of Lone Wolf Developers.” https://www.profocustechnology.com/general/danger-lone-wolf-developers
- Lockedown SEO. “The Dangers of Cowboy Coding.” https://lockedownseo.com/cowboy-coding/
