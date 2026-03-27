---
title: "Stop measuring AI adoption with token counts"
subtitle: "If your organisation tracks tokens consumed or AI-generated lines of code as proof of progress, it is not measuring transformation. It is measuring noise."
requested_url: "https://emmanuelvalverderamos.substack.com/p/stop-measuring-ai-adoption-with-token"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/stop-measuring-ai-adoption-with-token"
substack_post_id: 191673061
retrieved_at: "2026-03-27T08:57:43.963Z"
---
# Stop measuring AI adoption with token counts

### If your organisation tracks tokens consumed or AI-generated lines of code as proof of progress, it is not measuring transformation. It is measuring noise.

[![](https://substackcdn.com/image/fetch/$s_!q5fL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28084894-cada-481b-809a-cc3515f9bc34_1024x559.png)](https://substackcdn.com/image/fetch/$s_!q5fL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28084894-cada-481b-809a-cc3515f9bc34_1024x559.png)

There is something deeply unserious about the way many organisations are trying to measure AI adoption.

They say they want to know whether AI is changing the business. Whether it is helping teams move faster. Whether it is improving delivery. Whether it is creating real value.

And then they land on metrics like token consumption.

Or AI-generated lines of code.

That is not just weak measurement. It is management self-parody.

A token count does not tell you whether anything useful happened. It tells you that a machine processed text. That is all. Treating that as evidence of meaningful adoption is like measuring the quality of a construction project by the kilos of cement used, or judging a restaurant by how much gas the kitchen burned.

It is not just incomplete.

It is absurd.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## A token has no business meaning

This should not be controversial, and yet here we are.

A token does not tell you whether a customer problem was solved. It does not tell you whether a team delivered something users actually wanted. It does not tell you whether quality improved. It does not tell you whether cycle time fell. It does not tell you whether rework dropped. It does not tell you whether the organisation learned anything. It does not tell you whether the business is better off.

It tells you that text went in and text came out.

That is not impact.

That is exhaust.

And the fact that something is easy to count does not magically make it strategically meaningful. A dashboard full of clean graphs can still be a dashboard full of nonsense.

## In many cases, more tokens mean more waste

[![](https://substackcdn.com/image/fetch/$s_!r5XD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f90a0cf-1efa-4ec5-a6f3-32a2fb499e0c_1024x559.png)](https://substackcdn.com/image/fetch/$s_!r5XD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f90a0cf-1efa-4ec5-a6f3-32a2fb499e0c_1024x559.png)

This is the part that people conveniently ignore.

A high token count may not mean your teams are getting more value from AI. It may mean they are struggling.

It may mean:

- bloated prompts
- poor problem framing
- repeated retries
- low-quality outputs
- excessive back-and-forth
- generated code that gets thrown away
- workflows padded out to “show adoption”
- teams spending more energy managing the tool than solving the problem

So the same metric that some executive wants to present as proof of progress may actually be evidence of friction, confusion, and inefficiency.

That is what makes it such a dangerous metric. It does not merely fail to measure value. It can point in the wrong direction entirely.

And once a metric like that becomes a target, the organisation starts gaming it. More prompts. More activity. More visible usage. More generated material. More dashboard movement.

More theatre.

**> If your metric rewards more text, more prompts, or more machine output, do not be surprised when people optimise for performance art instead of results.**

## It can also become a metric that rewards higher spend

[![](https://substackcdn.com/image/fetch/$s_!dek-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc60ed007-97eb-4709-87df-8665b3b6e645_1024x559.png)](https://substackcdn.com/image/fetch/$s_!dek-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc60ed007-97eb-4709-87df-8665b3b6e645_1024x559.png)

There is another reason token consumption is a dangerous metric: it can push organisations towards spending more while telling themselves they are succeeding.

This is not some distant possibility. Token-based pricing is already normal across major AI APIs. OpenAI publishes prices per million tokens, Anthropic does the same for Claude, Google documents Gemini billing based on input, output, and cached token counts, and FinOps guidance treats token usage as the primary unit for tracking and attributing generative AI cost. ([OpenAI](https://openai.com/api/pricing/?utm_source=chatgpt.com))

If leadership uses token consumption as a headline KPI for AI adoption while vendors monetise token consumption directly, it risks creating a perverse incentive loop. The more tokens teams consume, the more successful adoption appears internally, even if that same behaviour mainly means higher external cost. That makes the metric worse than merely weak. It becomes economically distorting.

Instead of asking whether teams are delivering more value, reducing toil, improving quality, or making users happier, the organisation starts rewarding the one thing its suppliers already bill for: more machine output.

In that scenario, token consumption stops being a harmless vanity metric. It becomes a mechanism that can legitimise waste.

**> A metric is especially dangerous when it not only fails to measure value, but also rewards spending more money to simulate progress.**

## Counting AI-generated lines of code is the same stupidity with different branding

[![](https://substackcdn.com/image/fetch/$s_!Mvox!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99dd18e4-5acc-4ae9-950d-c96c01b7c261_1024x558.png)](https://substackcdn.com/image/fetch/$s_!Mvox!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99dd18e4-5acc-4ae9-950d-c96c01b7c261_1024x558.png)

Then there is the other favourite: AI-generated lines of code.

This one is almost insulting in how intellectually lazy it is.

The software industry has already been through this. Counting lines of code as a proxy for productivity was a bad idea decades ago. Good engineers are not valuable because they produce the most text. They are valuable because they solve the right problems with judgement, restraint, clarity, and leverage.

Sometimes the best engineering work adds code. Sometimes it removes code. Sometimes it changes almost nothing visible but eliminates risk, ambiguity, or operational pain.

More code is not inherently better.

Quite often it is worse.

More code can mean:

- more maintenance burden
- more bugs
- more accidental complexity
- more review cost
- more regression risk
- more future friction

So when an organisation celebrates AI-generated code volume, what it is often celebrating is surface area. Not value. Not elegance. Not maintainability. Just more stuff.

And “more stuff” has never been a serious north star.

## This is what happens when organisations confuse outputs with outcomes

[![](https://substackcdn.com/image/fetch/$s_!nkc2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f888aa5-1af3-4b63-b18a-d45b76aee9ea_1024x559.png)](https://substackcdn.com/image/fetch/$s_!nkc2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f888aa5-1af3-4b63-b18a-d45b76aee9ea_1024x559.png)

The real issue is not AI.

The real issue is managerial immaturity.

A lot of organisations still do not know how to distinguish output from outcome.

**Output** is what gets produced. **Outcome** is what changes because of it.

That distinction is basic. It should already be built into product thinking, delivery thinking, and leadership thinking. But AI has exposed how many companies still fall for shiny output metrics the moment a new tool arrives.

They do not ask whether users are happier. They do not ask whether the delivery system improved. They do not ask whether valuable work is landing sooner. They do not ask whether quality is holding. They do not ask whether the business is seeing meaningful effects.

They ask how many tokens were used.

That is the managerial equivalent of looking at a car’s fuel consumption and claiming you now understand whether the journey was worth taking.

## What they should be measuring is not mysterious

This is not hard conceptually.

It is only hard politically, because the meaningful metrics are less flattering and require more honesty.

If AI is genuinely helping, you should see signs such as:

- capabilities delivered that users actually wanted
- shorter time from idea to real use
- less repetitive manual work
- more time spent on higher-value work
- fewer defects
- less rework
- better user satisfaction
- stronger adoption in production
- measurable improvement in business goals

Those are imperfect too, but at least they are pointed in the right direction.

They ask whether anything got better.

Token counts do not. AI-generated lines do not. Prompt counts do not. AI-generated commit counts do not.

Those are usage traces. Useful for operational visibility, maybe. Useful for cost control, maybe. Useful for claiming business value, no.

## Tokens belong in finance and operations, not in your success story

There is one place where tokens do matter: cost and usage management.

That is fine.

If you want to understand spend, allocate cost, manage vendors, or monitor tooling usage, count tokens all day. That is exactly the kind of thing they are good for. The FinOps Foundation explicitly frames token usage as the primary unit of measurement for tracking and attributing AI workload costs. ([FinOps Foundation](https://www.finops.org/wg/how-to-build-a-generative-ai-cost-and-usage-tracker/))

But do not pretend that a cost-and-usage metric is suddenly a value metric because you put it on an executive slide.

That is the sleight of hand happening in too many organisations right now. A metric that belongs in finance or platform telemetry gets promoted into a proxy for transformation.

It does not deserve the promotion.

## The deeper problem is what these metrics reveal about leadership

[![](https://substackcdn.com/image/fetch/$s_!GYFA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5176a80c-3a5e-4f68-b346-9fc6dd2e0f95_1024x559.png)](https://substackcdn.com/image/fetch/$s_!GYFA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5176a80c-3a5e-4f68-b346-9fc6dd2e0f95_1024x559.png)

Bad metrics are never just bad metrics. They reveal what leadership actually values.

When leaders obsess over token usage, they are telling the organisation something, even if unintentionally.

They are saying:

- visible activity matters more than validated impact
- tool usage matters more than delivered outcomes
- volume matters more than judgement
- dashboards matter more than users

That is why these metrics are not harmless. They train behaviour. Teams learn what counts by what gets measured. If the signal of success is “use the AI a lot,” then teams will use the AI a lot. If the signal is “generate more code,” then more code will appear.

Whether any of that makes the product better is another question entirely.

And in weak organisations, that second question never gets asked.

**> When an organisation measures AI by token consumption, it is often revealing that it cares more about the appearance of progress than the substance of it.**

That is uncomfortable, but it is true often enough to be worth saying plainly.

## AI does not create value by existing

This is the part that should be obvious and somehow is not.

AI is not valuable because people touched it. It is not valuable because the bill was large. It is not valuable because the output was long. It is not valuable because code appeared quickly.

It is valuable when it helps people achieve something that matters.

That may mean faster delivery. That may mean better decisions. That may mean less toil. That may mean improved quality. That may mean giving skilled people more room for the work that actually requires skill.

But if none of that is happening, then the token count is just an expensive comfort blanket.

## The question leadership should ask

Not:

**How much AI did we use?**

But:

**What got better because of it?**

Did customers get something valuable sooner? Did teams spend less time on drudgery? Did quality improve? Did flow improve? Did more of the right work get finished? Did the business see a result that mattered?

That is the whole conversation.

Everything else is instrumentation, procurement, or vanity.

## Final point

If your organisation measures AI adoption by token consumption, it is not really measuring adoption.

It is measuring throughput from a tool and pretending that throughput is transformation.

That is not serious. That is not rigorous. That is not strategy.

It is just a modern-looking version of an old management failure: mistaking activity for achievement.

So stop counting tokens as if they prove value. Stop counting AI-generated lines of code as if they prove productivity. Stop rewarding volume and calling it innovation.

The business does not need metrics of noise.

It needs metrics of value.

**> The question is not how much AI you consumed. The question is what you achieved because of it.**

If you want, I can give you the exact same piece with a stronger Substack title and subtitle pack.
