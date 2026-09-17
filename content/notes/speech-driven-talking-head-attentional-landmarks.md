---
title: Speech Driven Talking Head Generation via Attentional Landmarks Based Representation
date: 2021-11-09
categories:
  - talking-head
  - speech-synthesis
  - computer-vision
  - deep-learning
  - video-generation
description: This paper introduces an attentional landmark-based representation for generating realistic talking head video from speech audio, using facial landmarks as a compact intermediate representation that bridges audio and visual domains. The approach decouples appearance generation from motion modeling, improving generalization across identities.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/ Speech Driven Talking Head Generation via Attentional Landmarks Based Representation.pdf
---

## Summary

This paper presents a method for driving a still portrait image to produce a talking head video synchronized with an input speech signal. The central innovation is using facial landmarks — a sparse set of 2D/3D keypoints describing the positions of eyes, nose, mouth, and jaw — as an intermediate representation that sits between the audio domain and the pixel domain. By first predicting how landmarks move given the speech audio, then rendering pixels from the landmark motion, the method separates the *what moves* problem (solved by audio-to-landmark prediction) from the *how it looks* problem (solved by landmark-to-pixel synthesis).

The attentional mechanism is key to quality: not all facial regions are equally relevant to speech at any given moment. During vowels, the mouth opening is the dominant cue; during consonants, specific tongue and lip positions matter more. A cross-modal attention module learns to weight landmark influence dynamically based on the audio context. This allows the generated motion to be both speech-synchronized and identity-preserving — the model learns to move landmarks in ways consistent with both the audio signal and the subject's characteristic expression range.

The synthesis stage takes the predicted landmark sequence and a single reference frame (the portrait) and generates temporally coherent video frames. This typically involves a generative adversarial network conditioned on both the reference image and the current landmark positions. The GAN discriminator enforces both per-frame realism and temporal consistency. The landmark bottleneck provides structural interpretability that purely end-to-end audio-to-video approaches lack, and it enables cross-identity driving: landmarks predicted from one person's speech can animate a different person's portrait.

## Key points

- Landmark-based intermediate representation: audio → facial landmark motion → pixel synthesis; separates motion modeling from appearance synthesis.
- Cross-modal attention weights landmark regions by their relevance to the current audio context (mouth for vowels, lips for consonants).
- Identity-preserving: landmark motion is constrained to be consistent with the reference portrait's characteristic expression range.
- Cross-identity driving: landmarks from one person's audio can animate a different person's portrait.
- GAN-based synthesis conditioned on reference frame + predicted landmark positions; discriminator enforces temporal consistency.
- Part of a family of methods including First Order Motion Model and SadTalker that use structural intermediates for video-driven synthesis.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/%20Speech%20Driven%20Talking%20Head%20Generation%20via%20Attentional%20Landmarks%20Based%20Representation.pdf)
