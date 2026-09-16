---
title: "Data is Ugly: Tales of Data Cleaning"
date: 2015-08-07
categories:
  - data-cleaning
  - data-science
  - engineering
  - collaboration
  - galvanize
description: Ryan Orban's KDnuggets piece on data cleaning — arguing that teaching data scientists and engineers to understand each other's work is more important than any technical fix. The piece reframes data quality as an organizational problem, not just a technical one.
params:
  source: pinboard
  sourceUrl: http://www.kdnuggets.com/2015/08/data-ugly-tales-data-cleaning.html
---

## Summary

This KDnuggets article (saved via a tweet crediting Ryan Orban from Zipfian Academy) addresses one of the most consistently underestimated parts of data science: cleaning. The piece frames data cleaning not just as a technical chore but as a symptom of organizational gaps between data scientists and software engineers — teams that need each other but often operate in silos.

The core argument is that data quality problems are as much about communication and workflow as they are about tool choice. When data engineers and data scientists don't understand each other's work, they build pipelines that look clean at handoff but create silent problems downstream: unexpected nulls, schema drift, encoding mismatches, inconsistent categorical values. Better tooling helps, but it doesn't substitute for data scientists who understand how data is produced and engineers who understand how it will be consumed.

The practical strategies: smarter data collection at the source (investing in logging design upfront), industry-specific custom tooling (no single cleaning solution fits all domains), and building reproducible workflows that allow results to be verified against new data. The statistical thinking dimension — recognizing when a result is suspicious and investigating rather than accepting it — is treated as foundational, not optional.

## Key points

- Data cleaning is an organizational problem, not just a technical one — cross-functional understanding matters more than tools.
- Data engineers and data scientists need baseline fluency in each other's domains to build reliable pipelines.
- Invest in logging and data collection design upfront — reactive cleaning is far more expensive than proactive schema design.
- Reproducible cleaning workflows (scripts, not manual fixes) allow verification on new data.
- Apply judgment: when results look wrong, investigate. "It's not enough to be good at statistics, you need to use your brain."
- Reflects the Galvanize/Zipfian Academy pedagogy of 2015: practical DS skills include understanding production systems.

[Original](http://www.kdnuggets.com/2015/08/data-ugly-tales-data-cleaning.html)
