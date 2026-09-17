---
title: The Three Cultures of Machine Learning
date: 2016-01-22
categories:
  - machine-learning
  - statistics
  - philosophy
  - paradigms
  - research
description: Jason Eisner's JHU tutorial describing three distinct cultures within machine learning — the statistical/probabilistic, the algorithmic/computational, and the geometric/optimization traditions. Useful framing for understanding why ML researchers sometimes talk past each other.
params:
  source: pinboard
  sourceUrl: http://cs.jhu.edu/~jason/tutorials/ml-simplex.html
---

## Summary

Jason Eisner at Johns Hopkins University describes machine learning not as a unified field but as three distinct intellectual cultures that share methods while disagreeing about what counts as understanding. The framing helps explain why ML researchers often talk past each other, why papers in different sub-communities are hard to compare, and why practitioners trained in one tradition often find the others alien.

The three cultures roughly map to: (1) the **statistical/probabilistic** tradition — descended from Bayesian statistics and probabilistic modeling, focused on uncertainty quantification and generative models; (2) the **algorithmic/computational** tradition — focused on sample complexity, PAC learning, and worst-case guarantees, descended from theoretical computer science; and (3) the **geometric/optimization** tradition — focused on loss landscapes, gradients, and representation, which now dominates deep learning practice.

Each culture has different journals, different success criteria, and different notions of elegance. A probabilistic modeler cares about whether the model reflects the true generative process. A computationalist cares about sample complexity bounds. An optimizationalist cares about whether the loss converges. The same algorithm can be simultaneously praised and dismissed depending on which lens is applied. Understanding this helps practitioners read cross-community literature and understand why deep learning has been more readily adopted by some traditions than others.

## Key points

- Three ML cultures: probabilistic (Bayes), computational theory (PAC/complexity), geometric (optimization/gradients).
- Each has distinct journals, success criteria, and criteria for understanding.
- Deep learning's success has most benefited the optimization tradition; has strained the probabilistic/theoretical traditions.
- The simplex visualization maps research problems by which culture's methods dominate.
- Helps explain why cross-community communication in ML research is often difficult.

[Original](http://cs.jhu.edu/~jason/tutorials/ml-simplex.html)
