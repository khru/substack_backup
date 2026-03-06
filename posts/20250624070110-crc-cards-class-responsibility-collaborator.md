---
title: "CRC cards: Class, Responsibility, Collaborator cards"
requested_url: "https://emmanuelvalverderamos.substack.com/p/crc-cards-class-responsibility-collaborator"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/crc-cards-class-responsibility-collaborator"
substack_post_id: 164630529
retrieved_at: "2026-03-06T08:33:00.205Z"
---
# CRC cards: Class, Responsibility, Collaborator cards

## Designing with CRC Cards

When we talk about object-oriented design, we usually think in terms of classes, methods, and inheritance. But that often leads to a technical tunnel vision, where we forget the real goal of design: to model meaningful behavior through collaboration.

That's exactly what CRC cards help us remember.

Developed by Kent Beck and Ward Cunningham in the late 1980s, CRC cards, which stand for *Class, Responsibility, Collaborator*, are a low-tech but high-impact tool to design software by focusing on what matters: behavior and communication between objects.

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## What is a CRC Card?

Each CRC card is divided into three clear sections:

• **Class**: the name of the object or component
• **Responsibilities**: what this object does (not how)
• **Collaborators**: other objects this one interacts with to fulfill its responsibilities

This simple structure forces you to answer three fundamental questions:

- Who am I?
- What do I have to do?
- Who do I need to work with?

---

## Why they still matter

CRC cards are deceptively simple, yet they solve a recurring problem in software teams: poor communication and vague design intent.

By using CRC cards:

• You focus on behavior, not structure
• You delay naming classes until you understand their role
• You visualize object interaction before you write code
• You get your team talking and thinking together

CRC cards are potent early in the design phase. They replace abstract discussions with concrete thinking. And they don’t require any tools, just paper, pens, and brains.

---

## A concrete example

[![](https://substackcdn.com/image/fetch/$s_!ES5E!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b4cd82c-e215-400d-8b69-25bae3d3486d_7402x3216.png)](https://substackcdn.com/image/fetch/$s_!ES5E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b4cd82c-e215-400d-8b69-25bae3d3486d_7402x3216.png)

Let’s look at a guessing game. We’ll use two CRC cards to model the core behavior.

### GuessRandomNumberGame

**Responsibilities:**

• Allow the user to play the game by introducing a number
• Tell if the number is higher or lower
• Tell the user if they have won or lost

**Collaborator:** `RandomNumberGenerator`

---

### RandomNumberGenerator

**Responsibility:** Generate a random number
**Collaborator:** None

---

## What you learn from this

This is where CRC cards show their value.

We can immediately see that `GuessRandomNumberGame` handles game logic and user interaction, but it relies on a separate class to generate numbers. That separation of concerns makes testing easier and behavior clearer. It also opens the door for reuse, maybe we swap the number generator in tests or add new game modes later.

## Final thoughts

CRC cards won’t design your system for you, but they will help you design **with intention**. They make responsibilities and collaborations explicit, and that’s where good software begins.
