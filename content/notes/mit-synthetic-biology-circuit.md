---
title: MIT Team Builds Most Complex Synthetic Biology Circuit
date: 2012-10-10
categories:
  - synthetic-biology
  - bioengineering
  - genetic-circuits
  - mit
  - science
description: Christopher Voigt's MIT team built the most complex synthetic genetic circuit to date — integrating four molecular sensors that can simultaneously monitor glucose, pH, temperature, and solute concentration. The breakthrough was eliminating crosstalk between biological components that had previously limited circuit complexity.
params:
  source: pinboard
  sourceUrl: http://web.mit.edu/newsoffice/2012/complex-biological-circuit-1007.html
---

![MIT Team Builds Most Complex Synthetic Biology Circuit](/images/notes/mit-synthetic-biology-circuit.png)

## Summary

Christopher Voigt's lab at MIT published a landmark result in synthetic biology in 2012: a genetic circuit that integrates four different molecular sensors simultaneously, making it the most complex synthetic biological circuit built at that point. The circuit can detect glucose, pH, temperature, and solute concentration in parallel — a combination that provides environmental specificity impossible to achieve with any single sensor.

The key engineering challenge in synthetic biology before this work was crosstalk: biological components inside a cell interfere with each other, limiting how many independent logic elements could coexist. Voigt's team addressed this through two approaches. First, they mined 60 variants of a regulatory pathway from *Salmonella* and other bacteria, identifying versions that naturally didn't interfere. Second, they applied directed evolution — mutating genes to produce thousands of variants, then screening for those that performed without crosstalk. This combination of combinatorial search and evolutionary pressure is how they achieved orthogonality between parts.

The result is a layered design where inputs and outputs could mesh together, allowing circuits to stack. Voigt noted that before this work, synthetic biologists "were just repackaging the same circuits over and over again" — the field was stuck reusing a small parts library because adding new components caused interference. This breakthrough opened the door to genuinely complex multicondition sensing, with applications in programming yeast for industrial fermentation monitoring and eventually in biocomputing more broadly.

## Key points

- Genetic circuit with four integrated sensors — a complexity level previously blocked by crosstalk between biological components inside cells.
- Component mining from 60 regulatory pathway variants in *Salmonella* to find naturally orthogonal parts — a combinatorial approach before any optimization.
- Directed evolution used to eliminate remaining crosstalk: mutating gene variants and screening thousands of candidates for non-interfering behavior.
- Layered design philosophy: circuits stacked by ensuring outputs of one layer are valid inputs to the next — borrowed from digital logic and applied to biology.
- Applications in industrial fermentation sensing — programming microorganisms to self-monitor complex environmental states.

[Original](http://web.mit.edu/newsoffice/2012/complex-biological-circuit-1007.html)
