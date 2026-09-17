---
title: Powering Search and Recommendations at DoorDash
date: 2021-02-28
categories:
  - machine-learning
  - search
  - recommendations
  - systems
  - engineering
description: DoorDash's engineering blog post on their search and recommendation systems — covering how they rank restaurants and dishes, handle cold-start problems, and personalize results. A practical look at production recommendation systems at a major food delivery platform.
params:
  source: pinboard
  sourceUrl: https://medium.com/@DoorDash/powering-search-recommendations-at-doordash-8310c5cfd88c
---

![Powering Search and Recommendations at DoorDash](/images/notes/doordash-search-recommendations.png)

## Summary

DoorDash's engineering team describes their approach to search and recommendations for restaurant and menu discovery. The problem is harder than typical e-commerce recommendations: queries are highly local (restaurants near you), inventory changes by time of day (a restaurant only available for lunch), and success is measured in completed orders rather than just clicks.

The system covers several components: query understanding (mapping pizza to a set of relevant restaurants and dishes), ranking (scoring candidates using learning-to-rank models with features like distance, delivery time, historical order rate, and personalization signals), and recommendation surfaces (the for you carousels on the home screen that surface restaurants and dishes before a user types anything). Collaborative filtering appears in the recommendation signals, adapted for the local inventory constraint.

The cold-start problem is particularly sharp at DoorDash: new restaurants and new users have no order history. The solution involves feature engineering from non-behavioral signals — restaurant cuisine type, menu item characteristics, demographics of the area — to bootstrap initial rankings before behavioral data accumulates. The post gives a useful real-world example of the gap between academic recommendation systems and production deployment constraints.

## Key points

- Search ranking uses learning-to-rank with features: distance, delivery time, order history, personalization.
- Local inventory constraint: results must be available near the user *right now* — harder than general e-commerce.
- Cold-start problem: new restaurants use menu/cuisine features to bootstrap before behavioral data exists.
- Collaborative filtering adapted to local geography — you can't recommend a restaurant 30 miles away.
- Recommendation surfaces (home screen carousels) require balancing exploration (new restaurants) vs. exploitation (favorites).

[Original](https://medium.com/@DoorDash/powering-search-recommendations-at-doordash-8310c5cfd88c)
