---
title: "Introduction to Event Storming"
requested_url: "https://emmanuelvalverderamos.substack.com/p/introduction-to-event-storming"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/introduction-to-event-storming"
substack_post_id: 184021815
retrieved_at: "2026-03-27T08:57:50.929Z"
---
# Introduction to Event Storming

## A business-first, time-based model

EventStorming is a way to understand a business by **telling its story over time**. You model the domain as a **timeline of domain events**: meaningful facts that happened in the business (not in the UI, not in the database). Once that timeline exists, everything else becomes easier: shared language, clearer rules, fewer assumptions, better boundaries, and better software decisions.

This guide focuses on what EventStorming *is*, what each building block means, the different types (Big Picture, Process, Design Level), and how to pick the right one. It is not a facilitation manual.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

### *An Act of Deliberate Collective Learning*

**Concept:** EventStorming is not just about drawing diagrams. It is a workshop format designed to invite the right people (domain experts and engineers) to explore complex business domains. Its goal is to build a shared understanding, identify friction points, and model the software that supports the business.

## The core idea: business reality as a timeline 🕒

Most complexity in software is not technical. It comes from ambiguity: different departments using different words, hidden exceptions, invisible handoffs, and rules that exist “in someone’s head”.

EventStorming attacks that problem by choosing a single, powerful perspective: **time**.

- What happened first?
- What happened next?
- What happens when it fails?
- Who decides, based on what information?
- Where do we wait, and why?

When you put business facts on a wall in sequence, disagreements stop being abstract. They become visible, concrete, and solvable.

## The Grammar (The Visual Language)

EventStorming uses a simple visual language. Colors may vary by team, but the meanings below are widely used and work well because they separate **facts, intentions, decisions, information, and uncertainty**.

### 🟠 Event (fact)

A domain event is **something meaningful that happened in the business**.

- Written in **past tense**
- Names reflect business outcomes: `OrderPlaced`, `PaymentAuthorized`, `RefundIssued`
- Events are the spine of the timeline

Why it matters: events are anchors. People can argue about causes and policies, but the event itself grounds the conversation in reality.

### 🔵 Command (intention)

A command is a **request to do something**. It is not a fact, it is an intention.

- Written in **imperative mood**
- Examples: `PlaceOrder`, `AuthorizePayment`, `CancelOrder`

Why it matters: commands reveal decision points and responsibilities. They force you to ask: “Who can request this, and under what rules?”

- **Relationship:** Command (Cause) → Event (effect)

### 👤 Actor (who triggers a command)

An actor is a **role** that issues a command.

- Prefer roles over individuals: `Customer`, `SupportAgent`, `FinanceClerk`
- A system can be an actor too: `Scheduler`, `FraudService`

Why it matters: actors reveal ownership, handoffs, and where misunderstandings often happen.

### ⚪ Policy (event-to-command automation)

A policy is reactive logic: **when this happens, do that**.

Write policies like:

- “When `PaymentAuthorized`, then `ReserveInventory`.”

Why it matters: policies expose the “invisible glue” that keeps processes moving. They also reveal long-running flows and where automation is assumed but not defined.

### 🟢 Read Model (information needed to decide)

A read model is the information someone needs before issuing a command.

Examples:

- `CartSummary`
- `AvailableStockBySku`
- `OrderStatusTimeline`

Why it matters: read models eliminate magical thinking. If you cannot state what information a decision requires, you cannot implement that decision reliably.

### 🟡 Aggregate (consistency boundary)

An aggregate is the part of the domain model that **decides** whether a command can succeed and which events are produced. It is a consistency and decision boundary.

Examples:

- `Order`, `Payment`, `InventoryReservation`, `Shipment`

Why it matters: aggregates protect invariants (rules that must not be violated), like “cannot refund more than paid” or “cannot ship a cancelled order”.

### 🌸 External System (boundary you do not control)

An external system is something you integrate with but do not control.

Examples:

- payment provider, carrier API, legacy ERP

Why it matters: external systems are where timeouts, partial failures, retries, and unclear contracts live. Modeling them explicitly prevents fragile designs.

### 🔥 Hotspot (risk, ambiguity, conflict)

A hotspot marks uncertainty: open questions, disagreements, risks, or performance concerns.

Examples:

- “Do we allow backorders?”
- “What is the retry policy for payment failures?”
- “Who can cancel after packing?”

Why it matters: hotspots become your backlog of research and decisions. They are a feature, not a failure.

## The three main EventStorming types (and why you use each) 🧭

EventStorming is a family of formats. The grammar stays similar, but the **goal** changes. That is why each type feels different and produces different outcomes.

### Big Picture EventStorming 🌍

**What it is:** a wide, end-to-end view of a business domain modeled as a timeline of domain events.

**Objective:** build shared understanding across the whole system or line of business.

**Participants:** all relevant roles: business experts, product, engineering, operations, support, stakeholders.

**Depth and coverage:** broad coverage, intentionally not deep on implementation details.

**Primary elements:**

- 🟠 events
- 👤 actors
- 🌸 external systems
- 🔥 hotspots, and often ⚪ policies once the story emerges.

**When to use it:**
Use Big Picture when you need alignment and discovery:

- starting large initiatives or transformations
- identifying bottlenecks, risks, and opportunities
- discovering boundaries and handoffs between teams or departments

**Why it beats other types:** it maximizes learning and vocabulary alignment. It prevents building the wrong thing because the domain was misunderstood.

### Process Level EventStorming 🔁

**What it is:** a focused model of a single workflow (returns, billing, onboarding, claims) with explicit branching, rules, and triggers.

**Objective:** understand and improve a specific process in detail.

**Participants:** the people closest to the process plus the people who will implement change.

**Depth and coverage:** medium depth, narrow scope.

**Primary elements:**

- 🟠 events
- 🔵 commands
- 👤 actors
- ⚪ policies
- 🟢 read models
- 🔥 hotspots

**When to use it:**
Use Process Level when:

- a particular workflow is slow, buggy, or controversial
- you need clarity on “what happens if…” cases
- you are evolving an existing system and must avoid accidental regressions

**Why it beats Big Picture:** it goes deep where it matters, without turning into architecture too early.

### Design Level EventStorming 🏗️

**What it is:** a model that connects the business timeline to buildable software design decisions: aggregates, command handling, policies, read models, and boundaries.

**Objective:** produce an implementable design for a specific domain area or feature.

**Participants:** primarily developers and architects, with domain experts involved to validate rules and language.

**Depth and coverage:** deep and convergent.

**Primary elements:**

- 🟠 events
- 🔵 commands
- ⚪ policies
- 🟢 read models
- 🟡 aggregates
- 🌸 external systems
- 🔥 hotspots.

**When to use it:**
Use Design Level when:

- you are preparing to implement a feature or a bounded context
- you must define invariants, ownership, and responsibilities
- you want a design that is robust under real business exceptions

**Why it beats Process Level:** it turns understanding into concrete software boundaries and consistency rules.

### A practical note on “Exploratory” 🧪

Many teams also run lightweight exploratory sessions early on: short, creative discovery to generate ideas and hypotheses. Think of it as “Big Picture energy” with less commitment to completeness.

## The Dynamics: The Workshop Flow

A session is never linear; it oscillates between chaotic exploration and structured enforcement.

### Phase 1: The Storm (Chaotic Exploration)

- **Goal:** Dump the brains of all participants onto the wall.
- **Action:** Everyone grabs orange stickies and markers. Everyone writes simultaneously. No turn-taking.
- **Rule:** “If you think of an event, write it.” Place them on the wall in a rough timeline (Past $\rightarrow$ Future).
- **Outcome:** A messy, duplicated, comprehensive list of everything that happens in the business.

### Phase 2: Enforce the Timeline

- **Goal:** Create a single, consistent narrative.
- **Action:** The Facilitator asks the group to clean up.
	- Remove duplicates.
	- Fix the grammar (ensure past tense).
	- Clarify the sequence: “Does `InvoiceCreated` happen before or after `GoodsShipped`?”
- **Outcome:** The emergence of **Hot Spots** (Purple). This is where business processes break, and where the most value is found.

### Phase 3: The Reverse Narrative

- **Goal:** Validate integrity.
- **Action:** Walk the wall backwards from the end to the beginning.
- **The Question:** “What *must* have happened immediately before this event to make it possible?”
- **Outcome:** This exposes “magic” steps where events appear without a cause. It forces the discovery of missing Commands or Policies.

### Phase 4: Explicit Walkthrough (Categorization)

- **Goal:** Define boundaries.
- **Action:** Identify **Pivotal Events** (major state changes, e.g., `ContractSigned`). Use these to group events into potential modules or **Bounded Contexts**.
- **Outcome:** A visual map of your system architecture and team responsibilities.

## How to choose the right type

- If you want to understand the entire business domain over time: **Big Picture**.
- If you want to optimize or clarify one workflow: **Process Level**.
- If you want to design software boundaries and invariants for implementation: **Design Level**.
- If you are ideating early and want fast discovery: a short **exploratory-style** session can be useful.

[![](https://substackcdn.com/image/fetch/$s_!KlKO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f2069a7-8ef6-46ae-bafa-af8fc6bf2cd8_9313x5261.jpeg)](https://substackcdn.com/image/fetch/$s_!KlKO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f2069a7-8ef6-46ae-bafa-af8fc6bf2cd8_9313x5261.jpeg)

## Workshop patterns that keep sessions productive 🧩 (Optional)

This guide is not a facilitation manual, but there are a few workshop “patterns” that show up again and again in successful EventStorming sessions. Think of them as small rules of thumb that protect the learning dynamics: parallel thinking, low friction, and visible decisions.

I’m listing them here because they map directly to the workshop flow above, and they work **both in-person and remote** (sometimes with a different implementation).

### 1) Set the conditions for parallel thinking

#### ♾️ Unlimited modelling space

**Applies to:** Big Picture, Process, Design (in-person + remote)

**Idea:** remove “scarcity” from the room (space, materials, or board area), so people don’t unconsciously compress the model.

- In-person: paper roll &gt; whiteboard, plenty of stickies and markers.
- Remote: an “infinite canvas” board (Miro/Mural/FigJam), with enough space + frames, and a visible legend area that doesn’t get buried.

**Why it matters:** if people feel the surface is limited, they will simplify early and zoom into a local area too soon.

#### ✍️ One person / one writing tool (remote adaptation)

**Applies to:** Big Picture (originally in-person)

**Idea:** avoid “scribe mode”. Everyone should be able to contribute in parallel.

- In-person: one marker per person.
- Remote: everyone gets editing permissions and is expected to create/edit stickies themselves (not dictating to a single person sharing screen).

**Why it matters:** when writing becomes centralized, you get committees, slower discovery, and some voices dominate by default.

#### 🧭 Open invitation (informed self-selection)

**Applies to:** Big Picture, Process, Design (in-person + remote)

**Idea:** don’t over-optimize attendee selection with titles. Secure the key roles you need, make the invitation visible, and let motivated people self-select.

**Why it matters:** commitment and proximity to the work predict contribution better than org charts.

### 2) Keep beginners in the zone (Big Picture)

#### 🪜 Incremental notation

**Applies to:** Big Picture

**Idea:** introduce notation only when it becomes necessary.

- Start with 🟠 Events (and correct past tense).
- When the group hits “what triggers this?” add 🔵 Commands and 👤 Actors.
- When “what happens next automatically?” appears, add ⚪ Policies.
- When decisions require data, add 🟢 Read Models.
- Keep a visible legend, and expand it step by step.

**Why it matters:** big upfront explanations increase cognitive load and trigger question spirals before people have any tangible experience.

#### 🏊 Do first, explain later

**Applies to:** Big Picture

**Idea:** let people touch the problem immediately. Give only the minimum rules to start, then explain in response to real questions.

- Kick off with: “Write domain events you know happened. Past tense. Place them on the timeline.”
- Clarify as you go, and normalize imperfection early (“we’ll refine together”).

**Why it matters:** experience creates the mental hooks that make explanations stick.

#### 🌫️ Fuzzy definitions (early exploration)

**Applies to:** Big Picture, Process, Design (in-person + remote)

**Idea:** allow “good enough” language early, and delay precision until the model demands it.

- If terms clash, keep both interpretations visible and mark the pressure points as 🔥 Hotspots.
- Use the visible legend as “current meaning”, not as a rigid formal spec.

**Why it matters:** forcing strict definitions too early shuts down discovery and filters out valuable dissonant perspectives.

### 3) Converge without getting stuck (Process + Design)

#### 🏁 Rush to the goal

**Applies to:** Process Level, Design Level

**Idea:** build the baseline path end-to-end first. Defer alternatives and objections into 🔥 Hotspots.

- “Let’s reach a valid end state quickly.”
- “We’ll come back to edge cases; capture them as hotspots now.”

**Why it matters:** branching too early overwhelms the group and creates standoffs instead of progress.

#### 🧗 Raise the bar

**Applies to:** Process Level, Design Level

**Idea:** once the baseline exists, pull hotspots and corner cases back in to stress-test the model.

- Add retries, failures, timing issues, exceptions.
- Keep an eye on user experience and complexity creep.

**Why it matters:** “happy path only” designs look clean and fail in production. Corner cases reveal where invariants and responsibilities really live.

#### 🗣️ Speaking out loud

**Applies to:** Process Level, Design Level

**Idea:** regularly narrate the story of the model out loud while pointing at the stickies.

- In-person: walk the wall.
- Remote: one person “drives” the board for a minute while narrating, others listen and drop corrections/hotspots.

**Why it matters:** silent reading makes weak models feel plausible. Spoken storytelling exposes gaps, contradictions, and missing steps.

#### ⏱️ Time-boxed leadership

**Applies to:** Process Level, Design Level

**Idea:** when consensus slows everything down, appoint a short-lived “driver”.

- For 2–5 minutes, one person can move stickies, choose the next step, and push the group forward.
- Everyone else writes objections as 🔥 Hotspots instead of interrupting.

**Why it matters:** it breaks analysis paralysis without silencing dissent—you’re just deferring debate into a visible backlog.

### 4) After the workshop: keep the learning going

#### 🧲 Leave stuff around (persistent artefact)

**Applies to:** Big Picture

**Idea:** the workshop isn’t really over when time ends. Keep the model accessible so late insights can land.

- In-person: keep the wall up longer or move it somewhere visible.
- Remote: keep the board link open and invite async comments for a few days.

**Why it matters:** people process complex domains slowly; the best insights often arrive after the session.

#### 🤝 Make yourself available

**Applies to:** Big Picture (in-person + remote)

**Idea:** make space for the “extra conversations” that don’t fit the group format.

- Leave slack time right after the workshop (or the next morning).
- Remote: keep a follow-up channel alive (board comments + chat thread), and visibly check/respond.

**Why it matters:** high-signal details often emerge in smaller follow-ups—especially from quieter participants.

## Three examples

The fastest way to learn EventStorming is to see the same grammar applied at different scales.

[![](https://substackcdn.com/image/fetch/$s_!iEn7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd53db7af-8f6d-49ed-b599-9d6de4b27fb8_2613x297.png)](https://substackcdn.com/image/fetch/$s_!iEn7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd53db7af-8f6d-49ed-b599-9d6de4b27fb8_2613x297.png)

### Simple “Hot Dog Stand” 🌭

This is intentionally tiny. The goal is to feel the difference between “facts” and “intentions”.

**Business timeline (events):**

- 🟠 `OrderPlaced`
- 🟠 `HotDogPrepared`
- 🟠 `OrderServed`
- 🟠 `PaymentCollected`

**What makes it interesting:** even here, reality bites.

- What if the customer cancels after the hot dog is prepared?
- Do we collect payment before serving, or after?

A minimal diagram:

[![](https://substackcdn.com/image/fetch/$s_!-edh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2159cb6b-266c-47b8-b492-c3389f9da205_2613x297.png)](https://substackcdn.com/image/fetch/$s_!-edh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2159cb6b-266c-47b8-b492-c3389f9da205_2613x297.png)

[Live editor](https://mermaid.live/edit#pako:eNqVlG1r2zAQx7-KUCl0kGSRn62xjcQP9EVLs2RQNnsvhC0nprbkyXIfVvrdJz80SZMOMoPBuvvf7053h59hwlMKMcwK_pBsiJDgahmz83Pw-e0Dwqub20NjzGaR19SSl1T8whiTRHIBxuMvwEPRoiAJvRFp70p4WRKWxsxDnSBAUefrVGmroPeUyZjFLOgVCxTdbigDezLQmgWtiKCXXPp83cZVvMiTp5gt-jBPi44ku-Ran1yLeuegPMjfizw9WlFx_94V9J6i91foVAeIXuEZkceLgiZyQZ5K5XuLMXqMEQ3eQXvAUrNYUpKCUg2qqMFFzjIuSiJzzgCjNFVtmQfhzTIAKU3yWpnrDzFbXqPomrJmxtKFyBNat0yhOB0GjCfdkFqdFn1raENXksjmPdVsKEJ1rK7UCy54pcbyu6F1W0MNPgKR13dt0qFzlygaxBgkw3qAgpJ7WgOSSXXIOE9BNTT_a5t00wcMuQ6Xb_X9x1WwOl6_pCB17dMM9JuX5UWBz8Iw1DxvVEvB7yg-c113-B4_5KncYFQ9jhJecIHPEEKf9ijDaAaOG3pm4Gw52tx2AuNUVDe-14KsuWbNt6C5YYZT6y1I-yeoX--B5Lu-FrhbkmUbwcw-tSSyXgu6JpJu--S7lrUrK3Sn0-mpsN2S9LC55duzXbN0x7aQf3KzHtVSMPLKCg3P2xug503_o7BhkQZUMLWsvTu67jHqqPVwBNciTyGWoqEjqJa3JO0RPscMgBjKDS1pDLH6TGlGmkLGMGYvKqwi7Cfn5Wuk4M16A3FGilqdmipVvfdzshak3FoFZeoX4vGGSYh11DEgfoaPEI_RFDkTzbR023Z0wzLVReATxKaOJoap6Y5jG7qr_C8j-KdLq08MZDimY9qupZuW9vIX72jpMA)

```
flowchart LR
%% =============== FLOW ===============
A[Customer]:::actor --&gt; C1[PlaceOrder]:::command
C1 --&gt; E1[OrderPlaced]:::event

E1 --&gt; P1[When OrderPlaced -&gt; PrepareHotDog]:::policy
P1 --&gt; C2[PrepareHotDog]:::command
C2 --&gt; E2[HotDogPrepared]:::event

E2 --&gt; C3[ServeOrder]:::command
C3 --&gt; E3[OrderServed]:::event

E3 --&gt; C4[CollectPayment]:::command
C4 --&gt; E4[PaymentCollected]:::event

%% Read models (information needed BEFORE decisions)
RM1[MenuAndPrices]:::readmodel -.-&gt; C1
RM2[QueueStatus]:::readmodel -.-&gt; A

%% Hotspots (open questions / risks)
E2 --&gt; H1[Hotspot: customer leaves after food prepared?]:::hotspot

%% =============== STYLES ===============
classDef actor fill:#FFF2CC,stroke:#999,stroke-width:1px,color:#111;
classDef command fill:#9FC5E8,stroke:#2B78E4,stroke-width:1px,color:#111;
classDef event fill:#F6B26B,stroke:#B45F06,stroke-width:2px,color:#111;
classDef policy fill:#D9D2E9,stroke:#674EA7,stroke-width:1px,color:#111;
classDef aggregate fill:#FFD966,stroke:#BF9000,stroke-width:1px,color:#111;
classDef readmodel fill:#B6D7A8,stroke:#38761D,stroke-width:1px,color:#111;
classDef external fill:#F4CCCC,stroke:#CC0000,stroke-width:1px,color:#111;
classDef hotspot fill:#E06666,stroke:#990000,stroke-width:2px,color:#111;
```

### Intermediate “Gym Membership” 🏋️‍♀️

Now we add rules, branching, and a read model.

**Scenario:** a user signs up for a gym. If payment succeeds, membership activates. If payment fails, membership stays pending. Support can cancel.

This is small enough to understand quickly but rich enough to teach real modeling.

[![](https://substackcdn.com/image/fetch/$s_!Dr0c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F887be258-bfea-4ea9-94d5-df1b670a7192_2613x413.png)](https://substackcdn.com/image/fetch/$s_!Dr0c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F887be258-bfea-4ea9-94d5-df1b670a7192_2613x413.png)

[Live Editor](https://mermaid.live/edit#pako:eNqVlG1vmzAUhf-K5WpSJyUdEMLbtE0JgfZDu0XptHWDffDghlgFmxmTtqv632dekiZpK3WRkDA5fu7x8bXvccJTwB5e5vwmWREh0fkiZm_eoA_7PxSef_l--DFmk2gueFVCIn95nkcSyQUaDj8iX48W8KeGSl5A8RtEtaJlo0h4URCWxszXW93kVI_2FSTLBGREgoKfdqJgV9NjIW3EsAYmYxazoFPO9ej7Chh6Ro4aV2qBGYRUVHJO7go1t4GUPKfJXczmHcM3oud1j96NVnilR_2_SIWwpimI1tOtBMFI3ti66hdgbJSTWq64oH_37G9V4UYWEpofrrAr6o-iSSLpWgX0UrKjTbI7CY52EtzMP-SHXQEz-swlXd7tWKkF7JcwO6oZ7YvaifQArHppASRFhWq0vELHlC25KIiknCEGkKqtmQbhl0WAUkhopT5Xb2O2uFDp5oT5RJKcZxOWzgVNKMsatlC8FoeGJ22zNXqjX-KlJLKuvlG4eUY66R2dcVmV6kHHvFT90vZIUxm9Q4JW142DTSBnetSrPSRACgoVWlcoEyQBVIKgPG3GCWEJ5Hm7rk9N5VU3qS94eJwuv_44Dy6fHqgkJ1U1gyXqztKS5rl3FIah4fuDSgp-Dd6R67r9-_CGpnLl6eXtIOE5F96Rruvvdyj9lvUcN_THgbPlGFPbCczXotoN3RiypoY13YKm5jjUrH2Q8SKoO289aebOjMDdkizbDCb2ay1t74ptTjPXsh5tha6maa-FPXZKB5taM3vyGNbIsS199uqw-ktgY8z0_Z0N9H3tP4z1jdSjAs2ydtbouk9RT6LHA5wJmmJPihoGuAB1_pohvo8ZQjGWKyggxp56TWFJ6lzGOGYPalpJ2E_Oi81Mwetshb0lySs1qstUZT-jRJ2FYvtVAFM3oc9rJrGnO-MWgr17fIu9oW5qJ46tTLu25Ri2azoDfIe9kWOcjA13NDYsxxxrjmU-DPDftrB-YmiuZo2V1jVN2xoZD_8ACqo1mg)

```
flowchart LR
%% =============== FLOW ===============
A[Prospect]:::actor --&gt; C1[RequestMembership]:::command
C1 --&gt; AG1[Membership]:::aggregate
AG1 --&gt; E1[MembershipRequested]:::event

E1 --&gt; P1[When MembershipRequested -&gt; ChargeFirstPayment]:::policy
P1 --&gt; C2[ChargeFirstPayment]:::command
C2 --&gt; X1[Payment Provider]:::external

X1 --&gt; E2[PaymentAuthorized]:::event
X1 --&gt; E2F[PaymentFailed]:::event

E2 --&gt; C3[ActivateMembership]:::command
C3 --&gt; AG1
AG1 --&gt; E3[MembershipActivated]:::event

E2F --&gt; C4[NotifyPaymentFailure]:::command
C4 --&gt; E4[PaymentFailureNotified]:::event

%% Read models (information needed BEFORE decisions)
RM1[PlanCatalogAndPricing]:::readmodel -.-&gt; C1
RM2[MemberStatusView]:::readmodel -.-&gt; A

%% Hotspots (open questions / risks)
E2F --&gt; H1[Hotspot: retries vs grace period vs cancellation?]:::hotspot

%% =============== STYLES ===============
classDef actor fill:#FFF2CC,stroke:#999,stroke-width:1px,color:#111;
classDef command fill:#9FC5E8,stroke:#2B78E4,stroke-width:1px,color:#111;
classDef event fill:#F6B26B,stroke:#B45F06,stroke-width:2px,color:#111;
classDef policy fill:#D9D2E9,stroke:#674EA7,stroke-width:1px,color:#111;
classDef aggregate fill:#FFD966,stroke:#BF9000,stroke-width:1px,color:#111;
classDef readmodel fill:#B6D7A8,stroke:#38761D,stroke-width:1px,color:#111;
classDef external fill:#F4CCCC,stroke:#CC0000,stroke-width:1px,color:#111;
classDef hotspot fill:#E06666,stroke:#990000,stroke-width:2px,color:#111;
```

What you learn here:

- 🔵 commands can fail, 🟠 events do not “fail”
- 🟢 read models define what someone must know to act
- 🌸 external systems create uncertainty and hotspots

### Complete “Marketplace Order Fulfillment” 🛒📦💳

This is a realistic domain with payments, inventory, shipping, and failure modes. It demonstrates how Design Level EventStorming connects business behavior to software design concepts.

[![](https://substackcdn.com/image/fetch/$s_!VgFN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3608a135-2820-4c9f-8752-40c892d66912_2587x236.png)](https://substackcdn.com/image/fetch/$s_!VgFN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3608a135-2820-4c9f-8752-40c892d66912_2587x236.png)

[Live editor](https://mermaid.live/edit#pako:eNqVlf-P2jYYxv8VK6dKnQY38p1k2iQISVvppougUm8L-8FNDFgkNrUdevR0__uc2BACTLuBkEL8-OPnef3GeTFyWiAjNFYl_Z5vIBPgYb4kzffdO_Bb_wOSh8cvlzeXZJJFNRe0QuzvMAxhLigDw-HvIDKztIQ5emSFGsppVUFSLElktoLJBzM7DcL1mqE1FEgCP6jxWA-3lKIRoT0iojEXK0VqZl82iIAzGZC35-hbjbhI4aGS-kktNpThH1BgShrKjpY4PyxJqiCRlf3HhM641c54ksmUFKSM7rGOgJ4FYgSWjcEnHcHKLqC9ICdVkt1aO4G4vAyuHKSWCn4FV_E5Ynv0iTSTKDv0Mqv5kZ3dUnVBbb1DVnYSqAmnovQ2TFFj-1Ldc9_JkpvUW3GVj9RWca_oTdyIIekixfn2AXPRC6tmR052remiOjqqXAMytKE1R1f5FCh2siNCAS_MKlLkys3Mtzfa3lUUV7e1FF0SlCJ1ztu6lTVBZ5jvoMg3iw3eNbvei6rX9rJbqs6CpxrYyiLIGEYMTNJP_d590pvkZUfCkXhpVrFSV5m9VrebA3eiZkj3ac-xyhr52bWm8-srM_7x-dDavhN5VM0RLEAlz7KSg_eYrCir2p4CBKFCWpnGyeM8BgXKMZe3-U9LMv_DbKogFrVcTPW_3NSihYDhfXuCNSorm-xlZ8KvJVoImm-nh8W2vqW2G7WtNnchoKj5Z1yhEhN0Qz3Rxj9SwXfyB97Tnaxiew41BsEvgGG-bYzK46Gtwkcz0-oQMCTYAbC6RBz8DHJ9AIMKcQ7XmKybFTdK3DxFGmB1gK-yrWjjFOw5yCHJpTF5xXclFoCf9c6JcvOVsPj850O8uH4p5CXkfIZWQL0PVrgsw7skSawoGnDB6BaFd0EQ6Ovhd1yITWjungc5LSkL70zT_PWMohtCc4IkcuPxiWNN_XHsvBXVds3RkDe1vOkJNHXcZOT1Qda_glQja9IsmFlxcCJ5vhNP_LdaOh01pzrNAs_rbCXBaDR6K6zrMwWbejN_0hXLHvueOXtzsfSxcDTmRNHZBkbR6H8Y042kUfHI884yBsE16qr0xsBYM1wYoWA1Ghiy4SvY_DVelgSApSE2qEJLI5SXBVrBuhRLY0le5bQdJH9RWh1nMlqvN0a4giWX_-pdIWs_w3DNYCdBRD4cEa2JMEJz5I9aiBG-GM9GODRH5vjecj3b98e247kyiXEwQtc27x3Xssdj37EDOf46MH6069r3jumM3bHrB57tetbrP2IxKe8)

```
flowchart LR

%% =============== FLOW ===============
A[Customer]:::actor --&gt; C1[PlaceOrder]:::command
C1 --&gt; AG1[Order]:::aggregate
AG1 --&gt; E1[OrderPlaced]:::event

E1 --&gt; P1[When OrderPlaced -&gt; RequestPaymentAuthorization]:::policy
P1 --&gt; C2[RequestPaymentAuthorization]:::command
C2 --&gt; X1[Payment Provider]:::external

X1 --&gt; E2[PaymentAuthorized]:::event
X1 --&gt; E2F[PaymentAuthorizationFailed]:::event

E2 --&gt; P2[When PaymentAuthorized -&gt; ReserveInventory]:::policy
P2 --&gt; C3[ReserveInventory]:::command
C3 --&gt; AG2[InventoryReservation]:::aggregate
AG2 --&gt; E3[InventoryReserved]:::event
AG2 --&gt; E3F[InventoryReservationFailed]:::event

E3 --&gt; P3[When InventoryReserved -&gt; CreatePickList]:::policy
P3 --&gt; C4[CreatePickList]:::command
C4 --&gt; AG3[Warehouse]:::aggregate
AG3 --&gt; E4[PickListCreated]:::event

E4 --&gt; C5[PackOrder]:::command
C5 --&gt; E5[OrderPacked]:::event

E5 --&gt; P4[When OrderPacked -&gt; DispatchShipment]:::policy
P4 --&gt; C6[DispatchShipment]:::command
C6 --&gt; X2[Carrier API]:::external
X2 --&gt; E6[ShipmentDispatched]:::event

E6 --&gt; P5[When ShipmentDispatched -&gt; CapturePayment]:::policy
P5 --&gt; C7[CapturePayment]:::command
C7 --&gt; E7[PaymentCaptured]:::event

%% Read models (information needed BEFORE decisions)
RM1[CartSummary]:::readmodel -.-&gt; C1
RM2[AvailableStockBySku]:::readmodel -.-&gt; C3
RM3[OrderStatusTimeline]:::readmodel -.-&gt; A

%% Hotspots (open questions / risks)
E2F --&gt; H1[Hotspot: retry rules + customer messaging]:::hotspot
E3F --&gt; H2[Hotspot: backorder vs cancel vs split shipment]:::hotspot

%% =============== STYLES ===============
classDef actor fill:#FFF2CC,stroke:#999,stroke-width:1px,color:#111;
classDef command fill:#9FC5E8,stroke:#2B78E4,stroke-width:1px,color:#111;
classDef event fill:#F6B26B,stroke:#B45F06,stroke-width:2px,color:#111;
classDef policy fill:#D9D2E9,stroke:#674EA7,stroke-width:1px,color:#111;
classDef aggregate fill:#FFD966,stroke:#BF9000,stroke-width:1px,color:#111;
classDef readmodel fill:#B6D7A8,stroke:#38761D,stroke-width:1px,color:#111;
classDef external fill:#F4CCCC,stroke:#CC0000,stroke-width:1px,color:#111;
classDef hotspot fill:#E06666,stroke:#990000,stroke-width:2px,color:#111;
```

Why this example is “expert level”:

- 🟡 aggregates reveal where invariants live (Order, InventoryReservation)
- ⚪ policies reveal automation and orchestration
- 🌸 external systems force reliability decisions (timeouts, retries, idempotency)
- 🔥 hotspots show what must be decided for a robust system design

## What you can produce from EventStorming

EventStorming is valuable because it creates multiple outcomes that are hard to get any other way:

### A shared ubiquitous language 🗣️

If business and engineering agree on words like “Authorized”, “Captured”, “Refunded”, your code, tests, dashboards, and support playbooks stop drifting apart.

### Clear rules and exceptions ⚖️

Policies and hotspots make “it depends” visible. You can list the real decision rules and the real failure modes.

### Better boundaries and architecture decisions 🧱

As the timeline grows, natural seams appear: changes in vocabulary, ownership, and rules. Those seams often map to modules or bounded contexts.

### Better delivery slices 🚀

Once you have commands, events, and read models, you can slice work by business outcome:

- “Customer can place an order and see its status”
- “Inventory is reserved after payment authorization”
- “Shipment dispatch triggers payment capture”

Those slices are meaningful, testable, and align with how the business measures success.

## Common mistakes that block mastery

**Mistake: writing UI actions as events.**
Fix: events are business facts, not clicks.

**Mistake: treating commands like facts.**
Fix: commands request change. Events state change.

**Mistake: ignoring read models.**
Fix: every decision needs information. Name the view.

**Mistake: modeling only the happy path.**
Fix: ask “what if it fails?” and capture hotspots.

**Mistake: jumping to microservices too early.**
Fix: start with business reality over time, then decide boundaries.

## Conclusion: what “expert” looks like 🎯

You are fluent in EventStorming when you can:

- create a clean business timeline 🟠⏱️
- distinguish facts from intentions 🟠 vs 🔵
- express automation and rules ⚪
- name the information needed to decide 🟢
- assign invariants to decision boundaries 🟡
- surface uncertainty without hiding it 🔥
- choose the right type (Big Picture, Process, Design) for your question 🧭

At that point, EventStorming stops being “stickies on a wall” and becomes a repeatable way to build shared understanding and better systems.

## Why This Works (The Philosophy)

- **Ubiquitous Language:** By the end of the session, Developers and Salespeople are using the same words. If the sticky says `OrderConfirmed`, the code class should be named `OrderConfirmed`.
- **Visualizing the Invisible:** Software is usually abstract. EventStorming makes it physical and tangible.
- **Active Learning:** You cannot learn a domain by reading a 200-page requirement document. You learn it by asking questions and moving stickies.

## An example app

My friend **[Jesús Mª Villar Vazquez](https://www.linkedin.com/in/geeksusma/)** after reading my post build this app following the article, and I think is a nice example of how to build something, just following the article.

[https://github.com/geeksusma/food-ordering/tree/main](https://github.com/geeksusma/food-ordering/tree/main)

## References 📚

- Alberto Brandolini, *Introducing EventStorming* (Leanpub).
- Alberto Brandolini, *Patterns and antipatterns of EventStorming*. [https://www.eventstorming.com/patterns/](https://www.eventstorming.com/patterns/)
- Alberto Brandolini, *Event Modeling and Event Sourcing* (Leanpub).
- Adam Bellemare, *Building Event-Driven Microservices: Leveraging Organizational Data at Scale*.
- Stefan Hofer, Henning Schwentner, *Domain Storytelling*.
