---
title: "ayb: Multi-Tenant Database for Data Ownership"
date: 2023-06-26
categories:
  - database
  - multi-tenancy
  - data-ownership
  - sqlite
  - open-source
description: ayb is a multi-tenant database server built on SQLite that lets individuals own and control their own data — each user gets their own database instance. A philosophical statement about data ownership as much as a technical product.
params:
  source: pinboard
  sourceUrl: https://blog.marcua.net/2023/06/25/ayb-a-multi-tenant-database-that-helps-you-own-your-data.html
---

![ayb: Multi-Tenant Database for Data Ownership](/images/notes/ayb-multitenant-database.png)

## Summary

ayb is a multi-tenant database server by Adam Marcus that takes an unusual philosophical stance: rather than centralizing all user data in one database that an application controls, each user gets their own isolated SQLite database that they can query, export, and take with them. The tagline helps you own your data is the core design goal.

The technical approach: ayb acts as a server that manages many individual SQLite database files — one per user or entity. Clients connect, authenticate, and send SQL queries that execute against their specific database file. The server handles multi-tenancy (authentication, routing to the right database file) while keeping data isolation absolute — your database is your database, not a row in someone else's table.

The philosophical argument is that most web applications give users no meaningful data portability. Your data lives in the app's database in a schema you don't control. ayb's model is closer to how filesystems work — your data is a file you can copy, query externally, and take elsewhere. This connects to the local-first software movement (Ink & Switch's work), Solid (Tim Berners-Lee's data pods proposal), and the broader conversation about user data sovereignty. The SQLite choice is significant — it's a single file format that's extremely portable and independently queryable without ayb.

## Key points

- Each user gets their own isolated SQLite database file — absolute data isolation by design.
- SQL queries route to the correct per-user database — multi-tenancy at the file level, not row level.
- Data portability: the SQLite file is a standard format you can query with any SQLite tool.
- Philosophical stance: data ownership vs data custody — users own their database, apps are granted access.
- From Adam Marcus (marcua) — researcher and engineer with database and data systems background.
- Connects to local-first software, Solid (data pods), and user data sovereignty movements.

[Original](https://blog.marcua.net/2023/06/25/ayb-a-multi-tenant-database-that-helps-you-own-your-data.html)
