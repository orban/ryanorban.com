---
title: Yelp Pyleus — Apache Storm Topologies in Pure Python
date: 2014-10-16
categories:
  - streaming
  - python
  - apache-storm
  - data-engineering
  - open-source
description: Yelp open-sources Pyleus — a framework for writing Apache Storm stream processing topologies in pure Python. Solved the JVM barrier that kept Python data engineers from using Storm's real-time streaming capabilities.
params:
  source: pinboard
  sourceUrl: http://engineeringblog.yelp.com/2014/10/introducing-pyleus.html
---

## Summary

Yelp published Pyleus in October 2014 — an open-source framework that let Python developers write Apache Storm stream processing topologies without touching Java or Clojure. Storm was the dominant real-time stream processing system before Apache Kafka Streams and Apache Flink matured, but its native API was Java/Clojure — a barrier for Python-native data engineering teams.

Apache Storm processes unbounded streams of data as directed acyclic graphs called topologies. Spouts emit records from sources (Kafka, queues, APIs); bolts transform and route them. Topologies run across a cluster with automatic fault tolerance and guaranteed processing. The problem: writing bolts in Java when your team thinks in Python means splitting your codebase and losing Python's ecosystem for data work.

Pyleus solved this with a YAML-based topology definition and a Python wrapper that handled the Storm multilang protocol (which Storm uses to spawn and communicate with non-JVM processes). Each bolt and spout became a Python class. This pattern — wrapping Storm's multilang protocol — wasn't unique to Yelp, but Pyleus was a clean, production-tested implementation from a company running real streaming workloads.

## Key points

- Pyleus: Yelp's open-source framework for writing Apache Storm topologies in pure Python.
- Apache Storm: real-time stream processing via spout/bolt DAGs — dominant before Kafka Streams and Flink.
- Solves the JVM barrier: Storm's multilang protocol allows non-JVM workers; Pyleus wraps this cleanly for Python.
- Topology defined in YAML; bolts and spouts as Python classes — no Java required.
- Yelp was an early serious user of real-time data infrastructure — their engineering blog was a credible source in 2014.
- By 2017, Apache Kafka + Kafka Streams had largely displaced Storm for new streaming projects.

[Original](http://engineeringblog.yelp.com/2014/10/introducing-pyleus.html)
