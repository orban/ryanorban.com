---
title: Deploying Storm on GCE
date: 2013-12-30
categories:
  - storm
  - stream-processing
  - google-cloud
  - distributed-systems
  - big-data
description: Tutorial on deploying Apache Storm on Google Compute Engine — a setup guide for real-time stream processing at a time when cloud deployments of Storm were uncommon. GCE was a relatively new platform and Storm was the dominant real-time processing framework before Flink/Spark Streaming.
params:
  source: pinboard
  sourceUrl: http://datadventures.markbox.io/2013/12/29/storm-on-gce
---

## Summary

Apache Storm was the dominant real-time stream processing framework in 2013 — Twitter had open-sourced it that year, and it was the standard tool for processing high-velocity data before Apache Flink and Spark Streaming displaced it. This tutorial covers deploying a Storm cluster on Google Compute Engine (GCE), which at the time was a newer platform still establishing itself against AWS.

A Storm deployment has three components: Zookeeper for cluster coordination, a Nimbus node (the master that distributes work), and Supervisor nodes (workers that run topology tasks). Deploying on GCE required provisioning VMs, configuring networking and firewall rules, and setting up the Storm cluster config to reference the GCE instance addresses — steps that today would largely be handled by Kubernetes or a managed service.

The tutorial represents the cloud but manual era: IaaS was available, but the tooling for automated cluster management (Kubernetes, Terraform) hadn't matured. Setting up a Storm cluster on GCE was a meaningful engineering task.

## Key points

- Apache Storm: real-time stream processing framework open-sourced by Twitter in 2013 — processes unbounded streams of tuples via directed acyclic graphs called topologies.
- Architecture: Nimbus (master) + Zookeeper (coordination) + Supervisor nodes (workers). All three needed on GCE.
- Google Compute Engine was newer than AWS EC2 in 2013 — tutorials for GCE deployment were less common.
- Storm was eventually superseded by Apache Flink and Spark Streaming for new deployments, though it ran production workloads for years.
- The "deploy a cluster manually on cloud VMs" paradigm was standard in 2013 — before containers and orchestration made it obsolete.

[Original](http://datadventures.markbox.io/2013/12/29/storm-on-gce)
