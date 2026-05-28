---
title: Tweetping — Real-Time Twitter Visualization
date: 2013-02-01
categories:
  - twitter
  - data-visualization
  - streaming
  - real-time
  - creative-coding
description: Tweetping visualized the Twitter streaming API as a real-time pulsing global map — each tweet a dot appearing at its geolocation. A landmark example of combining streaming data APIs with real-time browser visualization.
params:
  source: pinboard
  sourceUrl: http://tweetping.net/
---

![Tweetping — Real-Time Twitter Visualization](/images/notes/tweetping.png)

## Summary

[Tweetping](/notes/tweetping/) was a real-time visualization of the Twitter Streaming API that rendered each geotagged tweet as a pulsing dot on a global map — creating a hypnotic live view of Twitter's geographic activity. The content field shows it was shared with tags to @gstatton and @chrismatthieu as "Amazing use of the Twitter streaming API, backbone.js, and processing.js."

The technical stack: Twitter Streaming API for live tweet data (Twitter provided a 1% sample stream freely in 2013 — the Spritzer), Backbone.js for application state management, and Processing.js (or similar) for the animated dot rendering. The result was a globe with constantly-appearing dots concentrated in US/Europe/Asia during their respective daytime hours, with a visible wave following the planet's rotation.

This type of visualization was influential in 2013 for several reasons: it made abstract API data physically immediate and beautiful, it demonstrated that browser-side real-time processing of streaming data was viable, and it raised questions about what you could see in data that couldn't be seen otherwise. The global Twitter activity map showed geography of internet use, time zone boundaries in posting behavior, and event spikes.

## Key points

- Twitter Streaming API (2013): the 1% "Spritzer" stream was freely accessible and sufficient for real-time visualizations — later restricted significantly as Twitter's API policies tightened
- Backbone.js was the dominant client-side JavaScript framework in 2013 before React displaced it — used here for application structure and state
- Processing.js ported Processing (the creative coding environment) to the browser — enabling canvas-based animation without writing raw WebGL
- Geolocation on tweets was optional and only a small percentage of tweets included it — the visualization sampled the geotagged subset
- [Tweetping](/notes/tweetping/) belongs to a genre of live data is beautiful experiments that defined a period of real-time data visualization — Wind Map, RadarScope, and similar projects from the same era

[Original](http://tweetping.net/)
