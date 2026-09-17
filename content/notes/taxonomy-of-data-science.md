---
title: A Taxonomy of Data Science
date: 2013-05-25
categories:
  - data-science
  - taxonomy
  - career
  - skills
description: "Hilary Mason and Chris Wiggins' 2010 taxonomy of data science roles and skills, organized around the OSEMN framework: Obtain, Scrub, Explore, Model, iNterpret. One of the earliest attempts to define what data science actually comprises as a discipline."
params:
  source: pinboard
  sourceUrl: http://www.dataists.com/2010/09/a-taxonomy-of-data-science/
---

![A Taxonomy of Data Science](/images/notes/taxonomy-of-data-science.png)

## Summary

Hilary Mason and Chris Wiggins published this taxonomy in 2010 as one of the first serious attempts to define what data science actually comprises — at a time when the term was still contested and people were arguing about whether it was meaningfully different from statistics or machine learning. Their framework: OSEMN (pronounced awesome) — Obtain, Scrub, Explore, Model, iNterpret.

The OSEMN framework was important because it made explicit that most real-world data science time is spent *not* building models. Obtain (scraping, API calls, database dumps) and Scrub (cleaning, normalization, joining) together typically consume 60-80% of a data scientist's time. The Explore phase (visualization, summary statistics, distribution checks) is where intuition develops. Model is the part that gets the headlines. Interpret — translating model outputs into business decisions — is the hardest and most underappreciated.

This framing cut against the academic machine learning view that data science was primarily model selection and optimization. It also pre-figured the eventual data engineering split: as organizations matured, the Obtain and Scrub work got handed off to dedicated engineers, leaving data scientists to focus on Explore, Model, and Interpret.

## Key points

- **OSEMN**: Obtain → Scrub → Explore → Model → iNterpret — the full data science lifecycle
- Obtain: APIs, scraping, databases, public datasets — getting data into a usable state
- Scrub: missing value imputation, deduplication, normalization, schema alignment — the unglamorous majority of the work
- Explore: exploratory data analysis (EDA), visualization, distributional checks — where hypotheses form
- Model: statistical inference, machine learning, regression — what everyone focuses on, but not the bottleneck
- Interpret: communicating findings to stakeholders, translating model outputs to decisions — hardest to scale
- Hilary Mason later founded Fast Forward Labs (now Cloudera Fast Forward); Chris Wiggins is Chief Data Scientist at The New York Times

[Original](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/)
