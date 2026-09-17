---
title: Introduction to Apache Kafka (TriHUG, July 2013)
date: 2013-07-24
categories:
  - apache-kafka
  - distributed-systems
  - messaging
  - streaming
  - big-data
description: TriHUG July 2013 talk introducing Apache Kafka — the distributed log system LinkedIn built and open-sourced. Caught at the moment Kafka was still an unfamiliar tool to most data engineers, before it became the de-facto streaming backbone of the modern data stack.
params:
  source: pinboard
  sourceUrl: http://www.slideshare.net/mumrah/kafka-talk-tri-hug
---

![Introduction to Apache Kafka (TriHUG, July 2013)](/images/notes/apache-kafka-introduction.png)

## Summary

This Triangle Hadoop User Group (TriHUG) talk from July 2013 introduced Apache Kafka to a Hadoop-focused audience at a moment when Kafka was still a relatively unknown tool. LinkedIn had built Kafka to solve a specific problem: moving high-volume activity data (page views, clicks, searches) between their production systems and their analytics Hadoop cluster without data loss or coupling. The open-source release in 2011 had given the Hadoop community access to a distributed, durable, high-throughput message queue with fundamentally different semantics than existing messaging systems.

The core innovation in Kafka's design is that it's built around a distributed log rather than a traditional queue. Messages are persisted to disk (not discarded on consumption), consumers track their own offsets, and the same message stream can be read by multiple independent consumer groups. This means a single Kafka topic can simultaneously feed a Hadoop batch job, a real-time alerting system, and an audit log — all replaying from the same durable stream. In 2013, ActiveMQ and RabbitMQ dominated the messaging space; Kafka's durable-log model was a different paradigm.

The talk was given at a Hadoop user group, reflecting Kafka's original use case as a bridge between operational systems and the Hadoop ecosystem. By 2015, Apache Kafka had become the central nervous system for streaming architectures, and the Kafka Connect and Kafka Streams APIs extended it far beyond its original scope.

## Key points

- Apache Kafka is a distributed log, not a queue: messages persist after consumption, consumers manage their own offsets, and replay is built in.
- LinkedIn built Kafka to handle hundreds of billions of events per day — activity tracking at a scale that would overwhelm traditional messaging systems.
- The publish-subscribe model with consumer groups allows the same data stream to feed multiple downstream systems independently.
- Partitioning is the key to Kafka's horizontal scalability: a topic is split into ordered partitions distributed across brokers.
- In 2013, this was positioned as a pipeline tool for Hadoop — within a few years it had become the foundation for stream processing architectures replacing batch ETL.

[Original](http://www.slideshare.net/mumrah/kafka-talk-tri-hug)
