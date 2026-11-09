Title: Refactoring is a liquidity strategy

URL Source: http://emmanuelvalverderamos.substack.com/p/refactoring-is-a-liquidity-strategy

Final URL: https://emmanuelvalverderamos.substack.com/p/refactoring-is-a-liquidity-strategy

Published Time: 2026-04-22T05:01:27+00:00

Markdown Content:
Most conversations about refactoring start too late and at the wrong level.

They start when delivery is already hurting, when a team has become slower than anyone expected, when a small change suddenly takes three days, or when a bug fix that looked trivial turns into a negotiation with half the codebase. By then, the discussion is already distorted. People stop asking what is happening to the system and start asking whether engineers are trying to “clean up” code instead of shipping features.

[![Image 1: X avatar for @thdxr](https://substackcdn.com/image/fetch/$s_!Aw98!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1602333093485891584%2FmmVqjFNI.jpg) dax@thdxr are there people out there who just want to refactor every day? just wake up and find the worst code and just chip away at it and clean it up wake up the next day do it again, infinitely improving things with zero external impact? 3:29 PM · Apr 18, 2026 · 289K Views 749 Replies · 58 Reposts · 3.3K Likes](https://x.com/thdxr/status/2045525102268162459?s=20)[![Image 2: X avatar for @thdxr](https://substackcdn.com/image/fetch/$s_!Aw98!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1602333093485891584%2FmmVqjFNI.jpg) dax@thdxr i'm thinking about this because no matter how much you try, the existence of LLMs just makes our codebases rot more i feel like having a few people just cleaning up every day without getting pulled into feature work could be good assuming they enjoy it and don't get burnt out 3:35 PM · Apr 18, 2026 · 28.9K Views 119 Replies · 14 Reposts · 847 Likes](https://x.com/thdxr/status/2045526660292767895?s=20)
That framing sounds practical, but it is shallow. It makes refactoring sound like a dispute about taste. Sustainable Code versus visible output. Internal quality versus business value. Technical neatness versus delivery pressure.

That is not the real conflict.

The real conflict is economic.

Software is not just something a company builds. It is something a company invests in. That investment is supposed to create business capability, future revenue, adaptability, and room to respond when the world changes. If that is true, then the job of engineers is not only to make the software work today. It is also to help preserve the future value of that investment.

[![Image 3: X avatar for @plainionist](https://substackcdn.com/image/fetch/$s_!Whu4!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1660289602790342658%2FPYgGb9zX.jpg) Seb@plainionist Refactorings are important and should be integral part of software engineering just like writing automated tests. But of course each refactoring must have a purpose, it must add some (business) value - like everything else. ![Image 4: X avatar for @thdxr](https://substackcdn.com/image/fetch/$s_!Aw98!,w_20,h_20,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1602333093485891584%2FmmVqjFNI.jpg) dax@thdxr are there people out there who just want to refactor every day? just wake up and find the worst code and just chip away at it and clean it up wake up the next day do it again, infinitely improving things with zero external impact? 6:51 AM · Apr 19, 2026 · 680 Views 6 Replies · 11 Likes](https://x.com/plainionist/status/2045757109258649990?s=20)
That is why refactoring matters.

Not because it is elegant. Not because it is virtuous. Not because engineers enjoy rearranging code.

It matters because change has an economy, and refactoring is one of the ways we manage it.

Software is an investment, and engineers help protect that investment.

Code does not stop costing money once it works. It keeps consuming time, attention, coordination, and future capacity simply because it exists.

When the cost of change rises, liquidity falls. When liquidity falls, risk rises with it, and opportunity cost rises shortly after.

That is why refactoring usually creates value even when it does not produce immediate visible revenue. Its value is often in improving the economics of future change.

Test-Driven Development (TDD) matters here because it is not only a testing habit. It is also a design technique that helps teams make structural improvements safely and in the flow of real work.

[![Image 5: X avatar for @evrtrabajo](https://substackcdn.com/image/fetch/$s_!gApN!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1758644850596200448%2Fgz1BKnaC.jpg) Emmanuel Valverde | 👨‍💻 @ 🏡@evrtrabajo 1/12 I think this framing is still too narrow. A real refactor usually adds value by default. To see why, you need to stop talking about refactoring as “cleanup” and start talking about software economics. ![Image 6: X avatar for @plainionist](https://substackcdn.com/image/fetch/$s_!Whu4!,w_20,h_20,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1660289602790342658%2FPYgGb9zX.jpg) Seb@plainionist Refactorings are important and should be integral part of software engineering just like writing automated tests. But of course each refactoring must have a purpose, it must add some (business) value - like everything else. 6:31 PM · Apr 19, 2026 · 126 Views 1 Reply · 3 Likes](https://x.com/evrtrabajo/status/2045933231145357709?s=20)

[![Image 7](https://substackcdn.com/image/fetch/$s_!vTna!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6dbbb49-524e-4e62-babf-045ffd2ceaab_1024x558.png)](https://substackcdn.com/image/fetch/$s_!vTna!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6dbbb49-524e-4e62-babf-045ffd2ceaab_1024x558.png)

The usual debate about refactoring is built on a false opposition.

People ask whether it is worth spending time improving code when that same time could be used to ship something user-visible. That sounds reasonable until you notice what it smuggles in: the assumption that one side creates value and the other side merely polishes internals.

That assumption breaks down the moment you look at software through the lens of economics.

A great deal of software work only becomes understandable when you stop talking in the language of style and start talking in the language of value, cost, risk, liquidity, and opportunity cost. Those are not business words awkwardly imposed on software from the outside. They are the real structure of the problem.

Refactoring is not fundamentally a debate about whether code looks better. It is a debate about whether future change will be cheap or expensive, safe or dangerous, fluid or brittle.

That is a much more serious question.

The first shift that matters is this one: software is an investment.

That means it should be judged as investments are judged. Not only by what was spent to create it, but by what it enables, what it prevents, how much flexibility it preserves, and what kind of future return it can still support.

This is where many engineering conversations go wrong. Teams often talk as if the asset were the code itself. It is not. The asset is the business capability the software enables. The code is the mechanism by which that capability is created and maintained. Sometimes it is also the price paid to obtain it.

That distinction matters because it stops us from equating more code with more progress. More code may mean more capability. It may also mean more burden, more friction, more constraints, and more future cost.

Once you look at software this way, the question changes.

You stop asking, “Did we write more code?”

You start asking, “What did this decision do to the economics of the system we now have to live with?”

[![Image 8](https://substackcdn.com/image/fetch/$s_!emAy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c4fccb3-0397-43e9-a504-296511a98c79_1024x558.png)](https://substackcdn.com/image/fetch/$s_!emAy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c4fccb3-0397-43e9-a504-296511a98c79_1024x558.png)

One of the most useful corrections in this whole discussion is brutally simple: the cost of software does not end when a feature reaches production.

The code keeps charging rent.

It consumes cognitive effort. It increases the surface area for bugs. It creates dependency burden. It raises the cost of testing. It forces future changes to remain compatible with what already exists. It enlarges the amount of context a new person must absorb before they can change anything with confidence.

In other words, code has ongoing cost, not only build cost.

This is why working code is not free just because nobody is touching it this week. The mere fact that it remains part of the system means the team is still paying for it. Sometimes directly, often invisibly, always eventually.

That is one of the most important shifts in the whole article. Working code does not become economically neutral once it works. It becomes part of the cost structure of the business.

And once that is clear, refactoring stops looking like a private engineering preference. It starts looking like one of the ways you stop those costs from compounding faster than the value they support.

This is the central relationship.

If the system is hard to understand, hard to modify, hard to test, and hard to integrate, then every future change becomes more expensive. Once the cost of change rises, liquidity falls.

Liquidity in software is not decorative finance language. It is the practical condition of how easily the organization can move. How easily can it adapt when reality changes? How safely can it respond to new information? How much pain must it absorb before it can pursue a better option?

A liquid system is one that can move without paying an enormous price.

An illiquid system is one that turns every movement into friction.

That is why liquidity matters so much. If liquidity falls, risk rises. Now even simple changes become slower, more fragile, and more expensive. You become less able to exploit opportunities, less able to correct mistakes, and less able to respond to feedback before it expires.

And once that happens, opportunity cost rises too. The problem is not only what the current change costs you. It is also what you are failing to do because the current system makes adaptation too expensive, too slow, or too risky to attempt.

This is the causal chain weak conversations about refactoring usually miss.

Code creates ongoing cost. Ongoing cost raises the cost of change. A higher cost of change reduces liquidity. Reduced liquidity increases risk. Higher risk and lower flexibility increase opportunity cost.

That is not a technical vanity problem. That is already a business problem.

Once that chain is visible, the common framing begins to fall apart.

People often say that refactoring is important, but that each refactoring must somehow prove that it adds business value. That sounds careful, but it is often less precise than it appears.

A real refactor usually adds value by default in software that you expect to keep changing.

Not necessarily direct revenue tomorrow morning. Not necessarily a new capability the user can point at by the end of the day. But value nonetheless.

Why? Because if refactoring improves the internal structure of software without changing its observable behavior, and that improvement makes the system easier to understand and cheaper to modify, then it has already improved the economics of future change.

It has already affected cost.

It has already affected liquidity.

It has already affected risk.

It has already affected opportunity cost.

That is business value.

The better debate is not whether value exists at all. The better debate is about degree, timing, and expected future change. How much value is this structural improvement likely to create? In what part of the system? Under what rate of change? Over what horizon?

Those are serious questions. But they are very different from pretending that internal quality has no value until it becomes immediately visible on a roadmap.

[![Image 9](https://substackcdn.com/image/fetch/$s_!6dL5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F590126e2-7674-4a58-826e-6f9458a0a557_1024x558.png)](https://substackcdn.com/image/fetch/$s_!6dL5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F590126e2-7674-4a58-826e-6f9458a0a557_1024x558.png)

This is also why dental hygiene is a better analogy for refactoring than decoration.

Nobody asks whether brushing your teeth creates direct revenue. Nobody says, “I brushed twice today, but I still do not see measurable business value.”

People understand something simpler.

If you maintain basic hygiene, you prevent accumulation. If you prevent accumulation, you reduce the probability of painful and expensive intervention later. If you ignore small deterioration for long enough, you do not end up in a neutral state. You end up with tartar, cavities, pain, damage, and a much more expensive problem than the one you could have addressed earlier.

Software liquidity works in a very similar way.

If teams do not pay attention to small structural signals, duplication, hidden coupling, brittle tests, awkward dependencies, then friction accumulates quietly. Nothing explodes immediately. That is exactly what makes the problem dangerous. By the time the damage is impossible to ignore, the change is no longer a cheap habit. It has become an expensive repair.

The analogy becomes even stronger if you extend it one step further. Good dental care is not only about reacting when something hurts. It is also about paying attention before the pain arrives. Daily hygiene, yes. But also regular checking so that small problems stay small.

That is how teams should think about liquidity.

Not as a ceremonial refactoring sprint every few months. As a condition of the product that deserves continuous observation. Are simple changes getting harder than they should be? Are more files involved than before? Is fear increasing around specific parts of the system? Are tiny requests suddenly demanding disproportionate coordination?

Those are early signs.

A team that waits until a tooth breaks before caring about dental health is behaving foolishly.

A team that waits until delivery collapses before caring about software liquidity is doing the same thing in a different domain.

This is where precision matters.

Refactoring is not any technical work. It is not any cleanup. It is not a rewrite. It is not “we spent a week changing everything and production became unstable.”

Refactoring, used precisely, means improving the internal structure of software without changing its observable behavior, so that the software becomes easier to understand and cheaper to modify. That is what gives the concept its power. The moment the word expands to cover every large technical intervention, it becomes too vague to reason with.

That precision also sharpens the argument here.

A real refactor usually creates value because it improves the economics of future change, not because it creates a new visible capability on the spot. If what you are doing changes behavior, introduces extended instability, or turns into a detached multi-week restructuring effort, it may still be useful work, but it is no longer the same thing.

That distinction is not pedantic. It is what keeps the concept sharp enough to matter.

[![Image 10](https://substackcdn.com/image/fetch/$s_!NszG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17be47c0-22e6-408d-9c10-2fd8c402e0fa_1024x558.png)](https://substackcdn.com/image/fetch/$s_!NszG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17be47c0-22e6-408d-9c10-2fd8c402e0fa_1024x558.png)

This is also why the healthiest model of refactoring is usually opportunistic.

Once teams finally notice decay, they often imagine refactoring as a separate initiative. A special phase. A temporary pause in delivery. A project called “cleanup.” Sometimes reality does force bigger repair work. Neglect accumulates. Some systems really do need concerted effort to recover.

But that is not the ideal pattern.

The healthier pattern is quieter and more integrated. Most refactoring should happen in the flow of real work: while adding a feature, while fixing a bug, while clarifying a confusing area you already need to touch, while preparing a nearby behavior change.

That matters because it keeps structural improvement close to actual demand. It keeps it proportionate. It reduces speculative redesign detached from present need. It also makes the economics cleaner, because the improvement is directly connected to the cost of the change you are trying to make now and the changes you know are likely to follow.

That is also why the distinction between refactoring and broader rework matters. The moment structural improvement becomes a detached, large, scheduled, long-running pause in delivery, useful though it may be, you are moving away from refactoring in the precise sense and toward broader restructuring.

[![Image 11](https://substackcdn.com/image/fetch/$s_!Tnb0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc738fcbb-4663-4e52-97e9-7206915ca687_1024x558.png)](https://substackcdn.com/image/fetch/$s_!Tnb0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc738fcbb-4663-4e52-97e9-7206915ca687_1024x558.png)

This is also where Test-Driven Development (TDD) belongs in the argument.

Test-Driven Development is often discussed as if it were mainly about testing discipline. That is too shallow. Its deeper value is that it acts as a design technique. It encourages smaller steps. It keeps behavior changes visible. It makes structure changes safer. It helps teams preserve the ability to change the system while they are still working on it.

That is exactly what matters here.

If refactoring is one of the ways we protect software liquidity, then teams need practices that let them make small structural improvements without losing control of behavior. Test-Driven Development, when applied well, supports that rhythm. You change a little, verify behavior, improve structure, and keep moving.

That is not a side issue. It is one of the practical mechanisms by which the economics of change are managed in ordinary software delivery.

The easiest way to misunderstand refactoring is to reduce it to taste.

The easiest way to defend it badly is to talk about elegance, neatness, or professional pride.

Those things are not irrelevant, but they are not the main point.

The main point is this: software is an investment, code has ongoing cost, cost affects liquidity, liquidity affects risk, and risk affects what the business is actually able to do next.

Once you understand that chain, the old debate becomes much less convincing.

You stop asking whether refactoring has business value.

You start asking which part of the economics of change it is improving.

And once you ask that question honestly, the answer is usually clear.

If your code makes simple changes slow, risky, and expensive, that is not a private technical inconvenience. That is already a business problem.

And if small, behavior-preserving structural improvements make future change cheaper and safer, then refactoring is not code vanity.

It is economic maintenance.

[Video 3](https://www.youtube.com/watch?v=FLNz8RQf9Pc)

Teams should stop treating liquidity as something they only notice when delivery hurts. By then, the cost has already arrived.

*   Artola, Luis. _Software economics_. [leanpub.com/software-economics](https://leanpub.com/software-economics)

*   Beck, Kent. _Tidy First? A Personal Exercise in Empirical Software Design._

*   Fowler, Martin. _Refactoring: Improving the Design of Existing Code._[martinfowler.com/books/refactoring.html](https://martinfowler.com/books/refactoring.html)

*   Fowler, Martin. _Definition Of Refactoring._[martinfowler.com/bliki/DefinitionOfRefactoring.html](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)

*   Fowler, Martin. _Is High Quality Software Worth the Cost?_[martinfowler.com/articles/is-quality-worth-cost.html](https://martinfowler.com/articles/is-quality-worth-cost.html)
