---
title: Cookiecutter Data Science Template
date: 2021-12-20
categories:
  - data-science
  - mlops
  - project-structure
  - python
  - tools
description: Cookiecutter Data Science is a standardized, opinionated project template for data science work in Python — a sensible starting folder structure that makes projects reproducible and shareable. The de facto standard for organizing Python data science projects.
params:
  source: pinboard
  sourceUrl: https://drivendata.github.io/cookiecutter-data-science/
---

![Cookiecutter Data Science Template](/images/notes/cookiecutter-data-science.png)

## Summary

[Cookiecutter Data Science](/notes/cookiecutter-data-science/) is an opinionated project template maintained by DrivenData that provides a standardized folder structure for Python data science projects. Running `cookiecutter https://github.com/drivendata/cookiecutter-data-science` generates a project skeleton with sensible defaults: separate directories for raw data (immutable), processed data, notebooks, source code, models, reports, and references.

The philosophy behind the template: data science projects have a reproducibility crisis partly because every project is organized differently. If you return to a project after 6 months (or someone else opens it), the structure should immediately communicate where data lives, how it was processed, what's source code vs. exploratory notebook vs. final analysis. [Cookiecutter Data Science](/notes/cookiecutter-data-science/) enforces this structure by convention.

Key opinionated decisions: notebooks go in `notebooks/` and are for exploration only — production code lives in `src/`; data is treated as immutable (raw data is never modified); Makefile targets document the pipeline steps; references and papers go in `references/`; figures go in `reports/figures/`. The template integrates with conda or pip virtual environments and encourages DVC (Data Version Control) for larger datasets.

By 2021, this template had become something close to a community standard — I used Cookiecutter was shorthand for "the project is organized sensibly. It solved the where does this file go" decision fatigue that slows down early project setup.

## Key points

- Standardized directory structure: `data/raw/` (immutable), `src/` (source code), `notebooks/` (exploration only), `models/`, `reports/`
- Makefile-documented pipeline: `make data`, `make features`, `make train` — reproducible build steps
- Philosophy: raw data is sacred — never modify it; all transformations are code in `src/`
- Integrates with conda, pip, optionally DVC for large dataset versioning
- Community standard: using Cookiecutter signals organized, reproducible project structure to collaborators

[Original](https://drivendata.github.io/cookiecutter-data-science/) → GitHub
