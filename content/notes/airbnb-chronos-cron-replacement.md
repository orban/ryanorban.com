---
title: "Airbnb Open Sources Chronos: A Distributed Cron Replacement"
date: 2013-03-17
categories:
  - scheduling
  - distributed-systems
  - airbnb
  - mesos
  - open-source
description: Airbnb's open-sourcing of Chronos, a distributed cron replacement built on Apache Mesos. A notable moment in the early days of the Mesos ecosystem, showing how Twitter-era infrastructure patterns were spreading across Silicon Valley companies.
params:
  source: pinboard
  sourceUrl: http://techcrunch.com/2013/03/15/airbnb-open-sources-its-chronos-scheduler-a-more-flexible-cron-replacement-with-a-web-based-gui/
---

## Summary

In March 2013, Airbnb open-sourced Chronos, their internal distributed job scheduler — framed as a more flexible replacement for the traditional Unix cron daemon. Chronos ran on top of Apache Mesos, Twitter's cluster resource manager that was gaining traction as a way to run multiple workloads on shared infrastructure. The combination represented a pattern that would define the next few years of distributed infrastructure: replace single-node tools with cluster-aware equivalents built on a shared resource layer.

The problems cron solves at one machine don't scale: if the machine goes down, jobs don't run; there's no dependency management between jobs; there's no visibility into job status or history; and you can't easily distribute work across multiple machines. Chronos addressed all of these. It provided a web UI for managing and monitoring jobs, supported ISO 8601 schedule formats and job dependencies (job A starts after job B succeeds), and used Mesos for fault tolerance and resource allocation — if a job's executor node failed, Mesos could reschedule it on another node.

The broader significance was as an early validation of the Apache Mesos ecosystem. Twitter had built Mesos internally and open-sourced it, but having other major companies adopt it and build on top demonstrated it was becoming infrastructure-layer technology. LinkedIn was building their own job scheduler infrastructure, Netflix was building similar tools, and the pattern of "take a single-machine tool, make it cluster-aware via Mesos" was producing a wave of open-source projects. Chronos and Marathon (Airbnb's long-running service manager, also on Mesos) prefigured the scheduler wars that Kubernetes eventually settled.

## Key points

- Chronos is a distributed, fault-tolerant cron built on Apache Mesos — jobs are scheduled across a cluster, not on one machine
- Supports ISO 8601 repeating intervals, job dependency graphs (DAGs), and has a REST API for programmatic job management
- Web-based GUI for job creation and monitoring — a significant usability improvement over editing crontabs
- Apache Mesos provides the resource layer: Chronos tasks are Mesos tasks, so they get the same fault tolerance and isolation guarantees as other Mesos workloads
- Historically positioned: predates Kubernetes by 2 years and Apache Airflow by 1 year — part of the distributed scheduling lineage that led to current orchestration tools
- Airbnb was an early Mesos adopter because of Twitter's influence in Silicon Valley engineering culture; this was the network-effect moment for Mesos

[Original](http://techcrunch.com/2013/03/15/airbnb-open-sources-its-chronos-scheduler-a-more-flexible-cron-replacement-with-a-web-based-gui/)
