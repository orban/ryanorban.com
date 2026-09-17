---
title: The 5-Minute Guide to C Pointers
date: 2012-08-16
categories:
  - c
  - programming
  - memory
  - systems-programming
  - learning
description: A concise primer on C pointers — the concept that trips up most programmers learning C. The guide covers pointer declaration, dereferencing, pointer arithmetic, and common pitfalls, aimed at getting past the initial confusion quickly.
params:
  source: pinboard
  sourceUrl: http://denniskubes.com/2012/08/16/the-5-minute-guide-to-c-pointers/
---

## Summary

A concise tutorial on C pointers aimed at programmers who understand the concept abstractly but struggle with the syntax and mental model. C pointers are the mechanism by which C programs work directly with memory addresses — every pointer is a variable that holds the address of another variable, rather than the value itself. The guide walked through declaration, dereferencing, and pointer arithmetic in accessible terms.

The reason C pointers remain conceptually difficult is that they require holding two levels of indirection in mind simultaneously: the pointer variable (which has its own address) and the value it points to (which lives at a different address). The `*` operator means different things in declaration (`int *p` — p is a pointer to int) versus in expression (`*p` — dereference p to get the int). The `&` operator gets the address of a variable. Mixing these up is the source of most C memory bugs.

Pointer arithmetic in C is what makes the language both powerful and dangerous: adding 1 to an `int *` advances by `sizeof(int)` bytes, not 1 byte. This is what makes arrays and pointer interchangeable in C — `arr[i]` is syntactic sugar for `*(arr + i)`. Combined with manual memory management (malloc/free), pointers are the root of buffer overflows, use-after-free, and null pointer dereferences — the class of bugs that Rust and memory-safe languages were designed to eliminate.

## Key points

- A C pointer holds a memory address; `*ptr` dereferences it to get the value at that address.
- `*` in declaration means pointer to; `*` in expressions means dereference.
- `&var` gets the memory address of a variable — the value a pointer would store.
- Pointer arithmetic: `ptr + 1` advances by `sizeof(*ptr)` bytes, making arrays and pointers equivalent.
- Source of buffer overflow, use-after-free, and null pointer dereference bugs in C/C++ codebases.
- Rust's ownership + borrow checker eliminates pointer bugs at compile time by making invalid pointer states unrepresentable.

[Original](http://denniskubes.com/2012/08/16/the-5-minute-guide-to-c-pointers/)
