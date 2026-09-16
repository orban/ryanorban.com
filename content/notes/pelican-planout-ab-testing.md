---
title: "Pelican + PlanOut: A/B Testing on a Static Site"
date: 2014-05-27
categories:
  - ab-testing
  - experimentation
  - pelican
  - planout
  - python
description: Trent Hauck's post combining Facebook's PlanOut experiment framework with the Pelican static site generator — a creative integration showing how to run A/B tests on a static site without server-side logic. An early example of bringing rigorous experimentation tooling to lightweight web stacks.
params:
  source: pinboard
  sourceUrl: http://blog.trenthauck.com/posts/pelican-plus-planout/
---

## Summary

Trent Hauck's post demonstrates how to integrate PlanOut — Facebook's experiment framework — with Pelican, a Python-based static site generator. The combination is technically interesting: static sites don't have server-side request handling, so running A/B tests normally requires either a CDN with edge logic or client-side assignment. This post works around the limitation by having PlanOut generate the variant assignments at build time.

PlanOut was open-sourced by Facebook in 2014 as part of their experimentation infrastructure. Unlike simple A/B test tools, PlanOut is a domain-specific language for defining experiments — you describe which parameters to randomize, over which units (users, sessions, pages), and PlanOut handles the consistent assignment and logging. The Haskell-inspired syntax makes experiment definitions readable and auditable.

The Pelican integration is a specific hack for a specific use case, but the post represents a broader 2014 trend: taking tools built at scale by large tech companies (PlanOut at Facebook, Hadoop at Yahoo) and figuring out how to run them on smaller stacks. PlanOut was designed for Facebook-scale traffic; this post makes it work for a personal blog.

## Key points

- PlanOut separates experiment definition (which parameters to randomize) from assignment logic and logging — more rigorous than simple random splits.
- Pelican is a Python static site generator; the integration generates multiple site variants at build time, avoiding runtime randomization.
- Client-side experiment assignment (after page load) is the standard alternative for static sites — Optimizely and VWO built businesses on this model.
- Facebook's open-sourcing of PlanOut reflected the 2014 trend: tech companies sharing internal tooling to attract engineers and establish standards.
- The reproducibility of experiment assignments (given the same user/session ID, PlanOut always returns the same variant) is critical for consistent user experience.

[Original](http://blog.trenthauck.com/posts/pelican-plus-planout/)
