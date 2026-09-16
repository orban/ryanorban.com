---
title: "MIT 6.033: Computer System Engineering"
date: 2021-01-16
categories:
  - computer-science
  - distributed-systems
  - operating-systems
  - education
  - mit
description: MIT 6.033 Computer System Engineering covers the design of large, complex software systems — reliability, fault tolerance, operating systems, networking, and distributed systems. One of MIT's most comprehensive systems courses, available free via OpenCourseWare.
params:
  source: pinboard
  sourceUrl: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-033-computer-system-engineering-spring-2018/
---

## Summary

MIT 6.033 Computer System Engineering is one of MIT's foundational systems courses, covering how to design reliable, large-scale software systems. The curriculum spans operating system principles (processes, virtual memory, file systems), networking (routing, TCP/IP, DNS), distributed systems (two-phase commit, Paxos, Raft), security, and fault tolerance. The readings include both classic papers and the textbook Principles of Computer System Design by Saltzer and Kaashoek.

What distinguishes 6.033 from narrower courses is its scope: it treats "system" as a unified concept rather than splitting into separate OS, networks, and distributed systems courses. The unifying theme is managing complexity — how to build systems that remain correct and reliable as they scale in size and team size. The concepts of modularity, naming, abstraction, and layering appear throughout as recurring design tools.

The course's influence is visible in how MIT graduates think about system design. The end-to-end argument (Saltzer, Reed, Clark 1984) taught in 6.033 continues to shape decisions about where to implement functionality in networked systems. The fault tolerance material — retry semantics, idempotency, write-ahead logging — is directly applicable to any distributed system in production.

## Key points

- Covers OS, networking, distributed systems, and security in a unified systems engineering framework.
- Core reading: Principles of Computer System Design by Saltzer and Kaashoek, plus seminal papers on Paxos, two-phase commit, DNS.
- The end-to-end argument is a central paper — defines where functionality belongs in a layered system.
- Free via MIT OpenCourseWare with lecture notes, problem sets, and readings.
- Companion to CS231n (ML) and [Stanford CS149](/notes/stanford-cs149/) (parallel computing) for a complete systems education.

[Original](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-033-computer-system-engineering-spring-2018/)
