---
title: "Setosa.io: Conditional Probability Visualizer"
date: 2014-02-17
categories:
  - probability
  - statistics
  - data-visualization
  - education
  - interactive
description: Victor Powell's interactive visual explanation of conditional probability — part of the setosa.io series that made abstract statistical concepts tangible through browser-based animation. One of the best examples of explanatory visualization for statistics education.
params:
  source: pinboard
  sourceUrl: http://setosa.io/conditional/
---

## Summary

Victor Powell's setosa.io built a series of interactive browser-based visualizations for statistical and mathematical concepts that were notoriously hard to build intuition for through static text. The conditional probability visualization shows Bayes' theorem and conditional probability as animated diagrams — moving dots that split and re-sort based on the conditioning event.

The visualization approach directly addresses the most common confusion about conditional probability: the asymmetry of P(A|B) vs P(B|A). The base rate fallacy — treating P(test positive | disease) as the same as P(disease | test positive) — is visually obvious when you watch the population split. The classic medical test example (high test accuracy + low disease prevalence = low positive predictive value) becomes immediately intuitive through the animation.

Setosa.io was part of a movement in 2013-2014 to use D3.js (then newly released by Mike Bostock at the New York Times) for explanatory statistics. Other notable entries in this genre: Seeing Theory (Brown University), Bret Victor's "Explorable Explanations" manifesto, and Immersive Math. The common thread: static textbooks and even static data visualization can't communicate dynamics and relationships as well as animation with sliders.

## Key points

- Conditional probability P(A|B): probability of A given B has occurred — the order matters and the asymmetry is non-obvious without visual grounding.
- Base rate fallacy: P(positive test | disease) ≈ 99% does not imply P(disease | positive test) ≈ 99% — base rate of disease in the population determines predictive value.
- Bayes' theorem visualized: the population-splitting metaphor — start with everyone, filter by condition, compute ratio within the filtered group.
- D3.js as the tool: data-driven SVG manipulation in the browser enabled this class of interactive statistical explanation.
- Connection to Bayesian inference: conditional probability is the mechanics; the posterior is P(hypothesis | data) computed via the same machinery.

[Original](http://setosa.io/conditional/)
