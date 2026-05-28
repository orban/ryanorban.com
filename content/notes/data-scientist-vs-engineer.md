---
title: "Keys to Understanding: Data Scientist vs. Data Engineer"
date: 2015-11-11
categories:
  - data-science
  - data-engineering
  - hiring
  - team-building
  - career
description: Domino Data Lab slides on knowing when to hire a data scientist versus a data engineer — clarifying the distinct skills, responsibilities, and organizational needs each role fills. From the Data Popup Seattle conference, when this distinction was still being established.
params:
  source: pinboard
  sourceUrl: http://www.slideshare.net/dominodatalab/data-science-popup-seattle-keys-to-understanding-when-you-are-looking-for-a-data-scientist-vs-engineer-and-when-and-how-to-utilize-a-recruitment-firm
---

![Keys to Understanding: Data Scientist vs. Data Engineer](/images/notes/data-scientist-vs-engineer.png)

## Summary

These Domino Data Lab slides from Data Popup Seattle address a question that was causing real hiring confusion in 2015: what is the difference between a data scientist and a data engineer, and when do you need which? The distinction matters because mismatched hires are expensive — bringing in a PhD statistician who spends 90% of their time building ETL pipelines is a waste of a specialized SKILL set.

The data scientist role as conceived in 2015 covered: statistical modeling, machine learning algorithm selection and training, exploratory analysis, communicating insights to stakeholders. The data engineer role covered: building and maintaining data pipelines, designing data warehouse schemas, ensuring data quality and accessibility, instrumentation. The Venn diagram had some overlap (both need SQL, both need to understand data at scale) but the primary value-add of each is quite different.

A key point the slides made: most companies need a data engineer before they need a data scientist. You can't build models on top of unreliable, incomplete, or inaccessible data. The data scientist hype of 2012–2015 drove companies to hire modelers into data-desert environments, then wonder why they weren't getting results. The slides also cover when to use a recruitment firm versus direct hire for each role — suggesting the talent market was hot enough that specialized recruitment had become relevant.

## Key points

- Data scientist: modeling, statistical inference, analysis, stakeholder communication.
- Data engineer: pipelines, ETL, data warehouse design, data quality, instrumentation.
- Common mistake: hiring a data scientist before the data infrastructure exists to support modeling.
- Overlap exists (SQL, data scale) but primary value-add is distinct — don't hire one expecting the other.
- Context: 2015, when "data scientist" was still being defined and many companies conflated the roles.

[Original](http://www.slideshare.net/dominodatalab/data-science-popup-seattle-keys-to-understanding-when-you-are-looking-for-a-data-scientist-vs-engineer-and-when-and-how-to-utilize-a-recruitment-firm)
