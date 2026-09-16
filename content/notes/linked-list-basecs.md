---
title: What's a Linked List, Anyway? (BaseCS)
date: 2022-03-11
categories:
  - computer-science
  - data-structures
  - education
  - algorithms
  - programming
description: The first part of Vaidehi Joshi's BaseCS series on linked lists — a beginner-friendly explanation of singly and doubly linked lists with illustrations. Part of a comprehensive CS fundamentals series written for self-taught developers.
params:
  source: pinboard
  sourceUrl: https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d
---

## Summary

Part 1 of Vaidehi Joshi's BaseCS series on linked lists, published on Medium. BaseCS is a year-long writing project covering computer science fundamentals — data structures, algorithms, operating system concepts, networking — written accessibly for self-taught developers and people who came to programming without a CS degree. Joshi published one post per week, covering the curriculum she wished she'd had when teaching herself to code.

A linked list is a sequence of nodes where each node holds data and a reference (pointer) to the next node in the sequence. Unlike an array, a linked list doesn't require contiguous memory allocation — nodes can be anywhere in memory, connected by pointers. This gives linked lists efficient insertion and deletion (just update a pointer) but slow random access (you must traverse from the head to reach element N).

The BaseCS approach to explaining this is illustration-heavy and analogy-driven: Joshi uses everyday objects to make the pointer concept concrete before introducing any code. The writing is designed to be read, not just scanned — which distinguishes it from reference documentation that assumes you already understand what you're looking for.

The BaseCS series as a whole became influential in the self-taught developer community, partly because it demonstrates that deep technical knowledge can be explained without either dumbing down or requiring prerequisites. It was later turned into a podcast with Saron Yitbarek of CodeNewbie.

## Key points

- Linked list vs. array: linked lists sacrifice O(1) random access for O(1) insertion/deletion and non-contiguous memory.
- Singly linked list (pointer to next only) vs. doubly linked list (pointer to next and previous).
- BaseCS series is a year of CS fundamentals for self-taught developers — this is one entry in a comprehensive curriculum.
- Illustration-first approach: visual analogies before code, making pointer concepts concrete.
- By Vaidehi Joshi — later a staff engineer at Forem (DEV Community); the series built her reputation in tech education.

[Original](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)
