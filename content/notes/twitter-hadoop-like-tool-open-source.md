---
title: Twitter to Open Source Hadoop-Like Tool (Storm)
date: 2012-07-07
categories:
  - hadoop
  - big-data
  - twitter
  - open-source
  - distributed-systems
description: GigaOM coverage of Twitter's plans to open-source Storm — their real-time stream processing system. The moment the Hadoop-for-streaming gap became a major industry conversation, and Nathan Marz's Storm became the answer.
params:
  source: pinboard
  sourceUrl: http://gigaom.com/cloud/twitter-to-open-source-hadoop-like-tool/
---

![Twitter to Open Source Hadoop-Like Tool (Storm)](/images/notes/twitter-hadoop-like-tool-open-source.png)

## Summary

This 2012 GigaOM article covered Twitter's plans to open-source Apache Storm — at the time called "the Hadoop of real-time processing." While Hadoop MapReduce excelled at batch processing of large datasets, Twitter's core infrastructure need was different: process a firehose of tweets in real-time, continuously, with low latency. A batch job that runs every hour can't drive real-time trend detection or spam filtering. Twitter built Storm to fill this gap.

Apache Storm (developed by Nathan Marz at BackType, which Twitter acquired in 2011) implemented a stream processing model organized around topologies: directed graphs of spouts (data sources) and bolts (processing nodes). Spouts read from Kafka, databases, or the Twitter firehose; bolts transform, aggregate, and route data. The topology runs continuously — unlike MapReduce, there's no batch boundary. Storm guaranteed at-least-once message delivery, which made it reliable but required idempotent bolt logic to handle redelivery.

Storm's open-sourcing in 2011 (with wider attention through 2012) was a pivotal moment in the big data ecosystem. It established that Hadoop + Storm = batch + streaming — the "Lambda Architecture" pattern Nathan Marz would later formalize. The tension between batch and streaming views of large-scale data drove a decade of systems research, eventually leading to Apache Spark Streaming, Apache Flink, and Apache Kafka Streams as unified or hybrid models. Storm itself remained influential but eventually lost ground to Flink for stateful streaming workloads.

## Key points

- Apache Storm = real-time stream processing built on topologies of spouts (sources) and bolts (processors) — the Hadoop equivalent for streaming.
- Developed by Nathan Marz at BackType/Twitter; open-sourced 2011, entered Apache Incubator 2012.
- At-least-once delivery guarantee — reliable but requires idempotent bolt logic.
- Established the batch + streaming = Lambda Architecture pattern alongside Hadoop MapReduce.
- Superseded by Apache Flink for stateful streaming and Apache Spark Streaming for teams already on Spark.
- Twitter's open-sourcing was part of a broader wave: Apache Kafka (LinkedIn), Apache Samza (LinkedIn), all addressing the streaming gap that MapReduce couldn't fill.

[Original](http://gigaom.com/cloud/twitter-to-open-source-hadoop-like-tool/)
