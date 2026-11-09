Title: Parallel Change: how to evolve live systems without breaking consumers

URL Source: http://emmanuelvalverderamos.substack.com/p/parallel-change-how-to-evolve-live

Final URL: https://emmanuelvalverderamos.substack.com/p/parallel-change-how-to-evolve-live

Published Time: 2026-06-09T05:00:39+00:00

Markdown Content:
A `users` table has a `full_name` column. Product wants `first_name` and `last_name`. The table has two million rows. Writes are happening every second. Several parts of the system read the column. A mobile app depends on the API, and your team does not control when that app reaches its users. There is no maintenance window, no quiet deployment slot, and no moment where every consumer will stop long enough for you to change the shape in peace.

In isolation, the technical change looks small. In production, it does not. The backlog item stays open not because nobody understands the benefit, but because the path to the benefit looks risky. Separate first and last name fields are easier to validate, sort, display, and reason about than a single overloaded string. But the system around that change makes the obvious implementation feel dangerous.

That fear is healthy. Engineers have seen systems break when too many consumers had to move together. They have seen changes that looked small cause incidents because the real problem was never the code in isolation. The real problem was the coordination burden hiding around it.

The fear is rational. The risk is real. What is irrational is the assumption underneath the fear: that the change has to happen all at once.

Most engineers first learn to make changes in a simple world: one codebase, one runtime, one schema, one team, one deployment. In that world, a breaking change often feels atomic. You update the code, run the tests, deploy once, and the system moves cleanly from the old shape to the new one.

That mental model breaks as soon as the system stops being truly atomic in production. Multiple consumers moving at different speeds are one reason. But the same failure appears when old and new binaries coexist during a rolling deployment, when persistent data outlives the code that writes it, when traffic moves gradually through a flag or canary, or when an infrastructure dependency must be replaced while releases continue. The interface may be a constructor signature, a table schema, an API response, a message payload, or a whole application boundary.

This is why trunk-based development changes the conversation. Trunk-based development is the practice of integrating all changes directly into the main branch of the repository continuously, without long-lived feature branches. The goal is that the build is always green and that any commit on trunk is deployable at any moment. If your team works this way, every step of a change must be a commit that breaks nothing, because any other engineer can deploy trunk at any time. That constraint is not a burden. It is a forcing function that makes the hidden assumption visible.

The dangerous assumption is not “this change has risk.” That part is true. The dangerous assumption is “every consumer has to move together.” In real systems there is rarely one clean instant where before ends and after begins. For a while, both are true. Some consumers are on the last deployment, some are on the current one, some data was written before the migration logic existed, and some will be written after the migration has completed.

The system is not switching states. It is moving through states. The right question is not “when can we do this all at once?” The right question is “what sequence of safe intermediate states gets us from here to there?”

[![Image 1](https://substackcdn.com/image/fetch/$s_!PI36!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd6d52ac-100d-42bb-8499-d237a488f9fc_1672x941.png)](https://substackcdn.com/image/fetch/$s_!PI36!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd6d52ac-100d-42bb-8499-d237a488f9fc_1672x941.png)

Parallel Change is a way to evolve a contract without forcing every dependent part of the system to adopt the new shape immediately. It is also known as Expand and Contract, a term that comes from the world of database evolution. “Expand” refers to the act of adding without removing. “Contract” refers to the act of removing once nothing depends on what was added. The name “Parallel Change” emphasises that the two states coexist during the migrate phase: the system runs with the old and new interfaces both active at the same time.

The pattern breaks any backward-incompatible change into three phases: expand, migrate, and contract. Those phases reduce to two rules.

Never remove something until nothing depends on it. Never force adoption of something that does not yet exist.

Before going further, one clarification about the word “interface.” It does not mean only a method signature or a C# interface declaration. It means any surface through which two parts of a system communicate and depend on each other’s shape. A constructor parameter list is an interface. A database table is an interface. A REST endpoint is an interface. A message queue schema is an interface. Even a deployed application version can behave like an interface when two versions coexist temporarily during a rollout.

What makes these interfaces hard to evolve is not complexity in isolation. It is that the system must pass through a period where old and new shapes both exist. That period can be forced by many things: live writes that continue through a deployment, old and new binaries running side by side during a rolling update, persistent rows that were written before the migration logic existed, teams or services that deploy independently, traffic moving gradually through a feature flag, a dependency being replaced while releases continue, or a legacy module being displaced by a new one. Multiple consumers moving at different speeds are one reason. They are one item in a longer list.

[![Image 2](https://substackcdn.com/image/fetch/$s_!SJjC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b90b7c3-f0dc-45a2-8b8d-acc1c65b6150_1272x1912.png)](https://substackcdn.com/image/fetch/$s_!SJjC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b90b7c3-f0dc-45a2-8b8d-acc1c65b6150_1272x1912.png)

Once you stop seeing Parallel Change as “that database migration technique” or “that thing you do when multiple consumers exist” and start seeing it as a general discipline for safe evolution under mixed states, it becomes available in many places where teams usually attempt a risky atomic cut.

The hardest part of Parallel Change is not memorising the three phases. The hardest part is replacing a reflex.

The reflex is to begin with the target design and ask: “what do I need to change?” In a live system that question is incomplete. It hides the operational problem inside an unspoken “then we switch everything over.” Parallel Change replaces it with a better question: “what sequence of safe intermediate states gets me from the current system to the target system?”

Under the old framing, the change often becomes one large coordinated effort. Everything touching the migration is grouped into a single delivery: domain logic, persistence, migrations, API contracts, and frontend usage all at once. Reviewers have to hold the entire transformation in their heads. Deployment is fragile because several moving parts must align. Rollback is painful because reverting one part may not revert the others safely.

Under the new framing, the first good change is boring on purpose. It only adds. It cannot break anything. It can be deployed, observed, and rolled back completely independently of every subsequent step. That narrowness is not a constraint. It is the point.

There is a second shift that matters just as much, and it is less obvious. Sometimes Parallel Change is not only a way to protect the system while making a change you already understand. The safe, gradual nature of the migration gives the team time and space to arrive at a better understanding of what the domain actually looks like. An inheritance hierarchy that felt necessary before the migration might reveal itself as a conflation of two separate concepts once you slow down enough to see what would simplify if you split them. The migration is not just the mechanism. Sometimes it is the lens.

The corollary that engineers most often miss: the contract step is not optional. If you expand and migrate but never contract, you have not simplified the system. You have added complexity to it. The old interface still exists. New engineers do not know which path is current. Future changes need to account for both shapes. Schedule the contract step when you open the expand change. They are one decision made at one moment, not two separate decisions made months apart.

Before the examples, it is worth being precise about what each phase is for, what it allows, and where the real operational danger appears.

[![Image 3](https://substackcdn.com/image/fetch/$s_!Eo0Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1bab3f71-59db-439f-9515-5b7bfe7cc8d3_3180x2329.png)](https://substackcdn.com/image/fetch/$s_!Eo0Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1bab3f71-59db-439f-9515-5b7bfe7cc8d3_3180x2329.png)

Expand is the safest phase because it only adds. At the end of Expand, the new shape exists but the old shape still works. Old consumers continue untouched. New consumers have somewhere safe to move. The system is deliberately more flexible than usual.

In code, Expand might mean adding a new constructor while keeping the old one delegating to it. In a database, it means adding new nullable columns while leaving the old ones intact. In an API, it means introducing `v2` while keeping `v1` alive. In a deployment, it means introducing a new implementation behind an abstraction or a flag while the existing implementation still serves traffic.

The system can be deployed at any point during Expand and continues to function correctly.

Migrate is the phase where the real movement happens. Consumers move one by one. Existing rows get backfilled. Reads switch from old fields to new fields. Frontends move to new endpoints. Services start publishing or consuming the new message shape.

This is the phase with the most variety in technique. Rather than treating all migrations the same, it helps to have a shared vocabulary for the specific mechanism in use.

**Delegation** is used when an old code-level interface needs to stay valid while a new one takes over. The old constructor or method calls the new one internally. No caller breaks. The `[Obsolete]` attribute warns without preventing compilation. This is the technique in Example 1.

**Temporary scaffolding** is used for internal refactorings, particularly in test code, where many call sites use an old interface and need time to migrate. Transitional overloads, conditional adapters, or delegating builders are introduced solely to let old and new internal interfaces coexist. The scaffolding is explicitly temporary and deleted in the contract phase. This is the technique in Example 1.5.

**Dual-write** is used when a persistent store must carry two representations of the same data during migration. Every write operation populates both the old and new fields simultaneously, keeping both read paths current regardless of which is active. This appears in Examples 2 and 4.

**Batched backfill** is used to populate existing rows with values for a new column or field structure. On a table with millions of rows, a single-transaction mass update can lock the table for minutes. Running it in batches with a short pause between each leaves room for normal production writes and avoids exhausting the database server. This appears in Examples 2 and 4.

**Feature flag with runtime switch** is used when a behaviour needs to change at runtime without a deployment. The flag controls which read path, endpoint version, or render logic is active. Changing the flag in the dashboard takes effect within the poll interval. This appears in Examples 2, 3, and 5.

**API versioning** is used when using an application contract changes in a way that breaks existing consumers. A new versioned endpoint carries the new contract. The old endpoint stays alive until all consumers have migrated. This appears in Example 3.

**Compatibility view** is used when a database table or column names need to be renamed. A SQL view exposes the new names over the old structure at zero cost. New code reads from the view. Old code reads from the table. Both hit the same underlying data. This appears in Example 4.

Two additional techniques operate at a scale above the constructor and database examples but follow the same three-phase discipline. Branch by Abstraction is a technique for replacing an infrastructure dependency while the system continues running: a stable interface is introduced between callers and the current implementation, the new implementation is built behind it, and a feature flag routes traffic between old and new until the old one can be deleted. This is the technique in Example 6. Strangler Fig is the system-level version: new functionality is built as a separate deployable alongside a legacy module, a routing layer directs traffic incrementally from old to new, and the legacy module is deleted when it has no remaining consumers. This is the technique in Example 7. The distinction between them is the location of the suture: inside the code in Branch by Abstraction, in the routing layer in Strangler Fig.

The following diagram maps every technique in this article to the type of seam it addresses:

[![Image 4](https://substackcdn.com/image/fetch/$s_!_oUS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F364ce5bd-68b5-4caf-a18c-597cf639e4b0_3594x2157.png)](https://substackcdn.com/image/fetch/$s_!_oUS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F364ce5bd-68b5-4caf-a18c-597cf639e4b0_3594x2157.png)

[![Image 5](https://substackcdn.com/image/fetch/$s_!ztO0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F665ed1e3-38d5-4a16-9aef-57d96edb5be9_1860x540.png)](https://substackcdn.com/image/fetch/$s_!ztO0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F665ed1e3-38d5-4a16-9aef-57d96edb5be9_1860x540.png)

[![Image 6](https://substackcdn.com/image/fetch/$s_!kESV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9411585d-8ac6-4001-9926-c110d4222141_3480x1773.png)](https://substackcdn.com/image/fetch/$s_!kESV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9411585d-8ac6-4001-9926-c110d4222141_3480x1773.png)

[![Image 7](https://substackcdn.com/image/fetch/$s_!3LqX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50eef6ad-4c54-43a1-97e4-6afda046c353_3484x1552.png)](https://substackcdn.com/image/fetch/$s_!3LqX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50eef6ad-4c54-43a1-97e4-6afda046c353_3484x1552.png)

Migrate contains the most important operational boundary in the whole pattern: the point of no easy return. This is the moment when rollback stops being simple.

Before that point, reverting might be as easy as disabling a flag or routing reads back to the old path. After that point, the old path may no longer be trustworthy because it has stopped receiving fresh data or because new writes are only consistent in the new structure.

A concrete database example makes this clear. Suppose a system is moving from `full_name` to `first_name` and `last_name`. During dual-write, both the old and new columns stay current, so switching reads between them is still safe. Once the team stops writing to `full_name`, the old column begins to drift. At that moment, reading from it again is no longer rollback in any meaningful sense. It returns stale data.

Name this point before you reach it. Keep the observation period before it long enough to give you genuine confidence. Do not cross it under time pressure.

Contract is the phase where the migration stops being temporary. The old constructor is deleted. The old endpoint is removed. The old column is dropped. The compatibility view disappears. The transitional flag is torn out.

Structurally, Contract is often the simplest phase. Operationally, it is the one teams neglect most. The reason is predictable: Expand and Migrate are usually attached to visible business value. Contract is not. Nothing user-facing changes when `v1` is deleted or when `full_name` finally disappears. That makes Contract easy to postpone, easy to deprioritise, and easy to abandon.

Postponing it means carrying complexity that has already outlived its purpose. Temporary compatibility code, dual-write paths, old endpoints, and migration flags all have an ongoing cost: they add cognitive load to every future engineer who reads the code and must decide whether the old path is safe to use.

The procedural fix is simple and must happen at the start: when you open the expand change, open the contract ticket at the same time. Assign it. Give it a date. The two are one decision.

Before getting into the examples, it is worth being explicit about the conventions they follow, because those conventions are part of the teaching.

When the examples use a **port** and an **adapter**, they follow the ports-and-adapters style, also called hexagonal architecture. The port is the abstraction that expresses what the application needs. The adapter is the technology-specific implementation that fulfils it. `CustomerRepository` is the port because it names a business role. `SqlServerCustomerRepository` is the adapter because it implements that role using SQL Server. There is no `I` prefix on the port because the name already says what it does.

When the examples use a **DTO**, they are using an object whose only job is transport. It exists to describe the shape of data crossing a boundary. It has no business behaviour of its own. That separation matters during migration because the transport contract is often in motion while the domain model tries to remain stable.

When the examples use a **value object**, they are modelling a concept whose identity is its value. `PostalCode`, `CountryCode`, `EmailAddress`, and `CurrencyCode` are all better represented as value objects than as raw strings because the type itself can enforce the rules that make the value meaningful. This is one way to resist **Primitive Obsession**, which is the habit of representing domain concepts with raw types like `string` or `int`. A related smell is the **Data Clump**: a group of primitives that always travel together but have no encapsulating object. A **code smell** in general is a signal that suggests a potential design problem. It is not a bug, but it often indicates that a change will be harder than it should be.

The examples also apply a few rules from **Object Calisthenics**: one level of indentation per method, no `else` after an early return, wrapped primitives, and small entities. These are not ends in themselves but heuristics that make it harder to write code with hidden complexity. The examples also follow **Interface Segregation**: no client depends on methods it does not use. `UserProfileReader` and `UserProfileWriter` are two separate interfaces because their consumers have different reasons to change.

Where the examples need database evolution, they use **FluentMigrator**, a .NET library that defines migrations as C# code. Each migration has `Up()` and `Down()`. Migrations are versioned, executed in order, and form an auditable history of schema evolution. Where the examples need SQL mapping, they use **Dapper**, a micro-ORM that maps SQL results to C# objects. You write the SQL explicitly. This predictability is exactly what is needed when the schema is in transition.

The examples vary on purpose. Some involve multiple consumers. Some involve a single application, a single team, and a single codebase. What unifies them is not the number of consumers. It is the need to move through safe intermediate states while old and new shapes coexist for a while.

Several of the examples rely on a runtime switch. That switch is not there to hide unfinished work. It is there because moving gradually is often safer than moving everything at once, and a flag that requires a deployment to change is less useful than one that does not. A live system often needs to validate a new path under real traffic before the old path can be retired, whether the old and new shapes are consumed by different clients, different live instances of the same service, or a percentage of traffic in a canary rollout.

**Autopoll** is an evaluation mode in which the SDK periodically checks whether flag values have changed, without the application restarting or receiving an external notification. With a 30-second interval, any change in the ConfigCat dashboard reaches every running instance within that interval. No commit, no pipeline, no deployment.

`dotnet add package ConfigCat.Client``npm install configcat-js`
This infrastructure is established once here and reused in each example that needs it.

[![Image 8](https://substackcdn.com/image/fetch/$s_!NYic!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d70f119-f180-4333-b5ed-d2093cf6532d_3435x1943.png)](https://substackcdn.com/image/fetch/$s_!NYic!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d70f119-f180-4333-b5ed-d2093cf6532d_3435x1943.png)

You have a class that receives six constructor parameters. Four of them always travel together: street address, city, postal code, and country code. They are validated together, displayed together, and conceptually represent one thing, but the code still treats them as four unrelated strings. Other teams use this class. You cannot update all call sites at once. How do you introduce the missing abstraction without breaking any build?

This is the problem known as a **Data Clump**: four positional `string` parameters with no encapsulating object, no centralised validation, and no type that prevents them from being passed in the wrong order. If the country must be a two-letter ISO code, that rule exists scattered across every place where an `Order` is constructed rather than in one place where it can be trusted.

The starting point:

First, introduce value objects for each domain concept:

Then introduce the encapsulating object:

Now make the new constructor canonical, while keeping the old one alive as a delegating compatibility path. The `[Obsolete]`**attribute** is the mechanism for this. In .NET, `[Obsolete]` marks a member as deprecated. The compiler emits a warning at every call site that uses it. The attribute accepts a message that can include migration instructions or a link to the tracking issue. With `error: false`, the warning does not prevent compilation. That is exactly what the migrate phase needs: the system keeps working, but every IDE warns the developer that they are using something that needs updating.

At this point, nothing breaks. Old call sites compile with a warning. New code can use `ShippingAddress` directly.

Call sites move independently:

Once every caller has moved, the old constructor and the convenience accessors are removed:

Any unmigrated call site now fails at compile time. The compiler enforces the final state. No runtime check needed, no flag, no observation period. The safety net here is the build.

The lesson here is simple: even a local refactoring becomes safer when the old and new shapes are allowed to coexist deliberately for a short time. The compiler is the cheapest possible safety net. Use it.

**There is a more complete and better example here**: [https://codesai.com/posts/2025/11/simplifying-builders-parallel-change](https://codesai.com/posts/2025/11/simplifying-builders-parallel-change)

Sometimes the problem is not a database or an API. Sometimes it is a structure inside the codebase that many tests depend on, and the difficulty is not technical but organisational: too many usages to change at once, too much noise if done in one big rewrite.

You have a test suite where builders share behaviour through inheritance. The original design uses generics to preserve fluent chaining and to restrict which methods are available on each specialised builder. It works, but it is harder to read than it should be, and over time the team starts to feel that the design is compensating for something.

Then the team realises that two concepts have been conflated. What looked like different “states” of the same entity are actually different workflow commands. Once that becomes clear, the inheritance-heavy builder design no longer makes sense. Composition becomes a better fit. But hundreds of tests still use the old builders. Rewriting all of them at once would be noisy, risky, and unnecessary.

This is where Parallel Change applies to test infrastructure, and where a new migrate-phase technique appears: **temporary scaffolding**. Temporary scaffolding is transitional code introduced solely to let old and new internal interfaces coexist while usages migrate. Unlike the final design, it is not meant to survive. It might be an overloaded method that accepts both the old and new type, a conditional adapter that routes between two implementations, or a delegating builder that can wrap either shape. Its only purpose is to keep the build green while call sites move one at a time.

This example also illustrates something worth naming explicitly: the migration process is not always just an implementation detail. Sometimes slowing down to make a change safely is what gives the team space to see the domain more clearly. The inheritance hierarchy felt necessary before the migration. Once the team stopped to plan the transition carefully, the domain conflation became visible. That insight could have been invisible if the change had been forced through in one large rewrite.

`ReadyToOpenClaim` and `OpenButNotNotifiedClaim` are not domain states in any useful sense. They are workflow commands: `OpenClaimCommand` and `NotifyOpenedClaimCommand`. `ClaimData` becomes `Claim`. The inheritance hierarchy was compensating for a conceptual conflation between an entity’s state and the commands that transition it.

Once that is clear, the target design becomes simpler: command builders compose a plain `ClaimBuilder` instead of inheriting from a generic base builder.

Introduce the new plain builder and the new composition-based command builder without deleting anything:

The `OpenClaimCommandBuilder` accepts both the new `ClaimBuilder` and the legacy `ReadyToOpenClaimBuilder` through overloaded `Of()` methods. This is the scaffolding.

The field `claimBuilder` is never null: it starts as `new ClaimBuilder()`, which acts as a Null Object. When `Of(ClaimBuilder)` is called, it replaces that default. When `Of(ReadyToOpenClaimBuilder)` is called, it adapts the legacy builder into a `ClaimBuilder` immediately, at the call site, not in `Build()`. This means `Build()` has a single unconditional path with no null checks, no branching, and no `throw`. The scaffolding is in the overload, not in the assembly step.

This is not the final design. It is scaffolding. Its purpose is narrow: let old and new builders coexist while tests move independently.

Tests move one at a time. Before:

After:

Nothing forces every test to move in one change. The scaffolding keeps everything green throughout.

Once all usages of `ReadyToOpenClaimBuilder` and `OpenButNotNotifiedClaimBuilder` are gone, delete the legacy builders, the overloaded `Of()` methods that accept them, and the conditional dispatch logic. The final `OpenClaimCommandBuilder` is clean:

The lesson is that Parallel Change is not only a technique for protecting live production systems. It applies equally well to internal structures like test builders, and the careful approach to migration is sometimes what gives the team the space to find a better design.

[![Image 9](https://substackcdn.com/image/fetch/$s_!GC88!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6be3ccf9-78de-498d-a019-50e66fd4ef21_3435x1894.png)](https://substackcdn.com/image/fetch/$s_!GC88!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6be3ccf9-78de-498d-a019-50e66fd4ef21_3435x1894.png)

A `customers` table has a `full_name` column. The business needs separate first and last name fields. You have a live system with real writes happening continuously. If you can only run one migration per deployment and cannot take a maintenance window, what is the minimum sequence of migrations that gets you to the target state without data loss?

The starting schema:

**Dual-write** is the practice of writing the same data to two locations simultaneously during a migration. Every `INSERT` and every `UPDATE` writes to `full_name`, `first_name`, and `last_name` at the same time. This guarantees that both read paths return current data regardless of which is active at any moment.

**Batched backfill** is the process of retroactively populating existing rows that were created before the new columns existed. On a table with millions of rows, a single-transaction mass `UPDATE` can lock the table for minutes and block production writes. Running it in batches of a few hundred rows, with a short pause between each batch, leaves room for the system’s normal activity.

The domain model is updated to carry the target truth from the start:

Add the new columns without removing `full_name`. The old column stays intact and reads continue working:

All writes now use dual-write:

Backfill existing rows in batches, then enforce `NOT NULL`:

Reads can now switch behind a flag:

The point of no easy return in this example is when the team stops writing to `full_name`. Up to that moment, routing reads back to the old column is still safe. After it, the old column goes stale and returning to it is no longer rollback. It is returning incorrect data.

Enable the flag for a small percentage of traffic first. Validate that the split reads produce correct results. Then widen the rollout. Cross the point of no easy return only after the new path has proved trustworthy in production.

The repository now has a single read path. Remove the flag check and the legacy query:

[![Image 10](https://substackcdn.com/image/fetch/$s_!rXbv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a1d1353-960e-4438-b530-3c4a3a2acbe4_432x1940.png)](https://substackcdn.com/image/fetch/$s_!rXbv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a1d1353-960e-4438-b530-3c4a3a2acbe4_432x1940.png)

The real trick is not adding two columns. The real trick is maintaining trust in both shapes while the system passes through the transition, and knowing exactly when that trust no longer goes in both directions.

[![Image 11](https://substackcdn.com/image/fetch/$s_!yokR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e952142-d8a3-4134-ac25-d27036ec146c_3435x1857.png)](https://substackcdn.com/image/fetch/$s_!yokR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e952142-d8a3-4134-ac25-d27036ec146c_3435x1857.png)

Your BFF exposes

The Vue frontend uses it. A mobile app also uses it. The mobile team tells you they can migrate in six weeks. You need `firstName` and `lastName` in the database and in the API response. The change to the response shape is a breaking change: the old field disappears in the new contract. The old contract must remain alive for the mobile app. The frontend and the backend deploy independently. When is the old contract safe to delete? Who decides? How do you prevent the old endpoint from living in the codebase forever with nobody accountable for removing it?

A **Backend for Frontend**, or BFF, is a backend service designed specifically to serve the needs of a particular user interface. Instead of a generic API consumed by multiple clients, the BFF adapts data to the exact contract the frontend needs: the shape of the objects, the fields it includes, the level of aggregation.

**API versioning** means maintaining two distinct routes that expose different contracts for the same resource. Version 1 honours the old contract. Version 2 exposes the new one. No consumer is forced to migrate. The old contract does not disappear until nothing depends on it.

The database layer follows the same three-migration sequence as Example 2. By the time the API changes are deployed, `first_name` and `last_name` are already present and backfilled. The BFF always reads split fields. The `v1` endpoint computes `fullName` from them.

The domain model and the two DTOs:

The controller serves both versions from the same domain model:

At this point, nothing breaks. Mobile keeps consuming `v1`. New clients can use `v2` immediately.

The flag and the composable on the Vue side:

Enable the flag in the ConfigCat dashboard. The Vue frontend moves to `v2`. The mobile app keeps calling `v1`. Both receive correct data. No coordinated deployment needed.

When the mobile team confirms their migration is complete, delete the `v1` endpoints. Update the request DTO to accept only the new shape. Remove the flag check from the composable. Remove the `v-else` branch from the component.

A note on accountability: when `v2` is created, open the contract ticket at the same time. Assign it. Date it to the mobile team’s six-week timeline. Without this step, `v1` lives in the codebase indefinitely, nobody knows whether anything still depends on it, and removing it becomes progressively harder to justify in a sprint.

[![Image 12](https://substackcdn.com/image/fetch/$s_!5OJA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e6dc33b-2779-452c-926e-e6c48fb57b34_1962x1734.png)](https://substackcdn.com/image/fetch/$s_!5OJA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e6dc33b-2779-452c-926e-e6c48fb57b34_1962x1734.png)

Versioning is a bridge, not a destination. The value it creates is time. That time belongs to the mobile team, not to the endpoint.

You have a table named `benutzer` with columns in German: `vorname`, `nachname`, `strasse`, `ort`, `postleitzahl`, `erstellt_am`. Three applications read from it. None of them share a deployment cycle. You want to rename everything to English. You cannot lock the table. You cannot ask the three applications to deploy on the same day. How do you rename a database table without coordination?

A **compatibility view** is a SQL view created during a migration that exposes new column names over the old table structure. New code reads from the view with English names. Old code reads from the table with German names. Both access the same underlying data without duplication. It is the cheapest possible expand mechanism for a rename because it involves no data copying and no schema alteration, only a view definition.

`sp_rename` is a SQL Server stored procedure for renaming database objects at runtime. Renaming a table with `sp_rename` does not require recreating it or copying data. It is a metadata operation and takes effect immediately. It is used in the contract phase to perform the real rename after nothing depends on the old name.

The starting schema:

Create the compatibility view. New code reads from it immediately:

Old applications keep reading from `benutzer` unchanged. New code reads from `users` with English names. Both hit the same rows.

Add English columns alongside the German ones:

Backfill and enforce `NOT NULL`:

All inserts and updates now use dual-write: writing to both German and English columns simultaneously.

Once nothing depends on the German names, drop the compatibility view, drop the German columns, and execute the real rename:

The `Down()` throws `NotSupportedException`. This is not laziness. It is an honest statement: once the table is renamed, reversing that change with code is dangerous because views, stored procedures, and indexes may all reference the new name. The only safe rollback at this point is a database restore. Documenting this explicitly is more useful than a `Down()` that silently leaves the schema in an inconsistent state.

![Image 13](https://substackcdn.com/image/fetch/$s_!YPRP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3452014f-7865-4f90-bd77-5685463468b8_2129x236.png)

The lesson is that the safest way to rename something is often not to rename it first. It is to create a stable compatible surface, let everything migrate to it, and only then perform the real rename when nothing depends on the old name.

[![Image 14](https://substackcdn.com/image/fetch/$s_!l3Jo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F779faf9f-f59f-4f0e-a5f1-c5a054b4bc4a_3435x2001.png)](https://substackcdn.com/image/fetch/$s_!l3Jo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F779faf9f-f59f-4f0e-a5f1-c5a054b4bc4a_3435x2001.png)

Your product card renders `$ price.toFixed(2)`. The backend returns a plain decimal. The business now needs to support EUR, GBP, and JPY. Each currency has different formatting rules. The database has no currency column. The frontend and backend teams deploy on different cycles. If you ship the backend change before the frontend is ready to use the new fields, the old `price` field must still be present in the response. If you ship the frontend change before the backend provides a currency code, it has nothing to format with. What is the order? What does the API response look like during migrate? What gets deleted in contract?

**ISO 4217** is the international standard that defines three-letter codes for currencies: `USD` for the US dollar, `EUR` for the euro, `GBP` for the pound sterling, `JPY` for the Japanese yen. Using the standard instead of a free `string` guarantees interoperability with any payments API or formatting library. The `CurrencyCode` value object encapsulates this validation: if the code is not exactly three characters, the object cannot be constructed.

`Intl.NumberFormat` is the native JavaScript API for formatting numbers according to the regional conventions of a locale. With `{ style: 'currency', currency: 'EUR' }` and locale `es-ES`, it formats `89.99` as `89,99 €`. With the same value and locale `en-IE`, it produces `€89.99`. With `1000` and `{ currency: 'JPY' }` in `ja-JP`, it produces `¥1,000`. The formatting is handled by the browser and requires no third-party library.

Add the currency column with a default that makes existing rows immediately valid:

The domain model:

The response DTO carries both the old and new shapes simultaneously. Old consumers read `Price`. New consumers read `Amount` and `CurrencyCode`:

The frontend flag and the currency formatter composable:

The product card composable bridges both shapes behind the flag:

Enable the flag for a subset of users. Validate formatting per locale: `es-ES`, `en-IE`, `ja-JP`. Widen the rollout after each locale validates correctly.

Remove `Price` from the backend DTO. Remove `price` from the TypeScript type. Remove the flag branch from the composable. The composable has one path:

[![Image 15](https://substackcdn.com/image/fetch/$s_!8G2E!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F067357c3-2941-48ee-a4d6-db1661701644_1860x1676.png)](https://substackcdn.com/image/fetch/$s_!8G2E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F067357c3-2941-48ee-a4d6-db1661701644_1860x1676.png)

The migration is complete only when both the old shape and the old behaviour have disappeared from every layer.

Your system sends transactional emails through a direct dependency on `SmtpEmailSender`. The SMTP provider is being retired. You need to replace it with `SendGridEmailSender`. The system sends emails continuously. You cannot stop it to do the swap, and you cannot afford to find out at midnight that the new provider behaves differently in production than it did in staging.

A direct replacement would mean changing every class that depends on `SmtpEmailSender` and deploying with no safety net. If the new provider has a configuration problem or a quota behaviour you did not expect, the rollback is a full redeployment.

Branch by Abstraction solves this differently. The suture point is an interface introduced between the callers and the implementation. That interface exists before the new implementation does. Once it exists, the old and new implementations can coexist behind it, and a feature flag controls which one is active. Rollback is disabling a flag, not reverting a deployment.

This is the key distinction from Example 1 (delegation): in delegation, you change the shape of a single member and keep callers working via a forwarding path. In Branch by Abstraction, you replace an entire dependency that callers couple to directly, and the abstraction is the stable surface they couple to instead.

The notification service depends directly on the concrete implementation:

Introduce the port. Make `SmtpEmailSender` implement it. Change `NotificationService` to depend on the port instead of the concrete class. Deploy. Nothing changes behaviourally. The abstraction now exists as a stable surface:

Build the new implementation. Then introduce a routing adapter that uses the feature flag to decide which implementation to call. The flag controls which provider handles traffic. `NotificationService` is unaware of any of this: it still calls `EmailSender.SendAsync`:

Registration wires it all together:

Enable the flag for a small percentage of traffic. Monitor delivery rates, bounce rates, and latency for both providers in parallel. Widen the rollout when the new provider proves reliable. The old provider remains available as a fallback for as long as you need it.

Once `SendGridEmailSender` has proved itself in production and the flag is fully enabled for all traffic, delete `SmtpEmailSender`, delete `FeatureFlagRoutingEmailSender`, remove the flag check, and register `SendGridEmailSender` directly as `EmailSender`:

`NotificationService` has not changed since the expand phase. It never needed to know that the provider changed.

The lesson is the point of the suture. Branch by Abstraction does not route traffic between two systems. It places a seam inside the code, between a caller and a dependency, and routes execution between two implementations of the same interface. The caller never moves. The implementations are what change.

Your system has a `ReportsModule` inside the monolith. It generates business reports by running complex SQL queries directly against the production database. It works, but it is hard to test, impossible to scale independently, and its SQL has grown to a point where nobody is confident changing it. A new `ReportingService`, a separate deployable, is being built to replace it.

You cannot do a cutover rewrite. The new service is not finished yet. Some report types will be migrated before others. Business users depend on reports daily. If the new service has a problem, you need to fall back in seconds, not in the time it takes to redeploy the monolith.

Strangler Fig is the pattern for this situation. Its name comes from the strangler fig tree, which grows around a host tree and gradually takes its place. The old module is not removed first and replaced: it remains alive and continues serving traffic while the new service grows alongside it. Traffic is rerouted incrementally, one report type at a time. The old module is deleted only when it has no remaining consumers.

The key distinction from Branch by Abstraction is where the suture point lives. In Branch by Abstraction, the suture is inside the code: an interface between a caller and a dependency. In Strangler Fig, the suture is in the routing layer: a proxy, middleware, or API gateway that decides where each request goes. The callers do not change. The routing logic changes.

The monolith handles all report requests directly:

Introduce the routing middleware. At this point it forwards all requests to the legacy module unchanged. The new service does not exist yet. Nothing changes in observable behaviour. But the routing layer is now in place, and adding a new route to the new service will not require touching `ReportsController`:

Registration:

The new `ReportingService` is built and deployed as a separate process. Report types migrate one at a time. When `reports.sales-summary-uses-new-service` is enabled in ConfigCat, all requests for the sales summary report route to the new service. The legacy `ReportsController` still handles inventory and retention. Both are live simultaneously. Neither knows about the other.

The new service exposes the same API paths so callers do not change:

Enable each flag independently as the corresponding report type is ready and validated. The strangler fig grows one branch at a time.

Once all three flags are permanently enabled and no traffic reaches the legacy module, delete `ReportsController`, delete `LegacyReportQueryService`, and delete `ReportRoutingMiddleware`. Remove the three flags from ConfigCat. The new service handles all report traffic directly, with no routing layer in the middle.

[![Image 16](https://substackcdn.com/image/fetch/$s_!a6mZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4639d588-e8d2-4c0e-bfb3-3af37a826830_2018x1692.png)](https://substackcdn.com/image/fetch/$s_!a6mZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4639d588-e8d2-4c0e-bfb3-3af37a826830_2018x1692.png)

The difference from Branch by Abstraction is visible in this diagram. In Branch by Abstraction, the routing decision happens inside a single process, between an interface and two implementations, and callers see one coherent dependency. In Strangler Fig, the routing decision happens at the network layer, between two separate deployables, and callers see one coherent API. In both cases, the old and new implementations coexist safely. In both cases, the migration is gradual. What differs is the granularity and the location of the seam.

Strangler Fig carries a specific risk that Branch by Abstraction does not: the routing middleware becomes load-bearing infrastructure. If the middleware has a bug, all reports break. If it has a memory leak, it affects the monolith. The routing layer should be thin, observable, and tested. Its only responsibility is to decide where to send a request. All business logic stays in the implementations on either side of it.

Parallel Change sounds tidy when described in three words. In practice, teams usually fail not because they misunderstand the pattern, but because they mishandle the temporary state it creates.

The first failure mode is the **contract step that never ships**. The visible business benefit arrives during Expand or Migrate. Contract rarely has a direct user-facing value, so it loses the prioritisation argument unless someone owns it from the beginning. The fix is procedural, not technical: open the contract ticket when you open the expand change. Assign it. Give it a date derived from something real, like the mobile team’s migration timeline or a deployment cadence. The contract step is not optional follow-up. It is the second half of the same decision.

The second failure mode is **crossing the point of no easy return without naming it**. Teams tell themselves they can “always flip it back” long after the old path has stopped receiving fresh data. At that point the rollback story has already changed, whether they noticed or not. The fix is to name the point explicitly before the migration starts. In a database migration, write it into the migration comments. In a flag-based migration, note it in the flag description in ConfigCat. The knowledge of where rollback stops being free should be shared with everyone who might be asked to roll back at two in the morning.

The third failure mode is **feature flags that outlive the migration**. A migration flag that survives long after the migration is complete is no longer making release safer. It is just another branch that future engineers must understand, preserve, and account for in every subsequent change. The fix is to create the removal ticket when the flag is created, exactly as with the contract ticket, and to treat the flag’s existence as a temporary cost rather than a default state.

The fourth failure mode is **two valid shapes confusing new work**. If old and new coexist without any marking that one is transitional, new code keeps getting written against the old path. The `[Obsolete]` attribute on C# members, deprecation annotations in OpenAPI documentation, and a visible note in the expand change all prevent the silent accumulation of new dependencies on something that is scheduled to disappear.

Not every change needs this discipline. If you control all consumers and can update them safely in one atomic change, if the system is not live in a way that creates compatibility risk, and if rollback would be trivial, a direct change is usually better. The pattern adds intermediate steps. Intermediate steps have a cost.

Parallel Change becomes the right tool when direct coordination is unrealistic, risky, or expensive. Uncontrolled consumers, always-on traffic, shared schemas, independent deployment cycles, public contracts, or a legacy system that would otherwise demand a high-risk cutover are all situations where the cost of intermediate steps is lower than the cost of the alternative. The last two categories map directly to Branch by Abstraction (Example 6) and Strangler Fig (Example 7).

[![Image 17](https://substackcdn.com/image/fetch/$s_!J2xU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F875c1839-6762-4b67-9874-d2e8cb1cc5a6_1340x2967.png)](https://substackcdn.com/image/fetch/$s_!J2xU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F875c1839-6762-4b67-9874-d2e8cb1cc5a6_1340x2967.png)

The fear that keeps these changes stuck in the backlog is usually not irrational. It comes from experience. Engineers have seen systems break when too many moving parts had to shift together. They have seen “small” changes trigger incidents because the real problem was never the code in isolation. It was the coordination burden hiding around it.

Parallel Change does not remove risk by pretending the system is simpler than it is. It reduces risk by respecting reality. Different consumers move at different speeds. Old and new shapes often need to coexist for a while. Data survives deployments. Rollback is only easy up to a point. These are not exceptions. They are normal properties of live systems.

Once that is accepted, the change stops looking like one dangerous moment and starts looking like a sequence of safe states. A team that thinks this way can split a live database column without downtime, introduce a new API contract while a mobile app finishes its own cycle, refactor a constructor used across many call sites without freezing the codebase, and simplify a builder hierarchy that was compensating for a domain misunderstanding, doing so in a way that gave the team space to find the better design.

The part that requires the most discipline is not Expand. Teams usually find it satisfying to add the new path. It is not Migrate either. That phase often has visible momentum. The hard part is Contract, because once the new behaviour is live, it is easy to pretend the work is done. It is not. Contract is how the system returns to clarity. It is how temporary compatibility becomes temporary in truth rather than only in intention. It is how the next change stays possible.

A system stays healthy not because it avoids change, but because it learns how to change without forcing everything to move together.

*   Danilo Sato. _Parallel Change_. [https://martinfowler.com/bliki/ParallelChange.html](https://martinfowler.com/bliki/ParallelChange.html)

*   Tim Wellhausen. _Expand and Contract_. [https://martinfowler.com/articles/patterns-of-distributed-systems/two-phase-commit.html](https://martinfowler.com/articles/patterns-of-distributed-systems/two-phase-commit.html)

*   Martin Fowler. _Branch by Abstraction_. [https://martinfowler.com/bliki/BranchByAbstraction.html](https://martinfowler.com/bliki/BranchByAbstraction.html)

*   Martin Fowler. _Strangler Fig Application_. [https://martinfowler.com/bliki/StranglerFigApplication.html](https://martinfowler.com/bliki/StranglerFigApplication.html)

*   Martin Fowler. _Canary Release_. [https://martinfowler.com/bliki/CanaryRelease.html](https://martinfowler.com/bliki/CanaryRelease.html)

*   Pete Hodgson. _Feature Toggles (aka Feature Flags)_. [https://martinfowler.com/articles/feature-toggles.html](https://martinfowler.com/articles/feature-toggles.html)

*   Martin Fowler. _Continuous Integration_. [https://martinfowler.com/articles/continuousIntegration.html](https://martinfowler.com/articles/continuousIntegration.html)

*   FluentMigrator. _FluentMigrator documentation_.

[https://fluentmigrator.github.io](https://fluentmigrator.github.io/)

*   ConfigCat. _.NET SDK Reference_. [https://configcat.com/docs/sdk-reference/dotnet](https://configcat.com/docs/sdk-reference/dotnet)

*   ConfigCat. _Polling Modes and Caching_. [https://configcat.com/docs/advanced/caching](https://configcat.com/docs/advanced/caching)

*   Vue.js. _Composables_. [https://vuejs.org/guide/reusability/composables.html](https://vuejs.org/guide/reusability/composables.html)

*   Manuel Rivero and the Codesai team (2025). _Parallel change example: simplifying some test builders_. [https://codesai.com/posts/2025/11/simplifying-builders-parallel-change](https://codesai.com/posts/2025/11/simplifying-builders-parallel-change)
