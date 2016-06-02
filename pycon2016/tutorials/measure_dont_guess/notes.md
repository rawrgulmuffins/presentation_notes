# Measure Don't Guess (

* The first step is to always ensure that your program works correctly.

# The Price
* Optimization often comes at the price of readability.

# General guidelines
* Make sure your program is actually really slow.
    * Check other slow down factors (like networking)
* Does it hurt that your program runs slow?
* Only realistic use cases and user experiences should be considered.
* Architecture can be essential for performance.
* Bugs are often causes of slow down in programs.
* If the program is really too slow, find the bottleneck by profiling.
* You need tests to ensure that optimization doesn't change your results.
* Go for algorithms first. Typically most performance gains are algorithm
changes.
* Find the worse case and average case run time for your program.
* Hardware is also sometimes a great solution to slow downs. 

# The problem of profilers
* If you get strange results always check with a different method to make sure
that you observation isn't affecting the results.

# Wall time vs CPU time
* This is particulary import for Windows systems since clock and time in Python
return different results.

# Holy SHIT SNAKEVIZ
* !!!!

# sys.getrefcount
* This is so fucking cool.

    sys.getrefcount(1) # Returns something like 7000 references.

# %%python2 

* Again, holy shit.

# Guppy doesn't seem to want to compile with the latest version of Clang

* Looks like the latest patch was in 2013 so this seems to be a dead project.

# Meta note about tutorials
* If you have students download anything during the tutorial you have failed.
* If you don't have your programs pre-ready (as in you have to open things) you have failed.
* Don't invent words unless you are going to spend a lot of time on them.
* One change I want to make to Jupyter this week is a mode that turns jumping
off when a cell output is displayed.
* Jupyterhub notebook sharing patch.
* Show your users where the fuck you are. Have your terminal print the current path.
* If your content is good enough all the other fuck ups don't break the tutorial.
* Give everyone shit to pip install before hand.
* Lecturing is not teaching. Lecture is giving out facts but that doesn't
mean that people are retaining facts. It's better now a days that people hand
out Jupyter notebooks because that means people can self teach with said facts.
There's still a lot of room to learn.
