# HTTP/2 (Davey Shafic)
* Prompt (google serach term)

# What Is it?
* RFC 7540
* RFC 7541
* Created by IETF working group (Chaired by mark naughtingham)
* http/0.9 -> http/1.0 -> http/1.1 -> SPDY -> http/2.0

# Browser support
* Currently 60% of browsers support http/2.0

# Binary instead of text
* "Significant since you can't issue a request via telnet."
* Fully multiplexed which means you can use one connection for all requests.
* Uses header compressions.
* And includes server push.

# So What's The Point?
* "Http/1.x sucks", "To get around the problems with http/1.x we've built a
bunch of tools to make it suck less."
* One connection for parallel requests removes the need for most of those hacks.

# pycurl

    pycurl.curlmulti()

# ALPN (google term)

# H2C upgrade negotiations

# All browsers require TLS for http/2

# Still making subrequests

# Stream dependencies
* We can say sthat stream A depends on B. Don't send A until B has been recieved.
* Every message is comprised of frames that can be interleaved. They're headers
for each stream.

# HPACK

# http://daveyshafik.com/slides

# Questions
## What control does the client have?
* "The client is 100% in control of what it accepts but not what is pushed."
* "Curl adds pushes to the multirequests."

## Does javascript have multi-accept yet?
* "No"

## "Why doesn't minimization not matter?"
* "The difference between gzip and multiplex and gzip, multiplex, minimization is about 1%."

