---
title: "Materialization: turning a false peer into an internal"
subtitle: "A refactor to demote a peer"
requested_url: "https://emmanuelvalverderamos.substack.com/p/materialization-turning-a-false-peer"
canonical_url: "https://emmanuelvalverderamos.substack.com/p/materialization-turning-a-false-peer"
substack_post_id: 175454440
retrieved_at: "2026-03-27T08:57:51.875Z"
---
# Materialization: turning a false peer into an internal

### A refactor to demote a peer

> This article shows a refactoring we call **Materialization**. The example starts from a common but suboptimal design, in which an object’s tests are coupled to the interface of a collaborator that is actually an internal. To refactor it we will add a safety net, remove the double and stop injecting the internal while keeping the observable behavior intact.

## Definition

**Materialization.** Refactoring to **demote a peer, that is not pulling its weight, to be treated as an internal**.

*“**Not pulling its weight**” means that we are getting little or no testability benefits from coupling an object’s tests to the interface of a collaborator, i. e., treating the collaborator as a peer creates more pain than benefits as we evolve the code.*

## Before reading this article, you may want to read

---

Crafting software is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

Let’s see an example of this. Let’s say we have a system in this state.

[![](https://substackcdn.com/image/fetch/$s_!z1VG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F963187ea-8e57-4dd9-9f31-0f3ed40ae28f_13972x12875.png)](https://substackcdn.com/image/fetch/$s_!z1VG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F963187ea-8e57-4dd9-9f31-0f3ed40ae28f_13972x12875.png)

**The object:**

We will focus on how `SimulatedSecurityManager` interacts with `UserDataRequester`, and on its implementation `TextUserDataRequester`,

```
namespace Security;

public class SimulatedSecurityManager
{
    private readonly Encrypter _encrypter;
    private readonly Notifier _notifier;
    private readonly UserDataRequester _userDataRequester;

    public SimulatedSecurityManager(Notifier notifier, UserDataRequester userDataRequester)
    {
        _notifier = notifier;
        _userDataRequester = userDataRequester;
        _encrypter = new Encrypter();
    }

    public void CreateValidUser()
    {
        var userData = _userDataRequester.Request();

        if (userData.PasswordsDoNotMatch())
        {
            NotifyPasswordDoNotMatch();
            return;
        }

        if (userData.IsPasswordToShort())
        {
            NotifyPasswordIsToShort();
            return;
        }

        NotifyUserCreation(userData);
    }

    private void NotifyPasswordIsToShort()
    {
        _notifier.Notify(”Password must be at least 8 characters in length”);
    }

    private void NotifyPasswordDoNotMatch()
    {
        _notifier.Notify(”The passwords don’t match”);
    }

    private void NotifyUserCreation(UserData userData)
    {
        _notifier.Notify(
            $”Saving Details for User ({userData.UserName()}, {userData.FullName()}, {userData.EncryptPassword(_encrypter)})\n”
        );
    }
}
```

**The interface:**

```
namespace Security;

public interface UserDataRequester
{
    UserData Request();
}
```

**The “peer” implementation:**

```
namespace Security;

public class TextUserDataRequester : UserDataRequester
{
    private readonly InputReader _inputReader;

    public TextUserDataRequester(InputReader inputReader)
    {
        _inputReader = inputReader;
    }

    public UserData Request()
    {
        return new UserData(
            RequestUserName(),
            RequestFullName(),
            RequestPassword(),
            RequestPasswordConfirmation()
        );
    }

    private string RequestPasswordConfirmation()
    {
        return _inputReader.Read(”Re-enter your password”);
    }

    private string RequestPassword()
    {
        return _inputReader.Read(”Enter your password”);
    }

    private string RequestFullName()
    {
        return _inputReader.Read(”Enter your full name”);
    }

    private string RequestUserName()
    {
        return _inputReader.Read(”Enter a username”);
    }
}
```

**The test:**

For `SimulatedSecurityManager`:

```
using NSubstitute;
using NUnit.Framework;

namespace Security.Tests.Unit;

public class SimulatedSecurityManagerTest
{
    private Notifier _notifier;
    private SimulatedSecurityManager _simulatedSecurityManager;
    private UserDataRequester _userDataRequester;

    [SetUp]
    public void Setup()
    {
        _notifier = Substitute.For&lt;Notifier&gt;();
        _userDataRequester = Substitute.For&lt;UserDataRequester&gt;();
        _simulatedSecurityManager = new SimulatedSecurityManager(_notifier, _userDataRequester);
    }

    [Test]
    public void do_not_save_user_when_password_and_confirm_password_are_not_equals()
    {
        _userDataRequester.Request().Returns(new UserData(”username”, “fullName”, “Pepe1234”, “Pepe1234.”));

        _simulatedSecurityManager.CreateValidUser();

        _notifier.Received(1).Notify(”The passwords don’t match”);
    }

    [Test]
    public void do_not_save_user_when_password_too_short()
    {
        _userDataRequester.Request().Returns(new UserData(”username”, “fullName”, “Pepe123”, “Pepe123”));

        _simulatedSecurityManager.CreateValidUser();

        _notifier.Received(1).Notify(”Password must be at least 8 characters in length”);
    }

    [Test]
    public void save_user()
    {
        _userDataRequester.Request().Returns(new UserData(”username”, “fullName”, “Pepe1234”, “Pepe1234”));

        _simulatedSecurityManager.CreateValidUser();

        var encryptedPassword = “4321epeP”;
        _notifier.Received(1).Notify($”Saving Details for User (username, fullName, {encryptedPassword})\n”);
    }
}
```

**For the “peer” implementation:**

```
using NSubstitute;
using NUnit.Framework;

namespace Security.Tests.Unit;

public class TextUserDataRequesterTest
{
    private InputReader _inputReader;
    private TextUserDataRequester _userDataRequester;

    [SetUp]
    public void SetUp()
    {
        _inputReader = Substitute.For&lt;InputReader&gt;();
        _userDataRequester = new TextUserDataRequester(_inputReader);
    }

    [Test]
    public void request_user_data()
    {
        InputByConsole(
            “username”,
            “fullname”,
            “password”,
            “confirmationPassword”
        );

        var userData = _userDataRequester.Request();

        Assert.That(userData, Is.EqualTo(
                new UserData(
                    “username”,
                    “fullname”,
                    “password”,
                    “confirmationPassword”
                )
            )
        );
    }

    private void InputByConsole(string username, string fullName, string password, string confirmPassword)
    {
        _inputReader.Read(”Enter a username”).Returns(username);
        _inputReader.Read(”Enter your full name”).Returns(fullName);
        _inputReader.Read(”Enter your password”).Returns(password);
        _inputReader.Read(”Re-enter your password”).Returns(confirmPassword);
    }
}
```

## How to apply materialization

The recipe for this refactor:

- Apply a parallel change to refactor the tests of the object using the peer we want to materialize so that they stop using a test double of the peer and start using its implementation instead.
- Instantiate the implementation of the peer inside the constructor.
- Remove the parameter from the constructor.
- Remove the interface and rename the class that previously implemented it.

### 1. Refactor the test of the object using the peer

After applying the parallel change, we get to the following tests in which we are injecting the implementation of the peer’s interface instead of a test double:

```
using NSubstitute;
using NUnit.Framework;

namespace Security.Tests.Acceptance;

public class SimulatedSecurityManagerTest
{
    private const string Username = “Pepe”;
    private const string FullName = “Pepe Garcia”;
    private InputReader _inputReader;
    private Notifier _notifier;
    private SimulatedSecurityManager _simulatedSecurityManager;

    [SetUp]
    public void Setup()
    {
        _notifier = Substitute.For&lt;Notifier&gt;();
        _inputReader = Substitute.For&lt;InputReader&gt;();
        _simulatedSecurityManager = new SimulatedSecurityManager(_notifier, new TextUserDataRequester(_inputReader));
    }

    [Test]
    public void do_not_save_user_when_password_and_confirm_password_are_not_equals()
    {
        IntroducingUserDataWithPasswords(password: “Pepe1234”, confirmationPassword: “Pepe1234.”);

        _simulatedSecurityManager.CreateValidUser();

        Notified(”The passwords don’t match”);
    }

    [Test]
    public void do_not_save_user_when_password_too_short()
    {
        IntroducingUserDataWithPasswords(password: “Pepe123”, confirmationPassword: “Pepe123”);

        _simulatedSecurityManager.CreateValidUser();

        Notified(”Password must be at least 8 characters in length”);
    }

    [Test]
    public void save_user()
    {
        IntroducingUserDataWithPasswords(password: “Pepe1234”, confirmationPassword: “Pepe1234”);

        _simulatedSecurityManager.CreateValidUser();

        var encryptedPassword = “4321epeP”;
        Notified($”Saving Details for User ({Username}, {FullName}, {encryptedPassword})\n”);
    }

    private void IntroducingUserDataWithPasswords(string password, string confirmationPassword)
    {
        _inputReader.Read(”Enter a username”).Returns(Username);
        _inputReader.Read(”Enter your full name”).Returns(FullName);
        _inputReader.Read(”Enter your password”).Returns(password);
        _inputReader.Read(”Re-enter your password”).Returns(confirmationPassword);
    }

    private void Notified(string message)
    {
        _notifier.Received(1).Notify(message);
        _notifier.Received(1).Notify(Arg.Any&lt;string&gt;());
    }
}
```

### 1…4 Final version. The peer was demoted to an internal

```
namespace Security;

public class SimulatedSecurityManager
{
    private readonly Encrypter _encrypter;
    private readonly Notifier _notifier;
    private readonly TextUserDataRequester _userDataRequester;

    public SimulatedSecurityManager(Notifier notifier, InputReader inputReader)
    {
        _notifier = notifier;
        _userDataRequester = new TextUserDataRequester(inputReader);
        _encrypter = new Encrypter();
    }

    public void CreateValidUser()
    {
        var userData = _userDataRequester.Request();

        if (userData.PasswordsDoNotMatch())
        {
            NotifyPasswordDoNotMatch();
            return;
        }

        if (userData.IsPasswordToShort())
        {
            NotifyPasswordIsToShort();
            return;
        }

        NotifyUserCreation(userData);
    }

    private void NotifyPasswordIsToShort()
    {
        _notifier.Notify(”Password must be at least 8 characters in length”);
    }

    private void NotifyPasswordDoNotMatch()
    {
        _notifier.Notify(”The passwords don’t match”);
    }

    private void NotifyUserCreation(UserData userData)
    {
        _notifier.Notify(
            $”Saving Details for User ({userData.UserName()}, {userData.FullName()}, {userData.EncryptPassword(_encrypter)})\n”
        );
    }
}
```

From this moment on, the object `TextUserDataRequester`is no longer a peer; it has become an internal of `SimulatedSecurityManager`. However, it is still seen by the tests that validate its behavior directly. At this point, we have two options:

- If you want no tests to see the object, you need to cover its behavior by adding new tests to the object that uses it. Once the behavior is covered from there, delete the tests that target it directly. At that point, the collaborator would be completely an internal detail of the object that uses it (only that object would “see” it).
- Inline it into private methods if the behavior is truly trivial.

[![](https://substackcdn.com/image/fetch/$s_!KYTH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9eb3bb1f-953b-4e20-9c3e-26cfb9cf97e6_13972x12873.png)](https://substackcdn.com/image/fetch/$s_!KYTH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9eb3bb1f-953b-4e20-9c3e-26cfb9cf97e6_13972x12873.png)

## When to materialize

If treating a collaborator as a peer creates more pain than benefits for the evolution of the code.

**Do not materialize a peer if**

- The collaborator matches a peer stereotype (it is a real peer):
	- Dependency
	- Strategy
	- Notification
- Even though it not matches any peer stereotype, its behavior is so complex (high cyclomatic complexity) that it is worth it to test it independently, in order to improve the overall readability, writability, specificity or composability of the tests.
- It is simplifying the interaction with several collaborators (this is related to **bunding up**)

## What may lead to a peer that is not pulling its weight?

- Considering the class as the unit.
- After applying a **[breaking out](https://codesai.com/posts/2025/11/breaking-out-to-improve-cohesion)** and promoting an internal collaborator to a peer, we identify that we are getting little or no testability benefits from coupling to its interface.
- We applied **budding off**, and we lost the design bet.

## Possible pitfalls

- **Materializing a real peer**: You will couple your use case to a concrete implementation and may introduce testability problems.

## Closing

Materialization is a targeted **refactoring**. It converts a false peer into an internal, so your tests stop referencing it.

Apply **Materialization** to couple tests only to interfaces that provide some testability improvements. This refactoring can help you simplify your design when a peer is not pulling its weight and we can do with an internal.

## Acknowledgments

Thanks to **Manuel Rivero** for the thoughtful feedback that sharpened the framing of Materialization as a refactoring and for the two-step recipe to convert a false peer into an internal. Also, thanks to **Ángel Siendones Sillero** and the **Ensemble Podcasting** colleagues for helping coin and popularize the term **Materialization** in this context.
