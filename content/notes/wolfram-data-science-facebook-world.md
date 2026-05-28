---
title: Data Science of the Facebook World
date: 2013-04-24
categories:
  - data-science
  - social-networks
  - facebook
  - network-analysis
  - wolfram
description: Stephen Wolfram's data science analysis of Facebook social graph patterns — age cohort differences in network structure, relationship status effects, and how Wolfram Language's data computation tools enable individual-level analysis of social network data. A 2013 example of using data for personal-scale social science.
params:
  source: pinboard
  sourceUrl: http://blog.stephenwolfram.com/2013/04/data-science-of-the-facebook-world/
---

![Data Science of the Facebook World](/images/notes/wolfram-data-science-facebook-world.png)

## Summary

Stephen Wolfram used personal Facebook data collected via a Wolfram Alpha personal analytics tool to perform network analysis of social graph structure across thousands of users. The post is both a demonstration of Wolfram Language's data analysis capabilities and a substantive exploration of how social network topology varies by age, relationship status, and career stage.

Key findings: young users (teens) have a single dense cluster — everyone knows everyone else from school. As people age through college, the network splits into distinct clusters (hometown friends, college friends, new city). Professional-age users show the most fragmented structure, with multiple tight clusters corresponding to different life phases that barely connect. This reflects the sociology of social capital — Robert Putnam's distinction between bridging capital (weak ties across groups) and bonding capital (strong ties within groups). Facebook social graphs skew heavily toward bonding capital.

The analysis also showed relationship status effects on network structure: coupled users show tighter, more merged friend networks over time. Career effects were visible too: people who changed jobs multiple times have more fragmented graphs than those who stayed in one place. The post used Wolfram Mathematica's graph visualization and Alpha personal analytics, making it an early example of personal data science — using your own data for sociological self-analysis.

## Key points

- Facebook social graphs change structure predictably with age: dense monoculture (teens) → multi-cluster (college) → fragmented-but-connected (adult professional)
- Network clustering coefficient drops over time as bridge nodes (people who connect clusters) become more important
- Weak ties (Granovetter) are underrepresented in Facebook data vs. LinkedIn — Facebook captures bonding capital, LinkedIn bridges it
- Wolfram Language notebook-style analysis previewed the kind of computational essays that Observable and Jupyter later popularized
- Personal data analytics at scale: the post implicitly argued that individuals should be analyzing their own behavioral data, not just companies
- Notable early example of graph visualization and network science applied to social media at scale

[Original](http://blog.stephenwolfram.com/2013/04/data-science-of-the-facebook-world/)
