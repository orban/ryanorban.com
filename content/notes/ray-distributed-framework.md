---
title: "Ray: A Distributed Framework for Emerging AI Applications"
date: 2021-07-04
categories:
  - machine-learning
  - distributed-systems
  - ray
  - python
  - infrastructure
description: Micah Lerner's paper summary of Ray — UC Berkeley's distributed computing framework for AI workloads. Ray unified task-parallel and actor-based distributed computing in a Python-native API, becoming the foundation for libraries like RLlib, Tune, and later Ray Serve.
params:
  source: pinboard
  sourceUrl: https://www.micahlerner.com/2021/06/27/ray-a-distributed-framework-for-emerging-ai-applications.html
---

![Ray: A Distributed Framework for Emerging AI Applications](/images/notes/ray-distributed-framework.png)

## Summary

Micah Lerner's blog summarizes the Ray paper from UC Berkeley RISELab. Ray is a distributed computing framework designed specifically for AI and machine learning workloads — unlike general-purpose distributed systems (Spark, Dask), Ray was designed from the start for the specific patterns that ML training, hyperparameter tuning, and reinforcement learning require.

The core abstraction: two programming models unified under one API. **Tasks** are stateless remote functions — you call `ray.remote(my_function)(args)` and it executes on a worker in the cluster. **Actors** are stateful remote objects — a class decorated with `@ray.remote` can be instantiated in the cluster, with methods called remotely. The actor model is essential for RL training where you need multiple workers maintaining local state (experience buffers, policy weights).

What made Ray compelling at the time of the paper (2018–2019): it handled the RL training pattern better than Spark or TensorFlow's distributed primitives. Asynchronous task execution, dynamic task graphs, and fault tolerance through lineage reconstruction all matched the needs of large-scale deep RL experiments. The RLlib library built on Ray became a standard toolkit for RL research.

## Key points

- Dual model: stateless **tasks** (remote functions) + stateful **actors** (remote objects) in one API.
- Designed for AI workloads: handles asynchronous task graphs, RL training patterns, and large-scale hyperparameter search.
- Ray Tune (hyperparameter search), RLlib (reinforcement learning), and Ray Serve (model serving) are the main libraries built on Ray.
- Scales from a laptop (local mode) to a large cluster with the same code — dev/prod parity.
- From UC Berkeley RISELab; became the leading Python-native distributed ML framework alongside Dask.

[Original](https://www.micahlerner.com/2021/06/27/ray-a-distributed-framework-for-emerging-ai-applications.html)
