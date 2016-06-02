So you have these long running jobs that takes forever and a day to run.

So you use multiprocess to do a simple scatter gather but it still takes 48 hours to just grep a bunch of files.

What do you do?

Potentially you use something like Celery so that you can throw more hardware at the problem.

Is that the best solution? I don't know, that's why I'm at this conference.

But you find yourself with this Celery cluster and enough horse power to  push some greek dude and a rock over a hill.

Go team. You can now grep a bunch of files fast enough to get results by the time you take the train from Seattle to Portland.

Suddenly a new challenger appears. 

Your team changes what you're greping for or how the results look. Maybe you even change your celery workers because they're fiddly and look at you funny.

Now you need to update some files on each of your Celery workers so that they don't all disagree and murder each other.

Your first solution is probably to use Puppet or Chef to manage said files.

Puppet and you don't really get along but you still run in the same social circles so at least your civil.

You start off by just putting a pip distribution in a Puppet module. Hard coding is good time .

But now you have create two shiny new problems for yourself.

Every time you make even a tiny change to your search files or task files you have to push to puppet

and you have to wait for each node to pull said code

and you get no notification that puppet as pulled such code.

This makes you a very sad panda.

So then you change to puppet just pulling the latest version from git master

but this doesn't fix the second and the notification problem so you are an equally sad panda.

In your desperation you might find this project called fabric.

Fabric lets your write shell commands that will run on every box in parallel and reports the results.

It's kind of like tmux split windows except you can make mistakes without causing catastrophy.

So you write a function like 

    celery_start
    celery_stop
    celery_restart
    upgrade_search_files
    upgrade_tasks
    quick_start

And suddenly you get to push new versions of code when you want to.

Key word, push.

You get failure output like this

and success output like this

You can even push branches because your just running shell commands in a readable and re-runnable fashion.

Now I don't have to cry myself to sleep because computers are hard and I hate them.

Ok, that's a lie. Computers are still hard but I hate them a little less now.
