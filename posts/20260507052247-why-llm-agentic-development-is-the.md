Title: Why LLM agentic development is the worst developer experience

URL Source: http://emmanuelvalverderamos.substack.com/p/why-llm-agentic-development-is-the

Final URL: https://emmanuelvalverderamos.substack.com/p/why-llm-agentic-development-is-the

Published Time: 2026-05-07T05:22:47+00:00

Markdown Content:
Imagine downloading a framework that promises to remove half your work.

Authentication, user flows, integrations, scaffolding, boilerplate, the lot. Install it and, apparently, you become a 10x developer, whatever that is supposed to mean.

There is only one problem. Before it gives you anything useful, you have to do something absurd. Think of compiling the Linux kernel just to get started. Then, after all that effort, the framework still behaves like a cursed object. Sometimes it works. Sometimes it fails. Sometimes the same task, with the same apparent setup, produces a different result. The outcome depends not only on what you asked for, but on the model version, the tool version, the context you managed to cram into it, and the manual patching you applied to keep the thing from embarrassing itself.

Now ask the only question that matters.

Would you put that in production?

I would not.

I would not because this is not just an annoying developer experience. It is a bad investment. It introduces too much uncertainty, too many unknown unknowns, too much hidden maintenance cost, and too much supervision work just to obtain something that is being sold as effortless leverage. Worse, the part it claims to accelerate was rarely the real bottleneck in the first place.

That is my problem with LLM agentic development.

Not that it sometimes fails. Every tool fails.

My problem is that it too often demands a whole extra layer of human work just to become trustworthy, and then asks us to call that progress.

*   LLM agentic development is often a terrible developer experience because it ships its missing reliability layer to the developer.

*   It can save typing, but it frequently creates new work in supervision, verification, cleanup, and containment.

*   The evidence on speed is mixed. One controlled enterprise study estimated about 21% faster completion on the task studied, while METR found experienced open source developers were 19% slower on their own mature repositories, even though they believed the tools helped.

*   “It works for me” is the 2026 version of “it works on my machine.” Without a baseline, a defined problem, before and after numbers, and the cost of getting there, it is usually just gut feeling with better branding.

*   Even when local coding speed improves, system-level outcomes can still get worse. DORA reported higher perceived productivity and flow alongside worse delivery stability and throughput, and also found that heavier use of generative tools was associated with less time spent on work developers themselves considered valuable.

[![Image 1](https://substackcdn.com/image/fetch/$s_!ACop!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41e8d5c4-bbe5-4a81-a1df-521052fb2649_1024x559.png)](https://substackcdn.com/image/fetch/$s_!ACop!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41e8d5c4-bbe5-4a81-a1df-521052fb2649_1024x559.png)

If a normal library behaved like the metaphor I just described, nobody serious would defend it. Nobody would say the problem is that the user lacks faith. Nobody would say the rough edges are the price of genius. We would call it fragile, hostile, and operationally irresponsible.

That is the first thing this conversation keeps getting wrong. Our industry has become strangely willing to forgive in LLM agentic tooling what it would reject everywhere else. We have lowered the bar precisely because the sales pitch is bigger.

A product does not become good because it is powerful. It becomes good when that power is usable without ritual.

And this is where the article needs to be precise. The issue is not that good tools change how we work. Good tools do that all the time. The issue is not that new capabilities introduce new mechanics. The issue is that bad tools make us build defensive process around their weaknesses.

That distinction matters.

[![Image 2](https://substackcdn.com/image/fetch/$s_!lzBK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e0b2e41-d522-41b2-a247-f9d1ad8223e3_1024x559.png)](https://substackcdn.com/image/fetch/$s_!lzBK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e0b2e41-d522-41b2-a247-f9d1ad8223e3_1024x559.png)

I am not using the opening story because it sounds clever. I am using it because it is diagnostic.

LLM agentic development is sold as if it were a new abstraction layer that removes drudgery. In practice, it often feels like a volatile stack of prompts, tools, context windows, retries, wrappers, and guesswork that only sometimes converges into something you would trust.

The problem is not novelty. The problem is not that there are commands, skills, conventions, or reusable patterns. A good skill may add leverage. A good command may reduce friction. A good automation may save real effort.

The problem is that too much of the extra process exists to compensate for weak trustworthiness.

That is the real distinction.

A capability that extends what a team can do is one thing. A defensive operating layer whose main job is to stop the system from drifting, hallucinating, breaking assumptions, or wasting your time is something else entirely.

The product is the problem when the user has to finish it before it becomes safe to depend on.

[![Image 3](https://substackcdn.com/image/fetch/$s_!SY5X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2946349-ad0e-42df-879c-defea2fa56c3_1024x558.png)](https://substackcdn.com/image/fetch/$s_!SY5X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2946349-ad0e-42df-879c-defea2fa56c3_1024x558.png)

This is the part the demos always hide.

The dirty secret of LLM agentic development is that much of its cost does not disappear. It just moves.

It moves into prompt shaping. Context curation. Retrying. Reframing. Reviewing diffs you do not trust. Checking whether the system solved the actual problem or merely produced something that looks busy. Verifying that tests were not gamed. Cleaning up plausible nonsense. Recovering from confident mistakes. Re-validating assumptions after tool changes.

This is where the argument needs to become exact.

The issue is not any workflow change whatsoever. The issue is compensatory work. Work that exists not because the capability itself is so valuable, but because the base product is not trustworthy enough on its own.

That is the part people keep romanticising.

Guardrails built because the system is not predictably safe are not leverage. Repeated checking because the output is not trusted is not leverage. Retrying because the behaviour is unstable is not leverage. Cleanup because the result is plausible rather than reliable is not leverage.

The tool is not reliably removing engineering work. It is often relocating engineering work into supervision, verification, containment, and cleanup.

And that matters because the output may be faster, but the accountability is still yours. The blast radius is still yours. The incident is still yours. The maintenance burden is still yours.

[![Image 4](https://substackcdn.com/image/fetch/$s_!nJKu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f5d484-33dd-4c12-9bf7-e541a4026de8_1024x559.png)](https://substackcdn.com/image/fetch/$s_!nJKu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f5d484-33dd-4c12-9bf7-e541a4026de8_1024x559.png)

Once you stop treating this as a vibes discussion and start treating it as an investment decision, the whole thing looks worse.

A serious engineering decision is not judged by whether a tool can occasionally produce something impressive. It is judged by the relationship between value, cost, risk, and liquidity.

That is why I keep coming back to the same question: would I put this in production?

Because production is where slogans go to die. In production, uncertainty costs money. Hidden maintenance costs money. Supervision costs money. Rework costs money. Fragility costs money. Unknown unknowns cost money.

And this is exactly where LLM agentic development looks far worse than its fans admit. It may create local speedups, but it does so by introducing a layer of ongoing operational burden that has to be paid again and again.

That burden is not only in the generated output. It is also in the process you build around it. Prompts. Rules. Validation habits. Tool wrappers. Evaluation routines. Defensive conventions. New review patterns. New failure modes. All of that becomes part of the system’s continuing cost.

This is where the economic frame matters most. If time spent making the tool trustworthy is time not spent solving better product problems, simplifying architecture, reducing real bottlenecks, or learning from users, then the cost is not merely technical. It is opportunity cost.

The economics do not close when the promise is speed but the reality is permanent adaptation, permanent supervision, and permanent trust repair.

This is the part people still underestimate.

A difficult but stable tool may be worth learning because the knowledge compounds. The investment pays back over time. Your understanding deepens. Your judgment improves. Your team builds durable competence.

A lot of current LLM agentic development does not feel like that.

Models change. Toolchains change. APIs change. Pricing changes. Context limits change. Recommended practices change. Integrations appear and disappear. The setup that worked this month may be partially obsolete a few weeks later.

That is not a normal learning curve.

That is moving ground.

And moving ground is economically expensive because it creates recurring re-learning, recurring re-validation, recurring trust repair, and fast knowledge decay. The 2025 and 2026 DORA material frames AI in software development as an amplifier of the surrounding system rather than a universal fix, which fits this problem exactly: gains depend heavily on the broader organisational and technical foundation, and weak foundations turn local improvements into wider instability.

The problem is not that you have to learn a new tool. The problem is that the tool, the ecosystem around it, and the rules for using it keep changing before the learning has even had time to amortise.

Good tools usually let knowledge compound.

A lot of current LLM agentic tooling makes knowledge decay.

That is a much more serious indictment than “it changes the workflow.” Of course it changes the workflow. That alone proves nothing. What matters is that too much of the adaptation is recurring re-learning, recurring re-validation, and recurring trust repair.

Even success stories become weaker under that light. If the ecosystem mutates fast enough, many “it worked for us” stories are snapshots, not durable improvements.

[![Image 5](https://substackcdn.com/image/fetch/$s_!WeK_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0cecacae-c8ff-4e2b-a4d2-b2dd9f92117a_1024x558.png)](https://substackcdn.com/image/fetch/$s_!WeK_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0cecacae-c8ff-4e2b-a4d2-b2dd9f92117a_1024x558.png)

The most annoying part of this conversation is not that people claim LLMs with agents can help. Of course they can help. The annoying part is the certainty.

Because the evidence does not justify that certainty.

A Google enterprise-based randomized trial estimated developers using coding assistance were about 21% faster on the study task. But METR then found the opposite in a much more uncomfortable setting for the hype: experienced open source developers working on their own repositories were 19% slower when allowed to use early-2025 tools. The same METR study found something even more interesting: before starting, developers forecast a 24% speedup, and after the slowdown they still believed the tools had sped them up by 20%.

That pair of findings is much more useful than any neat, flattering productivity number.

Because it tells us two things at once.

First, the effect is highly context-dependent.

Second, belief in improvement can outrun measured improvement.

And that matters because a lot of this debate is being driven not by disciplined evaluation, but by a confidence that is far more stable than the evidence.

One of the weakest defences of LLM agentic development is also one of the most common: it works for me.

Fine. Maybe it does.

But that sentence has quietly become the 2026 version of “it works on my machine.” It sounds empirical. It sounds grounded. Most of the time, it is neither.

Because the question is not, “What did you do to make it work?”

That is already the wrong conversation.

The real question is: what does “works” mean, exactly?

What concrete problems did you have before? Which of those problems have actually been solved? How were they solved? What were the numbers before, and what are the numbers now? How much did it cost to get there? How much does it cost to maintain? Over what time horizon are you making the claim?

That is what serious evaluation looks like.

If you cannot answer those questions, then “it works for me” is not evidence. It is not even a meaningful claim. It is an educated guess dressed up as experience.

Maybe you feel faster. Fine. Compared to what? On which tasks? With what review burden? With what defect rate? With what maintenance cost? With what effect on the rest of the team? With what trade-off in understanding, reliability, or operational risk?

This is the part that frustrates me most. A lot of people defending LLM agentic development are not describing solved problems. They are describing rituals. They tell you which prompts they use, which tools they chain together, how they structure context, how they retry, how they recover. But none of that answers the actual question.

I do not care first about what you had to do to make it “work.” I care first about what problem you solved, how you know it was solved, and what it really cost to solve it.

Because if you cannot show the previous state, the current state, the cost of reaching it, and the cost of sustaining it, then what you have is not proof of improvement.

You have a story.

And the METR result makes this even more awkward. Developers felt helped. The clock said otherwise.

This is where DORA’s work becomes genuinely useful.

DORA’s 2024 findings reported a strange combination: greater generative-tool adoption was associated with higher self-reported productivity, better flow, and greater job satisfaction, but also with estimated decreases in delivery throughput and delivery stability. DORA also found that developers who used generative tools more extensively reported more flow, more satisfaction, more productivity, and less burnout, but no reduction in toilsome work and less time spent on work they themselves considered valuable. The 2025 DORA review reinforced the same pattern: AI can improve throughput, but often at the cost of stability when the foundation is weak.

That is not a side note. That is one of the most important facts in the whole debate.

People can feel more productive while spending less time on what they consider valuable. A developer can have a smoother local experience while the wider system becomes noisier, slower, or less stable.

So when someone says, “it works for me,” my first reaction is no longer interest. It is the same reaction I have when I hear, “it works on my machine.”

Good for you.

Now show me the before state. Show me the after state. Show me the cost of reaching it. Show me the cost of sustaining it. Show me what “works” means in numbers rather than vibes.

Even that is not enough, because software is not a one-shot task and it is not a benchmark screenshot.

Real software lives in time. It evolves. It accumulates constraints. It inherits old assumptions. It carries incidents, strange edge cases, compatibility baggage, and team memory. The problem is not whether a model can produce something that compiles today. The problem is whether the system remains understandable and safe after months of change.

That is why SWE-CI matters. It was built precisely because static, one-shot repair benchmarks miss what real codebases demand. It shifts evaluation toward long-term maintainability, using tasks drawn from real repositories with an average of 233 days and 71 consecutive commits of history.

Passing once is easy.

Surviving change is engineering.

Benchmarks reward visible completion. Production punishes hidden fragility.

That is the distinction a lot of benchmark culture still does not take seriously enough.

This is also why I do not find the “but it writes code faster” argument especially persuasive.

The central delusion behind a lot of this discourse is the assumption that software has historically been slow because developers could not type quickly enough.

That was rarely the real bottleneck.

The hard part was deciding what deserved to exist, why it mattered, which trade-offs were acceptable, how systems should evolve, and how teams should be structured to support that evolution. Build the wrong thing faster and you do not improve the system. You just produce waste faster.

That is why this whole moment feels so upside down. We have built an industry narrative around accelerating the most visible part of the work while leaving the hardest parts untouched. In some cases, we are making them worse.

Because when implementation becomes cheaper, bad decisions become easier to multiply. Waste becomes easier to produce. Fragile systems become easier to expand.

Accelerating output is not the same as improving delivery. Output was never the point anyway.

There is another reason this matters. If the human is meant to be the safety layer, then the human actually has to remain competent enough to supervise well.

A 2026 study on skill formation found that AI assistance impaired conceptual understanding, code reading, and debugging abilities when developers were learning a new library, without delivering significant efficiency gains on average. The important part is not the headline. It is the implication. If the workflow depends on the human catching bad output, then anything that weakens the human’s understanding is not a side effect. It strikes directly at the safety model itself. ([arXiv](https://arxiv.org/abs/2601.20245?utm_source=chatgpt.com))

That is devastating for one of the laziest replies in this whole discussion: “you just need better prompts.”

Maybe. Sometimes. Expertise obviously matters.

But that is not a defence. It is often the indictment.

A mature tool becomes more powerful with expertise. A weak product becomes merely tolerable once the user has built a private religion around its failure modes.

That is the distinction.

If acceptable results require rituals, careful phrasing, context packing, custom workflows, constant verification, selective trust, and learned superstition about what the model is likely to break, then what you have is not evidence of maturity. What you have is a product that shipped its missing reliability layer to the customer.

This is why the discussion about “AI slop” matters too.

A 2026 qualitative analysis of 1,154 posts across 15 discussion threads found recurring themes of review friction, trust erosion, quality degradation, and cost being pushed onto reviewers, maintainers, and the wider community. The paper frames the problem as a tragedy of the commons, where local gains can externalize costs onto everyone else.

That is almost the whole article in one sentence.

This is not pure productivity.

It is often cost transfer.

The speedup, if it exists, is local. The review burden is shared. The trust burden is shared. The maintenance burden is shared. The consequences are socialised while the productivity story is personalised.

That is not the same thing as leverage.

Now put all of that aside for a second and translate it into ordinary product judgment.

Imagine a SaaS with the worst out-of-the-box user experience you have ever seen.

The UI is hostile. The defaults are wrong. The behaviour is inconsistent. The product occasionally does something impressive, but only if you already know how to work around its worst instincts. And the company’s answer to every complaint is not to improve the product, but to tell the user to build their own usability layer.

Would you use it?

I would not.

I would say the product is unfinished. I would say the burden has been exported to the customer. I would say the company has confused possibility with usability.

That is how a lot of LLM agentic development feels to me.

Not like a finished tool. Like a powerful but badly productised capability whose cost has been deliberately relocated onto the people expected to depend on it.

That is my real problem with it.

Not that LLMs with agents can generate code.

My problem is that the current experience too often asks the developer to absorb all the cost of making that generation safe, comprehensible, and operationally trustworthy.

That is not leverage.

That is burden export.

LLM agentic development is not the worst developer experience because it sometimes fails. Every serious tool fails.

It is the worst developer experience because it too often fails in a very specific way: it produces the appearance of acceleration while quietly exporting the work of reliability, supervision, verification, and containment back to the developer.

That might still be worth it in some contexts. I am not denying that.

What I am denying is the mythology.

I do not think a tool deserves praise because it can generate code. I think it deserves praise when it reduces the total cost of building, understanding, changing, and safely operating software.

And no, “it works for me” is not a serious answer unless you can define what “works” means, name the problems that were solved, show the before and after, and account for the cost of getting there and keeping it there.

A good tool removes burden. LLM agentic development too often just moves that burden somewhere harder to see.

*   Artola, Luis. _Software economics_.

*   Baltes, Sebastian, Cheong, Marc, Treude, Christoph. _“An Endless Stream of AI Slop”: The Growing Burden of AI-Assisted Software Development_. [https://arxiv.org/abs/2603.27249](https://arxiv.org/abs/2603.27249)

*   Becker, Joel, Rush, Nate, Barnes, Elizabeth, Rein, David. _Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity_. [https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

*   Boehm, Barry W. _Software Engineering Economics_.

*   Chen, Jialong, Xu, Xander, Wei, Hu, Chen, Chuan, Zhao, Bing. _SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration_. [https://arxiv.org/abs/2603.03823](https://arxiv.org/abs/2603.03823)

*   DORA. _2024 DORA Report Preview_. [https://dora.dev/research/2024/ai-preview/](https://dora.dev/research/2024/ai-preview/)

*   DORA. _DORA 2025: Year in review_. [https://dora.dev/insights/dora-2025-year-in-review/](https://dora.dev/insights/dora-2025-year-in-review/)

*   DORA. _How gen AI affects the value of development work_. [https://dora.dev/insights/value-of-development-work/](https://dora.dev/insights/value-of-development-work/)

*   DORA. _State of AI-assisted Software Development 2025_. [https://dora.dev/dora-report-2025/](https://dora.dev/dora-report-2025/)

*   Paradis, Elise, Grey, Kate, Madison, Quinn, Nam, Daye, Macvean, Andrew, Meimand, Vahid, Zhang, Nan, Ferrari-Church, Ben, Chandra, Satish. _How Much Does AI Impact Development Speed? An Enterprise-based Randomized Controlled Trial_. [https://arxiv.org/abs/2410.12944](https://arxiv.org/abs/2410.12944)

*   Ramos, Emmanuel Valverde. _AI can write code. That was never the bottleneck._[https://emmanuelvalverderamos.substack.com/p/the-real-bottleneck-was-never-code](https://emmanuelvalverderamos.substack.com/p/the-real-bottleneck-was-never-code)

*   Ramos, Emmanuel Valverde. _My reflection on the real problem about AI in the software industry_. [https://emmanuelvalverderamos.substack.com/p/my-reflection-on-the-real-problem](https://emmanuelvalverderamos.substack.com/p/my-reflection-on-the-real-problem)

*   Shen, Judy Hanwen, Tamkin, Alex. _How AI Impacts Skill Formation_. [https://arxiv.org/abs/2601.20245](https://arxiv.org/abs/2601.20245)
