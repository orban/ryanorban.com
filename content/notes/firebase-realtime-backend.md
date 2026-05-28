---
title: "Firebase: Real-Time Backend as a Service"
date: 2012-04-12
categories:
  - backend
  - real-time
  - database
  - baas
  - javascript
description: Firebase (founded 2011, acquired by Google in 2014) was a real-time backend-as-a-service that synced data across clients via WebSockets — eliminating the need to write server-side code for data storage and live updates. It became the template for the 'serverless' and BaaS movement.
params:
  source: pinboard
  sourceUrl: http://www.firebase.com/
---

![Firebase: Real-Time Backend as a Service](/images/notes/firebase-realtime-backend.png)

## Summary

Firebase launched in 2011 as a backend-as-a-service (BaaS) aimed at eliminating the server-side boilerplate developers wrote just to persist and sync data. Its core insight was simple: most apps need the same basic backend operations — store data, authenticate users, push updates to connected clients — and none of that logic needed to be custom-built. Firebase provided a hosted real-time database with a WebSocket API that pushed changes to all subscribed clients instantly.

The appeal for JavaScript developers was immediate. Instead of writing an Express or Rails backend to handle CRUD operations, you could write purely client-side code and let Firebase handle persistence and sync. This was a genuine paradigm shift for small apps and prototypes, and it popularized what's now called the serverless model.

Google acquired Firebase in 2014 and expanded it substantially — adding authentication, cloud functions, hosting, crash reporting, and analytics to create what became Google's primary platform for mobile and web app development. The original real-time database eventually got a successor (Firestore) with better querying and offline support.

## Key points

- Hosted real-time database with WebSocket sync — data changes propagate to all clients without polling.
- Backend-as-a-service model: no server code needed for basic data persistence and auth.
- Pioneered serverless patterns that are now standard across the industry.
- Acquired by Google in 2014 and expanded into a full app development platform.
- The JavaScript SDK made it the go-to backend for frontend-only developers building real apps.
- Influenced a generation of BaaS competitors: Parse (2012, acquired by Facebook), Supabase, Appwrite.

[Original](http://www.firebase.com/)
