---
title: "WunderGraph: open-source GraphQL federation"
date: 2024-04-11
categories:
  - graphql
  - federation
  - api
  - developer-tools
  - open-source
description: WunderGraph is an open-source, Apache 2.0 licensed GraphQL federation solution with schema registry, composition checks, analytics, and routing — deployable on-premises or as a managed service. Targets teams building federated GraphQL APIs who want to avoid vendor lock-in.
params:
  source: pinboard
  sourceUrl: https://wundergraph.com/
---

![WunderGraph: open-source GraphQL federation](/images/notes/wundergraph-graphql-federation.png)

## Summary

WunderGraph provides the full lifecycle tooling for Federated GraphQL — schema registry, composition checks, analytics, metrics, tracing, and routing — under the Apache 2.0 license. The license is the key differentiator: Apollo Federation and Hasura federation are the incumbents in this space, but both have commercial licensing constraints for their most useful features. WunderGraph is a bet that the market wants a truly open alternative.

GraphQL Federation is an architectural pattern for composing multiple GraphQL subgraphs into a unified API. Each service exposes its own subgraph; the router composes them and routes queries to the right service. This solves the API proliferation problem in large organizations: instead of exposing dozens of separate REST APIs or GraphQL endpoints, you expose one unified graph that clients query as a single service.

The analytics and observability layer (metrics, tracing, routing analytics) addresses a practical gap: running a federated graph in production requires understanding query performance across subgraphs, identifying which services are bottlenecks, and monitoring composition health when subgraph schemas change. WunderGraph bundles this into the same system as the federation infrastructure itself.

## Key points

- Full GraphQL Federation lifecycle: schema registry, composition checks, router, analytics, tracing — all Apache 2.0.
- Deploys fully on-prem or as managed service — no vendor lock-in on the core federation infrastructure.
- Schema composition validation prevents breaking changes in subgraphs from propagating to the unified graph.
- Competes with Apollo Federation and Hasura but with open licensing.
- Tracing and analytics built into the federation layer — understand query performance across subgraphs.

[Original](https://wundergraph.com/)
