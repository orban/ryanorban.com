---
title: "Twitter Slams the Door on Tweetro: User Token Limits"
date: 2012-11-17
categories:
  - twitter
  - api
  - platform-risk
  - third-party-clients
  - windows-apps
description: "The Tweetro incident: Twitter denied an exemption from its new 100k user token cap to a popular Windows Twitter client, effectively killing it. A concrete example of the developer ecosystem damage from Twitter's 2012 API restrictions."
params:
  source: pinboard
  sourceUrl: http://www.windowsobserver.com/2012/11/16/breaking-twitter-completely-slams-the-door-on-tweetro-refuses-to-offer-exemption-to-user-token-limits/
---

## Summary

Tweetro was a popular third-party Twitter client for Windows — one of the better-designed apps in an ecosystem where Twitter's own Windows client was mediocre. When Twitter introduced user token limits in August 2012 (capping third-party clients at 100,000 active user tokens), Tweetro hit the ceiling and requested an exemption. Twitter refused.

This was a concrete incident in the broader developer ecosystem crisis. The 100k token cap was announced with the new Twitter API v1.1 guidelines in June 2012 — framed as protecting the quality of the Twitter experience, but functionally designed to prevent any third-party client from reaching scale. Apps already over 100k could continue but couldn't grow. Apps under 100k could grow only to that ceiling.

Tweetro's developers were in an impossible position: they had built a high-quality product, accumulated tens of thousands of users, and then hit an externally imposed ceiling with no path forward. The refusal to grant an exemption removed any remaining ambiguity about Twitter's intentions — existing ecosystem players were being wound down. This accelerated the exodus of iOS and Android client developers too: Twitterrific, Tweetbot, and others saw their ceiling and began pivoting accordingly.

## Key points

- Twitter API v1.1 (June 2012): 100,000 user token cap per third-party app — no growth beyond that ceiling
- Tweetro hit the cap, requested exemption, was denied — the clearest single data point of Twitter's intent
- The cap affected only third-party clients; Twitter's own apps were exempt — explicitly competitive
- Platform risk lesson: any developer ecosystem can be closed once the platform reaches critical mass
- Led to collapse of the third-party client ecosystem; Tweetbot, Twitterrific later shut down in 2023 when Twitter cut API access entirely

[Original](http://www.windowsobserver.com/2012/11/16/breaking-twitter-completely-slams-the-door-on-tweetro-refuses-to-offer-exemption-to-user-token-limits/)
