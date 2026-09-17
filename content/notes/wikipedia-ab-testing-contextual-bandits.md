---
title: Why Wikipedia's A/B Testing Is All Wrong (And How Contextual Bandits Can Fix It)
date: 2014-01-20
categories:
  - bandits
  - a-b-testing
  - experimentation
  - contextual-bandits
  - personalization
description: Synference blog post critiquing Wikipedia's A/B testing approach — argues that testing average effects ignores user heterogeneity, and contextual bandits could deliver personalized treatments rather than one-size-fits-all decisions.
params:
  source: pinboard
  sourceUrl: http://synference.blogspot.com/2014/01/why-wikipedias-highly-successful-ab.html
---

## Summary

This Synference blog post critiques the standard A/B testing approach used by Wikipedia and most large platforms. The core argument: measuring average treatment effects assumes users are homogeneous. In reality, the same feature might help experienced editors and harm new ones, or perform differently across geographies and browser contexts. A/B tests that compare population averages can declare a winner that makes some segments worse off.

Contextual bandits are the proposed solution. Unlike standard multi-armed bandit algorithms that pick one arm for everyone, contextual bandits condition the arm selection on observable features of the user or context. The result is personalized treatment — different users get different variants — and the algorithm learns which contexts match which treatments.

## Key points

- Standard A/B testing measures average effects over the whole population — the winning variant is an average that may be suboptimal for many individuals
- User heterogeneity is the core problem: a feature that improves conversion for power users may degrade it for new users, but a naive A/B test averages over both
- Contextual bandits use observable context (device, user history, geography, time of day) to select the arm, learning a policy rather than a single winner
- Wikipedia editing interfaces are a good case study: experienced editors and new contributors have very different needs, and the same UI change can hurt one group while helping the other
- The statistical analysis of contextual bandit experiments is harder — requires off-policy evaluation techniques to estimate what would have happened under different policies

[Original](http://synference.blogspot.com/2014/01/why-wikipedias-highly-successful-ab.html)
