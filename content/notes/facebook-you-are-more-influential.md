---
title: You Are More Influential Than You Think You Are
date: 2013-05-23
categories:
  - facebook
  - social-networks
  - influence
  - analytics
  - network-effects
description: Jay Shah's post on Facebook's finding that ordinary users have larger social influence than they think — driven by the long tail of weak-tie connections that Facebook's social graph captured better than individuals' self-perception.
params:
  source: pinboard
  sourceUrl: http://jayshah.me/blog/facebook-anayltics-you-are-more-influential-than-you-think-you-are
---

![You Are More Influential Than You Think You Are](/images/notes/facebook-you-are-more-influential.png)

## Summary

Jay Shah's post discussed Facebook's internal analytics finding that typical users underestimate their social influence significantly. The mechanism: while most people think of their "real" social network as close friends and family (strong ties, dozens of people), their Facebook network includes hundreds or thousands of weak ties — former colleagues, acquaintances, distant relatives. Information spreads much more effectively through weak ties than through strong ones (Mark Granovetter's strength of weak ties hypothesis).

Facebook's social graph data made this empirically measurable at scale. When you share something, your close friends likely already know it (high overlap in information exposure among strong ties); your weak ties are the bridges to entirely different social clusters who haven't seen it. This makes the weak-tie network disproportionately important for information spread.

The practical implication for platform design: engagement features (Like, Share, Comment) and News Feed algorithms should surface content to weak ties, not just strengthen strong-tie bonds, to maximize information cascade reach. This insight influenced Facebook's ranking algorithms and the broader design of social feed systems.

## Key points

- Weak ties (acquaintances, former colleagues) are more valuable for information spread than strong ties (close friends)
- Granovetter's strength of weak ties (1973): weak ties bridge otherwise disconnected social clusters
- Facebook's social graph captures weak ties that people don't consciously maintain — making their network larger than their subjective perception
- Information cascades flow through weak-tie bridges — content shared only within strong-tie clusters stays local
- Implication for feed algorithms: surfacing content to weak ties accelerates diffusion beyond the original poster's inner circle
- Connects to viral coefficient calculations in growth engineering: each share's reach multiplies through weak-tie networks

[Original](http://jayshah.me/blog/facebook-anayltics-you-are-more-influential-than-you-think-you-are)
