Title: Trunk-based development is not a Git trick. It is what continuous integration looks like.

URL Source: http://emmanuelvalverderamos.substack.com/p/trunk-based-development-is-not-a

Final URL: https://emmanuelvalverderamos.substack.com/p/trunk-based-development-is-not-a

Published Time: 2026-03-10T06:00:49+00:00

Markdown Content:
Many teams say they do CI and CD.

They have pipelines, green checks, staging environments, and a button that deploys. And yet integration is painful, releases are stressful, and “merge week” still exists.

This article is training grade. It is long because it is meant to be used as a playbook, not only as an opinion. It combines four perspectives into one coherent thread:

*   The CI and CD illusion: why having pipelines is not the same as practicing CI or achieving CD.

*   Merge hell as a business problem: why delayed integration creates compounding risk and cost.

*   The economics of small batches: why batch size and WIP change the financial profile of delivery.

*   A migration story: how to modernize legacy systems while staying in a trunk-based world.

It also includes two sets of concepts that make this practical in real systems:

*   Parallel change and expand and contract for safe evolution of APIs and databases.

*   Explore, expand, extract as a product phase model that explains why the “right” engineering behavior changes over time.

1.   The CI and CD illusion

2.   The vocabulary that stops most arguments

3.   Merge hell, fake feedback, and the cone of change

4.   The economics of small batches, WIP, and value delivery

5.   What trunk-based development is, and what it is not

6.   Branching models compared

7.   Working on trunk day to day

8.   Code review without killing flow

9.   Parallel change and expand and contract

10.   Safety techniques: feature flags, dark launching, branch by abstraction, strangler fig

11.   Explore, expand, extract and why strategy changes over time

12.   Rollback versus roll forward

13.   Databases: schema evolution without downtime, with a concrete example

14.   Measuring impact with delivery performance metrics

15.   Migration story: mature REST API, English schema, and performance fixes

16.   Capstone workshop exercise: thought and debate

17.   Failure modes and anti patterns

18.   Glossary

19.   Resume

20.   References

[![Image 1](https://substackcdn.com/image/fetch/$s_!UliO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1325e72c-b149-4472-8ab6-3bfd16e480a1_1280x698.png)](https://substackcdn.com/image/fetch/$s_!UliO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1325e72c-b149-4472-8ab6-3bfd16e480a1_1280x698.png)

The most common failure mode is confusing tools with practices.

A pipeline is automation. Automation is useful. But CI is a discipline and CD is a capability. You can automate a workflow that still batches work, delays feedback, and turns integration into an event. That does not become CI just because it runs faster.

> “Continuous Integration … has nothing to do with tools.”  
> Martin Fowler.

A second confusion is “branch builds equal CI”. If your code lives in long-lived branches and only meets at the end, you can have lots of green checks and still pay the delayed integration tax.

[![Image 2](https://substackcdn.com/image/fetch/$s_!UO2X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fb0a38e-4fc9-48ee-adeb-5bade5293851_3364x1012.png)](https://substackcdn.com/image/fetch/$s_!UO2X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fb0a38e-4fc9-48ee-adeb-5bade5293851_3364x1012.png)

> “Running such a process on every feature branch is ‘CI theater’ that debases the name.”  
> Martin Fowler.

If this sounds strict, that is the point. Strict definitions protect you from cargo-culting: doing the visible parts while missing the parts that create the benefits.

![Image 3](https://substackcdn.com/image/fetch/$s_!S2cD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04bdd791-8add-497b-a6fa-fd4b73da2ec4_5008x712.png)

Continuous integration is best understood as a habit: developers integrate work into a shared integration point frequently and validate it with automated checks. The intent is that conflicts and failures show up quickly, while context is still fresh and fixes are cheap.

> “Each member of a team merges their changes … at least daily.”  
> Martin Fowler.

A key detail is that CI is about verifying the shared integrated product. If your “CI” is validating many private branches that only meet at the end, you are still deferring the truth.

Some teams use short-lived branches and still match the intent of CI, as long as integration is genuinely frequent and feedback is fast. The practical issue is not the presence of a branch. The practical issue is branch lifetime, integration cadence, and review latency turning into a queue.

Continuous delivery is the capability to keep the system in a releasable state and release changes on demand with low risk. Automation is required, but CD also depends on test strategy, deployment discipline, observability, rollback, and team behavior.

Deploy means code is running somewhere, including production.  
Release means users can experience the behavior.

This distinction is the hinge that makes trunk-based work practical. If deploy and release are the same, teams feel forced to hide work in long-lived branches. If deploy and release are decoupled, teams can integrate continuously while controlling exposure safely.

> “Software that’s been successfully integrated into a mainline code stream still isn’t software that’s out in production doing its job.”  
> Martin Fowler.

[![Image 4](https://substackcdn.com/image/fetch/$s_!Akcr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0833d570-2fae-45f3-990f-787236b88c6e_1280x698.png)](https://substackcdn.com/image/fetch/$s_!Akcr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0833d570-2fae-45f3-990f-787236b88c6e_1280x698.png)

Merge conflicts hurt, but the deeper issue is divergence. The longer work stays isolated, the more assumptions diverge. Some conflicts are trivial text conflicts. Many are semantic conflicts where both changes make sense locally but not together.

That is why integration often feels unpredictable. It is not only about volume of code. It is about interactions between changes.

Long-lived branches create false confidence. You build and tests pass, but you validated a code state that will never reach production unchanged because it excludes parallel changes.

Trunk-based development forces evaluation against the integrated truth. That shifts discovery of conflicts and regressions earlier, when fixes are cheaper.

[![Image 5](https://substackcdn.com/image/fetch/$s_!AKfW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6a72a0f-da2d-4e42-892a-cde3e578c325_1280x698.png)](https://substackcdn.com/image/fetch/$s_!AKfW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6a72a0f-da2d-4e42-892a-cde3e578c325_1280x698.png)

As time passes, changing a decision often gets more expensive because more code, more people, and more dependencies pile up around it. Delayed integration widens that cone. You discover issues later, when they are harder to untangle.

Trunk-based development narrows the cone by pulling integration forward and shrinking the time between change and feedback.

![Image 6](https://substackcdn.com/image/fetch/$s_!yOpm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd561b042-7f30-4836-98c4-2da78fc3031d_4501x1060.png)

This is where trunk-based stops being preference and becomes an economic lever.

[![Image 7](https://substackcdn.com/image/fetch/$s_!NlLH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2ccc6a3-287b-4298-9075-3ae5f2bc84f0_1280x698.png)](https://substackcdn.com/image/fetch/$s_!NlLH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2ccc6a3-287b-4298-9075-3ae5f2bc84f0_1280x698.png)

Batch size is the amount of change you push through the system as a unit.

In software there is no visible inventory, so teams underestimate batch size. A two week feature merged at the end is a large batch. A small change shipped the same day is a small batch.

Small batches reduce risk and reduce the blast radius of failure. They also speed up learning. You learn sooner whether a change works technically and whether it matters commercially.

![Image 8](https://substackcdn.com/image/fetch/$s_!F6wE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F411dee46-3652-49c1-9776-ab3c1a40f99d_4232x906.png)

WIP means work in progress, the inventory of unfinished work.

High WIP increases context switching, queues, coordination cost, and lead time. This is not a personality problem. It is a system property. If you start too many things at once, you finish fewer things and you finish them later.

A practical consequence is that trunk-based pushes you toward “stop starting, start finishing” because frequent integration collapses when work items are too big.

Incremental value delivery means you add value in small, usable increments. Each increment should be capable of standing on its own, even if it is modest. That does not mean every increment is customer facing, but it does mean every increment moves the product toward a real outcome you can observe, validate, and build on.

Iterative delivery means you improve what already exists through feedback loops. You ship something, observe, learn, then refine. Iteration is how you reduce uncertainty and correct course without needing a rewrite. Increment is how you keep momentum and keep value flowing.

> “An evolutionary method is one that is both iterative and incremental in nature.”  
> Scott W. Ambler and Pramod J. Sadalage.

Trunk-based development supports both. It nudges teams to slice work into vertical slices that can be integrated frequently, deployed safely, and validated quickly. If your slices are purely technical and do not change a behavior you can observe, you will struggle to justify frequent delivery, and you will drift back into batching.

A useful test is: can you describe, in one sentence, what observable outcome this slice enables. If not, it is probably not a value slice yet.

[![Image 9](https://substackcdn.com/image/fetch/$s_!mMMZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65b2eb7d-de51-4e8d-865c-11e7b36d9bca_2993x1852.png)](https://substackcdn.com/image/fetch/$s_!mMMZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65b2eb7d-de51-4e8d-865c-11e7b36d9bca_2993x1852.png)

Trunk-based development is a branching model where developers collaborate on a single shared branch called trunk and resist pressure to create long-lived branches by using specific techniques so the system can remain releasable while work is in progress.

The enemy is not “branches exist.” The enemy is branch lifetime and delayed integration.

One practical rule captures the spirit:

> “It is of paramount importance that all team members commit to trunk at least once every 24 hours.”  
> Paul Hammant.

Different teams need different operating modes. The key is to choose one intentionally and set policies that protect flow.

![Image 10](https://substackcdn.com/image/fetch/$s_!Ub6h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68e9601c-8e27-4b1c-8b68-39dd46e953ff_1252x237.png)

[![Image 11](https://substackcdn.com/image/fetch/$s_!y22I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11aca183-e1ec-44f2-a024-bcf60860000b_1254x323.png)](https://substackcdn.com/image/fetch/$s_!y22I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11aca183-e1ec-44f2-a024-bcf60860000b_1254x323.png)

A useful reframe is:

You can keep pull requests and still behave like trunk-based, but only if branch lifetime stays short and review latency stays low enough that it does not become a queue.

A trunk-based workflow is a set of operational commitments.

Frequent integration keeps divergence small. The reason is mechanics: the longer you wait, the more you diverge, and the harder integration becomes.

If trunk is broken, the team is either blocked or building on unstable ground. A broken trunk is a flow incident.

Fix fast, or revert fast.

People fail at trunk-based adoption because “small” stays vague. Here are practical heuristics that work in real teams:

*   Time heuristic: if you cannot integrate at least daily, the batch is too big.

*   Scope heuristic: if a change touches many subsystems, split it or create a seam first.

*   Coordination heuristic: if you need many people to merge at once, you are batching.

*   Risk heuristic: if rollback is unclear, the batch is too big.

A simple batch ladder:

![Image 12](https://substackcdn.com/image/fetch/$s_!voSK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40b56f1c-7fc1-4af5-920d-7739668493d4_1252x226.png)

Code review is essential. The question is latency.

If review takes hours or days, it becomes a queue. Queues cause batching. Batching causes long-lived branches. Long-lived branches destroy frequent integration.

[![Image 13](https://substackcdn.com/image/fetch/$s_!-ICD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85b962ec-82b4-4449-8356-da33a8572a6a_1280x698.png)](https://substackcdn.com/image/fetch/$s_!-ICD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85b962ec-82b4-4449-8356-da33a8572a6a_1280x698.png)

Pairing gives continuous review with near zero latency. Mob style collaboration extends that to a group. Both reduce the need for slow asynchronous queues and increase shared understanding.

Pull requests can work in trunk-based development if they stay short-lived and reviews happen fast. If a PR sits for single day, it stops being review and becomes delayed integration.

A practical policy is to set a review latency target that matches your integration target. If you want daily integration, multi day PR queues are structurally incompatible.

> “Code review … should not be a requirement for a Pull Request to be merged.”  
> Martin Fowler.

That line is not an anti-review statement. It is an anti-queue statement. The goal is fast feedback without delaying integration.

Additional information in this post: [https://open.substack.com/pub/a4al6a/p/stop-using-pull-requests](https://open.substack.com/pub/a4al6a/p/stop-using-pull-requests)

This is the bridge between “integrate frequently” and “change real systems safely.”

In always-on systems, the engineer’s first responsibility is continuity of business operations. Code cleanliness matters, but not at the cost of risky maintenance windows and brittle big-bang changes. If the only way you can ship a structural change is “everyone awake at night and hope nothing goes wrong,” the delivery system is not safe enough.

Parallel change exists because real systems have concurrency, rolling deployments, and mixed versions running at the same time. That forces you to think in sequences, not events: add compatibility, migrate gradually, then remove compatibility when it is safe.

Two simple rules capture this priority:

> “Service is always up and running.”  
> Edu Ferro.
> 
> 
> “Support for two versions in parallel.”  
> Edu Ferro.

> “Parallel change, also known as expand and contract, is a pattern … in a safe manner.”  
> Danilo Sato.

The key mindset shift is: you do not perform the change. You perform a sequence that makes the change safe.

Expand and contract is parallel change with explicit operational constraints, especially for persistent data and systems that must remain available. The core idea is simple: expand by introducing a new structure without breaking the old, migrate consumers and data, then contract by removing the old structure only when it is no longer needed.

When you are changing persistent data, the hard part is mixed versions and long-running migrations. That is why the pattern insists on multiple steps.

> “The overall changes need to be deployed in several distinct steps.”  
> Tim Wellhausen.

![Image 14](https://substackcdn.com/image/fetch/$s_!lgO0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c3fb8dd-d842-4d30-91c0-35e76ecc9879_1531x236.png)

This pattern deliberately adds temporary complexity to protect the business. You may duplicate data, duplicate writes, accept two contracts, or run two code paths. That complexity is the safety investment. The “contract” step is where you pay it back by removing the old path.

![Image 15](https://substackcdn.com/image/fetch/$s_!jSEj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36af5680-2433-4e11-b6bf-563a2e4704ab_1396x236.png)

And this is where deploy versus release becomes practical: expand and contract keeps compatibility safe while feature flags and rollout controls decide when the business actually “launches.”

To understand better parallel change I’ve build a small web site to explain it with examples: [https://parallel-change-guide.netlify.app/](https://parallel-change-guide.netlify.app/)

[![Image 16](https://substackcdn.com/image/fetch/$s_!2dzB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F488b04cb-2745-40be-9d30-1f6ecb6aec4b_4705x1971.png)](https://substackcdn.com/image/fetch/$s_!2dzB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F488b04cb-2745-40be-9d30-1f6ecb6aec4b_4705x1971.png)

Feature flags are runtime switches that enable or disable behavior without branching the codebase. Their core purpose is to decouple deploy from release so you can integrate frequently while controlling exposure.

> “Separating [feature] release from [code] deployment.”  
> Pete Hodgson.

Feature flags work best when they are planned as part of feature design, not bolted on at the end. Planning affects scope, naming, rollout strategy, who can flip the flag, and how you remove it later.

> “Feature flags shouldn’t be an afterthought.”  
> LaunchDarkly.

A practical ownership rule:

*   Release flags are typically owned by product and engineering together.

*   Operational flags are typically owned by engineering and operations for safety.

*   Experiment flags are typically owned by product with engineering support.

This clarifies who controls what, and reduces the risk of a “kill switch” being treated like a marketing launch toggle.

Pete Hodgson shares two interesting categorizations on his categorization on the article “feature Toggles”

[![Image 17](https://substackcdn.com/image/fetch/$s_!QETV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3072dcaf-df32-49fb-817b-6fe479a236ac_1024x768.png)](https://substackcdn.com/image/fetch/$s_!QETV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3072dcaf-df32-49fb-817b-6fe479a236ac_1024x768.png)

[![Image 18](https://substackcdn.com/image/fetch/$s_!rxMi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b88cc59-bacc-451c-9d85-5805fcd2b16e_1024x768.png)](https://substackcdn.com/image/fetch/$s_!rxMi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b88cc59-bacc-451c-9d85-5805fcd2b16e_1024x768.png)

A single flag should control a small unit of behavior. If a feature has multiple parts, use multiple flags and treat one as the master, or define dependencies explicitly. This prevents one flag from becoming a hidden branching system.

If you want flag cleanup to happen, make cleanup easy.

A naming convention that helps in practice usually encodes:

*   team or service

*   purpose

*   temporary or permanent

*   creation date, or a ticket reference

That makes “stale flags” visible without needing a detective story.

Two rollout patterns show up repeatedly in trunk-based teams:

*   **Ring rollout**: internal users, then beta users, then all users.

*   **Percentage rollout also known as Test A/B**: 1 percent, 5 percent, 10 percent, 25 percent, 50 percent, then 100 percent.

The important part is not the exact percentages. The important part is having explicit stop conditions based on error rate, latency, or business metrics.

[![Image 19](https://substackcdn.com/image/fetch/$s_!YKgq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0789f487-cfe4-42a7-9511-5974357c1fcc_705x1212.png)](https://substackcdn.com/image/fetch/$s_!YKgq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0789f487-cfe4-42a7-9511-5974357c1fcc_705x1212.png)

A flag is only a rollback if “off” remains safe in the current data and code state.

> “You should test the behavior of the application with the flag toggled on and off.”  
> LaunchDarkly.

This is especially important when a flag hides a schema or database change.

> “This is especially important if the feature is related to a schema or database change.”  
> LaunchDarkly.

Also, define what happens when flag evaluation fails or settings cannot be fetched. This is not a corner case. It is normal in distributed systems.

> “Configuring a fallback value can eliminate unexpected experiences or errors with interrupted connections.”  
> LaunchDarkly.

A practical rule:

*   Every flag has a documented fallback behavior.

*   Every flag has a default state that is safe.

This point is important, usually on test suits that use feature flags, have a default setup for the feature falgs, so all the flags by default return on or off this helps to write less setup code on all the tes.

The biggest long-term risk with flags is debt: flags that never get removed and leave permanent conditional paths.

A simple operational discipline helps:

> “The act of removing a flag should not be a separate process from the act of creating a flag.”  
> LaunchDarkly.

Practical options:

*   Create the removal work item when you create the flag.

*   Schedule cleanup at the end.

*   Review flags in a recurring “flag review” cadence.

For operational flags, add governance:

*   role-based access control

*   audit logs for who changed what and when

*   runbook documentation, including what to do if a feature is disabled during an incident

This turns feature flags into a stability tool, not only a delivery tool.

Dark launching means deploying code into production that is not reachable by users yet. It is one of the safest ways to integrate incomplete work because you validate in the real environment without exposing behavior.

Dark launching works best when paired with observability, because you need to know whether the dark code path is behaving, consuming resources, or failing silently.

Branch by abstraction creates an interface seam so old and new implementations can coexist. You migrate gradually across multiple releases instead of building a long-lived branch.

> “Allows you to release the system regularly while the change is still in-progress.”  
> Martin Fowler.

A practical sequence:

1.   Introduce an abstraction.

2.   Route existing callers through it.

3.   Implement the new version behind the abstraction.

4.   Switch gradually, often behind a flag.

5.   Remove the old implementation.

6.   Optionally remove the abstraction once stable.

Strangler fig is a modernization pattern where you gradually route slices of behavior to a new implementation until the legacy system can be retired.

> “A gradual process of modernization.”  
> Martin Fowler.

The discipline is to find seams where you can reroute small slices first. If you try to strangle everything at once, you are back to a rewrite.

[![Image 20](https://substackcdn.com/image/fetch/$s_!oZwM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4baf1068-e41f-4b31-8f26-e744a16d4e52_4235x1358.png)](https://substackcdn.com/image/fetch/$s_!oZwM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4baf1068-e41f-4b31-8f26-e744a16d4e52_4235x1358.png)

[![Image 21](https://substackcdn.com/image/fetch/$s_!F37R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3a192f4-ea79-4cf5-b8ba-533875160c6a_1280x698.png)](https://substackcdn.com/image/fetch/$s_!F37R!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3a192f4-ea79-4cf5-b8ba-533875160c6a_1280x698.png)

Note: this “expand” refers to a product phase, not the “expand” step in expand and contract.

Explore, expand, extract is a model for how the “right” behavior changes as uncertainty declines and scaling pressure increases.

In explore, you are searching for a viable return on a viable investment. Speed means short feedback loops and many small experiments.

In expand, growth reveals bottlenecks. Speed means moving attention and resources to the next constraint before it chokes growth.

In extract, the product is clearer and the focus shifts toward profitability, repeatability, and efficiency. Speed means reducing unnecessary delay in a more stable operating mode.

Two lines capture the core shift:

> “Exploration requires diverse, tangential thinking and experimentation.”  
> Kent Beck.
> 
> 
> “Expansion requires singular focus on removing the next bottleneck.”  
> Kent Beck.

And the headline that explains why engineering strategy must adapt:

> “Value-maximizing behavior changes dramatically.”  
> Kent Beck.

This belongs in a trunk-based article because trunk-based development is a delivery constraint that helps in all three phases, but for different reasons:

*   In explore, it reduces the cost of learning.

*   In expand, it reduces the blast radius of urgent changes.

*   In extract, it reduces coordination waste and makes improvements routine.

[![Image 22](https://substackcdn.com/image/fetch/$s_!3xwG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff36106e4-f6d0-41cc-bf63-774ca760aaef_4594x1494.png)](https://substackcdn.com/image/fetch/$s_!3xwG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff36106e4-f6d0-41cc-bf63-774ca760aaef_4594x1494.png)

Rolling forward is often the default: fix the bug, deploy the fix. But rollback must remain viable for serious incidents.

A practical posture:

*   Use flags so disabling a feature is a rollback, when the data state allows it.

*   Use expand and contract so switching reads back is a rollback during migrations.

*   Accept that some steps create a point of no easy return and plan those steps carefully.

[![Image 23](https://substackcdn.com/image/fetch/$s_!_aMK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4c75341-920d-413d-b6b7-6c7d7e0a2279_1280x698.png)](https://substackcdn.com/image/fetch/$s_!_aMK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4c75341-920d-413d-b6b7-6c7d7e0a2279_1280x698.png)

Database change is where trunk-based adoption often breaks, because schema change feels risky and irreversible. Expand and contract is the safe path, but teams need to see it end to end.

One important nuance, tied to feature flags: a flag is only a rollback if the data remains compatible. After some schema changes, toggling “off” can mean data loss or corruption. That is why you separate schema evolution into steps and keep rollback paths explicit.

[![Image 24](https://substackcdn.com/image/fetch/$s_!bQRJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37ee0de6-06f0-4c83-86e9-d6c6bcd5e459_1280x698.png)](https://substackcdn.com/image/fetch/$s_!bQRJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37ee0de6-06f0-4c83-86e9-d6c6bcd5e459_1280x698.png)

Assume a table kunde with column kunden_id and you want customer_id. Also assume the system must stay up.

*   Add baseline metrics for the endpoints that read and write this table.

*   Add minimal tests around the API behavior that uses these fields.

*   Identify consumers: application code, reporting, exports, jobs.

*   Add customer_id alongside kunden_id.

*   Deploy code that writes both fields for new and updated rows.

*   Keep reads using the old field for now.

Rollback at this stage is easy: stop writing the new field and remove it if needed.

*   Backfill existing rows in small batches.

*   Ensure the backfill logic produces the same values as the application logic.

*   Protect against concurrent updates so you do not create inconsistent duplicates.

Rollback remains practical: you can clear the new field and rerun.

*   Switch reads to customer_id behind a flag.

*   Validate parity: compare results for a sample of requests or rows.

*   Watch performance metrics and error rates.

Rollback is practical: flip the flag back to read the old field.

*   Once all servers are using the new field for reads, stop writing the old field.

*   Remove old field usage in code.

This is a critical moment: rollback is no longer easy without restoring from backup, because the old field will fall behind.

*   Remove the old column only after you are confident no code writes or reads it and you have observed stability long enough.

[![Image 25](https://substackcdn.com/image/fetch/$s_!TVwa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cda0533-525c-4acb-94d7-ac4ddde09b60_679x1424.png)](https://substackcdn.com/image/fetch/$s_!TVwa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cda0533-525c-4acb-94d7-ac4ddde09b60_679x1424.png)

You cannot manage what you cannot see. Delivery performance metrics let you discuss trunk-based adoption as an outcome problem, not a preference war.

Two short quotes anchor the point.

> “We settled on four: delivery lead time, deployment frequency, time to restore service, and change fail rate.”  
> Nicole Forsgren, Jez Humble, and Gene Kim.
> 
> 
> “There is no tradeoff between improving performance and achieving higher levels of stability and quality.”  
> Nicole Forsgren, Jez Humble, and Gene Kim.

A simple adoption scorecard:

![Image 26](https://substackcdn.com/image/fetch/$s_!fSta!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52a2c4c0-0693-4b6e-b89f-5d5424756d9a_1252x271.png)

Agreements prevent relapse. They also reduce ambiguity.

[![Image 27](https://substackcdn.com/image/fetch/$s_!Uz7S!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd052956f-1f37-4007-a2b4-f699a430f379_1253x477.png)](https://substackcdn.com/image/fetch/$s_!Uz7S!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd052956f-1f37-4007-a2b4-f699a430f379_1253x477.png)

Now we combine the whole article into one scenario.

You have:

*   a legacy REST API that does not follow a mature REST model

*   a monolithic backend with weak modular boundaries

*   no automated tests

*   a database that is not normalized

*   query performance issues

*   column names in German

You want:

*   a more mature REST API

*   schema naming in English

*   performance improvements

You also want frequent integration and frequent deployment, without taking the system down.

In many real teams, a practical first target is consistent resource-oriented endpoints with correct HTTP semantics. That includes:

*   clear resource naming

*   consistent use of methods

*   consistent status codes

*   consistent error format

*   pagination and filtering conventions

*   backward compatible evolution strategy

Hypermedia may be valuable in some domains, but you can gain most of the benefits earlier by standardizing semantics and contracts.

![Image 28](https://substackcdn.com/image/fetch/$s_!PduZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F31975a13-8df0-479d-a9a2-85ea58738cfe_1250x266.png)

Use expand and contract at the boundary:

*   **expand**: add new endpoints or new fields without breaking old clients

*   **migrate**: move clients gradually and measure adoption

*   **contract**: remove old behavior only when adoption is complete

Do not couple API evolution to a big internal rewrite. Strangle the contract first, then evolve internals behind it.

Performance work should be evidence-led:

*   baseline metrics per endpoint

*   identify top offenders by total cost

*   inspect query plans and access patterns

*   fix indexing and query shapes

*   reduce over-fetching and add pagination

*   normalize where it reduces anomalies and improves indexing

*   consider read models only when necessary

[![Image 29](https://substackcdn.com/image/fetch/$s_!OW8d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a9007d4-a925-4910-b562-f3a8d1d95d86_527x2236.png)](https://substackcdn.com/image/fetch/$s_!OW8d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a9007d4-a925-4910-b562-f3a8d1d95d86_527x2236.png)

This is the exercise you run after the training, when people know the toolbox.

*   Groups of 3 to 5.

*   30 minutes to design a plan.

*   4 minutes to present.

*   2 minutes cross examination.

*   10 minutes debrief.

Design a migration plan for the scenario above under trunk-based constraints:

*   integrate at least daily

*   deploy frequently

*   keep the service running

*   each step must be small, safe, observable, reversible

*   API evolution plan using expand and contract

*   database evolution plan using expand, migrate, contract

*   performance plan with baseline and verification

*   safety plan: flags, dark launching, rollback

*   testing plan starting from zero

These kill trunk-based adoption more reliably than any technical limitation:

*   slow pipelines that force batching

*   PR queues that delay integration

*   trunk is allowed to stay red for hours

*   flags are added but never removed

*   big-bang database changes

*   “integration week” and “stabilization sprint” become rituals

*   slices are technical increments with no observable value, so urgency to deliver fades

If you see these, do not argue about Git. Fix the feedback loop, batch size, and safety mechanisms.

*   **Batch size**: the amount of change moved through the system as a unit.

*   **Characterization test:** a test that captures current behavior so you can refactor safely.

*   **Continuous delivery**: the capability to keep software releasable and release on demand with low risk.

*   **Continuous integration**: frequent integration into a shared mainline with automated validation and fast repair.

*   **Dark launching:** deploying code that is not reachable or visible to users yet.

*   **Deploy**: running a version in an environment.

*   **Expand and contract**: a safe evolution pattern that expands, migrates, then contracts.

*   **Explore, expand, extract**: a product phase model describing how value-maximizing behavior changes over time.

*   **Feature flag:** a runtime switch that controls behavior without branching.

*   **Iterative delivery:** improving what exists through feedback loops.

*   **Incremental delivery**: adding value in small usable increments.

*   **Parallel change**: running old and new in parallel long enough to migrate safely.

*   **Release**: making behavior available to users.

*   **Strangler fig**: incrementally replacing a legacy system by routing slices of behavior to a new implementation.

*   **Trunk**: the shared mainline branch used for collaboration.

*   **WIP**: work in progress, unfinished inventory that increases lead time and coordination cost.

[![Image 30](https://substackcdn.com/image/fetch/$s_!ARL4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3cecdb3c-2412-4ee5-b8e1-df0a292a8c1d_4740x3465.png)](https://substackcdn.com/image/fetch/$s_!ARL4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3cecdb3c-2412-4ee5-b8e1-df0a292a8c1d_4740x3465.png)

![Image 31](https://substackcdn.com/image/fetch/$s_!s4l2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3ba5db6d-7a55-4610-937b-02ef3c85c49c_9274x978.png)

*   Martin Fowler. “Continuous Integration Certification.” [https://martinfowler.com/bliki/ContinuousIntegrationCertification.html](https://martinfowler.com/bliki/ContinuousIntegrationCertification.html)

*   Martin Fowler. “Continuous Integration.” [https://martinfowler.com/articles/continuousIntegration.html](https://martinfowler.com/articles/continuousIntegration.html)

*   Jez Humble, David Farley. Continuous delivery: reliable software releases through build, test, and deployment automation.

*   Scott W. Ambler, Pramod J. Sadalage. Refactoring databases: evolutionary database design.

*   Paul Hammant. Trunk-based development.

*   Martin Fowler. “Ship, show, ask.” [https://martinfowler.com/articles/ship-show-ask.html](https://martinfowler.com/articles/ship-show-ask.html)

*   Edu Ferro. Lean software development: small safe steps workshop.

*   Martin Fowler.. “Parallel change.” [https://martinfowler.com/bliki/ParallelChange.html](https://martinfowler.com/bliki/ParallelChange.html)

*   Tim Wellhausen. “Expand and contract: a pattern to apply breaking changes to persistent data with zero downtime.” [https://www.tim-wellhausen.de/papers/ExpandAndContract/ExpandAndContract.html](https://www.tim-wellhausen.de/papers/ExpandAndContract/ExpandAndContract.html)

*   Pete Hodgson. “Feature toggles.” [https://martinfowler.com/articles/feature-toggles.html](https://martinfowler.com/articles/feature-toggles.html)

*   Martin Fowler. “Branch by abstraction.” [https://martinfowler.com/bliki/BranchByAbstraction.html](https://martinfowler.com/bliki/BranchByAbstraction.html)

*   Martin Fowler. “Strangler fig application.” [https://martinfowler.com/bliki/StranglerFigApplication.html](https://martinfowler.com/bliki/StranglerFigApplication.html)

*   Kent Beck. “Fast slow in 3x: explore, expand, extract.” [https://medium.com/@kentbeck_7670/fast-slow-in-3x-explore-expand-extract-6d4c94a7539](https://medium.com/@kentbeck_7670/fast-slow-in-3x-explore-expand-extract-6d4c94a7539)

*   Nicole Forsgren, Jez Humble, Gene Kim. Accelerate: the science of lean software and DevOps. LaunchDarkly. 30 feature flagging best practices mega guide.

*   Kent Beck. “Explore then expand then extract.”
