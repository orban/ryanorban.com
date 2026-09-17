---
title: "Production Code for Data Science: Our Experience with Kedro"
date: 2022-01-23
categories:
  - kedro
  - data-science
  - mlops
  - production
  - python
  - engineering
description: Beamery's engineering team shares their experience using Kedro to bring software engineering discipline to data science code in production — covering what worked, what required adaptation, and how the pipeline structure changed their team's workflows.
params:
  source: pinboard
  sourceUrl: https://medium.com/hacking-talent/production-code-for-data-science-and-our-experience-with-kedro-60bb69934d1f
---

## Summary

This post from Beamery's engineering blog (Hacking Talent) shares a practitioner's experience using Kedro to write production-grade data science code — one of the better accounts of what adopting a data pipeline framework actually feels like from the inside, rather than what it promises.

The core problem Beamery faced is common in ML teams: data science code starts in Jupyter notebooks, gets promoted to scripts, and accumulates into a codebase that nobody fully understands, that can't be reliably reproduced, and that new team members struggle to extend. Kedro addresses this by imposing structure: pipelines are explicit DAGs of functions, data flows through a typed catalog, and project layout is standardized.

The honest assessment of what Kedro actually changes: it's excellent at enforcing reproducibility and making data flows visible, but the up-front investment in catalog configuration is real, and teams coming from notebook-heavy workflows need time to adjust to the function-oriented pipeline model. The post is valuable precisely because it goes beyond the framework's own documentation to describe the friction of adoption alongside the payoffs.

## Key points

- Real adoption story: Kedro solved notebook-to-production reproducibility problems but required meaningful investment in catalog configuration and workflow change.
- Data Catalog makes data dependencies explicit — solves the "where does this data come from?" archaeology problem.
- DAG-based pipelines make execution order and dependencies visible — eliminates hidden state between notebook cells.
- Team adoption friction: data scientists coming from notebooks need time to adjust to the function/pipeline model.
- Validates the core Kedro value proposition for ML teams: reproducibility and modularity at the cost of initial configuration investment.

[Original](https://medium.com/hacking-talent/production-code-for-data-science-and-our-experience-with-kedro-60bb69934d1f)
