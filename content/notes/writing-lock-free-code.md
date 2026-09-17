---
title: "Writing Lock-Free Code: A Corrected Queue"
date: 2012-08-19
categories:
  - concurrency
  - lock-free
  - systems-programming
  - c++
  - algorithms
description: Dr. Dobb's article on writing correct lock-free code using a corrected queue implementation. Lock-free data structures are famously difficult to get right — this piece walked through the subtle bugs that make naive implementations incorrect.
params:
  source: pinboard
  sourceUrl: http://www.drdobbs.com/article/print?articleId=210604448&siteSectionName=parallel
---

## Summary

A Dr. Dobb's article on implementing correct lock-free data structures, using a concurrent queue as the case study. Lock-free programming is one of the most notoriously difficult areas of concurrent programming — the naive version of almost every lock-free algorithm is wrong, and the bugs are timing-dependent, making them nearly impossible to reproduce with testing.

The challenge with lock-free queues (and lock-free data structures generally) is that you can't use mutual exclusion to protect shared state, so you must use compare-and-swap (CAS) atomic operations to make updates appear instantaneous from other threads' perspectives. The classic Maged Michael and Michael Scott lock-free queue algorithm (published 1996) uses a two-pointer approach with CAS operations on both head and tail pointers, but has subtle correctness issues around the ABA problem — where a pointer value appears to have not changed but the underlying state has cycled.

The article's "corrected" framing referred to fixing the ABA problem through hazard pointers or epoch-based reclamation — memory management schemes that prevent the reuse of freed nodes until all threads that might have references to them have passed through a safe point. This was a major practical hurdle for lock-free implementations: correct memory reclamation in a lock-free context is almost as hard as the core algorithm itself. Rust's ownership model later made lock-free memory management significantly more tractable.

## Key points

- Lock-free data structures use compare-and-swap (CAS) atomic operations instead of mutexes.
- The ABA problem: a CAS succeeds because the value looks the same, but intermediate state changes have occurred — classic source of lock-free bugs.
- Hazard pointers and epoch-based reclamation solve the lock-free memory reclamation problem.
- The Michael-Scott lock-free queue (1996) is the canonical reference; this article provides corrections.
- Lock-free queues are faster than mutex-based queues under high contention but are much harder to implement correctly.
- Rust's ownership model later made lock-free memory management significantly more tractable.

[Original](http://www.drdobbs.com/article/print?articleId=210604448&siteSectionName=parallel)
