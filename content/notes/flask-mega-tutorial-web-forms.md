---
title: "The Flask Mega-Tutorial, Part III: Web Forms"
date: 2014-04-22
categories:
  - python
  - flask
  - web-development
  - tutorials
description: Part III of Miguel Grinberg's Flask Mega-Tutorial — covers web forms using Flask-WTF and WTForms. The Mega-Tutorial was the canonical resource for learning Flask web development in 2014, and this forms chapter is where most projects got real.
params:
  source: pinboard
  sourceUrl: http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
---

## Summary

Miguel Grinberg's Flask Mega-Tutorial was the go-to reference for learning Flask web development in the early 2010s. Part III covers web forms using Flask-WTF (a Flask extension wrapping WTForms), which handles form rendering, validation, and CSRF protection. This is the point in the tutorial series where a Flask project goes from returning static strings to handling user input — a meaningful threshold.

Flask itself is a micro-framework: it provides routing and request handling but intentionally leaves everything else to extensions. This design philosophy (sometimes called batteries not included) is the opposite of Django's opinionated approach, and the Mega-Tutorial reflects this by teaching the extension ecosystem alongside the core framework. Flask-WTF integrates WTForms' form classes with Flask's application context, making form validation declarative.

In the data science world of 2014, Flask was the dominant choice for building lightweight dashboards and model-serving APIs. Zipfian Academy students learned Flask for exactly this purpose — wrapping machine learning models in a web interface that could be demoed.

## Key points

- Flask-WTF provides form classes, validation, and CSRF protection on top of WTForms.
- Form fields are defined as class attributes with validators — declarative rather than imperative.
- Flask's micro-framework design means forms, auth, and databases all come from extensions, not core.
- The Mega-Tutorial was the canonical Flask resource before the official docs matured.
- In data science practice: Flask was the standard way to wrap ML models in a demo web app.

[Original](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
