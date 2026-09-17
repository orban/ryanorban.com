---
title: Spark, Storm and Real-Time Analytics
date: 2014-02-06
categories:
  - apache-spark
  - apache-storm
  - real-time
  - streaming
  - big-data
description: An early comparison of Apache Storm and Spark Streaming for real-time analytics — covering their different processing models, latency characteristics, and use cases. A snapshot of the stream processing options available before Kafka Streams, Flink, and other tools matured.
params:
  source: pinboard
  sourceUrl: http://www.slideshare.net/ptgoetz/apache-storm-vs-spark-streaming
---

## Summary

By early 2014, real-time stream processing had two major open-source contenders: Apache Storm (created by Nathan Marz at BackType, acquired by Twitter) and Apache Spark Streaming (the streaming extension of the broader Spark framework). This comparison captures the moment when practitioners had to choose between the two for streaming analytics workloads.

Apache Storm processed events one at a time as they arrived — true micro-second latency streaming. Its processing model used topologies: directed acyclic graphs of spouts (data sources) and bolts (processing steps). Storm guaranteed at-least-once or exactly-once delivery semantics via record-level acknowledgments (Trident for exactly-once). The latency was low because processing was per-record.

Spark Streaming used a different model — micro-batching: it collected events into small time windows (e.g., 1 second), processed each batch as a Spark RDD, and produced output. This meant slightly higher latency (bounded by batch interval) but full compatibility with the rest of the Spark ecosystem: you could share code between batch and streaming jobs, use MLlib for streaming ML, and query streaming results with Spark SQL. The unified model became the dominant argument for Spark Streaming.

The 2014 outcome of this comparison was context-dependent: Storm for sub-second latency requirements, Spark Streaming for workloads where unified batch+streaming mattered more than minimizing latency. Later, Apache Flink combined true streaming semantics with a unified batch model, and Kafka Streams simplified streaming by integrating directly with Kafka.

## Key points

- Apache Storm: per-record stream processing — true streaming semantics, sub-second latency, topology-based DAGs.
- Apache Spark Streaming: micro-batching — collects events into RDD batches, unified with Spark batch API.
- Latency tradeoff: Storm wins on latency; Spark Streaming wins on unified API and ecosystem integration.
- Nathan Marz created Storm and also coined the Lambda Architecture — the pattern combining Storm (speed layer) with Hadoop (batch layer).
- Historical trajectory: Apache Flink eventually superseded both for production stream processing by offering true streaming + batch unification.

[Original](http://www.slideshare.net/ptgoetz/apache-storm-vs-spark-streaming) → REST API
