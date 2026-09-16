---
title: Hasura GraphQL Streaming Subscriptions
date: 2022-10-17
categories:
  - graphql
  - realtime
  - databases
  - hasura
  - subscriptions
description: Hasura's architecture doc for streaming subscriptions — a way to stream ordered data from a database cursor in real time over GraphQL. Solves the problem of efficiently delivering large, incrementally-changing result sets without polling.
params:
  source: pinboard
  sourceUrl: https://github.com/hasura/graphql-engine/blob/master/architecture/streaming-subscriptions.md
---

## Summary

Hasura's streaming subscriptions architecture document describes an approach to streaming ordered data from a PostgreSQL (or compatible) database over GraphQL subscriptions. Regular GraphQL subscriptions (live queries) re-execute the full query on each change and send the entire updated result set — expensive for large tables. Streaming subscriptions instead use a database cursor, sending only the rows that are new since the last delivery.

The cursor-based approach is critical for use cases involving append-only data: event logs, chat messages, activity feeds, IoT sensor readings. With a regular live query subscription, if you have 10,000 messages, every new message triggers a re-fetch of all 10,000. With a streaming subscription, you get only the new message. This is real-time data delivery that scales.

Hasura generates the GraphQL API automatically from your database schema, including subscriptions — this doc explains the internals of how the streaming variant works and how the cursor is managed. It connects to Hasura's broader architecture of providing instant GraphQL APIs with fine-grained access control without writing resolver code.

## Key points

- Streaming subscriptions use a database cursor to deliver only new rows, not the full result set.
- Designed for append-only data: event logs, feeds, chat — anything with an ordered sequence.
- Solves the scalability problem of regular live-query subscriptions re-fetching everything on change.
- Hasura auto-generates the GraphQL API from the database schema, including streaming subscriptions.
- cursor argument lets clients reconnect and resume from where they left off.
- Works with PostgreSQL, MS SQL, CockroachDB backends in Hasura.

[Original](https://github.com/hasura/graphql-engine/blob/master/architecture/streaming-subscriptions.md) → GitHub
