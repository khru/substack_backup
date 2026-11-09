Title: Responsibility-driven design: giving behaviour a responsible home

URL Source: http://emmanuelvalverderamos.substack.com/p/responsibility-driven-design-giving

Final URL: https://emmanuelvalverderamos.substack.com/p/responsibility-driven-design-giving

Published Time: 2026-07-07T06:00:24+00:00

Markdown Content:
There is a way of writing object-oriented code that looks correct from the outside and still feels wrong from the inside.

The code has classes. The classes have methods. The methods call other methods. There may even be interfaces, diagrams, and patterns. At first glance, everything appears to be in the right place.

But when you try to understand the behaviour, the design starts to resist.

One object asks too many questions. Another object holds data but makes no decisions. A service coordinates everything. A domain object is reduced to a container. A collaborator exists, but nobody can explain what role it plays. A method works, but it reads like a script that happens to be written inside a class.

This is one of the traps of Object-Oriented Programming (OOP): it is possible to use classes without really thinking in objects.

Responsibility-Driven Design (RDD) starts from a different place.

It does not begin by asking, “what classes do we need?”

It begins by asking, “what behaviour needs to happen, and who should be responsible for it?”

That question changes the design conversation.

Not because it gives us a mechanical recipe. It does not. But because it moves our attention from structure to responsibility, from data to behaviour, and from isolated classes to collaborating objects.

This article is about that shift.

[![Image 1](https://substackcdn.com/image/fetch/$s_!yN3n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdca91fa9-d1a2-4ce4-aec3-a8391d8fc17c_1402x1122.png)](https://substackcdn.com/image/fetch/$s_!yN3n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdca91fa9-d1a2-4ce4-aec3-a8391d8fc17c_1402x1122.png)

Responsibility-Driven Design (RDD) is a way of designing Object-Oriented Programming (OOP) systems by starting from **responsibilities, roles, and collaborations**.

[![Image 2](https://substackcdn.com/image/fetch/$s_!W7Th!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4d9cad1-1a05-49ce-b3c7-41d312291609_1024x559.png)](https://substackcdn.com/image/fetch/$s_!W7Th!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4d9cad1-1a05-49ce-b3c7-41d312291609_1024x559.png)

Its core idea is simple:

> Objects should not be treated as mere data containers. They should be responsible participants in a collaborating system.

A responsibility is something an object is expected to know, do, decide, coordinate, translate, protect, or delegate. A role is the position an object plays in a scenario. A collaboration happens when one object asks another object for help by sending a message. A contract describes what that message means: what the receiver expects, what it promises, and what the caller should not need to know.

The point of Responsibility-Driven Design (RDD) is not to create more classes. It is to distribute behaviour well.

A good object-oriented design is not a pile of named things. It is a community of objects that know what they are responsible for and know when to ask one another for help.

[![Image 3: Object Design: Roles, Responsibilities, and Collaborations: Wirfs-Brock, Rebecca, McKean, Alan: 9780201379433: Amazon.com: Books](https://substackcdn.com/image/fetch/$s_!ud7N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17521a6a-4756-41ba-ac25-914217e4dbc5_812x1000.jpeg)](https://substackcdn.com/image/fetch/$s_!ud7N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17521a6a-4756-41ba-ac25-914217e4dbc5_812x1000.jpeg)

1.   Why classes are not enough

2.   Object thinking before object design

3.   What Responsibility-Driven Design (RDD) is really about

4.   Responsibilities before structure

5.   Doing and knowing responsibilities

6.   Roles and role stereotypes

7.   Finding candidate objects

8.   Assigning responsibilities

9.   Collaborations, messages, and contracts

10.   Class, Responsibility, Collaborator (CRC) cards

11.   Control style: centralized, dispersed, delegated

12.   A practical example in Kotlin

13.   Trust boundaries and reliable collaborations

14.   Flexibility and variation points

15.   Patterns as responsibility arrangements

16.   Conclusion

17.   References

A common mistake in Object-Oriented Programming (OOP) is to think that object-oriented design is mainly about finding classes.

It is understandable. Requirements often contain nouns, and nouns often look like objects. A library has members, books, loans, reservations, librarians, fines, and notifications. It is tempting to turn those words into classes and feel that the design has begun.

Sometimes that is useful. Some of those concepts may deserve representation in code.

But a list of nouns is not a design.

The problem is not noticing candidate objects. The problem is treating those candidates as if they already explain the behaviour of the system.

A class called `Loan` does not tell us who is responsible for creating a loan. A class called `Member` does not tell us who decides whether that member may borrow another book. A class called `Notification` does not tell us who should be told, when, or why. The class name gives us a possible concept, but not yet a distribution of responsibilities.

That is where many object-oriented designs become weak. They have objects, but the objects do not carry enough behaviour. They hold data, expose state, and wait for a central service to do the real work.

The design is object-shaped, but the thinking is still procedural.

Responsibility-Driven Design (RDD) pushes against that. It asks us to begin with behaviour.

Not “what entities exist?”  
But “what work must be done?”

Not “what data does this object have?”  
But “what is this object responsible for?”

Not “which class should hold this field?”  
But “who should know this, decide this, or do this?”

That is the first important shift:

> A class becomes useful when it gives a responsibility a good home.

![Image 4](https://substackcdn.com/image/fetch/$s_!GerK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c155a16-d5dc-42e0-8859-3d872df44dae_2956x420.png)

```
flowchart LR
    Requirement[Requirement] --> CandidateNouns[Candidate nouns]
    CandidateNouns --> Classes[Classes]
    Classes --> Data[Fields and data]
    Data --> CentralService[Central service makes decisions]

    Requirement --> Behaviour[Behaviour that must happen]
    Behaviour --> Responsibilities[Responsibilities]
    Responsibilities --> Roles[Roles]
    Roles --> Collaborations[Collaborations]
    Collaborations --> ResponsibleObjects[Responsible objects]
```

The second path does not reject classes. It simply refuses to let classes lead the design before responsibilities are understood.

[![Image 5](https://substackcdn.com/image/fetch/$s_!OPBX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e68a211-e3f2-497a-8838-570f4d06cea3_1024x558.png)](https://substackcdn.com/image/fetch/$s_!OPBX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e68a211-e3f2-497a-8838-570f4d06cea3_1024x558.png)

Before Responsibility-Driven Design (RDD) becomes a technique, it rests on a way of seeing software.

Object thinking asks us to stop seeing software as procedures operating over data. Instead, we see a system as a community of objects that know things, do things, make decisions, and collaborate.

The important shift is not syntax. A programming language can support classes and still allow procedural design. The deeper shift is cognitive.

A procedural instinct asks:

> What sequence of steps should I write?

An object thinking instinct asks:

> Which responsible participants should collaborate to make this behaviour happen?

That difference matters because it changes what we notice.

If we think procedurally, we tend to look for the flow first. We ask where the process starts, which data is needed, which functions transform it, and where the result goes. This can be useful for understanding an algorithm, but it often creates designs where objects become passive containers passed through a central process.

If we think in objects, we look for participants. We ask what each participant is responsible for, what it can do for others, what it should hide, and when it needs help.

The system is no longer just a sequence of steps.

It becomes a network of responsibilities.

[![Image 6](https://substackcdn.com/image/fetch/$s_!n_Ql!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2cc028de-37a7-4328-a416-111689586a3f_1852x543.png)](https://substackcdn.com/image/fetch/$s_!n_Ql!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2cc028de-37a7-4328-a416-111689586a3f_1852x543.png)

This does not mean every algorithm disappears. It means the design is no longer organized around one controlling procedure that interrogates everything else.

A good object-oriented design gives behaviour to objects that can own it.

![Image 7](https://substackcdn.com/image/fetch/$s_!VpoZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed51bcc2-e4a7-438e-b055-96833cca3322_2606x556.png)

```
flowchart TD
    ObjectThinking[Object thinking] --> Behaviour[Behaviour first]
    ObjectThinking --> Responsibilities[Responsibilities]
    ObjectThinking --> Collaboration[Collaboration]
    ObjectThinking --> Encapsulation[Encapsulation]
    ObjectThinking --> DistributedControl[Distributed control]

    Behaviour --> WhatHappens[What must happen?]
    Responsibilities --> WhoOwnsIt[Who should own it?]
    Collaboration --> WhoHelps[Who needs to help?]
    Encapsulation --> WhatIsHidden[What should stay hidden?]
    DistributedControl --> WhereControlLives[Where should control live?]
```

Responsibility-Driven Design (RDD) gives this way of thinking a practical vocabulary.

Responsibility-Driven Design (RDD) is a way of designing object-oriented systems by focusing on responsibilities, roles, and collaborations.

A responsibility is an obligation.

An object may be responsible for knowing something. It may be responsible for doing something. It may be responsible for deciding something. It may be responsible for coordinating a process. It may be responsible for translating between the system and an external boundary. It may be responsible for protecting an invariant. It may be responsible for delegating part of its work to another object.

The important part is that responsibility is behavioural language.

It tells us what an object contributes to the system.

That is why Responsibility-Driven Design (RDD) is not just a technique for finding classes. It is a way to reason about how behaviour should be distributed.

The practical questions are:

*   What responsibilities exist?

*   Which roles are needed?

*   Which object should carry each responsibility?

*   Which objects must collaborate?

*   What contract does each collaboration imply?

*   Where should control live?

*   Which details should be hidden?

*   Which boundaries are trustworthy?

*   Where is flexibility actually valuable?

These questions are not theoretical decoration. They are the questions we need when code starts to feel wrong.

![Image 8](https://substackcdn.com/image/fetch/$s_!rsAc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51a17530-4651-46a7-913a-4058d4f461a6_2722x556.png)

```
flowchart LR
    Scenario[Scenario] --> Responsibilities[Responsibilities]
    Responsibilities --> Roles[Roles]
    Roles --> Candidates[Candidate objects]
    Candidates --> Collaborations[Collaborations]
    Collaborations --> Contracts[Contracts]
    Contracts --> Protocols[Protocols]
    Collaborations --> ControlStyle[Control style]
    Collaborations --> Trust[Trust boundaries]
```

The diagram is not a process that must be followed mechanically. It is a map of design concerns. In real work, we move back and forth between them.

The phrase “responsibilities before structure” is easy to say, but it changes the design conversation.

Imagine we are designing a library lending system.

A structure-first approach might begin with:

*   `Member`

*   `Book`

*   `BookCopy`

*   `Loan`

*   `Reservation`

*   `Fine`

*   `Notification`

That list may contain useful candidates. But it does not yet tell us how the system behaves.

A responsibility-first approach asks different questions:

*   Who decides whether a member may borrow a book copy?

*   Who records that a book copy is now on loan?

*   Who knows when the loan is due?

*   Who decides whether the loan is overdue?

*   Who notifies the member?

*   Who coordinates the lending process?

*   Who talks to persistence?

*   Who talks to the notification channel?

Now we are no longer just naming concepts. We are distributing work.

That distribution is the heart of design.

A responsibility map might begin like this:

[![Image 9](https://substackcdn.com/image/fetch/$s_!IVXz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91ec6083-5bab-4e71-80ab-25fc4836b3cb_2750x703.png)](https://substackcdn.com/image/fetch/$s_!IVXz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91ec6083-5bab-4e71-80ab-25fc4836b3cb_2750x703.png)

This table is not the final design. It is a way to make the work visible.

That is one of the first things Responsibility-Driven Design (RDD) gives us: it makes responsibility visible before structure becomes fixed.

Responsibilities are not all the same kind.

A useful distinction in Responsibility-Driven Design (RDD) is the difference between **doing responsibilities** and **knowing responsibilities**.

A doing responsibility is about behaviour. It is the responsibility to calculate, validate, reserve, lend, notify, coordinate, translate, decide, or delegate.

A knowing responsibility is about information. It is the responsibility to know the member identifier, know the book copy identifier, know the due date, know whether a loan is active, or know which rules apply to a member.

This distinction is useful, but it should not be made too simplistic. Objects often do both.

For example, an `ActiveLoan` may know its due date, but it may also answer whether it is overdue on a given date. A `LoanPeriod` may know a start date and due date, but it may also calculate whether a date is within the period.

The point is not to force objects into boxes.

The point is to notice what kind of responsibility we are assigning.

![Image 10](https://substackcdn.com/image/fetch/$s_!kxRf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5ec01fe-c4f7-46b1-bc1f-2c460661d061_2754x564.png)

This matters because different responsibilities lead to different design pressures. A coordinator should not absorb every rule. A value should not be forced to know external systems. A boundary object should not leak external vocabulary into the domain.

Responsibility type helps us ask better questions.

A common weak definition of an object is this: an object is data plus methods.

That definition is not completely wrong, but it is not strong enough for design.

It keeps our attention on the wrong thing. It makes us think of objects as containers that happen to have functions attached. That is how we end up with data holders, getters, setters, and one large service making decisions from the outside.

A better design definition is this:

> An object is a responsible participant that plays a role in a collaboration.

A role is not the same thing as a class. A class is a code structure. A role is a behavioural position in a scenario.

Role stereotypes help us describe that position. They are not rigid categories. They are thinking tools.

![Image 11](https://substackcdn.com/image/fetch/$s_!EYfw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf0abf29-d049-4ea7-ba12-6832a665e2eb_2743x632.png)

A controller is not automatically a design mistake. It becomes dangerous when close direction turns into centralized intelligence and the rest of the model becomes passive.

An information holder is not automatically weak either. Some objects legitimately hold information. The problem appears when information holding becomes the whole model and behaviour migrates elsewhere.

The value of the stereotypes is that they help us see emphasis.

They let us ask:

> Is this object’s role clear?

That is more useful than asking whether the object has enough methods.

[![Image 12](https://substackcdn.com/image/fetch/$s_!utTe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07b488d5-7b67-4616-ac8c-13a52487575b_1024x559.png)](https://substackcdn.com/image/fetch/$s_!utTe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07b488d5-7b67-4616-ac8c-13a52487575b_1024x559.png)

If we do not simply underline nouns, how do we find candidate objects?

The answer is not to ignore domain language. Domain language matters. The problem is treating every noun as if it automatically deserves a class.

Candidate objects can come from many signals:

[![Image 13](https://substackcdn.com/image/fetch/$s_!zXsJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdafb5571-9d6c-48e7-9461-17ef8af3cf1e_2748x789.png)](https://substackcdn.com/image/fetch/$s_!zXsJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdafb5571-9d6c-48e7-9461-17ef8af3cf1e_2748x789.png)

[![Image 14](https://substackcdn.com/image/fetch/$s_!RpK5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37de79c1-9b3b-400d-8d89-0f01c7ece77a_2723x764.png)](https://substackcdn.com/image/fetch/$s_!RpK5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37de79c1-9b3b-400d-8d89-0f01c7ece77a_2723x764.png)

```
flowchart TD
    Scenario[Usage scenario] --> Responsibilities
    DomainLanguage[Domain language] --> CandidateConcepts[Candidate concepts]
    BusinessRules[Business rules] --> PolicyObjects[Policy objects]
    ExternalSystems[External systems] --> BoundaryObjects[Boundary objects]
    Relationships[Complex relationships] --> Structurers
    Events[Domain events] --> EventObjects

    Responsibilities --> Candidates[Candidate objects]
    CandidateConcepts --> Candidates
    PolicyObjects --> Candidates
    BoundaryObjects --> Candidates
    Structurers --> Candidates
    EventObjects --> Candidates

    Candidates --> Keep[Keep]
    Candidates --> Rename[Clarify]
    Candidates --> Merge[Merge]
    Candidates --> Reject[Reject]
```

Finding candidates is only half the work.

The other half is rejecting weak ones.

A candidate object should be questioned if it only exists because a noun appeared in a requirement, if it only holds data and exposes getters, if its responsibility is vague, if it duplicates another object’s responsibility, or if it creates a boundary before the design needs one.

That does not mean small objects are bad. It means an object must earn its place by carrying meaning, behaviour, or collaboration value.

A useful question is:

> Would removing this object make the design less clear, or only shorter?

If the design becomes clearer without it, the object may not be real yet.

Assigning responsibilities is the difficult part of object design.

It is easy to say that objects should have responsibilities. It is harder to decide where a responsibility belongs.

Responsibility-Driven Design (RDD) does not remove judgment, but it gives judgment better questions.

![Image 15](https://substackcdn.com/image/fetch/$s_!xMc5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71069dab-a867-44fc-88fe-8b6a8a84d014_2745x627.png)

One useful heuristic is “keep behaviour near the knowledge it needs”. But it must not be applied mechanically.

For example, we may try to put borrowing eligibility directly on `Member`:

That may be reasonable if the decision is mostly about member state. But if eligibility depends on loan limits, membership type, book category, library branch policy, and temporary suspension rules, then `Member` may become overloaded.

A clearer responsibility home may be `BorrowingPolicy`:

This is not about extracting for the sake of extracting. It is about asking where the decision belongs.

The better heuristic is:

> Keep behaviour near the knowledge it needs, unless doing so gives the object responsibilities that do not belong to its role.

That sentence is one of the most useful parts of Responsibility-Driven Design (RDD). It protects us from both extremes: passive data objects on one side and bloated domain objects on the other.

Responsibilities do not live in isolation.

An object fulfils a responsibility by doing its own work or by collaborating with others.

In Object-Oriented Programming (OOP), collaboration happens through messages. In most mainstream languages, that usually means method calls. But the design idea is larger than the syntax.

A message says:

> I need you to do something you are responsible for.

A contract says:

> This is what you can expect when you ask me to do it.

A protocol is the set of messages an object offers to its collaborators.

For example:

For this example, we might read the contract like this:

[![Image 16](https://substackcdn.com/image/fetch/$s_!rnvG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c07c751-8573-4aab-9288-2ae6f6a610cb_1434x596.png)](https://substackcdn.com/image/fetch/$s_!rnvG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c07c751-8573-4aab-9288-2ae6f6a610cb_1434x596.png)

The name `BorrowingDecision` matters because it says what the object represents. It is not a generic response. It is the result of assessing whether borrowing is allowed.

A contract should avoid leaking implementation details into the client. `LendBookService` should not need to know the internal order of policy checks. It should ask for a decision and act on it.

That is encapsulation as design language.

Not just private fields.

A responsibility becomes concrete through a protocol. But the protocol should not be invented too early. First the role must be real. Then the contract must be meaningful. Then the interface can earn its place.

[![Image 17](https://substackcdn.com/image/fetch/$s_!C701!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffef5e6e0-b051-4fe6-8f1e-7c043140e290_2307x726.png)](https://substackcdn.com/image/fetch/$s_!C701!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffef5e6e0-b051-4fe6-8f1e-7c043140e290_2307x726.png)

```
sequenceDiagram
    participant LendBookService
    participant BorrowingPolicy
    participant LoanRepository
    participant LoanNotificationSender

    LendBookService->>BorrowingPolicy: assess(member, activeLoans, bookCopy, today)
    BorrowingPolicy-->>LendBookService: BorrowingDecision
    LendBookService->>LoanRepository: save(activeLoan)
    LendBookService->>LoanNotificationSender: sendBookLentNotification(activeLoan)
```

A sequence like this helps because it shows behaviour over time. It reveals who asks, who answers, and who is responsible for each part of the scenario.

Class, Responsibility, Collaborator (CRC) cards are useful because they force a simple but important conversation:

*   What is this candidate responsible for?

*   What does it know?

*   What does it do?

*   Who does it collaborate with?

They are not useful because the card is magical. They are useful because they make the design conversation visible.

A weak card might look like this:

![Image 18](https://substackcdn.com/image/fetch/$s_!TV7c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2d23854-09ba-455e-aaf7-7637354a2e19_1857x377.png)

A better responsibility-driven version might look like this:

[![Image 19](https://substackcdn.com/image/fetch/$s_!pMM-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9d3696a-3297-4b97-8757-b6ba69be1fa0_1858x595.png)](https://substackcdn.com/image/fetch/$s_!pMM-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9d3696a-3297-4b97-8757-b6ba69be1fa0_1858x595.png)

This is still not a production ritual. It is a thinking tool.

The point is not to fill a card perfectly. The point is to ask whether an object has a real responsibility or whether we only gave a name to a thing.

https://emmanuelvalverderamos.substack.com/p/crc-cards-class-responsibility-collaborator

[![Image 20](https://substackcdn.com/image/fetch/$s_!vcwW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bb8df7d-7da1-4b93-bfc1-7015abfb7526_1024x558.png)](https://substackcdn.com/image/fetch/$s_!vcwW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bb8df7d-7da1-4b93-bfc1-7015abfb7526_1024x558.png)

Responsibility distribution affects the control style of the system.

There are three useful styles to think about:

1.   Centralized control

2.   Dispersed control

3.   Delegated control

A system can centralize control too much. In that style, one object knows the process, makes the decisions, tells everyone else what to do, and treats other objects mostly as data sources or technical endpoints. This may be easy to follow at first, but it often creates an object with centralized control, the kind of object many teams would casually call a God object.

A system can also disperse control too much. In that style, behaviour is spread everywhere, but without a clear sense of ownership. It becomes hard to know who is responsible for what. You avoid one dominant object, but you get a fog of tiny interactions where nobody can explain the flow.

The more useful middle is delegated control. A coordinator may still exist, but it does not do all the work. It delegates meaningful responsibilities to objects that are better homes for those responsibilities.

[![Image 21](https://substackcdn.com/image/fetch/$s_!gN2s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0dba436-7a67-433b-9bf3-33b11182535c_1868x520.png)](https://substackcdn.com/image/fetch/$s_!gN2s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0dba436-7a67-433b-9bf3-33b11182535c_1868x520.png)

[![Image 22](https://substackcdn.com/image/fetch/$s_!8Hn7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6cb8844-3bc5-4501-9cc2-ab1260e830db_2849x1320.png)](https://substackcdn.com/image/fetch/$s_!8Hn7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6cb8844-3bc5-4501-9cc2-ab1260e830db_2849x1320.png)

```
flowchart TD
    subgraph CentralizedControl[Centralized control]
        LendingServiceA[LendBookService] --> MemberA[LibraryMember]
        LendingServiceA --> LoansA[MemberLoans]
        LendingServiceA --> BookCopyA[BookCopy]
        LendingServiceA --> RepositoryA[LoanRepository]
        LendingServiceA --> SenderA[LoanNotificationSender]
        LendingServiceA --> CalendarA[Calendar]
    end

    subgraph DelegatedControl[Delegated control]
        LendingServiceB[LendBookService] --> BorrowingPolicyB[BorrowingPolicy]
        BorrowingPolicyB --> LoansB[MemberLoans]
        BorrowingPolicyB --> BookCopyB[BookCopy]
        BorrowingPolicyB --> MemberB[LibraryMember]
        LendingServiceB --> RepositoryB[LoanRepository]
        LendingServiceB --> SenderB[LoanNotificationSender]
        LendingServiceB --> CalendarB[Calendar]
    end
```

The difference is not that delegated control has more classes. The difference is that the work has a clearer shape.

`LendBookService` coordinates.  
`BorrowingPolicy` decides.  
`ActiveLoan` represents the loan.  
`LoanRepository` persists.  
`LoanNotificationSender` notifies.

That is the goal: not maximum distribution, but meaningful distribution.

Let us bring the ideas together in code.

Suppose we begin with this:

This code is not absurd. It may even be a reasonable first version.

But it has pressure.

`LendBookService` coordinates the use case, checks member eligibility, checks loan limits, checks book availability, creates the loan period, saves the loan, and sends the notification. Some of that may belong there. Some of it may not.

A responsibility-driven question is:

> Is lending responsible for deciding borrowing eligibility, or is lending responsible for asking whether borrowing is allowed?

That question lets us introduce a clearer responsibility:

> assess whether a member may borrow a requested book copy

One possible home is `BorrowingPolicy`:

Now `LendBookService` can coordinate at a higher level:

This is not a general rule that every condition must become a policy object. That would be another form of mechanical design.

The point is that a responsibility became visible. Once it became visible, we could ask where it belonged.

A responsibility-driven reading of the example might look like this:

[![Image 23](https://substackcdn.com/image/fetch/$s_!Fncz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8af2ce94-f696-4fec-93d3-a35ad6b4a809_1867x949.png)](https://substackcdn.com/image/fetch/$s_!Fncz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8af2ce94-f696-4fec-93d3-a35ad6b4a809_1867x949.png)

![Image 24](https://substackcdn.com/image/fetch/$s_!tghK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6702ff36-1512-4502-b656-5bd00d5d6b95_2511x556.png)

```
flowchart TD
    LendBookService --> Calendar
    LendBookService --> BorrowingPolicy
    BorrowingPolicy --> LibraryMember
    BorrowingPolicy --> MemberLoans
    BorrowingPolicy --> BookCopy
    LendBookService --> ActiveLoan
    ActiveLoan --> LoanPeriod
    LendBookService --> LoanRepository
    LendBookService --> LoanNotificationSender
```

The design now says something clearer.

The service coordinates the lending scenario. The policy decides whether the loan is allowed. The repository persists. The sender notifies. The values and information holders carry domain meaning.

That is Responsibility-Driven Design (RDD) in practice.

Not “make more classes”.

Not “hide everything behind interfaces”.

Not “avoid coordination”.

The lesson is simpler:

> Give behaviour a responsible home.

Not all collaborations are equal.

Some collaborations happen inside a trusted part of the model. Others cross boundaries where failure is normal.

This distinction matters because object-oriented design is not only about who talks to whom. It is also about how much trust is reasonable in that conversation.

In this simplified example, a collaboration between `LendBookService` and `BorrowingPolicy` can be designed with higher trust because both objects live inside the application model. If the domain values are valid, `BorrowingPolicy` can focus on the borrowing decision.

A collaboration between `LendBookService` and `LoanRepository` is different. Persistence can fail. A database may be unavailable. A write may conflict. A transaction may be interrupted.

A collaboration with notification is also different. An email provider can fail. A message can be delayed. A downstream consumer may be unavailable.

[![Image 25](https://substackcdn.com/image/fetch/$s_!6PKE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4c948dd-6a03-44e0-9eb0-89812b122a63_1659x1166.png)](https://substackcdn.com/image/fetch/$s_!6PKE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4c948dd-6a03-44e0-9eb0-89812b122a63_1659x1166.png)

```
flowchart LR
    subgraph ApplicationModel[Application model]
        LendBookService
        BorrowingPolicy
        ActiveLoan
        LoanPeriod
    end

    subgraph ExternalBoundaries[External boundaries]
        Database[(Database)]
        NotificationChannel[Notification channel]
    end

    LendBookService --> BorrowingPolicy
    LendBookService --> LoanRepository --> Database
    LendBookService --> LoanNotificationSender --> NotificationChannel
```

A table makes the difference visible:

[![Image 26](https://substackcdn.com/image/fetch/$s_!S9Cm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcaa02864-1139-4d7a-a0fc-6124a7eb2ec5_1860x593.png)](https://substackcdn.com/image/fetch/$s_!S9Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcaa02864-1139-4d7a-a0fc-6124a7eb2ec5_1860x593.png)

Reliability is responsibility allocation under uncertainty.

It is not enough to say that persistence can fail. We need to decide who notices the failure, who translates it, who decides what it means, and who takes recovery action.

[![Image 27](https://substackcdn.com/image/fetch/$s_!wshn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F017e90d6-76dc-475d-ab30-88436f23b730_1868x647.png)](https://substackcdn.com/image/fetch/$s_!wshn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F017e90d6-76dc-475d-ab30-88436f23b730_1868x647.png)

The point is not to make every object defensive against everything. That creates duplication and noise.

The point is to decide where trust is reasonable and where failure deserves explicit responsibility.

Flexibility is valuable, but it is not free.

Many object-oriented designs become over-engineered because every collaborator receives an interface, every rule becomes a strategy, and every small calculation becomes an object with a name. The design looks flexible, but the flexibility is speculative. The cost is paid immediately. The benefit may not arrive.

Responsibility-Driven Design (RDD) gives us a better question:

> Where is variation real enough to deserve a design boundary?

In the library example, some variation points are plausible.

Borrowing rules may vary by membership type. Loan periods may vary by book category. Notification channels may vary. Persistence mechanisms may vary. Holiday calendars may affect due dates.

Other things may not deserve flexibility yet.

A method that calculates whether one date is after another probably does not need an interface. A small value like `BookCopyId` is not a variation point. A simple `LoanPeriod` may not need a hierarchy.

[![Image 28](https://substackcdn.com/image/fetch/$s_!YwKO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54e2ff72-e6af-4bd7-a55e-9a39f5bd3990_1869x614.png)](https://substackcdn.com/image/fetch/$s_!YwKO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54e2ff72-e6af-4bd7-a55e-9a39f5bd3990_1869x614.png)

[![Image 29](https://substackcdn.com/image/fetch/$s_!yvkf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F063336bf-4105-4cae-8c90-da0bb9af077a_1400x1964.png)](https://substackcdn.com/image/fetch/$s_!yvkf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F063336bf-4105-4cae-8c90-da0bb9af077a_1400x1964.png)

```
flowchart TD
    VariationPoint[Potential variation point] --> ConcreteExamples{Do we have concrete variations?}
    ConcreteExamples -->|No| KeepSimple[Keep the design simple]
    ConcreteExamples -->|Yes| Impact{Does variation affect many clients?}
    Impact -->|No| Localize[Keep variation local]
    Impact -->|Yes| Boundary[Introduce explicit boundary]
    Boundary --> Contract[Define contract]
```

Patterns fit here, but not as decoration.

A pattern is useful when it expresses a better distribution of responsibilities.

[![Image 30](https://substackcdn.com/image/fetch/$s_!RqXq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8973884-57f0-4609-a78c-ef36c79de1f7_1351x625.png)](https://substackcdn.com/image/fetch/$s_!RqXq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8973884-57f0-4609-a78c-ef36c79de1f7_1351x625.png)

The pattern is justified only when the responsibility movement is justified.

Good design is not maximum abstraction. Good design is abstraction where it pays rent.

[![Image 31](https://substackcdn.com/image/fetch/$s_!i-FC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b100ef3-3eef-4e24-b742-c48087934fc3_1024x558.png)](https://substackcdn.com/image/fetch/$s_!i-FC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b100ef3-3eef-4e24-b742-c48087934fc3_1024x558.png)

Patterns deserve their own short reflection because they are often taught badly.

Many developers learn patterns as shapes. They recognize a class diagram, remember a name, and then look for a place to apply it. That is backwards.

From a Responsibility-Driven Design (RDD) perspective, a pattern is more useful when read as an arrangement of responsibilities.

Strategy is not “an interface with implementations”. It is a way to give a varying decision to interchangeable collaborators.

Observer is not “a list of subscribers”. It is a way to separate the fact that something happened from the objects that react to it.

Adapter is not “a wrapper”. It is a way to protect the model from a collaborator whose protocol does not fit the design we want.

State is not “classes for states”. It is a way to move state-dependent behaviour into the objects that represent those states.

That perspective is important because it prevents pattern worship. The pattern is not the goal. The responsibility movement is the goal.

In the library example, `BorrowingPolicy` might evolve into a strategy if borrowing rules vary by member type, branch, or material type. `LoanNotificationSender` might evolve toward an observer-like design if many parts of the system need to react to a `BookLent` event. `LoanRepository` may use an adapter internally to protect the application from a persistence framework.

But none of those choices should be automatic.

First understand the responsibility. Then understand the collaboration. Then choose the structure that expresses them well.

Responsibility-Driven Design (RDD) is not about collecting classes.

It is a way of thinking about object-oriented software as a community of responsible collaborators.

That changes the starting point. We do not begin with data and then attach behaviour. We begin with behaviour and ask where responsibility belongs. We do not reduce objects to containers. We treat them as participants. We do not centralize every decision in one smart service. We distribute intelligence across objects that know how to do their work.

We do not use Class, Responsibility, Collaborator (CRC) cards because cards are magic. We use them because they make responsibilities and collaborations visible. We do not delegate because indirection is good. We delegate because another object is a better home for the work.

We do not add flexibility everywhere. We add it where variation is real. We do not add interfaces because classes exist. We add boundaries when a role, a contract, or a trust boundary earns one. We do not use patterns to decorate code. We use patterns when they express a better distribution of responsibilities.

Good Object-Oriented Programming (OOP) is not about having more classes, more interfaces, or more pattern vocabulary. It is about making the system easier to understand because responsibilities are named, behaviour has a home, collaboration has a shape, and control lives where it belongs.

The best object designs do not feel like a pile of classes.

They feel like a community of objects that know what they are responsible for and know when to ask each other for help.

*   Beck, Kent; Cunningham, Ward. _A Laboratory for Teaching Object-Oriented Thinking_.  
[https://c2.com/doc/oopsla89/paper.html](https://c2.com/doc/oopsla89/paper.html)

*   Cooper, Ian. _Responsibility Driven Design Revisited_.

[Video 3](https://www.youtube.com/watch?v=xOpUpRIpH6k)

*   Freeman, Steve; Pryce, Nat. _Growing Object-Oriented Software, Guided by Tests_.

[https://www.growing-object-oriented-software.com/](https://www.growing-object-oriented-software.com/)

*   West, David. _Object Thinking_.  
[https://www.microsoftpressstore.com/store/object-thinking-9780735619654](https://www.microsoftpressstore.com/store/object-thinking-9780735619654)

*   Wirfs-Brock, Rebecca. _Object Technology: Basic Concepts_.  
[https://www.informit.com/articles/article.aspx?p=3109983](https://www.informit.com/articles/article.aspx?p=3109983)

*   Wirfs-Brock, Rebecca. _Responsibility-Driven Design_.  
[https://www.wirfs-brock.com/Design.html](https://www.wirfs-brock.com/Design.html)

*   Wirfs-Brock, Rebecca; McKean, Alan. _Object Design: Roles, Responsibilities, and Collaborations_.  
[https://www.informit.com/store/object-design-roles-responsibilities-and-collaborations-9780201379433](https://www.informit.com/store/object-design-roles-responsibilities-and-collaborations-9780201379433)

*   Wirfs-Brock, Rebecca; Wilkerson, Brian; Wiener, Lauren. _Designing Object-Oriented Software_.  
[https://archive.org/details/designingobjecto00wirf](https://archive.org/details/designingobjecto00wirf)
