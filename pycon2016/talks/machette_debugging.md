# Machette Debugging (Ned Batchell)

# Using Pythons chaos to debug
* Look up Ned Batchell blog posts.
* Don't use any of this in production code.

# Case one: Double importing
`inspect.stack`

# Different import paths can import files twice
    import thing.apps.first.models
    import first.models

This causes the import function to have different keys which causes double
imports.

This is also a problem with

    sys.path.append("thing/apps")
    sys.path.append("other/apps")

# Lessons Case 1
* import runs code
* if it's short lived, just hard code it.
* Wrong is OK.

# Case 2: Finding temp file creators
* " I'm upgrading grep to 'static analysis' which makes it sound fancy."
* The problem is that things are being left behind.
What happens if we use the things left behind to give you bread crumbs?
Let's monkeypatch the mkdtemp such that the file names are the function names.
* Definitely don't do this in production.
* The funny bit about monkeypatching is that it has to be run before the code
you want to monkeypatch.

# Running code on startup
* Site-packages/*py  will run the first `import ` line or add the file path
to the `sys.paths` dictionary.

# Lessons Case 2
* std lib is very readable.
* std lib is also patchable.
* Use whatever you can touch and change.
* Do use addCleanup

# Case 3: Who's chaing sys.path
* sys.path was modified unexpectedly.
* grep didn't find sys.path
* Third party?
* Knowing about dynamic analysis.

# Data break points
* pdb doesn't have them.
* So they wrote a trace function.

    def trace(frame, event, arg):
        pass
    sys.settrace(trace)

# Case 3 Lessons
* It's not just your code
* Dynamic analysis is very powerful and Python is great at it.
* Sometimes you need to use Big Hammers. More time on the computers part is
great.
* Case 4: Randomized Problems:

* Randomized but repeatable

    random.seed(1702)  @student.seed

# Problem code

    print(random.randint(1, 1000)) # 420?

* first time 284
* seocnd time 420?

# 1/0
* easy to drop in
* Unlikely exception: ZeroDivisionError
* easy to spot

    import random
    random.random = lambda 1/0

# Exceptions are a great source of information
* Don't be afraid to blow things up.
* sometimes you get lucky.
* Don't share global state.
* Do use your random object, do suspect third-party code

# Big Lessons
* Break conventions to get what you need.
* But only for debugging.
* Dynamic analysis is great in Python.
* Understand the mechanisms that make up Python.
