---
title: nginx Architecture (AOSA Vol. 2)
date: 2012-07-07
categories:
  - nginx
  - software-architecture
  - open-source
  - systems-programming
  - aosa
description: The nginx chapter from Architecture of Open Source Applications — Andrew Alexeev's deep dive into how nginx achieves high concurrency through event-driven, asynchronous I/O rather than the Apache thread-per-connection model. The clearest explanation of why nginx's design matters and what C10K forced people to rethink.
params:
  source: pinboard
  sourceUrl: http://www.aosabook.org/en/nginx.html
---

![nginx Architecture (AOSA Vol. 2)](/images/notes/nginx-architecture-aosa.png)

## Summary

nginx is a web server, reverse proxy, and load balancer built around a fundamentally different concurrency model than Apache HTTP Server. While Apache spawns a thread or process per connection — simple to reason about but catastrophically expensive at high concurrency — nginx handles tens of thousands of connections in a single worker process using event-driven I/O. This design choice was a direct response to the C10K problem: how do you handle 10,000 concurrent connections on commodity hardware?

The core abstraction is the event loop. An nginx worker runs a tight loop: ask the OS (via epoll on Linux, kqueue on BSD) which file descriptors are ready for I/O, then process the readable/writable events, advance state machines, and loop again. No threads, no blocking. The worker spends essentially no time waiting — it only works when there's work to do. Because each worker is single-threaded, there's no locking contention; the typical deployment runs one worker per CPU core, each handling thousands of connections independently.

The architecture is organized around modular handlers, filters, and upstream modules. Handlers produce responses (from disk, proxy, FastCGI, etc.), filters transform them (gzip, SSI, headers), and upstreams manage connections to backend servers. Memory management is arena-based: nginx allocates from per-request or per-connection memory pools and frees them all at once when the connection closes, avoiding malloc/free overhead and fragmentation. This chapter from AOSA (written by Andrew Alexeev) is one of the best documented case studies in how a constrained design goal — maximum connections per byte of RAM — forces architectural clarity.

## Key points

- nginx uses a non-blocking I/O event loop (epoll/kqueue) per worker, not threads per connection — the key departure from the Apache HTTP Server model.
- One worker process per CPU core; the OS handles distribution of accepted connections. No locking needed within a worker.
- Memory pools per connection/request: all allocations freed in bulk at teardown — avoids fragmentation and call overhead.
- Modular pipeline: handlers generate content, filters transform it, upstream modules proxy to backends — composable and predictable.
- The C10K problem drove this design: Apache's thread-per-connection model hits OS limits around 10K concurrent connections; nginx's model scales to 100K+.
- The AOSA book makes this chapter publicly available as a case study in designing for a specific performance constraint from first principles.

[Original](http://www.aosabook.org/en/nginx.html)
