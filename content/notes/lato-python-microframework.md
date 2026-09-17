---
title: "Lato: Python Microframework for Modular Monoliths"
date: 2023-12-04
categories:
  - python
  - architecture
  - modular-monolith
  - open-source
  - backend
description: Lato is a Python microframework for building modular monoliths and loosely coupled applications — explicit module boundaries, dependency injection, and event-driven communication within a single process. A structured alternative to ad-hoc Django app organization.
params:
  source: pinboard
  sourceUrl: https://github.com/pgorecki/lato
---

![Lato: Python Microframework for Modular Monoliths](/images/notes/lato-python-microframework.png)

## Summary

Lato is a lightweight Python framework for building modular monoliths — applications with clear internal module boundaries that run as a single process, without the operational overhead of microservices. It provides the structural tools that are missing from raw Django or Flask: explicit module interfaces, dependency injection, and in-process event-driven communication between modules.

The modular monolith pattern has been gaining traction as a more pragmatic alternative to microservices for most applications. Microservices solve distributed team coordination and independent scaling, but they add latency (network calls between services), operational complexity (service discovery, deployment pipelines per service), and distributed systems failure modes. For teams that don't need those tradeoffs, a well-structured monolith with clear module boundaries gives most of the organizational benefits without the operational cost.

Lato brings structure to Python applications that typically lack it: a Django project with many apps starts clean but accumulates cross-app imports, shared state, and tangled dependencies. Lato's module system enforces interfaces — modules communicate through events or explicit API calls, not by importing each other's internals. This makes it easier to extract a module into a microservice later if you actually need to.

## Key points

- Modular monolith pattern: clear module boundaries within a single process — organized without distributed overhead.
- Dependency injection built in — modules declare dependencies explicitly rather than importing globally.
- In-process event bus: modules communicate via events, not direct imports — decoupled but fast.
- Lightweight: not a full framework, layered on top of existing Python web frameworks.
- Facilitates gradual extraction to microservices if needed — modules have explicit interfaces.
- Compared to Django apps: lato enforces boundaries; Django apps encourage cross-app coupling.

[Original](https://github.com/pgorecki/lato) → GitHub
