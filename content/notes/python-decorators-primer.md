---
title: "Python Decorators: A Primer"
date: 2012-04-12
categories:
  - python
  - decorators
  - metaprogramming
  - functional-programming
description: A practical explainer on Python decorators — the @syntax wrapper pattern that lets you modify or extend function behavior without changing the function itself. A key Python metaprogramming tool used for logging, auth, caching, and more.
params:
  source: pinboard
  sourceUrl: http://www.thumbtack.com/engineering/a-primer-on-python-decorators/
---

![Python Decorators: A Primer](/images/notes/python-decorators-primer.png)

## Summary

Python decorators are a metaprogramming pattern that lets you wrap a function or class with additional behavior using the `@` syntax. A decorator is itself a function (or class) that takes a callable as input and returns a modified callable. The `@decorator` syntax is just syntactic sugar for `function = decorator(function)`.

The key insight is that in Python, functions are first-class objects — you can pass them as arguments, return them from other functions, and assign them to variables. Decorators exploit this: they intercept a function at definition time, apply some transformation, and substitute the result. This lets you add logging, authentication, caching, rate limiting, or any cross-cutting concern to a function without modifying its body.

Flask, Django, and FastAPI all make heavy use of decorators — `@app.route('/path')` in Flask is a decorator that registers a view function with the router. functools.wraps is the standard tool for preserving the original function's metadata (name, docstring) when writing your own decorators.

## Key points

- A decorator takes a function and returns a new function — `@d` before `def f()` is equivalent to `f = d(f)`.
- Inner functions (`wrapper`) give the decorator access to the original function's arguments via `*args, **kwargs`.
- `functools.wraps(func)` preserves `__name__`, `__doc__`, etc. — always use it when writing decorators.
- Common uses: logging, timing, caching (`@functools.lru_cache`), access control, input validation.
- Class-based decorators (with `__call__`) are useful when the decorator needs state.
- Web frameworks (Flask, Django) use decorators for routing, middleware, and permission checks.

[Original](http://www.thumbtack.com/engineering/a-primer-on-python-decorators/)
