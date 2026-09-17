---
title: Introduction to Deep Learning on Hadoop (Hadoop Summit 2014)
date: 2014-03-01
categories:
  - deep-learning
  - hadoop
  - distributed-systems
  - big-data
  - neural-networks
description: A Hadoop Summit 2014 session proposal on deep learning at Hadoop scale — from the team behind DL4J (DeepLearning4J), a Java-native deep learning framework designed to run on Hadoop/Spark clusters. A snapshot of the moment distributed deep learning was being invented.
params:
  source: pinboard
  sourceUrl: https://hadoopsummit.uservoice.com/forums/242804-data-science-hadoop-track/suggestions/5568291-introduction-to-deep-learning-on-hadoop
---

## Summary

This Hadoop Summit 2014 session proposal came from Josh Patterson ([@jpatanooga](https://twitter.com/jpatanooga)) and Adam Gibson ([@agibsonccc](https://twitter.com/agibsonccc)), the team building DL4J (DeepLearning4J) — one of the first deep learning frameworks written in Java specifically to run on Hadoop and Apache Spark clusters. The tweet from @ryanorban signals interest in this work at exactly the moment distributed deep learning was transitioning from lab curiosity to something practitioners could attempt.

In early 2014, running deep learning at scale meant solving a specific problem: existing frameworks (Theano, early Caffe) were single-machine tools. Training on large datasets required either downsampling to fit one GPU or building custom distributed infrastructure. DL4J attacked this by integrating with the Hadoop ecosystem — using HDFS for data storage, YARN for resource management, and later Apache Spark for the distributed computation layer.

The session would have covered backpropagation across distributed nodes, handling the gradient synchronization problem (how do you combine gradient updates from multiple machines without them stepping on each other?), and the specific neural networks architectures that were tractable to train at Hadoop scale in 2014. This was 18 months before Google's TensorFlow made distributed training infrastructure mainstream.

## Key points

- DL4J (DeepLearning4J): Java-native deep learning framework designed for Hadoop/Apache Spark integration — trained models on distributed clusters.
- Josh Patterson and Adam Gibson later co-authored "Deep Learning: A Practitioner's Approach" (O'Reilly) — the book emerging from this practical distributed work.
- Distributed deep learning in 2014 meant gradient synchronization across nodes — the parameter server pattern that later became standard.
- Hadoop Summit Data Science track: a signal that the Hadoop ecosystem was trying to absorb machine learning as a use case, not just ETL.
- Theano and Caffe were the single-machine alternatives — DL4J was the distributed bet.

[Original](https://hadoopsummit.uservoice.com/forums/242804-data-science-hadoop-track/suggestions/5568291-introduction-to-deep-learning-on-hadoop)
