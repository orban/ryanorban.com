---
title: "Solving Google Treasure Hunt Puzzle 4: Prime Numbers"
date: 2013-06-18
categories:
  - algorithms
  - prime-numbers
  - unix
  - problem-solving
  - competitive-programming
description: Peteris Krumins' solution to Google Treasure Hunt Puzzle 4 — find the smallest prime expressible as the sum of 7, 17, 41, and 541 consecutive primes simultaneously — solved pragmatically by downloading a pre-computed prime dataset and using Unix pipes instead of writing a sieve.
params:
  source: pinboard
  sourceUrl: http://www.catonmat.net/blog/solving-google-treasure-hunt-prime-number-problem-four/
---

![Solving Google Treasure Hunt Puzzle 4: Prime Numbers](/images/notes/google-treasure-hunt-prime-numbers.png)

## Summary

Peteris Krumins (catonmat.net) solved Google Treasure Hunt Puzzle 4 — find the smallest number that is simultaneously: the sum of 7 consecutive primes, the sum of 17 consecutive primes, the sum of 41 consecutive primes, the sum of 541 consecutive primes, and is itself prime. The answer is 7,830,239.

The solution method is the interesting part. Rather than implementing a Sieve of Eratosthenes or Miller-Rabin primality test from scratch, Krumins downloaded a pre-computed dataset of the first 50 million primes from a public source, then used Unix command-line tools to solve the problem: AWK scripts to compute rolling sums of consecutive primes for each window size, then `sort`, `uniq`, and `grep` to find the intersection across all four window sizes. The blog title — good coders code, great reuse — captures the philosophy exactly.

The approach works because the prime generation problem is solved (the dataset exists), the rolling sum computation is a straightforward AWK script, and the set intersection of four sorted lists is exactly what Unix sort+uniq+join pipelines do efficiently. Writing a full prime-sieve solution in Python or C++ would have taken longer and taught nothing new. This is the pragmatic engineer's mindset: the right tool for each sub-problem, composed via pipelines.

## Key points

- **Dataset reuse**: downloading pre-computed primes instead of generating them — the generation problem is solved, why solve it again?
- AWK for rolling sums: the stream-processing model of AWK maps naturally to "slide a window over a sequence and emit the sum" — no array needed, just running totals
- **Set intersection via Unix pipeline**: `sort | uniq -d` across multiple files finds common elements — a declarative approach that scales with the dataset size
- The problem structure (intersection of multiple constraints) maps naturally to pipeline composition — each constraint generates a sorted list, intersection finds candidates
- **Competitive programming insight**: decompose the problem into well-defined sub-problems, then find existing tools/data that solve each sub-problem — custom code only where necessary
- Related algorithmic content: prime sieves, Miller-Rabin, AKS primality test — the pure math version vs. the pragmatic reuse version

[Original](http://www.catonmat.net/blog/solving-google-treasure-hunt-prime-number-problem-four/)
