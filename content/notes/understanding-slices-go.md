---
title: Understanding Slices in Go Programming
date: 2013-08-19
categories:
  - go
  - programming
  - data-structures
  - memory
  - golang
description: Going Go Programming's deep explanation of slices in Go — the difference between arrays and slices, the three-field slice header, and the subtle bugs that emerge from sharing underlying arrays. Essential reading for anyone moving from C or Python to Go.
params:
  source: pinboard
  sourceUrl: http://www.goinggo.net/2013/08/understanding-slices-in-go-programming.html
---

![Understanding Slices in Go Programming](/images/notes/understanding-slices-go.png)

## Summary

This post from Going Go Programming by William Kennedy is a thorough explanation of how slices work in Go — the distinction between arrays and slices, the internal slice header (pointer, length, capacity), and the gotchas that trip up programmers coming from languages without this abstraction. Understanding slices is foundational to writing correct Go code, and the bugs they introduce are subtle enough that even experienced programmers hit them.

In Go, an array has a fixed size that's part of its type: `[3]int` and `[5]int` are different types. A slice is a view into an underlying array — a three-field struct containing a pointer to the first element, a length, and a capacity. When you append to a slice and it exceeds capacity, Go allocates a new backing array and copies. When it doesn't exceed capacity, the append mutates the existing backing array — which can cause surprising aliasing behavior if multiple slices share the same underlying array.

The shared-backing-array behavior is the primary source of slice bugs: taking a sub-slice (`s[1:3]`) gives you a new slice header pointing into the same memory. Appending to the sub-slice can silently overwrite data that the original slice still holds a reference to. The canonical fix is using three-index slices (`s[1:3:3]`) to set capacity equal to length, forcing a new allocation on the first append.

## Key points

- Slice header: three fields — pointer to underlying array, length, capacity — not the data itself.
- Append semantics: if `len < cap`, append modifies the existing array in place; if `len == cap`, Go allocates a new array. Sharing backing arrays across slices causes aliasing.
- Three-index slices `s[i:j:k]`: set capacity explicitly to prevent sub-slices from sharing capacity with the parent — defensive pattern for functions receiving slices.
- `copy()` vs. append: use `copy()` when you explicitly want a new backing array with no shared state.
- Go's slice design trades simplicity (no separate list type) for subtlety (pointer semantics hidden behind value-like syntax).
- 2013 context: Go was gaining adoption in systems programming and infrastructure (Docker would release in 2013) — understanding memory semantics was critical.

[Original](http://www.goinggo.net/2013/08/understanding-slices-in-go-programming.html)
