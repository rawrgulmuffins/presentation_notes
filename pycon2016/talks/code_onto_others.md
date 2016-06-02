# Code onto others (Nathaniel Manista, Augie Fackler)
* What's a problem? May not be a problem for compiler or interpreter or users.
* Sadly, software is made of people.
* Humans don't scale so readability really matters. Specifically, you don't
scale.

# Lack of Cohesion
* "If we gave you the first half of the class we'd guess that you couldn't
correctly guess what's in the last half."
* Mixing function and convenience. Better to have both split up.
* Mixing layers of abstraction.
* Just too many elements in API. 7 elements is about the sweet spot you want to hit.
* "it does this and this." Is a good clue about subdivisions.
* Classes shouldn't make you say  "I better put a pot of coffee on."

# Looking At Long Function.
* looking at values that were used in line compared to values in scope.
* Your brain is working memory, you need to be aware of how much you can retain.

# Requirements Of Any Software Change:
* A change must meet a need in the domain of the software
* A change must sufficently understand the scope of the code base and the problem being fixed.
* Most of the time we think about code that will only live for a little while.


# Silver Bullets
* Learning a problem domain can't be generically easier. But making a code
base easier to maintain and read makes it easier to change problems.
* It's easier to know state changes and program control than it is to know
domain knowledge.

# Do where the doing is simplist
* Code where the coding is simpliest? Not sure what that means.

    class bar(foo):
        ANSWER = 42

* Placing code at class scope invites a lot of questions.
* Avoid placing code elements at class scope unless you have an alternative.
* The class cannot function as a required by it's users without the code class
sscope.
* Use module scope as your default.

# Be A Class Realist
* Structure and aggregate data.
* Purely abstract classes define types.
* Classes implement pre-defined types.
* Classes are a way to create slightly different states for the same type.

#  Classes Are Not For Being Functions

    my_object = class_creation()
    data = my_object.method()

# Enumerated Polymorphism
* A base class that as a small set of potential subclasses.

# Mixins (Eww, Yuck!)
* Your class tries to use them but also becomes them.
* Avoid self-use of public API's. This normally betrays abstraction leaks.
* "In layers of the class you should only call donw in layers of the class."
* "This calls into question what is a lower level of abstraction or a higher
abstraction."
* Pass something less than self

# Things To Say About Modules
* Always place imports at the top of modules.
* import modules referenced in specifications.
* default to private variables at module scope (using `_`).

# Advanced Techniques
* "You've had a problem on the brain for weeks. Are you the best person to tell
what's obvious and obscure."
* If you have a long function the functions probably not just a black box. It's
also probably about the intermediate values between steps a to z.
* Don't abbrevaiate when naming.

# Your users and your maintainers are two very different audiances
* Sort your definitions in use-order
* Have a public API in a different documentation structure
* And make your code itself have standards that make programmers happy.
