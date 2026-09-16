---
title: Yahoo! Spinning Continuous Computing with YARN
date: 2013-06-29
categories:
  - yarn
  - hadoop
  - yahoo
  - stream-processing
  - distributed-systems
description: Yahoo's 2013 exploration of using YARN as a substrate for continuous/streaming computation beyond batch MapReduce. An early signal that the Hadoop ecosystem was trying to absorb real-time processing use cases before Apache Spark and Flink fully took over.
params:
  source: pinboard
  sourceUrl: http://www.datanami.com/datanami/2013-06-28/yahoo_spinning_continuous_computing_with_yarn.html
---

![Yahoo! Spinning Continuous Computing with YARN](/images/notes/yahoo-yarn-continuous-computing.png)

## Summary

Yahoo was one of the primary architects of YARN (Yet Another Resource Negotiator) — the resource management layer that decoupled Hadoop's compute scheduling from MapReduce specifically, making Hadoop 2.0 capable of running arbitrary distributed applications. This 2013 Datanami piece covered Yahoo's exploration of using YARN as the substrate not just for batch jobs but for continuous (streaming) computation.

The architectural insight: if YARN can schedule and manage arbitrary long-running distributed applications, not just batch MapReduce jobs, then a streaming application is just a YARN application that never terminates. Yahoo was experimenting with this model to run Apache Storm-style streaming pipelines and stateful continuous computation on the same cluster infrastructure as their Hadoop batch jobs.

This exploration happened at a critical moment: Apache Spark was gaining traction, Apache Storm was the dominant stream processing framework, and the question of whether the Hadoop ecosystem could absorb real-time workloads was live. YARN turned out to be the right bet — both Spark and Apache Flink run on YARN, making it the common resource management layer for the modern batch + streaming stack.

## Key points

- YARN separates resource management from the programming model — any distributed application can run as a YARN application, not just MapReduce.
- Continuous computing on YARN: long-running applications that receive and process events rather than processing a bounded input dataset.
- Yahoo was running petabyte-scale Hadoop clusters and needed both batch and streaming on the same infrastructure — multi-tenancy was the economic driver.
- YARN became the common substrate: Apache Spark, Apache Flink, and Apache Storm all gained YARN support, validating Yahoo's bet.
- The alternative was separate clusters for batch (Hadoop) and streaming (Storm) — YARN made the converged cluster possible.

[Original](http://www.datanami.com/datanami/2013-06-28/yahoo_spinning_continuous_computing_with_yarn.html)
