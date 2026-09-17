---
title: The Dangers of Cargo Cult Data Science
date: 2013-04-02
categories:
  - data-science
  - methodology
  - statistics
  - critical-thinking
  - cargo-cult
description: Forbes piece on cargo cult data science — organizations adopting the trappings of data-driven decision-making (dashboards, models, data scientists) without the epistemological rigor that makes it actually work. A 2013 critique that remains current.
params:
  source: pinboard
  sourceUrl: http://www.forbes.com/sites/ciocentral/2013/04/01/the-dangers-of-cargo-cult-data-science/
---

## Summary

The cargo cult metaphor — from Richard Feynman's famous 1974 Caltech commencement address on cargo cult science — describes organizations that copy the surface rituals of data-driven decision-making without understanding the underlying epistemology. In 2013, as "big data" and "data science" became boardroom-level concepts, this failure mode was becoming common: companies hired data scientists, bought analytics platforms, and built dashboards, then drew conclusions from the data without applying the statistical rigor that would make those conclusions valid.

The specific failure modes: p-hacking (running many tests until one reaches p<0.05 without correcting for multiple comparisons), survivorship bias (building models on available data that systematically excludes cases where you don't have data), confusing correlation with causation in observational data, and using complex models (random forests, neural networks) without understanding whether the problem warranted complexity or whether the training data was representative.

The harder problem the piece likely identified: organizational cargo culting is almost invisible from inside. The data is real, the models run, the dashboards look authoritative. Bad data science often produces confident wrong answers rather than obvious errors. The antidote — rigorous experimental design, appropriate null hypotheses, honest uncertainty quantification — required a statistical culture that most organizations were far from having in 2013. The piece was early to name this failure mode as a predictable consequence of data science hype outpacing statistical literacy.

## Key points

- Cargo cult science (Feynman): mimicking the form of scientific practice without the epistemic rigor — producing the appearance of data-driven decisions, not the substance.
- P-hacking / multiple comparisons: running many tests without correction inflates false positive rates — a dashboard with 50 metrics will "find" patterns by chance.
- Survivorship bias: models trained on available data that systematically excludes failures produce optimistic, wrong predictions.
- Correlation vs. causation: observational data can't establish causation without careful experimental design or causal inference methods.
- The org dynamics: buying tools and titles doesn't create statistical culture — the rigor has to be embedded in how questions are asked and answered.

[Original](http://www.forbes.com/sites/ciocentral/2013/04/01/the-dangers-of-cargo-cult-data-science/)
