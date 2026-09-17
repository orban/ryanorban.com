---
title: Insight Data Engineering Ecosystem Map
date: 2017-06-27
categories:
  - data-engineering
  - infrastructure
  - big-data
  - tools
  - ecosystem
description: Insight Data Science's map of the data engineering ecosystem circa 2017 — a diagram organizing dozens of tools by pipeline stage (ingest, store, process, visualize). A widely shared snapshot of the Hadoop/Spark era's explosion of competing infrastructure tools.
params:
  source: pinboard
  sourceUrl: http://xyz.insightdataengineering.com/blog/pipeline_map/
---

## Summary

Insight Data Science created this visual map of the data engineering ecosystem, organized by pipeline stage, during a period (2016-2017) when the number of open-source and commercial data tools had exploded to the point that practitioners needed a map just to understand the landscape. The diagram arranged tools along a flow from data ingestion to storage to processing to querying to visualization, showing where each tool fit.

The tools on the 2017 map reflect the Hadoop ecosystem's maturity and the transition toward real-time streaming. Ingestion layer: Kafka, Flume, Sqoop, Kinesis. Storage: HDFS, S3, HBase, Cassandra, Elasticsearch. Batch processing: Spark, MapReduce, Hive, Pig. Stream processing: Storm, Flink, Samza, Spark Streaming. Visualization: Tableau, Kibana, Superset. The sheer density of the map illustrated a real problem: the data engineering field had more tools than any individual engineer could evaluate, and the "right" stack depended heavily on scale, team size, and latency requirements.

Insight Data Science ran fellowship programs training data scientists and data engineers, and this map was both a teaching resource and a widely shared industry artifact — printed on office walls at data-heavy companies, referenced in blog posts and conference talks. By 2020, the landscape had shifted significantly: managed cloud services (AWS Glue, BigQuery, Databricks) had absorbed much of the open-source stack, and the map needed substantial revision. The 2017 version is now mainly useful as a historical document of what modern data engineering meant at the height of the Hadoop era.

## Key points

- Visual taxonomy of data pipeline tools organized by stage: ingest → store → process → query → visualize.
- Captured the 2017 Hadoop ecosystem at peak complexity — dozens of competing open-source tools for each pipeline stage.
- Insight Data Science fellowship used it as a teaching resource; became an industry reference for team onboarding.
- By 2020, managed cloud services (BigQuery, Databricks, AWS Glue) consolidated much of the open-source tool proliferation.
- Historical artifact: shows what a [modern data stack](/notes/modern-data-stack/) meant before dbt, Airflow, and cloud data warehouses became dominant.

[Original](http://xyz.insightdataengineering.com/blog/pipeline_map/)
