---
title: Python Quirks
date: 2013-07-12
categories:
  - python
  - gotchas
  - programming
  - language-design
description: LShift's catalog of Python behaviors that surprise experienced programmers — mutable default arguments, late-binding closures, class variable vs instance variable traps. The kind of language-design decisions that seem reasonable in isolation but bite you in real code.
params:
  source: pinboard
  sourceUrl: http://www.lshift.net/blog/2009/10/29/python-quirks
---

![Python Quirks](/images/notes/python-quirks.png)

## Summary

This LShift post cataloged subtle Python behaviors that surprised even experienced programmers — not bugs, but design decisions that have non-obvious consequences. The most famous: mutable default arguments. In Python, default argument values are evaluated once when the function is defined, not on each call. A function with `def f(x=[])` will share the same list across all calls — mutating it in one call affects the next.

The post also covers late-binding closures (variables in closures are looked up at call time, not when the function is defined), the difference between class variables and instance variables (a class variable that's a mutable object is shared across all instances until reassigned on a specific instance), and integer interning (small integers are cached and identity-compared, which means `a is b` is True for small integers but False for large ones).

These quirks are features, not bugs — they follow consistently from Python's object model and scoping rules — but they require explicit learning because they violate intuitions built from other languages. A programmer coming from Java or C++ would write `def f(x=[])` intending fresh list each call and get surprising results.

## Key points

- Mutable default arguments: `def f(x=[])` shares one list across all calls — use `def f(x=None): if x is None: x = []` as the idiomatic fix.
- Late-binding closures: `lambda: i` in a loop captures a reference to `i`, not the value of `i` at lambda creation — all lambdas in the loop return the same final value.
- Class variable vs instance variable: assigning to a class-level mutable (list or dict) creates a shared object; reassignment on `self` creates an instance-level shadow.
- Integer interning: CPython caches integers from -5 to 256; `x is y` is unreliable for identity checks on integers — use `==` instead.
- These quirks influenced Python 3's design in some cases, but most were preserved for backward compatibility.

[Original](http://www.lshift.net/blog/2009/10/29/python-quirks)
