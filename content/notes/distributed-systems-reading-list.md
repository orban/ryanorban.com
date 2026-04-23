---
title: A Distributed Systems Reading List
date: 2024-10-19
categories:
  - distributed-systems
  - reading-list
  - books
  - papers
  - engineering
description: Fred Hebert's curated distributed systems reading list — covering foundational papers, books, and blog posts from the Fallacies of Distributed Computing through CAP theorem, consensus, CRDTs, and failure handling. One of the more practical and opinionated guides to the field.
params:
  source: pinboard
  sourceUrl: https://ferd.ca/a-distributed-systems-reading-list.html
---

![A Distributed Systems Reading List](/images/notes/distributed-systems-reading-list.png)

## Summary

Fred Hebert (ferd.ca, author of Learn You Some Erlang) curated this reading list as a practical guide to distributed systems for engineers who need to build real systems rather than just pass interviews. The list is organized thematically: foundational failure modes (the Fallacies of Distributed Computing), consistency and consensus, fault tolerance, time and clocks, and practical tooling.

The opinionated framing is a feature — Fred spent years building distributed Erlang systems at places like Heroku and Discord, so the selections reflect battle-tested importance rather than just academic prestige. He includes classic papers (Lamport clocks, Paxos, Dynamo, Spanner) alongside practical resources that explain why these concepts matter when your RPC call fails silently or your clock skews by 100ms.

Key inclusions: Leslie Lamport's time and clocks paper, Werner Vogels' Amazon Dynamo paper, the Google Spanner paper on TrueTime, Martin Kleppmann's Designing Data-Intensive Applications (essentially the textbook version of this reading list), and Kyle Kingsbury's Jepsen analyses. Together they cover the gap between "I know what eventual consistency means and I know how to reason about what breaks when."

## Key points

- Covers distributed systems from foundations (Fallacies of Distributed Computing) through CAP theorem, consensus, CRDTs, and failure handling
- Curated by Fred Hebert — pragmatic selections reflecting production experience with Erlang/OTP distributed systems
- Essential reads: Lamport clocks, Dynamo paper, Spanner, Designing Data-Intensive Applications
- Pairs well with Heidi Howard's distributed consensus reading list (more focused on consensus algorithms)
- Good starting point before Jepsen analysis rabbit holes

[Original](https://ferd.ca/a-distributed-systems-reading-list.html)
