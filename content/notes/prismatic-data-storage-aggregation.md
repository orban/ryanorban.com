---
title: How Prismatic Deals with Data Storage and Aggregation
date: 2012-04-09
categories:
  - data-engineering
  - stream-processing
  - clojure
  - architecture
  - interest-graph
description: Prismatic's 2012 engineering post on their data architecture for real-time news personalization — using Storm for stream processing, Cassandra for distributed storage, and a Clojure-based interest graph. An early look at the stream-processing stack that became standard infrastructure.
params:
  source: pinboard
  sourceUrl: http://blog.getprismatic.com/blog/2012/4/9/how-prismatic-deals-with-data-storage-and-aggregation.html
---

![How Prismatic Deals with Data Storage and Aggregation](/images/notes/prismatic-data-storage-aggregation.png)

## Summary

Prismatic was a news aggregation startup (2011–2014) that built personalized news feeds based on users' interest graphs. Their engineering blog post from 2012 described the data infrastructure behind their real-time personalization engine — one of the earlier public write-ups of the stream processing architecture that later became standard.

Their stack used Apache Storm for stream processing (real-time computation on unbounded data streams), Apache Cassandra for distributed storage (write-heavy, eventually consistent, horizontally scalable), and Clojure as the implementation language throughout. The architecture separated ingestion, processing, and serving concerns: articles flowed in from RSS feeds and crawlers, Storm processed them through a topology of compute nodes, and Cassandra stored both the processed articles and the per-user interest models.

The interest graph was the core product: a representation of which topics a user cared about, inferred from their reading behavior and social graph connections. Aggregating signals from multiple sources (Twitter, reading history, explicit topic follows) and merging them in real-time required the kind of low-latency stream architecture that was only becoming tractable in 2012 with tools like Storm and Kafka.

## Key points

- Apache Storm for real-time stream processing — predecessor to Apache Flink and Kafka Streams.
- Apache Cassandra for distributed key-value/column storage — designed for write-heavy workloads at scale.
- Clojure throughout: the functional, immutable data model was a natural fit for stream processing pipelines.
- Interest graph as the core data model: inferring topic preferences from behavior rather than explicit tagging.
- Early example of the stream-first architecture that became the norm in data engineering by 2015–2017.
- Prismatic was acquired by Flipboard in 2014 — the product died but the engineering influenced the field.

[Original](http://blog.getprismatic.com/blog/2012/4/9/how-prismatic-deals-with-data-storage-and-aggregation.html)
