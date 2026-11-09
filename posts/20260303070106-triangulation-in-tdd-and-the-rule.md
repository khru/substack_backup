Title: Triangulation in TDD and the Rule of Three

URL Source: http://emmanuelvalverderamos.substack.com/p/triangulation-in-tdd-and-the-rule

Final URL: https://emmanuelvalverderamos.substack.com/p/triangulation-in-tdd-and-the-rule

Published Time: 2026-03-03T07:01:06+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!l1kq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90a2f9fb-905d-419a-8011-888331dcbf24_1408x752.png)](https://substackcdn.com/image/fetch/$s_!l1kq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90a2f9fb-905d-419a-8011-888331dcbf24_1408x752.png)

How to earn abstractions instead of guessing them

I tried to keep this friendly and practical, not academic. If I failed and wrote a brick, call me out. Also, challenge every word I wrote. Look for counterexamples, compare with your own codebase, and keep what survives.

Here is the idea in one sentence:

Triangulation is a brake. A brake on premature abstraction. A brake on “I saw a pattern once, therefore I will design a framework.”

[![Image 2](https://substackcdn.com/image/fetch/$s_!Rc8d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50f67ead-a9e2-454c-b03f-16ee1e019673_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!Rc8d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50f67ead-a9e2-454c-b03f-16ee1e019673_2816x1536.png)

**Triangulation:** drive abstraction using multiple concrete examples.

In TDD, you do not abstract because you can. You abstract because the tests forced you to.

Kent Beck describes triangulation with a very conservative rule: **abstract only when you have two or more examples**.

That sounds simple, but it changes your behavior.

*   You stop treating design as prediction.

*   You treat design as something you earn, step by step, from evidence.

Remember: tests do not only prevent regressions. Tests are also your proof that a generalization is real.

[![Image 3](https://substackcdn.com/image/fetch/$s_!upFu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c997ca3-0266-4041-a00e-b499638b889c_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!upFu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c997ca3-0266-4041-a00e-b499638b889c_2816x1536.png)

If triangulation can start at two examples, why do people repeat “three times”?

Because the second example often tells you “a constant is not enough”, but it does not always tell you “what the stable rule really is”.

The Rule of Three is a habit builder:

*   First time, do it.

*   Second time, you notice the duplication, but you keep it.

*   Third time, you refactor.

It is not a law. It is a guardrail.

It is also a nice way to avoid a very human failure mode: we see a pattern quickly, and we fall in love with our first explanation.

[![Image 4](https://substackcdn.com/image/fetch/$s_!4E2g!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fa664e2-7a9b-4d03-b7a2-19f5cc99ce3b_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!4E2g!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fa664e2-7a9b-4d03-b7a2-19f5cc99ce3b_2816x1536.png)

Here is the frustrating part: teams rarely pay the price of premature abstraction immediately.

They pay it later, with interest.

When you introduce an abstraction too early, you often introduce:

*   indirection

*   shared dependencies

*   a new vocabulary that shapes future design decisions

*   a bigger blast radius when you need to change behavior

And then the business asks for something “small” that does not fit your beautiful model, and suddenly the change is not small anymore.

Here is a diagnostic question I like:

**Can you say whether this abstraction reduced risk, reduced cost, reduced future work, or increased delivery speed?**

If you cannot answer, you might be paying for elegance, not value.

Kent Beck frames this in economic terms in _Extreme Programming Explained_: design is not free. More design today increases overhead. There is more to test, more to understand, more to explain. You pay a kind of design tax every day you carry it. He also points out the option value of waiting when uncertainty is high. If you guess wrong, you rework the design, sometimes multiple times.

Tradeoff framing:

*   Designing early can feel like “being responsible”.

*   Waiting can feel like “being sloppy”.

*   But if uncertainty is real, waiting preserves options and keeps you liquid. Less liquidity means less ability to react.

And this is where triangulation shines: it is a structured way to wait without freezing.

[![Image 5](https://substackcdn.com/image/fetch/$s_!BdeF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74eab360-8aa1-4ae9-8de3-766b5213b895_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!BdeF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74eab360-8aa1-4ae9-8de3-766b5213b895_2816x1536.png)

This section is the upgrade I would add from _The Programmer’s Brain_ by Felienne Hermans, because it explains something developers feel every day but rarely name: cognitive load.

A book is not hard because it is long, but because so much is new. More novelty means more cognitive load.

Hermans gives a simple mental model of what happens when you read and change code:

Short term memory can only hold a few elements at once. Hermans summarizes research that puts this capacity roughly in the **range of two to six elements**.

Now connect that to premature abstraction.

If you introduce new concepts early, you ask the reader to hold more things in mind while they are still trying to understand the problem. That is how you get slow reading, mistakes, and shallow comprehension.

Hermans distinguishes short term memory (storage) from working memory (processing). Working memory is where you simulate code, reason about it, and form new ideas. When working memory is overloaded, you start doing external memory hacks: notes, tables, rereads, debugging steps, and so on.

Triangulation reduces this load because it keeps the code concrete while you are still learning. You do not force yourself to solve “what works” and “what is the best abstraction” at the same time.

Hermans explains chunking: experts compress details into meaningful chunks using knowledge stored in long term memory. Beginners cannot do this as effectively, so they fall back to low level reading and quickly overload.

This is a practical point, not a motivational one.

A clever abstraction might feel cheap to the person who just created it. It can be expensive for everyone else, including future you, once the context fades.

Hermans talks about “beacons”: small cues like good names and recognizable structures that help readers form a mental model faster. Experts use these cues heavily.

Premature abstraction often destroys beacons:

*   the code gets generic names too early

*   behavior is hidden behind indirection

*   you see plumbing instead of intent

Triangulation tends to preserve beacons because the first versions stay direct and readable. You only introduce a concept once you can name it clearly and justify it.

Hermans cites estimates that programmers spend close to 60 percent of their time understanding existing code rather than writing it.

That makes this argument simple:  
If a practice makes code easier to understand, it compounds. Every day.

Imperative guidance:  
Resist the temptation to guess the long term future. Pause, chew, swallow, digest. Let the tests teach you what the system wants to become.

[![Image 6](https://substackcdn.com/image/fetch/$s_!QIJ_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62d43359-50e4-4753-b792-3e17f781cd8a_2816x1536.png)](https://substackcdn.com/image/fetch/$s_!QIJ_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62d43359-50e4-4753-b792-3e17f781cd8a_2816x1536.png)

A lot of people can repeat the slogan. Fewer people can apply it under pressure. Here is a workflow that holds up:

1.   **Write one concrete test.**  
Make it pass in the simplest way you can.

2.   **Add a test that forces a shape change.**  
Do not add “more of the same”. Add a case that makes your current solution uncomfortable.

3.   **Wait for repetition before generalizing.**  
On the second repetition you may generalize. On the third repetition you usually know what the safe generalization is.

4.   **Refactor only after green.**  
Focus on the habit as much as the result. Focus on the practice as much as the outcome.

This is intentionally small. but is a good example of triangulation. Is important to remember that we will start with the landing position and with de “Zero“ state that we mention on last week post from TDD guided by ZOMBIES.

At this point, you could generalize. You have enough to suspect a rule.

Rule of Three guidance:  
Wait one more repetition. Make the pattern earn the refactor.

Rover stays exactly as in Commit 3 in this commit.

Now the repetition is loud. The abstraction is not a guess anymore.

This is the triangulation moment: you did not invent a domain model you have not earned. You generalized only what the tests proved. And not only that but you also evaluate if the test can be refactor. This does not cover the entire behavior, but covers the behavior we have tested.

**Remember: our test are the first users of our applications.**

That is how wrong abstractions are born. The second example proves “not a constant”. The third often proves “the right rule”.

If you end up with names like `GenericHandler` or `BaseProcessor`, it is often a smell: you abstracted the how before you understood the why.

Flexibility is not free. If it is not used, it is overhead.

> Metaphor shift:  
> If requirement novelty is a torrent, do not surf it by guessing. Go upstream by collecting examples, then pave the path where people actually walk.

Triangulation and the Rule of Three are not about writing more tests. They are about timing.

*   They reduce the risk of locking in a wrong model.

*   They provide smaller and faster feedback loops

*   They keep cognitive load lower while you are still learning.

*   They align with how humans actually read and reason about code: small short term memory, limited working memory, and chunking that depends on experience.

*   They turn abstraction into something you earn, not something you assume.

**One last invitation**:  
Challenge this idea in your next refactor. Ask yourself, out loud, “Do I have enough examples to justify this abstraction?” If the answer is no, keep it concrete a little longer.

1.   Kent Beck, _Test-Driven Development: By Example_. Triangulation, fake it, obvious implementation, and the idea of controlling scope by starting with one concrete example and generalizing.

2.   Martin Fowler, _Refactoring: Improving the Design of Existing Code_. The Rule of Three and “three strikes, then you refactor.”

3.   Kent Beck, _Extreme Programming Explained: Embrace Change_. Design overhead, design tax, option value of waiting under uncertainty, and the warning about guessing wrong and paying rework.

4.   Kent Beck, _Tidy First?_ Optionality framing, economics of tidying, and reversible structure changes.

5.   Felienne Hermans, _The Programmer’s Brain_. Short term memory capacity, chunking, beacons, working memory versus short term memory, overload coping strategies, and the estimate that a large share of time is spent reading and comprehending code.

6.   Sandi Metz, “The Wrong Abstraction”. Practical advice: when you have the wrong abstraction, the fastest way forward is often backward, by reintroducing duplication locally. ([Sandi Metz](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction))

7.   Fabio Palomba et al., “On the Diffuseness and the Impact on Maintainability of Code Smells: A Large Scale Empirical Investigation”. Evidence relating code smells to change and fault proneness across many releases. ([fpalomba.github.io](https://fpalomba.github.io/pdf/Journals/J9.pdf))

8.   Victor R. Basili, Lionel C. Briand, Walcélio L. Melo, “A Validation of Object-Oriented Design Metrics as Quality Indicators”. Empirical validation linking OO design metrics with fault proneness. ([cs.umd.edu](https://www.cs.umd.edu/~basili/publications/technical/T102.pdf))
