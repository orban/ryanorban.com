---
title: System Design Primer
date: 2021-01-06
categories:
  - system-design
  - distributed-systems
  - interview
  - reference
  - github
description: Donnemartin's system-design-primer is the most starred GitHub repository for learning how to design large-scale systems — covers scalability, caching, databases, load balancing, and common interview patterns. The Anki flashcard deck makes it unusually retention-friendly.
params:
  source: pinboard
  sourceUrl: https://github.com/donnemartin/system-design-primer
---

## Summary

[System Design Primer](/notes/system-design-primer/) by donnemartin is one of the most starred repositories on GitHub — a comprehensive reference for understanding how large-scale systems are designed. It covers the canonical topics in distributed systems interviews: scalability, load balancing, caching, database sharding, CAP theorem, consistency patterns, DNS, CDNs, reverse proxy, microservices, message queues, and more. Each section includes diagrams, tradeoff discussions, and links to real-world examples.

The structure is dual-purpose: a learning resource for engineers who want to understand systems, and interview prep for system design interviews at large tech companies. It includes worked examples for designing systems like Twitter, URL shorteners, and pastebin — the classic interview archetypes. The Anki flashcard deck is a notable addition that takes the material beyond passive reading.

What's useful beyond interviews is the collection of real-world case studies: how Amazon, Twitter, Netflix, and others actually solved specific scaling problems. These aren't invented for the guide — they're summaries of engineering blog posts and papers. The section on database patterns (master-slave replication, federation, sharding, NoSQL tradeoffs) is particularly strong for practitioners who work with data at scale.

## Key points

- Covers the full system design interview surface: scalability, caching, load balancing, replication, consistent hashing, CAP theorem.
- Includes worked examples for classic interview problems: URL shortener, Twitter timeline, web crawler.
- Real-world case study summaries from engineering blogs at Amazon, Twitter, Netflix, Airbnb.
- Anki flashcard deck included — makes active recall viable for such a broad topic.
- Organized to be read sequentially (learning) or referenced selectively (interview prep).

[Original](https://github.com/donnemartin/system-design-primer)
