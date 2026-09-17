---
title: I Analyzed the Chords to 1,300 Songs for Patterns
date: 2013-03-14
categories:
  - music-theory
  - data-analysis
  - chord-progressions
  - hooktheory
  - patterns
description: Hooktheory's analysis of chord progression patterns across 1,300 pop songs — using crowdsourced music theory data to find statistical regularities in harmony. A rare example of quantitative musicology producing genuinely surprising findings about song structure.
params:
  source: pinboard
  sourceUrl: http://www.hooktheory.com/blog/chord-progression-search-patterns-and-trends/
---

## Summary

Hooktheory built a web application where musicians crowdsourced the chord progressions and melody for thousands of pop songs using a relative key notation (scale degrees rather than absolute pitches). After accumulating 1,300+ annotated songs, they ran a statistical analysis over the dataset — essentially treating music theory questions as data mining problems. The result was a rare piece of quantitative musicology that produced findings graspable by both musicians and data enthusiasts.

The core methodology: represent each chord as its Roman numeral analysis (I, IV, V, vi, etc.) and build a transition matrix of chord-to-chord probabilities. From this you can answer questions like "given a I chord, what chord is most likely to follow? or what are the most common two-chord and four-chord loops in pop?" The analysis confirmed folk wisdom about diatonic harmony (I–V–vi–IV dominates pop) while also surfacing non-obvious patterns in how songs structure their verse, chorus, and bridge sections.

The finding that resonated most widely: the IV–I–V–vi (Let It Be progression) and I–V–vi–IV (Don't Stop Believin') aren't just common — they account for a striking fraction of all four-chord progressions across genres. This had already been made famous by the Axis of Awesome's 4 Chord Song medley, but Hooktheory quantified it. The interactive chord progression search tool made the database genuinely explorable — you could type in a progression and find every song that used it.

## Key points

- Roman numeral analysis as data representation: chords as scale-degree relationships, not absolute pitches — allows comparison across songs in different keys
- Transition matrix approach: chord-to-chord probability is a Markov chain over harmonic space — this framing has been applied in music generation systems since
- I–V–vi–IV (or rotations) accounts for a disproportionate fraction of four-chord pop progressions — confirmed the Axis of Awesome observation quantitatively
- The vi chord (minor sixth degree) is the most harmonically interesting: it creates the emotional contrast in countless songs because it's the relative minor of the tonic
- Hooktheory's dataset later grew into the Hooktheory Trends product and informed TheoryTab — a searchable database of transcribed songs still in use as a music theory teaching tool
- Methodological note: crowdsourced data in relative notation introduces biases (English-language pop overrepresented, expert transcribers overrepresented) that affect conclusions about genre-level patterns

[Original](http://www.hooktheory.com/blog/chord-progression-search-patterns-and-trends/)
