---
title: Inverse FizzBuzz
date: 2012-05-06
categories:
  - programming
  - puzzles
  - interviews
  - hacker-news
description: "Hacker News discussion of Inverse FizzBuzz: given output like 'fizz buzz fizzbuzz fizz', figure out the smallest integer range that produces it. A clever inversion of the classic coding interview problem that tests parsing/reasoning rather than just implementation."
params:
  source: pinboard
  sourceUrl: http://news.ycombinator.com/item?id=3929308
---

## Summary

Hacker News thread discussing [Inverse FizzBuzz](/notes/inverse-fizzbuzz/) — a reversal of the classic FizzBuzz interview problem. Standard FizzBuzz: given a range of integers, output Fizz for multiples of 3, Buzz for multiples of 5, and FizzBuzz for multiples of both. Inverse FizzBuzz: given a sequence of FizzBuzz output (like buzz fizz fizzbuzz fizz buzz), find the smallest integer range that would produce it.

The problem is significantly harder than FizzBuzz and tests different skills. FizzBuzz checks whether someone can translate a simple rule to code. Inverse FizzBuzz requires reverse-engineering constraints from output — you have to determine the starting integer, the length of the sequence, and verify that the pattern is consistent with the FizzBuzz rules. It requires understanding of modular arithmetic, constraint satisfaction, and careful case analysis.

The original post was by Tom Moertel, who argued that Inverse FizzBuzz is a better interview question than FizzBuzz because it screens for reasoning ability and code correctness more rigorously. A candidate who can correctly solve Inverse FizzBuzz (handling edge cases like the sequence starting at 1, ambiguous starting positions, and invalid inputs) is demonstrating substantially more than someone who can write FizzBuzz. The HN discussion explored both solutions and broader arguments about what coding interview problems actually measure.

## Key points

- Standard FizzBuzz: integers → {Fizz/Buzz/FizzBuzz/number}. Inverse: sequence of output → smallest valid integer range.
- Harder because it requires constraint inference, not just rule application — tests reasoning under uncertainty.
- Edge cases: multiple valid starting positions, sequences starting at 1, invalid inputs that no integer range produces.
- Tom Moertel's framing: a better coding interview signal because it requires demonstrating understanding, not just implementation.
- FizzBuzz itself became a test because many candidates couldn't implement it — the bar is low, inverse raises it.

[Original](http://news.ycombinator.com/item?id=3929308)
