# Optimizations which made Python 3.6 faster then Python 3.5 (Victor Stinger)
## Benchmarks
* Benchmark instability is when you run a benchmark twice and get very
different results.
* New Python module: perf.
* Not doing IQR computation in perf module
* Spawns 20 processes sequentially, 3 values per process for 60 measurements.
* `$ sudo python3 -m perf system tune`
* "Python3.6 is significantly faster then 2.7 at this point."

## Python 3.6 optimizations
* `lru_cache` is now in c.
* `sympy` is 20% faster.
* `collections.OrderedDict` in c.
* `PyMem_malloc()` to use faster memory allocator
* `PYTHONMALLOC-debug` now available in release builds to detect memory
corruptions, bpo-262`49
* The `PyMem_malloc` change will effect how fast messages is readable.
* "Profile Guided Optimization" (PGO) Custom compiled Python that fits your
hardware architecture.
* bpo-24915
* PGO leads to 5%-27% faster python code for your specific case.
* bpo-26647 - 2 byte opcodes instead of 1 or 3 byte optcodes
* PEP 461
* glob: 3 to 6 times faster
* pathlib glob 1.5 to 4 times faster
* Asyncio programs are now around 30% faster (bpo-26081, bpo-28544)
* In python 3.7 method calls ar enot 10-20% faster

# Immutable Programming - Writing Functional Python (Calen Pennington)
* @vengefulpickle
* Immutability allows local thinking. You don't need to know what the rest of
the code does.
* Command Pattern
* @propery on a def for kind of lighter syntatic classes.
* "Spooky action at a distance."
* Python needs to be able to take in an "interface" object in function
definitions that checks to make sure that all functions or methods that use
that interface are changed at the same time. - Talk more with Tucker about this
* Really need to color code slides. I need to put some time into making pretty
slides in the future.
* Didn't cover tradeoffs. Didn't cover memory problems, didn't cover shared
mutable state, didn't talk about concurrency.

# Grok the GIL: Write Fast And Thread-Safe Python
* PyThread_type_lock is just an alias for whatever your systems basic log is.
* "One thread runs Python, while N other sleep or await I/O"
* Cooperative Multi-tasking or Preemptive multitasking
* Python2 used 1000 bytecodes for preemptive and 3 uses 50 ms.
* `PY_BEGIN_ALLOW_THREADS`
* `PY_END_ALLOW_THREADS`
* Python does have thread sharing on the single CPU.
* debuggers register callback functions using `c_tracefunc` in the case of pdb.
* `c_profile_func` is the callback for profilers.
* `PyThread_release_lock`
* `PyThread_aquire_lock`
* dis.dis is still really cool. But it also lets you see all of the byte codes
that python lines generate which lets you know what lines have critical values.
* "Shared mutible state."
* Concurrency and Parallelism have the same dictionary definition and different
computer science definitions.
* 10 threads downloaded 1000 urls in 16 seconds, 100 in 2.27
* Python does concurrency really well with threads and Parallelism really
poorly.
* `os.fork` is an option in Python.
* Threads for concurrency, processes for parallelism.
* bit.ly/grok-the-gil
* It wasn't hard to understand what the GIL actually is and does.

# Packing Let's Encrypt: Packing for Millions of Users
* Let's encrpyt started in 2012
* cross-signed by IdenTrust
* certbot
* certbot-auto
* pip-strap
* Pip doesn't have a dependency resolver. This means that if any of your
dependencies specify a package version last write wins.
* Just because a python package was pip installable on your machine doesn't
mean it's going to work on another machine. Python packages do have OS
dependencies.
* Use only one distrbution method.
* People don't like it when you change their system setup.
* eff.org/about/opportunities/jobs

# Effective Code Review (Erik Rose)
* Clerity of Explenation
* Clerity of Expectation

## Tact Hacks
* The question mark.
* You, We, Thus
* Compliments: positive compliments because we haven't seen the code yet.
* Humor

## Nitpicks
* Using Mechanical means to meet style guides
* Have someone to manage disagreements
* try to not let perfect be the enemy of better.

## Slow Turnarounds
* de-energizing
* Comprehensiveness not required
* respect working memeory
* Quick "no's" are better

# Dask: A Pythonic Distributed Data Science Framework (Matthew Rocklin)
* Dask.array is a set of set of numpy array.
* dask.dataframe
* How does node setup work with Dask?
* How does multi-tenancy work with clusters?
* local computation runs on a thread pool by default.
* Bokeh dashboards (look into)
* I'm really interested in both Dask and Bokeh
* Sinlge machine or multi-machine dynamic task scheduler
* Dask can take dynamic new tasks.
* `a = yield func_call( * args)` # The space is to get vims syntax highlithing to shut up

# Writing a Transpiler:
* exec, eval, ast, py_compile, dis
* ast.parse("file_name")
* ast contains the visitor pattern.
* Transpile to compiled representation

# The Fastest FizzBuzz In The West
* RPLY, PLY, LEX, Yacc, RPython

## Let's Make A Lexer
* `from rply impot LexarGenerator; lg = LexarGenerator(); lg.add("ELLIPSIS", r"\.\.\.")`
* 

# The Dictionary Even Mighter (Brandon Rhodes)
* Learn by extrapolating
* Take Away: Assign every possible attribute in `__init__()`
* medium.com/@robertgrosse/generating-64-bit-hash-collisions-to-dos-python-5b21404a5306
* Python -R flag to protect against DDOS
* Pep 509
* Compact Dictionaries
* Issue 27350 adds compact dict change.

# Building a C Extension in Python 2017 (Jean-Baptiste Aviat)
* `from distutils.core import setup, Extension`
* ```
ulimit -c unlimited`; python -m run_me.py
[1]     28653 abort (core dump) ...

libd -c core.28653
```
* On OS10 library/Application/Support/CrashReports
* valgrind ./myExtension
* clang --analyze file.c
* clang --asan file.c
* http://lcamtuf.coredump.cx/afl
* Pep503 - Many Linux wheels is compatible with most real world linxues.
* Only on pip >= 8.1
* github/com/pypa/manylinux

# Cython
## Performance Options
* Microservices, C Extensions, PyPy, Pyston, GrumPy
* Update CPython
* Cython
## Cython Brief Dive
* cdef
* def <return_value) function(<type> <name>)
* cdef
* cpdef
* cdef int[:, :, :] data # memory views like Numpy arrays
* cdef class PyConSpeaker

# Kubernetes For Pythonistas (Kelsey Hightower)
* "It's hello world! I can do that on a piece of paper." -Kelsey Hightower
* "Freebsd is a little too into it. They have tattoes of their mascot. like,
you know that's never coming off right?" 
* "Hold my keyboard" - Kelsey Hightower
* "This only solves the laptop problem." - Kelsey Hightower
* "We call todays solution is the meatclock. They determine where everything
will run with this fancy thing called a spread sheet." - Kelsey Hightower
* You need to know all error scenarios, if the machine is in maintenance,
* A load balancer acts as a stable end point for an app.
* "Ok, that was pretty dope."

# Random notes
* 12 sigma app? (talk to tucker)
