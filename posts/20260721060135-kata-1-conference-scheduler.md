Title: Kata 1: Conference scheduler

URL Source: http://emmanuelvalverderamos.substack.com/p/kata-1-conference-scheduler

Final URL: https://emmanuelvalverderamos.substack.com/p/kata-1-conference-scheduler

Published Time: 2026-07-21T06:01:35+00:00

Markdown Content:
Practise discovering responsibilities and collaborations while implementing a small scheduling workflow.

The exercise is intentionally manual. The organiser already knows which talk they want to schedule, which room they want to use, and which time they want. The system accepts or rejects that request according to the business rules.

This kata is not about finding an optimal schedule. It is about noticing how responsibility placement changes as more scheduling rules appear.

[![Image 1](https://substackcdn.com/image/fetch/$s_!opEl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb20910c5-7f6a-4fc8-a035-cc91691365a1_1024x559.png)](https://substackcdn.com/image/fetch/$s_!opEl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb20910c5-7f6a-4fc8-a035-cc91691365a1_1024x559.png)

A one-day software conference needs a simple scheduling tool.

The organiser builds the public agenda by placing talks into rooms at specific times. Attendees use that agenda to know what happens, where it happens, and when it happens.

[![Image 2](https://substackcdn.com/image/fetch/$s_!KQ34!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F919c0960-c966-4694-bf64-c13939ecbcda_1024x559.png)](https://substackcdn.com/image/fetch/$s_!KQ34!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F919c0960-c966-4694-bf64-c13939ecbcda_1024x559.png)

The system must protect the agenda from impossible schedules. A conference schedule is not valid just because talks have titles and times. It must also respect rooms, speakers, availability, and suitability.

Build the behaviour needed to schedule talks into rooms and show the public agenda.

A talk has:

*   A title

*   A speaker

*   An expected number of attendees

*   Optional requirements, such as needing a projector

A room has:

*   A name

*   A capacity

*   Optional capabilities, such as having a projector

A speaker may be unavailable at specific times.

Use this vocabulary to describe the business problem. It is not a proposed implementation model.

*   Conference

*   Public agenda

*   Talk

*   Speaker

*   Room

*   Time

*   Capacity

*   Capability

*   Scheduling request

*   Move request

*   Rejected request

*   The organiser schedules one talk at a time.

*   Time is represented using fixed labels such as `09:00`, `10:00`, and `11:00`.

*   A room can host at most one talk at the same time.

*   A speaker can give at most one talk at the same time.

*   A room is suitable only when it has enough capacity and the required capabilities.

*   A rejected scheduling request must not change the existing agenda.

*   A rejected move request must not change the existing agenda.

![Image 3](https://substackcdn.com/image/fetch/$s_!CYg6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F468b4f01-6638-4007-87cc-b69bf18cdf8b_3547x140.png)

Before moving to the next scenario:

*   Is the behaviour covered by a failing test first?

*   Is the expected outcome observable from outside the implementation?

*   Are previous scenarios still passing?

*   Does the test describe business behaviour rather than internal structure?

*   Did the last change introduce duplication worth refactoring?

*   Can the current design be explained without mentioning a framework, database, or user interface?

**⚠️ This kata has counterexample that you do not have to follow, they are meant to force you, to think about the sad path**

[![Image 4](https://substackcdn.com/image/fetch/$s_!uAi8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81701a19-e504-4301-8115-184f05c0dd07_1024x559.png)](https://substackcdn.com/image/fetch/$s_!uAi8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81701a19-e504-4301-8115-184f05c0dd07_1024x559.png)

The public agenda is the visible result of the scheduling work.

If nothing has been scheduled, the agenda is empty. If talks have been scheduled, the agenda shows those talks. The agenda should be useful for attendees, so talks must be shown in chronological order, regardless of the order in which the organiser scheduled them.

This rule does not say how the schedule is stored. It only says what the conference must be able to show.

This rule gives the kata its first observable behaviour.

Before rejecting invalid schedules, checking room conflicts, or moving talks, the system must be able to show what has already been accepted into the conference schedule.

The agenda is not a technical report. It is what attendees would read to know what happens during the day.

The organiser schedules “Refactoring legacy code” at `09:00`.

When the public agenda is requested, the talk appears at `09:00`.

A new conference has no scheduled talks.

When the public agenda is requested, it should not invent placeholder talks, default sessions, or sample data. It should be empty.

This rule starts with visibility. The first behaviour is not validation. The first behaviour is showing what the business has accepted so far.

Later rules will make it harder for something to become accepted into the agenda. For now, the goal is simply to make accepted talks visible.

![Image 5](https://substackcdn.com/image/fetch/$s_!y3er!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5aadc773-7466-47ef-968e-ab80b1c39417_2751x188.png)

A conference has just been created and no talk has been placed yet.

```
Scenario: Show an empty agenda
  Given a conference with no scheduled talks
  When the public agenda is requested
  Then the agenda is empty
```

![Image 6](https://substackcdn.com/image/fetch/$s_!L5Ov!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9cd99189-bfc4-48db-8122-a749fb476c8a_1419x140.png)

The organiser places one talk in a room that can host it.

```
Scenario: Schedule one talk
  Given Room A can host "Refactoring legacy code" at 09:00
  When the organiser schedules "Refactoring legacy code" in Room A at 09:00
  Then "Refactoring legacy code" appears in the public agenda at 09:00
```

![Image 7](https://substackcdn.com/image/fetch/$s_!_QRo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2caf0cc-05e3-463f-9389-73d941da7f84_1792x188.png)

The public agenda should show more than one scheduled talk.

```
Scenario: Show several scheduled talks
  Given 3 talks are scheduled
  When the public agenda is requested
  Then the agenda shows 3 talks
```

![Image 8](https://substackcdn.com/image/fetch/$s_!mknp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddfa7c8a-6e70-4ed4-a4bb-2fed7e0a5270_1648x140.png)

Talks may be scheduled in any order, but attendees need to read the agenda by time.

```
Scenario: Show scheduled talks in chronological order
  Given talks are scheduled at 11:00, 09:00, and 10:00
  When the public agenda is requested
  Then the talks are shown as 09:00, 10:00, and 11:00
```

![Image 9](https://substackcdn.com/image/fetch/$s_!SsV_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F937c8de6-87ee-4ea2-b348-a8a349fe0ea8_1714x188.png)

[![Image 10](https://substackcdn.com/image/fetch/$s_!YW8n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7953ad62-0fb4-4f0d-a872-0deb0a7af013_1024x559.png)](https://substackcdn.com/image/fetch/$s_!YW8n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7953ad62-0fb4-4f0d-a872-0deb0a7af013_1024x559.png)

A room can only host one talk at a given time.

Two talks may happen at the same time in the conference, but not in the same room. This is about protecting a physical constraint. A room cannot contain two independent sessions at the same time.

The agenda must be realistic.

A schedule that places two talks in Room A at `09:00` is not a valid conference schedule, even if both talks are otherwise valid.

This rule introduces the difference between:

`A talk can exist.`
and:

`A talk can be placed in this room at this time.`
Room A hosts “Refactoring legacy code” at `09:00`.

Room B hosts “Testing microservices” at `09:00`.

This is allowed because the talks use different rooms.

Room A already hosts “Refactoring legacy code” at `09:00`.

The organiser then tries to schedule “Testing microservices” in Room A at `09:00`.

The request must be rejected.

The system now has to preserve a valid agenda, not only record requested talks.

A rejected request must not replace or remove the talk that was already scheduled. Rejection is not just a return value or an error. It also means the previous valid schedule remains valid.

![Image 11](https://substackcdn.com/image/fetch/$s_!vRBY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90cbbf27-cfa2-4eb9-9b19-4a92f957c33e_2408x588.png)

Two different rooms can host two talks at the same time.

```
Scenario: Schedule two talks in different rooms at the same time
  Given Room A is available at 09:00
  And Room B is available at 09:00
  When two talks are scheduled at 09:00 in different rooms
  Then both talks appear in the public agenda
```

[![Image 12](https://substackcdn.com/image/fetch/$s_!o1nS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0adc7362-cceb-4b35-825e-8aefa828cd9c_1693x444.png)](https://substackcdn.com/image/fetch/$s_!o1nS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0adc7362-cceb-4b35-825e-8aefa828cd9c_1693x444.png)

A room already used at `09:00` cannot host another talk at `09:00`.

```
Scenario: Reject two talks in the same room at the same time
  Given Room A already has a talk at 09:00
  When another talk is scheduled in Room A at 09:00
  Then the scheduling request is rejected
```

![Image 13](https://substackcdn.com/image/fetch/$s_!pIkM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe19e605b-9932-4e98-aca4-10850c305d79_1669x188.png)

A rejected conflicting request must not remove or replace the original scheduled talk.

```
Scenario: Keep the original talk after a room conflict
  Given "Refactoring legacy code" is scheduled in Room A at 09:00
  When "Testing microservices" is scheduled in Room A at 09:00
  Then "Refactoring legacy code" remains scheduled in Room A at 09:00
```

![Image 14](https://substackcdn.com/image/fetch/$s_!ZpHc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aa70c82-3f0d-485f-9dfb-9ddefb38af59_2355x188.png)

[![Image 15](https://substackcdn.com/image/fetch/$s_!IRBd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4ff2e7e-4dfa-49b3-95ef-29528a7ecf68_1024x559.png)](https://substackcdn.com/image/fetch/$s_!IRBd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4ff2e7e-4dfa-49b3-95ef-29528a7ecf68_1024x559.png)

A speaker can only give one talk at a given time.

Even if two different rooms are available, the same person cannot speak in both rooms at once.

This rule is different from room conflict. A room conflict is about a place. A speaker conflict is about a person.

A schedule can look valid from the room perspective and still be impossible for a speaker.

The conference needs a schedule that works for both attendees and speakers. A schedule that asks Alice to give two talks at `09:00` is not valid, even when those talks are in different rooms.

Alice gives a talk at `09:00`.

Bob gives another talk at `09:00`.

This is allowed because they are different speakers.

Alice is already giving a talk at `09:00`.

The organiser tries to schedule another talk by Alice at `09:00`.

The request must be rejected.

The system now has more than one kind of conflict.

A talk can be rejected because of the room, because of the speaker, or because the speaker is unavailable. The kata starts to move from simple storage toward business rules that interact.

[![Image 16](https://substackcdn.com/image/fetch/$s_!cADp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa04a2d8e-043e-46e9-a014-7939d0ddce2c_1788x588.png)](https://substackcdn.com/image/fetch/$s_!cADp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa04a2d8e-043e-46e9-a014-7939d0ddce2c_1788x588.png)

Different speakers can give different talks at the same time.

```
Scenario: Schedule two talks by different speakers at the same time
  Given Alice is available at 09:00
  And Bob is available at 09:00
  When their talks are scheduled at 09:00
  Then both talks appear in the public agenda
```

![Image 17](https://substackcdn.com/image/fetch/$s_!rJaO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60c73c32-9d6a-4db1-b893-e963e6e144ca_1650x348.png)

Alice cannot give two talks at `09:00`.

```
Scenario: Reject two talks by the same speaker at the same time
  Given Alice is already speaking at 09:00
  When another talk by Alice is scheduled at 09:00
  Then the scheduling request is rejected
```

![Image 18](https://substackcdn.com/image/fetch/$s_!YQ_f!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F422c645d-d184-4942-bda2-783d72760897_1669x188.png)

A speaker may be unavailable even when they are not already scheduled for another talk.

```
Scenario: Reject a talk when the speaker is unavailable
  Given Alice is unavailable at 09:00
  When Alice's talk is scheduled at 09:00
  Then the scheduling request is rejected
```

![Image 19](https://substackcdn.com/image/fetch/$s_!TUZF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F63413122-0ee9-427e-ad74-a8d2cbb23caf_1642x188.png)

[![Image 20](https://substackcdn.com/image/fetch/$s_!qbSl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7680789b-1eed-493d-9b83-8aeefff80deb_1024x559.png)](https://substackcdn.com/image/fetch/$s_!qbSl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7680789b-1eed-493d-9b83-8aeefff80deb_1024x559.png)

A room being free is not enough. The room must also be appropriate for the talk.

A talk may need enough seats for expected attendees. A talk may also need a capability such as a projector. If the room does not satisfy those needs, the talk cannot be placed there.

A schedule should not only avoid conflicts. It should also make sense operationally.

A room with 30 seats cannot host a talk expecting 40 people. A talk that requires a projector cannot be placed in a room without one.

A room has capacity 40.

A talk expects 40 attendees.

The room is suitable by capacity.

A room has capacity 39.

A talk expects 40 attendees.

The request must be rejected because the room is too small.

The idea of “valid scheduling” becomes richer.

A request can now be rejected even when the room is free and the speaker is available. Availability and suitability are not the same thing.

[![Image 21](https://substackcdn.com/image/fetch/$s_!haGs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02d1815d-46ef-452a-b270-2412a1379f7c_1622x524.png)](https://substackcdn.com/image/fetch/$s_!haGs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02d1815d-46ef-452a-b270-2412a1379f7c_1622x524.png)

A room with capacity 40 can host a talk expecting 40 attendees.

```
Scenario: Schedule a talk when the room has exactly enough capacity
  Given Room A has capacity 40
  When a talk for 40 attendees is scheduled in Room A
  Then the talk appears in the public agenda
```

![Image 22](https://substackcdn.com/image/fetch/$s_!aVZC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee73bdb2-86f7-4125-b896-23059eb7069d_1575x140.png)

A room with capacity 39 cannot host a talk expecting 40 attendees.

** _Keep in mind that this is not probably how you would implemented in real life, because you may reject the attendee if you instead of the talk or have other kind of solution for this, this is only for the kata purpose_.

```
Scenario: Reject a talk when the room is too small
  Given Room A has capacity 39
  When a talk for 40 attendees is scheduled in Room A
  Then the scheduling request is rejected
```

![Image 23](https://substackcdn.com/image/fetch/$s_!sirG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ed7b8ec-c7d5-46e7-b3e0-6de4cc4d86e6_1525x140.png)

A talk requiring a projector can be scheduled in a room with a projector.

```
Scenario: Schedule a talk when the room has the required capability
  Given Room A has a projector
  When a talk requiring a projector is scheduled in Room A
  Then the talk appears in the public agenda
```

![Image 24](https://substackcdn.com/image/fetch/$s_!WVnt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f5b580-a02a-4adb-aa0e-f6bc859dd79a_1551x140.png)

A talk requiring a projector cannot be scheduled in a room without one.

```
Scenario: Reject a talk when the room lacks the required capability
  Given Room A has no projector
  When a talk requiring a projector is scheduled in Room A
  Then the scheduling request is rejected
```

![Image 25](https://substackcdn.com/image/fetch/$s_!fwE4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2609fb37-fbff-4075-a417-8fb603c8ddc0_1546x140.png)

[![Image 26](https://substackcdn.com/image/fetch/$s_!V3E1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41f45d95-c1f8-4af4-ae8a-76a004d4364b_1024x559.png)](https://substackcdn.com/image/fetch/$s_!V3E1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41f45d95-c1f8-4af4-ae8a-76a004d4364b_1024x559.png)

The organiser can move an already scheduled talk to another room or time, but the move must obey the same business rules as a new scheduling request.

If the target room and time are valid, the talk moves. If the target is invalid, the move is rejected and the original schedule remains unchanged.

Real schedules change.

A speaker may request another time, a room may become unavailable, or the organiser may want to improve the agenda.

But changing a schedule is risky. A failed move should not leave the agenda half-changed. The system must protect the current valid agenda while trying to apply the requested change.

“Refactoring legacy code” is scheduled at `09:00`.

The organiser moves it to an available slot at `10:00`.

The agenda now shows it at `10:00`.

“Refactoring legacy code” is scheduled in Room A at `09:00`.

The organiser tries to move it to Room B at `10:00`, but Room B is already occupied at `10:00`.

The move is rejected and the talk remains in Room A at `09:00`.

The kata now asks for safe change, not only initial scheduling.

The system must protect the current valid schedule when a requested change cannot be accepted.

![Image 27](https://substackcdn.com/image/fetch/$s_!hqUy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F952343f4-ef6d-4808-8fd9-6ad9ccbbcb4f_2690x407.png)

A scheduled talk can be moved to another valid time.

```
Scenario: Move a talk to an available slot
  Given "Refactoring legacy code" is scheduled at 09:00
  When the organiser moves it to 10:00
  Then "Refactoring legacy code" appears in the public agenda at 10:00
```

![Image 28](https://substackcdn.com/image/fetch/$s_!scY1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c48e2fa-0720-4560-91f9-c7049712c929_1618x140.png)

After a successful move, another talk can use the original room and time.

```
Scenario: Release the original slot after moving a talk
  Given "Refactoring legacy code" is scheduled in Room A at 09:00
  When the organiser moves it to Room B at 10:00
  Then another talk can be scheduled in Room A at 09:00
```

![Image 29](https://substackcdn.com/image/fetch/$s_!1uAs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F877d0141-e202-403f-91c3-9fa75cee4f5a_1757x188.png)

A talk cannot be moved into a room and time that are already occupied.

```
Scenario: Reject a move that creates a room conflict
  Given Room A already has a talk at 10:00
  When another talk is moved to Room A at 10:00
  Then the move request is rejected
```

![Image 30](https://substackcdn.com/image/fetch/$s_!moCf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccb06a5c-fb0a-43dc-96a7-4c5304b66a86_1629x188.png)

A rejected move must not remove the original scheduled talk.

```
Scenario: Keep the original schedule after a rejected move
  Given "Refactoring legacy code" is scheduled in Room A at 09:00
  When it is moved to an occupied room at 10:00
  Then "Refactoring legacy code" remains scheduled in Room A at 09:00
```

![Image 31](https://substackcdn.com/image/fetch/$s_!pnK0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc39b1d93-546b-440a-976f-77668d69f28c_2215x188.png)

[![Image 32](https://substackcdn.com/image/fetch/$s_!T1VF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e31e033-7017-461e-a9d5-1615c5391329_1402x1122.png)](https://substackcdn.com/image/fetch/$s_!T1VF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e31e033-7017-461e-a9d5-1615c5391329_1402x1122.png)
