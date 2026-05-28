---
title: Deploying Flask with uWSGI and nginx on Ubuntu
date: 2012-05-07
categories:
  - flask
  - nginx
  - python
  - web-servers
  - deployment
  - devops
description: A 2012 tutorial on deploying Flask applications behind nginx using uWSGI as the application server on Ubuntu. The canonical stack for Python web apps before Docker and cloud deployment made it simpler — and still the right choice for self-hosted production Flask.
params:
  source: pinboard
  sourceUrl: http://kramerapps.com/blog/post/22551999777/flask-uwsgi-nginx-ubuntu
---

## Summary

This tutorial covered the standard production deployment stack for Flask applications in 2012: nginx as a reverse proxy and static file server, uWSGI as the WSGI application server that runs the Python code, and Ubuntu as the OS. The Flask → uWSGI → nginx stack remained the dominant pattern for self-hosted Python web apps for most of the decade.

The architecture has a clean logic. Flask (and other WSGI-compliant Python frameworks like Django) expose a Python callable as their interface. You need a process that can speak HTTP, manage multiple concurrent requests, and call that Python callable — that's uWSGI. You also need a fast server for static files, TLS termination, rate limiting, and passing requests to uWSGI — that's nginx. Putting them together: nginx handles everything it can directly, passes dynamic requests to uWSGI via a Unix socket or TCP connection, and uWSGI manages a pool of Python worker processes.

Compared to alternatives at the time: mod_wsgi for Apache worked but Apache was heavier and more complex to configure. Gunicorn was simpler to set up than uWSGI but had less configuration flexibility. Heroku made this whole setup unnecessary for small apps, but for anything requiring custom server config or running on your own hardware, the uWSGI/nginx combination was the answer. By 2016-2018, Docker and cloud platforms largely displaced this pattern for new projects, but understanding it is still useful for legacy systems and self-hosted deployments.

## Key points

- Flask is a WSGI app — it doesn't speak HTTP directly and can't handle concurrency by itself.
- uWSGI: manages Python worker processes, speaks WSGI to Flask and uwsgi protocol to nginx.
- nginx: reverse proxy, static files, TLS termination, rate limiting — passes dynamic requests to uWSGI.
- Communication via Unix socket (faster, same machine) vs. TCP (cross-machine or container-to-container).
- Gunicorn is simpler alternative to uWSGI; mod_wsgi for Apache is the third option.

[Original](http://kramerapps.com/blog/post/22551999777/flask-uwsgi-nginx-ubuntu)
