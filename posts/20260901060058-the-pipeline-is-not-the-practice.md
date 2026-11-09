Title: The pipeline is not the practice

URL Source: http://emmanuelvalverderamos.substack.com/p/the-pipeline-is-not-the-practice

Final URL: https://emmanuelvalverderamos.substack.com/p/the-pipeline-is-not-the-practice

Published Time: 2026-09-01T06:00:58+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!PV4x!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7482a13a-9f67-4ce3-a7ee-2d527c02b0cb_1024x558.png)](https://substackcdn.com/image/fetch/$s_!PV4x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7482a13a-9f67-4ce3-a7ee-2d527c02b0cb_1024x558.png)

A restaurant can have a beautiful kitchen display system. Every order appears on a screen. Every plate has a timer. Every station has a checklist. The waiter can see whether the starter is ready, whether the main course is being plated, and whether the dessert is waiting in the cold section. From the outside, it looks controlled, digital, traceable, and modern.

But imagine something else is happening behind the screen. Each cook works alone for hours. The sauce is prepared without knowing whether the meat will be ready. The garnish changes without the person plating the dish knowing it. The dessert team only discovers at the end of the night that the menu was modified at noon. When service starts, the kitchen does not cook. It negotiates.

The screen did not solve integration. It only made part of the work visible.

Now imagine a second problem. The dishes are ready, the food is good, and the kitchen has done its work. But no plate can leave unless the owner, the head chef, the restaurant manager, and the nervous person who “knows how things usually go wrong” all stand together and approve it. Every plate leaving the kitchen becomes an event. The screen did not solve delivery either.

This is the software industry’s “CI/CD” problem.

Many teams say they have _Continuous Integration_ (CI) and _Continuous Delivery_ (CD) because they have a pipeline. They have a YAML file. They have build stages, test stages, security checks, code quality gates, deployment jobs, approval buttons, badges, dashboards, environments, and perhaps a notification channel full of green ticks and red crosses.

That tooling may be valuable. It may even be necessary. But it is not enough.

A pipeline is not _Continuous Integration_ (CI). A pipeline is not _Continuous Delivery_ (CD). A pipeline is a mechanism. _Continuous Integration_ (CI) and _Continuous Delivery_ (CD) are disciplines. They are related, they reinforce each other, and they often share infrastructure, but they solve different problems in the software value stream.

The phrase “CI/CD” is acceptable as a tool category. It is harmful as a mental model.

_Continuous Integration_ (CI) is the practice of integrating everyone’s work into a shared mainline frequently, at least daily, with automated feedback that detects integration problems quickly. Its central question is: **Can everyone’s work coexist safely in the shared codebase?**

_Continuous Delivery_ (CD) is the capability to release validated changes safely, quickly, and sustainably on demand. Its central question is: **Can this change be released safely when the business decides?**

A deployment pipeline can support both practices, but having a deployment pipeline does not mean a team is practicing either. A pipeline can run tests without real integration. A pipeline can deploy to staging without real release readiness. A pipeline can enforce gates while the team still works in large batches, integrates late, releases nervously, and depends on manual coordination.

The practical distinction is this:

[![Image 2](https://substackcdn.com/image/fetch/$s_!FPOg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F096758c0-86c4-435b-bea6-8c56d4056569_1816x644.png)](https://substackcdn.com/image/fetch/$s_!FPOg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F096758c0-86c4-435b-bea6-8c56d4056569_1816x644.png)

1.   The phrase that made us lazy

2.   Why the confusion costs money

3.   _Continuous Integration_ (CI): the discipline of shared reality

4.   The CI impostors

5.   _Continuous Delivery_ (CD): the discipline of release readiness

6.   Deployment is not release

7.   Where the deployment pipeline fits

8.   Quality gates inspect, capabilities produce

9.   Why CI and CD should not be glued together

10.   A diagnostic for your own team

11.   Diagrams

12.   Conclusions

13.   References

[![Image 3](https://substackcdn.com/image/fetch/$s_!GHeI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fb34ae5-214f-4877-bd6d-d3bc49c66610_2794x1890.png)](https://substackcdn.com/image/fetch/$s_!GHeI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fb34ae5-214f-4877-bd6d-d3bc49c66610_2794x1890.png)

“CI/CD” is one of those expressions that became useful before it became clear. It is short. It fits in product pages, job descriptions, architecture diagrams, platform team roadmaps, vendor documentation, and engineering presentations. Nobody wants to say, every time, “the set of practices and tools we use to integrate code frequently, build it, test it, package it, deploy it, promote it, verify it, and sometimes release it.”

So we say “CI/CD.”

[![Image 4](https://substackcdn.com/image/fetch/$s_!p3IW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44dfb4bd-f83f-4ae7-99e7-684870a6b2a2_1024x558.png)](https://substackcdn.com/image/fetch/$s_!p3IW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44dfb4bd-f83f-4ae7-99e7-684870a6b2a2_1024x558.png)

The problem is not the abbreviation itself. The problem starts when the abbreviation becomes the model. Once _Continuous Integration_ (CI) and _Continuous Delivery_ (CD) are compressed into a single object, teams stop asking which problem they are solving. They look at a pipeline and assume the practice exists. They look at a green build and assume integration is healthy. They look at a staging deployment and assume delivery is continuous.

That is where the damage begins.

Martin Fowler describes _Continuous Integration_ (CI) as a software development practice where team members merge their changes into a shared codebase frequently, usually at least daily, with each integration verified by an automated build that includes tests. The central purpose is to detect integration errors quickly and reduce the cost of combining everyone’s work.

The official Continuous Delivery framing is different. _Continuous Delivery_ (CD) is the ability to get changes of all types, including features, configuration changes, bug fixes, and experiments, into production or into users’ hands safely, quickly, and sustainably. Its goal is to make software release predictable, routine, and available on demand.

Those two definitions are related, but they are not interchangeable. _Continuous Integration_ (CI) is about keeping the shared codebase continuously integrated. _Continuous Delivery_ (CD) is about keeping the product continuously releasable. Those are different promises, and when we merge them into one phrase, we often lose the ability to see which promise is being broken.

That is why “CI/CD” is a weak mental model. It gives a single name to several different capabilities, then makes the team diagnose the whole delivery system through a foggy acronym.

[![Image 5](https://substackcdn.com/image/fetch/$s_!C3vi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabe4e80d-b130-4ce4-b541-8c822d5449f4_1024x558.png)](https://substackcdn.com/image/fetch/$s_!C3vi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabe4e80d-b130-4ce4-b541-8c822d5449f4_1024x558.png)

This is not a vocabulary argument for people who enjoy correcting terminology in meetings. The confusion has economic consequences.

When teams confuse pipelines with _Continuous Integration_ (CI), integration debt accumulates silently. Every hour a branch lives away from the mainline is an hour where assumptions can diverge. The cost does not always show up immediately. It compounds quietly until merge time, when the team pays in conflicts, broken tests, duplicated work, delayed feedback, rework, and fragile compromises.

Long-lived branches are inventory. They contain work that has consumed investment but has not yet been integrated into the shared product reality. Like any inventory, they carry risk. They may become obsolete, conflict with other work, hide defects, create coordination cost, or delay learning.

_Continuous Integration_ (CI) changes that economic equation by reducing batch size and shortening the feedback loop between private work and shared reality.

When teams confuse deployment pipelines with _Continuous Delivery_ (CD), release risk accumulates. The team may continue building features, but unreleased software produces no user value. It cannot validate assumptions, generate revenue, reduce customer pain, or teach the organisation whether the investment was worthwhile.

A slow release process turns finished work into trapped capital. The organisation has paid to build it, but cannot use it freely.

This is where _Continuous Delivery_ (CD) creates option value. If a change is releasable on demand, the business has more strategic freedom. It can release now, wait, canary, coordinate with a customer, hide functionality behind a feature flag, respond to a defect, or delay exposure without delaying readiness.

That distinction is subtle but powerful. _Continuous Delivery_ (CD) does not force constant release. It creates the option to release.

Options have value under uncertainty. When the market changes, a defect appears, a customer asks for something, or a competitor moves, the organisation with a safe release capability has more room to manoeuvre. The organisation without it has to negotiate with its own delivery process before it can respond.

The old question “Do we have CI/CD?” is too weak. Better questions expose cost, risk, liquidity, and optionality:

1.   How expensive is integration?

2.   How long does work remain unintegrated?

3.   How quickly do developers receive trustworthy feedback?

4.   How much unreleased work is accumulating?

5.   How risky is a normal release?

6.   Can we release during business hours without drama?

7.   Can the business choose release timing, or does the release process choose for us?  
That is where the real conversation starts.

[![Image 6](https://substackcdn.com/image/fetch/$s_!BBy-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c020bdc-71e9-4ea9-872f-c8e31f61eb39_1024x558.png)](https://substackcdn.com/image/fetch/$s_!BBy-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c020bdc-71e9-4ea9-872f-c8e31f61eb39_1024x558.png)

_Continuous Integration_ (CI) is not a server. It is not a tool. It is not the name of the first stage in a deployment pipeline. It is not “the thing that runs tests when I open a pull request.” _Continuous Integration_ (CI) is a working agreement between developers.

It says: we will not allow our work to drift away from each other for long. We will integrate small changes frequently into a shared mainline. We will use automation to detect problems quickly. When the shared codebase breaks, we will treat that as a team problem, not as background noise.

The important word is not “continuous.” The important word is “integration.”

Integration is the moment where private assumptions meet shared reality. My code meets your code. My refactoring meets your feature. My migration meets your query. My dependency update meets your build. My “small harmless change” meets the rest of the system. _Continuous Integration_ (CI) reduces the distance between those moments.

Humble and Farley describe _Continuous Integration_ (CI) as a practice supported by version control, automated builds, automated tests, regular check-ins to trunk, and a team norm of keeping the build working. Their description makes one thing clear: the build server matters, but it is not the practice by itself.

Paul Hammant’s work on trunk-based development sharpens this point. Trunk-based development is a strategy in which developers collaborate on a single shared branch called trunk, resisting long-lived development branches. Hammant presents it as a key enabler of _Continuous Integration_ (CI) because developers committing to trunk once or multiple times per day makes the core requirement of CI possible.

DORA expresses the same relationship in modern capability language: trunk-based development is required for _Continuous Integration_ (CI), and CI combines trunk-based development with fast automated tests that run after each commit to trunk to keep the system working.

That means CI has three structures:

1.   **A social structure:** shared ownership of the mainline. Developers do not disappear into private caves of work for a week and then throw a merge problem over the wall. The team cares about the state of the shared codebase because everyone depends on it

2.   **A technical structure:** a mainline, a build, and a test suite that can provide useful feedback quickly. The details vary by context, but the shape is stable: small changes, integrated frequently, verified automatically

3.   **A feedback structure:** immediacy. When integration breaks, the team knows quickly enough to fix it while the change is still fresh in someone’s head. The longer feedback takes, the more expensive the correction becomes  
A team practicing CI is not merely asking, “Did the build pass?” It is asking whether developers integrate into the shared codebase frequently, whether branches are short-lived enough to avoid hidden divergence, whether every integration receives fast and useful automated feedback, whether the team stops and repairs the shared state when it breaks, and whether the mainline is treated as a living product asset rather than a dumping ground.

This is why _Continuous Integration_ (CI) is so often claimed and so rarely practiced well. The tool is easy to install. The discipline is harder.

[![Image 7](https://substackcdn.com/image/fetch/$s_!iwvY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49c8a575-9688-4c9a-b50b-b60750e5694c_1024x559.png)](https://substackcdn.com/image/fetch/$s_!iwvY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49c8a575-9688-4c9a-b50b-b60750e5694c_1024x559.png)

It is useful to say what _Continuous Integration_ (CI) is not, but listing tools is not enough. The real problem is not Jenkins, GitHub Actions, GitLab CI, Azure Pipelines, CircleCI, Buildkite, TeamCity, or GoCD. Those tools can support CI. They simply cannot create CI alone.

The common impostors fall into four categories.

A team can install a CI server and still not practice _Continuous Integration_ (CI). The server may run builds, tests, linters, package jobs, container builds, security scans, and deployment jobs, but if developers keep their work isolated for long periods, integration is still delayed.

The pipeline may be continuous. The integration is not.

A branch can be green while the system is not integrated. This is especially common in pull request workflows. A pull request may pass all checks while the mainline keeps moving underneath it. Several branches may each be green in isolation while being incompatible together.

Pull requests do not kill CI. Long-lived, slow-moving, isolated pull requests do.

Short-lived branches can be compatible with CI when the team keeps changes small, reviews quickly, integrates frequently, and treats the mainline as the real shared product state. But when pull requests become storage for unfinished work, CI has already been weakened. The team is not continuously integrating. It is continuously accumulating unintegrated work behind a review gate.

Running tests is necessary, but not sufficient. If tests run against isolated branches that live too long, the team may have automated confidence in the wrong thing. The tests tell us that the branch is internally coherent. They do not necessarily tell us that the team’s work is continuously integrated.

Nightly builds have the same problem. They can reveal issues, and they may be better than chaos, but they delay the pain. CI is designed to bring pain forward. If integration hurts, the answer is not to postpone the pain until night. The answer is to integrate more frequently, reduce batch size, and make the pain smaller.

A green badge is a signal. It is not a culture. It does not tell us whether the team works in small batches, whether broken builds are treated seriously, whether developers wait for feedback, whether tests are reliable, or whether the mainline can be trusted.

_Continuous Integration_ (CI) is not a ceremony around code. It is a way of keeping the team’s reality close to the code’s reality.

[![Image 8](https://substackcdn.com/image/fetch/$s_!YcHR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1dd86e84-d467-4daa-99e0-b2f922fd3950_1024x558.png)](https://substackcdn.com/image/fetch/$s_!YcHR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1dd86e84-d467-4daa-99e0-b2f922fd3950_1024x558.png)

_Continuous Delivery_ (CD) starts from a different pain. The pain is not only that developers integrate late. The pain is that software can be “done” in development and still not be usable by customers. It can be coded, reviewed, tested locally, merged, and built, yet still sit behind a release process that is fragile, manual, political, risky, and slow.

That gap is the last mile.

In the foreword to _Continuous Delivery_, Martin Fowler describes CI as the foundation that keeps the development team in sync, then explains that successfully integrated code is still not production software. The book picks up the story from CI and deals with the “last mile,” showing how a deployment pipeline turns integrated code into production software.

_Continuous Delivery_ (CD) is the discipline of making that last mile boring. Not careless, uncontrolled, or reckless. Boring in the best possible sense: repeatable, visible, practiced, and understood.

A change should be able to move from version control toward production through a repeatable, visible, automated, evidence-producing process. The team should know which version is where, what has passed, what has failed, which risks remain, and whether the change is a viable release candidate.

Humble and Farley frame the goal as making the path from idea to business value shorter and safer by creating a reliable, predictable, visible, largely automated process with understood risks. DORA defines _Continuous Delivery_ (CD) as the ability to release changes of all kinds on demand quickly, safely, and sustainably. Teams practicing it well can release in a low-risk way at any time, including during normal business hours, without disrupting users.

That phrase “on demand” matters.

_Continuous Delivery_ (CD) does not mean every change must be released immediately. It means every validated change is releasable when the business chooses to release it. The decision to release becomes a product and business decision, not a hostage negotiation with the deployment process.

This is where many teams confuse _Continuous Delivery_ (CD) with _Continuous Deployment_. Continuous Deployment means every good build is released to users automatically. Humble described Continuous Deployment as the practice of releasing every good build to users, while also noting that “continuous release” would have been a more accurate name.

_Continuous Delivery_ (CD) is different. In CD, the system is kept in a releasable state. The release decision may still be manual. The business may choose when to expose a feature. Compliance, marketing, customer readiness, migration timing, or operational context may influence the decision. But the software delivery system does not make release terrifying.

The release button may exist. The important thing is that pressing it is not an act of faith.

[![Image 9](https://substackcdn.com/image/fetch/$s_!92BD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd803bc7b-db42-489b-8705-515bad305e62_1024x558.png)](https://substackcdn.com/image/fetch/$s_!92BD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd803bc7b-db42-489b-8705-515bad305e62_1024x558.png)

A lot of confusion around _Continuous Delivery_ (CD) comes from treating deployment and release as the same thing. They are related, but they are not identical.

A deployment is a technical act: putting a version of the software into an environment. That environment may be development, test, staging, pre-production, production, or a subset of production infrastructure.

A release is a product or business act: exposing a capability to users. A feature can be deployed but not released if it is hidden behind a feature flag, unavailable to a customer segment, or disabled by configuration. A feature can also be released gradually through canaries, beta cohorts, internal users, contractual availability, or regional rollout.

This distinction matters because _Continuous Delivery_ (CD) is not merely deployment automation. Deployment automation is part of the delivery system, but CD is the broader capability of keeping validated changes releasable on demand.

That leads to three common confusions:

1.   **“We deploy to staging, so we do CD.”** Staging deployments can be useful, but they do not prove release readiness. If production still requires manual fixing, freeze windows, special coordination, or one person’s private knowledge, delivery is not continuous

2.   **“We have approval gates, so our release process is controlled.”** Approval gates can serve governance, compliance, risk management, and coordination. But a gate is not delivery. A gate can decide whether a change may pass. It cannot, by itself, make deployments reliable, environments reproducible, tests meaningful, rollback understood, release candidates traceable, or work small enough to be safe

3.   **“We release often, so we do CD.”** Release frequency is an outcome, not the whole practice. A team could release often in a chaotic way, relying on heroics, weak testing, and luck. Another team might release less frequently for business reasons while still keeping every validated change releasable on demand  
The more precise test is not “How often did we release last month?” The more revealing test is: **Could we release this validated change safely now if the business wanted it?**

That question separates release capability from deployment theatre.

[![Image 10](https://substackcdn.com/image/fetch/$s_!H35R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed3f2297-0f9a-4183-a4c2-813975f04b08_1024x558.png)](https://substackcdn.com/image/fetch/$s_!H35R!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed3f2297-0f9a-4183-a4c2-813975f04b08_1024x558.png)

The deployment pipeline is the bridge between integrated code and releasable software. It is not CI. It is not CD. It is the mechanism that can support the journey from one to the other.

Humble and Farley describe the deployment pipeline as a process triggered by every change to configuration, source code, environment, or data. The pipeline creates binaries and installers, then runs tests to show whether those binaries can be released. Each test passed by the release candidate increases confidence that this combination of code, configuration, environment, and data will work.

That point prevents a simplistic view of delivery. The thing we release is not just “code.” We release a combination of code, configuration, infrastructure, data assumptions, dependencies, operational procedures, and user-visible behaviour. A deployment pipeline makes that combination visible and testable.

Humble and Farley describe three aims of the deployment pipeline:

1.   **Make the process visible:** everyone involved in building, deploying, testing, and releasing software can see where a change is and what has happened to it

2.   **Improve feedback:** problems are identified and resolved as early as possible, when they are cheaper and easier to understand

3.   **Enable controlled release movement:** teams can deploy and release any version of the software to any environment through an automated process  
This is why the pipeline is valuable. It turns delivery from folklore into a system. Without a pipeline, release knowledge often lives in people’s heads, shell histories, old tickets, wiki pages, private scripts, and anxious rituals. With a good pipeline, the release path becomes executable knowledge. It becomes visible, repeatable, and improvable.

But the pipeline remains a means. If the team integrates late, the pipeline receives large, risky chunks of work. If the tests are slow and flaky, the pipeline produces noise. If environments are inconsistent, the pipeline provides false comfort. If deployments need manual repair, the pipeline becomes a decorative front door to a broken house. If approval gates exist mainly to compensate for low trust, the pipeline becomes bureaucracy with better icons.

The pipeline is powerful because it makes the system visible. Once the system is visible, it becomes harder to lie to ourselves.

Quality gates are seductive because they look like control. A code quality gate can reject complexity. A security gate can reject vulnerable dependencies. A test gate can reject failing builds. An architecture gate can reject forbidden dependencies. A performance gate can reject unacceptable latency. A manual approval gate can stop a release candidate before production.

All of that can be useful. Gates are not bad. Gates become useful when they create meaningful feedback, protect important constraints, and support controlled promotion through the delivery system.

But gates are not practices. Gates are checks.

A gate can tell you that a release candidate failed a condition. It cannot tell you that the team is working in a way that produces small, safe, integrated, releasable changes. This is the difference between inspection and capability.

Inspection asks whether this thing passed the gate. Capability asks whether this system can repeatedly produce good outcomes under normal conditions.

A team can add more and more gates while becoming slower, more fragmented, and less capable. Each gate may be locally rational. Security wants safety. Architecture wants consistency. QA wants confidence. Operations wants stability. Management wants approval. The result can still be a delivery system where every change queues behind accumulated anxiety.

From a systems perspective, this is a classic local optimisation trap:

1.   If the constraint is late integration, adding a deployment approval gate does not solve it

2.   If the constraint is unreliable environments, adding a code coverage threshold does not solve it

3.   If the constraint is large batch size, adding more reviewers does not solve it

4.   If the constraint is a fragile release process, adding another staging sign-off may only move the stress upstream  
Quality gates can protect the system, but they can also become a place where the organisation hides fear. The more fear we have, the more gates we add. The more gates we add, the slower feedback becomes. The slower feedback becomes, the larger the batches become. The larger the batches become, the more frightening releases become. Then the organisation adds another gate.

That loop feels responsible from the inside. From the outside, it is release risk manufacturing itself.

_Continuous Integration_ (CI) and _Continuous Delivery_ (CD) break that loop differently. CI reduces the cost of integration by making integration frequent, small, and visible. CD reduces the cost of release by making deployment and release preparation repeatable, automated, and routine. Gates may support those aims, but they do not replace them.

A gate is a checkpoint. A practice is a way of working. A capability is what the system can reliably do. Confusing those three is how organisations buy tools and keep the same pain.

[![Image 11](https://substackcdn.com/image/fetch/$s_!xcbZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F700afa72-fd22-466a-bcf6-ad5206fab873_1024x558.png)](https://substackcdn.com/image/fetch/$s_!xcbZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F700afa72-fd22-466a-bcf6-ad5206fab873_1024x558.png)

_Continuous Integration_ (CI) and _Continuous Delivery_ (CD) are often adjacent. They reinforce each other. A strong CI practice makes CD easier because the deployment pipeline starts from a healthier mainline. A strong CD practice makes CI more valuable because integrated changes can move toward users quickly and safely.

But they are still different concepts with different feedback loops.

_Continuous Integration_ (CI) asks: **Can developers combine their work safely and frequently?**

_Continuous Delivery_ (CD) asks: **Can the organisation release validated changes safely and on demand?**

One operates primarily around the shared codebase. The other operates across the delivery path to users. One reduces integration uncertainty. The other reduces release uncertainty.

CI is about the team discovering code conflicts, design conflicts, test failures, and behavioural incompatibilities quickly. CD is about the organisation discovering release risks, environment problems, configuration issues, acceptance failures, operational concerns, and deployment problems early enough to act.

When we glue them together as “CI/CD,” we lose diagnostic power. Imagine a team says, “Our CI/CD is slow.” That sentence may be true, but it is not yet useful. It could mean developers wait too long for commit feedback. It could mean pull requests are too large. It could mean builds are slow, tests are flaky, acceptance suites take hours, deployment scripts are fragile, staging environments are scarce, approvals wait for a manager, production deployment is manual, or release decisions are blocked by business coordination.

Each of those problems lives in a different part of the system. Calling all of it “CI/CD” is like telling a doctor, “My body hurts.” It may be honest, but it does not yet diagnose anything.

The language matters because diagnosis matters. If integration is broken, improve integration. If delivery is broken, improve delivery. If the pipeline is broken, improve the pipeline. If governance is slow because trust is low, do not pretend YAML will fix it.

[![Image 12](https://substackcdn.com/image/fetch/$s_!N3gB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4201357a-4fde-419e-b983-06510f7fa14c_1024x558.png)](https://substackcdn.com/image/fetch/$s_!N3gB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4201357a-4fde-419e-b983-06510f7fa14c_1024x558.png)

A team does not need a perfect score to improve. But it does need honest language. The following diagnostic helps separate tool adoption from actual practice.

Claim What to check Warning sign “We do CI.” Developers integrate to trunk or mainline at least daily. Branches live for days or weeks. “Our pipeline is green.” Mainline is healthy, not only isolated branches. Green pull requests still produce painful merges. “Our tests run automatically.” Feedback is fast, trusted, and acted on. Broken builds are ignored or normalised. “We use pull requests.” Reviews are fast and changes are small. Pull requests become storage for unfinished work. “We do CD.” Validated changes are releasable on demand. Releases require freeze windows, heroics, or exceptional coordination. “We deploy to staging.” Staging increases confidence in production release. Production still needs manual fixing or special knowledge. “We have quality gates.” Gates create meaningful feedback and controlled promotion. Gates create waiting without confidence. “We deploy often.” Deployment is routine, repeatable, and low-risk. Deployment frequency depends on specific people. “We are done.” The change is releasable or already released according to the team’s definition of done. Merged work accumulates but cannot safely reach users.

This table is intentionally practical. It avoids maturity theatre. It does not ask whether a team has the right tool, badge, platform, or vendor. It asks whether the system can do the thing the term claims.

Developers integrate into trunk or mainline at least daily. Branches, if used, are short-lived and owned by one person or a pair. The build and test process gives fast feedback on integrated work. Broken builds are treated as urgent team problems. The mainline is kept in a working state. Developers trust the shared codebase enough to build on it.

Branches live for many days or weeks. Pull requests become storage for unfinished work. The team says “my branch is green” more often than “main is healthy.” Integration problems appear late. Developers avoid updating from mainline because it is painful. Broken builds are tolerated. The CI server exists, but integration is still delayed.

Every change that reaches the mainline can flow through an automated deployment pipeline. Release candidates are traceable. Deployments are repeatable. Environments are managed consistently. Tests provide useful confidence at different levels. People can deploy to required environments without secret knowledge. The team can release a validated change on demand in a low-risk way.

Releases require exceptional coordination. Deployments depend on manual steps that only a few people understand. Production differs mysteriously from test environments. Release candidates cannot be traced clearly to source changes. Staging deployments work but production still feels dangerous. Approval gates compensate for low confidence. The team delays release because the process itself is scary.

A change can move through build, test, packaging, deployment, verification, and promotion stages in a visible and repeatable way. The pipeline shows which release candidates passed which checks. It helps people select, promote, and deploy known versions. It makes delivery work visible enough to improve.

[![Image 13](https://substackcdn.com/image/fetch/$s_!96mo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd79dd59-1d6a-4794-a6bd-59c11e35cefa_2412x1676.png)](https://substackcdn.com/image/fetch/$s_!96mo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd79dd59-1d6a-4794-a6bd-59c11e35cefa_2412x1676.png)

The pipeline exists mainly to produce status signals. It runs checks, but nobody trusts them. It deploys somewhere, but not in a way that reduces production risk. It contains gates, but the gates do not map to meaningful confidence. It creates waiting time without creating learning. It looks like control, but the team still needs heroics.

The real theory could look something like this

[![Image 14](https://substackcdn.com/image/fetch/$s_!YnWp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7016d023-6ee7-4539-9f7d-ea0469a83167_763x2132.png)](https://substackcdn.com/image/fetch/$s_!YnWp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7016d023-6ee7-4539-9f7d-ea0469a83167_763x2132.png)

For me with my experience is more like this.

[![Image 15](https://substackcdn.com/image/fetch/$s_!Pjld!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7eab0704-c91a-43b2-bf3b-365f062a04ad_763x2132.png)](https://substackcdn.com/image/fetch/$s_!Pjld!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7eab0704-c91a-43b2-bf3b-365f062a04ad_763x2132.png)

[![Image 16](https://substackcdn.com/image/fetch/$s_!5LcE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48946c57-4368-40d7-a741-d36562df9a1b_1191x1772.png)](https://substackcdn.com/image/fetch/$s_!5LcE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48946c57-4368-40d7-a741-d36562df9a1b_1191x1772.png)

[![Image 17](https://substackcdn.com/image/fetch/$s_!SBLP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6252f261-7e49-4f4e-b567-636b10114173_1278x1020.png)](https://substackcdn.com/image/fetch/$s_!SBLP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6252f261-7e49-4f4e-b567-636b10114173_1278x1020.png)

The industry did not start saying “CI/CD” because people were foolish. It happened because the phrase was convenient. It grouped related tools, related workflows, and related aspirations under one label. But convenience becomes expensive when it weakens thought.

_Continuous Integration_ (CI) and _Continuous Delivery_ (CD) are connected, but they are not the same thing. CI is about integrating developer work into a shared codebase frequently and safely. CD is about making validated changes releasable on demand safely and sustainably. A deployment pipeline can support both, but it does not prove either.

This distinction is not pedantry. It is diagnosis.

If a team has late merges, painful conflicts, long-lived branches, and a mainline nobody trusts, the problem is not solved by adding a deployment stage. The team has an integration problem. If a team has green builds, merged code, and tested artifacts, but releases still require freeze windows, manual scripts, anxious approvals, and a person named Alex who “knows the production thing,” the problem is not solved by saying the pipeline passed. The team has a delivery problem.

If a team has many gates but little confidence, the problem may be that the gates are compensating for a weak system. More inspection is not the same as more capability.

Stop asking whether you have CI/CD. Ask whether your team integrates continuously, whether validated changes are releasable on demand, and whether your pipeline creates real confidence or only records that some checks ran.

The answer to those questions will tell you far more than any green badge.

*   Fowler, Martin. _Continuous Integration_. [https://www.martinfowler.com/articles/continuousIntegration.html](https://www.martinfowler.com/articles/continuousIntegration.html)

*   Fowler, Martin. _Continuous Delivery_. [https://martinfowler.com/bliki/ContinuousDelivery.html](https://martinfowler.com/bliki/ContinuousDelivery.html)

*   Fowler, Martin. _Deployment Pipeline_. [https://martinfowler.com/bliki/DeploymentPipeline.html](https://martinfowler.com/bliki/DeploymentPipeline.html)

*   Google Cloud DORA. _Continuous Integration_. [https://dora.dev/capabilities/continuous-integration/](https://dora.dev/capabilities/continuous-integration/)

*   Google Cloud DORA. _Continuous Delivery_. [https://dora.dev/capabilities/continuous-delivery/](https://dora.dev/capabilities/continuous-delivery/)

*   Google Cloud DORA. _Trunk-Based Development_. [https://dora.dev/capabilities/trunk-based-development/](https://dora.dev/capabilities/trunk-based-development/)

*   Google Cloud DORA. _Working in Small Batches_. [https://dora.dev/capabilities/working-in-small-batches/](https://dora.dev/capabilities/working-in-small-batches/)

*   Hammant, Paul. _Trunk-Based Development and Branch By Abstraction_. Leanpub, 2020. [https://leanpub.com/trunk-based-development](https://leanpub.com/trunk-based-development)

*   Humble, Jez. _What is Continuous Delivery?_[https://continuousdelivery.com/](https://continuousdelivery.com/)

*   Humble, Jez. _Continuous Delivery vs Continuous Deployment_. [https://continuousdelivery.com/2010/08/continuous-delivery-vs-continuous-deployment/](https://continuousdelivery.com/2010/08/continuous-delivery-vs-continuous-deployment/)

*   Humble, Jez, Farley, David. _Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation_. Addison-Wesley, 2010
