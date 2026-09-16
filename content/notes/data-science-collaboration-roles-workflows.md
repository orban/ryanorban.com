---
title: How Do Data Science Workers Collaborate? Roles, Workflows, and Tools
date: 2022-03-08
categories:
  - data-science
  - collaboration
  - hci
  - teams
  - research
description: ACM survey of how data science workers actually collaborate in practice — finding distinct roles (data engineers, ML engineers, domain scientists, communicators) that rarely map to job titles, with coordination breakdowns at handoff points between roles. One of the few empirical studies of real data science team dynamics rather than idealized workflow diagrams.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Data_Science_Collab.pdf
---

## Summary

Amy X. Zhang (UW/MIT), Michael Muller (IBM Research), and Dakuo Wang (IBM Research/MIT-IBM Watson AI Lab) conducted an online survey of 183 data science workers to understand how data science teams actually collaborate — as opposed to how textbooks describe the data science workflow. The distinction matters because most data science tooling and process design assumes a single practitioner, but most commercial data science work is team-based.

Key findings: real data science teams contain multiple distinct roles that don't map cleanly to job titles — there are people who primarily wrangle data, people who build models, domain experts who interpret results, and communicators who translate findings for business stakeholders. These roles are often performed by different people who may not have direct communication channels. The result is coordination failures at handoff points: a data engineer produces a cleaned dataset that a modeler then has to re-understand from scratch, losing context about data quality decisions.

The study also surfaced challenges with notebook-based workflows (e.g., Jupyter notebooks): notebooks are well-suited to individual exploration but create sharing and versioning problems for teams. Version control is rarely used for notebooks, leading to brittle, hard-to-reproduce pipelines. Tools for data science collaboration in 2020 were underdeveloped relative to software engineering tooling — the paper was published at a time when platforms like MLflow and DVC were emerging to address these gaps.

## Key points

- Real data science teams have 4-5 distinct role types that rarely align with formal job titles
- Coordination breaks down at handoff points between roles — context about data quality decisions gets lost
- Jupyter notebooks are great for individual exploration but problematic for team collaboration and reproducibility
- Version control adoption in data science was low in 2020 — a gap that MLflow, DVC, and Weights & Biases address
- Domain knowledge from subject-matter experts often isn't formalized — creating invisible dependencies
- Survey-based: 183 respondents, self-reported — findings are directional rather than causal

[Original (arXiv 2001.06684)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Data_Science_Collab.pdf)
