---
title: "Simpson's Paradox: Interactive Visualization"
date: 2013-09-19
categories:
  - statistics
  - simpsons-paradox
  - data-visualization
  - confounding
  - causality
description: VUDLab's interactive visualization of Simpson's Paradox — showing how a trend that appears in every subgroup can reverse when the groups are combined. A crucial statistical phenomenon for anyone working with observational data.
params:
  source: pinboard
  sourceUrl: http://vudlab.com/simpsons/
---

![Simpson's Paradox: Interactive Visualization](/images/notes/simpsons-paradox-visualization.png)

## Summary

Simpson's Paradox is the phenomenon where a trend present in every subgroup of a dataset reverses or disappears when the groups are combined. The classic example: a medical treatment appears beneficial in both men and women separately, but harmful when you look at the combined population — because the groups have very different baseline rates and the treatment was applied more often to the sicker group.

VUDLab's interactive visualization made this concrete and manipulable — you could see the paradox appear and understand intuitively what was happening rather than just being told about it. For students at Zipfian Academy learning statistics and causal inference, this was a vivid illustration of why aggregation can deceive and why understanding data collection and grouping is essential before interpreting results.

Simpson's Paradox is a specific case of confounding: a lurking third variable (group membership) mediates the relationship between treatment and outcome. The paradox is resolved by controlling for the confounder — but recognizing that you need to control for it requires understanding the data generating process, not just the data itself. This connects to broader debates about observational data and the limits of data analysis without causal models.

## Key points

- Simpson's Paradox: a trend in all subgroups can reverse in the combined population — one of the most important statistical illusions.
- The cause is confounding: a third variable (group assignment) is correlated with both treatment and outcome.
- Resolution requires understanding the data generating process — which group variable to condition on isn't determined by the data alone.
- Famous examples: Berkeley admissions bias case (1973), kidney stone treatment effectiveness, batting averages.
- Connects to causal inference: Simpson's Paradox is why let the data speak is insufficient — you need a causal model to know which aggregation is correct.

[Original](http://vudlab.com/simpsons/)
