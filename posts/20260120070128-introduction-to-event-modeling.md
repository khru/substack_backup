---
title: "Introduction to Event Modeling"
requested_url: "https://emmanuelvalverderamos.substack.com/p/introduction-to-event-modeling"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/introduction-to-event-modeling"
substack_post_id: 184032606
retrieved_at: "2026-03-14T08:29:38.046Z"
---
# Introduction to Event Modeling

Event Modeling is a method for **documenting system behavior and requirements over time** using a single, end to end visual model. Instead of splitting requirements across separate artifacts (UI flows, API docs, data models, business rules, acceptance criteria), Event Modeling puts them on **one horizontal timeline** so you can read the system like a story: what a user sees, what they do, what the system records, and what changes for everyone afterward. ([Event Modeling](https://eventmodeling.org/?utm_source=chatgpt.com))

At its core, Event Modeling treats software as an information machine:

- **Intent** (a user or automation issues a command)
- **Fact** (the system records an event)
- **Visibility** (views/read models are updated so users and other processes can see new information) ([Event Modeling](https://eventmodeling.org/posts/event-modeling-cheatsheet/))

This guide focuses on **what Event Modeling is**, **why it works**, and **how to read and build models that are implementation-ready**. It is not a facilitation guide.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## Event Modeling vs EventStorming (They are related, not the same)

**EventStorming** is primarily a collaborative learning and discovery technique. You explore a business domain through domain events on a timeline, uncovering hotspots, language, boundaries, and opportunities.

**Event Modeling** takes a different stance: it is a **requirements and system specification method** that connects user experience and behavior to the internal information flow, so the model becomes a blueprint for building and testing. ([Event Modeling](https://eventmodeling.org/))

A practical way to remember the difference:

- 🌪️ **EventStorming**: “What happens in the business and why?” (explore and discover)
- 🧭 **Event Modeling**: “What exactly must the system do and show, step by step?” (specify and design)

Even when you do not build an event-sourced system, Event Modeling can still be used because an “event” in the model simply means “this information was persisted” (the storage technology is not the point).

## The mental model: information flow over time

Event Modeling works on a **single timeline**, left to right. Each step shows how information changes and becomes visible. Done well, it removes “magic” from requirements: if a screen shows a value, the model forces you to explain where that value comes from.

Think of the model as a storyboard that answers, in one place:

- What does the user see now?
- What action do they take?
- What does the system record as a fact?
- What becomes visible afterward, and to whom?

This is why Event Modeling is often described as “white box requirements”: you are not just describing outcomes, you are describing **how the system produces those outcomes as information**.

## The notation: the minimal vocabulary

[![](https://substackcdn.com/image/fetch/$s_!kBaS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab90a73b-2f36-4470-a016-0522284bb563_2613x244.png)](https://substackcdn.com/image/fetch/$s_!kBaS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab90a73b-2f36-4470-a016-0522284bb563_2613x244.png)

Many teams introduce Event Modeling using only four core elements:

### ⚪ UI / Wireframe (white, dashed)

A rough sketch of what a user sees and where they act. It is deliberately low fidelity: enough to anchor conversations about **data and behavior**, not visual design.

### 🔵 Command (blue)

The user’s (or automation’s) **intent** sent to the system. Commands express what should happen.

### 🟧 Domain Event (orange)

A durable **fact**: something the system records as having happened. Events express what happened.

### 🟩 Read Model / View (green)

A queryable projection derived from past events. A key rule: **read models only read data that already exists as stored events**, which is what makes the model precise and testable.

Most real systems also need two more concepts, and they fit naturally:

### 🟣 Automation / Policy (lilac)

Background work triggered by an event (or timer, or sometimes a user interaction). Example: “when UserRegistered, send welcome email.”

### 🌸 External System (pink)

An integration boundary. Event Modeling supports external inputs using an “external event” concept and translation patterns so you can model integrations without committing to technologies too early.

And one element is hugely useful during modeling:

### 🟥 Hotspot (red)

Open questions, risks, disagreements, or “we need a business decision here.”

## The Slice: the golden rhythm of Event Modeling

The heart of Event Modeling is the **Slice**: a small, complete loop of behavior that you can build and test independently.

A typical slice looks like this:

**UI → Command → Event → Read Model → UI**

Many teams describe slices using **Given / When / Then** (from BDD). In Event Modeling this is not just text; it is a way to attach precise rules to each slice and later turn them into executable tests.

A powerful habit here is working backwards:

- From a UI element you need to show, define the **read model fields**
- For each read model field, identify the **event(s)** that provide that data
- For each event, define the **command** that must have produced it

This backwards reasoning keeps the conversation grounded in facts: what information must exist, and how it flows.

## The Information Completeness Check (Reframed so it actually makes sense)

You were right to question point “5” as it is often explained poorly.

The **Information Completeness Check** is not a “step” and it is not bureaucracy. It is a simple invariant:

> If a screen shows a piece of information, the model must prove where that information comes from, via events.

Concretely, it forces you to validate two mappings:

- **Read Model → Event(s)**
	Every attribute in a read model must be traceable to one or more stored events. If you cannot trace it, the team is assuming data exists when it does not.
- **Event → Command**
	If an event records a field, the triggering command must have provided that field (or it must be derivable in a way the team explicitly agrees on).

This check is valuable because data-assumption mistakes are expensive: teams discover missing fields, missing identifiers, or missing sources late, during implementation. Event Modeling surfaces those gaps early.

## Why Event Modeling works (Benefits that matter in practice)

### One blueprint, not a pile of diagrams

Event Modeling can unify UI thinking, behavior, and data flow into a single artifact that stays readable. It is explicitly designed as a “single source of truth” style model. ([Event Modeling](https://eventmodeling.org/))

### “No magic data”

Because views must be fed by events, the model pressures teams to stop hand-waving about “the database will have it.”

### Better slicing and more predictable planning

A slice is a unit of behavior small enough to estimate, implement, and verify. Some Event Modeling literature explicitly maps slices to work items and uses slice counts plus cycle time to forecast delivery more mechanically than abstract story points. ([Event Modeling](https://eventmodeling.org/posts/what-is-event-modeling/))

### Strong bridge between UX and backend

Wireframes are not “extra.” They are a way to align everyone on what information is shown and captured, and to anchor data discussions in concrete user interactions.

### Cleaner event design and evolution

Event Modeling tends to produce better events because it treats events as business facts that must carry the data needed downstream. Event design guidance from event-driven architecture literature reinforces this: avoid “overloaded” events with type fields that change meaning, keep events focused on a specific occurrence, and include the right data to make the event useful as a contract.

## How to choose scope (model boundaries without turning it into a workshop manual)

Event Modeling scales, but the most practical way to avoid messy models is to choose one of these scopes:

- **Single use case / customer journey** (best starting point)
	Example: “Change password,” “Add item to cart,” “Book a room.”
- **A full business workflow**
	Example: “Order to cash,” “Claims processing,” “Hotel booking with inventory and notifications.”
- **A system slice across boundaries**
	Example: “Inventory updates from an external system and how they change UI.”

A useful rule: start small enough that you can finish a clean timeline, then expand by adding slices that reuse existing views and commands.

## Three examples

Below are three **consistent Mermaid diagrams** using your legend and styles, with **square events** in all graphs.

[![](https://substackcdn.com/image/fetch/$s_!RuUb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3a3f2c4-b607-4578-9644-8db4bc5b5da4_2613x241.png)](https://substackcdn.com/image/fetch/$s_!RuUb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3a3f2c4-b607-4578-9644-8db4bc5b5da4_2613x241.png)

### Change Password

[![](https://substackcdn.com/image/fetch/$s_!mUEA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F700f5844-8411-4185-a184-511d4160d628_2613x1376.png)](https://substackcdn.com/image/fetch/$s_!mUEA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F700f5844-8411-4185-a184-511d4160d628_2613x1376.png)

[Live editor](https://mermaid.live/edit#pako:eNptVNty2jAQ_ZUdPdGpSWObQqKHzGRILzy0gVLSmQ4virWAWluikoxLM_n3rnxLWvLARdY5e86eXXhgmZHIOHP4q0Sd4Y0SWyuKtQYQpTe6LO7R1qfMGwsrEA5Wrnm0F9arTO2F9rCa1TczGLy3RnvU8tX_kEVAfEEh4RNp5jBYlGgVuhPg9X4foMuj81jAYGqKQmgJH-ktR3sCvzFFgM8kaq_8Ed7AErPShq8DuhNKn1Dm1vwInPCJdWODJ2PBUCB8Nh7BHJC6jlYzDh_UATUMoaT2wSE6IBVLonRo9ZTemEBdDa-uAuV2T4zezRK9V3rrasSMIAsOIYNjD7kltYPC6o5eAbUYtoVy4fx0J_QW5bWPSNA5ZbQDV1I29thWDGBOEWtJDl-Qfamrb7tnTZX3hfIOBGS11vNWlvUdmFzOK3gNGqt51TdCE-MwLSQ0HufCucpYOQhVZzJqWFFDOkmXyBHNicPXxopr5m4xoxLBzIZ2L1AISFo19E7kSopQofWDlLzNEGyZYx0wwYads3cHGnnrqU2xt5Z1qb7oKywI79aEEg9J7WvhMCb35KoBrpq7LvqPytFuHbtpBkzv6Tr72QgGfp9xltFk_5nmcmcq2FuzUTlCpfyuNSBhzcJWdKNia80itrVKMu5tiREr0NLy05E9hIpr5ndYEJDTV4kbUeY-sB6JRj-K78YUHdOacrtjfCNyR6dGr_1j6J_aesumptSe8fRtUhdh_IH9ZjxOx2dJnE4moziOk_PJeBSxI-NJenF2mcaTZJSko3F6cT55jNifWvf8jMD0IE3Ty9E4SS7ix78odIo_)

[![](https://substackcdn.com/image/fetch/$s_!OKW3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d5caf93-f249-40f4-b682-4b9c9acf7c12_2613x524.png)](https://substackcdn.com/image/fetch/$s_!OKW3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d5caf93-f249-40f4-b682-4b9c9acf7c12_2613x524.png)

[Live editor](https://mermaid.live/edit#pako:eNqNlF1vmzAUhv-K5apSJ5EICOHD01YlhKiVKjVqmk1b2YUHTrAGdmab0Kzqf58JkKRNK9U3tg9-H7_HPuYJJjwlEMFlzqskw0KBm7uYnZ-DLy8bmN7cfn8djNnIelhIIn4hhHCiuIhZzGT5eyXwOgNz62Ge04QgEGaYrQiYYSkrLtJfMUupIIminIH7ccwW1kMMF9cIzElSCqq2eqAUZSsZw5pd0piF9ZoG1HEuSr33dWoAnqezygCMVLPqUyNJeFFglsYsqnWdotEfhEkzH6lWRTaEqZjd1ZrOyxWVOrPtN0qqixxLFXYaA6Rko_OTBpBESp2MbDGC4LTQB5vr1Ow2tZngS5oTIDNeSVCD2t2BogU55Elq09qCeWThdkPERu9_6uH1hqDX730FC6tGjCzQayeLZhg2XdR0d-13u17cxq7qzK-4kmuuEBBkw_-QfXaXOvC31Den-17OV5RdAsYVXW67k7hs7GQNoOa-UUrz-x830fy0mBKdmZyQJdiVEtCnlaOz6XRqh6EhldBO0FkQBO24V9FUZchaPxoJz7lAZ5ZlfT6ilPSA0G2PME3zJcLWiDaQYqkfgcBbBIZg-A64La2WHkzDYeTv6fbY8yPnox539dbZdMe2O96Dxs5warqnTt8GHQqggY3diTc6uBr4nmtNPupqzfWz3bakSTCxo2BPcj0nGnkfzu9REcFw52rqhOHRZYaheXIZ77PaompRkenqdlQX5pv3eoSCBlwJmkKkREkMWBBR4HoKn2IGQAxVRup3iPQwJUtc5iqGMXvWsjVmPzkvOqXg5SqDaIlzqWflOsWKTCjWP71iHxX6GRMR8pIpiCzH2kEgeoKPEA2soO-5tmkPg8D3bN8eGHCrV7l237U9HfB9c-A7jvNswH-7fc3-0DVt2zI917Qsd-h5z_8Bf_Deng)

### Cart Add Item + Remove Item

[![](https://substackcdn.com/image/fetch/$s_!HTCa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23a34d53-ab6e-4c2c-b7d5-1f4cccd1ec20_2613x1900.png)](https://substackcdn.com/image/fetch/$s_!HTCa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23a34d53-ab6e-4c2c-b7d5-1f4cccd1ec20_2613x1900.png)

[Live editor](https://mermaid.live/edit#pako:eNq1VNtu2zAM_RVCTy7mFIkdJK0fChTuLgF2S7t0wJAXVVITrbaU6ZKsK_rvI20nXZtsb3uRJfKQ55AM88CElYoVzKsfURmhLjRfOF7PDQCPwZpY3yjXvESwDkrgHsrog61b84q7oIVecRNgNiEvnskbZ01QRh69hEwJcam4hA_IW0Eyjcpp5feA56sVQa_ufVA1JKWta24kvMOjUm4PXuK9kUbf5MLWXJs90GdnvxOIvqopJ3mSQhIo4KMNCuxaYa3pbFLAW71WBnoguqLBK-VB8MAru6CAsnd2RsBPK8RhahlFgPfaB3LOJuidFkBl3qO6Jupaqw05p70udNVGTWQKhtcqRYMWqotHTFlgz4xE8uf5D-n9umzkcilBY-v-VFhWWtzBuZQ7ZdhlNNeSjBNEf7HUwETgQWJ2uppWIpi0oK-Aa15pyZH5FQin6EIxT4z46G3zv14HoOTIoeQLBgp4xtTVvjcMzJTS3Irt9LSlMuNK7sjXXVtbnS141vqJkyT4bevJuxN4Lu62cV2nrqIQyvtnE2h-Wn5pN75RDc5uYKPDEkdTo0S4iQH3BZIl911ZR_-ckGvDDg-pzbk_p9ZOpeCK1QdauTepyxc0hybTYuTfU_7vtrZjRMZgcUM89kbwSsSKjHPDUrZwWrIiuKhShkuI641P9kCZ5iwsVa3mrMCrVLc8VmHO5uYRw3Dtv1lbbyOdjYslK26RAl8tafeHt7O6ZtFKG01gRdZvcrDigf1kxSAfHWeDfDweDgaDrD8eDVN2j6D85Pg0H4yzYZYPR_lJf_yYsl8Nbf8YwWjI8_x0OMqyk8ffs5jKeA)

[![](https://substackcdn.com/image/fetch/$s_!iD4m!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33463dc3-236e-4f7c-bcfb-101366abb74d_2613x333.png)](https://substackcdn.com/image/fetch/$s_!iD4m!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33463dc3-236e-4f7c-bcfb-101366abb74d_2613x333.png)

[Live editor](https://mermaid.live/edit#pako:eNqNVdtu2zgU_BWCQYEu4KS6y-K2XdiyjAYIsAsn3qIb9YERaVuoRBoUFScN8u97KNGOXbtt-GBeZzhneI78hAvJOCZ4UclNsaJKo6tZLt68QR8OG5pe_f35x8VcjG7TttGy5uorIYQWWqpc5GLm3OY4pZpWcvlvyTdv10qyttCXbIAErfkArVVZ8D9ybGCKU1aDjMpAm_Zuqeh6ha7d2-sKDhE0Ygxdal5_zQUrFS90KQW6Gedi7sI180uC_unp0VXZ6Pd36t1HA7lrtZaiv6Itc5Ga07BhqG5kCrG-LeDHaNrJs4oKWddUsFxkBmMAgOPsB1QJ6wfow7D4PRcavHA7LwACx5vODQNsBkhLMKg5NmHu2bAMCjUruWmQ4Buk5KYLbsZrec-P4uNG8L6B3tZACzjtob932a_oU6Oq3zNEUyXrE24cGehZA3sk-zVsa5n3G8tQu2ZUc3ZsXbBvnT3VRXXTIRGETquirV7Qe9aN0Pn5RzR3TQKj8ws7NnnWbaR9l_XdrO_mnnmwfuj3x_pZ1nczuxcYIgv9ZFLik9TNWmrS5wyC4hNL3iC60FwhythfneyF4vw7t2fut_oR1QDgxTfZ6j6KVc9mLjlRvNc3X66y6-PyLSraNBO-QF3lokVZVeRsOp16aTpotJLfODlLksSOzzcl0yvirh8GhaykImeu6_65x9KWLxTQdhSO4xxSeEBhFxht4LOj6CNBIQp_QmzTybIn0zTMhjt2bxwPs-C1GrsU28qMxl403hGNg3DqRMdKTxPtss6SjaNJPHpR5Q_jyJ28VtVaQqU-WqZJMvGyZMcUxUE2il8d3wPkj6BbVdMgTfceM02do8f4OZdNKkuVORG0vbxwTr7rARUe4KUqGSZatXyA4X-ipmaKn3KBUI71itc8xwSGjC9oW0E65-IZYGsq_pOy3iKVbJcrTBZQwzDrC3tSUvjS1btVBWXMVSpboTHxhh0HJk_4ARM3vHCTcBj6fhJFYeDC5iOsJs5F7IZxGCdx4kFwwfMAf-9udS9cP4alYRz4ru-HQfj8Pyk2WIA)

### Hotel booking with projections + automation + external system

[![](https://substackcdn.com/image/fetch/$s_!BIK2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe6c82b2-d114-489d-bb25-6e79037bd23e_2613x1548.png)](https://substackcdn.com/image/fetch/$s_!BIK2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe6c82b2-d114-489d-bb25-6e79037bd23e_2613x1548.png)

[Live editor](https://mermaid.live/edit#pako:eNp1VU1z2jAQ_Ss7OjkTkwabgcSHzFCSthz6QQjpTIeLsBdQY0uuLJPSTP57V7INIYYLtuS3T293n5YXFqsEWcQK_FOijPFW8JXm2VwC8NIoWWYL1G4VG6VhKDnwwj28zyUW5sx-y7k2IhY5lwZmYwugX--TVtKgTFqQiUXcI0_gKx2egjcpUQssWsBhnlvodFsYzMAbqSzjMoEv9JOibsE_KvUk5MqGNK8fYCw3KEn6FrxblXEhW2E_tPptY-wTXZbeXlxb1B2RpBZfvUxRb0SMLelJJmRVC_dKFZlLC_qmDILaoKulPxtH8FmQQugAp6IWiAXwDRHzhUiF2YJNWCuVQYKGtgvLQZGdmxsbO0Wu4_VhhJdwg4Xvoh62OboMZmOKmERgS72F4Rt8RfEo8NniJp2auYkmolxTgvR8e0rNSWASQzrW6hnurczbRubxZH-ud7nGSi6FzgpYVM16n1lKzahSPweX0iHgjsylYWVN2NSGgDnfZtRvMOoJ5S5xMlIEoyxxvrAyPRc3TvZV8qEuW83wYAnOWmnkuV97K4KHKpeisqfGWOmEugdLuitOa57T2Tv4I0-FPeOwW-ewKAshsShAl2mVZB3SaZTfbYwrrt3HxKvrdVR9nddR4dbgUWNzoaz2MneKNtT9Yi-5As6qb2-9MuIpXWiuG7dY4E7lMH46QVHnM6oazu3Zpxnaut1Fo680j6pgW3TS0TjI7e2PruHT9whAd2G9pSZLnZBU180S1TZrJknNhAns63927BZMyzi23ZzGGq0F3-VTzYW6F8MlefiZ68ReCTcm3ACoupKAiuOSpknsblsduautm1GnmkOD73sTbK3BD2pdMTXtOTiH-WylRcIio0v0WYZUHLtkL5ZhzswaM5yziF4TXPIyNXM2l68URgS_yI1NpFblas2iJU8LWlUZ1X8uu11NelGPVCkNi7qB42DRC_tLq7B_EXTDwaDX7XaDy0G_57Mti4Lw6uI67A6CXhD2-uHV5eDVZ__csZcXBKaNMAyve_0guHr9D5PGVdk)

[![](https://substackcdn.com/image/fetch/$s_!fdO9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38255ff6-a7bb-478b-b886-5d6ceaabfc8f_2613x516.png)](https://substackcdn.com/image/fetch/$s_!fdO9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38255ff6-a7bb-478b-b886-5d6ceaabfc8f_2613x516.png)

[Live editor](https://mermaid.live/edit#pako:eNqNlFFv2zYQx78KoaBPs1NTsixL2wrYsr0WCJogjttudh9oiY64SqRAUkm8IN99R5F25CYFohdRJ97v_ne846OXiZx6ibcrxX1WEKnRxfWGb_i7d-jP0wctLi6__mzc8MnnyXrCCeqjvxqq9PckSUimhTSQ68F6ckdYSbasZHq_pERmxRdG7__YyvcfcqKp6iEpRHWzr82yliyjyiAkJXkFykqDUc32VpK6QEu8XpawBWEIt6QlzTQT3IRmd5R_33CEVni9-gSWa6CiGdUQXbXRWjb6DZGOIMR4zjICak3MhhlACjFasiG0ngeBPdQqNlszUVWE5zYg6vc_gNuGU2PpyvWdXB8ETYX4wfgtrL4WlKOb4iDYt4Lb6oG-K7KvKNdoIWTVUeWvDeCo6dbs_pQ_V8-Jgxpa_xvxAwKcSp3jtQEYEM1bzNaKehXkQhgGhepqK9Yma1_z13IOXM4B5HQlxb_2jBR8XTa6bnSb9DU-aYyUlMAh8kVr0IowDgKN7J_7Aii2KPA_FXzHZEVMqCOkk5xqoAhy_4KwCmzxl00GjafQMpOU8q43yiya5s-HsRpar0leMY4us6ypCc_2aEZUsRVEHre64nzD6zkkUkLLyjuoTVvSB00lJ6WbtVQKpfqqrZwZxXau2iKvsJkj1D9369T228p3np0ab_gc243XbtOwY7Jntgqc36TRwhYMaYEOcpDaK00rCGm3X8FBPW80Q8fzbrHbvEw-tQDt-9bnG3YhPgqtaqGtBvjxEa-dCUi1bLsK5aLZlhS5crelL0SZw2ia30Lu0Z1CotasYkqzzJxH1khJoeDtZvhBRaMVgiaHhtGS2REtDsFfvcuWN39fzJcvb7OsJErN6A61dxjasbJMzhaLhZ-mPaUlDE5yFsexW_fvWa6LBNcPvUyUQiZnGOPfO5SGPSPgOSIGg8EpwgeEM-TQRURKsk9QiMJfgN1UO3q8SMP5-Ej3p9F4PnyrRnsMTuZo6o-mR9B0GC4Go5dKXwcdJ8vBpqNZNHlWFYyjEZ69VZXrJ0uaxTN_Hh9Jo2g4n0Rvzu_Q2i7FYZp2DjNNBy8O49cs11QONR-M4On0xeDVcz1BeT3vVrLcS7RsaM-rKAyS-fQezc2y8XRBK7rxEljmdEeaUm-8DX8CN7hj_oFr8OApRXNbeMmOlAq-mtpcmTNG4BaujlaYkpzKVDRce0kQtQwvefQevASH5zgOx2EQxKNROMTjnrcHazw4j3AYhVEcxT4kN3zqef-1UfE5DiIwjaNhgIMgHIZP_wMLZLow)

## Common mistakes

**Mistake 1: Modeling technology instead of information flow**
Event Modeling should stay at the level of “what information moves where and why,” not “we will use REST here and Kafka there.”

**Mistake 2: Screens that are too detailed**
Wireframes are there to clarify data and behavior, not to finalize UX. Keep them intentionally rough.

**Mistake 3: Events that are generic or overloaded**
Events should represent specific business occurrences. Avoid stuffing many meanings into one event via “type” fields if the business semantics differ, because it makes evolution painful.

**Mistake 4: Views that cannot be traced to events**
If a read model attribute has no source event, you have discovered either a missing event, a missing field, or a missing decision. That is exactly what the information completeness check is for.

## References

### Books

- Martin Dilger, *Understanding Eventsourcing: Planning and Implementing Scalable Systems with Event Modeling and Event Sourcing* (2024).
- Adam Bellemare, *Building Event-Driven Microservices* (O’Reilly, 2020).
- Alberto Brandolini, *Introducing EventStorming* (Leanpub).

- EventModeling.org, “Event Modeling is a method of describing systems using an example of how information has changed within them over time.” ([Event Modeling](https://eventmodeling.org/))
- EventModeling.org, “Event Modeling Cheat Sheet.” ([Event Modeling](https://eventmodeling.org/posts/event-modeling-cheatsheet/))
- EventModeling.org, “What is Event Modeling?” ([Event Modeling](https://eventmodeling.org/posts/what-is-event-modeling/))
- AxonIQ Concepts, “Event Modeling” (comparison framing with EventStorming). ([axoniq.io](https://www.axoniq.io/concepts/event-modeling))
