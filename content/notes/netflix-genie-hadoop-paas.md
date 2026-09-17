---
title: "Netflix Genie: Hadoop Platform-as-a-Service"
date: 2013-06-29
categories:
  - netflix
  - hadoop
  - platform-as-a-service
  - open-source
  - distributed-systems
description: Netflix open-sourced Genie in mid-2013 — a REST-based Hadoop Platform-as-a-Service that abstracted job submission across multiple Hadoop clusters. A key piece of Netflix's data platform that became an influential pattern for multi-cluster job routing.
params:
  source: pinboard
  sourceUrl: http://jaxenter.com/netflix-unleash-genie-a-hadoop-platform-as-a-service-47623.html
---

## Summary

Netflix released Genie, their internal Hadoop job execution service, as open source in mid-2013. Genie solved a specific operational problem at Netflix's scale: they ran multiple Hadoop clusters (different versions, different configurations, different data sets), and data engineers needed a single interface to submit jobs without knowing which cluster to target or how to configure each one.

Genie exposed a REST API for job submission and managed the routing: you described what you wanted to run (a Hive query, a Pig script, a MapReduce job), Genie figured out which cluster had the data you needed, submitted the job, and returned a job ID for status polling. This abstraction layer made it possible for Netflix's hundreds of data engineers to run analytics without cluster-specific knowledge.

The architectural pattern — a job routing and execution layer sitting above multiple heterogeneous clusters — became influential. Netflix's data platform papers and open-source releases (Genie, Lipstick for Pig visualization, Aegisthus for Cassandra bulk export) defined what production-grade big data infrastructure looked like in 2013, before fully managed cloud services like AWS EMR and Databricks simplified the stack.

## Key points

- Genie REST API: submit Hive, Pig, or MapReduce jobs via HTTP — cluster routing handled transparently by Genie's metadata catalog.
- Multi-cluster support: Genie tracked which clusters had which datasets, routing jobs to the appropriate cluster based on the configuration tags.
- Netflix data platform pattern: multiple specialized clusters (different Hadoop versions, SLAs, data localities) fronted by a single API — later generalized as a federation pattern.
- Open-source release on GitHub allowed other companies to adopt the same pattern; inspired later projects like Apache Submarine.
- Part of Netflix's broader open-source data stack strategy in 2013: releasing internal tools to attract engineering talent and establish thought leadership.

[Original](http://jaxenter.com/netflix-unleash-genie-a-hadoop-platform-as-a-service-47623.html)
