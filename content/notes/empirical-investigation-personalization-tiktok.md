---
title: An Empirical Investigation of Personalization Factors on TikTok
date: 2022-02-14
categories:
  - tiktok
  - recommendation-systems
  - algorithmic-amplification
  - filter-bubble
  - social-media
  - audit
description: First empirical audit of TikTok's recommendation algorithm using sock-puppet methodology, testing how language, location, follows, likes, and watch duration shape content recommendations. Follow-behavior is the dominant personalization signal, and all tested factors contribute to filter bubble formation.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2201.12271.pdf
---

## Summary

Boeker and Urman (Web Conference 2022) run the first systematic empirical audit of TikTok's recommendation algorithm, using sock-puppet accounts—automated profiles designed to isolate individual behavioral signals. Despite TikTok's 1 billion+ monthly users and significant concern about its content effects, the platform's recommendation mechanics had received almost no rigorous empirical scrutiny prior to this work.

The study tests five personalization factors: language, location, follows, likes, and video watch duration. All five influence recommendations, but the effect sizes differ sharply. Follow-behavior dominates—who you follow reshapes your feed more than any other signal. Likes and watch duration are second-tier but still meaningful. This has direct implications for filter bubble research: the strongest lever for algorithmic amplification is also the one that reflects the most deliberate user intent, complicating easy narratives about passive algorithmic capture.

The sock-puppet methodology they develop is worth noting in its own right—it's a reusable audit framework applicable to other social media platforms where behavioral signals need to be isolated from each other experimentally.

## Key points

- First empirical audit of TikTok's personalization algorithm; previously a significant research gap despite platform scale
- Follow-behavior is the strongest personalization signal, followed by likes then watch duration
- All five tested factors (language, location, follows, likes, view duration) influence recommendations
- Results raise questions about filter bubble formation and algorithmic amplification of problematic content
- The sock-puppet audit methodology is generalizable to other social media recommendation systems

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2201.12271.pdf)
