---
title: Distributed Systems and the End of the API
date: 2014-05-13
categories:
  - distributed-systems
  - architecture
  - api
  - microservices
  - engineering
description: Prismatic's provocative argument that the traditional synchronous REST API is the wrong primitive for distributed systems — proposing message-passing and event streams as the better foundation. Anticipates the 2014-era shift toward event-driven architectures and the explosion of streaming systems.
params:
  source: pinboard
  sourceUrl: http://getprismatic.com/story/1399903906122
---

## Summary

This Prismatic post argues that the conventional REST API — synchronous request-response over HTTP — is fundamentally mismatched to the demands of large-scale distributed systems. The argument: synchronous APIs create tight temporal coupling (caller blocks until response), cascade failures (one slow service slows all callers), and make it hard to reason about system-wide consistency when dozens of services call each other.

The alternative the post advocates is asynchronous message passing: services publish events to a message queue or event stream, and consumers subscribe and process at their own pace. This decouples producers from consumers in both time and availability — a service can be down without blocking its callers, and backlogs are handled by the queue rather than propagating as timeouts.

In 2014, this argument was ahead of the mainstream but gaining traction: Apache Kafka had been open-sourced by LinkedIn in 2011, RabbitMQ was in wide use, and companies like Twitter and Netflix were documenting their event-driven architectures. The post anticipates the subsequent explosion of streaming systems (Apache Flink, Apache Spark Streaming) and the microservices-with-event-bus pattern that became dominant by 2018.

## Key points

- Synchronous APIs create temporal coupling — the caller must wait, so slow dependencies create cascading latency across a system.
- Asynchronous messaging decouples availability: producers and consumers operate independently, with the message queue absorbing bursts and providing backpressure.
- Event-driven architecture enables eventual consistency — a design choice that trades strong consistency guarantees for availability and partition tolerance (CAP theorem).
- The pattern enables event sourcing and CQRS — treating the event log as the system of record rather than a database snapshot.
- Contrarian framing (end of API) reflects 2014's microservices moment: teams were questioning REST conventions they'd inherited from simpler systems.

[Original](http://getprismatic.com/story/1399903906122)
