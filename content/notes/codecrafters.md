---
title: "CodeCrafters: Advanced Programming Challenges"
date: 2022-08-04
categories:
  - programming
  - education
  - developer-tools
  - systems
description: CodeCrafters offers advanced programming challenges where you rebuild real systems — Redis, Git, SQLite, a Unix shell — from scratch in your own IDE using Git-push-based testing. Designed for experienced developers who want systems-level depth.
params:
  source: pinboard
  sourceUrl: https://codecrafters.io/
---

## Summary

[CodeCrafters](/notes/codecrafters/) is a programming challenge platform aimed squarely at experienced developers, not beginners. Where platforms like LeetCode focus on algorithm puzzles and Exercism on language idioms, [CodeCrafters](/notes/codecrafters/) asks you to rebuild entire real-world systems from scratch: Redis, Git, SQLite, a Unix shell, an HTTP server, a DNS server, a BitTorrent client, a Kafka clone. The challenges have dozens to nearly 100 stages each, progressively adding complexity until you've implemented something that actually works like the real thing.

The learning approach is deliberately professional: you work in your own editor with your own tools, push to a Git remote, and get automated test feedback. No web-based sandbox. This matches how working engineers actually write code, which is part of the value proposition — you're building skills the way you'll use them. The curriculum is currently in multiple languages, so you can implement Redis in Go, Rust, TypeScript, or Python depending on what you want to practice.

The value of rebuilding real systems is specifically that it forces you to understand the internals that are usually hidden behind abstractions. Most developers know Git as a porcelain layer of commands but have never thought about pack files, refs, or the object store. Building Git from scratch means understanding these. The same applies to Redis's single-threaded event loop, SQLite's B-tree storage, and DNS's wire format. Y Combinator-backed; endorsed by engineers from top tech companies.

## Key points

- Build real systems from scratch: Redis, Git, SQLite, Unix shell, HTTP server, DNS, BitTorrent, Kafka
- Work in your own IDE with Git-push-based test feedback — professional tooling, not web sandbox
- Targets experienced developers wanting systems-level depth, not algorithmic trivia
- Each challenge has 47–97 stages of progressive complexity
- Forces understanding of internals usually hidden by abstractions: pack files, B-trees, event loops, wire protocols
- Backed by Y Combinator; multiple language support

[Original](https://codecrafters.io/)
