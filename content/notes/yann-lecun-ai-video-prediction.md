---
title: "Yann LeCun: Making Facebook's AI Predict What Happens in Videos"
date: 2015-11-10
categories:
  - deep-learning
  - ai
  - computer-vision
  - video-understanding
  - research
description: New Scientist interview with Yann LeCun on Facebook AI Research's goal to build models that predict what will happen in videos — covering what AI can and can't do in 2015, and LeCun's view on unsupervised learning as the key unsolved problem.
params:
  source: pinboard
  sourceUrl: https://www.newscientist.com/article/dn28456-im-going-to-make-facebooks-ai-predict-what-happen-in-videos/
---

![Yann LeCun: Making Facebook's AI Predict What Happens in Videos](/images/notes/yann-lecun-ai-video-prediction.png)

## Summary

This New Scientist interview with Yann LeCun, director of Facebook AI Research (FAIR), covers his research priorities in late 2015 and his characteristically blunt view of what AI can and can't do. The headline goal was video prediction: building models that understand video sequences well enough to predict the next frames — a proxy for world understanding that goes far beyond pattern recognition on static images.

LeCun's framing is notable: he saw video prediction as a forcing function for unsupervised learning, which he considered the major unsolved problem in AI at the time. Supervised learning — training on labeled examples — had powered the deep learning revolution in image recognition and speech, but it requires enormous labeled datasets. Video contains rich structure and temporal relationships that don't require human annotation — a cat moving across the screen is self-supervised. Building models that can predict this structure would require learning genuine world models.

The interview also captures LeCun's views on the limits of deep learning: good at perception (vision, speech), not good at reasoning, planning, or common sense. These limitations remain relevant a decade later. The 2015 context: Facebook had just invested heavily in AI research, ImageNet models were achieving near-human accuracy on classification, but video understanding and temporal reasoning remained wide open problems.

## Key points

- Yann LeCun's 2015 research priority: video prediction as a path to unsupervised learning at scale.
- Video provides implicit temporal supervision — the model must learn world structure without labels.
- LeCun's honest assessment: deep learning is strong at perception, weak at reasoning and planning.
- Unsupervised learning identified as the key unsolved problem — still largely true a decade later.
- Facebook AI Research (FAIR) launched in 2013 with LeCun as director — this interview is near its early peak.

[Original](https://www.newscientist.com/article/dn28456-im-going-to-make-facebooks-ai-predict-what-happen-in-videos/)
