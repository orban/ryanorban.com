---
title: What I Wish I Knew About Data For Startups
date: 2016-08-11
categories:
  - data-science
  - startups
  - data-infrastructure
  - career
  - practical
description: Jean-Nicholas Hould's hard-won lessons about building data capabilities at startups — prioritizing tracking over models, avoiding premature data infrastructure, and why startups fail at data for different reasons than large companies.
params:
  source: pinboard
  sourceUrl: http://www.jeannicholashould.com/what-I-wish-I-knew-about-data-for-startups.html
---

![What I Wish I Knew About Data For Startups](/images/notes/data-for-startups.png)

## Summary

Jean-Nicholas Hould distills lessons from working with startup data teams — specifically what advice he'd give to a technical founder or early data hire who wants to build something useful and not waste time on the wrong things.

The core argument is about sequencing. Startups frequently make two mistakes in opposite directions: either they collect no data at all (building blind) or they invest in expensive data infrastructure before they have product-market fit (building the wrong thing at scale). The right order is rigorous event tracking first (every user action logged), then analytical capability (being able to query what happened), and only then machine learning models (which require both historical data and a stable enough product that the model doesn't become immediately stale). A startup that tries to build a recommendation engine before it has stable event logs is building on sand.

Hould's other key point is on communication: the data team at a startup is often a bottleneck not because of technical limitations but because they fail to translate findings into decisions. A beautiful analysis that sits unread in a notebook has zero impact. This connects to the communication > algorithms theme in David Robinson's Stack Overflow retrospective. Both writers are arguing that data scientists at companies need to develop judgment about which questions to answer and how to present answers — skills that are largely absent from ML curricula.

## Key points

- Sequence matters: tracking → analytics → ML. Don't build models before you have reliable event data.
- Event tracking is the highest-leverage early investment — it enables everything else and is cheap to set up compared to recovery from not having it.
- Premature data infrastructure (Hadoop, Spark, complex pipelines) before product-market fit is a common startup waste of time.
- Communication is the bottleneck more often than technical SKILL — analyses that don't reach decisions don't matter.
- Written in 2016 by Jean-Nicholas Hould — same author as the R-squared and Central Limit Theorem posts, part of a series on practical statistical thinking.

[Original](http://www.jeannicholashould.com/what-I-wish-I-knew-about-data-for-startups.html)
