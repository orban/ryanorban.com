---
title: Deep Anomaly Detection with Self-Supervised Learning and Adversarial Training
date: 2022-08-23
categories:
  - anomaly-detection
  - self-supervised-learning
  - adversarial-training
  - deep-learning
  - research
description: This paper combines self-supervised learning and adversarial training to improve deep anomaly detection, leveraging unlabeled normal data to learn representations that are robust to perturbations and more sensitive to out-of-distribution inputs. It matters because labeled anomaly data is rare in practice, making self-supervised approaches essential for real-world deployment.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Deep anomaly detection with self-supervised learning and adversarial training.pdf
---

## Summary

This paper addresses a fundamental problem in anomaly detection: labeled examples of anomalies are scarce or nonexistent in real-world settings, making purely supervised approaches impractical. The work combines self-supervised learning — which extracts useful representations from unlabeled normal data — with adversarial training to build deep anomaly detectors that are both more sensitive to out-of-distribution inputs and more robust to perturbations that might mask anomalies.

The self-supervised component trains a deep neural network on pretext tasks derived from normal data only — for example, predicting rotations, solving jigsaw puzzles, or contrastive instance discrimination. These tasks force the network to learn rich representations of what "normal" looks like without requiring anomaly labels. The adversarial training component then hardens these representations: by exposing the model to adversarially perturbed inputs during training, the decision boundary between normal and anomalous regions becomes sharper and less susceptible to exploitation.

The combination addresses a known weakness of self-supervised anomaly detectors: their representations can be fragile, and adversarial perturbations can push anomalous inputs into the "normal" region of feature space. This is directly analogous to the adversarial machine learning challenge documented in security domains, where gradient masking and evasion attacks have repeatedly broken deployed classifiers. By incorporating adversarial training into the anomaly detection pipeline, the method achieves more reliable detection especially against worst-case inputs — connecting to the broader robustness literature typified by work from Nicholas Carlini on evaluating adversarial defenses.

## Key points

- Self-supervised learning on normal data only eliminates the need for labeled anomalies — critical for real-world deployment where anomalies are rare or undefined
- Adversarial training sharpens the normal/anomalous decision boundary and prevents adversarial evasion of the detector
- Pretext tasks (rotation prediction, contrastive learning) provide the supervision signal for learning normal-data representations
- The adversarial component addresses a key failure mode: perturbation-based evasion of anomaly detectors, which mirrors gradient masking exploits in adversarial robustness research
- Practical relevance spans cybersecurity (intrusion detection), manufacturing (defect detection), and medical imaging (disease screening)

[Original PDF](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Deep anomaly detection with self-supervised learning and adversarial training.pdf)
