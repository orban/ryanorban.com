---
title: Security Data Science Papers
date: 2014-07-29
categories:
  - security
  - machine-learning
  - data-science
  - research
  - papers
description: Covert.io's curated list of academic papers applying data science and machine learning to security problems — covering network intrusion detection, malware classification, anomaly detection, and more. A reference for practitioners working at the intersection of ML and cybersecurity.
params:
  source: pinboard
  sourceUrl: http://www.covert.io/security-datascience-papers/
---

![Security Data Science Papers](/images/notes/security-data-science-papers.png)

## Summary

covert.io maintains a curated reading list of academic papers applying machine learning and data science to security problems. This compilation addresses a genuine gap: security practitioners who want to use ML need research-grounded baselines, and ML practitioners moving into security need to understand what problems have been studied and how.

The security+ML problem space in 2014 spanned: **network intrusion detection** (classifying traffic as normal vs. anomalous using features like packet size, timing, protocol), **malware classification** (static analysis — byte histograms, n-grams of opcodes; dynamic analysis — system call sequences), **phishing detection** (URL features, page structure, domain registration), **spam filtering** (NLP on email content, sender reputation), and **anomaly detection** for insider threats.

The common theme across security ML applications: adversarial dynamics. A standard machine learning model trained on historical malware may be evaded by an adversary who knows the feature space. This adversarial setting (where the data distribution shifts because the opponent adapts) makes security ML harder than most application domains and motivates work on adversarial machine learning and robust classification.

## Key points

- Security ML domains: network intrusion detection, malware classification, phishing, spam, insider threat detection.
- Features for malware classification: static (byte histograms, opcode n-grams) + dynamic (system call sequences, API calls).
- Key challenge: adversarial dynamics — attackers adapt to evade known detection features, causing distribution shift.
- Anomaly detection vs. supervised classification: anomaly detection handles unknown attacks but has high false positive rates.
- Adversarial machine learning: the formal study of attacks on ML models — FGSM, PGD, evasion attacks, poisoning attacks.
- covert.io curated this as practitioner resource — the security/ML crossover field was small enough in 2014 to fit on one page.

[Original](http://www.covert.io/security-datascience-papers/)
