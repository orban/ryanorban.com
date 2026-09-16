---
title: The True Power of Regular Expressions
date: 2013-05-27
categories:
  - regular-expressions
  - theory
  - computer-science
  - automata
  - algorithms
description: Nikita Popov's deep dive into what regular expressions can theoretically do — connecting regex to finite automata and formal language theory. Goes beyond syntax tutorials to explain why backtracking regex engines can be exponentially slow, and how to avoid it.
params:
  source: pinboard
  sourceUrl: http://nikic.github.io/2012/06/15/The-true-power-of-regular-expressions.html
---

![The True Power of Regular Expressions](/images/notes/true-power-of-regular-expressions.png)

## Summary

Nikita Popov (nikic) wrote a post connecting practical regular expressions to the underlying formal language theory — specifically finite automata and the Chomsky hierarchy. The post explains that a "true" regular expression (in the automata theory sense) can be compiled to a deterministic finite automaton (DFA) that matches in O(n) time with no backtracking. The catch: most regex engines in the wild (Perl, PCRE, Python's `re`) use backtracking NFA engines that are vulnerable to catastrophic backtracking.

The core issue: features like backreferences (`\1`) push beyond the regular language boundary into context-sensitive territory. An engine implementing backreferences can't use a DFA and must backtrack, which in the worst case is exponential in input length. This is the root cause of ReDoS (Regular Expression Denial of Service) attacks — a carefully crafted input triggers worst-case backtracking in a vulnerable regex.

The alternative is Thompson NFA construction (used by RE2, Go's regexp package, ripgrep) which guarantees O(n × m) time where n is input length and m is pattern length, at the cost of not supporting backreferences. For most practical regex use cases, this trade-off is excellent — you get guaranteed linear time and real DDoS safety.

## Key points

- "Regular" in regex theory means recognizable by a finite automaton — a much smaller class than what PCRE actually implements
- Thompson NFA → subset construction → DFA: O(n) matching, no backtracking, exponential state space only for automaton (not matching)
- Backtracking NFA engines (Perl, Python, JavaScript): support backreferences and lookahead but can run in exponential time
- ReDoS: exploiting catastrophic backtracking to DoS services — patterns like `(a+)+b` on input `aaa...aaa`
- RE2 (Google), Rust regex crate, Go `regexp`: linear-time guarantee, no backreferences
- The "regular" in regular expression refers to Chomsky Type 3 languages, not to sensible or well-designed

[Original](http://nikic.github.io/2012/06/15/The-true-power-of-regular-expressions.html) → GitHub
