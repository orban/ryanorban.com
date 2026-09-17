---
title: Ruby GC Internals
date: 2012-08-04
categories:
  - ruby
  - garbage-collection
  - internals
  - performance
  - memory
description: A guide to Ruby's garbage collector internals from 2012, covering the mark-and-sweep algorithm and the stop-the-world pauses that made Ruby 1.9's GC a known performance bottleneck. Ruby 2.0 and 2.1 later introduced generational and incremental GC to address these issues.
params:
  source: pinboard
  sourceUrl: http://furious-waterfall-55.heroku.com/ruby-guide/internals/gc.html
---

## Summary

A guide to Ruby's garbage collector internals from 2012, when Ruby 1.9.x was the dominant production version and the GC was a known weak point in the runtime's performance profile. Ruby 1.9 used a mark-and-sweep garbage collector with stop-the-world pauses — the entire application execution halted while the GC marked live objects and swept dead ones. For web applications with latency-sensitive requests, these pauses were visible and disruptive.

The mark-and-sweep algorithm works in two phases: the mark phase traverses the object graph starting from roots (global variables, stack frames, etc.) and marks all reachable objects; the sweep phase then iterates through all allocated objects and frees the unmarked ones. The stop-the-world requirement comes from the need for a consistent view of the object graph during traversal — concurrent mutation would cause the GC to miss live objects or incorrectly identify objects as garbage.

Ruby 1.9's GC also had a fixed heap size that could cause frequent GC cycles when heap pressure was high (many short-lived objects), and growing the heap was expensive. The ecosystem had workarounds: tweaking `RUBY_GC_HEAP_INIT_SLOTS`, `RUBY_GC_MALLOC_LIMIT`, and other environment variables. Ruby 2.0 (released 2013) introduced bitmap marking (reducing copy-on-write pressure). Ruby 2.1 introduced generational GC (RGenGC), dramatically reducing pause times by noting that most objects die young. Ruby 3.x added the Ractors model for concurrency. The GC evolution in Ruby mirrors the trajectory of JVM GC improvements a decade earlier.

## Key points

- Ruby 1.9 used mark-and-sweep with stop-the-world pauses — the entire app halted during GC.
- Mark phase: traverse object graph from roots, mark all reachable objects.
- Sweep phase: free all unmarked objects.
- Fixed heap size caused frequent GC under heap pressure; tuning via `RUBY_GC_HEAP_INIT_SLOTS` etc.
- Ruby 2.1 introduced generational GC (RGenGC): most objects die young, so minor GCs are cheap.
- Bitmap marking in Ruby 2.0 reduced copy-on-write pressure in forked processes (key for Unicorn/Passenger).

[Original](http://furious-waterfall-55.heroku.com/ruby-guide/internals/gc.html)
