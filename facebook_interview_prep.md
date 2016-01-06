# Instructor
* Name: Gayle
* Email: g@gayle.com
* Subject: fbprep

# How to Approach

## Scope
* Ask Questions
* Make appropriate assumptions
* Bad Sample "Overall best seller doesn't mean sum of all time. It often means sum over a specific window."

## key components
* Can be somewhat naive

## Identify Issues
* Bottlenecks, tradeoffs

## Repair and redesign

## NOTE
Having a high level slide with ideas followed by details is a good idea.

# How to Act

## Drive
* Lead the process
* be open about issues

### NOTE
* What does it mean to be in charge? Often I feel like I'm in charge when I ask
most of the questions but do less of the talking. I feel like most people feel
like they're in charge if they talk the most.

### NOTE
if someone is asking a question more than once it's an indication that they
think you've missed something.

## Teamwork

# How to prepare

## Read about the design of major companies
* Think, don't memorize

## Know key concepts
* Tasks, sharding, caching
* Web Stack, Rest, etc.

## Practice back of the envelope calculations

### NOTE
* Think about what makes google searches scale issues different from other
search tasks.
* "Tiny or how many?" for how many servers do you tihnk you need.

### NOTE
* Design questions are fundamentally problem solving questions.

# Algorithm questions

## Why?
* Analytical skills
* How you think
* Make tradeoffs
* Push through hard problems
* Communication
* Strong CS fundamentals
* "Great solutions are more than just correct."
* "Passing test cases is merely the lowest bar for success."

## Essential Knowledge
Data Structures | Algorithsm | Concepts
ArrayLists      | merge sort           | Big O Time
Hash Tables     | Quick Sort           | Big O Space
Trees (+ tries) | Breadth-First Search | Recursion
Graphs          | Depths-First Search  | Memoization / Dynamic programming
Stacks / Queues | Binary Search        |
Heaps           |                      |

## Preparation
* Master Big O
* Implement DS / Algorithms
* Practice with interview questions
* Code on paper / Whiteboard
* Mock interviews
* Push yourself

# Solving Algorithms

## What is not expected
* To know the answers
* To solve immediately
* To code perfectly

## What Is Expected
* Be excited about hard problems
* Drive
    * Keep trying when stuck
    * More than just "correct"
* Pay attention to the interviewer
* Write real code
* Show me how you think

# How to approach

## Listen (for clues)
* "If I mention that the data is sorted then that often means the fastest
solution uses that information."

### NOTE
* This feels like it's puzzle solving.

## What's the clue?

### Anagram server
* `rates -> aster, star, taser, tears`
* The clue is that it's a server.
* Servers often mean that we can pre-compute values

## Drawn an example
### Is It Big Enough?
### Is it general purpose?
### Most people draw something like this

    [1, 12, 15, 19]
    [2, 12, 13, 20]

* This is tool small and misses cases.

### Do something like this

    [1, 12, 15, 19, 20, 21]
    [2, 12, 13, 20, 21, 25, 27]

* It's closer to big. Big really means bigger than your initial idea.
* It's more complex and has more cases.

## Brute Force / Naive
* Stupid and Terrible is ok

## Optimize
* "The optimization step is often the most important part of the interview. 
Often it's what really distinguishes an engineer."

## What's The Bottleneck?

* Ex: counting the intersection
    [1, 12, 15, 19, 20, 21]
    [2, 12, 13, 20, 21, 25, 27]

* "N^2 doesn't really have meaning here."
* You really need to think about sizes about all of your data structures.
Increasing the number of datastructures inreases the amount of operation
variables.
* One hack is not use the variable N since it often is over used in bad
contextst.

* So in this case the search time is O(len(list_1) * len(list_2))
* Make sure to decclare what your run time variables are.
* a = len(list_1)
* b = len(list_2)
* Having a two pointer walk on the list changes the run time to O(a + b)

## Second example
Ex: `a^3 + b^3 = c^3 + d^3 (a <= a, b, c, d <= 1000`

    n = 1000
    for a from 1 to n
        for b from 1 to n
            for c from 1 to n
                for d from 1 to n
                    if a^3 + b^3 == c^3 + d^3 
                        print a, b, c, d

* There's no reason to compute this, just solve the equation.

## Another way to opitmize
Ex: `a^3 + b^3 = c^3 + d^3 (a <= a, b, c, d <= 1000`

    for c from 1 to n
        for d from 1 to n
            result = c^3 + d^3 
            append(c, d) to list at value map[result]

    for each result in map

## Space / Time Tradeoffs

### Example One
Find rectangle at origin with biggest sum

    6  5  -9 2
    -2 -5 -2 7
    3  -2 10 13
    -8 -3 1  -2

* One solution is to go through all n * n rectangels for all values in the
matrix.
* "A lot of problems with ineffencient run times can be solved with Hash 
tables"

## Third Approach (Do it yourself)
### Find Permutations of s within b
* s = abbc
* b = babcabbacaabcbabcacbb
### NOTE
This is a really common problem on the web.
* One approach is to look one character at a time and to look at the next
three characters. Every time you find a character in s remove that character
from a copy of s. If s is empty by the time you're at the end of the three
characters than it's a permuatation.

## Recursion / Base Case & Build
* Subset of a set
* "If you ever catch yourself saying 'I need to back track' that generally
means this is a recursive problem."

## Solve 'incorrectly'
* Develop incorrect solution
* Think about it
* refactor until it's correct

## Random node in BST

                50
            20          60
        10      25          70
    5       15          65      80

* "If I state the words API it generally means I want to see how you think 
about designing an API."

* Try: flip a coin
This method is incorrect to produce something "random"

* Assumption that should be checked: random means that we want an equal 
distribution
* NOTE: Ask what random means.

* try: random number in [0, 1, 2}
R = 0 -> branch left
R = 1 -> branch right
R = 2 -> return node

* Try: return root with 1/n probably
* then flip coin (heads -> left, tails -> right)
* This algorithm assums that we can track the size of the tree and subtree.
* Problem: The coin flip still isn't weighted by subtree length

* Try: return roor with 1 / len(tree) probably
* flip weighted_flit(len(left_subtree), len(right_subtree))

## Other Data Structures

### Giving out Phone numbers
* I want any available number
* I want this number
* "A hash table seems like a good idea but it's a key: value lookup not a 
value: key lookup."

# Walk Through
* Keep the variables and when they change
* "A bit array is really just a more condense hash table."
* bit array == bit vector
* USE CASE: anytime you have a hash table of booleans you can use a bit array.

# Goal is writing Beautiful Code
* Write straight
* Top left corner
* Use arrows if needed
* Error cases / TODOs
* Good variable names
* Modularized
* Pick a good language for you
* "Recursive code in Python that pops off a character on a list"

# Testing

## First Analyze
* What's it doing? Why?
* Anything that looks weird?
* Error hot spots
* "In tree problem check left node right now, then right node left node."

## Then use test cases
* Small test cases
* Edge cases
* Bigger test cases. Personally I believe all cases should be small test cases.

## But 
* Test code, not algorithm
* think before you fix
* "If you just fix a bug without thinking about what caused the bug than often
you have just made your code more complex without solving the real issue."

# Questions For Your Interviewer
* Passion
* Knowledge
* Interest
* Communication
* Curiosity
## Specifics
* What's made you unhappy / happy
* What are your goals
* Culture & work style
* Career goals
* Technology

# Final Thoughts
## Interviewers Have A Reason
* Survey: Coming your way
* Ready? Follow up with your recruiter.
* 
