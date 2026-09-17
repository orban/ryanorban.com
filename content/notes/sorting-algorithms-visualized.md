---
title: Sorting Algorithms Are Mesmerizing When Visualized
date: 2013-08-06
categories:
  - algorithms
  - visualization
  - sorting
  - computer-science
  - education
description: Gizmodo's coverage of a visualization showing 15 different sorting algorithms in motion — the classic side-by-side comparison of bubble sort, quicksort, merge sort, and others that makes their behavioral differences viscerally apparent. A perennial teaching tool.
params:
  source: pinboard
  sourceUrl: http://gizmodo.com/this-visualization-of-15-different-sorting-algorithms-i-987297677
---

![Sorting Algorithms Are Mesmerizing When Visualized](/images/notes/sorting-algorithms-visualized.png)

## Summary

This Gizmodo piece covered a video visualization showing 15 different sorting algorithms operating simultaneously on the same array — bubble sort, selection sort, insertion sort, shell sort, merge sort, quicksort, heapsort, radix sort, and others. The visual representation — typically bars of varying height being rearranged — makes the behavioral differences between algorithms immediately apparent in ways that pseudocode and Big O notation don't convey.

Sorting algorithms are a standard computer science curriculum topic, but they're often taught through complexity analysis (bubble sort is O(n²), quicksort O(n log n) average) without conveying what that means in practice. Visualizations fill the gap: watching bubble sort laboriously swap adjacent elements while quicksort recursively partitions makes the performance intuition concrete. The particularly striking visual is merge sort's divide-and-conquer structure — the recursive halving pattern is beautiful in motion.

The algorithms visualized genre has a long history as an educational tool, going back to Robert Sedgewick's algorithm animations in the 1990s. What made this particular video spread in 2013 was partly the visual quality and partly the era — algorithmic thinking was newly fashionable alongside the data science boom, and this gave non-practitioners a visceral sense of what algorithms do.

## Key points

- Bubble sort O(n²): makes n passes, each bubbling the largest element to the end — visually obvious why it's slow; each pass moves one element into place.
- Quicksort O(n log n) average: pivot selection and partitioning — the recursive structure is visible as the array gets divided into increasingly sorted sub-sections.
- Merge sort O(n log n) guaranteed: divide-and-conquer without the worst-case risk of quicksort's degenerate O(n²) behavior on sorted inputs.
- Radix sort O(n·k): non-comparison sort — sorts by digit position; the visual looks completely different from comparison sorts because it ignores value ordering within passes.
- Educational value: visualization makes O(n²) vs. O(n log n) intuitive without mathematical notation — the n² algorithms visually thrash while log-linear ones converge fast.
- Connected to algorithm animation as pedagogy: tools like VisuAlgo and AlgoViz extended this into interactive form.

[Original](http://gizmodo.com/this-visualization-of-15-different-sorting-algorithms-i-987297677)
