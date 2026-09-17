---
title: Django Sessions
date: 2024-02-26
categories:
  - django
  - sessions
  - authentication
  - backend
  - python
description: An article on Django sessions — how the session framework works, the available backends (database, cache, file, cookie), and how session data flows through requests. Django's session system is the foundation for authentication and stateful web behavior.
params:
  source: pinboard
  sourceUrl: https://awstip.com/django-sessions-70a40aaeaa28
---

![Django Sessions](/images/notes/django-sessions.png)

## Summary

Django sessions provide stateful behavior across the fundamentally stateless HTTP protocol — they let the server identify returning users and maintain per-user state between requests. A session cookie (containing only a session key, not the data) is sent to the client; the actual session data lives server-side in whichever backend is configured. This server-side storage is what distinguishes [Django sessions](/notes/django-sessions/) from simple cookie-based storage.

Django ships with four session backends. The **database backend** stores sessions in a `django_session` table — persistent across server restarts but requires database queries per request. The **cache backend** uses Django's cache framework (typically Redis or Memcached) — fast but sessions may be lost on cache flush. The **file backend** stores sessions as files on disk. The **cookie backend** stores all data client-side using signed cookies — no server-side storage but limited by cookie size and exposes data to clients.

Session data is a Python dictionary accessible via `request.session`. Django's session framework integrates with its authentication system — logging in sets `_auth_user_id` and related keys in the session. Sessions have configurable expiry (`SESSION_COOKIE_AGE`) and the `SESSION_EXPIRE_AT_BROWSER_CLOSE` setting controls behavior on browser close.

## Key points

- Session key in cookie; actual data stored server-side in the configured backend.
- Four backends: database (default), cache (Redis/Memcached), file, and signed cookie.
- `request.session` is a dictionary — set, get, and delete keys like any dict.
- Django authentication stores user identity in the session automatically on login.
- `SESSION_COOKIE_AGE` controls expiry; `SESSION_EXPIRE_AT_BROWSER_CLOSE` controls browser-close behavior.
- Cache backend is fastest but may lose sessions on flush — database backend is more durable.

[Original](https://awstip.com/django-sessions-70a40aaeaa28)
