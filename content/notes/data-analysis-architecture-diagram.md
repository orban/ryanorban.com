---
title: Data Analysis Architecture Workflow Diagram
date: 2013-12-06
categories:
  - data-science
  - architecture
  - big-data
  - workflow
  - visualization
description: VentureBeat/DataBeat data analysis architecture diagram circulated on Twitter in 2013 — a workflow schematic showing the layers of a big data pipeline from collection through analysis to visualization. Snapshot of how practitioners were thinking about data infrastructure.
params:
  source: pinboard
  sourceUrl: https://twitter.com/sekhardrona/status/408678191927017472/photo/1
---

## Summary

This VentureBeat data analysis architecture diagram (shared via DataBeat and DataScience Twitter during the 2013 big data discourse) illustrated the layered pipeline model for enterprise data analysis: raw data collection → storage (Hadoop/data warehouse) → processing/ETL → analytics → visualization/reporting.

These pipeline diagrams were common in 2013 as organizations tried to communicate the components of a big data stack to non-technical stakeholders. The era's dominant framework: ingest from diverse sources → land in HDFS or a data warehouse → transform with MapReduce or SQL → model/analyze → visualize in a BI tool. The full stack was often called a "Lambda architecture" (hot path + cold path) after Nathan Marz's 2012 design.

The diagram type is itself an artifact of 2013 data science discourse: when "big data" was being sold as a capability requiring architectural investment, these schematics appeared constantly in conference decks and vendor materials.

## Key points

- Classic big data pipeline architecture: collection → storage → processing → analytics → visualization.
- Lambda architecture was the dominant design pattern: batch (cold) path + stream (hot) path feeding a serving layer.
- Stack components: Hadoop/HDFS for storage, MapReduce or Hive for processing, R/Python for modeling.
- These diagrams were a primary communication vehicle in 2013 for selling "big data" architectures to business stakeholders.
- VentureBeat's DataBeat conferences were a nexus of big data vendor discourse in 2013.

[Original](https://twitter.com/sekhardrona/status/408678191927017472/photo/1)
