# Computational Statistics (Allen Downey)
* A surprising number of studies that are re-runs of prior studies are finding that
the previous study isn't reproducable.
* This tutorial is on why that is the case and how to help you get better statistics.

# Big Questions
* How big is the effect?

Effectict size: usually a single number, ideally comparable across studies. This
is usually the most important part of the question.

* How sure are we about that effect?

Confidence interval and / or standard error: quantifies the precision of the estimate
Second most important part. Distant second.

* Is it possible that we're being fooled by chance?

p-value: Indicates whether the apparent effect might be due to chance. This is
not completely useless according to Allen. =P

# The Problem with p-value
Don't care about the p-value until you have seen that the effect size is large
enough to care about.

# BIG TAKE AWAY
When reading a white paper that's not a tech paper look at the effect size
first

* Big or small really depends on the context. 

# Ways To measure affect size
* Difference in means.
* Difference in 

# Imagining A room full of people to make a percentage ratio concrete.
So children developing peanut allergy.

    "Administering peanuts decreases allergy rates by 83%" vs
    "avoiding peanuts increases allergy rates by 467%"

# Odds ratio (most common in medical journels)

The problem is that the ratios aren't symmetric in most cases.

"eating peanuts decreases allergy rates (OR=0.15)"

vs

"Avoiding peanuts increases allergy rates (OR=6.6)"

#Log odds ratio's

In many ways, LOR is the best way to work with probability and changes in probablity.

And it's comparable between studies.

Buuuuuut It's unfamiliar to most people.

# Summary

Treatment             | difference in rate | percent change | Odds ratio | log odds ratio
administering peanuts | -14 points         | -83%           | 0.15       | -0.82
Not administering     | +14 points         | +467%          | 6.6        | +0.82

# Over sampling
Oversampling people in red shirts may not be a problem. But over sampling young
people most likely does affect your study on human weight.

Sampling bias: hard to quantify.

Measuring error: Sometimes quantifiable.

Random error: relatively easy to quantify.

# Sampling distribution of sampling mean
The standard deviation of the sampling distrbution of sampling means is the
standard error. So the standard error is the STD of a set of sampling means
from the total data population.

# ipywidgets
jupyter nbextension enable --py widgetsnbextension

# Summary
* Use the sample to moddel the population
* Use the model to generate new samples.
* Compute the sampling distribution of whatever statistic you want.
* report SE or CL, or both (but be clear about which it is).
